---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:39:37.626358'
end_time: '2026-08-04T05:50:05.129995'
duration_seconds: 627.5
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Calvin-Benson-Bassham cycle
  trait_identifier: traitmech:000020
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: calvin_benson_bassham_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (the reductive pentose phosphate
    cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO).
    It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria,
    and many proteobacteria.
  parent_traits: traitmech:000019
  synonyms: Calvin cycle, reductive pentose phosphate cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham\
    \ (reductive pentose phosphate) cycle as the reference autotrophic pathway against\
    \ which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert support the Calvin cycle as the most common/widespread\
    \ CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)"
  causal_graph_summary: 'cbb_rubisco_co2_fixation: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Calvin-Benson-Bassham cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000020
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive pentose phosphate cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO). It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria, and many proteobacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** Calvin cycle, reductive pentose phosphate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham (reductive pentose phosphate) cycle as the reference autotrophic pathway against which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert support the Calvin cycle as the most common/widespread CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)
- **Existing causal graph summary:** cbb_rubisco_co2_fixation: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **Calvin-Benson-Bassham cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/calvin_benson_bassham_cycle.yaml`.

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
- **Trait label:** Calvin-Benson-Bassham cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000020
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive pentose phosphate cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO). It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria, and many proteobacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** Calvin cycle, reductive pentose phosphate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham (reductive pentose phosphate) cycle as the reference autotrophic pathway against which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert support the Calvin cycle as the most common/widespread CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)
- **Existing causal graph summary:** cbb_rubisco_co2_fixation: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **Calvin-Benson-Bassham cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/calvin_benson_bassham_cycle.yaml`.

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


# Curation report: Calvin–Benson–Bassham cycle

## Trait record and scope

