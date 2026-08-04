---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:18:57.893048'
end_time: '2026-08-04T12:26:31.140673'
duration_seconds: 453.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: observation
  trait_identifier: METPO:1001000
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: observation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A data-collection or measurement context in which trait-relevant qualities
    of organisms, samples, or conditions are recorded.
  parent_traits: ''
  synonyms: ''
  evidence_summary: 'DOI:10.1371/journal.pone.0154556: data generated and the types
    of analysis performed (Supports observation as an investigation/data-generation
    context.) | DOI:10.1371/journal.pone.0154556: the output of an assay is typically
    a data item (Supports observations as links between assays, measurements, and
    data.)'
  causal_graph_summary: 'observation_measurement_upper_context: 14 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** observation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1001000
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A data-collection or measurement context in which trait-relevant qualities of organisms, samples, or conditions are recorded.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1371/journal.pone.0154556: data generated and the types of analysis performed (Supports observation as an investigation/data-generation context.) | DOI:10.1371/journal.pone.0154556: the output of an assay is typically a data item (Supports observations as links between assays, measurements, and data.)
- **Existing causal graph summary:** observation_measurement_upper_context: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **observation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/observation.yaml`.

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
- **Trait label:** observation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1001000
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A data-collection or measurement context in which trait-relevant qualities of organisms, samples, or conditions are recorded.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1371/journal.pone.0154556: data generated and the types of analysis performed (Supports observation as an investigation/data-generation context.) | DOI:10.1371/journal.pone.0154556: the output of an assay is typically a data item (Supports observations as links between assays, measurements, and data.)
- **Existing causal graph summary:** observation_measurement_upper_context: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **observation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/observation.yaml`.

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


# Curation-focused report: microbial trait **observation**

**Target:** `METPO:1001000`  
**Category:** UPPER | **Kind:** CLASS | **Mapping:** REVIEWED

## Executive assessment

`METPO:1001000` should be modeled as an **investigation and measurement context**, not as a microbial phenotype, physiological capacity, pathway, or environmental preference. It connects an evaluant or specimen, its biological and environmental context, the assay and protocol used, the resulting data item, and any later interpretation. This reading is consistent with the supplied definition and with the Ontology for Biomedical Investigations (OBI), where an assay is a planned process whose output is typically a data item, while a conclusion is a separate information entity based on the generated data. (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 8-9)

Consequently, the most defensible TraitMech graph is a **measurement-provenance graph**. Genes, proteins, enzymes, pathways, metabolites, and electron donors or acceptors belong beneath a *specific observed microbial trait*—for example nitrate reduction, growth on glucose, or antimicrobial resistance—not directly beneath generic “observation.” Adding them to this upper class without a specified evaluant and assay would imply biological causality that the term does not express.

## 1. Scope and boundaries

### Positive scope

An observation context should capture:

1. **What was evaluated:** organism, strain, community, culture, specimen, or environmental sample.
2. **Under what conditions:** medium, temperature, pH, oxygen regime, exposure, location, collection time, host state, and other relevant biological or environmental metadata.
3. **How it was evaluated:** assay, protocol, instrument, reagents, sampling, preservation, extraction, sequencing, imaging, or other measurement processes.
4. **What was recorded:** qualitative call, numerical measurement, image-derived feature, taxonomic profile, sequence-derived feature, or another data item.
5. **How reliability was assessed:** controls, reference materials, replicates, calibration, detection limits, and quality-control data.
6. **What was inferred later:** a conclusion or phenotype assertion supported by—but not identical to—the observation datum.

OBI’s input–process–output pattern directly supports this interpretation: assays take material inputs and generate specified data outputs; protocols and study designs guide procedures; and conclusions based on data are distinguished from the data generated during study execution. (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 8-9, bandrowski2016theontologyfor pages 9-11)

### Boundary cases

