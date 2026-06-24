---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:31:18.604384'
end_time: '2026-06-18T06:42:17.169435'
duration_seconds: 658.57
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: carboxysome
  trait_identifier: traitmech:000072
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: carboxysome
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A bacterial microcompartment \u2014 a polyhedral protein-shelled organelle\
    \ that encapsulates RuBisCO and carbonic anhydrase to concentrate CO2 for carbon\
    \ fixation in cyanobacteria and many chemoautotrophs."
  parent_traits: traitmech:000066
  synonyms: bacterial microcompartment
  evidence_summary: 'DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial
    microcompartments; the carboxysome is the archetypal protein-shelled CO2-fixing
    microcompartment.) | DOI:10.1038/nrmicro1913:  (Yeates et al. describe protein-based
    organelles in bacteria (carboxysomes and related microcompartments), including
    the carboxysome shell and its encapsulated enzymes.)'
  causal_graph_summary: 'carboxysome_co2_concentrating: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxysome
- **METPO identifier:** traitmech:000072
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A bacterial microcompartment — a polyhedral protein-shelled organelle that encapsulates RuBisCO and carbonic anhydrase to concentrate CO2 for carbon fixation in cyanobacteria and many chemoautotrophs.
- **Parent traits:** traitmech:000066
- **Synonyms:** bacterial microcompartment
- **Existing evidence:** DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments; the carboxysome is the archetypal protein-shelled CO2-fixing microcompartment.) | DOI:10.1038/nrmicro1913:  (Yeates et al. describe protein-based organelles in bacteria (carboxysomes and related microcompartments), including the carboxysome shell and its encapsulated enzymes.)
- **Existing causal graph summary:** carboxysome_co2_concentrating: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **carboxysome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carboxysome.yaml`.

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
- **Trait label:** carboxysome
- **METPO identifier:** traitmech:000072
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A bacterial microcompartment — a polyhedral protein-shelled organelle that encapsulates RuBisCO and carbonic anhydrase to concentrate CO2 for carbon fixation in cyanobacteria and many chemoautotrophs.
- **Parent traits:** traitmech:000066
- **Synonyms:** bacterial microcompartment
- **Existing evidence:** DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments; the carboxysome is the archetypal protein-shelled CO2-fixing microcompartment.) | DOI:10.1038/nrmicro1913:  (Yeates et al. describe protein-based organelles in bacteria (carboxysomes and related microcompartments), including the carboxysome shell and its encapsulated enzymes.)
- **Existing causal graph summary:** carboxysome_co2_concentrating: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **carboxysome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carboxysome.yaml`.

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


# Carboxysome (TraitMech: traitmech:000072) — Curation-Focused Research Report (2023–2024 prioritized)

## Scope summary (Trait Scope)
The **carboxysome** is a **bacterial microcompartment (BMC)**: a polyhedral **protein-shelled organelle** that encapsulates **Form I RuBisCO** (EC:4.1.1.39) and **carbonic anhydrase** (EC:4.2.1.1), creating a microenvironment that supports **CO2 fixation** as part of the **Calvin–Benson–Bassham (CBB) cycle** and functions as a core element of bacterial **CO2-concentrating mechanisms (CCMs)**. (kerfeld2018bacterialmicrocompartments pages 1-2, kerfeld2018bacterialmicrocompartments pages 2-3, wieschollek2024anewtype pages 1-2)

**Boundary cases / nearby traits**: 
- “Bacterial microcompartment” is broader than carboxysome; many BMCs are **catabolic metabolosomes** (e.g., PDU/EUT) whereas the carboxysome is described as the **sole known anabolic BMC type**, distinguished by **CBB-cycle CO2 fixation cargo** (RuBisCO + CA) rather than catabolic enzyme sets. (kerfeld2018bacterialmicrocompartments pages 1-2)
- The trait “carboxysome” should refer to the **morphological presence of this proteinaceous organelle** and its **functional capacity to concentrate CO2 for RuBisCO**, not merely the presence of RuBisCO genes or a generic CCM. (kerfeld2018bacterialmicrocompartments pages 2-3, wieschollek2024anewtype pages 1-2)

**Major classes**: 
- **α-carboxysomes** (common in autotrophic Proteobacteria and some cyanobacteria) generally contain **Form IA RuBisCO** and have distinct scaffolding/assembly proteins (notably **CsoS2**). (cheng2024molecularinteractionsof pages 1-2, wieschollek2024anewtype pages 1-2, trettel2024modelingbacterialmicrocompartment pages 2-3)
- **β-carboxysomes** (exclusive to cyanobacteria) contain **Form IB RuBisCO** and key scaffolding/biogenesis proteins **CcmM/CcmN** and accessory factors such as **CcmS**. (cheng2024molecularinteractionsof pages 1-2, kerfeld2018bacterialmicrocompartments pages 4-5, cheng2024molecularinteractionsof pages 3-5)

## Key concepts and definitions (current understanding)
### 1) Core CO2-concentrating mechanism (CCM)
A common mechanistic model is:
1. **Transporters** elevate the **cytoplasmic bicarbonate (HCO3−)** pool.
2. HCO3− enters the carboxysome through the shell.
3. **Carboxysomal carbonic anhydrase (CA)** converts HCO3− to **CO2** inside the compartment.
4. The **shell diffusion barrier** reduces CO2 leakage, elevating CO2 near RuBisCO and favoring carboxylation over oxygenation. (kerfeld2018bacterialmicrocompartments pages 2-3, cheng2024molecularinteractionsof pages 1-2, wieschollek2024anewtype pages 1-2, trettel2024modelingbacterialmicrocompartment pages 2-3)

