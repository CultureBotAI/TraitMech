---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:24:07.988193'
end_time: '2026-08-04T09:32:19.830564'
duration_seconds: 491.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: peritrichous
  trait_identifier: traitmech:000060
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: peritrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with flagella distributed over the entire cell
    surface rather than localized to the poles.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous
    (surface-distributed) flagellation as one of the conserved flagellation patterns.)
    | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar
    filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)'
  causal_graph_summary: 'peritrichous_surface_distributed_flagella: 10 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** peritrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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
- **Trait label:** peritrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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


# Curation report: peritrichous flagellation

## Trait record and scope

- **Trait:** peritrichous
- **Identifier:** `traitmech:000060`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000056`
- **Operational definition:** a cell-level flagellation pattern in which multiple external flagella are distributed over the cell body rather than restricted to one or both poles.

The best-supported exemplars are *Escherichia coli* and *Bacillus subtilis*. A major review describes these organisms as having approximately **5–6 flagella**, while emphasizing that number varies with growth conditions and cell-cycle state. The pattern is reproduced across division, although *E. coli* flagella are not perfectly uniform: they are uncommon at the extreme poles and may be denser toward the old-pole region. Thus, “surface-distributed” should not be interpreted as mathematically uniform or completely random. (schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 2-4)

### Boundary cases

The trait should be distinguished from:

1. **Monotrichous or lophotrichous polar flagellation:** one flagellum or a tuft confined to one pole.
2. **Amphitrichous flagellation:** flagella at both poles.
3. **Periplasmic/endoflagella:** filaments lying between membranes, as in spirochetes; these are not surface-distributed exoflagella.
4. **Inducible lateral flagella:** a second, environmentally regulated flagellar system on the lateral surface in organisms that otherwise carry polar flagella. This is not necessarily constitutive peritrichy.
5. **Hyperflagellation:** increased filament number does not establish peritrichy unless microscopy demonstrates nonpolar surface distribution.
6. **Motility or flagellar-gene presence:** neither swimming nor possession of `fliC` or other assembly genes establishes the spatial morphology.
7. **Aflagellate/nonmotile assay states:** expression is environmentally variable, so absence under one culture condition does not necessarily contradict a species-level capacity for peritrichous flagellation.

Flagellation patterns are species-associated morphologies important for motility, biofilm formation, and pathogenicity, but their underlying placement systems are evolutionarily diverse. Consequently, the graph should not imply that one universal molecular pathway causes all peritrichous patterns. (schuhmacher2015howbacteriamaintain pages 1-2)

## Current mechanistic understanding

The classical *E. coli* model proposed that surface-distributed basal bodies arise largely by stochastic nucleation or “diffusion and capture,” rather than recruitment to a dedicated polar landmark. Nevertheless, inherited asymmetry and old-pole enrichment show that placement is not simply uniform random sampling. As of the major 2015 synthesis, the mechanisms setting flagellar position and number in *E. coli* and *Salmonella* remained poorly understood. (schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 2-4)

A major advance appeared after the requested 2023–2024 priority window. Dunn et al. reported in 2025 that nascent *B. subtilis* basal bodies are initially mobile and become immobilized when the flagellar rod assembles through the peptidoglycan. Rod defects increased basal-body mobility, randomized the pattern, and increased polar basal bodies. The authors infer that rod polymerization probes a pre-existing, grid-like organization of sufficiently large peptidoglycan pores. This provides direct support for a physical diffusion-and-capture mechanism in one peritrichous species, but it should not yet be generalized to Enterobacteriaceae. (dunn2025nascentflagellarbasal pages 1-2, dunn2025nascentflagellarbasal pages 17-18)

Recent 2023–2024 FlhF/FlhG studies largely concern polar flagellates. They strengthen the contrast between landmark-mediated polar confinement and distributed assembly but are not direct evidence that those polar mechanisms generate peritrichy. The appropriate expert interpretation is therefore modular: conserved flagellar assembly produces each organelle, whereas separate, taxon-dependent placement and number-control processes generate the peritrichous pattern. (schuhmacher2015howbacteriamaintain pages 9-10, schuhmacher2015howbacteriamaintain pages 1-2)

## Candidate nodes grouped by type

### Phenotypes and processes

- `traitmech:000060` — peritrichous flagellation
- surface-distributed flagellar pattern
- flagellar number control
- flagellar spatial patterning
- basal-body nucleation
- basal-body diffusion and capture
- basal-body immobilization
- flagellar rod polymerization
- bacterial swimming
- chemotaxis
- swarming motility
- initial surface colonization
- biofilm formation

### Cellular structures and localizations

- bacterial-type flagellum
- flagellar basal body
- MS ring
- C ring/switch complex
- flagellar rod
- flagellar hook
- flagellar filament
- cell body surface
- cytoplasmic membrane
- peptidoglycan layer
- peptidoglycan pore/grid organization
- old-pole region
- cell pole

### Genes and proteins

These are useful candidate nodes, but most are **generic assembly machinery rather than demonstrated determinants of peritrichous placement**:

- **FliF** — MS-ring protein
- **FliG, FliM, FliN/FliY** — C-ring components; FliM fusions are also experimental basal-body markers
- flagellar rod proteins — species-specific names should be represented individually only where direct mutant evidence is available
- **FlhF** — SRP-family GTPase implicated in placement; its role is strongly taxon-dependent
- **FlhG/FleN** — MinD/ParA-family ATPase implicated in number and placement control; most direct literature concerns polar systems
- **FlhDC**, **FliA/σ28**, **FlgM** — transcriptional hierarchy candidates in enterobacteria
- **FliC/Hag** — flagellin/filament subunit
- **MotA/MotB** — stator proteins required for rotation
- flagellar type III secretion/export apparatus

For `FlhDC → flagellar transcription`, `FliA → late flagellar genes`, `FliF → MS-ring formation`, and `MotAB → rotation`, the relationships are biologically established but should enter this particular graph only as generic organelle-assembly or downstream-function branches with direct references attached. They should not be annotated as causing the *spatial distribution* without placement-specific experiments.

### Environmental and experimental factors

- surface contact
- growth medium and nutrient state
- cell-cycle stage and replicative age
- microscopy/flagellar staining
- fluorescent FliM basal-body tracking
- rod-gene mutation or depletion
- `flhF`/`flhG` mutation
- swimming-agar and swarming assays

### Chemicals and physical factors

- peptidoglycan
- proton motive force, as a generic driver of many flagellar motors
- attractants and repellents, as inputs to chemotaxis

No specific nutrient, inhibitor, electron donor, or electron acceptor currently has sufficient evidence to be represented as a general cause of peritrichous morphology.

## Candidate causal edges

The compact evidence table below separates curation-ready observations from hypotheses and taxon-specific relations.

| candidate subject | predicate | object | taxon/scope | evidence strength | DOI/year | short supporting snippet | curation decision |
|---|---|---|---|---|---|---|---|
| peritrichous flagellation | has_participant_distribution | surface-distributed flagella over cell body; typically 5–6 flagella | *Escherichia coli*, *Bacillus subtilis*; trait-level scope from review | Moderate (review synthesis) | 10.1093/femsre/fuv034 (2015) | “peritrichous (flagellar filaments distributed over the cell body), e.g. *Escherichia coli* and *Bacillus subtilis* (5–6 flagella)” (schuhmacher2015howbacteriamaintain pages 2-4) | Curate as core phenotype definition |
| stochastic basal-body placement / diffusion-and-capture model | may_cause | peritrichous surface distribution of flagella | Mainly *E. coli* / enteric peritrichous systems; inferred model | Weak–moderate, uncertain | 10.1093/femsre/fuv034 (2015) | “peritrichous flagellation may arise through stochastic self-assembly via ‘diffusion and capture’ mechanisms rather than specific landmark proteins” (schuhmacher2015howbacteriamaintain pages 2-4) | Curate only as uncertain/mechanistic hypothesis |
| ancestor flagellar localization / old-pole bias | influences_distribution_of | asymmetric peritrichous flagella with higher density near old pole | *E. coli*; taxon-specific | Weak–moderate, taxon-specific | 10.1093/femsre/fuv034 (2015) | “Flagellar number distribution is asymmetric, with higher density at the ‘old’ cell pole post-division” (schuhmacher2015howbacteriamaintain pages 4-5) | Keep as taxon-specific, uncertain; not trait-general |
| nascent basal bodies | is_initially | mobile | *Bacillus subtilis* peritrichous patterning; taxon-specific | Strong for taxon, but newer than priority window | 10.1128/mbio.00530-25 (2025) | “B. subtilis basal bodies are mobile soon after assembly” (dunn2025nascentflagellarbasal pages 1-2) | Curate as taxon-specific newer evidence |
| rod assembly / rod polymerization | immobilizes | nascent flagellar basal bodies | *Bacillus subtilis* peritrichous patterning; taxon-specific | Strong for taxon, but newer than priority window | 10.1128/mbio.00530-25 (2025) | “nascent flagellar basal bodies are immobilized by rod assembly” (dunn2025nascentflagellarbasal pages 1-2) | Curate as taxon-specific mechanistic edge |
| rod synthesis | probes/interprets | peptidoglycan pore grid | *Bacillus subtilis* peritrichous patterning; taxon-specific | Moderate–strong, mechanistic inference, newer than priority window | 10.1128/mbio.00530-25 (2025) | “rod polymerization probes the PG superstructure for pores of sufficient diameter” and coordinates with “a pre-existent grid-like pore pattern in peptidoglycan” (dunn2025nascentflagellarbasal pages 1-2) | Curate as taxon-specific, note inferred physical mechanism |
| rod mutation | disrupts_patterning_of | basal body distribution, causing more-random and polar phenotypes | *Bacillus subtilis* peritrichous patterning; taxon-specific | Strong for taxon, newer than priority window | 10.1128/mbio.00530-25 (2025) | “defects in the flagellar rod lead to a more-random distribution of flagella and an increase in polar basal bodies” (dunn2025nascentflagellarbasal pages 1-2) | Curate as taxon-specific causal edge |
| rod mutation phenotype | phenocopies | FlhF patterning defect | *Bacillus subtilis* peritrichous patterning; taxon-specific | Moderate–strong, newer than priority window | 10.1128/mbio.00530-25 (2025) | “mutation of the rod disrupts basal body patterning in a way that phenocopies mutation of the cytoplasmic flagellar patterning protein FlhF” (dunn2025nascentflagellarbasal pages 1-2) | Curate as taxon-specific relation; avoid overgeneralization to all peritrichous taxa |
| surface contact | increases | flagellar number | *E. coli*; assay/environment-specific | Moderate (review synthesis) | 10.1093/femsre/fuv034 (2015) | “Flagellar number varies with environmental conditions and cell cycle phase, increasing upon surface contact in E. coli to facilitate swarming” (schuhmacher2015howbacteriamaintain pages 2-4) | Curate as environmental modulation, taxon/assay-specific |
| surface contact | does_not_increase | flagellar number | *Salmonella*; assay/environment-specific contrast | Moderate (review synthesis) | 10.1093/femsre/fuv034 (2015) | “increasing upon surface contact in E. coli to facilitate swarming, though not in Salmonella” (schuhmacher2015howbacteriamaintain pages 2-4) | Curate only as comparative taxon-specific contrast |
| peritrichous patterning mechanism | remains_poorly_understood_in | *E. coli* and *Salmonella* | Enteric peritrichous systems | Strong as cautionary summary | 10.1093/femsre/fuv034 (2015) | “despite decades of study, little is known about how flagella place and number are established in E. coli and Salmonella” (schuhmacher2015howbacteriamaintain pages 2-4) | Add warning; avoid unsupported universal graph edges |


*Table: This table summarizes only the evidence actually gathered for traitmech:000060, separating core phenotype definition from taxon-specific or uncertain mechanisms. It is useful for deciding which edges are safe to curate now versus which should remain provisional, especially the newer 2025 Bacillus subtilis mechanism.*

### Recommended core graph

The safest initial graph is deliberately small:

1. **peritrichous flagellation — has part — multiple external flagella**
2. **multiple external flagella — spatially distributed over — cell body surface**
3. **surface-distributed flagellar pattern — contrasts with — polar flagellar localization**
4. ***B. subtilis* nascent basal body — initially has state — mobile basal body** `[taxon-specific]`
5. ***B. subtilis* flagellar rod assembly — immobilizes — nascent basal body** `[taxon-specific; direct 2025 evidence]`
6. ***B. subtilis* flagellar rod — probes/interacts with — peptidoglycan pore organization** `[taxon-specific; mechanistic inference]`
7. **basal-body immobilization at distributed peptidoglycan sites — contributes to — peritrichous pattern** `[taxon-specific; inferred synthesis]`
8. **flagellar rod defect — disrupts — distributed basal-body pattern** `[taxon-specific]`
9. **surface contact — increases — flagellar number** `[E. coli; condition-specific]`
10. **peritrichous flagella — enable — swimming/swarming motility** `[downstream function, not pattern formation]`

The 2015 review supports the core definition and recognizes stochastic or diffusion-and-capture models, but also states that exact regulatory networks remain incompletely characterized. Therefore, stochastic nucleation should be encoded as `may_contribute_to`, not as a definitive universal cause. (schuhmacher2015howbacteriamaintain pages 9-10, schuhmacher2015howbacteriamaintain pages 2-4)

## Quantitative observations

- The review gives approximately **5–6 flagella per cell** for the representative peritrichous organisms *E. coli* and *B. subtilis*. This is illustrative, not a diagnostic threshold. (schuhmacher2015howbacteriamaintain pages 2-4)
- In *E. coli*, flagellar distribution is asymmetric, with greater density toward the old-pole region after division; the pattern depends partly on inherited flagellar positions. (schuhmacher2015howbacteriamaintain pages 4-5)
- Surface contact can increase *E. coli* flagellar number during swarming development, whereas the same response was not reported for *Salmonella* in the cited comparison. (schuhmacher2015howbacteriamaintain pages 2-4)
- The 2025 *B. subtilis* study describes about **25 basal bodies over the cell length** in its experimental system, substantially above the older review’s illustrative 5–6-filament figure. Differences in strain, growth condition, developmental state, and whether basal bodies or completed filaments were counted likely matter; these values should not be merged into a universal count.

## Applications and real-world relevance

Peritrichous flagella provide distributed propellers that can bundle during swimming and support migration through liquids or over hydrated surfaces. Their number is environmentally adjustable, making the phenotype relevant to swarming, nutrient seeking, host colonization, and initial attachment. Correct patterning also ensures that daughter cells can inherit motility machinery and rapidly chemotax after division. (schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 1-2, schuhmacher2015howbacteriamaintain pages 2-4)

Applied relevance includes control of enterobacterial surface colonization and biofilms, interpretation of clinical and food-isolate morphology, and engineering or inhibition of motile bacterial systems. However, downstream effects are context-dependent: a flagellum may contribute to initial attachment or dispersal without being indispensable for mature biofilm formation. Such outcomes belong downstream of the morphology and should not be treated as defining evidence for peritrichy.

## Ontology-grounding recommendations

Use the supplied identifier exactly as **`traitmech:000060`**. Candidate structure/process nodes should be mapped to verified Gene Ontology terms for bacterial-type flagellum, basal body, MS ring, C ring, hook, filament, flagellum-dependent motility, chemotaxis, and flagellar assembly. Protein nodes should use organism-specific UniProt accessions only after the target taxon and strain are fixed.

Recommended practice:

- Represent genes/proteins such as FliF, FliM, FlhF, and FlhG initially by label plus taxon.
- Resolve UniProt identifiers separately for *E. coli*, *Salmonella*, and *B. subtilis*; do not collapse orthologues with divergent placement functions.
- Ground peptidoglycan to its verified ChEBI term during YAML validation.
- Treat “peptidoglycan pore grid,” “distributed capture site,” and “old-pole enrichment” as label-only nodes unless an appropriate stable ontology class is confirmed.
- Add NCBITaxon identifiers only after checking the exact species/strain used by each experiment.

## Warnings: claims not ready for curation

1. **No universal peritrichous-patterning gene is established.** FlhF/FlhG functions differ across taxa, and most recent mechanistic work concerns polar flagellation.
2. **Do not encode `FlhF causes peritrichous flagellation` generally.** The strongest retrieved direct placement mechanism is the 2025 *B. subtilis* rod–peptidoglycan result; even there, FlhF phenocopy does not prove a simple linear pathway.
3. **Do not infer morphology from genome content.** Flagellar genes establish capacity for organelle assembly, not where flagella are positioned.
4. **Do not use motility assays alone.** Swimming, swarming, or chemotaxis require functional flagella but do not distinguish peritrichous from polar arrangements.
5. **Do not impose a fixed flagellar count.** Published counts depend on species, strain, medium, surface contact, cell cycle, and whether basal bodies or completed filaments are measured.
6. **Keep generic assembly edges separate from pattern-generating edges.** FliF/MS-ring, C-ring, export, hook, filament, and stator relations explain flagellum construction or operation but not necessarily surface-wide placement.
7. **Treat old-pole bias and stochastic placement as provisional and *E. coli*-specific.** The observed asymmetry argues against a fully random universal model. (schuhmacher2015howbacteriamaintain pages 4-5)
8. **Treat the peptidoglycan-grid model as *B. subtilis*-specific pending replication.** It is compelling direct evidence but was published in 2025 and should not be retroactively generalized to Gram-negative peritrichous bacteria. (dunn2025nascentflagellarbasal pages 1-2)

## DOI-first bibliography

1. Schuhmacher JS, Thormann KM, Bange G. “How bacteria maintain location and number of flagella?” *FEMS Microbiology Reviews*. Published November 2015. DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034). Foundational synthesis defining major flagellation patterns and emphasizing unresolved placement mechanisms. (schuhmacher2015howbacteriamaintain pages 9-10, schuhmacher2015howbacteriamaintain pages 1-2, schuhmacher2015howbacteriamaintain pages 2-4)
2. Dunn CM, Foust DJ, Gao Y, Biteen JS, Shaw SL, Kearns DB. “Nascent flagellar basal bodies are immobilized by rod assembly in *Bacillus subtilis*.” *mBio*. Published June 2025. DOI: [10.1128/mbio.00530-25](https://doi.org/10.1128/mbio.00530-25). Direct evidence for rod-dependent capture and patterning in a peritrichous species. (dunn2025nascentflagellarbasal pages 1-2, dunn2025nascentflagellarbasal pages 17-18)

## Curation conclusion

`traitmech:000060` should be represented primarily as a **spatial morphology**, not as a synonym of motility or flagellar assembly. The strongest current graph consists of the external-flagellum/cell-surface relationship plus a taxon-scoped *B. subtilis* branch in which mobile nascent basal bodies are immobilized through rod–peptidoglycan interaction. Enterobacterial stochastic placement, old-pole bias, and surface-induced number changes are useful provisional branches, but the literature does not yet support a single conserved causal pathway for peritrichous pattern formation.

References

1. (schuhmacher2015howbacteriamaintain pages 4-5): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

2. (schuhmacher2015howbacteriamaintain pages 2-4): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

3. (schuhmacher2015howbacteriamaintain pages 1-2): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

4. (dunn2025nascentflagellarbasal pages 1-2): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (dunn2025nascentflagellarbasal pages 17-18): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (schuhmacher2015howbacteriamaintain pages 9-10): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.