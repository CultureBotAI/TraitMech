---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:04:27.098407'
end_time: '2026-08-04T05:14:39.178617'
duration_seconds: 612.08
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pangenome openness
  trait_identifier: traitmech:000102
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: pangenome_openness
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing the structure of a species' pangenome \u2014\
    \ the balance of core versus accessory genes and whether the pangenome is open\
    \ (continually acquiring new genes across genomes) or closed."
  parent_traits: METPO:1000188
  synonyms: open pangenome
  evidence_summary: 'DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the
    microbial pan-genome concept, distinguishing core and dispensable genes and open
    versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally
    & O''Connell review why prokaryotes have pangenomes and what drives their openness.)'
  causal_graph_summary: 'pangenome_openness_hgt: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pangenome openness
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **pangenome openness** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/pangenome_openness.yaml`.

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
- **Trait label:** pangenome openness
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **pangenome openness** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/pangenome_openness.yaml`.

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


# TraitMech curation report: pangenome openness

## Trait record and scope

- **Trait label:** pangenome openness
- **Trait identifier:** `traitmech:000102`
- **Category / kind / status:** GENOMICS / CLASS / REVIEWED
- **Parent:** `METPO:1000188`
- **Recommended operational definition:** A population- or taxon-level genomic property describing whether the cumulative number of nonredundant gene families continues to increase as additional genomes are sampled, and therefore the balance between conserved core genes and variably distributed accessory genes. An **open** pangenome continues to yield novel gene families; a **closed** pangenome approaches saturation. Core genes occur in all—or, operationally, nearly all—sampled genomes; accessory genes occur in a subset, and strain-specific/singleton genes occur in one sampled genome. Thresholds such as 95% for “core” are conventions rather than biological invariants. (medini2020thepangenomea pages 7-10, tonkinhill2023challengesinprokaryote pages 4-6)

Openness is usually inferred from randomized genome-accumulation/rarefaction curves or a Heaps-law model. Under the convention used by Pardeshi et al., a decay exponent **α < 1** denotes an open pangenome and **α > 1** a closed one. However, notation differs among implementations, so the equation, fitted parameter, confidence interval, number of genomes, taxonomic scope, and software must accompany any value. (medini2020thepangenomea pages 7-10, tonkinhill2023challengesinprokaryote pages 4-6, pardeshi2024pangenomicstounderstand pages 3-7)

### What the trait is—and is not

1. **It is a property of a delimited collection and model, not an intrinsic binary state observable in one cell.** Only the pangenome parameters of the sampled genomes can be estimated; unsampled lineages, population structure, and taxonomic boundaries affect the result. (tonkinhill2023challengesinprokaryote pages 4-6)
2. **It is not genome size.** A species may have similarly sized individual genomes yet a large collective accessory pool maintained by turnover.
3. **It is not simply accessory-genome fraction.** Accessory fraction describes the current sample; openness describes the expected accumulation of new families with further sampling.
4. **It is not identical to pangenome fluidity.** Fluidity is the mean proportion of genes not shared by pairs of genomes. It is correlated with pangenome variability and is useful comparative evidence, but it does not directly measure asymptotic gene-family accumulation. Dewar et al. observed fluidities from 0.012 to 0.41 across 126 species. (dewar2024bacteriallifestyleshapes pages 2-3, dewar2024bacteriallifestyleshapes media 30d7ccd4)
5. **It is not nucleotide diversity, recombination rate, HGT rate, genome plasticity, or taxonomic diversity**, although each may influence or correlate with it.
6. **Species-level and genus-level pangenomes must not be merged.** For example, the 2024 *Pectobacterium* result is primarily a genus-level graph over 22 species, with separate species-level sub-pangenomes. (pardeshi2024pangenomicstounderstand pages 3-7)

## Current mechanistic understanding

The proximal biological determinants are **gene-family gain and loss across lineages**. HGT through transformation, conjugation, transduction, and mobile genetic elements supplies gene gains; deletion and lineage-specific loss remove genes. Selection, drift, ecological exposure, and barriers to exchange determine which gains persist. Tonkin-Hill et al. therefore recommend gain/loss-rate models as a more mechanistic alternative to treating open/closed status as a simple binary. (tonkinhill2023challengesinprokaryote pages 4-6)

