---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:47:00.145552'
end_time: '2026-08-04T14:53:35.202116'
duration_seconds: 395.06
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: free-living
  trait_identifier: traitmech:000048
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: free_living
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A habitat association in which an organism lives independently in the
    environment, not obligately associated with a host.
  parent_traits: traitmech:000047
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic
    patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole
    et al. describe rhizobia in their free-living soil phase, contrasting it with
    the host-associated endosymbiotic phase.)'
  causal_graph_summary: 'free_living_environmental_habitat: 9 nodes, 7 edges'
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
- **Trait label:** free-living
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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
- **Trait label:** free-living
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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


# Curation report: microbial trait “free-living”

**Trait:** `traitmech:000048`  
**Category:** ECOLOGY | **Kind:** CLASS | **Status:** REVIEWED  
**Parent:** `traitmech:000047`

## Executive curation recommendation

“Free-living” should be modeled primarily as a **habitat-association state**: an organism occurs and can persist independently in an environmental compartment, without an obligatory association with a host. It should not be represented as a single conserved molecular program. The literature instead supports a layered graph in which environmental conditions select free-living populations, while taxon-specific mechanisms—resource acquisition, metabolic autonomy, stress tolerance, and genomic plasticity—permit persistence in particular environments.

The strongest broadly curatable edge is **environmental variation → selects/shapes → free-living microbial community composition**. Mechanistic edges involving ribonucleotide reductase, tetrahymanol synthesis, type IV secretion, or horizontal gene transfer are informative but taxon-specific and should not be asserted as universal causes of the trait.

## 1. Trait scope and boundaries

### Operational definition

A free-living microorganism occupies an environmental habitat—such as soil, water, or sediment—without being obligately dependent on a plant, animal, fungal, or microbial host. Martiny et al. treat free-living microorganisms as environmentally distributed taxa and conclude that both contemporary environmental selection and historical/dispersal processes generate their biogeographic patterns. Their habitat definition is “an environment defined by the suite of its abiotic and biotic characteristics.” (martiny2006microbialbiogeographyputting pages 1-2)

The phenotype can be asserted from evidence such as:

1. repeated recovery from environmental samples outside hosts;
2. growth or persistence in host-free environmental microcosms;
3. a documented environmental phase in a facultative or horizontally transmitted symbiont;
4. phylogenomic or experimental evidence that the organism can proliferate independently of a host.

### Boundary cases

- **Free-living is not synonymous with planktonic.** Biofilm-associated organisms can be free-living if the biofilm is environmental and not obligately host-associated. Conversely, planktonic cells released from a host need not constitute a self-maintaining environmental population.
- **Free-living is not synonymous with metabolically autonomous.** Cross-feeding and auxotrophy can occur in free-living communities. Ramoneda et al. found amino-acid auxotrophy in free-living streamlined bacteria, although auxotrophic taxa were relatively rare in soil and aquatic systems compared with host-associated environments. (ramoneda2023taxonomicandenvironmental pages 1-2)
- **Free-living is not synonymous with nonpathogenic or nonsymbiotic.** Facultative pathogens and horizontally transmitted symbionts may have both environmental and host-associated phases. Free-living and host-associated *Alviniconcha hessleri* symbionts were strains of one species, with differentiation explained more strongly by vent field than lifestyle. (hauer2023geographynotlifestyle pages 1-2)
- **Extracellular does not necessarily mean free-living.** An extracellular microbe may remain obligately associated with a host surface or host-derived matrix.
- **Environmental detection alone is insufficient.** DNA, dormant propagules, recently released symbionts, or contamination do not establish environmental replication or host independence.
- **The state may be facultative or continuous rather than binary.** In diplomonads, *Hexamita* and *Trimitus* isolates occur in both anaerobic sediments and hosts; the authors explicitly recommend treating host dependence as a continuum and considering amphizoic lineages capable of both states. (wisniewska2024expandedgeneand pages 12-13)
- **Oligotrophy is a neighboring but distinct trait.** Oligotrophy describes adaptation to low substrate concentrations, whereas free-living describes host-independent habitat association. Many free-living organisms are copiotrophs, and some host-associated organisms show oligotrophic adaptations.

## 2. Current understanding and recent evidence

### Environmental selection and biogeography

The foundational synthesis states that “a large body of research supports the idea that free-living microbial taxa exhibit biogeographic patterns” and that “‘the environment selects’ and is, in part, responsible for spatial variation in microbial diversity.” It also rejects an unrestricted interpretation of “everything is everywhere,” supporting roles for dispersal limitation and historical contingency. (martiny2006microbialbiogeographyputting pages 1-2)

