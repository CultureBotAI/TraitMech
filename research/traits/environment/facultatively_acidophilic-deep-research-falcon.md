---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:35:12.322367'
end_time: '2026-08-04T00:41:46.355472'
duration_seconds: 394.03
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively acidophilic
  trait_identifier: METPO:1003007
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by optimal growth in acidic environments
    (pH below 5.5) with the capacity to also grow at near-neutral pH values.
  parent_traits: METPO:1003000
  synonyms: facultative acidophile
  evidence_summary: 'DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level
    example supports acidic-to-near-neutral growth capacity in a mildly acidophilic
    bacterium.)'
  causal_graph_summary: 'facultatively_acidophilic_ph_homeostasis: 15 nodes, 14 edges'
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
- **Trait label:** facultatively acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 15 nodes, 14 edges

## Research Objective

Research the microbial trait **facultatively acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_acidophilic.yaml`.

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
- **Trait label:** facultatively acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 15 nodes, 14 edges

## Research Objective

Research the microbial trait **facultatively acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_acidophilic.yaml`.

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


# Curation report: facultatively acidophilic

## 1. Scope summary

**Target:** `METPO:1003007` — **facultatively acidophilic**  
**Category:** ENVIRONMENT · **Term kind:** CLASS · **Status:** REVIEWED  
**Parent:** `METPO:1003000`  
**Operational definition:** optimal growth in acidic conditions, below pH 5.5, together with reproducible growth at near-neutral pH.

This is an **organism-level growth-preference phenotype**, not merely survival after acid shock. For curation, evidence should ideally report growth rate or biomass across a controlled pH series and demonstrate both (i) an acidic optimum and (ii) growth near neutrality. A recent review places moderate acidophiles at approximately pH 3–5 optimum and extreme acidophiles at pH ≤3 optimum; another uses a broader moderate-acidophile range of pH 3–7.5 with optima near pH 4–5. These conventions overlap the target but do not themselves establish facultative acidophily. (gonzalez2024acidophilicheterotrophsbasic pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 2-4)

A useful phenotype example is the mildly acidophilic methanotroph class with optima at pH 5.0–5.5 and reported ranges of pH 4.2–7.2. This directly spans acidic to near-neutral conditions and is closer to the target than an extreme acidophile that cannot grow near neutrality. (yao2023howmethanotrophsrespond pages 4-5)

### Boundary cases

* **Acid tolerant but not acidophilic:** survives low pH, but optimum remains near neutral. Do not annotate as `METPO:1003007` without an acidic growth optimum.
* **Obligate/extreme acidophile:** optimum below pH 3 but no demonstrated near-neutral growth. Relevant mechanistic evidence may be imported cautiously, but the organism does not establish the target phenotype.
* **Broad-pH environmental occurrence:** metagenomic detection at acidic and alkaline sites is not equivalent to cultured growth. For example, *Ca.* Eremiobacteria occurred predominantly below pH 6 but also in 19 alkaline samples; this is ecological association, not proof that individual organisms grow across that range. (ji2021candidatuseremiobacterotaa pages 7-9)
* **Acid resistance or acid-shock response:** transient survival, stationary-phase persistence, or induced stress genes do not establish a growth preference.
* **“Facultative” metabolism:** facultative anaerobiosis, autotrophy, or methanotrophy is unrelated to facultative acidophily.
* **Assay dependence:** medium composition, organic acids, chloride, temperature, oxygen, and growth phase can shift the apparent pH range and must be captured as experimental context.

## 2. Current mechanistic model

The best-supported general model is layered pH homeostasis. Acidic extracellular conditions create a large inward proton gradient. A relatively proton-impermeable envelope and an inside-positive membrane potential reduce proton entry; antiporters and other proton-removal systems expel protons that enter; decarboxylation and ammonia-generating reactions consume or buffer cytoplasmic protons. Together these processes preserve a near-neutral cytoplasm and permit growth at low external pH. Comparative genomics indicates that acidophilic Acidithiobacillia acquired or expanded many such systems relative to neutrophilic relatives, but much of that evidence remains predictive rather than perturbational. (gonzalezrosales2022integrativegenomicssheds pages 1-2, gonzalezrosales2022integrativegenomicssheds pages 9-12)

