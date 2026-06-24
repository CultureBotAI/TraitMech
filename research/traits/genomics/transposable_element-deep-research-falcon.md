---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:47:47.006459'
end_time: '2026-06-18T04:08:11.369775'
duration_seconds: 1224.36
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
  causal_graph_summary: 'te_transposition_rearrangement: 3 nodes, 2 edges'
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
- **Trait label:** transposable element
- **METPO identifier:** traitmech:000092
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of transposable elements — such as insertion sequences and transposons — that move within the genome and drive genome rearrangement, gene inactivation, and plasticity.
- **Parent traits:** traitmech:000089
- **Synonyms:** insertion sequence, transposon
- **Existing evidence:** DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review bacterial insertion sequences and their genomic impact and diversity.) | DOI:10.1038/nrmicro1235:  (Frost et al. include transposons among the mobile genetic elements driving genome evolution.)
- **Existing causal graph summary:** te_transposition_rearrangement: 3 nodes, 2 edges

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
- **METPO identifier:** traitmech:000092
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of transposable elements — such as insertion sequences and transposons — that move within the genome and drive genome rearrangement, gene inactivation, and plasticity.
- **Parent traits:** traitmech:000089
- **Synonyms:** insertion sequence, transposon
- **Existing evidence:** DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review bacterial insertion sequences and their genomic impact and diversity.) | DOI:10.1038/nrmicro1235:  (Frost et al. include transposons among the mobile genetic elements driving genome evolution.)
- **Existing causal graph summary:** te_transposition_rearrangement: 3 nodes, 2 edges

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


## Microbial Trait Causal Graph Curation Report: **Transposable element** (METPO: traitmech:000092)

### Scope summary (TraitMech meaning and boundaries)
The TraitMech trait **transposable element** (TE) captures a *genomic capacity*—possession of insertion sequences (IS) and transposons (including composite and Tn7-like elements) capable of moving within microbial genomes via element-encoded mobility functions (typically a transposase), thereby causing gene disruption and genome rearrangements and enabling acquisition/spread of accessory genes such as antimicrobial resistance (AMR) and virulence factors. Mechanistically, IS are compact mobile genetic elements flanked by inverted repeats and typically generate target site duplications upon insertion, so the trait is expressed as **transposase-mediated transposition** with downstream consequences (gene inactivation, deletions/inversions, cointegrates, etc.). (sheng2023insertionsequencetransposition pages 1-2, harmer2024is26and pages 6-8)

**Boundary cases / nearby traits**: 
- **Plasmids and phages** are mobile genetic elements but not “transposable elements” per se; they can *carry* IS/transposons and thereby enable their horizontal dissemination (e.g., phage/antibiotic pressure-associated IS activity in enterococci). (kirsch2023targetediselementsequencing pages 1-2)
- **Integrons** are not transposons; however, they are frequently found in resistance regions together with IS/transposons that mobilize and remodel those regions (curate as separate traits/nodes; connect via co-occurrence/association edges only if evidence is explicit). (harmer2024is26and pages 6-8)
- **Non-autonomous elements** (e.g., MITEs) are TE-derived sequences mobilized in trans by related transposases; they belong in the TE scope only if the organism’s genome includes the required transposase activity. (sheng2023insertionsequencetransposition pages 1-2)
- **CRISPR-associated transposons (CASTs)** are specialized **Tn7-like** elements that use guide RNAs to target transposition and are within scope as TE subtypes. (hsieh2024naturalandengineered pages 1-3)

---

## 1) Key concepts and definitions (current understanding)

### Core mechanistic definitions
- **Insertion sequence (IS)**: a compact transposable element that encodes a transposase and is bounded by terminal inverted repeats; insertion typically creates a target site duplication (TSD). IS movement can disrupt genes and provide repeated sequences that recombine to create rearrangements. (sheng2023insertionsequencetransposition pages 1-2)
- **Transposase (often DDE family)**: a catalytic protein encoded by many IS/transposons that is required for movement (e.g., IS26 encodes a DDE-family transposase Tnp26). (harmer2024is26and pages 6-8)
- **Gene disruption and genome rearrangement**: IS movement can directly disrupt coding sequences, and homologous recombination between identical IS copies can generate rearrangements such as deletions/inversions/duplications. (sheng2023insertionsequencetransposition pages 1-2)

