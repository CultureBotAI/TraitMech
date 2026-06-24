---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:30:27.837626'
end_time: '2026-06-18T06:50:52.955104'
duration_seconds: 1225.12
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: capsule
  trait_identifier: traitmech:000063
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: capsule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait in which the cell is surrounded by a well-organized
    layer of polysaccharide (or rarely polypeptide) external to the cell envelope,
    mediating adhesion, desiccation resistance, and immune evasion.
  parent_traits: METPO:1000059
  synonyms: capsulated, capsular polysaccharide
  evidence_summary: 'DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry
    and genetics of capsular polysaccharide production in bacteria", treats the capsule
    as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield
    reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)'
  causal_graph_summary: 'capsule_polysaccharide_protection: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** capsule
- **METPO identifier:** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **capsule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/capsule.yaml`.

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
- **Trait label:** capsule
- **METPO identifier:** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **capsule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/capsule.yaml`.

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


## Capsule (TraitMech: traitmech:000063) — curation-focused research report

### Scope summary (trait definition and boundaries)
Bacterial capsules are polymers secreted near the cell wall that envelop the entire cell, forming a surface-associated layer that can be covalently connected to peptidoglycan (Gram-negative) or the plasma membrane (Gram-positive), and may also connect to surface proteins. (gao2024bacterialcapsulesoccurrence pages 1-3) Capsules are most commonly polysaccharide (capsular polysaccharides, CPS), but can also be polypeptide (e.g., poly-γ-D-glutamate) or mixed polysaccharide/polypeptide depending on species. (gao2024bacterialcapsulesoccurrence pages 1-3)

**Trait scope for curation:** the TraitMech “capsule” trait should represent the *presence and production of an organized, cell-associated capsule layer* (typically CPS), including its biosynthesis, export, attachment/organization on the surface, and regulatory systems that alter capsule abundance/architecture. (gao2024bacterialcapsulesoccurrence pages 1-3)

**Boundary cases and nearby traits (caution):** the retrieved sources strongly link capsule to biofilm formation and dispersion, including statements that capsule can regulate biofilm size/dispersion and can both inhibit early biofilm formation (via surface charge/steric effects) and facilitate biofilm dissociation at maturity. (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-5) However, within the retrieved corpus there is **limited explicit text** cleanly distinguishing *capsule* from *loosely associated slime layer/exopolysaccharide (EPS) matrix*; therefore, nodes/edges that refer generally to “EPS” or “biofilm matrix” should be curated as **uncertain** unless the source explicitly states “capsule/CPS” or demonstrates surface-associated capsule by genetics/assay. (ascari2025recentinsightsinto pages 1-2, gao2024bacterialcapsulesoccurrence pages 3-5)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Capsule composition and structural diversity
Capsules primarily consist of high-molecular-weight polymers, typically polysaccharides composed of repeating oligosaccharide units; composition varies between species and serotypes and includes host-mimicking monosaccharides such as sialic acid (N‑acetylneuraminic acid) in some capsules. (gao2024bacterialcapsulesoccurrence pages 3-5) This structural diversity underpins antigenic/serotype classification and can impact virulence properties such as invasiveness. (gao2024bacterialcapsulesoccurrence pages 3-5)

#### 1.2 Canonical capsule biosynthesis/assembly pathways
A recent synthesis of capsule biology recognizes **three primary capsule synthesis pathways**: **(i) Wzx/Wzy-dependent**, **(ii) ABC transporter-dependent**, and **(iii) synthase-dependent** mechanisms. (gao2024bacterialcapsulesoccurrence pages 1-3)

In the Wzx/Wzy-dependent mechanism, a lipid-linked repeat unit is flipped by Wzx and polymerized by Wzy; Wzc/Wzb phosphoregulation is described as crucial for assembly, and export across the outer membrane can occur via Wza (Gram-negative) with Wzi supporting surface organization in some species. (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87)

In the ABC transporter-dependent mechanism (often group II/III capsules), polysaccharide chains polymerize in the cytoplasm and are exported by the ABC transporter **KpsMT**, with **KpsE** and **KpsD** essential for translocation across periplasm and outer membrane. (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87)

**Visual evidence:** Gao et al. 2024 provide a schematic of these mechanisms and key proteins (Wzx/Wzy/Wza/Wzc/Wzb; KpsMT/KpsE/KpsD). (gao2024bacterialcapsulesoccurrence media dbd78d87)

#### 1.3 Functional roles (mechanistic interpretation)
Across pathogens, capsules are described as major contributors to immune evasion and host adaptation, including reduction of antimicrobial peptide and complement efficacy, suppression of phagocytosis, and promotion of intracellular survival in some contexts. (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-5)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 Environment-responsive capsule regulation (2024 review synthesis)
Gao et al. summarize multiple environmental cues affecting capsule synthesis during infection transitions, including **bloodstream-like osmolarity** and **oxygen availability**. Specifically, entry into the bloodstream exposes bacteria to “0.15 M sodium chloride osmotic pressure, triggering prioritized CPS synthesis”. (gao2024bacterialcapsulesoccurrence pages 7-8) In *S. pneumoniae*, “CPS synthesis is reduced under hyperoxic conditions compared to hypoxic growth” and is linked to CpsB phosphatase activity. (gao2024bacterialcapsulesoccurrence pages 7-8)

They also report CO2-dependent regulation: in *S. aureus*, capsule synthesis in multiple serotypes is inhibited with 1–5% CO2, and “CO2 impedes the transcription of the cap gene”. (gao2024bacterialcapsulesoccurrence pages 7-8)

#### 2.2 Regulatory modules connecting metabolism/iron homeostasis to capsule (2024)
Gao et al. describe regulatory coupling of iron sensing to capsule expression in *K. pneumoniae*, stating “Fur suppresses CPS biosynthesis by inhibiting RmpA and RcsA” and that sRNA **RyhB** can activate transcription of cps-cluster ORFs (orf1, orf16) in a manner described as independent of RmpA/RcsA. (gao2024bacterialcapsulesoccurrence pages 9-10) They also describe the Fe‑S regulator **IscR** as “positively influencing CPS biosynthesis”. (gao2024bacterialcapsulesoccurrence pages 9-10)