The strongest recent cross-species result is Dewar et al. (May 2024), a phylogenetically controlled analysis of 126 bacterial species. Free-living species had higher fluidity than host-associated species (**R²=0.139, pMCMC=0.004**). Among 115 host-associated species, facultative host reliance, extracellular location, mutualism, and motility jointly explained **25.7%** of fluidity variation; all five lifestyle variables explained **29.9%** across 119 species. The authors interpret variable lifestyles as increasing exposure to novel genes and/or selection for niche-specific gains and losses, but could not separate adaptive from neutral contributions. These are strong comparative associations, not experimental proof that any lifestyle state directly changes Heaps-law openness. (dewar2024bacteriallifestyleshapes pages 2-3, dewar2024bacteriallifestyleshapes pages 5-5, dewar2024bacteriallifestyleshapes pages 5-7, dewar2024bacteriallifestyleshapes media 20431c56)

Selection also structures which accessory genes coexist. Across 40 *Pseudomonas* species, **86.7% of common accessory genes** participated in significant co-occurrence or avoidance relationships; non-vertically inherited coincident genes were more likely to share functions, be co-transcribed, and encode interacting proteins. This supports selection on functional combinations, but not a simple claim that selection always increases openness. (whelan2021evidenceforselection pages 1-2)

## Candidate nodes

### Trait and measurable genomic-state nodes

| Candidate node | Grounding | Curation note |
|---|---|---|
| pangenome openness | `traitmech:000102` | Target node; retain identifier verbatim. |
| pangenome | `METPO:1000188` only if this parent denotes the intended pangenome concept | Verify the parent’s label before reuse as an entity node. |
| core genome / core gene family | Label only | Prevalence threshold is assay-dependent. |
| accessory genome / accessory gene family | Label only | Includes shell/cloud partitions in some pipelines. |
| singleton or strain-specific gene family | Label only | Highly sensitive to errors and sample size. |
| pangenome fluidity | Label only | Comparative proxy, not synonymous with openness. |
| gene-family accumulation curve | Label only | Assay/output node. |
| Heaps-law exponent | Label only | Store equation and convention with the value. |
| gene gain rate; gene loss rate | Label only | Prefer these as proximal mechanistic nodes. |

### Biological processes and molecular mechanisms

| Candidate node | Suggested grounding | Role |
|---|---|---|
| horizontal gene transfer | `GO:0042710` | Umbrella process supplying nonvertical gene gains; verify ontology version. |
| natural transformation | `GO:0009294` | Uptake and incorporation of exogenous DNA; verify label/version. |
| DNA recombination | `GO:0006310` | Incorporation/reshuffling of imported DNA. |
| homologous recombination | `GO:0035825` | Candidate child process; verify before YAML insertion. |
| conjugation | Label only pending ontology verification | Plasmid/ICE-mediated transfer. |
| transduction | Label only pending ontology verification | Phage-mediated transfer. |
| DNA integration | `GO:0015074` may be relevant | Verify that the intended ontology meaning fits genomic integration. |
| transposition | `GO:0032196` | Movement of transposable elements; verify version. |
| gene deletion / gene loss | Label only | Proximal process reducing retained repertoire. |
| natural competence | Label only | Cell state enabling transformation. |
| CSP–ComD/ComE competence signaling | Taxon-specific, label only | Pneumococcal regulatory module. |
| transformasome | Label only | Multiprotein DNA-uptake machinery. |
| RecA-mediated recombination | Protein grounding should be taxon-specific UniProt | Do not assign one UniProt ID across taxa. |
| selection on accessory-gene combinations | Label only | Supported in *Pseudomonas*; direction on openness is unresolved. |
| genetic drift / neutral retention | Label only | Competing explanation; not directly resolved by current evidence. |

### Mobile elements and cellular entities

- Plasmid; integrative and conjugative element; prophage; bacteriophage; transposon; insertion sequence; genomic island; extracellular vesicle; extracellular DNA; chromosomal DNA.
- `CHEBI:16991` is a candidate for DNA, but curators should verify the current label and whether a more specific ontology term is appropriate.
- Mobile-element classes should remain label-only until a suitable sequence/mobile-element ontology is selected. They are physical carriers or genomic contexts, not pathways.

### Environmental, ecological, and experimental nodes

- Free-living lifestyle; host-associated lifestyle; obligate host reliance; facultative host reliance; intracellular host location; extracellular host location; niche/environmental variability; motility; mutualism; pathogenicity.
- Genome sampling depth; taxonomic delimitation; population structure; phylogenetic diversity; assembly quality; annotation error; gene-clustering threshold; core prevalence threshold; rarefaction procedure; pangenome software/model.
- ENVO grounding should be applied only to a specific habitat such as soil, seawater, or host-associated habitat—not to abstract “niche breadth” or “lifestyle.”

## Candidate causal edges

The following table is the recommended starting set. “Curate” means that directionality is sufficiently mechanistic for a causal graph; “uncertain” means retain scope/qualifier metadata and do not generalize beyond the evidence.

