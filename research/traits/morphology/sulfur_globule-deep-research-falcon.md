---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:17:01.475371'
end_time: '2026-08-04T10:23:24.427110'
duration_seconds: 382.95
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: sulfur globule
  trait_identifier: traitmech:000069
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sulfur_globule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular (or periplasmic) inclusion of elemental sulfur formed
    as an intermediate during the oxidation of reduced sulfur compounds, characteristic
    of many sulfur-oxidizing and phototrophic sulfur bacteria.
  parent_traits: traitmech:000066
  synonyms: sulfur inclusion
  evidence_summary: 'DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe
    sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism
    in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening
    & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)'
  causal_graph_summary: 'sulfur_globule_sulfur_oxidation_intermediate: 8 nodes, 6
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur globule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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
- **Trait label:** sulfur globule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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


# Curation-focused research report: sulfur globule

**Trait:** `traitmech:000069`  
**Category:** MORPHOLOGY | **Term kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** `traitmech:000066`  
**Synonym:** sulfur inclusion

## 1. Scope and current interpretation

For TraitMech, a **sulfur globule** should denote a cell-associated, microscopically discernible inclusion enriched in zero-valent/elemental sulfur, formed during oxidation of reduced sulfur compounds. It may be **cytoplasmic** or **periplasmic (intracellular but extracytoplasmic)** and ordinarily represents a transient metabolic intermediate or reserve that can subsequently be oxidized. In *Allochromatium vinosum*, globules are obligatory periplasmic intermediates of oxidative sulfur metabolism; in SQR-containing aerobic bacteria, S8 can instead aggregate in the cytoplasm. These are mechanistically distinct realizations of the same high-level morphology (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3, kumpel2023cellbiologyof pages 1-3).

The graph should not imply that all sulfur globules share one coat, localization, chemical allotrope, or downstream oxidation pathway. Classical Sgp-coated globules are best established in *A. vinosum*, whereas *Beggiatoa leptomitoformis* D-402 uses a distinct PDO/Sox-associated route and lacks several canonical sulfur-oxidation systems (rudenko2024mechanismofintracellular pages 10-12, kumpel2023cellbiologyof pages 1-3).

### Boundary cases

1. **Extracellular biogenic S(0): exclude from this trait.** *Chlorobaculum tepidum* uses extracellular biogenic sulfur particles requiring direct cell contact and oxidizes them to sulfate. These are substrates outside the cell, not intracellular/periplasmic inclusions (hanson2016chlorobaculumtepidumgrowth pages 5-6).
2. **Desulfurase encapsulins: exclude or model as a sibling trait.** The 2024 system is a 24-nm, T=1 icosahedral protein nanocompartment containing cysteine desulfurase and crystalline S0. Its cysteine-derived sulfur, ordered shell, nanoscale architecture, and proposed assimilatory/detoxification role distinguish it from lithotrophic sulfur globules (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 1-2, benisch2024awidespreadbacterial pages 3-4).
3. **Visible extracellular sulfur deposits adjacent to cells:** do not infer `traitmech:000069` without localization evidence.
4. **Generic “sulfur granule” annotations:** insufficient unless microscopy, fractionation, or localization establishes a cell-associated inclusion.

