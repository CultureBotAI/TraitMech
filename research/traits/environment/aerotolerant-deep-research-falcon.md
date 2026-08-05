---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:57:59.934445'
end_time: '2026-08-04T00:06:24.062320'
duration_seconds: 504.13
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: aerotolerant
  trait_identifier: METPO:1000609
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: aerotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that does not use O\u2082 for growth but tolerates\
    \ its presence."
  parent_traits: METPO:1000601
  synonyms: aerotolerant anaerobe
  evidence_summary: 'https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements:
    they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance
    without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant
    and survives limited oxygen exposure (Organism example: Clostridium perfringens
    is described as aerotolerant.)'
  causal_graph_summary: 'aerotolerant_anaerobe_ros_defense: 11 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** aerotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000609
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that does not use O₂ for growth but tolerates its presence.
- **Parent traits:** METPO:1000601
- **Synonyms:** aerotolerant anaerobe
- **Existing evidence:** https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements: they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant and survives limited oxygen exposure (Organism example: Clostridium perfringens is described as aerotolerant.)
- **Existing causal graph summary:** aerotolerant_anaerobe_ros_defense: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **aerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerotolerant.yaml`.

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
- **Trait label:** aerotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000609
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that does not use O₂ for growth but tolerates its presence.
- **Parent traits:** METPO:1000601
- **Synonyms:** aerotolerant anaerobe
- **Existing evidence:** https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements: they do not utilize it for ATP production (Supports aerotolerance as oxygen tolerance without oxygen use.) | PMID:38864615: this bacterium is relatively aerotolerant and survives limited oxygen exposure (Organism example: Clostridium perfringens is described as aerotolerant.)
- **Existing causal graph summary:** aerotolerant_anaerobe_ros_defense: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **aerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/aerotolerant.yaml`.

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


# Curation report: aerotolerant

**Trait:** aerotolerant  
**Identifier:** **METPO:1000609**  
**Category / kind:** ENVIRONMENT / CLASS  
**Reviewed definition:** an oxygen preference in which the organism does not use O₂ for growth but tolerates its presence.

## 1. Scope and current interpretation

Aerotolerance should be curated primarily as **persistence of viable cells, maintenance or recovery of anaerobic activity, or reversible growth inhibition during oxygen exposure, without evidence that O₂ supports growth**. Bacteroides illustrates the distinction: aeration can stop fermentation, yet metabolism resumes after anoxia is restored. Thus, “no aerobic growth” does not by itself mean rapid oxygen killing. Conventional plating can also confound reversible growth arrest with loss of viability. (imlay2002howoxygendamages pages 25-28, lu2021whenanaerobesencounter pages 22-27, lu2021whenanaerobesencounter pages 8-9)

The phenotype is a **quantitative, assay-dependent spectrum**, not a binary property. Reported tolerance varies with O₂ concentration and exposure time, temperature, medium, inoculum density, aggregation/biofilm state, growth phase, and recovery conditions. For example, planktonic marine *“Candidatus Scalindua”* had an O₂ IC50 of 18.0 µM and an upper activity limit of 51.6 µM, whereas four freshwater anammox taxa had IC50 values of 2.7–4.2 µM and upper limits of 10.9–26.6 µM. High biomass density or shielding by aerobic partners can overestimate intrinsic tolerance. (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 6-7)

### Boundary cases

