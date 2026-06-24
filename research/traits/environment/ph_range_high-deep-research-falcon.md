---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:38:19.339603'
end_time: '2026-06-18T00:56:06.665152'
duration_seconds: 1067.33
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range high
  trait_identifier: METPO:1000464
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 10\u201314, characteristic of extreme-alkaliphile physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
  evidence_summary: 'DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review
    supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005:
    proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity
    as the extreme-alkaliphile mechanism sustaining the proton motive force above
    pH 10.)'
  causal_graph_summary: 'ph_range_high_extreme_alkaliphile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range high
- **METPO identifier:** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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
- **Trait label:** pH range high
- **METPO identifier:** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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


## Curation-focused research report: Microbial trait “pH range high” (METPO:1000464)

### Scope summary (trait meaning, boundaries, and current understanding)
**Trait definition in this template:** *growth-supporting external pH range spans approximately 10–14* (extreme alkaliphile physiology). A key curation choice is to anchor this trait to **demonstrated growth** (not survival) at **pH ≥10**, ideally with controlled buffering, and to distinguish it from (i) **alkali-tolerant** organisms that survive or grow only up to ~pH 9–10 and (ii) organisms whose **optimum** is alkaline but whose **maximum growth pH** is <10. (krulwich2011molecularaspectsof pages 12-14)

A canonical model system is *Bacillus pseudofirmus* OF4 (and related alkaliphilic *Bacillus* spp.), which can grow at pH ≥10 and has been used to define mechanistic requirements. In pH-controlled continuous cultures, *B. pseudofirmus* OF4 maintains near-complete homeostasis (pHin ~7.5) only between pHout 7.5–9.5, yet can still grow optimally up to ~pHout 10.5 (with pHin ~8.3) and even grow at pHout ≥11 (with pHin ≥9.5). This emphasizes that the trait is **growth at high external pH**, not necessarily maintenance of neutral cytoplasmic pH. (krulwich2011molecularaspectsof pages 12-14)

**Boundary warning for METPO:1000464:** several mechanistic studies address alkaliphily in the pH 9–10 range (e.g., heterologous expression assays showing tolerance to pH 9.5) which are relevant to *alkaline tolerance* but may not reach the trait’s extreme boundary (pH ≥10–14). Such edges should be curated with explicit “assay-specific / lower-pH” caveats. (wang2023characterizationoftwo pages 7-8)

---

### Key concepts and mechanistic “modules” (what enables growth at pH ≥10?)
Mechanistically, high-pH growth is often described as a **systems phenotype** composed of (1) **electrogenic cation/proton antiport** to import scarce protons, (2) **maintenance of a large membrane potential (Δψ)** to drive that antiport, (3) **Na+ cycling** to keep antiport running in a low-H+ environment, (4) **ATP synthase adaptations** to synthesize ATP without losing protons, and (5) **cell-surface features** that may retain protons near the membrane. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14)

A concise schematic model for extreme alkaliphilic *Bacillus* (OF4) is provided in Krulwich et al. (2011) Figure 4: Na+/H+ antiport (Mrp as “critical”), Na+ re-entry (Na+/solute symporters, NaVBP channel, MotPS channel), proton-pumping respiratory complexes generating Δψ, ATP synthase near-surface proton capture, and cell-wall polymers (S-layer/SCWP). (krulwich2011molecularaspectsof media 2a26910f, krulwich2011molecularaspectsof pages 27-28)

---

## Candidate nodes (grouped by type; ontology grounding where feasible)
The following candidate nodes are intended for curating into `data/traits/environment/ph_range_high.yaml`.