| candidate mechanism/edge | exemplar taxon | evidence strength | curate now? | key caveat |
|---|---|---|---|---|
| Sulfur globule envelope proteins SgpA/SgpB/SgpC support classical periplasmic sulfur globule formation/expansion; rDsr supports downstream oxidation of stored sulfur | *Allochromatium vinosum* | Strong for this taxon; direct microscopy/genetic evidence (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10) | Yes, as taxon-scoped edges | 2023 source is a preprint; avoid overgeneralizing to all sulfur bacteria without broader evidence (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10) |
| SQR-catalyzed sulfide oxidation produces polysulfides that spontaneously yield S8, which aggregates into cytoplasmic sulfur globules | *Corynebacterium vitaeruminis* DSM 20294; recombinant *Escherichia coli* | Strong for SQR-to-S8 cytoplasmic route in tested systems (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3) | Yes, but mark as non-classical/taxon-contextual | Represents a cytoplasmic aerobic route distinct from classical periplasmic Sgp-coated globules; engineered *E. coli* evidence should not be treated as native species-wide trait evidence (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3) |
| Intracellular sulfur oxidation uses PDO to oxidize stored sulfur to sulfite, with thiosulfate then oxidized by periplasmic Sox system | *Beggiatoa leptomitoformis* D-402 | Moderate to strong; multi-omic and biochemical support in one species (rudenko2024mechanismofintracellular pages 10-12) | Yes, as uncertain/taxon-specific consumption pathway edges | Mechanism is unusual because this strain lacks canonical Dsr/SOR routes; formation steps are less directly established than oxidation steps (rudenko2024mechanismofintracellular pages 10-12) |
| Direct utilization of extracellular biogenic S(0) globules as electron donor | *Chlorobaculum tepidum* | Strong for extracellular sulfur use, not for sulfur globule trait itself (hanson2016chlorobaculumtepidumgrowth pages 5-6) | No | Boundary case: evidence concerns extracellular biogenic sulfur particles requiring cell contact, not intracellular/periplasmic sulfur globules matching traitmech:000069 (hanson2016chlorobaculumtepidumgrowth pages 5-6) |
| Cysteine-desulfurase encapsulin stores elemental sulfur inside a 24-nm protein nanocompartment | desulfurase-encapsulin bacteria (broad distribution) | Strong for encapsulin sulfur storage as a distinct compartment (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 8-9, benisch2024awidespreadbacterial pages 6-7, benisch2024awidespreadbacterial pages 4-6, benisch2024awidespreadbacterial pages 1-2, benisch2024awidespreadbacterial pages 3-4) | No | Distinct boundary case: ordered protein nanocompartment, cysteine-derived sulfur donor, likely detoxification/assimilatory role, and nanometer-scale shell differ from classical sulfur globules used in sulfur oxidation metabolism (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 1-2) |


*Table: This table summarizes which sulfur-storage mechanisms are strong candidates for TraitMech curation of traitmech:000069 and which are better treated as boundary cases. It helps separate classical sulfur globules from related but mechanistically distinct sulfur inclusions or extracellular sulfur particles.*

## 2. Candidate nodes grouped by type

### Focal morphology and localization

| Node | Type | Suggested grounding |
|---|---|---|
| sulfur globule | morphology | `traitmech:000069` |
| sulfur-globule envelope | cellular structure | Label only |
| cytoplasm | localization | `GO:0005737` |
| periplasmic space | localization | `GO:0042597` |
| extracellular biogenic sulfur particle | boundary morphology | Label only; exclude from focal trait |
| desulfurase encapsulin | protein nanocompartment/boundary case | Label only pending system-specific grounding |

### Chemicals and metabolites

Use label-only nodes until the exact ChEBI record and protonation state have been curator-verified:

- hydrogen sulfide/sulfide;
- thiosulfate;
- elemental sulfur, S0;
- octasulfur, S8;
- short- and long-chain inorganic polysulfides;
- organic polysulfides;
- sulfane sulfur;
- glutathione and glutathione persulfide;
- sulfite;
- sulfate;
- L-cysteine, relevant to the excluded encapsulin system.

### Proteins, enzymes, and complexes

- sulfide:quinone oxidoreductase (**SQR**);
- sulfur-globule proteins **SgpA, SgpB, SgpC, SgpD**;
- Sec-dependent protein-export machinery/signal peptide;
- reverse dissimilatory sulfite reductase system (**rDsr**), including **DsrAB**;
- persulfide dioxygenase (**PDO**);
- Sox sulfur-oxidation system, particularly **SoxAX, SoxB, SoxY** in the *B. leptomitoformis* study;
- cysteine desulfurase and encapsulin shell—boundary-case nodes only.

Exact UniProt, EC, Rhea, and KEGG identifiers should be assigned only after strain-specific sequence or reaction verification. “SQR,” “PDO,” and “Sox system” each encompass families or modules for which a single generic identifier could overstate biochemical specificity.

### Processes and modules

- oxidation of sulfide to polysulfide;
- spontaneous formation of S8 from polysulfides;
- aggregation of S8 into a cytoplasmic globule;
- formation and expansion of a periplasmic sulfur globule;
- storage of sulfur oxidation intermediate;
- mobilization/oxidation of globular sulfur;
- reverse Dsr sulfur oxidation;
- PDO-mediated persulfide oxidation;
- Sox-mediated thiosulfate oxidation to sulfate;
- anoxygenic photolithotrophy;
- aerobic chemolithotrophy/heterotrophic sulfide detoxification.