- **Observation versus assay:** the assay is the planned measurement process; observation is the broader recording context that may include assay, evaluant, conditions, and output.
- **Observation versus data item:** a datum is the information output, not the entire context that generated it.
- **Observation versus conclusion:** “OD600 = 0.42” or “growth detected” is an observation/data output; “the strain can grow anaerobically on nitrate” is an interpreted trait assertion requiring stated conditions and decision criteria.
- **Observation versus phenotype:** phenotype is the organismal quality or disposition being estimated. The observation is evidence about that phenotype.
- **Observation versus observational study:** the target term is not restricted to epidemiological observational designs; it can cover laboratory, field, sequencing, imaging, and computationally derived measurement contexts.
- **Observation versus environmental preference:** temperature, pH, salinity, oxygen, nutrients, and host factors contextualize a measurement. They become causal biological factors only in a graph for a specified microbial response.
- **Observation versus in silico prediction:** a genome-scale model or classifier output may be recorded as a prediction, but it should not be represented as a direct experimental observation unless separately validated.

## 2. Candidate nodes grouped by type

### Core investigation entities

- **observation** — `METPO:1001000`
- assay — OBI candidate; verify the exact current OBI CURIE before YAML insertion
- investigation
- study design
- protocol / plan specification
- instrument or measurement device
- operator or laboratory
- computational analysis process
- conclusion based on data

### Material and biological entities

- evaluant
- specimen
- microbial isolate
- microbial strain
- microbial community
- culture
- environmental sample
- reference material
- mock community
- spike-in control organism or DNA

These should be specialized with NCBITaxon or other identifiers only when a concrete taxon is part of a specific observation record.

### Environmental and experimental factors

- sampling location and time
- habitat or environmental material — ENVO candidates
- growth medium
- incubation temperature
- pH
- salinity
- oxygen availability or atmosphere
- nutrient concentration
- antimicrobial or inhibitor exposure
- inoculum density
- incubation duration
- sample collection method
- preservation method and storage conditions
- homogenization or cell-disruption method
- DNA/RNA extraction method
- library-preparation method
- sequencing platform and depth
- batch, plate, and well position

A recent microbiome metadata review distinguishes assay metadata—such as machine, date, and reagent kit—from biological metadata such as sample conditions, drug exposure, housing, and genetic information. It also identifies collection time and place, temperature, salinity, pH, extraction, primers, library kits, instrumentation, batch effects, diet, medication, and lifestyle as variables needed for valid interpretation. (kumar2024acomprehensiveoverview pages 11-12)

### Information entities and measured qualities

- data item — IAO candidate; verify exact CURIE in the ontology release used by TraitMech
- measurement datum
- qualitative observation
- quantitative observation
- taxonomic relative-abundance profile
- sequence data
- image data
- optical-density datum
- viable-count datum
- fluorescence or luminescence datum
- metabolite-abundance datum
- detection/non-detection call
- uncertainty, detection limit, and quality-control datum

### Biological mechanism nodes

No generic gene, protein, enzyme, transporter, complex, pathway, metabolite, electron donor, or electron acceptor should be attached directly to `METPO:1001000`. Such nodes become appropriate only in a narrower graph, for example:

- nitrate + nitrate reductase + electron-transport pathway → observed nitrate respiration;
- glucose transporter + glycolysis → observed growth on glucose;
- β-lactamase + cefotaxime hydrolysis → observed cefotaxime resistance.

Those are examples of graph patterns, **not evidence-backed edges proposed for this generic target**.

## 3. Candidate causal and provenance edges

The following table is the recommended compact graph backbone.

