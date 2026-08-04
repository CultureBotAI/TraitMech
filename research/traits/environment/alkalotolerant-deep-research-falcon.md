---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:00:19.730006'
end_time: '2026-08-04T00:09:20.199099'
duration_seconds: 540.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: alkalotolerant
  trait_identifier: METPO:1003009
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: alkalotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism can tolerate alkaline pH
    but grows optimally at neutral pH.
  parent_traits: METPO:1003000
  synonyms: alkalitolerant
  evidence_summary: 'DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely
    alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis
    phenotype.)'
  causal_graph_summary: 'alkalotolerant_alkaline_stress_homeostasis: 11 nodes, 10
    edges'
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
- **Trait label:** alkalotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkalitolerant
- **Existing evidence:** DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis phenotype.)
- **Existing causal graph summary:** alkalotolerant_alkaline_stress_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **alkalotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkalotolerant.yaml`.

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
- **Trait label:** alkalotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkalitolerant
- **Existing evidence:** DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis phenotype.)
- **Existing causal graph summary:** alkalotolerant_alkaline_stress_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **alkalotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkalotolerant.yaml`.

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


# Curation-focused research report: microbial alkalotolerance

## Executive summary

**Target trait:** `METPO:1003009` (**alkalotolerant**; synonym *alkalitolerant*). The supplied reviewed definition—“a pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH”—should control graph membership. The most defensible core mechanism is: **external alkaline pH → threatened cytoplasmic alkalinization → inward proton recovery through monovalent-cation/H⁺ antiport → maintenance of a cytoplasm more acidic than the environment → sustained growth**. Neutralophilic bacteria commonly maintain cytoplasmic pH near 7.5–7.7 across an external range of approximately pH 5.5–9.0; growth and mere survival must nevertheless be distinguished experimentally. (krulwich2011molecularaspectsof pages 1-3)

The strongest trait-matched causal evidence comes from neutralophilic or moderately alkali-tolerant organisms: *Escherichia coli* MdtM, *Corynebacterium glutamicum* Mrp1, and alkaline-stable penicillin-binding proteins (PBPs) in *Bacillus subtilis*. The 2024 PBP study is an important recent development because it adds **cell-envelope enzyme specialization and redundancy** to the traditional antiporter-centered model. By contrast, ATP-synthase specialization, low-pI surface proteins, teichuronic acids, S-layers, and specialized respiratory chains are supported principally in true alkaliphiles and should not automatically be asserted as mechanisms of `METPO:1003009`. (krulwich2011molecularaspectsof pages 5-6, mitchell2024penicillinbindingproteinredundancy pages 8-10)

## 1. Scope and phenotype boundaries

### Inclusion criterion

An organism should be annotated `METPO:1003009` when a controlled growth profile demonstrates:

1. an optimum in the neutral range, preferably from a full pH-response curve; and
2. reproducible growth at one or more alkaline pH values above that optimum.

The causal graph may include mechanisms measured during alkaline shock or survival, but those assays should be marked as **supporting mechanistic evidence**, not as sufficient proof of the growth-preference trait. Neutralophilic bacteria can remain viable in alkaline environments and resume growth after return to permissive pH without growing under the alkaline exposure itself. (krulwich2011molecularaspectsof pages 1-3)

### Boundary cases

- **Alkaliphile:** optimal growth is alkaline. For example, *Bacillus pseudofirmus* OF4 grows optimally near pH 10.5, and Halomonas sp. Y2 has an optimum of pH 10.0 and range of pH 5.0–11.0. These are mechanistic comparators, not direct instances of the target definition. (krulwich2011molecularaspectsof pages 12-14, cheng(程彬)2016alkalineresponseof pages 2-4)
- **Extreme/obligate alkaliphile:** sustained growth at very high alkaline pH, often with specialized bioenergetics. Do not merge this with neutral-optimum tolerance.
- **Haloalkaliphile or salt–alkali tolerance:** high pH is combined with elevated NaCl, carbonate, or bicarbonate. Sodium may be both a stressor and the exchange substrate that enables proton uptake; salt dependence must therefore be represented separately.
- **Alkaline-shock resistance:** viability after a brief pH pulse is not equivalent to chronic alkaline growth. In *B. subtilis*, cells were 100% viable after 30 minutes at pH 8.5 but only 40% viable at pH 10.5, and chronic exposure above pH 9.5 was not tolerated. (mitchell2024penicillinbindingproteinredundancy pages 6-8, mitchell2024penicillinbindingproteinredundancy pages 8-10)
- **Assay artifact:** unbuffered rich medium can be neutralized by metabolism. In the 2024 *B. subtilis* work, medium beginning at pH 9.4 could fall to pH 8.0 overnight. Endpoint growth without measured pH is consequently weak evidence. (mitchell2024penicillinbindingproteinredundancy pages 8-10)

