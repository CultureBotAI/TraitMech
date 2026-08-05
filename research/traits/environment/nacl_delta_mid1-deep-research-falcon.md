---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:34:05.384005'
end_time: '2026-08-04T01:42:30.810582'
duration_seconds: 505.43
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta mid1
  trait_identifier: METPO:1000480
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately\
    \ 1\u20133% (w/v), characteristic of organisms with modest salinity tolerance\
    \ breadth."
  parent_traits: METPO:1000335
  synonyms: Nad_1_3
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports intermediate breadths as common among osmoadaptive bacteria.)'
  causal_graph_summary: 'nacl_delta_mid1_modest_breadth: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000480
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 1–3% (w/v), characteristic of organisms with modest salinity tolerance breadth.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_1_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports intermediate breadths as common among osmoadaptive bacteria.)
- **Existing causal graph summary:** nacl_delta_mid1_modest_breadth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **NaCl delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid1.yaml`.

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
- **Trait label:** NaCl delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000480
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 1–3% (w/v), characteristic of organisms with modest salinity tolerance breadth.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_1_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports intermediate breadths as common among osmoadaptive bacteria.)
- **Existing causal graph summary:** nacl_delta_mid1_modest_breadth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **NaCl delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid1.yaml`.

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


# Curation report: NaCl delta mid1

## Executive assessment

**Target:** “METPO:1000480” — *NaCl delta mid1* (synonym **Nad_1_3**), parent **METPO:1000335**.

The most defensible interpretation is an **assay-derived NaCl growth-breadth class**: the difference between the highest and lowest tested NaCl concentrations that support growth is approximately **1–3 percentage points (w/v)**. It is not the NaCl optimum, maximum tolerated concentration, minimum salt requirement, or a claim that growth occurs specifically at 1–3% NaCl. This distinction matters because organisms can have a narrow optimum inside a much wider growth range; for example, *Spiribacter salinus* had an optimum near 0.8 M NaCl but a reported growth range of roughly 0.6–2.0 M. (leon2018compatiblesolutesynthesis pages 4-5)

The literature strongly supports a general osmoadaptation chain—hyperosmotic water loss, K⁺/counterion accumulation, compatible-solute synthesis or uptake, and regulated solute release—but does **not** establish a mechanism unique to the 1–3% breadth bin. Accordingly, the graph should represent mechanisms that **contribute to growth across an NaCl interval**, while the terminal edge to “METPO:1000480” remains inferred unless phenotype-matched perturbation data are obtained.

## 1. Trait scope and boundaries

### Operational definition

A recommended computable interpretation is:

`NaCl_delta = maximum growth-supporting NaCl (% w/v) − minimum growth-supporting NaCl (% w/v)`

Assign “METPO:1000480” when the measured delta is approximately 1–3 percentage points under a declared assay protocol. Record the tested concentration grid because coarse spacing can turn a continuous phenotype into an artificial bin.

“Growth-supporting” should require a prespecified endpoint, preferably reproducible increase in biomass or viable count rather than survival alone. Growth rate, lag time, final yield, and area under the growth curve are not interchangeable. Likewise, plate growth, broth turbidity, colony formation, and short-term viability can yield different boundaries.

### Boundary cases

- **Not NaCl optimum:** the concentration supporting fastest growth can lie anywhere within the interval.
- **Not maximum NaCl tolerance:** an organism growing from 0–2% and one growing from 6–8% have the same 2-point delta but very different salinity preferences.
- **Not obligate halophily:** the class does not specify whether growth occurs at 0% NaCl.
- **Not survival/VBNC formation:** detectable viability without multiplication should not define a growth-supporting boundary.
- **Not total salinity:** NaCl percentage does not capture Mg²⁺, K⁺, sulfate, water activity, or ionic-strength effects in natural brines.
- **Assay dependence:** medium osmolytes, compatible solutes, carbon source, pH, temperature, aeration, inoculum history, and adaptation time can shift both endpoints. Compatible-solute availability is especially important because exogenous glycine betaine can materially improve osmoprotection. (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 10-11)

## 2. Current mechanistic understanding

A hyperosmotic NaCl upshift rapidly draws water out of bacterial cells. A 2024 authoritative review reports volume losses ranging from several percent to approximately 50%, with reduced turgor and increased macromolecular crowding and ionic strength. Cells first accumulate K⁺ with counterions such as glutamate, then commonly replace much of this ionic osmolyte pool with less perturbing compatible solutes such as glycine betaine, trehalose, proline, or ectoine. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 2-4)