| Node type | Node label | Suggested identifier(s) | Role in trait | Key supporting source |
|---|---|---|---|---|
| Environment/Phenotype | pH range high / extreme alkaliphily | METPO:1000464 | target trait: growth at external pH ≥10 | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Environment/Phenotype | high external pH / hyperalkaline conditions | ENVO:01000314 candidate | selective pressure requiring proton capture and alkali homeostasis | Scott 2024 doi:10.1128/AEM.01557-23; Colman 2024 doi:10.1101/2024.11.10.622848 (scott2024widespreaddissolvedinorganic pages 7-10, colman2024themicrobialecology pages 14-18) |
| Environment/Phenotype | hypersaline soda lake | ENVO:00000037 candidate | common habitat coupling high pH with high Na+ stress | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Environment/Phenotype | hyperalkaline serpentinite fluid | ENVO:01000256 candidate | high-pH, DIC-poor habitat selecting for ion and carbon adaptations | Colman 2024 doi:10.1101/2024.11.10.622848 (colman2024themicrobialecology pages 14-18) |
| Process | Na+/H+ antiport | GO:0015385 candidate | major H+ uptake mechanism at high pH | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Process | K+/H+ antiport | GO:0015386 candidate | auxiliary cation/proton balancing under alkali stress | Cheng 2016 doi:10.1074/jbc.M116.751016 (cheng(程彬)2016alkalineresponseof pages 1-2) |
| Process | cytoplasmic pH homeostasis | GO:0051452 | maintains viable intracellular pH during alkaline growth | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Process | Na+ cycle / Na+ re-entry | label-only | sustains continuous antiport at low external proton availability | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14) |
| Process | membrane potential (Δψ) generation/use | GO:0006818 candidate | electrical driving force for electrogenic antiport | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8) |
| Process | K+ homeostasis | GO:0055075 | stabilizes intracellular ion balance under haloalkaline stress | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Process | compatible-solute accumulation | GO:0015850 candidate | offsets osmotic stress in haloalkaliphiles | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Process | dissolved inorganic carbon toolkit / CCM | label-only | mitigates low CO2 availability at high pH | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Process | DIC speciation shift at high pH | label-only | shifts carbon from CO2/HCO3- toward CO3^2- | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Process | Wood–Ljungdahl pathway | MetaCyc:PWY-5177 candidate | carbon fixation strategy favored in DIC-limited hyperalkaline systems | Colman 2024 doi:10.1101/2024.11.10.622848 (colman2024themicrobialecology pages 18-21) |
| Protein complex | Mrp Na+/H+ antiporter | TCDB:2.A.63; CPA3 family | core multisubunit antiporter for extreme alkaliphily | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Protein complex | F1Fo-ATP synthase | GO:0045263 | proton uptake during ATP synthesis aids pH homeostasis | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Protein complex | Na+-translocating FoF1-ATPase | GO:0046933 candidate | sodium-coupled bioenergetics in polyextremophiles | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Protein complex | carboxysome / CCM module | GO:0031469 candidate | concentrates CO2 for autotrophy under alkaline DIC limitation | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Gene/protein family | mrpA–G operon | label-only | encodes hetero-oligomeric Mrp antiporter | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Gene/protein family | NhaA family antiporter | TCDB:2.A.33.1 | paradigm alkaline-activated Na+/H+ antiporter | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8) |
| Gene/protein family | NhaD family antiporter (e.g., Ha-NhaD2) | label-only | robust Na+/Li+ export supporting alkaline/salt adaptation | Cheng 2016 doi:10.1074/jbc.M116.751016 (cheng(程彬)2016alkalineresponseof pages 1-2) |
| Gene/protein family | NhaC family antiporter | TCDB:2.A.35 candidate | alkaline-active Na+(K+,Li+)/H+ exchange | Wang 2023 doi:10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8) |
| Gene/protein family | NhaP family antiporter | TCDB:2.A.36 candidate | K+/H+ exchange supporting alkali stress tolerance | Cheng 2016 doi:10.1074/jbc.M116.751016 (cheng(程彬)2016alkalineresponseof pages 1-2) |
| Gene/protein family | NaVBP voltage-gated Na+ channel | label-only | Na+ re-entry supporting Na+/H+ antiport cycle | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28) |
| Gene/protein family | MotPS channel | label-only | flagellar-associated Na+ influx for antiport support | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28) |
| Gene/protein family | Na+/solute symporters | GO:0015294 candidate | replenishes cytoplasmic Na+ to fuel antiport | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Gene/protein family | glycine betaine ABC transporters (Opu/ProU) | KEGG:K05845/K02000 candidate | imports compatible solutes in haloalkaliphiles | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Gene/protein family | carbonic anhydrase / DIC toolkit proteins | EC:4.2.1.1 | interconvert DIC species for carbon acquisition at high pH | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Gene/protein family | bicarbonate transporter SbtA | label-only | candidate high-affinity HCO3- uptake in alkaline CCMs | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Gene/protein family | bicarbonate transporter BicA | label-only | candidate Na+-dependent HCO3- uptake in alkaline CCMs | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Metabolite/ion | Na+ | CHEBI:29101 | coupling ion for antiport and sodium cycle | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Metabolite/ion | H+ | CHEBI:15378 | limiting ion imported to offset alkaline exterior | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14) |
| Metabolite/ion | K+ | CHEBI:29103 | intracellular cation buffered by transport systems | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Metabolite/ion | glycine betaine | CHEBI:17750 | compatible solute accumulated in haloalkaliphiles | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Metabolite/ion | glutamate | CHEBI:29985 | compatible solute / osmoadaptive metabolite | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Metabolite/ion | proline | CHEBI:17203 | compatible solute / osmoadaptive metabolite | Xing 2024 doi:10.1128/AEM.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Metabolite/ion | CO2 | CHEBI:16526 | scarce DIC species above alkaline pH | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Metabolite/ion | bicarbonate (HCO3-) | CHEBI:17544 | dominant DIC near neutral to mildly alkaline pH | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Metabolite/ion | carbonate (CO3^2-) | CHEBI:18311 | dominant DIC species above ~pH 10.3 | Scott 2024 doi:10.1128/AEM.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10) |
| Metabolite/ion | formate | CHEBI:15740 | alternative carbon/reductant in hyperalkaline DIC-poor systems | Colman 2024 doi:10.1101/2024.11.10.622848 (colman2024themicrobialecology pages 21-24) |
| Cellular structure | S-layer (including SlpA) | GO:0030111 candidate | acidic surface layer aiding adaptation to alkaline shift | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8) |
| Cellular structure | SlpA S-layer protein | label-only | surface component linked to pH-shift adaptation | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8) |
| Cellular structure | teichuronic acids / acidic secondary cell wall polymers | label-only | proton-binding cell-surface polymers at high pH | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8) |
| Cellular structure | ATP synthase c-ring alkaliphile motifs (AxAxAxA; PxxExxP) | label-only | motif-level rotor adaptation for tight proton binding | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14) |