## 2. Candidate nodes grouped by type

### Trait, environmental, and assay nodes

- `METPO:1003009` — alkalotolerant
- external alkaline pH — label-only environmental factor pending verified ENVO/assay grounding
- alkaline shock — label-only experimental process
- chronic alkaline growth — label-only assay state
- sodium-containing alkaline medium; potassium-containing alkaline medium — compound experimental factors
- cytoplasmic pH; external pH; transmembrane ΔpH; membrane potential Δψ; proton-motive force

### Chemicals and ions

- proton — `CHEBI:15378`
- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- lithium ion and rubidium ion — retain label-only unless identifiers are checked during implementation
- CCCP — inhibitor/control node, label-only pending CHEBI verification
- peptidoglycan — label-only pending ontology verification

### Processes and functions

- pH homeostasis — `GO:0006885`
- monovalent-cation/H⁺ antiport
- Na⁺/H⁺ antiport
- K⁺/H⁺ antiport
- sodium-ion exclusion
- inward proton transport
- maintenance of cytoplasmic pH below external pH
- peptidoglycan biosynthetic process — `GO:0009252`
- transglycosylation, transpeptidation, and carboxypeptidase activity — label-only pending exact GO/EC verification
- respiratory-chain remodeling and proton retention — provisional

### Cellular locations and structures

- plasma membrane — `GO:0005886`
- cytoplasm — `GO:0005737`
- cell wall / peptidoglycan layer
- extracellularly exposed or periplasm-facing PBP compartment
- S-layer and secondary cell-wall polymers — comparator nodes only

### Genes, proteins, and complexes

Use organism-qualified labels until UniProt/NCBI Gene identifiers are verified:

- *E. coli* MdtM; dysfunctional MdtM-D22A
- *E. coli* NhaA, NhaB, ChaA, and MdfA
- *C. glutamicum* Mrp1 complex, Mrp2 complex, NhaP, and ChaA
- *C. glutamicum* Mrp1A Lys299 and K299 replacement variants
- *B. subtilis* PBP2a/*pbpA*, PBP3/*pbpC*, PBP4/*pbpD*, PBPH/*pbpH* or *ykuA*, PBP5/*dacA*, and PBP1a/PBP1b products of *ponA*
- F₁F₀ ATP synthase, cytochrome bd, proton-pumping respiratory complexes, acidic surface proteins, teichuronic acids, and SlpA — provisional comparative nodes

## 3. Candidate causal graph

The following table ranks edges by evidentiary and trait relevance.

| priority | subject | predicate | object | organism/context | evidence type | confidence/curation status |
|---|---|---|---|---|---|---|
| High | external alkaline pH | causes | cytoplasmic alkalinization stress / need for pH homeostasis | Neutralophilic bacteria; trait scope context for alkalotolerance | Authoritative review synthesis with physiological ranges (krulwich2011molecularaspectsof pages 1-3, holdsworth2013multidrugresistanceprotein pages 1-2) | High for generic trait framing; curate as broad environmental-to-process edge |
| High | MdtM | catalyzes | Na+/H+ antiport | *Escherichia coli*; inverted vesicles, alkaline pH; Na+ exchange optimum pH 9.25 (holdsworth2013multidrugresistanceprotein pages 7-9, holdsworth2013multidrugresistanceprotein pages 1-2) | Direct transport assay + mutant/complementation | High; core mechanistic edge |
| High | MdtM | catalyzes | K+/H+ antiport | *Escherichia coli*; inverted vesicles, alkaline pH; K+ exchange optimum pH 9.0 (holdsworth2013multidrugresistanceprotein pages 7-9, holdsworth2013multidrugresistanceprotein pages 1-2) | Direct transport assay + mutant/complementation | High; core mechanistic edge |
| High | MdtM activity | supports | acidic cytoplasmic pH relative to external alkaline pH | *Escherichia coli* under alkaline stress (holdsworth2013multidrugresistanceprotein pages 1-2) | Internal pH measurement + functional inference | High; core mechanistic edge |
| High | MdtM | supports | alkalotolerance / growth at alkaline pH in presence of Na+ or K+ | *Escherichia coli* Δ*mdtM* growth phenotypes pH 8.5–10 (holdsworth2013multidrugresistanceprotein pages 1-2) | Deletion + plasmid complementation growth assay | High; core mechanistic edge |
| High | Mrp1 antiporter | supports | Na+ exclusion / low intracellular Na+ | *Corynebacterium glutamicum*; moderately salt-alkali tolerant organism (xu2018thelysine299 pages 1-3, xu2018thelysine299 pages 6-8) | Mutant phenotype + intracellular Na+ measurement summary | High; core mechanistic edge |
| High | Mrp1 antiporter | supports | intracellular pH homeostasis under alkaline stress | *Corynebacterium glutamicum* (xu2018thelysine299 pages 1-3) | Mutant phenotype + intracellular pH summary | High; core mechanistic edge |
| High | alkaline stimulus | induces | Mrp-type antiporter transcript levels | *Corynebacterium glutamicum* (xu2018thelysine299 pages 1-3) | Expression response under alkaline stress | Medium-high; useful upstream regulation edge |
| High | Mrp1A Lys299 | supports | Mrp1 antiporter function | *Corynebacterium glutamicum*; chromosomal replacement / site-directed mutagenesis (xu2018thelysine299 pages 1-3) | Residue perturbation | High; curate as taxon/protein-specific edge |
| High | Mrp1A Lys299 replacement | causes | higher intracellular Na+ and more alkaline intracellular pH, reducing growth | *Corynebacterium glutamicum* (xu2018thelysine299 pages 1-3) | Residue perturbation + physiological readouts | High; curate with explicit taxon specificity |
| High | PBP2a | supports | growth in alkaline media | *Bacillus subtilis*; mutant growth curves in basic LB (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 1-2) | Null mutant phenotype | High; core edge for envelope adaptation under alkaline shock/growth |
| High | PBP3 | supports | growth in alkaline media | *Bacillus subtilis* (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 1-2) | Null mutant phenotype | High; core edge |
| High | PBP5 | supports | growth in alkaline media | *Bacillus subtilis*; highest base sensitivity in Δ*dacA* (mitchell2024penicillinbindingproteinredundancy pages 8-10) | Null mutant phenotype | High; core edge |
| High | alkaline shock | inactivates | PBPH | *Bacillus subtilis*; rapid loss within ~5 min; 30 min shock assays (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 6-8) | In vivo activity-based probe assay | High; core edge |
| High | alkaline shock | inactivates | PBP4 | *Bacillus subtilis*; begins ~pH 10; lost by pH 10.5–11 (mitchell2024penicillinbindingproteinredundancy pages 4-6, mitchell2024penicillinbindingproteinredundancy pages 8-10) | In vivo activity-based probe assay | High; core edge |
| High | alkaline shock | promotes transition | PBP1a -> PBP1b | *Bacillus subtilis*; occurs around pH ~10.5; slower than PBPH/PBP4 inactivation (mitchell2024penicillinbindingproteinredundancy pages 4-6) | In vivo activity-based probe assay + time course | High; core edge |
| Medium | ATP synthase expression/activity | supports | alkaline pH homeostasis | Neutralophiles and alkaliphiles; review-level synthesis, not trait-matched perturbation in alkalotolerant neutral-optimum taxa (krulwich2011molecularaspectsof pages 5-6) | Review synthesis | Medium-low; contextual only, do not treat as core until direct alkalotolerant perturbation evidence |
| Medium | alkaline conditions | remodel | respiratory chain composition to reduce proton loss | *E. coli* and other bacteria; e.g., downregulation of proton-pumping complexes / upregulation of alternative oxidases in review synthesis (krulwich2011molecularaspectsof pages 5-6) | Review synthesis | Medium-low; contextual only, not core yet |
| Low-Medium | acidic cell-surface polymers / low-pI surface proteins | support | proton capture / pH homeostasis at high external pH | Mainly alkaliphilic *Bacillus* context, not neutral-optimum alkalotolerant trait match (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14) | Comparative review synthesis | Low for this trait; useful comparator but not core for METPO:1003009 until trait-matched direct evidence |


*Table: This table ranks candidate causal edges for curating microbial alkalotolerance, emphasizing direct perturbation-backed mechanisms and separating contextual but not-yet-core comparative evidence. It is useful for deciding which edges can be safely promoted into a TraitMech graph versus which should remain provisional.*

## 4. Edge-level evidence and proposed triples

| Proposed subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|
| external alkaline pH → **challenges** → cytoplasmic pH homeostasis | Krulwich et al.: neutralophiles maintain cytoplasmic pH “~7.5–7.7” across external pH “~5.5–9.0.” DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), published May 2011. (krulwich2011molecularaspectsof pages 1-3) | **Core generic edge.** The perturbation initially threatens alkalinization; successful organisms buffer the observed endpoint. |
| Na⁺/H⁺ or K⁺/H⁺ antiport → **imports** → H⁺ | Cheng et al.: antiporters “actively transport protons inward while extruding monovalent cations.” DOI: [10.1074/jbc.M116.751016](https://doi.org/10.1074/jbc.M116.751016), published December 2016. (cheng(程彬)2016alkalineresponseof pages 2-4) | **Core mechanism**, but instantiate with a protein and taxon where possible. |
| *E. coli* MdtM → **catalyzes** → Na⁺/H⁺ antiport | Wild-type MdtM vesicles showed rapid dequenching after Na⁺ addition; maximal response occurred at pH 9.25, whereas D22A controls had negligible activity. DOI: [10.1186/1471-2180-13-113](https://doi.org/10.1186/1471-2180-13-113), published May 2013. (holdsworth2013multidrugresistanceprotein pages 7-9, holdsworth2013multidrugresistanceprotein pages 1-2) | **High-confidence core edge.** Direct transport assay in a neutralophile. |
| *E. coli* MdtM → **catalyzes** → K⁺/H⁺ antiport | The same vesicle assay found maximal K⁺-driven dequenching at pH 9.0. (holdsworth2013multidrugresistanceprotein pages 7-9) | **High-confidence core edge.** |
| MdtM-mediated cation/H⁺ antiport → **supports** → acidic cytoplasm relative to alkaline exterior | Internal-pH measurements confirmed that MdtM contributes to a stable cytoplasmic pH under alkaline stress. (holdsworth2013multidrugresistanceprotein pages 1-2) | **High-confidence core edge.** |
| MdtM → **supports** → alkaline growth | At pH 9.5–9.75, wild type still grew at low density while Δ*mdtM* growth was arrested; neither grew at pH 10. The effect required millimolar Na⁺ or K⁺. (holdsworth2013multidrugresistanceprotein pages 1-2) | **High confidence but context-dependent.** Encode cation availability as a condition/modifier. |
| alkaline stimulus → **increases expression of** → *C. glutamicum* Mrp antiporters | “An alkaline stimulus particularly induced transcript levels of the Mrp-type antiporters.” DOI: [10.1128/AEM.00110-18](https://doi.org/10.1128/AEM.00110-18), manuscript posted March 9, 2018. (xu2018thelysine299 pages 1-3) | **Medium-high confidence.** Expression is not itself proof of necessity, but is supported by mutant physiology below. |
| *C. glutamicum* Mrp1 → **supports** → Na⁺ resistance and alkaline-pH homeostasis | The study reports that Mrp1 had “crucial roles” in Na⁺ resistance and alkali tolerance; Δ*mrp1 mrp2* failed to grow under high-salt or alkaline conditions. (xu2018thelysine299 pages 1-3) | **High-confidence, taxon-specific core edge.** Confirm that the exact strain’s optimum satisfies the METPO definition before using it as trait-instance evidence. |
| Mrp1A Lys299 → **supports** → Mrp1 ion transport/pH-homeostasis function | Chromosomal replacement of K299 produced “a higher intracellular Na⁺ level and a more alkaline intracellular pH,” with marked growth attenuation. (xu2018thelysine299 pages 1-3) | **Strong residue-level causal edge.** Retain taxon and allele details. |
| alkaline shock → **inactivates** → *B. subtilis* PBPH | PBPH activity was lost by approximately pH 8.5–9 and rapidly within about 5 minutes, whereas PBP2a remained active. DOI: [10.1128/AEM.00548-23](https://doi.org/10.1128/AEM.00548-23), published online December 21, 2023; January 2024 issue. (mitchell2024penicillinbindingproteinredundancy pages 2-4, mitchell2024penicillinbindingproteinredundancy pages 6-8, mitchell2024penicillinbindingproteinredundancy pages 4-6) | **Direct activity edge**, but it describes dispensability/sensitivity rather than a positive tolerance mechanism. |
| alkaline shock → **inactivates** → *B. subtilis* PBP4 | PBP4 inactivation began near pH 10 and was observed during 30-minute pH 10.5–11 treatments. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6) | **High-confidence direct edge.** |
| alkaline shock → **promotes transition from** → PBP1a to PBP1b | The activity shift occurred near pH 10.5 and required about 10 minutes; intact-cell machinery was required for PBP1b activation. (mitchell2024penicillinbindingproteinredundancy pages 4-6) | **High confidence for activity/processing; mechanism uncertain.** Do not encode direct proteolytic cleavage until established. |
| PBP2a, PBP3, and PBP5 → **support** → growth in alkaline medium | Their null mutants were more base-sensitive; Δ*dacA* had the greatest increase in time to maximal growth rate. Basic conditions extended lag by approximately 3–7 hours. (mitchell2024penicillinbindingproteinredundancy pages 8-10) | **Strong recent trait-relevant evidence.** Effects were measured in unbuffered LB, so represent assay context. |
| PBP redundancy → **buffers loss of individual PBP activity during** → alkaline shock | Despite selective PBP inactivation, mutant strains retained similar activity-profile transitions and showed no shock-induced morphology change; the authors interpret redundancy as enabling envelope synthesis across conditions. (mitchell2024penicillinbindingproteinredundancy pages 1-2, mitchell2024penicillinbindingproteinredundancy pages 8-10) | **Medium-high confidence systems edge.** “Redundancy” is a higher-order module and may need a grouped node. |
| F₁F₀ ATP synthase upregulation → **supports** → proton capture at alkaline pH | Authoritative review: ATP-synthase expression rises under alkaline stress; aerobic alkaliphiles have specialized H⁺-coupled ATP synthases. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6) | **Provisional.** Do not add as a universal core edge without a neutral-optimum, direct perturbation study. |
| respiratory-chain remodeling → **reduces** → outward proton loss | Review synthesis indicates that *E. coli* can decrease proton-pumping complexes and increase non-proton-pumping cytochrome bd under alkaline stress. (krulwich2011molecularaspectsof pages 5-6) | **Provisional**, because expression correlation and oxygen status may confound causality. |
| acidic surface polymers/low-pI proteins → **promote** → surface proton retention | Alkaliphile examples include low-pI CtaC, teichuronic acids, and acidic SlpA. (krulwich2011molecularaspectsof pages 5-6) | **Do not curate into the target graph yet.** Evidence is largely from true alkaliphiles. |

## 5. Recommended minimal graph architecture

A conservative first revision of `alkalotolerant_alkaline_stress_homeostasis` should center on two experimentally supported branches:

1. **Ion/pH-homeostasis branch**  
   external alkaline pH → cytoplasmic alkalinization pressure → induction/activation of MdtM or Mrp-type antiporters → Na⁺ or K⁺ efflux coupled to H⁺ influx → lower intracellular Na⁺ and more acidic cytoplasmic pH → alkaline growth/tolerance.

2. **Envelope-function branch**  
   external alkaline pH → differential PBP activity → loss of PBPH/PBP4 activity plus persistence of PBP2a/PBP3/PBP5 activity → continued peptidoglycan synthesis and replication → alkaline growth. The PBP1a→PBP1b transition can be added as a side branch whose functional consequence remains unresolved. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 4-6)

ATP synthase, respiratory remodeling, acidic cell-wall polymers, S-layers, and cytochrome-c-based proton capture should remain in a **provisional comparator module** rather than the minimal target graph.

## 6. Recent developments and quantitative findings

The principal 2023–2024 advance is Mitchell et al.’s in-vivo activity mapping of PBPs. It showed that extracellularly exposed enzymes are not interchangeable across pH: PBPH and PBP4 rapidly lose activity, PBP1 shifts isoforms, and PBP2a/PBP3/PBP5 remain functional. At pH 8.5, loss of PBPH activity was compatible with 100% viability; at pH 10.5, coincident PBP4 loss and the PBP1 isoform shift accompanied viability of only 40%. Alkaline medium added about 3–7 hours to the time required to reach maximum growth rate, with Δ*dacA* the most base-sensitive mutant. (mitchell2024penicillinbindingproteinredundancy pages 8-10)

This work refines the prevailing expert model. Earlier authoritative synthesis emphasized cytoplasmic pH homeostasis through antiporters, PMF management, ATP synthase, respiration, and proton-retaining envelopes. The new PBP data show that **preservation of cell-wall biogenesis outside the pH-buffered cytoplasm is an additional causal requirement**, at least in *B. subtilis*. (krulwich2011molecularaspectsof pages 5-6, mitchell2024penicillinbindingproteinredundancy pages 1-2)

The best quantitative neutralophile antiporter evidence remains MdtM: Δ*mdtM* showed progressively impaired growth from pH 9.0 and complete arrest at pH 9.5–9.75, while wild type retained low-density growth; transport optima were pH 9.0 for K⁺/H⁺ exchange and pH 9.25 for Na⁺/H⁺ exchange. MdtM had no detectable antiport at pH 6.5 and only about 20% fluorescence dequenching at pH 7–8 in vesicle assays. (holdsworth2013multidrugresistanceprotein pages 7-9, holdsworth2013multidrugresistanceprotein pages 1-2)

## 7. Applications and real-world relevance

- **Industrial fermentation:** *C. glutamicum* is an amino-acid-production workhorse. Salt and alkaline excursions reduce biomass and product yields, making Mrp1 and its K299-dependent transport function plausible engineering targets for process robustness. The source itself highlights adaptation as important for “product yields.” (xu2018thelysine299 pages 1-3, xu2018thelysine299 pages 6-8)
- **Pathogen persistence and food/public-health microbiology:** neutralophilic enteric bacteria can remain viable for weeks in alkaline marine or estuarine environments. Understanding MdtM/NhaA/ChaA-mediated tolerance may improve persistence models and hurdle-process design. (holdsworth2013multidrugresistanceprotein pages 1-2)
- **Antibacterial development:** pH-dependent reliance on PBP2a, PBP3, or PBP5 suggests that envelope targets may have condition-specific vulnerabilities. This is a research implication, not yet a validated therapeutic implementation. (mitchell2024penicillinbindingproteinredundancy pages 8-10)
- **High-pH bioprocessing and remediation:** alkaliphiles supply alkaline-stable enzymes and cells for high-pH operations, but these applications concern alkaliphily more directly than `METPO:1003009`; they should be cited as adjacent use cases rather than evidence defining the target trait.

## 8. Curation warnings

1. **Do not infer the trait from a gene.** MdtM, Mrp, NhaA, or PBP homologues are neither necessary nor sufficient annotations for alkalotolerance without phenotype data.
2. **Do not merge alkalotolerance with alkaliphily.** Halomonas sp. Y2 and *B. pseudofirmus* OF4 optimize growth at alkaline pH and are comparative evidence only. (krulwich2011molecularaspectsof pages 12-14, cheng(程彬)2016alkalineresponseof pages 2-4)
3. **Separate growth, survival, and shock response.** A 30-minute CFU assay cannot establish a growth optimum.
4. **Encode ionic context.** MdtM-supported growth depended on millimolar Na⁺ or K⁺; Na⁺/H⁺ and K⁺/H⁺ exchange should be distinct edges. (holdsworth2013multidrugresistanceprotein pages 1-2)
5. **Treat transcript changes as regulation, not mechanism completion.** Mrp induction supports an upstream edge, but deletion, allele replacement, internal-pH, and ion measurements provide the causal evidence.
6. **Represent buffered versus unbuffered media.** Metabolic neutralization of LB can turn a nominal pH-9.4 treatment into a lower-pH exposure. (mitchell2024penicillinbindingproteinredundancy pages 8-10)
7. **Do not assert that PBP1a is cleaved directly into PBP1b.** Differential C-terminal processing is proposed, but the responsible machinery and exact modification remain unresolved. (mitchell2024penicillinbindingproteinredundancy pages 4-6)
8. **Do not generalize PBP behavior across bacteria.** *Staphylococcus aureus* PBPs did not show the same alkaline response, whereas *Streptococcus pneumoniae* PBP1a activity decreased. (mitchell2024penicillinbindingproteinredundancy pages 8-10)
9. **Keep alkaliphile-specific proton-retention mechanisms provisional.** Low-pI surface proteins, teichuronic acids, S-layers, and specialized ATP synthase motifs lack direct trait-matched evidence for neutral-optimum alkalotolerance. (krulwich2011molecularaspectsof pages 5-6)
10. **Verify all organism-specific identifiers before YAML insertion.** Protein/gene labels above intentionally remain ungrounded rather than risk invented or strain-mismatched CURIEs.

## DOI-first bibliography

1. Mitchell SL, Kearns DB, Carlson EE. “Penicillin-binding protein redundancy in *Bacillus subtilis* enables growth during alkaline shock.” *Applied and Environmental Microbiology* 90(1). Published online **21 December 2023**; issue **January 2024**. DOI: [10.1128/AEM.00548-23](https://doi.org/10.1128/AEM.00548-23). (mitchell2024penicillinbindingproteinredundancy pages 1-2)
2. Xu N et al. “The Lysine 299 Residue Endows the Multisubunit Mrp1 Antiporter with Dominant Roles in Na⁺ Resistance and pH Homeostasis in *Corynebacterium glutamicum*.” *Applied and Environmental Microbiology* 84(10), **May 2018**; posted **9 March 2018**. DOI: [10.1128/AEM.00110-18](https://doi.org/10.1128/AEM.00110-18). (xu2018thelysine299 pages 1-3)
3. Cheng B et al. “Alkaline Response of a Halotolerant Alkaliphilic Halomonas Strain and Functional Diversity of Its Na⁺(K⁺)/H⁺ Antiporters.” *Journal of Biological Chemistry* 291:26056–26065, **December 2016**. DOI: [10.1074/jbc.M116.751016](https://doi.org/10.1074/jbc.M116.751016). (cheng(程彬)2016alkalineresponseof pages 1-2)
4. Holdsworth SR, Law CJ. “Multidrug resistance protein MdtM adds to the repertoire of antiporters involved in alkaline pH homeostasis in *Escherichia coli*.” *BMC Microbiology* 13:113, **May 2013**. DOI: [10.1186/1471-2180-13-113](https://doi.org/10.1186/1471-2180-13-113). (holdsworth2013multidrugresistanceprotein pages 1-2)
5. Krulwich TA, Sachs G, Padan E. “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343, **May 2011**. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3)

**Curation recommendation:** promote MdtM, Mrp1/K299, and alkaline-stable PBP edges into the candidate YAML with explicit taxon and assay qualifiers. Retain ATP synthase, respiratory remodeling, and acidic-envelope mechanisms as uncertain comparator edges until direct perturbation evidence is found in organisms whose measured optimum is neutral.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (mitchell2024penicillinbindingproteinredundancy pages 8-10): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (cheng(程彬)2016alkalineresponseof pages 2-4): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

6. (mitchell2024penicillinbindingproteinredundancy pages 6-8): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

7. (holdsworth2013multidrugresistanceprotein pages 1-2): Scarlett R Holdsworth and Christopher J Law. Multidrug resistance protein mdtm adds to the repertoire of antiporters involved in alkaline ph homeostasis in escherichia coli. BMC Microbiology, 13:113-113, May 2013. URL: https://doi.org/10.1186/1471-2180-13-113, doi:10.1186/1471-2180-13-113. This article has 58 citations and is from a peer-reviewed journal.

8. (holdsworth2013multidrugresistanceprotein pages 7-9): Scarlett R Holdsworth and Christopher J Law. Multidrug resistance protein mdtm adds to the repertoire of antiporters involved in alkaline ph homeostasis in escherichia coli. BMC Microbiology, 13:113-113, May 2013. URL: https://doi.org/10.1186/1471-2180-13-113, doi:10.1186/1471-2180-13-113. This article has 58 citations and is from a peer-reviewed journal.

9. (xu2018thelysine299 pages 1-3): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.

10. (xu2018thelysine299 pages 6-8): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.

11. (mitchell2024penicillinbindingproteinredundancy pages 1-2): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

12. (mitchell2024penicillinbindingproteinredundancy pages 4-6): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

13. (mitchell2024penicillinbindingproteinredundancy pages 2-4): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

14. (cheng(程彬)2016alkalineresponseof pages 1-2): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.