| subject | predicate | object | suggested grounding | evidence status | curation note |
|---|---|---|---|---|---|
| METPO:1001000 observation | has part (candidate) | assay | subject: METPO:1001000; object: OBI assay [exact CURIE not verified here] | robust | OBI treats assays as planned investigative processes within the broader investigation context; good upper-level backbone edge for observation-centered graph, while keeping relation wording provisional. (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 8-9) |
| assay | has specified input / has material input (candidate) | specimen or evaluant | object candidates: specimen [label], evaluant role [label; OBI/IAO terms mentioned in OBI modeling] | robust | OBI modeling consistently distinguishes assay inputs from outputs; use a generic specimen/evaluant node unless a subtype of observation is known. (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 9-11) |
| assay | has specified output (candidate) | data item | object candidate: IAO data item [exact CURIE not verified here] | robust | Directly supported by OBI statement that assay output is typically a data item; this is one of the safest curation edges. (bandrowski2016theontologyfor pages 8-9) |
| protocol | guides / concretizes (candidate) | assay | protocol [label or OBI protocol term if later verified] | moderate | OBI represents protocols and study designs as plan specifications guiding procedures; relation wording should remain candidate pending exact ontology property choice. (bandrowski2016theontologyfor pages 8-9) |
| instrument | participates in (candidate) | assay | instrument/device [label; OBI instrument functions discussed] | moderate | OBI describes instrument functions such as measurement within experimental procedures; curate conservatively as participation unless a precise relation is chosen. (bandrowski2016theontologyfor pages 9-11) |
| environmental or experimental condition | contextualizes (candidate) | METPO:1001000 observation | object candidates: environment [ENVO label], pH/salinity/temperature [label/PATO or ENVO if later verified] | moderate | Recent microbiome metadata reviews emphasize collection time, location, temperature, salinity, pH, drug exposure, housing, and other contextual variables as necessary metadata for interpreting observations. (kumar2024acomprehensiveoverview pages 11-12) |
| sample processing | precedes (candidate) | assay | sample processing [label] | moderate | Recent workflow literature separates sampling, preservation, extraction, and preparation from downstream sequencing assay; useful provenance edge, but generic unless a specific assay subtype is curated. (kumar2024acomprehensiveoverview pages 11-12, forry2024variabilityandbias pages 1-2) |
| DNA extraction method | influences measured abundance/profile of (candidate) | taxonomic profile data item | DNA extraction method [label]; taxonomic profile data item [label] | assay-specific, robust | Interlaboratory evidence shows extraction choices significantly affect MGS results and can introduce bias; curate as assay-specific influence on measured profile, not organism biology. (forry2024variabilityandbias pages 2-3, forry2024variabilityandbias pages 7-8, forry2024variabilityandbias pages 9-10) |
| sequencing or analysis strategy | influences measured abundance/profile of (candidate) | taxonomic profile data item | sequencing strategy [16S/WGS label]; bioinformatic analysis strategy [label] | assay-specific, robust | Forry et al. found analysis strategy, sequencing depth, and related methodological choices significantly altered readouts; safe as observation-pipeline influence edge. (forry2024variabilityandbias pages 9-10, forry2024variabilityandbias pages 8-9) |
| reference material or control | enables bias assessment of (candidate) | assay output / measured profile | reference material [label]; control [label] | robust | Shared stool references, mock communities, and spike-ins were used to estimate variability and compare measurements to ground truth; good edge for observation quality-control subgraph. (forry2024variabilityandbias pages 1-2, forry2024variabilityandbias pages 7-8, forry2024variabilityandbias pages 8-9) |
| data item | supports (candidate) | conclusion based on data | conclusion based on data [label; OBI concept mentioned] | robust | OBI explicitly separates generated data from later interpretation/conclusion; important boundary edge to prevent collapsing observation into inference. (bandrowski2016theontologyfor pages 8-9) |


*Table: This table summarizes compact candidate nodes and edges for curating METPO:1001000 observation as an investigation and measurement context. It emphasizes robust provenance relations while flagging assay-specific influence edges that affect measured microbial profiles rather than microbial biology itself.*

### Expanded evidence notes and supporting snippets