### Mechanistic variants relevant to causal graphs
- **Cointegration / replicon fusion** (IS26 family): IS26 frequently moves by a copy-in (cointegrate) mechanism that fuses replicons and can be resolved by host homologous recombination. (harmer2024is26and pages 6-8)
- **Targeted conservative cointegration and “translocatable units (TU)”** (IS26): a more efficient conservative route moves a single IS26 plus adjacent DNA as a TU and leaves little/no molecular trace, complicating historical inference. (harmer2024is26and pages 8-12)
- **Circular intermediates** (e.g., IS256): some IS form circular intermediates during transposition; these can be measured as a proxy of mobility. (kirsch2023targetediselementsequencing pages 13-15)
- **RNA-guided transposition (CASTs)**: Tn7-like elements co-opt CRISPR guide RNAs to direct insertion, enabling programmable integration; they evolved complementary targeting pathways for a conserved chromosomal site and for mobile plasmids. (hsieh2024naturalandengineered pages 1-3)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### Stress-responsive activation of TE mobility
- **Physiological DNA damage** (DSBs) can trigger IS transposition: induction of double-strand DNA breakage was used as “a physiological host stress” to monitor IS insertions into cas genes; natural transpositions into cas genes were observed, linking stress to TE movement and host-defense inactivation. (Sheng et al., *Nature Communications*, 2023-07-24; DOI:10.1038/s41467-023-39964-7; https://doi.org/10.1038/s41467-023-39964-7) (sheng2023insertionsequencetransposition pages 1-2)
- **Oxidative stress and irradiation** can induce IS movement: in *Deinococcus geothermalis*, IS elements were “actively transposed using oxidative stress conditions, including gamma irradiation and hydrogen peroxide treatment,” with H2O2 concentrations of 80–100 mM used experimentally. (Park et al., *Microorganisms*, 2024-02-01; DOI:10.3390/microorganisms12020328; https://doi.org/10.3390/microorganisms12020328) (park2024thetranspositionof pages 1-2)
- **Selective pressures in vivo** can drive genome-scale IS diversification: chronic lytic phage infection and antibiotic exposure were shown to drive rapid IS256 transposition/diversification in enterococci; IS256 is described as transcriptionally regulated and tightly controlled absent selective pressure. (Kirsch et al., *PLOS Pathogens*, 2023-06-15; DOI:10.1371/journal.ppat.1011424; https://doi.org/10.1371/journal.ppat.1011424) (kirsch2023targetediselementsequencing pages 1-2)

### Regulatory mechanisms controlling mobility
- **Transcriptional/antisense RNA control of IS256**: IS256 mobility is regulated at the transcriptional level, including antisense RNAs; loss of a site-1 asRNA “dramatically reduces IS256 circular intermediates,” supporting an asRNA-mediated repression mechanism. (Kirsch et al., 2023-06-15; DOI:10.1371/journal.ppat.1011424) (kirsch2023targetediselementsequencing pages 13-15)
- **Stress-dependent transposase expression** in phytopathogens: transcriptome analyses under stress conditions showed differences in expression of genes encoding transposases across several plant-pathogenic bacteria, suggesting environment-responsive regulation (while not itself proving transposition). (Fernandes et al., *Microbial Genomics*, 2024-04-01; DOI:10.1099/mgen.0.001219; https://doi.org/10.1099/mgen.0.001219) (fernandes2024investigatingtheimpact pages 1-2)

### Mechanistic deepening for AMR region remodeling (IS26 family)
A 2024 authoritative review emphasizes IS26 as a “versatile resistance gene mover and genome reorganizer,” detailing two cointegration routes (copy-in and targeted conservative), intramolecular deletion/inversion outcomes, and the TU concept as a key unit of mobility in pseudo-compound transposon architectures. (Harmer & Hall, *Microbiology and Molecular Biology Reviews*, 2024-06-12; DOI:10.1128/mmbr.00119-22; https://doi.org/10.1128/mmbr.00119-22) (harmer2024is26and pages 6-8, harmer2024is26and pages 8-12)

### Rapidly evolving programmable TE systems (CASTs)
CASTs are highlighted in 2024 reviews and primary studies as naturally occurring RNA-guided transposons derived from Tn7-like elements, with complementary targeting pathways for chromosomal reservoirs vs plasmid dissemination. (Hsieh & Peters, *Annual Review of Biochemistry*, 2024-08; DOI:10.1146/annurev-biochem-030122-041908; https://doi.org/10.1146/annurev-biochem-030122-041908) (hsieh2024naturalandengineered pages 1-3)

A 2024 *Nature Communications* study adds that CASTs can utilize crRNAs from co-occurring host defense CRISPR arrays “nearly as efficiently as their own spacers,” which is important when reasoning about CAST horizontal spread and portability. (Hu et al., 2024-08-01; DOI:10.1038/s41467-024-50816-w; https://doi.org/10.1038/s41467-024-50816-w) (hu2024distincthorizontaltransfer pages 1-2)

---

## 3) Current applications and real-world implementations

### Applications as experimental tools (transposon mutagenesis and functional genomics)
The trait “transposable element” underlies widespread experimental implementations including transposon insertion sequencing approaches (e.g., IS-Seq/Tn-Seq style workflows), and recent work demonstrates targeted IS-element deep sequencing to measure within-host TE diversification under selective pressure (enterococci). (Kirsch et al., 2023-06-15; DOI:10.1371/journal.ppat.1011424) (kirsch2023targetediselementsequencing pages 1-2)

### Real-world clinical and environmental relevance: AMR and virulence mobilization
- IS/transposons can carry virulence and antibiotic resistance determinants (e.g., type III secretion effectors; streptomycin resistance genes) in plant-pathogenic bacteria. (Fernandes et al., 2024-04-01; DOI:10.1099/mgen.0.001219) (fernandes2024investigatingtheimpact pages 1-2)
- IS26 family elements restructure resistance regions by mobilizing adjacent DNA segments and forming complex multi-ARG assemblies; IS26 terminal repeats can also enhance expression of adjacent antibiotic resistance genes when promoter motifs are appropriately formed. (Harmer & Hall, 2024-06-12; DOI:10.1128/mmbr.00119-22) (harmer2024is26and pages 6-8, harmer2024is26and pages 8-12)

### Programmable gene integration (emerging implementation path)
CAST systems are emphasized as promising programmable integration tools because they combine transposon-derived integration machinery with guide RNA target selection, enabling targeted insertion without the canonical CRISPR double-strand break route. (Hsieh & Peters, 2024-08; DOI:10.1146/annurev-biochem-030122-041908) (hsieh2024naturalandengineered pages 1-3)

---

## 4) Expert opinions and analysis (authoritative synthesis)

### IS26 as a paradigmatic “resistance island” engine
Harmer & Hall (MMBR 2024) synthesize a mechanistic framework in which IS26’s two cointegration pathways (including a highly efficient targeted conservative route) and intramolecular deletion/inversion reactions explain the frequent emergence of complex overlapping resistance structures and rapid remodeling of AMR regions. (harmer2024is26and pages 8-12)

### TE activity as a stress-linked evolutionary “accelerator” with regulation
Kirsch et al. (PLOS Pathogens 2023) provide a within-host evolutionary perspective: IS256 activity is tightly controlled under baseline conditions, but environmental/host stressors (phage predation, antibiotics) can drive genome-scale transposition, supporting a causal-graph framing where **stressors increase TE mobility**, which then increases genetic/phenotypic diversification. (kirsch2023targetediselementsequencing pages 1-2)

### TE–host defense interplay
Sheng et al. (Nat Comm 2023) support a mechanistic and ecological interaction: IS transposition into cas genes can inactivate CRISPR-Cas defenses, potentially increasing susceptibility to foreign DNA invasion, which in turn may facilitate further horizontal gene transfer and TE spread. (sheng2023insertionsequencetransposition pages 1-2)

---

## 5) Relevant recent statistics and data

### Genome-scale abundance/distribution
- Across **270 complete genomes** of major phytopathogenic bacteria, **35,692 ISs and 71 transposons** were identified; this provides a large empirical baseline for TE prevalence in important microbial taxa. (Fernandes et al., 2024-04-01; DOI:10.1099/mgen.0.001219) (fernandes2024investigatingtheimpact pages 1-2)
- In the same survey, species-level burden can be extremely high, e.g., **Xanthomonas oryzae** with **29,046 IS copies** reported in a per-species table, and median per-genome IS counts reaching ~**383** in X. oryzae, illustrating wide variance in TE load. (Fernandes et al., 2024-04-01; DOI:10.1099/mgen.0.001219) (fernandes2024investigatingtheimpact pages 5-6)
- In 36 **Acidithiobacillus** genomes, **248 IS members** across **23 IS families** totaling **10,652 copies** were identified, and the authors note that while many prokaryotic genomes have ≤60 IS, some exceed 300, emphasizing heterogeneity and potential environment-linked expansion. (Huang et al., *BMC Genomics*, 2023-05-08; DOI:10.1186/s12864-023-09372-8; https://doi.org/10.1186/s12864-023-09372-8) (huang2023insertionsequencecontributes pages 1-2)

### Quantified experimental/selection contexts
- In plasmid host adaptation experiments (pB1000 adapting to *E. coli*), evolved populations showed high stability: “>90% of colonies retained the plasmid for at least 100 generations,” and IS insertions (IS1a or IS10R) were repeatedly observed as adaptive mechanisms reducing fitness cost. (Wedel et al., *mBio*, 2023-06-13; DOI:10.1128/mbio.03158-22; https://doi.org/10.1128/mbio.03158-22) (wedel2023insertionsequencesdetermine pages 2-4)
- IS256 activation in enterococci during antibiotic treatment was operationalized with insertion-enrichment thresholds (adjusted p<0.05; fold change >4; ≥100 reads) and associated with increased circular intermediates during therapy, illustrating curatable assay context for “antibiotic exposure increases transposition.” (Kirsch et al., 2023-06-15; DOI:10.1371/journal.ppat.1011424) (kirsch2023targetediselementsequencing pages 13-15)

---

# Candidate causal graph entities (nodes) grouped by type

## A) Trait node
- **METPO**: traitmech:000092 (transposable element; reviewed definition in prompt)

## B) Biological processes / molecular functions (GO candidates)
- **Transposition**: GO:0032196 (transposition) (used as object node in multiple edges) (sheng2023insertionsequencetransposition pages 1-2)
- **DNA recombination / homologous recombination**: GO:0006310 (DNA recombination) (sheng2023insertionsequencetransposition pages 1-2)
- **DNA transposase activity**: GO:0004803 (DNA transposase activity; or label-only “transposase”) (harmer2024is26and pages 6-8)

## C) Genes/proteins/complexes (label nodes; ground when available)
- **Transposase** (generic; e.g., IS26 Tnp26 DDE-family transposase) (harmer2024is26and pages 6-8)
- **IS26** (insertion sequence family member; label node) (harmer2024is26and pages 6-8)
- **IS256** (insertion sequence implicated in enterococcal pathoadaptation; label node) (kirsch2023targetediselementsequencing pages 1-2)
- **Antisense RNA regulators** (IS256 asRNAs; label node) (kirsch2023targetediselementsequencing pages 13-15)
- **CRISPR-Cas “cas genes”** (host defense target; label node) (sheng2023insertionsequencetransposition pages 1-2)
- **CAST / CRISPR-associated transposon** (Tn7-like; label node) (hsieh2024naturalandengineered pages 1-3)

## D) Genomic structures / intermediates (label nodes)
- Terminal inverted repeats (TIR) / target site duplication (TSD) (sheng2023insertionsequencetransposition pages 1-2)
- **Cointegrate** / replicon fusion (IS26 copy-in pathway) (harmer2024is26and pages 6-8)
- **Translocatable unit (TU)** (IS26 targeted conservative pathway) (harmer2024is26and pages 8-12)
- **Circular intermediate** (IS256) (kirsch2023targetediselementsequencing pages 13-15)

## E) Environmental / experimental factors (ENVO/CHEBI where possible)
- **Oxidative stress**; **hydrogen peroxide** CHEBI:16240 (park2024thetranspositionof pages 1-2)
- **Gamma irradiation** (label; ENVO grounding optional depending on ontology availability) (park2024thetranspositionof pages 1-2)
- **Antibiotic exposure/therapy** (label; can connect to specific drugs if known in curated dataset) (kirsch2023targetediselementsequencing pages 1-2)
- **Phage infection/predation** (label node) (kirsch2023targetediselementsequencing pages 1-2)
- **Double-strand DNA break stress** (label node; DNA damage response context) (sheng2023insertionsequencetransposition pages 1-2)

## F) Chemicals / phenotypes / cargos
- **Streptomycin** CHEBI:17076 (as context for resistance genes carried by Tns) (fernandes2024investigatingtheimpact pages 1-2)
- **Virulence genes** (e.g., type III secretion effectors; label node) (fernandes2024investigatingtheimpact pages 1-2)

---

# Candidate causal edges (evidence-backed triples)
The following table is designed for direct curation into `data/traits/genomics/transposable_element.yaml`.

| Edge (triple) | Evidence snippet (short quote) | Reference (DOI + URL + pub date) | Notes/curation guidance | Suggested ontology grounding |
|---|---|---|---|---|
| transposable element — has_participant — transposase | “IS26 is an 820 bp element with 14 bp terminal inverted repeats (TIRs) and a single ORF, tnp26, encoding a 234-aa DDE-family transposase (Tnp26) required for movement” (harmer2024is26and pages 6-8) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong generic mechanistic edge for IS/TEs: the defining effector is a transposase. Can curate as broad TE mechanism; taxon/example comes from IS26. | subject: METPO:traitmech:000092; predicate: has_participant; object: GO:0004803 DNA transposase activity / label: transposase |
| transposase — enables — transposition | “tnp26, encoding a 234-aa DDE-family transposase (Tnp26) required for movement” (harmer2024is26and pages 6-8) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Direct mechanistic support that transposase activity is causal for element movement. | subject: label: Tnp26/transposase; predicate: enables; object: GO:0032196 transposition |
| transposable element insertion — causes — target site duplication | “typically create target site duplications (TSDs) upon insertion” (sheng2023insertionsequencetransposition pages 1-2) | Sheng et al. 2023. DOI:10.1038/s41467-023-39964-7. https://doi.org/10.1038/s41467-023-39964-7. Pub: 2023-07 | Good general IS edge. Applies to many but not all TE pathways; keep as broad with note that some conservative mechanisms may not generate TSD. | subject: label: transposable element insertion; predicate: causes; object: label: target site duplication |
| transposable element insertion — causes — gene disruption | “enabling their movement and causing gene disruption” (sheng2023insertionsequencetransposition pages 1-2) | Sheng et al. 2023. DOI:10.1038/s41467-023-39964-7. https://doi.org/10.1038/s41467-023-39964-7. Pub: 2023-07 | Strong, central phenotype/mechanism edge. Useful for graphing genome plasticity and mutagenesis. | subject: label: transposable element insertion; predicate: causes; object: GO:0010629 negative regulation of gene expression by disruption / label: gene disruption |
| transposable element insertion into cas genes — inactivates — CRISPR-Cas immunity | “identified multiple natural transpositions of insertion sequences (ISs) into cas genes, thus inactivating CRISPR-Cas defenses” (sheng2023insertionsequencetransposition pages 1-2) | Sheng et al. 2023. DOI:10.1038/s41467-023-39964-7. https://doi.org/10.1038/s41467-023-39964-7. Pub: 2023-07 | Strong but target-specific edge; curate as an example of host-defense gene inactivation by IS insertion rather than universal TE effect. | subject: label: IS insertion in cas gene; predicate: inactivates; object: GO:0140355 CRISPR-Cas system / label: CRISPR-Cas immunity |
| double-strand DNA break stress — increases — IS transposition | “monitor IS insertions into cas genes following the induction of double-strand DNA breakage as a physiological host stress” (sheng2023insertionsequencetransposition pages 1-2) | Sheng et al. 2023. DOI:10.1038/s41467-023-39964-7. https://doi.org/10.1038/s41467-023-39964-7. Pub: 2023-07 | Stress-induction edge supported in assay context. Mark as condition-specific rather than universal. | subject: label: double-strand DNA break stress; predicate: increases; object: GO:0032196 transposition |
| homologous recombination between IS copies — causes — genome rearrangement | “homologous recombination between identical IS copies, can produce genome rearrangements” (sheng2023insertionsequencetransposition pages 1-2) | Sheng et al. 2023. DOI:10.1038/s41467-023-39964-7. https://doi.org/10.1038/s41467-023-39964-7. Pub: 2023-07 | Strong generic mechanism for rearrangements; fits parent graph summary. | subject: GO:0006310 DNA recombination / label: homologous recombination between IS copies; predicate: causes; object: label: genome rearrangement |
| IS26 copy-in transposition — causes — cointegrate formation | “IS26 often moves by a copy-in (cointegrate) mechanism that fuses replicons” (harmer2024is26and pages 6-8) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong, IS26-specific. Candidate node for subtype-specific branch, not broad TE branch unless distinguished as example. | subject: label: IS26 copy-in transposition; predicate: causes; object: label: cointegrate |
| homologous recombination — resolves — IS26 cointegrate | “host homologous recombination is needed to resolve cointegrates into simple insertions” (harmer2024is26and pages 6-8) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Useful mechanistic edge linking host process to TE outcomes. Taxon/family-specific to IS26. | subject: GO:0006310 DNA recombination; predicate: resolves; object: label: IS26 cointegrate |
| IS26 intramolecular transposition — causes — adjacent deletion | “intramolecular events causing adjacent deletions or inversions” (harmer2024is26and pages 8-12) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong IS26-specific rearrangement edge. Matches available figure evidence. | subject: label: IS26 intramolecular transposition; predicate: causes; object: label: adjacent deletion |
| IS26 intramolecular transposition — causes — inversion | “intramolecular events causing adjacent deletions or inversions” (harmer2024is26and pages 8-12) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong IS26-specific rearrangement edge. | subject: label: IS26 intramolecular transposition; predicate: causes; object: label: inversion |
| IS26 targeted conservative mechanism — mobilizes — translocatable unit | “The targeted conservative mechanism moves a single IS26 plus an adjacent DNA segment (a translocatable unit, TU)” (harmer2024is26and pages 8-12) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong subtype-specific mechanistic edge; ideal for IS26 subgraph. | subject: label: IS26 targeted conservative mechanism; predicate: mobilizes; object: label: translocatable unit |
| IS26 terminal inverted repeat promoter element — increases_expression_of — adjacent antibiotic resistance gene | “The TIRs contain a bidirectional -35 promoter element that drives tnp26 expression and can, when combined with an external -10 box, enhance expression of adjacent genes including antibiotic resistance genes” (harmer2024is26and pages 6-8) | Harmer & Hall 2024. DOI:10.1128/MMBR.00119-22. https://doi.org/10.1128/MMBR.00119-22. Pub: 2024-06 | Strong regulatory edge; keep IS26-specific. Distinguishes possession from mere mobility. | subject: label: IS26 TIR promoter element; predicate: increases_expression_of; object: label: adjacent antibiotic resistance gene |
| insertion sequence/transposon — carries — virulence gene | “Some Tns were identified as carrying virulence factors, such as genes encoding effector proteins of the type III secretion system” (fernandes2024investigatingtheimpact pages 1-2) | Fernandes et al. 2024. DOI:10.1099/mgen.0.001219. https://doi.org/10.1099/mgen.0.001219. Pub: 2024-04 | Good broad cargo edge; evidence from phytopathogens. Consider object branch to T3SS effector specifically. | subject: label: transposon; predicate: carries; object: label: virulence gene / label: type III secretion effector gene |
| insertion sequence/transposon — carries — streptomycin resistance gene | “Some Tns were identified as carrying virulence factors… and resistance genes for the antimicrobial streptomycin” (fernandes2024investigatingtheimpact pages 1-2) | Fernandes et al. 2024. DOI:10.1099/mgen.0.001219. https://doi.org/10.1099/mgen.0.001219. Pub: 2024-04 | Useful antibiotic-resistance cargo edge; may be curated with CHEBI:streptomycin if desired. | subject: label: transposon; predicate: carries; object: CHEBI:17076 streptomycin resistance gene (label-only for gene) |
| IS insertion near virulence/fitness genes — modulates — virulence-associated loci | “IS elements tend to be inserted in regions near virulence and fitness genes” (fernandes2024investigatingtheimpact pages 1-2) | Fernandes et al. 2024. DOI:10.1099/mgen.0.001219. https://doi.org/10.1099/mgen.0.001219. Pub: 2024-04 | Suggest as weaker/proximity-based edge; mechanism may be regulatory or mutational, but proximity alone is not causal. Mark uncertain. | subject: label: IS insertion near virulence gene; predicate: modulates; object: label: virulence-associated locus |
| IS insertion — disrupts — avirulence gene | “ISs disrupting avirulence genes in X. oryzae genomes” (fernandes2024investigatingtheimpact pages 1-2) | Fernandes et al. 2024. DOI:10.1099/mgen.0.001219. https://doi.org/10.1099/mgen.0.001219. Pub: 2024-04 | Strong but taxon-specific. Good example of TE-driven host adaptation. | subject: label: IS insertion; predicate: disrupts; object: label: avirulence gene |
| stress conditions — alters_expression_of — transposase gene | “transcriptome analysis under different stress conditions revealed differences in the expression of genes encoding transposases” (fernandes2024investigatingtheimpact pages 1-2) | Fernandes et al. 2024. DOI:10.1099/mgen.0.001219. https://doi.org/10.1099/mgen.0.001219. Pub: 2024-04 | Good regulation edge but expression change does not guarantee transposition. Mark moderate evidence. | subject: label: stress condition; predicate: alters_expression_of; object: label: transposase gene |
| oxidative stress (H2O2) — induces — IS transposition | “80 and 100 mM H2O2 treatments induced different transpositions” (park2024thetranspositionof pages 1-2) | Park et al. 2024. DOI:10.3390/microorganisms12020328. https://doi.org/10.3390/microorganisms12020328. Pub: 2024-02 | Strong experimental induction edge; species-specific (Deinococcus geothermalis). | subject: CHEBI:16240 hydrogen peroxide / label: oxidative stress; predicate: induces; object: GO:0032196 transposition |
| gamma irradiation — induces — IS transposition | “actively transposed using oxidative stress conditions, including gamma irradiation and hydrogen peroxide treatment” (park2024thetranspositionof pages 1-2) | Park et al. 2024. DOI:10.3390/microorganisms12020328. https://doi.org/10.3390/microorganisms12020328. Pub: 2024-02 | Strong stress edge; experimental and taxon-specific. | subject: ENVO:01001000 gamma radiation / label: gamma irradiation; predicate: induces; object: GO:0032196 transposition |
| IS transposition — interrupts — phytoene desaturase gene | “integration of ISDge7 of the IS5 family, resulting in the interruption of phytoene desaturase (Dgeo_0524, crtI)” (park2024thetranspositionof pages 1-2) | Park et al. 2024. DOI:10.3390/microorganisms12020328. https://doi.org/10.3390/microorganisms12020328. Pub: 2024-02 | Strong concrete gene-inactivation example; likely too taxon/gene-specific for core graph unless examples are allowed. | subject: label: ISDge7 transposition; predicate: interrupts; object: label: phytoene desaturase gene crtI |
| chronic lytic phage infection — drives — genome-scale IS256 transposition | “chronic lytic phage infection and antibiotic exposure drive rapid genome-scale transposition in the enterococci” (kirsch2023targetediselementsequencing pages 1-2) | Kirsch et al. 2023. DOI:10.1371/journal.ppat.1011424. https://doi.org/10.1371/journal.ppat.1011424. Pub: 2023-06 | Strong selective-pressure edge; IS256/enterococci-specific. | subject: label: chronic lytic phage infection; predicate: drives; object: label: IS256 transposition |
| antibiotic exposure — drives — IS256 transposition | “chronic lytic phage infection and antibiotic exposure drive rapid genome-scale transposition” (kirsch2023targetediselementsequencing pages 1-2) | Kirsch et al. 2023. DOI:10.1371/journal.ppat.1011424. https://doi.org/10.1371/journal.ppat.1011424. Pub: 2023-06 | Strong but selective-pressure specific; links environment to TE activity. | subject: label: antibiotic exposure; predicate: drives; object: label: IS256 transposition |
| antisense RNA — negatively_regulates — IS256 transposition | “loss of the site-1 asRNA dramatically reduces IS256 circular intermediates, indicating asRNA-mediated repression controls transposition activity” (kirsch2023targetediselementsequencing pages 13-15) | Kirsch et al. 2023. DOI:10.1371/journal.ppat.1011424. https://doi.org/10.1371/journal.ppat.1011424. Pub: 2023-06 | Strong regulatory edge for IS256; mechanism-specific and useful for regulation branch. | subject: label: antisense RNA to IS256; predicate: negatively_regulates; object: label: IS256 transposition |
| IS256 transposition — forms — circular intermediate | “IS256 forms circular intermediates, showing active transposition” (kirsch2023targetediselementsequencing pages 13-15) | Kirsch et al. 2023. DOI:10.1371/journal.ppat.1011424. https://doi.org/10.1371/journal.ppat.1011424. Pub: 2023-06 | Good mechanistic intermediate edge. Specific to IS256 but likely extends to some IS families only. | subject: label: IS256 transposition; predicate: forms; object: label: circular intermediate |
| IS element insertion — decreases_fitness_cost_of — plasmid in novel host | “IS1 and IS10… decrease the fitness cost of the plasmid by disrupting an uncharacterized gene on pB1000 that is harmful to E. coli” (wedel2023insertionsequencesdetermine pages 2-4) | Wedel et al. 2023. DOI:10.1128/mBio.03158-22. https://doi.org/10.1128/mbio.03158-22. Pub: 2023-06 | Strong but host/plasmid-specific adaptive edge; useful for adaptation branch. | subject: label: IS1/IS10 insertion in pB1000; predicate: decreases_fitness_cost_of; object: label: plasmid pB1000 in E. coli |
| IS insertion — increases — plasmid stability in novel host | “after coevolution evolved plasmids were much more stable… >90% of colonies retained the plasmid for at least 100 generations” (wedel2023insertionsequencesdetermine pages 2-4) | Wedel et al. 2023. DOI:10.1128/mBio.03158-22. https://doi.org/10.1128/mbio.03158-22. Pub: 2023-06 | Good adaptation edge, but causal contribution shared with oriV SNPs in study; mark moderate if generalized. | subject: label: IS-mediated plasmid adaptation; predicate: increases; object: label: plasmid stability |
| insertion sequence pair — provides_homology_for — RecA-mediated duplication of chromosomal region | “RecA-mediated homologous recombination between a pair of insertion sequence (IS) 2-like elements duplicates a 208.6 kb region” (chandler2023theinsertionsequence pages 22-25) | Lowrey et al. 2023. DOI:10.7554/eLife.84327. https://doi.org/10.7554/eLife.84327. Pub: 2023-01 | Strong rearrangement/amplification edge but from eLife evidence summary context; useful for IS-mediated recombination branch. | subject: label: IS2-like element pair; predicate: provides_homology_for; object: label: RecA-mediated regional duplication |
| CRISPR-associated transposon (CAST) — enables — RNA-guided DNA transposition | “CASTs inherit transposon-derived machinery for DNA integration and combine it with CRISPR guide-RNA targeting, enabling guide RNA–directed transposition” (hsieh2024naturalandengineered pages 1-3) | Hsieh & Peters 2024. DOI:10.1146/annurev-biochem-030122-041908. https://doi.org/10.1146/annurev-biochem-030122-041908. Pub: 2024-08 | Strong subtype edge for Tn7-like branch. | subject: label: CRISPR-associated transposon; predicate: enables; object: label: RNA-guided DNA transposition |
| CAST targeting pathway — targets — conserved chromosomal site | “one pathway recognizes a highly conserved chromosomal site” (hsieh2024naturalandengineered pages 1-3) | Hsieh & Peters 2024. DOI:10.1146/annurev-biochem-030122-041908. https://doi.org/10.1146/annurev-biochem-030122-041908. Pub: 2024-08 | Strong conceptual edge for CAST lifecycle/targeting. | subject: label: CAST targeting pathway; predicate: targets; object: label: conserved chromosomal site |
| CAST targeting pathway — targets — mobile plasmid | “a second pathway targets mobile plasmids capable of cell-to-cell transfer” (hsieh2024naturalandengineered pages 1-3) | Hsieh & Peters 2024. DOI:10.1146/annurev-biochem-030122-041908. https://doi.org/10.1146/annurev-biochem-030122-041908. Pub: 2024-08 | Strong conceptual edge; distinguishes reservoir vs dissemination paths. | subject: label: CAST targeting pathway; predicate: targets; object: label: mobile plasmid |
| defense-associated CRISPR array crRNA — supports — CAST horizontal transfer/transposition | “type I-F, I-B, and V CASTs can utilize crRNAs from these defense arrays nearly as efficiently as their own spacers” (hu2024distincthorizontaltransfer pages 1-2) | Hu et al. 2024. DOI:10.1038/s41467-024-50816-w. https://doi.org/10.1038/s41467-024-50816-w. Pub: 2024-08 | Strong but specialized edge; may matter for CAST portability rather than baseline TE trait. | subject: label: defense-associated CRISPR array crRNA; predicate: supports; object: label: CAST transposition/horizontal transfer |
| insertion sequence excision enhancer (IEE) — promotes — IS excision | “deletion of iee greatly reduces excision and is rescued by plasmid-borne iee” (chandler2023theinsertionsequence pages 5-9) | Chandler et al. 2023. DOI:10.1101/2023.06.07.543989. https://doi.org/10.1101/2023.06.07.543989. Pub: 2023-06 | Interesting but preprint and family-limited (IS629/related copy-out elements). Mark uncertain/do not curate into core graph without stronger peer-reviewed support. | subject: label: IEE; predicate: promotes; object: label: IS excision |
| IEE-dependent IS excision — restores — interrupted gene function | “High levels of available OrfAB transposase strongly stimulate precise IS excision, which can restore interrupted genes (e.g., reactivation of stx2)” (chandler2023theinsertionsequence pages 5-9) | Chandler et al. 2023. DOI:10.1101/2023.06.07.543989. https://doi.org/10.1101/2023.06.07.543989. Pub: 2023-06 | Mechanistically interesting but preprint and system-specific. Curate cautiously. | subject: label: IEE/transposase-dependent IS excision; predicate: restores; object: label: interrupted gene function |
| insertion sequences — contribute_to — heavy-metal resistance adaptation | “Tn3 and IS110 families were inserted around the regions whose functions were As/Hg/Cu/Co/Zn/Cd translocation… implying that ISs could improve the adaptive capacities… by enhancing their resistance to heavy metals” (huang2023insertionsequencecontributes pages 1-2) | Huang et al. 2023. DOI:10.1186/s12864-023-09372-8. https://doi.org/10.1186/s12864-023-09372-8. Pub: 2023-05 | Association/inference rather than direct mechanistic proof. Mark uncertain. | subject: label: insertion sequences; predicate: contribute_to; object: label: heavy-metal resistance adaptation |
| insertion sequences — contribute_to — sulfur oxidation adaptation | “Tn3 and IS110 families were inserted around… sulfur oxidation, implying that ISs could improve the adaptive capacities” (huang2023insertionsequencecontributes pages 1-2) | Huang et al. 2023. DOI:10.1186/s12864-023-09372-8. https://doi.org/10.1186/s12864-023-09372-8. Pub: 2023-05 | Same caution as above: genomic association/inference. | subject: label: insertion sequences; predicate: contribute_to; object: label: sulfur oxidation adaptation |


*Table: This table lists candidate subject–predicate–object edges for the microbial trait transposable element, with short supporting quotes, references, curation notes, and suggested ontology grounding. It is designed to help prioritize which mechanisms are strong enough for TraitMech curation and which should remain provisional.*

### Visual evidence (mechanism schematic)
Cropped figures from Harmer & Hall (MMBR 2024) show the IS26 **copy-in** vs **targeted conservative** cointegration routes and intramolecular **deletion/inversion** outcomes (supporting IS26 rearrangement edges) and TU relocation logic. (harmer2024is26and media ac0d1e9d, harmer2024is26and media 0ed4c930)

---

## Warnings / claims that should not yet be curated (or should be marked uncertain)
1. **Association ≠ causation**: genomic proximity of IS to “virulence/fitness genes” (phytopathogens) supports a hypothesis of TE-driven adaptation, but proximity alone does not establish a causal regulatory effect; curate as *uncertain* unless a mechanistic/functional test exists. (fernandes2024investigatingtheimpact pages 1-2)
2. **Expression ≠ mobility**: stress-induced changes in transposase gene expression suggest regulation, but transposition rate changes require direct mobility evidence (e.g., new insertions/circular intermediates). (fernandes2024investigatingtheimpact pages 1-2)
3. **Preprint evidence**: the IEE (insertion sequence-excision enhancer) mechanistic model is based on a bioRxiv preprint in the retrieved set; do not curate into a core TraitMech graph without corroborating peer-reviewed confirmation, or mark as *uncertain/inferred*. (chandler2023theinsertionsequence pages 5-9)
4. **Subtype specificity**: IS26 TU/targeted conservative pathway and IS256 antisense regulation are subtype/family-specific. Curate them as subclass branches or taxon-specific edges, not as universal TE properties. (kirsch2023targetediselementsequencing pages 13-15, harmer2024is26and pages 8-12)

---

# DOI-first bibliography (recent prioritized)

1. Harmer CJ, Hall RM. **IS26 and the IS26 family: versatile resistance gene movers and genome reorganizers.** *Microbiology and Molecular Biology Reviews*. 2024-06-12. DOI:10.1128/mmbr.00119-22. URL: https://doi.org/10.1128/mmbr.00119-22 (harmer2024is26and pages 6-8, harmer2024is26and pages 8-12, harmer2024is26and media ac0d1e9d, harmer2024is26and media 0ed4c930)
2. Hsieh S-C, Peters JE. **Natural and Engineered Guide RNA–Directed Transposition with CRISPR-Associated Tn7-Like Transposons.** *Annual Review of Biochemistry*. 2024-08 (Vol 93). DOI:10.1146/annurev-biochem-030122-041908. URL: https://doi.org/10.1146/annurev-biochem-030122-041908 (hsieh2024naturalandengineered pages 1-3)
3. Hu K, Chou C-W, Wilke CO, Finkelstein IJ. **Distinct horizontal transfer mechanisms for type I and type V CRISPR-associated transposons.** *Nature Communications*. 2024-08-01. DOI:10.1038/s41467-024-50816-w. URL: https://doi.org/10.1038/s41467-024-50816-w (hu2024distincthorizontaltransfer pages 1-2)
4. Fernandes AS, et al. **Investigating the impact of insertion sequences and transposons in the genomes of the most significant phytopathogenic bacteria.** *Microbial Genomics*. 2024-04-01. DOI:10.1099/mgen.0.001219. URL: https://doi.org/10.1099/mgen.0.001219 (fernandes2024investigatingtheimpact pages 5-6, fernandes2024investigatingtheimpact pages 1-2, fernandes2024investigatingtheimpact pages 2-5)
5. Park JH, et al. **The Transposition of Insertion Sequences in Sigma-Factor- and LysR-Deficient Mutants of Deinococcus geothermalis.** *Microorganisms*. 2024-02-01. DOI:10.3390/microorganisms12020328. URL: https://doi.org/10.3390/microorganisms12020328 (park2024thetranspositionof pages 1-2)
6. Sheng Y, et al. **Insertion sequence transposition inactivates CRISPR-Cas immunity.** *Nature Communications*. 2023-07-24. DOI:10.1038/s41467-023-39964-7. URL: https://doi.org/10.1038/s41467-023-39964-7 (sheng2023insertionsequencetransposition pages 1-2)
7. Kirsch JM, et al. **Targeted IS-element sequencing uncovers transposition dynamics during selective pressure in enterococci.** *PLOS Pathogens*. 2023-06-15. DOI:10.1371/journal.ppat.1011424. URL: https://doi.org/10.1371/journal.ppat.1011424 (kirsch2023targetediselementsequencing pages 13-15, kirsch2023targetediselementsequencing pages 1-2)
8. Wedel E, et al. **Insertion Sequences Determine Plasmid Adaptation to New Bacterial Hosts.** *mBio*. 2023-06-13. DOI:10.1128/mbio.03158-22. URL: https://doi.org/10.1128/mbio.03158-22 (wedel2023insertionsequencesdetermine pages 2-4)
9. Huang S, et al. **Insertion sequence contributes to the evolution and environmental adaptation of Acidithiobacillus.** *BMC Genomics*. 2023-05-08. DOI:10.1186/s12864-023-09372-8. URL: https://doi.org/10.1186/s12864-023-09372-8 (huang2023insertionsequencecontributes pages 1-2)
10. Chandler M, Ross K, Varani AM. **The Insertion Sequence Excision Enhancer (IEE): a PrimPol-based system for Immobilizing Transposon-Transmitted Antibiotic Resistance Genes?** *bioRxiv* (preprint). 2023-06-07. DOI:10.1101/2023.06.07.543989. URL: https://doi.org/10.1101/2023.06.07.543989 (chandler2023theinsertionsequence pages 5-9)


References

1. (sheng2023insertionsequencetransposition pages 1-2): Yong Sheng, Hengyu Wang, Yixin Ou, Yingying Wu, Wei Ding, Meifeng Tao, Shuangjun Lin, Zixin Deng, Linquan Bai, and Qianjin Kang. Insertion sequence transposition inactivates crispr-cas immunity. Nature Communications, Jul 2023. URL: https://doi.org/10.1038/s41467-023-39964-7, doi:10.1038/s41467-023-39964-7. This article has 30 citations and is from a highest quality peer-reviewed journal.

2. (harmer2024is26and pages 6-8): Christopher J. Harmer and Ruth M. Hall. Is <i>26</i> and the is <i>26</i> family: versatile resistance gene movers and genome reorganizers. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00119-22, doi:10.1128/mmbr.00119-22. This article has 114 citations and is from a domain leading peer-reviewed journal.

3. (kirsch2023targetediselementsequencing pages 1-2): Joshua M. Kirsch, Shannon Ely, Madison E. Stellfox, Karthik Hullahalli, Phat Luong, Kelli L. Palmer, Daria Van Tyne, and Breck A. Duerkop. Targeted is-element sequencing uncovers transposition dynamics during selective pressure in enterococci. PLOS Pathogens, 19:e1011424, Jun 2023. URL: https://doi.org/10.1371/journal.ppat.1011424, doi:10.1371/journal.ppat.1011424. This article has 29 citations and is from a highest quality peer-reviewed journal.

4. (hsieh2024naturalandengineered pages 1-3): Shan-Chi Hsieh and Joseph E. Peters. Natural and engineered guide rna–directed transposition with crispr-associated tn7-like transposons. Aug 2024. URL: https://doi.org/10.1146/annurev-biochem-030122-041908, doi:10.1146/annurev-biochem-030122-041908. This article has 25 citations and is from a domain leading peer-reviewed journal.

5. (harmer2024is26and pages 8-12): Christopher J. Harmer and Ruth M. Hall. Is <i>26</i> and the is <i>26</i> family: versatile resistance gene movers and genome reorganizers. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00119-22, doi:10.1128/mmbr.00119-22. This article has 114 citations and is from a domain leading peer-reviewed journal.

6. (kirsch2023targetediselementsequencing pages 13-15): Joshua M. Kirsch, Shannon Ely, Madison E. Stellfox, Karthik Hullahalli, Phat Luong, Kelli L. Palmer, Daria Van Tyne, and Breck A. Duerkop. Targeted is-element sequencing uncovers transposition dynamics during selective pressure in enterococci. PLOS Pathogens, 19:e1011424, Jun 2023. URL: https://doi.org/10.1371/journal.ppat.1011424, doi:10.1371/journal.ppat.1011424. This article has 29 citations and is from a highest quality peer-reviewed journal.

7. (park2024thetranspositionof pages 1-2): Ji Hyun Park, Sohee Lee, Eunjung Shin, Sama Abdi Nansa, and Sung-Jae Lee. The transposition of insertion sequences in sigma-factor- and lysr-deficient mutants of deinococcus geothermalis. Microorganisms, 12:328, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020328, doi:10.3390/microorganisms12020328. This article has 2 citations.

8. (fernandes2024investigatingtheimpact pages 1-2): Alexia Suellen Fernandes, Kiara França Campos, Jéssica Catarine Silva de Assis, Osiel Silva Gonçalves, Marisa Vieira de Queiroz, Denise Mara Soares Bazzolli, and Mateus Ferreira Santana. Investigating the impact of insertion sequences and transposons in the genomes of the most significant phytopathogenic bacteria. Apr 2024. URL: https://doi.org/10.1099/mgen.0.001219, doi:10.1099/mgen.0.001219. This article has 10 citations and is from a peer-reviewed journal.

9. (hu2024distincthorizontaltransfer pages 1-2): Kuang Hu, Chia-Wei Chou, Claus O. Wilke, and Ilya J. Finkelstein. Distinct horizontal transfer mechanisms for type i and type v crispr-associated transposons. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50816-w, doi:10.1038/s41467-024-50816-w. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (fernandes2024investigatingtheimpact pages 5-6): Alexia Suellen Fernandes, Kiara França Campos, Jéssica Catarine Silva de Assis, Osiel Silva Gonçalves, Marisa Vieira de Queiroz, Denise Mara Soares Bazzolli, and Mateus Ferreira Santana. Investigating the impact of insertion sequences and transposons in the genomes of the most significant phytopathogenic bacteria. Apr 2024. URL: https://doi.org/10.1099/mgen.0.001219, doi:10.1099/mgen.0.001219. This article has 10 citations and is from a peer-reviewed journal.

11. (huang2023insertionsequencecontributes pages 1-2): Shanshan Huang, Huiying Li, Liyuan Ma, Rui Liu, Yiran Li, Hongmei Wang, Xiaolu Lu, Xinping Huang, Xinhong Wu, and Xueduan Liu. Insertion sequence contributes to the evolution and environmental adaptation of acidithiobacillus. BMC Genomics, May 2023. URL: https://doi.org/10.1186/s12864-023-09372-8, doi:10.1186/s12864-023-09372-8. This article has 9 citations and is from a peer-reviewed journal.

12. (wedel2023insertionsequencesdetermine pages 2-4): Emilia Wedel, Cristina Bernabe-Balas, Manuel Ares-Arroyo, Natalia Montero, Alfonso Santos-Lopez, Didier Mazel, and Bruno Gonzalez-Zorn. Insertion sequences determine plasmid adaptation to new bacterial hosts. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03158-22, doi:10.1128/mbio.03158-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

13. (chandler2023theinsertionsequence pages 22-25): Mick Chandler, Karen Ross, and Alessandro M. Varani. The insertion sequence excision enhancer (iee): a primpol-based system for immobilizing transposon-transmitted antibiotic resistance genes? bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.07.543989, doi:10.1101/2023.06.07.543989. This article has 1 citations.

14. (chandler2023theinsertionsequence pages 5-9): Mick Chandler, Karen Ross, and Alessandro M. Varani. The insertion sequence excision enhancer (iee): a primpol-based system for immobilizing transposon-transmitted antibiotic resistance genes? bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.07.543989, doi:10.1101/2023.06.07.543989. This article has 1 citations.

15. (harmer2024is26and media ac0d1e9d): Christopher J. Harmer and Ruth M. Hall. Is <i>26</i> and the is <i>26</i> family: versatile resistance gene movers and genome reorganizers. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00119-22, doi:10.1128/mmbr.00119-22. This article has 114 citations and is from a domain leading peer-reviewed journal.

16. (harmer2024is26and media 0ed4c930): Christopher J. Harmer and Ruth M. Hall. Is <i>26</i> and the is <i>26</i> family: versatile resistance gene movers and genome reorganizers. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00119-22, doi:10.1128/mmbr.00119-22. This article has 114 citations and is from a domain leading peer-reviewed journal.

17. (fernandes2024investigatingtheimpact pages 2-5): Alexia Suellen Fernandes, Kiara França Campos, Jéssica Catarine Silva de Assis, Osiel Silva Gonçalves, Marisa Vieira de Queiroz, Denise Mara Soares Bazzolli, and Mateus Ferreira Santana. Investigating the impact of insertion sequences and transposons in the genomes of the most significant phytopathogenic bacteria. Apr 2024. URL: https://doi.org/10.1099/mgen.0.001219, doi:10.1099/mgen.0.001219. This article has 10 citations and is from a peer-reviewed journal.