### 2) Shell architecture and permeability
BMC shells are built from conserved protein classes:
- **BMC-H** (hexameric tiles), **BMC-T** (trimeric pseudohexamers; sometimes gated pores), and **BMC-P** (pentamers at vertices). Central pores act as **metabolite channels**. (kerfeld2018bacterialmicrocompartments pages 2-3, kerfeld2018bacterialmicrocompartments media d626e058, kerfeld2018bacterialmicrocompartments media 32458108)
Recent synthesis/modeling reviews report **pore diameters ~4–7 Å** and emphasize that pore residue changes can alter permeation and whole-compartment function, supporting “shell permeability” as a tunable causal node. (trettel2024modelingbacterialmicrocompartment pages 2-3)

### 3) Assembly and biogenesis pathways (α vs β)
A major conceptual distinction is **assembly pathway**:
- **β-carboxysome: “core-first”**. RuBisCO is aggregated/condensed by scaffolding factors (e.g., **CcmM**) and then enveloped by shell proteins recruited by interactions including **CcmN encapsulation peptide**; **CcmL pentamers** contribute to closure. (kerfeld2018bacterialmicrocompartments pages 4-5, kerfeld2018bacterialmicrocompartments media d626e058)
- **α-carboxysome: “concomitant/shell-associated”**. Assembly is assisted by **CsoS2**, which recruits shell components and organizes cargo–shell interfaces. (kerfeld2018bacterialmicrocompartments pages 4-5, kerfeld2018bacterialmicrocompartments media d626e058)

## Recent developments and latest research (2023–2024)
### A) α-carboxysome shell assembly: CsoS2 “molecular thread”
A key 2023 advance is high-resolution cryo-EM evidence that **CsoS2** uses its C-terminus to **“stitch” shell-protein interfaces**, acting as a general “molecular thread” for α-carboxysome shell assembly. The study reports a **1.86 Å** cryo-EM map and identifies structured C-terminal fragments binding at tri-capsomere interfaces with large interface areas (e.g., **3333 Å²** at one site), and emphasizes a conserved repetitive **[IV]TG** interaction motif important for assembly architecture. (ni2023intrinsicallydisorderedcsos2 pages 3-5, ni2023intrinsicallydisorderedcsos2 pages 7-8)

This supports curating **CsoS2-dependent shell assembly** as a mechanistic subgraph specific to α-carboxysomes. (kerfeld2018bacterialmicrocompartments pages 4-5, ni2023intrinsicallydisorderedcsos2 pages 3-5)

### B) β-carboxysome assembly regulation: CcmS–CcmK1 interaction (2024)
A 2024 structural/biochemical study provides quantitative evidence for an accessory assembly mechanism in β-carboxysomes: **CcmS binds the unique C-terminal extension of shell protein CcmK1** with **Kd = 41.5 μM**, identifies critical residues (e.g., Arg108), and proposes how CcmS-mediated interactions drive/organize outer-shell assembly. This fills a gap between “core-first condensation” and “shell enclosure” and motivates adding **chaperone-mediated shell assembly** edges to the causal graph. (cheng2024molecularinteractionsof pages 3-5, cheng2024molecularinteractionsof pages 1-2)

### C) Expanded diversity of carboxysomal carbonic anhydrases: iota CA in alkaline chemolithoautotrophs (2024)
A 2024 report identifies a **new carboxysomal CA type** in sulfur chemolithoautotrophs from alkaline environments: an **ι-class carbonic anhydrase (ιCA)** encoded in carboxysome loci. Functional genetics show that interrupting the **ιCA gene abolished growth under low-CO2 conditions** and eliminated detectable CA activity in carboxysome enrichments, supporting a direct phenotype link between **carboxysomal CA** and **low-CO2 fitness**. (wieschollek2024anewtype pages 1-2)

This is important for TraitMech because it provides direct, causal genotype→trait function evidence, but it is taxon- and niche-specific (alkaline environments). (wieschollek2024anewtype pages 1-2)

### D) Modeling and pore chemistry: anions and chloride as permeability modulators (2024)
A 2024 modeling-focused review synthesizes evidence that pore properties (diameter, ion coordination) regulate permeation. It reports chloride occupancy at pore-adjacent sites and proposes that chloride may competitively hinder substrate permeation (example given for 1,2-propanediol pores in other BMCs), suggesting a potentially general “ion-gated permeability” concept; however, this is partially model-driven and may not be universal across carboxysomes. (trettel2024modelingbacterialmicrocompartment pages 5-6)

## Current applications and real-world implementations
### 1) Carboxysome/BMC shells as engineerable nanocages (2024)
Carboxysome shells are being repurposed as **programmable protein cages**. A 2024 ACS Nano study reports engineering of **α-carboxysome shell-based nanocages** with docking systems (SpyTag/SpyCatcher; coiled-coils) to modulate cargo loading. This supports curation of “engineered shell can encapsulate heterologous cargo” as an application edge, though these constructs may be outside the strict native carboxysome trait boundary. (li2024nanoengineeringcarboxysomeshells pages 1-3)