#### 2.3 Envelope-stress control of capsule genes via Rcs phosphorelay (2024)
A 2024 PLOS Genetics study frames the **Rcs (regulator of capsule synthesis) phosphorelay** as a conserved envelope stress response in enterobacteria that responds to multiple perturbations including antimicrobial peptides, beta-lactams, and changes in osmolarity, and “regulates the expression of genes related to capsule synthesis”. (petchiappan2024rcsfindependentmechanismsof pages 1-2)

#### 2.4 Capsule architecture vs hypermucoviscosity (primary clinical isolate study, 2024)
Liang et al. (mSystems 2024) provide primary data linking CPS content to hypermucoviscosity in an ST412-K57 *K. pneumoniae* clonal set: HMV isolates had higher CPS by uronic acid assay and poor sedimentation/string-test positivity; non-HMV isolates had ~3× higher biofilm formation and ~3-log lower organ colonization in mice. (liang2024cooccurrenceofst412 pages 2-5) This supports a causal subgraph connecting capsule abundance to HMV and to downstream infectivity/virulence phenotypes (taxon- and context-specific). (liang2024cooccurrenceofst412 pages 2-5)

### 3) Current applications and real-world implementations

#### 3.1 Capsule typing and surveillance (gene-based and enzyme-based)
A practical implementation in clinical microbiology is **capsule typing**. Yang et al. (J Bacteriol 2025) describe two main classes of capsule typing methods: immunology (serology) and molecular biology, with PCR amplification of conserved CPS synthesis genes “such as polymerase wzy, outer membrane protein wzi, and tyrosine kinase wzc” and highlight that wzi-based typing is widely used. (yang2025identificationofa pages 1-2)

A newer typing modality is **phage-derived depolymerases** as typing reagents; Yang et al. explicitly state “Phage-encoded depolymerase can be used for capsular typing of K. pneumoniae” across multiple K types. (yang2025identificationofa pages 1-2)

#### 3.2 Phage depolymerases as antivirulence/adjunct therapeutics (2024–2025)
Cheetham et al. (Essays Biochem 2024) review that *K. pneumoniae*-targeting phages encode capsule depolymerases that “selectively degrade the highly varied protective capsules”, facilitating access to the cell wall, and note these enzymes are key determinants of phage host range. (cheetham2024specificityanddiversity pages 1-2) They also report a quantitative landscape: “only 58 have been experimentally validated” depolymerases and that “at least 134 capsule synthesis loci (K-loci) have been identified”. (cheetham2024specificityanddiversity pages 1-2)

Yang et al. (J Bacteriol 2025) provide a concrete engineering/translation example: a recombinant K64-specific depolymerase (Dep37) “increased the susceptibility…to serum killing”, inhibited and degraded biofilms, and improved outcomes in a *Galleria mellonella* infection model, increasing survival “by up to 73% and 53%” when injected 5 min and 2 h after infection, respectively. (yang2025identificationofa pages 1-2)

#### 3.3 Vaccines (capsular polysaccharides as immunogens)
Capsules/CPS remain central to polysaccharide/conjugate vaccine paradigms. Gao et al. note CPS immunomodulatory properties have “garnered considerable attention in vaccine development” and cite the efficacy of polyvalent pneumococcal polysaccharide vaccines as an established example. (gao2024bacterialcapsulesoccurrence pages 9-10)

### 4) Expert opinions and authoritative analysis (selected themes)

#### 4.1 Capsule as a regulated, energetically costly virulence factor
Gao et al. emphasize capsules as “energy-consuming” virulence factors and integrate regulation across two-component systems, quorum sensing, and central metabolism to explain why capsule production is conditional on niche and metabolic state. (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10)

#### 4.2 Rcs as a canonical capsule-control hub for enterobacteria
The PLOS Genetics analysis (2024) presents the Rcs cascade as a hallmark envelope stress response with capsule synthesis among its historically defining outputs and provides updated mechanistic insight into alternative activation routes beyond the canonical RcsF sensor. (petchiappan2024rcsfindependentmechanismsof pages 1-2)

### 5) Recent statistics and data (from recent studies)

* **Validated depolymerases:** 58 experimentally validated *K. pneumoniae* CPS depolymerases, with 8 structurally characterized (as of this 2024 review). (cheetham2024specificityanddiversity pages 1-2)
* **Capsule locus diversity:** at least 134 *K. pneumoniae* K-loci identified, though fewer structures (79) reported. (cheetham2024specificityanddiversity pages 1-2)
* **Clinical AMR trend statistic (China, CHINET):** *K. pneumoniae* resistance to meropenem increased from 2.9% (2005) to 24.2% (2023), and resistance to imipenem from 3% to 22.6% over the same period. (yang2025identificationofa pages 1-2)
* **In vivo efficacy statistic (Galleria model):** Dep37 depolymerase increased survival rates “by up to 73% and 53%” with dosing 5 min and 2 h post-infection. (yang2025identificationofa pages 1-2)
* **Clinical isolate phenotype quantification:** non-HMV isolates had “3-fold higher biofilm-forming capacity” than HMV isolates in the ST412-K57 set, while organ colonization was about “three logs lower” for non-HMV isolates in mice. (liang2024cooccurrenceofst412 pages 2-5)

---

## Candidate nodes grouped by type (for capsule.yaml)

The following node list is a curation-oriented starting point; grounding is provided where the source text supports it, and label-only nodes are used where stable IDs were not directly confirmable from the retrieved sources.