| subject | predicate | object | evidence strength | taxon/scope | key quantitative support | DOI |
|---|---|---|---|---|---|---|
| gene gain and loss rate | directly shapes | pangenome gene diversity / openness estimates | Direct mechanism (review synthesis) | Prokaryotes broadly | “The rate at which genes are gained and lost forms a critical component of the dynamics of pangenome evolution”; alternative to binary open/closed classification is explicit gain/loss modeling (tonkinhill2023challengesinprokaryote pages 4-6) | 10.1099/mgen.0.001021 |
| horizontal gene transfer | increases | accessory-gene diversity and pangenome openness | Direct mechanism (review synthesis) | Prokaryotes broadly | Open pangenomes yield “novel gene clusters... with each additional genome”; HGT has “important implications” for adaptation and gene diversity (tonkinhill2023challengesinprokaryote pages 4-6, medini2020thepangenomea pages 7-10) | 10.1099/mgen.0.001021; 10.1007/978-3-030-38281-0_1 |
| prophage integration / prophage gene cargo | contributes to growth of | accessory pangenome | Direct mechanism | *Pectobacterium* genus, 454 genomes | 30,156 homology groups total; Heaps’ α = 0.534 (<1, open); pangenome increase of 7,815 groups after expansion, mainly accessory (+6,474); prophage genes accounted for 4,801 groups (15.9%), with 3,286 accessory and 1,477 unique; 1,369 prophage-like regions detected (pardeshi2024pangenomicstounderstand pages 1-3, pardeshi2024pangenomicstounderstand pages 3-7) | 10.1101/2024.09.02.610764 |
| mobile genetic elements (plasmids, prophages, transposons) | can inhibit evolution/maintenance of | natural transformation | Association with causal interpretation | *A. baumannii* (496 genomes), *L. pneumophila* (786 genomes) | 378 gene families in *L. pneumophila* and 836 in *A. baumannii* associated with transformation inhibition; transformable strains had fewer MGEs; <5% of pangenome associated either way (mazzamurro2024intragenomicconflictswith pages 2-3, mazzamurro2024intragenomicconflictswith pages 8-10) | 10.1371/journal.pbio.3002814 |
| MGE insertion into comM | disrupts | transformation-related function | Direct mechanism, taxon-specific | *A. baumannii* | comM pseudogenized more often in non-transformable strains (phyloglm p = 9.45 × 10−9); >50% of comM inactivations due to AbaR islands, 40% CBASS, 6% Zorya (mazzamurro2024intragenomicconflictswith pages 8-10) | 10.1371/journal.pbio.3002814 |
| extracellular vesicle DNA delivery via competence system | feeds into | transformation machinery / homologous recombination | Direct mechanism, not direct openness assay | *Streptococcus pneumoniae* | EV DNA “can deliver this DNA to the transformation machinery”; purified EVs ~2.4 × 10^10 vesicles/mL; transformation requires CSP signaling, transformasome, and RecA pathway (lass2024pneumococcalextracellularvesicles pages 1-2) | 10.1128/msphere.00727-24 |
| competence signaling (CSP → ComD/ComE) and transformasome | enables | uptake of extracellular DNA for recombination | Direct mechanism, not direct openness assay | *Streptococcus pneumoniae* | CSP induces competence; transformasome “imports single-stranded DNA... and delivers it to RecA for recombination” (lass2024pneumococcalextracellularvesicles pages 1-2) | 10.1128/msphere.00727-24 |
| ecological/lifestyle variability (free-living, facultative, extracellular, mutualist, motile) | is associated with more fluid / open | pangenomes | Cross-species association, phylogenetically controlled | 126 bacterial species | Fluidity range 0.012–0.41; free-living > host-associated (R² = 0.139, pMCMC = 0.004); four host-associated lifestyle traits explained 25.7% of variance (N = 115); all five lifestyle variables explained 29.9% (N = 119) (dewar2024bacteriallifestyleshapes pages 2-3, dewar2024bacteriallifestyleshapes pages 3-5) | 10.1073/pnas.2320170121 |
| intracellular host location / obligate host reliance | is associated with lower | pangenome fluidity / openness | Cross-species association, phylogenetically controlled | Host-associated bacteria | Intracellular location correlated with lower fluidity (N = 120, R² = 0.128, pMCMC = 0.046); species more obligately reliant and intracellular had less fluid pangenomes (dewar2024bacteriallifestyleshapes pages 5-5, dewar2024bacteriallifestyleshapes pages 3-5) | 10.1073/pnas.2320170121 |
| selection on accessory-gene combinations | structures | accessory genome content | Strong association supporting selection | *Pseudomonas* pangenome, 40 species | 86.7% of common accessory genes participated in significant co-occurrence/avoidance relationships; linked genes more likely to share function, be co-transcribed, and encode interacting proteins (whelan2021evidenceforselection pages 1-2) | 10.1093/molbev/msab139 |
| population structure / biased sampling | biases inference of | openness, core size, and rarefaction-based diversity | Assay confounder | Prokaryote pangenomics broadly | Sampling only part of a phylogeny can infer larger core genome and lower diversity despite identical underlying dynamics; hospital/convenience sampling causes strong structure (tonkinhill2023challengesinprokaryote pages 4-6) | 10.1099/mgen.0.001021 |
| annotation, assembly, and gene clustering errors | inflate or distort | rarefaction curves and openness estimates | Assay confounder | Prokaryote pangenomics broadly | “gene annotation errors are frequent and can significantly bias these plots”; strict core thresholds fail to adapt to error rate and dataset diversity (tonkinhill2023challengesinprokaryote pages 4-6) | 10.1099/mgen.0.001021 |
| Heaps’ law / rarefaction model choice | operationalizes but does not equal | biological mechanism of openness | Assay/definition caveat | Prokaryote pangenomics broadly | Open/closed status often inferred from limited samples with Heaps’ law; estimates apply only to sampled genomes and can be biased if population structure/errors ignored (tonkinhill2023challengesinprokaryote pages 4-6, medini2020thepangenomea pages 7-10) | 10.1099/mgen.0.001021; 10.1007/978-3-030-38281-0_1 |


