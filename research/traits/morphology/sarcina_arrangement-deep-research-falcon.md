---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:47:50.707623'
end_time: '2026-08-04T09:59:39.818764'
duration_seconds: 709.11
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: sarcina arrangement
  trait_identifier: traitmech:000120
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sarcina_arrangement
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell arrangement in which cocci divide in three perpendicular planes
    and remain attached as cubic packets of eight (sarcinae).
  parent_traits: METPO:1000666
  synonyms: cubic packet cocci
  evidence_summary: 'DOI:10.1128/MMBR.00001-06:  (Young''s review treats the sarcina
    cubic packet as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Three-plane
    division with incomplete daughter-cell separation yields cubic eight-cell packets.)'
  causal_graph_summary: 'sarcina_three_plane_division_packet: 14 nodes, 9 edges'
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
- **Trait label:** sarcina arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000120
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in three perpendicular planes and remain attached as cubic packets of eight (sarcinae).
- **Parent traits:** METPO:1000666
- **Synonyms:** cubic packet cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the sarcina cubic packet as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Three-plane division with incomplete daughter-cell separation yields cubic eight-cell packets.)
- **Existing causal graph summary:** sarcina_three_plane_division_packet: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **sarcina arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sarcina_arrangement.yaml`.

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
- **Trait label:** sarcina arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000120
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in three perpendicular planes and remain attached as cubic packets of eight (sarcinae).
- **Parent traits:** METPO:1000666
- **Synonyms:** cubic packet cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the sarcina cubic packet as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Three-plane division with incomplete daughter-cell separation yields cubic eight-cell packets.)
- **Existing causal graph summary:** sarcina_three_plane_division_packet: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **sarcina arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sarcina_arrangement.yaml`.

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


# TraitMech curation report: sarcina arrangement

## Record and scope

- **Trait:** sarcina arrangement
- **Identifier:** `traitmech:000120`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Supplied parent:** `METPO:1000666`
- **Definition:** coccoid cells divide in three mutually perpendicular planes and remain attached, producing a cubic packet whose canonical first complete form contains eight cells; repeated cycles can produce larger packets.

This is an **assay-observed cellular arrangement**, not a metabolic capacity, habitat preference, taxon name, or single-cell shape. In *Sarcina ventriculi*, nearly spherical 1.8–3 µm cells occur as tetrads or packets of eight or more, attributed to division in perpendicular planes. Flattened interfaces and extracellular cellulose are accompanying structural features. (marcelino2021sarcinaventriculia pages 6-7)

### Boundary cases

1. **Tetrads:** a tetrad is an intermediate/partial sarcinous arrangement, but a tetrad alone demonstrates division in two planes—not necessarily the defining third orthogonal division that creates a cubic octet.
2. **Irregular staphylococcal clusters:** *Staphylococcus aureus* also uses successive orthogonal division planes, but septum splitting and rearrangement produce irregular clusters rather than stable cubic packets. Orthogonal division is therefore necessary or strongly contributory, but not sufficient by itself. (pereira2016ftszdependentelongationof pages 5-6)
3. **Chains and diplococci:** retention after division in one plane produces chains or pairs, not sarcinae.
4. **Cuboid cells:** “cuboid” describes individual-cell appearance; the target trait concerns packet topology.
5. **Large packets:** packets containing more than eight cells remain in scope when their architecture reflects continued orthogonal division and persistent attachment.
6. **Taxonomy:** morphology should not be equated with membership in genus *Sarcina*. The genus name is contested because sarcinae lie within Clostridia “cluster I,” and packet-forming organisms can differ substantially in size, physiology, and genome content. (owens2021asarcinabacterium pages 5-6)
7. **Methanosarcina aggregates:** archaeal aggregates named “sarcina” historically should not be included without evidence of the same three-plane bacterial division mechanism.

## Current mechanistic model

The best-supported graph has two interacting modules:

1. **Geometric division module:** coccoid growth → sequential orthogonal septum placement → division in three perpendicular planes → tetrad and cubic-octet geometry.
2. **Cohesion module:** extracellular, packet-associated cellulose → persistent cell–cell binding → stabilization and enlargement of packets.

