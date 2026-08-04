---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:30:33.672249'
end_time: '2026-08-04T11:37:51.075783'
duration_seconds: 437.4
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: natural competence
  trait_identifier: traitmech:000087
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: natural_competence
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological state in which a cell takes up free extracellular DNA
    from the environment and integrates it into its genome (natural genetic transformation).
  parent_traits: METPO:1000059
  synonyms: natural transformation
  evidence_summary: 'DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution,
    shared mechanisms, and control of natural bacterial transformation (competence
    for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene
    transfer supports natural transformation as a major route of bacterial DNA acquisition.)'
  causal_graph_summary: 'natural_competence_dna_uptake: 12 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** natural competence
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 12 nodes, 8 edges

## Research Objective

Research the microbial trait **natural competence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/natural_competence.yaml`.

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
- **Trait label:** natural competence
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 12 nodes, 8 edges

## Research Objective

Research the microbial trait **natural competence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/natural_competence.yaml`.

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


# Curation report: natural competence

**Trait:** natural competence  
**Trait identifier:** `traitmech:000087`  
**Category / term kind / status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** `METPO:1000059`  
**Synonym:** natural transformation

## 1. Scope summary

Natural competence is the regulated physiological state or capacity in which a bacterium expresses machinery that captures naked extracellular DNA, transports it across the cell envelope, and establishes it intracellularly. Establishment most often means RecA-dependent homologous integration into the chromosome, although autonomously replicating DNA can sometimes be maintained without chromosomal integration. Natural transformation is more precisely the DNA-transfer event or resulting genetic change; competence is the enabling state. Recent mechanistic reviews describe the conserved sequence as extracellular DNA capture, envelope translocation, ssDNA protection, and recombination. (zuke2024fromisotopicallylabeled pages 9-12, niu2025molecularmechanismsand pages 1-2, hardy2024yranisa pages 1-4)

### Boundary cases

* **Exclude artificial transformation:** electroporation, chemical transformation, heat shock, and engineered DNA injection do not demonstrate natural competence.
* **Exclude conjugation and transduction:** these require a donor-cell transfer apparatus or bacteriophage, whereas natural transformation uses free extracellular DNA. (toussaint2024unveilingtheregulatory pages 1-6)
* **Do not equate gene presence with phenotype:** intact competence genes indicate potential, but expression and permissive conditions are required. In *S. dysgalactiae*, 64.2% of 179 genomes had an intact gene set, yet transformation required pheromone induction and optimized conditions. In *Lactococcus lactis*, only one of 18 initially tested intact strains transformed spontaneously in rich medium. (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5, toussaint2024unveilingtheregulatory pages 6-9)
* **DNA binding alone is insufficient:** competence requires productive internalization and intracellular establishment.
* **DNA uptake for nutrition is adjacent but not identical:** uptake followed only by degradation should not be scored as natural genetic transformation unless genetic establishment is demonstrated.
* **Taxonomic architectures differ:** diderms generally move DNA through an outer-membrane secretin and periplasm before cytoplasmic-membrane passage; monoderms move DNA through the cell wall to a membrane-proximal receptor. Regulatory circuits are substantially more taxon-specific than the late uptake machinery. (zuke2024fromisotopicallylabeled pages 6-9, hardy2024yranisa pages 1-4, toussaint2024unveilingtheregulatory pages 1-6)

## 2. Candidate nodes

### Trait and process nodes

* natural competence — `traitmech:000087`
* natural transformation — label-only process candidate
* DNA uptake / DNA import — consider `GO:0031508` only after confirming that its current ontology definition matches bacterial transformation uptake
* homologous recombination — `GO:0035825`
* DNA strand invasion — label-only unless a suitable current GO term is verified
* D-loop formation and extension — label-only
* competence-gene transcription / competence regulon activation — label-only
* quorum sensing — `GO:0009372`

### Molecular and chemical nodes

* extracellular DNA, transforming dsDNA, incoming ssDNA, homologous donor DNA, homeologous donor DNA — label-only forms are preferable; generic DNA can be grounded to `CHEBI:16991`
* ATP — `CHEBI:15422`
* competence-stimulating peptide (CSP), ComX-inducing peptide (XIP), pre-CSP/ComC — label-only because peptide sequences and alleles are taxon-specific
* D-loop recombination intermediate — label-only
* antibiotics/stressors tested in pneumococcus: ampicillin, vancomycin, streptomycin, kanamycin, norfloxacin, tetracycline and methyl methanesulfonate; use ChEBI identifiers only after compound-by-compound validation
* carbon/nutritional inputs in *L. lactis*: glucose, maltose, xylose, cellobiose, galactose, arabinose, amino-acid/nitrogen-base limitation and diauxic shift