| Node type | Label | Brief description | Suggested grounding CURIE(s) | Key supporting citation IDs |
|---|---|---|---|---|
| Phenotype/trait | capsule | Organized cell-associated external layer, usually polysaccharide but sometimes polypeptide, surrounding the cell and contributing to immune evasion, adhesion, and stress protection | METPO:traitmech:000063; GO:0044029 (biofilm exopolysaccharide, broader related); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-5) |
| Phenotype/trait | capsular polysaccharide (CPS) production | Biosynthesis and surface display of capsule polysaccharide repeat polymers | GO:0033692 (cellular polysaccharide biosynthetic process, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Phenotype/trait | hypermucoviscosity / hypermucoidy | Mucoid phenotype often associated with high capsule abundance or altered capsule architecture, especially in Klebsiella | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, liang2024cooccurrenceofst412 pages 2-5, liang2024cooccurrenceofst412 pages 1-2) |
| Phenotype/trait | non-capsulated / capsule-loss variant | Variant lacking or reducing capsule, often with altered biofilm and virulence traits | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 5-7, nguyen2025howklebsiellapneumoniae pages 15-16) |
| Processes/pathways | Wzx/Wzy-dependent capsule biosynthesis | Repeat-unit pathway: phosphoglycosyltransferase initiates lipid-linked repeat, Wzx flips, Wzy polymerizes, Wzc/Wzb regulate assembly/export | GO:0009103 (lipopolysaccharide biosynthetic process, related only); KEGG/MetaCyc label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, ascari2025recentinsightsinto pages 1-2, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Processes/pathways | ABC transporter-dependent capsule export | Cytoplasmic polymerization followed by export via KpsMT and trans-envelope transfer through KpsE/KpsD | GO:0015431 (ABC-type transporter activity, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Processes/pathways | synthase-dependent capsule biosynthesis | Capsule assembly via membrane synthase(s), including short-chain initiation and extension mechanisms | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Processes/pathways | capsular repeat-unit assembly | Formation of undecaprenyl-linked oligosaccharide repeat units on the cytoplasmic face of the membrane | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Processes/pathways | polysaccharide translocation across outer membrane | Export of assembled capsule polymer to the cell surface | GO:0015758 (carbohydrate transport, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Processes/pathways | capsule attachment to peptidoglycan | Covalent or organized association of capsule with cell wall, especially in Gram-positive bacteria via LCP-family proteins | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Processes/pathways | tyrosine-phosphoregulatory control of capsule assembly | Regulation of capsule polymerization/export by CpsBCD or Wzc/Wzb phosphoregulatory cycles | GO:0006468 (protein phosphorylation, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Processes/pathways | Rcs phosphorelay signaling | Envelope-stress-responsive regulatory cascade controlling capsule synthesis genes in enterobacteria | GO:0000160 (phosphorelay signal transduction system); label-only candidate | (petchiappan2024rcsfindependentmechanismsof pages 1-2, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Processes/pathways | quorum-sensing regulation of capsule | AI-2/Rgg-Shp/Agr-linked signaling affecting capsule gene expression and abundance | GO:0009372 (quorum sensing); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Processes/pathways | carbon catabolite regulation of capsule | Capsule modulation by central carbon metabolism, cAMP/CRP, pyruvate fate, and sugar transport | GO:0016051 (carbohydrate biosynthetic process, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 4-5) |
| Processes/pathways | iron-responsive regulation of capsule | Fur/RyhB/IscR-linked regulation coupling iron availability to capsule synthesis | GO:0006879 (cellular iron ion homeostasis, broad); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Genes/proteins/complexes | Wzx flippase | Membrane flippase that translocates lipid-linked repeat units across the inner membrane | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, ascari2025recentinsightsinto pages 1-2, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | Wzy polymerase | Polymerase that links repeat units into growing capsule chains in Wzx/Wzy pathway | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, ascari2025recentinsightsinto pages 1-2, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | Wzc tyrosine autokinase / PCP | Polysaccharide copolymerase/tyrosine kinase involved in capsule assembly and export control | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, liang2024cooccurrenceofst412 pages 1-2, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | Wzb phosphotyrosine phosphatase | Dephosphorylates Wzc to regulate capsule assembly cycle | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | Wza outer-membrane export protein | Outer-membrane polysaccharide export protein for Wzx/Wzy-dependent capsules | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | Wzi surface organizer | Surface-associated factor helping organize/exported polymer into capsule structures in some Gram-negative bacteria | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-3) |
| Genes/proteins/complexes | KpsM/KpsT ABC transporter complex | ATP-binding cassette exporter moving capsule polymer across the inner membrane | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | KpsE | Periplasmic/trans-envelope factor required for ABC-dependent capsule export | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | KpsD | Outer-membrane/periplasmic component required for ABC-dependent capsule translocation | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Genes/proteins/complexes | CpsE / WchA | Initial glucose-1-phosphotransferase or related initiating transferase in pneumococcal capsule assembly | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Genes/proteins/complexes | cpsA (LCP-family protein) | Putative ligase attaching capsule to peptidoglycan in cocci | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | cpsB phosphatase | Phosphatase in CpsBCD regulatory system affecting capsule polymerization and oxygen-responsive control | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Genes/proteins/complexes | cpsC | Membrane partner required for CpsD phosphorylation and capsule assembly control | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | cpsD tyrosine kinase | Tyrosine-phosphorylated regulator modulating capsule biosynthesis/polymerization | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Genes/proteins/complexes | CcpS | Regulator linking Stk1/Stp1 signaling to CpsB/CpsD and Wzx/Wzy capsule control in Streptococcus suis | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Genes/proteins/complexes | Stk1/Stp1 | Ser/Thr kinase-phosphatase system modulating CcpS and capsule synthesis | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Genes/proteins/complexes | RcsF | Outer-membrane lipoprotein sensor for Rcs phosphorelay | UniProt label-only candidate | (petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Genes/proteins/complexes | IgaA | Inner-membrane negative regulator of Rcs signaling | label-only candidate | (petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Genes/proteins/complexes | RcsC | Histidine kinase component of Rcs phosphorelay | label-only candidate | (petchiappan2024rcsfindependentmechanismsof pages 1-2, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Genes/proteins/complexes | RcsD | Phosphotransfer intermediate of Rcs phosphorelay | label-only candidate | (petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Genes/proteins/complexes | RcsB | Response regulator controlling capsule-related promoters | label-only candidate | (xu2024klebsiellapneumoniaecapsular pages 11-12, nguyen2025howklebsiellapneumoniae pages 16-17) |
| Genes/proteins/complexes | RcsA | Positive capsule regulator repressed by Fur in Klebsiella | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Genes/proteins/complexes | RmpA | Mucoid regulator promoting capsule expression and hypermucoviscosity in Klebsiella | label-only candidate | (nguyen2025howklebsiellapneumoniae pages 5-8, liang2024cooccurrenceofst412 pages 1-2, liang2024cooccurrenceofst412 pages 2-5) |
| Genes/proteins/complexes | RmpA2 | RmpA homolog associated with hypermucoid/hypervirulent Klebsiella regulation | label-only candidate | (nguyen2025howklebsiellapneumoniae pages 4-5, nguyen2025howklebsiellapneumoniae pages 16-17) |
| Genes/proteins/complexes | RmpC | rmp locus regulator promoting capsule gene transcription | label-only candidate | (nguyen2025howklebsiellapneumoniae pages 4-5, liang2024cooccurrenceofst412 pages 1-2, liang2024cooccurrenceofst412 pages 2-5) |
| Genes/proteins/complexes | RmpD | Small rmp locus factor driving hypermucoviscosity and affecting capsule chain architecture via Wzc | label-only candidate | (nguyen2025howklebsiellapneumoniae pages 4-5, nguyen2025howklebsiellapneumoniae pages 15-16, liang2024cooccurrenceofst412 pages 1-2) |
| Genes/proteins/complexes | WbaP | Initiating glycosyltransferase; mutation associated with non-HMV phenotype in K. pneumoniae | label-only candidate | (liang2024cooccurrenceofst412 pages 2-5) |
| Genes/proteins/complexes | WcaJ | Capsule/glycan initiating transferase; variation linked to capsule phenotypes | label-only candidate | (nguyen2025howklebsiellapneumoniae pages 15-16, xu2024klebsiellapneumoniaecapsular pages 11-12) |
| Genes/proteins/complexes | galF | CPS locus gene commonly used in Klebsiella CPS loci and controlled by RcsAB | label-only candidate | (yang2025identificationofa pages 1-2, nguyen2025howklebsiellapneumoniae pages 4-5) |
| Genes/proteins/complexes | magA / wzyK1 | K1 polymerase gene associated with Klebsiella K1 capsule polymerization | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 3-3, xu2024klebsiellapneumoniaecapsular pages 11-12) |
| Genes/proteins/complexes | Fur | Ferric uptake regulator repressing capsule regulators under iron-replete conditions | UniProt label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Genes/proteins/complexes | RyhB | Small RNA affecting capsule transcription in iron-responsive regulation | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 4-5, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Genes/proteins/complexes | IscR | Iron-sulfur cluster regulator positively influencing CPS biosynthesis | UniProt label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 4-5) |
| Genes/proteins/complexes | CRP / cAMP receptor protein | Carbon catabolite regulator influencing capsule and rcsA/rmp circuits in Klebsiella | UniProt label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 4-5) |
| Genes/proteins/complexes | FruA | AI-2-responsive PTS component influencing pneumococcal CPS synthesis | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | Agr | Quorum-sensing regulator positively regulating S. aureus CP5 | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Genes/proteins/complexes | MisR/MisS | Two-component system negatively regulating meningococcal CPS production | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | CsrR/CsrS (CovR/CovS) | GAS two-component system controlling capsule production | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | ArlR/ArlS | Staphylococcal TCS influencing capsule synthesis and antibiotic resistance | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Genes/proteins/complexes | BfmRS | Acinetobacter TCS activating K-locus transcription and capsule synthesis under antibiotic stress | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 5-7) |
| Cellular locations/structures | cell surface-associated capsule layer | Organized extracellular layer closely associated with bacterial surface | GO:0009279 (cell outer membrane, related); GO:0005618 (cell wall, related); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 3-5) |
| Cellular locations/structures | peptidoglycan / cell wall attachment site | Attachment location for some capsules in Gram-positive bacteria | GO:0009273 (peptidoglycan-based cell wall) | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Cellular locations/structures | outer membrane export channel | Outer membrane conduit used by Wza/KpsD-like export systems | GO:0019867 (outer membrane) | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Cellular locations/structures | cytoplasmic membrane lipid carrier interface | Site where undecaprenyl-linked repeat units are initiated and flipped | GO:0005886 (plasma membrane) | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence media dbd78d87) |
| Cellular locations/structures | cps locus / K locus | Genomic locus encoding capsule biosynthesis/export/regulation genes | SO:0001217 (gene cluster, candidate) | (yang2025identificationofa pages 1-2, xu2024klebsiellapneumoniaecapsular pages 11-12, liang2024cooccurrenceofst412 pages 2-5) |
| Metabolites/chemicals | undecaprenyl phosphate / undecyl isoprene phosphate | Lipid carrier for repeat-unit assembly in Wzx/Wzy pathway | CHEBI:16460 (undecaprenyl phosphate) candidate | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Metabolites/chemicals | ATP | Energy source for ABC-dependent export and kinase reactions | CHEBI:15422 | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Metabolites/chemicals | glucose | Carbon source affecting capsule regulation and composition | CHEBI:17234 | (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 8-9) |
| Metabolites/chemicals | pyruvate | Central metabolite whose fate influences capsule synthesis | CHEBI:15361 | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Metabolites/chemicals | acetyl-CoA | Central metabolite linked to restored capsule production in metabolic studies | CHEBI:15351 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Metabolites/chemicals | cAMP | Second messenger regulating CPS production via catabolite repression | CHEBI:17489 | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 4-5) |
| Metabolites/chemicals | Fe(II) / iron | Iron availability regulates capsule through Fur/IscR/RyhB systems | CHEBI:29033 | (gao2024bacterialcapsulesoccurrence pages 9-10, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Metabolites/chemicals | AI-2 | Quorum-sensing autoinducer affecting capsule synthesis | CHEBI label-only candidate | (gao2024bacterialcapsulesoccurrence pages 8-9, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Metabolites/chemicals | xylitol / xylitol-phosphate | Sugar alcohol whose uptake/phosphorylation can impair CPS production | CHEBI:16483 (xylitol) | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Metabolites/chemicals | sialic acid / N-acetylneuraminic acid | Capsule component associated with serum resistance and hypermucoviscosity in some taxa | CHEBI:60983 | (gao2024bacterialcapsulesoccurrence pages 3-5, xu2024klebsiellapneumoniaecapsular pages 11-12) |
| Metabolites/chemicals | D-glutamic acid / poly-γ-D-glutamate | Polypeptide capsule component in Bacillus anthracis-like systems | CHEBI:29985 (D-glutamate) | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Environmental/experimental factors | high osmolarity / 0.15 M NaCl | Bloodstream-like osmotic pressure that can prioritize CPS synthesis | ENVO:09200014 (saline environment, related); label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| Environmental/experimental factors | low oxygen / hypoxia | Lower oxygen associated with increased capsule synthesis in pneumococcus | ENVO:01001443 (hypoxic environment) | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| Environmental/experimental factors | hyperoxia / high oxygen | Higher oxygen reduces pneumococcal CPS synthesis via CpsB-related control | ENVO label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| Environmental/experimental factors | elevated CO2 | CO2 inhibits cap gene transcription in some Staphylococcus aureus contexts | CHEBI:16526 | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| Environmental/experimental factors | iron limitation | Environmental iron scarcity affecting capsule regulatory networks | ENVO label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 9-10) |
| Environmental/experimental factors | acidic pH | Low pH reported as an environmental factor affecting capsule synthesis | ENVO label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Environmental/experimental factors | nutrient richness / glucose availability | Nutrient state modulates CPS maintenance and carbon catabolite regulation | ENVO label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, nguyen2025howklebsiellapneumoniae pages 8-10) |
| Environmental/experimental factors | antibiotic stress | Cell envelope stressor that can induce capsule via BfmRS or Rcs-like pathways | CHEBI label-only candidate | (gao2024bacterialcapsulesoccurrence pages 7-8, petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Environmental/experimental factors | antimicrobial peptides | Envelope/host stressors that interact with capsule and activate Rcs-like responses | CHEBI label-only candidate | (gao2024bacterialcapsulesoccurrence pages 3-5, petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Assays/measurements | string test | Phenotypic assay for hypermucoviscosity / mucoidy | label-only candidate | (liang2024cooccurrenceofst412 pages 2-5) |
| Assays/measurements | uronic acid CPS quantification | Chemical quantification of extracted capsule content | label-only candidate | (liang2024cooccurrenceofst412 pages 2-5) |
| Assays/measurements | natural sedimentation assay | Measures mucoviscosity-related poor sedimentation of HMV strains | label-only candidate | (liang2024cooccurrenceofst412 pages 2-5) |
| Assays/measurements | serum killing assay | Tests capsule-linked serum resistance / complement susceptibility | label-only candidate | (yang2025identificationofa pages 1-2, liang2024cooccurrenceofst412 pages 2-5) |
| Assays/measurements | biofilm crystal violet assay | Quantifies biofilm effects associated with capsule state or depolymerase treatment | label-only candidate | (yang2025identificationofa pages 1-2, liang2024cooccurrenceofst412 pages 2-5) |
| Assays/measurements | capsule typing by wzi/wzy/wzc PCR or sequencing | Molecular typing of capsule/K-antigen loci | label-only candidate | (yang2025identificationofa pages 1-2, xu2024klebsiellapneumoniaecapsular pages 11-12) |
| Assays/measurements | Kaptive / K-locus typing | Genome-based identification of capsule synthesis loci | label-only candidate | (xu2024klebsiellapneumoniaecapsular pages 11-12, nguyen2025howklebsiellapneumoniae pages 15-16) |
| Applications/interventions | capsular polysaccharide conjugate vaccine | Real-world vaccine platform exploiting capsule as immunogen | label-only candidate | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Applications/interventions | phage capsule depolymerase | Enzymatic capsule removal to sensitize bacteria to serum/antibiotics and enable typing | label-only candidate | (cheetham2024specificityanddiversity pages 1-2, yang2025identificationofa pages 1-2) |
| Applications/interventions | recombinant depolymerase Dep37 | K64-specific depolymerase with antibiofilm and in vivo therapeutic activity | label-only candidate | (yang2025identificationofa pages 1-2) |
| Applications/interventions | capsule-targeted serotyping / capsular typing | Diagnostic use of CPS-specific genes or depolymerases to assign K types | label-only candidate | (yang2025identificationofa pages 1-2, xu2024klebsiellapneumoniaecapsular pages 11-12) |
| Applications/interventions | combination depolymerase + antibiotic therapy | Strategy combining capsule degradation with antibiotics such as kanamycin | label-only candidate | (yang2025identificationofa pages 1-2, cheetham2024specificityanddiversity pages 1-2) |


*Table: This table lists candidate nodes for a TraitMech causal graph of the microbial capsule trait, grouped by node type and linked to supporting evidence contexts. It is useful as a curation-ready starting point for selecting grounded entities to include in capsule.yaml.*

**Note on grounding:** GO/CHEBI/ENVO IDs in the node table should be treated as *candidate mappings* for TraitMech graph normalization; many capsule-specific proteins (e.g., Wzx, Wzy, Wza) are best grounded at the UniProt level per organism/strain, which will need taxon-specific curation outside this evidence-only synthesis. (gao2024bacterialcapsulesoccurrence media dbd78d87)

---

## Candidate causal edges (triples) with evidence

Edges below are presented as subject–predicate–object triples with verbatim evidence snippets, context, and uncertainty notes, suitable for direct conversion to YAML edges.

| Subject node | Predicate | Object node | Evidence snippet (verbatim short quote) | Context (organism if specified; experimental condition) | Strength/uncertainty notes | Reference (DOI, year, URL if present) | Citation ID |
|---|---|---|---|---|---|---|---|
| Wzx flippase | flips | lipid-linked capsule repeat unit | “the complete repeat unit is turned outward by the Wzx flip enzyme” | General capsule biosynthesis; Wzx/Wzy-dependent pathway | Strong review-level mechanistic statement; broad, not taxon-specific | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Wzy polymerase | polymerizes | capsule repeat units into growing polymer | “the Wzy polymerase attaches the growing polymer chain to the newly formed repeat unit” | General capsule biosynthesis; Wzx/Wzy-dependent pathway | Strong review-level mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Wzb phosphatase cycle | required_for | Wzc-regulated capsule assembly | “The phosphorylation cycle of Wzc, catalyzed by Wzb, is a crucial step.” | General capsule biosynthesis; Wzx/Wzy-dependent pathway | Strong but somewhat pathway-summary wording | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Wza | exports | capsule polymer across outer membrane | “The polymer translocates across the outer membrane via Wza” | Gram-negative bacteria; Wzx/Wzy-dependent pathway | Strong pathway figure/text support | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| Wzi | enables | surface-associated capsule organization | “Wzi assists in organizing the translocated polymer into surface-associated capsule structures” | Gram-negative bacteria; some prototype and other species | Moderate; explicitly limited to some species | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| KpsMT ABC transporter | exports | polysaccharide chains across inner membrane | “the ABC transporter (KpsMT) plays a pivotal role in exporting these chains” | Gram-negative bacteria; ABC transporter-dependent pathway | Strong review-level mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| KpsE | required_for | translocation of assembled capsule chains | “KpsE and KpsD are essential for translocating the assembled chains across the periplasm and outer membrane” | Gram-negative bacteria; ABC transporter-dependent pathway | Strong review-level mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| KpsD | required_for | translocation of assembled capsule chains | “KpsE and KpsD are essential for translocating the assembled chains across the periplasm and outer membrane” | Gram-negative bacteria; ABC transporter-dependent pathway | Strong review-level mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 1-3) |
| cpsA (LCP family) | enables | capsule attachment to peptidoglycan | “The cpsA gene encodes LytR-Cps2A-Psr (LCP) protein, which is believed to conjugate CPS to peptidoglycan (PG)” | Cocci; cps locus organization | Moderate; “believed to” indicates some uncertainty | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| CpsC | activates | CpsD tyrosine phosphorylation | “CpsC is essential for CpsD’s tyrosine phosphorylation.” | Cocci; tyrosine phosphoregulatory system | Strong direct mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| CpsD self-phosphorylation | decreases | capsule production | “the resulting tyrosine phosphorylated CpsD (CpsD-p) dissociates from CpsC, reducing CPS production” | Cocci; CpsBCD system | Strong direct mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| CpsB | activates | capsule biosynthesis/polymerization | “CpsB assists in CpsD-p dephosphorylation, facilitating its interaction with CpsC, leading to an accelerated rate of CPS biosynthesis/polymerization” | Cocci; CpsBCD system | Strong direct mechanistic statement | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 8-9) |
| Stk1/Stp1 | phosphorylates | CcpS | “Stk1/Stp1 specially mediates Thr-phosphorylation of the CcpS protein.” | Streptococcus suis; linkage of Ser/Thr signaling to Wzx-Wzy pathway | Strong but taxon-specific | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| non-phosphorylated CcpS | represses | CpsB-catalyzed dephosphorylation of CpsD-P | “Non-phosphorylated CcpS can inhibit CpsB-catalyzed dephosphorylation of CpsD-P” | Streptococcus suis; in vivo | Strong but taxon-specific | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| 0.15 M sodium chloride osmotic pressure | increases | capsule synthesis | “they are exposed to a 0.15 M sodium chloride osmotic pressure, triggering prioritized CPS synthesis” | Pathogenic bacteria entering bloodstream | Moderate; environment-response statement, broad not universal | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| hyperoxic conditions | decreases | capsule synthesis | “In S. pneumoniae, CPS synthesis is reduced under hyperoxic conditions compared to hypoxic growth” | Streptococcus pneumoniae; oxygen comparison | Strong but taxon-specific | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| CO2 | represses | cap gene transcription | “CO2 impedes the transcription of the cap gene” | Staphylococcus aureus; CO2-supplemented environments | Strong but taxon-specific | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 7-8) |
| Fur | represses | RmpA | “In K. pneumoniae, Fur suppresses CPS biosynthesis by inhibiting RmpA and RcsA.” | Klebsiella pneumoniae; iron-responsive regulation | Strong review statement; regulator may be strain-context dependent | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Fur | represses | RcsA | “In K. pneumoniae, Fur suppresses CPS biosynthesis by inhibiting RmpA and RcsA.” | Klebsiella pneumoniae; iron-responsive regulation | Strong review statement; regulator may be strain-context dependent | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| RyhB | activates | orf1 and orf16 in cps cluster | “sRNA RyhB activates the transcription of orf1 and orf16” | Klebsiella pneumoniae; iron-responsive regulation | Moderate; downstream effect on capsule inferred through cps locus context | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| IscR | activates | capsule biosynthesis | “positively influencing CPS biosynthesis” | Klebsiella pneumoniae; Fe-S/iron-responsive regulation | Moderate; mechanism summarized rather than experimentally detailed here | 10.1038/s41522-024-00497-6 (2024), https://doi.org/10.1038/s41522-024-00497-6 | (gao2024bacterialcapsulesoccurrence pages 9-10) |
| Rcs phosphorelay | responds_to | antimicrobial peptides, beta-lactams, osmotic shock | “The Rcs pathway has been shown to be activated in response to beta-lactams, antimicrobial peptides, osmotic shock” | Enterobacteria; envelope stress response | Strong pathway-level statement; capsule effect indirect through regulon | 10.1371/journal.pgen.1011408 (2024), https://doi.org/10.1371/journal.pgen.1011408 | (petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| Rcs phosphorelay | activates | genes related to capsule synthesis | “The Rcs phosphorelay signaling cascade regulates the expression of genes related to capsule synthesis” | Enterobacteria | Strong direct pathway-function statement | 10.1371/journal.pgen.1011408 (2024), https://doi.org/10.1371/journal.pgen.1011408 | (petchiappan2024rcsfindependentmechanismsof pages 1-2) |
| RmpA deletion | decreases | capsule amount | “deletion of rmpA resulted in reduced amount of capsule” | Klebsiella pneumoniae; hypermucoviscosity context | Strong primary-study-supported relation in K. pneumoniae | 10.1128/msystems.00262-24 (2024), https://doi.org/10.1128/msystems.00262-24 | (liang2024cooccurrenceofst412 pages 1-2) |
| RmpD | binds | Wzc | “RmpD binds Wzc” | Klebsiella pneumoniae; hypermucoviscosity regulation | Strong but taxon-specific; mechanism from summarized primary literature | 10.1128/msystems.00262-24 (2024), https://doi.org/10.1128/msystems.00262-24 | (liang2024cooccurrenceofst412 pages 1-2) |
| RmpD | increases | capsule chain length / hypermucoviscosity-associated architecture | “altering Wzc-mediated CPS synthesis to yield longer, more uniform polysaccharide chains likely important for HMV” | Klebsiella pneumoniae | Moderate; “likely important” indicates mechanistic inference | 10.1128/msystems.00262-24 (2024), https://doi.org/10.1128/msystems.00262-24 | (liang2024cooccurrenceofst412 pages 1-2) |
| Dep37 depolymerase | degrades | K64 capsular polysaccharide | “The expressed and purified depolymerase Dep37 cleaved only ST11 K64 CRKP” | ST11 K64 carbapenem-resistant Klebsiella pneumoniae | Strong primary experimental evidence; narrow serotype specificity | 10.1128/jb.00387-24 (2025), https://doi.org/10.1128/jb.00387-24 | (yang2025identificationofa pages 1-2) |
| Dep37 depolymerase | increases | susceptibility to serum killing | “Dep37 increased the susceptibility of K. pneumoniae B1 to serum killing” | Klebsiella pneumoniae B1; in vitro serum assay | Strong primary experimental evidence | 10.1128/jb.00387-24 (2025), https://doi.org/10.1128/jb.00387-24 | (yang2025identificationofa pages 1-2) |
| Dep37 depolymerase | decreases | biofilm formation | “inhibited CRKP biofilm formation, and degraded mature biofilms” | ST11 K64 CRKP; in vitro biofilm assays | Strong primary experimental evidence | 10.1128/jb.00387-24 (2025), https://doi.org/10.1128/jb.00387-24 | (yang2025identificationofa pages 1-2) |