Direct physiology supports the central role of this architecture. *Methylacidiphilum* sp. RTK17.1 maintained intracellular pH 6.52 ± 0.04 across external pH 1.5–3.0. A measured inside-positive potential of 5.86 mV at external pH 2–3 opposed proton entry. Although this organism is an extreme thermoacidophile rather than a demonstrated facultative acidophile, the experiment strongly supports the core pH-homeostasis edges. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 1-2)

Recent work also reinforces the general importance of membrane potential and antiporters in bacterial pH homeostasis, but extrapolation from neutrophiles to facultative acidophiles should be explicit rather than treated as trait-specific proof.

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

* `METPO:1003007` — facultatively acidophilic
* `METPO:1003000` — supplied parent trait
* acidic external pH / acidic environment — label-level environmental condition; verify the exact ENVO term during implementation
* near-neutral external pH — label-only candidate
* extracellular-to-cytoplasmic proton gradient — label-only candidate
* pH growth-range assay — experimental-factor node
* medium composition, temperature, oxygen availability, growth phase — experimental modifiers

### Chemicals and ions

* proton — `CHEBI:15378`
* potassium ion — `CHEBI:29103`
* sodium ion — `CHEBI:29101`
* chloride — `CHEBI:17996`
* ammonia — `CHEBI:16134`
* formic acid — `CHEBI:30751`
* amino-acid substrates for decarboxylation — ground separately only when the specific system is demonstrated

### Structures and cellular states

* cytoplasm — `GO:0005737`
* plasma membrane — `GO:0005886`
* outer membrane — `GO:0019867`, where applicable
* proton-impermeable/low-permeability membrane — label-only state
* inside-positive membrane potential — label-only electrophysiological state
* intracellular pH homeostasis — `GO:0030003`
* cytosolic acidification — label-only state
* proton motive force — label-only candidate unless a suitable stable ontology term is verified

### Genes, proteins, and complexes

* KdpABC high-affinity K⁺ uptake system; KdpD/KdpE regulatory system
* Trk potassium-uptake system
* Kch potassium channel
* NhaA and NhaP Na⁺/H⁺ antiporters
* ClcA Cl⁻/H⁺ antiporter
* glutamate decarboxylase system, including Gad/GDAR components
* arginine decarboxylase system
* urease complex
* squalene-hopene cyclase and the hopanoid-biosynthesis module
* spermidine/polyamine-associated envelope module
* respiratory-chain proton-translocation machinery and ATPase: plausible candidates, but no sufficiently trait-specific evidence was recovered here for gene-level curation

Gene symbols are not universal ortholog identifiers. They should be grounded to organism-specific UniProt, KEGG Orthology, EC, or Rhea records only after the taxon and reaction are fixed.

### Processes and outcomes

* potassium uptake
* generation of inside-positive membrane potential
* restriction of passive proton influx
* proton export by antiport
* cytoplasmic proton consumption
* ammonia-mediated buffering
* maintenance of circumneutral intracellular pH
* growth under acidic conditions
* growth at near-neutral pH
* organic-acid uncoupling and cytosolic acidification
* chloride-associated disruption of the electrical barrier

## 4. Candidate causal edges

The following table is the proposed starting set. “Strong” means direct physiological evidence, but several strong edges remain **taxon-specific to an extreme acidophile**, not direct evidence from a facultatively acidophilic isolate.

