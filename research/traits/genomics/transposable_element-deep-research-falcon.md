---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:22:02.782583'
end_time: '2026-08-04T05:32:14.662152'
duration_seconds: 611.88
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: transposable element
  trait_identifier: traitmech:000092
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: transposable_element
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing possession of transposable elements \u2014\
    \ such as insertion sequences and transposons \u2014 that move within the genome\
    \ and drive genome rearrangement, gene inactivation, and plasticity."
  parent_traits: traitmech:000089
  synonyms: insertion sequence, transposon
  evidence_summary: 'DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler
    review bacterial insertion sequences and their genomic impact and diversity.)
    | DOI:10.1038/nrmicro1235:  (Frost et al. include transposons among the mobile
    genetic elements driving genome evolution.)'
  causal_graph_summary: 'te_transposition_rearrangement: 8 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** transposable element
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000092
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of transposable elements — such as insertion sequences and transposons — that move within the genome and drive genome rearrangement, gene inactivation, and plasticity.
- **Parent traits:** traitmech:000089
- **Synonyms:** insertion sequence, transposon
- **Existing evidence:** DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review bacterial insertion sequences and their genomic impact and diversity.) | DOI:10.1038/nrmicro1235:  (Frost et al. include transposons among the mobile genetic elements driving genome evolution.)
- **Existing causal graph summary:** te_transposition_rearrangement: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **transposable element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/transposable_element.yaml`.

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
- **Trait label:** transposable element
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000092
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of transposable elements — such as insertion sequences and transposons — that move within the genome and drive genome rearrangement, gene inactivation, and plasticity.
- **Parent traits:** traitmech:000089
- **Synonyms:** insertion sequence, transposon
- **Existing evidence:** DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review bacterial insertion sequences and their genomic impact and diversity.) | DOI:10.1038/nrmicro1235:  (Frost et al. include transposons among the mobile genetic elements driving genome evolution.)
- **Existing causal graph summary:** te_transposition_rearrangement: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **transposable element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/transposable_element.yaml`.

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


# Curation report: microbial transposable element

**Trait:** `traitmech:000092`  
**Category:** GENOMICS | **Term kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** `traitmech:000089`

## 1. Scope summary

This trait should mean **genomic possession of at least one transposable element (TE)**: a DNA segment capable of changing genomic location through element-encoded or trans-supplied transposition machinery. In prokaryotes, an insertion sequence (IS) is the simplest autonomous form—typically a transposase ORF bounded by cognate ends—whereas larger or composite transposons may additionally carry “passenger” genes such as antimicrobial-resistance determinants. Nonautonomous elements belong in scope when recognizable as transposase-mobilizable TE derivatives. (hickman2016dnatranspositionat pages 2-3, siguier2014bacterialinsertionsequences pages 12-13)

The trait records **possession**, not necessarily current transposition activity. A defective or transcriptionally silent TE can therefore satisfy the trait, while an assay showing transposition rate is a related but different phenotype. Likewise, Tn-seq libraries made by experimentally delivering engineered Tn5/Mariner elements do not establish that the tested wild-type strain naturally possesses a TE. Modern Tn-seq constructs commonly place transposase outside the inserted segment to prevent remobilization. (fernandezgarcia2024essentialgenesdiscovery pages 2-4, fernandezgarcia2024essentialgenesdiscovery pages 1-2)

### Boundary cases

- **Include:** autonomous ISs; simple and composite transposons; replicative transposons; mobilizable nonautonomous TE derivatives; chromosomal or plasmid-borne elements.
- **Do not equate with:** plasmid possession, integron possession, prophage, integrative/conjugative elements, or horizontal gene transfer generally. These entities can carry or interact with TEs but have distinct replication/transfer machinery.
- **Do not require:** a resistance gene, terminal inverted repeats, target-site duplication, or a cut-and-paste mechanism. These are common but not universal. HUH-family elements use different chemistry, and some “peel-and-paste” systems do not produce target-site duplications. (hickman2016dnatranspositionat pages 5-6, tenjocastano2022transposonsandcrispr pages 2-3)
- **Assay caution:** a transposase annotation alone is suggestive, but fragmented assemblies and domesticated transposases can produce false-positive trait calls. Prefer a bounded element architecture, family assignment, or insertion evidence.

## 2. Current mechanistic model

The most defensible generic causal chain is:

**TE DNA containing cognate ends → transposase binding → end cleavage/excision or replicative strand transfer → target-DNA capture and integration → gap repair/target-site duplication where applicable → insertional mutation, altered neighboring-gene expression, or genome rearrangement → genomic plasticity.**