*Table: This table lists curation-ready, evidence-backed causal edges for the microbial capsule trait, emphasizing biosynthesis, regulation, environmental control, and capsule-targeting interventions. It is useful for translating literature evidence into TraitMech graph triples with provenance and uncertainty notes.*

---

## Warnings / claims not yet ready for curation into TraitMech

1. **Capsule vs slime layer/EPS boundary:** while capsule is repeatedly linked to biofilm phenotypes, the retrieved sources do not provide a crisp definitional boundary between an organized “capsule” and a loosely associated slime/EPS layer; avoid curating edges that treat all “EPS” as “capsule” unless explicitly stated or genetically demonstrated as CPS. (gao2024bacterialcapsulesoccurrence pages 3-5, ascari2025recentinsightsinto pages 1-2)
2. **Taxon specificity:** several regulation edges (e.g., CO2→cap repression; oxygen→CpsB-mediated effects; Fur/RyhB/IscR regulation of CPS) are supported in particular organisms/contexts and should be marked **taxon-specific** (and sometimes condition-specific). (gao2024bacterialcapsulesoccurrence pages 7-8, gao2024bacterialcapsulesoccurrence pages 9-10)
3. **Hypermucoviscosity vs capsule amount:** primary data show HMV correlates with higher CPS content in a clinical clone set, but other summarized literature suggests hypermucoviscosity can reflect capsule architecture and regulator effects (e.g., rmp locus, Wzc interactions). Curate HMV-related edges as **phenotype-specific** and avoid assuming HMV ≡ capsule abundance in all taxa. (liang2024cooccurrenceofst412 pages 2-5, liang2024cooccurrenceofst412 pages 1-2)