*Table: This table lists candidate nodes for a causal graph of METPO:1000464, spanning environments, processes, transporters, bioenergetic complexes, metabolites, and cell structures implicated in microbial growth at very high pH. It is useful for selecting ontology-grounded entities to curate into a TraitMech YAML graph.*

---

## Evidence-backed candidate causal edges (triples) for a TraitMech causal graph
The table below provides candidate edges (subject–predicate–object), each with an evidence snippet, DOI-first citation, and curation notes.

| Edge ID | Subject (CURIE if known) | Predicate | Object (CURIE if known) | Evidence snippet | Source | Notes / uncertainty |
|---|---|---|---|---|---|---|
| E1 | Mrp Na+/H+ antiporter complex (CPA3 family; GO:0015385 candidate) | enables | pH range high / extreme alkaliphily (METPO:1000464) | “the unusual hetero-oligomeric Mrp antiporter has an indispensible role at high pH” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong but mostly Bacillus-centered; trait-level generalization across taxa should be marked moderate. |
| E2 | mrpA | loss_of_function_decreases | alkaline pH homeostasis | “A point mutation in the mrpA gene of alkaliphilic B. halodurans C-125 leads to a non-alkaliphilic phenotype accompanied by loss of alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong genetic evidence; taxon-specific to B. halodurans C-125. |
| E3 | mrpA | loss_of_function_decreases | Na+/H+ antiport activity (GO:0015385 candidate) | “accompanied by… loss of Na+/H+ antiport measured in whole cells” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong genetic/physiological link; taxon-specific. |
| E4 | MrpA–G operon | encodes | hetero-oligomeric Mrp antiporter complex | “Bacillus Mrp antiporters are encoded in operons that contain genes for seven hydrophobic proteins” and “All the Mrp proteins are required to form a hetero-oligomeric complex” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Mechanistic assembly edge; good curation candidate. |
| E5 | membrane potential Δψ | drives | electrogenic Na+/H+ antiport-mediated H+ uptake | “A large transmembrane potential (Δψ) is essential to drive electrogenic Na+/H+ and K+/H+ antiporters that import H+” (krulwich2011molecularaspectsof pages 5-6) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | General pH-homeostasis principle; not unique to alkaliphiles, but directly relevant. |
| E6 | Na+/solute symporters | supplies cytoplasmic Na+ for | alkaliphile antiport activity | “The ongoing requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport activity is met by numerous Na+/solute symporters” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Supports Na+ cycle model; likely taxon-general within extreme alkaliphiles. |
| E7 | NaVBP voltage-gated sodium channel | contributes_to | continuous Na+/H+ antiport via Na+ re-entry | “Na+ re-entry… occurs through… the voltage-gated NaVBP channel” (krulwich2011molecularaspectsof pages 27-28) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Mechanistic model from Bacillus pseudofirmus OF4 schematic; moderate confidence. |
| E8 | MotPS channel | contributes_to | continuous Na+/H+ antiport via Na+ re-entry | “Na+ re-entry… occurs through… flagellar-associated MotPS channel” (krulwich2011molecularaspectsof pages 27-28) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Mechanistic model; likely conditional on motility/flagellar state. |
| E9 | F1Fo-ATP synthase | contributes_to | alkaliphile pH homeostasis | “The proton uptake that accompanies ATP synthesis by the F1F0-ATP synthase contributes to alkaliphile pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong review synthesis; mostly aerobic alkaliphilic Bacillus. |
| E10 | ATP synthase subunit-a / subunit-c alkaliphile-specific motifs | supports | ATP synthase function at high pH | “They have specific sequence motifs in proton-translocating subunit-a and subunit-c that support function at high pH” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Good mechanistic edge; motif-level curation may need label-only nodes. |
| E11 | ATP synthase motif mutations | decreases | pH homeostasis during sudden alkaline shift | “Mutations of these motifs… leads to reduced ATP synthase activity… [and] correlates with a loss of the mutants’ capacities for pH homeostasis during a sudden alkaline shift” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong experimental support; mutation-specific. |
| E12 | SlpA S-layer protein | contributes_to | adaptation to sudden shift to high pH | “Deletion of slpA… results in reduced ability to adapt to a sudden shift from pH 7.5 to 11” (krulwich2011molecularaspectsof pages 6-8) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong for shift adaptation; not direct proof of full growth range trait. |
| E13 | acidic secondary cell wall polymers / SlpA | may_bind | protons (CHEBI:15378) near cell surface | “They may bind protons, perhaps enhancing proton uptake by increasing the proton concentration near the surface” (krulwich2011molecularaspectsof pages 6-8) | Krulwich 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Hypothesized mechanism; curate as uncertain/inferred. |
| E14 | Ha-Mrp | enables | alkaline-condition cation resistance and pH homeostasis | “Ha-Mrp showed central roles in the pH homeostasis of Halomonas sp. Y2. An Ha-mrp-disrupted mutant was seriously inhibited by high concentrations of Na+(Li+, K+), but only under alkaline conditions” (cheng(程彬)2016alkalineresponseof pages 1-2) | Cheng 2016, doi:10.1074/jbc.M116.751016, https://doi.org/10.1074/jbc.M116.751016 | Strong gene disruption evidence; taxon-specific to Halomonas sp. Y2. |
| E15 | Ha-NhaD2 | contributes_to | osmotic homeostasis across pH including alkaline pH | “Ha-NhaD2 displayed robust Na+(Li+) resistance… a ΔHa-nhaD2 mutant exhibited growth inhibition at high Na+(Li+) concentrations at pHs of 6.2, 8.0, and 10.0” (cheng(程彬)2016alkalineresponseof pages 1-2) | Cheng 2016, doi:10.1074/jbc.M116.751016, https://doi.org/10.1074/jbc.M116.751016 | Strong but broader salt/osmotic role, not exclusive high-pH determinant. |
| E16 | Ha-NhaP | functions_as | K+/H+ antiporter | “Ha-NhaP was determined to be a K+/H+ antiporter and shown to confer strong K+ resistance both at acidic and alkaline stresses” (cheng(程彬)2016alkalineresponseof pages 1-2) | Cheng 2016, doi:10.1074/jbc.M116.751016, https://doi.org/10.1074/jbc.M116.751016 | Strong functional assignment; relevance to extreme alkaliphily is supportive, not sufficient alone. |
| E17 | nhaC2 | confers | alkaline pH resistance up to pH 9.5 in E. coli KNabc | “nhaC2 could confer higher alkaline pH resistance on KNabc, resisting up to pH 9.5” (wang2023characterizationoftwo pages 7-8) | Wang 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 | Heterologous complementation assay; supports alkaline resistance, but below pH 10 and not native-trait proof. |
| E18 | nhaC1 | confers | alkaline pH resistance up to pH 8.5 in E. coli KNabc | “KNabc/nhaC1 could still grow at pH 8.5” (wang2023characterizationoftwo pages 7-8) | Wang 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 | Weaker relevance to METPO:1000464 because phenotype does not reach pH ≥10 in assay. |
| E19 | glycine betaine ABC transporters (Opu, ProU families) | contributes_to | adaptation to high salinity in alkalithermophile N. thermophilus | “N. thermophilus employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing 2024, doi:10.1128/AEM.00145-24, https://doi.org/10.1128/AEM.00145-24 | Strong for haloalkalithermophile adaptation; more salinity-linked than pH-linked. |
| E20 | glutamate / proline biosynthesis pathways | increases | compatible-solute pool under multiple extremes | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing 2024, doi:10.1128/AEM.00145-24, https://doi.org/10.1128/AEM.00145-24 | Useful background node set; primarily salinity adaptation evidence. |
| E21 | Na+/K+/H+ transporters | maintains | intracellular K+ homeostasis under alkaline hypersaline conditions | “the upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing 2024, doi:10.1128/AEM.00145-24, https://doi.org/10.1128/AEM.00145-24 | Strong in N. thermophilus; indirect link to high-pH growth via ion homeostasis. |
| E22 | Na+-translocating FoF1-ATPase | contributes_to | adaptation to multiple extremes in N. thermophilus | “N. thermophilus possesses… Na+-translocating FOF1-ATPase to adapt to multiple extremes” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing 2024, doi:10.1128/AEM.00145-24, https://doi.org/10.1128/AEM.00145-24 | Genome-based plus contextual physiological evidence; direct causality for pH trait remains moderate. |
| E23 | external pH >10.3 | shifts_DIC_speciation_toward | carbonate CO3^2− (CHEBI:18311) and away from CO2 | “DIC speciation shifts strongly with pH… CO3= above ~10.3” (scott2024widespreaddissolvedinorganic pages 7-10) | Scott 2024, doi:10.1128/AEM.01557-23, https://doi.org/10.1128/AEM.01557-23 | Environmental chemistry edge; important context for hyperalkaline carbon limitation. |
| E24 | hyperalkaline waters (ENVO:01000314 candidate) | decreases_availability_of | dissolved inorganic carbon (DIC) | “highly serpentinized, hyperalkaline waters commonly have critically low dissolved inorganic carbon (DIC) — often below analytical detection (~10 µM)” (colman2024themicrobialecology pages 14-18) | Colman 2024, doi:10.1101/2024.11.10.622848, https://doi.org/10.1101/2024.11.10.622848 | Preprint; strong environmental evidence but not a direct organismal mechanism edge. |
| E25 | Wood–Ljungdahl pathway | is_enriched_in | higher-pH, DIC-limited serpentinite waters | “the Wood–Ljungdahl (WL) pathway enriched in higher-pH, more serpentinization-influenced waters—consistent with WL being energetically efficient under energy- and DIC-limited conditions” (colman2024themicrobialecology pages 18-21) | Colman 2024, doi:10.1101/2024.11.10.622848, https://doi.org/10.1101/2024.11.10.622848 | Preprint and community-level inference; useful but should be curated as uncertain/contextual. |