### Machinery and protein nodes

**Conserved or broadly distributed uptake/recombination machinery:** competence type-IV pilus/pseudopilus; ComGA, ComGB, ComGC/comG operon; minor pilins such as FimT or ComP; PilQ; ComEA; ComEC; ComFA; ComFC; EndA or another strand-degrading nuclease; SsbB/SsbA; DprA; RecA; ComM. The precise ortholog and protein identifier must be assigned per organism/strain rather than globally. (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled pages 6-9, marli2024geneticmodificationof pages 1-2, hardy2024yranisa pages 1-4)

**Regulatory nodes:** ComABCDE/ComCDE, ComAB exporter, ComD histidine kinase, ComE response regulator, CSP, ComRS, ComR, ComS/XIP, Opp/Ami permease, ComX/SigX, ComK, CcpA, CodY, CovR/CovRS, MecA-ClpCP, and paratox. These should be represented in taxon-specific subgraphs. (prudhomme2024pneumococcalcompetenceis pages 3-4, marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5, toussaint2024unveilingtheregulatory pages 1-6)

**Provisional 2024 nodes:** YraN nuclease and the YraN–ComM functional system. Current evidence came from a February 9, 2024 bioRxiv preprint and should not yet be treated as a universally conserved module. (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12)

### Cellular-location nodes

* extracellular region — `GO:0005576`
* cell surface — `GO:0009986`
* pilus — `GO:0009289`
* cell wall — `GO:0005618`
* outer membrane — `GO:0019867`
* periplasmic space — `GO:0042597`
* plasma membrane — `GO:0005886`
* cytoplasm — `GO:0005737`
* chromosome — `GO:0005694`

These generic GO terms are safe candidates, but envelope edges must be conditioned on monoderm versus diderm architecture.

### Taxon/context nodes

Useful exemplar taxa include *Streptococcus pneumoniae*, *S. dysgalactiae*, *Bacillus subtilis*, *Lactococcus lactis*, *Vibrio cholerae*, *Legionella pneumophila*, *Acinetobacter baylyi*, pathogenic *Acinetobacter* spp., and *Synechococcus elongatus*. Assign `NCBITaxon` CURIEs only after confirming the exact species and strain used by each experiment.

## 3. Candidate causal graph edges

The following table gives a compact graph overview. “Conserved” means broadly supported across models, not necessarily universal in every naturally competent bacterium.