Recent estuarine data sharpen this model. Across six Australian estuaries spanning approximately 500 km, free-living seawater communities exhibited a strong distance-decay relationship, **R = −0.69**. Sediment communities had a stronger relationship within estuaries, **R = −0.50**, whereas fish-hindgut communities showed a weaker relationship, **R = −0.36**, and limited variation explained by measured environmental variables. These findings support environmental filtering and spatial structure as important upstream determinants of free-living community composition, while hosts partially buffer or replace those determinants. (suzzi2023spatialpatternsin pages 1-2)

A 2023 hydrothermal-vent comparison provides an important counterexample: free-living and host-associated snail symbionts formed monophyletic populations of a single species, and gene-content structure followed vent field rather than lifestyle. The two vent fields were approximately 300 km apart and differed in geochemistry, including hydrogen-sulfide availability. Thus, geography and local chemistry can outweigh a free-living/host-associated label. (hauer2023geographynotlifestyle pages 1-2)

### Metabolic independence and lifestyle transitions

A mechanistically strong but narrow example comes from the secondarily free-living anaerobic diplomonad *Trepomonas* sp. PC1. Its transcriptome contained expanded carbohydrate-degradation and nucleotide-metabolism capacity, proteins for bacterial membrane/cell-wall degradation, and bacterial genes acquired by horizontal transfer. An acquired ribonucleotide reductase removed the requirement to scavenge deoxyribonucleosides, while squalene–tetrahymanol cyclase generated the sterol substitute tetrahymanol under anoxia, potentially reducing dependence on eukaryotic sterols. (xu2016onthereversibility pages 1-2)

The 2024 expanded diplomonad study sequenced **13 free-living and one endobiotic isolate** and found several free-living clades nested within endobiotic lineages. The authors infer multiple lifestyle switches and propose that laterally transferred genes may have helped restore host independence. They nevertheless call for complete genomes, larger HGT analyses, and culture experiments before generalizing gene-presence patterns. (wisniewska2024expandedgeneand pages 1-3, wisniewska2024expandedgeneand pages 12-13)

### Genomic plasticity

A 2023 comparative study of six *Paracoccus* type strains, embedded in a phylogenomic analysis of **160 genomes**, identified an open pan-genome of **13,819 genes** with an **8.84% minimal chromosomal core**. Free-living strains tended to have larger genomes or more extrachromosomal elements, more genomic islands and insertion sequences, and fewer intact prophage regions. Genes associated with type IV secretion and genetic exchange were shared among the free-living genomes and were interpreted as supporting adaptation to dynamic environments. These are comparative correlations from a small genus-level sample, not universal requirements. (hollensteiner2023pangenomeanalysisof pages 1-2)

### Resource limitation

Dragone et al. analyzed three independent soil datasets: **185 US soil-profile samples**, **950 paired European bulk-soil/rhizosphere samples**, and a carbon-manipulation microcosm. Putative oligotrophs were enriched in carbon-limited settings, had smaller genomes and slower predicted maximum growth, and more often encoded pathways for use of diverse energy sources and carbon storage; chemotaxis and motility genes were under-represented. Few features were shared universally, leading the authors to emphasize multiple strategies rather than one oligotrophic program. These findings concern an environmental adaptation that can support free living but do not define the trait itself. (dragone2024taxonomicandgenomic pages 1-2)

Ramoneda et al. evaluated **26,277 genomes across 12 phyla** and community data from **3,813 samples in 12 habitat classes**. They estimated that **78.4%** of taxa could synthesize all amino acids. Auxotrophs were relatively rare in soil and aquatic systems but enriched in host-associated and fermented-food habitats. This supports biosynthetic capacity as one route to environmental independence while demonstrating that it is neither necessary nor sufficient for free-living status. (ramoneda2023taxonomicandenvironmental pages 1-2)

### Experimental boundary mechanism

Experimental evolution of free-living *Pseudomonas lurida* with *Caenorhabditis elegans* produced host-specialist populations after **10 passages**. Mutations consistently upregulated cyclic di-GMP; engineered increases in c-di-GMP across multiple *Pseudomonas* backgrounds increased host association, accompanied by biofilm-linked persistence. This is strong causal evidence for movement toward host association and is useful as a contrasting boundary mechanism, not as a positive free-living mechanism. (obeng2023bacterialcdigmphas pages 1-2)

The most defensible graph core is summarized below.