*Table: This table lists candidate subject–predicate–object edges for curating a causal graph of microbial high-pH growth, with concise evidence snippets, source details, and uncertainty notes. It emphasizes experimentally supported transport, bioenergetic, surface, and carbon-limitation mechanisms relevant to growth at high external pH.*

---

## Recent developments (prioritizing 2023–2024)
### 1) Polyextremophiles in soda lakes: coupled halo-alkali adaptation
A 2024 quantitative multi-omics study of the haloalkalithermophile *Natranaerobius thermophilus* (optimal pH 9.5; multiple extremes) reports a **hybrid osmoadaptation strategy** (“compatible solute” plus “salt-in”) supported by proteomics, ddPCR validation, and metabolite measurements. Key components include glycine betaine transporters (Opu/ProU), Na+/solute symporters (SSS family), glutamate/proline synthesis, and upregulated Na+/K+/H+ transporters that maintain intracellular K+. (xing2024thepolyextremophilenatranaerobius pages 1-2)

**TraitMech relevance:** these edges are most directly connected to **haloalkaline ecological settings** (soda lakes) and ion homeostasis. They are mechanistically adjacent to high-pH growth but should be curated as *contextual support* unless tied explicitly to pH ≥10 growth assays in the same organism. (xing2024thepolyextremophilenatranaerobius pages 1-2)

