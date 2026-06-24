---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:29:47.459747'
end_time: '2026-06-18T00:39:36.528962'
duration_seconds: 589.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum mid1
  trait_identifier: METPO:1000456
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH between approximately
    6 and 7, corresponding to neutrophilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Neutrophile, pHO_6_to_7
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic
    pH homeostasis operates with minimal load.)'
  causal_graph_summary: 'ph_optimum_mid1_neutrophile_setpoint: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum mid1
- **METPO identifier:** METPO:1000456
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 6 and 7, corresponding to neutrophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Neutrophile, pHO_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic pH homeostasis operates with minimal load.)
- **Existing causal graph summary:** ph_optimum_mid1_neutrophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid1.yaml`.

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
- **Trait label:** pH optimum mid1
- **METPO identifier:** METPO:1000456
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 6 and 7, corresponding to neutrophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Neutrophile, pHO_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic pH homeostasis operates with minimal load.)
- **Existing causal graph summary:** ph_optimum_mid1_neutrophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid1.yaml`.

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


## Microbial Trait Causal Graph Curation Report: pH optimum mid1 (METPO:1000456)

### 0. Trait summary (scope)
**Trait:** *pH optimum mid1* (METPO:1000456) denotes a **neutrophilic growth optimum**, i.e., best growth at **external pH approximately 6–7** (near-neutral). This should be curated as an **optimum (peak growth rate/fitness)**, not merely a capacity to survive outside that range.

**Key boundary distinctions**
- **Optimum vs tolerance:** A strain can tolerate pH outside its optimum; therefore genes enabling survival at very low pH should not be treated as defining the optimum trait. For example, *Staphylococcus aureus* grew similarly at **pH 5.5 and pH 7.3**, but growth was substantially reduced at **pH 4.5**, indicating that the extreme-acid response is a boundary/tolerance regime rather than “the” optimum phenotype (beetham2024histidinetransportis pages 2-3).
- **Assay dependence (buffering confounder):** Buffered media can mask biologically generated pH shifts. In minimally buffered conditions, *Bacillus subtilis* biofilms exhibit a clear acidification→alkalinization program and **actively condition extracellular pH toward a preferred neutrophile range**, which may be missed in conventional buffered biofilm media (tran2024activephregulation pages 5-7).

### 1. Current mechanistic understanding (key concepts & definitions)
Neutrophilic pH optimum emerges when **external pH and intracellular pH homeostasis** align to minimize energetic and macromolecular stress. Mechanistically, organisms (or communities such as biofilms) deploy **(i) metabolic proton-consuming or proton-producing pathways**, **(ii) proton/ion transporters**, and **(iii) envelope-level controls over proton permeability** to keep cytosolic processes compatible with growth.

Two conceptually distinct (but not mutually exclusive) mechanisms relevant to neutrophiles:
1. **Cell-intrinsic cytoplasmic pH homeostasis**: cells counter external acid/alkali via proton export (e.g., F0F1-ATPase), proton-consuming reactions (amino acid decarboxylation; NH3/NH4+ chemistry), and decreased proton permeability of the envelope (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3).
2. **Community/extracellular pH conditioning**: biofilms can actively regulate extracellular pH through metabolic routing to restore near-neutral conditions, effectively shifting the local microenvironment toward the neutrophilic optimum (tran2024activephregulation pages 5-7, tran2024activephregulation media 32cc027f, tran2024activephregulation media b964d018).

### 2. Recent developments and latest research (priority 2023–2024)
#### 2.1 Active extracellular pH regulation in neutrophile-range biofilms (mBio 2024)
Tran et al. (mBio, 2024) demonstrated that *B. subtilis* biofilms grown in minimally buffered media can **modulate extracellular pH** into a preferred neutrophile range via a **metabolic “division of labor”**:
- **Acetate production** drives acidification.
- **Acetoin biosynthesis (AlsS → AlsD)** drives alkalinization, and critically **each enzymatic step consumes a proton**, providing a mechanistic basis for pH increase (tran2024activephregulation pages 5-7).

Quantitative, curation-relevant data:
- Starting from **pH 6**, alkalinization proceeded at **~0.03 pH units/hour** over **36.6 ± 0.4 h** (tran2024activephregulation pages 5-7).
- A double mutant **ΔackAΔacsA** reduced the acidification rate by **~48%** vs wild type, supporting acetate overflow as a causal acidifying process (tran2024activephregulation pages 5-7).