| Proposed triple | Supporting snippet | Reference | Curation assessment |
|---|---|---|---|
| `observation context —has part→ assay` | “Assays are processes that produce data items as outputs.” | Bandrowski et al., 2016 | **Strong conceptual support.** Predicate remains provisional because METPO’s relation vocabulary must be checked. (bandrowski2016theontologyfor pages 8-9) |
| `assay —has material input→ specimen/evaluant` | OBI represents assays as planned processes that take “material inputs (specimens, isolates).” | Bandrowski et al., 2016 | **Strong.** Use a generic label until the exact OBI class/property is verified. (bandrowski2016theontologyfor pages 11-13) |
| `assay —has specified output→ data item` | “The output of an assay is typically a data item.” | Bandrowski et al., 2016 | **Strongest candidate edge.** This is directly aligned with the supplied existing evidence. (bandrowski2016theontologyfor pages 8-9) |
| `protocol —guides→ assay` | “Protocols and study designs are plan specifications that guide procedures.” | Bandrowski et al., 2016 | **Moderate–strong.** Verify whether `is concretized as`, `achieves planned objective`, or another OBI relation is preferred. (bandrowski2016theontologyfor pages 8-9) |
| `instrument —participates in→ assay` | OBI represents “instrument functions like measurement” in experimental procedures. | Bandrowski et al., 2016 | **Moderate.** Participation is safer than asserting direct causation. (bandrowski2016theontologyfor pages 9-11) |
| `environmental/experimental condition —contextualizes→ observation` | Relevant metadata include “collection date/time, location coordinates…temperature, salinity, pH,” plus diet, medication, and lifestyle. | Kumar et al., 2024 | **Strong contextual edge; not necessarily causal.** Conditions should be attached to the observation or evaluant-at-time rather than asserted as organism-level causes by default. (kumar2024acomprehensiveoverview pages 11-12) |
| `sample processing —precedes→ assay` | The workflow distinguishes sampling, preservation, extraction, library preparation, sequencing, and analysis. | Kumar et al., 2024; Forry et al., 2024 | **Strong provenance pattern.** Specific process subclasses are preferable to one undifferentiated node. (forry2024variabilityandbias pages 1-2, kumar2024acomprehensiveoverview pages 11-12) |
| `DNA extraction method —influences→ measured taxonomic profile` | “DNA extraction protocol, extraction kit manufacturer…significantly impact results.” | Forry et al., 2024 | **Strong but assay-specific.** The affected object is the measured profile, not the underlying organismal trait. (forry2024variabilityandbias pages 7-8) |
| `homogenization method —influences robustness of→ measured profile` | Homogenization equipment “reduces inter-lab variability despite not changing mean abundances.” | Forry et al., 2024 | **Moderate, assay-specific.** Preserve the distinction between precision/robustness and mean bias. (forry2024variabilityandbias pages 7-8) |
| `sequencing/analysis strategy —influences→ measured profile` | “Choice of analysis strategy (16S vs WGS) had statistically significant effects”; extraction and sequencing depth also affected outcomes. | Forry et al., 2024 | **Strong, assay-specific.** Consider separate nodes for sequencing assay and bioinformatic analysis. (forry2024variabilityandbias pages 9-10) |
| `reference material/control —enables assessment of→ measurement bias` | Five stool samples and two mock communities enabled assessment of variability and bias against ground truth. | Forry et al., 2024 | **Strong.** This is preferable to saying the control biologically causes the observation. (forry2024variabilityandbias pages 2-3, forry2024variabilityandbias pages 1-2) |
| `reference-database coverage —influences detectability of→ taxon` | A spike-in organism showed low abundance/non-detection attributed partly to “bioinformatic database gaps.” | Forry et al., 2024 | **Moderate, uncertain mechanism.** Multiple explanations were possible; represent as an uncertain assay-specific influence. (forry2024variabilityandbias pages 7-8) |
| `data item —supports→ conclusion based on data` | OBI “distinguishes between data generated during investigation execution and conclusions based on that data.” | Bandrowski et al., 2016 | **Strong conceptual boundary.** Avoid collapsing the observation output and inferred trait assertion. (bandrowski2016theontologyfor pages 8-9) |

## 4. Recent developments, implementation, and quantitative evidence

### Interlaboratory measurement bias

The most directly relevant 2024 evidence is the Mosaic Standards Challenge. **Forty-four laboratories** analyzed **seven shared reference samples**—five human stool samples and two mock communities—using their usual protocols. They returned **30 16S rRNA datasets and 14 WGS datasets**, while approximately **100 protocol variables** were captured per participating workflow. Protocol choices significantly affected measurement bias and interlaboratory robustness, and consensus across laboratories could still disagree with ground truth. (forry2024variabilityandbias pages 2-3, forry2024variabilityandbias pages 1-2, forry2024variabilityandbias pages 8-9)

This has a major graph-design implication: an observed abundance is not solely a function of the sampled microbial system. It is also a product of extraction, library preparation, platform, depth, database, and analytical workflow. Those factors should therefore point to the **measurement output**, rather than being modeled as causes of the organism’s intrinsic phenotype. The study also found non-random method adoption: nearly half of 16S participants used the same extraction kit, while only about **4%** used a non-Illumina platform. (forry2024variabilityandbias pages 8-9)

### Standardized contextual metadata in public-health surveillance