### Environmental and experimental factors

- availability and concentration of sulfide or thiosulfate;
- availability of an appropriate terminal electron acceptor or phototrophic energy source;
- excess sulfide relative to immediate downstream oxidation capacity;
- cellular glutathione status;
- sulfur-source depletion or transition to endogenous sulfur-supported growth;
- microscopy localization, Raman spectroscopy, XPS/EDS, and sulfur-speciation assays;
- genetic deletion, insertional inactivation, and heterologous SQR expression.

## 3. Candidate causal edges

The snippets below are concise evidence extracts or close source-backed summaries. Predicates should be normalized to the TraitMech relation vocabulary during YAML implementation.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| sulfide | is oxidized by | SQR | Wang 2022: SQR “oxidized H2S into short-chain inorganic polysulfide … and organic polysulfide” (wang2022thepathwayof pages 1-3) | **Curate**, but taxon/context scope is required. |
| SQR activity | produces | polysulfide intermediates | SQR-dependent H2S oxidation generated inorganic and organic polysulfides (wang2022thepathwayof pages 1-3) | **Curate** for the cytoplasmic S8 route. |
| polysulfide intermediates | yield | octasulfur (S8) | Long-chain products ultimately produced S8; S8 comprised >70% of measured cellular sulfane sulfur (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3) | **Curate**; some steps are spontaneous rather than enzyme-catalyzed. |
| S8 | aggregates into | sulfur globule | “S8 spontaneously aggregates into globules” in the bacterial cytoplasm (wang2022thepathwayof pages 1-3) | **Strong edge** for tested aerobic systems. |
| sulfide concentration | positively regulates above an observed threshold | cytoplasmic sulfur-globule formation | At OD600 2.0, approximately 100 µM sulfide was required before globules/S8 were observed (wang2022thepathwayof pages 3-4) | **Assay-specific**; do not encode 100 µM as a universal threshold. |
| SQR | is required for | S8 globule production | Empty-vector *E. coli* accumulated <100 µM sulfane sulfur and no S8, unlike SQR-expressing cells (wang2022thepathwayof pages 3-4) | **Strong in the engineered system**; native generalization uncertain. |
| sulfur globule | located in | cytoplasm | CTAB-dependent probe access and microscopy placed 0.2–0.4-µm globules intracellularly (wang2022thepathwayof pages 3-4) | Curate for *C. vitaeruminis* and engineered *E. coli*, not universally. |
| SgpA/SgpB/SgpC | form or support | sulfur-globule envelope | *A. vinosum* globule envelope contains three highly hydrophobic proteins; SgpA and SgpB can replace one another (kumpel2023cellbiologyof pages 1-3) | **Strong, taxon-specific.** Use `part_of` or `contributes_to_formation_of`, not generic catalysis. |
| SgpA | functionally overlaps with | SgpB | SgpA and SgpB were described as interchangeable/redundant in the presence of SgpC (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10) | Curate as redundancy only if relation vocabulary supports it. |
| SgpC | promotes | sulfur-globule expansion | SgpC “participates in globule expansion” (kumpel2023cellbiologyof pages 1-3) | **Curate**, *A. vinosum*-scoped. |
| loss of SgpB and SgpC | prevents | sulfur-inclusion formation and sulfide/thiosulfate oxidation | Double mutants could not form inclusions or oxidize sulfide/thiosulfate (kumpel2023cellbiologyof pages 7-10) | Strong genetic evidence, but the combined deletion does not resolve every individual contribution. |
| Sec signal peptide of SgpD | targets | SgpD to periplasm | SgpD-mCherry carrying its native Sec signal was periplasmic and colocalized with sulfur deposits (kumpel2023cellbiologyof pages 1-3) | Curate localization/targeting; oxygen maturation of mCherry is an assay condition, not native biology. |
| SgpD | associates with | sulfur globule | Fluorescent SgpD colocalized with sulfur deposits and was abundant in enriched globules (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10) | Curate association, not necessity. |
| SgpD | is not required for | sulfur-globule formation/degradation | Inactivation retained normal formation, size, quantity, and sulfur-oxidation capacity (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10) | Preserve as a **negative finding**; do not create a positive “SgpD causes formation” edge. |
| reduced-sulfur oxidation | produces | periplasmic sulfur globule | In *A. vinosum*, globules are obligatory intracellular but extracytoplasmic intermediates of sulfur oxidation (kumpel2023cellbiologyof pages 1-3) | Strong high-level edge, taxon-scoped. |
| rDsr/DsrAB system | enables | further oxidation of stored globular sulfur | The rDsr system, including rDsrAB, is essential for subsequent cytoplasmic sulfur oxidation (kumpel2023cellbiologyof pages 1-3) | Curate for *A. vinosum*; transport/mobilization across the membrane remains mechanistically incomplete. |
| endogenous sulfur | is oxidized by | PDO | Recombinant PDO used glutathione persulfide, and PDO was detected during growth on endogenous sulfur (rudenko2024mechanismofintracellular pages 10-12) | **Taxon-specific; moderate-to-strong.** Substrate linkage includes inference. |
| PDO-mediated sulfur oxidation | produces | sulfite | The proposed *B. leptomitoformis* mechanism converts sulfane sulfur to sulfite (rudenko2024mechanismofintracellular pages 10-12) | Curate as **uncertain/proposed** unless the YAML supports evidence qualifiers. |
| sulfite plus sulfane sulfur | forms | thiosulfate | Chemical reaction was proposed to connect PDO output to Sox processing (rudenko2024mechanismofintracellular pages 10-12) | **Uncertain mechanistic edge.** |
| thiosulfate | is oxidized by | Sox system | Sox genes were induced 8.6–15-fold during endogenous-sulfur growth; proposed periplasmic Sox oxidation yields sulfate (rudenko2024mechanismofintracellular pages 10-12) | Curate as taxon-specific and partly inferred; expression alone is not direct flux proof. |
| sulfur globule mobilization | supports | prolonged chemolithoautotrophic growth | Over 24 days, stored sulfur declined during growth, with thiosulfate and sulfate detected (rudenko2024mechanismofintracellular pages 10-12) | Curate phenotype-to-process association; later reaccumulation after day 14 complicates a simple monotonic edge. |

