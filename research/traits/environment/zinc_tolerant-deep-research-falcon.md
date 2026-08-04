---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:40:01.763951'
end_time: '2026-08-04T04:47:09.866820'
duration_seconds: 428.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: zinc tolerant
  trait_identifier: traitmech:000014
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: zinc_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such
    as the czc determinant.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc
    to a MIC of 20 mM.)'
  causal_graph_summary: 'zinc_tolerance_czc_efflux: 11 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** zinc tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000014
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc to a MIC of 20 mM.)
- **Existing causal graph summary:** zinc_tolerance_czc_efflux: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **zinc tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/zinc_tolerant.yaml`.

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
- **Trait label:** zinc tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000014
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc to a MIC of 20 mM.)
- **Existing causal graph summary:** zinc_tolerance_czc_efflux: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **zinc tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/zinc_tolerant.yaml`.

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


# Curation report: microbial zinc tolerance

## Trait record and scope

- **Trait label:** zinc tolerant
- **Trait identifier:** `traitmech:000014`
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** `traitmech:000012`

### Recommended operational definition

This trait should denote the **capacity of a microorganism to grow or remain viable when exposed to an elevated, bioavailable Zn²⁺ concentration that inhibits an appropriate reference strain or condition**. It is an assay-observed phenotype, not simply the presence of a zinc-resistance gene. Zinc is essential at low concentration but toxic in excess; bacterial management therefore combines uptake, intracellular allocation, storage, and export in a regulated flow equilibrium. The boundary between ordinary homeostasis and “tolerance” is quantitative and assay-dependent. (butof2017thecomponentsof pages 3-5)

For curation, record at minimum the organism/strain, zinc salt, nominal concentration, medium, pH, incubation time and temperature, inoculum, endpoint, and comparator. This matters because free Zn²⁺ depends on complexation and precipitation. One recent *Cupriavidus metallidurans* study noted a Zn(OH)₂ solubility limit near 4.5 mM at neutral pH; nominal concentrations above this value cannot automatically be interpreted as freely dissolved Zn²⁺. (schulz2024theeffluxsystem pages 12-14)

A strong organism-level example is *C. metallidurans* CH34ZnR: its liquid-medium Zn²⁺ MIC was 24 mM versus 12 mM for parental CH34, and 24–25 mM Zn²⁺ was bactericidal or sharply reduced survival of the wild type. Prior exposure to 0.3 mM Zn²⁺ improved subsequent survival, consistent with inducible resistance. (houdt2021adaptationofcupriavidus pages 5-7)

### Boundary cases

1. **Basal zinc homeostasis is not automatically zinc tolerance.** A transporter that maintains zinc nutrition under ordinary conditions belongs in the graph only if perturbation evidence connects it to growth or survival under elevated zinc.
2. **Gene presence is not phenotype evidence.** `czc`, `zntA`, or CDF-family annotations can predict a mechanism, but require expression, transport, mutant, complementation, or susceptibility data for a causal edge.
3. **Biosorption, precipitation, immobilization, and bioaccumulation are distinct.** They may lower bioavailable zinc and thereby support tolerance, but tolerance alone does not establish environmental zinc removal.
4. **Cross-resistance should remain separate.** CH34ZnR displayed a twofold increase in both Zn²⁺ and Cd²⁺ MIC, but not Ni²⁺ or Co²⁺ cross-resistance; a “general heavy-metal tolerant” assertion would therefore overstate the evidence. (houdt2021adaptationofcupriavidus pages 5-7)
5. **Environmental preference is not implied.** Growth in a zinc-rich site may reflect transient survival, community protection, or low free-Zn²⁺ speciation rather than a preferred zinc concentration.

## Current mechanistic understanding

The best-supported model in Gram-negative *C. metallidurans* is **adaptive, layered efflux**. Inner-membrane ATPases and CDF proteins move cytoplasmic Zn²⁺ into the periplasm; the CzcCBA RND complex then performs trans-envelope export from the periplasm to the exterior. The layers differ in rate, substrate competition, induction threshold, and physiological role. (schulz2024theeffluxsystem pages 12-14, houdt2021adaptationofcupriavidus pages 2-4, galea2024linkingthetranscriptome pages 1-2)