### 2) Genome/ecology synthesis: DIC limitation at high pH and carbon-acquisition constraints
Scott et al. (2024) provides a 2024 synthesis of **dissolved inorganic carbon (DIC) speciation versus pH** and reports systematic correlations between DIC toolkit genes and host optimal pH (e.g., carbonate predominance above ~pH 10.3). (scott2024widespreaddissolvedinorganic pages 7-10)

Colman et al. (2024 preprint) emphasizes that **hyperalkaline waters can be extremely DIC-limited** (often below detection around ~10 µM) and that pathways like the **Wood–Ljungdahl pathway** and **formate use** may be enriched/selected in higher-pH serpentinization-influenced systems. (colman2024themicrobialecology pages 14-18, colman2024themicrobialecology pages 18-21, colman2024themicrobialecology pages 21-24)

**TraitMech relevance:** these sources motivate adding environmental driver nodes/edges (high pH → DIC scarcity; high pH → carbonate precipitation → DIC limitation) and downstream “constraint/selection” edges to carbon fixation strategies (WL pathway, formate assimilation) in hyperalkaline systems. Because Colman et al. is a preprint and many claims are community-level inferences, curation should be marked uncertain. (colman2024themicrobialecology pages 18-21, colman2024themicrobialecology pages 14-18)

