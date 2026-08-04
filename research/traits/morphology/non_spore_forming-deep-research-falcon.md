---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:12:37.808125'
end_time: '2026-08-04T09:22:39.966820'
duration_seconds: 602.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: non-spore forming
  trait_identifier: METPO:1000872
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: non_spore_forming
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A sporulation in which an organism lacks the ability to produce endospores.
  parent_traits: METPO:1000870
  synonyms: no, no_spore
  evidence_summary: 'DOI:10.1155/2013/898106: S. aureus does not form spores (Organism
    example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297:
    activation of these sigma factors to landmark events in morphogenesis (Sporulation
    regulatory review supports the Spo0A/sigma cascade as the sporulation control
    program whose absence yields a non-spore-forming phenotype.)'
  causal_graph_summary: 'non_spore_forming_absent_spo0a_cascade: 12 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non-spore forming
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000872
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism lacks the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** no, no_spore
- **Existing evidence:** DOI:10.1155/2013/898106: S. aureus does not form spores (Organism example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297: activation of these sigma factors to landmark events in morphogenesis (Sporulation regulatory review supports the Spo0A/sigma cascade as the sporulation control program whose absence yields a non-spore-forming phenotype.)
- **Existing causal graph summary:** non_spore_forming_absent_spo0a_cascade: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **non-spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_spore_forming.yaml`.

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
- **Trait label:** non-spore forming
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000872
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism lacks the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** no, no_spore
- **Existing evidence:** DOI:10.1155/2013/898106: S. aureus does not form spores (Organism example: Staphylococcus aureus is described as non-spore-forming.) | DOI:10.1146/annurev.genet.30.1.297: activation of these sigma factors to landmark events in morphogenesis (Sporulation regulatory review supports the Spo0A/sigma cascade as the sporulation control program whose absence yields a non-spore-forming phenotype.)
- **Existing causal graph summary:** non_spore_forming_absent_spo0a_cascade: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **non-spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_spore_forming.yaml`.

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


# Curation-focused research report: non-spore forming

## Trait record and scope

- **Trait label:** non-spore forming
- **Trait identifier:** `METPO:1000872`
- **Category / kind:** MORPHOLOGY / CLASS
- **Mapping status:** REVIEWED
- **Parent:** `METPO:1000870`
- **Supplied definition:** “A sporulation in which an organism lacks the ability to produce endospores.”
- **Recommended operational definition:** a stable, strain-level inability to complete bacterial endospore differentiation under validated sporulation-inducing conditions, preferably demonstrated by both absence of morphologically mature endospores and absence of resistant-spore recovery.

The wording “a sporulation” is logically awkward because the phenotype denotes absence of a capacity, not a type of successful sporulation. The graph should terminate in **failure/absence of mature endospore formation**, rather than treating “non-spore-forming” as an active developmental process.

### Boundaries and nearby traits

1. **Not merely “no spores observed.”** Sporulation is heterogeneous, asynchronous, medium-dependent, and sometimes rare. In *Clostridioides difficile* 630Δerm, heat-resistant spores were undetectable for the first 10 h, only 0.3% sporulation was measured at 24 h, and 43.8% at 72 h; at 24 h, spore titers in sporulation medium were two orders of magnitude higher than in BHIS. A negative observation under one condition or time point therefore does not establish incapacity. (pereira2013thesporedifferentiation pages 3-4)
2. **Not environmentally repressed sporulation.** High glucose and low pH can reduce *Bacillus subtilis* sporulation, partly through reduced SigH activity, yet all tested isolates retained sporulation after transfer to 2×SG sporulation agar following 14 days at 200–600 mM glucose and pH 5–9. This is conditional suppression, not a stable non-spore-forming trait. (bosnar2023attemptstolimit pages 3-4, bosnar2023attemptstolimit pages 6-8)
3. **Not a germination defect.** A strain may make mature resistant spores that fail to germinate efficiently. Heat-resistant CFU assays require germination/outgrowth and can therefore underestimate spore formation; microscopy and direct structural assays should accompany them. This ambiguity was explicitly considered for the *C. difficile sigK* mutant. (pereira2013thesporedifferentiation pages 4-5)
4. **Not an incomplete or defective-spore phenotype.** Mutants can reach asymmetric septation, engulfment, cortex formation, or phase refractility without producing normal released spores. These are mechanistic intermediates and should generally be represented as stage-specific failures, not automatically collapsed into the organism-level trait.
5. **Not exospore, myxospore, cyst, or akinete formation.** Endosporulation is distinguished by polar asymmetric division, a mother cell and forespore, engulfment of the forespore, cortex/coat assembly, maturation, and usually mother-cell lysis. Other microbial resting structures are nearby but biologically distinct. (pereira2013thesporedifferentiation pages 2-3, voitsekhovsky2024peculiaritiesofthe pages 9-10)
6. **Taxonomic qualifier.** Validated heat-, solvent-, and UV-resistant bacterial endospores are documented within Firmicutes/Bacillota; reports outside this phylum remain unvalidated. Well-studied lactobacilli, listeria, staphylococci, and streptococci contain no known endospore formers. (galperin2022conservationandevolution pages 1-2)

## Current mechanistic model

The best-supported causal architecture is not simply “absence of Spo0A.” It is a hierarchy:

**environmental and population signals → phosphorylation/activation of Spo0A → asymmetric septation → compartment-specific SigF/SigE activity → engulfment → SigG/SigK-controlled maturation → cortex and coat assembly → mother-cell lysis/release → mature resistant endospore.**

In bacilli, sporulation kinases transfer phosphate through Spo0F and Spo0B to Spo0A; Rap phosphatases oppose this by dephosphorylating Spo0F-P, while imported Phr peptides inhibit their cognate Rap proteins. Clostridia frequently use distinct orphan kinases rather than the complete bacillar Spo0F–Spo0B phosphorelay, so a universal graph should not require KinA–E, Spo0F, or Spo0B. (m.2023sporulationstructureassembly pages 6-7, galperin2022conservationandevolution pages 7-9)

After commitment, SigF and SigG act sequentially in the forespore, while SigE and SigK act sequentially in the mother cell. The ordering and intercompartmental dependencies vary between bacilli and clostridia; these entities are conserved, but their exact edges must be taxon-qualified. (pereira2013thesporedifferentiation pages 2-3, galperin2022conservationandevolution pages 7-9)

## Candidate graph nodes

### Trait and phenotype nodes

| Node | Suggested grounding | Curation note |
|---|---|---|
| non-spore forming | `METPO:1000872` | Use verbatim as requested. |
| endospore formation / sporulation | Label-only pending ontology verification | Do not conflate with germination. |
| mature heat-resistant endospore | Label-only | Useful terminal positive phenotype. |
| absence of recoverable heat-resistant spores | Label-only assay phenotype | Assay-specific; not identical to lack of morphogenesis. |
| asymmetric septation failure | Label-only | Early developmental block. |
| engulfment failure | Label-only | Intermediate block. |
| defective cortex assembly | Label-only | May yield phase-gray or heat-sensitive spores. |
| defective coat assembly | Label-only | Does not always abolish cortex or heat resistance. |
| defective mother-cell lysis/spore release | Label-only | Late-stage phenotype, especially relevant to SigK. |

### Genes, proteins, and complexes

| Module | Candidate nodes | Role / qualification |
|---|---|---|
| Initiation | **spo0A / Spo0A**, Spo0A-P | Master response regulator; absence is strongly predictive, but presence is insufficient. |
| Bacillar phosphorelay | KinA–KinE, Spo0F, Spo0F-P, Spo0B | Appropriate for *Bacillus*-type graphs, not universal across clostridia. |
| Negative initiation control | Rap phosphatases, Phr peptides, Spo0E-family phosphatases | Change Spo0A phosphorylation threshold and sporulation probability. |
| Early transcription | **sigF / σF**, **sigE / σE** | Forespore and mother-cell early programs, respectively. |
| Late transcription | **sigG / σG**, **sigK / σK** | Forespore maturation and mother-cell late program. |
| SigK maturation | skin element, **spoIVCA**, pro-σK, **spoIVFB** | Organism-specific processing; in *C. difficile*, skin excision creates mature SigK without SpoIVFB cleavage. |
| Polar septum | FtsZ, SpoIIE, DivIB/DivIC/DivIVA, **SpoVD**, **SpoVE**, FtsL/FtsQ/FtsB | Several are also involved in vegetative division; use sporulation-specific context. |
| Engulfment | SpoIID, SpoIIM, SpoIIP; SpoIIQ–SpoIIIA complex | Conserved module with substantial lineage variation and redundancy. |
| Cortex | SpoVD, SpoVE, SpoVV, CwlD/CwlC, DacB/DacF | Cortex peptidoglycan synthesis/remodeling. |
| Coat/envelope | SpoIVA, SpoVM, SafA, Cot proteins, GerM | Loss may impair resistance without abolishing all morphogenesis. |
| Core protection | SspA/SspB and other SASPs | DNA protection; in *C. difficile*, SspA/SspB also affect cortex formation. (brantl2023smallproteinsin pages 9-10) |
| Dipicolinate | DpaA/SpoVFA, DpaB/SpoVFB, SpoVA proteins | Bacillar markers are not universally necessary in clostridia. |
| Release | SigK-regulated hydrolases such as CwlC/CwlB/CwlE | Taxon-specific late mother-cell lysis module. (m.2023sporulationstructureassembly pages 7-9) |

Gene/protein nodes should initially remain label-only or be grounded to taxon-specific UniProt records during YAML implementation. A single universal UniProt CURIE would be inappropriate for orthologous proteins from different organisms.

### Processes and cellular locations

- vegetative cell; predivisional cell; polar septum; mother-cell compartment; forespore compartment; intermembrane space; cortex; coat; exosporium; mother-cell lysis;
- Spo0A phosphorylation and transcriptional activation;
- asymmetric cell division and chromosome translocation;
- forespore engulfment;
- compartment-specific transcription;
- cortex peptidoglycan biosynthesis;
- coat/exosporium assembly;
- core dehydration and calcium–dipicolinate accumulation;
- spore maturation, resistance acquisition, and release.

### Environmental, chemical, and assay nodes

- nutrient limitation/starvation; glucose abundance/depletion; low pH; stationary phase; medium composition; incubation time; cell density/quorum peptides;
- phosphate transferred through the phosphorelay; calcium ions; dipicolinic acid/calcium dipicolinate; peptidoglycan;
- sporulation medium, 2×SG agar, BHIS, heat treatment, phase-contrast microscopy, DAPI/FM4-64 staining, TEM, malachite-green spore stain, reporter activity, and heat-resistant CFU count.

Environmental variables should be modeled as regulators of **sporulation induction or efficiency**, not as direct stable causes of `METPO:1000872`, unless persistent heritable loss is demonstrated.

## Candidate causal edges

The following compact overview identifies the strongest first-pass edges.

| subject | predicate | object | taxon/scope | evidence strength |
|---|---|---|---|---|
| spo0A deletion | abolishes | sporulation | *Bacillus subtilis*; knockout strain shows inability to form spores and long-term survival defect (zhu2023afitnesstradeoff pages 2-3, zhu2023afitnesstradeoff pages 3-5) | strong experimental |
| sigF disruption | blocks at | asymmetric division and eliminates detectable heat-resistant spores | *Clostridioides difficile* 630Δerm; 0 heat-resistant spores at tested time points (pereira2013thesporedifferentiation pages 3-4, pereira2013thesporedifferentiation pages 4-5) | strong experimental |
| sigE disruption | blocks at | asymmetric division and eliminates detectable heat-resistant spores | *Clostridioides difficile* 630Δerm; 0 heat-resistant spores at tested time points (pereira2013thesporedifferentiation pages 4-5, pereira2013thesporedifferentiation pages 9-10) | strong experimental |
| sigG disruption | blocks after | engulfment and eliminates detectable heat-resistant spores | *Clostridioides difficile* 630Δerm; engulfment completed but no heat-resistant spores detected (pereira2013thesporedifferentiation pages 4-5) | strong experimental |
| sigK disruption | impairs | late coat assembly and mother-cell lysis, but does not fully abolish heat-resistant spore formation | *Clostridioides difficile* 630Δerm; rare/low heat-resistant spores persist (pereira2013thesporedifferentiation pages 5-7, pereira2013thesporedifferentiation pages 4-5) | strong experimental |
| spoVD loss | causes | defective polar septal peptidoglycan synthesis and reduced progression through sporulation | *Clostridioides difficile*; ~3-fold fewer cells with morphological signs of sporulation than WT (shrestha2023diversificationofdivision pages 3-4) | strong experimental |
| spoVE loss | causes | defective polar septal peptidoglycan synthesis and reduced progression through sporulation | *Clostridioides difficile*; ~3-fold fewer cells with morphological signs of sporulation than WT (shrestha2023diversificationofdivision pages 3-4) | strong experimental |
| high glucose and low pH | suppress | sporulation induction/efficiency without proving stable non-spore-forming state | *Bacillus subtilis* selection experiments; all tested isolates retained ability to sporulate on 2×SG agar (bosnar2023attemptstolimit pages 6-8, bosnar2023attemptstolimit pages 3-4) | moderate experimental; trait-boundary caution |
| absence of spo0A | strongly predicts | inability to sporulate | broad Firmicutes comparative genomics; absence judged an excellent predictor, presence alone insufficient (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 1-2) | strong comparative |
| broad sporulation gene loss | is consistent with | evolutionary non-spore-forming state | Firmicutes lineages including nonsporeformers retaining only partial sporulation programs; stepwise loss inferred (galperin2022conservationandevolution pages 15-17, galperin2022conservationandevolution pages 4-5) | moderate comparative/inferred |


*Table: This compact table summarizes the strongest candidate causal edges for curating the non-spore-forming trait, emphasizing experimentally supported mutant phenotypes and carefully qualified comparative-genomic inferences. It is useful as a first-pass edge list for TraitMech YAML curation.*

A more detailed evidence table follows. Quotations are deliberately short and retain source wording.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation interpretation |
|---|---|---|---|---|---|
| absence of **spo0A** | predicts | inability to form endospores | Galperin et al., 2022, DOI 10.1128/jb.00079-22 | “its absence unequivocally indicates that it is not” a sporeformer | **Strong comparative edge**, Firmicutes scope. Suitable as `absence_of_spo0A → strongly_associated_with → non-spore forming`; do not claim experimental causality across every taxon. (galperin2022conservationandevolution pages 4-5) |
| presence of **spo0A** | is insufficient to establish | spore-forming capacity | Galperin et al., 2022 | “all 76 sporeformers and 40 nonsporeformers” encoded spo0A | Important negative constraint: do not curate `Spo0A present → spore forming`. In the 180-species sample, 32/42 non-spore-forming Clostridia encoded spo0A. (galperin2022conservationandevolution pages 4-5) |
| **spo0A knockout** | abolishes | spore formation after nutrient depletion | Zhu et al., 2023, DOI 10.1126/sciadv.adg9733 | survival defect was “partially attributed to its inability of forming spores after nutrient depletion” | **Strong, species-specific experimental edge** for *B. subtilis* 168. Also causes broad pleiotropy; represent loss of Spo0A activity upstream of failure to initiate sporulation. (zhu2023afitnesstradeoff pages 2-3) |
| **spo0A knockout** | reallocates proteome away from | sporulation and survival programs | Zhu et al., 2023 | “spo0A knockout triggers a global down-regulation of various survival-related pathways” | Supporting mechanistic context, not the core morphology edge. Ribosomal proteome rose 4.9→8%, amino-acid biosynthesis 9.7→12.9%, and growth rate 0.41→0.69 h⁻¹. (zhu2023afitnesstradeoff pages 3-5) |
| Spo0A phosphorylation | initiates/regulates | sporulation commitment | Guerrero, 2023, DOI 10.3390/microbiolres14020035 | “starting sporulation programs is characterized by the phosphorylation of the master regulator Spo0A” | **Supported review edge**, principally Bacillus. Use Spo0A-P as the active state. (m.2023sporulationstructureassembly pages 4-6) |
| sporulation kinase activity | phosphorylates | Spo0F | Guerrero, 2023 | “These kinases phosphorylate Spo0F” | Bacillar phosphorelay edge; taxon-specific. (m.2023sporulationstructureassembly pages 6-7) |
| Spo0B | transfers phosphate to | Spo0A | Guerrero, 2023 | Spo0F “is used as a substrate by the phosphotransferase Spo0B to phosphorylate Spo0A” | Bacillar phosphorelay edge; do not generalize to all clostridia. (m.2023sporulationstructureassembly pages 6-7) |
| Rap phosphatases | dephosphorylate/inhibit | Spo0F-P signaling | Guerrero, 2023 | “Rap… inhibit this signal transduction pathway by dephosphorylating… Spo0F-P” | Negative regulatory edge. (m.2023sporulationstructureassembly pages 6-7) |
| Phr peptide | inhibits | cognate Rap protein | Guerrero, 2023 | “Rap protein activity inhibited by its related Phr peptide” | Positive indirect edge to Spo0A activation via double inhibition. (m.2023sporulationstructureassembly pages 6-7) |
| **sigF disruption** | blocks | development at asymmetric division | Pereira et al., 2013, DOI 10.1371/journal.pgen.1003782 | “sigF and sigE mutants were blocked at the asymmetric division stage” | **Strong experimental**, *C. difficile* 630Δerm. (pereira2013thesporedifferentiation pages 4-5) |
| **sigE disruption** | blocks | development at asymmetric division | Pereira et al., 2013 | same quotation | **Strong experimental**, *C. difficile*. (pereira2013thesporedifferentiation pages 4-5) |
| **sigF**, **sigE**, or **sigG** disruption | eliminates detectable | heat-resistant spores | Pereira et al., 2013 | “no heat resistant spores were found, at any time point tested” | **Strong assay-backed edge** at 24, 48, and 72 h. Complementation restored heat-resistant spores, strengthening causality. (pereira2013thesporedifferentiation pages 3-4, pereira2013thesporedifferentiation pages 4-5) |
| **sigG disruption** | permits engulfment but blocks | later morphogenesis | Pereira et al., 2013 | “sigG mutant completed the engulfment sequence, but did not proceed further” | Strong stage-specific edge in *C. difficile*. (pereira2013thesporedifferentiation pages 4-5) |
| **sigK disruption** | impairs | late coat assembly | Pereira et al., 2013 | “late stages in the assembly of the coats are under σK control” | Strong species-specific edge. It should not be represented as universally abolishing cortex or all resistant spores. (pereira2013thesporedifferentiation pages 5-7) |
| **sigK disruption** | impairs | mother-cell lysis and spore release | Pereira et al., 2013 | “mother cell remained viable in the sigK mutant”; free spores were “only rarely seen” | Strong late-stage edge in *C. difficile*. (pereira2013thesporedifferentiation pages 5-7) |
| **sigK disruption** | reduces but does not eliminate | heat-resistant-spore formation | Pereira et al., 2013 | mutant yielded approximately 1.76×10³ heat-resistant CFU/mL at 72 h versus 1.56×10⁷ total cells/mL; WT yielded about 1.5×10⁷ heat-resistant CFU/mL | This is a critical warning against `loss of sigK → non-spore forming` as a universal binary edge. (pereira2013thesporedifferentiation pages 4-5) |
| SpoIVCA-mediated skin excision | produces | intact functional **sigK** | Pereira et al., 2013 | excision “is essential for sporulation” | Strong *C. difficile* edge. Premature skinless multicopy sigK also blocked early development, showing that timing matters. (pereira2013thesporedifferentiation pages 5-7) |
| **SpoVD** loss | causes | incomplete polar septum formation | Shrestha et al., 2023, DOI 10.1038/s41467-023-43595-3 | “detected incomplete polar septum formation in ΔspoVD and ΔspoVE” | Strong experimental, *C. difficile*. Spo0A activation remained at WT level, placing the defect downstream of initiation. (shrestha2023diversificationofdivision pages 3-4) |
| **SpoVE** loss | causes | incomplete polar septum formation | Shrestha et al., 2023 | same quotation | Strong experimental, *C. difficile*. (shrestha2023diversificationofdivision pages 3-4) |
| loss of **spoVD** or **spoVE** | reduces | progression beyond asymmetric division | Shrestha et al., 2023 | morphological sporulation frequency was “~3-fold lower than WT” | Strong quantitative edge, but not proof of absolute non-spore-forming capacity. (shrestha2023diversificationofdivision pages 3-4) |
| SpoVD/SpoVE | synthesizes | septal peptidoglycan during asymmetric division | Shrestha et al., 2023 | proteins “play important roles in synthesizing septal PG during asymmetric division” | Strong experimental mechanistic edge; also involved in cortex synthesis. (shrestha2023diversificationofdivision pages 3-4) |
| SigF/SigE | promotes | forespore engulfment | Guerrero, 2023 | “sigma factors (σF, σE) play a role in forespore engulfment” | Review-level Bacillus/Bt edge; retain taxonomic qualifier. (m.2023sporulationstructureassembly pages 6-7) |
| loss of SpoIID/SpoIIM/SpoIIP function | impairs | engulfment | Guerrero, 2023 | “morphological and cytological changes impaired in spoIID, spoIIM, and spoIIP mutants” | Foundational/review-supported edge; individual primary studies should be attached before high-confidence YAML curation. (m.2023sporulationstructureassembly pages 4-6) |
| SpoIVA and SpoVM | provides framework for | coat/cortex envelope assembly | Brantl & Haq, 2023, DOI 10.1093/femsre/fuad064 | “development… relies on the correct assembly of a foundational coat layer comprised of… SpoIVA and SpoVM” | Review-supported *B. subtilis* edge. (brantl2023smallproteinsin pages 9-10) |
| defective envelope assembly | activates CmpA/ClpXP quality control causing | SpoIVA degradation and sporulating-cell lysis | Brantl & Haq, 2023 | “CmpA serves as an adaptor to ClpXP, leading to the degradation of SpoIVA… halts sporulation” | Mechanistically valuable but not a constitutive species trait; curate as an abortive-sporulation branch. (brantl2023smallproteinsin pages 9-10) |
| high glucose | inhibits/reduces | sporulation induction | Bosnar et al., 2023, DOI 10.1099/acmi.0.000419 | “glucose being classified as an inhibitor of sporulation” | **Conditional environmental edge only.** It should not directly imply `METPO:1000872`. (bosnar2023attemptstolimit pages 6-8) |
| low pH (~5) | reduces SigH activity and thereby | transcription of SigH-dependent sporulation genes | Bosnar et al., 2023 | “decreased activity… Sigma H… and subsequent decline in transcription” | Conditional, *B. subtilis*-specific edge. (bosnar2023attemptstolimit pages 6-8) |
| transfer to validated sporulation conditions | reveals | retained sporulation capacity | Bosnar et al., 2023 | “all… tested… isolates… retained the ability to produce spores” | Strong boundary evidence: reversible environmental suppression is not the target trait. (bosnar2023attemptstolimit pages 6-8) |
| lineage-specific loss of many core sporulation genes | contributes to | evolutionary non-spore-forming state | Galperin et al., 2022 | three nonsporeforming Peptostreptococcaceae had “loss of at least 29 of the 40 analyzed genes” | **Comparative inference**, not a single-gene causal edge. Useful as an evolutionary provenance branch. (galperin2022conservationandevolution pages 15-17) |

## Recommended TraitMech graph design

### Minimal high-confidence graph

A defensible initial YAML graph should be smaller than an exhaustive sporulation network:

1. `absence_or_inactivation_of_spo0A` **prevents** `Spo0A-dependent sporulation initiation`.
2. `failed_sporulation_initiation` **prevents** `asymmetric sporulation septation`.
3. `loss_of_sigF_or_sigE_activity` **causes** `arrest_at_asymmetric_division`.
4. `arrest_at_asymmetric_division` **prevents** `forespore_engulfment_completion`.
5. `loss_of_sigG_activity` **causes** `post-engulfment developmental arrest`.
6. `post-engulfment developmental arrest` **prevents** `mature heat-resistant endospore formation`.
7. `failure_to_form_mature_endospores_under_inducing_conditions` **realizes** `METPO:1000872`.

Attach species/evidence annotations to each molecular edge. The terminal phenotype may be shared, but upstream causal routes differ between naturally asporogenous taxa and engineered mutants.

### Optional taxon-specific branches

- **Bacillus branch:** starvation/kinases → Spo0F-P → Spo0B → Spo0A-P; Rap/Phr and Spo0E-family regulation.
- ***C. difficile* branch:** SpoVD/SpoVE → polar septal peptidoglycan → successful asymmetric division; SigK/skinCd → coat completion and mother-cell lysis.
- **Evolutionary-loss branch:** ancestral sporulation machinery → stepwise loss of multiple core modules → stable lineage-level asporogeny.
- **Conditional-suppression branch:** glucose abundance or low pH → reduced sporulation-gene activity → low observed sporulation, explicitly terminating in an assay phenotype rather than `METPO:1000872`.

## Recent developments and relevant data

### 2024 metagenome-based prediction

Machado et al. screened 2,194 vertebrate-host MAGs. Of 934 Firmicutes MAGs, 724 encoded spo0A; 225 lacked family-level assignments, and 146 contained genes spanning all ten sporulation stages considered. Host counts among the 724 Spo0A-positive MAGs were 268 human, 187 cattle, 155 poultry, and 114 swine. These data illustrate the scale of genomic prediction but do not experimentally prove sporulation or non-sporulation. (machado2024uncoveringnewfirmicutes pages 7-10, machado2024uncoveringnewfirmicutes pages 4-7)

Among the 146 selected MAGs, Spo0A-regulon genes were often the most represented module: median proportions included 70% in medium-quality Bacilli MAGs and 60–80% in Clostridia subsets. Again, this supports “sporulation potential,” not phenotype assignment. (machado2024uncoveringnewfirmicutes pages 7-10)

### 2023 division-mechanism work

Shrestha et al. showed that the *C. difficile* dcw-encoded synthases SpoVD and SpoVE are specialized for sporulation-specific septal peptidoglycan synthesis. Their deletion did not prevent Spo0A activation but produced incomplete polar septa and approximately threefold fewer cells progressing through visible sporulation. This adds a mechanistic route to non-sporulating or severely hypomorphic phenotypes downstream of a normal initiation signal. (shrestha2023diversificationofdivision pages 3-4)

### 2023 Spo0A fitness trade-off

Quantitative proteomics in *B. subtilis* captured more than 2,500 proteins. Deleting spo0A abolished spore formation after nutrient depletion, increased growth-associated allocation, and compromised long-term viability. Ribosomal allocation increased from 4.9% to 8%, amino-acid-biosynthetic allocation from 9.7% to 12.9%, and growth rate from 0.41 to 0.69 h⁻¹. This demonstrates that engineered non-sporulation can increase short-term growth while imposing survival costs. (zhu2023afitnesstradeoff pages 3-5, zhu2023afitnesstradeoff pages 2-3)

### Comparative-genomic expert assessment

Galperin and colleagues analyzed 180 Firmicute species from 160 genera, including 76 spore formers. Sporulation in *B. subtilis* can affect more than 500 genes, whereas an approximately 60-gene core is broadly conserved. Nevertheless, individual spore formers can lack presumed core genes, and non-spore formers can retain many sporulation genes. Their central expert conclusion is asymmetric: **absence of spo0A is an excellent predictor of inability, but presence of spo0A is not evidence of ability.** (galperin2022conservationandevolution pages 4-5, galperin2022conservationandevolution pages 1-2)

## Current applications and real-world relevance

1. **Industrial strain engineering.** Blocking sporulation can redirect resources toward growth, enzymes, surfactants, or other products, but the associated long-term viability and stress-resistance losses must be managed. The Spo0A-null proteome-allocation results quantify this trade-off. (zhu2023afitnesstradeoff pages 3-5, zhu2023afitnesstradeoff pages 2-3)
2. **Probiotic design.** Bosnar et al. attempted to create a non-GMO, non-sporulating *B. subtilis* probiotic because durable spores may be undesirable in vulnerable hosts. Their failure to obtain a stable non-sporulator after environmental selection underscores the need for direct genotype and phenotype validation. (bosnar2023attemptstolimit pages 3-4, bosnar2023attemptstolimit pages 6-8)
3. **Food, clinical, and environmental control.** Distinguishing non-spore-forming organisms from low-frequency spore formers changes decontamination requirements because mature endospores withstand stresses that kill vegetative cells. Core sporulation genes are consequently potential intervention targets, although incomplete inhibition may leave resistant or germination-defective spores. (galperin2022conservationandevolution pages 1-2)
4. **Metagenomic ecology and transmission.** Sporulation potential is being inferred in uncultivated gut Firmicutes to study persistence and host-to-host transmission. Such predictions should be labeled “potential” until culture, microscopy, and resistance assays validate them. (machado2024uncoveringnewfirmicutes pages 7-10, machado2024uncoveringnewfirmicutes pages 15-17)
5. **Therapeutic targeting.** The specialized *C. difficile* sporulation divisome, including SpoVD/SpoVE and associated polar-septum components, may offer intervention points distinct from vegetative division. However, reduced sporulation is not equivalent to complete elimination. (shrestha2023diversificationofdivision pages 6-8, shrestha2023diversificationofdivision pages 3-4)

## Ontology-grounding recommendations

- Preserve `METPO:1000872` exactly.
- Ground taxa with NCBITaxon during implementation, but verify strain-level records for *B. subtilis* 168, *C. difficile* 630Δerm, and experimental derivatives rather than assigning species-level identifiers indiscriminately.
- Use GO identifiers only after confirming exact current terms for bacterial sporulation, asymmetric division, engulfment, cortex formation, coat assembly, and mother-cell lysis. No unverified GO CURIE should be inserted.
- Ground glucose, calcium, dipicolinic acid, phosphate, and peptidoglycan to ChEBI only after identifier verification; labels are safer than guessed CURIEs.
- Use taxon-specific UniProt accessions for Spo0A, sigma factors, SpoVD, and SpoVE. Gene symbols alone should be stored with organism context because orthology and regulatory dependencies differ.
- Model experimental perturbations separately from biological entities: `gene deletion`, `insertional disruption`, `CRISPRi`, medium, incubation time, and heat-resistance assay are evidence-context nodes, not intrinsic trait components.

## Warnings: claims not yet ready for TraitMech curation

1. **Do not curate “Spo0A present causes spore formation.”** Forty non-spore formers in the 180-species comparative set encoded spo0A. (galperin2022conservationandevolution pages 4-5)
2. **Do not infer non-spore-forming from one negative stain, one medium, or an early time point.** Sporulation frequency changed from undetectable to 43.8% over 72 h in *C. difficile* and varied by two orders of magnitude between media. (pereira2013thesporedifferentiation pages 3-4)
3. **Do not infer phenotype solely from MAG gene content.** MAG incompleteness, annotation errors, paralogy, missing regulatory context, and retained genes in evolutionary remnants all confound prediction. (galperin2022conservationandevolution pages 15-17, galperin2022conservationandevolution pages 4-5)
4. **Do not universalize the Bacillus phosphorelay.** Many clostridia lack Spo0B/Spo0F and use unrelated orphan kinases. (galperin2022conservationandevolution pages 7-9)
5. **Do not make SigK a universal binary switch for non-spore formation.** In *C. difficile*, sigK mutants retained low numbers of heat-resistant spores and formed cortex, although coat assembly and release were defective. (pereira2013thesporedifferentiation pages 5-7, pereira2013thesporedifferentiation pages 4-5)
6. **Do not equate phase-bright structures with fully functional endospores.** In the *C. difficile sigK* mutant, phase-bright/gray structures were much more frequent than heat-resistant CFU, implying incomplete cortex or defective germination. (pereira2013thesporedifferentiation pages 4-5)
7. **Do not curate high glucose or low pH as stable causes of `METPO:1000872`.** They suppress induction; transfer experiments showed retained capacity. (bosnar2023attemptstolimit pages 6-8)
8. **Treat evolutionary gene-loss edges as inferred.** Comparative reconstruction supports stepwise loss, but individual missing genes are not necessarily causal because sporulation networks contain redundancy and taxon-specific substitutions. (galperin2022conservationandevolution pages 15-17, galperin2022conservationandevolution pages 1-2)
9. **The supplied *Staphylococcus aureus* example supports the taxonomic phenotype but not the proposed Spo0A-cascade mechanism.** *S. aureus* is from a lineage with no known endospore formers; its asporogeny should not automatically be represented as a single recent spo0A knockout-like event. (galperin2022conservationandevolution pages 1-2)

## DOI-first bibliography

1. **Machado DT, et al.** “Uncovering new Firmicutes species in vertebrate hosts through metagenome-assembled genomes with potential for sporulation.” *Microbiology Spectrum*. Published November 2024. DOI: [10.1128/spectrum.02113-24](https://doi.org/10.1128/spectrum.02113-24). (machado2024uncoveringnewfirmicutes pages 7-10)
2. **Voitsekhovsky VG, et al.** “Peculiarities of the Ontogenesis of Bacilli During Development from a Vegetative Cell to a Spore.” *Mikrobiolohichnyi Zhurnal*. Published September 2024. DOI: [10.15407/microbiolj86.04.091](https://doi.org/10.15407/microbiolj86.04.091). (voitsekhovsky2024peculiaritiesofthe pages 3-5)
3. **Shrestha S, et al.** “Diversification of division mechanisms in endospore-forming bacteria revealed by analyses of peptidoglycan synthesis in Clostridioides difficile.” *Nature Communications* 14:7975. Published December 2023. DOI: [10.1038/s41467-023-43595-3](https://doi.org/10.1038/s41467-023-43595-3). (shrestha2023diversificationofdivision pages 3-4)
4. **Zhu M, et al.** “A fitness trade-off between growth and survival governed by Spo0A-mediated proteome allocation constraints in Bacillus subtilis.” *Science Advances* 9:eadg9733. Published 27 September 2023. DOI: [10.1126/sciadv.adg9733](https://doi.org/10.1126/sciadv.adg9733). (zhu2023afitnesstradeoff pages 2-3)
5. **Brantl S, Haq IU.** “Small proteins in Gram-positive bacteria.” *FEMS Microbiology Reviews* 47(6). Published November 2023. DOI: [10.1093/femsre/fuad064](https://doi.org/10.1093/femsre/fuad064). (brantl2023smallproteinsin pages 9-10)
6. **Bosnar LM, et al.** “Attempts to limit sporulation in the probiotic strain Bacillus subtilis BG01-4TM through mutation accumulation and selection.” *Access Microbiology* 5. Published May 2023. DOI: [10.1099/acmi.0.000419](https://doi.org/10.1099/acmi.0.000419). (bosnar2023attemptstolimit pages 3-4)
7. **Guerrero GGM.** “Sporulation, Structure Assembly, and Germination in the Soil Bacterium Bacillus thuringiensis.” *Microbiology Research* 14:466–491. Published April 2023. DOI: [10.3390/microbiolres14020035](https://doi.org/10.3390/microbiolres14020035). (m.2023sporulationstructureassembly pages 4-6)
8. **Galperin MY, et al.** “Conservation and Evolution of the Sporulation Gene Set in Diverse Members of the Firmicutes.” *Journal of Bacteriology* 204(6). Published 31 May 2022. DOI: [10.1128/jb.00079-22](https://doi.org/10.1128/jb.00079-22). (galperin2022conservationandevolution pages 1-2)
9. **Pereira FC, et al.** “The Spore Differentiation Pathway in the Enteric Pathogen Clostridium difficile.” *PLoS Genetics* 9:e1003782. Published October 2013. DOI: [10.1371/journal.pgen.1003782](https://doi.org/10.1371/journal.pgen.1003782). (pereira2013thesporedifferentiation pages 4-5)

## Curation conclusion

The existing 12-node “absent Spo0A cascade” graph captures one valid engineered mechanism but is too narrow for the trait class. The most reliable universal statement is that failure at any indispensable stage—from initiation through septation, engulfment, maturation, or release—can prevent mature endospore production. For a first curated graph, use experimentally supported Spo0A and sigma-factor branches, retain *C. difficile*-specific SpoVD/SpoVE and SigK branches with taxonomic qualifiers, and keep environmental suppression and comparative gene loss as separate uncertain/contextual branches. This structure avoids incorrectly equating a single gene’s presence, temporary assay negativity, or defective germination with the stable trait `METPO:1000872`.

References

1. (pereira2013thesporedifferentiation pages 3-4): Fátima C. Pereira, Laure Saujet, Ana R. Tomé, Mónica Serrano, Marc Monot, Evelyne Couture-Tosi, Isabelle Martin-Verstraete, Bruno Dupuy, and Adriano O. Henriques. The spore differentiation pathway in the enteric pathogen clostridium difficile. PLoS Genetics, 9:e1003782, Oct 2013. URL: https://doi.org/10.1371/journal.pgen.1003782, doi:10.1371/journal.pgen.1003782. This article has 190 citations and is from a domain leading peer-reviewed journal.

2. (bosnar2023attemptstolimit pages 3-4): Luke M. Bosnar, Anya E. Shindler, Jennifer Wood, Craig Patch, and Ashley E. Franks. Attempts to limit sporulation in the probiotic strain bacillus subtilis bg01-4tm through mutation accumulation and selection. Access Microbiology, May 2023. URL: https://doi.org/10.1099/acmi.0.000419, doi:10.1099/acmi.0.000419. This article has 2 citations.

3. (bosnar2023attemptstolimit pages 6-8): Luke M. Bosnar, Anya E. Shindler, Jennifer Wood, Craig Patch, and Ashley E. Franks. Attempts to limit sporulation in the probiotic strain bacillus subtilis bg01-4tm through mutation accumulation and selection. Access Microbiology, May 2023. URL: https://doi.org/10.1099/acmi.0.000419, doi:10.1099/acmi.0.000419. This article has 2 citations.

4. (pereira2013thesporedifferentiation pages 4-5): Fátima C. Pereira, Laure Saujet, Ana R. Tomé, Mónica Serrano, Marc Monot, Evelyne Couture-Tosi, Isabelle Martin-Verstraete, Bruno Dupuy, and Adriano O. Henriques. The spore differentiation pathway in the enteric pathogen clostridium difficile. PLoS Genetics, 9:e1003782, Oct 2013. URL: https://doi.org/10.1371/journal.pgen.1003782, doi:10.1371/journal.pgen.1003782. This article has 190 citations and is from a domain leading peer-reviewed journal.

5. (pereira2013thesporedifferentiation pages 2-3): Fátima C. Pereira, Laure Saujet, Ana R. Tomé, Mónica Serrano, Marc Monot, Evelyne Couture-Tosi, Isabelle Martin-Verstraete, Bruno Dupuy, and Adriano O. Henriques. The spore differentiation pathway in the enteric pathogen clostridium difficile. PLoS Genetics, 9:e1003782, Oct 2013. URL: https://doi.org/10.1371/journal.pgen.1003782, doi:10.1371/journal.pgen.1003782. This article has 190 citations and is from a domain leading peer-reviewed journal.

6. (voitsekhovsky2024peculiaritiesofthe pages 9-10): V.G. Voitsekhovsky, L.V. Avdeeva, O.B. Balko, and O.I. Balko. Peculiarities of the ontogenesis of bacilli during development from a vegetative cell to a spore. Mikrobiolohichnyi Zhurnal, 86:91-105, Sep 2024. URL: https://doi.org/10.15407/microbiolj86.04.091, doi:10.15407/microbiolj86.04.091. This article has 0 citations.

7. (galperin2022conservationandevolution pages 1-2): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 104 citations and is from a peer-reviewed journal.

8. (m.2023sporulationstructureassembly pages 6-7): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 24 citations.

9. (galperin2022conservationandevolution pages 7-9): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 104 citations and is from a peer-reviewed journal.

10. (brantl2023smallproteinsin pages 9-10): Sabine Brantl and Inam Ul Haq. Small proteins in gram-positive bacteria. FEMS Microbiology Reviews, Nov 2023. URL: https://doi.org/10.1093/femsre/fuad064, doi:10.1093/femsre/fuad064. This article has 7 citations and is from a domain leading peer-reviewed journal.

11. (m.2023sporulationstructureassembly pages 7-9): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 24 citations.

12. (zhu2023afitnesstradeoff pages 2-3): Manlu Zhu, Qian Wang, Haoyan Mu, Fei Han, Yanling Wang, and Xiongfeng Dai. A fitness trade-off between growth and survival governed by spo0a-mediated proteome allocation constraints in <i>bacillus subtilis</i>. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adg9733, doi:10.1126/sciadv.adg9733. This article has 33 citations and is from a highest quality peer-reviewed journal.

13. (zhu2023afitnesstradeoff pages 3-5): Manlu Zhu, Qian Wang, Haoyan Mu, Fei Han, Yanling Wang, and Xiongfeng Dai. A fitness trade-off between growth and survival governed by spo0a-mediated proteome allocation constraints in <i>bacillus subtilis</i>. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adg9733, doi:10.1126/sciadv.adg9733. This article has 33 citations and is from a highest quality peer-reviewed journal.

14. (pereira2013thesporedifferentiation pages 9-10): Fátima C. Pereira, Laure Saujet, Ana R. Tomé, Mónica Serrano, Marc Monot, Evelyne Couture-Tosi, Isabelle Martin-Verstraete, Bruno Dupuy, and Adriano O. Henriques. The spore differentiation pathway in the enteric pathogen clostridium difficile. PLoS Genetics, 9:e1003782, Oct 2013. URL: https://doi.org/10.1371/journal.pgen.1003782, doi:10.1371/journal.pgen.1003782. This article has 190 citations and is from a domain leading peer-reviewed journal.

15. (pereira2013thesporedifferentiation pages 5-7): Fátima C. Pereira, Laure Saujet, Ana R. Tomé, Mónica Serrano, Marc Monot, Evelyne Couture-Tosi, Isabelle Martin-Verstraete, Bruno Dupuy, and Adriano O. Henriques. The spore differentiation pathway in the enteric pathogen clostridium difficile. PLoS Genetics, 9:e1003782, Oct 2013. URL: https://doi.org/10.1371/journal.pgen.1003782, doi:10.1371/journal.pgen.1003782. This article has 190 citations and is from a domain leading peer-reviewed journal.

16. (shrestha2023diversificationofdivision pages 3-4): Shailab Shrestha, Najwa Taib, Simonetta Gribaldo, and Aimee Shen. Diversification of division mechanisms in endospore-forming bacteria revealed by analyses of peptidoglycan synthesis in clostridioides difficile. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43595-3, doi:10.1038/s41467-023-43595-3. This article has 23 citations and is from a highest quality peer-reviewed journal.

17. (galperin2022conservationandevolution pages 4-5): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 104 citations and is from a peer-reviewed journal.

18. (galperin2022conservationandevolution pages 15-17): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Journal of Bacteriology, Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 104 citations and is from a peer-reviewed journal.

19. (m.2023sporulationstructureassembly pages 4-6): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 24 citations.

20. (machado2024uncoveringnewfirmicutes pages 7-10): Douglas Terra Machado, Beatriz do Carmo Dias, Rodrigo Cayô, Ana Cristina Gales, Fabíola Marques de Carvalho, and Ana Tereza Ribeiro Vasconcelos. Uncovering new <i>firmicutes</i> species in vertebrate hosts through metagenome-assembled genomes with potential for sporulation. Microbiology Spectrum, Nov 2024. URL: https://doi.org/10.1128/spectrum.02113-24, doi:10.1128/spectrum.02113-24. This article has 10 citations and is from a domain leading peer-reviewed journal.

21. (machado2024uncoveringnewfirmicutes pages 4-7): Douglas Terra Machado, Beatriz do Carmo Dias, Rodrigo Cayô, Ana Cristina Gales, Fabíola Marques de Carvalho, and Ana Tereza Ribeiro Vasconcelos. Uncovering new <i>firmicutes</i> species in vertebrate hosts through metagenome-assembled genomes with potential for sporulation. Microbiology Spectrum, Nov 2024. URL: https://doi.org/10.1128/spectrum.02113-24, doi:10.1128/spectrum.02113-24. This article has 10 citations and is from a domain leading peer-reviewed journal.

22. (machado2024uncoveringnewfirmicutes pages 15-17): Douglas Terra Machado, Beatriz do Carmo Dias, Rodrigo Cayô, Ana Cristina Gales, Fabíola Marques de Carvalho, and Ana Tereza Ribeiro Vasconcelos. Uncovering new <i>firmicutes</i> species in vertebrate hosts through metagenome-assembled genomes with potential for sporulation. Microbiology Spectrum, Nov 2024. URL: https://doi.org/10.1128/spectrum.02113-24, doi:10.1128/spectrum.02113-24. This article has 10 citations and is from a domain leading peer-reviewed journal.

23. (shrestha2023diversificationofdivision pages 6-8): Shailab Shrestha, Najwa Taib, Simonetta Gribaldo, and Aimee Shen. Diversification of division mechanisms in endospore-forming bacteria revealed by analyses of peptidoglycan synthesis in clostridioides difficile. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43595-3, doi:10.1038/s41467-023-43595-3. This article has 23 citations and is from a highest quality peer-reviewed journal.

24. (voitsekhovsky2024peculiaritiesofthe pages 3-5): V.G. Voitsekhovsky, L.V. Avdeeva, O.B. Balko, and O.I. Balko. Peculiarities of the ontogenesis of bacilli during development from a vegetative cell to a spore. Mikrobiolohichnyi Zhurnal, 86:91-105, Sep 2024. URL: https://doi.org/10.15407/microbiolj86.04.091, doi:10.15407/microbiolj86.04.091. This article has 0 citations.