---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:28:14.099162'
end_time: '2026-08-04T10:36:00.908807'
duration_seconds: 466.81
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
  causal_graph_summary: 'white_pigmented_low_chromophore: 11 nodes, 10 edges'
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
- **Trait label:** white pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 11 nodes, 10 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 11 nodes, 10 edges

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


# Curation report: white pigmented microbial trait

## 1. Scope and current interpretation

**Target:** `METPO:1003029` — **white pigmented**; category **MORPHOLOGY**; term kind **CLASS**; parent `METPO:1003021`; synonym **Pigment_white**.

This trait should represent an **assay-observed achromatic or very-low-chromophore appearance of microbial colonies or cells**. Mechanistically, it is an endpoint rather than a conserved pathway: white appearance can result from deletion or reduced expression of a pigment-biosynthetic module, impaired positive regulation, chemical inhibition, lack of an inducing condition, or an organism’s constitutively low pigment output.

The strongest operational graph is therefore:

> pigment-pathway impairment or non-induction → reduced visible pigment accumulation → white/nonpigmented appearance.

The literature supports this interpretation. In *Serratia marcescens*, spontaneous nonpigmented morphotypes retain the complete `pigA–N` cluster but markedly downregulate it, demonstrating that white appearance need not imply pathway deletion. A `slyA` deletion likewise produces a white colony and loss of prodigiosin synthesis (xiang2022transcriptomicanalysisreveals pages 1-2). In *Staphylococcus aureus*, disruption of `crtN` produces low/pale pigmentation, whereas `crtMN` complementation restores visibly gold colonies, directly connecting carotenoid-pathway activity to departure from the white state (campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 17-19).

### Boundary cases

1. **White versus nonpigmented.** These should be treated as equivalent only when white appearance is explicitly attributed to absent or low visible chromophore. White biomass caused by scattering, extracellular matrix, mineral precipitation, or an opaque medium is outside scope.
2. **Cream, beige, gray, translucent, or colorless.** These should not automatically map to `METPO:1003029`; curate only if the source equates them with white/nonpigmented or quantitatively establishes negligible pigment.
3. **Small-colony variants.** Colony size and pigmentation are independent axes. Some *S. aureus* small-colony variants lack staphyloxanthin, but “small colony” alone does not establish this trait (painter2015staphylococcusaureusadapts pages 20-23).
4. **Environmentally inducible pigmentation.** A colony may be white under one medium, temperature, illumination, oxygen level, or growth phase and pigmented under another. Assay conditions and observation time should therefore be represented in the graph or evidence annotation.
5. **Intrinsically white taxa versus white variants.** A constitutively unpigmented species-level phenotype and a white mutant of a normally colored strain share the observable endpoint but not necessarily the mechanism. Taxon and strain context are essential.
6. **Inverse evidence.** Experiments that restore or increase pigment—`crtMN` complementation, constitutive `pig` expression, phage induction, or pigment-enhancing medium—are valuable boundary evidence, but their direct endpoint is “not white.”

## 2. Candidate graph nodes

### Phenotypes and biological processes

- **white pigmented** — `METPO:1003029`
- visible pigment accumulation — label-only candidate
- reduced/absent visible chromophore accumulation — label-only candidate
- carotenoid biosynthetic process — `GO:0016117`
- staphyloxanthin biosynthesis — label-only candidate
- prodigiosin biosynthesis — label-only candidate
- oxidative-stress resistance — `GO:0006979` is a candidate for the broader response-to-oxidative-stress process; verify intended ontology granularity before curation
- neutrophil survival/opsonophagocytic-killing resistance — label-only candidates

### Genes, proteins, and regulatory modules

**In *S. aureus***

- `crtOPQMN` operon — label-only taxon-specific gene module
- `crtM`, dehydrosqualene synthase — label-only pending strain-specific UniProt/NCBI Gene grounding
- `crtN`, dehydrosqualene desaturase — label-only pending strain-specific grounding
- `crtMN` complementation construct — experimental-factor node
- `rsbU`, sigma-B regulatory phosphatase — label-only pending strain-specific grounding
- sigma factor B / SigB — protein/regulatory-factor node; use a strain-specific UniProt identifier only after selecting the reference strain
- `slyA` transcriptional regulator — label-only pending *S. marcescens* strain grounding