Genetic causality:
- **ΔalsS or ΔalsD** biofilms retained the acidification phase but **lost alkalinization**, supporting acetoin-pathway necessity for restoring pH (tran2024activephregulation pages 5-7).
- **AlsS overexpression** accelerated return to the neutrophile range (tran2024activephregulation pages 5-7).

**Visual evidence:** the pH-vs-time dynamics and the acetate/acetoin schematic are captured in cropped figure regions (tran2024activephregulation media 32cc027f, tran2024activephregulation media b964d018).

#### 2.2 Chemical modulation of biofilm pH stress adaptability via polyamines (AEM 2024)
Jiang et al. (Applied and Environmental Microbiology, 2024) studied activated-sludge biofilms and showed that **exogenous putrescine** alters pH-stress adaptability in a pH-dependent fashion.

Mechanistic anchors for causal graph curation:
- Putrescine acts as a **proton acceptor**; its protonation decreases with increasing pH, affecting its adsorption and intracellular effects (jiang2024exogenousputrescineplays pages 6-9).
- Under acidic conditions, putrescine promoted **glutamate decarboxylase (GAD) expression** and **GABA pathway** activity (a proton-consuming acid resistance strategy) (jiang2024exogenousputrescineplays pages 6-9).
- Putrescine metabolism generated **NH3**, which binds intracellular **H+ to form NH4+**, a direct chemical buffering mechanism (jiang2024exogenousputrescineplays pages 6-9).

Quantitative biofilm-matrix evidence:
- EPS macromolecules increased under acidic conditions: “PN and PS … increased by **99% and 54%** … under acidic conditions compared with control” (jiang2024exogenousputrescineplays pages 6-9).
- Intracellular H+ decreases were reported (e.g., “intracellular H+ concentration decreased by **74%, 68%, and 32%** …” across conditions) (jiang2024exogenousputrescineplays pages 6-9).

These results support **nodes for polyamines, EPS, decarboxylation, and NH3/NH4+ buffering** as part of pH-regulation machinery adjacent to neutrophilic optimum behavior.

#### 2.3 Gene-level determinants of low pH growth and cytosolic pH maintenance (PLOS Pathogens 2024)
Beetham et al. (PLOS Pathogens, 2024) used genome-scale genetics (Tn-Seq) to identify *S. aureus* genes required for growth at **pH 4.5**, highlighting mechanisms relevant to pH homeostasis and boundary conditions.

Mechanisms directly described:
- **Envelope charge/permeability modulation:** D-alanylation of teichoic acids via the **dlt operon** is implicated in reducing proton permeability and supporting low-pH growth (beetham2024histidinetransportis pages 1-2).
- **Proton pumping:** active proton export via **F0F1-ATPase** (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3).
- **Proton-consuming metabolism:** amino acid decarboxylation (glutamate/lysine/arginine) (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3).
- **Ammonia-based buffering:** **urease** and **arginine deaminase** pathways generate NH3 that consumes H+ when protonated to NH4+ (beetham2024histidinetransportis pages 2-3).

New mechanistic link:
- A gene encoding a previously uncharacterized **histidine transporter (SAUSA300_0846)** was among the most important genes for growth at pH 4.5. Mutants were “unable to maintain [their] cytosolic pH to the same extent as a WT strain,” supporting histidine transport as a causal contributor to intracellular pH maintenance under acid stress (beetham2024histidinetransportis pages 1-2).

### 3. Current applications and real-world implementations
1. **Biofilm control in minimally buffered (natural/industrial) settings:** Demonstrating that biofilms can actively regulate extracellular pH suggests intervention points—e.g., targeting acetoin biosynthesis genes (alsS/alsD) or overflow metabolism—to control unwanted biofilm growth outside buffered lab conditions (tran2024activephregulation pages 5-7).
2. **Wastewater and engineered biofilms:** Putrescine’s pH-dependent “switch-like” behavior suggests that polyamines could be operational levers to shift biofilm stability under acid vs alkaline conditions in engineered systems (activated sludge), by modulating GAD/GABA and ATPase-linked pH homeostasis (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 6-9).
3. **Pathogen persistence in acidic niches:** Mechanisms such as F0F1-ATPase proton export, amino-acid decarboxylation, urease/ADI ammonia production, and envelope D-alanylation are implicated in pathogen growth/survival at low pH (skin, phagosomes). While this is not identical to a neutrophilic optimum trait, it defines neighboring mechanisms relevant for boundary-case curation (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3).