Transposases are site-specific endonucleases for their own element ends but are often less sequence-specific toward target DNA. In canonical DDE systems, acidic active-site residues coordinate divalent metal ions; exposed 3′-OH groups then attack target-DNA phosphodiester bonds. (hickman2016dnatranspositionat pages 3-5)

Mechanistic branching is essential. Cut-and-paste systems excise the donor copy; copy-in/replicative systems retain and duplicate it; copy-out–paste-in pathways pass through circular intermediates. IS200/IS605- and IS91-related HUH transposases instead use single-stranded intermediates and covalent 5′-phosphotyrosine linkages. (hickman2016dnatranspositionat pages 5-6, hickman2016dnatranspositionat pages 2-3)

For Tn3-family replicative transposition, transposase nicks both 3′ ends, the resulting 3′-OH groups attack staggered target strands, and repair of 5-bp gaps generates 5-bp direct target-site duplications in the cointegrate. This exact duplication length is family-specific and must not be generalized to all TEs. (nicolas2015thetn3familyof pages 13-15)

## 3. Candidate nodes grouped by type

### A. Trait and element-architecture nodes

- `traitmech:000092` — transposable element possession
- insertion sequence; simple transposon; composite transposon
- autonomous TE; nonautonomous TE
- transposon left end/right end
- terminal inverted repeat
- passenger gene/cargo DNA
- target-site duplication

These architecture nodes should remain **label-only** unless the project has verified ontology terms. ISfinder is the relevant specialist nomenclature resource; one review reported more than 4,000 classified IS sequences and about 30 recognized prokaryotic IS families at that time. (hickman2016dnatranspositionat pages 5-6)

### B. Genes, proteins, and complexes

- **transposase** — DDE/DD(E/D) or HUH catalytic class
- transpososome/synaptic complex
- **TnpR/resolvase** — family-scoped for cointegrate resolution
- H-NS, histone-like nucleoid-structuring protein
- TnsA, TnsB, TnsC, TnsD/TniQ and Cascade/Cas effector—only for Tn7/CAST branches
- IS-excision enhancer (IEE)—IS629-specific modifier

Recommended ontology-grounding candidates, subject to release-level verification, are **GO:0004803, transposase activity**, **GO:0006313, transposition, DNA-mediated**, and **GO:0003677, DNA binding**. Do not assign a generic transposase UniProt accession because transposases are element- and taxon-specific.

### C. Molecular intermediates and chemicals

- donor DNA and target DNA
- cleaved transposon-end 3′-OH
- strand-transfer/Shapiro intermediate
- excised circular or figure-eight intermediate
- cointegrate
- repaired insertion junction
- magnesium ion, candidate **CHEBI:18420**, for Mg²⁺-dependent DDE catalysis

### D. Processes and outcomes

- transposon-end recognition
- DNA cleavage/excision
- target capture and DNA strand transfer
- DNA integration
- DNA repair and target-site duplication
- site-specific recombination/cointegrate resolution
- insertional gene inactivation
- activation of a neighboring gene
- deletion, inversion, duplication, or other rearrangement
- antimicrobial-resistance-gene mobilization
- genome plasticity and phenotypic diversification

### E. Cellular and genomic locations

- bacterial chromosome/nucleoid
- plasmid
- prophage or pathogenicity island
- horizontally acquired, AT-rich DNA
- intergenic/noncoding region

Chromosome, plasmid, and prophage are legitimate contexts rather than obligatory parts of one mechanism. ISs have been detected in both chromosome and plasmid contexts, and H-NS-directed insertions can enrich in horizontally acquired regions. (cooper2024hnsisa pages 2-3, siguier2014bacterialinsertionsequences pages 12-13)

### F. Environmental and experimental factors

No universal environmental trigger should be placed in the core graph. Stress, antibiotics, host infection, and DNA damage can alter selection for particular insertions, but the evidence assembled here does not justify a generic edge such as “antibiotic exposure activates transposition.” Experimental nodes—transposon delivery vector, transposase induction, selective medium, sequencing, and Tn-seq library—belong in an assay branch, not the native trait mechanism.

## 4. Candidate evidence-backed causal edges

The table below separates broadly curatable edges from family-, taxon-, and assay-specific branches.