*Table: This table compacts the strongest candidate causal and quasi-causal edges relevant to microbial pangenome openness, separating direct mechanisms from cross-species associations and assay confounders. It is useful as a starting point for TraitMech curation because it highlights which relationships are strongly supportable versus which should be marked uncertain or measurement-related.*

### Edge-level curation recommendations and supporting snippets

| # | Subject–predicate–object | Supporting snippet | Interpretation and status |
|---|---|---|---|
| 1 | gene-family gain rate — **increases** → pangenome openness | “The rate at which genes are gained and lost forms a critical component of the dynamics of pangenome evolution and relates directly to the diversity of genes…” | **Curate**, preferably paired with loss/retention. This is the closest general causal edge to the target. (tonkinhill2023challengesinprokaryote pages 4-6) |
| 2 | sustained lineage-specific gene loss/turnover — **contributes to** → accessory-gene diversity | Multiple genes are “often gained and lost at once,” and gain/loss models describe pangenome dynamics. | **Curate with care.** Loss can increase between-genome heterogeneity through differential loss, but uniform loss can shrink the pangenome; predicate should be “modulates” unless lineage-specific turnover is explicit. (tonkinhill2023challengesinprokaryote pages 4-6) |
| 3 | horizontal gene transfer — **supplies gene gains that increase** → accessory repertoire | HGT has “important implications for a bacterium’s ability to adapt to new niches”; transformation, conjugation, and transduction are identified as drivers of accessory expansion. | **Curate** as an umbrella mechanism, but avoid claiming every HGT event increases long-term openness because transferred genes may be purged. (medini2020thepangenomea pages 7-10, tonkinhill2023challengesinprokaryote pages 4-6) |
| 4 | prophage integration — **adds genes to** → accessory pangenome | In 454 *Pectobacterium* genomes, “genes from prophages accounted for 4,801 (15.9%) of the pangenome homology groups”; 3,286 were accessory and 1,477 unique. | **Curate, taxon-specific.** This is direct gene-content evidence. The genus pangenome had 30,156 groups and α=0.534; 1,369 prophage-like regions were found. DOI is a 2024 preprint, so preserve preprint status. (pardeshi2024pangenomicstounderstand pages 1-3, pardeshi2024pangenomicstounderstand pages 3-7) |
| 5 | prophage gene cargo — **contributes to** → open *Pectobacterium* pangenome | “The Pectobacterium genus pangenome is open and its growth is mainly contributed by the accessory genome”; expansion added 7,815 groups, 6,474 accessory. | **Uncertain causal bridge.** Prophage contribution is quantified, but not all accessory growth was proved to be phage-derived. (pardeshi2024pangenomicstounderstand pages 1-3, pardeshi2024pangenomicstounderstand pages 3-7) |
| 6 | CSP–ComD/ComE signaling — **induces assembly of** → transformasome | “CSP activates a two-component system (ComD and ComE)… A critical phenotypic consequence… is the assembly of the transformasome.” | **Curate only in *S. pneumoniae*.** Direct molecular mechanism. (lass2024pneumococcalextracellularvesicles pages 1-2) |
| 7 | transformasome — **imports and delivers** → extracellular ssDNA to RecA | The complex “imports single-stranded DNA from the immediate extracellular environment and delivers it to RecA for recombination.” | **Curate only in the pneumococcal mechanism module.** (lass2024pneumococcalextracellularvesicles pages 1-2) |
| 8 | pneumococcal extracellular vesicles — **deliver DNA to** → transformation machinery | EV-associated DNA “can deliver this DNA to the transformation machinery of competent cells”; transfer required CSP signaling and recipient transformation machinery. | **Curate, taxon-specific.** Direct experimental HGT mechanism, but its effect on species-level openness was not measured. (lass2024pneumococcalextracellularvesicles pages 1-2) |
| 9 | MGE insertion into `comM` — **disrupts** → transformation capacity | `comM` was more often pseudogenized in nontransformable strains (**p=9.45×10⁻⁹**); >50% of interruptions were AbaR, 40% CBASS, and 6% Zorya. | **Curate, *A. baumannii*-specific.** Direct gene-disruption mechanism. Do not infer a net effect on openness without an additional demonstrated link. (mazzamurro2024intragenomicconflictswith pages 8-10) |
| 10 | MGE burden — **is negatively associated with** → transformability | In 496 *A. baumannii* and 786 *L. pneumophila* genomes, hundreds of gene families were associated with transformation inhibition, although all associations represented <5% of each pangenome. | **Uncertain/association.** Genetic conflict may select against transformation, but MGE abundance simultaneously adds accessory genes, so its net openness effect may be bidirectional. (mazzamurro2024intragenomicconflictswith pages 2-3, mazzamurro2024intragenomicconflictswith pages 8-10) |
| 11 | free-living / variable lifestyle — **is associated with increased** → pangenome fluidity | Free-living species had greater fluidity than host-associated species (**R²=0.139; pMCMC=0.004**). | **Uncertain comparative edge**, because fluidity is a proxy and the study is observational despite phylogenetic control. (dewar2024bacteriallifestyleshapes pages 2-3, dewar2024bacteriallifestyleshapes media 20431c56) |
| 12 | intracellular, obligate host association — **is associated with decreased** → pangenome fluidity | Intracellular location correlated with lower fluidity (**N=120, R²=0.128, pMCMC=0.046**). | **Uncertain comparative edge.** Plausible mediation includes reduced environmental gene exposure and genome reduction, but those mediators were not directly tested here. (dewar2024bacteriallifestyleshapes pages 5-5, dewar2024bacteriallifestyleshapes pages 3-5) |
| 13 | selection on interacting accessory genes — **structures** → accessory gene combinations | “86.7% of common accessory genes” had significant coincident relationships and were enriched for shared function, co-transcription, and protein interaction. | **Curate as ‘structures,’ not ‘increases openness.’** Strong evidence for nonrandom retention in *Pseudomonas*. (whelan2021evidenceforselection pages 1-2) |
| 14 | annotation/clustering error — **biases** → inferred pangenome openness | “Gene annotation errors are frequent and can significantly bias these plots.” | Put in an **assay/provenance subgraph**, not the biological causal graph. (tonkinhill2023challengesinprokaryote pages 4-6) |
| 15 | biased lineage sampling/population structure — **biases** → inferred openness | Sampling one clade can infer a larger core and lower gene diversity despite identical underlying dynamics. | **Mandatory assay qualifier.** (tonkinhill2023challengesinprokaryote pages 4-6) |