### 3) Antiporter diversity and functional genetics beyond Bacillus models
Cheng et al. (2016) gives direct genetic evidence in a halotolerant alkaliphile (*Halomonas* sp. Y2 from wastewater pH >11) that distinct Na+/H+ and K+/H+ antiporters support alkaline/saline stress via “division of labor”, including an Mrp antiporter with alkaline-condition phenotypes upon disruption. (cheng(程彬)2016alkalineresponseof pages 1-2)

Wang et al. (2023) provides 2023 heterologous evidence that archaeal NhaC-family antiporters can increase alkaline resistance up to pH 9.5 in an *E. coli* antiporter-deficient host. (wang2023characterizationoftwo pages 7-8)

**TraitMech relevance:** Mrp-centric edges have strong support for high pH growth in *Bacillus* and in *Halomonas*. NhaC complementation edges provide supportive mechanistic evidence but do not meet pH ≥10 in the assay and therefore should be marked “not sufficient alone” for METPO:1000464. (krulwich2011molecularaspectsof pages 12-14, cheng(程彬)2016alkalineresponseof pages 1-2, wang2023characterizationoftwo pages 7-8)

---

## Current applications and real-world implementations (high-pH trait relevance)
While the core sources here focus on physiology/ecology rather than industrial processes, the mechanistic modules (antiporters, Na+ cycling, ATP synthase adaptations) are directly relevant to:
- **Bioprocessing under alkaline conditions** (e.g., alkaline waste streams, high-soda media), where maintaining growth and energy conservation at high pH is limiting; mechanistic nodes such as Mrp antiporters and Na+-coupled ATPases are targetable engineering points. (krulwich2011molecularaspectsof pages 12-14, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Carbon acquisition in alkaline systems**, where DIC speciation and scarcity shape feasibility of autotrophy and informs process design for alkaline cultivation/carbon capture schemes (DIC toolkit logic). (scott2024widespreaddissolvedinorganic pages 7-10)
- **Environmental and astrobiology analogs**, including hyperalkaline serpentinite-hosted systems with extreme pH and low DIC; the trait’s causal graph should include “environmental constraint” edges as above. (colman2024themicrobialecology pages 14-18)

---

## Expert synthesis / authoritative interpretation
Krulwich et al. (Nature Reviews Microbiology, 2011) remains a central synthesis for alkaliphile pH homeostasis and provides multiple lines of mechanistic evidence: Mrp essentiality, Na+ cycling, Δψ dependence, ATP synthase motif-function relationships, and surface-layer contributions (SlpA). (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 12-14)

A key “expert consensus” that is strongly supported in this evidence set is that, in extreme alkaliphilic *Bacillus*, **Na+/H+ antiport-dependent pH homeostasis is the major strategy**, with the **multisubunit Mrp antiporter being indispensable** at high pH. (krulwich2011molecularaspectsof pages 12-14)

---

## Relevant statistics and quantitative data points (from the retrieved sources)
- *B. pseudofirmus* OF4 chemostat: maintains pHin ~7.5 from pHout 7.5–9.5; grows optimally up to pHout ~10.5 with pHin ~8.3; still grows at pHout ≥11 with pHin ≥9.5. (krulwich2011molecularaspectsof pages 12-14)
- *N. thermophilus* growth conditions: thrives at high salinity (3.3–3.9 M Na+), alkaline pH 9.5, 53°C; can grow at 3.1–4.9 M Na+ (optimum 3.3–3.9 M). (xing2024thepolyextremophilenatranaerobius pages 1-2)
- NhaC heterologous alkaline tolerance: E. coli KNabc expressing nhaC2 grows up to pH 9.5 (nhaC1 up to pH 8.5) in the described assay. (wang2023characterizationoftwo pages 7-8)
- DIC speciation threshold: DIC shifts toward CO3^2− above ~pH 10.3 (and away from CO2), consistent with CO2 scarcity at high pH. (scott2024widespreaddissolvedinorganic pages 7-10)
- Hyperalkaline serpentinite waters: DIC can be “below analytical detection (~10 µM)” and pH can exceed 12 in some systems, creating strong carbon limitation. (colman2024themicrobialecology pages 14-18)

---

## Curation warnings (what should *not* yet be curated as strong edges)
1. **Alkaline tolerance below pH 10 is not equivalent to METPO:1000464.** For example, nhaC complementation reaching pH 9.5 supports alkaline tolerance mechanisms but does not itself establish extreme alkaliphily (pH ≥10). Curate these edges with explicit assay range notes. (wang2023characterizationoftwo pages 7-8)
2. **Hypothesized proton-binding surface polymers:** claims that teichuronic acids / acidic S-layers “may bind protons” are mechanistically plausible but described as hypotheses; curate as uncertain unless direct functional tests exist. (krulwich2011molecularaspectsof pages 6-8)
3. **Community-level enrichment claims from preprints:** serpentinite ecological inferences (WL enrichment, formate reliance, extracellular hydrogenase effects on DIC liberation) are valuable context but should be curated as uncertain and environment-specific pending peer-reviewed confirmation and organism-level experiments. (colman2024themicrobialecology pages 18-21, colman2024themicrobialecology pages 14-18, colman2024themicrobialecology pages 21-24)

---

## DOI-first bibliography (with URLs and publication dates where available)
1. **Krulwich TA, Sachs G, Padan E.** Molecular aspects of bacterial pH sensing and homeostasis. *Nature Reviews Microbiology* (May 2011). DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof media 2a26910f)
2. **Xing Q et al.** The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress… *Applied and Environmental Microbiology* (Published 5 Apr 2024; issue May 2024). DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
3. **Scott KM, Payne RR, Gahramanova A.** Widespread dissolved inorganic carbon-modifying toolkits… *Applied and Environmental Microbiology* (Feb 2024). DOI: **10.1128/aem.01557-23**. URL: https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 7-10)
4. **Wang Q, Qiao M, Song J.** Characterization of two Na+(K+, Li+)/H+ antiporters from *Natronorubrum daqingense*. *International Journal of Molecular Sciences* (Jun 2023). DOI: **10.3390/ijms241310786**. URL: https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8)
5. **Colman DR et al.** The Microbial Ecology of Serpentinites. *bioRxiv* (Nov 2024, preprint). DOI: **10.1101/2024.11.10.622848**. URL: https://doi.org/10.1101/2024.11.10.622848 (colman2024themicrobialecology pages 18-21, colman2024themicrobialecology pages 14-18, colman2024themicrobialecology pages 21-24)
6. **Cheng B et al.** Alkaline response of a halotolerant alkaliphilic *Halomonas* strain and functional diversity of its Na+(K+)/H+ antiporters. *Journal of Biological Chemistry* (Published online Oct 24, 2016). DOI: **10.1074/jbc.M116.751016**. URL: https://doi.org/10.1074/jbc.M116.751016 (cheng(程彬)2016alkalineresponseof pages 1-2)