## 4. Quantitative findings and recent developments

### 2023–2024 advances

- **Direct protein localization in *A. vinosum* (2023):** SgpD-mCherry was targeted to the periplasm and colocalized with refractile sulfur deposits. The reporter required approximately 60 minutes of oxygen exposure for fluorophore maturation, demonstrating a workable localization method for an anaerobically growing phototroph. Globules can reach about 1 µm and account for up to 34% of cell dry mass (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10).
- **Alternative intracellular-sulfur oxidation in *Beggiatoa* (2024):** stored sulfur can reach 70% of dry cell mass. During endogenous-sulfur growth, soxAX/soxB/soxY expression rose 8.6–15-fold. The work supports a PDO-to-sulfite/thiosulfate-to-Sox model in a strain lacking Dsr, sHdr/rDsr, and SOR genes, showing that sulfur-globule consumption is not mechanistically uniform (rudenko2024mechanismofintracellular pages 10-12).
- **Encapsulin boundary clarified (2024):** each 24-nm shell can contain approximately 150,000 sulfur atoms; sulfur puncta are 10–15 nm and occupy about 50% of the lumen. Encapsulated desulfurase had a threefold higher turnover than free enzyme (0.147 versus 0.046 s−1). These striking statistics describe a distinct nanocompartment, not evidence that classical sulfur globules are encapsulins (benisch2024awidespreadbacterial pages 8-9, benisch2024awidespreadbacterial pages 6-7, benisch2024awidespreadbacterial pages 4-6, benisch2024awidespreadbacterial pages 1-2).

### Earlier but mechanistically important data

In the 2022 SQR study, cytoplasmic globules were 0.2–0.4 µm and S8 constituted more than 70% of cellular sulfane sulfur. These results support an experimentally tractable minimal pathway—SQR, polysulfides, spontaneous S8 formation, and aggregation—but derive partly from recombinant *E. coli* and therefore should not be generalized as the canonical pathway for all sulfur bacteria (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3).

## 5. Applications and real-world relevance