| subject | predicate | object | evidence strength | taxon/context | DOI |
|---|---|---|---|---|---|
| environmental variation | selects for spatial variation in | free-living microbial community composition | strong, broad ecology | free-living microorganisms across habitats/provinces; biogeography framework (martiny2006microbialbiogeographyputting pages 1-2) | 10.1038/nrmicro1341 |
| low available organic carbon / carbon limitation | favors | oligotrophic strategy | moderate, recent but trait-proxy | soil bacteria in subsurface, bulk, and unamended soils; resource-limited environments (dragone2024taxonomicandgenomic pages 1-2) | 10.1093/ismeco/ycae081 |
| horizontally acquired ribonucleotide reductase | reduces dependence on | deoxyribonucleoside scavenging | strong, taxon-specific | free-living diplomonad *Trepomonas* sp. PC1; secondary host independence (xu2016onthereversibility pages 1-2) | 10.1186/s12915-016-0284-z |
| squalene-tetrahymanol cyclase | enables synthesis of | tetrahymanol under anoxia | strong, taxon-specific | free-living anaerobic bacterivore *Trepomonas* sp. PC1 in anoxic sediment context (xu2016onthereversibility pages 1-2) | 10.1186/s12915-016-0284-z |
| mobile genetic elements and T4SS-associated genes | support | genomic adaptation to dynamic environments / free-living lifestyle | moderate, comparative genomic correlation; taxon-specific | free-living *Paracoccus* genomes versus host-associated genomes (hollensteiner2023pangenomeanalysisof pages 1-2) | 10.1371/journal.pone.0287947 |
| elevated c-di-GMP | increases | host association and biofilm-linked persistence | strong, experimental negative-boundary contrast | experimentally evolved *Pseudomonas lurida* with *Caenorhabditis elegans* host; contrasts with free-living state (obeng2023bacterialcdigmphas pages 1-2) | 10.1038/s41564-023-01468-x |


*Table: This table summarizes the strongest candidate causal triples for curating the free-living habitat trait, with taxon specificity and evidence strength made explicit. It also includes a contrasting host-association mechanism to help define the trait boundary.*

## 3. Candidate nodes grouped by type

### Trait and ecological-state nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| free-living environmental habitat association | `traitmech:000048` | Root phenotype node; retain identifier verbatim. |
| environmental habitat | `ENVO:01000739` (“habitat”) | Verify preferred ENVO term/version during implementation. |
| host-associated habitat | Label only pending the intended TraitMech/ENVO scope | Contrasting state; do not equate with symbiosis alone. |
| facultative free-living/endobiotic lifestyle | Label only | Useful for amphizoic taxa; may be better represented through multiple state assertions. |
| environmental filtering | `GO:0065007` is too broad; label-only ecological process preferred | Do not force an inappropriate molecular-process identifier. |
| dispersal limitation | Label only | Ecological process contributing to spatial structure. |
| geographic isolation | Label only | Supported in vent and estuarine systems. |

### Environmental and experimental factors

| Candidate node | Suggested grounding | Note |
|---|---|---|
| soil | `ENVO:00001998` | Environmental compartment. |
| sediment | `ENVO:00002007` | Includes anoxic freshwater/marine sediment contexts. |
| seawater | `ENVO:00002149` | Environmental free-living compartment. |
| anoxic environment | `ENVO:01001039` if confirmed locally; otherwise label only | Check current ENVO label before import. |
| low organic-carbon availability | Label only | Upstream selector of oligotrophic strategies. |
| nutrient limitation | `GO:0009267` for cellular response to starvation only when a cellular response is intended | Do not use a GO response term for the environmental condition itself. |
| pH, salinity, dissolved oxygen, temperature, turbidity | ChEBI/ENVO/PATO terms as appropriate | Measured environmental selectors; study-dependent. |
| experimental serial passage with host | Label only | Assay factor in the *Pseudomonas* experiment. |

### Genes, proteins, enzymes, and complexes

| Candidate node | Suggested grounding | Note |
|---|---|---|
| ribonucleoside-diphosphate reductase / ribonucleotide reductase | `EC:1.17.4.1` for the common ribonucleoside-diphosphate reductase activity; exact class depends on sequence | In *Trepomonas*, bacterial acquisition reduced deoxyribonucleoside dependence. |
| squalene–tetrahymanol cyclase | `EC:5.4.99.52` | Produces tetrahymanol; taxon-specific mechanism. |
| type IV secretion system | `GO:0030255` (“type IV protein secretion system complex”), subject to ontology-version verification | Comparative *Paracoccus* evidence; likely involved in genetic exchange. |
| diguanylate cyclase | `GO:0052621` for c-di-GMP-forming activity, subject to verification | Generates c-di-GMP; the causal experiment manipulated pathway output rather than one universal enzyme. |
| phosphodiesterases degrading c-di-GMP | Exact GO/EC term depends on enzyme family | Potential opposing regulators; not directly needed in the initial graph. |
| variant-specific surface proteins | Label only | Parasitic-ancestry signature in diplomonads; not a positive free-living mechanism. |
| tenascin-like proteins | Label only | Same caution as above. |