| subject | predicate | object | taxon/context | evidence strength |
|---|---|---|---|---|
| Type IV competence pilus / competence pilus | captures | extracellular dsDNA | conserved bacteria; Gram+ competence pili and Gram- T4P models (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled pages 6-9, hardy2024yranisa pages 1-4) | strong, conserved |
| Pilus retraction | moves inward | DNA toward envelope uptake machinery | Vibrio cholerae; Streptococcus pneumoniae; Bacillus subtilis; broader model (zuke2024fromisotopicallylabeled pages 9-12, hardy2024yranisa pages 1-4) | strong, conserved but architecture-specific |
| ComEA | binds / ratchets | dsDNA in periplasm or at membrane-proximal uptake site | Bacillus subtilis and diderm model (zuke2024fromisotopicallylabeled pages 6-9, hardy2024yranisa pages 1-4) | moderate-strong |
| EndA nuclease | degrades one strand of | duplex transforming DNA | streptococci / S. dysgalactiae competence model (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | moderate, taxon-specific |
| ComEC | translocates | ssDNA across cytoplasmic membrane | conserved competence channel model; required in L. lactis assay (marli2024geneticmodificationof pages 1-2, hardy2024yranisa pages 1-4, toussaint2024unveilingtheregulatory pages 6-9) | strong for requirement, moderate for exact mechanism |
| ComFA | assists transport of | ssDNA through ComEC | streptococcal competence model (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | moderate |
| DprA and SsbB | protect | incoming ssDNA from nucleases | streptococci (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | moderate |
| DprA | promotes loading of | RecA onto incoming ssDNA | conserved model emphasized in 2024 review and diderm overview (zuke2024fromisotopicallylabeled pages 9-12, hardy2024yranisa pages 1-4) | strong |
| RecA | drives | homologous recombination of transforming DNA into chromosome | conserved bacteria (marli2024geneticmodificationof pages 1-2, hardy2024yranisa pages 1-4) | strong |
| XIP-ComR complex | activates transcription of | comX | Streptococcus dysgalactiae / ComRS system (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | strong, taxon-specific |
| ComX | activates transcription of | late competence genes (for DNA uptake/recombination) | S. dysgalactiae; Lactococcus lactis; streptococci broadly (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5, toussaint2024unveilingtheregulatory pages 1-6) | strong |
| CSP-ComD-ComE phosphorelay | activates transcription of | comX | Streptococcus pneumoniae / ComABCDE quorum sensing (prudhomme2024pneumococcalcompetenceis pages 3-4, toussaint2024unveilingtheregulatory pages 1-6) | strong, taxon-specific |
| Antibiotic or lethal stress | increases / induces | self-induced competent subpopulation and competence propagation | Streptococcus pneumoniae (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 2-3, prudhomme2024pneumococcalcompetenceis pages 5-6) | strong, taxon-specific |
| CcpA | represses transcription of | comX | Lactococcus lactis (toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6) | strong, taxon-specific |
| CodY | represses transcription of | comX | Lactococcus lactis (toussaint2024unveilingtheregulatory pages 1-6) | strong, taxon-specific |
| CovR (CovRS) | represses transcription of | comX | Lactococcus lactis (toussaint2024unveilingtheregulatory pages 1-6) | strong, taxon-specific |
| MecA-ClpCP machinery | degrades | ComX | Lactococcus lactis (toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6) | strong, taxon-specific |
| ComM | promotes | antibiotic tolerance / division inhibition during competence | Streptococcus pneumoniae (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8) | strong, taxon-specific |
| YraN with ComM | promotes | D-loop extension / extended recombination events | diderm species; L. pneumophila, Acinetobacter models (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12) | uncertain, 2024 preprint |
| Complete competence gene set | enables | natural transformation only under permissive conditions | S. dysgalactiae and L. lactis boundary case (marli2024geneticmodificationof pages 2-5, toussaint2024unveilingtheregulatory pages 6-9) | strong for boundary condition |


*Table: This table lists compact candidate causal edges for curating a natural competence TraitMech graph, separating conserved core uptake/recombination steps from taxon-specific regulation. It also flags the newer YraN-ComM recombination edge as uncertain because the current 2024 source is a preprint.*

### Evidence snippets and curation notes

| Proposed triple | Reference and supporting snippet | Curation note |
|---|---|---|
| competence pilus — **captures** → extracellular dsDNA | Zuke & Burton: competence pili “directly bind extracellular DNA at pilus tips”; Hardy et al.: “process is initiated by the capture of DNA by an extracellular Type IV filament.” DOI [10.1128/mmbr.00125-23](https://doi.org/10.1128/mmbr.00125-23), published March 2024; DOI [10.1101/2024.02.06.579203](https://doi.org/10.1101/2024.02.06.579203), posted February 9, 2024. (zuke2024fromisotopicallylabeled pages 9-12, hardy2024yranisa pages 1-4) | Strong core edge, but pilin identity and sequence specificity vary by taxon. |
| pilus retraction — **moves** → bound DNA toward uptake machinery | The 2024 review reports that retraction “brings bound DNA across outer membrane/cell wall”; physical obstruction of retraction decreases transformation. (zuke2024fromisotopicallylabeled pages 9-12) | Strong, but do not encode an outer-membrane step for monoderms. |
| ComEA — **binds/ratchets** → dsDNA | In *B. subtilis*, ComEA mediates irreversible membrane-proximal DNA binding; in diderms it “would function as a ratchet for double-strand DNA.” (zuke2024fromisotopicallylabeled pages 6-9, hardy2024yranisa pages 1-4) | Curate `binds` confidently; mark the ratchet mechanism somewhat model-dependent. |
| EndA — **degrades one strand of** → transforming dsDNA | Mårli et al.: “After cleavage of one of the DNA duplex strands by the nuclease EndA, single-stranded DNA….” DOI [10.1128/msphere.00214-24](https://doi.org/10.1128/msphere.00214-24), published June 21, 2024. (marli2024geneticmodificationof pages 1-2) | Good streptococcal edge; the responsible nuclease is not universally EndA. |
| ComEC — **translocates** → ssDNA across cytoplasmic membrane | Mårli et al.: ssDNA “is passed through ComEC”; Hardy et al. describe a presumed channel formed by ComEC. Deleting/deficient ComEC abolished *L. lactis* competence. (marli2024geneticmodificationof pages 1-2, hardy2024yranisa pages 1-4, toussaint2024unveilingtheregulatory pages 6-9) | Strong requirement/channel candidate; exact strand-conversion coupling remains incompletely resolved. |
| ComFA — **assists transport of** → ssDNA through ComEC | Mårli et al.: ssDNA passes through ComEC “with the help of ComFA.” A cited primary study reports ssDNA-translocase activity. (niu2025molecularmechanismsand pages 15-16, marli2024geneticmodificationof pages 1-2) | Moderate-to-strong. A direct primary-paper assertion is preferable in YAML evidence. |
| SsbB and DprA — **protect** → incoming ssDNA | Mårli et al.: intracellular ssDNA “is protected from nucleases by the ssDNA-binding proteins SsbB and DprA.” (marli2024geneticmodificationof pages 1-2) | Strong in streptococci; SSB paralog usage differs among taxa. |
| DprA — **promotes loading of** → RecA on ssDNA | The 2024 review states that DprA with Ssb proteins mediates RecA binding; Hardy et al. state that DprA-coated ssDNA promotes RecA-dependent recombination. (zuke2024fromisotopicallylabeled pages 9-12, hardy2024yranisa pages 1-4) | Strong core edge. |
| RecA — **causes** → homologous integration of transforming DNA | Mårli et al.: RecA loading allows “identification of homology regions and homologous recombination to insert the foreign DNA into the genome.” (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | Strong core edge for chromosomal transformants. |
| XIP — **binds** → ComR; XIP–ComR — **activates** → comS and comX | Mårli et al. report that imported XIP interacts with ComR, which binds promoter sequences and triggers increased `comS` and `comX` expression. (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | Strong but specific to ComRS-bearing streptococci. |
| ComX — **activates transcription of** → late competence genes | ComX recognizes CIN boxes upstream of genes for DNA uptake and recombination; in *S. dysgalactiae*, XIP rapidly induced `comX`, followed by the late marker `ssbB`. (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) | Strong; regulon membership should be strain-specific. |
| CSP/ComD/ComE~P — **activates** → comX | CSP activates the ComDE phosphorelay, after which ComE~P triggers `comX`; pre-CSP is exported by ComAB and activates ComD. (prudhomme2024pneumococcalcompetenceis pages 3-4, toussaint2024unveilingtheregulatory pages 1-6) | Strong for mitis/anginosus streptococci, including pneumococcus. |
| antibiotic stress — **increases** → pneumococcal self-induction and population competence propagation | Prudhomme et al. found stochastic stress-responsive cells and exponential propagation through the ComABCDE/CSP system; rare self-induced cells occurred at approximately 1 per 10⁷. DOI [10.1038/s41467-024-49853-2](https://doi.org/10.1038/s41467-024-49853-2), published July 2024. (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 2-3) | Strong but *S. pneumoniae*-specific; different drugs can have opposite downstream survival effects. |
| CcpA/CodY/CovR — **repress transcription of** → comX | Toussaint et al.: carbon source, nitrogen and pH are sensed by “CcpA, CodY, and CovR, which repress comX transcription directly.” (toussaint2024unveilingtheregulatory pages 1-6) | Strong *L. lactis*-specific regulatory edges. The retrieved record points to preprint DOI [10.1101/2024.02.08.579460](https://doi.org/10.1101/2024.02.08.579460), February 2024; verify the final PLOS Genetics DOI before production curation. |
| MecA–ClpCP — **degrades** → ComX | The same study identifies “ComX-degrading MecA-ClpCP machinery”; impaired degradation allows ComX to accumulate above the competence threshold. (toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6) | Strong in *L. lactis*; do not merge automatically with the related ComK-control circuit of *B. subtilis*. |
| YraN with ComM — **promotes** → D-loop extension and longer recombination | The preprint proposes that YraN is a nuclease associated with ComM. Wild-type mean recombination tracts were 6.7 kb versus 5.5 kb in `yraN` and 4.3 kb in `comM` mutants; marker co-migration at 3 kb declined from about 0.7 in wild type to 0.4 without ComM. (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12) | **Uncertain/preprint.** Suitable for a provisional edge only, with taxon and evidence-status qualifiers. |

## 4. Recent developments and quantitative findings

### Dynamic DNA-import model

The 2024 MMBR synthesis consolidates live-cell imaging across *V. cholerae*, *S. pneumoniae* and *B. subtilis*. Competence pili can extend into extracellular space, bind DNA and retract; *V. cholerae* pili reach approximately 2.5 µm. DNA-binding-deficient pili and mechanically obstructed retraction both sharply reduce transformation, supporting an active capture-and-retraction model rather than passive diffusion through the envelope. (zuke2024fromisotopicallylabeled pages 9-12)

### Competence as a population health sensor

Prudhomme and colleagues recast pneumococcal competence as a biphasic self-induction-and-propagation system. Competence affects approximately 17% of pneumococcal genes. Of 12 antibiotics surveyed, ten lethal exposures produced greater survival in competent cells; reported tolerance ratios for several cell-wall/genotoxic stresses were 2.5–7.8. Conversely, competence markedly increased sensitivity to streptomycin and kanamycin, with ratios of 0.0024 and 0.04. Deleting `comM` removed increased tolerance to ampicillin and tetracycline. Surviving tolerant competent cells also had 3–8-fold lower transformation efficiency for heterologous cassettes, consistent with hyperactivated mismatch repair. Thus, “competence increases antibiotic tolerance” is not a generalizable edge; drug, target and assay must be represented. (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8, prudhomme2024pneumococcalcompetenceis pages 5-6)

### Newly tractable pyogenic streptococci

Mårli et al. screened 179 *S. dysgalactiae* genomes: 54.2% of 59 animal-associated SDSD isolates and 69.2% of 120 SDSE isolates possessed complete intact competence machinery, totaling 64.2%. XIP induction activated `comX` and late genes and enabled allelic-exchange deletion mutants in multiple strains. This is both a real-world genetic-engineering application and evidence that genomic potential must be separated from an expressed phenotype. (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5)

### Nutrient-controlled competence in lactococci

In *L. lactis*, ComX overproduction transformed 15 of 16 tested strains at frequencies of approximately 10⁻⁷–10⁻². Under optimized spontaneous conditions, a glucose–maltose diauxic shift produced approximately 5×10⁻⁶ transformants; removing aspartate, glutamate and nitrogen bases increased this roughly tenfold to 4.5×10⁻⁵. Eight of 18 intact strains then transformed spontaneously at approximately 10⁻⁸–10⁻⁵. These results identify carbon source, nitrogen supply and pH as causal environmental variables, mediated by CcpA, CodY, CovR and ComX proteolysis. (toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6)

### Provisional YraN–ComM recombination module

The 2024 YraN work compared distant diderms and implicated a conserved nuclease in processing the displaced chromosomal strand during ComM-assisted D-loop extension. The quantitative shortening and fragmentation of recombination tracts in mutants are compelling, but the work was retrieved as a non-peer-reviewed preprint and its proposed molecular cleavage step remains model-based. (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12)

## 5. Applications and real-world significance

1. **Genome engineering:** Natural competence permits marker exchange or gene deletion using linear PCR DNA without an intermediate donor cell or phage. The 2024 *S. dysgalactiae* work used it to construct deletion mutants, while optimized *L. lactis* transformation supports development of food-fermentation and recombinant-protein chassis. (marli2024geneticmodificationof pages 1-2, toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6)
2. **Industrial biotechnology:** *L. lactis* is used in fermented foods and as a recombinant-protein, vaccine-antigen and therapeutic-delivery platform. Controlling its competence could accelerate precise strain construction, but containment and horizontal-transfer risks must be considered. (toussaint2024unveilingtheregulatory pages 1-6)
3. **Antimicrobial-resistance surveillance:** Natural transformation can acquire resistance determinants. In pathogenic *Acinetobacter*, experimental mixed populations transferred resistance islands with recombination tracts of 13–123 kb, illustrating clinically relevant genome remodeling; this supports natural transformation as an AMR route but not as an inevitable consequence of every competence episode.
4. **Mechanism-informed intervention:** Pilus–DNA binding, pilus retraction, ComEC transport and competence signaling are potential points for limiting horizontal transfer. Conversely, increasing competence can make non-model organisms genetically tractable. Such interventions remain primarily laboratory strategies rather than established clinical therapies.
5. **Evolution and adaptation:** Competence supplies alleles for adaptation, DNA repair and diversification, yet its net fitness effect is context-dependent. The 2024 pneumococcal data support an expert interpretation of competence as a stress-responsive bet-hedging system rather than merely a DNA-acquisition switch. (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8)

## 6. Recommended graph architecture

A robust TraitMech representation should separate:

1. **Conserved late-mechanism backbone:** extracellular dsDNA → competence pilus capture → retraction/envelope movement → ComEA binding → strand degradation/ssDNA formation → ComEC/ComFA transport → DprA/SSB protection → RecA loading → homologous recombination → natural transformation phenotype.
2. **Taxon-specific regulatory modules:** ComABCDE/CSP in pneumococcus; ComRS/XIP in pyogenic and other streptococci; ComK/ComS/MecA-ClpCP in *B. subtilis*; CcpA/CodY/CovRS plus MecA-ClpCP control of ComX in *L. lactis*.
3. **Contextual environmental branches:** antibiotic stress, cell density, carbon source/diauxic shift, nitrogen limitation, pH, growth phase and biofilm/in-vivo conditions.
4. **Downstream outcomes distinct from the trait:** transformant formation, recombination-tract length, acquired AMR, altered antibiotic tolerance, and engineered genotype.

## 7. Warnings—claims not ready for unqualified curation

* Do not encode natural competence as universally constitutive; it is often transient, bistable, quorum-controlled or condition-dependent.
* Do not infer phenotype solely from an intact `com` gene set.
* Do not use `EndA degrades one DNA strand` as a universal bacterial edge; nuclease identity differs and strand conversion remains unresolved in several systems.
* Do not treat all type-IV pili as competence pili or all pilus functions as DNA uptake.
* Do not assert that competence universally increases antibiotic resistance or tolerance. Pneumococcal outcomes were drug-specific and included extreme sensitization to aminoglycosides. (prudhomme2024pneumococcalcompetenceis pages 7-8)
* Do not generalize CSP/ComABCDE, XIP/ComRS, ComK or ComX regulatory relationships across bacteria.
* Do not curate the YraN cleavage mechanism as established or universal until peer-reviewed replication and biochemical resolution are available. (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12)
* Do not conflate competence with completed chromosomal integration; uptake may fail, DNA may be degraded, or replicating plasmid DNA may establish independently.
* Verify ontology definitions and species-specific UniProt/NCBITaxon accessions before adding CURIEs to YAML; label-only nodes are safer than guessed identifiers.

## DOI-first bibliography

1. Zuke JD, Burton BM. “From isotopically labeled DNA to fluorescently labeled dynamic pili: building a mechanistic model of DNA transport to the cytoplasmic membrane.” *Microbiology and Molecular Biology Reviews* 88, March 2024. DOI: [10.1128/mmbr.00125-23](https://doi.org/10.1128/mmbr.00125-23). (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled pages 6-9)
2. Prudhomme M et al. “Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics.” *Nature Communications* 15, July 2024. DOI: [10.1038/s41467-024-49853-2](https://doi.org/10.1038/s41467-024-49853-2). (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8)
3. Mårli MT et al. “Genetic modification of *Streptococcus dysgalactiae* by natural transformation.” *mSphere* 9, published June 21, 2024. DOI: [10.1128/msphere.00214-24](https://doi.org/10.1128/msphere.00214-24). (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5)
4. Toussaint F et al. “Unveiling the regulatory network controlling natural transformation in lactococci.” 2024 retrieved version. Preprint DOI: [10.1101/2024.02.08.579460](https://doi.org/10.1101/2024.02.08.579460). Verify final journal DOI before curation. (toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 1-6)
5. Hardy L et al. “YraN is a helicase-associated nuclease fostering extended recombination events by natural transformation.” bioRxiv, posted February 9, 2024. DOI: [10.1101/2024.02.06.579203](https://doi.org/10.1101/2024.02.06.579203). (hardy2024yranisa pages 1-4, hardy2024yranisa pages 9-12)
6. Godeux A-S et al. “Interbacterial Transfer of Carbapenem Resistance and Large Antibiotic Resistance Islands by Natural Transformation in Pathogenic *Acinetobacter*.” *mBio* 13, February 2022. DOI: [10.1128/mbio.02631-21](https://doi.org/10.1128/mbio.02631-21).
7. Braus S et al. “The molecular basis of FimT-mediated DNA uptake during bacterial natural transformation.” *Nature Communications* 13, August 2022. DOI: [10.1038/s41467-022-28690-1](https://doi.org/10.1038/s41467-022-28690-1).

**Curation recommendation:** retain the existing 12-node/8-edge graph as a minimal core only if it already distinguishes DNA capture, membrane transport and homologous recombination. Expand it with ComEA, ComEC, ComFA, DprA/SSB and RecA as the evidence-backed backbone; place ComRS, ComABCDE and lactococcal nutrient regulation in explicitly taxon-qualified branches; and hold YraN–ComM as provisional evidence rather than a core conserved edge.

References

1. (zuke2024fromisotopicallylabeled pages 9-12): Jason D. Zuke and Briana M. Burton. From isotopically labeled dna to fluorescently labeled dynamic pili: building a mechanistic model of dna transport to the cytoplasmic membrane. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00125-23, doi:10.1128/mmbr.00125-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (niu2025molecularmechanismsand pages 1-2): Changcheng Niu, Hao Wu, Xiaona Wang, Liying Hu, Yanping Han, and Jianjun Qiao. Molecular mechanisms and applications of natural transformation in bacteria. Frontiers in Microbiology, Jun 2025. URL: https://doi.org/10.3389/fmicb.2025.1578813, doi:10.3389/fmicb.2025.1578813. This article has 10 citations and is from a peer-reviewed journal.

3. (hardy2024yranisa pages 1-4): Léo Hardy, Julie Plantade, Violette Morales, Fanny Mazzamuro, Eduardo P. C. Rocha, Patrice Polard, and Xavier Charpentier. Yran is a helicase-associated nuclease fostering extended recombination events by natural transformation. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.06.579203, doi:10.1101/2024.02.06.579203. This article has 4 citations.

4. (toussaint2024unveilingtheregulatory pages 1-6): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (marli2024geneticmodificationof pages 1-2): M. T. Mårli, Oddvar Oppegaard, D. Porcellato, D. Straume, and M. Kjos. Genetic modification of streptococcus dysgalactiae by natural transformation. mSphere, Jun 2024. URL: https://doi.org/10.1128/msphere.00214-24, doi:10.1128/msphere.00214-24. This article has 5 citations and is from a peer-reviewed journal.

6. (marli2024geneticmodificationof pages 2-5): M. T. Mårli, Oddvar Oppegaard, D. Porcellato, D. Straume, and M. Kjos. Genetic modification of streptococcus dysgalactiae by natural transformation. mSphere, Jun 2024. URL: https://doi.org/10.1128/msphere.00214-24, doi:10.1128/msphere.00214-24. This article has 5 citations and is from a peer-reviewed journal.

7. (toussaint2024unveilingtheregulatory pages 6-9): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 6 citations and is from a domain leading peer-reviewed journal.

8. (zuke2024fromisotopicallylabeled pages 6-9): Jason D. Zuke and Briana M. Burton. From isotopically labeled dna to fluorescently labeled dynamic pili: building a mechanistic model of dna transport to the cytoplasmic membrane. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00125-23, doi:10.1128/mmbr.00125-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (prudhomme2024pneumococcalcompetenceis pages 3-4): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

10. (hardy2024yranisa pages 9-12): Léo Hardy, Julie Plantade, Violette Morales, Fanny Mazzamuro, Eduardo P. C. Rocha, Patrice Polard, and Xavier Charpentier. Yran is a helicase-associated nuclease fostering extended recombination events by natural transformation. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.06.579203, doi:10.1101/2024.02.06.579203. This article has 4 citations.

11. (prudhomme2024pneumococcalcompetenceis pages 1-2): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

12. (prudhomme2024pneumococcalcompetenceis pages 2-3): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

13. (prudhomme2024pneumococcalcompetenceis pages 5-6): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

14. (prudhomme2024pneumococcalcompetenceis pages 8-8): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

15. (prudhomme2024pneumococcalcompetenceis pages 7-8): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 18 citations and is from a highest quality peer-reviewed journal.

16. (niu2025molecularmechanismsand pages 15-16): Changcheng Niu, Hao Wu, Xiaona Wang, Liying Hu, Yanping Han, and Jianjun Qiao. Molecular mechanisms and applications of natural transformation in bacteria. Frontiers in Microbiology, Jun 2025. URL: https://doi.org/10.3389/fmicb.2025.1578813, doi:10.3389/fmicb.2025.1578813. This article has 10 citations and is from a peer-reviewed journal.