### 2) Synthetic BMCs for pathway insulation and improved production (2024)
A 2024 Biochemical Society Transactions review (Doron & Kerfeld) compiles multiple experimental demonstrations:
- **Ethanol nano-bioreactor**: encapsulated pyruvate decarboxylase + alcohol dehydrogenase increased ethanol production **by 63%** versus unencapsulated control. (doron2024bacterialmicrocompartmentsas pages 7-8)
- **Hydrogen nanoreactor**: carboxysome shell encapsulation produced a **4.1-fold increase in H2 production** in aerobically grown E. coli vs free enzyme. (doron2024bacterialmicrocompartmentsas pages 7-8)
- **sFUT**: purified particles converted **1 μmol pyruvate to 600 nmol formate** in vitro (formate-utilizing BMC module). (doron2024bacterialmicrocompartmentsas pages 7-8)

This supports a general expert consensus that BMC shells can increase effective flux by colocalization and protection from toxic intermediates, and can protect oxygen-sensitive catalysts by creating an O2-limited microenvironment. (doron2024bacterialmicrocompartmentsas pages 5-7, doron2024bacterialmicrocompartmentsas pages 7-8)

### 3) Heterologous shell assembly as an industrial platform (2024)
Doron et al. demonstrate heterologous expression and purification of capped and uncapped (“wiffle ball”) shells in **Zymomonas mobilis**, with particle diameters ~**39–42 nm** and demonstrated cargo targeting via SpyTag/SpyCatcher. This provides an implementation pathway for transferring microcompartment scaffolds into industrial chassis organisms. (doron2024towardsusingbacterial pages 5-6)

## Expert opinions and analysis (authoritative sources)
- Kerfeld et al. (2018) is a high-citation review that frames BMCs (including carboxysomes) as **selectively permeable protein organelles** that enhance pathway flux via colocalization and also provide protection from unwanted reactions. This can be treated as the “expert consensus” backdrop for carboxysome causal graph modeling. (kerfeld2018bacterialmicrocompartments pages 1-2, kerfeld2018bacterialmicrocompartments pages 2-3)
- Doron & Kerfeld (2024) argue that BMCs represent a “next-generation metabolic engineering tool” because they are autonomous catalytic modules that can be installed and tuned using shell composition, targeting peptides, and engineered pores/transport. (doron2024bacterialmicrocompartmentsas pages 1-3, doron2024bacterialmicrocompartmentsas pages 10-12)

## Relevant statistics and data (recent studies)
Mechanism/structure:
- Shell pores are reported as **~4–7 Å** and contribute to selective permeability. (trettel2024modelingbacterialmicrocompartment pages 2-3)
- Modeled/compiled estimates suggest carboxysomes can **concentrate CO2 around RuBisCO >1000×** (review synthesis), supporting “local CO2 elevation” as a core function. (trettel2024modelingbacterialmicrocompartment pages 2-3)
- CcmS binds CcmK1-C-terminus with **Kd = 41.5 μM** and forms a complex consistent with multi-subunit assembly roles. (cheng2024molecularinteractionsof pages 3-5)

Engineering/permeability:
- “Wiffle ball” uncapped shells can create **~50 Å vertex gaps**, enabling passage of larger metabolites/small proteins. (doron2024bacterialmicrocompartmentsas pages 5-7)

Phenotype:
- Disrupting a carboxysomal **ιCA** gene causes inability to grow under **low-CO2** conditions (strong causal phenotype link). (wieschollek2024anewtype pages 1-2)

## Visual evidence (figures)
Kerfeld et al. figures summarize key concepts required for curation: (i) shell protein classes (BMC-H/T/P) and (ii) α vs β assembly pathways (core-first vs concomitant). These can guide what nodes/edges to represent explicitly. (kerfeld2018bacterialmicrocompartments media d626e058, kerfeld2018bacterialmicrocompartments media 32458108)

## Candidate nodes for TraitMech curation (grouped)
### Trait and sub-traits
- **Carboxysome** (METPO: traitmech:000072)
- α-carboxysome (label-only)
- β-carboxysome (label-only)

### Cellular structures / compartments
- Carboxysome shell (label-only)
- Shell pore (label-only)
- Enzymatic core / RuBisCO condensate (label-only)

### Proteins / complexes (examples; label-only unless curated via UniProt in downstream work)
- RuBisCO (EC:4.1.1.39)
- Carbonic anhydrase (EC:4.2.1.1), including β-/γ-CA and **ιCA** (label-only subtype)
- α-carboxysome proteins: **CsoS2**, **CsoS1**, **CsoS4** (label-only)
- β-carboxysome proteins: **CcmK** (e.g., CcmK1), **CcmL**, **CcmM**, **CcmN**, **CcmS** (label-only)
- Shell building blocks: BMC-H, BMC-T, BMC-P (label-only)

### Processes / pathways
- CO2-concentrating mechanism (CCM) (label-only)
- Calvin–Benson–Bassham cycle (CBB) (label-only)
- Carboxysome assembly/biogenesis (label-only)
- Selective permeability / diffusion barrier function (label-only)