The cellulose module has the strongest perturbational support: a review of primary *S. ventriculi* work states that extracellular cellulose “tightly bind[s] the cells into large packets”; chemical removal of the cementing material leaves cell walls intact but breaks large packets into smaller aggregates. This distinguishes packet cohesion from cell-wall integrity. (moniri2017productionandstatus pages 3-6)

By contrast, molecular division machinery is not resolved directly in *Sarcina*. In the coccal model *S. aureus*, an FtsZ ring positions symmetric mid-cell septal peptidoglycan synthesis; the ring constricts and the septum splits to produce daughters. An FtsZ G193D mutation redirects peptidoglycan insertion asymmetrically/helically and causes elongation. These results establish a plausible molecular bridge from FtsZ geometry to coccal division, but transfer to *Sarcina* remains inferential. (pereira2016ftszdependentelongationof pages 5-6)

## Candidate nodes grouped by type

### Phenotypes and cellular structures

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| sarcina arrangement | `traitmech:000120` | Target node. |
| parent morphology trait | `METPO:1000666` | Supplied parent; preserve verbatim. |
| coccoid cell | Label only | Avoid asserting that packet geometry equals individual-cell shape. |
| tetrad | Label only | Intermediate/boundary phenotype. |
| cubic eight-cell packet | Label only | Canonical positive phenotype. |
| large sarcina packet | Label only | Repeated-division extension of the octet. |
| flattened cell–cell interface | Label only | Directly described in *S. ventriculi*. (marcelino2021sarcinaventriculia pages 6-7) |
| extracellular packet-associated cellulose | `CHEBI:18246` for cellulose | Localization/role should remain in the node label or edge annotation. |
| peptidoglycan | CHEBI grounding should be verified before YAML insertion | Supported in the coccal model, not directly demonstrated as the sarcina-specific determinant. |
| division septum | GO process grounding may use `GO:0000917` where appropriate | Ensure the GO term’s scope matches bacterial barrier-septum assembly. |

### Processes and modules

| Candidate node | Suggested grounding | Evidence status |
|---|---|---|
| cell division | `GO:0051301` | General process. |
| cell cycle | `GO:0007049` | Broad contextual process. |
| successive perpendicular division-plane selection | Label only | Direct phenotype-level support; no verified specific ontology term. |
| symmetric mid-cell septal peptidoglycan synthesis | Label only | Direct in *S. aureus*; inferred for sarcinae. |
| septum constriction | Label only | Coccal-model support. |
| septum splitting / daughter-cell separation | Label only | Coccal-model support; sarcina packets require incomplete effective dispersal or renewed adhesion. |
| persistent daughter-cell attachment | Label only | Necessary graph concept; cellulose evidence supports cohesion. |
| cellulose biosynthesis | Label only pending exact GO verification | General pathway support, not genetically mapped in retrieved *Sarcina* evidence. |

### Genes and proteins

| Candidate node | Grounding | Curation status |
|---|---|---|
| FtsZ | Protein-family label only | Include only as **uncertain, cross-taxon support**; no verified *Sarcina* accession or perturbation evidence was retrieved. |
| FtsZ G193D variant | Label only | Comparator from *S. aureus*; not part of the core sarcina graph. |
| cellulose synthase | Enzyme/protein-family label only | Do not assign a *Sarcina* gene or UniProt accession without genomic/biochemical confirmation. |
| peptidoglycan synthases, including PBP2 | Label only | Mentioned in the coccal model; not established as sarcina-specific determinants. |
| autolysins/septum-splitting enzymes | Label only | Mechanistically plausible but unsupported for this trait by retrieved direct evidence. |

### Chemicals, substrates, and environmental factors

| Candidate node | Suggested grounding | Note |
|---|---|---|
| glucose | `CHEBI:17234` | General cellulose precursor and fermentable substrate. |
| UDP-α-D-glucose | `CHEBI:18066` | Direct cellulose precursor in general bacterial-cellulose biosynthesis. (moniri2017productionandstatus pages 3-6) |
| cellulose | `CHEBI:18246` | Directly relevant cohesion material. |
| carbohydrate availability | Label only | *S. ventriculi* depends on carbohydrate fermentation, but a direct effect on packet morphology has not been isolated. (marcelino2021sarcinaventriculia pages 6-7) |
| Cross and Bevan’s reagent | Label only | Experimental cellulose-removal factor; chemical composition/identifier should be curated only after checking the primary method. |
| low pH | Label only | Relevant to persistence of *S. ventriculi*, not demonstrated to cause sarcina arrangement. |
| gastric stasis / retained substrate | Label only | Clinical enrichment context, not a morphogenesis determinant. |