The reverse transition is also relevant to **breadth**. During hypoosmotic downshift, mechanosensitive channels rapidly release osmolytes, limiting excessive turgor and lysis. Thus, a strain’s measurable interval may depend on both high-salt adaptation and safe recovery when salinity falls. (leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 13-16)

The second messenger cyclic di-AMP is now viewed as a major cell-volume regulator in many Firmicutes, Actinobacteria, and Cyanobacteria. It restricts K⁺ and compatible-solute influx and promotes K⁺ efflux. Directly characterized targets include Ktr/Trk-type systems and OpuA-like ABC importers; c-di-AMP also acts through the BusR regulator. These are strong causal mechanisms in c-di-AMP-using lineages, but they are not universal bacterial mechanisms. (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 31-33, foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 12-13)

## 3. Candidate graph nodes

### Trait and environmental nodes

- **NaCl delta mid1** — “METPO:1000480”
- Parent trait — **METPO:1000335**
- sodium chloride — **CHEBI:26710**
- hyperosmotic NaCl exposure — label-only candidate
- hypoosmotic downshift — label-only candidate
- extracellular osmolarity / water activity — label-only candidates
- growth-supporting NaCl minimum, maximum, and breadth — assay-result nodes
- growth under NaCl stress — label-only process/phenotype node

### Chemicals and metabolites

- potassium ion — **CHEBI:29103**
- sodium ion — **CHEBI:29101**
- chloride — **CHEBI:17996**
- L-glutamate — **CHEBI:29985**
- L-proline — **CHEBI:17203**
- glycine betaine — **CHEBI:17750**
- ectoine — **CHEBI:16919**
- trehalose — **CHEBI:27082**
- cyclic di-AMP — use the current ChEBI record after identifier validation; do not guess the CURIE
- hydroxyectoine, glutamine, carnitine, and arsenobetaine — optional secondary osmolytes; validate CURIEs before use

### Genes, proteins, and complexes

- **EctA/EctB/EctC** — ectoine-biosynthesis enzymes; genes often denoted `ectABC`, although noncanonical arrangements occur
- **EctD** — ectoine hydroxylase; taxon/context dependent
- **OpuA/OpuC and ProU-family ABC importers** — compatible-solute uptake
- **Ktr/Trk systems**, including KtrAB/TrkAH and TrkG/TrkH — K⁺ uptake
- **KdpFABC/KdpDE** — high-affinity K⁺ transport and regulation
- **KimA** — K⁺ importer in characterized c-di-AMP lineages
- **BusR** — c-di-AMP-responsive compatible-solute transport regulator
- **Mrp Na⁺/H⁺ antiporter complex** — sodium extrusion candidate
- **MscL/MscS-family mechanosensitive channels** — emergency osmolyte release
- c-di-AMP cyclases/phosphodiesterases — include only when the organism’s proteins are identified

Do not assign UniProt accessions without selecting a specific organism and protein sequence. Gene symbols alone are preferable to an incorrect cross-taxon accession.

### Pathways, functions, and cellular locations

- compatible-solute biosynthesis
- compatible-solute transmembrane transport
- potassium-ion transport
- sodium/proton antiport
- response to osmotic stress — **GO:0006970**
- transmembrane transport — **GO:0055085**
- plasma membrane — **GO:0005886**
- cytoplasm — **GO:0005737**
- maintenance of turgor/cell volume
- macromolecular-crowding homeostasis
- ectoine biosynthesis, glycine-betaine uptake, trehalose biosynthesis, and proline/glutamate metabolism — pathway nodes; validate KEGG/MetaCyc identifiers against the taxon before insertion

## 4. Candidate causal edges

The following condensed graph distinguishes directly supported mechanisms from associations and phenotype-level inference.