---

## DOI-first bibliography (publication date and URL)

* Gao S, Jin W, Quan Y, et al. **Bacterial capsules: Occurrence, mechanism, and function.** *NPJ Biofilms and Microbiomes.* **Mar 2024**. DOI: **10.1038/s41522-024-00497-6**. URL: https://doi.org/10.1038/s41522-024-00497-6 (gao2024bacterialcapsulesoccurrence pages 1-3)
* Petchiappan A, Majdalani N, Wall E, Gottesman S. **RcsF-independent mechanisms of signaling within the Rcs phosphorelay.** *PLOS Genetics.* **Dec 26, 2024**. DOI: **10.1371/journal.pgen.1011408**. URL: https://doi.org/10.1371/journal.pgen.1011408 (petchiappan2024rcsfindependentmechanismsof pages 1-2)
* Liang Q, Chen N, Wang W, et al. **Co-occurrence of ST412 Klebsiella pneumoniae isolates with hypermucoviscous and non-mucoviscous phenotypes in a short-term hospitalized patient.** *mSystems.* **Jul 2024**. DOI: **10.1128/msystems.00262-24**. URL: https://doi.org/10.1128/msystems.00262-24 (liang2024cooccurrenceofst412 pages 2-5)
* Cheetham MJ, Huo Y, Stroyakovski M, et al. **Specificity and diversity of Klebsiella pneumoniae phage-encoded capsule depolymerases.** *Essays in Biochemistry.* **Dec 17, 2024**. DOI: **10.1042/EBC20240015**. URL: https://doi.org/10.1042/EBC20240015 (cheetham2024specificityanddiversity pages 1-2)
* Yang P, Shan B, Hu X, et al. **Identification of a novel phage depolymerase against ST11 K64 carbapenem-resistant Klebsiella pneumoniae and its therapeutic potential.** *Journal of Bacteriology.* **Published Mar 26, 2025**. DOI: **10.1128/jb.00387-24**. URL: https://doi.org/10.1128/jb.00387-24 (yang2025identificationofa pages 1-2)
* Xu L, Li J, Wu W, Wu X, Ren J. **Klebsiella pneumoniae capsular polysaccharide: Mechanism in regulation of synthesis, virulence, and pathogenicity.** *Virulence.* **Dec 2024**. DOI: **10.1080/21505594.2024.2439509**. URL: https://doi.org/10.1080/21505594.2024.2439509 (xu2024klebsiellapneumoniaecapsular pages 11-12)
* Ascari A, Morona R. **Recent insights into Wzy polymerases and lipopolysaccharide O-antigen biosynthesis.** *Journal of Bacteriology.* **Apr 2025**. DOI: **10.1128/jb.00417-24**. URL: https://doi.org/10.1128/jb.00417-24 (ascari2025recentinsightsinto pages 1-2)