### Chemicals and metabolites

| Candidate node | Suggested grounding | Note |
|---|---|---|
| cyclic di-3′,5′-guanylate (c-di-GMP) | `CHEBI:49537` if confirmed against the current release | Increased levels causally promoted host association. |
| deoxyribonucleosides | `CHEBI:18240` is the class “2′-deoxyribonucleoside” if confirmed | Scavenged by RNR-deficient parasites in the diplomonad comparison. |
| deoxyribonucleotides | ChEBI class; select the exact substrate/product level used in YAML | Products supported by RNR activity. |
| squalene | `CHEBI:15440` | Substrate of squalene–tetrahymanol cyclase. |
| tetrahymanol | `CHEBI:16680` if confirmed | Sterol surrogate under anaerobic conditions. |
| sterols | `CHEBI:15889` | Host/eukaryote-derived dependency contrasted with tetrahymanol synthesis. |
| organic carbon | Label or appropriate ENVO/ChEBI material class | Environmental resource, not one discrete chemical. |
| amino acids | `CHEBI:33709` | Biosynthetic autonomy is probabilistically associated with environmental habitat. |

### Biological processes and modules

| Candidate node | Suggested grounding | Note |
|---|---|---|
| horizontal gene transfer | `GO:0032196` (“transposition”) is not equivalent; use label-only unless a suitable ontology term is selected | Do not misground HGT as transposition. |
| amino-acid biosynthesis | `GO:0008652` | Use only where pathway completeness is directly demonstrated. |
| deoxyribonucleotide biosynthesis | `GO:0009263` | Downstream of RNR activity. |
| tetrahymanol biosynthesis | MetaCyc pathway/reaction if verified; otherwise label only | Do not invent a MetaCyc or Rhea identifier. |
| carbon storage | Process-specific term depends on polymer, e.g., glycogen or PHA | Broad evidence from oligotroph genomes does not identify one universal storage product. |
| chemotaxis | `GO:0006935` | Under-represented in putative soil oligotrophs; correlational. |
| motility | `GO:0001539` is ciliary/flagellar motility in eukaryotic contexts and may be inappropriate; use a bacterial motility term after verification | Avoid broad unverified grounding. |
| biofilm formation | `GO:0042710` | Increased during experimentally evolved host specialization. |
| genetic exchange | Label only | Potential consequence of T4SS in *Paracoccus*. |

### Taxa

- *Paracoccus* — `NCBITaxon:265`
- *Pseudomonas* — `NCBITaxon:286`
- *Caenorhabditis elegans* — `NCBITaxon:6239`
- *Trepomonas* — verify the current NCBITaxon identifier before import; species PC1 may lack a stable species-level taxon.
- Diplomonadida — verify the accepted current NCBITaxon rank/identifier.
- *Alviniconcha hessleri* and its gammaproteobacterial symbiont — use study-specific taxon accessions only after checking NCBI taxonomy and MAG metadata.

## 4. Candidate evidence-backed edges

