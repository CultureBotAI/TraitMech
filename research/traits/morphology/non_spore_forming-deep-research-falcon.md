---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:43:48.965047'
end_time: '2026-06-18T08:51:12.403507'
duration_seconds: 443.44
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: non-spore forming
  trait_identifier: METPO:1000872
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: non_spore_forming
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A sporulation in which an organism lacks the ability to produce endospores.
  parent_traits: METPO:1000870
  synonyms: no, no_spore
  evidence_summary: 'DOI:10.1155/2013/898106: S. aureus does not form spores (Organism
    example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297:
    activation of these sigma factors to landmark events in morphogenesis (Sporulation
    regulatory review supports the Spo0A/sigma cascade as the sporulation control
    program whose absence yields a non-spore-forming phenotype.)'
  causal_graph_summary: 'non_spore_forming_absent_spo0a_cascade: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non-spore forming
- **METPO identifier:** METPO:1000872
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism lacks the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** no, no_spore
- **Existing evidence:** DOI:10.1155/2013/898106: S. aureus does not form spores (Organism example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297: activation of these sigma factors to landmark events in morphogenesis (Sporulation regulatory review supports the Spo0A/sigma cascade as the sporulation control program whose absence yields a non-spore-forming phenotype.)
- **Existing causal graph summary:** non_spore_forming_absent_spo0a_cascade: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **non-spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_spore_forming.yaml`.

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
- **Trait label:** non-spore forming
- **METPO identifier:** METPO:1000872
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism lacks the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** no, no_spore
- **Existing evidence:** DOI:10.1155/2013/898106: S. aureus does not form spores (Organism example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297: activation of these sigma factors to landmark events in morphogenesis (Sporulation regulatory review supports the Spo0A/sigma cascade as the sporulation control program whose absence yields a non-spore-forming phenotype.)
- **Existing causal graph summary:** non_spore_forming_absent_spo0a_cascade: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **non-spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_spore_forming.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **non-spore forming** (METPO:1000872)

### 0) Scope summary (what this trait *is*)
**Trait label:** non-spore forming (METPO:1000872) refers to the **lack of ability to produce bacterial endospores** (i.e., an organism is *asporogenic* in the endosporulation sense). Mechanistically, the trait typically reflects either (i) **absence** of essential sporulation regulators (especially **Spo0A**) or (ii) **loss/inactivation** of a substantial fraction of the conserved sporulation machinery, such that endospore morphogenesis and maturation cannot proceed. Comparative genomics supports using **spo0A absence** as a strong indicator of inability to sporulate, while also highlighting boundary cases where some “nonsporeformers” retain spo0A and fragments of sporulation genes but still lack full sporulation capacity. (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 13-15)

### Boundary cases (what can be misclassified)
*Kurthia* spp. illustrate an important boundary: historically described as “non-spore-forming/asporogenic,” yet microscopy revealed **spore-like structures** (“cryptosporulation”) with endosporulation-like morphological hallmarks, but **without canonical heat/UV resistance** and with instability across subculturing. This warns against curating “non-spore forming” solely from old phenotype descriptions without standardized assays or genomic corroboration. (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2)

**Assay/readout implications for curation:** many historical “non-spore-forming” calls were based on **wet-heat resistance** or lack of phase-bright spores; however, cryptic or incomplete sporulation states can produce spore-like morphologies without full resistance phenotypes. (fatton2022cryptosporulationinkurthia pages 2-2, fatton2022cryptosporulationinkurthia pages 13-13)

---

## 1) Key concepts and current mechanistic understanding

### 1.1 Master regulator logic: Spo0A as a gatekeeper
A core organizing concept for endosporulation is that **Spo0A is the master regulator**, and its activation state (Spo0A~P) gates entry into sporulation. Reviews and primary studies emphasize that sufficient Spo0A~P is required to initiate sporulation. (beskrovnaya2021structuralmetabolicand pages 2-3, bidnenko2024complexsporulationspecificexpression pages 2-3)

A major genomics-based definition relevant to the “non-spore forming” trait is:
- **Spo0A absence** is an “excellent predictor of the organism’s inability to sporulate” across Firmicutes (Bacillota). (galperin2022conservationandevolution pages 4-5)

### 1.2 Initiation signaling: Bacillus phosphorelay vs clostridial kinases
In Bacilli, Spo0A activation is classically mediated by a **phosphorelay** (KinA/KinB → Spo0F → Spo0B → Spo0A). Disruptions in this relay would be expected to arrest sporulation initiation. (beskrovnaya2021structuralmetabolicand pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18)

In (some) Clostridia, Spo0A activation can be mediated by **orphan histidine kinases** that directly phosphorylate Spo0A, creating additional taxon-specific edges relevant to “non-spore forming” outcomes. (humphreys2023clostridiumbeijerinckiistrain pages 1-2, gohari2023identificationoforphan pages 23-24)

### 1.3 Execution program: compartment-specific sigma cascade
Sporulation involves a **cascade of sporulation sigma factors** (notably SigH upstream and SigF/SigE/SigG/SigK in compartmentalized programs) that drive temporally ordered gene expression for morphogenesis and maturation; disruption at this level can prevent completion of spore formation. (bidnenko2024complexsporulationspecificexpression pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18)

### 1.4 Gene-loss framing and “sporulation gene set”
A comparative genomics view supports that many non-spore-forming Firmicutes reflect **lineage-specific loss of a conserved core sporulation gene set**. Ancestral-state reconstruction inferred core sporulation genes at the Firmicutes root, with extensive losses in non-spore-forming clades. (galperin2022conservationandevolution pages 13-15)

---

## 2) Recent developments and latest research (prioritized 2023–2024)

### 2.1 2024: Quorum-sensing signal AI-2 inhibits sporulation via RapC–ComA
Xiong et al. (2024) describe a mechanistically explicit anti-sporulation route in *Bacillus velezensis*: **AI-2 binds RapC**, stimulates **RapC–ComA interaction**, produces **inactive ComA**, and **inhibits sporulation**. This provides curatable nodes/edges linking an extracellular chemical signal to sporulation inhibition through a known regulatory node family (Rap). (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2)

### 2.2 2024: Transcription termination factor Rho modulates Spo0A activation and sporulation
Bidnenko et al. (2024) provide evidence that maintaining high rho expression **“prevents the activation of Spo0A”** and **blocks spore formation**, while also reporting quantitative reporter timing changes consistent with altered Spo0A program dynamics. This supplies a noncanonical regulatory branch that can yield a non-sporulating state without deleting core sporulation genes. (bidnenko2024complexsporulationspecificexpression pages 2-3)

### 2.3 2023: spo0A activity loss drives emergence of degenerate non-sporulating variants
Humphreys et al. (2023) investigated strain degeneration in *Clostridium beijerinckii* and reported degeneration “driven by the loss of spo0A activity,” with **71 degenerate variants** showing mutation hotspots including spo0A and spo0A-network genes. This supports a concrete genotype→phenotype path where spo0A mutation yields a non-sporulating phenotype in an otherwise spore-forming organism. (humphreys2023clostridiumbeijerinckiistrain pages 1-2)

### 2.4 2023: Transcriptomic timing supports the Spo0A phosphorelay and sigma cascade as essential control architecture
Jun et al. (2023) describe Spo0A as “the master regulator” essential for transition into sporulation and outline the initiation phosphorelay (KinA/KinB→Spo0F→Spo0B→Spo0A) that “signals the start of sporulation,” along with involvement of Rap-family phosphatases and sigma-factor ordering. While not a knockout study per se, it is a citable mechanistic source consistent with curating pathway-structure edges. (jun2023timecoursetranscriptomeanalysis pages 17-18)

---

## 3) Current applications and real-world implementations (with relevance to “non-spore forming”)

### 3.1 Industrial strain stability: avoiding loss of sporulation competence
In solventogenic clostridia, degeneration during subculturing is a practical industrial problem; the *C. beijerinckii* study links this to spo0A-network mutation accumulation and eventual dominance of spo0A mutants, i.e., an emergent “non-sporulating” state in production cultures. This provides a real-world context for why a “non-spore forming” phenotype can arise in spore-formers via selection and mutation. (humphreys2023clostridiumbeijerinckiistrain pages 1-2)

### 3.2 Microbiome/ecology inference from genomes: predicting sporulation potential vs non-spore forming
Comparative genomics frameworks explicitly use gene presence/absence (notably spo0A and additional core sporulation genes) to infer sporulation potential and, conversely, non-spore-forming states. The 180-genome Firmicute survey provides one evidence base for curatable “gene absence predicts trait absence” edges used in genome-informed microbial ecology and annotation. (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 13-15)

---

## 4) Expert opinions and authoritative analyses (what experts emphasize)

### 4.1 Spo0A absence is a strong indicator; Spo0A presence is not sufficient
The large Firmicute comparative-genomics study emphasizes an asymmetry crucial for curation:
- Absence of Spo0A is an “excellent predictor” of inability to sporulate.
- Yet spo0A is present in many genomes described as nonsporeformers (40/118 spo0A+ in a 180-genome set), indicating retained remnants or partial programs; therefore, “spo0A present ⇒ spore-forming” is not a valid rule. (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 15-17)

### 4.2 Sporulation loss is often stepwise and lineage-specific
Ancestral reconstruction and comparative patterns support that many non-spore-forming lineages derive from **vertical inheritance followed by gene loss**, rather than recurrent reacquisition, reinforcing gene-loss edges as central to a causal graph for the trait. (galperin2022conservationandevolution pages 13-15)

---

## 5) Candidate nodes for TraitMech curation (grouped)
The following node inventory is designed to seed `data/traits/morphology/non_spore_forming.yaml`.

| Node label | Node type | Brief role in sporulation/non-sporulation | Suggested ontology grounding |
|---|---|---|---|
| non-spore forming | process | Trait state denoting lack of ability to produce endospores; often inferred from absence/inactivation of core sporulation machinery or failure in phenotypic assays | METPO:1000872 |
| endospore formation | process | Developmental program producing dormant, resistant endospores; its failure or absence underlies the non-spore-forming trait (beskrovnaya2021structuralmetabolicand pages 2-3, galperin2022conservationandevolution pages 2-4) | GO:0043934 |
| spore morphogenesis | process | Morphological progression of sporulation controlled by compartment-specific sigma factors; disruption blocks mature spore formation (bidnenko2024complexsporulationspecificexpression pages 2-3) | label-only candidate |
| sporulation initiation phosphorelay | pathway | Bacillus signaling pathway KinA/KinB → Spo0F → Spo0B → Spo0A that activates entry into sporulation; disruption prevents sporulation initiation (beskrovnaya2021structuralmetabolicand pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| core sporulation gene set / sporulation gene signature | pathway | Conserved set of sporulation-associated genes used as genomic markers; lineage-specific loss correlates with non-spore-forming clades (galperin2022conservationandevolution pages 2-4, galperin2022conservationandevolution pages 13-15) | label-only candidate |
| gene loss of sporulation machinery | process | Evolutionary or strain-level loss/inactivation of many sporulation genes causes asporogenic phenotype and explains many non-spore-forming lineages (fatton2022cryptosporulationinkurthia pages 2-2, galperin2022conservationandevolution pages 13-15) | GO:0006281 (too broad, prefer label-only) |
| Spo0A | gene/protein | Master regulator of sporulation; absence is an excellent predictor of inability to sporulate, but presence alone is insufficient (galperin2022conservationandevolution pages 4-5, beskrovnaya2021structuralmetabolicand pages 2-3) | label-only candidate |
| Spo0A~P (phosphorylated Spo0A) | protein | Activated form required to trigger sporulation; insufficient Spo0A phosphorylation prevents entry into sporulation (beskrovnaya2021structuralmetabolicand pages 2-3, bidnenko2024complexsporulationspecificexpression pages 2-3) | label-only candidate |
| Spo0F | gene/protein | Intermediate response regulator in Bacillus phosphorelay; Rap phosphatases dephosphorylate it to reduce phosphate flow to Spo0A (xiong2024autoinducer2relievessoil pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| Spo0B | gene/protein | Phosphotransferase relaying phosphate from Spo0F to Spo0A in Bacillus phosphorelay (beskrovnaya2021structuralmetabolicand pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| KinA | gene/protein | Histidine kinase that initiates Bacillus phosphorelay upstream of Spo0F/Spo0B/Spo0A (jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| KinB | gene/protein | Histidine kinase that contributes to Spo0A activation; increased KinB expression can accelerate Spo0A~P accumulation (bidnenko2024complexsporulationspecificexpression pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| orphan histidine kinases (general) | gene/protein | In some clostridia, directly activate Spo0A rather than a Bacillus-like phosphorelay; perturbation can reduce sporulation (humphreys2023clostridiumbeijerinckiistrain pages 1-2, gohari2023identificationoforphan pages 23-24) | label-only candidate |
| CPR1953 | gene/protein | C. perfringens orphan histidine kinase required for normal Spo0A levels and sporulation; inactivation virtually eliminated sporulation (gohari2023identificationoforphan pages 23-24) | label-only candidate |
| CPR1954 | gene/protein | C. perfringens orphan histidine kinase whose inactivation lowers Spo0A and strongly reduces sporulation (gohari2023identificationoforphan pages 23-24) | label-only candidate |
| Rap phosphatases | gene/protein | Negative regulators of sporulation in Bacillus; dephosphorylate Spo0F and reduce phosphate flow to Spo0A (xiong2024autoinducer2relievessoil pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| RapC | gene/protein | Rap phosphatase-family regulator that, when stimulated by AI-2, binds ComA and inhibits sporulation in B. velezensis (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | label-only candidate |
| Phr peptides | chemical | Peptide regulators that modulate Rap activity in RRNPP signaling, thereby indirectly affecting sporulation control (xiong2024autoinducer2relievessoil pages 1-2) | label-only candidate |
| ComA | gene/protein | DNA-binding regulator whose inactivation via RapC interaction inhibits sporulation in B. velezensis (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | label-only candidate |
| Rho | gene/protein | Transcription termination factor; sustained expression prevents Spo0A activation and blocks spore formation, while inactivation stimulates sporulation (bidnenko2024complexsporulationspecificexpression pages 2-3) | label-only candidate |
| SigH | gene/protein | Early alternative sigma factor linked to sporulation initiation; low pH can reduce its activity, and it participates upstream of the sporulation cascade (bosnar2023attemptstolimit pages 6-8, bidnenko2024complexsporulationspecificexpression pages 2-3) | label-only candidate |
| SigF | gene/protein | Forespore-specific sigma factor in sporulation cascade required for temporally ordered morphogenesis (bidnenko2024complexsporulationspecificexpression pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| SigE | gene/protein | Mother-cell sigma factor in sporulation cascade required for correct spore development (bidnenko2024complexsporulationspecificexpression pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| SigG | gene/protein | Late forespore sigma factor required for proper spore maturation (bidnenko2024complexsporulationspecificexpression pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | label-only candidate |
| SigK | gene/protein | Late mother-cell sigma factor controlling late sporulation/spore surface genes such as dpaAB in Bacilli (galperin2022conservationandevolution pages 5-7, bidnenko2024complexsporulationspecificexpression pages 2-3) | label-only candidate |
| dpaA / spoVFA | gene/protein | Dipicolinate synthase subunit; strong genomic marker of sporulation in Bacilli and usually absent in nonsporeformers (galperin2022conservationandevolution pages 5-7, galperin2022conservationandevolution pages 4-5) | label-only candidate |
| dpaB / spoVFB | gene/protein | Dipicolinate synthase subunit; accompanies dpaA as a strong Bacilli sporulation marker (galperin2022conservationandevolution pages 5-7, galperin2022conservationandevolution pages 4-5) | label-only candidate |
| sspA | gene/protein | Small acid-soluble spore protein; marker associated with spores, though presence can extend to some nonsporeformers retaining Spo0A (galperin2022conservationandevolution pages 5-7, galperin2022conservationandevolution pages 4-5) | label-only candidate |
| gpr | gene/protein | Germination protease-like marker reported as universally conserved in spore-forming Firmicutes and absent in many non-spore-formers (galperin2022conservationandevolution pages 13-15) | label-only candidate |
| nutrient limitation / starvation | environmental factor | Canonical trigger for sporulation; relief from such stress reduces selection for sporulation, while harsh conditions favor it (beskrovnaya2021structuralmetabolicand pages 2-3, fatton2022cryptosporulationinkurthia pages 2-2) | ENVO:label-only candidate |
| high glucose | environmental factor | Environmental condition that inhibits sporulation in Bacillus and was used in attempts to select against sporulation (bosnar2023attemptstolimit pages 6-8) | CHEBI:17234 (glucose) |
| low pH | environmental factor | Environmental condition that reduces sporulation, partly through reduced SigH activity in Bacillus (bosnar2023attemptstolimit pages 6-8) | PATO/ENVO label-only candidate |
| autoinducer-2 (AI-2) | chemical | Quorum-sensing signal that binds RapC, inactivates ComA, and inhibits sporulation in B. velezensis (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | label-only candidate |
| wet heat resistance assay | assay | Phenotypic test for canonical endospore formation; historical non-spore-forming calls in Kurthia relied on lack of wet-heat resistance (fatton2022cryptosporulationinkurthia pages 2-2) | label-only candidate |
| phase-bright spore-like structures | readout | Microscopy-based readout suggesting cryptosporulation or incomplete sporulation, especially in boundary taxa like Kurthia spp. (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2) | label-only candidate |
| Bacillus subtilis | taxon | Model endospore-former used to define phosphorelay, sigma cascade, and core sporulation genes; useful positive reference taxon (jun2023timecoursetranscriptomeanalysis pages 17-18, bidnenko2024complexsporulationspecificexpression pages 2-3) | NCBITaxon:1423 |
| Bacillus velezensis | taxon | Experimental system for AI-2 → RapC/ComA → sporulation inhibition mechanism (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | NCBITaxon:492670 |
| Clostridium beijerinckii | taxon | Spore-forming clostridial model where loss of spo0A activity drives degenerate non-sporulating variants (humphreys2023clostridiumbeijerinckiistrain pages 1-2) | NCBITaxon:1520 |
| Clostridium perfringens | taxon | Species in which orphan histidine kinases affect Spo0A level and sporulation; useful for direct-phosphorylation branch of regulation (gohari2023identificationoforphan pages 23-24) | NCBITaxon:1502 |
| Kurthia spp. | taxon | Boundary-case taxon historically labeled asporogenic but shown to exhibit cryptosporulation/spore-like structures under some conditions (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2) | NCBITaxon:33882 |
| Firmicutes / Bacillota | taxon | Higher taxon containing many spore-forming and non-spore-forming lineages; comparative genomics shows widespread lineage-specific loss of sporulation genes (galperin2022conservationandevolution pages 13-15, galperin2022conservationandevolution pages 4-5) | NCBITaxon:1239 |


*Table: This table lists candidate causal-graph nodes for the non-spore-forming trait, spanning regulators, pathways, environmental factors, assays, and exemplar taxa. It is useful as a starting node inventory for TraitMech curation, with provisional ontology grounding and context-backed roles.*

---

## 6) Evidence-backed candidate causal edges (triples) for the causal graph
The table below lists candidate edges with evidence snippets, references, and curation notes.

| Subject node | Predicate | Object node | Evidence (short quote/snippet) | Reference (DOI + URL + publication date/year) | Notes/uncertainty | Suggested CURIE grounding |
|---|---|---|---|---|---|---|
| absence of **spo0A** | predicts absence of | endospore formation / non-spore-forming phenotype | “every experimentally characterized spore-forming Firmicute encodes Spo0A, and its absence is described as ‘an excellent predictor of the organism’s inability to sporulate.’” Survey context: 180 genomes total; 76 sporeformers; **spo0A** in 118 genomes, including all 76 sporeformers and 40 nonsporeformers. (galperin2022conservationandevolution pages 4-5) | Galperin et al., 2022. DOI: 10.1128/jb.00079-22. https://doi.org/10.1128/jb.00079-22. Published Jun 2022. | Strong comparative-genomic edge for **absence** of spo0A → non-sporulation. Reverse direction is not valid: spo0A presence is insufficient because many nonsporeformers retain spo0A. | spo0A: UniProtKB gene label only; sporulation: GO:0043934; trait: METPO:1000872 |
| loss of a substantial fraction of sporulation genes | causes / contributes to | asporogenic (non-spore-forming) phenotype | “asporogenic phenotypes can result from ‘the inactivation or loss of a considerable fraction of sporulation genes.’” Kurthia spp. show boundary cases where classical non-spore-forming labels may mask cryptosporulation. (fatton2022cryptosporulationinkurthia pages 2-2) | Fatton et al., 2022. DOI: 10.1111/1462-2920.16145. https://doi.org/10.1111/1462-2920.16145. Published Aug 2022. | Mechanistically broad but well supported. Best curated as a generic edge from loss of core sporulation machinery to non-spore-forming phenotype. Boundary warning: some taxa may retain partial pathways and form cryptospores. | sporulation genes: label-only candidate node; sporulation: GO:0043934; trait: METPO:1000872 |
| lineage-specific loss of core sporulation genes | leads to | non-spore-forming lineages in Firmicutes | “GLOOME ancestral-state reconstruction placed all 40 core sporulation genes at the root of Firmicutes and inferred extensive, lineage-specific loss of these genes in non-spore-forming clades.” (galperin2022conservationandevolution pages 13-15) | Galperin et al., 2022. DOI: 10.1128/jb.00079-22. https://doi.org/10.1128/jb.00079-22. Published Jun 2022. | Good evolutionary/mechanistic support; edge is clade-level rather than strain-level. Suitable as supporting background for a graph centered on gene-loss mechanisms. | Firmicutes/Bacillota: NCBITaxon:1239; sporulation genes: label-only; trait: METPO:1000872 |
| low or absent Spo0A activity | causes | loss of sporulation capacity | Spo0A is the “‘master regulator’ of endospore formation”; “elevated Spo0A∼P levels are required to trigger sporulation,” so failure to produce/activate Spo0A prevents sporulation. (beskrovnaya2021structuralmetabolicand pages 2-3) | Beskrovnaya et al., 2021. DOI: 10.3389/fmicb.2021.630573. https://doi.org/10.3389/fmicb.2021.630573. Published Mar 2021. | Broad mechanistic edge synthesizing phosphorelay logic across Bacilli/Clostridia. Not 2023–2024, but authoritative review support. | Spo0A: label-only candidate node; protein phosphorylation pathway: GO:0000160; sporulation initiation: GO:0009847 (candidate); trait: METPO:1000872 |
| autoinducer-2 (AI-2) | stimulates interaction of | RapC with ComA | “AI-2 directly binds RapC and stimulates RapC–ComA interaction”; this yields “an inactive ComA.” AI-2 tested at 2, 4, 10 μM. (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | Xiong et al., 2024. DOI: 10.1038/s41522-024-00594-6. https://doi.org/10.1038/s41522-024-00594-6. Published Nov 2024. | Taxon-specific experimental edge in *Bacillus velezensis* SQR9; useful regulatory branch upstream of sporulation inhibition. | AI-2: CHEBI candidate label (autoinducer-2; stable CHEBI not asserted here); RapC: label-only; ComA: label-only |
| RapC–ComA interaction / inactive ComA | inhibits | sporulation initiation | AI-2 promoted RapC binding to ComA, “which leads to an inactive ComA and subsequently a sporulation inhibition”; “sporulation of B. velezensis SQR9 was inhibited by AI-2.” (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2) | Xiong et al., 2024. DOI: 10.1038/s41522-024-00594-6. https://doi.org/10.1038/s41522-024-00594-6. Published Nov 2024. | Strong experimental regulatory edge, but should be marked species-specific unless generalized by additional Bacillus evidence. | ComA: label-only; sporulation initiation: GO:0009847 (candidate); NCBITaxon:*Bacillus velezensis* |
| Rap phosphatases | dephosphorylate | Spo0F | “Rap phosphatases directly dephosphorylate Spo0F and thereby reduce phosphate flow to Spo0A.” (xiong2024autoinducer2relievessoil pages 2-3) | Xiong et al., 2024. DOI: 10.1038/s41522-024-00594-6. https://doi.org/10.1038/s41522-024-00594-6. Published Nov 2024. | Useful mechanistic intermediate edge connecting quorum sensing/regulation to reduced Spo0A activation; generic to Bacillus phosphorelay logic. | Spo0F: label-only; phosphatase activity: GO:0016791 (broad candidate) |
| dephosphorylation of Spo0F / reduced phosphate flow | decreases activation of | Spo0A | “reduce phosphate flow to Spo0A” in the sporulation phosphorelay. (xiong2024autoinducer2relievessoil pages 2-3, jun2023timecoursetranscriptomeanalysis pages 17-18) | Xiong et al., 2024. DOI: 10.1038/s41522-024-00594-6. https://doi.org/10.1038/s41522-024-00594-6. Published Nov 2024; Jun et al., 2023. DOI: 10.3390/microorganisms11081928. https://doi.org/10.3390/microorganisms11081928. Published Jul 2023. | Intermediate biochemical edge; supports graph path from regulatory signals to non-sporulation via Spo0A. | Spo0A: label-only; Spo0F: label-only |
| orphan histidine kinase **CPR1953** inactivation | causes decrease/absence of | Spo0A protein | cpr1953 mutant “virtually eliminated sporulation,” producing “no detectable Spo0A.” (gohari2023identificationoforphan pages 23-24) | Gohari et al., 2023. DOI unavailable in provided context. URL unavailable in provided context. Published 2023. | Strong causal evidence but incomplete bibliographic metadata in provided context; curate cautiously until DOI/full citation is verified. Taxon-specific to *Clostridium perfringens* SM101 and culture-condition dependent literature context. | CPR1953: label-only; Spo0A: label-only; NCBITaxon:*Clostridium perfringens* |
| orphan histidine kinase **CPR1954** inactivation | decreases | Spo0A level | cpr1954 null mutant made “substantially less Spo0A than wild-type SM101” and “virtually eliminated sporulation.” (gohari2023identificationoforphan pages 23-24) | Gohari et al., 2023. DOI unavailable in provided context. URL unavailable in provided context. Published 2023. | Same caution as above: strong phenotype link, but finalize only after DOI verification. | CPR1954: label-only; Spo0A: label-only; NCBITaxon:*Clostridium perfringens* |
| decreased Spo0A in *C. perfringens* | abolishes / severely reduces | sporulation | Kinase mutants “virtually eliminated sporulation and CPE production”; complementation “restores wild-type sporulation.” (gohari2023identificationoforphan pages 23-24) | Gohari et al., 2023. DOI unavailable in provided context. URL unavailable in provided context. Published 2023. | Good organism-specific edge; because the direct perturbation is kinase loss, this edge is slightly inferred but strongly supported by linked Spo0A measurements. | Spo0A: label-only; sporulation: GO:0043934; NCBITaxon:*Clostridium perfringens* |
| **spo0A** mutations / loss of spo0A activity | drives | degenerate non-sporulating phenotype in *Clostridium beijerinckii* | Study title and summary: “strain degeneration is driven by the loss of spo0A activity”; comparative genomics of **71 degenerate variants** found mutation hotspots including **spo0A**; mutations in spo0A ultimately dominated populations. (humphreys2023clostridiumbeijerinckiistrain pages 1-2) | Humphreys et al., 2023. DOI: 10.3389/fmicb.2022.1075609. https://doi.org/10.3389/fmicb.2022.1075609. Published Jan 2023. | Strong species-level evidence that spo0A disruption is sufficient to explain emergence of non-sporulating degenerate variants. | spo0A: label-only; NCBITaxon:*Clostridium beijerinckii* |
| sustained **rho** expression | prevents activation of | Spo0A | “maintaining high rho expression ‘prevents the activation of Spo0A’.” (bidnenko2024complexsporulationspecificexpression pages 2-3) | Bidnenko et al., 2024. DOI: 10.1016/j.jbc.2024.107905. https://doi.org/10.1016/j.jbc.2024.107905. Published Dec 2024. | Strong mechanistic regulatory edge in *Bacillus subtilis*; relevant as a noncanonical upstream inhibitor of sporulation. | rho: label-only; Spo0A: label-only; NCBITaxon:*Bacillus subtilis* |
| sustained **rho** expression | blocks formation of | spores | same experiment: high rho expression “inhibits some late sporulation events, thus blocking the formation of spores.” (bidnenko2024complexsporulationspecificexpression pages 2-3) | Bidnenko et al., 2024. DOI: 10.1016/j.jbc.2024.107905. https://doi.org/10.1016/j.jbc.2024.107905. Published Dec 2024. | Strong but organism-specific. Useful edge for a graph path rho → Spo0A inhibition → no spores. | rho: label-only; sporulation: GO:0043934; NCBITaxon:*Bacillus subtilis* |
| Spo0A phosphorylation phosphorelay (KinA/KinB → Spo0F → Spo0B → Spo0A) disruption | arrests / prevents entry into | sporulation | “from KinA/KinB to Spo0F, Spo0B, and Spo0A...signals the start of sporulation”; stages 0/I are where mutants arrest when this initiation program fails. (jun2023timecoursetranscriptomeanalysis pages 17-18) | Jun et al., 2023. DOI: 10.3390/microorganisms11081928. https://doi.org/10.3390/microorganisms11081928. Published Jul 2023. | Good pathway-level edge. More indirect than specific knockout data, but still useful for graph scaffolding around absence of sporulation. | KinA/KinB/Spo0F/Spo0B/Spo0A: label-only; sporulation initiation: GO:0009847 (candidate) |
| disruption or loss of sporulation sigma-factor cascade (**SigH/SigF/SigE/SigG/SigK**) | prevents completion of | endospore morphogenesis | “a cascade of sigma factors (SigF, SigE, SigG, and SigK) that drives temporally- and spatially-defined... programs of spore morphogenesis.” Therefore loss of the cascade blocks normal spore formation. (bidnenko2024complexsporulationspecificexpression pages 2-3) | Bidnenko et al., 2024. DOI: 10.1016/j.jbc.2024.107905. https://doi.org/10.1016/j.jbc.2024.107905. Published Dec 2024. | This row is partly mechanistic inference from accepted pathway architecture; curate as background unless direct loss-of-function evidence is added. | SigH/SigF/SigE/SigG/SigK: label-only; spore morphogenesis: GO:0009847/GO:0043934 candidate |
| cryptosporulation phenotype in some *Kurthia* spp. | warns against overcalling | true non-spore-forming status | *Kurthia* historically classified as asporogenic, but authors observed “spore-like structures” and engulfment hallmarks; however these structures lacked normal heat/UV resistance. (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2) | Fatton et al., 2022. DOI: 10.1111/1462-2920.16145. https://doi.org/10.1111/1462-2920.16145. Published Aug 2022. | This is a curation warning rather than a core causal edge: morphology-only or old phenotype labels may misclassify taxa with partial/unstable sporulation programs. | NCBITaxon:*Kurthia*; trait: METPO:1000872 |


*Table: This table lists evidence-backed candidate causal edges for the trait non-spore forming (METPO:1000872), emphasizing Spo0A-centered mechanisms, sporulation gene loss, and experimentally validated regulatory inhibitors. It is designed to support TraitMech curation by pairing each edge with quotable evidence, references, uncertainty notes, and provisional ontology grounding.*

---

## 7) Recent statistics and data points (curation-relevant)
- **Comparative genomics survey size:** 180 Firmicute genomes (160 genera), with **76 species described as spore-forming** and **102 described as nonsporeformers**; spo0A present in **118/180 genomes**, including all 76 sporeformers and 40 nonsporeformers. (galperin2022conservationandevolution pages 2-4, galperin2022conservationandevolution pages 4-5)
- **Degeneration dataset:** comparative genomics of **71 degenerate variants** of *C. beijerinckii* identified mutation hotspots including **spo0A** and genes suspected to regulate its expression/activity. (humphreys2023clostridiumbeijerinckiistrain pages 1-2)
- **Signal concentrations tested (AI-2):** AI-2 additions at **2, 4, and 10 μM** in *B. velezensis* sporulation inhibition experiments. (xiong2024autoinducer2relievessoil pages 2-3)

---

## 8) DOI-first bibliography (with URLs and publication dates where available)

1. **Bidnenko V. et al.** (Dec 2024). *Complex sporulation-specific expression of transcription termination factor Rho highlights its involvement in Bacillus subtilis cell differentiation.* **Journal of Biological Chemistry** 300:107905. DOI: **10.1016/j.jbc.2024.107905**. URL: https://doi.org/10.1016/j.jbc.2024.107905 (bidnenko2024complexsporulationspecificexpression pages 2-3)

2. **Xiong Q. et al.** (Nov 2024). *Autoinducer-2 relieves soil stress-induced dormancy of Bacillus velezensis by modulating sporulation signaling.* **NPJ Biofilms and Microbiomes** 10. DOI: **10.1038/s41522-024-00594-6**. URL: https://doi.org/10.1038/s41522-024-00594-6 (xiong2024autoinducer2relievessoil pages 2-3, xiong2024autoinducer2relievessoil pages 1-2)

3. **Humphreys J.R. et al.** (Jan 2023). *Clostridium beijerinckii strain degeneration is driven by the loss of Spo0A activity.* **Frontiers in Microbiology** 13. DOI: **10.3389/fmicb.2022.1075609**. URL: https://doi.org/10.3389/fmicb.2022.1075609 (humphreys2023clostridiumbeijerinckiistrain pages 1-2)

4. **Jun J.-S. et al.** (Jul 2023). *Time-Course Transcriptome Analysis of Bacillus subtilis DB104 during Growth.* **Microorganisms** 11:1928. DOI: **10.3390/microorganisms11081928**. URL: https://doi.org/10.3390/microorganisms11081928 (jun2023timecoursetranscriptomeanalysis pages 17-18)

5. **Galperin M.Y. et al.** (Jun 2022). *Conservation and Evolution of the Sporulation Gene Set in Diverse Members of the Firmicutes.* **Journal of Bacteriology** 204(6). DOI: **10.1128/jb.00079-22**. URL: https://doi.org/10.1128/jb.00079-22 (galperin2022conservationandevolution pages 2-4, galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 15-17, galperin2022conservationandevolution pages 13-15, galperin2022conservationandevolution pages 5-7)

6. **Fatton M. et al.** (Aug 2022). *Cryptosporulation in Kurthia spp. forces a rethinking of asporogenesis in Firmicutes.* **Environmental Microbiology** 24:6320–6335. DOI: **10.1111/1462-2920.16145**. URL: https://doi.org/10.1111/1462-2920.16145 (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2)

7. **Beskrovnaya P. et al.** (Mar 2021). *Structural, Metabolic and Evolutionary Comparison of Bacterial Endospore and Exospore Formation.* **Frontiers in Microbiology** 12. DOI: **10.3389/fmicb.2021.630573**. URL: https://doi.org/10.3389/fmicb.2021.630573 (beskrovnaya2021structuralmetabolicand pages 2-3)

8. **Gohari I.M. et al.** (2023). *Identification of orphan histidine kinases that impact sporulation and enterotoxin production by Clostridium perfringens type F strain SM101…* **(journal/DOI not available in retrieved text snippet)**. (gohari2023identificationoforphan pages 23-24)

---

## 9) Curation warnings (do-not-curate / curate-as-uncertain)
1. **Do not equate “spo0A present” with spore formation.** The 180-genome survey includes many spo0A+ genomes described as nonsporeformers; additional missing core genes and/or regulatory degeneration likely explain these cases. Curate “spo0A absence → non-spore forming” as strong; curate the reverse only as uncertain. (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 15-17)

2. **Boundary phenotype (cryptosporulation):** taxa described as non-spore-forming may produce unstable spore-like structures lacking canonical resistance. Curate such cases with an uncertainty flag unless assay conditions and resistance phenotypes are clear. (fatton2022cryptosporulationinkurthia pages 13-13, fatton2022cryptosporulationinkurthia pages 2-2)

3. **Incomplete bibliographic metadata:** the *C. perfringens* kinase study evidence is strong mechanistically (kinase mutants reduce Spo0A and sporulation), but the DOI/journal metadata were not available in the retrieved snippet; treat as **provisionally citable** pending verification before curating into a permanent knowledge base. (gohari2023identificationoforphan pages 23-24)


References

1. (galperin2022conservationandevolution pages 4-5): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 106 citations and is from a peer-reviewed journal.

2. (galperin2022conservationandevolution pages 13-15): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 106 citations and is from a peer-reviewed journal.

3. (fatton2022cryptosporulationinkurthia pages 13-13): Mathilda Fatton, Sevasti Filippidou, Thomas Junier, Guillaume Cailleau, Matthieu Berge, Daniel Poppleton, Thorsten B. Blum, Marek Kaminek, Adolfo Odriozola, Jochen Blom, Shannon L. Johnson, Jan Pieter Abrahams, Patrick S. Chain, Simonetta Gribaldo, Elitza I. Tocheva, Benoît Zuber, Patrick H. Viollier, and Pilar Junier. Cryptosporulation in <scp><i>kurthia</i></scp> spp. forces a rethinking of asporogenesis in firmicutes. Environmental Microbiology, 24:6320-6335, Aug 2022. URL: https://doi.org/10.1111/1462-2920.16145, doi:10.1111/1462-2920.16145. This article has 6 citations and is from a domain leading peer-reviewed journal.

4. (fatton2022cryptosporulationinkurthia pages 2-2): Mathilda Fatton, Sevasti Filippidou, Thomas Junier, Guillaume Cailleau, Matthieu Berge, Daniel Poppleton, Thorsten B. Blum, Marek Kaminek, Adolfo Odriozola, Jochen Blom, Shannon L. Johnson, Jan Pieter Abrahams, Patrick S. Chain, Simonetta Gribaldo, Elitza I. Tocheva, Benoît Zuber, Patrick H. Viollier, and Pilar Junier. Cryptosporulation in <scp><i>kurthia</i></scp> spp. forces a rethinking of asporogenesis in firmicutes. Environmental Microbiology, 24:6320-6335, Aug 2022. URL: https://doi.org/10.1111/1462-2920.16145, doi:10.1111/1462-2920.16145. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (beskrovnaya2021structuralmetabolicand pages 2-3): Polina Beskrovnaya, Danielle L. Sexton, Mona Golmohammadzadeh, Ameena Hashimi, and Elitza I. Tocheva. Structural, metabolic and evolutionary comparison of bacterial endospore and exospore formation. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.630573, doi:10.3389/fmicb.2021.630573. This article has 89 citations and is from a peer-reviewed journal.

6. (bidnenko2024complexsporulationspecificexpression pages 2-3): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 9 citations and is from a domain leading peer-reviewed journal.

7. (jun2023timecoursetranscriptomeanalysis pages 17-18): Ji-Su Jun, Hyang-Eun Jeong, Su-Yeong Moon, Se-Hee Shin, and Kwang-Won Hong. Time-course transcriptome analysis of bacillus subtilis db104 during growth. Microorganisms, 11:1928, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081928, doi:10.3390/microorganisms11081928. This article has 10 citations.

8. (humphreys2023clostridiumbeijerinckiistrain pages 1-2): Jonathan R. Humphreys, Bisrat J. Debebe, Stephen P. Diggle, and Klaus Winzer. Clostridium beijerinckii strain degeneration is driven by the loss of spo0a activity. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1075609, doi:10.3389/fmicb.2022.1075609. This article has 14 citations and is from a peer-reviewed journal.

9. (gohari2023identificationoforphan pages 23-24): I Mehdizadeh Gohari, J Li, and MA Navarro. Identification of orphan histidine kinases that impact sporulation and enterotoxin production by clostridium perfringens type f strain sm101 in a pathophysiologically …. Unknown journal, 2023.

10. (xiong2024autoinducer2relievessoil pages 2-3): Qin Xiong, Huihui Zhang, Xia Shu, Xiting Sun, Haichao Feng, Zhihui Xu, Ákos T. Kovács, Ruifu Zhang, and Yunpeng Liu. Autoinducer-2 relieves soil stress-induced dormancy of bacillus velezensis by modulating sporulation signaling. NPJ Biofilms and Microbiomes, Nov 2024. URL: https://doi.org/10.1038/s41522-024-00594-6, doi:10.1038/s41522-024-00594-6. This article has 12 citations and is from a peer-reviewed journal.

11. (xiong2024autoinducer2relievessoil pages 1-2): Qin Xiong, Huihui Zhang, Xia Shu, Xiting Sun, Haichao Feng, Zhihui Xu, Ákos T. Kovács, Ruifu Zhang, and Yunpeng Liu. Autoinducer-2 relieves soil stress-induced dormancy of bacillus velezensis by modulating sporulation signaling. NPJ Biofilms and Microbiomes, Nov 2024. URL: https://doi.org/10.1038/s41522-024-00594-6, doi:10.1038/s41522-024-00594-6. This article has 12 citations and is from a peer-reviewed journal.

12. (galperin2022conservationandevolution pages 15-17): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 106 citations and is from a peer-reviewed journal.

13. (galperin2022conservationandevolution pages 2-4): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 106 citations and is from a peer-reviewed journal.

14. (bosnar2023attemptstolimit pages 6-8): Luke M. Bosnar, Anya E. Shindler, Jennifer Wood, Craig Patch, and Ashley E. Franks. Attempts to limit sporulation in the probiotic strain bacillus subtilis bg01-4tm through mutation accumulation and selection. Access Microbiology, May 2023. URL: https://doi.org/10.1099/acmi.0.000419, doi:10.1099/acmi.0.000419. This article has 2 citations.

15. (galperin2022conservationandevolution pages 5-7): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 106 citations and is from a peer-reviewed journal.