---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:02:08.817061'
end_time: '2026-08-04T05:15:14.420380'
duration_seconds: 785.6
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: mobile genetic element
  trait_identifier: traitmech:000089
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: mobile_genetic_element
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing possession of DNA segments that can move
    within or between genomes and mediate horizontal gene transfer, including plasmids,
    prophages, transposable elements, and genomic islands.
  parent_traits: METPO:1000188
  synonyms: MGE
  evidence_summary: 'DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic
    elements as the agents of horizontal gene transfer and genome plasticity; parent
    of the plasmid, prophage, transposable- element, and genomic-island sub-variants.)
    | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion
    sequences as a major class of mobile genetic elements shaping bacterial genomes.)'
  causal_graph_summary: 'mge_horizontal_gene_transfer: 16 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mobile genetic element
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000089
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of DNA segments that can move within or between genomes and mediate horizontal gene transfer, including plasmids, prophages, transposable elements, and genomic islands.
- **Parent traits:** METPO:1000188
- **Synonyms:** MGE
- **Existing evidence:** DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic elements as the agents of horizontal gene transfer and genome plasticity; parent of the plasmid, prophage, transposable- element, and genomic-island sub-variants.) | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion sequences as a major class of mobile genetic elements shaping bacterial genomes.)
- **Existing causal graph summary:** mge_horizontal_gene_transfer: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **mobile genetic element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/mobile_genetic_element.yaml`.

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
- **Trait label:** mobile genetic element
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000089
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of DNA segments that can move within or between genomes and mediate horizontal gene transfer, including plasmids, prophages, transposable elements, and genomic islands.
- **Parent traits:** METPO:1000188
- **Synonyms:** MGE
- **Existing evidence:** DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic elements as the agents of horizontal gene transfer and genome plasticity; parent of the plasmid, prophage, transposable- element, and genomic-island sub-variants.) | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion sequences as a major class of mobile genetic elements shaping bacterial genomes.)
- **Existing causal graph summary:** mge_horizontal_gene_transfer: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **mobile genetic element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/mobile_genetic_element.yaml`.

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


# Curation report: mobile genetic element

## Trait record

- **Trait label:** mobile genetic element
- **Trait identifier:** `traitmech:000089`
- **Category / kind / status:** GENOMICS / CLASS / REVIEWED
- **Parent:** `METPO:1000188`
- **Synonym:** MGE

## 1. Scope summary

This trait should denote the **possession or assay-detected presence of DNA segments capable of movement within a genome or transfer between genomes/cells**. The class includes plasmids, temperate phages in the prophage state, insertion sequences and other transposable elements, integrative and conjugative elements (ICEs), integrative mobilizable elements (IMEs), and mobilizable genomic islands. A useful mechanistic division is between **intercellular MGEs**—such as conjugative plasmids and phages—and **intracellular MGEs**, such as insertion sequences, whose intercellular spread generally depends on another vehicle. Siguier and colleagues explicitly distinguish elements transmissible from cell to cell from transposable elements that move within DNA molecules or hitchhike in transmissible elements. (siguier2014bacterialinsertionsequences pages 1-2)

The trait is a **genomic property**, not itself a physiological activity. Consequently:

- **Horizontal gene transfer (HGT), conjugation, transduction, transformation, transposition, integration, and excision are processes**, not synonyms for the trait.
- **Antimicrobial resistance, virulence, bacteriocin production, metabolic versatility, and host adaptation are cargo-dependent phenotypes**, not necessary features of every MGE.
- **Integrons are gene-capture platforms and are not necessarily independently mobile**; mobility commonly results from location on plasmids or transposons.
- **Genomic islands are boundary cases:** curate as MGEs only when mobility or a mechanistically credible mobilization module is demonstrated. Sequence composition or an integration signature alone establishes putative horizontal origin, not present-day mobility.
- **Defective prophages, truncated insertion sequences, and transfer-defective plasmids remain MGE-derived sequence classes**, but should not be asserted to cause active mobility without functional evidence. Genome annotations based only on a transposase fragment can miss element boundaries or represent an ancestral “scar.” (siguier2014bacterialinsertionsequences pages 1-2)
- **Natural transformation is recipient-controlled and is not encoded by an MGE**, although transformation can acquire or remove MGE DNA. A 2024 analysis explicitly distinguishes transformation from MGE-encoded conjugation and transduction. (mazzamurro2024intragenomicconflictswith pages 1-2)

The most defensible causal-graph architecture therefore begins with separate branches for **element identity**, **mobilization**, **recipient establishment/maintenance**, **host defense**, and **cargo-derived phenotype**.

## 2. Current mechanistic understanding and recent developments

### 2.1 Conjugative transfer

Conjugation is contact-dependent transfer. In the experimentally resolved F-plasmid system, IHF, TraY, TraM, and the TraI relaxase assemble at `oriT`; TraD recruits this relaxosome to a type IV secretion system (T4SS). TraI introduces a strand-specific nick at `oriT`, remains linked to the 5′ end, and helicase activity extrudes the single-stranded T-strand for transfer through the T4SS. (couturier2023realtimevisualisationof pages 1-2)