Feng et al. analyzed **1,498** free-text environmental swab-site descriptions from **nine facilities**, identified **five informational facets** containing **338 unique terms**, and obtained approval for **21 new ontology term requests**. Their schema was implemented in NCBI’s **One Health Enteric Metadata Package**. In an applied analysis, *Listeria monocytogenes* positivity was significantly elevated for wheels (**28/128**) and brooms (**8/11**; P<0.05), illustrating how structured observation context enables aggregate epidemiological interpretation. (feng2023aschemafor pages 7-8)

This is a real-world implementation of the proposed graph pattern: specimen collection site and structure contextualize a detection observation, which then supports a surveillance conclusion. The contextual entity should not be confused with the assay output itself.

### Current expert consensus

Recent authoritative reviews emphasize that missing or heterogeneous metadata can prevent valid stratification, confound statistical interpretation, and impair machine-learning generalization. Kumar et al. state that absent comprehensive metadata may make downstream statistical and even qualitative interpretation challenging or impossible. They recommend recording metadata across the whole sampling-to-analysis chain and applying appropriate normalization and batch correction. (kumar2024acomprehensiveoverview pages 11-12)

OBI supplies the mature semantic pattern needed to implement this recommendation: planned processes, material inputs, roles, instruments, data outputs, and conclusions are represented as distinct entities connected by explicit relations. OBI also reuses domain ontologies such as GO and PATO, allowing a generic observation framework to link to biological mechanisms only when a specific assay and phenotype warrant doing so. (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 9-11)

## 5. Ontology-grounding recommendations

### Safe to insert now

- `METPO:1001000` — observation; retain exactly as supplied.

### Ground by label now; resolve CURIE before merge

- assay — OBI
- specimen — OBI
- evaluant role — OBI
- protocol / plan specification — OBI
- data item — IAO
- conclusion based on data — OBI/IAO
- measurement datum — IAO/OBI
- instrument — OBI
- reference material and quality-control roles — OBI
- environmental material, habitat, and location — ENVO
- measured qualities such as temperature, concentration, opacity, and abundance — PATO/CHMO/OBI as appropriate

This conservative approach is preferable because no identifier should be guessed from a label. Record the ontology release used during final resolution, since labels and axioms can change.

### Relation recommendations

Prefer established OBO relations where verified in the local dependency set:

- `has specified input`
- `has specified output`
- `has participant`
- `precedes`
- `is about`
- `realizes`
- `is concretized as`
- `has quality`

If TraitMech uses a simplified causal predicate vocabulary, distinguish at least:

1. **structural/provenance:** has-part, input-of, output-of, precedes;
2. **contextual:** measured-under, collected-from, contextualized-by;
3. **measurement influence:** affects-measured-value-of;
4. **epistemic:** supports, contradicts, or is-evidence-for.

A generic `causes` predicate would be misleading for most edges in this graph.

## 6. Recommended initial YAML graph content

The first revision of `data/traits/upper/observation.yaml` should contain a small, general backbone:

1. observation context → assay;
2. specimen/evaluant → assay input;
3. environmental and experimental conditions → observation context;
4. protocol → assay;
5. instrument → assay;
6. assay → data item;
7. control/reference material → quality or bias assessment;
8. data item → conclusion based on data.

A second, explicitly assay-specific branch may include sampling, preservation, extraction, sequencing, and computational analysis as processes that influence the resulting measurement. These should not be represented as universal biological mechanisms.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not attach metabolic pathways or genes directly to generic observation.** No source supports a universal biological mechanism for this upper context class.
2. **Do not equate observation with phenotype.** An observed value is evidence for a phenotype assertion and may be affected by measurement error.
3. **Do not treat relative abundance as absolute organism abundance.** The cited interlaboratory study used compositional ratio analysis specifically because MGS outputs are compositional. (forry2024variabilityandbias pages 9-10)
4. **Do not interpret laboratory consensus as accuracy.** Consensus measurements can retain substantial bias relative to ground truth. (forry2024variabilityandbias pages 7-8)
5. **Do not curate database coverage → taxon absence as a certain causal edge.** Non-detection may reflect extraction inefficiency, low abundance, database gaps, or other pipeline effects. (forry2024variabilityandbias pages 7-8)
6. **Do not generalize extraction, platform, or homogenization effects across all microbial assays.** These are robust for the reported metagenomic workflows but remain assay-, matrix-, and taxon-dependent.
7. **Do not infer environmental causality from contextual metadata alone.** Location, pH, temperature, host state, and exposure can be confounders, selection conditions, or causes; the relation requires an explicit study design.
8. **Do not insert unverified CURIEs.** Label-only nodes are preferable until exact identifiers and ontology versions are confirmed.
9. **Do not encode conclusions as raw outputs.** Preserve the OBI distinction between generated data and conclusions based on those data. (bandrowski2016theontologyfor pages 8-9)