The plasmid-borne Czc determinant is dominant at high zinc. CzcCBA spans the cell envelope, while CzcD and the P-type ATPase CzcP contribute earlier transport steps. The zinc-inducible module is controlled by CzcRS. Loss of pMOL30, which carries major Czc resistance determinants, drastically lowers zinc resistance. (houdt2021adaptationofcupriavidus pages 2-4, houdt2021adaptationofcupriavidus pages 1-2)

The 2024 discovery of **CdfX** materially extends the graph. A quadruple mutant lacking `zntA`, `cadA`, `dmeF`, and `fieF` retained residual zinc export; deleting `cdfX` further lowered resistance. Both radioactive ⁶⁵Zn and stable-isotope ⁶⁷Zn pulse–chase experiments assigned that residual export to CdfX. ZntR drives zinc- and cadmium-dependent `cdfX` expression, especially when ZntA or CadA is absent, making CdfX a backup layer rather than a universal primary exporter. (schulz2024theeffluxsystem pages 1-3)

Recent proteomics reinforces this dynamic model. Following metal shock, resistance genes were induced within minutes; physiological adjustment occurred over approximately 15–60 minutes. After about 1.5 cell doublings, or three hours, plasmid-encoded resistance proteins—especially CzcCBA—were among the most prominent responses. Across metal-shock and starvation comparisons, 3,540 proteins changed in abundance; 76% appeared in only one condition, while 24% were quantitatively up- or downregulated. (galea2024linkingthetranscriptome pages 1-2)

## Candidate nodes grouped by type

### Trait, organism, and assay nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| zinc tolerant | Trait class | `traitmech:000014` | Target trait; quote identifier exactly. |
| elevated extracellular Zn²⁺ exposure | Environmental/experimental factor | Zn²⁺: `CHEBI:29105` | Add concentration, salt, medium, pH, and duration as evidence qualifiers. |
| *Cupriavidus metallidurans* CH34 | Organism/strain | `NCBITaxon:266264` | Verify that this taxon record matches the intended CH34 strain in the target database version. |
| Zn²⁺ MIC | Assay endpoint | Label-only candidate | MIC is protocol-dependent, not an intrinsic universal constant. |
| high-Zn survival | Assay endpoint | Label-only candidate | Distinguish bacteriostatic growth inhibition from killing. |

### Genes, proteins, and complexes

| Node | Role | Grounding recommendation |
|---|---|---|
| CzcCBA | RND-type trans-envelope Co/Zn/Cd efflux complex | Label-only until strain-specific protein accessions are verified. Model subunits CzcA, CzcB, and CzcC separately if assembly edges are required. |
| CzcA | Inner-membrane RND transporter component | Label-only candidate. |
| CzcB | Periplasmic membrane-fusion component | Label-only candidate. |
| CzcC | Outer-membrane channel component | Label-only candidate. |
| CzcD | CDF-family secondary metal transporter | Label-only candidate; substrate and direction must be strain-qualified. |
| CzcP | PᵢB4-type ATPase; rapid cytoplasmic Zn export layer | Label-only candidate pending verified UniProt accession. |
| ZntA | PᵢB2-type ATPase; central inner-membrane zinc exporter | Label-only candidate pending verified strain accession. |
| CdfX | CDF-family backup Zn exporter | Label-only candidate; newly characterized in 2024. |
| CadA | P-type ATPase with major Cd-export role | Include because Cd/Zn competition affects the zinc-efflux network, but do not label it a primary Zn exporter without context. |
| DmeF; FieF | Broad-specificity CDF-family transporters | Secondary/backup candidates; taxon-specific substrate evidence required. |
| CzcRS | Two-component regulator of `czc` expression | Label-only candidate; represent sensor and response regulator separately if supported by the YAML schema. |
| ZntR | MerR-family Zn-responsive regulator | Label-only candidate; direct evidence supports control of `cdfX` and `zntR` expression in *C. metallidurans*. |
| CzcI | Modulator that quenches CzcCBA activity | Label-only; useful for preventing over-efflux under lower zinc, but curate only with the taxon-specific evidence. |
| GlpR | DeoR-family repressor | Label-only candidate. Its loss derepresses the adjacent transporter in CH34ZnR. |
| Rmet_2229–2234 ABC-type transporter | Adaptive resistance-associated transporter | Keep as a locus-labelled node; transported substrate and direct mechanism remain unclear. |
| ZupT | ZIP-family zinc importer | Context node for zinc starvation/homeostasis; not a zinc-tolerance effector by itself. |
| Zur | Zinc uptake regulator | Context node controlling starvation responses and cytoplasmic zinc handling. |