| subject | predicate | object | evidence tier | DOI | short supporting snippet | curation note/uncertainty |
|---|---|---|---|---|---|---|
| insertion sequence / transposon | encodes | transposase | strong | 10.1111/1574-6976.12067 | “Insertion sequences (ISs), arguably the smallest and most numerous autonomous transposable elements (TEs)” and are classified by “their transposases (Tpases)” (siguier2014bacterialinsertionsequences pages 1-2, siguier2014bacterialinsertionsequences pages 12-13) | Core trait-defining edge; applies broadly to autonomous ISs. Nonautonomous elements are exceptions. |
| transposon terminal inverted repeats / ends | recruit / are recognized by | transposase | strong | 10.1021/acs.chemrev.6b00003 | transposases “recognize specific sequences at transposon ends called Left End (LE) and Right End (RE), with sequences known as Terminal Inverted Repeats (TIRs)” (hickman2016dnatranspositionat pages 3-5) | Good mechanistic node for element architecture; label-only grounding unless a specific repeat ontology term is later verified. |
| transposase | cleaves | transposon ends | strong | 10.1021/acs.chemrev.6b00003 | “Cut-and-paste transposition involves introducing double-strand breaks at transposon ends” by transposase (hickman2016dnatranspositionat pages 2-3) | General for cut-and-paste systems; some families use distinct chemistry (e.g., HUH systems). |
| 3'-OH transposon ends | attacks | target DNA | strong | 10.1128/9781555819217.ch32 | “releasing 3´ OH groups that attack target DNA strands” (nicolas2015thetn3familyof pages 13-15) | Mechanistically specific, well supported for Tn3-family replicative transposons. |
| staggered integration + DNA repair | produces | target-site duplication | strong | 10.1128/9781555819217.ch32 | “Target DNA phosphates are staggered by five base pairs… repaired by DNA synthesis, generating 5-bp direct target-site duplications” (nicolas2015thetn3familyof pages 13-15) | Strong but family-specific in exact duplication length; curate generic TSD edge, not fixed bp length unless family-scoped. |
| replicative transposition | forms | cointegrate | strong | 10.1128/9781555819217.ch32 | transposition generates “the final cointegrate structure” with flanking duplicated element copies (nicolas2015thetn3familyof pages 13-15) | Strong for Tn3-family and similar replicative systems; not universal to all TEs. |
| resolvase (TnpR) | resolves | cointegrate | moderate | 10.1021/acs.chemrev.6b00003 | Tn3 “encodes a resolvase” and carries β-lactamase resistance (hickman2016dnatranspositionat pages 3-5) | Resolution step is biologically expected for Tn3-family, but exact quoted wording for “resolves cointegrate” was not retrieved here; curate as family-scoped or await direct primary quote. |
| transposon insertion | disrupts / inactivates | host gene | moderate | 10.1038/s41467-024-51407-5 | without H-NS, “transcribed and essential genes are disrupted” (cooper2024hnsisa pages 2-3) | Strong recent evidence for disruptive insertions, but wording is in H-NS context; acceptable as general insertional mutagenesis edge with note. |
| insertion sequences | activate | neighbouring genes | strong | 10.1111/1574-6976.12067 | review highlights “their role in activating neighbouring genes, a phenomenon of particular importance in the recent upsurge of bacterial antibiotic resistance” (siguier2014bacterialinsertionsequences pages 1-2) | Strong for regulatory activation; specific “outward promoter” mechanism is implied by IS biology but not directly quoted in retrieved evidence, so keep object generic unless more direct text is gathered. |
| repeated IS copies | promote | genome rearrangement / deletions / inversions / duplications | moderate | 10.1038/ncomms1152 | IEE-mediated IS excision “induces various genomic deletions including deletions, inversions, and duplications” (kusumoto2011insertionsequenceexcisionenhancer pages 1-2) | Supports rearrangement consequence, but mechanism is IS629/IEE-specific; repeated-copy recombination per se not directly quoted in retrieved evidence. Mark uncertain/generalized. |
| transposons / composite transposons | carry | antibiotic-resistance passenger genes | strong | 10.1021/acs.chemrev.6b00003 | Tn5 carries “kanamycin, bleomycin, and streptomycin resistance”; Tn10 carries tetracycline resistance; Tn3 carries β-lactamase (hickman2016dnatranspositionat pages 3-5, hickman2016dnatranspositionat pages 5-6) | Strong for many named bacterial transposons; useful branch linking TE possession to AMR dissemination. |
| H-NS DNA bridging | directs | transposon insertions to hotspots | strong | 10.1038/s41467-024-51407-5 | “H-NS bound chromosomal regions are transposition ‘hotspots’” and capture is “mediated by the DNA bridging activity of H-NS” (cooper2024hnsisa pages 2-3, cooper2024hnsisa pages 8-8, cooper2024hnsisa pages 1-2) | Recent, high-value host-factor edge; likely taxonomically variable. |
| H-NS-directed transposition | protects | essential / housekeeping genes from disruption | strong | 10.1038/s41467-024-51407-5 | “if absent, more ubiquitous transposition results. Consequently, transcribed and essential genes are disrupted” and H-NS “protects essential and housekeeping genes” (cooper2024hnsisa pages 2-3) | Strong but derived from A. baumannii / E. coli experiments; annotate host-factor specificity. |
| engineered Tn-seq transposon insertion | disrupts | nonessential genes to create mutant libraries | strong | 10.3390/ijms252011298 | Tn-Seq creates “mutants with single transposon insertions” and identifies genes that “cannot tolerate insertions”; engineered transposons are modified to prevent further mobility (fernandezgarcia2024essentialgenesdiscovery pages 2-4, fernandezgarcia2024essentialgenesdiscovery pages 1-2, fernandezgarcia2024essentialgenesdiscovery pages 4-5) | Assay-only edge; useful for distinguishing experimental readout from natural trait mechanism. Do not curate as native trait biology. |
| guide RNA / Cascade (CAST) | recruits | CRISPR-associated transposition machinery | strong | 10.1021/acs.biochem.2c00379 | “TniQ partners with Cascade” and subtype I-F “replaces TnsD/TnsE with the CRISPR-Cas effector” (tenjocastano2022transposonsandcrispr pages 6-7, tenjocastano2022transposonsandcrispr pages 4-6) | Derived/application system from microbial TEs; not a core natural node for generic TE possession trait. |
| TnsA/TnsB (CAST/Tn7-like) | integrates | cargo DNA at target site | strong | 10.1016/j.cobme.2023.100491 | Tn7-like systems use “TnsA and TnsB transposases for 5' and 3' end cleavage” and INTEGRATE “inserts cargo 47-51 bp downstream, forming 5 bp target-site duplications” (wang2023longsequenceinsertion pages 3-4) | Application/derived system; valuable for recent developments section, but separate from baseline trait graph unless adding applied-technology branch. |