References

1. (gao2024bacterialcapsulesoccurrence pages 1-3): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

2. (gao2024bacterialcapsulesoccurrence pages 3-5): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

3. (ascari2025recentinsightsinto pages 1-2): Alice Ascari and Renato Morona. Recent insights into wzy polymerases and lipopolysaccharide o-antigen biosynthesis. Journal of Bacteriology, Apr 2025. URL: https://doi.org/10.1128/jb.00417-24, doi:10.1128/jb.00417-24. This article has 13 citations and is from a peer-reviewed journal.

4. (gao2024bacterialcapsulesoccurrence media dbd78d87): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

5. (gao2024bacterialcapsulesoccurrence pages 7-8): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

6. (gao2024bacterialcapsulesoccurrence pages 9-10): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

7. (petchiappan2024rcsfindependentmechanismsof pages 1-2): Anushya Petchiappan, Nadim Majdalani, Erin Wall, and Susan Gottesman. Rcsf-independent mechanisms of signaling within the rcs phosphorelay. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.08.29.610257, doi:10.1101/2024.08.29.610257. This article has 6 citations.

8. (liang2024cooccurrenceofst412 pages 2-5): Qinghua Liang, Nan Chen, Wei Wang, Biying Zhang, Jinjing Luo, Ying Zhong, Feiyang Zhang, Zhikun Zhang, Alberto J. Martín–Rodríguez, Ying Wang, Li Xiang, Xia Xiong, Renjing Hu, and Yingshun Zhou. Co-occurrence of st412 <i>klebsiella pneumoniae</i> isolates with hypermucoviscous and non-mucoviscous phenotypes in a short-term hospitalized patient. mSystems, Jul 2024. URL: https://doi.org/10.1128/msystems.00262-24, doi:10.1128/msystems.00262-24. This article has 5 citations and is from a peer-reviewed journal.