### Taxonomic contexts

- *Sarcina ventriculi* (also encountered as *Clostridium ventriculi* in modern nomenclature): direct morphology and cellulose-cohesion context.
- “Candidatus *Sarcina troglodytae*”: confirms that related organisms can exhibit flattened cells, large packets, and cellulose-containing outer material, but it is a distinct taxon with larger mean cell diameter. (owens2021asarcinabacterium pages 5-6)
- *Staphylococcus aureus*: mechanistic comparator for orthogonal coccal division, not a direct positive instance of stable cubic sarcina packets. (pereira2016ftszdependentelongationof pages 5-6)

Exact NCBITaxon identifiers should be verified against the nomenclature used in the final database release rather than inferred here.

## Candidate causal edges

The following table separates edges suitable for cautious curation from supporting analogies and biochemical background.

| subject | predicate | object | evidence tier | DOI | curation decision |
|---|---|---|---|---|---|
| successive perpendicular division planes | produces | tetrads / packets of eight or more cells (sarcina arrangement) | Direct Sarcina | 10.4322/acr.2021.337 | **Curate, medium confidence.** Direct descriptive morphology in *Sarcina ventriculi*; mechanism stated at phenotype level, not gene-resolved. (marcelino2021sarcinaventriculia pages 6-7) |
| extracellular cellulose | tightly binds | cells into large packets | Direct Sarcina | 10.3390/nano7090257 | **Curate cautiously, medium confidence.** Strongly stated for *S. ventriculi* but sourced through a later review summarizing older primary work. (moniri2017productionandstatus pages 3-6) |
| removal of cellulose from packets with Cross and Bevan’s reagent | causes | packet disaggregation into smaller aggregates while cell walls remain intact | Direct Sarcina | 10.3390/nano7090257 | **Curate cautiously, medium confidence.** Useful causal edge for adhesion/cementing material; evidence is review-level, not directly from the primary experiment in retrieved text. (moniri2017productionandstatus pages 3-6) |
| FtsZ ring at mid-cell | directs / initiates | symmetric septal peptidoglycan synthesis | Supporting coccal model | 10.1128/mbio.00908-16 | **Do not curate as Sarcina-specific yet.** Strong mechanism in *Staphylococcus aureus*; transfer to sarcinae is plausible but unproven. (pereira2016ftszdependentelongationof pages 5-6) |
| symmetric septal peptidoglycan synthesis followed by constriction and splitting | generates | two daughter cells | Supporting coccal model | 10.1128/mbio.00908-16 | **Do not curate as Sarcina-specific yet.** General coccal division mechanism, not demonstrated in *Sarcina* packets. (pereira2016ftszdependentelongationof pages 5-6) |
| asymmetric FtsZ/peptidoglycan synthesis pattern | leads to | elongation rather than normal coccal division | Supporting coccal model | 10.1128/mbio.00908-16 | **Do not curate into sarcina graph.** Negative/comparator mechanism from mutant *S. aureus* helps delimit normal orthogonal division but is not Sarcina evidence. (pereira2016ftszdependentelongationof pages 5-6) |
| glucose (CHEBI:17234) | is converted to | UDP-glucose (CHEBI:18066) | General biochemical inference | 10.3390/nano7090257 | **Background only; do not curate yet.** Non-Sarcina-specific cellulose-biosynthesis pathway summary. (moniri2017productionandstatus pages 3-6) |
| UDP-glucose (CHEBI:18066) | serves as precursor for synthesis of | cellulose (CHEBI:18246) | General biochemical inference | 10.3390/nano7090257 | **Background only; do not curate yet.** Valid for bacterial cellulose generally, but no Sarcina-specific synthase/gene evidence here. (moniri2017productionandstatus pages 3-6) |
| cellulose (CHEBI:18246) | is associated with | cellulose-containing cell wall / outer packet-associated material in Sarcina-like taxa | Direct Sarcina | 10.1038/s41467-021-21012-x | **Curate only as supporting structural association, not full mechanism.** Confirms cellulose-containing material in a Sarcina relative, but does not prove causation of packet formation. (owens2021asarcinabacterium pages 5-6) |