*Table: This table summarizes the strongest curation-ready causal edges for microbial transposable elements, prioritizing direct mechanistic evidence and noting where claims are family-specific, host-factor-specific, assay-only, or derived from CRISPR-associated applications.*

### Recommended minimal graph

For a conservative replacement or refinement of the existing 8-node/7-edge graph, prioritize:

1. **transposable element — encodes → transposase**
2. **transposon ends/TIRs — are recognized by → transposase**
3. **transposase — catalyzes → transposon-end cleavage**
4. **cleaved 3′-OH transposon ends — attack → target DNA**
5. **strand transfer — produces → integrated TE junction**
6. **junction-gap repair — produces → target-site duplication** *(conditional, not universal)*
7. **TE insertion — causes → gene disruption or altered neighboring-gene expression**
8. **TE-mediated mutation/rearrangement — increases → genome plasticity**

A separate **replicative branch** should contain cointegrate formation and resolvase-mediated resolution. A separate **host-targeting branch** should contain H-NS. This avoids falsely asserting that every microbial TE uses Tn3-like replication or H-NS targeting.

## 5. Recent developments, expert analysis, and quantitative evidence

### 5.1 H-NS as a transposon-capture factor (2024)

Cooper and colleagues reframed H-NS from only a silencer of horizontally acquired DNA to a physical transposon-targeting factor. In *Acinetobacter baumannii*, H-NS binding and ISAba13 hotspots correlated at **r = 0.72**; deleting H-NS reduced this to **r = 0.16** and redistributed, rather than reduced, total transposition. Thus, the supported causal claim is that H-NS controls **where** insertions occur, not their total frequency. (cooper2024hnsisa pages 2-3)

The same work found that noncoding regions comprised **25% of insertions despite only 13% of the DNA**. In *E. coli*, **19/32** IS903 insertions occurred in H-NS-bound regions at eight hotspots; without H-NS, hotspots disappeared and only **11/33** insertions remained in such regions. DNA bridging was implicated in capture. The authors caution that the mechanism need not apply to every IS family. (cooper2024hnsisa pages 8-8, cooper2024hnsisa pages 1-2)

These insertions generated altered capsule, competence, serum sensitivity, motility, biofilm formation, and host-interaction phenotypes. This is strong evidence for a host-factor-specific path from insertion targeting to clinically relevant phenotypic heterogeneity, but it remains taxon- and element-specific rather than a universal core edge. (cooper2024hnsisa pages 2-3, cooper2024hnsisa pages 8-9)

### 5.2 CRISPR-associated transposases and programmable integration (2023)

CAST systems connect RNA-guided target recognition to transposase-catalyzed insertion. Cascade/Cas12k and TniQ recruit Tns machinery, while TnsA cleaves one strand/end and DDE transposase TnsB binds terminal repeats and performs integration. (tenjocastano2022transposonsandcrispr pages 6-7, tenjocastano2022transposonsandcrispr pages 4-6)