## Quantitative recent examples and applications

### *Pectobacterium* prophage surveillance and plant pathology

Pardeshi et al. analyzed **454 genomes from 22 species**, clustering **1,977,865 proteins into 30,156 homology groups**: 1,949 core, 19,642 accessory, and 8,571 unique groups. The genus-level Heaps exponent was **α=0.534**, and *P. versatile* and *P. brasiliense* had species-level exponents of 0.501 and 0.538. Prophage-associated genes represented **15.9%** of all homology groups. The graph was used to trace lineage-specific prophages and emerging blackleg-causing lineages, illustrating a real application in crop-pathogen diagnostics and epidemiological surveillance. (pardeshi2024pangenomicstounderstand pages 1-3, pardeshi2024pangenomicstounderstand pages 3-7)

### Lifestyle-aware comparative genomics

Dewar et al.’s 2024 analysis operationalized fluidity as the average proportion of genes not shared between two conspecific genomes. It ranged from approximately **0.01 in *Chlamydia muridarum*** to **0.41 in *Pseudomonas fluorescens***, corresponding to about 99% versus 59% pairwise gene sharing. This provides an evidence-based way to prioritize lifestyle nodes in TraitMech, while also demonstrating that ecology explains only about 30% of variation and cannot substitute for direct gain/loss measurements. (dewar2024bacteriallifestyleshapes pages 2-3, dewar2024bacteriallifestyleshapes media 30d7ccd4)