| # | Subject | Predicate | Object | Reference | Supporting snippet | Curation assessment |
|---:|---|---|---|---|---|---|
| 1 | contemporary environmental variation | selects/shapes | spatial variation in free-living microbial diversity | 10.1038/nrmicro1341 | “free-living microbial taxa exhibit biogeographic patterns” and “‘the environment selects’ … is, in part, responsible for spatial variation” | **Strong, broad ecological edge.** Suitable for the core graph, but “selects” should not imply a single molecular mechanism. (martiny2006microbialbiogeographyputting pages 1-2) |
| 2 | geographic distance and environmental variation | decrease similarity of | free-living seawater communities | 10.1093/femsec/fiad061 | Seawater showed “strong distance-decay relationships (R = −0.69)” and associations with environmental variables. | **Moderate-to-strong observational edge.** Directly measured but ecosystem-specific. (suzzi2023spatialpatternsin pages 1-2) |
| 3 | host habitat | buffers/reduces exposure to | surrounding environmental filtering | 10.1093/femsec/fiad061 | Hindgut communities had weak distance decay, R = −0.36, and “limited variation explained by environmental variables.” | **Uncertain/inferred causal wording.** Prefer “is associated with reduced environmental signal” unless intervention evidence is added. (suzzi2023spatialpatternsin pages 1-2) |
| 4 | low available organic carbon | favors | oligotrophic soil taxa | 10.1093/ismeco/ycae081 | Oligotrophic taxa were “consistently more abundant in carbon-limited environments.” | **Moderate, condition-specific.** Supports an environmental adaptation subgraph, not free living per se. (dragone2024taxonomicandgenomic pages 1-2) |
| 5 | oligotrophic strategy | is associated with | diverse-energy-source metabolism and carbon-storage pathways | 10.1093/ismeco/ycae081 | Oligotroph genomes were enriched in pathways enabling use of “a range of energy sources and store carbon.” | **Correlational.** Mark uncertain; pathway identity varied across taxa. (dragone2024taxonomicandgenomic pages 1-2) |
| 6 | oligotrophic strategy | is associated with decreased representation of | chemotaxis and motility genes | 10.1093/ismeco/ycae081 | Energy-intensive functions “like chemotaxis and motility were under-represented.” | **Correlational and not universal.** Do not encode as a necessary loss. (dragone2024taxonomicandgenomic pages 1-2) |
| 7 | horizontally acquired bacterial genes | expand | metabolic capacity of secondarily free-living *Trepomonas* | 10.1186/s12915-016-0284-z | “Most of the differences in metabolic capacity … are due to recent acquisitions of bacterial genes via gene transfer.” | **Strong within one taxon.** Represent with a taxon constraint and evolutionary timescale. (xu2016onthereversibility pages 1-2) |
| 8 | acquired ribonucleotide reductase | enables | deoxyribonucleotide synthesis | 10.1186/s12915-016-0284-z | The acquired gene “encodes a ribonucleotide reductase.” | **Strong biochemical/taxon-specific edge.** (xu2016onthereversibility pages 1-2) |
| 9 | ribonucleotide reductase acquisition | reduces requirement for | deoxyribonucleoside scavenging | 10.1186/s12915-016-0284-z | RNR “frees *Trepomonas* from the need to scavenge deoxyribonucleosides.” | **Strong, direct interpretive edge.** Good mechanistic candidate with taxon qualifier. (xu2016onthereversibility pages 1-2) |
| 10 | squalene–tetrahymanol cyclase | catalyzes/enables | tetrahymanol synthesis in anoxia | 10.1186/s12915-016-0284-z | “This enzyme synthesizes the sterol substitute tetrahymanol in the absence of oxygen.” | **Strong biochemical edge.** (xu2016onthereversibility pages 1-2) |
| 11 | tetrahymanol synthesis | reduces dependence on | sterols from other eukaryotes | 10.1186/s12915-016-0284-z | It potentially allows *Trepomonas* to thrive “without depending on sterols from other eukaryotes.” | **Plausible but explicitly potential.** Mark uncertain and taxon-specific. (xu2016onthereversibility pages 1-2) |
| 12 | mobile genetic elements/genomic islands/insertion sequences | increase/support | genomic plasticity in free-living *Paracoccus* | 10.1371/journal.pone.0287947 | Free-living genomes tended to contain more extrachromosomal elements, genomic islands, and insertion sequences. | **Comparative association.** Small taxon sample; use “associated with,” not universal causal language. (hollensteiner2023pangenomeanalysisof pages 1-2) |
| 13 | type IV secretion-associated genetic exchange | supports | adaptation to dynamic environments | 10.1371/journal.pone.0287947 | Free-living genomes shared T4SS-linked genes, described as enabling adaptation to dynamic environments. | **Moderate, inferred and *Paracoccus*-specific.** Confirm T4SS function experimentally before promoting to a core edge. (hollensteiner2023pangenomeanalysisof pages 1-2) |
| 14 | complete amino-acid biosynthetic capacity | reduces dependence on | environmental/host amino-acid supply | 10.1038/s41467-023-43435-4 | Auxotrophy is inability to synthesize required compounds; essential metabolites can instead be obtained from the environment or nearby cells. | **Biochemically reasonable but not a free-living determinant.** Use as a metabolic-autonomy modifier only. (ramoneda2023taxonomicandenvironmental pages 1-2) |
| 15 | host-associated or nutrient-rich habitat | favors/is associated with | amino-acid auxotrophy | 10.1038/s41467-023-43435-4 | Auxotrophs were more abundant in host-associated environments and fermented foods and relatively rare in soil and aquatic systems. | **Strong large-scale association, not deterministic.** Useful as a contrast. (ramoneda2023taxonomicandenvironmental pages 1-2) |
| 16 | increased c-di-GMP | increases | host association | 10.1038/s41564-023-01468-x | Mutations “uniformly upregulate” c-di-GMP, and engineered upregulation “consistently increased host association.” | **Strong experimental contrast edge.** Keep outside the positive free-living core or model as inhibition of the free-living state transition. (obeng2023bacterialcdigmphas pages 1-2) |
| 17 | increased biofilm formation | increases | persistence in nematode host | 10.1038/s41564-023-01468-x | Improved host persistence was associated with increased biofilm formation after ten passages. | **Experimental association within one system.** Biofilm formation itself must not be labeled non-free-living. (obeng2023bacterialcdigmphas pages 1-2) |
| 18 | vent-field geography/local geochemistry | structures | free-living and host-associated symbiont populations | 10.1186/s40168-023-01493-2 | Populations were “differentiated by vent field rather than by lifestyle.” | **Strong counterexample to lifestyle-essentialist graphs.** Curate as environmental context, not a universal mechanism. (hauer2023geographynotlifestyle pages 1-2) |