Reported microbial-system performance includes ShCAST insertion of cargo up to **10 kb**, approximately **60–66 bp** downstream of the protospacer, at about **60% efficiency**, albeit with off-target insertions enriched near highly expressed genes. INTEGRATE inserted cargo **47–51 bp** downstream, generated **5-bp target-site duplications**, tolerated cargo up to **10 kb**, and showed less than **5% off-target integration** in the summarized studies; improved variants approached **99% efficiency** under specified bacterial configurations. These figures are platform-specific, not intrinsic properties of natural TEs. (wang2023longsequenceinsertion pages 3-4)

The expert significance is that CAST can make kilobase-scale integrations without relying on homologous recombination or repair of nuclease-generated double-strand breaks. However, 2023 reviews emphasized that testing remained principally bacterial and that transposition immunity, orientation, cargo delivery, and off-target integration remain constraints. (tenjocastano2022transposonsandcrispr pages 6-7)

### 5.3 Transposon insertion sequencing in functional genomics (2024)

Tn-seq combines saturated transposon mutagenesis with next-generation sequencing. Genes unable to tolerate insertions are inferred to be essential; differential depletion between environments identifies conditionally essential loci. A 2024 review reported analysis across **14 eubacteria yielding 133 conserved essential genes**, with conditionally essential genes studied in **18 bacterial species**. (fernandezgarcia2024essentialgenesdiscovery pages 18-19, fernandezgarcia2024essentialgenesdiscovery pages 1-2)

Reported organism-level essential-gene counts included **465** in *Ralstonia solanacearum*, **247** in *Streptococcus pneumoniae*, **264** in *S. pyogenes*, **317** in *S. agalactiae*, and **1,258** in *Schizosaccharomyces pombe*. Other applications identified **140** aminoglycoside-resistance genes in *E. coli*, **200** genes associated with invasive *Staphylococcus aureus* infection, and **336** iron-dependent genes in *Salmonella Typhimurium*. (fernandezgarcia2024essentialgenesdiscovery pages 5-7, fernandezgarcia2024essentialgenesdiscovery pages 11-12)

This is a major real-world use of transposition in antimicrobial-target discovery, pathogenesis, microbial agriculture, and industrial strain optimization. It is nonetheless an **engineered mutagenesis application**, not evidence that every assayed organism naturally has the target trait. The 2024 InducTn-seq preprint reported millions of mutants from one colony and demonstrated in-host induction to bypass infection bottlenecks, but it should remain provisional until peer review. (basta2024inducibletransposonmutagenesis pages 1-3)

## 6. Biological and clinical applications

1. **Antimicrobial-resistance surveillance.** Composite transposons can carry resistance genes: Tn5 carries kanamycin, bleomycin, and streptomycin resistance; Tn10 carries tetracycline resistance; Tn3 carries β-lactamase. This supports “TE carries resistance cargo,” followed by a separate transfer/selection path—not the claim that TE possession alone causes phenotypic resistance. (hickman2016dnatranspositionat pages 3-5)
2. **Insertion-site epidemiology.** ISMapper identified bacterial insertion sites with **97% accuracy in simulated reads and 98% in real Illumina reads**; confident calls generally required more than 50× depth. It also found an ISAba1 insertion upstream of *ampC* in each tested *A. baumannii* genome, consistent with third-generation cephalosporin resistance. (hawkey2015ismapperidentifyingtransposase pages 1-2)
3. **Genome-wide target discovery.** Tn-seq and RB-Tn-seq identify essential genes, condition-specific fitness determinants, virulence factors, stress responses, and industrially relevant pathways. (fernandezgarcia2024essentialgenesdiscovery pages 18-19, fernandezgarcia2024essentialgenesdiscovery pages 11-12)
4. **Programmable genome engineering.** CAST/INTEGRATE systems repurpose microbial TEs for RNA-guided, kilobase-scale DNA insertion. (wang2023longsequenceinsertion pages 3-4, tenjocastano2022transposonsandcrispr pages 4-6)
5. **Genome reduction and stabilization.** IS excision has been explored to remove unstable elements, although the IS-excision enhancer can also induce deletions, inversions, and duplications and is therefore not a universally safe stabilization mechanism. (kusumoto2011insertionsequenceexcisionenhancer pages 1-2)

## 7. Curation warnings