### Transformation and antimicrobial-resistance surveillance

Mazzamurro et al. measured transformation across **1,282 strains** and analyzed pangenomes containing **31,103 gene families in *A. baumannii*** and **11,932 in *L. pneumophila***. The work identifies transformation machinery and MGE conflicts as mechanistic modifiers of gene exchange. Lass et al. further demonstrated that pneumococcal extracellular vesicles carry surface-associated DNA and deliver it through competence machinery, a potential route for resistance-gene dissemination. These studies support HGT mechanism nodes but do not directly estimate changes in Heaps-law openness. (mazzamurro2024intragenomicconflictswith pages 2-3, mazzamurro2024intragenomicconflictswith pages 8-10, lass2024pneumococcalextracellularvesicles pages 1-2)

### Applied interpretation

Pangenome analysis is currently used for pathogen surveillance, resistome/virulome discovery, vaccine antigen selection, diagnostic target design, lineage tracing, and identification of niche- or host-associated accessory loci. Its practical value comes from detecting genes absent from a single reference genome. Nevertheless, “open” should not be used as a direct synonym for adaptability, pathogenicity, or resistance; those require phenotype-specific evidence.

## Recommended minimal graph architecture

A conservative first TraitMech graph could contain:

1. **ecological exposure / lifestyle variability** —associated-with→ **opportunity to encounter foreign DNA**;
2. **opportunity to encounter foreign DNA** —increases→ **HGT-mediated gene gain**;
3. **transformation**, **conjugation**, and **transduction/prophage integration** —subprocess-of→ **HGT-mediated gene gain**;
4. **natural competence** —enables→ **transformation**;
5. **CSP–ComD/ComE signaling** —activates→ **transformasome** [*S. pneumoniae*];
6. **transformasome** —delivers→ **ssDNA to RecA-mediated recombination** [*S. pneumoniae*];
7. **extracellular vesicle-associated DNA** —provides substrate for→ **transformation** [*S. pneumoniae*];
8. **prophage integration** —adds→ **accessory gene families** [*Pectobacterium*];
9. **lineage-specific gene gain and loss** —increases/modulates→ **between-genome gene-content diversity**;
10. **sustained novel gene-family accumulation** —constitutes assay evidence for→ **`traitmech:000102`**;
11. **population structure**, **annotation error**, and **clustering settings** —bias→ **inferred `traitmech:000102`** [measurement layer].

This separates biological causation from the measurement chain. Taxon-specific molecular modules should connect to the general graph through HGT/gene-gain processes rather than being asserted as universal bacterial machinery.

## Warnings: claims not ready for unqualified TraitMech curation

1. **Do not assert “HGT causes an open pangenome” without qualifiers.** HGT supplies gains, but fixation, deletion, sampling, and taxonomic scope determine the observed curve.
2. **Do not assert “plasmids/prophages increase openness” universally.** The *Pectobacterium* prophage result is strong but genus-specific; MGEs can also suppress transformation through conflict. (mazzamurro2024intragenomicconflictswith pages 8-10, pardeshi2024pangenomicstounderstand pages 3-7)
3. **Do not equate fluidity with openness.** Lifestyle edges from Dewar et al. should be marked proxy-based and observational. (dewar2024bacteriallifestyleshapes pages 2-3)
4. **Do not assign a universal direction to selection.** Selection may retain adaptive accessory modules or purge costly genes; current evidence establishes structure, not a general positive effect on openness. (whelan2021evidenceforselection pages 1-2, tonkinhill2023challengesinprokaryote pages 4-6)
5. **Do not curate effective population size as a settled cause.** Neutral diversity and niche adaptation offer competing explanations, and the 2024 path analysis found little direct influence. (dewar2024bacteriallifestyleshapes pages 5-7, tonkinhill2023challengesinprokaryote pages 4-6)
6. **Do not treat core/accessory thresholds as universal.** Roary’s common 95% core threshold is a software convention and errors accumulate with dataset size. (tonkinhill2023challengesinprokaryote pages 4-6)
7. **Do not compare Heaps exponents across studies unless equations and conventions match.** Symbols α and γ are used differently.
8. **Do not use species-wide language for genus-level analyses.** The principal *Pectobacterium* result spans 22 species. (pardeshi2024pangenomicstounderstand pages 3-7)
9. **The Pardeshi DOI is a bioRxiv DOI in the retrieved record.** Preserve its preprint status unless a peer-reviewed version and final DOI are independently verified.
10. **Ontology identifiers listed as candidates require release-level verification.** No identifiers should be inserted merely from label similarity; label-only nodes are preferable to incorrect CURIEs.

