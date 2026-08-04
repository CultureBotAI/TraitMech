---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:02:57.491745'
end_time: '2026-08-04T01:14:15.228259'
duration_seconds: 677.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mesophilic
  trait_identifier: METPO:1000615
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: mesophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at intermediate\
    \ temperatures, typically ~20\u201345 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic
    bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612:
    more unsaturated fatty acids (Membrane-adaptation review supports homoviscous
    membrane composition matched to ambient temperature as the basis of mesophile
    physiology.)'
  causal_graph_summary: 'mesophilic_homoviscous_adaptation: 15 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mesophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000615
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at intermediate temperatures, typically ~20–45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition matched to ambient temperature as the basis of mesophile physiology.)
- **Existing causal graph summary:** mesophilic_homoviscous_adaptation: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **mesophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mesophilic.yaml`.

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
- **Trait label:** mesophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000615
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at intermediate temperatures, typically ~20–45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition matched to ambient temperature as the basis of mesophile physiology.)
- **Existing causal graph summary:** mesophilic_homoviscous_adaptation: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **mesophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mesophilic.yaml`.

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


# Curation report: microbial trait **mesophilic**

## Executive summary

**Trait:** `METPO:1000615`  
**Category:** ENVIRONMENT  
**Term kind:** CLASS  
**Mapping status:** REVIEWED  
**Parent:** `METPO:1000613`

Mesophily should be modeled as an **organism-level temperature preference in which the optimum or favored growth occurs at intermediate temperature**, operationally about **20–45 °C** under the supplied METPO definition. It is not equivalent to merely surviving at one temperature in that interval, having a broad growth range, or mounting a cold- or heat-shock response. Published boundaries are not perfectly uniform: one comparative study uses an optimal-growth-temperature range of 20–50 °C for mesophiles, illustrating why the measured optimum, complete growth curve, medium, pressure, pH, oxygen status, and acclimation history should accompany trait assertions (sen2022insightsonrigidity pages 1-3).

The strongest curation-ready mechanism is **homeoviscous adaptation**: temperature changes alter fatty-acid biosynthetic flux and membrane lipid composition, which counters temperature-driven changes in membrane viscosity. A 2024 quantitative study in *Escherichia coli* identified a fast, temperature-sensitive FabI/FabB metabolic valve plus slower FabR-mediated transcriptional feedback, restoring membrane composition within one generation after a temperature shift (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 1-2). Heat-shock and cold-shock systems are important **boundary-support mechanisms**, but they do not define mesophily.

## 1. Trait scope and boundary cases

### 1.1 Positive scope

The preferred representation is:

> A microbial phenotype in which growth rate, yield, or another validated growth measure is optimal or favored at intermediate temperature, typically approximately 20–45 °C.

An assay should ideally estimate an optimum from several temperatures rather than infer mesophily from growth at 30 or 37 °C alone. “Mesophilic” may describe an organism, community, reactor regime, enzyme, or process; only the **organism-level growth preference** directly instantiates `METPO:1000615`.

### 1.2 Distinctions from neighboring concepts

- **Psychrophile:** optimum near low temperature; cold-active macromolecules are evolutionarily tuned for activity and flexibility in the cold. Growth by a mesophile after acclimation at 10–15 °C does not make it psychrophilic.
- **Psychrotolerant/psychrotrophic:** can grow at low temperature but has a higher optimum. The 2023 review notes that most microorganisms multiply poorly below 4 °C, while some mesophilic pathogens can still proliferate at refrigeration temperatures; low-temperature growth alone is therefore insufficient for classification (ramon2023ageneraloverview pages 2-4).
- **Thermophile:** optimum above the mesophilic interval. A protein study uses `Topt >50 °C`, but classifications near 45–50 °C depend on the convention used (sen2022insightsonrigidity pages 1-3).
- **Thermotolerant:** withstands elevated temperature without having a thermophilic optimum.
- **Heat/cold shock:** acute response to a change relative to the organism’s previous or optimal temperature. In experimental bacterial literature, “cold shock” may mean a rapid shift such as 37→15 °C, followed by transient growth arrest and acclimation (horn2007structureandfunction pages 1-2).
- **Growth range versus optimum:** survival limits, minimum/maximum growth temperatures, and optimum growth temperature are separate phenotypes.
- **Mesophilic process condition:** “mesophilic anaerobic digestion at 35 °C” describes a reactor regime and community-level function; it does not prove every community member is a mesophile.

### 1.3 Mechanistic interpretation

