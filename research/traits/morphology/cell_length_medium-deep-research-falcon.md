---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:37:57.266915'
end_time: '2026-08-04T07:44:30.852684'
duration_seconds: 393.59
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length medium
  trait_identifier: METPO:1000885
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length_medium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-length phenotype in which the longer cell dimension lies approximately
    between 2 and 3 micrometers.
  parent_traits: METPO:1000881
  synonyms: L_2_3
  evidence_summary: 'DOI:10.1126/science.aaa1313: cell size scales with growth rate
    (Growth-rate-dependent size law supports medium cell length as a typical outcome
    at moderate growth rates.)'
  causal_graph_summary: 'cell_length_medium_growth_rate: 13 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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
- **Trait label:** cell length medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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


# Curation-focused research report: microbial **cell length medium**

## Executive assessment

The target is the reviewed morphology class **`METPO:1000885`**, defined as a cell-length phenotype in which the longer cellular dimension is approximately **2–3 µm**; its parent is `METPO:1000881`, and its synonym is `L_2_3`. It should be modeled as an **assay-observed categorical endpoint**, not as a pathway, physiological capacity, or intrinsic species constant.

The strongest mechanistic graph is a balance between (i) lateral envelope growth/elongation and biomass synthesis and (ii) FtsZ-dependent cytokinesis. Nutrient status can shift that balance through UDP-glucose–OpgH/UgtP regulation, ppGpp, central-carbon flux, and fatty-acid synthesis. Min and nucleoid-occlusion systems constrain where division occurs, while DNA-damage responses such as SulA can arrest division and produce cells far longer than the target range. However, none of the retrieved studies directly establishes that a particular mechanism *causes the exact 2–3 µm class*. Therefore, mechanistic edges should generally terminate in continuous processes such as **cell elongation**, **division timing**, or **cell length**, followed by a carefully marked inferred classification edge to `METPO:1000885`.

## 1. Trait scope and boundary cases

### Intended scope

`METPO:1000885` represents an individual-cell or population-summary observation in which the **longer dimension** is approximately 2–3 µm. Curated observations should record:

- taxon and strain;
- growth medium, carbon source, temperature, aeration and growth phase;
- whether 2–3 µm describes individual cells, a mean/median, or a binned population fraction;
- imaging method and segmentation convention, including whether poles are included;
- treatment, genotype and sampling time.

### Important exclusions

1. **Width and volume are not length.** Nutrient and metabolic perturbations can change length, width and volume unequally. For example, a *Bacillus subtilis* study reported widths of approximately **0.92–1.16 µm**, while lengths ranged from **3.5–12.7 µm** across conditions; a generic “size” edge therefore cannot automatically be translated into a 2–3 µm length edge. (ojkic2021bacterialcellshape pages 1-2)
2. **Rod shape is not medium length.** MreB-dependent lateral wall synthesis supports rod morphology, but does not by itself specify a 2–3 µm endpoint. (westfall2017bacterialcellsize pages 11-12)
3. **Filaments are outside scope.** Division arrest through FtsZ inhibition can generate elongated or filamentous cells and should normally point away from `METPO:1000885`.
4. **Coccoid, branched, helical, filamentous and pleomorphic organisms require morphology-specific measurement rules.** “Longer dimension” may not correspond to the rod-axis length used in *E. coli* studies.
5. **L-forms are a special assay context.** Recent evidence that FtsZ plus Min or nucleoid occlusion restores uniform morphology in wall-less *E. coli* is mechanistically informative but should not be generalized without a taxon/context qualifier. (hayashi2024septalwallsynthesis pages 1-2)

## 2. Current mechanistic understanding

The classical nutrient growth law associates nutrient-supported growth with larger bacterial cells, but modern work shows that growth rate alone is insufficient. In a systematic *E. coli* central-metabolism screen, no simple universal growth-rate–size relationship was observed across mutants in LB or glucose minimal medium. Instead, multiple metabolic and cell-cycle pathways contributed independently. (westfall2018comprehensiveanalysisof pages 17-18)

