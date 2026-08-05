---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:42:16.788836'
end_time: '2026-08-04T09:51:12.928476'
duration_seconds: 536.14
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: red pigmented
  trait_identifier: METPO:1003028
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: red_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    red due to production of red pigments such as prodiginines or carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_red
  evidence_summary: 'DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports
    red microbial pigmentation as a prodiginine-associated color phenotype in representative
    bacteria.)'
  causal_graph_summary: 'red_pigmented_prodiginine_pathway: 10 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** red pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003028
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear red due to production of red pigments such as prodiginines or carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_red
- **Existing evidence:** DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports red microbial pigmentation as a prodiginine-associated color phenotype in representative bacteria.)
- **Existing causal graph summary:** red_pigmented_prodiginine_pathway: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **red pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/red_pigmented.yaml`.

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
- **Trait label:** red pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003028
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear red due to production of red pigments such as prodiginines or carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_red
- **Existing evidence:** DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports red microbial pigmentation as a prodiginine-associated color phenotype in representative bacteria.)
- **Existing causal graph summary:** red_pigmented_prodiginine_pathway: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **red pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/red_pigmented.yaml`.

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


# Curation report: microbial trait **red pigmented**

## 1. Executive scope

- **Trait:** red pigmented
- **Identifier:** **METPO:1003028**
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1003021
- **Synonym:** `Pigment_red`

### Recommended operational definition

A positive instance is a microbial colony, biomass, or cell population that appears red because the organism produces and accumulates a red pigment under the recorded culture or assay conditions. The trait is an **observable morphology**, not a single conserved biochemical pathway. In *Serratia marcescens*, the best-supported mechanism is biosynthesis of the red linear tripyrrole prodigiosin by the 14-gene `pigABCDEFGHIJKLMN` operon. Other organisms can appear red through chemically unrelated carotenoids, including lycopene, astaxanthin, torularhodin, or deinoxanthin-like compounds. A 2024 primary study describes *S. marcescens* ATCC 274 as producing a “vibrant red pigment called prodigiosin.” (esteves2024serratiamarcescensatcc pages 1-2)

### Boundary cases

1. **Do not equate the phenotype with prodigiosin.** Prodigiosin is one sufficient molecular cause, not the definition of the trait.
2. **Color is condition-dependent.** Purified prodigiosin from *S. marcescens* OK482790 was reported as red at neutral/acidic pH, pink at pH 2, and orange at pH 9, with an absorption maximum of approximately 533–540 nm. Thus pH, medium, illumination, growth phase, and scoring method should be recorded as assay context. (hamada2024characterizationofserratia pages 8-9)
3. **Exclude red fluorescence without red visible pigmentation**, staining by an exogenous dye, red medium caused by a secreted product when colonies/cells themselves were not scored, blood agar hemolysis, and host-derived coloration.
4. **Orange, pink, yellow, or brown isolates are not automatically positive.** Curate them only if the source explicitly calls the colony/cells red under specified conditions.
5. **Production capacity versus observed morphology:** a biosynthetic gene cluster predicts capacity, whereas METPO:1003028 should normally require observed red appearance or chemically confirmed pigment production linked to appearance.

## 2. Current mechanistic model

The strongest TraitMech-ready model is a taxon-qualified *Serratia* prodigiosin graph:

1. The `pigA–pigN` operon encodes two precursor branches.
2. The MAP branch produces 2-methyl-3-*n*-amylpyrrole; the MBC branch produces 4-methoxy-2,2′-bipyrrole-5-carbaldehyde.
3. PigC performs terminal condensation of the two branch products to form prodigiosin.
4. Accumulated prodigiosin generates the visible red phenotype.
5. Transcription is modulated by direct and indirect regulators and by environmental inputs, including temperature, phosphate status, quorum-sensing context, and phage infection. The pathway assignment reported by Sun et al. is `pigD/pigE/pigB` for MAP and `pigA` plus `pigF–pigN` for MBC. (sun2020improvedprodigiosinproduction pages 1-2)