| subject | predicate | object | evidence strength/qualifier |
|---|---|---|---|
| NaCl osmotic upshift | causes | water efflux and cell volume loss | Strong, general bacterial physiology; direct review synthesis (foster2024bacterialcellvolume pages 6-8) |
| K+ uptake | restores | osmotic balance / turgor after hyperosmotic stress | Strong, general; direct mechanism across bacteria (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 1-2) |
| glutamate counterion | supports | electroneutrality during K+ accumulation | Strong, general; direct review synthesis (foster2024bacterialcellvolume pages 6-8) |
| ectoine biosynthesis | increases | compatible-solute pool | Strong in moderate halophiles; direct metabolite evidence in *Spiribacter salinus* (leon2018compatiblesolutesynthesis pages 10-11) |
| glycine betaine import | increases | osmoprotection under salt stress | Strong in tested taxa; direct transport/osmoprotection evidence (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 10-11) |
| compatible-solute pool | supports | growth under NaCl stress | Moderate-strong; direct in tested halophiles, generalizable with caution (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 10-11, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| c-di-AMP | inhibits | K+ import | Strong in c-di-AMP-utilizing lineages; direct regulatory mechanism (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 12-13) |
| c-di-AMP | inhibits | OpuA/OpuC-type compatible-solute uptake | Strong but lineage/transporter-specific; direct binding/regulation evidence (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) |
| hypoosmotic downshift | activates | mechanosensitive channels | Strong, general; direct review synthesis (leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 13-16) |
| mechanosensitive channels | release | osmolytes / solutes | Strong, general; direct review synthesis (leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 13-16) |
| Na+/H+ antiporter | exports | sodium ions | Moderate; general/genomic support, often not directly assayed for this trait bin; curate as uncertain (leon2018compatiblesolutesynthesis pages 4-5) |
| compatible-solute accumulation + ion homeostasis | contributes_to | METPO:1000480 NaCl delta mid1 | Weak/inferred; plausible determinant of modest breadth, not directly proven for the discretized trait class (leon2018compatiblesolutesynthesis pages 4-5, leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 6-8) |


*Table: This table lists compact candidate causal edges for a NaCl breadth TraitMech graph, emphasizing which links are directly supported versus inferred or taxon-specific. It is useful for deciding which edges can be curated now and which should remain tentative.*

### Evidence table with curation snippets

| Proposed triple | Reference and supporting snippet | Curation note |
|---|---|---|
| hyperosmotic NaCl exposure — **causes** → water efflux/cell-volume loss | Foster et al. 2024: water “rapidly leaves cells”; volume loss ranges from “several percent to 50%.” DOI: [10.1128/mmbr.00181-23](https://doi.org/10.1128/mmbr.00181-23). (foster2024bacterialcellvolume pages 6-8) | **Strong/general physiology.** NaCl combines osmotic and ionic effects; represent the immediate osmotic edge separately from Na⁺ toxicity. |
| water efflux — **decreases** → turgor pressure | Foster et al. 2024 reports reduced turgor following hyperosmotic volume loss. (foster2024bacterialcellvolume pages 6-8) | **Strong.** Suitable as a core edge. |
| K⁺ uptake — **increases** → intracellular osmolarity | Cells respond by importing potassium and counterions after osmotic upshift. (foster2024bacterialcellvolume pages 6-8) | **Strong but transporter implementation varies.** |
| glutamate accumulation — **supports** → electroneutrality during K⁺ accumulation | The review identifies glutamate as a prominent K⁺ counterion. (foster2024bacterialcellvolume pages 6-8) | **Strong/generalized**, but other counterions occur. |
| ectoine biosynthesis — **increases** → intracellular compatible-solute pool | In *S. salinus*, ectoine increased from about 80 µM at 0.6 M NaCl to 170 µM at 0.8 M; measured over 0.6–1.6 M NaCl. DOI: [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108). (leon2018compatiblesolutesynthesis pages 10-11) | **Direct, taxon-specific metabolite evidence.** Concentrations are far above the target’s 1–3% interval, so do not use them to set the trait bin. |
| glycine-betaine import — **increases** → intracellular compatible-solute pool | Radiolabeled transport showed that glycine-betaine accumulation was “sensitively tied” to medium salinity; glycine betaine and arsenobetaine were most effective in osmoprotection assays. (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 10-11) | **Direct in *S. salinus*.** Good pathway edge, not proof of the terminal trait class. |
| compatible-solute accumulation — **reduces** → ionic-strength stress while maintaining osmotic balance | Cells replace K⁺ with compatible solutes such as glycine betaine and proline that balance osmolality without strongly perturbing ionic strength. (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 6-8) | **Strong review-level mechanism.** |
| c-di-AMP — **inhibits** → K⁺ import | High c-di-AMP reduces K⁺ import; transporter-binding affinities summarized across systems span about 40 nM–8 µM. (foster2024bacterialcellvolume pages 6-8) | **Strong in c-di-AMP-utilizing taxa; not universal.** |
| c-di-AMP — **inhibits** → OpuA/OpuC-type compatible-solute uptake | c-di-AMP binds CBS domains of OpuA/OpuC-type systems and RCK_C domains of BusR, negatively regulating uptake. (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) | **Strong but lineage/transporter-specific.** OpuC architecture varies; curate exact protein only with organism-specific evidence. |
| hypoosmotic downshift — **activates** → mechanosensitive channels | Mechanosensitive channels provide sub-second relief after osmotic downshift. (foster2024bacterialcellvolume pages 13-16) | **Strong/general.** |
| mechanosensitive-channel opening — **causes** → osmolyte release | Channel opening releases osmolytes/solutes and prevents damaging excess turgor. (leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 13-16) | **Strong.** Add MscL or MscS only with taxon-specific evidence. |
| Mrp Na⁺-extrusion system — **decreases** → cytoplasmic Na⁺ | *S. salinus* encodes a multicomponent Mrp system, alongside TrkG/TrkH K⁺ systems. (leon2018compatiblesolutesynthesis pages 4-5) | **Uncertain/genomic association in this source.** Do not encode as experimentally demonstrated for this organism or trait. |
| compatible-solute/ion homeostasis — **contributes to** → “METPO:1000480” | The mechanisms support growth across salinity ranges, but no retrieved perturbation study maps them specifically to a 1–3% w/v delta. (leon2018compatiblesolutesynthesis pages 4-5, leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 6-8) | **Inferred terminal edge.** Use `contributes_to` with an uncertainty/evidence qualifier, not `causes`. |

## 5. Recent developments and quantitative findings

### 2024: cell volume as the unifying regulatory target

Foster, van den Noort, and Poolman argue that c-di-AMP is a master regulator of cell volume rather than merely a generic stress signal. Their synthesis connects K⁺ transport, compatible-solute uptake, amino-acid transport, K⁺ efflux, and cell-wall physiology. A key quantitative point is that hyperosmotic shock can reduce cytoplasmic volume by up to approximately 50%; characterized c-di-AMP interactions with K⁺-transport gating components span nanomolar-to-low-micromolar affinities. (foster2024bacterialcellvolume pages 31-33, foster2024bacterialcellvolume pages 6-8)

### 2024: hybrid salt-in/salt-out strategies

A multi-omics study of *Natranaerobius thermophilus* found simultaneous K⁺ accumulation and compatible-solute use under 2.5–4.3 M Na⁺. Amino-acid-related proteins accounted for 7.2% of differentially expressed proteins and carbohydrate/energy metabolism for 14.3%; four transport/metabolism genes were induced more than 100-fold. The organism is an extreme polyextremophile, so these results update the conceptual model but are **not quantitatively transferable** to modest 1–3% breadth organisms. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), published May 2024. (xing2024thepolyextremophilenatranaerobius pages 10-14)

### Context-dependent osmolyte choice

*Halorhodospira halophila* switches from KCl to glycine betaine near 1 g/L environmental KCl; K⁺ limitation reduced cytoplasmic K⁺ by more than tenfold. This demonstrates that external K⁺ and nutrient composition can change the mechanism observed at the same salinity and therefore should be modeled as experimental-factor nodes. DOI: [10.1038/s41598-020-59231-9](https://doi.org/10.1038/s41598-020-59231-9), published February 2020. (deole2020apotassiumchloride pages 8-8)

### Evolutionary interpretation

Recent large-scale phylogenomics shows that adaptation between freshwater, brackish, and marine environments involves changes in K⁺ uptake systems, Na⁺/Ca²⁺ antiporters, mechanosensitive channels, proteome amino-acid composition, and gene content. Such comparative evidence is useful for nominating nodes, but gene presence is not equivalent to causal determination of an isolate’s measured NaCl delta. DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059), published May 2023.

## 6. Applications and real-world relevance

1. **Strain selection and industrial fermentation.** NaCl-growth curves can identify production strains likely to remain active despite salinity changes. Compatible-solute engineering and transporter control are relevant to ectoine production, food fermentation, saline feedstocks, and robust whole-cell biocatalysis. However, a 1–3% breadth alone does not establish process suitability; absolute endpoints and productivity must also be measured.
2. **Food microbiology.** Growth breadth helps distinguish organisms that merely survive salt preservation from those capable of multiplying. Assay standardization is important because lag, growth rate, yield, and area under the curve classify tolerance differently.
3. **Agriculture and saline-soil inoculants.** Salt-adapted plant-associated bacteria are being developed as biostimulants, but plant benefits arise through additional traits—exopolysaccharides, nutrient mobilization, hormones, and antioxidant effects—not simply microbial NaCl breadth.
4. **Wastewater and bioprocess stability.** Osmoadaptation modules can guide selection or engineering of organisms exposed to fluctuating conductivity and salinity. Mechanosensitive release systems matter when reactors undergo dilution as well as salt loading.
5. **Environmental forecasting.** Breadth measurements can inform niche models under freshwater salinization, but natural salinity is multionic and cannot be represented completely by NaCl-only assays.

## 7. Recommended minimal TraitMech graph

A conservative first version should contain the following backbone:

1. `hyperosmotic_NaCl_exposure causes water_efflux`
2. `water_efflux decreases cell_volume`
3. `cell_volume_loss decreases turgor_pressure`
4. `osmotic_upshift activates potassium_uptake`
5. `potassium_uptake increases intracellular_osmolarity`
6. `compatible_solute_biosynthesis increases compatible_solute_pool`
7. `compatible_solute_import increases compatible_solute_pool`
8. `compatible_solute_pool supports osmotic_balance`
9. `osmotic_balance supports growth_under_NaCl`
10. `hypoosmotic_downshift activates mechanosensitive_channel`
11. `mechanosensitive_channel releases osmolytes`
12. `growth_under_NaCl contributes_to “METPO:1000480”` **[inferred]**

Add c-di-AMP regulation only for a taxon known to synthesize and use this messenger. Add ectABC, ProU/Opu, Trk/Ktr/Kdp, Mrp, MscL, or MscS as organism-specific refinements rather than universally required nodes.

## 8. Claims not yet suitable for TraitMech curation

- **Do not claim that ectoine, glycine betaine, c-di-AMP, Mrp, or any single gene causes the 1–3% delta class.** No retrieved study tested that discretized outcome directly.
- **Do not treat gene presence as functional evidence.** Genome annotations for Trk, Mrp, transporters, or ectoine genes are candidate-generating evidence unless supported by expression, metabolite, transport, knockout, or complementation data.
- **Do not generalize c-di-AMP to all microbes.** Its cell-volume role is strong in several bacterial lineages but absent or differently implemented elsewhere. (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 12-13)
- **Do not use extreme-halophile concentrations to calibrate this trait.** The 2.5–4.3 M experiments in *N. thermophilus* establish possible mechanisms, not the biology of a modest percentage-point breadth. (xing2024thepolyextremophilenatranaerobius pages 10-14)
- **Do not equate total salinity with NaCl.** Natural brines and saline soils have distinct ionic compositions.
- **Do not encode exact 1% and 3% cutoffs without confirming METPO’s binning convention.** “Approximately” implies a curation policy is needed for endpoints, rounding, and concentration-grid resolution.
- **Do not merge high-salt adaptation and low-salt recovery.** Compatible-solute accumulation and mechanosensitive release are directionally opposite but jointly influence measured breadth.

## DOI-first bibliography

1. Foster AJ, van den Noort M, Poolman B. **Bacterial cell volume regulation and the importance of cyclic di-AMP.** *Microbiology and Molecular Biology Reviews*. Published June 2024. DOI: [10.1128/mmbr.00181-23](https://doi.org/10.1128/mmbr.00181-23). (foster2024bacterialcellvolume pages 13-16, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 31-33, foster2024bacterialcellvolume pages 6-8)
2. Xing Q et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.** *Applied and Environmental Microbiology*. Published May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 10-14)
3. Jurdzinski KT et al. **Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.** *Science Advances*. Published May 2023. DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059).
4. León MJ et al. **Compatible Solute Synthesis and Import by the Moderate Halophile Spiribacter salinus: Physiology and Genomics.** *Frontiers in Microbiology*. Published February 2018. DOI: [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108). (leon2018compatiblesolutesynthesis pages 4-5, leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 10-11)
5. Deole R, Hoff WD. **A potassium chloride to glycine betaine osmoprotectant switch in the extreme halophile Halorhodospira halophila.** *Scientific Reports*. Published February 2020. DOI: [10.1038/s41598-020-59231-9](https://doi.org/10.1038/s41598-020-59231-9). (deole2020apotassiumchloride pages 8-8)
6. Gunde-Cimerman N, Plemenitaš A, Oren A. **Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.** *FEMS Microbiology Reviews*. Published May 2018. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). This is the supplied existing evidence and provides broad osmoadaptation context, but it does not by itself prove a mechanism specific to “METPO:1000480”.

References

1. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

2. (leon2018compatiblesolutesynthesis pages 1-2): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

3. (leon2018compatiblesolutesynthesis pages 10-11): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

4. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

5. (foster2024bacterialcellvolume pages 2-4): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

6. (foster2024bacterialcellvolume pages 13-16): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

8. (foster2024bacterialcellvolume pages 31-33): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

9. (foster2024bacterialcellvolume pages 1-2): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

10. (foster2024bacterialcellvolume pages 12-13): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

12. (deole2020apotassiumchloride pages 8-8): Ratnakar Deole and Wouter D. Hoff. A potassium chloride to glycine betaine osmoprotectant switch in the extreme halophile halorhodospira halophila. Scientific Reports, Feb 2020. URL: https://doi.org/10.1038/s41598-020-59231-9, doi:10.1038/s41598-020-59231-9. This article has 45 citations and is from a peer-reviewed journal.