Mesophily is probably an **emergent balance** rather than a single pathway: membranes must remain liquid-crystalline but sufficiently impermeable; proteins must retain both stability and catalytic dynamics; transcription, translation, transport, and central metabolism must remain coordinated. Reviews distinguish long-term genome evolution, which sets the viable temperature range, from short-term reversible regulation of gene expression and enzyme activity (siliakus2017adaptationsofarchaeal pages 3-5). Accordingly, causal edges from acute stress experiments should be annotated as acclimation or boundary support—not automatically as causes of the constitutive mesophilic optimum.

## 2. Candidate nodes grouped by type

Only identifiers that can be stated confidently are included. Labels should be retained without a CURIE when the exact accession has not been verified.

### 2.1 Trait, environmental, and experimental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| mesophilic | `METPO:1000615` | Target phenotype; quote identifier verbatim. |
| parent temperature-preference trait | `METPO:1000613` | Supplied parent. |
| intermediate growth temperature | label only | Represent measured temperature in °C as assay metadata. |
| temperature downshift / cold shock | label only | Experimental perturbation, not the trait itself. |
| temperature upshift / heat shock | label only | Experimental perturbation, not the trait itself. |
| optimal growth temperature | label only | Quantitative phenotype; do not collapse into growth range. |
| phosphate limitation | label only | Relevant modifier in 2024 *D. alkenivorans* lipidomics. |
| mesophilic anaerobic digestion | label only | Process/application node, generally around 35–40 °C. |

### 2.2 Organisms

| Organism | Grounding | Role |
|---|---|---|
| *Escherichia coli* | `NCBITaxon:562` | Principal mesophilic model for fatty-acid, cold-shock, and heat-shock mechanisms. |
| *Bacillus subtilis* | `NCBITaxon:1423` | DesK–DesR–desaturase membrane thermosensing exemplar. |
| *Acinetobacter baumannii* | `NCBITaxon:470` | Taxon-specific lipid-A remodeling by LpxS. |
| *Desulfatibacillum alkenivorans* | label only unless strain taxon ID is verified | Mesophilic anaerobic sulfate reducer with unusual ether-rich membrane. |

### 2.3 Genes, proteins, enzymes, and complexes

- **E. coli fatty-acid module:** `fabA`, FabA; `fabB`, FabB; `fabI`, FabI; `fabF`, FabF; `fabR`, FabR; acyl-carrier-protein intermediates. Keep label-only or add organism-specific UniProt accessions after database verification.
- **Heat response:** `rpoH`/σ32, `rpoE`/σE, DnaK–DnaJ–GrpE, GroEL–GroES, FtsH, ClpXP, DegS, RseA, RseP.
- **Cold response:** CspA-family RNA chaperones, CsdA/DeaD RNA helicase, RNase R, RbfA, trigger factor.
- ***B. subtilis* module:** DesK sensor kinase, DesR response regulator, Δ5-desaturase/Des.
- ***A. baumannii* module:** LpxS acyltransferase; LpxL, LpxM, and LpxO as related lipid-A remodeling enzymes.
- **Compatible-solute module:** OtsA trehalose-6-phosphate synthase and OtsB trehalose-6-phosphate phosphatase.

### 2.4 Chemicals and lipid classes

| Node | Suggested grounding/handling |
|---|---|
| saturated fatty acid | ChEBI class; verify exact CURIE before YAML insertion |
| unsaturated fatty acid | ChEBI class; verify exact CURIE |
| palmitic acid / palmitate (16:0) | ChEBI; verify protonation-specific identifier |
| cis-vaccenic acid (18:1) | ChEBI; verify stereochemistry-specific identifier |
| palmitoleic acid (16:1) | ChEBI; verify identifier |
| octanoate (8:0) | ChEBI; verify charge-specific identifier |
| laurate (12:0) | ChEBI; verify identifier |
| trehalose | `CHEBI:27082` |
| glycerophospholipid | ChEBI class; verify identifier |
| lipid A / lipooligosaccharide | ChEBI or label-only pending exact form |
| ether lipids, sulfur aminolipids, glucuronosylglycerols | label-only pending structure-specific grounding |

### 2.5 Cellular components, functions, and processes

Candidate GO-grounded concepts include **plasma membrane** (`GO:0005886`), **fatty-acid biosynthetic process** (`GO:0006633`), **unsaturated fatty-acid biosynthetic process** (`GO:0006636`), **protein folding** (`GO:0006457`), **response to heat** (`GO:0009408`), and **response to cold** (`GO:0009409`). “Membrane fluidity” and “homeoviscous adaptation” should remain label-only unless the project’s ontology stack provides verified process terms.

## 3. Candidate causal edges

Predicates are proposed in readable form and can be normalized to the project’s relation vocabulary. “High” means direct or strongly synthesized mechanistic support; it does not mean universal across microbial taxa.