| subject | predicate | object | evidence strength | DOI | short exact/near-exact supporting snippet | curation note |
|---|---|---|---|---|---|---|
| acidic environment (ENVO:00002009) | causes increased influx of | proton (CHEBI:15378) | moderate, review/general | 10.3389/fmicb.2021.822229 | “preventing proton influx that allows the cell to maintain a near-neutral cytoplasmic pH” (gonzalezrosales2022integrativegenomicssheds pages 1-2) | General acidophile mechanism underlying the trait; not specific to one facultative acidophile assay. |
| hopanoid biosynthesis | decreases permeability to | proton (CHEBI:15378) | weak, genomic-inference-only | 10.1038/s41396-021-00944-8 | “hopanoid biosynthesis genes (squalene-hopene cyclase) that reduce membrane proton permeability” (ji2021candidatuseremiobacterotaa pages 10-12) | Candidate node only; inference from genomes of Ca. Eremiobacterota, not direct experiment. |
| potassium uptake | produces | inside-positive membrane potential | moderate, review/inference | 10.1038/s41396-021-00944-8 | “potassium uptake systems… maintaining inside-positive membrane potential as a proton charge barrier” (ji2021candidatuseremiobacterotaa pages 10-12) | Mechanistically relevant first-line defense; genomic inference in Ca. Eremiobacterota. |
| inside-positive membrane potential | inhibits entry of | proton (CHEBI:15378) | strong, direct experiment but taxon-specific | 10.3389/fmicb.2021.651744 | “employs a reversed membrane potential (inside-positive Δψ = 5.86 mV at external pH 2-3), which mechanistically inhibits extracellular proton entry” (carere2021growthonformic pages 4-5) | Direct physiological evidence from thermoacidophile Methylacidiphilum sp. RTK17.1; use as taxon-specific support for broader mechanism. |
| Na+/H+ antiporter NhaA | exports | proton (CHEBI:15378) | weak, review/genomic-inference-only | 10.3389/fmicb.2021.822229 | “The excerpt identifies proton extrusion mechanisms including Na+/H+ antiporters (NhaA, NhaP)” (gonzalezrosales2022integrativegenomicssheds pages 9-12) | Broad acidophile mechanism; source is comparative genomics/review, not direct perturbation. |
| Na+/H+ antiporter NhaP | exports | proton (CHEBI:15378) | weak, review/genomic-inference-only | 10.3389/fmicb.2021.822229 | “The excerpt identifies proton extrusion mechanisms including Na+/H+ antiporters (NhaA, NhaP)” (gonzalezrosales2022integrativegenomicssheds pages 9-12) | Same as above; keep uncertain until species-level experimental evidence is added. |
| amino-acid decarboxylation | consumes | cytoplasmic proton (CHEBI:15378) | weak to moderate, review/genomic-inference-only | 10.3389/fmicb.2021.822229 | “proton consumption by amino acid decarboxylation (GAD and GDAR systems)” (gonzalezrosales2022integrativegenomicssheds pages 9-12) | Good candidate process edge; direct evidence in facultatively acidophilic taxa still needed. |
| urease | produces | ammonia (CHEBI:16134) | weak, review/genomic-inference-only | 10.3389/fmicb.2021.822229 | “urease-mediated ammonia production for pH buffering” (gonzalezrosales2022integrativegenomicssheds pages 9-12) | Candidate buffering mechanism; curate as uncertain unless species/assay support is found. |
| ammonia (CHEBI:16134) | contributes to | pH buffering | weak, review/genomic-inference-only | 10.3389/fmicb.2021.822229 | “urease-mediated ammonia production for pH buffering” (gonzalezrosales2022integrativegenomicssheds pages 9-12) | Process-level edge derived from review statement; no safe GO/CHEBI target for “pH buffering” beyond label-only node. |
| formic acid (CHEBI:30751) | causes | cytosolic acidification | strong, direct experiment but taxon-specific | 10.3389/fmicb.2021.651744 | “formic acid addition causes dose-dependent cytosolic acidification (pH 6.52 to 6.05 at 1 mM concentration)” (carere2021growthonformic pages 4-5) | Direct quantitative support in Methylacidiphilum sp. RTK17.1. |
| cytosolic acidification | inhibits | growth | strong, direct experiment but taxon-specific | 10.3389/fmicb.2021.651744 | “cannot grow on formic acid in batch culture due to cytosolic acidification and cell death” (carere2021growthonformic pages 1-2) | Strong phenotype link; taxon- and substrate-specific. |
| chloride (CHEBI:17996) | disrupts | inside-positive membrane potential | weak, genomic-inference/review | 10.3389/fmicb.2022.848410 | “chloride ions can disrupt reversed membrane potential, potentially inhibiting growth” (boase2022predictionandinferred pages 1-2) | Important inhibitor edge, but presented as hypothesis/genomic interpretation in Acidihalobacter context. |
| pH homeostasis | enables | growth in acidic environment (ENVO:00002009) | strong, direct experiment but taxon-specific | 10.3389/fmicb.2021.651744 | “stable growth on formic acid as the only source of energy was demonstrated… when cells are able to maintain pH homeostasis” (carere2021growthonformic pages 1-2) | Central trait-level edge; direct evidence that maintaining intracellular pH is necessary for acidic growth/acid-associated substrate use. |
| facultatively acidophilic growth phenotype (METPO:1003007) | associated with capacity for growth at | pH 4.2–7.2 | moderate, review/taxon-specific phenotype range | 10.3389/fmicb.2022.1034164 | “Mildly acidophilic Proteobacteria (pH 5.0–5.5 optima, ranges 4.2–7.2) like Methylocapsa acidiphila B2” (yao2023howmethanotrophsrespond pages 4-5) | Useful boundary-case phenotype support for acid-to-near-neutral growth, but from methanotroph review rather than mechanism study. |