## 5. Suggested initial causal-graph architecture

A conservative first revision should prioritize a small general backbone and place narrow mechanisms in qualified branches:

1. **environmental habitat** → `has_condition` → environmental variation;
2. **environmental variation** → `selects/shapes` → free-living community composition;
3. **geographic isolation/dispersal limitation** → `contributes_to` → spatial differentiation;
4. **resource limitation** → `selects_for` → resource-efficient life-history strategy;
5. **metabolic autonomy** → `supports` → host-independent environmental persistence;
6. **stress tolerance/environment-specific metabolism** → `supports` → persistence in a specified habitat;
7. **genomic plasticity/HGT** → `can_enable` → acquisition of habitat-adaptive functions;
8. **obligate host dependence** → `incompatible_with` → free-living trait;
9. **facultative host association** → `coexists_with` → free-living environmental phase.

Taxon-specific subgraphs can then instantiate mechanisms:

- *Trepomonas*: HGT → RNR acquisition → deoxyribonucleotide synthesis → reduced deoxyribonucleoside scavenging; and squalene–tetrahymanol cyclase → tetrahymanol → reduced sterol dependence under anoxia.
- *Paracoccus*: mobile elements/T4SS-linked exchange → genomic plasticity → adaptation to dynamic environmental conditions, all marked comparative and uncertain.
- *Pseudomonas lurida*: c-di-GMP elevation → biofilm formation/host persistence → increased host association, retained as a boundary/transition branch.

## 6. Applications and real-world implementations

1. **Environmental microbiome classification.** The scope can guide annotation of MAGs and isolates from soils, sediments, seawater, groundwater, and engineered ecosystems while preventing environmental detection from being mistaken for demonstrated host independence.
2. **Biogeographic and climate-response modeling.** Environmental filtering, nutrient acquisition, stress response, transport, and redox modules can be incorporated into trait-based models of soil and aquatic microbiomes. Estuarine distance-decay data demonstrate that free-living communities can be spatially predictable. (suzzi2023spatialpatternsin pages 1-2)
3. **Biogeochemical process prediction.** Free-living environmental populations mediate carbon, nitrogen, sulfur, phosphorus, and redox transformations. The trait can contextualize, but should not replace, direct pathway annotations.
4. **Symbiont transmission and conservation.** Environmental populations of horizontally acquired symbionts can seed new hosts. In the *A. hessleri* system, population structure depended strongly on vent geography and geochemistry, relevant to conserving a host listed as vulnerable in the study’s account. (hauer2023geographynotlifestyle pages 1-2)
5. **Synthetic minimal-cell research.** Metabolic autonomy and host-independent growth are central to minimal-genome design, but laboratory growth in rich defined medium should be distinguished from natural environmental free living.
6. **Agricultural and environmental inoculants.** Formulations intended for soil or water release need survival under nutrient limitation, desiccation, salinity, temperature fluctuation, and competition. These are deployment-relevant supporting traits, not definitional components of free living.
7. **Pathogen and symbiosis evolution.** The experimentally demonstrated c-di-GMP route to host specialization and the diplomonad reversals to environmental life provide testable transition mechanisms. (wisniewska2024expandedgeneand pages 1-3, obeng2023bacterialcdigmphas pages 1-2)

## 7. Expert interpretation

The literature argues against a universal “free-living gene set.” Environmental free living is an ecological outcome produced by different combinations of dispersal, environmental filtering, resource-use strategy, stress physiology, community exchange, and evolutionary history. Recent comparative studies repeatedly show that **taxonomy and geography can explain as much as or more than lifestyle labels**. The most robust TraitMech representation should therefore separate:

- the observed habitat state;
- upstream environmental selectors;
- enabling but nonessential physiological modules;
- taxon-specific evolutionary mechanisms; and
- contrasting mechanisms that promote host dependence or association.

This separation prevents correlations such as genome size, motility loss, T4SS abundance, or prototrophy from being promoted into false universal causes.

## 8. Claims not yet ready for curation