---

### Note on coverage gaps
Within the retrieved full texts, the strongest direct mechanistic/genetic support for pH ≥10 growth remains centered on Mrp/ATP synthase/surface features in extreme alkaliphilic *Bacillus* (foundational) and antiporter genetics in *Halomonas*. Several 2023–2024 sources provide critical context (DIC toolkit/pH correlations; DIC limitation in hyperalkaline serpentinite systems; polyextremophile adaptation under alkaline conditions), but fewer provide direct gene knockout-to-high-pH growth links specifically at pH ≥10–12 in pure culture. (krulwich2011molecularaspectsof pages 12-14, scott2024widespreaddissolvedinorganic pages 7-10, colman2024themicrobialecology pages 14-18, xing2024thepolyextremophilenatranaerobius pages 1-2)

References

1. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

3. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof media 2a26910f): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

6. (colman2024themicrobialecology pages 14-18): Daniel R. Colman, Alexis S. Templeton, John R. Spear, and Eric S. Boyd. The microbial ecology of serpentinites. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.10.622848, doi:10.1101/2024.11.10.622848. This article has 1 citations.

7. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

8. (cheng(程彬)2016alkalineresponseof pages 1-2): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 57 citations and is from a domain leading peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

10. (colman2024themicrobialecology pages 18-21): Daniel R. Colman, Alexis S. Templeton, John R. Spear, and Eric S. Boyd. The microbial ecology of serpentinites. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.10.622848, doi:10.1101/2024.11.10.622848. This article has 1 citations.

11. (colman2024themicrobialecology pages 21-24): Daniel R. Colman, Alexis S. Templeton, John R. Spear, and Eric S. Boyd. The microbial ecology of serpentinites. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.10.622848, doi:10.1101/2024.11.10.622848. This article has 1 citations.

12. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.