*Table: This table summarizes candidate causal graph edges for METPO:1003007 with evidence strength, DOI, supporting snippets, and curation notes. It highlights which mechanisms are directly demonstrated versus only inferred from comparative genomics or reviews.*

### Recommended graph backbone

A conservative initial YAML graph could use this causal chain:

1. **acidic external pH → increases → inward proton pressure**;
2. **hopanoid-containing/low-permeability membrane → decreases → passive proton influx**;
3. **K⁺ uptake → contributes to → inside-positive membrane potential**;
4. **inside-positive membrane potential → inhibits → proton entry**;
5. **Nha-family antiport → contributes to → proton removal**;
6. **amino-acid decarboxylation → consumes → cytoplasmic protons**;
7. **urease-derived ammonia → increases → cytoplasmic buffering**;
8. **combined pH-homeostasis processes → maintain → circumneutral intracellular pH**;
9. **intracellular pH homeostasis → enables → growth below pH 5.5**;
10. **retention of viable bioenergetics near neutral pH → enables → near-neutral growth**;
11. **acidic optimum + near-neutral growth → realizes → `METPO:1003007`**.

Edges 2–7 should initially carry `uncertain`, `inferred`, or taxon-specific qualifiers. Comparative genomic studies identify hopanoid synthesis, K⁺ systems, Nha antiporters, decarboxylases, and urease as candidate acid-resistance mechanisms, but do not establish that every module is required for facultative acidophily. (boase2022predictionandinferred pages 1-2, gonzalezrosales2022integrativegenomicssheds pages 9-12, ji2021candidatuseremiobacterotaa pages 10-12)

## 5. Inhibitors and experimental modifiers

### Organic acids

Undissociated weak acids can cross the membrane and dissociate in the cytoplasm, acidifying it and dissipating proton motive force. In *Methylacidiphilum* sp. RTK17.1, 1 mM formic acid lowered intracellular pH from 6.52 to 6.05; batch addition prevented growth and caused cell death, whereas controlled chemostat growth was possible at dilution rate 0.0052 h⁻¹. This supports `formic acid → cytosolic acidification → growth inhibition`, but the concentration response and substrate context are taxon-specific. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 1-2)

The 2024 acidophilic-heterotroph review likewise treats organic acids as respiratory uncouplers and emphasizes that their degradation can be necessary for growth at very low pH. (gonzalez2024acidophilicheterotrophsbasic pages 1-2)

### Chloride

Chloride can compromise the electrical barrier, promote cytoplasmic acidification, and impose osmotic and oxidative stress. The retrieved Acidihalobacter analysis specifically presents disruption of reversed membrane potential as a proposed mechanism rather than a direct causal perturbation; therefore the edge should remain uncertain. (boase2022predictionandinferred pages 1-2)

### Assay covariates

A curatable phenotype record should include:

* complete tested pH series and buffer system;
* pH at inoculation and after growth;
* growth-rate or biomass endpoint, not survival alone;
* carbon and energy source, especially weak organic acids;
* chloride and total ionic strength;
* temperature and oxygen/electron-acceptor conditions;
* replicate number and criterion for detectable growth.

## 6. Recent developments and applications

### 2023–2024 research direction

Recent research has shifted toward comparative genomics, metagenome-resolved ecology, quantitative electrophysiology, and polyextremophile trade-offs. A 2023 review identifies the inside-positive potential, rigid low-permeability membranes, cytoplasmic buffering, and primary/secondary proton-removal systems as the principal defense layers. It also stresses that adaptations to low pH and low temperature can be synergistic or antagonistic, limiting simple transfer of mechanisms among taxa. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 1-2)

Environmental genomics provides useful candidate discovery but weaker phenotype evidence. In *Ca.* Eremiobacteria, 154 of 195 samples having >1% relative abundance were acidic, and genomic analyses predicted hopanoid synthesis, potassium uptake, Nha antiporters, and amino-acid decarboxylases. These are hypotheses suitable for prioritizing cultured validation, not proof of facultative acidophily. (ji2021candidatuseremiobacterotaa pages 10-12, ji2021candidatuseremiobacterotaa pages 7-9)