After entry, the transferred strand circularizes and is converted to double-stranded DNA. Live-cell analysis showed that single-stranded promoters in the leading region drive immediate transient expression, whereas conversion to dsDNA switches expression to conventional promoters controlling establishment, maintenance, and subsequent dissemination. The reported model places ssDNA-to-dsDNA conversion at approximately four minutes after entry in this F-plasmid/*Escherichia coli* assay; this timing must not be generalized to other plasmids or hosts. (couturier2023realtimevisualisationof pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e)

A 2024 authoritative review describes T4SSs as envelope-spanning nanomachines that mediate contact-dependent DNA or protein transfer. VirD4-family coupling ATPases recruit substrates to the translocation channel; however, T4SSs also transport effectors or function in adhesion, so **T4SS presence alone does not prove MGE transfer**. (costa2024structuralandfunctional pages 1-5)

### 2.2 Transposition

Insertion sequences are among the smallest and most numerous autonomous prokaryotic transposable elements. Their transposases catalyse DNA-strand cleavage and rejoining during transposition; many insertions generate target-site duplications and are bounded by terminal inverted repeats. ISs can alter genome structure and activate neighboring genes, including resistance determinants. Different transposase families use different chemistries, so a graph should represent “transposase activity” generically unless the element family is known. (siguier2014bacterialinsertionsequences pages 1-2)

### 2.3 Prophage persistence and induction

Temperate phages can integrate at a discrete chromosomal site or persist extrachromosomally. In lysogeny, prophage replication with the host transmits the element vertically. Host DNA damage and activation of the bacterial SOS response are the canonical triggers for switching many temperate phages to the lytic cycle; replication and packaging are followed by host lysis and release of phage particles. This is a common—not universal—control scheme because some prophages respond to other cues or cannot be induced under standard laboratory conditions. (silpe2023inductionmechanismsand pages 1-2)

Prophage cargo can directly modify host phenotype. Recent expert synthesis cites phage-encoded photosystem components, O-antigen-modifying enzymes, capsule-modifying enzymes, and toxins underlying cholera, dysentery, diphtheria, and botulism. These are valid cargo-specific subgraphs, but not universal consequences of prophage carriage. (silpe2023inductionmechanismsand pages 1-2)

### 2.4 Integrons and gene cassettes

Integrons capture and express gene cassettes through an integron-integrase-mediated site-specific recombination system. Recent work expands the possible integration landscape beyond canonical sites by demonstrating cassette integration at widespread non-classical attG-like sites. (olsen2025metagenomicsasa pages 7-9, loot2024integroncassettesintegrate pages 38-48)

Integrons should be modeled as **mobilizable gene-capture systems**, not automatically as autonomous intercellular MGEs. Their association with plasmids, transposons, and phages can create nested or composite elements. Phage genomes carrying integron integrases, attI/attC-related sites, and cassettes provide evidence for an additional route by which integron components may move among hosts. (olsen2025metagenomicsasa pages 10-12)

### 2.5 Maintenance, cost, and host–element coevolution

Plasmid acquisition usually requires replication and expression resources and can disrupt host regulation, producing a context-dependent fitness cost. Compensatory mutations in either chromosome or plasmid can reduce that cost and promote persistence. A 2024 review identified chromosomal transcriptional regulators as common targets and grouped plasmid compensation into copy-number regulation, conjugation efficiency, and resistance-gene expression. These are synthesized mechanisms rather than universal one-step causal relations. (liu2024compensatoryevolutionof pages 1-2)

A large 2024 study measured natural transformation in 786 *Legionella pneumophila* and 496 *Acinetobacter baumannii* strains. Rates varied over six orders of magnitude; nearly half of *L. pneumophila* and more than one-third of *A. baumannii* strains were below detection under standard conditions. Transformation was negatively associated with plasmids/conjugative elements in *L. pneumophila*, prophages in *A. baumannii*, and transposable elements in both. These are population-level associations consistent with intragenomic conflict, not direct proof that every MGE suppresses competence. (mazzamurro2024intragenomicconflictswith pages 1-2)

### 2.6 Host defense

CRISPR–Cas and restriction–modification (R–M) systems can impede MGE acquisition. In *Klebsiella pneumoniae*, analysis of 932 public genomes plus 459 Chinese isolates found an inverse association between these systems and `blaKPC` plasmids. Conjugation experiments showed that combined CRISPR–Cas3 and type-I R–M activity produced an approximately **4-log reduction** in acquisition of `blaKPC`-IncF plasmids; 97% of those plasmids contained matched recognition sequences for both systems. This is strong but taxon-, defense-system-, and plasmid-specific evidence. (yang2024crisprcas3andtype pages 1-2)

## 3. Candidate nodes and ontology grounding

Identifiers below are limited to high-confidence mappings. Where precise grounding depends on the particular element or gene family, a label-only candidate is preferable to an invented or over-broad CURIE.

### A. Trait and element classes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| mobile genetic element | `traitmech:000089` | Target trait; retain verbatim. |
| plasmid | `SO:0000155` | Extrachromosomal replicon; mobility ranges from nonmobilizable to self-transmissible. |
| transposable element | `SO:0000101` | Parent for insertion sequences and transposons. |
| insertion sequence | Label only unless project mapping is verified | Usually transposase plus element ends; fragments may be inactive. |
| prophage | Label only unless project mapping is verified | Integrated or plasmid-like temperate-phage state. |
| integrative and conjugative element | Label only | Encodes integration/excision and conjugative transfer modules. |
| integrative mobilizable element | Label only | Uses a helper element’s transfer machinery. |
| integron | Label only | Gene-capture platform; not necessarily independently mobile. |
| genomic island | Label only | Require evidence of mobility for inclusion as an active MGE. |
| gene cassette | Label only | Often promoterless cargo plus recombination site. |

### B. Genes, proteins, sites, and complexes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| relaxase / TraI | `GO:0009379` where catalytic molecular function is intended | Nicks `oriT`; remains linked to and processes the transferred strand. |
| origin of transfer (`oriT`) | Label only | Cis-acting recognition and nicking site. |
| relaxosome | Label only | Nucleoprotein DNA-processing complex at `oriT`. |
| TraD / VirD4-family coupling protein | UniProt entry only for a specified sequence | Couples DNA substrate to T4SS. |
| type IV secretion system | `GO:0043684` | Transfer channel; not specific to conjugation in all organisms. |
| conjugative pilus | Label only | Donor–recipient contact/attachment in systems that encode a pilus. |
| transposase | `GO:0004803` | Catalyses transposition-associated DNA cleavage/rejoining. |
| integrase | `GO:0008907` only where site-specific DNA integration activity fits | Use separate sequence-specific UniProt IDs when available. |
| excisionase | Label only | Directionality factor in some ICE/prophage systems. |
| IntI integron integrase | UniProt entry for specified IntI | Captures, excises, or rearranges cassettes. |
| RecA | `UniProt:P0A7G6` only for *E. coli* RecA; otherwise taxon-specific UniProt | SOS activation and homologous recombination. |
| LexA | Taxon-specific UniProt | SOS repressor; cleavage/de-repression is lineage dependent. |
| CRISPR–Cas3 system | Label or system-specific ontology term | Sequence-specific anti-MGE defense. |
| type-I restriction–modification system | Label only | Distinguishes methylated self from susceptible foreign DNA. |
| plasmid partition system / SopABC | Label only | Improves segregational inheritance; SopABC is F-plasmid-specific. |

### C. Processes, cellular locations, and molecular entities

| Candidate node | Suggested grounding | Note |
|---|---|---|
| bacterial conjugation | `GO:0009291` | Intercellular DNA transfer process. |
| DNA-mediated transposition | `GO:0006313` | Intracellular movement process. |
| SOS response | `GO:0009432` | Environmental/experimental mediator of some prophage and integron responses. |
| horizontal gene transfer | `GO:0044826` | Broader process, not equivalent to MGE possession. |
| DNA | `CHEBI:16991` | Material transferred or transposed. |
| single-stranded DNA | Label only unless a verified CHEBI mapping is used | Conjugative T-strand substrate. |
| double-stranded circular DNA | Label only | Excised ICE or established plasmid form. |
| chromosome | `GO:0005694` | Integration target/localization. |
| cytoplasm | `GO:0005737` | Recipient-side plasmid establishment. |
| cell envelope | Label only | T4SS spans envelope; Gram-positive and Gram-negative architectures differ. |
| host-cell lysis | `GO:0019835` | Output of productive lytic infection. |
| biofilm | `GO:0042710` | Ecological structure that can raise cell contact and HGT opportunity; effect is system dependent. |
| DNA damage | `GO:0006974` | Upstream stress process for canonical SOS induction. |
| antibiotic | `CHEBI:33281` | Selection pressure; individual compounds should use specific CHEBI IDs. |
| antimicrobial-resistance gene | `ARO` term for the specified determinant | Do not model “ARG” as a single molecular entity when a gene is known. |

### D. Environmental and assay nodes

Candidate labels include **biofilm growth**, **planktonic growth**, **donor–recipient contact**, **sub-inhibitory antibiotic exposure**, **DNA-damaging treatment**, **whole-genome sequencing**, **long-read sequencing**, **conjugation assay**, **excision-circle PCR**, **transformation assay**, **plaque/lysis assay**, and **live-cell fluorescence microscopy**. Keep experimental perturbations separate from ecological exposures.

## 4. Candidate causal edges

The following compact table summarizes the strongest graph backbone.

| subject | predicate | object | mechanistic module | evidence strength/caveat |
|---|---|---|---|---|
| oriT-bound relaxosome | is recruited to | Type IV secretion system via TraD | conjugative plasmid transfer initiation | Strong; explicitly described for F plasmid in *E. coli*; donor-side mechanism, taxon/model-specific (couturier2023realtimevisualisationof pages 1-2, costa2024structuralandfunctional pages 1-5) |
| TraI relaxase | introduces site- and strand-specific nick at | oriT | conjugation DNA processing | Strong; direct mechanistic statement for F plasmid conjugation (couturier2023realtimevisualisationof pages 1-2) |
| TraI relaxase | remains covalently bound to and helicase-extrudes | T-strand ssDNA | conjugative transfer substrate generation | Strong; primary-study evidence in F plasmid system (couturier2023realtimevisualisationof pages 1-2) |
| Type IV secretion system | transfers | T-strand ssDNA into recipient cell | cell-to-cell DNA transfer | Strong; supported by review and live-cell study; core feature of conjugative MGEs (couturier2023realtimevisualisationof pages 1-2, costa2024structuralandfunctional pages 1-5) |
| transferred plasmid ssDNA | is converted into | dsDNA in recipient cell | plasmid establishment after transfer | Strong; real-time visualization in F plasmid system; timing/subcellular details are assay-specific (couturier2023realtimevisualisationof pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e) |
| leading ssDNA region of conjugative plasmid | enables early expression of | plasmid establishment functions | zygotic/plasmid establishment | Strong in F plasmid microscopy study; likely not universal to all MGEs (couturier2023realtimevisualisationof pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e) |
| transposase | cleaves and rejoins | DNA strands during transposition | insertion sequence/transposon mobility | Strong but mostly review-level and general across IS families; not one single enzyme class (siguier2014bacterialinsertionsequences pages 1-2) |
| bacterial SOS response / host DNA damage | triggers induction of | prophage lytic cycle | prophage induction | Strong; canonical mechanism described in 2023 review; generalized from temperate phage biology (silpe2023inductionmechanismsand pages 1-2) |
| lytic prophage induction | causes | host cell lysis and phage particle release | prophage dissemination | Strong; canonical phage life-cycle relationship (silpe2023inductionmechanismsand pages 1-2) |
| integron integrase (IntI) | catalyzes insertion/exchange of | gene cassettes at integron recombination sites | integron cassette capture and rearrangement | Strong; broad integron mechanism, mostly review-level plus recent supporting studies (tang2026targetinghorizontalgene pages 4-5, olsen2025metagenomicsasa pages 7-9) |
| plasmid acquisition | imposes | host fitness cost | plasmid maintenance/evolution | Strong; well-established review synthesis, but magnitude is plasmid-host-context dependent (liu2024compensatoryevolutionof pages 1-2) |
| compensatory evolution in chromosome or plasmid | counteracts | plasmid fitness cost | persistence of plasmids | Strong review synthesis; pathways include copy number, conjugation efficiency, AMR gene expression (liu2024compensatoryevolutionof pages 1-2) |
| CRISPR-Cas3 plus type I restriction-modification | reduces acquisition of | blaKPC-IncF plasmids | anti-MGE defense | Strong quantitative evidence in *Klebsiella pneumoniae*; reported ~4-log reduction, species/plasmid-specific (yang2024crisprcas3andtype pages 1-2) |
| mobile genetic elements (plasmids, ICEs, prophages, transposons, integrons) | carry and disseminate | antimicrobial resistance / virulence / adaptation genes | cargo-mediated host phenotype change | Strong overall, but specific cargo and impact vary by element and taxon; e.g., ICE/prophage-linked resistance in recent genomes (dec2024integrativeandconjugative pages 1-2, hossain2026mobilegeneticelements pages 5-7, hossain2026mobilegeneticelements pages 2-4, colombini2023themobilomeof pages 1-5) |


*Table: This table lists high-priority causal edges for curating the mobile genetic element trait graph, emphasizing mechanisms with direct recent support. It highlights which edges are strongest to curate first and where taxon- or assay-specific caveats should be preserved.*

The expanded evidence table below supplies curation snippets and restrictions.

| # | Subject — predicate → object | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | Relaxosome — **binds/assembles at** → `oriT` | Couturier et al., 2023, DOI [10.1038/s41467-023-35978-3](https://doi.org/10.1038/s41467-023-35978-3), published 24 Jan 2023 | “relaxosome components…are recruited to the origin of transfer (oriT)” | **Curate.** Direct F-plasmid mechanism; proteins vary among systems. (couturier2023realtimevisualisationof pages 1-2) |
| 2 | TraD coupling protein — **recruits** → relaxosome to T4SS | Same | “relaxosome complex is then recruited to the Type IV secretion system…by…TraD” | **Curate with taxon/model qualifier.** (couturier2023realtimevisualisationof pages 1-2) |
| 3 | TraI relaxase — **nicks** → plasmid DNA at `oriT` | Same | “TraI introduces a site- and strand-specific DNA cut (nick) into the plasmid’s oriT” | **High-confidence direct edge.** (couturier2023realtimevisualisationof pages 1-2) |
| 4 | TraI helicase/relaxase — **extrudes and remains attached to** → T-strand ssDNA | Same | “remains covalently bound to the 5′ phosphate end…[and] extrudes the ssDNA plasmid” | **Curate for F-like transfer.** Other relaxases may have different accessory requirements. (couturier2023realtimevisualisationof pages 1-2) |
| 5 | T4SS — **translocates** → ssDNA T-strand into recipient | Couturier et al., 2023; Costa et al., 2024, DOI [10.1038/s41579-023-00974-3](https://doi.org/10.1038/s41579-023-00974-3), published online 30 Oct 2023 / issue Mar 2024 | T4SSs function as “DNA transfer (conjugation) systems”; F-plasmid T-strand is transferred through the T4SS. | **Core edge.** Do not infer conjugation from T4SS alone because T4SSs also transport proteins or mediate adhesion. (costa2024structuralandfunctional pages 1-5, couturier2023realtimevisualisationof pages 1-2) |
| 6 | Transferred plasmid ssDNA — **is converted into** → dsDNA | Couturier et al., 2023 | “subsequent conversion into double-stranded DNA…[is] fast and efficient” | **Curate.** Approximate four-minute timing is assay-specific. (couturier2023realtimevisualisationof pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e) |
| 7 | dsDNA plasmid establishment — **activates** → maintenance and transfer-gene expression | Same | ssDNA-to-dsDNA conversion “activates the expression of other plasmid genes” and supports “establishing, maintaining and disseminating the plasmid” | **Curate as F-plasmid-specific regulatory sequence**, not universal architecture. (couturier2023realtimevisualisationof pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e) |
| 8 | Transposase — **cleaves and rejoins** → DNA during transposition | Siguier et al., 2014, DOI [10.1111/1574-6976.12067](https://doi.org/10.1111/1574-6976.12067), published online 26 Feb 2014 | “catalytic activities used in cleaving and rejoining DNA strands during transposition” | **Curate generic process edge.** Family-specific products and mechanisms need separate evidence. (siguier2014bacterialinsertionsequences pages 1-2) |
| 9 | Prophage integration/lysogeny — **enables** → vertical inheritance with host division | Silpe et al., 2023, DOI [10.1371/journal.ppat.1011363](https://doi.org/10.1371/journal.ppat.1011363), published 18 May 2023 | “prophage replication during host cell division ensures transmission to progeny” | **Curate.** Includes integrated and rarer plasmid-like prophage states. (silpe2023inductionmechanismsand pages 1-2) |
| 10 | Host DNA damage/SOS response — **induces** → lysogeny-to-lysis transition | Same | “canonical trigger…is the activation of the bacterial SOS response following host DNA damage” | **Curate as canonical/conditional**, not universal. (silpe2023inductionmechanismsand pages 1-2) |
| 11 | Lytic phage replication and packaging — **causes** → host lysis and virion release | Same | particles are “released, killing the host cell and promoting phage dissemination” | **High-confidence process edge.** (silpe2023inductionmechanismsand pages 1-2) |
| 12 | IntI integron integrase — **captures/integrates** → gene cassette | Olsen & Riber, 2025, DOI [10.3390/antibiotics14030296](https://doi.org/10.3390/antibiotics14030296), published Mar 2025; Loot et al., 2024, DOI [10.1038/s41564-023-01548-y](https://doi.org/10.1038/s41564-023-01548-y), published Jan 2024 | Integrons contain “site-specific recombination systems for capturing and integrating gene cassettes”; recent work supports non-classical integration sites. | **Curate.** Represent cassette capture separately from intercellular mobility. (olsen2025metagenomicsasa pages 7-9, loot2024integroncassettesintegrate pages 38-48) |
| 13 | MGE carriage — **imposes** → host fitness cost | Liu et al., 2024, DOI [10.1002/ece3.70121](https://doi.org/10.1002/ece3.70121), accepted 23 Jul 2024 | “plasmids require additional resources for their replication” and may impose metabolic burden | **Conditional edge.** Cost may be absent or reversed in a selective environment. (liu2024compensatoryevolutionof pages 1-2) |
| 14 | Chromosomal or plasmid compensatory evolution — **reduces** → plasmid fitness cost | Same | compensatory mutations “reduce or eliminate fitness costs, allowing the plasmid to persist” | **Curate as evolutionary mechanism**, preferably with an intermediate mutation/gene node when known. (liu2024compensatoryevolutionof pages 1-2) |
| 15 | CRISPR–Cas3 + type-I R–M — **inhibits** → `blaKPC`-IncF plasmid acquisition | Yang et al., 2024, DOI [10.1186/s12866-024-03381-7](https://doi.org/10.1186/s12866-024-03381-7), published Jul 2024 | systems “worked together to confer a 4-log reduction” in conjugative acquisition | **Strong but explicitly taxon/plasmid-specific.** (yang2024crisprcas3andtype pages 1-2) |
| 16 | ICE/prophage/transposon carriage — **associates with dissemination of** → resistance genes | Dec et al., 2024, DOI [10.3390/ijms25094638](https://doi.org/10.3390/ijms25094638), published 24 Apr 2024 | `tetM` occurred in a Tn916-like transposon within a 130-kb ICE; phage infection “appears” to have introduced `ermB` | **Uncertain/observational.** Four goose isolates plus comparative genomes; “appears” and “most likely” do not establish experimental transfer. (dec2024integrativeandconjugative pages 1-2) |
| 17 | MGE cargo gene — **confers** → resistance, virulence, or adaptation phenotype | Multiple | Plasmids carry resistance, virulence and metabolic genes; prophages can supply toxins or host-surface modifiers. | **Curate only as cargo-specific edges** tied to a named gene and phenotype. (colombini2023themobilomeof pages 1-5, silpe2023inductionmechanismsand pages 1-2) |
| 18 | Biofilm state — **promotes/opportunizes** → HGT | Michaelis & Grohmann, 2023, DOI [10.3390/antibiotics12020328](https://doi.org/10.3390/antibiotics12020328), published Feb 2023 | environmental biofilms are described as ARG-dissemination “hotspots,” with HGT often more frequent than in planktonic culture | **Conditional.** Direction and magnitude vary with species, element, matrix, antibiotic exposure, and assay. (hossain2026mobilegeneticelements pages 5-7) |

## 5. Recent statistics and application-relevant observations

1. **Direct transfer dynamics:** F-plasmid ssDNA-to-dsDNA conversion occurred at roughly four minutes in the reported microscopy model, followed by establishment-phase expression over approximately 10–90 minutes. This is valuable for designing time-resolved conjugation assays, not a universal kinetic constant. (couturier2023realtimevisualisationof media 13eb1d1e)
2. **Defense effect size:** combined CRISPR–Cas3 and type-I R–M generated an approximately 10,000-fold reduction in conjugative acquisition of the tested `blaKPC`-IncF plasmid. (yang2024crisprcas3andtype pages 1-2)
3. **Population-scale transformation:** transformation phenotypes across 1,282 strains varied by six orders of magnitude; close to half of *L. pneumophila* and over one-third of *A. baumannii* were below detection in standard conditions. (mazzamurro2024intragenomicconflictswith pages 1-2)
4. **Strain mobilome burden:** one *Streptococcus pneumoniae* genome analyzed in recent mobilome work contained a mobilome comprising 15.54% of the genome, including an ICE, IME, transposon, prophages, genomic islands, and 72 insertion sequences. This is an illustrative strain value, not an estimate for bacteria generally. (colombini2023themobilomeof pages 1-5)
5. **Recent resistance example:** in four goose-derived *Erysipelothrix rhusiopathiae* isolates, a 130-kb ICE-like region carried a Tn916-like `tetM` transposon and additional resistance genes. Comparative analysis included 363 public *E. rhusiopathiae* genomes and 13 genomes from other *Erysipelothrix* species. (dec2024integrativeandconjugative pages 1-2)
6. **Environmental perturbation example:** one synthesis reports penicillin-G stress increasing RP4 transfer from `5.6 × 10⁻4` to `1.8 × 10⁻2` events per cell, approximately 32-fold. Because this is a secondary-source example dependent on the specific community and assay, it should not become a generic antibiotic→conjugation edge without checking the underlying primary experiment. (li2025theenvironmentallifecycle pages 15-17)

## 6. Current applications and real-world implementations

- **AMR and virulence surveillance:** hybrid short/long-read whole-genome sequencing can resolve whether resistance determinants are chromosomal, plasmid-borne, nested in transposons, or associated with ICEs/prophages. Current metagenomic tools include MGEfinder, MobileElementFinder, and OriTfinder, but predictions require validation and tool outputs are not interchangeable. (olsen2025metagenomicsasa pages 10-12)
- **Outbreak and One Health analysis:** MGE-context reconstruction distinguishes clonal spread from repeated plasmid or transposon transfer. The *E. rhusiopathiae* study illustrates veterinary surveillance linking `tetM`, `erm`, and other genes to ICE, transposon, or putative prophage contexts. (dec2024integrativeandconjugative pages 1-2)
- **Synthetic biology:** plasmids are routine expression vectors; ICE-based systems can provide stable chromosomal integration and interspecies transfer. A recent streptococcal ICE-derived system was transferred by conjugation to several *Streptococcus* species and *Enterococcus faecalis*, demonstrating practical use of MGE modules as delivery platforms. (colombini2023themobilomeof pages 1-5)
- **Anti-transfer interventions:** T4SS components are considered therapeutic targets for limiting conjugation-driven resistance, while sequence-specific CRISPR systems can potentially cure or disable resistance plasmids. Current evidence is strongest in laboratory and preclinical settings, with host range, delivery, escape, and off-target effects remaining major barriers. (costa2024structuralandfunctional pages 1-5, yang2024crisprcas3andtype pages 1-2)
- **Phage and mobilome ecology:** prophage induction can restructure biofilms by killing either broad communities or selected species, depending on phage host range and community composition. This supports ecological applications but also warns that prophage activation can have unpredictable community-level effects. (silpe2023inductionmechanismsand pages 1-2)

## 7. Recommended YAML graph strategy

For `data/traits/genomics/mobile_genetic_element.yaml`, prioritize a compact, modular backbone:

1. `mobile genetic element` **has subtype** plasmid / prophage / transposable element / ICE / IME.
2. `oriT` + relaxase + coupling protein + T4SS **enable** conjugative transfer.
3. Transferred ssDNA **undergoes** circularization and dsDNA synthesis **enabling** plasmid establishment.
4. Transposase **catalyses** DNA-mediated transposition.
5. Integrase/excisionase **enable** integration–excision cycles for specified ICEs/prophages.
6. Host DNA damage → SOS response → prophage induction → lytic replication → host lysis.
7. IntI + recombination sites **enable** cassette capture/rearrangement; association with a plasmid/transposon **enables** intercellular dissemination.
8. Replication/partition and compensation **promote** persistence; fitness cost and incompatibility **oppose** persistence.
9. CRISPR–Cas and R–M systems **inhibit** acquisition when recognition conditions are satisfied.
10. Named cargo gene → named molecular function → measured resistance/virulence/adaptation phenotype.

## 8. Warnings: claims not ready for unqualified curation

- Do **not** encode “all MGEs cause HGT”; many elements are defective, nonmobilizable, or move only intracellularly.
- Do **not** treat detection of a transposase, integrase, `oriT`, T4SS, or atypical-GC region alone as proof of a complete active MGE.
- Do **not** infer that every T4SS transfers DNA; some translocate proteins or mediate adhesion. (costa2024structuralandfunctional pages 1-5)
- Do **not** equate integrons with independently mobile elements; add a plasmid/transposon/phage carrier node when supported.
- Do **not** curate the *E. rhusiopathiae* prophage→`ermB` relation as experimentally proven transfer; the authors describe it as apparent, and the study is genomic/observational. (dec2024integrativeandconjugative pages 1-2)
- Do **not** generalize the four-minute F-plasmid conversion time, the 4-log *K. pneumoniae* defense effect, or any reported antibiotic-induced transfer fold-change beyond the tested systems. (yang2024crisprcas3andtype pages 1-2, couturier2023realtimevisualisationof media 13eb1d1e)
- Treat biofilm→HGT and antibiotic exposure→mobility as context-dependent edges requiring organism, element, dose, and assay qualifiers.
- Associations from comparative genomics or GWAS—such as fewer MGEs in transformable strains—should use predicates such as **negatively associated with**, not **causes**. (mazzamurro2024intragenomicconflictswith pages 1-2)
- Avoid generic “MGE → AMR” edges. Curate named chains such as `ICEEr1023 contains Tn916-like element`; `Tn916-like element carries tetM`; `tetM expression confers tetracycline resistance`, each with appropriate evidence.
- Ontology identifiers not independently verified should remain label-only rather than being guessed.

## DOI-first bibliography

1. Couturier A. et al. **Real-time visualisation of the intracellular dynamics of conjugative plasmid transfer.** *Nature Communications* 14, 294. Published 24 January 2023. DOI: [10.1038/s41467-023-35978-3](https://doi.org/10.1038/s41467-023-35978-3). (couturier2023realtimevisualisationof pages 1-2)
2. Costa T.R.D. et al. **Structural and functional diversity of type IV secretion systems.** *Nature Reviews Microbiology* 22, 170–185. Online 30 October 2023; issue March 2024. DOI: [10.1038/s41579-023-00974-3](https://doi.org/10.1038/s41579-023-00974-3). (costa2024structuralandfunctional pages 1-5)
3. Silpe J.E., Duddy O.P., Bassler B.L. **Induction mechanisms and strategies underlying interprophage competition during polylysogeny.** *PLOS Pathogens* 19, e1011363. Published 18 May 2023. DOI: [10.1371/journal.ppat.1011363](https://doi.org/10.1371/journal.ppat.1011363). (silpe2023inductionmechanismsand pages 1-2)
4. Loot C. et al. **Integron cassettes integrate into bacterial genomes via widespread non-classical attG sites.** *Nature Microbiology* 9, 228–240. Published January 2024. DOI: [10.1038/s41564-023-01548-y](https://doi.org/10.1038/s41564-023-01548-y). (loot2024integroncassettesintegrate pages 38-48)
5. Yang Y. et al. **CRISPR-Cas3 and type I restriction-modification team up against blaKPC-IncF plasmid transfer in Klebsiella pneumoniae.** *BMC Microbiology* 24, 240. Published July 2024. DOI: [10.1186/s12866-024-03381-7](https://doi.org/10.1186/s12866-024-03381-7). (yang2024crisprcas3andtype pages 1-2)
6. Mazzamurro F. et al. **Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species.** *PLOS Biology* 22, e3002814. Published 14 October 2024. DOI: [10.1371/journal.pbio.3002814](https://doi.org/10.1371/journal.pbio.3002814). (mazzamurro2024intragenomicconflictswith pages 1-2)
7. Liu Z. et al. **Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost.** *Ecology and Evolution* 14, e70121. Accepted 23 July 2024. DOI: [10.1002/ece3.70121](https://doi.org/10.1002/ece3.70121). (liu2024compensatoryevolutionof pages 1-2)
8. Dec M. et al. **Integrative and Conjugative Elements and Prophage DNA as Carriers of Resistance Genes in Erysipelothrix rhusiopathiae Strains from Domestic Geese in Poland.** *International Journal of Molecular Sciences* 25, 4638. Published 24 April 2024. DOI: [10.3390/ijms25094638](https://doi.org/10.3390/ijms25094638). (dec2024integrativeandconjugative pages 1-2)
9. Michaelis C., Grohmann E. **Horizontal Gene Transfer of Antibiotic Resistance Genes in Biofilms.** *Antibiotics* 12, 328. Published February 2023. DOI: [10.3390/antibiotics12020328](https://doi.org/10.3390/antibiotics12020328). (hossain2026mobilegeneticelements pages 5-7)
10. Siguier P., Gourbeyre E., Chandler M. **Bacterial insertion sequences: their genomic impact and diversity.** *FEMS Microbiology Reviews* 38, 865–891. Published online 26 February 2014. DOI: [10.1111/1574-6976.12067](https://doi.org/10.1111/1574-6976.12067). (siguier2014bacterialinsertionsequences pages 1-2)
11. Olsen N.S., Riber L. **Metagenomics as a Transformative Tool for Antibiotic Resistance Surveillance.** *Antibiotics* 14, 296. Published March 2025. DOI: [10.3390/antibiotics14030296](https://doi.org/10.3390/antibiotics14030296). (olsen2025metagenomicsasa pages 10-12, olsen2025metagenomicsasa pages 7-9)
12. Frost L.S. et al. **Mobile genetic elements: the agents of open source evolution.** *Nature Reviews Microbiology* 3, 722–732. Published September 2005. DOI: [10.1038/nrmicro1235](https://doi.org/10.1038/nrmicro1235). Foundational source supplied in the existing evidence record.

References

1. (siguier2014bacterialinsertionsequences pages 1-2): Patricia Siguier, Edith Gourbeyre, and Mick Chandler. Bacterial insertion sequences: their genomic impact and diversity. FEMS Microbiology Reviews, 38:865-891, Sep 2014. URL: https://doi.org/10.1111/1574-6976.12067, doi:10.1111/1574-6976.12067. This article has 885 citations and is from a domain leading peer-reviewed journal.

2. (mazzamurro2024intragenomicconflictswith pages 1-2): Fanny Mazzamurro, Jason Baby Chirakadavil, Isabelle Durieux, Ludovic Poiré, Julie Plantade, Christophe Ginevra, Sophie Jarraud, Gottfried Wilharm, Xavier Charpentier, and Eduardo P. C. Rocha. Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species. PLOS Biology, 22:e3002814, Oct 2024. URL: https://doi.org/10.1371/journal.pbio.3002814, doi:10.1371/journal.pbio.3002814. This article has 22 citations and is from a highest quality peer-reviewed journal.

3. (couturier2023realtimevisualisationof pages 1-2): Agathe Couturier, Chloé Virolle, Kelly Goldlust, Annick Berne-Dedieu, Audrey Reuter, Sophie Nolivos, Yoshiharu Yamaichi, Sarah Bigot, and Christian Lesterlin. Real-time visualisation of the intracellular dynamics of conjugative plasmid transfer. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35978-3, doi:10.1038/s41467-023-35978-3. This article has 90 citations and is from a highest quality peer-reviewed journal.

4. (couturier2023realtimevisualisationof media 13eb1d1e): Agathe Couturier, Chloé Virolle, Kelly Goldlust, Annick Berne-Dedieu, Audrey Reuter, Sophie Nolivos, Yoshiharu Yamaichi, Sarah Bigot, and Christian Lesterlin. Real-time visualisation of the intracellular dynamics of conjugative plasmid transfer. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35978-3, doi:10.1038/s41467-023-35978-3. This article has 90 citations and is from a highest quality peer-reviewed journal.

5. (costa2024structuralandfunctional pages 1-5): Tiago R. D. Costa, Jonasz B. Patkowski, Kévin Macé, Peter J. Christie, and Gabriel Waksman. Structural and functional diversity of type iv secretion systems. Nature reviews. Microbiology, 22:170-185, Oct 2024. URL: https://doi.org/10.1038/s41579-023-00974-3, doi:10.1038/s41579-023-00974-3. This article has 142 citations.

6. (silpe2023inductionmechanismsand pages 1-2): Justin E. Silpe, Olivia P. Duddy, and Bonnie L. Bassler. Induction mechanisms and strategies underlying interprophage competition during polylysogeny. PLOS Pathogens, 19:e1011363, May 2023. URL: https://doi.org/10.1371/journal.ppat.1011363, doi:10.1371/journal.ppat.1011363. This article has 50 citations and is from a highest quality peer-reviewed journal.

7. (olsen2025metagenomicsasa pages 7-9): Nikoline S. Olsen and Leise Riber. Metagenomics as a transformative tool for antibiotic resistance surveillance: highlighting the impact of mobile genetic elements with a focus on the complex role of phages. Antibiotics, 14:296, Mar 2025. URL: https://doi.org/10.3390/antibiotics14030296, doi:10.3390/antibiotics14030296. This article has 53 citations.

8. (loot2024integroncassettesintegrate pages 38-48): Céline Loot, Gael A. Millot, Egill Richard, Eloi Littner, Claire Vit, Frédéric Lemoine, Bertrand Néron, Jean Cury, Baptiste Darracq, Théophile Niault, Delphine Lapaillerie, Vincent Parissi, Eduardo P. C. Rocha, and Didier Mazel. Integron cassettes integrate into bacterial genomes via widespread non-classical attg sites. Nature Microbiology, 9:228-240, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01548-y, doi:10.1038/s41564-023-01548-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (olsen2025metagenomicsasa pages 10-12): Nikoline S. Olsen and Leise Riber. Metagenomics as a transformative tool for antibiotic resistance surveillance: highlighting the impact of mobile genetic elements with a focus on the complex role of phages. Antibiotics, 14:296, Mar 2025. URL: https://doi.org/10.3390/antibiotics14030296, doi:10.3390/antibiotics14030296. This article has 53 citations.

10. (liu2024compensatoryevolutionof pages 1-2): Ziyi Liu, Qiuyun Zhao, Chenggang Xu, and Houhui Song. Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost. Ecology and Evolution, Aug 2024. URL: https://doi.org/10.1002/ece3.70121, doi:10.1002/ece3.70121. This article has 22 citations and is from a peer-reviewed journal.

11. (yang2024crisprcas3andtype pages 1-2): Yang Yang, Peiyao Zhou, Dongxing Tian, Weiwen Wang, Ying Zhou, and Xiaofei Jiang. Crispr-cas3 and type i restriction-modification team up against blakpc-incf plasmid transfer in klebsiella pneumoniae. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03381-7, doi:10.1186/s12866-024-03381-7. This article has 14 citations and is from a peer-reviewed journal.

12. (tang2026targetinghorizontalgene pages 4-5): Lili Tang, Wei Yang, Lingqi Yang, You Lv, and Jian Zhang. Targeting horizontal gene transfer to combat antimicrobial resistance: a review of mechanisms, drivers, and multi-omics strategies. Infection and Drug Resistance, Volume 19:1-19, Apr 2026. URL: https://doi.org/10.2147/idr.s589962, doi:10.2147/idr.s589962. This article has 4 citations and is from a peer-reviewed journal.

13. (dec2024integrativeandconjugative pages 1-2): Marta Dec, Aldert Zomer, John Webster, Tomasz Nowak, Dagmara Stępień-Pyśniak, and Renata Urban-Chmiel. Integrative and conjugative elements and prophage dna as carriers of resistance genes in erysipelothrix rhusiopathiae strains from domestic geese in poland. International Journal of Molecular Sciences, 25:4638, Apr 2024. URL: https://doi.org/10.3390/ijms25094638, doi:10.3390/ijms25094638. This article has 7 citations.

14. (hossain2026mobilegeneticelements pages 5-7): Hemayet Hossain, Md. Hasan Ali, Tanvir Ahmad, Snigdha Sharmin Binte Sayeed, Md. Abdur Nur Sakib, Khadiza Akter Brishty, Md. Shah Jahan Saleh, Md. Mosharof Hosen, Shahabuddin Ahmed, Shihab Ahmed, Md. Shahidur Rahman Chowdhury, and Md. Mahfujur Rahman. Mobile genetic elements as central drivers of antimicrobial resistance: molecular mechanisms, evolutionary ecology, one health implications and control strategies. Antibiotics, 15:418, Apr 2026. URL: https://doi.org/10.3390/antibiotics15040418, doi:10.3390/antibiotics15040418. This article has 7 citations.

15. (hossain2026mobilegeneticelements pages 2-4): Hemayet Hossain, Md. Hasan Ali, Tanvir Ahmad, Snigdha Sharmin Binte Sayeed, Md. Abdur Nur Sakib, Khadiza Akter Brishty, Md. Shah Jahan Saleh, Md. Mosharof Hosen, Shahabuddin Ahmed, Shihab Ahmed, Md. Shahidur Rahman Chowdhury, and Md. Mahfujur Rahman. Mobile genetic elements as central drivers of antimicrobial resistance: molecular mechanisms, evolutionary ecology, one health implications and control strategies. Antibiotics, 15:418, Apr 2026. URL: https://doi.org/10.3390/antibiotics15040418, doi:10.3390/antibiotics15040418. This article has 7 citations.

16. (colombini2023themobilomeof pages 1-5): Lorenzo Colombini, Francesco Santoro, Mariana Tirziu, Elisa Lazzeri, Lorenzo Morelli, Gianni Pozzi, and Francesco Iannelli. The mobilome of lactobacillus crispatus m247 includes two novel genetic elements: tn7088 coding for a putative bacteriocin and the siphovirus prophage φm247. Dec 2023. URL: https://doi.org/10.1099/mgen.0.001150, doi:10.1099/mgen.0.001150. This article has 11 citations and is from a peer-reviewed journal.

17. (li2025theenvironmentallifecycle pages 15-17): Zhiguo Li, Jialu Tang, Xueting Wang, Xiaoling Ma, Heng Yuan, Congyong Gao, Qiong Guo, Xiaoying Guo, Junfeng Wan, and Christophe Dagot. The environmental lifecycle of antibiotics and resistance genes: transmission mechanisms, challenges, and control strategies. Microorganisms, 13:2113, Sep 2025. URL: https://doi.org/10.3390/microorganisms13092113, doi:10.3390/microorganisms13092113. This article has 36 citations.