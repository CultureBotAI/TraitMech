---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:17:57.516364'
end_time: '2026-08-04T08:25:38.405873'
duration_seconds: 460.89
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: flagellar arrangement
  trait_identifier: traitmech:000056
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: flagellar_arrangement
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait describing the number and spatial distribution of
    flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous,
    amphitrichous, or peritrichous.
  parent_traits: METPO:1000704
  synonyms: flagellation pattern
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe
    how bacteria maintain a regular number and cellular location of flagella (the
    flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial
    flagellum review supports the flagellum as the locomotory organelle whose number
    and placement define flagellar arrangement.)'
  causal_graph_summary: 'flagellar_arrangement_flhf_flhg: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellar arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **flagellar arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellar_arrangement.yaml`.

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
- **Trait label:** flagellar arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **flagellar arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellar_arrangement.yaml`.

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


# Curation report: bacterial flagellar arrangement

## Executive summary

**Target:** `traitmech:000056` — **flagellar arrangement**; category **MORPHOLOGY**; term kind **CLASS**; mapping **REVIEWED**; supplied parent `METPO:1000704`.

The trait should represent the **cell-level combination of flagellar number and spatial distribution**—for example monotrichous, lophotrichous, amphitrichous, and peritrichous flagellation. It should not be equated with flagellum presence, flagellar assembly, swimming motility, motor rotation, chemotaxis, or gene expression. Those are separate structures, processes, or assay outcomes that may lie upstream or downstream of arrangement.

The best-supported causal backbone for a polar-flagellation graph is:

**HubP/FimV and FipA → FlhF recruitment/activation → FliG–FliF recruitment and polar MS-ring initiation → polar flagellar placement**, with **FlhG-mediated FlhF inactivation/C-ring progression and transcriptional feedback → restriction of flagellar number**. The 2024 literature materially refines this model: FlhF is now supported as a molecular tether and assembly checkpoint, while FipA is a newly described membrane-associated licensing factor. These mechanisms are strongest in polarly flagellated Proteobacteria and must not be generalized uncritically to peritrichous species. (arroyoperez2024aconservedcellpole pages 14-15, dornes2024polarconfinementof pages 1-2)

| Proposed causal edge | Evidence class | Primary taxon | Confidence / curation status | DOI |
|---|---|---|---|---|
| HubP/FimV directly interacts with FlhF | Direct protein-protein interaction; structural/biochemical plus localization genetics | *Shewanella putrefaciens* CN-32 | High; curate as taxon-supported polar landmark interaction, not universal across all polar flagellates (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 4-6) | 10.1038/s41467-024-50274-4 |
| FipA directly interacts with FlhF | Direct interaction by co-IP/MS and BACTH; conserved mutational support | *Vibrio parahaemolyticus*; also supported in *Pseudomonas putida* and *Shewanella putrefaciens* | High; curate as strong 2024 node-edge for FlhF-dependent polar synthesis pathway (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 12-14, arroyoperez2024aconservedcellpole pages 8-11) | 10.7554/eLife.93004.3 |
| FlhF directly binds FliG | Direct interaction; structural and biochemical mapping of FlhF FID/B-domain to FliG | *Shewanella putrefaciens* CN-32 | High; curate as core mechanistic recruitment edge for polar assembly (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 6-7) | 10.1038/s41467-024-50274-4 |
| FliG promotes/captures FliF MS-ring assembly | Biochemical assembly and localization evidence | *Vibrio* spp.; *Shewanella putrefaciens* | High but taxon-scoped; curate as assembly-promoting edge upstream of arrangement phenotype (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 6-7) | 10.1038/s41467-024-50274-4; 10.1128/JB.00236-20 |
| FlhF-bound FliG is prevented from interacting with FliM/FliN | Direct interaction antagonism/gating from biochemical interaction assays | *Shewanella putrefaciens* CN-32 | High; curate as mechanistic checkpoint edge with explicit taxon note (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 6-7) | 10.1038/s41467-024-50274-4 |
| FlhG stimulates FlhF GTP hydrolysis | Biochemical/regulatory interaction supported by review synthesis and current model | Multiple polar-flagellated bacteria | Moderate-high; curate as conserved regulatory edge, but usually supported across taxa rather than a single universal assay system here (schuhmacher2015howbacteriamaintain pages 8-9, dornes2024polarconfinementof pages 7-8, dornes2024polarconfinementof pages 6-7) | 10.1093/femsre/fuv034; 10.1038/s41467-024-50274-4 |
| FlhF promotes polar flagellar placement | Mutant phenotypes, localization microscopy, rescue/inference from assembly mutants | *Helicobacter pylori*; also Vibrio/*Pseudomonas*/*Shewanella* | High; curate as trait-proximal positive edge to polar placement with species-specific quantitative manifestations (gibson2023controlofthe pages 11-13, gibson2023controlofthe pages 1-2, arroyoperez2024aconservedcellpole pages 14-15) | 10.1128/JB.00110-23; 10.7554/eLife.93004.3 |
| FlhG restricts flagellar number | Mutant phenotype genetics and review synthesis | *Helicobacter pylori*; Vibrio/*Pseudomonas*/*Shewanella* | High; curate as trait-proximal negative edge to flagellar number, with taxon-specific output distributions (gibson2023controlofthe pages 1-2, arroyoperez2024aconservedcellpole pages 1-2, gibson2023controlofthe pages 11-13) | 10.1128/JB.00110-23; 10.7554/eLife.93004.3 |
| FipA promotes FlhF polar localization and thereby polar flagellar synthesis | Localization genetics plus loss-of-function phenotype | *Vibrio parahaemolyticus*; *Pseudomonas putida*; *Shewanella putrefaciens* | High; curate as strong 2024 licensing/localization edge, noting some species retain polar positioning despite reduced number (arroyoperez2024aconservedcellpole pages 11-12, arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 12-14, arroyoperez2024aconservedcellpole pages 8-11) | 10.7554/eLife.93004.3 |
| HubP/FimV contributes to proper polar flagellar placement/number via FlhF/FlhG pathway | Localization genetics and comparative phenotypes | *Vibrio parahaemolyticus*; *Shewanella putrefaciens* | Moderate; curate only with explicit species-variation warning because phenotypic strength differs across taxa (dornes2024polarconfinementof pages 7-8, arroyoperez2024aconservedcellpole pages 14-15) | 10.1038/s41467-024-50274-4; 10.7554/eLife.93004.3 |


*Table: This table prioritizes the strongest causal edges currently supported for curating traitmech:000056. It highlights which interactions are direct and high-confidence versus those that are taxon-dependent and should be curated with explicit scope notes.*

## 1. Trait scope and boundaries

### Included phenotype

A valid observation describes both or either component of the arrangement state:

- **Number:** zero, one, several, or many flagella per cell.
- **Position:** one pole, both poles, a polar tuft, lateral sites, or distribution around the cell surface.
- **Composite named pattern:** monotrichous, lophotrichous, amphitrichous, peritrichous, or a taxon-specific mixed pattern.
- **Population distribution:** where relevant, the distribution of numbers or positions across cells, rather than only the mean.

This scope is consistent with the current mechanistic literature, which uses “flagellation pattern” for species-specific flagellar location and abundance and treats FlhF and FlhG as principal spatial and numerical regulators. (gibson2023controlofthe pages 1-2, dornes2024polarconfinementof pages 1-2)

### Boundary cases

1. **Flagellum presence/absence:** “Aflagellate” is an extreme arrangement outcome, but a generic ability to synthesize a flagellum is not itself the arrangement trait.
2. **Assembly:** MS-ring, C-ring, hook, filament, and type III export assembly are upstream processes. Include them only where evidence connects them causally to number or position.
3. **Motility:** Soft-agar spread and swimming speed are indirect functional readouts. A motility defect does not establish altered arrangement without microscopy or flagellar enumeration.
4. **Chemotaxis and rotational switching:** These influence movement rather than flagellar placement or count.
5. **Cell-cycle timing:** Uni-to-bipolar localization transitions can be causal intermediates, but cell-cycle stage should be represented as experimental context unless directly manipulated.
6. **Dual flagellar systems:** Polar and lateral systems in the same organism require system-specific nodes. In *S. putrefaciens*, FlhF selectively recognizes polar FliG rather than its lateral paralog. (dornes2024polarconfinementof pages 2-4)
7. **Pilus placement and other polar organelles:** HubP/FimV can organize several polar systems; only the branch demonstrably connected to flagellar arrangement belongs in this graph. (arroyoperez2024aconservedcellpole pages 1-2)

## 2. Candidate nodes grouped by type

### Trait and phenotype nodes

- **flagellar arrangement** — `traitmech:000056`
- **flagellar number** — label-only candidate
- **polar flagellar placement** — label-only candidate
- **nonpolar/lateral mislocalization** — label-only candidate
- **monotrichous, lophotrichous, amphitrichous, peritrichous flagellation** — retain as label-only subphenotypes until exact ontology mappings are verified
- **bacterial-type flagellum** — `GO:0009288`

### Genes and proteins

- **FlhF:** SRP-family GTPase; spatial landmark/tether and positive assembly factor. Its NG domain binds HubP, while an N-terminal FliG-interaction domain binds polar FliG. Candidate molecular-function grounding: GTP binding, `GO:0005525`. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4)
- **FlhG/FleN:** MinD/ParA-family ATPase; stimulates FlhF GTPase activity, restricts flagellar number, and contributes to C-ring assembly and transcriptional feedback. Candidate ATP-binding grounding: `GO:0005524`. (schuhmacher2015howbacteriamaintain pages 8-9)
- **HubP/FimV:** cell-pole landmark/scaffold; directly binds FlhF in *S. putrefaciens* and helps localize FlhG or FlhF in several taxa. Effects are strongly species-dependent. (dornes2024polarconfinementof pages 7-8, dornes2024polarconfinementof pages 4-6)
- **FipA:** 2024-discovered integral membrane protein with DUF2802; directly interacts with FlhF and licenses normal polar flagellum synthesis in *V. parahaemolyticus*, *P. putida*, and *S. putrefaciens*. Keep label-only pending organism-specific UniProt verification. (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 1-2)
- **FliF:** transmembrane MS-ring protein and early assembly substrate. Candidate parent structure: bacterial-type flagellum basal body, `GO:0009425`.
- **FliG:** rotor/C-ring component recruited by FlhF; captures or promotes FliF assembly.
- **FliM, FliN, FliY:** C-ring/switch components; interact with FlhG and/or FliG in a taxon-specific assembly sequence.
- **FleQ/FlrA:** transcriptional activators whose activity can be restrained by FlhG/FleN after assembly initiation. This is an indirect numerical-control branch, not a morphology node itself. (schuhmacher2015howbacteriamaintain pages 8-9)
- **FaaA:** possible *H. pylori* suppressor-associated factor; do not curate yet because causality for placement was unresolved. (gibson2023controlofthe pages 11-13)

### Complexes, organelles, and localizations

- **FlhF–HubP complex** — direct biochemical complex
- **FlhF–FliG complex** — direct biochemical complex
- **FliF–FliG/MS-ring initiation complex** — assembly intermediate
- **C ring / switch complex** — label-only; part of `GO:0009425`
- **bacterial-type flagellum basal body** — `GO:0009425`
- **bacterial-type flagellum hook** — `GO:0009424`
- **bacterial-type flagellum filament** — `GO:0009420`
- **plasma membrane** — `GO:0005886`
- **cytoplasm** — `GO:0005737`
- **cell pole, old pole, new pole, division plane** — label-only localization candidates; verify exact GO terms before YAML insertion

### Processes and molecular activities

- FlhF GTP binding/hydrolysis — `GO:0005525` for binding; retain hydrolysis as label-only unless an exact activity term is verified
- FlhG ATP binding/homodimerization — `GO:0005524` for binding
- polar recruitment/diffusion-capture
- MS-ring assembly
- C-ring assembly
- flagellar gene transcription
- cell division — `GO:0051301`, contextual only
- motor activity — `GO:0003774`, normally downstream and outside the core arrangement graph

### Environmental and experimental-factor nodes

No environmental condition currently has sufficiently direct evidence in the retrieved corpus to serve as a general causal parent of `traitmech:000056`. Appropriate **experimental-context** nodes include:

- gene deletion or depletion;
- protein overexpression;
- point mutation and domain truncation;
- fluorescent-protein fusion;
- heterologous expression in *E. coli*;
- soft-agar spreading;
- planktonic single-cell tracking;
- fluorescence microscopy;
- electron/flagellar staining microscopy;
- bacterial two-hybrid, yeast two-hybrid, co-IP/MS, pulldown, crystallography, and size-exclusion chromatography.

These should normally be evidence metadata rather than biological graph nodes.

## 3. Candidate evidence-backed causal edges

“Snippet” below is concise source wording or a close extractive condensation suitable for evidence notes; quotation marks should not be treated as a claim of full-sentence verbatim transcription.

| # | Subject–predicate–object | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | HubP/FimV — **directly binds** → FlhF NG domain | DOI: [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4), July 2024 | “FlhF interacts with HubP-C … through its NG domain.” | **High confidence**, direct pulldown/interaction evidence in *S. putrefaciens*; nucleotide-independent. (dornes2024polarconfinementof pages 4-6) |
| 2 | FlhF FID/B-domain — **directly binds** → polar FliG | Same DOI | “The N-terminal 60 amino acids … are necessary and sufficient for FliG binding.” | **High confidence**; yeast two-hybrid, pulldown, crystallography, and SEC. Polar-system specificity was demonstrated against lateral FliG. (dornes2024polarconfinementof pages 2-4) |
| 3 | HubP-bound FlhF — **recruits** → FliG to the pole | Same DOI | “FlhF serves as a tether between … HubP/FimV and developing flagellar structures.” | **High confidence**, supported by reconstitution/localization; ≥310 cells per replicate in three experiments, reported *p*<0.0001. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 6-7) |
| 4 | FlhF-bound FliG — **captures/promotes recruitment of** → FliF | Same DOI | “FID-tethered FliG captures diffusing FliF proteins at the cell pole.” | **High confidence model** backed by interaction and localization data; graph predicate may be `promotes_localization_of`. (dornes2024polarconfinementof pages 7-8) |
| 5 | FliG — **promotes assembly of** → FliF MS ring | DOI: [10.1128/JB.00236-20](https://doi.org/10.1128/JB.00236-20), July 2020; 2024 corroboration | “FliG facilitates MS-ring formation.” | **High confidence but taxon-scoped** to *Vibrio*/*Shewanella* evidence. (dornes2024polarconfinementof pages 2-4) |
| 6 | FlhF-bound FliG — **fails to engage / inhibits premature engagement with** → FliM/FliN | DOI: 10.1038/s41467-024-50274-4 | “FlhF-bound FliG … is prevented from engaging C-ring proteins FliM and FliN.” | **High confidence interaction-gating edge** in *S. putrefaciens*. Use an explicit negative predicate; do not claim degradation or transcriptional repression. (dornes2024polarconfinementof pages 2-4) |
| 7 | FlhG — **stimulates GTPase activity of** → FlhF | DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034), November 2015; DOI: 10.1038/s41467-024-50274-4 | “FlhG interacts with FlhF to stimulate its GTPase activity.” | **Moderate-high confidence/conserved model**; biochemical support exists across polar flagellates, but encode taxon scope where possible. (schuhmacher2015howbacteriamaintain pages 8-9, dornes2024polarconfinementof pages 6-7) |
| 8 | FlhG-mediated FlhF inactivation — **limits** → polar assembly initiation | Same references | “FlhG’s modulation of FlhF … regulat[es] progression of flagellar assembly at the pole.” | **Model-level edge**. Curate only if the YAML accepts regulatory-process intermediates; otherwise connect FlhG directly to flagellar number. (dornes2024polarconfinementof pages 7-8) |
| 9 | FlhG — **restricts** → flagellar number | DOI: [10.1128/JB.00110-23](https://doi.org/10.1128/JB.00110-23), September 2023 | “Deleting flhG … shifted … approximately four flagella to a wider … distribution.” | **High-confidence trait-proximal edge**, but phenotype differs by taxon: *H. pylori* did not simply show uniform hyperflagellation. (gibson2023controlofthe pages 1-2) |
| 10 | FlhF — **promotes** → polar flagellar placement | Same DOI | “Deleting flhF … [caused] improper localization of flagella to nonpolar sites.” | **High confidence** in *H. pylori*; also supported across polar flagellates, with taxon-dependent severity. (gibson2023controlofthe pages 1-2, gibson2023controlofthe pages 11-13) |
| 11 | FlhF — **promotes** → flagellar biogenesis/number | Same DOI | “ΔflhF mutants show reduced motility, hypoflagellation, and increased lateral flagella.” | **High confidence**, but distinguish number and placement as separate output edges. (gibson2023controlofthe pages 11-13) |
| 12 | FliF N255D — **enhances** → MS-ring oligomerization | Same DOI | “FliF N255D … formed ordered ring-like assemblies … ~50 nm wide.” | **High confidence but allele- and taxon-specific**; useful as mechanistic rescue evidence, not a general wild-type edge. (gibson2023controlofthe pages 1-2) |
| 13 | enhanced FliF oligomerization — **partially bypasses** → FlhF requirement | Same DOI | “FliF N255D … partially rescues ΔflhF mutant motility defects.” | **Moderate confidence** for causal bypass; rescue was partial and motility is indirect. Annotate *H. pylori* and the specific allele. (gibson2023controlofthe pages 11-13) |
| 14 | FipA — **directly binds** → FlhF | DOI: [10.7554/eLife.93004.3](https://doi.org/10.7554/eLife.93004.3), December 2024 | “FipA directly interacts with FlhF via conserved DUF2802 domain residues.” | **High confidence** by co-IP/MS and bacterial two-hybrid across three γ-proteobacterial models. (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15) |
| 15 | FipA membrane anchoring — **enables** → FipA–FlhF function | Same DOI | “The FipA transmembrane domain is functionally essential.” | **High confidence** in *V. parahaemolyticus*: ΔTM produced no flagella; retain taxon annotation. (arroyoperez2024aconservedcellpole pages 11-12, arroyoperez2024aconservedcellpole pages 8-11) |
| 16 | FipA — **promotes** → FlhF polar localization | Same DOI | “Deletion significantly reduces polar FlhF in all species.” | **High confidence**, but dependence differs by species and HubP/FimV background. (arroyoperez2024aconservedcellpole pages 14-15) |
| 17 | FipA — **promotes/licenses** → polar flagellar synthesis | Same DOI | “FipA … is present at the designated pole before flagellar synthesis begins.” | **High confidence for requirement; ‘licenses’ remains mechanistic interpretation.** In *V. parahaemolyticus*, ΔfipA abolished synthesis; in the other species it reduced number. (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 12-14) |
| 18 | FipA G110/L129 residues — **enable** → FlhF interaction | Same DOI | “G110A and L129A … are essential for FipA–FlhF interaction.” | **High confidence but residue- and species-specific** to *V. parahaemolyticus* numbering; homologous positions differ in other species. (arroyoperez2024aconservedcellpole pages 8-11) |
| 19 | FipA and HubP/FimV — **act in partially parallel pathways to promote** → active/polar FlhF | Same DOI | “FipA and HubP/FimV represent two parallel pathways stimulating FlhF polar localization.” | **Moderate-high model-level edge**; double deletions nearly eliminated localization, but exact pathway architecture varies among species. (arroyoperez2024aconservedcellpole pages 14-15) |
| 20 | C-ring FliM/FliN(Y) — **recruits/supports localization of** → FlhG | DOI: 10.1093/femsre/fuv034; supporting *Campylobacter/Shewanella* work | “FlhG … binds FliM/FliN(Y) … and facilitates their association with FliG.” | **Moderate and taxon-specific**. FliM/FliN paralog composition and interaction motifs vary; avoid universalization. (schuhmacher2015howbacteriamaintain pages 8-9, rossmann2017spatialregulationof pages 117-120) |
| 21 | membrane-associated FlhG dimerization — **enables** → numerical/transcriptional feedback | DOI: 10.1093/femsre/fuv034 | “ATP-dependent homodimerization … release … allows interaction with transcription factors like FleQ.” | **Model-level/indirect**; curate only if transcriptional control is within graph scope. (schuhmacher2015howbacteriamaintain pages 8-9) |

### Recommended minimal YAML backbone

For a compact first revision of the existing nine-node/eight-edge graph, prioritize edges **1, 2, 4, 6, 7, 9, 10, 14, 16, and 17**. Keep number and position as separate phenotype nodes converging on `traitmech:000056`. Add taxon qualifiers to every experimental edge rather than representing the FlhF–FlhG circuit as universally identical.

## 4. Recent developments and quantitative findings

### 2024: FlhF as a polar tether and assembly checkpoint

Dornes and colleagues resolved a hierarchical mechanism in *S. putrefaciens*: the FlhF NG domain contacts HubP, whereas an N-terminal FID contacts polar FliG. FlhF-bound FliG can engage FliF but not FliM/FliN, suggesting that FlhF both confines initiation to the pole and delays full C-ring assembly until FlhG-dependent progression. Deleting the 44-residue FliG-binding region left FlhF polar in roughly **70%** of cells but redistributed hooks: approximately **40% subpolar** and **10% polar**, compared with **92% monopolar** in wild type. Measurements used at least three biological replicates and ≥310–330 cells per strain. (dornes2024polarconfinementof pages 7-8, dornes2024polarconfinementof pages 4-6)

This is the strongest current direct evidence that arrangement is generated not merely by a diffuse “landmark” but by a physical scaffold–GTPase–rotor recruitment chain. The authors’ biochemical and localization evidence supports curating FlhF as both a localization factor and an ordered-assembly checkpoint. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4)

### 2024: FipA as a licensing factor

Arroyo-Pérez and colleagues identified FipA, a 163-aa integral membrane protein, as a direct FlhF partner. In *V. parahaemolyticus*, ΔfipA and transmembrane-anchor deletion abolished flagellar synthesis. G110A and L129A substitutions disrupted FlhF interaction, eliminated motility, and caused diffuse FlhF signal in about **50%** of cells. In *P. putida* and *S. putrefaciens*, ΔfipA reduced rather than abolished flagellar number; soft-agar spread fell by about **25%** and **90%**, respectively, whereas ΔflhF reduced spread by approximately **40–50%**. Because soft-agar spreading is indirect, the microscopy-backed number/position phenotypes should carry greater curation weight. (arroyoperez2024aconservedcellpole pages 11-12, arroyoperez2024aconservedcellpole pages 8-11)

FipA localization was also species-specific: about **100%** of *P. putida* cells versus roughly **50%** of *V. parahaemolyticus* cells showed polar localization, with bipolar:unipolar ratios near **1:2** and **1:5**, respectively. These results argue against a single universal cell-cycle topology. (arroyoperez2024aconservedcellpole pages 12-14)

### 2023: multi-flagellated *H. pylori* revises the simple FlhG model

Wild-type *H. pylori* populations centered around approximately **four flagella per cell**. ΔflhG broadened the distribution and increased aflagellated/hypoflagellated fractions rather than producing only the simple hyperflagellated phenotype familiar from monotrichous vibrios. ΔflhF caused hypoflagellation and increased nonpolar flagella. The FliF N255D suppressor formed MS-ring-like particles approximately **50 nm** across and partially bypassed FlhF, supporting a role for FlhF in FliF oligomerization. (gibson2023controlofthe pages 11-13, gibson2023controlofthe pages 1-2)

## 5. Applications and expert interpretation

### Real-world relevance

- **Phenotypic identification and systematics:** Flagellar number and placement are long-standing species-level morphological descriptors. The 2024 work reiterates that these patterns were among microbiology’s earliest taxonomic criteria. Mechanistic graphs can connect those observations to genotype while preserving taxon-specificity. (dornes2024polarconfinementof pages 1-2)
- **Pathogenesis research:** *H. pylori* requires flagellar motility for gastric colonization; arrangement defects therefore provide mechanistic targets for studying colonization, although the evidence reviewed here does not validate FlhF/FlhG/FipA as clinical drug targets. (gibson2023controlofthe pages 1-2)
- **Environmental and industrial microbiology:** *P. putida*, *Shewanella*, and *Vibrio* models show how spatial assembly governs navigation and colonization-related behavior. Current implementations are primarily genetic manipulation, quantitative microscopy, and single-cell phenotyping—not deployed arrangement-engineering products.
- **Synthetic biology:** The modular HubP/FipA–FlhF–FliG/FliF pathway is a plausible framework for engineering localized macromolecular assembly. This is a prospective application, not yet a source-backed production implementation.

### Expert analysis

The authoritative 2015 review proposed a cycle in which FlhF marks the assembly site and FlhG couples C-ring assembly, FlhF inactivation, and transcriptional feedback. The 2023–2024 studies support that general framework but show that it must be represented as a **family of taxon-conditioned mechanisms**, not one universal graph. (schuhmacher2015howbacteriamaintain pages 8-9, gibson2023controlofthe pages 11-13)

The most defensible graph architecture separates:

1. **spatial licensing** — FipA and HubP/FimV;
2. **polar recruitment and initiation** — FlhF, FliG, FliF;
3. **assembly checkpoint release and numerical control** — FlhG and C-ring proteins;
4. **trait outputs** — number and position;
5. **functional consequences** — motility, colonization, and fitness.

This separation prevents common causal errors, especially treating reduced motility as proof of changed arrangement or treating a direct protein interaction as proof of a universal phenotype.

## 6. Ontology-grounding recommendations

Use only verified stable identifiers in the initial YAML:

| Entity | Suggested CURIE | Comment |
|---|---|---|
| Flagellar arrangement | `traitmech:000056` | Quote verbatim as requested. |
| Supplied parent trait | `METPO:1000704` | Preserve supplied mapping. |
| Bacterial-type flagellum | `GO:0009288` | Whole organelle. |
| Bacterial-type flagellum basal body | `GO:0009425` | Suitable parent for MS/C-ring structural nodes. |
| Bacterial-type flagellum hook | `GO:0009424` | Structural readout in microscopy studies. |
| Bacterial-type flagellum filament | `GO:0009420` | Distinct from arrangement. |
| GTP binding | `GO:0005525` | FlhF molecular function. |
| ATP binding | `GO:0005524` | FlhG/FleN molecular function. |
| Plasma membrane | `GO:0005886` | FipA and FliF localization. |
| Cytoplasm | `GO:0005737` | FlhG and C-ring context. |
| Cell division | `GO:0051301` | Contextual process, not a core arrangement output. |
| Motor activity | `GO:0003774` | Downstream functional node if needed. |

Keep FlhF, FlhG/FleN, HubP/FimV, FipA, FliF, FliG, FliM, FliN, FliY, FleQ/FlrA, cell pole, MS ring, C ring, and named arrangement subtypes as **label-only candidates** until organism-specific accessions or exact ontology terms are checked. Protein symbols alone are unsafe identifiers because paralogs and nomenclature differ among taxa.

## 7. Claims not ready for TraitMech curation

1. **A universal HubP → FlhF phenotype:** HubP deletion reportedly causes about 50% flagellation loss in *V. parahaemolyticus*, increased polar flagella in *V. alginolyticus*, minor effects in *V. cholerae*, and minimal polarity effects in *S. putrefaciens*. Curate species-specific edges only. (dornes2024polarconfinementof pages 7-8)
2. **FipA universally determines placement:** In *S. putrefaciens*, ΔfipA sharply reduced number while remaining flagella retained polar positioning. The strongest general statement is that FipA promotes normal FlhF localization and synthesis, not that it always specifies position. (arroyoperez2024aconservedcellpole pages 14-15)
3. **ΔflhG universally causes hyperflagellation:** The *H. pylori* result broadened the distribution and increased low-number classes. Numerical regulation is conserved; the direction and shape of the phenotype are not. (gibson2023controlofthe pages 1-2)
4. **Motility phenotype equals arrangement phenotype:** Soft-agar spread integrates growth, chemotaxis, motor function, and filament assembly. Do not curate a morphology edge from motility alone.
5. **FaaA controls polar placement:** Suppressor variants implicated the locus, but the responsible determinants were unresolved. (gibson2023controlofthe pages 11-13)
6. **Environmental-factor edges:** No retrieved 2023–2024 study established a general nutrient, temperature, oxygen, electron donor/acceptor, chemical, or inhibitor as a direct determinant of arrangement. Do not add such nodes from ecological plausibility.
7. **Peritrichous extrapolation:** The detailed FlhF/FlhG–HubP/FipA chain is principally supported in polar flagellates. Peritrichous and grid-like systems may use different localization logic.
8. **“Licensing” as an observed biochemical activity:** FipA precedes synthesis and is required for it, but licensing is the authors’ mechanistic interpretation; annotate as a proposed mechanism. (arroyoperez2024aconservedcellpole pages 1-2)
9. **Generic UniProt or NCBITaxon accessions:** Do not assign cross-species protein identifiers without selecting a strain and verifying the accession.

## DOI-first bibliography

1. **Dornes A, et al.** “Polar confinement of a macromolecular machine by an SRP-type GTPase.” *Nature Communications* 15 (July 2024). DOI: [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4). Direct structural, biochemical, and localization evidence for the HubP–FlhF–FliG/FliF mechanism. (dornes2024polarconfinementof pages 1-2)
2. **Arroyo-Pérez EE, et al.** “A conserved cell-pole determinant organizes proper polar flagellum formation.” *eLife* 13 (December 2024). DOI: [10.7554/eLife.93004.3](https://doi.org/10.7554/eLife.93004.3). Discovery and cross-species analysis of FipA. (arroyoperez2024aconservedcellpole pages 1-2)
3. **Gibson KH, et al.** “Control of the flagellation pattern in *Helicobacter pylori* by FlhF and FlhG.” *Journal of Bacteriology* 205(9) (September 2023). DOI: [10.1128/JB.00110-23](https://doi.org/10.1128/JB.00110-23). Quantitative multi-flagellar phenotypes and FliF suppressor mechanism. (gibson2023controlofthe pages 1-2)
4. **Arroyo-Pérez EE, Ringgaard S.** “Interdependent Polar Localization of FlhF and FlhG and Their Importance for Flagellum Formation of *Vibrio parahaemolyticus*.” *Frontiers in Microbiology* 12 (March 2021). DOI: [10.3389/fmicb.2021.655239](https://doi.org/10.3389/fmicb.2021.655239). Cell-cycle localization and HubP dependence.
5. **Terashima H, et al.** “Assembly Mechanism of a Supramolecular MS-Ring Complex To Initiate Bacterial Flagellar Biogenesis in *Vibrio* Species.” *Journal of Bacteriology* 202(16) (July 2020). DOI: [10.1128/JB.00236-20](https://doi.org/10.1128/JB.00236-20). FlhF/FliG promotion of FliF MS-ring assembly.
6. **Henderson LD, et al.** “Diversification of *Campylobacter jejuni* Flagellar C-Ring Composition…” *mBio* 11(1) (February 2020). DOI: [10.1128/mBio.02286-19](https://doi.org/10.1128/mBio.02286-19). C-ring composition, FlhG localization, and numerical control.
7. **Burnham PM, et al.** “A Polar Flagellar Transcriptional Program…” *mBio* 11(2) (April 2020). DOI: [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19). Integration of transcriptional checkpoints with FlhF/FlhG control.
8. **Schuhmacher JS, Thormann KM, Bange G.** “How bacteria maintain location and number of flagella?” *FEMS Microbiology Reviews* 39(6):812–822 (November 2015). DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034). Authoritative conceptual foundation. (schuhmacher2015howbacteriamaintain pages 8-9)

## Curation recommendation

`traitmech:000056` is a strong candidate for an expanded, taxon-aware causal graph. The immediate high-value update is to add **FipA** and explicit **HubP/FimV–FlhF–FliG–FliF** assembly intermediates, while separating **polar placement** from **flagellar number**. Every mechanistic edge should carry organism and assay provenance. The graph should represent the FlhF/FlhG module as a conserved regulatory theme whose phenotypic realization varies by flagellation system, rather than as a universal one-gene/one-phenotype pathway.

References

1. (arroyoperez2024aconservedcellpole pages 14-15): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

3. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

4. (dornes2024polarconfinementof pages 4-6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

5. (arroyoperez2024aconservedcellpole pages 2-3): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (arroyoperez2024aconservedcellpole pages 12-14): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (arroyoperez2024aconservedcellpole pages 8-11): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (dornes2024polarconfinementof pages 6-7): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

9. (schuhmacher2015howbacteriamaintain pages 8-9): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

10. (dornes2024polarconfinementof pages 7-8): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

11. (gibson2023controlofthe pages 11-13): Katherine H. Gibson, Jack M. Botting, Natalie Al-Otaibi, Kriti Maitre, Julien Bergeron, Vincent J. Starai, and Timothy R. Hoover. Control of the flagellation pattern in <i>helicobacter pylori</i> by flhf and flhg. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00110-23, doi:10.1128/jb.00110-23. This article has 10 citations and is from a peer-reviewed journal.

12. (gibson2023controlofthe pages 1-2): Katherine H. Gibson, Jack M. Botting, Natalie Al-Otaibi, Kriti Maitre, Julien Bergeron, Vincent J. Starai, and Timothy R. Hoover. Control of the flagellation pattern in <i>helicobacter pylori</i> by flhf and flhg. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00110-23, doi:10.1128/jb.00110-23. This article has 10 citations and is from a peer-reviewed journal.

13. (arroyoperez2024aconservedcellpole pages 1-2): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (arroyoperez2024aconservedcellpole pages 11-12): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (rossmann2017spatialregulationof pages 117-120): Florian Roßmann. Spatial regulation of dual flagellar systems. ArXiv, Jan 2017. URL: https://doi.org/10.17192/z2017.0061, doi:10.17192/z2017.0061. This article has 0 citations.