*Table: This table lists compact candidate causal edges for sarcina arrangement, separating direct Sarcina evidence from coccal-model and general biochemical inferences. It is useful for deciding which edges are safe to curate now versus which should remain provisional.*

### Recommended minimal core for `sarcina_arrangement.yaml`

The defensible near-term core is:

1. `successive perpendicular division planes` **produces** `tetrads and packets of eight or more cells`.
2. `three mutually perpendicular division cycles` **establishes geometry of** `cubic eight-cell packet`.
3. `extracellular packet-associated cellulose` **tightly binds** `adjacent Sarcina cells`.
4. `persistent cellulose-mediated cell binding` **stabilizes/promotes** `large sarcina packets`.
5. `chemical removal of packet cellulose` **disrupts** `large packet cohesion`.
6. `chemical removal of packet cellulose` **does not disrupt** `individual cell-wall integrity`.

Edges 1–2 have direct descriptive but not gene-level support. Edges 3–6 have useful perturbational support, although the retrieved source is a 2017 review summarizing foundational primary work. (marcelino2021sarcinaventriculia pages 6-7, moniri2017productionandstatus pages 3-6)

### Provisional mechanistic extension

A second, explicitly uncertain tier could represent:

`FtsZ ring` → `symmetric mid-cell septal peptidoglycan synthesis` → `septum constriction` → `daughter-cell formation` → `successive orthogonal division-plane selection` → `cubic packet geometry`.

Only the first three relationships are experimentally demonstrated in the retrieved *S. aureus* study; linkage to stable sarcina packets is an extrapolation. The mutant result—abnormal FtsZ geometry causing asymmetric/helical peptidoglycan insertion and elongation—supports FtsZ as a geometric controller of coccal morphogenesis, but not specifically of *Sarcina* packet formation. (pereira2016ftszdependentelongationof pages 5-6)

## Recent developments, applications, and quantitative evidence

### State of the 2023–2024 literature

The search did not identify a 2023–2024 primary mechanistic study that genetically dissects cubic packet formation in *S. ventriculi*. Recent publications are dominated by clinical case reports and diagnostic recognition rather than division-plane genetics. Accordingly, foundational ultrastructural and cellulose studies, modern coccal-cell-division work, and the 2021 comparative-genomic study remain more informative for causal-graph construction. The absence of a recent mechanistic paper should be recorded as an evidence gap, not filled by analogy.

### Diagnostic implementation

Sarcina arrangement is used in real-world histopathology: H&E and Gram stains commonly reveal the conspicuous tetrad/packet morphology; Brown–Hopps staining can highlight it. PCR/16S rRNA sequencing can confirm identity, but morphology often drives diagnosis. In a 2021 review of 47 human cases, organisms were found most frequently in the stomach (36 cases; 77%); gastric-content stasis was present in 26 cases (55%). Reported presentations included epigastric pain in 24 (51%), nausea/vomiting in 22 (47%), gastric perforation in four, and emergency laparotomy in six (13%). These data concern clinical occurrence, not the causal mechanism of packet formation. (marcelino2021sarcinaventriculia pages 6-7)

### Comparative genomics and surveillance

In chimpanzees with epizootic neurologic and gastroenteric syndrome, diagnostic PCR detected “Ca. *S. troglodytae*” in 13/19 cases (68.4%) and 0/13 controls, with odds ratio 56.1, 95% CI 2.87–1097.2, and Fisher’s exact *P*=0.0001. Cell diameters averaged 4.29 µm versus 2.83 µm for *S. ventriculi* “Goodsir” (*P*=0.0006). Packet morphology and cellulose staining were useful taxonomic/diagnostic features, but the study did not establish that the organism caused disease or identify packet-morphogenesis genes. (owens2021asarcinabacterium pages 5-6)

### Expert interpretation

The literature supports treating sarcina arrangement as the outcome of **division geometry plus post-division cohesion**, rather than assigning it solely to FtsZ, peptidoglycan synthesis, or cellulose. Orthogonal division can occur in cocci that do not form regular cubic packets, while cellulose removal disrupts packet cohesion without destroying cell walls. Thus, the causal graph should preserve two converging branches and avoid a single linear pathway. (pereira2016ftszdependentelongationof pages 5-6, moniri2017productionandstatus pages 3-6)