**In *S. marcescens***

- `pigA–N` prodigiosin-biosynthetic cluster — label-only gene-module node
- `pig` promoter — label-only regulatory-region node
- constitutive J23119 promoter replacement — experimental genetic construct
- `fliC`/flagellum-dependent χ-phage susceptibility — candidate contextual mechanism; not yet a direct white-trait edge

### Chemicals and metabolites

- staphyloxanthin — label-only candidate; do not assign an unverified ChEBI identifier
- prodigiosin — label-only candidate pending identifier verification
- farnesyl diphosphate — `CHEBI:37565`
- celastrol — label-only candidate pending identifier verification
- hydrogen peroxide — `CHEBI:16240`
- reactive oxygen species — `CHEBI:26523`

### Environmental and experimental factors

- agar growth medium — label-only experimental factor
- tryptic soy agar (TSA) — label-only medium
- nutrient agar — label-only medium
- milk agar — label-only medium
- beetroot agar — study-specific medium
- carrot agar — study-specific medium
- incubation time — experimental factor
- incubation at 37°C — experimental condition
- bacteriophage χ infection — biological/experimental factor; phage taxon grounding should be verified separately
- spontaneous serial passage — experimental/evolutionary factor

### Taxa

- *Staphylococcus aureus* — `NCBITaxon:1280`
- *Serratia marcescens* — `NCBITaxon:615`

Strain nodes such as *S. aureus* JE2, SA925, SA1088, and *S. marcescens* ATCC 274 should be grounded only after confirming stable strain-level taxonomy or culture-collection identifiers.

## 3. Candidate causal edges

The following compact table gives the strongest graph-ready relationships.

| subject | predicate | object | organism/context | evidence strength | DOI |
|---|---|---|---|---|---|
| crtN disruption | reduces | staphyloxanthin production | *Staphylococcus aureus* JE2 `crtN::Tn`; pale/low-pigment phenotype relative to gold parent (campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 17-19) | strong, direct genetic intervention | 10.1016/j.celrep.2023.113281 |
| crtMN complementation | restores | gold staphyloxanthin pigmentation | *S. aureus* JE2 `crtN::Tn` complemented with inducible `crtMN`; gold colonies on TSA (campbell2023variablestaphyloxanthinproduction pages 17-19) | strong, direct complementation | 10.1016/j.celrep.2023.113281 |
| RsbU / sigma-B signaling | activates | crt biosynthetic operon / staphyloxanthin production | *S. aureus* clinical isolates; low-pigment phenotype linked to `rsbU` SNP; regulatory direction supported but SNP-specific causality remains uncertain (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 38-41) | moderate; direct for sigma-B pathway direction, uncertain for SNP-specific edge | 10.1016/j.celrep.2023.113281 |
| SlyA deletion | downregulates | pigA-N operon expression | *Serratia marcescens* Δ`slyA` mutant; prodigiosin-loss program (xiang2022transcriptomicanalysisreveals pages 1-2) | strong, direct genetic intervention | 10.3389/fmicb.2021.793202 |
| SlyA deletion | causes | white/non-pigmented colony phenotype | *S. marcescens* Δ`slyA` mutant reported as white colony (xiang2022transcriptomicanalysisreveals pages 1-2) | strong, direct genetic intervention | 10.3389/fmicb.2021.793202 |
| pigA-N downregulation | reduces | prodigiosin biosynthesis | spontaneous non-pigmented *S. marcescens* morphotypes with intact pig cluster but lowered pig transcription (xiang2022transcriptomicanalysisreveals pages 1-2) | strong, transcriptome-supported association | 10.3389/fmicb.2021.793202 |
| Chi phage infection | increases | prodigiosin production (>5-fold) | *S. marcescens* ATCC 274; inverse boundary evidence showing movement away from white/nonpigmented state (esteves2024serratiamarcescensatcc pages 8-9) | strong, direct perturbation | 10.1038/s41598-024-68747-3 |
| constitutive pig promoter replacement | increases | prodigiosin production | *S. marcescens* `pigq` strain with strong constitutive promoter at pig operon; inverse boundary evidence (esteves2024serratiamarcescensatcc pages 8-9) | strong, direct promoter engineering | 10.1038/s41598-024-68747-3 |
| beetroot agar | increases | staphyloxanthin production versus nutrient agar | *S. aureus* on assay media; absorbance ~0.46 at 460 nm on beetroot agar vs ~0.13 on nutrient agar; assay-specific inverse boundary evidence (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) | moderate, assay-specific environmental effect | 10.7759/cureus.59892 |