| subject | predicate | object | taxon/strain | evidence type | confidence | DOI |
|---|---|---|---|---|---|---|
| pigABCDEFGHIJKLMN operon | enables biosynthesis of | prodigiosin | *Serratia marcescens* ATCC 274; JNB5-1 | operon/genetic evidence, transcriptional response (esteves2024serratiamarcescensatcc pages 1-2, pan2021regulatorrcsbcontrols pages 7-10) | High | 10.1038/s41598-024-68747-3; 10.1128/AEM.02052-20 |
| MAP precursor branch + MBC precursor branch | are condensed by | PigC to form prodigiosin | *Serratia* spp. / prodigiosin pathway literature | pathway/mechanistic review summarized from primary studies (esteves2024serratiamarcescensatcc pages 11-12, sun2020improvedprodigiosinproduction pages 1-2) | High | 10.1038/nrmicro1531; 10.3389/fbioe.2020.00344 |
| prodigiosin | causes | red pigmented phenotype | *Serratia marcescens* ATCC 274; OK482790 | phenotype-chemistry association, pigment characterization (esteves2024serratiamarcescensatcc pages 1-2, hamada2024characterizationofserratia pages 8-9) | High | 10.1038/s41598-024-68747-3; 10.1186/s12866-024-03634-5 |
| Chi phage infection | increases transcription of | pig operon | *Serratia marcescens* ATCC 274 | primary infection/reporter assay (esteves2024serratiamarcescensatcc pages 1-2) | High | 10.1038/s41598-024-68747-3 |
| Chi phage infection | increases production of | prodigiosin | *Serratia marcescens* ATCC 274 | primary infection/phenotype assay (esteves2024serratiamarcescensatcc pages 1-2) | High | 10.1038/s41598-024-68747-3 |
| CpxR | directly represses transcription of | pig gene cluster promoter | *Serratia marcescens* JNB5-1 | primary EMSA + mutant analysis (sun2020improvedprodigiosinproduction pages 1-2) | High | 10.3389/fbioe.2020.00344 |
| MetR | directly represses transcription of | pigP | *Serratia marcescens* | primary EMSA + RT-qPCR/transcriptomics (pan2020lysrtypetranscriptionalregulator pages 1-2) | High | 10.1128/AEM.02241-19 |
| PigP | positively regulates | pig operon | *Serratia marcescens* | regulator linkage from direct MetR→pigP repression and pigP as positive regulator (pan2020lysrtypetranscriptionalregulator pages 1-2) | High | 10.1128/AEM.02241-19 |
| RcsB | binds promoter of and negatively regulates | flhDC | *Serratia marcescens* JNB5-1 | primary EMSA + expression analysis (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 46-48) | High | 10.1128/AEM.02052-20 |
| FlhDC | activates biosynthesis of | prodigiosin | *Serratia marcescens* JNB5-1 | primary regulatory genetics downstream of RcsB (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 1-3) | High | 10.1128/AEM.02052-20 |


*Table: This table summarizes the strongest, most curation-ready causal edges for the red pigmented trait METPO:1003028, emphasizing direct genetic and regulatory evidence in Serratia prodigiosin systems. It is useful as a compact starting point for building a TraitMech YAML graph while preserving taxon specificity and confidence.*

## 3. Candidate nodes grouped by type

### A. Trait and observable-state nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| red pigmented | **METPO:1003028** | Terminal phenotype node; quote the CURIE verbatim. |
| pigmentation phenotype | METPO:1003021 | Supplied parent trait. |
| red colony/cell appearance | Label only | Assay-observed state; keep distinct from pigment concentration. |
| pigment accumulation | GO biological-process candidate; verify exact term before use | Proximal process linking chemistry to visible phenotype. |

### B. Pathways and metabolic modules

| Candidate node | Grounding recommendation | Evidence/qualification |
|---|---|---|
| prodigiosin biosynthesis | MetaCyc/KEGG pathway candidate; verify release-specific identifier | Strongest pathway-level cause in *Serratia*. |
| prodiginine biosynthesis | Label or verified MetaCyc/KEGG term | Broader family pathway; structurally diverse products occur in *Pseudoalteromonas* and actinomycetes. |
| `pigABCDEFGHIJKLMN` operon | Label plus strain-specific genomic locus | Fourteen genes in *S. marcescens* ATCC 274 and JNB5-1. (esteves2024serratiamarcescensatcc pages 1-2, pan2021regulatorrcsbcontrols pages 7-10) |
| MAP branch | Label only | Produces 2-methyl-3-*n*-amylpyrrole; literature abbreviations can be inconsistent, so store the chemical name. |
| MBC branch | Label only | Produces 4-methoxy-2,2′-bipyrrole-5-carbaldehyde. |
| carotenoid biosynthesis | GO:0016117 | Candidate alternative mechanism, not part of the *Serratia* prodigiosin pathway. |
| mevalonate pathway | GO:0019287 | Relevant to red yeasts; upstream and not sufficient for red appearance. |
| methylerythritol-phosphate pathway | GO:0019288 | Relevant to many bacterial carotenoids; upstream and not sufficient alone. |