### Chemicals, compartments, processes, and modules

| Node | Suggested grounding | Role |
|---|---|---|
| Zn²⁺ | `CHEBI:29105` | Essential micronutrient and toxic stressor at elevated bioavailable concentration. |
| Cd²⁺ | Use a verified ChEBI identifier at implementation time | Competes within the export network and induces some shared regulators. |
| Cytoplasm | GO cellular-component term after schema verification | Source compartment for ATPase/CDF-mediated export. |
| Periplasm | GO cellular-component term after schema verification | Intermediate compartment feeding CzcCBA. |
| Plasma membrane | `GO:0005886` | Location of inner-membrane exporters. |
| Cellular zinc-ion homeostasis | `GO:0006882` | Broad homeostatic module; verify current GO label/version. |
| Zinc-ion transport | `GO:0071577` | General transport process. |
| Response to zinc ion | `GO:0010043` | Regulatory/stress response. |
| Czc-mediated trans-envelope efflux | Label-only module | High-zinc terminal export module. |
| Layered zinc-efflux network | Label-only module | Integrates ZntA/CzcP/CdfX/CzcD with CzcCBA. |

Protein and complex CURIEs should remain absent until checked against the exact CH34 proteome. Ortholog-level identifiers can silently conflate paralogs, plasmid copies, or proteins with different substrate ranges.

## Candidate causal edges

The following artifact summarizes the strongest compact graph.

| subject | predicate | object | evidence strength/taxon | DOI |
|---|---|---|---|---|
| elevated extracellular Zn2+ | induces/activates | CzcRS–czc resistance determinant expression | Strong; taxon-specific to *Cupriavidus metallidurans* CH34/AE104; primary studies show zinc-inducible czc and rapid metal-shock upregulation (houdt2021adaptationofcupriavidus pages 2-4, galea2024linkingthetranscriptome pages 1-2) | 10.3390/microorganisms9020309; 10.1093/mtomcs/mfae058 |
| CzcCBA transenvelope efflux system | exports | periplasmic Zn2+ to the extracellular space | Strong; taxon-specific to *C. metallidurans*; localization/mechanism supported by primary studies (houdt2021adaptationofcupriavidus pages 2-4, galea2024linkingthetranscriptome pages 1-2) | 10.3390/microorganisms9020309; 10.1093/mtomcs/mfae058 |
| CzcCBA transenvelope efflux system | positively_regulates/contributes_to | zinc tolerance | Strong; taxon-specific to *C. metallidurans*; prominent determinant under metal shock and central to resistance (houdt2021adaptationofcupriavidus pages 2-4, galea2024linkingthetranscriptome pages 1-2) | 10.3390/microorganisms9020309; 10.1093/mtomcs/mfae058 |
| CzcP (PIB4-type ATPase) | exports | cytoplasmic Zn2+ to the periplasm | Strong; taxon-specific to *C. metallidurans*; foundational mechanism summarized in recent studies (schulz2024theeffluxsystem pages 12-14, houdt2021adaptationofcupriavidus pages 2-4) | 10.1128/jb.00299-24; 10.3390/microorganisms9020309 |
| ZntA (PIB2-type ATPase) | exports | cytoplasmic Zn2+ to the periplasm | Strong; taxon-specific to *C. metallidurans*; recent mechanistic evidence identifies ZntA as central inner-membrane Zn exporter (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 1-3) | 10.1128/jb.00299-24 |
| CdfX (CDF family exporter) | exports | cytoplasmic Zn2+ to the periplasm | Strong; taxon-specific to *C. metallidurans*; pulse-chase evidence in 2024 paper (schulz2024theeffluxsystem pages 1-3, galea2024linkingthetranscriptome pages 1-2) | 10.1128/jb.00299-24; 10.1093/mtomcs/mfae058 |
| ZntR | activates expression of | cdfX | Strong; taxon-specific to *C. metallidurans*; Zn/Cd-dependent upregulation shown by reporter fusions, especially when ZntA/CadA are absent (schulz2024theeffluxsystem pages 1-3) | 10.1128/jb.00299-24 |
| Zn2+ and/or Cd2+ plus loss of major efflux systems | increases | ZntR-dependent cdfX expression | Strong; taxon-specific to *C. metallidurans* Δe4 background (schulz2024theeffluxsystem pages 1-3) | 10.1128/jb.00299-24 |
| cdfX deletion | decreases | zinc resistance in Δe4 (ΔzntA ΔcadA ΔdmeF ΔfieF) | Strong; taxon-specific mutant evidence in *C. metallidurans* (schulz2024theeffluxsystem pages 1-3) | 10.1128/jb.00299-24 |
| loss of megaplasmid pMOL30 | decreases | zinc resistance | Moderate-to-strong; taxon-specific to *C. metallidurans*; pMOL30 carries major zinc-resistance determinants including czc (houdt2021adaptationofcupriavidus pages 1-2) | 10.3390/microorganisms9020309 |
| glpR loss-of-function | derepresses | neighboring ABC-type transporter (Rmet_2229_2234) | Strong; taxon-specific adaptive-mutant evidence in *C. metallidurans* CH34ZnR (houdt2021adaptationofcupriavidus pages 5-7) | 10.3390/microorganisms9020309 |
| derepressed ABC-type transporter (Rmet_2229_2234) | increases | zinc tolerance | Strong; taxon-specific to *C. metallidurans* CH34ZnR; mutant/complementation evidence (houdt2021adaptationofcupriavidus pages 1-2, houdt2021adaptationofcupriavidus pages 5-7) | 10.3390/microorganisms9020309 |
| pre-induction with 0.3 mM Zn2+ | improves | survival during high-Zn challenge via prior czc induction | Strong; taxon-specific to *C. metallidurans* CH34 and CH34ZnR (houdt2021adaptationofcupriavidus pages 5-7) | 10.3390/microorganisms9020309 |