### Real-world applications

Acidophiles are already used or investigated in biomining, acid-mine-drainage remediation, acidic fermentation, microbial electrochemical systems, and methane mitigation. More than 80 heterotrophic acidophiles have reportedly been isolated. Their acidic cultivation conditions can reduce contamination, while iron-reducing acidophiles may complement oxidative bioleaching. (gonzalez2024acidophilicheterotrophsbasic pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 2-3)

Recent reported examples include:

* mixed acidophile cultures used to improve leaching of phosphate, pyrite and copper ores, and printed circuit boards;
* production of schwertmannite for removal of iron, sulfate, and arsenic from acidic waters;
* optimized polyhydroxybutyrate production of **19.75 g/L at pH 3.0**;
* electricity generation by *Acidiphilium cryptum* Lhet2 at pH ≤4, with maximum power density **12.6 mW/m²**, far below cited mesophilic systems at 5.61–7.72 W/m². (gonzalez2024acidophilicheterotrophsbasic pages 3-4)

Mildly acidophilic methanotrophs with ranges extending to pH 7.2 may act as methane sinks across heterogeneous acidic soils and peatlands, illustrating why broad-pH growth can be ecologically valuable. (yao2023howmethanotrophsrespond pages 4-5)

Authoritative reviews nevertheless emphasize that heterotrophic/mixotrophic acidophiles, low-temperature acidophiles, microbial electrochemical systems, and acidophile-derived extremozymes remain understudied. Scale-up, substrate cost, organic-acid inhibition, ionic stress, and limited genetic validation remain major constraints. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalez2024acidophilicheterotrophsbasic pages 6-7)

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate a universal facultative-acidophily mechanism from extreme acidophiles alone.** The strongest physiology retrieved comes from organisms optimal below pH 3 and establishes acid homeostasis, not near-neutral growth.
2. **Do not infer the trait from gene presence.** Kdp/Trk/Kch, Nha, decarboxylase, urease, or hopanoid genes are neither individually necessary nor sufficient for an acidic growth optimum plus near-neutral growth.
3. **Do not equate environmental occurrence with growth capacity.** Metagenomic abundance across pH values can reflect strain turnover, dormancy, transport, or community interactions.
4. **Keep hopanoid, spermidine, urease, ClcA, and individual antiporter edges uncertain** until knockout, inhibition, complementation, transport, or intracellular-pH experiments are available in a qualifying facultative acidophile.
5. **Do not curate DNA/protein repair as a core causal parent of this trait yet.** Repair responses are plausible downstream stress defenses, but the retrieved evidence does not connect them specifically to the acid-to-neutral growth phenotype.
6. **Do not curate sulfur oxidation, iron oxidation, methanotrophy, or heterotrophy as necessary mechanisms.** These are taxon-specific energy metabolisms and applications, not defining causes of facultative acidophily.
7. **Verify ontology identifiers before YAML insertion.** In particular, environmental-pH states, membrane-potential states, proton motive force, and organism-specific proteins need exact ontology resolution.
8. **Audit the supplied species DOI independently.** `10.1099/ijs.0.066175-0` supports a pH 4.0–7.2 growth range according to the provided evidence, but an acidic optimum must also be confirmed before using it as complete evidence for `METPO:1003007`.

## 8. DOI-first bibliography