### Chemicals / metabolites
- CO2 (CHEBI:16526)
- Bicarbonate HCO3− (CHEBI:17544)
- Oxygen O2 (CHEBI:15379)
- (Optional/if curated) ribulose-1,5-bisphosphate (RuBP) and 3-phosphoglycerate (3-PGA) (labels only in current evidence set) (trettel2024modelingbacterialmicrocompartment pages 2-3)

### Environmental and experimental factors
- Low CO2 condition (ENVO label-only)
- High external CO2 requirement as assay phenotype (ENVO label-only) (kerfeld2018bacterialmicrocompartments pages 4-5)
- Alkaline environments / high pH (ENVO label-only; supported contextually for ιCA distribution) (wieschollek2024anewtype pages 1-2)

## Candidate causal edges (curation table)
The following table is formatted for direct translation into a TraitMech YAML causal graph (subject–predicate–object), including evidence snippets, DOIs/URLs, dates, and grounding notes:

| Edge (subject–predicate–object) | Evidence type | Source (first author year, journal) | DOI + URL | Publication date | Supporting snippet | Curation notes (strength/uncertainty, taxon-specificity) | Candidate ontology grounding for subject/object |
|---|---|---|---|---|---|---|---|
| carboxysome shell → prevents loss of → CO2 to cytoplasm | mechanistic | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “The shell prevents loss of CO2 to the cytoplasm” (kerfeld2018bacterialmicrocompartments pages 2-3) | Strong review-level statement; central causal edge for carboxysome CCM function. | subject: carboxysome shell [label-only]; object: CO2 [CHEBI:16526] |
| carboxysomal carbonic anhydrase → converts → HCO3- to CO2 | mechanistic | Wieschollek 2024, *Appl Environ Microbiol* | 10.1128/aem.01075-24 — https://doi.org/10.1128/aem.01075-24 | Sep 2024 | “transporters elevate cytoplasmic HCO3−, which upon entry into carboxysomes is converted by CA to CO2” (wieschollek2024anewtype pages 1-2) | Strong, directly stated mechanism; broad to bacterial CCMs with carboxysomes. | subject: carbonic anhydrase [EC:4.2.1.1]; object: bicarbonate [CHEBI:17544], CO2 [CHEBI:16526] |
| CO2/HCO3- transporters → elevate → cytoplasmic HCO3- | mechanistic | Wieschollek 2024, *Appl Environ Microbiol* | 10.1128/aem.01075-24 — https://doi.org/10.1128/aem.01075-24 | Sep 2024 | “CCMs comprise CO2 and HCO3− transporters plus carboxysomes; transporters elevate cytoplasmic HCO3−” (wieschollek2024anewtype pages 1-2) | Strong for CCM context; edge belongs to broader CCM graph but is upstream of carboxysome function. | subject: bicarbonate transporter [GO:0015701 candidate]; object: bicarbonate [CHEBI:17544] |
| elevated cytoplasmic HCO3- → enables entry into → carboxysome | mechanistic | Trettel 2024, *Front Plant Sci* | 10.3389/fpls.2024.1346759 — https://doi.org/10.3389/fpls.2024.1346759 | Feb 2024 | “Bicarbonate is actively accumulated in the cell, enters the carboxysome, is converted into CO2” (trettel2024modelingbacterialmicrocompartment pages 2-3) | Moderate; mechanistically explicit but phrased at process level rather than single molecular actor. | subject: bicarbonate [CHEBI:17544]; object: carboxysome [METPO:traitmech:000072] |
| carboxysome shell → permits passage of → HCO3- and RuBP | permeability | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “the shell has selective permeability that permits HCO3− and RuBP passage” (cheng2024molecularinteractionsof pages 1-2) | Strong review-style summary within primary paper; useful for pore/selective permeability node. | subject: carboxysome shell [label-only]; object: bicarbonate [CHEBI:17544], ribulose 1,5-bisphosphate [CHEBI candidate label-only] |
| carboxysome shell → limits influx of → O2 | permeability | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “while limiting O2 influx” (cheng2024molecularinteractionsof pages 1-2) | Strong and biologically important; supports anti-oxygenation role. | subject: carboxysome shell [label-only]; object: oxygen [CHEBI:15379] |
| carbonic anhydrase activity inside carboxysome → elevates local concentration of → CO2 around Rubisco | mechanistic | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “CA inside the carboxysome dehydrates HCO3− to CO2, elevating CO2 concentration around Rubisco” (cheng2024molecularinteractionsof pages 1-2) | Strong; direct causal link from enzyme activity to local microenvironment. | subject: carbonic anhydrase [EC:4.2.1.1]; object: CO2 [CHEBI:16526], Rubisco [EC:4.1.1.39] |
| elevated CO2 around Rubisco → enhances → Rubisco carboxylation | mechanistic | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “enhances Rubisco carboxylation rates and reduces unproductive oxygenation” (cheng2024molecularinteractionsof pages 1-2) | Strong process edge; could also connect to reduced oxygenation/photorespiration. | subject: CO2 concentration around Rubisco [label-only]; object: Rubisco carboxylase activity [GO:0016984 candidate] |
| CcmM SSLDs → cause aggregation of → Rubisco molecules | assembly | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “the SSLDs of CcmM cause the aggregation of Rubisco molecules” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong, β-carboxysome-specific assembly mechanism. | subject: CcmM [label-only]; object: Rubisco [EC:4.1.1.39] |
| CcmM-mediated Rubisco aggregation → forms → β-carboxysome core/condensate | assembly | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “Rubisco condensate formation by CcmM in β-carboxysome biogenesis” (cheng2024molecularinteractionsof pages 10-10) | Strong; β-carboxysome-specific and useful for condensate intermediate node. | subject: CcmM [label-only]; object: Rubisco condensate [label-only] |
| CcmN encapsulation peptide → recruits/enables envelopment by → shell proteins | assembly | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | core is “encapsulated by shell proteins that interact with … the encapsulation peptide of CcmN47” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong for β-carboxysome shell recruitment; peptide-specific. | subject: CcmN encapsulation peptide [label-only]; object: shell proteins [BMC-H/T/P label set] |
| CcmL pentamers → mediate → shell closure | assembly | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “Shell closure is mediated by CcmL pentamers” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong, β-carboxysome-specific structural edge. | subject: CcmL [label-only; BMC-P family]; object: shell closure [GO candidate label-only] |
| CsoS2 C-terminus → stitches/threads through → multiple shell protein interfaces | assembly | Ni 2023, *Nat Commun* | 10.1038/s41467-023-41211-y — https://doi.org/10.1038/s41467-023-41211-y | Sep 2023 | “CsoS2 C-terminus is well-structured and acts as a universal ‘molecular thread’ stitching through multiple shell protein interfaces” (kerfeld2018bacterialmicrocompartments pages 4-5, ni2023intrinsicallydisorderedcsos2 pages 3-5) | Strong, α-carboxysome-specific primary structural evidence. | subject: CsoS2 C-terminus [label-only]; object: shell protein interfaces [CsoS1A/CsoS4A label-only] |
| conserved [IV]TG motif in CsoS2 → is critical for → shell assembly and architecture | assembly | Ni 2023, *Nat Commun* | 10.1038/s41467-023-41211-y — https://doi.org/10.1038/s41467-023-41211-y | Sep 2023 | “[IV]TG … is critical to the shell assembly and architecture” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong for α-carboxysome motif-level mechanism; curation may require sequence-feature node. | subject: CsoS2 [IV]TG motif [label-only]; object: α-carboxysome shell assembly [label-only] |
| CsoS2 → recruits → major shell protein CsoS1 | assembly | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “α‑carboxysomes require the intrinsically disordered CsoS2, which ‘recruits the major shell protein CsoS1’” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong review statement; α-carboxysome-specific. | subject: CsoS2 [label-only]; object: CsoS1 [label-only] |
| CcmS → binds → CcmK1 C-terminal extension | assembly | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | “CcmS specifically interacts with the C-terminal extension of the carboxysome shell protein CcmK1” (cheng2024molecularinteractionsof pages 1-2) | Strong primary structural/biochemical evidence; β-carboxysome-specific. | subject: CcmS [label-only]; object: CcmK1 C-terminus [label-only] |
| CcmS–CcmK1 interaction → mediates → β-carboxysome assembly | assembly | Cheng 2024, *Plant Physiol* | 10.1093/plphys/kiae438 — https://doi.org/10.1093/plphys/kiae438 | Aug 2024 | title/summary: “interactions … mediate β-carboxysome assembly” and “ccmS deletion impairs CcmK1 assembly and growth” (cheng2024molecularinteractionsof pages 3-5) | Strong but taxon-tested in cyanobacteria; include note on species conservation inference. | subject: CcmS:CcmK1 complex [label-only]; object: β-carboxysome assembly [label-only] |
| BMC-H/T/P shell proteins → form → selectively permeable shell with central pores | permeability | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “BMC‑H…hexamer”, “BMC‑T…pseudohexameric trimers”, “BMC‑P…pentamers”; “A pore…serves as a channel for metabolites” (kerfeld2018bacterialmicrocompartments pages 2-3) | Strong generalized shell architecture edge across BMCs including carboxysomes. | subject: BMC-H/BMC-T/BMC-P [label-only]; object: shell pore [label-only] |
| shell central pores (~4–7 Å) → control permeation of → metabolites/anions | permeability | Trettel 2024, *Front Plant Sci* | 10.3389/fpls.2024.1346759 — https://doi.org/10.3389/fpls.2024.1346759 | Feb 2024 | “central pores (~4–7 Å) control permeation” (trettel2024modelingbacterialmicrocompartment pages 2-3) | Moderate-to-strong; partly synthesis/modeling-based but anchored in structural literature. | subject: shell pore [label-only]; object: metabolites [CHEBI:25212], anions [CHEBI:22563] |
| chloride binding at shell pore → blocks/hinders permeation of → substrate through pore | permeability | Trettel 2024, *Front Plant Sci* | 10.3389/fpls.2024.1346759 — https://doi.org/10.3389/fpls.2024.1346759 | Feb 2024 | “Chloride can competitively block substrates … and thus hinder permeation rates” (trettel2024modelingbacterialmicrocompartment pages 5-6) | Uncertain/modeling-derived; not carboxysome-universal and may depend on shell protein/pore context. Mark as tentative. | subject: chloride [CHEBI:17996]; object: substrate permeation through shell pore [label-only] |
| disruption of carboxysomal iota carbonic anhydrase → abolishes → growth under low-CO2 conditions | phenotype | Wieschollek 2024, *Appl Environ Microbiol* | 10.1128/aem.01075-24 — https://doi.org/10.1128/aem.01075-24 | Sep 2024 | “When the gene encoding ιCA was interrupted… cells could no longer grow under low-CO2 conditions” (wieschollek2024anewtype pages 1-2) | Strong primary phenotype; taxon-specific to *Thiomicrospira pelophila* but highly relevant for CA necessity in some carboxysomes. | subject: iota carbonic anhydrase [label-only]; object: low CO2 growth [ENVO low CO2 label-only] |
| low external CO2 → reveals requirement for → intact carboxysome/CCM | phenotype | Kerfeld 2018, *Nat Rev Microbiol* | 10.1038/nrmicro.2018.10 — https://doi.org/10.1038/nrmicro.2018.10 | Mar 2018 | “Loss or defect of carboxysomes is indicated by a requirement for high external CO2” (kerfeld2018bacterialmicrocompartments pages 4-5) | Strong phenotype marker; useful assay edge rather than intrinsic mechanism. | subject: defective carboxysome [label-only]; object: high external CO2 requirement [ENVO elevated CO2 label-only] |
| uncapped “wiffle-ball” shell → increases permeability to → larger metabolites and small proteins | engineering | Doron & Kerfeld 2024, *Biochem Soc Trans* | 10.1042/bst20230229 — https://doi.org/10.1042/bst20230229 | May 2024 | “producing ~50 Å gaps at vertices that permit passage of large metabolites and small proteins” (doron2024bacterialmicrocompartmentsas pages 5-7) | Strong engineering evidence; synthetic shell state, not native trait edge. | subject: uncapped shell / wiffle ball [label-only]; object: large metabolites [CHEBI:25212], proteins [PR:000000001] |
| encapsulation of ethanol-pathway enzymes in BMC → increases → ethanol production | engineering | Doron & Kerfeld 2024, *Biochem Soc Trans* | 10.1042/bst20230229 — https://doi.org/10.1042/bst20230229 | May 2024 | “encapsulated pyruvate decarboxylase and an alcohol dehydrogenase… increased ethanol production by 63%” (doron2024bacterialmicrocompartmentsas pages 7-8) | Strong engineering application; not a native carboxysome function but supports compartmentalization benefit. | subject: engineered BMC encapsulation [label-only]; object: ethanol production [CHEBI:16236] |
| encapsulation in carboxysome shell-based hydrogen nanoreactor → increases → H2 production | engineering | Doron & Kerfeld 2024, *Biochem Soc Trans* | 10.1042/bst20230229 — https://doi.org/10.1042/bst20230229 | May 2024 | “encapsulation yielded a 4.1-fold increase in H2 production” (doron2024bacterialmicrocompartmentsas pages 7-8) | Strong engineering evidence; shell-based application leveraging O2-limited microenvironment. | subject: engineered carboxysome shell nanoreactor [label-only]; object: hydrogen production [CHEBI:18276] |
| HO shell synthetic operon expression in Zymomonas mobilis → produces → ~39–42 nm shells with cargo targeting | engineering | Doron et al. 2024, *Front Bioeng Biotechnol* | 10.3389/fbioe.2024.1344260 — https://doi.org/10.3389/fbioe.2024.1344260 | Jan 2024 | “Purified particles were morphologically homogeneous… diameters ~39 nm… ~42 nm… Cargo targeting was demonstrated” (doron2024towardsusingbacterial pages 5-6) | Strong implementation evidence for heterologous shell assembly platform; HO shell is non-carboxysome BMC model, so peripheral to native trait. | subject: HO shell synthetic operon [label-only]; object: BMC shell particle [label-only] |