### 4. Expert opinions / authoritative synthesis (2023–2025)
A recent peer-reviewed review on probiotic stress resistance summarized that maintaining cytosolic pH (or ΔpH) is **energetically costly** and tightly connected to essential growth processes (ATP synthesis, DNA replication, transcription, translation). It emphasizes upregulation of **F0F1-ATPase/H+-ATPase** and related strategies as central responses during acid stress, consistent with the mechanistic nodes identified above (bustos2025recentadvancesin pages 8-9).

Additionally, a 2023 peer-reviewed source surveying genomic/physiological adaptation mechanisms highlights canonical **Na+/H+ antiporters (e.g., NhaA)** and **Mrp/Mnh family antiporters**, plus alternative Na+- or H+-coupled ATPases, as key candidate modules for ion and pH homeostasis (liu2023isolationandgenomics pages 20-20). For pH optimum mid1 curation, these are strong **candidate nodes**, but direct linkage to “optimum at 6–7” should be treated as *inferred* unless supported by strain-level phenotype assays.

### 5. Candidate nodes for TraitMech causal graph (grouped)

#### 5.1 Pathways / modules
- **Acetoin biosynthesis** (AlsS → AlsD); proton-consuming alkalinization module (tran2024activephregulation pages 5-7, tran2024activephregulation media b964d018)
- **Acetate overflow metabolism** (AckA/AcsA) as acidification driver (tran2024activephregulation pages 5-7, tran2024activephregulation media b964d018)
- **Glutamate decarboxylase (GAD) / GABA pathway** (proton consuming) (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 6-9)
- **Amino-acid decarboxylation systems** (glutamate/lysine/arginine) (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3)
- **Urease** and/or **arginine deaminase (ADI)** ammonia-producing alkalinization/buffering modules (beetham2024histidinetransportis pages 2-3)

#### 5.2 Genes / proteins / complexes
- **alsS** (EC 2.2.1.6 acetolactate synthase); **alsD** (EC 4.1.1.5 acetolactate decarboxylase) (tran2024activephregulation pages 5-7)
- **ackA / acsA** (acetate-linked acidification; genetic evidence) (tran2024activephregulation pages 5-7)
- **F0F1-ATPase / H+-ATPase** (proton export; energy coupling) (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3)
- **Histidine transporter SAUSA300_0846** (supports cytosolic pH maintenance at low pH) (beetham2024histidinetransportis pages 1-2)
- **dlt operon** (teichoic-acid D-alanylation; reduced proton permeability) (beetham2024histidinetransportis pages 1-2)
- **Na+/H+ antiporters NhaA** (candidate); **Mrp/Mnh antiporter complex** (candidate) (liu2023isolationandgenomics pages 20-20)

#### 5.3 Chemicals / metabolites
- **H+** (CHEBI:15378)
- **Acetate** (CHEBI:30089)
- **Acetoin** (contextual product; alkalinization mechanism is pathway proton consumption) (tran2024activephregulation pages 5-7)
- **Putrescine** (CHEBI:17148)
- **GABA** (CHEBI:16865)
- **NH3 / NH4+** (CHEBI:16134 / CHEBI:28938) (jiang2024exogenousputrescineplays pages 6-9)

#### 5.4 Environmental / experimental factors
- **External pH** (starting pH, pH gradients)
- **Buffer capacity** of medium (minimally buffered vs buffered) (tran2024activephregulation pages 5-7)
- **Biofilm vs planktonic growth mode** (biofilms can condition pH) (tran2024activephregulation pages 5-7)

### 6. Evidence-backed candidate causal edges (curation table)
The following artifact is a curation-oriented table of subject–predicate–object edges with snippets, identifiers where possible, and curation notes.