9. (yang2025identificationofa pages 1-2): Peini Yang, Bin Shan, Xing Hu, Li Xue, Guibo Song, Pingan He, and Xu Yang. Identification of a novel phage depolymerase against st11 k64 carbapenem-resistant <i>klebsiella pneumoniae</i> and its therapeutic potential. Journal of Bacteriology, Apr 2025. URL: https://doi.org/10.1128/jb.00387-24, doi:10.1128/jb.00387-24. This article has 13 citations and is from a peer-reviewed journal.

10. (cheetham2024specificityanddiversity pages 1-2): Max J. Cheetham, Yunlong Huo, Maria Stroyakovski, Li Cheng, Daniel Wan, Anne Dell, and Joanne M. Santini. Specificity and diversity of klebsiella pneumoniae phage-encoded capsule depolymerases. Essays in Biochemistry, 68:661-677, Dec 2024. URL: https://doi.org/10.1042/ebc20240015, doi:10.1042/ebc20240015. This article has 28 citations and is from a peer-reviewed journal.

11. (gao2024bacterialcapsulesoccurrence pages 8-9): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

12. (liang2024cooccurrenceofst412 pages 1-2): Qinghua Liang, Nan Chen, Wei Wang, Biying Zhang, Jinjing Luo, Ying Zhong, Feiyang Zhang, Zhikun Zhang, Alberto J. Martín–Rodríguez, Ying Wang, Li Xiang, Xia Xiong, Renjing Hu, and Yingshun Zhou. Co-occurrence of st412 <i>klebsiella pneumoniae</i> isolates with hypermucoviscous and non-mucoviscous phenotypes in a short-term hospitalized patient. mSystems, Jul 2024. URL: https://doi.org/10.1128/msystems.00262-24, doi:10.1128/msystems.00262-24. This article has 5 citations and is from a peer-reviewed journal.