### C. Genes, proteins, regulators, and complexes

| Node | Role | Grounding recommendation |
|---|---|---|
| PigC | Terminal condensing enzyme joining MAP and MBC | Label plus strain-specific UniProt accession after sequence verification. |
| PigA, PigF–PigN | MBC-branch proteins | Preserve individual labels; do not assign ortholog accessions across strains without sequence checks. |
| PigD, PigE, PigB | MAP-branch proteins | Same caution. |
| PigP | Positive regulator of the `pig` operon | Label/strain-specific protein. |
| MetR | LysR-family regulator; directly represses `pigP` | Label plus verified strain locus BVG90_22495 where applicable. (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| CpxA–CpxR | Two-component envelope-stress system; CpxR directly represses the `pig` promoter in JNB5-1 | GO:0000156 can ground two-component response-regulator activity only after exact role checking. |
| RcsB | Response regulator that directly binds the `flhDC` promoter and indirectly represses prodigiosin | Taxon/strain-specific regulatory edge. (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 46-48) |
| FlhD–FlhC | Transcriptional regulator activating prodigiosin production downstream of RcsB | Label plus verified protein accessions. |
| RpoS, PhoBR, LuxIR/AHL, LuxS/AI-2, HexS, Fnr | Additional candidate regulators | Do not add directionality globally; reported effects vary by strain and condition. (esteves2024serratiamarcescensatcc pages 11-12) |
| CrtI, CrtYB, CrtS, CrtR | Carotenogenic enzymes/regulators in red yeasts | Separate carotenoid subgraph. A 2024 genomic study identifies these as crucial candidates but largely infers pathway roles rather than proving each edge in its mutant. |

### D. Chemicals and metabolites

| Node | Suggested grounding | Curation note |
|---|---|---|
| prodigiosin | ChEBI identifier candidate—verify against current ChEBI before insertion | Red linear tripyrrole; proximal molecular cause in *Serratia*. |
| prodiginines | ChEBI class candidate—verify | Broader family; not every member has identical color or pathway. |
| 2-methyl-3-*n*-amylpyrrole (MAP) | ChEBI candidate—verify | PigC substrate. |
| 4-methoxy-2,2′-bipyrrole-5-carbaldehyde (MBC) | ChEBI candidate—verify | PigC substrate. |
| L-proline | CHEBI:17203 | MBC-branch precursor reported in the retrieved pathway evidence. |
| lycopene | CHEBI:15948 | Red carotenoid; a potential alternative proximal cause. |
| β-carotene, astaxanthin, torularhodin, deinoxanthin | Verify current ChEBI entries individually | Color ranges from yellow/orange to red and depends on mixture and concentration; require explicit phenotype evidence. |
| phosphate, oxygen, H₂O₂, cAMP, AHL, AI-2 | Verify chemical CURIEs individually | Regulatory/environmental inputs, not pigments. |

### E. Environmental and experimental factors

- Growth temperature, particularly **28°C versus ≥37°C** in *S. marcescens* JNB5-1.
- Phosphate availability.
- Cell density and quorum-sensing state.
- Oxidative stress.
- Aeration/oxygen regime.
- Medium composition and precursor supply.
- Solid versus liquid growth.
- Extracellular pH.
- Infection by flagellotropic bacteriophage χ.
- Growth phase/stationary phase.

These should usually be modeled as **context-qualified modulators**, not universal causes. The 2024 ATCC 274 study lists temperature, phosphate availability, oxidative stress, cAMP, and quorum sensing among known influences. (esteves2024serratiamarcescensatcc pages 1-2)

### F. Taxa

- *Serratia marcescens* ATCC 274: strongest 2024 phage-induction evidence.
- *S. marcescens* JNB5-1: strongest CpxR and RcsB genetic evidence.
- *S. marcescens* OK482790: pigment chemistry and pH-dependent color evidence.
- *Pseudoalteromonas* spp.: prodiginine analogs; pathway products and regulation differ from *Serratia*.
- *Streptomyces* spp.: undecylprodigiosin and related prodiginines.
- *Rhodotorula*/*Xanthophyllomyces*: carotenoid-producing red yeasts.
- *Deinococcus* spp.: deinoxanthin and related carotenoids.
- *Haloferax* spp.: red halophilic archaeal colonies associated with carotenoids.

Use exact NCBITaxon CURIEs only after verifying species and strain records; do not infer a species-level mechanism from genus-level color.

## 4. Candidate causal edges with evidence

| # | Subject–predicate–object | Reference | Supporting snippet | Curation notes |
|---:|---|---|---|---|
| 1 | `pigABCDEFGHIJKLMN operon` **enables** `prodigiosin biosynthesis` | Esteves & Scharf 2024, DOI 10.1038/s41598-024-68747-3 | “pig operon, containing genes essential for pigment biosynthesis” | **High confidence; ATCC 274.** Genetic/pathway evidence. (esteves2024serratiamarcescensatcc pages 1-2) |
| 2 | `PigD/PigE/PigB module` **produces** `MAP precursor` | Sun et al. 2020, DOI 10.3389/fbioe.2020.00344 | “pigD, pigE, and pigB encode MAP … production enzymes” | **High for JNB5-1/pathway; taxon-specific.** Retain full chemical name because MAP/MBC expansion is inconsistent across papers. (sun2020improvedprodigiosinproduction pages 1-2) |
| 3 | `PigA and PigF–PigN module` **produces** `MBC precursor` | Sun et al. 2020 | “pigA and pigF–pigN encode MBC … synthesis proteins” | **High for the cited pathway.** (sun2020improvedprodigiosinproduction pages 1-2) |
| 4 | `PigC` **condenses** `MAP + MBC` **to form** `prodigiosin` | Williamson et al. 2006; pathway summarized in Esteves & Scharf 2024 | “joined by condensation via PigC-like mechanism” | **High but foundational evidence should be attached directly in YAML:** DOI 10.1038/nrmicro1531 and the primary 2005 pathway paper. (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 11-12) |
| 5 | `prodigiosin accumulation` **causes** `red pigmented [METPO:1003028]` | Esteves & Scharf 2024; Hamada & Mohamed 2024 | “vibrant red pigment called prodigiosin”; “red pigment” with λmax 533–540 nm | **High; proximal phenotype edge.** Assay/pH context should be retained. (esteves2024serratiamarcescensatcc pages 1-2, hamada2024characterizationofserratia pages 8-9) |
| 6 | `χ phage infection` **increases** `prodigiosin production` | Esteves & Scharf 2024 | “greater than fivefold overproduction of prodigiosin” | **High; ATCC 274 and active flagellar infection only.** χ-resistant, nonflagellated cells did not respond. (esteves2024serratiamarcescensatcc pages 1-2) |
| 7 | `χ-induced cell lysate` **increases** `pig-operon transcription` | Esteves & Scharf 2024 | “threefold increase in transcription of the pig operon” | **High; reporter assay.** The lysate signal is unidentified, so do not invent an intermediate ligand. (esteves2024serratiamarcescensatcc pages 1-2) |
| 8 | `pig promoter regulatory elements` **mediate** `χ-induced pigmentation increase` | Esteves & Scharf 2024 | “Replacement of the pig promoter with a constitutive promoter abolished the pigmentation increase” | **High; mechanistic but promoter element remains unresolved.** (esteves2024serratiamarcescensatcc pages 1-2) |
| 9 | `CpxR` **directly represses transcription of** `pig gene cluster` | Sun et al. 2020 | “CpxR could bind to the promoter of the pig gene cluster and repress” | **High; EMSA plus mutant/expression evidence in JNB5-1.** (sun2020improvedprodigiosinproduction pages 1-2) |
| 10 | `cpxR deletion` **increases** `pig-operon and precursor-pathway transcription` | Sun et al. 2020 | “ΔcpxR mutant … increased transcription of the entire pig cluster” | **High; strain-specific.** Precursor pathways include proline, pyruvate, serine, methionine, and SAM. (sun2020improvedprodigiosinproduction pages 1-2, sun2020improvedprodigiosinproduction pages 2-3) |
| 11 | `37°C or higher` **decreases** `prodigiosin biosynthesis` relative to 28°C | Sun et al. 2020 | “efficient synthesis at 28°C but sharp reduction at 37°C or higher” | **Moderate–high; JNB5-1 and medium-specific.** Do not generalize the threshold to every *Serratia* strain. (sun2020improvedprodigiosinproduction pages 1-2) |
| 12 | `MetR` **directly represses** `pigP expression` | Pan et al. 2020, DOI 10.1128/AEM.02241-19 | “MetR directly binding to the promoter region of … PigP” | **High; EMSA, RT-qPCR, reporter, and mutant evidence.** (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| 13 | `PigP` **positively regulates** `pig operon` | Pan et al. 2020 | “PigP (a positive regulator of the pig operon)” | **High in the tested *Serratia* background; avoid assuming PigP is the master regulator in ATCC 274.** (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| 14 | `metR disruption` **increases** `prodigiosin production` | Pan et al. 2020 | “prodigiosin-hyperproducing strain … with disrupted metR” | **High; genetic perturbation.** (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| 15 | `RcsB` **binds and represses** `flhDC promoter` | Pan et al. 2021, DOI 10.1128/AEM.02052-20 | “RcsB specifically binds … in the flhDC promoter region” | **High; EMSA and regulatory genetics in JNB5-1.** (pan2021regulatorrcsbcontrols pages 46-48) |
| 16 | `FlhDC` **activates** `prodigiosin synthesis` | Pan et al. 2021 | “FlhDC acts as an activator” | **High within the RcsB–FlhDC network.** (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 46-48) |
| 17 | `rcsB disruption` **increases** `pigA–pigN transcription` | Pan et al. 2021 | “all 14 genes … upregulated 2.91–11.48 fold” | **High; direct perturbation, but regulation is indirect through FlhDC rather than direct pig-promoter binding.** (pan2021regulatorrcsbcontrols pages 7-10, pan2021regulatorrcsbcontrols pages 46-48) |
| 18 | `low phosphate / PhoBR state` **modulates** `prodigiosin biosynthesis` | Slater et al. 2003; summarized in 2024 study | “PhoBR responds to phosphate availability” | **Moderate pending direct full-text extraction.** Direction and strain context must be represented from the primary article, DOI 10.1046/j.1365-2958.2003.03295.x. (esteves2024serratiamarcescensatcc pages 11-12) |
| 19 | `quorum-sensing state` **modulates** `prodigiosin production` | Van Houdt et al. 2007; Hamada & Mohamed 2024 | QS “enhanced pigment production on solid surfaces” | **Uncertain/generalization risk.** LuxIR/AHL and LuxS/AI-2 effects are strain-dependent. (esteves2024serratiamarcescensatcc pages 1-2, hamada2024characterizationofserratia pages 8-9) |
| 20 | `carotenoid accumulation` **can cause** `red pigmented` | Wang et al. 2024; Anshi et al. 2024 | Reviews identify carotenoid-producing *Deinococcus* and red yeasts | **Biologically plausible but too broad for one universal edge.** Curate pigment-specific, taxon-specific edges only after direct color and perturbation evidence. (anshi2024unveilingtheintricacies pages 4-5, wang2024insightsintothe pages 11-11, wang2024insightsintothe pages 10-11) |

## 5. Recent developments and quantitative evidence

### 2024 phage–pigmentation connection

Esteves and Scharf showed that χ infection caused **more than a fivefold increase** in prodigiosin production in *S. marcescens* ATCC 274. A χ-induced cell lysate caused an approximately **threefold increase** in `pig`-operon reporter transcription, and constitutive promoter replacement eliminated the inducible pigmentation response. This is unusually strong evidence connecting an environmental biological factor to transcription and then to the visible trait. The responsible lysate signal remains unknown. (esteves2024serratiamarcescensatcc pages 1-2)

### Production engineering

Sun et al. deleted the negative regulator `cpxR` and inserted `proC`, `serC`, and `metH` at that locus. The engineered strain reached **5.83 g/L prodigiosin**, a **41.9% increase** over the parent. This demonstrates a real bioprocess implementation of the regulatory graph, but the engineering intervention should not be represented as a naturally occurring trait mechanism. (sun2020improvedprodigiosinproduction pages 1-2)

### Pigment characterization and biomedical assays

Hamada and Mohamed chemically characterized prodigiosin from *S. marcescens* OK482790 and observed pH-sensitive color and spectral behavior. Their 2024 study reported a minimum inhibitory concentration of **3.9 µg/mL** against *Enterococcus faecalis*, an ABTS-radical IC₅₀ of **74.18 ± 23.77 µg/mL**, and concentration-dependent inhibition of *Pseudomonas aeruginosa* biofilm. These are properties of the extracted molecule, not defining properties of METPO:1003028. (hamada2024characterizationofserratia pages 8-9)

### Broader microbial pigments

Recent reviews emphasize microbial pigments as potentially biodegradable colorants for food, cosmetics, textiles, and pharmaceutical research. Reported carotenoid production examples include **262 mg/L** by *Rhodotorula acheniorum* on whey filtrate and **30.39 mg/g** by *R. rubra* on sugarcane juice. These values show application potential but do not prove that every culture was scored specifically red. (anshi2024unveilingtheintricacies pages 4-5)

## 6. Applications and expert analysis

1. **Phenotypic identification and screening.** Red colony appearance remains useful for recognizing pigment-producing isolates, but it is not species-specific. Chemical confirmation is needed because unrelated pigments converge on similar visible colors.
2. **Metabolic engineering and fermentation.** Direct manipulation of CpxR and precursor supply can substantially increase prodigiosin titers. Phage-induced production is an intriguing process-control concept, although infection introduces stability, containment, and reproducibility challenges. (esteves2024serratiamarcescensatcc pages 1-2, sun2020improvedprodigiosinproduction pages 1-2)
3. **Natural colorants.** Microbial pigments are being investigated for food, textile, and cosmetic uses. Authoritative reviews emphasize scalability and biodegradability but also identify cost, extraction, stability, toxicity, and regulatory approval as bottlenecks. (anshi2024unveilingtheintricacies pages 4-5)
4. **Drug discovery.** Prodigiosin has antibacterial, antibiofilm, anticancer, antimalarial, and immunomodulatory activity in experimental systems. These activities motivate fermentation research but do not establish approved clinical use or make bioactivity part of the red-pigmented trait. (hamada2024characterizationofserratia pages 8-9)
5. **Stress physiology.** Carotenoids can protect against oxidative and radiation stress in taxa such as *Deinococcus*. Nevertheless, the causal direction “red pigmentation causes stress resistance” requires pigment-deficient mutants and rescue experiments in each taxon; review-level associations are insufficient. (wang2024insightsintothe pages 11-11, wang2024insightsintothe pages 10-11)

## 7. Recommended TraitMech graph structure

Use a **core phenotype node with multiple taxon-qualified mechanism branches**, rather than one universal pathway:

```text
Serratia branch:
pig operon → MAP branch ┐
                        ├─ PigC condensation → prodigiosin accumulation
pig operon → MBC branch ┘                         ↓
                                      red pigmented (METPO:1003028)

Regulatory inputs:
MetR ┤ pigP → pig operon
CpxR ┤ pig promoter
RcsB ┤ flhDC → prodigiosin synthesis
χ infection → pig-promoter-dependent transcription → prodigiosin
high temperature (strain/context qualified) ┤ prodigiosin synthesis

Separate carotenoid branches:
carotenogenic genes → specific red carotenoid → pigment accumulation
                                      ↓
                           red pigmented (METPO:1003028)
```

Every regulatory edge should carry `taxon`, `strain`, `medium`, `temperature`, and `assay` qualifiers where available. The phenotype edge should preferably distinguish **production**, **accumulation**, and **visible appearance**.

## 8. Claims that should not yet be curated

1. **Do not curate “all red-pigmented microbes produce prodigiosin.”** The phenotype is chemically heterogeneous.
2. **Do not assign the entire `pigA–pigN` operon outside verified prodiginine-producing taxa** merely from colony color.
3. **Do not curate χ phage as a universal inducer.** Evidence is for *S. marcescens* ATCC 274, requires active flagellar infection, and the inducing lysate component is unknown. (esteves2024serratiamarcescensatcc pages 1-2)
4. **Do not make CpxR, MetR, RcsB, PigP, PhoBR, RpoS, or quorum-sensing directionality species-wide.** The retrieved effects are strain- and condition-specific; some quorum-sensing effects conflict among strains. (esteves2024serratiamarcescensatcc pages 11-12)
5. **Do not state that RcsB directly binds the `pig` promoter.** EMSA evidence supports direct binding to `flhDC`; prodigiosin regulation is indirect. (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 46-48)
6. **Do not curate the pH-dependent pink/orange forms as red without the assay pH.** (hamada2024characterizationofserratia pages 8-9)
7. **Do not curate antimicrobial or anticancer activity as a consequence of the morphology trait.** Those are compound-specific experimental properties.
8. **Do not use review-only carotenoid associations as gene-to-red-phenotype edges.** Require direct pigment-deficient knockout, complementation, chemical identification, and visible-color evidence.
9. **Do not invent CURIEs.** Pig proteins and unusual intermediates should remain label-only until current UniProt, ChEBI, Rhea, KEGG, or MetaCyc records are verified.

## 9. DOI-first bibliography

1. Esteves NC, Scharf BE. “*Serratia marcescens* ATCC 274 increases production of the red pigment prodigiosin in response to Chi phage infection.” *Scientific Reports*. **July 2024**. DOI: [10.1038/s41598-024-68747-3](https://doi.org/10.1038/s41598-024-68747-3). (esteves2024serratiamarcescensatcc pages 1-2)
2. Lu Y, et al. “Prodigiosin: unveiling the crimson wonder—a comprehensive journey from diverse bioactivity to synthesis and yield enhancement.” *Frontiers in Microbiology*. **June 2024**. DOI: [10.3389/fmicb.2024.1412776](https://doi.org/10.3389/fmicb.2024.1412776).
3. Hamada MA, Mohamed ET. “Characterization of *Serratia marcescens* (OK482790)’ prodigiosin…” *BMC Microbiology*. **November 2024**. DOI: [10.1186/s12866-024-03634-5](https://doi.org/10.1186/s12866-024-03634-5). (hamada2024characterizationofserratia pages 8-9)
4. Wang Y, et al. “Insights into the synthesis, engineering, and functions of microbial pigments in *Deinococcus* bacteria.” *Frontiers in Microbiology*. **July 2024**. DOI: [10.3389/fmicb.2024.1447785](https://doi.org/10.3389/fmicb.2024.1447785). (wang2024insightsintothe pages 11-11, wang2024insightsintothe pages 10-11)
5. Anshi, Kapil S, Goswami L, Sharma V. “Unveiling the Intricacies of Microbial Pigments…” *Micro*. **October 2024**. DOI: [10.3390/micro4040038](https://doi.org/10.3390/micro4040038). (anshi2024unveilingtheintricacies pages 4-5)
6. Pan X, et al. “LysR-Type Transcriptional Regulator MetR Controls Prodigiosin Production…” *Applied and Environmental Microbiology*. **February 2020**. DOI: [10.1128/AEM.02241-19](https://doi.org/10.1128/AEM.02241-19). (pan2020lysrtypetranscriptionalregulator pages 1-2)
7. Sun Y, et al. “Improved Prodigiosin Production by Relieving CpxR Temperature-Sensitive Inhibition.” *Frontiers in Bioengineering and Biotechnology*. **June 2020**. DOI: [10.3389/fbioe.2020.00344](https://doi.org/10.3389/fbioe.2020.00344). (sun2020improvedprodigiosinproduction pages 1-2)
8. Pan X, et al. “Regulator RcsB Controls Prodigiosin Synthesis and Various Cellular Processes in *Serratia marcescens* JNB5-1.” *Applied and Environmental Microbiology*. **January 2021**. DOI: [10.1128/AEM.02052-20](https://doi.org/10.1128/AEM.02052-20). (pan2021regulatorrcsbcontrols pages 10-12, pan2021regulatorrcsbcontrols pages 46-48)
9. Williamson NR, Fineran PC, Leeper FJ, Salmond GPC. “The biosynthesis and regulation of bacterial prodiginines.” *Nature Reviews Microbiology*. **December 2006**. DOI: [10.1038/nrmicro1531](https://doi.org/10.1038/nrmicro1531). This is the supplied foundational evidence.
10. Slater H, et al. “Phosphate availability regulates biosynthesis of two antibiotics, prodigiosin and carbapenem…” *Molecular Microbiology*. **2003**. DOI: [10.1046/j.1365-2958.2003.03295.x](https://doi.org/10.1046/j.1365-2958.2003.03295.x).

## Curation priority

The immediate YAML expansion should preserve the existing prodiginine graph and add the well-supported **χ infection → pig-promoter transcription → prodigiosin → red phenotype**, **CpxR ┤ pig promoter**, **MetR ┤ PigP → pig operon**, and **RcsB ┤ FlhDC → prodigiosin** chains. Carotenoid mechanisms should be introduced as separate, pigment- and taxon-specific subgraphs only after direct knockout/complementation evidence is assembled.

References

1. (esteves2024serratiamarcescensatcc pages 1-2): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 7 citations and is from a peer-reviewed journal.

2. (hamada2024characterizationofserratia pages 8-9): Marwa A. Hamada and Eslam T. Mohamed. Characterization of serratia marcescens (ok482790)’ prodigiosin along with in vitro and in silico validation for its medicinal bioactivities. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03634-5, doi:10.1186/s12866-024-03634-5. This article has 17 citations and is from a peer-reviewed journal.

3. (sun2020improvedprodigiosinproduction pages 1-2): Yang Sun, Lijun Wang, Xuewei Pan, Tolbert Osire, Haitian Fang, Huiling Zhang, Shang-Tian Yang, Taowei Yang, and Zhiming Rao. Improved prodigiosin production by relieving cpxr temperature-sensitive inhibition. Frontiers in Bioengineering and Biotechnology, Jun 2020. URL: https://doi.org/10.3389/fbioe.2020.00344, doi:10.3389/fbioe.2020.00344. This article has 41 citations.

4. (pan2021regulatorrcsbcontrols pages 7-10): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 30 citations and is from a peer-reviewed journal.

5. (esteves2024serratiamarcescensatcc pages 11-12): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 7 citations and is from a peer-reviewed journal.

6. (pan2020lysrtypetranscriptionalregulator pages 1-2): Xuewei Pan, Changhao Sun, Mi Tang, Jiajia You, Tolbert Osire, Youxi Zhao, Meijuan Xu, Xian Zhang, Minglong Shao, Shangtian Yang, Taowei Yang, and Zhiming Rao. Lysr-type transcriptional regulator metr controls prodigiosin production, methionine biosynthesis, cell motility, h <sub>2</sub> o <sub>2</sub> tolerance, heat tolerance, and exopolysaccharide synthesis in serratia marcescens. Feb 2020. URL: https://doi.org/10.1128/aem.02241-19, doi:10.1128/aem.02241-19. This article has 49 citations and is from a peer-reviewed journal.

7. (pan2021regulatorrcsbcontrols pages 10-12): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 30 citations and is from a peer-reviewed journal.

8. (pan2021regulatorrcsbcontrols pages 46-48): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 30 citations and is from a peer-reviewed journal.

9. (pan2021regulatorrcsbcontrols pages 1-3): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 30 citations and is from a peer-reviewed journal.

10. (sun2020improvedprodigiosinproduction pages 2-3): Yang Sun, Lijun Wang, Xuewei Pan, Tolbert Osire, Haitian Fang, Huiling Zhang, Shang-Tian Yang, Taowei Yang, and Zhiming Rao. Improved prodigiosin production by relieving cpxr temperature-sensitive inhibition. Frontiers in Bioengineering and Biotechnology, Jun 2020. URL: https://doi.org/10.3389/fbioe.2020.00344, doi:10.3389/fbioe.2020.00344. This article has 41 citations.

11. (anshi2024unveilingtheintricacies pages 4-5): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 18 citations.

12. (wang2024insightsintothe pages 11-11): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

13. (wang2024insightsintothe pages 10-11): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.