## Warnings: claims not yet ready for TraitMech curation

1. **Do not assert a specific *Sarcina* FtsZ allele or FtsZ-dependent three-plane mechanism.** Current support is transferred from *S. aureus*.
2. **Do not assign cellulose-synthase genes, operons, EC numbers, UniProt accessions, or c-di-GMP regulation to *S. ventriculi*** without direct genomic and experimental evidence. General bacterial-cellulose pathways are insufficient.
3. **Do not equate cellulose staining with causal proof.** The removal experiment supports cohesion, whereas staining alone demonstrates association.
4. **Do not encode low pH, gastric stasis, carbohydrate fermentation, acetaldehyde, or disease as causes of packet geometry.** They concern ecology, growth, or pathology; morphology-specific causality was not shown. (marcelino2021sarcinaventriculia pages 6-7)
5. **Do not use pyruvate decarboxylase or 16S rRNA as morphogenesis genes.** They are diagnostic/phylogenetic markers in this context.
6. **Do not treat every tetrad as a complete sarcina phenotype.** A canonical cubic octet requires the third perpendicular division.
7. **Do not generalize from “Ca. *S. troglodytae*” to *S. ventriculi*.** The former is larger, genomically distinct, difficult to propagate, and only a supporting comparative taxon. (owens2021asarcinabacterium pages 7-9, owens2021asarcinabacterium pages 5-6)
8. **Do not infer pathogenicity from packet morphology.** Human pathogenicity remains incompletely understood, and the chimpanzee association does not itself establish causation. (owens2021asarcinabacterium pages 7-9, marcelino2021sarcinaventriculia pages 6-7)
9. **Verify ontology terms before committing YAML.** Label-only nodes are preferable to inaccurate GO, EC, NCBITaxon, or UniProt mappings.

## DOI-first bibliography