- **Facultative anaerobe:** can grow using aerobic respiration when O₂ is available and use anaerobic metabolism otherwise. That is outside the narrow METPO definition unless the asserted phenotype specifically concerns survival independent of aerobic growth.
- **Microaerophile:** uses O₂ for growth but prefers sub-atmospheric concentrations. This is mechanistically distinct, although published descriptions sometimes blur the categories; *Fusibacter* WBS was called aerotolerant and “can even be considered as microaerophile,” making it a boundary case rather than an ideal defining exemplar. (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 8-9)
- **Aerobic respiration:** O₂ consumption is not sufficient evidence. In anammox cells, O₂-reduction rates were four orders of magnitude below N₂-production rates, supporting detoxification rather than respiration. (okabe2023oxygentoleranceand pages 6-7)
- **Obligate anaerobe:** the traditional label describes inability to grow aerobically, but includes organisms ranging from rapidly killed to highly oxygen-persistent. Some nominally strict anaerobes therefore express an aerotolerant phenotype under defined assays. (imlay2002howoxygendamages pages 25-28, okabe2023oxygentoleranceand pages 6-7)
- **Oxidant resistance:** resistance to H₂O₂, superoxide generators, or hypochlorous acid is mechanistically relevant but does not alone establish survival in molecular O₂.
- **VBNC state or spore survival:** these should not automatically be equated with vegetative-cell aerotolerance. Campylobacter can enter a viable-but-nonculturable state during oxidative exposure, and assay design must distinguish this from growth or recoverable vegetative survival. (delaporte2024aerotolerancyofcampylobacter pages 5-6)

## 2. Mechanistic model

The strongest general model has four connected modules:

1. **O₂ exposure and toxicity.** O₂ diffuses into cells and can form superoxide and H₂O₂ as reduction by-products. O₂ also directly poisons low-potential enzymes central to anaerobic metabolism. PFOR and PFL are directly inactivated by O₂, whereas fumarase and other iron enzymes can be damaged by endogenous ROS. (okabe2023oxygentoleranceand pages 1-2, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)
2. **O₂ removal.** Flavodiiron/rubredoxin systems and cytochrome bd oxidase can reduce O₂ without necessarily supporting respiration. In *Fusibacter* WBS, washed cells showed menadiol-dependent O₂ reduction of 11 ± 2 nmol O₂ min⁻¹ mg⁻¹ protein alongside `cydAB`. (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
3. **ROS detoxification.** SOD converts superoxide to H₂O₂; catalase, peroxidases, rubrerythrin, and alkyl-hydroperoxide reductase remove peroxides. Anaerobes may instead or additionally use superoxide reductase, avoiding production of O₂ during superoxide removal. Comparative evidence indicates that no single enzyme set is universal. (lu2021whenanaerobesencounter pages 3-4, okabe2023oxygentoleranceand pages 1-2, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
4. **Damage limitation and recovery.** Metal homeostasis, thioredoxin-dependent reduction, repair of oxidized proteins and Fe–S clusters, and re-metallation of damaged enzymes permit recovery after anoxia returns. The recovery branch is biologically important but remains less experimentally resolved than detoxification. (lu2021whenanaerobesencounter pages 13-15, hernandezmorfa2023theoxidativestress pages 8-9, hernandezmorfa2023theoxidativestress pages 5-6, hernandezmorfa2023theoxidativestress pages 3-4)

## 3. Candidate nodes

### Trait and environmental/experimental nodes

- aerotolerant — **METPO:1000609**
- parent trait — **METPO:1000601**
- molecular oxygen — **CHEBI:15379**
- oxygen exposure; dissolved-oxygen concentration; headspace O₂ percentage; exposure duration — label-only assay nodes
- anoxic recovery; reversible oxygen inhibition; viability after oxygen exposure — label-only phenotype/assay nodes
- oxic–anoxic interface, biofilm, cell aggregate, inoculum density, temperature, medium composition, carbon source — label-only contextual nodes
- response to oxidative stress — **GO:0006979**

### Chemicals and metabolites

- superoxide — **CHEBI:18421**
- hydrogen peroxide — **CHEBI:16240**
- hydroxyl radical — **CHEBI:29191**
- manganese(2+) — **CHEBI:29035**
- iron(2+) — **CHEBI:29033**
- cysteine, rhamnose, glucose, menadiol, pyruvate, ferredoxin, NAD(P)H, nitric oxide, glutathione — retain as label-only until exact graph-specific ChEBI mappings are verified

### Enzymes, proteins, and complexes

- superoxide dismutase / SodA or SodB — **GO:0004784**
- catalase / KatA or KatE — **GO:0004096**
- peroxidase activity — **GO:0004601**
- superoxide reductase / desulfoferrodoxin
- rubrerythrin and reverse rubrerythrin
- flavodiiron protein; rubredoxin:oxygen oxidoreductase/ROO/NorV
- cytochrome bd ubiquinol oxidase / CydAB
- alkyl-hydroperoxide reductase / AhpCF
- thiol peroxidase/peroxiredoxin TpxD
- thioredoxin and thioredoxin reductase
- glutathione peroxidase and glutathione reductase
- PFOR, PFL, fumarase, oxygen-sensitive Fe–S enzymes
- iron–sulfur cluster repair/assembly — **GO:0016226** for the general process
- manganese transporter PsaABC; iron transporter PiuBCDA; Dpr iron-storage protein

Exact EC, UniProt, Rhea, KEGG, or MetaCyc identifiers should be assigned only after choosing a taxon and reaction direction. The current evidence does not justify universalizing a taxon-specific protein accession.

### Regulators and community structures

- RhaR and its rhamnose-responsive metabolic program
- PerR, Rex, CosR, CodY, RitR, SifR, SpxR, RggM
- biofilm formation, extracellular polysaccharide/capsule, polymicrobial oxygen shielding

These are candidate auxiliary modules rather than universal aerotolerance determinants.

## 4. Candidate causal edges

The following table separates direct genetic evidence from physiological association, transcriptomic association, and genomic inference.

| subject | predicate | object | organism/context | evidence class | short exact supporting snippet | DOI/year | curation status/uncertainty |
|---|---|---|---|---|---|---|---|
| O2 | generates/byproduct leads to | reactive oxygen species (superoxide, H2O2) | anammox bacteria; general anaerobe context | review synthesis | "when molecular oxygen (O2) diffuses into cells, reactive oxygen species (ROSs), such as superoxide anion (O2∙-) and hydrogen peroxide (H2O2) are generated as oxygen reduction by-products" (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 / 2023 | Curate as broad mechanism; not trait-specific alone |
| O2 | directly inactivates | pyruvate:ferredoxin oxidoreductase (PFOR) | anaerobes including Bacteroides; oxygen exposure | review synthesis | "PFOR and PFL are primarily inactivated directly by molecular oxygen" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Curate with caution as review-level but strong/mechanistically established |
| O2 | directly inactivates | pyruvate-formate lyase (PFL) | anaerobes including Bacteroides; oxygen exposure | review synthesis | "PFOR and PFL are primarily inactivated directly by molecular oxygen" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Curate with caution as review-level but strong/mechanistically established |
| superoxide | inactivates | fumarase | anaerobes including Bacteroides; oxidative stress | review synthesis | "whereas enzymes like fumarase are mainly deactivated by ROS such as O2− and H2O2" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Curate as ROS-damage mechanism; specific ROS assignment partly review-derived |
| Sod activity + Cat activity | supports higher O2 tolerance of | “Ca. Scalindua sp.” | planktonic anammox; IC50 and DOmax measured | biochemical/physiological | "only Scalindua exhibited high Sod activity of 22.6 ± 1.9 U/mg-protein with moderate Cat activity of 1.6 ± 0.7 U/mg-protein... This Sod-Cat dependent detoxification system could be responsible for the higher O2 tolerance" (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 / 2023 | Curate as association/mechanistic candidate; wording "could be responsible" indicates inference |
| “Ca. Scalindua sp.” | has phenotype | higher oxygen tolerance | marine anammox; quantitative assay | biochemical/physiological | "IC50 = 18.0 µM and DOmax = 51.6 µM" and freshwater species had "IC50 = 2.7–4.2 µM and DOmax = 10.9–26.6 µM" (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 / 2023 | Strong phenotype support for aerotolerance spectrum |
| Fusibacter SOD + peroxidase activities | contribute to | relative aerotolerance | Fusibacter sp. strain WBS from oxygenated sediments | biochemical/physiological | "relatively high superoxide dismutase (SOD) (17.4 U mg−1 protein) and moderate peroxidase (3.2 U mg−1 protein) activities"; "SOD and SOR (desulfoferrodoxin) play a major role... contributing to the relative aerotolerance" (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8) | 10.3390/microorganisms11071642 / 2023 | Curate as taxon-specific candidate; partly inferential for causality |
| cydAB / cytochrome d ubiquinol oxidase | enables oxygen reduction/consumption | O2 detoxification | Fusibacter sp. strain WBS; menadiol-dependent washed cells | biochemical/physiological | "based on the detection of cydAB genes... the washed cells... exhibited relatively high O2 reduction activity (11 ± 2 nmol O2 min−1 mg−1 protein), which was dependent of menadiol" (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8) | 10.3390/microorganisms11071642 / 2023 | Curate as candidate edge; enzyme-to-activity link inferred from gene presence + assay |
| RhaR | downregulates | pfor expression | Bacteroides thetaiotaomicron grown on rhamnose | direct genetic | "the expression of the regulator RhaR inhibits the transcription of pfor" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Curate; supported by deletion/overexpression and qPCR |
| RhaR | reduces | cellular ROS / H2O2 production | B. thetaiotaomicron; rhamnose-dependent oxidative tolerance | direct genetic | "In the absence of RhaR, there is no down-regulation of PFOR expression, and consequently, cellular ROS levels remain unaffected" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Curate as direct genetic mechanism in this taxon |
| rhaR deletion | abolishes | tolerance advantage in O2-rich environments | B. thetaiotaomicron ΔrhaR mutant | direct genetic | "The abolishment of rhaR causes B. thetaiotaomicron to forfeit its tolerance advantage in O2-rich environments" (xie2024bacteroidesthetaiotaomicronenhances pages 9-11) | 10.3389/fmicb.2024.1505218 / 2024 | Strong taxon-specific causal evidence |
| Mn2+ uptake via PsaABC(A/D operon context) | supports/cofactor for | SodA-mediated ROS detoxification and peroxide resistance | Streptococcus pneumoniae | review synthesis | "Mn2+... assists in the detoxification of ROS as a critical cofactor for SodA" and "when the psa genes are inactivated... shows increased sensitivity to exogenous H2O2" (hernandezmorfa2023theoxidativestress pages 5-6) | 10.3389/fmicb.2023.1269843 / 2023 | Curate as taxon-specific oxidative-defense mechanism; operon structure details should be checked carefully |
| excess free iron | promotes | Fenton-reaction oxidative stress | S. pneumoniae ritR/codY regulatory context | review synthesis | "higher intracellular concentration of free iron... heightened toxicity resulting from ROS hyperproduction through the Fenton reaction" (hernandezmorfa2023theoxidativestress pages 8-9) | 10.3389/fmicb.2023.1269843 / 2023 | Curate as general oxidative-stress mechanism, not aerotolerance-specific alone |
| TpxD thiol peroxidase | supports survival/growth under | exogenous H2O2 | S. pneumoniae | review synthesis | "the absence of the tpxD gene has been found to negatively impact the survival and growth of S. pneumoniae under these conditions" (hernandezmorfa2023theoxidativestress pages 3-4) | 10.3389/fmicb.2023.1269843 / 2023 | Curate as taxon-specific peroxide-defense edge |
| constitutive/high oxygen-defense gene transcription | associates with | survival under periodic oxic exposure | peatland sulfate reducers in bioreactor; 133 µM O2, 1-week oxic cycles | expression association | "maintained high transcript levels of oxygen defense genes even under anoxic conditions" and this "may be keys adaptation to withstand periodically occurring changes in redox regimes" (dyksma2024growthofsulfatereducing pages 10-12) | 10.1186/s40168-024-01909-7 / 2024 | Association only; community/MAG-level, not direct causation |
| periodic exposure to 133 µM O2 | selects for / is survived by | growing sulfate-reducer populations | peatland bioreactor community | biochemical/physiological | "survived regular exposure to relatively high oxygen concentrations (133 µM O2) and was even enriched in the bioreactor" (dyksma2024growthofsulfatereducing pages 5-6) | 10.1186/s40168-024-01909-7 / 2024 | Strong phenotype/community evidence; not a single-gene edge |


*Table: This table compiles the strongest curation-ready causal edges and closely associated mechanisms for microbial aerotolerance, emphasizing direct genetic and quantitative physiological evidence where available. It is useful for deciding which nodes and edges are strong enough for TraitMech curation and which should remain flagged as inferred or taxon-specific.*

### Recommended minimal TraitMech backbone

A conservative taxon-general graph could begin with these edges:

1. **molecular oxygen → generates as reduction by-products → superoxide and hydrogen peroxide**. This is the initiating ROS branch, although spontaneous ROS flux depends on the organism’s enzyme inventory. (okabe2023oxygentoleranceand pages 1-2)
2. **molecular oxygen → directly inactivates → PFOR/PFL and other oxygen-labile anaerobic enzymes**. (lu2021whenanaerobesencounter pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)
3. **superoxide/H₂O₂ → damages → iron enzymes, Fe–S proteins, and fumarase**. (lu2021whenanaerobesencounter pages 22-27, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)
4. **superoxide dismutase or superoxide reductase → lowers → superoxide burden**. The alternatives should not be forced into every organism. (lu2021whenanaerobesencounter pages 3-4, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
5. **catalase/peroxidase/rubrerythrin → lowers → H₂O₂/peroxide burden**. (botin2023thetoleranceof pages 1-2, okabe2023oxygentoleranceand pages 1-2, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
6. **nonrespiratory O₂ reductase or CydAB → consumes → molecular oxygen**, thereby limiting O₂ penetration and ROS generation; curate as “detoxification” only where low flux or other evidence excludes respiratory growth. (okabe2023oxygentoleranceand pages 6-7, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
7. **reduced ROS and direct O₂ damage → increases → survival and recovery after oxygen exposure → supports METPO:1000609**. This final integration edge is mechanistic synthesis, not a single universal experiment. (lu2021whenanaerobesencounter pages 13-15, okabe2023oxygentoleranceand pages 1-2)

## 5. Strong organism-specific subgraphs

### Marine anammox: *“Ca. Scalindua”*

This is the strongest recent quantitative phenotype. Its IC50 was 18.0 µM O₂ and DOmax 51.6 µM, versus 2.7–4.2 and 10.9–26.6 µM in freshwater comparators. It had SOD activity of 22.6 ± 1.9 U mg⁻¹ protein and catalase activity of 1.6 ± 0.7 U mg⁻¹ protein. After 12 h at ambient-air headspace, recovered anammox activity was 65 ± 36%; after 24 h, activity restarted immediately at approximately the anoxic-control level. The authors infer that the SOD–catalase system contributes to the superior phenotype, but no knockout establishes necessity. (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 6-7)

**Curate:** quantitative aerotolerance phenotype and SOD/catalase association.  
**Do not yet curate as proven:** `SodA causes METPO:1000609` or `catalase is necessary for Scalindua aerotolerance`.

### *Fusibacter* sp. WBS

WBS remained viable under 4% O₂ flow and displayed SOD activity of 17.4 U mg⁻¹ protein, peroxidase activity of 3.2 U mg⁻¹ protein, no detected catalase activity, and menadiol-dependent O₂ reduction of 11 ± 2 nmol min⁻¹ mg⁻¹ protein. Its genome contains `sod`, `dfx`, `rbr`, `gpx`, and `cydAB`; the combined genomic and biochemical evidence supports an O₂-removal/ROS-defense module, but individual necessity was not genetically tested. (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 8-9, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)

**Curate:** measured phenotype, measured activities, and gene-presence-to-candidate-function links marked inferential.  
**Warning:** because the paper also calls the strain potentially microaerophilic, verify whether it actually grows using O₂ before using it as a canonical instance of the strict METPO definition.

### *Bacteroides thetaiotaomicron*: carbon-source-dependent aerotolerance

The strongest recent direct genetic chain is taxon specific:

**rhamnose → RhaR activity → lower `pfor` transcription → lower ROS/H₂O₂ accumulation → improved recovery after oxygen exposure.** Deleting `rhaR` abolished the rhamnose-associated tolerance advantage and prevented carbon-source-dependent `pfor` downregulation; overexpression and qPCR support the regulatory connection. The authors caution that PFOR is not the principal ROS source, so this is a modifying pathway rather than a complete explanation of aerotolerance. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)

### Periodically oxygenated sulfate reducers

In a 211-day bioreactor exposed to 1-week oxic/4-week anoxic cycles, sulfate-reducing populations survived approximately 133 µM O₂ and reached 0.3–2.4% relative abundance. MAGs transcribed genes for O₂ reduction, ROS detoxification, and oxidized-protein repair; three maintained high oxygen-defense transcript levels even under anoxia. This suggests anticipatory or constitutive preparedness, but it is community-level association and may include oxygen scavenging by partners or aggregation. (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 10-12)

### Pneumococcal metal and peroxide-defense module

In aerotolerant *Streptococcus pneumoniae*, `sodA` disruption reduces aerobic growth and increases paraquat susceptibility; loss of `tpxD` impairs growth/survival under H₂O₂. Mn²⁺ uptake supports Mn-SOD function, while manganese-transporter mutants become more peroxide sensitive. Conversely, excessive labile Fe²⁺ promotes Fenton chemistry; altered `piu`/`dpr` regulation can increase free iron and oxidative stress. This is valuable mechanistic evidence, but pneumococcus produces substantial endogenous H₂O₂ and is not a simple model of all aerotolerant anaerobes. (hernandezmorfa2023theoxidativestress pages 8-9, hernandezmorfa2023theoxidativestress pages 5-6, hernandezmorfa2023theoxidativestress pages 3-4)

## 6. Applications and real-world relevance

- **Anammox engineering and marine nitrogen-cycle models:** oxygen-tolerance parameters affect predictions of nitrogen loss in oxygen-minimum zones and the design/stability of anammox wastewater processes. Oxygen-minimum zones defined at ≤5 µM O₂ occupy about 0.1% of ocean volume but account for an estimated 20–40% of oceanic nitrogen loss; taxon-specific inhibition constants therefore matter. (okabe2023oxygentoleranceand pages 1-2)
- **Next-generation probiotics:** oxygen sensitivity limits cultivation, formulation, and delivery of *Faecalibacterium*. Strain-level variation in flavodiiron proteins, rubrerythrins, superoxide reductases, and peroxidases provides candidate biomarkers for selecting more process-tolerant strains. Cysteine improved survival of *F. longum* L2-6 under high O₂, but this remains strain-specific and lacks knockout validation. (botin2023thetoleranceof pages 1-2)
- **Food safety:** Campylobacter aerotolerance can enhance persistence during poultry processing. Biofilms, polymicrobial partners, refrigeration, medium composition, and serial passage alter measured survival; 43 of 83 *C. jejuni* strains reportedly acclimated after repeated aerobic subculture. These findings support interventions targeting biofilms and assay standardization rather than a single universal gene target. (delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 5-6)
- **Environmental sulfur cycling:** sulfate reducers can persist at oxic–anoxic interfaces and sustain populations through repeated oxygen pulses, influencing sulfur transformations in sediments, wetlands, and engineered systems. (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 10-12)

## 7. Warnings: claims not yet ready for unqualified curation

1. **Do not define aerotolerance by antioxidant-gene presence.** Many taxa carry homologues without demonstrated expression, activity, localization, or phenotype; *Faecalibacterium* inventories vary strongly by strain. (botin2023thetoleranceof pages 1-2)
2. **Do not infer respiration from O₂ consumption.** O₂ reduction may be defensive and orders of magnitude below energy-metabolic flux. (okabe2023oxygentoleranceand pages 6-7)
3. **Do not treat SOD/catalase as universally necessary.** Some anaerobes rely on superoxide reductase, rubrerythrin, flavodiiron proteins, metal substitution, or repair. The SOD–catalase inference in *Scalindua* is correlational. (lu2021whenanaerobesencounter pages 3-4, okabe2023oxygentoleranceand pages 1-2)
4. **Do not universalize RhaR–PFOR regulation.** It is direct evidence in *B. thetaiotaomicron* under specific carbon-source and exposure conditions. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)
5. **Do not encode community shielding as a cell-autonomous mechanism.** Biofilms, aggregates, high density, and oxygen-consuming partners can generate apparent aerotolerance. (delaporte2024aerotolerancyofcampylobacter pages 5-6, dyksma2024growthofsulfatereducing pages 5-6, okabe2023oxygentoleranceand pages 1-2)
6. **Do not conflate survival, recovery, growth, and activity.** Recommended annotations should record O₂ concentration, exposure duration, temperature, medium, cell density, endpoint, and recovery protocol. (imlay2002howoxygendamages pages 25-28, okabe2023oxygentoleranceand pages 1-2)
7. **Avoid a universal “O₂ → ROS → death” chain.** O₂ directly attacks radical and low-potential metal enzymes, while ROS independently damage other targets; both branches are required. (lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 8-9)
8. **Protein-repair and Fe–S-repair edges remain under-supported in strict anaerobes.** They are plausible and review-supported but less directly tested than ROS detoxification. (lu2021whenanaerobesencounter pages 13-15)

## 8. DOI-first bibliography

1. Okabe S, et al. **Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing bacteria.** *ISME Communications*. Published May 2023. https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 1-2)
2. Brioukhanov AL, et al. **Aerotolerant thiosulfate-reducing bacterium *Fusibacter* sp. strain WBS—biochemical and genome analysis.** *Microorganisms*. Published June 2023. https://doi.org/10.3390/microorganisms11071642 (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 8-9, brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8)
3. Botin T, et al. **The tolerance of gut commensal *Faecalibacterium* to oxidative stress is strain dependent and relies on detoxifying enzymes.** *Applied and Environmental Microbiology*. Published July 2023. https://doi.org/10.1128/aem.00606-23 (botin2023thetoleranceof pages 1-2)
4. Hernandez-Morfa M, et al. **The oxidative stress response of *Streptococcus pneumoniae*: its contribution to both extracellular and intracellular survival.** *Frontiers in Microbiology*. Published September 2023. https://doi.org/10.3389/fmicb.2023.1269843 (hernandezmorfa2023theoxidativestress pages 8-9, hernandezmorfa2023theoxidativestress pages 5-6, hernandezmorfa2023theoxidativestress pages 3-4)
5. Xie S, Ma J, Lu Z. **Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms.** *Frontiers in Microbiology*. Published December 2024. https://doi.org/10.3389/fmicb.2024.1505218 (xie2024bacteroidesthetaiotaomicronenhances pages 8-9, xie2024bacteroidesthetaiotaomicronenhances pages 9-11)
6. Dyksma S, Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O₂ saturation.** *Microbiome*. Published October 2024. https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 10-12)
7. Delaporte E, Karki AB, Fakhr MK. **Aerotolerancy of *Campylobacter* spp.: a comprehensive review.** *Pathogens*. Published September 2024. https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 5-6)
8. Lu Z, Imlay JA. **When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.** *Nature Reviews Microbiology*. Published June 2021. https://doi.org/10.1038/s41579-021-00583-y (lu2021whenanaerobesencounter pages 3-4, lu2021whenanaerobesencounter pages 13-15, lu2021whenanaerobesencounter pages 8-9, lu2021whenanaerobesencounter pages 1-3)
9. Imlay JA. **How oxygen damages microbes: oxygen tolerance and obligate anaerobiosis.** *Advances in Microbial Physiology*. Published January 2002. https://doi.org/10.1016/S0065-2911(02)46003-1 (imlay2002howoxygendamages pages 25-28)

**Curation recommendation:** expand the existing `aerotolerant_anaerobe_ros_defense` graph into three explicit branches—**direct O₂ damage**, **O₂/ROS detoxification**, and **damage repair/recovery**—with assay-context nodes attached to the terminal aerotolerance phenotype. The most defensible additions are the quantitative *Scalindua* phenotype, the *Fusibacter* O₂-reduction module, and the taxon-scoped RhaR→`pfor`→ROS→oxygen-recovery chain.

References

1. (imlay2002howoxygendamages pages 25-28): James A. Imlay. How oxygen damages microbes: oxygen tolerance and obligate anaerobiosis. Advances in microbial physiology, 46:111-53, Jan 2002. URL: https://doi.org/10.1016/s0065-2911(02)46003-1, doi:10.1016/s0065-2911(02)46003-1. This article has 357 citations and is from a peer-reviewed journal.

2. (lu2021whenanaerobesencounter pages 22-27): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

3. (lu2021whenanaerobesencounter pages 8-9): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

4. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

5. (okabe2023oxygentoleranceand pages 6-7): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

6. (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 8-9): Andrei L. Brioukhanov, Vitaly V. Kadnikov, Alexey V. Beletsky, and Alexander S. Savvichev. Aerotolerant thiosulfate-reducing bacterium fusibacter sp. strain wbs isolated from littoral bottom sediments of the white sea—biochemical and genome analysis. Microorganisms, 11:1642, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071642, doi:10.3390/microorganisms11071642. This article has 14 citations.

7. (delaporte2024aerotolerancyofcampylobacter pages 5-6): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

8. (xie2024bacteroidesthetaiotaomicronenhances pages 9-11): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

9. (brioukhanov2023aerotolerantthiosulfatereducingbacterium pages 7-8): Andrei L. Brioukhanov, Vitaly V. Kadnikov, Alexey V. Beletsky, and Alexander S. Savvichev. Aerotolerant thiosulfate-reducing bacterium fusibacter sp. strain wbs isolated from littoral bottom sediments of the white sea—biochemical and genome analysis. Microorganisms, 11:1642, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071642, doi:10.3390/microorganisms11071642. This article has 14 citations.

10. (lu2021whenanaerobesencounter pages 3-4): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

11. (lu2021whenanaerobesencounter pages 13-15): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

12. (hernandezmorfa2023theoxidativestress pages 8-9): Mirelys Hernandez-Morfa, Nadia B. Olivero, Victoria E. Zappia, German E. Piñas, Nicolas M. Reinoso-Vizcaino, Melina B. Cian, Mariana Nuñez-Fernandez, Paulo R. Cortes, and Jose Echenique. The oxidative stress response of streptococcus pneumoniae: its contribution to both extracellular and intracellular survival. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1269843, doi:10.3389/fmicb.2023.1269843. This article has 31 citations and is from a peer-reviewed journal.

13. (hernandezmorfa2023theoxidativestress pages 5-6): Mirelys Hernandez-Morfa, Nadia B. Olivero, Victoria E. Zappia, German E. Piñas, Nicolas M. Reinoso-Vizcaino, Melina B. Cian, Mariana Nuñez-Fernandez, Paulo R. Cortes, and Jose Echenique. The oxidative stress response of streptococcus pneumoniae: its contribution to both extracellular and intracellular survival. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1269843, doi:10.3389/fmicb.2023.1269843. This article has 31 citations and is from a peer-reviewed journal.

14. (hernandezmorfa2023theoxidativestress pages 3-4): Mirelys Hernandez-Morfa, Nadia B. Olivero, Victoria E. Zappia, German E. Piñas, Nicolas M. Reinoso-Vizcaino, Melina B. Cian, Mariana Nuñez-Fernandez, Paulo R. Cortes, and Jose Echenique. The oxidative stress response of streptococcus pneumoniae: its contribution to both extracellular and intracellular survival. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1269843, doi:10.3389/fmicb.2023.1269843. This article has 31 citations and is from a peer-reviewed journal.

15. (dyksma2024growthofsulfatereducing pages 10-12): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 56 citations and is from a highest quality peer-reviewed journal.

16. (dyksma2024growthofsulfatereducing pages 5-6): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 56 citations and is from a highest quality peer-reviewed journal.

17. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 20 citations and is from a peer-reviewed journal.

18. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 22 citations and is from a peer-reviewed journal.

19. (delaporte2024aerotolerancyofcampylobacter pages 9-11): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

20. (lu2021whenanaerobesencounter pages 1-3): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.