## DOI-first bibliography

1. **Dewar AE, Hao C, Belcher LJ, Ghoul M, West SA.** “Bacterial lifestyle shapes pangenomes.” *PNAS*. Published May 2024. DOI: [10.1073/pnas.2320170121](https://doi.org/10.1073/pnas.2320170121). (dewar2024bacteriallifestyleshapes pages 2-3)
2. **Mazzamurro F, et al.** “Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species.” *PLOS Biology* 22:e3002814. Published October 2024. DOI: [10.1371/journal.pbio.3002814](https://doi.org/10.1371/journal.pbio.3002814). (mazzamurro2024intragenomicconflictswith pages 2-3, mazzamurro2024intragenomicconflictswith pages 8-10)
3. **Lass SW, et al.** “Pneumococcal extracellular vesicles mediate horizontal gene transfer via the transformation machinery.” *mSphere* 9. Published online November 6, 2024; December 2024 issue. DOI: [10.1128/msphere.00727-24](https://doi.org/10.1128/msphere.00727-24). (lass2024pneumococcalextracellularvesicles pages 1-2)
4. **Pardeshi LA, et al.** “Pangenomics to understand prophage dynamics in the *Pectobacterium* genus and the radiating lineages of *P. brasiliense*.” bioRxiv preprint, September 2024. DOI: [10.1101/2024.09.02.610764](https://doi.org/10.1101/2024.09.02.610764). (pardeshi2024pangenomicstounderstand pages 1-3, pardeshi2024pangenomicstounderstand pages 3-7)
5. **Li W, Wu Q, Kwok L-y, et al.** “Population and functional genomics of lactic acid bacteria….” *Food Frontiers* 5:3–23. Published October 2024. DOI: [10.1002/fft2.321](https://doi.org/10.1002/fft2.321). (li2024populationandfunctional pages 9-9)
6. **Tonkin-Hill G, Corander J, Parkhill J.** “Challenges in prokaryote pangenomics.” *Microbial Genomics* 9:001021. Published May 2023. DOI: [10.1099/mgen.0.001021](https://doi.org/10.1099/mgen.0.001021). (tonkinhill2023challengesinprokaryote pages 4-6)
7. **Whelan FJ, Hall RJ, McInerney JO.** “Evidence for selection in the abundant accessory gene content of a prokaryote pangenome.” *Molecular Biology and Evolution* 38:3697–3708. Published May 2021. DOI: [10.1093/molbev/msab139](https://doi.org/10.1093/molbev/msab139). (whelan2021evidenceforselection pages 1-2)
8. **Medini D, Donati C, Rappuoli R, Tettelin H.** “The Pangenome: A Data-Driven Discovery in Biology.” In *The Pangenome*. Published January 2020. DOI: [10.1007/978-3-030-38281-0_1](https://doi.org/10.1007/978-3-030-38281-0_1). (medini2020thepangenomea pages 7-10)

The foundational source supplied in the trait record—Tettelin et al., DOI [10.1073/pnas.0506758102](https://doi.org/10.1073/pnas.0506758102)—should remain attached as provenance for the original microbial pangenome/open-versus-closed concept. McInerney, McNally, and O’Connell, DOI [10.1038/nmicrobiol.2017.40](https://doi.org/10.1038/nmicrobiol.2017.40), remains the key conceptual review on why prokaryotic pangenomes arise, but the edge-specific recommendations above are anchored principally in the retrieved 2023–2024 evidence.

References

1. (medini2020thepangenomea pages 7-10): Duccio Medini, Claudio Donati, Rino Rappuoli, and Hervé Tettelin. The Pangenome: A Data-Driven Discovery in Biology, pages 3-20. Springer International Publishing, Jan 2020. URL: https://doi.org/10.1007/978-3-030-38281-0\_1, doi:10.1007/978-3-030-38281-0\_1. This article has 37 citations.

2. (tonkinhill2023challengesinprokaryote pages 4-6): Gerry Tonkin-Hill, Jukka Corander, and Julian Parkhill. Challenges in prokaryote pangenomics. Microbial Genomics, May 2023. URL: https://doi.org/10.1099/mgen.0.001021, doi:10.1099/mgen.0.001021. This article has 42 citations and is from a peer-reviewed journal.

3. (pardeshi2024pangenomicstounderstand pages 3-7): Lakhansing A. Pardeshi, Inge van Duivenbode, Michiel J. C. Pel, Eef M. Jonkheer, Anne Kupczok, Dick de Ridder, Sandra Smit, and Theo A. J. van der Lee. Pangenomics to understand prophage dynamics in the pectobacterium genus and the radiating lineages of pectobacterium brasiliense. Microbial Genomics, Sep 2024. URL: https://doi.org/10.1101/2024.09.02.610764, doi:10.1101/2024.09.02.610764. This article has 0 citations and is from a peer-reviewed journal.

4. (dewar2024bacteriallifestyleshapes pages 2-3): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

5. (dewar2024bacteriallifestyleshapes media 30d7ccd4): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

6. (dewar2024bacteriallifestyleshapes pages 5-5): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

7. (dewar2024bacteriallifestyleshapes pages 5-7): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

8. (dewar2024bacteriallifestyleshapes media 20431c56): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

9. (whelan2021evidenceforselection pages 1-2): Fiona J Whelan, Rebecca J Hall, and James O McInerney. Evidence for selection in the abundant accessory gene content of a prokaryote pangenome. Molecular Biology and Evolution, 38:3697-3708, May 2021. URL: https://doi.org/10.1093/molbev/msab139, doi:10.1093/molbev/msab139. This article has 67 citations and is from a highest quality peer-reviewed journal.

10. (pardeshi2024pangenomicstounderstand pages 1-3): Lakhansing A. Pardeshi, Inge van Duivenbode, Michiel J. C. Pel, Eef M. Jonkheer, Anne Kupczok, Dick de Ridder, Sandra Smit, and Theo A. J. van der Lee. Pangenomics to understand prophage dynamics in the pectobacterium genus and the radiating lineages of pectobacterium brasiliense. Microbial Genomics, Sep 2024. URL: https://doi.org/10.1101/2024.09.02.610764, doi:10.1101/2024.09.02.610764. This article has 0 citations and is from a peer-reviewed journal.

11. (mazzamurro2024intragenomicconflictswith pages 2-3): Fanny Mazzamurro, Jason Baby Chirakadavil, Isabelle Durieux, Ludovic Poiré, Julie Plantade, Christophe Ginevra, Sophie Jarraud, Gottfried Wilharm, Xavier Charpentier, and Eduardo P. C. Rocha. Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species. PLOS Biology, 22:e3002814, Oct 2024. URL: https://doi.org/10.1371/journal.pbio.3002814, doi:10.1371/journal.pbio.3002814. This article has 22 citations and is from a highest quality peer-reviewed journal.

12. (mazzamurro2024intragenomicconflictswith pages 8-10): Fanny Mazzamurro, Jason Baby Chirakadavil, Isabelle Durieux, Ludovic Poiré, Julie Plantade, Christophe Ginevra, Sophie Jarraud, Gottfried Wilharm, Xavier Charpentier, and Eduardo P. C. Rocha. Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species. PLOS Biology, 22:e3002814, Oct 2024. URL: https://doi.org/10.1371/journal.pbio.3002814, doi:10.1371/journal.pbio.3002814. This article has 22 citations and is from a highest quality peer-reviewed journal.

13. (lass2024pneumococcalextracellularvesicles pages 1-2): Sarah Werner Lass, Bailey E. Smith, Shaw Camphire, Rory A. Eutsey, Jojo A. Prentice, Saigopalakrishna S. Yerneni, Ashni Arun, Andrew A. Bridges, Jason W. Rosch, James F. Conway, Phil Campbell, and N. Luisa Hiller. Pneumococcal extracellular vesicles mediate horizontal gene transfer via the transformation machinery. mSphere, Dec 2024. URL: https://doi.org/10.1128/msphere.00727-24, doi:10.1128/msphere.00727-24. This article has 10 citations and is from a peer-reviewed journal.

14. (dewar2024bacteriallifestyleshapes pages 3-5): Anna E. Dewar, Chunhui Hao, Laurence J. Belcher, Melanie Ghoul, and Stuart A. West. Bacterial lifestyle shapes pangenomes. Proceedings of the National Academy of Sciences of the United States of America, May 2024. URL: https://doi.org/10.1073/pnas.2320170121, doi:10.1073/pnas.2320170121. This article has 67 citations and is from a highest quality peer-reviewed journal.

15. (li2024populationandfunctional pages 9-9): Weicheng Li, Qiong Wu, Lai‐yu Kwok, Heping Zhang, Renyou Gan, and Zhihong Sun. Population and functional genomics of lactic acid bacteria, an important group of food microorganism: current knowledge, challenges, and perspectives. Food Frontiers, 5:3-23, Oct 2024. URL: https://doi.org/10.1002/fft2.321, doi:10.1002/fft2.321. This article has 53 citations and is from a peer-reviewed journal.