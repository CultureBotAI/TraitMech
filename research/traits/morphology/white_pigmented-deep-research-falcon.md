---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:24:37.978092'
end_time: '2026-06-18T10:41:00.755239'
duration_seconds: 982.78
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: white pigmented
  trait_identifier: METPO:1003029
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: white_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    white or nonpigmented because visible chromophore accumulation is absent or low.
  parent_traits: METPO:1003021
  synonyms: Pigment_white
  evidence_summary: 'DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus
    aureus (Supports white colony appearance as a microbial pigmentation phenotype
    tied to absent or inducible staphyloxanthin production in a representative bacterium.)'
  causal_graph_summary: 'white_pigmented_low_chromophore: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** white pigmented
- **METPO identifier:** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **white pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/white_pigmented.yaml`.

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
- **Trait label:** white pigmented
- **METPO identifier:** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **white pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/white_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **white pigmented** (METPO:1003029)

### Scope summary (trait definition + boundaries)
**Trait meaning.** *White pigmented* (METPO:1003029) is best operationalized as an **assay-observed morphology phenotype** in which microbial colonies/cells appear **white, colorless, or nonpigmented** due to **low/absent accumulation of visible chromophores** (e.g., carotenoids, melanin, phenazines, prodigiosin). This is consistent with bacterial examples where loss of carotenoid pigments yields unpigmented/white colonies (e.g., *Staphylococcus aureus* white variants after **sigB** inactivation) (alves2024experimentalevolutionof pages 13-15) and fungal examples where loss of melanin biosynthesis produces colonies with a “white surface” (zhong2024roleofdectin1 pages 1-2).

**Boundary cases and nearby traits.**
1. **White due to pigment loss vs. white due to opacity/precipitate/halo.** Some assays produce “white halos” or precipitates unrelated to pigment biosynthesis (e.g., zones of opaqueness), which should *not* be curated as METPO:1003029 unless the source explicitly ties the whiteness to chromophore absence (alves2024experimentalevolutionof pages 13-15).
2. **Inducible pigmentation vs. constitutive nonpigmented.** Some taxa exhibit nutrient- and time-dependent induction of pigment; “white” may reflect **culture conditions** rather than a stable genetic lesion (siems2023identificationofstaphyloxanthin pages 6-8).
3. **Taxon-specific pigment classes.** The same “white colony” phenotype can arise from distinct pigment systems (staphyloxanthin in *Staphylococcus*, prodigiosin in *Serratia*, DHN-melanin/carotenoids in fungi), implying the causal graph should include **pigment-specific submodules** that converge on the same terminal phenotype node (alves2024experimentalevolutionof pages 13-15, esteves2024serratiamarcescensatcc pages 1-2, erdmann2024thetetonsystem pages 1-2).

---

## 1) Key concepts and definitions (current understanding)

### 1.1. Pigment-dependent vs pigment-independent whiteness
In TraitMech terms, **white pigmented** should primarily capture **pigment-dependent whiteness** (low chromophore accumulation). Multiple systems show direct genetic causality between pigment pathway disruption and a white/nonpigmented phenotype:
- In *S. aureus*, white colonies are associated with disruptive **sigB** mutations, and SigB is stated to positively regulate genes involved in **staphyloxanthin** synthesis (alves2024experimentalevolutionof pages 13-15).
- In fungi, knockout of polyketide synthase genes in melanin biosynthesis reduces melanin and produces colonies with a “white surface” (zhong2024roleofdectin1 pages 1-2).

### 1.2. White as a convergent endpoint phenotype
The curatable abstraction is a **convergent phenotype**:
- Upstream: multiple pigments and pathways
- Downstream: visible “white/nonpigmented” colony or cell appearance
This suggests a causal graph architecture where **multiple pigment modules** (carotenoid, prodigiosin, melanin) converge on the terminal trait node METPO:1003029.

---

## 2) Candidate causal-graph nodes (grouped; ontology grounding where possible)

### A. Phenotype nodes
- **white pigmented** — METPO:1003029
- **pigment deficiency / nonpigmented colony phenotype** — (label-only; maps to METPO:1003029)

### B. Pigment/chromophore chemical nodes
- **staphyloxanthin** (carotenoid; label-only chemical; commonly treated as a carotenoid pigment in *Staphylococcus*) (alves2024experimentalevolutionof pages 13-15)
- **prodigiosin** (red pigment) (esteves2024serratiamarcescensatcc pages 1-2)
- **melanin** — CHEBI:25901 (zhong2024roleofdectin1 pages 1-2)
- **DHN melanin** (label-only; pathway-specific melanin class) (erdmann2024thetetonsystem pages 1-2)

### C. Pathway / biological process nodes
- **carotenoid biosynthetic process** — GO:0016117 (supported by SigB→staphyloxanthin synthesis statements) (alves2024experimentalevolutionof pages 13-15)
- **secondary metabolite biosynthetic process** — GO:0044550 (prodigiosin is a secondary metabolite; pig operon encodes biosynthesis) (esteves2024serratiamarcescensatcc pages 1-2)

### D. Genetic/protein regulator nodes
**Staphylococcus (carotenoid module):**
- **sigB** (alternative sigma factor; key regulator of pigment) (alves2024experimentalevolutionof pages 13-15)
- **rsbW** (anti-SigB factor; mutations modulate SigB activity) (alves2024experimentalevolutionof pages 9-13, alves2024experimentalevolutionof pages 13-15)
- **glmS** (direct upstream regulator of sigB in AGE response; knockout yields white colonies) (ni2024glmsplaysa pages 7-10, ni2024glmsplaysa pages 5-7)

**Staphylococcus capitis (carotenoid biosynthesis gene):**
- **crtN** (carotenoid biosynthesis gene; frameshift/premature stop in nonpigmented strain) (siems2023identificationofstaphyloxanthin pages 6-8)

**Serratia (prodigiosin module):**
- **pig operon (pigABCDEFGHIJKLMN)** (prodigiosin biosynthesis locus) (esteves2024serratiamarcescensatcc pages 1-2)
- **luxS** (regulatory locus affecting pigment output in ATCC 274 study) (esteves2024serratiamarcescensatcc pages 2-3)

**Fungi (melanin/carotenoid module):**
- **pksA** (polyketide synthase gene in *Fonsecaea*; knockout reduces melanin and yields white phenotype) (zhong2024roleofdectin1 pages 1-2)
- **pks1**, **phs1**, **phd1** (genes where combined mutations produce albino/white colonies in *Knufia petricola*) (erdmann2024thetetonsystem pages 1-2)

### E. Environmental/experimental factor nodes
- **advanced glycation end products (AGEs)** (host-associated chemical stressor; upregulates glmS and acts via GlmS to affect sigB and pigment) (ni2024glmsplaysa pages 7-10, ni2024glmsplaysa pages 5-7)
- **temperature (25 °C pigment-permissive for prodigiosin in Serratia ATCC 274)** — ENVO temperature term suggested (label-only if CURIE not available) (esteves2024serratiamarcescensatcc pages 2-3)
- **growth phase (stationary vs exponential)** (affects magnitude of prodigiosin induction by phage; also relevant to pigment production) (esteves2024serratiamarcescensatcc pages 2-3)
- **nutrient limitation / low nutrient conditions** — ENVO:00001998 (suggested) (pigmentation induction context in *S. capitis*) (siems2023identificationofstaphyloxanthin pages 6-8)

---

## 3) Evidence-backed candidate causal edges (triples)
The following table is designed for direct translation into `white_pigmented.yaml` edge assertions.

| Edge (triple) | Evidence snippet (short quote) | Organism/taxon | Assay/condition | Ontology grounding | Strength/notes | Reference (DOI + URL + year) | Citation ID |
|---|---|---|---|---|---|---|---|
| rsbW missense mutation `positively_regulates` SigB activity | “A mutation in rsbW increases SigB activity” | *Staphylococcus aureus* N315 lineage 3 | Experimental evolution in macrophages; orange SCV emergence | `gene:rsbW` ; `gene:sigB` ; GO:0006355 regulation of transcription, DNA-templated | Strong but taxon-specific; inferred from anti-SigB role and mutant phenotype | 10.1128/mbio.00346-24 · https://doi.org/10.1128/mbio.00346-24 · 2024 | (alves2024experimentalevolutionof pages 13-15) |
| SigB activity `positively_regulates` staphyloxanthin synthesis | “SigB positively regulates genes involved in staphyloxanthin synthesis” | *Staphylococcus aureus* | Same as above | `gene:sigB` ; `staphyloxanthin` ; GO:0016117 carotenoid biosynthetic process | Strong for *S. aureus*; direct statement | 10.1128/mbio.00346-24 · https://doi.org/10.1128/mbio.00346-24 · 2024 | (alves2024experimentalevolutionof pages 13-15) |
| sigB disruptive mutation `causes_decreased_accumulation_of` staphyloxanthin | “white colonies uniformly contained disruptive mutations in sigB” | *Staphylococcus aureus* | White revertant colonies from evolved lineage | `gene:sigB` ; `staphyloxanthin` ; METPO:1003029 white pigmented | Strong for this taxon/assay; mechanistic link via pigment loss | 10.1128/mbio.00346-24 · https://doi.org/10.1128/mbio.00346-24 · 2024 | (alves2024experimentalevolutionof pages 13-15) |
| decreased staphyloxanthin accumulation `causes` white colony phenotype | “conversion to unpigmented, normal-size colonies was associated with sigB inactivation” | *Staphylococcus aureus* | White large-colony revertants after SCV phase | `staphyloxanthin` ; METPO:1003029 | Strong within *S. aureus*; colony color is assay-observed morphology | 10.1128/mbio.00346-24 · https://doi.org/10.1128/mbio.00346-24 · 2024 | (alves2024experimentalevolutionof pages 13-15) |
| GlmS `positively_regulates` sigB transcription | “GlmS directly upregulates sigB transcription” | *Staphylococcus aureus* NCTC 8325 | Dual-luciferase and EMSA; ΔglmS mutant | `gene:glmS` ; `gene:sigB` ; GO:0006355 | Strong; direct promoter binding shown | 10.1080/21505594.2024.2352476 · https://doi.org/10.1080/21505594.2024.2352476 · 2024 | (ni2024glmsplaysa pages 7-10, ni2024glmsplaysa pages 5-7) |
| ΔglmS `causes_decreased_expression_of` sigB | “glmS knockout … significant reduction in sigB expression” | *Staphylococcus aureus* NCTC 8325 | Gene deletion strain under laboratory growth | `gene:glmS` ; `gene:sigB` | Strong; mutant phenotype | 10.1080/21505594.2024.2352476 · https://doi.org/10.1080/21505594.2024.2352476 · 2024 | (ni2024glmsplaysa pages 5-7, ni2024glmsplaysa pages 1-2) |
| ΔglmS `causes` pigment deficiency / white colony phenotype | “Knockout of glmS … causes loss of the typical golden colony pigment (colony turns white)” | *Staphylococcus aureus* NCTC 8325 | Colony morphology comparison WT vs ΔglmS | `gene:glmS` ; METPO:1003029 | Strong; direct morphology evidence | 10.1080/21505594.2024.2352476 · https://doi.org/10.1080/21505594.2024.2352476 · 2024 | (ni2024glmsplaysa pages 5-7, ni2024glmsplaysa media 6fd318fc) |
| AGEs `positively_regulate` glmS expression | “AGEs significantly upregulate glmS mRNA (average 2−∆∆CT ≈ 3.28-fold)” | *Staphylococcus aureus* NCTC 8325 | AGE stimulation | `advanced glycation end products` ; `gene:glmS` | Strong in this assay; environmental/host chemical factor | 10.1080/21505594.2024.2352476 · https://doi.org/10.1080/21505594.2024.2352476 · 2024 | (ni2024glmsplaysa pages 5-7) |
| AGEs `positively_regulate` sigB via GlmS | “AGEs failed to upregulate sigB … in the glmS knockout, indicating that AGEs act via GlmS” | *Staphylococcus aureus* NCTC 8325 | AGE stimulation of WT and ΔglmS | `advanced glycation end products` ; `gene:glmS` ; `gene:sigB` | Strong in this system; indirect edge mediated by GlmS | 10.1080/21505594.2024.2352476 · https://doi.org/10.1080/21505594.2024.2352476 · 2024 | (ni2024glmsplaysa pages 7-10, ni2024glmsplaysa pages 1-2) |
| crtN frameshift / premature stop `causes_decreased_function_of` carotenoid biosynthesis | “crtN is split into two predicted ORFs due to a frameshift and premature stop codon” | *Staphylococcus capitis* subsp. *capitis* strain D2T | Comparative genomics of pigmented vs non-pigmented strains | `gene:crtN` ; GO:0016117 carotenoid biosynthetic process | Moderate; based on wild-type comparative genomics, not knockout | 10.3389/fmicb.2023.1272734 · https://doi.org/10.3389/fmicb.2023.1272734 · 2023 | (siems2023identificationofstaphyloxanthin pages 6-8) |
| reduced carotenoid biosynthesis `causes` non-pigmented/white phenotype | “the non-pigmented strains remained colorless regardless of the type of medium” | *Staphylococcus capitis* subsp. *capitis* | Growth on multiple media; Raman and HPLC-MS | `staphyloxanthin` ; METPO:1003029 | Moderate; phenotype is clear but causality to crtN is inferred | 10.3389/fmicb.2023.1272734 · https://doi.org/10.3389/fmicb.2023.1272734 · 2023 | (siems2023identificationofstaphyloxanthin pages 6-8) |
| low-nutrient conditions / longer incubation `positively_regulate` staphyloxanthin accumulation | “intensity of pigmentation … increased under low nutrient conditions and with longer incubation times” | *Staphylococcus capitis* subsp. *capitis* | Low-nutrient R2A versus richer media; longer incubation | ENVO:00001998 nutrient limitation ; `staphyloxanthin` | Moderate; environmental modulation of color, not directly white phenotype | 10.3389/fmicb.2023.1272734 · https://doi.org/10.3389/fmicb.2023.1272734 · 2023 | (siems2023identificationofstaphyloxanthin pages 6-8) |
| pig operon transcription `positively_regulates` prodigiosin biosynthesis | “pig operon (pigABCDEFGHIJKLMN)” and “threefold increase in transcription of the pig operon” | *Serratia marcescens* ATCC 274 | Phage χ-induced lysate; promoter assays | `pig operon` ; `prodigiosin` ; GO:0044550 secondary metabolite biosynthetic process | Strong for *Serratia*; direct transcriptional evidence | 10.1038/s41598-024-68747-3 · https://doi.org/10.1038/s41598-024-68747-3 · 2024 | (esteves2024serratiamarcescensatcc pages 1-2) |
| prodigiosin biosynthesis `causes` red pigmentation; loss implies white/non-pigmented colonies | “prodigiosin is the red pigment of Serratia marcescens” | *Serratia marcescens* | General pigment phenotype | `prodigiosin` ; METPO:1003029 | Moderate for white phenotype: red pigment identity is direct, white state is inferred from non-pigmented strains | 10.1038/s41598-024-68747-3 · https://doi.org/10.1038/s41598-024-68747-3 · 2024 | (esteves2024serratiamarcescensatcc pages 1-2) |
| low temperature (<30°C) and post-exponential growth `positively_regulate` prodigiosin production | “prodigiosin pigment, is reported at low temperatures (< 30°C), at post-exponential growth” | *Serratia marcescens* | Environmental regulation of secondary metabolites | ENVO:00000484 temperature ; `prodigiosin` | Moderate; review-like statement within primary paper | 10.33073/pjm-2024-002 · https://doi.org/10.33073/pjm-2024-002 · 2024 | (andamora2024increasedproteolyticactivity pages 1-2) |
| pigment-permissive temperature 25°C `positively_regulates` prodigiosin accumulation | “pigment-permissive temperature of 25 °C” | *Serratia marcescens* ATCC 274 | Overnight incubation at 25°C; A535 quantification | ENVO:00000484 ; `prodigiosin` | Strong for assay condition; taxon/strain specific | 10.1038/s41598-024-68747-3 · https://doi.org/10.1038/s41598-024-68747-3 · 2024 | (esteves2024serratiamarcescensatcc pages 2-3, esteves2024serratiamarcescensatcc pages 9-10) |
| χ phage infection / induced lysate `positively_regulates` pig operon transcription | “χ-induced S. marcescens cell lysate … causes a threefold increase in transcription of the pig operon” | *Serratia marcescens* ATCC 274 | Phage infection or lysate exposure | `bacteriophage χ` ; `pig operon` | Strong but niche-specific; not a general white-pigment mechanism | 10.1038/s41598-024-68747-3 · https://doi.org/10.1038/s41598-024-68747-3 · 2024 | (esteves2024serratiamarcescensatcc pages 1-2) |
| active χ phage infection `positively_regulates` prodigiosin accumulation | “a greater than fivefold overproduction of prodigiosin” | *Serratia marcescens* ATCC 274 | Phage infection under pigment-permissive conditions | `bacteriophage χ` ; `prodigiosin` | Strong but highly assay-specific | 10.1038/s41598-024-68747-3 · https://doi.org/10.1038/s41598-024-68747-3 · 2024 | (esteves2024serratiamarcescensatcc pages 1-2) |
| pksA knockout `causes_decreased_accumulation_of` melanin | “knocking out pksA reduced melanin production” | *Fonsecaea monophora* | Agrobacterium-mediated transformation; Mel− mutant | `gene:pksA` ; CHEBI:25901 melanin | Strong for this fungus | 10.1080/21501203.2023.2249010 · https://doi.org/10.1080/21501203.2023.2249010 · 2024 | (zhong2024roleofdectin1 pages 1-2) |
| reduced melanin accumulation `causes` white colony surface / white conidia | “Mel- colonies are uneven with a white surface … and white conidia” | *Fonsecaea monophora* | Comparison of Mel+ vs Mel− colonies | CHEBI:25901 melanin ; METPO:1003029 | Strong; direct phenotype description | 10.1080/21501203.2023.2249010 · https://doi.org/10.1080/21501203.2023.2249010 · 2024 | (zhong2024roleofdectin1 pages 1-2) |
| pks1 mutation `causes_decreased_accumulation_of` DHN melanin | “mutation of pks1 abolishes melanization” | *Knufia petricola* | CRISPR/Cas9 pigment-gene targeting | `gene:pks1` ; `DHN melanin` | Strong for melanin branch | 10.1007/s00792-024-01354-2 · https://doi.org/10.1007/s00792-024-01354-2 · 2024 | (erdmann2024thetetonsystem pages 1-2) |
| combined pks1 + phs1/phd1 mutation `causes` albino/white colonies | “combined mutation of pks1 and phs1 or phd1 produces albino (white) colonies” | *Knufia petricola* | CRISPR/Cas9 double mutants | `gene:pks1` ; `gene:phs1` ; `gene:phd1` ; METPO:1003029 | Strong; direct white phenotype, but taxon-specific | 10.1007/s00792-024-01354-2 · https://doi.org/10.1007/s00792-024-01354-2 · 2024 | (erdmann2024thetetonsystem pages 1-2) |


*Table: This table lists candidate causal edges for the microbial trait 'white pigmented' using only the provided evidence contexts. It highlights mechanisms where reduced chromophore biosynthesis or regulation leads to white/nonpigmented colony phenotypes across bacteria and fungi.*

**Note on interpreting Serratia edges.** The provided Serratia papers strongly support *pig operon → prodigiosin → increased red pigmentation* and environmental modulation, but do not directly quote “creamy white colonies” when prodigiosin is absent; that final “loss of red pigment implies nonpigmented/white appearance” step should be marked **inferred/uncertain** unless a source explicitly states colony appearance in the same experiment (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 5-7).

---

## 4) Recent developments (prioritizing 2023–2024)

### 4.1. *Staphylococcus aureus*: white variants as outcomes of regulatory evolution in host-like environments (2024)
An experimental evolution study in macrophages identified a hyper-pigmented SCV state driven by **rsbW** mutation (increasing SigB activity) that was unstable in nutrient-replete conditions and could revert via **sigB deletions**, yielding **nonpigmented/white colonies** (alves2024experimentalevolutionof pages 13-15). This provides a contemporary, mechanistically grounded example of **regulatory switching** between pigmented and white states in a clinically relevant pathogen.

### 4.2. Host chemical microenvironment: AGEs → GlmS → sigB as a pigment-control axis (2024)
Ni et al. (2024) identified **GlmS** as a direct regulator that binds and upregulates **sigB**, and showed that a **ΔglmS** mutant exhibits **pigment deficiency with white colonies**; they also quantified that AGEs upregulate glmS (~3.28-fold) (ni2024glmsplaysa pages 5-7, ni2024glmsplaysa pages 7-10). This provides a mechanistic link between a **host-associated factor** and the microbial pigmentation state.

### 4.3. *Staphylococcus capitis*: comparative genomics linking crtN lesions to nonpigmented phenotypes (2023)
Siems et al. (2023) report nonpigmented strains that remain colorless across media and identify a frameshift/premature stop in **crtN** as a plausible mechanism for impaired carotenoid biosynthesis; they also show pigment induction by low nutrient conditions and longer incubation (siems2023identificationofstaphyloxanthin pages 6-8). This highlights that “white” can reflect **both genetics and culture-dependent induction thresholds**, relevant for assay interpretation.

### 4.4. *Serratia marcescens*: promoter-level pig operon control and stress-responsive prodigiosin modulation (2024)
Esteves & Scharf (2024) show the **pig operon** is co-transcribed and that pigment increases can be induced (>5-fold) by phage χ infection, mediated by promoter-level regulation (Ppig) and modulated by growth phase and temperature (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 2-3). Although not “white phenotype” per se, this provides robust causal structure for the **prodigiosin module**, whose absence would yield a non-red, nonpigmented colony phenotype.

### 4.5. Fungal genetics toolkits using albino/white mutants as selectable reporters (2024)
Erdmann et al. (2024) describe how mutation of **pks1** and combined mutation of **pks1** with **phs1**/**phd1** yields **albino (white) colonies** in the rock-inhabiting fungus *Knufia petricola*, supporting pigment-pathway nodes and demonstrating real-world use of white phenotypes as genetic markers (erdmann2024thetetonsystem pages 1-2).

---

## 5) Current applications and real-world implementations

### 5.1. Clinical microbiology phenotyping and within-host adaptation
The *S. aureus* evidence indicates that **pigment loss (white colonies)** can arise through specific regulatory gene disruptions (sigB lesions), and that these variants can differ in survival phenotypes; this supports the practical importance of observing colony color when screening isolates and interpreting within-host adaptation (alves2024experimentalevolutionof pages 13-15).

### 5.2. Genetic engineering and strain construction
White/albino colonies are used as **visual reporters** for successful genome edits or expression platform construction in fungi (e.g., using pigment biosynthesis loci as selectable markers) (erdmann2024thetetonsystem pages 1-2).

### 5.3. Industrial microbiology and pigment bioprocessing (inverse relevance)
While this trait focuses on *absence* of pigment, several 2024 sources emphasize optimizing pigment production (prodigiosin). These studies provide mechanistic levers (temperature, promoter control, growth phase) that can be reversed or disrupted to intentionally generate nonpigmented/white phenotypes when needed for specific applications (e.g., reduced metabolite background) (esteves2024serratiamarcescensatcc pages 9-10, esteves2024serratiamarcescensatcc pages 2-3).

---

## 6) Expert opinions / authoritative analysis (from sources)
- The *S. aureus* study explicitly frames SigB as a positive regulator of staphyloxanthin synthesis and links loss-of-function sigB mutations to unpigmented/white revertants, supporting SigB-centered regulatory models of pigment control (alves2024experimentalevolutionof pages 13-15).
- The *S. capitis* study emphasizes that pigmentation may be **stress- or nutrient-dependent**, warning against treating colony color as purely genetic without considering culture conditions (siems2023identificationofstaphyloxanthin pages 6-8).
- The *Serratia* study emphasizes that prodigiosin regulation is complex and influenced by multiple environmental/physiological factors, reinforcing that pigment presence/absence may be strongly context-dependent (esteves2024serratiamarcescensatcc pages 1-2).

---

## 7) Relevant statistics and quantitative data (recent studies)
- **Prevalence of sigB length changes in public *S. aureus* genomes.** 134 of 45,887 genomes (~0.29%) had sigB length changes flagged; among these, 103 were truncated by frameshifts and 13 had deletions (11–498 bp) (alves2024experimentalevolutionof pages 13-15).
- **Serratia prodigiosin induction.** Phage χ exposure stimulated “greater than fivefold” prodigiosin overproduction, and χ-induced lysate caused a threefold increase in pig operon transcription (esteves2024serratiamarcescensatcc pages 1-2).
- **S. aureus AGEs–GlmS response.** AGEs increased glmS mRNA by ~3.28-fold (qRT-PCR) (ni2024glmsplaysa pages 5-7).
- **Prodigiosin production yield and bioassay (Serratia Se9).** Optimized yield 83.4±1.7 mg/L after 96 h at 30 °C with methanol extraction; 1000 ppm caused 40% mortality and doubling caused 91% mortality; LC50 1192 ppm (koc2024prodigiosinapromising pages 1-3).

---

## 8) Warnings / curation caveats (do not curate yet)
1. **Avoid curating “white halos/opaqueness zones”** as white-pigmented unless explicitly tied to pigment/chromophore absence; some white visual features are precipitation/lysis artifacts (alves2024experimentalevolutionof pages 13-15).
2. **Serratia ‘white colony’ inference is incomplete** in the retrieved excerpts. While prodigiosin is confirmed as the red pigment and the pig operon controls it, direct statements connecting prodigiosin loss to “white colonies” are not present in the evidence snippets; mark the terminal step “loss of prodigiosin → white colony” as **inferred** until a source explicitly describes colony appearance (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 5-7).
3. **S. capitis crtN causality is comparative-genomics-based.** Frameshift in crtN is a strong candidate mechanism but remains **non-knockout** evidence; curate as “putative” or “uncertain” unless a functional validation paper is added (siems2023identificationofstaphyloxanthin pages 6-8).

---

## 9) Key visual evidence (retrieved figure panels)
- Ni et al. (2024) includes a figure panel showing the **ΔglmS mutant colony color switching to white** vs wild-type golden colonies, directly supporting METPO:1003029 for *S. aureus* pigment deficiency (ni2024glmsplaysa media 6fd318fc).
- The same paper includes dual-luciferase and EMSA panels supporting **GlmS binding/activation of the sigB promoter**, supporting mechanistic edges upstream of pigment deficiency (ni2024glmsplaysa media 896fc7a0, ni2024glmsplaysa media ebb659dc).

---

## DOI-first bibliography (with URLs and publication dates)
1. **Alves J, et al.** Experimental evolution of *Staphylococcus aureus* in macrophages… *mBio* (published Jun 2024). DOI: **10.1128/mbio.00346-24**. URL: https://doi.org/10.1128/mbio.00346-24 (alves2024experimentalevolutionof pages 13-15)
2. **Ni L, et al.** GlmS plays a key role… promoted by advanced glycation end products. *Virulence* (published May 2024). DOI: **10.1080/21505594.2024.2352476**. URL: https://doi.org/10.1080/21505594.2024.2352476 (ni2024glmsplaysa pages 7-10, ni2024glmsplaysa pages 5-7, ni2024glmsplaysa media 6fd318fc)
3. **Siems K, et al.** Identification of staphyloxanthin and derivates in yellow-pigmented *Staphylococcus capitis*… *Frontiers in Microbiology* (published Sep 2023). DOI: **10.3389/fmicb.2023.1272734**. URL: https://doi.org/10.3389/fmicb.2023.1272734 (siems2023identificationofstaphyloxanthin pages 6-8)
4. **Esteves NC, Scharf BE.** *Serratia marcescens* ATCC 274 increases prodigiosin… *Scientific Reports* (published Jul 2024). DOI: **10.1038/s41598-024-68747-3**. URL: https://doi.org/10.1038/s41598-024-68747-3 (esteves2024serratiamarcescensatcc pages 1-2)
5. **De Anda-Mora KL, et al.** Increased proteolytic activity… *Polish Journal of Microbiology* (published Mar 2024). DOI: **10.33073/pjm-2024-002**. URL: https://doi.org/10.33073/pjm-2024-002 (andamora2024increasedproteolyticactivity pages 1-2)
6. **Zhong J, et al.** Role of Dectin-1… melanin-deficient mutant. *Mycology* (published online Sep 2024; DOI year 2023, article year 2024). DOI: **10.1080/21501203.2023.2249010**. URL: https://doi.org/10.1080/21501203.2023.2249010 (zhong2024roleofdectin1 pages 1-2)
7. **Erdmann EA, et al.** The Tet-on system… *Extremophiles* (published Aug 2024). DOI: **10.1007/s00792-024-01354-2**. URL: https://doi.org/10.1007/s00792-024-01354-2 (erdmann2024thetetonsystem pages 1-2)

---

## Suggested minimal YAML-ready causal-graph skeleton (high-confidence core)
1. `AGEs` → `glmS` → `sigB` → `staphyloxanthin` → `white pigmented` (with directionality: decreased staphyloxanthin increases whiteness), noting that ΔglmS yields white colonies and reduces sigB (ni2024glmsplaysa pages 5-7, ni2024glmsplaysa pages 7-10, ni2024glmsplaysa media 6fd318fc).
2. `rsbW (anti-sigma)` → `sigB` → `staphyloxanthin` → colony color; `sigB loss-of-function` → `white pigmented` (alves2024experimentalevolutionof pages 13-15, alves2024experimentalevolutionof pages 9-13).
3. `pksA/pks1` → `melanin` → `white pigmented` (zhong2024roleofdectin1 pages 1-2, erdmann2024thetetonsystem pages 1-2).

(Additional modules for `pig operon → prodigiosin` and `crtN → carotenoids` are well-supported upstream, but the final mapping to an explicit “white colony” endpoint should be curated as inferred/uncertain with current evidence.) (esteves2024serratiamarcescensatcc pages 1-2, siems2023identificationofstaphyloxanthin pages 6-8)


References

1. (alves2024experimentalevolutionof pages 13-15): Joana Alves, Manouk Vrieling, Natalie Ring, Gonzalo Yebra, Amy Pickering, Tomasz K. Prajsnar, Stephen A. Renshaw, and J. Ross Fitzgerald. Experimental evolution of <i>staphylococcus aureus</i> in macrophages: dissection of a conditional adaptive trait promoting intracellular survival. Jun 2024. URL: https://doi.org/10.1128/mbio.00346-24, doi:10.1128/mbio.00346-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

2. (zhong2024roleofdectin1 pages 1-2): Jiaojiao Zhong, Jing Zhang, Jianchi Ma, Wen-ying Cai, Xi-qing Li, and Junmin Zhang. Role of dectin-1 in immune response of macrophages induced by fonsecaea monophora wild strain and melanin-deficient mutant strain. Mycology, 15:45-56, Sep 2024. URL: https://doi.org/10.1080/21501203.2023.2249010, doi:10.1080/21501203.2023.2249010. This article has 5 citations.

3. (siems2023identificationofstaphyloxanthin pages 6-8): Katharina Siems, Katharina Runzheimer, Katarina Rebrosova, Lara Etzbach, Alina Auerhammer, Anna Rehm, Oliver Schwengers, Martin Šiler, Ota Samek, Filip Růžička, and Ralf Moeller. Identification of staphyloxanthin and derivates in yellow-pigmented staphylococcus capitis subsp. capitis. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1272734, doi:10.3389/fmicb.2023.1272734. This article has 11 citations and is from a peer-reviewed journal.

4. (esteves2024serratiamarcescensatcc pages 1-2): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

5. (erdmann2024thetetonsystem pages 1-2): Eileen A. Erdmann, Antonia K. M. Brandhorst, Anna A. Gorbushina, and Julia Schumacher. The tet-on system for controllable gene expression in the rock-inhabiting black fungus knufia petricola. Extremophiles, Aug 2024. URL: https://doi.org/10.1007/s00792-024-01354-2, doi:10.1007/s00792-024-01354-2. This article has 10 citations and is from a peer-reviewed journal.

6. (alves2024experimentalevolutionof pages 9-13): Joana Alves, Manouk Vrieling, Natalie Ring, Gonzalo Yebra, Amy Pickering, Tomasz K. Prajsnar, Stephen A. Renshaw, and J. Ross Fitzgerald. Experimental evolution of <i>staphylococcus aureus</i> in macrophages: dissection of a conditional adaptive trait promoting intracellular survival. Jun 2024. URL: https://doi.org/10.1128/mbio.00346-24, doi:10.1128/mbio.00346-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

7. (ni2024glmsplaysa pages 7-10): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.

8. (ni2024glmsplaysa pages 5-7): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.

9. (esteves2024serratiamarcescensatcc pages 2-3): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

10. (ni2024glmsplaysa pages 1-2): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.

11. (ni2024glmsplaysa media 6fd318fc): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.

12. (andamora2024increasedproteolyticactivity pages 1-2): Karla L. De Anda-Mora, Faviola Tavares-Carreón, Carlos Alvarez, Samantha Barahona, Miguel A. Becerril-García, Rogelio J. Treviño-Rangel, Rodolfo García-Contreras, and Angel Andrade. Increased proteolytic activity of serratia marcescens clinical isolate hu1848 is associated with higher eepr expression. Polish Journal of Microbiology, 73:11-20, Mar 2024. URL: https://doi.org/10.33073/pjm-2024-002, doi:10.33073/pjm-2024-002. This article has 3 citations and is from a peer-reviewed journal.

13. (esteves2024serratiamarcescensatcc pages 9-10): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

14. (esteves2024serratiamarcescensatcc pages 5-7): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

15. (koc2024prodigiosinapromising pages 1-3): Muhammed Koç, Duygu Bekircan Eski, Ismail Demir, and Ardahan Eski. Prodigiosin, a promising biocontrol agent against thaumetopoea wilkinsoni (tams, 1926) (lepidoptera: notodontidae). Turkish Journal of Entomology, 48:343-352, Oct 2024. URL: https://doi.org/10.16970/entoted.1517520, doi:10.16970/entoted.1517520. This article has 1 citations.

16. (ni2024glmsplaysa media 896fc7a0): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.

17. (ni2024glmsplaysa media ebb659dc): Lijia Ni, Rui Shen, Hua Luo, Xuexue Li, Xiaofan Zhang, Lisi Huang, Yawen Deng, Xiaoyan Liao, Yonglin Wu, Chaohui Duan, and Xiaoying Xie. Glms plays a key role in the virulence factor expression and biofilm formation ability of staphylococcus aureus promoted by advanced glycation end products. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2352476, doi:10.1080/21505594.2024.2352476. This article has 9 citations and is from a peer-reviewed journal.