1. **Do not assert that all free-living microbes have larger genomes.** The *Paracoccus* trend conflicts with streamlined free-living lineages and oligotrophic soil taxa with small genomes. (hollensteiner2023pangenomeanalysisof pages 1-2, dragone2024taxonomicandgenomic pages 1-2)
2. **Do not make amino-acid prototrophy necessary.** Free-living streamlined taxa can be auxotrophic and depend on environmental cross-feeding. (ramoneda2023taxonomicandenvironmental pages 1-2)
3. **Do not equate biofilm with host association.** Only the specific experimentally evolved *Pseudomonas* biofilm phenotype increased host persistence. Environmental biofilms remain free-living. (obeng2023bacterialcdigmphas pages 1-2)
4. **Do not generalize RNR or tetrahymanol synthesis beyond *Trepomonas*.** Both are compelling mechanisms for one secondarily free-living anaerobic lineage. (xu2016onthereversibility pages 1-2)
5. **Do not treat T4SS as a universal free-living determinant.** Its role is inferred from six *Paracoccus* type-strain genomes and may vary with the ecological function of each element. (hollensteiner2023pangenomeanalysisof pages 1-2)
6. **Do not infer environmental replication from sequence detection alone.** The detected material may represent dormant cells, propagules, recently shed symbionts, or extracellular DNA.
7. **Do not force binary classification for amphizoic organisms.** Some diplomonads plausibly occupy both endobiotic and environmental states, and additional complete genomes and reciprocal culture experiments are needed. (wisniewska2024expandedgeneand pages 12-13)
8. **Do not curate the supplied rhizobial free-living/endosymbiotic contrast mechanistically from DOI 10.1038/nrmicro.2017.171 without full-text verification.** The citation is appropriate contextual evidence for a soil phase, but no directly retrieved passage was available here to support a specific molecular edge.
9. **Do not assign unverified CURIEs.** Several proposed ontology mappings above are candidates requiring release-level confirmation; label-only nodes are preferable to invented or semantically mismatched identifiers.

## DOI-first bibliography

1. Wiśniewska MM, et al. “Expanded gene and taxon sampling of diplomonads shows multiple switches to parasitic and free-living lifestyle.” *BMC Biology*. Published September 2024. https://doi.org/10.1186/s12915-024-02013-w. (wisniewska2024expandedgeneand pages 1-3, wisniewska2024expandedgeneand pages 12-13)
2. Dragone NB, et al. “Taxonomic and genomic attributes of oligotrophic soil bacteria.” *ISME Communications*. Published June 12, 2024. https://doi.org/10.1093/ismeco/ycae081. (dragone2024taxonomicandgenomic pages 1-2)
3. Hollensteiner J, et al. “Pan-genome analysis of six Paracoccus type strain genomes reveal lifestyle traits.” *PLOS ONE*. Published December 20, 2023. https://doi.org/10.1371/journal.pone.0287947. (hollensteiner2023pangenomeanalysisof pages 1-2)
4. Ramoneda J, et al. “Taxonomic and environmental distribution of bacterial amino acid auxotrophies.” *Nature Communications*. Published November 2023. https://doi.org/10.1038/s41467-023-43435-4. (ramoneda2023taxonomicandenvironmental pages 1-2)
5. Obeng N, et al. “Bacterial c-di-GMP has a key role in establishing host–microbe symbiosis.” *Nature Microbiology*. Published online August 31, 2023. https://doi.org/10.1038/s41564-023-01468-x. (obeng2023bacterialcdigmphas pages 1-2)
6. Suzzi AL, et al. “Spatial patterns in host-associated and free-living bacterial communities across six temperate estuaries.” *FEMS Microbiology Ecology*. Published June 2, 2023. https://doi.org/10.1093/femsec/fiad061. (suzzi2023spatialpatternsin pages 1-2)
7. Hauer MA, et al. “Geography, not lifestyle, explains the population structure of free-living and host-associated deep-sea hydrothermal vent snail symbionts.” *Microbiome*. Published May 2023. https://doi.org/10.1186/s40168-023-01493-2. (hauer2023geographynotlifestyle pages 1-2)
8. Xu F, et al. “On the reversibility of parasitism: adaptation to a free-living lifestyle via gene acquisitions in the diplomonad Trepomonas sp. PC1.” *BMC Biology*. Published August 2016. https://doi.org/10.1186/s12915-016-0284-z. (xu2016onthereversibility pages 1-2)
9. Martiny JBH, et al. “Microbial biogeography: putting microorganisms on the map.” *Nature Reviews Microbiology*. Published February 2006. https://doi.org/10.1038/nrmicro1341. (martiny2006microbialbiogeographyputting pages 1-2)
10. Poole P, Ramachandran V, Terpolilli J. “Rhizobia: from saprophytes to endosymbionts.” *Nature Reviews Microbiology*. Published 2018; supplied contextual source. https://doi.org/10.1038/nrmicro.2017.171.

References

1. (martiny2006microbialbiogeographyputting pages 1-2): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3495 citations and is from a highest quality peer-reviewed journal.