1. Marcelino LP, et al. **Sarcina ventriculi a rare pathogen.** *Autopsy & Case Reports.* Published October 2021. DOI: [10.4322/acr.2021.337](https://doi.org/10.4322/acr.2021.337). Direct definition, perpendicular-plane packet morphology, cellulose, diagnostic boundaries, and human case statistics. (marcelino2021sarcinaventriculia pages 6-7)
2. Owens LA, et al. **A Sarcina bacterium linked to lethal disease in sanctuary chimpanzees in Sierra Leone.** *Nature Communications.* Published February 2021. DOI: [10.1038/s41467-021-21012-x](https://doi.org/10.1038/s41467-021-21012-x). Comparative morphology, cellulose staining, genomic distinction, and case-control statistics. (owens2021asarcinabacterium pages 7-9, owens2021asarcinabacterium pages 5-6)
3. Pereira AR, et al. **FtsZ-Dependent Elongation of a Coccoid Bacterium.** *mBio.* Published September/October 2016. DOI: [10.1128/mBio.00908-16](https://doi.org/10.1128/mbio.00908-16). FtsZ geometry, septal peptidoglycan synthesis, orthogonal division, and mutant elongation in *S. aureus*. (pereira2016ftszdependentelongationof pages 5-6)
4. Moniri M, et al. **Production and Status of Bacterial Cellulose in Biomedical Engineering.** *Nanomaterials.* Published September 2017. DOI: [10.3390/nano7090257](https://doi.org/10.3390/nano7090257). Review-level account of extracellular cellulose as *S. ventriculi* packet cement and its chemical removal. (moniri2017productionandstatus pages 3-6)
5. Ross P, Mayer R, Benziman M. **Cellulose Biosynthesis and Function in Bacteria.** *Microbiological Reviews.* Published March 1991. DOI: [10.1128/MR.55.1.35-58.1991](https://doi.org/10.1128/mr.55.1.35-58.1991). Authoritative bacterial-cellulose background identifying *Sarcina* among cellulose-producing genera and citing foundational localization work. (ross1991cellulosebiosynthesisand pages 20-21, ross1991cellulosebiosynthesisand pages 1-2)

## Curation conclusion

`traitmech:000120` is suitable for a compact causal graph, but the evidence supports only a small direct core. The highest-value edges are **orthogonal division → cubic packet geometry** and **extracellular cellulose → persistent packet cohesion**. FtsZ, septal peptidoglycan, cellulose-synthase genes, and precursor metabolism should remain provisional until demonstrated directly in a sarcina-forming bacterium. This conservative structure avoids converting plausible general microbiology into unsupported *Sarcina*-specific mechanism.

References

1. (marcelino2021sarcinaventriculia pages 6-7): Luciano Paludo Marcelino, Dirceu Felipe Valentini, Simone Márcia dos Santos Machado, Pedro Guilherme Schaefer, Raquel Camara Rivero, and Alessandro Bersch Osvaldt. Sarcina ventriculi a rare pathogen. Autopsy & Case Reports, 11:e2021337, Oct 2021. URL: https://doi.org/10.4322/acr.2021.337, doi:10.4322/acr.2021.337. This article has 42 citations.

2. (pereira2016ftszdependentelongationof pages 5-6): Ana R. Pereira, Jen Hsin, Ewa Król, Andreia C. Tavares, Pierre Flores, Egbert Hoiczyk, Natalie Ng, Alex Dajkovic, Yves V. Brun, Michael S. VanNieuwenhze, Terry Roemer, Rut Carballido-Lopez, Dirk-Jan Scheffers, Kerwyn Casey Huang, and Mariana G. Pinho. Ftsz-dependent elongation of a coccoid bacterium. Nov 2016. URL: https://doi.org/10.1128/mbio.00908-16, doi:10.1128/mbio.00908-16. This article has 30 citations and is from a domain leading peer-reviewed journal.

3. (owens2021asarcinabacterium pages 5-6): Leah A. Owens, Barbara Colitti, Ismail Hirji, Andrea Pizarro, Jenny E. Jaffe, Sophie Moittié, Kimberly A. Bishop-Lilly, Luis A. Estrella, Logan J. Voegtly, Jens H. Kuhn, Garret Suen, Courtney L. Deblois, Christopher D. Dunn, Carles Juan-Sallés, and Tony L. Goldberg. A sarcina bacterium linked to lethal disease in sanctuary chimpanzees in sierra leone. Nature Communications, Feb 2021. URL: https://doi.org/10.1038/s41467-021-21012-x, doi:10.1038/s41467-021-21012-x. This article has 44 citations and is from a highest quality peer-reviewed journal.

4. (moniri2017productionandstatus pages 3-6): Mona Moniri, Amin Boroumand Moghaddam, Susan Azizi, Raha Abdul Rahim, Arbakariya Bin Ariff, Wan Zuhainis Saad, Mohammad Navaderi, and Rosfarizan Mohamad. Production and status of bacterial cellulose in biomedical engineering. Nanomaterials, 7:257, Sep 2017. URL: https://doi.org/10.3390/nano7090257, doi:10.3390/nano7090257. This article has 387 citations and is from a peer-reviewed journal.

5. (owens2021asarcinabacterium pages 7-9): Leah A. Owens, Barbara Colitti, Ismail Hirji, Andrea Pizarro, Jenny E. Jaffe, Sophie Moittié, Kimberly A. Bishop-Lilly, Luis A. Estrella, Logan J. Voegtly, Jens H. Kuhn, Garret Suen, Courtney L. Deblois, Christopher D. Dunn, Carles Juan-Sallés, and Tony L. Goldberg. A sarcina bacterium linked to lethal disease in sanctuary chimpanzees in sierra leone. Nature Communications, Feb 2021. URL: https://doi.org/10.1038/s41467-021-21012-x, doi:10.1038/s41467-021-21012-x. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (ross1991cellulosebiosynthesisand pages 20-21): P. Ross, R. Mayer, and M. Benziman. Cellulose biosynthesis and function in bacteria. Microbiological Reviews, 55:35-58, Mar 1991. URL: https://doi.org/10.1128/mr.55.1.35-58.1991, doi:10.1128/mr.55.1.35-58.1991. This article has 1794 citations.

7. (ross1991cellulosebiosynthesisand pages 1-2): P. Ross, R. Mayer, and M. Benziman. Cellulose biosynthesis and function in bacteria. Microbiological Reviews, 55:35-58, Mar 1991. URL: https://doi.org/10.1128/mr.55.1.35-58.1991, doi:10.1128/mr.55.1.35-58.1991. This article has 1794 citations.