| Edge (subject–predicate–object) | Node type(s) | Suggested identifiers | Evidence (short snippet/quote) | Source (DOI, year, URL) | Curation notes |
|---|---|---|---|---|---|
| acetoin biosynthesis pathway — consumes — H+ | pathway → chemical | Acetoin biosynthesis pathway; CHEBI:15378 (H+) | “the acetoin biosynthesis pathway (AlsS → AlsD). Each enzymatic step consumes a proton” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Strong but assay-specific to *Bacillus subtilis* biofilms in minimally buffered medium. |
| acetoin biosynthesis pathway — raises — extracellular pH | pathway → environmental factor | GO:0006086 (acetyl-CoA metabolic process, broad); CHEBI:15378 (H+) | “drives alkalinization” and biofilms “condition local pH into a preferred neutrophile range” (tran2024activephregulation pages 5-7, tran2024activephregulation media 32cc027f) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Good candidate edge for community-level pH regulation; taxon/biofilm specific. |
| extracellular pH ~6 start — increases duration/rate of alkalinization toward neutrophile range — biofilm pH regulation program | environmental factor → process | ENVO:09200014 (pH, if using ENVO label only uncertain) | “starting at pH 6, alkalinization proceeds at ~0.03 pH/h over 36.6 ± 0.4 h” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Quantitative support for recovery into preferred range; assay-specific. |
| acetate/overflow metabolism — acidifies — extracellular environment | pathway → environmental factor | acetate: CHEBI:30089 | “Acetate production … is a major source of biofilm-associated acidification” and ΔackAΔacsA “reduces acidification rate by ~48%” (tran2024activephregulation pages 5-7, tran2024activephregulation media 32cc027f) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Strong in *B. subtilis* biofilms; may generalize to overflow metabolism but curate cautiously. |
| alsS loss-of-function — abolishes — alkalinization phase | gene/protein → process | alsS; EC 2.2.1.6 (acetolactate synthase) | “mutants lacking alsS or alsD retain the acidification phase but completely lose the alkalinization phase” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Strong, direct genetics; taxon-specific. |
| alsD loss-of-function — abolishes — alkalinization phase | gene/protein → process | alsD; EC 4.1.1.5 (alpha-acetolactate decarboxylase) | “mutants lacking alsS or alsD retain the acidification phase but completely lose the alkalinization phase” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Strong, direct genetics; taxon-specific. |
| alsS overexpression — accelerates return to — neutrophile-range extracellular pH | gene/protein → trait-relevant environment | alsS; EC 2.2.1.6 | “Overexpression of AlsS accelerates return to the neutrophile range” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Very useful positive causal edge; biofilm/assay-specific. |
| failure of acetoin-pathway alkalinization (e.g., ΔalsS) — decreases — CFU / biofilm fitness in minimally buffered conditions | process/gene → phenotype |  | “∆alsS mutants fail to maintain local pH… and show significantly lower CFU in minimally buffered conditions” (tran2024activephregulation pages 5-7) | 10.1128/mbio.03387-23, 2024, https://doi.org/10.1128/mbio.03387-23 | Connects pH conditioning to growth; strong but biofilm-specific. |
| exogenous putrescine — increases — glutamate decarboxylase / GABA pathway activity | chemical → pathway | putrescine: CHEBI:17148; glutamate decarboxylase: EC 4.1.1.15; GABA: CHEBI:16865 | “putrescine could enhance the expression of glutamate decarboxylase” and “GABA as a key intermediate” (jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Strong within activated-sludge biofilm system; conditional on acidic context. |
| glutamate decarboxylation / GABA pathway — consumes — intracellular H+ | pathway → chemical | EC 4.1.1.15; CHEBI:15378 (H+) | “glutamate-based systems and the GABA metabolic pathway … consume H+” (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Mechanistically plausible and supported; community/biofilm study, not single-isolate genetics. |
| exogenous putrescine — increases expression of — ATPase / H+ transmembrane transport | chemical → protein complex/process | F-type ATPase; GO:0015991 (ATP hydrolysis coupled proton transport) | “putrescine stimulated ATPase expression, allowing for better utilization of energy in H+ transmembrane transport” (jiang2024exogenousputrescineplays pages 1-2) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Useful but indirect; ATPase subunit not grounded in this excerpt. |
| protonated putrescine — adsorbs to — EPS | chemical → biofilm matrix | putrescine: CHEBI:17148 | “The negatively charged nucleic acids and PN within the EPS strongly adsorb to protonated putrescine” (jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Physicochemical edge relevant to extracellular buffering; community-specific. |
| lower external pH — increases protonation of — putrescine | environmental factor → chemical state | putrescine: CHEBI:17148 | “The protonation degree of putrescine decreases with increasing pH” (jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Environmental chemistry edge; useful context node for assay effects. |
| putrescine oxidative metabolism — produces — NH3 | pathway → chemical | putrescine: CHEBI:17148; ammonia: CHEBI:16134 | “generated NH3” during putrescine metabolism (jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Mechanistic but pathway enzymes not fully specified here. |
| NH3 — binds — H+ forming NH4+ | chemical → chemical | ammonia: CHEBI:16134; H+: CHEBI:15378; ammonium: CHEBI:28938 | “generated NH3 bind with intracellular free H+ to form NH4+” (jiang2024exogenousputrescineplays pages 6-9) | 10.1128/aem.00569-24, 2024, https://doi.org/10.1128/aem.00569-24 | Direct acid-buffering chemistry; generalizable. |
| dlt operon-mediated D-alanylation of teichoic acids — reduces — cell envelope proton permeability | gene cluster/process → cellular property | dlt operon; GO:1902600 (proton transmembrane transport, related broad) | “reducing membrane/cell-wall proton permeability (e.g., D-alanylation of teichoic acids via the dlt operon)” (beetham2024histidinetransportis pages 1-2) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Strong for *Staphylococcus aureus* acid stress; relevant boundary mechanism, not specific to pH 6–7 optimum. |
| F0F1-ATPase — exports — H+ | protein complex → chemical | F-type ATPase; GO:0015991 | “actively exporting protons via proton pumps such as the F0F1-ATPase” (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Classic pH-homeostasis edge; strong but from acid-stress context. |
| amino-acid decarboxylation pathways — consume — H+ | pathway → chemical | glutamate decarboxylase EC 4.1.1.15; lysine decarboxylase EC 4.1.1.18; arginine decarboxylase EC 4.1.1.19 | “consume protons through amino-acid decarboxylation pathways (glutamate, lysine, arginine)” (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Good general acid-resistance edge; not specific to neutrophile optimum itself. |
| histidine transporter SAUSA300_0846 — supports maintenance of — cytosolic pH | transporter → physiological state | SAUSA300_0846 (uncharacterized histidine transporter) | mutant “is… unable to maintain its cytosolic pH to the same extent as a WT strain” (beetham2024histidinetransportis pages 1-2) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Strong, gene-linked; species-specific and acid-stress-specific. |
| histidine transporter SAUSA300_0846 — required for growth at — pH 4.5 | transporter → phenotype/environment | SAUSA300_0846 | “Histidine transport is essential for the growth of S. aureus at low pH” and genes were required for growth at “pH 4.5” (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Strong but boundary-case evidence outside pH-optimum-mid1 range; useful as neighboring-trait mechanism. |
| external pH 5.5 vs 7.3 — has similar growth effect on — S. aureus | environmental factor → phenotype |  | “growth at pH 5.5 was similar to pH 7.3, whereas pH 4.5 significantly reduced growth” (beetham2024histidinetransportis pages 2-3) | 10.1371/journal.ppat.1011927, 2024, https://doi.org/10.1371/journal.ppat.1011927 | Helpful boundary evidence distinguishing tolerance from optimum; species-specific. |
| Na+/H+ antiporter NhaA — contributes to — cytoplasmic pH control | transporter → process | NhaA; KEGG K03313 (candidate) | “NhaA from E. coli as a model pH-regulated Na+/H+ antiporter” (liu2023isolationandgenomics pages 20-20) | 10.1128/spectrum.04110-22, 2023, https://doi.org/10.1128/spectrum.04110-22 | Mechanistic candidate only; inferred/general, not direct evidence for trait pH optimum mid1. |
| Mrp/Mnh antiporter complex — contributes to — Na+/H+ exchange and pH homeostasis | transporter complex → process | Mrp/Mnh antiporter complex | “Mrp-family antiporters” contribute to maintaining “cytoplasmic pH and ion balance” (liu2023isolationandgenomics pages 20-20) | 10.1128/spectrum.04110-22, 2023, https://doi.org/10.1128/spectrum.04110-22 | Candidate node/edge for graph expansion; general/inferred and not yet trait-specific enough for curation. |


*Table: This table compiles evidence-backed candidate causal edges relevant to the pH optimum mid1 trait, emphasizing mechanisms that help microbes maintain or restore near-neutral external and internal pH. It is useful as a curation-ready starting point for selecting TraitMech nodes and filtering strong versus tentative edges.*

### 7. Statistics & data highlights (recent studies)
- *B. subtilis* biofilm starting at **pH 6**: alkalinization rate **~0.03 pH/h** over **36.6 ± 0.4 h** (tran2024activephregulation pages 5-7).
- *B. subtilis* ΔackAΔacsA: **~48% reduction** in acidification rate vs wild type (tran2024activephregulation pages 5-7).
- Activated-sludge biofilms under acidic conditions: EPS “PN and PS … increased by **99% and 54%** …” (jiang2024exogenousputrescineplays pages 6-9).
- Activated-sludge biofilms: intracellular H+ concentration decreased by up to **74%** under tested conditions (jiang2024exogenousputrescineplays pages 6-9).
- *S. aureus*: growth at **pH 5.5** similar to **pH 7.3**, but **pH 4.5** substantially reduces growth (beetham2024histidinetransportis pages 2-3).

### 8. Warnings / non-curatable (yet) claims
1. **Na+/H+ antiporters (NhaA) and Mrp/Mnh complexes** are well-motivated candidate nodes for pH homeostasis, but the currently extracted evidence is **general** and does not directly demonstrate that they *set* the neutrophilic optimum at pH 6–7 in a specific strain. These should be included as **candidate/inferred edges** pending trait-matched phenotyping evidence (liu2023isolationandgenomics pages 20-20).
2. **Extreme-acid survival mechanisms (pH ~4.5)** (e.g., histidine transport dependency in *S. aureus*) are important for boundary setting but should be curated carefully so as not to redefine “pH optimum mid1” into an “acid tolerance” trait (beetham2024histidinetransportis pages 1-2, beetham2024histidinetransportis pages 2-3).
3. **Community-level activated sludge findings** (putrescine effects) may be **assay- and community-specific**; causal edges should be marked uncertain unless replicated in isolate genetics or mechanistic biochemistry (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 6-9).

---

## DOI-first bibliography (with publication dates and URLs)
1. **Tran P, Lander SM, Prindle A.** Active pH regulation facilitates *Bacillus subtilis* biofilm development in a minimally buffered environment. *mBio*. **2024-03**. DOI: **10.1128/mbio.03387-23**. URL: https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 5-7)
2. **Jiang G, Wang C, Wang Y, et al.** Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge. *Applied and Environmental Microbiology*. **2024-07**. DOI: **10.1128/aem.00569-24**. URL: https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2)
3. **Beetham CM, Schuster CF, Kviatkovski I, et al.** Histidine transport is essential for the growth of *Staphylococcus aureus* at low pH. *PLOS Pathogens*. **2024-01**. DOI: **10.1371/journal.ppat.1011927**. URL: https://doi.org/10.1371/journal.ppat.1011927 (beetham2024histidinetransportis pages 1-2)
4. **Liu L, Huang W-C, Pan J, et al.** Isolation and genomics of *Futiania mangrovii* gen. nov., sp. nov., a rare and metabolically versatile member in the class *Alphaproteobacteria*. *Microbiology Spectrum*. **2023-02**. DOI: **10.1128/spectrum.04110-22**. URL: https://doi.org/10.1128/spectrum.04110-22 (liu2023isolationandgenomics pages 20-20)
5. **Bustos AY, Taranto MP, Gerez CL, et al.** Recent advances in the understanding of stress resistance mechanisms in probiotics: relevance for the design of functional food systems. *Probiotics and Antimicrobial Proteins*. **2025-06**. DOI: **10.1007/s12602-024-10273-9**. URL: https://doi.org/10.1007/s12602-024-10273-9 (bustos2025recentadvancesin pages 8-9)


References

1. (beetham2024histidinetransportis pages 2-3): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

2. (tran2024activephregulation pages 5-7): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (beetham2024histidinetransportis pages 1-2): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

4. (tran2024activephregulation media 32cc027f): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (tran2024activephregulation media b964d018): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

6. (jiang2024exogenousputrescineplays pages 6-9): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

7. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

8. (bustos2025recentadvancesin pages 8-9): Ana Yanina Bustos, María Pía Taranto, Carla Luciana Gerez, Sofia Agriopoulou, Slim Smaoui, Theodoros Varzakas, and Hesham Ali El Enshasy. Recent advances in the understanding of stress resistance mechanisms in probiotics: relevance for the design of functional food systems. Probiotics and Antimicrobial Proteins, 17:138-158, Jun 2025. URL: https://doi.org/10.1007/s12602-024-10273-9, doi:10.1007/s12602-024-10273-9. This article has 101 citations and is from a peer-reviewed journal.

9. (liu2023isolationandgenomics pages 20-20): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.