2. (ramoneda2023taxonomicandenvironmental pages 1-2): Josep Ramoneda, Thomas B. N. Jensen, Morgan N. Price, Emilio O. Casamayor, and Noah Fierer. Taxonomic and environmental distribution of bacterial amino acid auxotrophies. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43435-4, doi:10.1038/s41467-023-43435-4. This article has 93 citations and is from a highest quality peer-reviewed journal.

3. (hauer2023geographynotlifestyle pages 1-2): Michelle A. Hauer, Corinna Breusing, Elizabeth Trembath-Reichert, Julie A. Huber, and Roxanne A. Beinart. Geography, not lifestyle, explains the population structure of free-living and host-associated deep-sea hydrothermal vent snail symbionts. Microbiome, May 2023. URL: https://doi.org/10.1186/s40168-023-01493-2, doi:10.1186/s40168-023-01493-2. This article has 15 citations and is from a highest quality peer-reviewed journal.

4. (wisniewska2024expandedgeneand pages 12-13): Monika M. Wiśniewska, Eric D. Salomaki, Jeffrey D. Silberman, Kristina X. Terpis, Eva Mazancová, Petr Táborský, Vasana Jinatham, Eleni Gentekaki, Ivan Čepička, and Martin Kolisko. Expanded gene and taxon sampling of diplomonads shows multiple switches to parasitic and free-living lifestyle. BMC Biology, Sep 2024. URL: https://doi.org/10.1186/s12915-024-02013-w, doi:10.1186/s12915-024-02013-w. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (suzzi2023spatialpatternsin pages 1-2): Alessandra L Suzzi, Michael Stat, Troy F Gaston, and Megan J Huggett. Spatial patterns in host-associated and free-living bacterial communities across six temperate estuaries. FEMS Microbiology Ecology, Jun 2023. URL: https://doi.org/10.1093/femsec/fiad061, doi:10.1093/femsec/fiad061. This article has 18 citations and is from a peer-reviewed journal.

6. (xu2016onthereversibility pages 1-2): Feifei Xu, Jon Jerlström-Hultqvist, Martin Kolisko, Alastair G. B. Simpson, Andrew J. Roger, Staffan G. Svärd, and Jan O. Andersson. On the reversibility of parasitism: adaptation to a free-living lifestyle via gene acquisitions in the diplomonad trepomonas sp. pc1. BMC Biology, Aug 2016. URL: https://doi.org/10.1186/s12915-016-0284-z, doi:10.1186/s12915-016-0284-z. This article has 70 citations and is from a domain leading peer-reviewed journal.

7. (wisniewska2024expandedgeneand pages 1-3): Monika M. Wiśniewska, Eric D. Salomaki, Jeffrey D. Silberman, Kristina X. Terpis, Eva Mazancová, Petr Táborský, Vasana Jinatham, Eleni Gentekaki, Ivan Čepička, and Martin Kolisko. Expanded gene and taxon sampling of diplomonads shows multiple switches to parasitic and free-living lifestyle. BMC Biology, Sep 2024. URL: https://doi.org/10.1186/s12915-024-02013-w, doi:10.1186/s12915-024-02013-w. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (hollensteiner2023pangenomeanalysisof pages 1-2): Jacqueline Hollensteiner, Dominik Schneider, Anja Poehlein, Thorsten Brinkhoff, and Rolf Daniel. Pan-genome analysis of six paracoccus type strain genomes reveal lifestyle traits. PLOS ONE, 18:e0287947, Dec 2023. URL: https://doi.org/10.1371/journal.pone.0287947, doi:10.1371/journal.pone.0287947. This article has 17 citations and is from a peer-reviewed journal.

9. (dragone2024taxonomicandgenomic pages 1-2): Nicholas B Dragone, Michael Hoffert, Michael S Strickland, and Noah Fierer. Taxonomic and genomic attributes of oligotrophic soil bacteria. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae081, doi:10.1093/ismeco/ycae081. This article has 73 citations and is from a peer-reviewed journal.

10. (obeng2023bacterialcdigmphas pages 1-2): Nancy Obeng, Anna Czerwinski, Daniel Schütz, Jan Michels, Jan Leipert, Florence Bansept, Maria Garcia Garcia, Thekla Schultheiß1†, Melinda Kemlein, Janina Fuß, Arne Traulsen, Holger Sondermann, Andreas Tholey, and Hinrich Schulenburg. Bacterial c-di-gmp has a key role in establishing host–microbe symbiosis. Nature Microbiology, 8:1809-1819, Aug 2023. URL: https://doi.org/10.1038/s41564-023-01468-x, doi:10.1038/s41564-023-01468-x. This article has 60 citations and is from a highest quality peer-reviewed journal.