*Table: This table summarizes the best-supported, curation-ready causal edges for traitmech:000014, emphasizing experimentally supported transport and regulatory relationships in Cupriavidus metallidurans. It is useful for selecting graph edges with clear mechanistic backing and explicit taxon-specific scope.*

Additional evidence detail suitable for curator review is provided below. Snippets are short evidence extracts or faithful source summaries, not necessarily continuous verbatim quotations.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|---|
| Elevated extracellular Zn²⁺ | activates | CzcRS-dependent `czc` expression | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | “The plasmid-borne czc system is zinc-inducible” and is controlled by CzcRS. | **Strong, taxon-specific.** Do not generalize CzcRS architecture to every `czc` locus. (houdt2021adaptationofcupriavidus pages 2-4) |
| CzcCBA | transports | periplasmic Zn²⁺ to extracellular space | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | “RND systems export from periplasm to extracellular space.” | **Strong, taxon-specific.** Represents the terminal trans-envelope step. (houdt2021adaptationofcupriavidus pages 2-4) |
| CzcCBA activity | increases | zinc tolerance | DOI: [10.1093/mtomcs/mfae058](https://doi.org/10.1093/mtomcs/mfae058) | Under metal shock, “the most prominent polypeptides” included CzcCBA. | Strong physiological association; combine with pMOL30-loss evidence for causality. (galea2024linkingthetranscriptome pages 1-2) |
| Loss of pMOL30 | decreases | zinc tolerance | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | “Loss of pMOL30 drastically reduces resistance.” | **Strong but plasmid-level perturbation:** pMOL30 contains multiple determinants, so this does not isolate CzcCBA alone. (houdt2021adaptationofcupriavidus pages 1-2) |
| CzcP | exports | loosely bound cytoplasmic Zn²⁺ toward periplasm | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24); foundational DOI: [10.1111/j.1365-2958.2009.06792.x](https://doi.org/10.1111/j.1365-2958.2009.06792.x) | CzcP is described as a PᵢB4 ATPase that exports loosely bound zinc faster than ZntA. | **Strong, taxon-specific.** The exact kinetic comparison should be checked against the foundational paper before encoding a “faster than” edge. (schulz2024theeffluxsystem pages 12-14) |
| ZntA | exports | cytoplasmic Zn²⁺ toward periplasm | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24) | ZntA is the “central inner-membrane zinc efflux system.” | **Strong.** Membrane transport direction is mechanistically supported in this organism. (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 1-3) |
| CdfX | exports | cytoplasmic Zn²⁺ toward periplasm | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24) | ⁶⁵Zn and ⁶⁷Zn pulse–chase experiments assigned residual zinc efflux to CdfX. | **Very strong direct transport evidence; taxon-specific.** (schulz2024theeffluxsystem pages 1-3) |
| `cdfX` deletion in Δe4 | decreases | zinc resistance | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24) | Deleting `cdfX` from Δ`zntA cadA dmeF fieF` “resulted in a further decrease in zinc resistance.” | **Very strong mutant evidence.** Background-specific epistasis must be retained. (schulz2024theeffluxsystem pages 1-3) |
| ZntR | activates | `cdfX` expression | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24) | Reporter fusions showed ZntR-dependent, Zn/Cd-responsive `cdfX` upregulation. | **Strong regulatory evidence.** (schulz2024theeffluxsystem pages 1-3) |
| Loss/impairment of ZntA or CadA | enhances | ZntR-dependent `cdfX` induction | DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24) | Upregulation was strongest in cells lacking one or both previously characterized exporters. | **Strong but genetic-background-specific.** Model as conditional regulation, not an unconditional edge. (schulz2024theeffluxsystem pages 1-3) |
| Cytoplasmic exporters CdfX/ZntA/CzcP/CzcD | supplies Zn²⁺ to | periplasmic CzcCBA export step | DOI: [10.1093/mtomcs/mfae058](https://doi.org/10.1093/mtomcs/mfae058) | Inner-membrane exporters act “with further export via periplasmic CzcCBA.” | **Mechanistically coherent module-level edge.** Exact physical channeling is not established; use “supplies substrate to,” not “forms complex with.” (galea2024linkingthetranscriptome pages 1-2) |
| `glpR` loss-of-function | derepresses | Rmet_2229–2234 ABC transporter | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | IS1088 disruption of `glpR` caused constitutive expression of the adjacent ABC transporter. | **Strong adaptive-mutant and complementation evidence.** (houdt2021adaptationofcupriavidus pages 1-2) |
| Derepressed Rmet_2229–2234 transporter | increases | Zn²⁺ and Cd²⁺ tolerance | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | Deletion and complementation showed the transporter’s derepression was “pivotal” for the phenotype. | **Strong phenotype edge, uncertain molecular mechanism.** Do not assert direct zinc export or glycerol import as the resistance mechanism. (houdt2021adaptationofcupriavidus pages 1-2) |
| 0.3 mM Zn²⁺ pre-exposure | induces an adaptive state that increases | survival during high-Zn challenge | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | Pre-induction of `czc` with 0.3 mM Zn²⁺ enhanced survival in parental and adapted strains. | **Strong assay-specific edge.** Encode concentration and challenge protocol. (houdt2021adaptationofcupriavidus pages 5-7) |
| High Zn²⁺ exposure | decreases | wild-type growth/survival | DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309) | Wild-type MIC was 12 mM; 24–25 mM caused bactericidal or sharply reduced survival. | **Strong but medium-specific.** This is the phenotype pressure edge. (houdt2021adaptationofcupriavidus pages 5-7) |
| Zur-regulated uptake/cytoplasmic-handling network | maintains | zinc homeostasis | DOI: [10.1128/JB.00372-17](https://doi.org/10.1128/JB.00372-17) | Zinc requires tight control of “import, storage, distribution, and export”; Zur regulons commonly control import and starvation responses. | **Supported context edge, not sufficient alone for high-zinc tolerance.** (butof2017thecomponentsof pages 3-5) |

## Proposed graph architecture for `zinc_tolerant.yaml`

A conservative initial graph could contain the following causal spine:

1. **Elevated extracellular Zn²⁺** → activates → **CzcRS**.
2. **CzcRS** → increases expression of → **CzcCBA/CzcD/CzcP module**.
3. **ZntR** → increases expression of → **ZntA and CdfX backup layer**.
4. **ZntA, CzcP, CdfX, and context-dependent CzcD** → transport → **cytoplasmic Zn²⁺ to periplasm**.
5. **CzcCBA** → transports → **periplasmic Zn²⁺ to extracellular space**.
6. **Net Zn²⁺ efflux** → decreases → **cytoplasmic/periplasmic zinc burden**.
7. **Lower cellular zinc burden** → increases → **growth/survival under elevated Zn²⁺**.

For a second, explicitly adaptive branch:

- `glpR` loss → ABC-transporter derepression → increased zinc-tolerance phenotype, with the intermediate transport chemistry marked **unknown**.

This design is preferable to a single “`czc` causes zinc tolerance” edge because it captures compartmentalized transport, inducible regulation, backup capacity, and the experimentally demonstrated phenotype.

## Recent developments, expert interpretation, and quantitative findings

### 2024 mechanistic advances

The principal 2024 advance is identification of CdfX as a fifth detectable inner-membrane zinc-efflux activity in the engineered Δe4 background. The combination of deletion and isotope pulse–chase data provides unusually strong support for a direct transport edge. The authors interpret zinc homeostasis as “adaptive layering”: overlapping systems cover conditions from starvation through extreme resistance, and backup exporters become important when substrate competition compromises the main system. (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 1-3)

The 2024 proteomic study adds a temporal dimension. Transcriptional induction begins within minutes, cellular metal physiology adjusts within approximately one hour, and the proteome is substantially remodeled by three hours. This supports representing tolerance as a regulated state rather than a static transporter inventory. (galea2024linkingthetranscriptome pages 1-2)

### Adaptive evolution

The CH34ZnR study shows that resistance can increase without mutation of the canonical `czc` operon. An IS1088 insertion disrupted `glpR`, derepressing a neighboring ABC transporter; mutant deletion and complementation linked that change to the phenotype. CH34ZnR doubled the Zn²⁺ MIC from 12 to 24 mM. This is important expert evidence that causal graphs should permit noncanonical adaptation branches but should not assign the transporter a substrate without direct transport data. (houdt2021adaptationofcupriavidus pages 1-2, houdt2021adaptationofcupriavidus pages 5-7)

### Applications and real-world implementation

Zinc-tolerant microbes are candidates for bioaugmentation, rhizosphere-assisted phytoremediation, biosorption, immobilization, and metal recovery. A 2024 review reported that *Pseudomonas* sp. Lk9 increased shoot Zn accumulation by 16.4% and Cu accumulation by 16.0% in a plant-remediation setting. Other implementations combine bacteria with hyperaccumulators, compost, moss, or mycorrhizal fungi to alter metal bioavailability and plant uptake. (li2024researchprogressin pages 14-15, li2024researchprogressin pages 19-20)

Recent strain-screening work also highlights biofilm-forming *Pseudomonas putida* and *Brevundimonas* strains for soil/water treatment and plant protection. Reported resistance in *P. putida* ranged from 100 ppm Co(II) to 2,500 ppm Fe(III), although those values are not zinc-specific and therefore should not enter this zinc graph. (hovorukha2024metalresistanceof pages 13-14)

Authoritative reviews remain cautious about deployment. Laboratory strains or simple two- to three-member consortia often perform poorly in complex natural communities; soil type, nutrient status, climate, mixed contaminants, long remediation cycles, low biomass, and uncertain economic returns constrain field-scale translation. Accordingly, **zinc tolerance is a strain-selection prerequisite, not proof of zinc removal, immobilization, or field efficacy**. (li2024researchprogressin pages 14-15, li2024researchprogressin pages 1-2)

## Warnings: claims not ready for TraitMech curation

1. **Do not curate “all CDF proteins export zinc.”** CDF substrate ranges and physiological directions vary; DmeF, FieF, CzcD, and CdfX need protein- and taxon-specific evidence.
2. **Do not assert that the Rmet_2229–2234 ABC transporter directly exports Zn²⁺.** Its derepression causes increased tolerance, but transported substrate and causal chemistry are unresolved. (houdt2021adaptationofcupriavidus pages 1-2)
3. **Do not encode nominal millimolar zinc as free Zn²⁺.** Speciation and Zn(OH)₂ precipitation can make these very different quantities. (schulz2024theeffluxsystem pages 12-14)
4. **Do not generalize CH34 or AE104 edges to all bacteria.** Czc architecture, plasmid context, paralogs, and regulatory thresholds are taxon-specific.
5. **Do not equate `czc` presence with expression or phenotype.** Require susceptibility, induction, transport, or perturbation evidence.
6. **Do not treat pMOL30 loss as a CzcCBA-only knockout.** It is a multi-gene plasmid perturbation.
7. **Do not curate CzcP “faster than ZntA” until the original kinetic experiment is checked.** The qualitative export role is supported; the comparative-rate edge requires exact conditions.
8. **Do not add zinc biosorption or bioremediation edges from tolerance data alone.** Removal efficiency, mass balance, and zinc fate require separate measurements.
9. **Do not use the supplied BS1 MIC of 20 mM as a universal species threshold.** MIC is strain-, medium-, pH-, salt-, and protocol-dependent.
10. **Avoid unverified protein CURIEs.** Label-only nodes are preferable to an accession from the wrong paralog or replicon.

## DOI-first bibliography

1. **Schulz V, et al.** “The efflux system CdfX exports zinc that cannot be transported by ZntA in *Cupriavidus metallidurans*.” *Journal of Bacteriology* 206(11). **November 2024.** DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24). Primary evidence for CdfX transport, deletion phenotype, and ZntR regulation. (schulz2024theeffluxsystem pages 1-3)
2. **Galea D, et al.** “Linking the transcriptome to physiology: response of the proteome of *Cupriavidus metallidurans* to changing metal availability.” *Metallomics* 16(12). **November 2024.** DOI: [10.1093/mtomcs/mfae058](https://doi.org/10.1093/mtomcs/mfae058). Primary proteomic and temporal evidence. (galea2024linkingthetranscriptome pages 1-2)
3. **Van Houdt R, et al.** “Adaptation of *Cupriavidus metallidurans* CH34 to Toxic Zinc Concentrations Involves an Uncharacterized ABC-Type Transporter.” *Microorganisms* 9:309. **February 2021.** DOI: [10.3390/microorganisms9020309](https://doi.org/10.3390/microorganisms9020309). MIC, survival, adaptive evolution, mutant, and complementation evidence. (houdt2021adaptationofcupriavidus pages 1-2, houdt2021adaptationofcupriavidus pages 5-7)
4. **Bütof L, et al.** “The Components of the Unique Zur Regulon of *Cupriavidus metallidurans* Mediate Cytoplasmic Zinc Handling.” *Journal of Bacteriology* 199(21). **November 2017.** DOI: [10.1128/JB.00372-17](https://doi.org/10.1128/JB.00372-17). Homeostasis and Zur-regulon context. (butof2017thecomponentsof pages 3-5)
5. **Scherer J, Nies DH.** “CzcP is a novel efflux system contributing to transition metal resistance in *Cupriavidus metallidurans* CH34.” *Molecular Microbiology* 73:601–621. **August 2009.** DOI: [10.1111/j.1365-2958.2009.06792.x](https://doi.org/10.1111/j.1365-2958.2009.06792.x). Foundational CzcP evidence supplied in the trait record.
6. **Li H, et al.** “Research Progress in the Joint Remediation of Plants–Microbes–Soil for Heavy Metal-Contaminated Soil in Mining Areas: A Review.” *Sustainability* 16:8464. **September 2024.** DOI: [10.3390/su16198464](https://doi.org/10.3390/su16198464). Applications, quantitative plant-accumulation examples, and field limitations. (li2024researchprogressin pages 14-15, li2024researchprogressin pages 1-2)
7. **Hovorukha V, et al.** “Metal Resistance of Microorganisms as a Crucial Factor for Their Homeostasis and Sustainable Environment.” *Sustainability* 16:9655. **November 2024.** DOI: [10.3390/su16229655](https://doi.org/10.3390/su16229655). Recent strain-screening and environmental-application perspective. (hovorukha2024metalresistanceof pages 13-14, hovorukha2024metalresistanceof pages 16-17)
8. **Frontiers in Microbiology trait-record source.** “Organism example: *Cupriavidus metallidurans* BS1 tolerates zinc to a MIC of 20 mM.” **2020.** DOI: [10.3389/fmicb.2020.00047](https://doi.org/10.3389/fmicb.2020.00047). Retain as organism-level phenotype evidence, with its original assay conditions attached.

References

1. (butof2017thecomponentsof pages 3-5): Lucy Bütof, Christopher Schmidt-Vogler, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. The components of the unique zur regulon of cupriavidus metallidurans mediate cytoplasmic zinc handling. Journal of Bacteriology, Nov 2017. URL: https://doi.org/10.1128/jb.00372-17, doi:10.1128/jb.00372-17. This article has 33 citations and is from a peer-reviewed journal.

2. (schulz2024theeffluxsystem pages 12-14): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 8 citations and is from a peer-reviewed journal.

3. (houdt2021adaptationofcupriavidus pages 5-7): Rob Van Houdt, Joachim Vandecraen, Natalie Leys, Pieter Monsieurs, and Abram Aertsen. Adaptation of cupriavidus metallidurans ch34 to toxic zinc concentrations involves an uncharacterized abc-type transporter. Microorganisms, 9:309, Feb 2021. URL: https://doi.org/10.3390/microorganisms9020309, doi:10.3390/microorganisms9020309. This article has 15 citations.

4. (houdt2021adaptationofcupriavidus pages 2-4): Rob Van Houdt, Joachim Vandecraen, Natalie Leys, Pieter Monsieurs, and Abram Aertsen. Adaptation of cupriavidus metallidurans ch34 to toxic zinc concentrations involves an uncharacterized abc-type transporter. Microorganisms, 9:309, Feb 2021. URL: https://doi.org/10.3390/microorganisms9020309, doi:10.3390/microorganisms9020309. This article has 15 citations.

5. (galea2024linkingthetranscriptome pages 1-2): Diana Galea, Martin Herzberg, Dirk Dobritzsch, Matt Fuszard, and Dietrich H Nies. Linking the transcriptome to physiology: response of the proteome of cupriavidus metallidurans to changing metal availability. Metallomics: Integrated Biometal Science, Nov 2024. URL: https://doi.org/10.1093/mtomcs/mfae058, doi:10.1093/mtomcs/mfae058. This article has 9 citations.

6. (houdt2021adaptationofcupriavidus pages 1-2): Rob Van Houdt, Joachim Vandecraen, Natalie Leys, Pieter Monsieurs, and Abram Aertsen. Adaptation of cupriavidus metallidurans ch34 to toxic zinc concentrations involves an uncharacterized abc-type transporter. Microorganisms, 9:309, Feb 2021. URL: https://doi.org/10.3390/microorganisms9020309, doi:10.3390/microorganisms9020309. This article has 15 citations.

7. (schulz2024theeffluxsystem pages 1-3): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 8 citations and is from a peer-reviewed journal.

8. (li2024researchprogressin pages 14-15): Hong Li, Tao Wang, Hongxia Du, Pan Guo, Shufeng Wang, and Ming Ma. Research progress in the joint remediation of plants–microbes–soil for heavy metal-contaminated soil in mining areas: a review. Sustainability, 16:8464, Sep 2024. URL: https://doi.org/10.3390/su16198464, doi:10.3390/su16198464. This article has 25 citations.

9. (li2024researchprogressin pages 19-20): Hong Li, Tao Wang, Hongxia Du, Pan Guo, Shufeng Wang, and Ming Ma. Research progress in the joint remediation of plants–microbes–soil for heavy metal-contaminated soil in mining areas: a review. Sustainability, 16:8464, Sep 2024. URL: https://doi.org/10.3390/su16198464, doi:10.3390/su16198464. This article has 25 citations.

10. (hovorukha2024metalresistanceof pages 13-14): Vira Hovorukha, Ewa Moliszewska, Olesia Havryliuk, Iryna Bida, and Oleksandr Tashyrev. Metal resistance of microorganisms as a crucial factor for their homeostasis and sustainable environment. Sustainability, 16:9655, Nov 2024. URL: https://doi.org/10.3390/su16229655, doi:10.3390/su16229655. This article has 9 citations.

11. (li2024researchprogressin pages 1-2): Hong Li, Tao Wang, Hongxia Du, Pan Guo, Shufeng Wang, and Ming Ma. Research progress in the joint remediation of plants–microbes–soil for heavy metal-contaminated soil in mining areas: a review. Sustainability, 16:8464, Sep 2024. URL: https://doi.org/10.3390/su16198464, doi:10.3390/su16198464. This article has 25 citations.

12. (hovorukha2024metalresistanceof pages 16-17): Vira Hovorukha, Ewa Moliszewska, Olesia Havryliuk, Iryna Bida, and Oleksandr Tashyrev. Metal resistance of microorganisms as a crucial factor for their homeostasis and sustainable environment. Sustainability, 16:9655, Nov 2024. URL: https://doi.org/10.3390/su16229655, doi:10.3390/su16229655. This article has 9 citations.