*Table: This table lists the strongest graph-ready causal edges relevant to the microbial white-pigmented trait, emphasizing direct genetic and environmental evidence and marking uncertain regulatory associations. It is useful as a compact starting point for TraitMech curation of METPO:1003029.*

A more detailed evidence interpretation follows.

| Proposed subject–predicate–object triple | Supporting snippet | Evidence and curation note |
|---|---|---|
| `crtN disruption` **decreases** `staphyloxanthin accumulation` | “crtN transposon mutant … shows reduced staphyloxanthin” | Direct genetic intervention in *S. aureus* JE2. Strong and curatable as a taxon/strain-specific molecular edge. DOI: [10.1016/j.celrep.2023.113281](https://doi.org/10.1016/j.celrep.2023.113281) (published October 2023) (campbell2023variablestaphyloxanthinproduction pages 30-38). |
| `crtN disruption` **promotes** `pale/low-pigment colony appearance` | The mutant was pale relative to the gold complemented strain on TSA | Direct phenotype evidence, but the paper’s evidence summary says “pale,” not unequivocally “white.” Curate to the white trait only with an uncertainty qualifier or after checking the original image/legend (campbell2023variablestaphyloxanthinproduction pages 17-19). |
| `crtMN complementation` **increases** `staphyloxanthin accumulation` | “Complementation restored staphyloxanthin production” | Direct rescue experiment. Strong inverse evidence for the white phenotype (campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 17-19). |
| `crtMN complementation` **causes** `gold colony appearance` | “visible as gold coloration in colonies on TSA … compared to pale control colonies” | Direct visual rescue on a defined medium; useful as evidence that low CrtMN activity lies upstream of pale/white appearance (campbell2023variablestaphyloxanthinproduction pages 17-19). |
| `RsbU` **positively regulates** `sigma-B activity` | “RsbU phosphatase positively regulates sigma B” | Mechanistically supported regulatory edge in *S. aureus* (campbell2023variablestaphyloxanthinproduction pages 8-10). |
| `sigma-B` **activates** `crt biosynthetic operon` | sigma B “directly activates the crt biosynthetic operon” | Curatable positive-regulation edge upstream of pigment accumulation (campbell2023variablestaphyloxanthinproduction pages 8-10). |
| `rsbU Met→Leu variant` **associated with decreased** `staphyloxanthin production` | The SNP was “consistently present in low-staphyloxanthin isolates” and affects the catalytic phosphatase domain | Clinical-isolate association, not a clean allele-replacement experiment. Mark **uncertain** and do not encode as proven causation (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 38-41). |
| `SlyA deletion` **decreases** `pigA–N transcription` | “Most of the pig genes are significantly downregulated”; deletion of `slyA` generated a nonpigmented mutant | Direct deletion plus transcriptomic evidence in *S. marcescens*. Curatable and taxon specific (xiang2022transcriptomicanalysisreveals pages 1-2). |
| `SlyA deletion` **decreases** `prodigiosin biosynthesis` | “The ΔslyA strain loses prodigiosin synthesis capacity” | Strong direct genetic evidence (xiang2022transcriptomicanalysisreveals pages 1-2). |
| `SlyA deletion` **causes** `white colony appearance` | “The ΔslyA mutant showed a white colony” | This is the cleanest direct edge to `METPO:1003029` among the retrieved studies (xiang2022transcriptomicanalysisreveals pages 1-2). |
| `pigA–N transcriptional downregulation` **decreases** `prodigiosin accumulation` | The intact cluster was “dramatically” downregulated, “directly lead[ing] to prodigiosin dyssynthesis” | Strong transcriptome/phenotype evidence. Because multiple upstream changes occurred in spontaneous variants, retain an evidence note rather than asserting a single initiating cause (xiang2022transcriptomicanalysisreveals pages 1-2). |
| `repeated passage` **selects for** `nonpigmented S. marcescens variants` | Mutants arose within “about five passages” and replaced wild type by “about 24 passages” | Quantitative evolutionary/experimental edge. Selection is supported by competitive replacement, although the initiating mutations/regulatory states remain unresolved (xiang2022transcriptomicanalysisreveals pages 1-2). |
| `χ-phage infection` **increases** `prodigiosin production` | “increases pigment production by more than five-fold” | Direct 2024 perturbation evidence in ATCC 274. This moves cells away from the white state and should be encoded as inverse/boundary evidence rather than as a cause of white pigmentation. DOI: [10.1038/s41598-024-68747-3](https://doi.org/10.1038/s41598-024-68747-3) (published July 2024) (esteves2024serratiamarcescensatcc pages 8-9). |
| `constitutive pig promoter replacement` **increases** `prodigiosin production` | A strong constitutive J23119 promoter “significantly overproduces pigment” | Direct promoter-engineering evidence. Strong inverse edge; the native phage-responsive regulator remains unresolved (esteves2024serratiamarcescensatcc pages 8-9). |
| `beetroot agar` **increases** `staphyloxanthin signal relative to nutrient agar` | Absorbance was 0.46 at 460 nm versus 0.13 on nutrient agar | Direct medium comparison but assay-specific and potentially confounded by plant-derived pigments or extraction background. Do not make it a core white-trait mechanism without controls. DOI: [10.7759/cureus.59892](https://doi.org/10.7759/cureus.59892) (published May 2024) (nirmala2024enhancingstaphyloxanthinsynthesis pages 2-5, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11). |
| `incubation time` **positively correlates with** `measured pigment concentration` | “r=0.93, p<0.01” | Correlation from the 2024 agar study; useful for assay metadata, not a universal causal edge (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11). |

## 4. Recommended minimal TraitMech graph

A conservative cross-study graph should center on a generic low-chromophore module and attach taxon-specific branches:

### *S. aureus* branch

1. `RsbU` → **positively_regulates** → `sigma-B`
2. `sigma-B` → **positively_regulates** → `crtOPQMN expression`
3. `crtM/crtN activity` → **increases** → `staphyloxanthin biosynthesis`
4. `staphyloxanthin accumulation` → **increases** → `gold/yellow visible pigmentation`
5. `reduced staphyloxanthin accumulation` → **promotes** → `pale/white appearance`

Edges 1–4 have direct or strong mechanistic support. Edge 5 is biologically coherent but should remain qualified as **pale/white**, because the recent study’s rescue comparison explicitly describes pale controls rather than an ontology-scored white endpoint (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 17-19).

### *S. marcescens* branch

1. `SlyA` → **positively_regulates** → `pigA–N transcription`
2. `pigA–N expression` → **increases** → `prodigiosin biosynthesis`
3. `reduced prodigiosin accumulation` → **causes** → `white/nonpigmented colony appearance`

This branch is the strongest candidate for immediate curation because `slyA` deletion, loss of prodigiosin, and white colonies are linked by direct intervention evidence (xiang2022transcriptomicanalysisreveals pages 1-2).

## 5. Recent developments, applications, and relevant statistics

### Clinical and pathogenesis relevance

The 2023 *Cell Reports* study shows that pigment output is not merely taxonomic decoration. High-staphyloxanthin *S. aureus* strains survived significantly better in human neutrophils than low producers or a `crtN` mutant, with reported comparisons of **p=0.0358** and **p=0.0103**. A high-producing clinical strain also induced greater neutrophil infiltration than a low producer in an ear-wound model (**p=10⁻⁴**). The study analyzed longitudinal healing associations across **84 healed and 82 unhealed patient/timepoint combinations**. These results support staphyloxanthin as a mechanistic virulence and wound-outcome trait, while showing that low/white pigmentation may predict altered oxidative-stress resistance rather than simply species identity (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 38-41, campbell2023variablestaphyloxanthinproduction pages 1-3).

### Evolutionary switching and resource allocation

Nonpigmented *S. marcescens* variants appeared after approximately **five serial passages** and replaced pigmented parents by approximately **24 passages**. Their `pigA–N` genes remained present but were transcriptionally suppressed; amino-acid degradation and transport pathways increased while several costly systems decreased. This supports an expert interpretation of white pigmentation as a possible **resource-allocation state** rather than necessarily a biosynthetic lesion. However, the same study found increased cell density and enhanced insect-pathogen virulence in the `slyA` mutant, warning against interpreting loss of pigment as universal attenuation (xiang2022transcriptomicanalysisreveals pages 1-2).

### Phage-responsive pigment production

In 2024, χ-phage infection was shown to increase prodigiosin by **more than fivefold**. The broader study also found that infected-cell lysate increased `pig`-operon transcription approximately **threefold**, while replacement of the native promoter by a constitutive promoter removed the inducible pigmentation response. These results implicate promoter-level stress signaling and provide a practical route for increasing industrial prodigiosin yield, although the responsible signal and regulator remain unresolved (esteves2024serratiamarcescensatcc pages 8-9).

### Media optimization

A 2024 study reported staphyloxanthin-associated absorbance of **0.46 at 460 nm** on beetroot agar versus **0.13** on nutrient agar and a time–pigment correlation of **r=0.93, p<0.01**. Proposed formulations used 10 g beetroot powder/100 mL, 10 g carrot powder/100 mL, or 5 g of each in a basal agar, incubated at 37°C for 24–48 h (nirmala2024enhancingstaphyloxanthinsynthesis pages 2-5, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11). This is potentially useful for pigment screening or production, but its evidentiary weight is below that of genetic rescue because colored plant ingredients can complicate pigment-specific spectrophotometry.

### Antivirulence applications

Staphyloxanthin enzymes are candidate antivirulence targets. Celastrol treatment reduced staphyloxanthin, with LC–MS and intermediate measurements implicating CrtM inhibition and accumulation of its substrate farnesyl diphosphate. Treated cells became more sensitive to environmental stress, blood killing, and membrane-targeting antibiotics. This is useful as a candidate `celastrol inhibits CrtM → reduced staphyloxanthin` branch, but the retrieved evidence did not explicitly score colonies as white; it should not yet terminate directly at `METPO:1003029` without confirming the original phenotype data. DOI: [10.1186/s12866-022-02515-z](https://doi.org/10.1186/s12866-022-02515-z) (published April 2022).

## 6. Curation warnings

1. **Do not create a universal “white pigment” molecule.** The phenotype denotes low visible pigment, not accumulation of a white chromophore.
2. **Do not merge staphyloxanthin and prodigiosin pathways.** They are independent taxon-specific mechanisms converging on the same visual endpoint.
3. **Do not infer gene deletion from white appearance.** The complete `pigA–N` cluster was preserved in spontaneous white *S. marcescens* variants (xiang2022transcriptomicanalysisreveals pages 1-2).
4. **Do not curate the `rsbU` Met→Leu allele as causal yet.** It is a compelling clinical-isolate association but lacks allele-swap validation in the retrieved evidence (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 38-41).
5. **Do not equate all `crtN` mutants with unequivocally white colonies.** The recent source supports reduced/pale pigmentation and gold rescue; curate the direct white endpoint as uncertain unless the primary figure or explicit text confirms white (campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 17-19).
6. **Keep enhanced-pigment experiments as inverse edges.** χ phage, constitutive `pig` expression, `crtMN` complementation, and pigment-enhancing media explain escape from the white state, not its production (campbell2023variablestaphyloxanthinproduction pages 17-19, esteves2024serratiamarcescensatcc pages 8-9, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11).
7. **Treat media findings as assay specific.** Beetroot/carrot ingredients may affect extraction or absorbance; they should not become universal environmental mechanisms without pigment-specific chemical validation.
8. **Do not infer reduced virulence from low pigment across taxa or strains.** The *S. marcescens* `slyA` mutant had enhanced entomopathogenic virulence, while staphyloxanthin increased selected *S. aureus* wound and immune-survival phenotypes (xiang2022transcriptomicanalysisreveals pages 1-2, campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 1-3).
9. **Ground genes and proteins by strain.** Avoid assigning a single UniProt identifier to `crtM`, `crtN`, `slyA`, or SigB until the YAML specifies the organism and reference strain.
10. **The supplied DOI 10.2147/IDR.S49039 should be retained as existing evidence but rechecked manually.** It was not recovered as full-text evidence in this search, so its exact organism, variant, and inducibility wording were not independently validated here.

## 7. DOI-first bibliography

1. Campbell AE et al. **Variable staphyloxanthin production by *Staphylococcus aureus* drives strain-dependent effects on diabetic wound-healing outcomes.** *Cell Reports* 42, 113281. Published October 2023. DOI: [10.1016/j.celrep.2023.113281](https://doi.org/10.1016/j.celrep.2023.113281) (campbell2023variablestaphyloxanthinproduction pages 8-10, campbell2023variablestaphyloxanthinproduction pages 38-41, campbell2023variablestaphyloxanthinproduction pages 30-38, campbell2023variablestaphyloxanthinproduction pages 1-3, campbell2023variablestaphyloxanthinproduction pages 17-19).
2. Esteves NC, Scharf BE. ***Serratia marcescens* ATCC 274 increases production of the red pigment prodigiosin in response to Chi phage infection.** *Scientific Reports* 14. Published July 2024. DOI: [10.1038/s41598-024-68747-3](https://doi.org/10.1038/s41598-024-68747-3) (esteves2024serratiamarcescensatcc pages 8-9).
3. Nirmala B et al. **Enhancing Staphyloxanthin Synthesis in *Staphylococcus aureus* Using Innovative Agar Media Formulations.** *Cureus* 16. Published May 2024. DOI: [10.7759/cureus.59892](https://doi.org/10.7759/cureus.59892) (nirmala2024enhancingstaphyloxanthinsynthesis pages 2-5, nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11).
4. Xiang T et al. **Transcriptomic Analysis Reveals Competitive Growth Advantage of Non-pigmented *Serratia marcescens* Mutants.** *Frontiers in Microbiology* 12. Published January 2022. DOI: [10.3389/fmicb.2021.793202](https://doi.org/10.3389/fmicb.2021.793202) (xiang2022transcriptomicanalysisreveals pages 1-2).
5. Yehia FAA et al. **Celastrol mitigates staphyloxanthin biosynthesis and biofilm formation in *Staphylococcus aureus* via targeting key regulators of virulence.** *BMC Microbiology* 22. Published April 2022. DOI: [10.1186/s12866-022-02515-z](https://doi.org/10.1186/s12866-022-02515-z).
6. Painter KL et al. ***Staphylococcus aureus* adapts to oxidative stress by producing H₂O₂-resistant small-colony variants via the SOS response.** *Infection and Immunity* 83:1830–1844. Published May 2015. DOI: [10.1128/IAI.03016-14](https://doi.org/10.1128/IAI.03016-14) (painter2015staphylococcusaureusadapts pages 20-23).

**Curation priority:** immediately curate the *S. marcescens* `SlyA → pigA–N transcription → prodigiosin → white/nonpigmented colony` branch and the *S. aureus* `CrtN/CrtMN → staphyloxanthin → pale-versus-gold appearance` branch. Retain RsbU alleles, colored-media effects, celastrol-to-white appearance, and generalized virulence consequences as uncertain or contextual extensions.

References

1. (xiang2022transcriptomicanalysisreveals pages 1-2): Tingting Xiang, Wei Zhou, Cailing Xu, Jing Xu, Rui Liu, Nuo Wang, Liang Xu, Yu Zhao, Minhui Luo, Xiaoxin Mo, Zeyang Mao, and Yongji Wan. Transcriptomic analysis reveals competitive growth advantage of non-pigmented serratia marcescens mutants. Frontiers in Microbiology, Jan 2022. URL: https://doi.org/10.3389/fmicb.2021.793202, doi:10.3389/fmicb.2021.793202. This article has 12 citations and is from a peer-reviewed journal.

2. (campbell2023variablestaphyloxanthinproduction pages 30-38): Amy E. Campbell, Amelia R. McCready-Vangi, Aayushi Uberoi, Sofía M. Murga-Garrido, Victoria M. Lovins, Ellen K. White, Jamie Ting-Chun Pan, Simon A.B. Knight, Alexis R. Morgenstern, Colleen Bianco, Paul J. Planet, Sue E. Gardner, and Elizabeth A. Grice. Variable staphyloxanthin production by staphylococcus aureus drives strain-dependent effects on diabetic wound-healing outcomes. Cell Reports, 42:113281, Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113281, doi:10.1016/j.celrep.2023.113281. This article has 53 citations and is from a highest quality peer-reviewed journal.

3. (campbell2023variablestaphyloxanthinproduction pages 17-19): Amy E. Campbell, Amelia R. McCready-Vangi, Aayushi Uberoi, Sofía M. Murga-Garrido, Victoria M. Lovins, Ellen K. White, Jamie Ting-Chun Pan, Simon A.B. Knight, Alexis R. Morgenstern, Colleen Bianco, Paul J. Planet, Sue E. Gardner, and Elizabeth A. Grice. Variable staphyloxanthin production by staphylococcus aureus drives strain-dependent effects on diabetic wound-healing outcomes. Cell Reports, 42:113281, Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113281, doi:10.1016/j.celrep.2023.113281. This article has 53 citations and is from a highest quality peer-reviewed journal.

4. (painter2015staphylococcusaureusadapts pages 20-23): Kimberley L. Painter, Elizabeth Strange, Julian Parkhill, Kathleen B. Bamford, Darius Armstrong-James, and Andrew M. Edwards. Staphylococcus aureus adapts to oxidative stress by producing h <sub>2</sub> o <sub>2</sub> -resistant small-colony variants via the sos response. Infection and Immunity, 83:1830-1844, May 2015. URL: https://doi.org/10.1128/iai.03016-14, doi:10.1128/iai.03016-14. This article has 190 citations and is from a peer-reviewed journal.

5. (campbell2023variablestaphyloxanthinproduction pages 8-10): Amy E. Campbell, Amelia R. McCready-Vangi, Aayushi Uberoi, Sofía M. Murga-Garrido, Victoria M. Lovins, Ellen K. White, Jamie Ting-Chun Pan, Simon A.B. Knight, Alexis R. Morgenstern, Colleen Bianco, Paul J. Planet, Sue E. Gardner, and Elizabeth A. Grice. Variable staphyloxanthin production by staphylococcus aureus drives strain-dependent effects on diabetic wound-healing outcomes. Cell Reports, 42:113281, Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113281, doi:10.1016/j.celrep.2023.113281. This article has 53 citations and is from a highest quality peer-reviewed journal.

6. (campbell2023variablestaphyloxanthinproduction pages 38-41): Amy E. Campbell, Amelia R. McCready-Vangi, Aayushi Uberoi, Sofía M. Murga-Garrido, Victoria M. Lovins, Ellen K. White, Jamie Ting-Chun Pan, Simon A.B. Knight, Alexis R. Morgenstern, Colleen Bianco, Paul J. Planet, Sue E. Gardner, and Elizabeth A. Grice. Variable staphyloxanthin production by staphylococcus aureus drives strain-dependent effects on diabetic wound-healing outcomes. Cell Reports, 42:113281, Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113281, doi:10.1016/j.celrep.2023.113281. This article has 53 citations and is from a highest quality peer-reviewed journal.

7. (esteves2024serratiamarcescensatcc pages 8-9): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 7 citations and is from a peer-reviewed journal.

8. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 6 citations.

9. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 6 citations.

10. (nirmala2024enhancingstaphyloxanthinsynthesis pages 2-5): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 6 citations.

11. (campbell2023variablestaphyloxanthinproduction pages 1-3): Amy E. Campbell, Amelia R. McCready-Vangi, Aayushi Uberoi, Sofía M. Murga-Garrido, Victoria M. Lovins, Ellen K. White, Jamie Ting-Chun Pan, Simon A.B. Knight, Alexis R. Morgenstern, Colleen Bianco, Paul J. Planet, Sue E. Gardner, and Elizabeth A. Grice. Variable staphyloxanthin production by staphylococcus aureus drives strain-dependent effects on diabetic wound-healing outcomes. Cell Reports, 42:113281, Oct 2023. URL: https://doi.org/10.1016/j.celrep.2023.113281, doi:10.1016/j.celrep.2023.113281. This article has 53 citations and is from a highest quality peer-reviewed journal.