13. (gao2024bacterialcapsulesoccurrence pages 5-7): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

14. (nguyen2025howklebsiellapneumoniae pages 15-16): To Nguyen Thi Nguyen, Gareth Howells, and Francesca L. Short. How klebsiella pneumoniae controls its virulence. Sep 2025. URL: https://doi.org/10.1371/journal.ppat.1013499, doi:10.1371/journal.ppat.1013499. This article has 15 citations and is from a highest quality peer-reviewed journal.

15. (gao2024bacterialcapsulesoccurrence pages 3-3): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, Li Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. NPJ Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 112 citations and is from a peer-reviewed journal.

16. (nguyen2025howklebsiellapneumoniae pages 8-10): To Nguyen Thi Nguyen, Gareth Howells, and Francesca L. Short. How klebsiella pneumoniae controls its virulence. Sep 2025. URL: https://doi.org/10.1371/journal.ppat.1013499, doi:10.1371/journal.ppat.1013499. This article has 15 citations and is from a highest quality peer-reviewed journal.

17. (nguyen2025howklebsiellapneumoniae pages 4-5): To Nguyen Thi Nguyen, Gareth Howells, and Francesca L. Short. How klebsiella pneumoniae controls its virulence. Sep 2025. URL: https://doi.org/10.1371/journal.ppat.1013499, doi:10.1371/journal.ppat.1013499. This article has 15 citations and is from a highest quality peer-reviewed journal.

18. (xu2024klebsiellapneumoniaecapsular pages 11-12): Li Xu, Jiayang Li, Wenqi Wu, Xiuwen Wu, and Jianan Ren. <i>klebsiella pneumoniae</i> capsular polysaccharide: mechanism in regulation of synthesis, virulence, and pathogenicity. Virulence, Dec 2024. URL: https://doi.org/10.1080/21505594.2024.2439509, doi:10.1080/21505594.2024.2439509. This article has 92 citations and is from a peer-reviewed journal.

19. (nguyen2025howklebsiellapneumoniae pages 16-17): To Nguyen Thi Nguyen, Gareth Howells, and Francesca L. Short. How klebsiella pneumoniae controls its virulence. Sep 2025. URL: https://doi.org/10.1371/journal.ppat.1013499, doi:10.1371/journal.ppat.1013499. This article has 15 citations and is from a highest quality peer-reviewed journal.

20. (nguyen2025howklebsiellapneumoniae pages 5-8): To Nguyen Thi Nguyen, Gareth Howells, and Francesca L. Short. How klebsiella pneumoniae controls its virulence. Sep 2025. URL: https://doi.org/10.1371/journal.ppat.1013499, doi:10.1371/journal.ppat.1013499. This article has 15 citations and is from a highest quality peer-reviewed journal.