1. González E. et al. **Acidophilic heterotrophs: basic aspects and technological applications.** *Frontiers in Microbiology*. Published May 2024. DOI: [10.3389/fmicb.2024.1374800](https://doi.org/10.3389/fmicb.2024.1374800). (gonzalez2024acidophilicheterotrophsbasic pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 3-4)
2. Terradot G. et al. **Escherichia coli Maintains pH via the Membrane Potential.** *PRX Life*. Published November 2024. DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015). Relevant as recent comparative bacterial electrophysiology, not direct trait evidence.
3. Dopson M. et al. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology*. Published March 2023. DOI: [10.3389/fmicb.2023.1149903](https://doi.org/10.3389/fmicb.2023.1149903). (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 1-2)
4. Yao X., Wang J., Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology*. Published January 2023. DOI: [10.3389/fmicb.2022.1034164](https://doi.org/10.3389/fmicb.2022.1034164). (yao2023howmethanotrophsrespond pages 4-5)
5. González-Rosales C. et al. **Integrative Genomics Sheds Light on Evolutionary Forces Shaping the Acidithiobacillia Class Acidophilic Lifestyle.** *Frontiers in Microbiology*. Published February 2022. DOI: [10.3389/fmicb.2021.822229](https://doi.org/10.3389/fmicb.2021.822229). (gonzalezrosales2022integrativegenomicssheds pages 1-2, gonzalezrosales2022integrativegenomicssheds pages 9-12)
6. Boase K. et al. **Prediction and Inferred Evolution of Acid Tolerance Genes in the Biotechnologically Important Acidihalobacter Genus.** *Frontiers in Microbiology*. Published April 2022. DOI: [10.3389/fmicb.2022.848410](https://doi.org/10.3389/fmicb.2022.848410). (boase2022predictionandinferred pages 1-2)
7. Ji M. et al. **Candidatus Eremiobacterota, a metabolically and phylogenetically diverse terrestrial phylum with acid-tolerant adaptations.** *ISME Journal* 15:2692–2707. Published March 2021. DOI: [10.1038/s41396-021-00944-8](https://doi.org/10.1038/s41396-021-00944-8). (ji2021candidatuseremiobacterotaa pages 10-12, ji2021candidatuseremiobacterotaa pages 7-9)
8. Carere C.R. et al. **Growth on Formic Acid Is Dependent on Intracellular pH Homeostasis for the Thermoacidophilic Methanotroph Methylacidiphilum sp. RTK17.1.** *Frontiers in Microbiology*. Published March 2021. DOI: [10.3389/fmicb.2021.651744](https://doi.org/10.3389/fmicb.2021.651744). (carere2021growthonformic pages 4-5, carere2021growthonformic pages 1-2)
9. Existing phenotype evidence supplied for this task. *International Journal of Systematic and Evolutionary Microbiology*. DOI: [10.1099/ijs.0.066175-0](https://doi.org/10.1099/ijs.0.066175-0). Reported growth range pH 4.0–7.2; acidic optimum should be checked in the full species description before final annotation.

References

1. (gonzalez2024acidophilicheterotrophsbasic pages 1-2): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.

2. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

3. (yao2023howmethanotrophsrespond pages 4-5): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

4. (ji2021candidatuseremiobacterotaa pages 7-9): Mukan Ji, Timothy J Williams, Kate Montgomery, Hon Lun Wong, Julian Zaugg, Jonathan F Berengut, Andrew Bissett, Maria Chuvochina, Philip Hugenholtz, and Belinda C Ferrari. Candidatus eremiobacterota, a metabolically and phylogenetically diverse terrestrial phylum with acid-tolerant adaptations. The ISME Journal, 15:2692-2707, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00944-8, doi:10.1038/s41396-021-00944-8. This article has 93 citations.

5. (gonzalezrosales2022integrativegenomicssheds pages 1-2): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

6. (gonzalezrosales2022integrativegenomicssheds pages 9-12): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

7. (carere2021growthonformic pages 4-5): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

8. (carere2021growthonformic pages 1-2): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

9. (ji2021candidatuseremiobacterotaa pages 10-12): Mukan Ji, Timothy J Williams, Kate Montgomery, Hon Lun Wong, Julian Zaugg, Jonathan F Berengut, Andrew Bissett, Maria Chuvochina, Philip Hugenholtz, and Belinda C Ferrari. Candidatus eremiobacterota, a metabolically and phylogenetically diverse terrestrial phylum with acid-tolerant adaptations. The ISME Journal, 15:2692-2707, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00944-8, doi:10.1038/s41396-021-00944-8. This article has 93 citations.

10. (boase2022predictionandinferred pages 1-2): Katelyn Boase, Carolina González, Eva Vergara, Gonzalo Neira, David Holmes, and Elizabeth Watkin. Prediction and inferred evolution of acid tolerance genes in the biotechnologically important acidihalobacter genus. Frontiers in Microbiology, Apr 2022. URL: https://doi.org/10.3389/fmicb.2022.848410, doi:10.3389/fmicb.2022.848410. This article has 22 citations and is from a peer-reviewed journal.

11. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

12. (gonzalez2024acidophilicheterotrophsbasic pages 2-3): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.

13. (gonzalez2024acidophilicheterotrophsbasic pages 3-4): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.

14. (gonzalez2024acidophilicheterotrophsbasic pages 6-7): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.