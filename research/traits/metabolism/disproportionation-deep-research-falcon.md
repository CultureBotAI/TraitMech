---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:50:07.162040'
end_time: '2026-08-04T06:09:07.872564'
duration_seconds: 1140.71
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Disproportionation
  trait_identifier: METPO:1000806
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: disproportionation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which a single substrate simultaneously undergoes both
    oxidation and reduction reactions, with part of the substrate serving as the electron
    donor and another part serving as the electron acceptor.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1080/17415990802105770: serve as both electron donor and
    acceptor (Review supports inorganic sulfur disproportionation as one substrate
    serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental
    sulfur disproportionation (Study supports elemental sulfur disproportionation
    in acidophilic microbial metabolism.)'
  causal_graph_summary: 'sulfur_disproportionation_redox_split: 14 nodes, 15 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Disproportionation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 14 nodes, 15 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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
- **Trait label:** Disproportionation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 14 nodes, 15 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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


# Curation-focused research report: microbial disproportionation

## Executive summary

**Target trait:** **Disproportionation**  
**Trait identifier:** **METPO:1000806**  
**Category / kind / status:** METABOLISM / CLASS / REVIEWED  
**Parent:** **METPO:1000060**

The trait should represent a microbial metabolic capacity in which **one intermediate-oxidation-state substrate supplies both the oxidized and reduced product branches**. For the evidence currently available, the best-resolved microbial instance is inorganic sulfur disproportionation: elemental sulfur, thiosulfate, sulfite, or tetrathionate is converted into more oxidized sulfur—usually sulfate—and more reduced sulfur—usually sulfide. It is often termed “inorganic fermentation,” although that phrase is an analogy rather than a mechanistic ontology definition. In canonical anaerobic growth, no external electron donor or terminal acceptor is required for the redox split itself. Sulfide removal can nevertheless be essential to the thermodynamics of elemental-sulfur disproportionation. (thamdrup1993bacterialdisproportionationof pages 1-2, finster2013completegenomesequence pages 1-2)

The strongest graph should contain **substrate-specific reaction modules**, not one universal enzyme pathway. Desulfobulbaceae-like organisms support a model involving Sat–AprAB in an oxidative branch and DsrAB/DsrC in a reductive branch. Conversely, 2023 experiments showed that *Sulfurimonas* and *Sulfurovum* disproportionate sulfur despite lacking `aprAB`, `dsrAB`, `dsrC`, `dsrMKJOP`, and `qmoABC`, demonstrating at least one unresolved alternative mechanism. (wang2023disproportionationofinorganic pages 1-2, hashimoto2022physiologicalandcomparative pages 12-13, hashimoto2022physiologicalandcomparative pages 7-9)

## 1. Trait scope and diagnostic phenotype

### 1.1 Recommended operational definition

Curate **METPO:1000806** when all of the following are demonstrated or explicitly asserted by a reliable source:

1. The same named substrate pool is partitioned into products at both higher and lower oxidation states.
2. Both product branches are measured or otherwise directly supported.
3. The reaction is biologically catalyzed.
4. For a physiological trait assertion, growth, energy conservation, repeated transfer, or substrate-dependent activity is shown.
5. Alternative explanations—ordinary oxidation using oxygen/nitrate, ordinary sulfur reduction using an added donor, and abiotic product formation—are excluded or separately modeled.

A high-confidence sulfur assay therefore measures substrate depletion, sulfate and sulfide formation, and cell growth under anoxic conditions. The 2023 Campylobacterota study used direct cell counts, methylene-blue sulfide assays, ion chromatography for thiosulfate/sulfate, and ferrozine measurements of iron reduction. (wang2023disproportionationofinorganic pages 15-17)

### 1.2 Core reactions

Canonical net reactions supported by culture experiments include:

- **Elemental sulfur:** `4 S0 + 4 H2O → SO4^2− + 3 H2S + 2 H+`.
- **Thiosulfate:** `S2O3^2− + H2O → SO4^2− + HS− + H+`.
- With ferrihydrite as sulfide sink, the observed elemental-sulfur net reaction can be written `3 S0 + 2 Fe(OH)3 → SO4^2− + 2 FeS + 2 H+ + 2 H2O`. (wang2023disproportionationofinorganic pages 9-12, thamdrup1993bacterialdisproportionationof pages 1-2, canfield1998isotopefractionationand pages 7-8)

Thiosulfate and sulfite disproportionation were reported as exergonic under standard conditions, approximately −21.9/−22.3 and −58.9 kJ mol−1 substrate, respectively. Elemental-sulfur disproportionation is unfavorable or nearly neutral under standard conditions but becomes favorable when free sulfide is maintained at low concentration; one analysis estimated approximately −30 kJ mol−1 S0 at `H2S = 10−7 M` and sulfate `2.8 × 10−2 M`. (wang2023disproportionationofinorganic pages 1-2, finster2013completegenomesequence pages 1-2)

### 1.3 Boundaries and nearby traits

- **Not ordinary sulfur oxidation:** oxidation of sulfide, sulfur, or thiosulfate with O2 or nitrate as the external electron acceptor does not satisfy the same-substrate redox split.
- **Not sulfur reduction:** reduction of S0, sulfite, or thiosulfate using H2 or organic carbon as the electron donor is a separate respiratory process.
- **Not comproportionation:** combining sulfur species at different oxidation states to produce an intermediate is the reverse conceptual pattern.
- **SOR is a boundary case:** sulfur oxygenase reductase catalyzes coupled oxidation and reduction of S0, but its reported reaction consumes molecular oxygen. It should be represented as **oxygen-dependent SOR-catalyzed sulfur oxygenation/reduction**, not automatically equated with canonical anaerobic, energy-conserving disproportionation. (guo2016sulfurmetabolismpathways pages 7-8)
- **TetH/TTH is a boundary case:** acidophilic tetrathionate hydrolase converts tetrathionate into thiosulfate, elemental sulfur, sulfate, and related polythionates in the S4-intermediate sulfur-oxidation pathway. This is enzyme-catalyzed bond hydrolysis within sulfur oxidation metabolism; evidence of TetH activity alone is insufficient to assign the physiological trait METPO:1000806. (kanao2024tetrathionatehydrolasefrom pages 1-2, kanao2024tetrathionatehydrolasefrom pages 3-4)
- **Metagenomic prediction alone is insufficient:** `dsr`, `apr`, `sor`, `phs`, `psr`, `ttr`, or `tetH` genes are neither individually necessary nor sufficient for the trait.

## 2. Candidate nodes grouped by type

### Trait and process nodes

- Disproportionation — **METPO:1000806**
- Parent trait — **METPO:1000060**
- Inorganic sulfur disproportionation
- Elemental-sulfur disproportionation
- Thiosulfate disproportionation
- Sulfite disproportionation
- Tetrathionate disproportionation
- Oxidative branch of sulfur disproportionation
- Reductive branch of sulfur disproportionation
- Chemolithoautotrophic growth
- CO2 fixation / Wood–Ljungdahl pathway
- Sulfide scavenging and iron-sulfide precipitation

### Chemicals and environmental factors

High-confidence labels suitable for subsequent identifier verification include elemental sulfur, thiosulfate, sulfite, tetrathionate, sulfate, hydrogen sulfide/bisulfide, carbon dioxide/bicarbonate, ferrihydrite or amorphous Fe(III) hydroxide, FeS, pyrite, manganese dioxide, water, and proton.

Use ChEBI identifiers only after checking protonation and charge conventions against the intended reaction database. Suggested high-confidence starting points are **CHEBI:15377** for water, **CHEBI:15378** for hydron, **CHEBI:16526** for carbon dioxide, **CHEBI:16189** for sulfate, **CHEBI:17359** for sulfur, and **CHEBI:18422** for hydrogen sulfide. Thiosulfate, sulfite, tetrathionate, ferrihydrite, FeS, and MnO2 should be curator-verified before insertion because database entries can distinguish acid, conjugate-base, mineral, and generic material forms.

Environmental/experimental nodes include anoxic condition, low free-sulfide activity, sulfide sink, hydrothermal vent/plume, marine sediment, suboxic sediment, ferrihydrite amendment, dialysis membrane separation, temperature, pH, and salinity. In GF1T, growth occurred at 25–50°C, pH 6.1–6.8, and 2–4% NaCl; these are strain-specific ranges, not trait-level requirements. (hashimoto2022physiologicalandcomparative pages 12-13, hashimoto2022physiologicalandcomparative pages 6-7)

### Genes, proteins, complexes, and modules

- `sat` / sulfate adenylyltransferase
- `aprAB` / APS reductase
- `qmoABC` / APS-reductase-associated electron-transfer complex
- `dsrAB` / dissimilatory sulfite reductase
- `dsrC`, `dsrD`, and `dsrMKJOP`
- Tetrathionate-reductase-like `ttrBCA` complex
- Thiosulfate-reductase-like `phsAB`
- YTD cluster: YedE, TusA, DsrE-like and conserved hypothetical proteins
- Rhodanese-like sulfurtransferase
- Molybdopterin oxidoreductases
- Sulfur oxidation/reduction candidates in Campylobacterota: `soxABCDXYZ`, `sqr`, `sdo`, `sorAB`, `psrABC`, `phsAB`, and `fsr`
- Wood–Ljungdahl CO2-fixation module
- Nitrogen-fixation module (`nif` genes), as an accessory phenotype in some taxa

Exact GO, EC, UniProt, Rhea, KEGG, and MetaCyc identifiers should be assigned only after selecting the intended directional reaction and taxon-specific protein. This is particularly important for Apr, DsrAB, Ttr/Phs-like molybdoenzymes, and sulfurtransferases, whose homologs can function in different pathways.

### Taxonomic nodes

- *Desulfocapsa sulfexigens* SB164P1
- *Desulfolithobacter dissulfuricans* GF1T
- *Desulfocapsa thiozymogenes*
- *Desulfobulbus propionicus*
- *Thermosulfurimonas dismutans*
- *Dissulfuribacter thermophilus*
- *Desulfurella amilsii*
- *Sulfurimonas* spp.
- *Sulfurovum* spp.
- Campylobacterota
- Desulfobulbaceae

NCBI Taxonomy CURIEs should be resolved from the current NCBI taxonomy dump rather than inferred from names, especially for recently renamed strains and higher taxa.

## 3. Candidate causal edges

The following table is the recommended evidence-centered starting set for `disproportionation.yaml`.

| subject | predicate | object | evidence strength | key reference DOI | short supporting snippet | curation note |
|---|---|---|---|---|---|---|
| Disproportionation (METPO:1000806) | has_input | elemental sulfur (S0) | strong | 10.4056/sigs.3777412 | “elemental sulfur, thiosulfate and sulfite serve as both electron donor and acceptor, and are converted to hydrogen sulfide and sulfate” (finster2013completegenomesequence pages 1-2) | Core trait scope; sulfur-focused but broadly consistent with the supplied METPO definition. |
| Elemental sulfur disproportionation | has_output | sulfate + hydrogen sulfide | strong | 10.1128/aem.59.1.101-108.1993 | “The quantification of the products revealed that S0 was microbially disproportionated to sulfate and sulfide, as follows: 4S0 + 4H20 → SO42- + 3H2S + 2H+” (thamdrup1993bacterialdisproportionationof pages 1-2) | Foundational stoichiometric edge for canonical sulfur disproportionation. |
| Thiosulfate disproportionation | has_output | sulfate + sulfide | strong | 10.1128/msystems.00954-22 | “For thiosulfate, the reaction follows S2O32– + H2O → SO42– + HS– + H+” (wang2023disproportionationofinorganic pages 9-12) | Strong experimental support from 2023 isolates; use as substrate-specific child edge. |
| Ferrihydrite [Fe(III)] | scavenges/removes | sulfide produced during S0 disproportionation | strong | 10.1128/aem.59.1.101-108.1993 | “The observed microbial disproportionation of S0 only proceeds significantly in the presence of sulfide-scavenging agents such as iron and manganese compounds.” (thamdrup1993bacterialdisproportionationof pages 1-2) | Environmental-factor edge; mechanistically explains why elemental sulfur disproportionation becomes favorable. |
| Ferrihydrite [Fe(III)] | enhances | growth during elemental sulfur disproportionation | strong | 10.1128/msystems.00954-22 | “Ferrihydrite (Fe(III)) addition enhanced growth, increasing maximum cell densities from 1.04-2.40 × 107 to 1.36-4.28 × 107 cells/mL” (wang2023disproportionationofinorganic pages 9-12) | Quantitative, recent support; edge should note substrate-specificity to S0 assays. |
| Manganese oxide [Mn(IV)] | enables/significantly supports | elemental sulfur disproportionation by sulfide scavenging | moderate | 10.1128/aem.59.1.101-108.1993 | “With both FeOOH and MnO2, cultures that metabolized S0 with concomitant reduction of the metal oxide were obtained.” (thamdrup1993bacterialdisproportionationof pages 1-2, thamdrup1993bacterialdisproportionationof pages 5-6) | Curate as environmental coupling; less directly resolved than Fe(III), but strong foundational evidence. |
| Direct cell contact with bulk S0 | not_required_for | elemental sulfur disproportionation | strong | 10.1128/msystems.00954-22 | “Dialysis membrane experiments showed that S0 disproportionation did not require the direct contact of cells with bulk sulfur.” (wang2023disproportionationofinorganic pages 1-2) | Negative mechanistic constraint; useful boundary edge. |
| Sat + AprAB | oxidizes | sulfite to sulfate in disproportionation model | moderate | 10.3389/fmicb.2022.1042116 | “proposed model for thiosulfate disproportionation… oxidation of sulfite to sulfate by Apr and Sat (II)” (hashimoto2022physiologicalandcomparative pages 12-13) | Strong for GF1T model; mark taxon-specific/model-supported rather than universal. |
| DsrAB | reduces | sulfite to sulfide in disproportionation model | moderate | 10.3389/fmicb.2022.1042116 | “reduction of sulfite to sulfide by DsrAB (IV)” (hashimoto2022physiologicalandcomparative pages 12-13) | Mechanistic edge supported by proposed model and proteomics context; curate as taxon-specific unless generalized separately. |
| DsrC | positively_associated_with | thiosulfate disproportionation condition | moderate | 10.3389/fmicb.2022.1042116 | “DsrC… was found to be 3.4-fold more abundantly produced in TD than in SR” (hashimoto2022physiologicalandcomparative pages 7-9) | Association, not direct catalytic proof; mark uncertain. |
| QmoABC | positively_associated_with | oxidative branch of disproportionation | moderate | 10.3389/fmicb.2022.1042116 | “APS reductase-associated electron transfer complex (QmoABC) was also abundantly produced in TD” (hashimoto2022physiologicalandcomparative pages 7-9) | Association to oxidative branch is inferred from co-production with Sat/Apr; mark uncertain. |
| TtrBCA tetrathionate reductase-type complex | positively_associated_with | thiosulfate disproportionation | moderate | 10.3389/fmicb.2022.1042116 | “proteins related to the subunits of molybdopterin-containing tetrathionate reductase-type protein… were specifically and abundantly produced… when strain GF1T was grown via thiosulfate disproportionation” (hashimoto2022physiologicalandcomparative pages 9-10) | Strong proteomic association but exact directionality/function unresolved; mark uncertain. |
| YTD gene cluster | positively_associated_with | microbial sulfur disproportionation | moderate | 10.3389/fmicb.2022.1042116 | “The YTD cluster is reported to potentially have an important role in microbial sulfur disproportionation” (hashimoto2022physiologicalandcomparative pages 7-9) | Association only; explicit functional uncertainty should be retained. |
| Wood-Ljungdahl pathway | enables | CO2 fixation during disproportionation growth | strong | 10.3389/fmicb.2022.1042116 | “a full set of enzymes required for CO2 fixation by the Wood-Ljungdhal pathway were detected in both TD and SR” (hashimoto2022physiologicalandcomparative pages 7-9) | Strong metabolic module edge for autotrophic sulfur disproportionators such as GF1T. |
| Desulfocapsa sulfexigens | grows_with | CO2 as sole carbon source during sulfur disproportionation | strong | 10.4056/sigs.3777412 | “appears metabolically specialized in growing by disproportionating elemental sulfur, sulfite or thiosulfate with CO2 as the sole carbon source” (finster2013completegenomesequence pages 1-2) | Useful phenotype edge linking trait to chemolithoautotrophy. |
| Campylobacterota sulfur disproportionation pathway | lacks_components | aprAB + dsrAB/dsrC + dsrMKJOP + qmoABC | strong | 10.1128/msystems.00954-22 | “Campylobacterota strains did not contain some genes of the Dsr and rDSR pathways (aprAB, dsrAB, dsrC, dsrMKJOP, and qmoABC)… suggesting the existence of an unrevealed catabolic pathway” (wang2023disproportionationofinorganic pages 1-2) | Key recent distinction: evidence for an alternative mechanism; curate as a separate causal subgraph, not a contradiction of canonical Desulfobulbaceae-like models. |
| Campylobacterota sulfur disproportionation pathway | has_mechanism | unrevealed/distinct catabolic pathway | moderate | 10.1128/msystems.00954-22 | “suggesting the existence of an unrevealed catabolic pathway for sulfur disproportionation” (wang2023disproportionationofinorganic pages 1-2) | High-value recent edge, but inherently uncertain until biochemically resolved. |
| Sulfurimonas / Sulfurovum (Campylobacterota) | capable_of | thiosulfate and elemental sulfur disproportionation | strong | 10.1128/msystems.00954-22 | “five Sulfurimonas and Sulfurovum isolates could disproportionate thiosulfate and elemental sulfur” (wang2023disproportionationofinorganic pages 1-2) | Important taxonomic expansion of the trait in 2023. |


*Table: This table compiles the strongest candidate causal edges for microbial sulfur disproportionation, emphasizing experimentally supported reactions, environmental dependencies, and mechanistic modules. It separates well-supported canonical edges from taxon-specific or still-uncertain associations, especially for the distinct Campylobacterota pathway.*

### Additional candidate triples

1. **Elemental sulfur disproportionation — produces — sulfate.** Strong, direct chemistry.
2. **Elemental sulfur disproportionation — produces — sulfide.** Strong, direct chemistry.
3. **Low free-sulfide concentration — increases thermodynamic favorability of — elemental-sulfur disproportionation.** Strong thermodynamic interpretation; environmental rather than intracellular edge. (finster2013completegenomesequence pages 1-2)
4. **Ferrihydrite — reacts with — produced sulfide.** Strong chemical coupling.
5. **Ferrihydrite–sulfide reaction — produces — FeS and regenerated S0.** Strong foundational chemistry; note that regenerated sulfur complicates measured product ratios. (thamdrup1993bacterialdisproportionationof pages 5-6, canfield1998isotopefractionationand pages 7-8)
6. **Sulfide scavenging — promotes — chemolithotrophic growth on S0.** Strong for the tested organisms, but not universal for more favorable substrates.
7. **Thiosulfate disproportionation — supports — chemolithoautotrophic growth of Sulfurimonas/Sulfurovum isolates.** Strong, taxon-specific. (wang2023disproportionationofinorganic pages 1-2)
8. **Wood–Ljungdahl pathway — fixes — CO2 during GF1T growth.** Strong module-level evidence; avoid claiming it is universal. (hashimoto2022physiologicalandcomparative pages 7-9)
9. **Nitrogen fixation — co-occurs with — sulfur-disproportionating growth in GF1T and D. sulfexigens.** Supported accessory phenotype, but not part of the causal core. (finster2013completegenomesequence pages 1-2, hashimoto2022physiologicalandcomparative pages 9-10)
10. **Direct S0 contact — increases efficiency of — S0 disproportionation.** Moderate: dialysis separation lowered ferrous iron and sulfate production by approximately 51% and 50%, while demonstrating contact was not absolutely required. (wang2023disproportionationofinorganic pages 9-12)

## 4. Recent developments, 2023–2024

### Alternative mechanism in Campylobacterota — 2023

Wang and colleagues provided the most important recent mechanistic revision. Five *Sulfurimonas*/*Sulfurovum* isolates were shown to grow by thiosulfate and elemental-sulfur disproportionation. Campylobacterota comprised 56.4–99.9% of enrichment communities; *Sulfurimonas* reached 3.7–93.0% and *Sulfurovum* 83.0–96.1% in relevant enrichments. One hydrothermal-plume result reported up to 61.60% abundance. (wang2023disproportionationofinorganic pages 12-13, wang2023disproportionationofinorganic pages 2-4)

The measured chemistry was substantial: strain ST-27 consumed 10.61 mM thiosulfate and generated 10.43 mM sulfate plus 4.10 mM sulfide over 12 days; ST-29 generated 9.64 mM sulfate and 7.12 mM sulfide from 10.12 mM thiosulfate. Ferrihydrite increased maximum cell density from 1.04–2.40 × 10^7 to 1.36–4.28 × 10^7 cells mL−1, with reported doubling times of 1.6–1.9 days. (wang2023disproportionationofinorganic pages 9-12)

Most importantly, these genomes lacked the canonical Apr/Dsr/Qmo machinery. The authors therefore inferred an unrevealed pathway, potentially involving reduction proteins such as Psr/Phs and oxidation proteins such as Sox, Sqr, Sdo, or Sor. Those candidate assignments remain hypotheses; the physiological phenotype is strong, but the causal enzyme chain is not resolved. (wang2023disproportionationofinorganic pages 1-2, wang2023disproportionationofinorganic pages 12-13)

### Tetrathionate-hydrolase clarification — 2024

Kanao’s 2024 review sharpened a major boundary issue. Purified TTHs from acidophilic sulfur oxidizers have acidic activity optima, generally pH 2.5–4.0, consistent with periplasmic or outer-membrane localization. In *Acidithiobacillus ferrooxidans*, `tth` expression was elevated 68 ± 21-fold on elemental sulfur and 181 ± 5-fold on tetrathionate relative to Fe2+; an *A. caldus* `tetH` S4/S0 expression ratio of 233.5 ± 134.0 was reported. Proposed overall Af-TTH chemistry is `8 S4O6^2− + 8 H2O → 8 S2O3^2− + S8 + 8 SO4^2− + 16 H+`. These data establish TetH as a real sulfur-splitting enzyme, but in an acidophilic S4-intermediate oxidation system rather than, by themselves, a growth-linked anaerobic disproportionation phenotype. (kanao2024tetrathionatehydrolasefrom pages 1-2, kanao2024tetrathionatehydrolasefrom pages 3-4)

## 5. Applications and real-world significance

1. **Primary production in dark ecosystems.** Chemolithoautotrophic disproportionators fix CO2 in marine sediments and hydrothermal systems. The newly demonstrated Campylobacterota capacity suggests that primary production attributed only to sulfur oxidation may partly include disproportionation. (wang2023disproportionationofinorganic pages 1-2, finster2013completegenomesequence pages 1-2)
2. **Iron and manganese cycling.** Produced sulfide reacts with Fe(III), Fe(II), or Mn(IV), precipitating FeS/pyrite or reducing Mn oxides. The process therefore links sulfur turnover to mineral formation and metal mobility. (thamdrup1993bacterialdisproportionationof pages 3-4, thamdrup1993bacterialdisproportionationof pages 5-6)
3. **Sedimentary isotope interpretation.** Elemental-sulfur disproportionation produced sulfide depleted in 34S by 5.5–6.9‰, average 6.3‰, and sulfate enriched by 17.1–20.2‰, average 18.8‰, in most tested cultures. *Desulfobulbus propionicus* showed nearly twice those effects, suggesting pathway diversity. Such signals can influence interpretations of ancient sulfur cycling. (canfield1998isotopefractionationand pages 9-10, canfield1998isotopefractionationand pages 1-2)
4. **Sulfidogenic water treatment and metal recovery.** In principle, an organic-free process can generate sulfide for precipitating dissolved metals while producing sulfate. However, reactor performance depends on maintaining favorable sulfide activity and avoiding thermodynamic inhibition; application-level nodes should be added only from reactor-specific studies, not inferred from pure-culture physiology.
5. **Mine and acidic environments.** TetH/SOR-related sulfur splitting affects thiosulfate, tetrathionate, elemental sulfur, sulfate, and acidity in biomining systems, but these modules should remain separate from anaerobic METPO:1000806 unless a physiological disproportionation assay is available. (kanao2024tetrathionatehydrolasefrom pages 1-2, kanao2024tetrathionatehydrolasefrom pages 3-4)

## 6. Expert synthesis for graph design

The evidence favors a **modular causal graph**:

- **Shared phenotype layer:** intermediate-valence substrate → oxidized product + reduced product → energy conservation/growth.
- **Environmental thermodynamics layer:** sulfide removal → lower sulfide activity → more favorable S0 disproportionation → increased growth.
- **Canonical Desulfobulbaceae-like mechanism:** substrate activation/cleavage → sulfite intermediate; Sat/AprAB oxidize one fraction to sulfate; DsrAB/DsrC reduce another fraction to sulfide; Qmo and Dsr membrane complexes provide electron-transfer links.
- **Ttr/YTD-associated GF1T module:** TtrBCA-like proteins and YTD sulfur carriers are enriched under thiosulfate disproportionation, but exact reactions remain uncertain.
- **Alternative Campylobacterota module:** phenotype established; canonical Apr/Dsr pathway absent; mechanistic edges should end at “unknown pathway” until genetics or biochemistry resolves the enzymes.

This structure avoids treating `dsrAB` as a universal marker. The same genes occur in sulfate reduction and reverse-Dsr sulfur oxidation, while verified Campylobacterota disproportionators lack them. Likewise, the presence of SOR or TetH indicates sulfur-splitting chemistry but not necessarily the target physiological trait. (wang2023disproportionationofinorganic pages 1-2, vliet2021thebacterialsulfur pages 13-14, hashimoto2022physiologicalandcomparative pages 9-10)

## 7. Claims not yet suitable for TraitMech curation

- Do **not** curate a universal `DsrAB causes disproportionation` edge.
- Do **not** assign disproportionation from `dsrAB`, `aprAB`, `sor`, `phs`, `psr`, `ttr`, or `tetH` occurrence alone.
- Treat **TtrBCA**, **YTD**, rhodanese, and molybdopterin-oxidoreductase roles as **taxon-specific, proteomically associated, and uncertain** pending knockout or purified-enzyme evidence. (hashimoto2022physiologicalandcomparative pages 9-10, hashimoto2022physiologicalandcomparative pages 7-9)
- Do not curate the proposed Campylobacterota activation mechanisms—polysulfane formation, polymeric-sulfur uptake, soluble polysulfides, or extracellular electron transfer—as factual edges; they were hypotheses. (wang2023disproportionationofinorganic pages 12-13)
- Ferrihydrite is not a universal biochemical reactant. It is chiefly a sulfide sink and growth-promoting environmental factor; thiosulfate disproportionation can proceed without it, and recent cultures had similar reaction rates with and without ferrihydrite even though growth efficiency improved. (wang2023disproportionationofinorganic pages 7-9)
- MnO2 experiments combine biological disproportionation with rapid abiotic sulfide oxidation; assign separate biological and chemical edges and mark the exact coupling as partially unresolved. (thamdrup1993bacterialdisproportionationof pages 5-6)
- SOR requires O2 in the cited reaction and TetH is primarily placed in acidophilic sulfur oxidation. Neither should be merged with the anaerobic core without phenotype-level evidence. (guo2016sulfurmetabolismpathways pages 7-8, kanao2024tetrathionatehydrolasefrom pages 1-2)
- Isotope fractionation is a useful assay signature, not a necessary defining property; values differ among organisms and pathways. (canfield1998isotopefractionationand pages 9-10, canfield1998isotopefractionationand pages 1-2)

## DOI-first bibliography

1. Wang S. et al. **Disproportionation of Inorganic Sulfur Compounds by Mesophilic Chemolithoautotrophic Campylobacterota.** *mSystems* 8, published February 2023. DOI: [10.1128/msystems.00954-22](https://doi.org/10.1128/msystems.00954-22). (wang2023disproportionationofinorganic pages 1-2)
2. Kanao T. **Tetrathionate hydrolase from the acidophilic microorganisms.** *Frontiers in Microbiology* 15, published 29 January 2024. DOI: [10.3389/fmicb.2024.1338669](https://doi.org/10.3389/fmicb.2024.1338669). (kanao2024tetrathionatehydrolasefrom pages 1-2)
3. Hashimoto Y. et al. **Physiological and comparative proteomic characterization of Desulfolithobacter dissulfuricans gen. nov., sp. nov.** *Frontiers in Microbiology* 13, published December 2022. DOI: [10.3389/fmicb.2022.1042116](https://doi.org/10.3389/fmicb.2022.1042116). (hashimoto2022physiologicalandcomparative pages 12-13)
4. Finster K.W. et al. **Complete genome sequence of Desulfocapsa sulfexigens.** *Standards in Genomic Sciences* 8:58–68, published April 2013. DOI: [10.4056/sigs.3777412](https://doi.org/10.4056/sigs.3777412). (finster2013completegenomesequence pages 1-2)
5. Thamdrup B. et al. **Bacterial Disproportionation of Elemental Sulfur Coupled to Chemical Reduction of Iron or Manganese.** *Applied and Environmental Microbiology* 59:101–108, published January 1993. DOI: [10.1128/AEM.59.1.101-108.1993](https://doi.org/10.1128/AEM.59.1.101-108.1993). (thamdrup1993bacterialdisproportionationof pages 1-2)
6. Canfield D.E., Thamdrup B., Fleischer S. **Isotope fractionation and sulfur metabolism by pure and enrichment cultures of elemental sulfur-disproportionating bacteria.** *Limnology and Oceanography* 43:253–264, published March 1998. DOI: [10.4319/lo.1998.43.2.0253](https://doi.org/10.4319/lo.1998.43.2.0253). (canfield1998isotopefractionationand pages 1-2)
7. Guo W. et al. **Sulfur Metabolism Pathways in Sulfobacillus acidophilus TPY.** *Frontiers in Microbiology* 7, published November 2016. DOI: [10.3389/fmicb.2016.01861](https://doi.org/10.3389/fmicb.2016.01861). (guo2016sulfurmetabolismpathways pages 7-8)
8. van Vliet D.M. et al. **The bacterial sulfur cycle in expanding dysoxic and euxinic marine waters.** *Environmental Microbiology* 23:2834–2857, published 2021. DOI: [10.1111/1462-2920.15265](https://doi.org/10.1111/1462-2920.15265). (vliet2021thebacterialsulfur pages 13-14)
9. Finster K. **Microbiological disproportionation of inorganic sulfur compounds.** *Journal of Sulfur Chemistry* 29:281–292, published 2008. DOI: [10.1080/17415990802105770](https://doi.org/10.1080/17415990802105770). This is the supplied review evidence and remains useful for historical scope, but newer organism- and pathway-specific evidence should control graph edges.

References

1. (thamdrup1993bacterialdisproportionationof pages 1-2): Bo Thamdrup, Kai Finster, Jens Würgler Hansen, and Friedhelm Bak. Bacterial disproportionation of elemental sulfur coupled to chemical reduction of iron or manganese. Applied and Environmental Microbiology, 59:101-108, Jan 1993. URL: https://doi.org/10.1128/aem.59.1.101-108.1993, doi:10.1128/aem.59.1.101-108.1993. This article has 513 citations and is from a peer-reviewed journal.

2. (finster2013completegenomesequence pages 1-2): Kai Waldemar Finster, Kasper Urup Kjeldsen, Michael Kube, Richard Reinhardt, Marc Mussmann, Rudolf Amann, and Lars Schreiber. Complete genome sequence of desulfocapsa sulfexigens, a marine deltaproteobacterium specialized in disproportionating inorganic sulfur compounds. Standards in Genomic Sciences, 8:58-68, Apr 2013. URL: https://doi.org/10.4056/sigs.3777412, doi:10.4056/sigs.3777412. This article has 105 citations.

3. (wang2023disproportionationofinorganic pages 1-2): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.

4. (hashimoto2022physiologicalandcomparative pages 12-13): Yurina Hashimoto, Shigeru Shimamura, Akihiro Tame, Shigeki Sawayama, Junichi Miyazaki, Ken Takai, and Satoshi Nakagawa. Physiological and comparative proteomic characterization of desulfolithobacter dissulfuricans gen. nov., sp. nov., a novel mesophilic, sulfur-disproportionating chemolithoautotroph from a deep-sea hydrothermal vent. Frontiers in Microbiology, Dec 2022. URL: https://doi.org/10.3389/fmicb.2022.1042116, doi:10.3389/fmicb.2022.1042116. This article has 25 citations and is from a peer-reviewed journal.

5. (hashimoto2022physiologicalandcomparative pages 7-9): Yurina Hashimoto, Shigeru Shimamura, Akihiro Tame, Shigeki Sawayama, Junichi Miyazaki, Ken Takai, and Satoshi Nakagawa. Physiological and comparative proteomic characterization of desulfolithobacter dissulfuricans gen. nov., sp. nov., a novel mesophilic, sulfur-disproportionating chemolithoautotroph from a deep-sea hydrothermal vent. Frontiers in Microbiology, Dec 2022. URL: https://doi.org/10.3389/fmicb.2022.1042116, doi:10.3389/fmicb.2022.1042116. This article has 25 citations and is from a peer-reviewed journal.

6. (wang2023disproportionationofinorganic pages 15-17): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.

7. (wang2023disproportionationofinorganic pages 9-12): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.

8. (canfield1998isotopefractionationand pages 7-8): D. E. Canfield, B. Thamdrup, and S. Fleischer. Isotope fractionation and sulfur metabolism by pure and enrichment cultures of elemental sulfur‐disproportionating bacteria. Limnology and Oceanography, 43:253-264, Mar 1998. URL: https://doi.org/10.4319/lo.1998.43.2.0253, doi:10.4319/lo.1998.43.2.0253. This article has 242 citations and is from a highest quality peer-reviewed journal.

9. (guo2016sulfurmetabolismpathways pages 7-8): Wenbin Guo, Huijun Zhang, Wengen Zhou, Yuguang Wang, Hong-bo Zhou, and Xinhua Chen. Sulfur metabolism pathways in sulfobacillus acidophilus tpy, a gram-positive moderate thermoacidophile from a hydrothermal vent. Frontiers in Microbiology, Nov 2016. URL: https://doi.org/10.3389/fmicb.2016.01861, doi:10.3389/fmicb.2016.01861. This article has 19 citations and is from a peer-reviewed journal.

10. (kanao2024tetrathionatehydrolasefrom pages 1-2): Tadayoshi Kanao. Tetrathionate hydrolase from the acidophilic microorganisms. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1338669, doi:10.3389/fmicb.2024.1338669. This article has 9 citations and is from a peer-reviewed journal.

11. (kanao2024tetrathionatehydrolasefrom pages 3-4): Tadayoshi Kanao. Tetrathionate hydrolase from the acidophilic microorganisms. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1338669, doi:10.3389/fmicb.2024.1338669. This article has 9 citations and is from a peer-reviewed journal.

12. (hashimoto2022physiologicalandcomparative pages 6-7): Yurina Hashimoto, Shigeru Shimamura, Akihiro Tame, Shigeki Sawayama, Junichi Miyazaki, Ken Takai, and Satoshi Nakagawa. Physiological and comparative proteomic characterization of desulfolithobacter dissulfuricans gen. nov., sp. nov., a novel mesophilic, sulfur-disproportionating chemolithoautotroph from a deep-sea hydrothermal vent. Frontiers in Microbiology, Dec 2022. URL: https://doi.org/10.3389/fmicb.2022.1042116, doi:10.3389/fmicb.2022.1042116. This article has 25 citations and is from a peer-reviewed journal.

13. (thamdrup1993bacterialdisproportionationof pages 5-6): Bo Thamdrup, Kai Finster, Jens Würgler Hansen, and Friedhelm Bak. Bacterial disproportionation of elemental sulfur coupled to chemical reduction of iron or manganese. Applied and Environmental Microbiology, 59:101-108, Jan 1993. URL: https://doi.org/10.1128/aem.59.1.101-108.1993, doi:10.1128/aem.59.1.101-108.1993. This article has 513 citations and is from a peer-reviewed journal.

14. (hashimoto2022physiologicalandcomparative pages 9-10): Yurina Hashimoto, Shigeru Shimamura, Akihiro Tame, Shigeki Sawayama, Junichi Miyazaki, Ken Takai, and Satoshi Nakagawa. Physiological and comparative proteomic characterization of desulfolithobacter dissulfuricans gen. nov., sp. nov., a novel mesophilic, sulfur-disproportionating chemolithoautotroph from a deep-sea hydrothermal vent. Frontiers in Microbiology, Dec 2022. URL: https://doi.org/10.3389/fmicb.2022.1042116, doi:10.3389/fmicb.2022.1042116. This article has 25 citations and is from a peer-reviewed journal.

15. (wang2023disproportionationofinorganic pages 12-13): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.

16. (wang2023disproportionationofinorganic pages 2-4): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.

17. (thamdrup1993bacterialdisproportionationof pages 3-4): Bo Thamdrup, Kai Finster, Jens Würgler Hansen, and Friedhelm Bak. Bacterial disproportionation of elemental sulfur coupled to chemical reduction of iron or manganese. Applied and Environmental Microbiology, 59:101-108, Jan 1993. URL: https://doi.org/10.1128/aem.59.1.101-108.1993, doi:10.1128/aem.59.1.101-108.1993. This article has 513 citations and is from a peer-reviewed journal.

18. (canfield1998isotopefractionationand pages 9-10): D. E. Canfield, B. Thamdrup, and S. Fleischer. Isotope fractionation and sulfur metabolism by pure and enrichment cultures of elemental sulfur‐disproportionating bacteria. Limnology and Oceanography, 43:253-264, Mar 1998. URL: https://doi.org/10.4319/lo.1998.43.2.0253, doi:10.4319/lo.1998.43.2.0253. This article has 242 citations and is from a highest quality peer-reviewed journal.

19. (canfield1998isotopefractionationand pages 1-2): D. E. Canfield, B. Thamdrup, and S. Fleischer. Isotope fractionation and sulfur metabolism by pure and enrichment cultures of elemental sulfur‐disproportionating bacteria. Limnology and Oceanography, 43:253-264, Mar 1998. URL: https://doi.org/10.4319/lo.1998.43.2.0253, doi:10.4319/lo.1998.43.2.0253. This article has 242 citations and is from a highest quality peer-reviewed journal.

20. (vliet2021thebacterialsulfur pages 13-14): Daan M. van Vliet, F.A. Bastiaan von Meijenfeldt, Bas E. Dutilh, Laura Villanueva, Jaap S. Sinninghe Damsté, Alfons J.M. Stams, and Irene Sánchez‐Andrea. The bacterial sulfur cycle in expanding dysoxic and euxinic marine waters. Environmental Microbiology, 23:2834-2857, Oct 2021. URL: https://doi.org/10.1111/1462-2920.15265, doi:10.1111/1462-2920.15265. This article has 156 citations and is from a domain leading peer-reviewed journal.

21. (wang2023disproportionationofinorganic pages 7-9): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 39 citations and is from a peer-reviewed journal.