- **Trait:** Calvin–Benson–Bassham (CBB) cycle
- **Identifier:** `traitmech:000020`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000019`
- **Synonyms:** Calvin cycle; reductive pentose-phosphate cycle

### Recommended operational definition

This trait represents the genetically encoded and physiologically operable **autocatalytic pathway that incorporates inorganic carbon into biomass through Rubisco-dependent carboxylation of ribulose-1,5-bisphosphate (RuBP), ATP/NADPH-dependent reduction of 3-phosphoglycerate (3-PGA), and phosphoribulokinase (PRK)-dependent regeneration of RuBP**. Fixation of three CO2 to one net glyceraldehyde-3-phosphate requires nine ATP and six NADPH. Rubisco and PRK are the most diagnostic enzymes; much of the remaining chemistry overlaps glycolysis, gluconeogenesis, and the pentose-phosphate pathway. (berg2011ecologicalaspectsof pages 3-4, wang2023microbialconversionand pages 2-3, meloni2023ribulose15bisphosphateregenerationin pages 1-2, prywes2023rubiscofunctionevolution pages 10-13)

The CBB cycle is quantitatively the dominant autotrophic pathway and occurs in cyanobacteria and diverse Proteobacteria, among other bacteria. It can be powered by oxygenic photosynthesis or by chemolithotrophic oxidation of compounds such as H2, reduced sulfur, Fe(II), ammonia, or nitrite. A 2024 environmental synthesis estimated that CBB accounts for **>99% of planetary autotrophy**, although that estimate is dominated by oxygenic phototrophs rather than microbes alone. (berg2011ecologicalaspectsof pages 2-3, harrison2024prevalenceofthe pages 1-5)

### Inclusion and exclusion boundaries

**Include:** complete native or engineered CBB operation; Rubisco carboxylation; ATP/NADPH-dependent 3-PGA reduction; RuBP regeneration through PRK; directly supporting carbon-concentrating mechanisms (CCMs), activases, regulators, and phosphoglycolate salvage when represented as modifiers.

**Do not infer the trait from Rubisco alone.** Forms III and some II/III Rubiscos can participate in nucleoside salvage or other pathways, while Form IV Rubisco-like proteins generally do not carboxylate RuBP. Proteobacteria may encode several Rubisco forms, so gene context and PRK evidence are important. (prywes2023rubiscofunctionevolution pages 10-13, harrison2024prevalenceofthe pages 1-5)

**Nearby but distinct traits/processes:**

1. rTCA, Wood–Ljungdahl, 3-hydroxypropionate, 3HP/4HB, DC/4HB, reductive-glycine, and synthetic carbon-fixation cycles.
2. Isolated anaplerotic CO2 incorporation by PEP or pyruvate carboxylase.
3. C4 and CAM carbon-concentrating adaptations, which deliver CO2 to CBB but are not the CBB cycle itself.
4. Carboxysomes and bicarbonate uptake: supporting CCM modules, not universal defining components.
5. Rubisco oxygenation and phosphoglycolate salvage: competing/repair processes, not positive evidence of productive CBB flux.
6. Photoheterotrophic CBB activity as an electron sink: genuine cycle activity, but not necessarily autotrophic growth. (berg2011ecologicalaspectsof pages 3-4, berg2011ecologicalaspectsof pages 2-3)

## Candidate nodes

### Core pathway and processes

- Calvin–Benson–Bassham cycle — `traitmech:000020`; candidate cross-reference **KEGG:M00165**.
- Carbon fixation / carbon assimilation — candidate **GO:0015977**.
- Carboxylation, reduction, and RuBP-regeneration phases.
- Photorespiration/phosphoglycolate salvage — modifier or competing pathway, not part of the positive trait core.
- Carbon-concentrating mechanism — label-only unless a validated ontology term is selected.

### Genes, proteins, enzymes, and complexes

- **Rubisco**; bacterial genes `rbcL/rbcS` or `cbbL/cbbS`, Form-II `cbbM`; **EC:4.1.1.39**, **KEGG:K01601**.
- **Phosphoribulokinase**; `prk`, `prkA`, or `cbbP`; **EC:2.7.1.19**, **KEGG:K00855**.
- Phosphoglycerate kinase, **EC:2.7.2.3**.
- NAD(P)-dependent glyceraldehyde-3-phosphate dehydrogenase; curate the taxon-appropriate isoenzyme only after sequence/context validation.
- Fructose-bisphosphate aldolase, **EC:4.1.2.13**.
- Fructose-1,6-bisphosphatase, **EC:3.1.3.11**.
- Transketolase, **EC:2.2.1.1**.
- Ribose-5-phosphate isomerase; ribulose-phosphate 3-epimerase; sedoheptulose-bisphosphatase or bifunctional FBPase/SBPase where taxonomically appropriate.
- Rubisco activases/chaperones CbbQ, CbbX, and RbcX — accessory and non-universal. Comparative genomics associates CbbQ/CbbX and several regeneration enzymes with CBB-positive genomes. (asplundsamuelsson2021widerangeof pages 12-13, asplundsamuelsson2021widerangeof pages 8-11, asplundsamuelsson2021widerangeof pages 7-8)
- CbbR — bacterial cbb-regulon transcriptional regulator; taxon-specific.
- Cyanobacterial CcmR/NdhR, CmpR, CyAbrB2, and RbcR — CCM/carboxysome regulators, not universal CBB regulators.
- Cyanobacterial phosphoketolase SeXPK — negative flux branch under low ATP in *Synechococcus elongatus* PCC 7942. (lu2023anatpsensitivephosphoketolase pages 1-2)

### Chemicals and metabolites

- Carbon dioxide, bicarbonate, oxygen.
- RuBP, ribulose-5-phosphate, 3-PGA, 1,3-bisphosphoglycerate, glyceraldehyde-3-phosphate.
- Ribose-5-phosphate, xylulose-5-phosphate, fructose-6-phosphate, fructose-1,6-bisphosphate, sedoheptulose-7-phosphate, erythrose-4-phosphate.
- ATP/ADP, NADPH/NADP+.
- 2-phosphoglycolate and glycolate as oxygenation/salvage intermediates.

Use ChEBI identifiers only after direct registry verification during YAML authoring; this search did not independently validate exact ChEBI CURIEs for every metabolite.

### Transporters, compartments, and environmental nodes

- Carboxysome; alpha- and beta-carboxysomes should be distinguished.
- Carboxysomal shell proteins CcmK/CcmL or CsoS proteins; carboxysomal carbonic anhydrase.
- Cyanobacterial bicarbonate transporters SbtA, BicA, and BCT1.
- Specialized cyanobacterial NDH-1₃/NDH-1₄ CO2-uptake complexes.
- Cytoplasm and carboxysome lumen/interior.
- Light, CO2 concentration, O2 concentration, temperature, ATP availability, and inorganic electron donors.

These CCM components raise CO2 near Rubisco but are absent from many valid CBB organisms. In cyanobacteria, HCO3− enters through shell pores, carbonic anhydrase generates CO2 inside the carboxysome, and Rubisco produces 3-PGA. (kurkela2024inorganiccarbonsensing pages 6-6, claassens2016harnessingthepower pages 8-9, asplundsamuelsson2021widerangeof pages 12-13)

## Candidate causal edges

The following compact graph summarizes the strongest candidates; the detailed evidence notes below should control curation decisions.

| subject | predicate | object | confidence/scope | key reference DOI |
|---|---|---|---|---|
| CO2 + ribulose-1,5-bisphosphate (RuBP) | is converted by Rubisco into | 2 x 3-phosphoglycerate (3-PGA) | High; core CBB reaction across native CBB users (liang2020recentadvancesin pages 2-3, harrison2024prevalenceofthe pages 1-5) | 10.3389/fmicb.2020.592631 |
| ATP + NADPH | drive reduction of | 3-PGA to glyceraldehyde-3-phosphate (G3P) | High; core CBB reduction phase (liang2020recentadvancesin pages 2-3, lu2023anatpsensitivephosphoketolase pages 1-2) | 10.3389/fmicb.2020.592631 |
| phosphoribulokinase (PRK) + ATP | regenerates | RuBP from ribulose-5-phosphate (Ru5P) | High; core CBB-defining step, required with Rubisco for complete cycle (meloni2023ribulose15bisphosphateregenerationin pages 1-2, prywes2023rubiscofunctionevolution pages 10-13, liang2020recentadvancesin pages 2-3) | 10.3389/fpls.2023.1130430 |
| Rubisco oxygenase activity | produces | 2-phosphoglycolate | High; side reaction competing with carboxylation (liang2020recentadvancesin pages 2-3, harrison2024prevalenceofthe pages 1-5) | 10.3389/fmicb.2020.592631 |
| 2-phosphoglycolate | inhibits / lowers efficiency of | carbon fixation by the CBB cycle | High; broad but often discussed via photorespiratory burden (liang2020recentadvancesin pages 2-3, harrison2024prevalenceofthe pages 1-5) | 10.1101/2024.08.01.606197 |
| bicarbonate transporters (e.g., SbtA, BicA, BCT1) | increase intracellular supply of | HCO3- for CCM/carboxysome function | High; cyanobacteria-specific CCM edge (kurkela2024inorganiccarbonsensing pages 6-6) | 10.1111/ppl.14140 |
| carboxysomal carbonic anhydrase | converts | HCO3- to CO2 inside carboxysomes | High; cyanobacteria/proteobacterial carboxysome CCM (kurkela2024inorganiccarbonsensing pages 6-6, claassens2016harnessingthepower pages 8-9, asplundsamuelsson2021widerangeof pages 12-13) | 10.1111/ppl.14140 |
| carboxysome | concentrates | CO2 around Rubisco | High; cyanobacteria and some proteobacteria (kurkela2024inorganiccarbonsensing pages 6-6, claassens2016harnessingthepower pages 8-9, asplundsamuelsson2021widerangeof pages 12-13, prywes2023rubiscofunctionevolution pages 8-10) | 10.1111/ppl.14140 |
| low ATP | relieves inhibition of | SeXPK phosphoketolase | High; cyanobacteria-specific regulatory edge in Synechococcus elongatus PCC 7942 (lu2023anatpsensitivephosphoketolase pages 1-2) | 10.1038/s42255-023-00831-w |
| SeXPK phosphoketolase | diverts RuBP-regeneration intermediates away from | the CBB cycle | High; cyanobacteria-specific regulatory edge in Synechococcus elongatus PCC 7942 (lu2023anatpsensitivephosphoketolase pages 1-2) | 10.1038/s42255-023-00831-w |
| xpk deletion | increases | CO2 fixation (~60% in high-density cultures) | High; cyanobacteria-specific phenotype, not universal (lu2023anatpsensitivephosphoketolase pages 1-2) | 10.1038/s42255-023-00831-w |
| light-activated rhodopsin proton pumping + extracellular electron uptake (MtrCAB) | powers ATP synthesis and NAD(P)H regeneration for | CO2 fixation/biomass synthesis in engineered Cupriavidus necator | High; engineering-specific, non-native energy input architecture (tu2023engineeringartificialphotosynthesis pages 1-2) | 10.1038/s41467-023-43524-4 |
| overexpressed beta-carbonic anhydrase in engineered Cupriavidus necator | enhances | CO2 fixation | Medium-High; engineering-specific enhancement (tu2023engineeringartificialphotosynthesis pages 1-2) | 10.1038/s41467-023-43524-4 |
| heterologous PRK + Rubisco in engineered Escherichia coli / E. coli Nissle | enable | non-native CBB-type CO2 assimilation | High; engineering-specific, not evidence of native trait in host (prywes2023rubiscofunctionevolution pages 10-13, effendi2024nonnativepathwayengineering pages 1-3) | 10.1021/acssynbio.4c00318 |
| CRISPRi of pfkAB and zwf in engineered E. coli Nissle | redirects carbon flux to strengthen | non-native CO2 fixation | Medium-High; engineering-specific tuning of introduced pathway (effendi2024nonnativepathwayengineering pages 1-3) | 10.1021/acssynbio.4c00318 |


*Table: This table summarizes the strongest curation-ready causal edges for the Calvin-Benson-Bassham cycle trait, including core chemistry, carbon-concentrating mechanisms, regulation, and engineering-specific augmentations. It is useful for selecting high-confidence nodes and edges for a TraitMech causal graph while keeping cyanobacterial and synthetic-biology claims clearly separated.*

### Detailed evidence table

| Subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---|---|---|
| CO2 + RuBP — **substrates_of** → Rubisco carboxylation | Harrison et al. 2024: Rubisco “catalyzes the step in which CO2 is added to…RuBP to form two 3-phosphoglycerate molecules.” DOI: [10.1101/2024.08.01.606197](https://doi.org/10.1101/2024.08.01.606197). (harrison2024prevalenceofthe pages 1-5) | **High confidence, core.** The paper is a preprint, but the reaction is established independently by reviews. |
| Rubisco — **catalyzes_production_of** → 2 3-PGA | Same direct reaction statement; Berg also identifies Rubisco carboxylation as the entry reaction. (berg2011ecologicalaspectsof pages 3-4, harrison2024prevalenceofthe pages 1-5) | **High confidence, core.** Represent stoichiometry if the graph schema permits. |
| ATP + NADPH — **enables_reduction_of** → 3-PGA to G3P | Lu et al. 2023: “Subsequent steps require ATP and NADPH to reduce 3PG to glyceraldehyde-3-phosphate.” DOI: [10.1038/s42255-023-00831-w](https://doi.org/10.1038/s42255-023-00831-w). (lu2023anatpsensitivephosphoketolase pages 1-2) | **High confidence, core.** More detailed edges can connect phosphoglycerate kinase and GAPDH to their immediate reactions. |
| PRK + ATP — **converts** → Ru5P to RuBP | Meloni et al. 2023: PRK performs the “ATP-dependent final step converting ribulose-5-phosphate to RuBP.” DOI: [10.3389/fpls.2023.1130430](https://doi.org/10.3389/fpls.2023.1130430). (meloni2023ribulose15bisphosphateregenerationin pages 1-2) | **High confidence, core.** Although this review emphasizes photosynthetic organisms, the reaction is conserved in bacterial CBB cycles. |
| CBB cycle — **consumes_per_net_G3P** → 3 CO2 + 9 ATP + 6 NADPH | Berg reports nine ATP and six NADPH per G3P; Wang et al. state the same stoichiometry for three CO2. (berg2011ecologicalaspectsof pages 3-4, wang2023microbialconversionand pages 2-3) | **High confidence.** Best represented as pathway stoichiometry rather than three binary causal edges if supported by the schema. |
| O2 — **competes_with** → CO2 at Rubisco | Rubisco is competitively inhibited by oxygen; Forms differ in specificity. (liang2020recentadvancesin pages 2-3, liang2020recentadvancesin pages 3-5, harrison2024prevalenceofthe pages 1-5) | **High confidence.** Kinetics are Rubisco-form and environment dependent. |
| Rubisco oxygenase activity — **produces** → 2-phosphoglycolate | Harrison et al.: oxygen competition results in “2-phosphoglycolate…whose removal results in the loss of recently fixed carbon.” (harrison2024prevalenceofthe pages 1-5) | **High confidence, competing branch.** Do not model 2-PG as a normal productive CBB intermediate. |
| 2-phosphoglycolate salvage — **causes_loss_of** → recently fixed carbon | Same source reports carbon loss; up to 49% of gross primary production may be lost in plants. (harrison2024prevalenceofthe pages 1-5) | **Mechanism high confidence; numerical value not microbial.** Do not transfer the 49% statistic to bacteria. |
| Bicarbonate transporters — **increase_supply_of** → cytosolic HCO3− | Kurkela & Tyystjärvi 2024 identify SbtA, BicA, and BCT1 as components that collect inorganic carbon under low Ci. DOI: [10.1111/ppl.14140](https://doi.org/10.1111/ppl.14140). (kurkela2024inorganiccarbonsensing pages 6-6) | **High confidence, cyanobacteria-specific CCM.** Not a defining edge for all CBB users. |
| HCO3− — **passes_through** → CcmK shell pores | The same review states that HCO3− enters carboxysomes through CcmK hexamer pores. (kurkela2024inorganiccarbonsensing pages 6-6) | **High confidence, beta-carboxysome/cyanobacterial context.** Avoid generalizing CcmK to alpha-carboxysomes. |
| Carboxysomal carbonic anhydrase — **converts** → HCO3− to CO2 | Directly described for the cyanobacterial carboxysome. (kurkela2024inorganiccarbonsensing pages 6-6) | **High confidence, CCM accessory.** |
| Carboxysome — **increases_local_concentration_of** → CO2 around Rubisco | Reviews describe Rubisco/carbonic-anhydrase microcompartments that concentrate CO2; bicarbonate-transporter engineering nearly doubled biomass at atmospheric CO2 in one *Synechocystis* context. (claassens2016harnessingthepower pages 8-9, asplundsamuelsson2021widerangeof pages 12-13, prywes2023rubiscofunctionevolution pages 8-10) | **High confidence mechanism; performance taxon/construct-specific.** |
| Low ATP — **relieves_allosteric_inhibition_of** → SeXPK | Lu et al. 2023 found that two ATP molecules bind a two-subunit allosteric site and suppress SeXPK until ATP falls. (lu2023anatpsensitivephosphoketolase pages 1-2) | **High confidence, strain-specific.** Curate only under *S. elongatus* PCC 7942 or an appropriately qualified clade. |
| SeXPK — **diverts** → F6P/Xu5P/S7P from RuBP regeneration | SeXPK consumes regeneration intermediates to make acetyl phosphate and shorter sugar phosphates. (lu2023anatpsensitivephosphoketolase pages 1-2) | **High confidence, negative regulatory branch.** |
| `xpk` deletion — **increases** → CBB carbon fixation | The deletion strain showed a **60% increase** in high-density cultures and secreted sucrose. (lu2023anatpsensitivephosphoketolase pages 1-2) | **Strong experimental phenotype but assay-specific.** Do not encode as a universal gene-function relation. |
| Photosystems/electron transport — **produce** → ATP and NADPH — **support** → cyanobacterial CBB | Lu et al. describe solar-energy-driven water splitting and electron transport producing ATP/NADPH for CBB fixation. (lu2023anatpsensitivephosphoketolase pages 1-2) | **High confidence, oxygenic phototrophs only.** Energy source should be modular rather than intrinsic to CBB. |
| GR rhodopsin + MtrCAB + cathodic electrons — **drive** → ATP/NAD(P)H production — **supports** → CBB-based biomass synthesis | Tu et al. 2023 engineered *C. necator*: GR supplied proton motive force, MtrCAB supplied electrons, and reverse ETC regenerated reducing power. DOI: [10.1038/s41467-023-43524-4](https://doi.org/10.1038/s41467-023-43524-4). (tu2023engineeringartificialphotosynthesis pages 1-2) | **Engineering-specific.** Place in an application extension, not the canonical trait core. |
| Heterologous PRK + Rubisco — **enables** → CBB-type CO2 assimilation in *E. coli* | *E. coli* lacks only PRK and Rubisco among core CBB functions because the remaining reactions can be supplied by native central metabolism. (prywes2023rubiscofunctionevolution pages 10-13, prywes2023rubiscofunctionevolution pages 8-10) | **High confidence concept.** Full autotrophy additionally requires energy/redox rewiring and selection. |
| CRISPRi of `pfkAB` and `zwf` — **redirects_flux_toward** → engineered CO2 assimilation | Effendi & Ng 2024 reconstructed Ru5P and R15P routes; the Ru5P design suppressed CO2 release by **77%**. DOI: [10.1021/acssynbio.4c00318](https://doi.org/10.1021/acssynbio.4c00318). (effendi2024nonnativepathwayengineering pages 1-3) | **Do not curate as canonical CBB.** This is glucose-supported, non-native assimilation; the R15P route is explicitly not the conventional CBB cycle. |
| CBB-responsive promoters — **drive_expression_during** → autotrophic *C. necator* cultivation | Arhar et al. 2024 used CBB and hydrogenase promoters for phytase production; activities were 2–50 U mg−1 and reached 22 U mL−1 in a 1-L fed-batch gas fermentation. DOI: [10.1186/s12934-023-02280-2](https://doi.org/10.1186/s12934-023-02280-2). (arhar2024co2basedproductionof pages 1-2) | **Application evidence**, not a pathway-mechanism edge unless promoter identities and direct regulatory relationships are extracted from the full experiment. |

## Recent research and applications, 2023–2024

1. **Flux regulation:** Lu et al. discovered an ATP-sensing phosphoketolase switch in *S. elongatus*. The 60% fixation increase after `xpk` deletion shows that regeneration-phase drains, not only Rubisco kinetics, can constrain pathway output. This supports expert views that CBB engineering should address network regulation and RuBP regeneration as well as Rubisco. (meloni2023ribulose15bisphosphateregenerationin pages 1-2, lu2023anatpsensitivephosphoketolase pages 1-2)

2. **Low-Ci sensing and CCM regulation:** A 2024 review integrated SbtA/BicA/BCT1 transport, specialized NDH complexes, carboxysomes, and regulators CcmR, CmpR, CyAbrB2, and RbcR. It also identified 2-phosphoglycolate as a low-Ci signal, illustrating that Rubisco’s side product participates in acclimation rather than acting only as waste. (kurkela2024inorganiccarbonsensing pages 6-6)

3. **Engineered carbon-recycling cell factories:** In *E. coli* Nissle, non-native Ru5P/Rubisco assimilation combined with CRISPRi reduced CO2 release during 5-aminolevulinate production by 77%. This is a real implementation of CBB-derived enzymology, but not evidence that the host performs native autotrophic CBB growth. (effendi2024nonnativepathwayengineering pages 1-3)

4. **Gas fermentation:** Native CBB metabolism in *C. necator* is being used to convert CO2 into biomass, PHAs, proteins, and enzymes. A 2024 1-L demonstration produced phytase at up to 22 U mL−1 using autotrophy-responsive expression systems. (arhar2024co2basedproductionof pages 1-2)

5. **Photoelectrosynthesis:** Engineered *C. necator* combined cathodic electron uptake through MtrCAB with light-driven rhodopsin proton pumping, ATP synthesis, reverse electron transport, and carbonic-anhydrase enhancement. This demonstrates that CBB carbon assimilation can be decoupled from its native H2 energy supply and connected to synthetic light/electrode modules. (tu2023engineeringartificialphotosynthesis pages 1-2)

6. **Extreme-environment ecology:** A 2024 preprint found CBB to be the dominant predicted chemolithoautotrophic pathway in Arctic cryopeg brines and first-year sea ice, reconstructing four candidate chemolithoautotrophic MAGs. Form-II Rubisco was modeled to outperform Form I at low O2, but cold reduced that advantage. These are genomic/modeling results, not direct flux measurements. (harrison2024prevalenceofthe pages 1-5)

### Relevant quantitative context

- Canonical stoichiometry: **3 CO2 + 9 ATP + 6 NADPH per net G3P**. (berg2011ecologicalaspectsof pages 3-4, wang2023microbialconversionand pages 2-3)
- Rubisco turnover reported across forms: approximately **1–12 s−1**, illustrating the central kinetic bottleneck. (berg2011ecologicalaspectsof pages 2-3)
- Comparative genomic survey: **6.0% of thousands of microbial genomes** contained both diagnostic Calvin-cycle genes under the study’s criteria. This is genomic potential, not measured activity. (asplundsamuelsson2021widerangeof pages 12-13)
- In vitro Rubisco activity may peak at **45–60°C**; at 15°C it was estimated at **4–13%** of peak in the cited synthesis. Generalization depends on Rubisco form. (harrison2024prevalenceofthe pages 1-5)
- Form-I bacterial Rubisco specificity factors of **25–75** versus **10–15** for Form II were reported in an engineering review. These are broad ranges, not universal constants. (liang2020recentadvancesin pages 3-5)

## Recommended graph architecture

For `data/traits/metabolism/calvin_benson_bassham_cycle.yaml`, retain a compact **universal core**:

1. CO2 + RuBP → Rubisco → 3-PGA.
2. ATP/NADPH → reduction module → G3P.
3. Pentose rearrangement module → Ru5P.
4. Ru5P + ATP → PRK → RuBP.
5. G3P → biomass precursors/net fixed carbon.
6. O2 → Rubisco oxygenation → 2-phosphoglycolate → reduced net fixation.

Attach optional qualified modules for:

- cyanobacterial or proteobacterial carboxysomes/CCMs;
- Rubisco activases;
- CbbR or cyanobacterial low-Ci transcriptional regulation;
- phosphoglycolate salvage;
- taxon-specific phosphoketolase regulation;
- photosynthetic, H2-driven, sulfur-driven, or electrode/rhodopsin energy supply.

This modular design avoids incorrectly asserting that carboxysomes, oxygenic photosynthesis, a particular Rubisco form, or a specific electron donor is universal.

## Warnings: claims not yet suitable for unqualified curation

1. **Do not use `rbcL`, `cbbM`, or a Rubisco annotation alone as sufficient evidence.** Require PRK and preferably pathway completeness, gene context, or physiological/isotope evidence.
2. **Do not treat Form IV Rubisco-like proteins as CBB enzymes.** Form III and II/III assignments also require pathway context. (prywes2023rubiscofunctionevolution pages 10-13, harrison2024prevalenceofthe pages 1-5)
3. **Do not make carboxysomes obligatory.** They are important CCMs in cyanobacteria and some Proteobacteria but are not universal.
4. **Do not generalize cyanobacterial regulators or SeXPK.** Their edges require taxonomic qualifiers.
5. **Do not call reduced CO2 release equivalent to autotrophy.** The 2024 *E. coli* Nissle implementation remained glucose-supported and included an R15P route distinct from CBB. (effendi2024nonnativepathwayengineering pages 1-3)
6. **Do not curate metagenome pathway calls as demonstrated physiology.** MAG completeness, gene annotation, and environmental expression/flux need independent validation.
7. **Do not transfer plant photorespiration statistics to microbes.** The reported 49% loss is a plant-context upper estimate. (harrison2024prevalenceofthe pages 1-5)
8. **Verify ontology records directly before YAML insertion.** One automated source excerpt swapped the EC assignments of Rubisco and PRK; the correct assignments are Rubisco **EC:4.1.1.39** and PRK **EC:2.7.1.19**. Stable identifiers not directly verified should remain label-only rather than being guessed.

## DOI-first bibliography

1. Lu K-J et al. **An ATP-sensitive phosphoketolase regulates carbon fixation in cyanobacteria.** *Nature Metabolism*. Published 22 June 2023. DOI: [10.1038/s42255-023-00831-w](https://doi.org/10.1038/s42255-023-00831-w). (lu2023anatpsensitivephosphoketolase pages 1-2)
2. Meloni M et al. **Ribulose-1,5-bisphosphate regeneration in the Calvin-Benson-Bassham cycle.** *Frontiers in Plant Science*. Published February 2023. DOI: [10.3389/fpls.2023.1130430](https://doi.org/10.3389/fpls.2023.1130430). (meloni2023ribulose15bisphosphateregenerationin pages 1-2)
3. Tu W et al. **Engineering artificial photosynthesis based on rhodopsin for CO2 fixation.** *Nature Communications*. Accepted 11 November 2023; published December 2023. DOI: [10.1038/s41467-023-43524-4](https://doi.org/10.1038/s41467-023-43524-4). (tu2023engineeringartificialphotosynthesis pages 1-2)
4. Kurkela J, Tyystjärvi T. **Inorganic carbon sensing and signalling in cyanobacteria.** *Physiologia Plantarum*. January 2024. DOI: [10.1111/ppl.14140](https://doi.org/10.1111/ppl.14140). (kurkela2024inorganiccarbonsensing pages 6-6)
5. Effendi SSW, Ng I-S. **Non-native Pathway Engineering with CRISPRi for Carbon Dioxide Assimilation and Valued 5-Aminolevulinic Acid Synthesis in Escherichia coli Nissle.** *ACS Synthetic Biology*. Published 2 July 2024. DOI: [10.1021/acssynbio.4c00318](https://doi.org/10.1021/acssynbio.4c00318). (effendi2024nonnativepathwayengineering pages 1-3)
6. Arhar S et al. **CO2-based production of phytase from highly stable expression plasmids in Cupriavidus necator H16.** *Microbial Cell Factories*. January 2024. DOI: [10.1186/s12934-023-02280-2](https://doi.org/10.1186/s12934-023-02280-2). (arhar2024co2basedproductionof pages 1-2)
7. Harrison K et al. **Prevalence of the Calvin-Benson-Bassham cycle in chemolithoautotrophic psychrophiles and the potential for cold-adapted Rubisco.** bioRxiv preprint, posted August 2024. DOI: [10.1101/2024.08.01.606197](https://doi.org/10.1101/2024.08.01.606197). (harrison2024prevalenceofthe pages 1-5)
8. Prywes N et al. **Rubisco Function, Evolution, and Engineering.** *Annual Review of Biochemistry*. July 2023. Retrieved manuscript DOI: [10.48550/arXiv.2207.10773](https://doi.org/10.48550/arXiv.2207.10773). The final journal DOI should be verified before database deposition. (prywes2023rubiscofunctionevolution pages 10-13, prywes2023rubiscofunctionevolution pages 8-10)
9. Asplund-Samuelsson J, Hudson EP. **Wide range of metabolic adaptations to the acquisition of the Calvin cycle revealed by comparison of microbial genomes.** *PLOS Computational Biology*. February 2021. DOI: [10.1371/journal.pcbi.1008742](https://doi.org/10.1371/journal.pcbi.1008742). (asplundsamuelsson2021widerangeof pages 12-13, asplundsamuelsson2021widerangeof pages 8-11, asplundsamuelsson2021widerangeof pages 7-8)
10. Berg IA. **Ecological Aspects of the Distribution of Different Autotrophic CO2 Fixation Pathways.** *Applied and Environmental Microbiology*. March 2011. DOI: [10.1128/AEM.02473-10](https://doi.org/10.1128/AEM.02473-10). (berg2011ecologicalaspectsof pages 3-4, berg2011ecologicalaspectsof pages 2-3)
11. Claassens NJ et al. **Harnessing the power of microbial autotrophy.** *Nature Reviews Microbiology*. September 2016. DOI: [10.1038/nrmicro.2016.130](https://doi.org/10.1038/nrmicro.2016.130). (claassens2016harnessingthepower pages 8-9)
12. Liang B et al. **Recent Advances in Developing Artificial Autotrophic Microorganism for Reinforcing CO2 Fixation.** *Frontiers in Microbiology*. November 2020. DOI: [10.3389/fmicb.2020.592631](https://doi.org/10.3389/fmicb.2020.592631). (liang2020recentadvancesin pages 2-3, liang2020recentadvancesin pages 3-5)

References

1. (berg2011ecologicalaspectsof pages 3-4): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

2. (wang2023microbialconversionand pages 2-3): Ge-Ge Wang, Zhang Yuan, Xiao-Yan Wang, and Gen-Lin Zhang. Microbial conversion and utilization of co2. Annals of Civil and Environmental Engineering, 7:045-060, Sep 2023. URL: https://doi.org/10.29328/journal.acee.1001055, doi:10.29328/journal.acee.1001055. This article has 3 citations.

3. (meloni2023ribulose15bisphosphateregenerationin pages 1-2): Maria Meloni, Libero Gurrieri, Simona Fermani, Lauren Velie, Francesca Sparla, Pierre Crozet, Julien Henri, and Mirko Zaffagnini. Ribulose-1,5-bisphosphate regeneration in the calvin-benson-bassham cycle: focus on the last three enzymatic steps that allow the formation of rubisco substrate. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1130430, doi:10.3389/fpls.2023.1130430. This article has 52 citations.

4. (prywes2023rubiscofunctionevolution pages 10-13): Noam Prywes, Naiya R Phillips, Owen T Tuck, Luis E Valentin-Alvarado, and David F Savage. Rubisco function, evolution, and engineering. Annual review of biochemistry, Jul 2023. URL: https://doi.org/10.48550/arxiv.2207.10773, doi:10.48550/arxiv.2207.10773. This article has 198 citations and is from a domain leading peer-reviewed journal.

5. (berg2011ecologicalaspectsof pages 2-3): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

6. (harrison2024prevalenceofthe pages 1-5): Kaitlin Harrison, Josephine Z. Rapp, Alexander L. Jaffe, Jody W. Deming, and Jodi Young. Prevalence of the calvin-benson-bassham cycle in chemolithoautotrophic psychrophiles and the potential for cold-adapted rubisco. BioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.01.606197, doi:10.1101/2024.08.01.606197. This article has 1 citations.

7. (asplundsamuelsson2021widerangeof pages 12-13): Johannes Asplund-Samuelsson and Elton P. Hudson. Wide range of metabolic adaptations to the acquisition of the calvin cycle revealed by comparison of microbial genomes. PLOS Computational Biology, 17:e1008742, Feb 2021. URL: https://doi.org/10.1371/journal.pcbi.1008742, doi:10.1371/journal.pcbi.1008742. This article has 40 citations and is from a highest quality peer-reviewed journal.

8. (asplundsamuelsson2021widerangeof pages 8-11): Johannes Asplund-Samuelsson and Elton P. Hudson. Wide range of metabolic adaptations to the acquisition of the calvin cycle revealed by comparison of microbial genomes. PLOS Computational Biology, 17:e1008742, Feb 2021. URL: https://doi.org/10.1371/journal.pcbi.1008742, doi:10.1371/journal.pcbi.1008742. This article has 40 citations and is from a highest quality peer-reviewed journal.

9. (asplundsamuelsson2021widerangeof pages 7-8): Johannes Asplund-Samuelsson and Elton P. Hudson. Wide range of metabolic adaptations to the acquisition of the calvin cycle revealed by comparison of microbial genomes. PLOS Computational Biology, 17:e1008742, Feb 2021. URL: https://doi.org/10.1371/journal.pcbi.1008742, doi:10.1371/journal.pcbi.1008742. This article has 40 citations and is from a highest quality peer-reviewed journal.

10. (lu2023anatpsensitivephosphoketolase pages 1-2): Kuan-Jen Lu, Chiung-Wen Chang, Chun-Hsiung Wang, Frederic Y-H Chen, Irene Y. Huang, Pin-Hsuan Huang, Cheng-Han Yang, Hsiang-Yi Wu, Wen-Jin Wu, Kai-Cheng Hsu, Meng-Chiao Ho, and Ming-Daw Tsai. An atp-sensitive phosphoketolase regulates carbon fixation in cyanobacteria. Nature Metabolism, 5:1111-1126, Jun 2023. URL: https://doi.org/10.1038/s42255-023-00831-w, doi:10.1038/s42255-023-00831-w. This article has 37 citations and is from a domain leading peer-reviewed journal.

11. (kurkela2024inorganiccarbonsensing pages 6-6): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 16 citations and is from a peer-reviewed journal.

12. (claassens2016harnessingthepower pages 8-9): Nico J. Claassens, Diana Z. Sousa, Vitor A. P. Martins dos Santos, Willem M. de Vos, and John van der Oost. Harnessing the power of microbial autotrophy. Nature Reviews Microbiology, 14:692-706, Sep 2016. URL: https://doi.org/10.1038/nrmicro.2016.130, doi:10.1038/nrmicro.2016.130. This article has 333 citations and is from a highest quality peer-reviewed journal.

13. (liang2020recentadvancesin pages 2-3): Bo Liang, Yukun Zhao, and Jianming Yang. Recent advances in developing artificial autotrophic microorganism for reinforcing co2 fixation. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.592631, doi:10.3389/fmicb.2020.592631. This article has 64 citations and is from a peer-reviewed journal.

14. (prywes2023rubiscofunctionevolution pages 8-10): Noam Prywes, Naiya R Phillips, Owen T Tuck, Luis E Valentin-Alvarado, and David F Savage. Rubisco function, evolution, and engineering. Annual review of biochemistry, Jul 2023. URL: https://doi.org/10.48550/arxiv.2207.10773, doi:10.48550/arxiv.2207.10773. This article has 198 citations and is from a domain leading peer-reviewed journal.

15. (tu2023engineeringartificialphotosynthesis pages 1-2): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 76 citations and is from a highest quality peer-reviewed journal.

16. (effendi2024nonnativepathwayengineering pages 1-3): Sefli Sri Wahyu Effendi and I-Son Ng. Non-native pathway engineering with crispri for carbon dioxide assimilation and valued 5-aminolevulinic acid synthesis in escherichia coli nissle. ACS Synthetic Biology, 13:2038-2044, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00318, doi:10.1021/acssynbio.4c00318. This article has 10 citations and is from a domain leading peer-reviewed journal.

17. (liang2020recentadvancesin pages 3-5): Bo Liang, Yukun Zhao, and Jianming Yang. Recent advances in developing artificial autotrophic microorganism for reinforcing co2 fixation. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.592631, doi:10.3389/fmicb.2020.592631. This article has 64 citations and is from a peer-reviewed journal.

18. (arhar2024co2basedproductionof pages 1-2): Simon Arhar, Thomas Rauter, Holly Stolterfoht-Stock, Vera Lambauer, Regina Kratzer, Margit Winkler, Marianna Karava, Robert Kourist, and Anita Emmerstorfer-Augustin. Co2-based production of phytase from highly stable expression plasmids in cupriavidus necator h16. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02280-2, doi:10.1186/s12934-023-02280-2. This article has 24 citations and is from a peer-reviewed journal.