*Table: This table compiles evidence-backed candidate subject-predicate-object edges for a TraitMech carboxysome causal graph. It emphasizes mechanistic function, assembly, permeability, phenotype, and engineering evidence, while flagging uncertain or non-native edges for cautious curation.*

## Warnings / claims needing caution before curation
1. **Modeling-derived pore chemistry edges** (e.g., chloride competitive blocking of substrate permeation) are valuable hypotheses but may not be general across carboxysomes; these should be curated as **uncertain** or moved to a “model prediction” evidence tier until validated in the specific carboxysome shell context. (trettel2024modelingbacterialmicrocompartment pages 5-6)
2. **Engineering outcomes** (ethanol +63%, H2 ×4.1) are strong evidence for the general principle that protein shells can increase pathway performance, but they are **not native carboxysome trait edges**; include them only if the TraitMech graph is intended to cover “carboxysome-derived shell used as scaffold” applications. (doron2024bacterialmicrocompartmentsas pages 7-8)
3. **CO2 >1000× concentration** is presented in a review-synthesis context; if the YAML requires numeric parameters, this should be tied to specific primary measurements not available in the current evidence set. (trettel2024modelingbacterialmicrocompartment pages 2-3)
4. **Taxon specificity**: ιCA dependence and low-CO2 growth phenotype are demonstrated in *Thiomicrospira pelophila* and should be marked taxon-linked rather than universal. (wieschollek2024anewtype pages 1-2)