A well-supported pathway in *E. coli* and *B. subtilis* is:

**nutrient-rich condition → increased UDP-glucose signaling → OpgH/UgtP interaction with FtsZ → reduced/delayed FtsZ assembly → delayed cytokinesis → increased cell size/length.**

Defects in OpgH, UgtP or associated UDP-glucose-production enzymes reduce cell size by approximately **15–30%** with little effect on growth rate. UDP-glucose-linked regulation was estimated to explain **25–35%** of the size difference between nutrient-rich and nutrient-poor conditions. A modest approximately **20% reduction in FtsZ** can substantially affect exponential-phase size. (westfall2017bacterialcellsize pages 9-11, vadia2015growthrateand pages 4-6)

Conversely, starvation-associated **(p)ppGpp** is negatively associated with size. Experimental induction by serine hydroxamate or RelA overexpression reduces both length and width in nutrient-rich medium. Fatty-acid synthesis also contributes: `fabH` perturbation reduced *E. coli* volume by as much as **70%** in rich medium, although this is evidence about volume rather than an isolated length endpoint. (westfall2017bacterialcellsize pages 11-12, vadia2015growthrateand pages 4-6)

FtsZ remains the central cytokinetic scaffold. It polymerizes at the division site to form the Z-ring, while MinC inhibits ectopic FtsZ polymerization and SlmA/Noc prevent assembly over unsegregated nucleoids. These spatial systems influence division symmetry and daughter-cell dimensions rather than directly selecting a 2–3 µm target. (meunier2021bacterialcellproliferation pages 22-24, cameron2024insightsintothe pages 3-4, jun2018fundamentalprinciplesin pages 27-28)

## 3. Candidate graph nodes

### Target and measurement nodes

- **`METPO:1000885`** — cell length medium; exact target class.
- **Cell length** — continuous measurement node; label-only candidate unless the project has an established measurement ontology.
- **Longer cell dimension, 2–3 µm** — threshold/classification criterion.
- **Cell width**, **cell volume**, **aspect ratio**, **filamentation** — neighboring but non-equivalent phenotypes.
- **Micrometre** — `UO:0000017` may be used if Units of Measurement Ontology is accepted by the schema.

### Environmental and experimental nodes

- Nutrient-rich condition; nutrient-poor condition; carbon limitation; starvation.
- Growth rate; exponential growth; stationary phase.
- DNA damage/SOS-inducing treatment.
- Serine hydroxamate; RelA overexpression; cerulenin.
- Cell-wall-deficient/L-form growth condition.
- Microscopy and image segmentation assay—retain as label-only candidates if no assay ontology is already adopted.

### Chemicals and metabolites

- UDP-glucose — **`CHEBI:18066`**.
- Guanosine 3′,5′-bis(diphosphate), ppGpp — ontology mapping should be verified against the current ChEBI release before insertion.
- ATP; glucose; fatty acids; peptidoglycan.
- cAMP — **`CHEBI:17489`**.
- Cerulenin and serine hydroxamate — verify ChEBI records before curation rather than assigning from memory.

### Genes, proteins and complexes

- **FtsZ** — tubulin-like GTPase and Z-ring scaffold.
- **OpgH** — *E. coli* glucosyltransferase and nutrient-dependent FtsZ antagonist.
- **UgtP** — *B. subtilis* glucosyltransferase and nutrient-dependent division antagonist.
- **MreB** and the **Rod complex** — lateral peptidoglycan synthesis/rod-shape machinery.
- **SepF**, **FtsA**, divisome and Z-ring.
- **MinC, MinD, MinE**; **SlmA** in *E. coli*; **Noc** in *B. subtilis*.
- **SulA**, **RelA**, **Clp proteases**, **BolA**, **Crp**.
- Central-metabolism candidates: **fabH, pta, ackA, aceE**, and cognate UDP-glucose-pathway phosphoglucomutases/pyrophosphorylases.