- **Do not make target-site duplication mandatory.** TSD production and length depend on the family; IS200/IS605-like peel-and-paste systems can lack TSDs. (nicolas2015thetn3familyof pages 13-15, tenjocastano2022transposonsandcrispr pages 2-3)
- **Do not merge all mechanisms.** Cut-and-paste, replicative, copy-out–paste-in, serine/tyrosine recombinase-like, and HUH pathways need qualified branches. (hickman2016dnatranspositionat pages 5-6, hickman2016dnatranspositionat pages 6-7)
- **Do not curate “resolvase resolves cointegrate” generically** from the present evidence. It is appropriate for a Tn3-family branch, but a direct retrieved quotation for the resolution step was not obtained.
- **Do not curate “outward promoter activates adjacent gene” yet.** Neighboring-gene activation is strongly supported, but the retrieved snippet did not directly establish an outward-promoter mechanism for a particular element. (siguier2014bacterialinsertionsequences pages 1-2)
- **Do not generalize H-NS targeting.** The 2024 result is strong for ISAba13/*A. baumannii* and IS903/*E. coli*, but the authors explicitly leave room for element-family variation. (cooper2024hnsisa pages 2-3, cooper2024hnsisa pages 8-8)
- **Do not infer active mobility from sequence possession.** Frameshifted, truncated, silenced, or domesticated elements may retain recognizable sequence without current transposition competence.
- **Do not equate TE cargo with expressed phenotype.** Resistance requires an intact, expressed determinant in an appropriate host and context.
- **Do not place Tn-seq discoveries in the native causal graph.** Tn-seq is an experimental implementation using engineered insertions. (fernandezgarcia2024essentialgenesdiscovery pages 2-4)
- **Treat rearrangement edges cautiously.** IEE-dependent IS629 excision produced deletions, inversions, and duplications, but that modifier and mechanism are not universal. (kusumoto2011insertionsequenceexcisionenhancer pages 1-2)
- **Assembly warning:** repetitive IS copies are difficult to resolve with short reads. Long-read confirmation or junction-spanning evidence is preferable for trait calls and copy-number estimates.

## 8. DOI-first bibliography

1. **Cooper C, et al.** “H-NS is a bacterial transposon capture protein.” *Nature Communications*. Published February 2024. DOI: [10.1038/s41467-024-51407-5](https://doi.org/10.1038/s41467-024-51407-5). (cooper2024hnsisa pages 2-3)
2. **Fernández-García G, et al.** “Essential Genes Discovery in Microorganisms by Transposon-Directed Sequencing (Tn-Seq).” *International Journal of Molecular Sciences*. Published October 2024. DOI: [10.3390/ijms252011298](https://doi.org/10.3390/ijms252011298). (fernandezgarcia2024essentialgenesdiscovery pages 1-2)
3. **Tenjo-Castaño F, Montoya G, Carabias A.** “Transposons and CRISPR: Rewiring Gene Editing.” *Biochemistry*. Published September 2023. DOI: [10.1021/acs.biochem.2c00379](https://doi.org/10.1021/acs.biochem.2c00379). (tenjocastano2022transposonsandcrispr pages 6-7)
4. **Wang X, et al.** “Long sequence insertion via CRISPR/Cas gene-editing with transposase, recombinase, and integrase.” *Current Opinion in Biomedical Engineering*. Published December 2023. DOI: [10.1016/j.cobme.2023.100491](https://doi.org/10.1016/j.cobme.2023.100491). (wang2023longsequenceinsertion pages 3-4)
5. **Siguier P, Gourbeyre E, Chandler M.** “Bacterial insertion sequences: their genomic impact and diversity.” *FEMS Microbiology Reviews*. Published September 2014. DOI: [10.1111/1574-6976.12067](https://doi.org/10.1111/1574-6976.12067). (siguier2014bacterialinsertionsequences pages 1-2)
6. **Hickman AB, Dyda F.** “DNA Transposition at Work.” *Chemical Reviews*. Published 2016. DOI: [10.1021/acs.chemrev.6b00003](https://doi.org/10.1021/acs.chemrev.6b00003). (hickman2016dnatranspositionat pages 3-5)
7. **Nicolas E, et al.** “The Tn3-family of Replicative Transposons.” *Mobile DNA III*. Published May 2015. DOI: [10.1128/9781555819217.ch32](https://doi.org/10.1128/9781555819217.ch32). (nicolas2015thetn3familyof pages 13-15)
8. **Hawkey J, et al.** “ISMapper: identifying transposase insertion sites in bacterial genomes from short read sequence data.” *BMC Genomics*. Published September 2015. DOI: [10.1186/s12864-015-1860-2](https://doi.org/10.1186/s12864-015-1860-2). (hawkey2015ismapperidentifyingtransposase pages 1-2)
9. **Kusumoto M, et al.** “Insertion sequence-excision enhancer removes transposable elements from bacterial genomes and induces various genomic deletions.” *Nature Communications*. Published January 2011. DOI: [10.1038/ncomms1152](https://doi.org/10.1038/ncomms1152). (kusumoto2011insertionsequenceexcisionenhancer pages 1-2)
10. **Basta DW, et al.** “Inducible transposon mutagenesis for genome-scale forward genetics.” *bioRxiv* preprint. Posted May 2024. DOI: [10.1101/2024.05.21.595064](https://doi.org/10.1101/2024.05.21.595064). (basta2024inducibletransposonmutagenesis pages 1-3)

**Curation recommendation:** retain a compact, mechanism-neutral core centered on element possession, transposase/end recognition, integration, and genomic consequences. Represent replicative transposition, HUH chemistry, H-NS targeting, antimicrobial-resistance cargo, Tn-seq, and CAST as explicitly qualified branches rather than universal properties.

References

1. (hickman2016dnatranspositionat pages 2-3): Alison B. Hickman and Fred Dyda. Dna transposition at work. Chemical reviews, 116 20:12758-12784, May 2016. URL: https://doi.org/10.1021/acs.chemrev.6b00003, doi:10.1021/acs.chemrev.6b00003. This article has 179 citations and is from a highest quality peer-reviewed journal.

2. (siguier2014bacterialinsertionsequences pages 12-13): Patricia Siguier, Edith Gourbeyre, and Mick Chandler. Bacterial insertion sequences: their genomic impact and diversity. FEMS Microbiology Reviews, 38:865-891, Sep 2014. URL: https://doi.org/10.1111/1574-6976.12067, doi:10.1111/1574-6976.12067. This article has 885 citations and is from a domain leading peer-reviewed journal.

3. (fernandezgarcia2024essentialgenesdiscovery pages 2-4): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

4. (fernandezgarcia2024essentialgenesdiscovery pages 1-2): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

5. (hickman2016dnatranspositionat pages 5-6): Alison B. Hickman and Fred Dyda. Dna transposition at work. Chemical reviews, 116 20:12758-12784, May 2016. URL: https://doi.org/10.1021/acs.chemrev.6b00003, doi:10.1021/acs.chemrev.6b00003. This article has 179 citations and is from a highest quality peer-reviewed journal.

6. (tenjocastano2022transposonsandcrispr pages 2-3): Francisco Tenjo-Castaño, Guillermo Montoya, and Arturo Carabias. Transposons and crispr: rewiring gene editing. Biochemistry, 62:3521-3532, Sep 2023. URL: https://doi.org/10.1021/acs.biochem.2c00379, doi:10.1021/acs.biochem.2c00379. This article has 25 citations and is from a peer-reviewed journal.

7. (hickman2016dnatranspositionat pages 3-5): Alison B. Hickman and Fred Dyda. Dna transposition at work. Chemical reviews, 116 20:12758-12784, May 2016. URL: https://doi.org/10.1021/acs.chemrev.6b00003, doi:10.1021/acs.chemrev.6b00003. This article has 179 citations and is from a highest quality peer-reviewed journal.

8. (nicolas2015thetn3familyof pages 13-15): Emilien Nicolas, Michael Lambin, Damien Dandoy, Christine Galloy, Nathan Nguyen, Cédric A. Oger, and Bernard Hallet. The tn<i>3</i>-family of replicative transposons. Mobile DNA III, pages 693-726, May 2015. URL: https://doi.org/10.1128/9781555819217.ch32, doi:10.1128/9781555819217.ch32. This article has 196 citations.

9. (cooper2024hnsisa pages 2-3): Charles Cooper, Simon Legood, Rachel L Wheat, David Forrest, Prateek Sharma, James RJ Haycocks, and David C Grainger. H-ns is a bacterial transposon capture protein. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-51407-5, doi:10.1038/s41467-024-51407-5. This article has 30 citations and is from a highest quality peer-reviewed journal.

10. (siguier2014bacterialinsertionsequences pages 1-2): Patricia Siguier, Edith Gourbeyre, and Mick Chandler. Bacterial insertion sequences: their genomic impact and diversity. FEMS Microbiology Reviews, 38:865-891, Sep 2014. URL: https://doi.org/10.1111/1574-6976.12067, doi:10.1111/1574-6976.12067. This article has 885 citations and is from a domain leading peer-reviewed journal.

11. (kusumoto2011insertionsequenceexcisionenhancer pages 1-2): Masahiro Kusumoto, Tadasuke Ooka, Yoshiaki Nishiya, Yoshitoshi Ogura, Takashi Saito, Yasuhiko Sekine, Taketoshi Iwata, Masato Akiba, and Tetsuya Hayashi. Insertion sequence-excision enhancer removes transposable elements from bacterial genomes and induces various genomic deletions. Nature communications, 2:152, Jan 2011. URL: https://doi.org/10.1038/ncomms1152, doi:10.1038/ncomms1152. This article has 62 citations and is from a highest quality peer-reviewed journal.

12. (cooper2024hnsisa pages 8-8): Charles Cooper, Simon Legood, Rachel L Wheat, David Forrest, Prateek Sharma, James RJ Haycocks, and David C Grainger. H-ns is a bacterial transposon capture protein. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-51407-5, doi:10.1038/s41467-024-51407-5. This article has 30 citations and is from a highest quality peer-reviewed journal.

13. (cooper2024hnsisa pages 1-2): Charles Cooper, Simon Legood, Rachel L Wheat, David Forrest, Prateek Sharma, James RJ Haycocks, and David C Grainger. H-ns is a bacterial transposon capture protein. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-51407-5, doi:10.1038/s41467-024-51407-5. This article has 30 citations and is from a highest quality peer-reviewed journal.

14. (fernandezgarcia2024essentialgenesdiscovery pages 4-5): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

15. (tenjocastano2022transposonsandcrispr pages 6-7): Francisco Tenjo-Castaño, Guillermo Montoya, and Arturo Carabias. Transposons and crispr: rewiring gene editing. Biochemistry, 62:3521-3532, Sep 2023. URL: https://doi.org/10.1021/acs.biochem.2c00379, doi:10.1021/acs.biochem.2c00379. This article has 25 citations and is from a peer-reviewed journal.

16. (tenjocastano2022transposonsandcrispr pages 4-6): Francisco Tenjo-Castaño, Guillermo Montoya, and Arturo Carabias. Transposons and crispr: rewiring gene editing. Biochemistry, 62:3521-3532, Sep 2023. URL: https://doi.org/10.1021/acs.biochem.2c00379, doi:10.1021/acs.biochem.2c00379. This article has 25 citations and is from a peer-reviewed journal.

17. (wang2023longsequenceinsertion pages 3-4): Xiaotong Wang, Guangxue Xu, William A. Johnson, Yuanhao Qu, Di Yin, Nurupa Ramkissoon, Hong Xiang, and Le Cong. Long sequence insertion via crispr/cas gene-editing with transposase, recombinase, and integrase. Current Opinion in Biomedical Engineering, 28:100491, Dec 2023. URL: https://doi.org/10.1016/j.cobme.2023.100491, doi:10.1016/j.cobme.2023.100491. This article has 25 citations and is from a peer-reviewed journal.

18. (cooper2024hnsisa pages 8-9): Charles Cooper, Simon Legood, Rachel L Wheat, David Forrest, Prateek Sharma, James RJ Haycocks, and David C Grainger. H-ns is a bacterial transposon capture protein. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-51407-5, doi:10.1038/s41467-024-51407-5. This article has 30 citations and is from a highest quality peer-reviewed journal.

19. (fernandezgarcia2024essentialgenesdiscovery pages 18-19): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

20. (fernandezgarcia2024essentialgenesdiscovery pages 5-7): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

21. (fernandezgarcia2024essentialgenesdiscovery pages 11-12): Gemma Fernández-García, Paula Valdés-Chiara, Patricia Villazán-Gamonal, Sergio Alonso-Fernández, and Angel Manteca. Essential genes discovery in microorganisms by transposon-directed sequencing (tn-seq): experimental approaches, major goals, and future perspectives. International Journal of Molecular Sciences, 25:11298, Oct 2024. URL: https://doi.org/10.3390/ijms252011298, doi:10.3390/ijms252011298. This article has 16 citations.

22. (basta2024inducibletransposonmutagenesis pages 1-3): David W. Basta, Ian W. Campbell, Emily J. Sullivan, Julia A. Hotinger, Karthik Hullahalli, and Matthew K. Waldor. Inducible transposon mutagenesis for genome-scale forward genetics. bioRxiv, May 2024. URL: https://doi.org/10.1101/2024.05.21.595064, doi:10.1101/2024.05.21.595064. This article has 1 citations.

23. (hawkey2015ismapperidentifyingtransposase pages 1-2): Jane Hawkey, Mohammad Hamidian, Ryan R. Wick, David J. Edwards, Helen Billman-Jacobe, Ruth M. Hall, and Kathryn E. Holt. Ismapper: identifying transposase insertion sites in bacterial genomes from short read sequence data. BMC Genomics, Sep 2015. URL: https://doi.org/10.1186/s12864-015-1860-2, doi:10.1186/s12864-015-1860-2. This article has 171 citations and is from a peer-reviewed journal.

24. (hickman2016dnatranspositionat pages 6-7): Alison B. Hickman and Fred Dyda. Dna transposition at work. Chemical reviews, 116 20:12758-12784, May 2016. URL: https://doi.org/10.1021/acs.chemrev.6b00003, doi:10.1021/acs.chemrev.6b00003. This article has 179 citations and is from a highest quality peer-reviewed journal.