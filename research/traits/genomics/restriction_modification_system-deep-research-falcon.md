---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:38:55.143298'
end_time: '2026-06-18T03:49:53.056741'
duration_seconds: 657.91
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: restriction-modification system
  trait_identifier: traitmech:000095
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: restriction_modification_system
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing possession of a restriction-modification
    system that distinguishes self from non-self DNA through sequence-specific methylation
    and cleavage of unmethylated DNA by a restriction endonuclease.
  parent_traits: METPO:1000188
  synonyms: R-M system
  evidence_summary: 'DOI:10.1128/MMBR.00044-12:  (Vasu & Nagaraja review restriction-modification
    systems and their defense and additional cellular functions.) | DOI:10.3389/fmicb.2015.00528:  (Review
    of restriction-modification systems as engines of genomic diversity.)'
  causal_graph_summary: 'rm_self_nonself_defense: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** restriction-modification system
- **METPO identifier:** traitmech:000095
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a restriction-modification system that distinguishes self from non-self DNA through sequence-specific methylation and cleavage of unmethylated DNA by a restriction endonuclease.
- **Parent traits:** METPO:1000188
- **Synonyms:** R-M system
- **Existing evidence:** DOI:10.1128/MMBR.00044-12:  (Vasu & Nagaraja review restriction-modification systems and their defense and additional cellular functions.) | DOI:10.3389/fmicb.2015.00528:  (Review of restriction-modification systems as engines of genomic diversity.)
- **Existing causal graph summary:** rm_self_nonself_defense: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **restriction-modification system** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/restriction_modification_system.yaml`.

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
- **Trait label:** restriction-modification system
- **METPO identifier:** traitmech:000095
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a restriction-modification system that distinguishes self from non-self DNA through sequence-specific methylation and cleavage of unmethylated DNA by a restriction endonuclease.
- **Parent traits:** METPO:1000188
- **Synonyms:** R-M system
- **Existing evidence:** DOI:10.1128/MMBR.00044-12:  (Vasu & Nagaraja review restriction-modification systems and their defense and additional cellular functions.) | DOI:10.3389/fmicb.2015.00528:  (Review of restriction-modification systems as engines of genomic diversity.)
- **Existing causal graph summary:** rm_self_nonself_defense: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **restriction-modification system** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/restriction_modification_system.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Restriction–Modification (R–M) System (traitmech:000095)

### Scope summary (TraitMech curation focus)
Restriction–modification (R–M) systems are genetically encoded defense modules that distinguish self from non-self DNA using sequence-specific epigenetic marks (typically DNA methylation, but also phosphorothioate (PT) backbone modification in PT-based systems) and restriction of DNA that lacks the correct mark. Canonical R–M systems couple a **restriction endonuclease** activity with a **cognate DNA methyltransferase (MTase)** that protects host recognition sites; incoming DNA with unmodified recognition sites is treated as non-self and restricted (dimitriu2024variousplasmidstrategies pages 1-2, shaw2023restrictionmodificationsystemshave pages 1-2). Boundary cases relevant for curation include: (i) **Type IV** restriction enzymes that preferentially cleave **methylated** DNA motifs and lack a cognate MTase (kottenhahn2023therestriction–modificationsystems pages 1-2), and (ii) non-canonical “restriction glycosylases” (e.g., PabI family) that damage DNA by base-excision rather than phosphodiester hydrolysis, expanding the concept to broader “epigenetic immune systems” (kojima2023baseexcisionrestrictionenzymes pages 1-2). Distinguish the trait from **orphan MTases** (methylation without restriction; regulatory/epigenetic roles) and from non-RM anti-phage systems such as CRISPR-Cas, BREX, DISARM, and toxin–antitoxin modules (kojima2023baseexcisionrestrictionenzymes pages 1-2, xu2024overviewofphage pages 4-6).

### Key concepts and definitions (current understanding)
**Self/non-self discrimination via epigenetic marking.** In Type II systems, the MTase methylates short recognition sites (often 4–8 bp, frequently palindromic) to protect host DNA, while the restriction endonuclease cleaves foreign DNA lacking the mark (shaw2023restrictionmodificationsystemshave pages 1-2). A recent conjugation-focused study reiterates the core logic: “incoming DNA with unmodified recognition sites is recognized as non-self, and restricted” (dimitriu2024variousplasmidstrategies pages 1-2).

**R–M system types (mechanistic distinctions).** Recent and foundational sources summarize differences that are curation-relevant:
- **Type I**: multiprotein complexes that cleave DNA at a distance from the recognition site (dimitriu2024variousplasmidstrategies pages 1-2).
- **Type II**: restriction and modification typically as separate enzymes; cleavage within/near the recognition site; widely used in genetic engineering (vasu2013diversefunctionsof pages 2-4).
- **Type III**: multiprotein complexes that require two inverted recognition sites and may assemble as M2R1 or M2R2 complexes (dimitriu2024variousplasmidstrategies pages 1-2, vasu2013diversefunctionsof pages 2-4).
- **Type IV**: restriction enzymes lacking cognate MTases that cleave methylated motifs (kottenhahn2023therestriction–modificationsystems pages 1-2).

**Non-canonical/expanded “epigenetic immunity.”** The PabI family comprises restriction enzymes that act as DNA glycosylases, generating abasic sites and atypical strand breaks, and do not require divalent cations (kojima2023baseexcisionrestrictionenzymes pages 1-2). This broadens what “restriction” can mean mechanistically.

### Recent developments and latest research (priority 2023–2024)
#### 1) Quantifying R–M as a barrier to plasmid conjugation and how plasmids evade it (2024)
A 2024 Nucleic Acids Research study systematically tested **10 RM systems** against **13 natural antibiotic-resistance plasmids** in *E. coli* and found defense efficiency spanning “none to 10^5-fold protection” (dimitriu2024variousplasmidstrategies pages 1-2). Mechanistic determinants included (i) **recognition-site counts** on the plasmid correlating with defense strength, (ii) **plasmid-encoded methylases** that protect against restriction, and (iii) widespread plasmid **anti-restriction genes** (dimitriu2024variousplasmidstrategies pages 1-2). The study concludes that anti-RM strategies are common, rendering RM systems “only a weak barrier” to conjugative transfer in many cases (dimitriu2024variousplasmidstrategies pages 1-2).

Visual evidence for the defense-efficiency range and plasmid features (methylases, anti-restriction genes) is provided in the cropped figures/tables retrieved from the same study (dimitriu2024variousplasmidstrategies media 57fcbf16, dimitriu2024variousplasmidstrategies media 3980ff1e, dimitriu2024variousplasmidstrategies media 1b5654e9).

#### 2) Synergy between CRISPR-Cas and Type I R–M in blocking AMR plasmid transfer (2024)
A 2024 study in *Klebsiella pneumoniae* combined genomic surveys with functional conjugation assays and found that Type I-E CRISPR-Cas and Type I R–M systems “worked together” to inhibit transfer of a blaKPC IncF plasmid, with a reported ~4-log reduction at the summary level (yang2024crisprcas3andtype pages 1-2). In conjugation assays with the IncF plasmid p187-2, quantitative results showed baseline conjugation frequency 1.28×10−3 transconjugants/donors, reduced to 2.23×10−5 with R–M alone and 5.13×10−5 with CRISPR alone, while the combined defenses reduced it to 3.07×10−7 (a 4167-fold decrease) (yang2024crisprcas3andtype pages 6-8). This supports a causal edge that combined defense modules can create stronger HGT barriers than either alone.

#### 3) Phase-variable Type I R–M systems as epigenetic regulators of virulence (2024)
A 2024 mBio study demonstrates that the phase-variable Type I R–M locus **SsuCC20p** in *Streptococcus suis* “dictates the methylome,” impacts transcriptomes during growth in human serum, and changes virulence in a zebrafish larvae infection model (roodsant2024thestreptococcalphasevariable pages 1-2). Mechanistically, phase variability depends on a recombinase (**xerD**) encoded within the locus; the study reports the “indispensability of xerD for TRD shuffling” (roodsant2024thestreptococcalphasevariable pages 10-12). Locked mutants expressing single **hsdS** alleles exhibit unique methylation profiles and distinct serum transcriptomes, including “90 differentially expressed genes (>2-fold, P < 0.05)” (roodsant2024thestreptococcalphasevariable pages 10-12, roodsant2024thestreptococcalphasevariable pages 1-2). Quantitative methylation differences across motifs were observed (e.g., ~99–100% methylation at one motif class versus ~44–48% partial methylation at another) (roodsant2024thestreptococcalphasevariable pages 7-10). In vivo, virulence differed among locked mutants and allele frequencies shifted during infection (roodsant2024thestreptococcalphasevariable pages 10-12, roodsant2024thestreptococcalphasevariable pages 1-2).

#### 4) PT (phosphorothioate) modification-based R–M systems and HGT/AMR outcomes (2023–2024)
A 2023 Microbiology Spectrum study links PT-based R–M systems (DndABCDE modification; DndFGH restriction) to reduced acquisition of mobile-element-derived AMR genes: presence of PT R–M “effectively reduced the distribution of horizontal gene transfer (HGT)-derived AMR genes” and “could suppress HGT frequency” (xu2023thednaphosphorothioation pages 1-2). A 2024 review summarizes additional PT-based defense architectures, including Dnd and Ssp modules and effectors (SspE, SspFGH) that target unmodified or replication processes, and notes that compatible effectors can “greatly enhance resistance” (xu2024overviewofphage pages 4-6). Because parts of this PT mechanistic detail are review-derived, edges involving specific Ssp effectors should be curated with caution pending primary-source confirmation.

### Current applications and real-world implementations
**Biotechnology and genetic engineering constraints/solutions.** R–M systems are practical barriers to transforming and engineering many microbes; for example, *Clostridium carboxidivorans* encodes many restriction enzymes and MTases, and methylome profiling (SMRT/bisulfite) identified motifs enabling strategies such as removing recognition sites from plasmids or matching donor methylation to the recipient to improve transformation success (kottenhahn2023therestriction–modificationsystems pages 1-2). This supports curation of edges linking RM presence to decreased transformation/conjugation efficiency and linking methylome characterization to mitigation strategies.

**AMR control via HGT modulation (conceptual application).** The PT-based study suggests that defense barriers can reduce HGT-derived AMR gene acquisition by suppressing HGT frequency (xu2023thednaphosphorothioation pages 1-2). The *K. pneumoniae* study further implies that engineering or selecting for co-occurrence of defense systems (CRISPR + RM) could limit spread of carbapenem-resistance plasmids (yang2024crisprcas3andtype pages 6-8, yang2024crisprcas3andtype pages 1-2).

### Expert opinions and analysis (authoritative sources)
**R–M as abundant, evolution-shaping defense with pervasive counter-defense.** A 2023 NAR analysis argues R–M systems are among the most abundant defenses (present in ~83% of genomes in their dataset) and shape plasmid sequence evolution via restriction-site avoidance; plasmid strategies differ with size/host range (shaw2023restrictionmodificationsystemshave pages 1-2). A 2024 NAR study reinforces that despite high prevalence, plasmids commonly encode anti-RM strategies, making RM an often “weak barrier” to conjugation (dimitriu2024variousplasmidstrategies pages 1-2). Foundational synthesis emphasizes phage countermeasures (DNA modification, phage-encoded MTases, antirestriction proteins such as Ocr) that can erode RM effectiveness (vasu2013diversefunctionsof pages 5-6).

### Relevant statistics and quantitative findings (recent studies)
- **Defense efficiency range against conjugation:** none to ~10^5-fold protection across tested RM system–plasmid combinations (dimitriu2024variousplasmidstrategies pages 1-2, dimitriu2024variousplasmidstrategies media 57fcbf16).
- **CRISPR+RM synergy against blaKPC IncF plasmid transfer (conjugation frequencies):** baseline 1.28×10−3; RM alone 2.23×10−5; CRISPR alone 5.13×10−5; combined 3.07×10−7 (4167-fold decrease) (yang2024crisprcas3andtype pages 6-8).
- **SsuCC20p prevalence in surveyed *S. suis* genomes:** 22 complete loci among 1,749 assemblies (roodsant2024thestreptococcalphasevariable pages 1-2).
- **SsuCC20p transcriptome impact in serum:** 90 DE genes (>2-fold, P<0.05) (roodsant2024thestreptococcalphasevariable pages 10-12).
- **Methylation fraction differences across motifs in *S. suis* WT:** ~99–100% vs ~44–48% for specific motif classes (roodsant2024thestreptococcalphasevariable pages 7-10).

---

## Candidate mechanistic nodes (grouped for curation)

### A) Systems / processes
- Restriction–modification system (METPO:traitmech:000095; GO:0009307 DNA restriction-modification system) (dimitriu2024variousplasmidstrategies pages 1-2, shaw2023restrictionmodificationsystemshave pages 1-2)
- DNA methylation (GO:0006306) (shaw2023restrictionmodificationsystemshave pages 1-2)
- Restriction endonuclease activity / DNA cleavage (GO:0016888) (shaw2023restrictionmodificationsystemshave pages 1-2)
- Conjugation / HGT barrier (GO:0000746 conjugation) (dimitriu2024variousplasmidstrategies pages 1-2, yang2024crisprcas3andtype pages 6-8)
- Phase variation via recombination in hsdS/TRDs (GO:0006310 DNA recombination; label-only for TRD shuffling) (roodsant2024thestreptococcalphasevariable pages 10-12, roodsant2024thestreptococcalphasevariable pages 1-2)

### B) Genes/proteins/complexes (label-only unless curated to UniProt per taxon)
- Restriction endonuclease (REase) (shaw2023restrictionmodificationsystemshave pages 1-2)
- DNA methyltransferase (MTase) (shaw2023restrictionmodificationsystemshave pages 1-2)
- Type I subunits: HsdR / HsdM / HsdS (yang2024crisprcas3andtype pages 1-2)
- Site-specific recombinase XerD (SsuCC20p locus) (roodsant2024thestreptococcalphasevariable pages 10-12, roodsant2024thestreptococcalphasevariable pages 1-2)
- Anti-restriction proteins: Ocr, ArdA, ArdB (vasu2013diversefunctionsof pages 5-6, kudryavtseva2023broadnessandspecificity pages 1-2)

### C) Mobile genetic element features (plasmid/phage)
- RM recognition sites (sequence feature; label-only) (dimitriu2024variousplasmidstrategies pages 1-2)
- Plasmid-encoded methylases (e.g., Dam/Dcm as examples listed in Dimitriu figures/tables) (dimitriu2024variousplasmidstrategies pages 1-2, dimitriu2024variousplasmidstrategies media 3980ff1e)
- Plasmid anti-restriction genes (e.g., ardA/ardB/ardC; klcA; as summarized in Dimitriu table) (dimitriu2024variousplasmidstrategies pages 1-2, dimitriu2024variousplasmidstrategies media 3980ff1e)

### D) PT (phosphorothioate) modules
- DndABCDE (PT modification) / DndFGH (restriction) (label-only; PT-based RM) (xu2023thednaphosphorothioation pages 1-2)
- SspABCD, SspE, SspFGH (review-derived; label-only) (xu2024overviewofphage pages 4-6)

---

## Candidate causal edges (evidence-backed)
The following table is structured for direct curation into `restriction_modification_system.yaml`.

| Edge (subject—predicate—object) | Node type(s) | Suggested CURIE grounding (if known) | Evidence snippet (short quote) | Source (DOI, year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|---|
| Restriction–modification system — enables discrimination of — self vs non-self DNA by methylation state | trait → biological process | METPO:traitmech:000095; GO:0009307 DNA restriction-modification system | “incoming DNA with unmodified recognition sites is recognized as non-self, and restricted” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Core defining edge; broad across classical RM systems. |
| Cognate DNA methyltransferase — methylates — host recognition sites | protein/enzyme → DNA modification | GO:0009008 DNA-methyltransferase activity; GO:0006306 DNA methylation | “a methyltransferase (MTase) that methylates those sites to protect host DNA” (shaw2023restrictionmodificationsystemshave pages 1-2) | DOI:10.1093/nar/gkad452, 2023, https://doi.org/10.1093/nar/gkad452 | Curate as generic MTase node unless subtype-specific enzyme is known. |
| Host-site methylation — protects from — cognate restriction endonuclease cleavage | DNA modification → process inhibition | GO:0006306; GO:0016888 endodeoxyribonuclease activity | “host DNA is protected while incoming foreign DNA lacking the same methylation is cleaved” (shaw2023restrictionmodificationsystemshave pages 1-2) | DOI:10.1093/nar/gkad452, 2023, https://doi.org/10.1093/nar/gkad452 | Central mechanistic edge for self-protection. |
| Restriction endonuclease — cleaves — unmethylated foreign double-stranded DNA | protein/enzyme → substrate/process | GO:0016888; GO:0009307 | “a restriction endonuclease (REase) that cuts double-stranded DNA” and foreign DNA “is cleaved” (shaw2023restrictionmodificationsystemshave pages 1-2) | DOI:10.1093/nar/gkad452, 2023, https://doi.org/10.1093/nar/gkad452 | Broad, well-supported; applies most clearly to Types I–III and PT-associated effectors analogously. |
| Type I RM complex — cleaves — DNA at a distance from recognition site | complex → process | GO:0009307 | “Type I are multiprotein complexes that cleave at a distance” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Mechanistic subtype edge; no stable complex CURIE provided. |
| Type III RM complex — requires — two inverted recognition sites for cleavage | complex → requirement | GO:0009307 | “Type III require two inverted recognition sites” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Important subtype-specific constraint; curate as subtype-specific. |
| Type III RM complex — has subunit composition — M2R1/M2R2 hetero-oligomer | complex → has part | GO:0032991 protein-containing complex | “type III enzymes form heterotrimers (M2R1) or heterotetramers (M2R2)” (vasu2013diversefunctionsof pages 2-4) | DOI:10.1128/MMBR.00044-12, 2013, https://doi.org/10.1128/MMBR.00044-12 | Structural edge; foundational but older. |
| Type IV restriction enzyme — cleaves — methylated DNA motifs | protein/enzyme → substrate/process | GO:0016888 | “Type IV… cut methylated motifs” (kottenhahn2023therestriction–modificationsystems pages 1-2) | DOI:10.3390/microorganisms11122962, 2023, https://doi.org/10.3390/microorganisms11122962 | Distinguishes type IV from methylation-protected Types I–III. |
| PabI-family restriction glycosylase — excises base from — unmethylated recognition sequence | protein/enzyme → substrate/process | GO:0008725 DNA-3-methyladenine glycosylase activity (approximate only); label-only candidate: restriction glycosylase | “a DNA glycosylase that excises a base to create an abasic (AP) site” (kojima2023baseexcisionrestrictionenzymes pages 1-2) | DOI:10.1093/dnares/dsad009, 2023, https://doi.org/10.1093/dnares/dsad009 | Non-classical BER-based restriction; grounding may need label-only node. |
| Restriction cleavage of incoming DNA — reduces — plasmid conjugation success | process → phenotype | GO:0009307; GO:0000746 conjugation | “RM systems form only a weak barrier for plasmid transfer by conjugation” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Direction is well-supported, but magnitude is context-dependent and often weak. |
| Number of RM recognition sites on plasmid — positively correlates with — restriction efficiency | DNA feature → phenotype | label-only candidate: RM recognition-site count | “higher numbers of sites being associated with stronger defence” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Strong candidate quantitative edge; recipient-system specific. |
| Natural plasmid features — modulate — RM defence efficiency from none to 10^5-fold | DNA feature set → phenotype | label-only candidate: plasmid anti-RM strategy | “variation in defence efficiency ranging from none to 10^5-fold protection” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Aggregate edge summarizing assay outcome; do not overgeneralize to all taxa. |
| Plasmid-encoded methylase — protects plasmid from — host restriction activity | protein/enzyme → process inhibition | GO:0009008 | “some plasmids encode methylases that protect against restriction activity” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Strong mechanistic edge; specific methylases vary. |
| Anti-restriction genes on plasmids — decrease — RM-mediated restriction during conjugation | gene family/protein → phenotype | label-only candidates: ArdA, ArdB, Ocr, KlcA, ArdC | “many encode anti-restriction genes that provide protection against several types of RM systems” (dimitriu2024variousplasmidstrategies pages 1-2) | DOI:10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Broad anti-defence edge; curate named proteins separately where possible. |
| Ocr — inhibits — type I restriction-modification complex | protein → complex inhibition | label-only candidate: Ocr | “Dedicated antirestriction proteins (e.g., T7 OCR… DNA mimic) block type I systems” (vasu2013diversefunctionsof pages 5-6) | DOI:10.1128/MMBR.00044-12, 2013, https://doi.org/10.1128/MMBR.00044-12 | Foundational evidence; mechanism supported further by newer studies on DNA mimicry. |
| ArdA — inhibits — type I restriction and modification activities | protein → complex inhibition | label-only candidate: ArdA | “ArdA and Ocr are DNA-mimic proteins that can inhibit both restriction and modification activities” (kudryavtseva2023broadnessandspecificity pages 1-2) | DOI:10.3389/fmicb.2023.1133144, 2023, https://doi.org/10.3389/fmicb.2023.1133144 | Good mechanistic edge; mainly tested on type I systems. |
| ArdB — inhibits — type I restriction systems broadly across families | protein → complex inhibition | label-only candidate: ArdB | “ArdB shows antirestriction activity in vivo across multiple type I families” (kudryavtseva2023broadnessandspecificity pages 1-2) | DOI:10.3389/fmicb.2023.1133144, 2023, https://doi.org/10.3389/fmicb.2023.1133144 | Mechanism less resolved than Ocr/ArdA; mark mechanistic details uncertain. |
| ArdB — does not inhibit — BREX or RMIII | protein → lacks effect on system | label-only candidates: ArdB, BREX, RMIII | “ArdB… fails against systems fundamentally different from type I such as BREX and RMIII” (kudryavtseva2023broadnessandspecificity pages 1-2) | DOI:10.3389/fmicb.2023.1133144, 2023, https://doi.org/10.3389/fmicb.2023.1133144 | Useful negative edge; scope limited to tested systems. |
| Phage-encoded DNA methyltransferase — reduces — host RM restriction of phage genome | protein/enzyme → phenotype | GO:0009008 | “phages encode DNA methyltransferases… to protect genomes” (vasu2013diversefunctionsof pages 5-6) | DOI:10.1128/MMBR.00044-12, 2013, https://doi.org/10.1128/MMBR.00044-12 | Broad phage counter-defence strategy; foundational evidence. |
| Phage DNA base modification — reduces — sensitivity to restriction enzymes | DNA modification → phenotype | CHEBI candidates for modified bases not specified; label-only candidate: hydroxymethylated/glycosylated DNA | “Phages also modify DNA… to resist many REases” (vasu2013diversefunctionsof pages 5-6) | DOI:10.1128/MMBR.00044-12, 2013, https://doi.org/10.1128/MMBR.00044-12 | Strong but broad; specific chemistries and taxa vary. |
| DndABCDE complex — installs — DNA phosphorothioate modification | protein complex → DNA modification | label-only candidate: DndABCDE; GO label candidate: DNA phosphorothioation | “modification by DndABCDE” (xu2023thednaphosphorothioation pages 1-2) | DOI:10.1128/spectrum.03509-22, 2023, https://doi.org/10.1128/spectrum.03509-22 | PT-based RM; ontology grounding may require label-only nodes. |
| DndFGH complex — restricts — non-PT-modified exogenous DNA | protein complex → substrate/process | label-only candidate: DndFGH | “restriction by DndFGH” and PT systems “attack non-PT-modified exogenous DNA” (xu2023thednaphosphorothioation pages 1-2, xu2024overviewofphage pages 4-6) | DOI:10.1128/spectrum.03509-22, 2023, https://doi.org/10.1128/spectrum.03509-22 | Core PT self/non-self edge; combine classical and review evidence. |
| PT-based RM system — suppresses — horizontal gene transfer frequency | trait/system → process | label-only candidate: PT-based RM system | “could suppress HGT frequency” (xu2023thednaphosphorothioation pages 1-2) | DOI:10.1128/spectrum.03509-22, 2023, https://doi.org/10.1128/spectrum.03509-22 | Strong applied edge; taxon breadth from comparative study, but still not universal. |
| PT-based RM system — reduces acquisition of — HGT-derived AMR genes | trait/system → phenotype | label-only candidate: PT-based RM system | “effectively reduced the distribution of horizontal gene transfer (HGT)-derived AMR genes” (xu2023thednaphosphorothioation pages 1-2) | DOI:10.1128/spectrum.03509-22, 2023, https://doi.org/10.1128/spectrum.03509-22 | Valuable ecological/clinical edge; indirect via HGT suppression. |
| SspABCD complex — installs — single-strand phosphorothioate modification | protein complex → DNA modification | label-only candidate: SspABCD | “The Ssp systems (SspABCD) perform single-strand PT modification” (xu2024overviewofphage pages 4-6) | DOI:10.3390/ijms252413316, 2024, https://doi.org/10.3390/ijms252413316 | Review source; useful candidate but secondary evidence. |
| SspE — damages/nicks — phage DNA in PT-dependent manner | protein/effector → substrate/process | label-only candidate: SspE | “SspE… nicks/damages phage DNA in a modification-dependent manner” (xu2024overviewofphage pages 4-6) | DOI:10.3390/ijms252413316, 2024, https://doi.org/10.3390/ijms252413316 | Review-derived edge; seek primary source before final curation if possible. |
| SspFGH — destroys — unmodified DNA | protein complex → substrate/process | label-only candidate: SspFGH | “SspFGH… phosphorylates and destroys unmodified DNA” (xu2024overviewofphage pages 4-6) | DOI:10.3390/ijms252413316, 2024, https://doi.org/10.3390/ijms252413316 | Review-derived; wording suggests mechanism but may need primary validation. |
| XerD recombinase — mediates TRD shuffling of — phase-variable hsdS locus (SsuCC20p) | recombinase → gene rearrangement | label-only candidate: XerD; hsdS; GO:0006310 DNA recombination | “phase variability relies on a recombinase present within the locus” and “indispensability of xerD for TRD shuffling” (roodsant2024thestreptococcalphasevariable pages 1-2, roodsant2024thestreptococcalphasevariable pages 10-12) | DOI:10.1128/mbio.02259-23, 2024, https://doi.org/10.1128/mbio.02259-23 | Strong phase-variation edge; currently best supported in S. suis SsuCC20p. |
| hsdS allele state — determines — genome methylation profile | gene allele → methylome | label-only candidate: hsdS; GO:0006306 | “locked mutants expressing a single hsdS each show a unique genome methylation profile” (roodsant2024thestreptococcalphasevariable pages 1-2) | DOI:10.1128/mbio.02259-23, 2024, https://doi.org/10.1128/mbio.02259-23 | Strong, locus-specific but broadly consistent with phasevarion literature. |
| SsuCC20p methylome state — alters — transcriptome in human serum | methylome → gene expression program | GO:0010468 regulation of gene expression, epigenetic | “when grown in human serum, have distinct transcriptomes” and “90 differentially expressed genes” (roodsant2024thestreptococcalphasevariable pages 1-2, roodsant2024thestreptococcalphasevariable pages 10-12) | DOI:10.1128/mbio.02259-23, 2024, https://doi.org/10.1128/mbio.02259-23 | Strong in serum-growth context; environment-specific edge. |
| SsuCC20p phase state — modulates — virulence in zebrafish infection model | epigenetic phase state → virulence phenotype | ENVO not applicable; label-only candidate: zebrafish larvae infection model | “significant differences in virulence between the locked mutants” (roodsant2024thestreptococcalphasevariable pages 1-2) | DOI:10.1128/mbio.02259-23, 2024, https://doi.org/10.1128/mbio.02259-23 | Assay/model-specific; mark as host-model dependent. |
| CRISPR-Cas type I-E + type I RM co-occurrence — reduces — blaKPC-IncF plasmid acquisition | defense system combination → HGT phenotype | label-only candidates: CRISPR-Cas type I-E, type I RM, blaKPC-IncF plasmid | “produced a ~4-log reduction in acquisition of blaKPC plasmids” (yang2024crisprcas3andtype pages 1-2) | DOI:10.1186/s12866-024-03381-7, 2024, https://doi.org/10.1186/s12866-024-03381-7 | Strong recent quantitative edge; species-specific to K. pneumoniae assay. |
| Type I RM alone — reduces conjugation frequency of — blaKPC plasmid to 2.23×10−5 from 1.28×10−3 | defense system → quantitative phenotype | label-only candidate: type I RM | “with R-M alone 2.23×10−5… baseline 1.28×10−3” (yang2024crisprcas3andtype pages 6-8) | DOI:10.1186/s12866-024-03381-7, 2024, https://doi.org/10.1186/s12866-024-03381-7 | Quantitative edge from a specific plasmid/host pair; curate with assay note. |
| CRISPR-Cas alone — reduces conjugation frequency of — blaKPC plasmid to 5.13×10−5 from 1.28×10−3 | defense system → quantitative phenotype | label-only candidate: CRISPR-Cas type I-E | “with CRISPR alone 5.13×10−5… baseline 1.28×10−3” (yang2024crisprcas3andtype pages 6-8) | DOI:10.1186/s12866-024-03381-7, 2024, https://doi.org/10.1186/s12866-024-03381-7 | Useful comparison edge for combination logic. |
| CRISPR-Cas + type I RM combined — lowers conjugation frequency to — 3.07×10−7 transconjugants/donor | defense system combination → quantitative phenotype | label-only candidates: CRISPR-Cas type I-E, type I RM | “dropped to 3.07×10−7, a 4167-fold decrease” (yang2024crisprcas3andtype pages 6-8) | DOI:10.1186/s12866-024-03381-7, 2024, https://doi.org/10.1186/s12866-024-03381-7 | Strongest quantitative combination edge; likely assay-specific but highly informative. |


*Table: This table lists curation-ready candidate causal edges for the restriction–modification system trait, spanning core self/non-self discrimination, subtype mechanisms, anti-restriction countermeasures, PT-based systems, phase-variable epigenetic effects, and quantitative HGT inhibition. It is useful as a direct starting point for TraitMech YAML curation with evidence snippets, grounding suggestions, and uncertainty notes.*

Key figures/tables supporting plasmid-conjugation barrier quantification and plasmid counter-defence features:
- Defense-efficiency range and site-count relationship (dimitriu2024variousplasmidstrategies media 57fcbf16, dimitriu2024variousplasmidstrategies media 1b5654e9)
- Plasmid anti-RM genes and methylases summary (dimitriu2024variousplasmidstrategies media 3980ff1e)

---

## Warnings / “do not yet curate” items (or curate as uncertain)
1. **SspE/SspFGH mechanistic edges** are sourced from a 2024 review rather than primary mechanistic studies in the retrieved evidence; curate as *uncertain* or defer until primary citations are added (xu2024overviewofphage pages 4-6).
2. **Generality of quantitative effects** (e.g., 10^5-fold conjugation protection; 4167-fold reduction with CRISPR+RM) is assay- and taxon-specific; curate edges with explicit context (host strain, plasmid, and experimental design) rather than as universal constants (dimitriu2024variousplasmidstrategies pages 1-2, yang2024crisprcas3andtype pages 6-8).
3. **PabI restriction glycosylase grounding** may require label-only nodes unless curated to specific families/EC/GO terms; treat as a boundary case expanding RM mechanisms (kojima2023baseexcisionrestrictionenzymes pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates where available)
- Dimitriu T, Szczelkun MD, Westra ER. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. *Nucleic Acids Research*. Oct 2024. https://doi.org/10.1093/nar/gkae896 (dimitriu2024variousplasmidstrategies pages 1-2, dimitriu2024variousplasmidstrategies media 57fcbf16, dimitriu2024variousplasmidstrategies media 3980ff1e, dimitriu2024variousplasmidstrategies media 1b5654e9)
- Yang Y et al. CRISPR-Cas3 and type I restriction-modification team up against blaKPC-IncF plasmid transfer in *Klebsiella pneumoniae*. *BMC Microbiology*. Jul 2024. https://doi.org/10.1186/s12866-024-03381-7 (yang2024crisprcas3andtype pages 6-8, yang2024crisprcas3andtype pages 1-2)
- Roodsant TJ et al. The streptococcal phase-variable type I restriction modification system SsuCC20p dictates the methylome of *Streptococcus suis* impacting the transcriptome and virulence in a zebrafish larvae infection model. *mBio*. Jan 2024. https://doi.org/10.1128/mbio.02259-23 (roodsant2024thestreptococcalphasevariable pages 10-12, roodsant2024thestreptococcalphasevariable pages 7-10, roodsant2024thestreptococcalphasevariable pages 1-2)
- Xu C et al. The DNA phosphorothioation restriction-modification system influences the antimicrobial resistance of pathogenic bacteria. *Microbiology Spectrum*. Feb 2023. https://doi.org/10.1128/spectrum.03509-22 (xu2023thednaphosphorothioation pages 1-2)
- Shaw LP, Rocha EPC, MacLean RC. Restriction-modification systems have shaped the evolution and distribution of plasmids across bacteria. *Nucleic Acids Research*. May 2023. https://doi.org/10.1093/nar/gkad452 (shaw2023restrictionmodificationsystemshave pages 1-2)
- Kudryavtseva AA et al. Broadness and specificity: ArdB, ArdA, and Ocr against various restriction-modification systems. *Frontiers in Microbiology*. Apr 2023. https://doi.org/10.3389/fmicb.2023.1133144 (kudryavtseva2023broadnessandspecificity pages 1-2)
- Kojima KK, Kobayashi I. Base-excision restriction enzymes: expanding the world of epigenetic immune systems. *DNA Research*. May 2023. https://doi.org/10.1093/dnares/dsad009 (kojima2023baseexcisionrestrictionenzymes pages 1-2)
- Kottenhahn P et al. The Restriction–Modification Systems of *Clostridium carboxidivorans* P7. *Microorganisms*. Dec 2023. https://doi.org/10.3390/microorganisms11122962 (kottenhahn2023therestriction–modificationsystems pages 1-2)
- Xu X, Gu P. Overview of Phage Defense Systems in Bacteria and Their Applications. *International Journal of Molecular Sciences*. Dec 2024. https://doi.org/10.3390/ijms252413316 (xu2024overviewofphage pages 4-6)
- Vasu K, Nagaraja V. Diverse Functions of Restriction-Modification Systems in Addition to Cellular Defense. *Microbiology and Molecular Biology Reviews*. Mar 2013. https://doi.org/10.1128/MMBR.00044-12 (vasu2013diversefunctionsof pages 5-6, vasu2013diversefunctionsof pages 2-4)
- Wang X, Yu D, Chen L. Antimicrobial resistance and mechanisms of epigenetic regulation. *Frontiers in Cellular and Infection Microbiology*. Jun 2023. https://doi.org/10.3389/fcimb.2023.1199646 (wang2023antimicrobialresistanceand pages 7-8)


References

1. (dimitriu2024variousplasmidstrategies pages 1-2): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 41 citations and is from a highest quality peer-reviewed journal.

2. (shaw2023restrictionmodificationsystemshave pages 1-2): Liam P Shaw, Eduardo P C Rocha, and R Craig MacLean. Restriction-modification systems have shaped the evolution and distribution of plasmids across bacteria. Nucleic Acids Research, 51:6806-6818, May 2023. URL: https://doi.org/10.1093/nar/gkad452, doi:10.1093/nar/gkad452. This article has 110 citations and is from a highest quality peer-reviewed journal.

3. (kottenhahn2023therestriction–modificationsystems pages 1-2): Patrick Kottenhahn, Gabriele Philipps, Boyke Bunk, Cathrin Spröer, and Stefan Jennewein. The restriction–modification systems of clostridium carboxidivorans p7. Microorganisms, 11:2962, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122962, doi:10.3390/microorganisms11122962. This article has 6 citations.

4. (kojima2023baseexcisionrestrictionenzymes pages 1-2): Kenji K Kojima and Ichizo Kobayashi. Base-excision restriction enzymes: expanding the world of epigenetic immune systems. DNA Research: An International Journal for Rapid Publication of Reports on Genes and Genomes, May 2023. URL: https://doi.org/10.1093/dnares/dsad009, doi:10.1093/dnares/dsad009. This article has 6 citations.

5. (xu2024overviewofphage pages 4-6): Xiaomei Xu and Pengfei Gu. Overview of phage defense systems in bacteria and their applications. International Journal of Molecular Sciences, 25:13316, Dec 2024. URL: https://doi.org/10.3390/ijms252413316, doi:10.3390/ijms252413316. This article has 34 citations.

6. (vasu2013diversefunctionsof pages 2-4): Kommireddy Vasu and Valakunja Nagaraja. Diverse functions of restriction-modification systems in addition to cellular defense. Microbiology and Molecular Biology Reviews, 77:53-72, Mar 2013. URL: https://doi.org/10.1128/mmbr.00044-12, doi:10.1128/mmbr.00044-12. This article has 796 citations and is from a domain leading peer-reviewed journal.

7. (dimitriu2024variousplasmidstrategies media 57fcbf16): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 41 citations and is from a highest quality peer-reviewed journal.

8. (dimitriu2024variousplasmidstrategies media 3980ff1e): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 41 citations and is from a highest quality peer-reviewed journal.

9. (dimitriu2024variousplasmidstrategies media 1b5654e9): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 41 citations and is from a highest quality peer-reviewed journal.

10. (yang2024crisprcas3andtype pages 1-2): Yang Yang, Peiyao Zhou, Dongxing Tian, Weiwen Wang, Ying Zhou, and Xiaofei Jiang. Crispr-cas3 and type i restriction-modification team up against blakpc-incf plasmid transfer in klebsiella pneumoniae. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03381-7, doi:10.1186/s12866-024-03381-7. This article has 14 citations and is from a peer-reviewed journal.

11. (yang2024crisprcas3andtype pages 6-8): Yang Yang, Peiyao Zhou, Dongxing Tian, Weiwen Wang, Ying Zhou, and Xiaofei Jiang. Crispr-cas3 and type i restriction-modification team up against blakpc-incf plasmid transfer in klebsiella pneumoniae. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03381-7, doi:10.1186/s12866-024-03381-7. This article has 14 citations and is from a peer-reviewed journal.

12. (roodsant2024thestreptococcalphasevariable pages 1-2): Thomas J. Roodsant, Boas C. L. van der Putten, Jaime Brizuela, Jordy P. M. Coolen, Tim J. H. Baltussen, Kim Schipper, Yvonne Pannekoek, Kees C H van der Ark, and Constance Schultsz. The streptococcal phase-variable type i restriction modification system ssucc20p dictates the methylome of <i>streptococcus suis</i> impacting the transcriptome and virulence in a zebrafish larvae infection model. Jan 2024. URL: https://doi.org/10.1128/mbio.02259-23, doi:10.1128/mbio.02259-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (roodsant2024thestreptococcalphasevariable pages 10-12): Thomas J. Roodsant, Boas C. L. van der Putten, Jaime Brizuela, Jordy P. M. Coolen, Tim J. H. Baltussen, Kim Schipper, Yvonne Pannekoek, Kees C H van der Ark, and Constance Schultsz. The streptococcal phase-variable type i restriction modification system ssucc20p dictates the methylome of <i>streptococcus suis</i> impacting the transcriptome and virulence in a zebrafish larvae infection model. Jan 2024. URL: https://doi.org/10.1128/mbio.02259-23, doi:10.1128/mbio.02259-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

14. (roodsant2024thestreptococcalphasevariable pages 7-10): Thomas J. Roodsant, Boas C. L. van der Putten, Jaime Brizuela, Jordy P. M. Coolen, Tim J. H. Baltussen, Kim Schipper, Yvonne Pannekoek, Kees C H van der Ark, and Constance Schultsz. The streptococcal phase-variable type i restriction modification system ssucc20p dictates the methylome of <i>streptococcus suis</i> impacting the transcriptome and virulence in a zebrafish larvae infection model. Jan 2024. URL: https://doi.org/10.1128/mbio.02259-23, doi:10.1128/mbio.02259-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (xu2023thednaphosphorothioation pages 1-2): Congrui Xu, Jing Rao, Yuqing Xie, Jiajun Lu, Zhiqiang Li, Changjiang Dong, Lianrong Wang, Jinghong Jiang, Chao Chen, and Shi Chen. The dna phosphorothioation restriction-modification system influences the antimicrobial resistance of pathogenic bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.03509-22, doi:10.1128/spectrum.03509-22. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (vasu2013diversefunctionsof pages 5-6): Kommireddy Vasu and Valakunja Nagaraja. Diverse functions of restriction-modification systems in addition to cellular defense. Microbiology and Molecular Biology Reviews, 77:53-72, Mar 2013. URL: https://doi.org/10.1128/mmbr.00044-12, doi:10.1128/mmbr.00044-12. This article has 796 citations and is from a domain leading peer-reviewed journal.

17. (kudryavtseva2023broadnessandspecificity pages 1-2): Anna A. Kudryavtseva, Eva Cséfalvay, Evgeniy Yu Gnuchikh, Darya D. Yanovskaya, Mikhail A. Skutel, Artem B. Isaev, Sergey V. Bazhenov, Anna A. Utkina, and Ilya V. Manukhov. Broadness and specificity: ardb, arda, and ocr against various restriction-modification systems. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1133144, doi:10.3389/fmicb.2023.1133144. This article has 23 citations and is from a peer-reviewed journal.

18. (wang2023antimicrobialresistanceand pages 7-8): Xinrui Wang, Donghong Yu, and Lu Chen. Antimicrobial resistance and mechanisms of epigenetic regulation. Frontiers in Cellular and Infection Microbiology, Jun 2023. URL: https://doi.org/10.3389/fcimb.2023.1199646, doi:10.3389/fcimb.2023.1199646. This article has 73 citations.