1. **Sulfide detoxification and sulfur recovery.** Engineering SQR-containing heterotrophs could convert toxic H2S into comparatively benign, recoverable S8 globules. This is a proof-of-concept application rather than an established industrial implementation (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3).
2. **Biological desulfurization process control.** Globule accumulation records imbalance between reduced-sulfur oxidation and downstream sulfur mobilization. Globule abundance, size, and chemical state could therefore be phenotyping targets for optimizing sulfide-removal reactors.
3. **Environmental sulfur cycling.** Sulfur inclusions can comprise 34–70% of cell dry mass in studied organisms, making them substantial transient reservoirs that uncouple sulfide oxidation from final sulfate production (rudenko2024mechanismofintracellular pages 10-12, kumpel2023cellbiologyof pages 1-3).
4. **Single-cell metabolic monitoring.** Fluorescence localization and sulfur-sensitive spectroscopic approaches enable temporal measurement of globule formation and consumption. Assay observations must be distinguished from constitutive taxonomy-level traits.
5. **Biomaterial and nanocompartment engineering.** The encapsulin study shows a route to protected intracellular sulfur storage, but it should motivate a separate causal graph rather than be merged into the classical sulfur-globule graph (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 8-9, benisch2024awidespreadbacterial pages 6-7).

## 6. Recommended YAML graph architecture

A single universal linear pathway would be misleading. Prefer a shared phenotype node with three taxon-qualified mechanistic branches:

1. **Classical phototrophic/periplasmic branch:** reduced sulfur → periplasmic Sgp-coated globule → rDsr-dependent mobilization/oxidation.
2. **Aerobic cytoplasmic S8 branch:** sulfide → SQR → polysulfides → spontaneous S8 → cytoplasmic globule.
3. ***Beggiatoa leptomitoformis* branch:** stored sulfane sulfur → PDO → sulfite → chemically generated thiosulfate → periplasmic Sox system → sulfate, with the middle connections marked uncertain.

Taxon, localization, and evidence qualifiers should be attached to every branch. Negative evidence for SgpD should be retained in notes or an explicit `not_required_for` relation if supported by the schema.

## 7. Warnings: claims not yet ready for unqualified curation

- Do not assert that **all sulfur globules are periplasmic**, Sgp-coated, or composed predominantly of S8.
- Do not assert that **SgpD causes globule formation**; deletion evidence shows it is dispensable in *A. vinosum* (kumpel2023cellbiologyof pages 7-10).
- Do not merge extracellular *Chlorobaculum* biogenic sulfur with `traitmech:000069`; direct-contact utilization and sulfate production do not establish an intracellular inclusion (hanson2016chlorobaculumtepidumgrowth pages 5-6).
- Do not merge desulfurase encapsulins with classical globules solely because both contain S0 (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 1-2).
- Treat the complete PDO→sulfite→thiosulfate→Sox chain as **proposed and species-specific**. Proteomics, RT-qPCR, recombinant activity, and products support it, but not every intracellular transfer step was directly observed (rudenko2024mechanismofintracellular pages 10-12).
- The approximately 100-µM sulfide threshold is condition-specific, not a universal ecological cutoff (wang2022thepathwayof pages 3-4).
- Avoid assigning exact EC, UniProt, Rhea, KEGG, ChEBI, or NCBITaxon CURIEs without strain/reaction verification. Label-only nodes are safer than incorrect identifiers.
- The retrieved 2023 SgpD evidence included a preprint DOI; the corresponding peer-reviewed article is Kümpel et al., *Microorganisms* 11:1792, DOI below. Curators should cite the journal version in the YAML.

## 8. DOI-first bibliography