## DOI-first bibliography (with URLs and publication dates)
1. Kerfeld CA, Aussignargues C, Zarzycki J, Cai F, Sutter M. **Bacterial microcompartments**. *Nature Reviews Microbiology*. **Mar 2018**. DOI: **10.1038/nrmicro.2018.10**. URL: https://doi.org/10.1038/nrmicro.2018.10 (kerfeld2018bacterialmicrocompartments pages 1-2, kerfeld2018bacterialmicrocompartments pages 2-3, kerfeld2018bacterialmicrocompartments pages 4-5, kerfeld2018bacterialmicrocompartments media d626e058)
2. Ni T, Jiang Q, Ng PC, et al. **Intrinsically disordered CsoS2 acts as a general molecular thread for α-carboxysome shell assembly**. *Nature Communications*. **Sep 2023**. DOI: **10.1038/s41467-023-41211-y**. URL: https://doi.org/10.1038/s41467-023-41211-y (ni2023intrinsicallydisorderedcsos2 pages 3-5, ni2023intrinsicallydisorderedcsos2 pages 7-8)
3. Doron L, Kerfeld CA. **Bacterial microcompartments as a next-generation metabolic engineering tool**. *Biochemical Society Transactions*. **May 2024**. DOI: **10.1042/bst20230229**. URL: https://doi.org/10.1042/bst20230229 (doron2024bacterialmicrocompartmentsas pages 1-3, doron2024bacterialmicrocompartmentsas pages 5-7, doron2024bacterialmicrocompartmentsas pages 7-8)
4. Li T, Chang P, Chen W, et al. **Nanoengineering Carboxysome Shells for Protein Cages with Programmable Cargo Targeting**. *ACS Nano*. **Feb 2024**. DOI: **10.1021/acsnano.3c11559**. URL: https://doi.org/10.1021/acsnano.3c11559 (li2024nanoengineeringcarboxysomeshells pages 1-3)
5. Trettel DS, Pacheco SL, Laskie AK, et al. **Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation**. *Frontiers in Plant Science*. **Feb 2024**. DOI: **10.3389/fpls.2024.1346759**. URL: https://doi.org/10.3389/fpls.2024.1346759 (trettel2024modelingbacterialmicrocompartment pages 2-3, trettel2024modelingbacterialmicrocompartment pages 5-6)
6. Doron L, Raval D, Kerfeld CA. **Towards using bacterial microcompartments as a platform for spatial metabolic engineering in Zymomonas mobilis**. *Frontiers in Bioengineering and Biotechnology*. **Jan 2024**. DOI: **10.3389/fbioe.2024.1344260**. URL: https://doi.org/10.3389/fbioe.2024.1344260 (doron2024towardsusingbacterial pages 5-6)
7. Cheng J, Li C-Y, Meng M, et al. **Molecular interactions of the chaperone CcmS and carboxysome shell protein CcmK1 that mediate β-carboxysome assembly**. *Plant Physiology*. **Aug 2024**. DOI: **10.1093/plphys/kiae438**. URL: https://doi.org/10.1093/plphys/kiae438 (cheng2024molecularinteractionsof pages 3-5, cheng2024molecularinteractionsof pages 1-2)
8. Wieschollek J, Fuller D, Gahramanova A, et al. **A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments**. *Applied and Environmental Microbiology*. **Sep 2024**. DOI: **10.1128/aem.01075-24**. URL: https://doi.org/10.1128/aem.01075-24 (wieschollek2024anewtype pages 1-2)