Protein nodes should use taxon-specific **UniProt accessions** only after strain selection. A bare protein-family label is safer than assigning one accession across taxa.

### Processes, functions and localizations

- FtsZ polymerization; Z-ring assembly; cytokinesis; septum formation.
- Division-site selection; nucleoid occlusion; asymmetric division.
- Lateral peptidoglycan synthesis; cell-wall elongation; fatty-acid biosynthesis.
- Stringent response; SOS response; central-carbon metabolism.
- Midcell, nascent septal site, inner membrane and lateral cell wall.

Appropriate GO identifiers should be selected from the current GO release during YAML implementation. The evidence supports the labels, but inventing or guessing GO accessions would violate the requested grounding standard.

## 4. Candidate evidence-backed causal edges

The following table is the primary curation worksheet. “Strong” means the mechanistic relationship is well supported, not that it directly yields the exact 2–3 µm class.

| subject | predicate | object | taxon/context | evidence snippet (short quotation or faithful extracted wording) | DOI/date | strength/curation note |
|---|---|---|---|---|---|---|
| nutrient-rich conditions | increases proxy metabolite availability | UDP-glucose | *E. coli*, *B. subtilis*; nutrient-rich vs nutrient-poor growth | “conservation of uridine diphosphate glucose as a proxy for nutrient status”; nutrient-rich conditions produce metabolites that activate OpgH/UgtP (vadia2015growthrateand pages 4-6, vadia2015growthrateand pages 6-7) | 10.1016/j.mib.2015.01.011 / 2015-04 | Review-backed, broad mechanism; curate as indirect nutrient-sensing edge, not a direct 2–3 µm determinant |
| UDP-glucose | activates/enables interaction of | OpgH/UgtP with FtsZ | *E. coli* OpgH; *B. subtilis* UgtP | “UDP-glucose modulates UgtP affinity to FtsZ”; OpgH/UgtP are “activated by UDP-glucose” and couple nutrient status to division (ojkic2021bacterialcellshape pages 1-2, vadia2015growthrateand pages 4-6) | 10.1101/2021.03.25.436990 / 2021-03; 10.1016/j.mib.2015.01.011 / 2015-04 | Strong for nutrient-dependent regulation, but one source is a preprint; acceptable with note |
| OpgH/UgtP | inhibits assembly of | FtsZ | *E. coli*, *B. subtilis*; exponential growth, nutrient-rich conditions | “OpgH localizes to the nascent septal site, where it antagonizes assembly of… FtsZ, delaying division and increasing cell size”; UgtP/OpgH “delay FtsZ assembly” (westfall2017bacterialcellsize pages 9-11, vadia2015growthrateand pages 4-6) | 10.1146/annurev-micro-090816-093803 / 2017-09; 10.1016/j.mib.2015.01.011 / 2015-04 | Strong mechanism from primary studies summarized in reviews; good curation candidate |
| FtsZ assembly | enables | Z-ring formation and cell division | broad bacteria; divisome assembly | “FtsZ polymerization at midcell initiates Z-ring formation”; “FtsZ forms a Z-ring at the division site” and is central to cytokinesis (gulsoy2024divisomeminimizationshows pages 1-4, jun2018fundamentalprinciplesin pages 27-28) | 10.1101/2024.01.12.575403 / 2024-01; 10.1088/1361-6633/aaa628 / 2018-02 | Foundational and strong; preprint support is consistent with established reviews |
| delayed division / reduced FtsZ assembly | increases | cell length or overall cell size | *E. coli*, *B. subtilis*; nutrient-rich growth | “delaying division and increasing cell size”; in *B. subtilis*, growth-rate-dependent UgtP/FtsZ regulation causes substantial length changes, with length spanning “3.5–12.7 μm” across conditions (westfall2017bacterialcellsize pages 9-11, ojkic2021bacterialcellshape pages 1-2) | 10.1146/annurev-micro-090816-093803 / 2017-09; 10.1101/2021.03.25.436990 / 2021-03 | Strong for directional effect on size/length; not specific to medium-length class |
| ppGpp | reduces | cell length and width | *E. coli* and/or *B. subtilis*; nutrient starvation, serine hydroxamate, RelA overexpression | “ppGpp… is negatively correlated with cell size”; induction “substantially reduces both cell length and width” (westfall2017bacterialcellsize pages 9-11, westfall2017bacterialcellsize pages 11-12) | 10.1146/annurev-micro-090816-093803 / 2017-09 | Strong review synthesis of direct experiments; curate as negative regulator of larger size states |
| fatty-acid synthesis | supports/permits | larger cell size | *E. coli*; rich medium; fabH and cerulenin perturbations | “Fatty acid biosynthesis (fabH) perturbations reduce E. coli cell volume by up to 70% in rich medium”; cerulenin “reduces cell size” (vadia2015growthrateand pages 4-6, westfall2017bacterialcellsize pages 11-12) | 10.1016/j.mib.2015.01.011 / 2015-04; 10.1146/annurev-micro-090816-093803 / 2017-09 | Strong for size support, but mainly volume/overall size rather than isolated length |
| MreB / Rod-complex-guided elongation | supports | lateral wall elongation and rod shape maintenance | rod-shaped bacteria; sidewall synthesis | MreB forms “platforms for transpeptidases and transglycosylases,” is “critical for maintaining rod shape and lateral cell wall synthesis,” and “locally guide[s] sidewall” growth (westfall2017bacterialcellsize pages 11-12, cameron2024insightsintothe pages 3-4) | 10.1146/annurev-micro-090816-093803 / 2017-09; 10.1038/s41579-023-00942-x / 2024-07 | Strong for morphology maintenance; effect on exact length class is indirect |
| MinC/Min system | inhibits misplaced polymerization of | FtsZ | *E. coli*, *B. subtilis*; division-site positioning | “MinC inhibits FtsZ polymerization” and restricts the Z-ring to midcell; Min inactivation can cause asymmetric division/minicells (cameron2024insightsintothe pages 3-4, meunier2021bacterialcellproliferation pages 22-24) | 10.1038/s41579-023-00942-x / 2024-07; 10.1093/femsre/fuaa046 / 2021-09 | Strong spatial-regulation edge; supports normal rather than aberrant length outcomes |
| SlmA / Noc nucleoid occlusion | inhibits assembly of | FtsZ over the nucleoid | *E. coli* SlmA; *B. subtilis* Noc | “SlmA binds directly to FtsZ and inhibits its assembly near the nucleoid”; NO prevents division machinery assembly over unsegregated chromosomes (cameron2024insightsintothe pages 3-4, meunier2021bacterialcellproliferation pages 22-24) | 10.1038/s41579-023-00942-x / 2024-07; 10.1093/femsre/fuaa046 / 2021-09 | Strong spatial checkpoint edge; useful for preventing abnormal elongation/filamentation from misplaced division |
| SOS response / SulA | inhibits polymerization/assembly of | FtsZ | *E. coli* DNA damage response | “SulA… binds to FtsZ, inhibiting its [assembly/polymerization]”; SulA is a “potent inhibitor of bacterial cell division” associated with filamentation (jun2018fundamentalprinciplesin pages 27-28, cameron2024insightsintothe pages 3-4) | 10.1088/1361-6633/aaa628 / 2018-02; 10.1038/s41579-023-00942-x / 2024-07 | Strong, classic mechanism; curate as stress-induced long-cell/filament edge |
| FtsZ-dependent division plus Min or nucleoid occlusion | controls | cell shape and size | *E. coli* L-forms, wall-less context | “FtsZ-dependent division alone is sufficient to convert heterogeneous ameba-like L-form cells into mostly uniform oval-shaped cells”; requires “either the Min or nucleoid occlusion systems” for positioning (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y / 2024-11 | Direct recent evidence, but special wall-less/L-form context; mark taxon/assay-specific |
| METPO:1000885 cell length medium (2–3 µm) | may arise from balanced nutrient-growth and division control | moderate growth / non-filamentous rod state | ontology class; inferred from growth-law and division-control literature | Existing evidence summary: growth-rate-dependent size law supports medium cell length as typical at moderate growth rates; however no cited study directly maps these mechanisms to the exact 2–3 µm class (vadia2015growthrateand pages 4-6, westfall2017bacterialcellsize pages 9-11) | 10.1016/j.mib.2015.01.011 / 2015-04; 10.1146/annurev-micro-090816-093803 / 2017-09 | **Uncertain**; do not over-curate as a direct mechanistic edge to the exact class without primary assay data |
| morphology engineering perturbation of FtsZ/MreB | can alter | cell morphology/size for bioprocess aims | engineered microbes; biopolymer production applications | review describes “modifying the cell morphology and size” and notes strains with “deletions of ftsZ or mreB genes” used in morphology engineering (gulsoy2024divisomeminimizationshows pages 1-4) | 10.3390/polym16030410 / 2024-02 | Application-focused review; useful for real-world implementation context, weak for exact causal graph edge to medium length |


*Table: This table compiles evidence-backed candidate causal edges relevant to the microbial trait METPO:1000885, prioritizing mechanisms controlling bacterial cell length, size, and division. It highlights which edges are strong curation candidates and which should remain uncertain because no cited study directly maps them to the exact 2–3 µm medium-length class.*

### Recommended conservative core

The most defensible initial YAML graph is:

1. nutrient-rich condition → increases → UDP-glucose availability;
2. UDP-glucose → promotes → OpgH/UgtP interaction with FtsZ;
3. OpgH/UgtP → inhibits/delays → FtsZ assembly;
4. FtsZ assembly → enables → Z-ring formation;
5. Z-ring formation → enables → cytokinesis;
6. delayed cytokinesis while elongation continues → increases → cell length;
7. MreB/Rod complex → promotes → lateral wall elongation;
8. MinC and SlmA/Noc → inhibit → spatially inappropriate FtsZ assembly;
9. ppGpp → decreases → cell dimensions under the tested conditions;
10. measured cell length of 2–3 µm → classified as → **`METPO:1000885`**.

Edge 10 is a measurement/classification assertion. It is preferable to the biologically overstrong claim that “moderate growth rate causes `METPO:1000885`.”

## 5. Recent developments, 2023–2024

- A 2024 *Nature Reviews Microbiology* synthesis emphasizes that MinC directly restricts FtsZ polymerization to midcell and that SlmA/Noc can sequester FtsZ in non-polymerized states. This supports explicit spatial-regulation nodes rather than treating FtsZ abundance as the sole determinant of length. Published July 2024; DOI [10.1038/s41579-023-00942-x](https://doi.org/10.1038/s41579-023-00942-x). (cameron2024insightsintothe pages 3-4)
- A November 2024 *Communications Biology* study showed that FtsZ-dependent division can convert heterogeneous, wall-less *E. coli* L-forms into mostly uniform oval cells, but only when at least Min or nucleoid occlusion can position FtsZ. This is direct evidence that division machinery can regulate size and shape independently of cylindrical wall synthesis, although the L-form context is exceptional. DOI [10.1038/s42003-024-07279-y](https://doi.org/10.1038/s42003-024-07279-y). (hayashi2024septalwallsynthesis pages 1-2)
- A January 2024 *B. subtilis* preprint found that FtsZ and SepF can form a minimal active Z-ring after deletion of eight conserved division regulators—ZapA, MinC, MinJ, UgtP, ClpX, Noc, EzrA and FtsA—using suppressor mutations. Division frequency fell substantially, demonstrating robustness but also extensive genetic compensation; it should not be interpreted as showing that the deleted regulators are normally irrelevant to length. DOI [10.1101/2024.01.12.575403](https://doi.org/10.1101/2024.01.12.575403). (gulsoy2024divisomeminimizationshows pages 1-4)
- Current morphology engineering reviews describe manipulating FtsZ/MreB and cell dimensions to increase intracellular storage or simplify recovery of products such as polyhydroxyalkanoates. These are real-world applications of size control, but engineered enlargement or filamentation is not evidence for the natural 2–3 µm phenotype.

## 6. Expert interpretation and applications

Authoritative reviews characterize bacterial size as **multifactorial and multifaceted**, with nutrient status, biosynthetic capacity, envelope synthesis, chromosome cycles and cytokinesis contributing in parallel. This argues against a single linear “growth rate → medium length” graph. (westfall2017bacterialcellsize pages 9-11, vadia2015growthrateand pages 4-6)

Practical implementations include:

- **Antibacterial discovery:** FtsZ is an established drug target; inhibition commonly blocks cytokinesis and causes elongation/filamentation. Such edges are useful negative controls because they generally move cells outside the medium-length class.
- **Microbial cell factories:** Altering FtsZ or MreB can enlarge cells or change morphology, potentially increasing intracellular storage and facilitating downstream biopolymer recovery.
- **Synthetic/minimal cells:** The FtsZ–SepF minimal-ring work informs which division components are indispensable versus conditionally dispensable, but suppressor evolution complicates causal interpretation. (gulsoy2024divisomeminimizationshows pages 1-4)
- **Phenotypic antimicrobial assays:** Cell-length distributions can report division inhibition, SOS activation or envelope stress, provided width and lysis phenotypes are measured separately.

## 7. Warnings: claims not yet suitable for TraitMech curation

1. **Do not curate “moderate growth rate → `METPO:1000885`” as a strong direct edge.** The supplied Science evidence supports a growth-dependent size law, but the retrieved evidence does not demonstrate an invariant 2–3 µm outcome.
2. **Do not translate cell volume into cell length.** A 70% volume reduction or a 15–30% size reduction does not establish entry into the 2–3 µm bin. (westfall2017bacterialcellsize pages 9-11, vadia2015growthrateand pages 4-6)
3. **Do not universalize OpgH and UgtP.** OpgH is established in *E. coli* and UgtP in *B. subtilis*; they are functionally analogous but non-homologous and taxon-specific.
4. **Do not make Min or nucleoid occlusion direct positive causes of medium length.** They ensure spatially appropriate division; their loss can produce mixed outcomes including minicells, asymmetric cells and elongation. (meunier2021bacterialcellproliferation pages 22-24, cameron2024insightsintothe pages 3-4)
5. **Do not curate MreB as sufficient for 2–3 µm length.** Its strongest supported role is rod-shape maintenance and lateral wall synthesis. (westfall2017bacterialcellsize pages 11-12)
6. **Treat SulA/SOS as a long-cell or filamentation mechanism, not a medium-length mechanism.** Any transient passage through 2–3 µm during elongation would be assay-time dependent.
7. **Mark the 2024 FtsZ–SepF minimal-divisome result as preprint evidence** and record suppressor mutations. (gulsoy2024divisomeminimizationshows pages 1-4)
8. **Keep L-form evidence explicitly assay-specific.** Wall-less oval-cell control is not equivalent to normal rod-length homeostasis. (hayashi2024septalwallsynthesis pages 1-2)
9. **Avoid unverified ontology accessions.** Use label-only nodes until current GO, ChEBI, UniProt, Rhea, KEGG or MetaCyc mappings are checked for the exact taxon and molecular entity.

## 8. DOI-first bibliography

1. Cameron TA, Margolin W. “Insights into the assembly and regulation of the bacterial divisome.” *Nature Reviews Microbiology* 22, 33–45. Published July 2024. [https://doi.org/10.1038/s41579-023-00942-x](https://doi.org/10.1038/s41579-023-00942-x). (cameron2024insightsintothe pages 3-4)
2. Hayashi M, et al. “Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in *Escherichia coli* L-forms.” *Communications Biology* 7. Published November 2024. [https://doi.org/10.1038/s42003-024-07279-y](https://doi.org/10.1038/s42003-024-07279-y). (hayashi2024septalwallsynthesis pages 1-2)
3. Gulsoy IC, et al. “Divisome minimization shows that FtsZ and SepF can form an active Z-ring…” *bioRxiv*. Posted January 2024; preprint. [https://doi.org/10.1101/2024.01.12.575403](https://doi.org/10.1101/2024.01.12.575403). (gulsoy2024divisomeminimizationshows pages 1-4)
4. Meunier A, Cornet F, Campos M. “Bacterial cell proliferation: from molecules to cells.” *FEMS Microbiology Reviews* 45. Published September 2021. [https://doi.org/10.1093/femsre/fuaa046](https://doi.org/10.1093/femsre/fuaa046). (meunier2021bacterialcellproliferation pages 22-24)
5. Westfall CS, Levin PA. “Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in *Escherichia coli*.” *PLOS Genetics* 14:e1007205. Published February 2018. [https://doi.org/10.1371/journal.pgen.1007205](https://doi.org/10.1371/journal.pgen.1007205). (westfall2018comprehensiveanalysisof pages 17-18)
6. Jun S, Si F, Pugatch R, Scott M. “Fundamental principles in bacterial physiology…with focus on cell size control.” *Reports on Progress in Physics* 81:056601. Published February 2018. [https://doi.org/10.1088/1361-6633/aaa628](https://doi.org/10.1088/1361-6633/aaa628). (jun2018fundamentalprinciplesin pages 27-28)
7. Westfall CS, Levin PA. “Bacterial Cell Size: Multifactorial and Multifaceted.” *Annual Review of Microbiology* 71:499–517. Published September 2017. [https://doi.org/10.1146/annurev-micro-090816-093803](https://doi.org/10.1146/annurev-micro-090816-093803). (westfall2017bacterialcellsize pages 9-11, westfall2017bacterialcellsize pages 11-12)
8. Vadia S, Levin PA. “Growth rate and cell size: a re-examination of the growth law.” *Current Opinion in Microbiology* 24:96–103. Published April 2015. [https://doi.org/10.1016/j.mib.2015.01.011](https://doi.org/10.1016/j.mib.2015.01.011). (vadia2015growthrateand pages 4-6, vadia2015growthrateand pages 6-7)
9. Hill NS, Buske PJ, Shi Y, Levin PA. “A Moonlighting Enzyme Links *Escherichia coli* Cell Size with Central Metabolism.” *PLOS Genetics* 9:e1003663. Published July 2013. [https://doi.org/10.1371/journal.pgen.1003663](https://doi.org/10.1371/journal.pgen.1003663). Mechanism summarized in the retrieved reviews. (westfall2017bacterialcellsize pages 9-11)

## Final curation recommendation

Retain **`METPO:1000885`** as the terminal measured phenotype and expand the existing `cell_length_medium_growth_rate` graph into two convergent modules: **nutrient/biosynthetic control of division timing** and **elongation/division-site control**. Curate the UDP-glucose–OpgH/UgtP–FtsZ pathway, FtsZ–Z-ring–cytokinesis pathway, MreB/Rod elongation pathway, and Min/NO spatial-control pathway with taxon qualifiers. Represent the link from those mechanisms to the exact 2–3 µm class as **uncertain or measurement-derived** until a primary study reports length distributions crossing that explicit threshold under defined perturbations.

References

1. (ojkic2021bacterialcellshape pages 1-2): Nikola Ojkic and Shiladitya Banerjee. Bacterial cell shape control by nutrient-dependent synthesis of cell division inhibitors. bioRxiv, Mar 2021. URL: https://doi.org/10.1101/2021.03.25.436990, doi:10.1101/2021.03.25.436990. This article has 32 citations.

2. (westfall2017bacterialcellsize pages 11-12): Corey S. Westfall and Petra Anne Levin. Bacterial cell size: multifactorial and multifaceted. Annual review of microbiology, 71:499-517, Sep 2017. URL: https://doi.org/10.1146/annurev-micro-090816-093803, doi:10.1146/annurev-micro-090816-093803. This article has 96 citations and is from a peer-reviewed journal.

3. (hayashi2024septalwallsynthesis pages 1-2): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

4. (westfall2018comprehensiveanalysisof pages 17-18): Corey S. Westfall and Petra Anne Levin. Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in escherichia coli. PLOS Genetics, 14:e1007205, Feb 2018. URL: https://doi.org/10.1371/journal.pgen.1007205, doi:10.1371/journal.pgen.1007205. This article has 79 citations and is from a domain leading peer-reviewed journal.

5. (westfall2017bacterialcellsize pages 9-11): Corey S. Westfall and Petra Anne Levin. Bacterial cell size: multifactorial and multifaceted. Annual review of microbiology, 71:499-517, Sep 2017. URL: https://doi.org/10.1146/annurev-micro-090816-093803, doi:10.1146/annurev-micro-090816-093803. This article has 96 citations and is from a peer-reviewed journal.

6. (vadia2015growthrateand pages 4-6): Stephen Vadia and Petra Anne Levin. Growth rate and cell size: a re-examination of the growth law. Current Opinion in Microbiology, 24:96-103, Apr 2015. URL: https://doi.org/10.1016/j.mib.2015.01.011, doi:10.1016/j.mib.2015.01.011. This article has 133 citations and is from a peer-reviewed journal.

7. (meunier2021bacterialcellproliferation pages 22-24): Alix Meunier, François Cornet, and Manuel Campos. Bacterial cell proliferation: from molecules to cells. FEMS Microbiology Reviews, Sep 2021. URL: https://doi.org/10.1093/femsre/fuaa046, doi:10.1093/femsre/fuaa046. This article has 42 citations and is from a domain leading peer-reviewed journal.

8. (cameron2024insightsintothe pages 3-4): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 142 citations and is from a highest quality peer-reviewed journal.

9. (jun2018fundamentalprinciplesin pages 27-28): Suckjoon Jun, Fangwei Si, Rami Pugatch, and Matthew Scott. Fundamental principles in bacterial physiology—history, recent progress, and the future with focus on cell size control: a review. Reports on Progress in Physics, 81:056601, Feb 2018. URL: https://doi.org/10.1088/1361-6633/aaa628, doi:10.1088/1361-6633/aaa628. This article has 254 citations and is from a highest quality peer-reviewed journal.

10. (vadia2015growthrateand pages 6-7): Stephen Vadia and Petra Anne Levin. Growth rate and cell size: a re-examination of the growth law. Current Opinion in Microbiology, 24:96-103, Apr 2015. URL: https://doi.org/10.1016/j.mib.2015.01.011, doi:10.1016/j.mib.2015.01.011. This article has 133 citations and is from a peer-reviewed journal.

11. (gulsoy2024divisomeminimizationshows pages 1-4): Ilkay Celik Gulsoy, Terrens N. V. Saaki, Michaela Wenzel, Simon Syvertsson, Taku Morimoto, and Leendert W. Hamoen. Divisome minimization shows that ftsz and sepf can form an active z-ring, and reveals brab as a new cell division influencing protein in bacillus subtilis. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.12.575403, doi:10.1101/2024.01.12.575403. This article has 2 citations.