## DOI-first bibliography

1. Bandrowski A, et al. **The Ontology for Biomedical Investigations.** *PLoS ONE*. Published April 2016. DOI: [10.1371/journal.pone.0154556](https://doi.org/10.1371/journal.pone.0154556). (bandrowski2016theontologyfor pages 11-13, bandrowski2016theontologyfor pages 8-9, bandrowski2016theontologyfor pages 9-11)
2. Forry SP, et al. **Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols.** *Scientific Reports*. Published April 2024. DOI: [10.1038/s41598-024-57981-4](https://doi.org/10.1038/s41598-024-57981-4). (forry2024variabilityandbias pages 2-3, forry2024variabilityandbias pages 1-2, forry2024variabilityandbias pages 7-8, forry2024variabilityandbias pages 9-10, forry2024variabilityandbias pages 8-9)
3. Kumar B, Lorusso E, Fosso B, Pesole G. **A comprehensive overview of microbiome data in the light of machine learning applications: categorization, accessibility, and future directions.** *Frontiers in Microbiology*. Published February 2024. DOI: [10.3389/fmicb.2024.1343572](https://doi.org/10.3389/fmicb.2024.1343572). (kumar2024acomprehensiveoverview pages 11-12)
4. Feng J, et al. **A schema for digitized surface swab site metadata in open-source DNA sequence databases.** *mSystems*. Published April 2023. DOI: [10.1128/msystems.01284-22](https://doi.org/10.1128/msystems.01284-22). (feng2023aschemafor pages 7-8)

## Final curation recommendation

Retain `METPO:1001000` as an upper-level **observation/measurement context** and orient its causal graph around provenance, measurement, contextual conditions, controls, and epistemic support. The scientifically strongest new content is not a universal molecular mechanism but the explicit representation that assay and preprocessing choices can causally affect the **recorded data item**, while that data item only subsequently supports a phenotype conclusion. This preserves biological and epistemic correctness and provides a reusable backbone for narrower microbial TraitMech graphs.

References

1. (bandrowski2016theontologyfor pages 11-13): Anita Bandrowski, Ryan Brinkman, Mathias Brochhausen, Matthew H. Brush, Bill Bug, Marcus C. Chibucos, Kevin Clancy, Mélanie Courtot, Dirk Derom, Michel Dumontier, Liju Fan, Jennifer Fostel, Gilberto Fragoso, Frank Gibson, Alejandra Gonzalez-Beltran, Melissa A. Haendel, Yongqun He, Mervi Heiskanen, Tina Hernandez-Boussard, Mark Jensen, Yu Lin, Allyson L. Lister, Phillip Lord, James Malone, Elisabetta Manduchi, Monnie McGee, Norman Morrison, James A. Overton, Helen Parkinson, Bjoern Peters, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H. Scheuermann, Daniel Schober, Barry Smith, Larisa N. Soldatova, Christian J. Stoeckert, Chris F. Taylor, Carlo Torniai, Jessica A. Turner, Randi Vita, Patricia L. Whetzel, and Jie Zheng. The ontology for biomedical investigations. PLoS ONE, 11:e0154556, Apr 2016. URL: https://doi.org/10.1371/journal.pone.0154556, doi:10.1371/journal.pone.0154556. This article has 517 citations and is from a peer-reviewed journal.

2. (bandrowski2016theontologyfor pages 8-9): Anita Bandrowski, Ryan Brinkman, Mathias Brochhausen, Matthew H. Brush, Bill Bug, Marcus C. Chibucos, Kevin Clancy, Mélanie Courtot, Dirk Derom, Michel Dumontier, Liju Fan, Jennifer Fostel, Gilberto Fragoso, Frank Gibson, Alejandra Gonzalez-Beltran, Melissa A. Haendel, Yongqun He, Mervi Heiskanen, Tina Hernandez-Boussard, Mark Jensen, Yu Lin, Allyson L. Lister, Phillip Lord, James Malone, Elisabetta Manduchi, Monnie McGee, Norman Morrison, James A. Overton, Helen Parkinson, Bjoern Peters, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H. Scheuermann, Daniel Schober, Barry Smith, Larisa N. Soldatova, Christian J. Stoeckert, Chris F. Taylor, Carlo Torniai, Jessica A. Turner, Randi Vita, Patricia L. Whetzel, and Jie Zheng. The ontology for biomedical investigations. PLoS ONE, 11:e0154556, Apr 2016. URL: https://doi.org/10.1371/journal.pone.0154556, doi:10.1371/journal.pone.0154556. This article has 517 citations and is from a peer-reviewed journal.

3. (bandrowski2016theontologyfor pages 9-11): Anita Bandrowski, Ryan Brinkman, Mathias Brochhausen, Matthew H. Brush, Bill Bug, Marcus C. Chibucos, Kevin Clancy, Mélanie Courtot, Dirk Derom, Michel Dumontier, Liju Fan, Jennifer Fostel, Gilberto Fragoso, Frank Gibson, Alejandra Gonzalez-Beltran, Melissa A. Haendel, Yongqun He, Mervi Heiskanen, Tina Hernandez-Boussard, Mark Jensen, Yu Lin, Allyson L. Lister, Phillip Lord, James Malone, Elisabetta Manduchi, Monnie McGee, Norman Morrison, James A. Overton, Helen Parkinson, Bjoern Peters, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H. Scheuermann, Daniel Schober, Barry Smith, Larisa N. Soldatova, Christian J. Stoeckert, Chris F. Taylor, Carlo Torniai, Jessica A. Turner, Randi Vita, Patricia L. Whetzel, and Jie Zheng. The ontology for biomedical investigations. PLoS ONE, 11:e0154556, Apr 2016. URL: https://doi.org/10.1371/journal.pone.0154556, doi:10.1371/journal.pone.0154556. This article has 517 citations and is from a peer-reviewed journal.

4. (kumar2024acomprehensiveoverview pages 11-12): Bablu Kumar, Erika Lorusso, Bruno Fosso, and Graziano Pesole. A comprehensive overview of microbiome data in the light of machine learning applications: categorization, accessibility, and future directions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1343572, doi:10.3389/fmicb.2024.1343572. This article has 107 citations and is from a peer-reviewed journal.

5. (forry2024variabilityandbias pages 1-2): Samuel P. Forry, Stephanie L. Servetas, Jason G. Kralj, Keng Soh, Michalis Hadjithomas, Raul Cano, Martha Carlin, Maria G. de Amorim, Benjamin Auch, Matthew G. Bakker, Thais F. Bartelli, Juan P. Bustamante, Ignacio Cassol, Mauricio Chalita, Emmanuel Dias-Neto, Aaron Del Duca, Daryl M. Gohl, Jekaterina Kazantseva, Muyideen T. Haruna, Peter Menzel, Bruno S. Moda, Lorieza Neuberger-Castillo, Diana N. Nunes, Isha R. Patel, Rodrigo D. Peralta, Adrien Saliou, Rolf Schwarzer, Samantha Sevilla, Isabella K. T. M. Takenaka, Jeremy R. Wang, Rob Knight, Dirk Gevers, and Scott A. Jackson. Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-57981-4, doi:10.1038/s41598-024-57981-4. This article has 77 citations and is from a peer-reviewed journal.

6. (forry2024variabilityandbias pages 2-3): Samuel P. Forry, Stephanie L. Servetas, Jason G. Kralj, Keng Soh, Michalis Hadjithomas, Raul Cano, Martha Carlin, Maria G. de Amorim, Benjamin Auch, Matthew G. Bakker, Thais F. Bartelli, Juan P. Bustamante, Ignacio Cassol, Mauricio Chalita, Emmanuel Dias-Neto, Aaron Del Duca, Daryl M. Gohl, Jekaterina Kazantseva, Muyideen T. Haruna, Peter Menzel, Bruno S. Moda, Lorieza Neuberger-Castillo, Diana N. Nunes, Isha R. Patel, Rodrigo D. Peralta, Adrien Saliou, Rolf Schwarzer, Samantha Sevilla, Isabella K. T. M. Takenaka, Jeremy R. Wang, Rob Knight, Dirk Gevers, and Scott A. Jackson. Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-57981-4, doi:10.1038/s41598-024-57981-4. This article has 77 citations and is from a peer-reviewed journal.

7. (forry2024variabilityandbias pages 7-8): Samuel P. Forry, Stephanie L. Servetas, Jason G. Kralj, Keng Soh, Michalis Hadjithomas, Raul Cano, Martha Carlin, Maria G. de Amorim, Benjamin Auch, Matthew G. Bakker, Thais F. Bartelli, Juan P. Bustamante, Ignacio Cassol, Mauricio Chalita, Emmanuel Dias-Neto, Aaron Del Duca, Daryl M. Gohl, Jekaterina Kazantseva, Muyideen T. Haruna, Peter Menzel, Bruno S. Moda, Lorieza Neuberger-Castillo, Diana N. Nunes, Isha R. Patel, Rodrigo D. Peralta, Adrien Saliou, Rolf Schwarzer, Samantha Sevilla, Isabella K. T. M. Takenaka, Jeremy R. Wang, Rob Knight, Dirk Gevers, and Scott A. Jackson. Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-57981-4, doi:10.1038/s41598-024-57981-4. This article has 77 citations and is from a peer-reviewed journal.

8. (forry2024variabilityandbias pages 9-10): Samuel P. Forry, Stephanie L. Servetas, Jason G. Kralj, Keng Soh, Michalis Hadjithomas, Raul Cano, Martha Carlin, Maria G. de Amorim, Benjamin Auch, Matthew G. Bakker, Thais F. Bartelli, Juan P. Bustamante, Ignacio Cassol, Mauricio Chalita, Emmanuel Dias-Neto, Aaron Del Duca, Daryl M. Gohl, Jekaterina Kazantseva, Muyideen T. Haruna, Peter Menzel, Bruno S. Moda, Lorieza Neuberger-Castillo, Diana N. Nunes, Isha R. Patel, Rodrigo D. Peralta, Adrien Saliou, Rolf Schwarzer, Samantha Sevilla, Isabella K. T. M. Takenaka, Jeremy R. Wang, Rob Knight, Dirk Gevers, and Scott A. Jackson. Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-57981-4, doi:10.1038/s41598-024-57981-4. This article has 77 citations and is from a peer-reviewed journal.

9. (forry2024variabilityandbias pages 8-9): Samuel P. Forry, Stephanie L. Servetas, Jason G. Kralj, Keng Soh, Michalis Hadjithomas, Raul Cano, Martha Carlin, Maria G. de Amorim, Benjamin Auch, Matthew G. Bakker, Thais F. Bartelli, Juan P. Bustamante, Ignacio Cassol, Mauricio Chalita, Emmanuel Dias-Neto, Aaron Del Duca, Daryl M. Gohl, Jekaterina Kazantseva, Muyideen T. Haruna, Peter Menzel, Bruno S. Moda, Lorieza Neuberger-Castillo, Diana N. Nunes, Isha R. Patel, Rodrigo D. Peralta, Adrien Saliou, Rolf Schwarzer, Samantha Sevilla, Isabella K. T. M. Takenaka, Jeremy R. Wang, Rob Knight, Dirk Gevers, and Scott A. Jackson. Variability and bias in microbiome metagenomic sequencing: an interlaboratory study comparing experimental protocols. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-57981-4, doi:10.1038/s41598-024-57981-4. This article has 77 citations and is from a peer-reviewed journal.

10. (feng2023aschemafor pages 7-8): Jingzhang Feng, Devin Daeschel, Damion Dooley, Emma Griffiths, Marc Allard, Ruth Timme, Yi Chen, and Abigail B. Snyder. A schema for digitized surface swab site metadata in open-source dna sequence databases. mSystems, Apr 2023. URL: https://doi.org/10.1128/msystems.01284-22, doi:10.1128/msystems.01284-22. This article has 13 citations and is from a peer-reviewed journal.