References

1. (kerfeld2018bacterialmicrocompartments pages 1-2): C. Kerfeld, Clément Aussignargues, J. Zarzycki, Fei Cai, and M. Sutter. Bacterial microcompartments. Nature Reviews Microbiology, 16:277-290, Mar 2018. URL: https://doi.org/10.1038/nrmicro.2018.10, doi:10.1038/nrmicro.2018.10. This article has 515 citations and is from a highest quality peer-reviewed journal.

2. (kerfeld2018bacterialmicrocompartments pages 2-3): C. Kerfeld, Clément Aussignargues, J. Zarzycki, Fei Cai, and M. Sutter. Bacterial microcompartments. Nature Reviews Microbiology, 16:277-290, Mar 2018. URL: https://doi.org/10.1038/nrmicro.2018.10, doi:10.1038/nrmicro.2018.10. This article has 515 citations and is from a highest quality peer-reviewed journal.

3. (wieschollek2024anewtype pages 1-2): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

4. (cheng2024molecularinteractionsof pages 1-2): Jin Cheng, Chun-Yang Li, Meng Meng, Jian-Xun Li, Shu-Jun Liu, Hai-Yan Cao, Ning Wang, Yu-Zhong Zhang, and Lu-Ning Liu. Molecular interactions of the chaperone ccms and carboxysome shell protein ccmk1 that mediate β-carboxysome assembly. Plant Physiology, 196:1778-1787, Aug 2024. URL: https://doi.org/10.1093/plphys/kiae438, doi:10.1093/plphys/kiae438. This article has 9 citations and is from a highest quality peer-reviewed journal.

5. (trettel2024modelingbacterialmicrocompartment pages 2-3): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 8 citations.

6. (kerfeld2018bacterialmicrocompartments pages 4-5): C. Kerfeld, Clément Aussignargues, J. Zarzycki, Fei Cai, and M. Sutter. Bacterial microcompartments. Nature Reviews Microbiology, 16:277-290, Mar 2018. URL: https://doi.org/10.1038/nrmicro.2018.10, doi:10.1038/nrmicro.2018.10. This article has 515 citations and is from a highest quality peer-reviewed journal.