| # | Subject — predicate — object | Reference | Supporting snippet | Notes |
|---:|---|---|---|---|
| 1 | lower temperature — **decreases** — membrane fluidity | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5), October 2024 | “Low temperatures increase membrane lipid packing and reduce fluidity.” | **High; broadly physical.** Curation-ready (hoogerland2024atemperaturesensitivemetabolic pages 1-2). |
| 2 | increased unsaturated acyl-chain proportion — **increases** — membrane fluidity | DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x), March 2023 | “Membrane fluidity increases when the amount of unsaturated acyl chains…is higher.” | **High.** General membrane-physics edge (moon2023temperaturemattersbacterial pages 7-9). |
| 3 | higher temperature — **favors increase in** — saturated membrane acyl chains | same 2023 review | “Under heat stress, the proportion of saturated acyl chains…increases.” | **Moderate.** Common but lipid strategy varies among taxa (moon2023temperaturemattersbacterial pages 7-9). |
| 4 | temperature — **modulates activity of** — FabI | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5), October 2024 | FabI showed “~2-fold reduced activity at 27 °C versus 37 °C.” | **High; E. coli-specific quantitative result.** Curate under an *E. coli* context (hoogerland2024atemperaturesensitivemetabolic pages 5-6). |
| 5 | FabI/FabB branchpoint activity — **partitions flux between** — saturated and unsaturated fatty-acid synthesis | same 2024 study | A “temperature-sensitive metabolic valve…allocates flux between the saturated and unsaturated fatty acid synthesis pathways.” | **High; E. coli.** Core edge (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 1-2). |
| 6 | lower temperature plus reduced FabI activity relative to FabB — **biases flux toward** — unsaturated fatty-acid synthesis | same 2024 study | FabI activity falls at 27 °C, whereas FabB is comparatively temperature-stable. | **High; E. coli.** Mechanistic interpretation directly tested/modelled (hoogerland2024atemperaturesensitivemetabolic pages 5-6). |
| 7 | FabA — **introduces** — cis double bond into C10 fatty-acyl intermediate | DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4), July 2023 | “FabA introduces cis double-bonds in 10-carbon chains.” | **Moderate–high; E. coli pathway.** Use a structure-specific substrate only after chemical grounding (ramon2023ageneraloverview pages 2-4). |
| 8 | FabB — **elongates** — cis-unsaturated fatty-acyl intermediates | same 2023 review | “FabB elongates these intermediates.” | **Moderate–high; E. coli pathway** (ramon2023ageneraloverview pages 2-4). |
| 9 | FabR transcriptional feedback — **counteracts** — temperature-sensitive FabI/FabB metabolic valve | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | A slower FabR-dependent negative-feedback loop permits an initial overshoot and subsequent correction. | **High; E. coli.** Core regulation edge (hoogerland2024atemperaturesensitivemetabolic pages 9-10). |
| 10 | transient SFA/UFA synthesis overshoot — **accelerates restoration of** — adapted membrane composition | same 2024 study | The dual-timescale system “accelerates membrane adaptation” and restores optimal fluidity “within a single generation.” | **High; E. coli.** Avoid asserting a universal one-generation timescale (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 1-2). |
| 11 | homeoviscous lipid remodeling — **maintains** — membrane fluidity, permeability, and membrane-protein function | DOI: [10.1128/mbio.01295-21](https://doi.org/10.1128/mbio.01295-21), August 24, 2021 | Lipid alteration is “critical for maintaining membrane fluidity, permeability… and protein function.” | **High, broadly supported.** Suitable bridge to growth fitness (herrera2021homeoviscousadaptationof pages 1-3). |
| 12 | 37→20 °C downshift — **activates** — DesK→DesR→Δ5-desaturase pathway | DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x) | DesK detects the membrane state, phosphorylates DesR, and phosphorylated DesR activates desaturase transcription. | **Moderate; *B. subtilis*-specific.** Do not generalize to all mesophiles (moon2023temperaturemattersbacterial pages 7-9). |
| 13 | Δ5-desaturase — **adds** — cis double bonds to membrane fatty acids | same 2023 review | “D5-desaturase changes the lipid composition by adding cis double bonds.” | **Moderate; *B. subtilis*-specific** (moon2023temperaturemattersbacterial pages 7-9). |
| 14 | cold conditions — **upregulate** — LpxS | DOI: [10.1128/mbio.01295-21](https://doi.org/10.1128/mbio.01295-21), August 24, 2021 | “Expression of LpxS was highly upregulated under cold conditions.” | **High; *A. baumannii*-specific** (herrera2021homeoviscousadaptationof pages 1-3). |
| 15 | LpxS — **replaces C12:0 with** — C8:0 at lipid-A 2′ position | same 2021 primary study | “LpxS transfers an octanoate (C8:0)…replacing a C12:0 fatty acid.” | **High; taxon- and membrane-layer-specific** (herrera2021homeoviscousadaptationof pages 1-3). |
| 16 | LpxS-dependent C8:0 lipid-A incorporation — **increases** — outer-membrane permeability-barrier effectiveness under cold conditions | same 2021 study | C8:0 incorporation “increased the effectiveness of the outer membrane permeability barrier.” | **High for phenotype; fluidity mediation remains ‘likely.’** Preserve this distinction (herrera2021homeoviscousadaptationof pages 1-3). |
| 17 | heat shock / unfolded cytoplasmic proteins — **activates and stabilizes** — RpoH/σ32 | DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x), March 2023 | RpoH causes a “rapid and transient transcriptional increase” in heat-shock genes; DnaK retains it until heat-denatured proteins compete for the chaperone. | **High; E. coli boundary response.** Not a defining mesophily edge (moon2023temperaturemattersbacterial pages 3-5). |
| 18 | RpoH/σ32 — **upregulates** — heat-shock chaperones and proteases | DOI: [10.18006/2022.10(1).190.200](https://doi.org/10.18006/2022.10(1).190.200), February 2022 | RpoH is the “prime regulator” of most heat-shock genes, including chaperones and proteases. | **Moderate–high; E. coli-focused review.** Boundary-only (paul2022anoverviewof pages 3-5). |
| 19 | cold shock — **induces** — CspA | DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x) | CspA accounts for “~15% of total protein synthesis after a cold shock.” | **High; E. coli quantitative boundary response** (moon2023temperaturemattersbacterial pages 3-5). |
| 20 | CspA — **reduces inhibitory secondary structure in** — RNA at low temperature | DOI: [10.4161/rna.7.6.13482](https://doi.org/10.4161/rna.7.6.13482), November 1, 2010 | CspA-family proteins act through “RNA chaperoning function”; stabilized RNA structures otherwise inhibit transcription, degradation, and growth. | **High; E. coli boundary response** (phadtare2010rnaremodelingand pages 1-3). |
| 21 | low temperature — **upregulates** — trigger factor | DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x) | Trigger factor shows “~40-fold overexpression at low temperatures.” | **Moderate; context-dependent.** The same review warns that some chaperones are downregulated and overexpression can be harmful near 4 °C (moon2023temperaturemattersbacterial pages 7-9). |
| 22 | otsAB expression — **increases** — trehalose synthesis and cold tolerance | same 2023 review | The `otsAB` operon is induced by cold shock; trehalose helps *E. coli* withstand cold shock and stabilize membranes/proteins. | **Moderate; E. coli boundary response** (moon2023temperaturemattersbacterial pages 9-10). |
| 23 | temperature and phosphate availability — **remodel** — *D. alkenivorans* lipidome | DOI: [10.1073/pnas.2400711121](https://doi.org/10.1073/pnas.2400711121), published June 4, 2024 | The study identified “nearly 400 distinct lipids”; temperature and phosphate scarcity strongly affected lipidome composition. | **High; organism-specific recent evidence** (ding2024nitrogenandsulfur pages 1-2). |
| 24 | phosphate limitation — **induces replacement of** — phospholipids by sulfur-containing aminolipids | same 2024 PNAS study | Under phosphorus limitation, the organism “replaces phospholipids with significant numbers of sulfur-aminolipids.” | **High; *D. alkenivorans*-specific.** Relevant as an environmental modifier, not a core cause of mesophily (ding2024nitrogenandsulfur pages 1-2). |

The recommended core and boundary placement is summarized below.

| module | subject-predicate-object edge | exemplar taxon | evidence strength | curation recommendation |
|---|---|---|---|---|
| trait scope warning | mesophily **is_a** optimal-growth-temperature preference at intermediate temperatures; mesophily **not_equivalent_to** any single cold- or heat-shock pathway (horn2007structureandfunction pages 1-2, sen2022insightsonrigidity pages 1-3, siliakus2017adaptationsofarchaeal pages 3-5) | general microbial trait | Moderate | **Curate as scope note/warning.** Treat as organism-level phenotype; do not reduce trait to one mechanism. |
| core homeoviscous control | decreased temperature **decreases_activity_of** FabI (saturated-fatty-acid branch enzyme) (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 1-2) | *Escherichia coli* | High | **Curate.** Strong 2024 quantitative evidence; taxon exemplar likely broadly informative for mesophilic bacteria. |
| core homeoviscous control | FabI/FabB branchpoint balance **partitions_flux_between** saturated-fatty-acid synthesis and unsaturated-fatty-acid synthesis (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 1-2) | *Escherichia coli* | High | **Curate.** Central mechanistic edge for mesophilic membrane adaptation. |
| core homeoviscous control | decreased temperature **biases_flux_toward** unsaturated-fatty-acid synthesis via relative FabB robustness (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6) | *Escherichia coli* | High | **Curate.** Mark as primarily demonstrated in *E. coli*. |
| lipid composition outcome | increased unsaturated-fatty-acid proportion **increases** membrane fluidity (moon2023temperaturemattersbacterial pages 7-9, siliakus2017adaptationsofarchaeal pages 3-5, ding2024nitrogenandsulfur pages 1-2) | *Escherichia coli* / general bacteria | High | **Curate.** Generic supportive membrane-physics edge. |
| physiological outcome | homeoviscous lipid remodeling **maintains** membrane fluidity across temperature shifts (hoogerland2024atemperaturesensitivemetabolic pages 1-2, herrera2021homeoviscousadaptationof pages 1-3, ding2024nitrogenandsulfur pages 1-2) | general bacteria | High | **Curate.** Broad process edge, useful between lipid module and phenotype. |
| boundary heat response | heat shock **activates** RpoH/σ32 (moon2023temperaturemattersbacterial pages 3-5, paul2022anoverviewof pages 3-5) | *Escherichia coli* | High | **Boundary-only.** Useful for neighboring trait graphs or stress subgraphs, but not defining for mesophily itself. |
| boundary heat response | RpoH/σ32 **upregulates** DnaK-DnaJ-GrpE and GroEL-GroES heat-shock systems (paul2022anoverviewof pages 3-5, moon2023temperaturemattersbacterial pages 3-5) | *Escherichia coli* | High | **Boundary-only.** Curate only if graph includes upper-temperature-limit acclimation. |
| boundary cold response | cold shock **induces** CspA-family RNA chaperones (moon2023temperaturemattersbacterial pages 3-5, phadtare2010rnaremodelingand pages 1-3, horn2007structureandfunction pages 1-2) | *Escherichia coli* | High | **Boundary-only.** Represents acclimation below optimum, not mesophily per se. |
| boundary cold response | CspA **promotes** single-stranded RNA formation / limits inhibitory RNA secondary structure at low temperature (moon2023temperaturemattersbacterial pages 3-5, phadtare2010rnaremodelingand pages 1-3) | *Escherichia coli* | High | **Boundary-only.** Curate if modeling low-temperature boundary responses. |
| taxon-specific cold sensing | decreased temperature **activates** DesK/DesR two-component system (moon2023temperaturemattersbacterial pages 7-9) | *Bacillus subtilis* | Moderate | **Curate as taxon-specific/uncertain-generalization.** Good mechanistic exemplar, not universal. |
| taxon-specific desaturation | activated DesR **upregulates** Δ5-desaturase; Δ5-desaturase **introduces** cis double bonds into membrane fatty acids (moon2023temperaturemattersbacterial pages 7-9) | *Bacillus subtilis* | Moderate | **Curate as taxon-specific.** Strong model-system mechanism for Gram-positive mesophiles. |
| taxon-specific outer membrane adaptation | cold conditions **upregulate** LpxS (herrera2021homeoviscousadaptationof pages 1-3) | *Acinetobacter baumannii* | High | **Curate as taxon-specific.** Relevant for Gram-negative outer-membrane adaptation, not universal mesophile mechanism. |
| taxon-specific outer membrane adaptation | LpxS-mediated C8:0 incorporation into lipid A **likely_increases** outer-membrane fluidity / permeability fitness under cold conditions (herrera2021homeoviscousadaptationof pages 1-3) | *Acinetobacter baumannii* | Moderate | **Curate cautiously.** Mechanistically compelling but organism- and membrane-layer-specific. |


*Table: This table prioritizes curation-ready and boundary-only edges for a mesophilic TraitMech graph. It separates broadly useful homeoviscous-adaptation edges from taxon-specific or stress-boundary mechanisms so curators can decide what belongs in the core trait graph.*

## 4. Recent developments and quantitative findings

### 4.1 Rapid homeoviscous control in *E. coli* (2024)

Hoogerland and colleagues provide the most directly useful new mechanism for the existing `mesophilic_homoviscous_adaptation` graph. FabI activity was approximately **twofold lower at 27 °C than at 37 °C**, whereas FabB was comparatively temperature-stable. This creates a fast metabolic valve; slower FabR feedback adjusts FabB abundance and corrects the initial overshoot. The combined architecture permits membrane adaptation within **one generation** after a shock (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6). This is authoritative mechanistic evidence, but the authors’ hypothesis that core features will be ubiquitous remains a hypothesis rather than demonstrated microbial universality.

### 4.2 Mesophilic sulfate reducer with an ether-rich lipidome (2024)

The *D. alkenivorans* study broadens mesophile membrane biology beyond the standard ester-linked phospholipid model. Its membrane contains approximately **70–90% ether lipids**, and the analysis resolved **nearly 400 lipid species**. Temperature significantly affected double-bond equivalents (`P=0.004`) and alkyl/acyl-chain carbon number (`P=0.015`), while phosphate limitation had stronger effects (`P<0.001`). The first two lipidomic principal components explained **30.1% and 20.6%** of variance (ding2024nitrogenandsulfur pages 5-6, ding2024nitrogenandsulfur pages 1-2). These findings argue against curating “mesophilic membrane = ester phospholipids with one universal SFA/UFA ratio.”

### 4.3 Protein stability and flexibility

Mesophilic proteins should not be represented by a universal sequence rule. Comparative work found average atomic fluctuations generally ordered **psychrophilic > mesophilic > thermophilic**, but global packing factors did not cleanly separate the three classes (sen2022insightsonrigidity pages 1-3). In one homologous α-amylase comparison at 20 °C, extrapolated unfolding free energies were **3.7, 6.9, and 23.8 kcal/mol** for psychrophilic, mesophilic, and thermophilic enzymes, respectively—approximately a **1:2:6** stability ratio (feller2010proteinstabilityand pages 3-4). This is valuable context, not a safe generic causal edge from “mesophilic protein rigidity” to mesophilic growth.

## 5. Applications and real-world implementation

### Mesophilic anaerobic digestion

Mesophilic microbial communities are widely used to convert agricultural and municipal organic wastes into methane-rich biogas and digestate. A 2024 reactor study found that inoculum stored at **35 °C** had higher bacterial diversity than inoculum stored at **15 °C**, supporting stable mesophilic start-up. It also reported that full-scale initiation may require inoculum exceeding **1,000 m³** and commonly **10–60% of reactor volume**, demonstrating the operational importance of preservation temperature (wu2024effectoftemperature pages 1-2).

Community composition can causally constrain process performance. In the same study, Prevotellaceae relative abundances of **14.3%, 11.8%, and 2.7%** corresponded to butyrate concentrations of **2.5, 1.8, and 0.9 g/L**, respectively; accumulation of propionate and butyrate reduced operational capacity. Thermotogaceae abundance fell **44%** during transition from high to moderate temperature, yet its persistence was associated with hydrogenotrophic methanogenesis (wu2024effectoftemperature pages 11-12). These are reactor/community edges and should be kept outside the organism-level core trait graph.

A documented dry-digestion implementation heats feed to **35–40 °C** for mesophilic operation. Reported full-scale performance reached up to **10 m³ biogas per m³ active digester per day**; one 3,150-m³ digester treating 50,000 tonnes/year yielded **7.4 million m³ biogas at 55% methane** and approximately **9–10 million kWh/year** (hayyat2024areviewon pages 1-4). Because the retrieved document appears to be technical process literature rather than the correctly matched 2024 review text, use these figures for implementation context, not as primary evidence for biological causal edges.

### Biotechnology and pathogen control

- Mesophilic *E. coli* is a standard recombinant-production host. Cold-responsive promoters and chaperone systems can support lower-temperature expression of difficult proteins, but these are engineered applications of boundary responses rather than evidence defining mesophily.
- Understanding ambient-versus-host temperature responses is relevant to foodborne and clinical pathogens. The 2023 review links temperature-response mechanisms to food and hospital pathogen control and documents temperature-dependent biofilm regulation; for example, *E. coli* `bolA` transcription was reported **3.5-fold higher at 23 °C than at 37 °C** (moon2023temperaturemattersbacterial pages 9-10).

## 6. Recommended YAML graph architecture

A conservative graph should have three layers:

1. **Core phenotype layer**  
   `intermediate environmental temperature → favored cellular growth → METPO:1000615`

2. **Core supporting mechanism—homeoviscous adaptation**  
   `temperature → FabI/FabB flux partitioning → SFA/UFA composition → membrane fluidity/permeability → membrane-protein function → growth fitness`

3. **Optional boundary/taxon modules**  
   - cold: CspA/CsdA, trigger factor, trehalose;
   - heat: RpoH/RpoE, DnaK–DnaJ–GrpE, GroEL–GroES, proteases;
   - *B. subtilis*: DesK→DesR→Des;
   - *A. baumannii*: cold→LpxS→C8:0 lipid A;
   - *D. alkenivorans*: temperature/nutrient state→ether-rich lipidome remodeling.

Each edge should carry `taxon`, `temperature_before`, `temperature_after`, `medium`, `growth_phase`, `oxygen_status`, `assay`, `evidence_type`, and `uncertainty`. This prevents acute shock, steady-state acclimation, and evolutionary adaptation from being conflated.

## 7. Claims not yet suitable for TraitMech curation

1. **No universal mesophile gene set.** FabI/FabB/FabR is strongly supported in *E. coli*, but universality across bacteria, archaea, and fungi has not been demonstrated.
2. **Do not equate more unsaturated fatty acids with mesophily itself.** This is principally a response to cooling; composition is taxon-, medium-, nutrient-, growth-rate-, and membrane-layer-dependent.
3. **FabF requires careful placement.** It contributes to C18:1 production and cold adaptation, but the 2024 study found it non-essential for the core temperature response. Do not encode `FabF causes mesophily` (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6).
4. **Heat- and cold-shock regulons are boundary mechanisms.** They support survival after perturbation and may influence the growth range, but are not sufficient evidence for an intermediate optimum.
5. **Protein rigidity is not a single causal rule.** Differences are clearer locally than globally and vary among protein families (sen2022insightsonrigidity pages 1-3).
6. **LpxS is not generalizable beyond *Acinetobacter* without comparative evidence.** Its fluidity effect was described as likely, whereas improved permeability-barrier function was measured (herrera2021homeoviscousadaptationof pages 1-3).
7. **Reactor-community associations are not organism-level trait edges.** Family abundance–VFA correlations in anaerobic digestion can be affected by substrate and community succession.
8. **Avoid unverified ontology accessions.** Add UniProt, EC, Rhea, KEGG, MetaCyc, and structure-specific ChEBI identifiers only after checking the relevant organism, reaction, stereochemistry, and protonation state.
9. **Do not curate a hard universal 45 °C boundary.** Preserve the supplied METPO definition, but annotate literature-specific thresholds and measured optima.

## DOI-first bibliography

1. Hoogerland L, et al. “A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*.” *Nature Communications* 15 (October 2024). DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5). (hoogerland2024atemperaturesensitivemetabolic pages 9-10, hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 1-2)
2. Ding S, et al. “Nitrogen and sulfur for phosphorus: Lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions.” *PNAS* 121 (published June 4, 2024). DOI: [10.1073/pnas.2400711121](https://doi.org/10.1073/pnas.2400711121). (ding2024nitrogenandsulfur pages 5-6, ding2024nitrogenandsulfur pages 1-2)
3. Wu J, et al. “Effect of Temperature on the Inocula Preservation, Mesophilic Anaerobic Digestion Start-Up, and Microbial Community Dynamics.” *Agronomy* 14, 2991 (published December 16, 2024). DOI: [10.3390/agronomy14122991](https://doi.org/10.3390/agronomy14122991). (wu2024effectoftemperature pages 11-12, wu2024effectoftemperature pages 1-2)
4. Moon S, et al. “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology* 61:343–357 (March 2023). DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). (moon2023temperaturemattersbacterial pages 9-10, moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9)
5. Ramón A, et al. “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* 54:2259–2287 (July 2023). DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 22-23, ramon2023ageneraloverview pages 21-22, ramon2023ageneraloverview pages 2-4)
6. Sen S, Sarkar M. “Insights on Rigidity and Flexibility…in Homologous Psychrophilic, Mesophilic, and Thermophilic Proteins.” *Journal of Chemical Information and Modeling* 62:1916–1932 (April 2022). DOI: [10.1021/acs.jcim.1c01381](https://doi.org/10.1021/acs.jcim.1c01381). (sen2022insightsonrigidity pages 1-3)
7. Paul D, Ghosh S. “An overview of heat-stress response regulation in Gram-negative bacteria considering *Escherichia coli* as a model organism.” *Journal of Experimental Biology and Agricultural Sciences* 10:190–200 (February 2022). DOI: [10.18006/2022.10(1).190.200](https://doi.org/10.18006/2022.10(1).190.200). (paul2022anoverviewof pages 3-5)
8. Herrera CM, Voss BJ, Trent MS. “Homeoviscous Adaptation of the *Acinetobacter baumannii* Outer Membrane.” *mBio* 12:e01295-21 (August 24, 2021). DOI: [10.1128/mBio.01295-21](https://doi.org/10.1128/mBio.01295-21). (herrera2021homeoviscousadaptationof pages 1-3)
9. Siliakus MF, van der Oost J, Kengen SWM. “Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.” *Extremophiles* 21:651–670 (May 2017). DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 3-5)
10. Phadtare S, Severinov K. “RNA remodeling and gene regulation by cold shock proteins.” *RNA Biology* 7:788–795 (published online November 1, 2010). DOI: [10.4161/rna.7.6.13482](https://doi.org/10.4161/rna.7.6.13482). (phadtare2010rnaremodelingand pages 1-3)
11. Feller G. “Protein stability and enzyme activity at extreme biological temperatures.” *Journal of Physics: Condensed Matter* 22:323101 (July 2010). DOI: [10.1088/0953-8984/22/32/323101](https://doi.org/10.1088/0953-8984/22/32/323101). (feller2010proteinstabilityand pages 3-4)
12. Horn G, et al. “Structure and function of bacterial cold shock proteins.” *Cellular and Molecular Life Sciences* 64:1457–1470 (online April 16, 2007). DOI: [10.1007/s00018-007-6388-4](https://doi.org/10.1007/s00018-007-6388-4). (horn2007structureandfunction pages 1-2)

References

1. (sen2022insightsonrigidity pages 1-3): Srikanta Sen and Munna Sarkar. Insights on rigidity and flexibility at the global and local levels of protein structures and their roles in homologous psychrophilic, mesophilic, and thermophilic proteins: a computational study. Apr 2022. URL: https://doi.org/10.1021/acs.jcim.1c01381, doi:10.1021/acs.jcim.1c01381. This article has 14 citations and is from a peer-reviewed journal.

2. (hoogerland2024atemperaturesensitivemetabolic pages 9-10): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

3. (hoogerland2024atemperaturesensitivemetabolic pages 5-6): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

4. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

5. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

6. (horn2007structureandfunction pages 1-2): G. Horn, R. Hofweber, W. Kremer, and H. R. Kalbitzer. Structure and function of bacterial cold shock proteins. Cellular and Molecular Life Sciences, 64:1457-1470, Apr 2007. URL: https://doi.org/10.1007/s00018-007-6388-4, doi:10.1007/s00018-007-6388-4. This article has 351 citations and is from a domain leading peer-reviewed journal.

7. (siliakus2017adaptationsofarchaeal pages 3-5): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

8. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

9. (herrera2021homeoviscousadaptationof pages 1-3): Carmen M. Herrera, Bradley J. Voss, and M. Stephen Trent. Homeoviscous adaptation of the acinetobacter baumannii outer membrane: alteration of lipooligosaccharide structure during cold stress. Aug 2021. URL: https://doi.org/10.1128/mbio.01295-21, doi:10.1128/mbio.01295-21. This article has 35 citations and is from a domain leading peer-reviewed journal.

10. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

11. (paul2022anoverviewof pages 3-5): Deborupa Paul and Sanmitra Ghosh. An overview of heat-stress response regulation in gram-negative bacteria considering escherichia coli as a model organism. Journal of Experimental Biology and Agricultural Sciences, 10:190-200, Feb 2022. URL: https://doi.org/10.18006/2022.10(1).190.200, doi:10.18006/2022.10(1).190.200. This article has 1 citations.

12. (phadtare2010rnaremodelingand pages 1-3): Sangita Phadtare and Konstantin Severinov. Rna remodeling and gene regulation by cold shock proteins. RNA Biology, 7:788-795, Nov 2010. URL: https://doi.org/10.4161/rna.7.6.13482, doi:10.4161/rna.7.6.13482. This article has 225 citations and is from a peer-reviewed journal.

13. (moon2023temperaturemattersbacterial pages 9-10): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

14. (ding2024nitrogenandsulfur pages 1-2): Su Ding, Vincent Grossi, Ellen C. Hopmans, Nicole J. Bale, Cristiana Cravo-Laureau, and Jaap S. Sinninghe Damsté. Nitrogen and sulfur for phosphorus: lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2400711121, doi:10.1073/pnas.2400711121. This article has 12 citations and is from a highest quality peer-reviewed journal.

15. (ding2024nitrogenandsulfur pages 5-6): Su Ding, Vincent Grossi, Ellen C. Hopmans, Nicole J. Bale, Cristiana Cravo-Laureau, and Jaap S. Sinninghe Damsté. Nitrogen and sulfur for phosphorus: lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2400711121, doi:10.1073/pnas.2400711121. This article has 12 citations and is from a highest quality peer-reviewed journal.

16. (feller2010proteinstabilityand pages 3-4): Georges Feller. Protein stability and enzyme activity at extreme biological temperatures. Journal of Physics: Condensed Matter, 22:323101, Jul 2010. URL: https://doi.org/10.1088/0953-8984/22/32/323101, doi:10.1088/0953-8984/22/32/323101. This article has 421 citations and is from a domain leading peer-reviewed journal.

17. (wu2024effectoftemperature pages 1-2): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.

18. (wu2024effectoftemperature pages 11-12): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.

19. (hayyat2024areviewon pages 1-4): Umer Hayyat, Muhammad Usman Khan, Muhammad Sultan, Umair Zahid, Showkat Ahmad Bhat, and Mohd Muzamil. A review on dry anaerobic digestion: existing technologies, performance factors, challenges, and recommendations. Methane, 3:33-52, Jan 2024. URL: https://doi.org/10.3390/methane3010003, doi:10.3390/methane3010003. This article has 27 citations.

20. (ramon2023ageneraloverview pages 22-23): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

21. (ramon2023ageneraloverview pages 21-22): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.