1. **Rudenko TS et al.** “Mechanism of Intracellular Elemental Sulfur Oxidation in *Beggiatoa leptomitoformis*, Where Persulfide Dioxygenase Plays a Key Role.” *International Journal of Molecular Sciences* 25, 10962. **Published October 2024.** https://doi.org/10.3390/ijms252010962 (rudenko2024mechanismofintracellular pages 10-12)
2. **Benisch R, Andreas MP, Giessen TW.** “A widespread bacterial protein compartment sequesters and stores elemental sulfur.” *Science Advances* 10. **Published February 2024.** https://doi.org/10.1126/sciadv.adk9345 (benisch2024awidespreadbacterial pages 9-10, benisch2024awidespreadbacterial pages 1-2)
3. **Kümpel C, Grein F, Dahl C.** “Fluorescence Microscopy Study of the Intracellular Sulfur Globule Protein SgpD in the Purple Sulfur Bacterium *Allochromatium vinosum*.” *Microorganisms* 11, 1792. **Published July 2023.** https://doi.org/10.3390/microorganisms11071792. Retrieved full-text evidence was from the June 2023 preprint, https://doi.org/10.20944/preprints202306.1429.v1 (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 7-10)
4. **Wang T et al.** “The Pathway of Sulfide Oxidation to Octasulfur Globules in the Cytoplasm of Aerobic Bacteria.” *Applied and Environmental Microbiology* 88. **Published February 2022.** https://doi.org/10.1128/AEM.01941-21 (wang2022thepathwayof pages 3-4, wang2022thepathwayof pages 1-3)
5. **Hanson TE et al.** “*Chlorobaculum tepidum* Growth on Biogenic S(0) as the Sole Photosynthetic Electron Donor.” *Environmental Microbiology* 18:2856–2867. **Published September 2016.** https://doi.org/10.1111/1462-2920.12995 (hanson2016chlorobaculumtepidumgrowth pages 5-6)

### Bottom-line curation recommendation

Curate `traitmech:000069` as a localization-flexible elemental-sulfur inclusion phenotype and represent its mechanisms as taxon-qualified branches. The strongest immediate edges are **SQR→polysulfides→S8→cytoplasmic globule**, **SgpA/B/C→periplasmic globule structure/expansion**, and **rDsr→stored-sulfur oxidation**. Add the *Beggiatoa* PDO/Sox branch with uncertainty qualifiers, and explicitly exclude extracellular biogenic sulfur and cysteine-desulfurase encapsulins from the focal class.

References

1. (wang2022thepathwayof pages 3-4): Tianqi Wang, Mingxue Ran, Xiaoju Li, Yequn Liu, Yufeng Xin, Honglei Liu, Huaiwei Liu, Yongzhen Xia, and Luying Xun. The pathway of sulfide oxidation to octasulfur globules in the cytoplasm of aerobic bacteria. Feb 2022. URL: https://doi.org/10.1128/aem.01941-21, doi:10.1128/aem.01941-21. This article has 45 citations and is from a peer-reviewed journal.

2. (wang2022thepathwayof pages 1-3): Tianqi Wang, Mingxue Ran, Xiaoju Li, Yequn Liu, Yufeng Xin, Honglei Liu, Huaiwei Liu, Yongzhen Xia, and Luying Xun. The pathway of sulfide oxidation to octasulfur globules in the cytoplasm of aerobic bacteria. Feb 2022. URL: https://doi.org/10.1128/aem.01941-21, doi:10.1128/aem.01941-21. This article has 45 citations and is from a peer-reviewed journal.

3. (kumpel2023cellbiologyof pages 1-3): Carolin Kümpel, Fabian Grein, and Christiane Dahl. Cell biology of a purple sulfur bacterium: fluorescence micros-copy of intracellular sulfur globules in allochromatium vinosum. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.1429.v1, doi:10.20944/preprints202306.1429.v1.

4. (rudenko2024mechanismofintracellular pages 10-12): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

5. (hanson2016chlorobaculumtepidumgrowth pages 5-6): Thomas E. Hanson, Ernest Bonsu, Amalie Tuerk, Cassandra L. Marnocha, Deborah H. Powell, and Clara S. Chan. Chlorobaculum tepidum growth on biogenic s(0) as the sole photosynthetic electron donor. Environmental microbiology, 18 9:2856-67, Sep 2016. URL: https://doi.org/10.1111/1462-2920.12995, doi:10.1111/1462-2920.12995. This article has 35 citations and is from a domain leading peer-reviewed journal.

6. (benisch2024awidespreadbacterial pages 9-10): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.

7. (benisch2024awidespreadbacterial pages 1-2): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (benisch2024awidespreadbacterial pages 3-4): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (kumpel2023cellbiologyof pages 7-10): Carolin Kümpel, Fabian Grein, and Christiane Dahl. Cell biology of a purple sulfur bacterium: fluorescence micros-copy of intracellular sulfur globules in allochromatium vinosum. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.1429.v1, doi:10.20944/preprints202306.1429.v1.

10. (benisch2024awidespreadbacterial pages 8-9): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.

11. (benisch2024awidespreadbacterial pages 6-7): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (benisch2024awidespreadbacterial pages 4-6): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 28 citations and is from a highest quality peer-reviewed journal.