7. (cheng2024molecularinteractionsof pages 3-5): Jin Cheng, Chun-Yang Li, Meng Meng, Jian-Xun Li, Shu-Jun Liu, Hai-Yan Cao, Ning Wang, Yu-Zhong Zhang, and Lu-Ning Liu. Molecular interactions of the chaperone ccms and carboxysome shell protein ccmk1 that mediate β-carboxysome assembly. Plant Physiology, 196:1778-1787, Aug 2024. URL: https://doi.org/10.1093/plphys/kiae438, doi:10.1093/plphys/kiae438. This article has 9 citations and is from a highest quality peer-reviewed journal.

8. (kerfeld2018bacterialmicrocompartments media d626e058): C. Kerfeld, Clément Aussignargues, J. Zarzycki, Fei Cai, and M. Sutter. Bacterial microcompartments. Nature Reviews Microbiology, 16:277-290, Mar 2018. URL: https://doi.org/10.1038/nrmicro.2018.10, doi:10.1038/nrmicro.2018.10. This article has 515 citations and is from a highest quality peer-reviewed journal.

9. (kerfeld2018bacterialmicrocompartments media 32458108): C. Kerfeld, Clément Aussignargues, J. Zarzycki, Fei Cai, and M. Sutter. Bacterial microcompartments. Nature Reviews Microbiology, 16:277-290, Mar 2018. URL: https://doi.org/10.1038/nrmicro.2018.10, doi:10.1038/nrmicro.2018.10. This article has 515 citations and is from a highest quality peer-reviewed journal.

10. (ni2023intrinsicallydisorderedcsos2 pages 3-5): Tao Ni, Qiuyao Jiang, Pei Cing Ng, Juan Shen, Hao Dou, Yanan Zhu, Julika Radecke, Gregory F. Dykes, Fang Huang, Lu-Ning Liu, and Peijun Zhang. Intrinsically disordered csos2 acts as a general molecular thread for α-carboxysome shell assembly. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41211-y, doi:10.1038/s41467-023-41211-y. This article has 53 citations and is from a highest quality peer-reviewed journal.

11. (ni2023intrinsicallydisorderedcsos2 pages 7-8): Tao Ni, Qiuyao Jiang, Pei Cing Ng, Juan Shen, Hao Dou, Yanan Zhu, Julika Radecke, Gregory F. Dykes, Fang Huang, Lu-Ning Liu, and Peijun Zhang. Intrinsically disordered csos2 acts as a general molecular thread for α-carboxysome shell assembly. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41211-y, doi:10.1038/s41467-023-41211-y. This article has 53 citations and is from a highest quality peer-reviewed journal.

12. (trettel2024modelingbacterialmicrocompartment pages 5-6): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 8 citations.

13. (li2024nanoengineeringcarboxysomeshells pages 1-3): Tianpei Li, Ping Chang, Weixian Chen, Zhaoyang Shi, Chunling Xue, Gregory F. Dykes, Fang Huang, Qiang Wang, and Lu-Ning Liu. Nanoengineering carboxysome shells for protein cages with programmable cargo targeting. ACS Nano, 18:7473-7484, Feb 2024. URL: https://doi.org/10.1021/acsnano.3c11559, doi:10.1021/acsnano.3c11559. This article has 31 citations and is from a highest quality peer-reviewed journal.

14. (doron2024bacterialmicrocompartmentsas pages 7-8): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

15. (doron2024bacterialmicrocompartmentsas pages 5-7): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

16. (doron2024towardsusingbacterial pages 5-6): Lior Doron, Dhairya Raval, and Cheryl A. Kerfeld. Towards using bacterial microcompartments as a platform for spatial metabolic engineering in the industrially important and metabolically versatile zymomonas mobilis. Frontiers in Bioengineering and Biotechnology, Jan 2024. URL: https://doi.org/10.3389/fbioe.2024.1344260, doi:10.3389/fbioe.2024.1344260. This article has 11 citations.

17. (doron2024bacterialmicrocompartmentsas pages 1-3): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

18. (doron2024bacterialmicrocompartmentsas pages 10-12): Lior Doron and Cheryl A. Kerfeld. Bacterial microcompartments as a next-generation metabolic engineering tool: utilizing nature's solution for confining challenging catabolic pathways. Biochemical Society Transactions, 52:997-1010, May 2024. URL: https://doi.org/10.1042/bst20230229, doi:10.1042/bst20230229. This article has 22 citations and is from a peer-reviewed journal.

19. (cheng2024molecularinteractionsof pages 10-10): Jin Cheng, Chun-Yang Li, Meng Meng, Jian-Xun Li, Shu-Jun Liu, Hai-Yan Cao, Ning Wang, Yu-Zhong Zhang, and Lu-Ning Liu. Molecular interactions of the chaperone ccms and carboxysome shell protein ccmk1 that mediate β-carboxysome assembly. Plant Physiology, 196:1778-1787, Aug 2024. URL: https://doi.org/10.1093/plphys/kiae438, doi:10.1093/plphys/kiae438. This article has 9 citations and is from a highest quality peer-reviewed journal.