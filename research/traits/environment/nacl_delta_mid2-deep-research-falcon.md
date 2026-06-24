---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:07:10.583347'
end_time: '2026-06-17T23:22:45.238619'
duration_seconds: 934.66
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta mid2
  trait_identifier: METPO:1000481
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately\
    \ 3\u20138% (w/v), characteristic of organisms with broad salinity tolerance."
  parent_traits: METPO:1000335
  synonyms: Nad_3_8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline
    phenotype.)'
  causal_graph_summary: 'nacl_delta_mid2_broad_breadth: 3 nodes, 2 edges'
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
- **Trait label:** NaCl delta mid2
- **METPO identifier:** METPO:1000481
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 3–8% (w/v), characteristic of organisms with broad salinity tolerance.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_3_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline phenotype.)
- **Existing causal graph summary:** nacl_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid2.yaml`.

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
- **Trait label:** NaCl delta mid2
- **METPO identifier:** METPO:1000481
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 3–8% (w/v), characteristic of organisms with broad salinity tolerance.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_3_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline phenotype.)
- **Existing causal graph summary:** nacl_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid2.yaml`.

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


# Curation-Focused Research Report: NaCl delta mid2 (METPO:1000481)

## 1) Scope summary (what the trait represents)
**NaCl delta mid2** denotes a *growth-supporting salinity breadth* in which an organism can grow across approximately **3–8% (w/v) NaCl** (synonym: *Nad_3_8*). This breadth straddles the classic boundary between **slight halophiles** and **moderate halophiles**, implying a broadly salt-tolerant/euryhaline growth phenotype rather than a narrow optimum.

### Distinguishing from nearby traits (boundary cases)
* **Slight vs moderate halophile boundary:** A commonly used classification defines **slight halophiles** as growing optimally at **0.2–0.85 M (2–5% NaCl)**, **moderate halophiles** at **0.85–3.4 M (5–20% NaCl)**, and **extreme halophiles** at **3.4–5.1 M (20–30% NaCl)**. Under this scheme, a 3–8% breadth crosses the 5% boundary (nesrine2020phylogeneticcharacterizationand pages 1-2).
* **Halotolerant vs halophilic:** A reviewed definition emphasizes that **halotolerant** organisms can remain viable/grow with or without high salinity (salt not required for optimal growth), whereas halophiles require elevated salt for optimal growth (lach2023charakterystykabioróżnorodnościi pages 41-42). NaCl delta mid2 should therefore not be conflated with “halotolerant” unless the organism’s optimum is clearly at low/zero NaCl.
* **Assay dependence:** Growth range depends strongly on medium and temperature. For example, *Vibrio diabolicus* growth at 37°C is best at **3–4% NaCl**, while growth is **abolished at 7% NaCl** (and growth at 0% NaCl depends on lower temperature) (lichty2024compatiblesolutesare pages 74-78). This supports treating NaCl delta mid2 as an assay-observed breadth (not an intrinsic fixed property).

## 2) Current understanding: mechanistic basis of broad NaCl growth breadth (~3–8%)
Broad NaCl breadth is generally enabled by coupling **(i) ionic homeostasis** (rapid K+ and Na+ management) with **(ii) salt-out osmoprotection** (accumulating/transporting compatible solutes) and, in some taxa, **(iii) extracellular protection** (e.g., EPS matrices).

### 2.1 Compatible-solute (“salt-out”) strategies
Evidence across taxa supports **biosynthesis and/or uptake of compatible solutes (osmolytes)** as a central mechanism for tolerating higher NaCl while maintaining macromolecular function (rain‐franco2022nichebreadthaffects pages 8-9). In halophilic bacteria, compatible solutes include amino acids/derivatives such as **ectoine**, **glycine betaine**, **proline**, **glutamate**, and others (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2).

### 2.2 Ion homeostasis and second-messenger regulation (c-di-AMP)
A 2024 domain-leading review argues that **cyclic di-AMP (c-di-AMP) is a master regulator of bacterial cell volume** and that most known c-di-AMP targets are tied to **cell volume control** via ion/solute transport (foster2024bacterialcellvolume pages 8-10). In particular, c-di-AMP regulation links:
* **K+ uptake systems** (e.g., KimA, Kup, Ktr, Kdp) and associated regulation,
* **Antiporters/exporters** affecting cation balance,
* **Compatible-solute transporters** (e.g., Opu systems in Gram-positives),
into a coordinated osmoadaptation network (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369).

## 3) Recent developments and latest research (prioritizing 2023–2024)
### 3.1 Direct causal evidence: osmolyte rewiring expands NaCl tolerance into the 3–8% window (2024)
Two 2024 *Applied and Environmental Microbiology* studies in *Halomonas elongata* provide unusually direct causal evidence that **changing compatible-solute composition** can shift the upper NaCl growth limit into the **6–8% range**.

* **Ectoine pathway deletion causes salt sensitivity:** An ectoine-deficient mutant “only grows well… up to 3% NaCl” (zou2024metabolicengineeringof pages 1-2) and in another experiment “could not grow… more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2). This directly ties ectoine biosynthesis capacity to growth beyond ~3–4%.
* **Installing proline as a major osmolyte restores/extends growth:** An engineered strain “thrived… in 8% NaCl” while accumulating **proline to 353.1 ± 40.5 µmol/g cell fresh weight** (khanh2024metabolicpathwayengineering pages 1-2). Another analysis reported quantitative tolerance shifts (IC50/IC25), with an engineered strain reaching **IC50 6.1% NaCl and IC25 7.2% NaCl** (khanh2024metabolicpathwayengineering pages 6-9). These numbers fall squarely within NaCl delta mid2’s breadth.
* **Engineering glutamate→GABA improves tolerance via pH homeostasis:** A 2024 study engineered salt-inducible glutamate decarboxylase to convert glutamate to **GABA**, reporting that the resulting strain accumulated **GABA to 176.94 µmol/g cell dry weight at 7% NaCl**, and exhibited higher salt tolerance than a glutamate-overproducing precursor strain (zou2024metabolicengineeringof pages 1-2). The authors explicitly link the decarboxylation to **restoring pH homeostasis** (zou2024metabolicengineeringof pages 1-2).

### 3.2 Quantitative physiology illustrating boundary behavior near 7% NaCl (2024)
A 2024 dissertation measured *Vibrio diabolicus* growth across NaCl concentrations, showing:
* best growth at **3–4% NaCl (37°C)** and
* **no growth at 7% NaCl (37°C)**,
highlighting that the upper end of NaCl delta mid2 (near ~7–8%) can be a sharp boundary for some taxa and conditions (lichty2024compatiblesolutesare pages 74-78).

### 3.3 Consolidated mechanistic “expert” synthesis (2024)
The 2024 MMBR review provides quantitative parameters supporting mechanistic curation nodes (e.g., K+ uptake affinities; c-di-AMP binding affinities; inferred intracellular c-di-AMP ~2–5 µM) and explicitly states that c-di-AMP binding can **inhibit potassium import** (including Kup/KimA and kdp operon regulation) (foster2024bacterialcellvolume pages 8-10). This is a key current synthesis for a causal graph because it explicitly integrates transport and regulation into osmoadaptation (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369).

## 4) Current applications and real-world implementations
### 4.1 Industrial bioprocessing in saline media (cell factories)
The 2024 *Halomonas elongata* studies position broad salt tolerance as an enabling trait for **bioproduction under high salinity**, where compatible solutes become both a *stress-protection mechanism* and a *product strategy*:
* engineered strains that grow at **7–8% NaCl** while accumulating high intracellular osmolyte titers (proline or GABA) provide proof-of-concept for producing osmolytes in saline processes (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2).

### 4.2 Mechanism-guided engineering targets
The c-di-AMP-centered view implies that engineering or selecting for broad NaCl breadth should consider not only osmolyte biosynthesis, but also **K+ uptake tuning and antiporter/exchanger regulation** (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369).

## 5) Candidate entities for TraitMech causal graph (nodes)
The following artifact lists candidate nodes grouped by type with suggested ontology grounding.

| Type | Candidate node | Suggested grounding | Rationale/evidence |
|---|---|---|---|
| Phenotype/Assay | NaCl delta mid2 broad salinity breadth (~3–8% w/v NaCl growth breadth) | METPO:1000481 | Trait target; overlaps the slight/moderate halophile boundary and is exemplified by strains shifting growth from ≤3–4% to 6–8% NaCl under osmolyte rewiring (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2, nesrine2020phylogeneticcharacterizationand pages 1-2, lach2023charakterystykabioróżnorodnościi pages 41-42) |
| Phenotype/Assay | Moderate halophile / broad niche breadth along salinity gradient |  | Quantitative halophile category boundaries and broad-niche salinity transcription studies help delimit nearby traits (rain‐franco2022nichebreadthaffects pages 8-8, nesrine2020phylogeneticcharacterizationand pages 1-2, lach2023charakterystykabioróżnorodnościi pages 41-42) |
| Phenotype/Assay | Halotolerant phenotype |  | Distinguishes tolerance without salt requirement from halophily; useful boundary case for curation (schiavo2025proposalfornew pages 1-4, lach2023charakterystykabioróżnorodnościi pages 41-42, schiavo2025proposalfornew pages 4-7) |
| Environmental factor | Sodium chloride salinity | CHEBI:26710 | Central environmental variable defining the assay and salinity-stress condition (zou2024metabolicengineeringof pages 1-2, lichty2024compatiblesolutesare pages 74-78, nesrine2020phylogeneticcharacterizationand pages 1-2) |
| Environmental factor | Hyperosmotic stress / osmotic upshift | GO:0006970 | Direct stimulus for compatible-solute accumulation and K+ homeostasis responses (rain‐franco2022nichebreadthaffects pages 8-9, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Environmental factor | Osmotic downshift | GO:0006973 | Relevant counter-stimulus; included in c-di-AMP/osmoadaptation schematics and compatible-solute release logic (zou2024metabolicengineeringof pages 1-2, foster2024bacterialcellvolume media 91e74369) |
| Environmental factor | Osmolality |  | Review evidence ties osmolality to induction of Kdp expression and cell-volume regulation (foster2024bacterialcellvolume pages 8-10) |
| Biological process | Osmoadaptation / response to osmotic stress | GO:0006970 | Umbrella process supported across reviews and primary studies on compatible solutes, ion transport, and niche breadth (rain‐franco2022nichebreadthaffects pages 8-9, zou2024metabolicengineeringof pages 1-2, foster2024bacterialcellvolume pages 8-10) |
| Biological process | Compatible-solute accumulation | GO:0006970 | Core mechanism for broad NaCl tolerance; repeatedly implicated across taxa (rain‐franco2022nichebreadthaffects pages 8-9, zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2, lichty2024compatiblesolutesare pages 10-14, lichty2024compatiblesolutesare pages 74-78) |
| Biological process | Potassium ion homeostasis | GO:0055075 | Early ionic response to osmotic stress and a major c-di-AMP-regulated axis (goszcz2025bacterialosmoprotectants—away pages 5-5, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Biological process | Sodium ion homeostasis | GO:0055078 | Supported by Na+/H+ antiporters and ion-balance mechanisms under high salinity (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Biological process | pH homeostasis | GO:0006885 | GABA production from glutamate is linked to restored pH homeostasis under salt stress (zou2024metabolicengineeringof pages 1-2) |
| Biological process | Cell volume regulation | GO:0008361 | c-di-AMP review frames cell volume control as a master regulated function under osmotic change (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Biological process | Heat-shock/stress-protein response | GO:0009408 | Transcriptomic niche-breadth study identifies heat-shock proteins as adaptation-related/stress-marker features (rain‐franco2022nichebreadthaffects pages 8-9, rain‐franco2022nichebreadthaffects pages 14-14) |
| Biological process | Exopolysaccharide-mediated pericellular protection | GO:0005618 | EPS matrix can bind Na+ and retain water, supporting salt tolerance indirectly (goszcz2025bacterialosmoprotectants—away pages 5-5) |
| Pathway/module | Ectoine biosynthesis pathway |  | Strongly supported osmolyte pathway in halophiles/halotolerants; salt-induced in Halomonas (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Pathway/module | Proline biosynthesis pathway |  | Engineering and physiology data show proline can replace ectoine and expand growth to 8% NaCl (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Pathway/module | Glutamate-to-GABA shunt |  | Salt-inducible GAD-mediated conversion of glutamate to GABA improves tolerance and pH homeostasis (zou2024metabolicengineeringof pages 1-2) |
| Pathway/module | Glycine betaine biosynthesis/uptake module |  | Widely cited osmoprotectant system in marine/halotolerant bacteria (rain‐franco2022nichebreadthaffects pages 8-9, lichty2024compatiblesolutesare pages 10-14, lichty2024compatiblesolutesare pages 74-78) |
| Pathway/module | Trehalose-associated osmoprotection module |  | Included among bacterial osmoprotectants and EPS-linked sugar precursors in saline adaptation review (goszcz2025bacterialosmoprotectants—away pages 5-5) |
| Pathway/module | c-di-AMP osmotic homeostasis signaling network |  | Integrates K+ transport, compatible-solute transport, antiporters, and cell-volume control (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | EctA |  | Part of ectABC osmolyte biosynthetic operon; salt-inducible promoter usage supports mechanistic relevance (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | EctB |  | Core ectoine biosynthesis enzyme; operon loss causes salt sensitivity in Halomonas models (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | EctC |  | Core ectoine biosynthesis enzyme; operon replacement/removal reduces high-salt growth (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | ProB (γ-glutamate kinase) |  | Feedback-insensitive variants increase proline accumulation and salt tolerance (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | ProA (γ-glutamyl phosphate reductase) |  | Part of engineered proline-biosynthesis cassette supporting high-salt growth (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | ProC (pyrroline-5-carboxylate reductase) |  | Final step in proline biosynthesis used in engineered osmolyte replacement (khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | PutA (proline dehydrogenase / P5C dehydrogenase) |  | Deletion prevents proline catabolism and increases intracellular proline under salt stress (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Gene/protein/complex | Glutamate decarboxylase (GadB / GAD) |  | Engineered salt-inducible GAD increased GABA accumulation and NaCl tolerance (zou2024metabolicengineeringof pages 1-2) |
| Gene/protein/complex | Heat-shock proteins (HSPs) |  | Proposed stress/adaptation markers associated with broad niche breadth responses (rain‐franco2022nichebreadthaffects pages 8-9, rain‐franco2022nichebreadthaffects pages 14-14) |
| Gene/protein/complex | KimA |  | High-affinity K+ importer directly regulated by c-di-AMP; central osmoadaptation node (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | KdpD sensor kinase |  | c-di-AMP target and regulator of kdpFABC; senses ionic/osmotic cues (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | KdpFABC complex |  | High-affinity K+ uptake system induced by osmolality; key ionic homeostasis module (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | Ktr/Kup family proteins |  | Major K+ uptake systems under osmotic stress; regulated in c-di-AMP network (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | CpaA cation/H+ antiporter |  | c-di-AMP-binding antiporter participating in ionic homeostasis (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | Mrp antiporter complex |  | Frequently implicated multi-subunit Na+/H+ antiporter for salt tolerance; good candidate but current support here is indirect/generic (foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | BetP |  | BCCT-family compatible-solute transporter widely used for glycine betaine uptake/osmoprotection (foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | OpuA |  | ABC-compatible-solute transporter in c-di-AMP/osmoadaptation networks (foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | OpuC |  | ABC-compatible-solute transporter in c-di-AMP/osmoadaptation networks (foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | ProP |  | Compatible-solute transporter frequently linked to osmoprotection, included in schematics/genome screens (foster2024bacterialcellvolume media 91e74369) |
| Gene/protein/complex | ProU |  | ABC-type compatible-solute uptake system frequently linked to osmoprotection (foster2024bacterialcellvolume media 91e74369) |
| Metabolite/chemical | Ectoine | CHEBI:27689 | Canonical compatible solute whose loss reduces salt tolerance and whose synthesis is salt-induced (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2, lichty2024compatiblesolutesare pages 74-78) |
| Metabolite/chemical | Hydroxyectoine | CHEBI:58173 | Included among known halophilic osmolytes/compatible solutes in reviewed systems (khanh2024metabolicpathwayengineering pages 1-2, lichty2024compatiblesolutesare pages 10-14) |
| Metabolite/chemical | Glycine betaine | CHEBI:17750 | Widely effective osmoprotectant accumulated or imported under salinity stress (rain‐franco2022nichebreadthaffects pages 8-9, lichty2024compatiblesolutesare pages 10-14, lichty2024compatiblesolutesare pages 74-78) |
| Metabolite/chemical | L-proline | CHEBI:26271 | Demonstrated substitute osmolyte that restores/extends growth to 8% NaCl in engineered Halomonas (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2) |
| Metabolite/chemical | L-glutamate | CHEBI:29985 | Osmolyte/intermediate whose overproduction partially restores salt tolerance but has pH costs (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Metabolite/chemical | GABA (γ-aminobutyric acid) | CHEBI:16865 | Accumulation improves salt tolerance and pH homeostasis in engineered Halomonas (zou2024metabolicengineeringof pages 1-2) |
| Metabolite/chemical | Trehalose | CHEBI:16551 | Common osmoprotectant candidate discussed in saline adaptation review (goszcz2025bacterialosmoprotectants—away pages 5-5) |
| Metabolite/chemical | Potassium ion | CHEBI:29103 | Central counterion in osmoadaptation and c-di-AMP-regulated transport (goszcz2025bacterialosmoprotectants—away pages 5-5, foster2024bacterialcellvolume pages 8-10) |
| Metabolite/chemical | Sodium ion | CHEBI:29101 | Principal toxic/osmotic ion whose balance is managed by antiporters and EPS interactions (goszcz2025bacterialosmoprotectants—away pages 5-5, foster2024bacterialcellvolume pages 8-10) |
| Metabolite/chemical | Cyclic di-AMP | CHEBI:194755 | Master second messenger coordinating ion and osmolyte transport under osmotic stress (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Metabolite/chemical | Exopolysaccharide matrix (EPS) |  | Candidate extracellular protective matrix that binds Na+ and improves water retention (goszcz2025bacterialosmoprotectants—away pages 5-5) |
| Transport system | BCCT-family compatible-solute transporter |  | Broad transporter class for betaine/carnitine/choline-type osmolytes in marine and Gram-positive bacteria (lichty2024compatiblesolutesare pages 10-14, foster2024bacterialcellvolume media 91e74369) |
| Transport system | ABC-type compatible-solute uptake transporter |  | Includes OpuA/OpuC/ProU-type systems central to osmoprotection (foster2024bacterialcellvolume media 91e74369) |
| Transport system | High-affinity potassium uptake system (Kdp) |  | Quantitatively characterized and osmolality responsive under c-di-AMP control (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Transport system | Ktr/Kup potassium uptake system |  | Major osmoadaptive K+ influx route, c-di-AMP connected (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Transport system | Na+/H+ antiporter system | GO:0015385 | Generic node for sodium extrusion/proton coupling; useful umbrella for CpaA/Mrp-like functions (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) |
| Transport system | Mechanosensitive channel-mediated osmolyte release |  | Relevant to osmotic downshift and cell-volume recovery, though less directly evidenced for the trait than uptake systems (foster2024bacterialcellvolume media 91e74369) |


*Table: This table lists candidate causal-graph nodes for the NaCl delta mid2 trait, organized by entity type and grounded where possible to stable ontologies. It highlights the strongest currently supported osmoadaptation mechanisms for broad growth across roughly 3–8% NaCl, with citations to the gathered evidence contexts.*

## 6) Evidence-backed candidate causal edges (triples) for curation
The following artifact compiles proposed edges with references, direct snippets, and uncertainty notes.

| Edge (subject–predicate–object) | Evidence source | Context ID | Supporting snippet/quote | Notes on strength/uncertainty | Suggested grounding for subject/object |
|---|---|---|---|---|---|
| ectABC loss — reduces growth above → 3–4% NaCl | Zou et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01905-23 | (zou2024metabolicengineeringof pages 1-2) | “an ectoine-deficient KA1 mutant ‘only grows well in minimal medium containing up to 3% NaCl’” | Strong experimental evidence in *Halomonas elongata* mutant; taxon-specific and assay-specific, so not universally generalizable without caution. | subject: ectABC operon (label-only); object: sodium chloride (CHEBI:26710) |
| ectABC loss — reduces growth above → 4% NaCl | Khanh et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01195-24 | (khanh2024metabolicpathwayengineering pages 1-2) | “an ectoine-deficient KA1 ‘could not grow in minimal media containing more than 4% NaCl’” | Strong and directly quantitative; same mechanistic direction as above, but still primarily demonstrated in engineered *H. elongata*. | subject: ectABC operon (label-only); object: sodium chloride (CHEBI:26710) |
| L-proline accumulation — enables growth in → 8% NaCl | Khanh et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01195-24 | (khanh2024metabolicpathwayengineering pages 1-2) | “H. elongata HN6 ‘thrived in the medium containing 8% NaCl’ and accumulated Pro to ‘353.1 ± 40.5 µmol/g cell fresh weight.’” | Strong causal support from metabolic engineering; species/strain specific but directly relevant to the target 3–8% breadth. | subject: L-proline (CHEBI:26271); object: NaCl tolerance / growth at 8% NaCl (label-only) |
| proline biosynthesis pathway — increases → NaCl tolerance (IC50 6.1%, IC25 7.2%) | Khanh et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01195-24 | (khanh2024metabolicpathwayengineering pages 6-9) | “HN6 IC50 6.1% (IC25 7.2%)” | Strong quantitative support for improved tolerance within the trait window; still engineered and strain-specific. | subject: proline biosynthesis pathway (label-only); object: NaCl tolerance (label-only) |
| putA deletion — increases intracellular → L-proline accumulation | Khanh et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01195-24 | (khanh2024metabolicpathwayengineering pages 6-9) | “putA deletion plus feedback-insensitive γ-GK mutations produced the greatest salinity tolerance” and “very high Pro levels” | Good causal support, though the excerpt bundles putA deletion with engineered proB variants; curate as partly composite unless full paper confirms separability. | subject: PutA (label-only); object: L-proline (CHEBI:26271) |
| increased intracellular L-proline — increases → NaCl tolerance | Khanh et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01195-24 | (khanh2024metabolicpathwayengineering pages 6-9) | “The text links PutA dual activity to intracellular Pro concentrations and shows that putA deletion plus feedback-insensitive γ-GK mutations produced the greatest salinity tolerance.” | Moderate-to-strong, but mechanistically composite; best curated with uncertainty note. | subject: L-proline (CHEBI:26271); object: NaCl tolerance (label-only) |
| glutamate decarboxylase activity — increases → GABA accumulation | Zou et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01905-23 | (zou2024metabolicengineeringof pages 1-2) | “introduced an engineered salt-inducible GAD (HopgadBmut) to convert Glu to GABA” | Strong mechanistic evidence in engineered *H. elongata*. | subject: glutamate decarboxylase / GadB (label-only); object: GABA (CHEBI:16865) |
| GABA accumulation — improves → pH homeostasis | Zou et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01905-23 | (zou2024metabolicengineeringof pages 1-2) | “convert Glu to γ-aminobutyric acid (GABA) by a Glu decarboxylase (GAD) could restore cellular pH homeostasis” | Strong within-study mechanistic claim; may be context-dependent. | subject: GABA (CHEBI:16865); object: pH homeostasis (GO:0006885) |
| improved pH homeostasis — increases → NaCl tolerance up to 7% | Zou et al., *Applied and Environmental Microbiology* (2024), DOI: https://doi.org/10.1128/aem.01905-23 | (zou2024metabolicengineeringof pages 1-2) | “the resulting H. elongata GOP-Gad strain exhibits higher salt tolerance… accumulating high concentration of GABA… in minimal medium containing 7% NaCl” | Strong but indirect chain from pH homeostasis to salt tolerance; taxon/construct specific. | subject: pH homeostasis (GO:0006885); object: NaCl tolerance / growth at 7% NaCl (label-only) |
| cyclic di-AMP binding — inhibits → K+ uptake systems | Foster et al., *Microbiology and Molecular Biology Reviews* (2024), DOI: https://doi.org/10.1128/mmbr.00181-23 | (foster2024bacterialcellvolume pages 8-10) | “Binding of c-di-AMP to transporters and riboswitches inhibits potassium import (e.g., KupA/KupB, KimA, kdp operon)” | Strong review synthesis from multiple primary studies; broad bacterial relevance but not universal across all taxa. | subject: cyclic di-AMP (CHEBI:194755); object: potassium uptake systems (KimA/KupA/KupB/Kdp; label-only) |
| cyclic di-AMP signaling — modulates → cell volume regulation / osmoadaptation | Foster et al., *Microbiology and Molecular Biology Reviews* (2024), DOI: https://doi.org/10.1128/mmbr.00181-23 | (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369) | “we argue that cyclic di-AMP is a master regulator of cell volume” | Strong high-level synthesis; suitable as a broad mechanistic edge. | subject: cyclic di-AMP signaling network (label-only); object: cell volume regulation (GO:0008361) |
| osmolality — upregulates → kdpFABC expression | Foster et al., *Microbiology and Molecular Biology Reviews* (2024), DOI: https://doi.org/10.1128/mmbr.00181-23 | (foster2024bacterialcellvolume pages 8-10) | “Osmolality upregulates kdpFABC expression.” | Strong review-level statement; broadly useful for curation. | subject: osmolality (label-only); object: KdpFABC complex (label-only) |
| compatible-solute accumulation/transport — causes → osmoprotection | Rain-Franco et al., *Molecular Ecology* (2022), DOI: https://doi.org/10.1111/mec.16316 | (rain‐franco2022nichebreadthaffects pages 8-9) | “accumulation and transport of compatible solutes/osmolytes… support causal links: compatible-solute biosynthesis/uptake and transporter genes -> osmotic protection” | Moderate-to-strong general mechanistic support; ecological/transcriptomic framing rather than direct knockout causality. | subject: compatible-solute accumulation/transport (label-only); object: osmoprotection / response to osmotic stress (GO:0006970) |
| EPS matrix — binds → Na+ ions | Goszcz et al., *FEMS Microbiology Reviews* (2025), DOI: https://doi.org/10.1093/femsre/fuaf020 | (goszcz2025bacterialosmoprotectants—away pages 5-5) | “the EPS matrix ‘binds cations such as Na+ ions’” | Good review support; broad mechanism but indirect relative to growth breadth phenotype. | subject: exopolysaccharide matrix (label-only); object: sodium ion (CHEBI:29101) |
| EPS matrix — promotes → water retention / reduced pericellular Na+ toxicity | Goszcz et al., *FEMS Microbiology Reviews* (2025), DOI: https://doi.org/10.1093/femsre/fuaf020 | (goszcz2025bacterialosmoprotectants—away pages 5-5) | “lowering effective pericellular Na+ and retaining water” | Moderate support from review synthesis; indirect and likely context-dependent. | subject: exopolysaccharide matrix (label-only); object: water retention / reduced Na+ toxicity (label-only) |
| *Vibrio diabolicus* — has growth optimum at → 3–4% NaCl | Lichty, Dissertation (2024), DOI: https://doi.org/10.58088/07hg-r941 | (lichty2024compatiblesolutesare pages 74-78) | “V. diabolicus grew best at 37°C in M9G with 3%–4% NaCl” | Strong quantitative growth phenotype, but organism-specific and from dissertation evidence. Useful for boundary illustration rather than universal mechanism. | subject: *Vibrio diabolicus* (label-only); object: sodium chloride 3–4% w/v (CHEBI:26710) |
| 7% NaCl at 37°C — abolishes growth of → *Vibrio diabolicus* | Lichty, Dissertation (2024), DOI: https://doi.org/10.58088/07hg-r941 | (lichty2024compatiblesolutesare pages 74-78) | “growth was abolished at 37°C in 7% NaCl” | Strong quantitative phenotype; assay-specific (temperature and medium matter). | subject: sodium chloride 7% w/v at 37°C (CHEBI:26710); object: *Vibrio diabolicus* growth (label-only) |
| slight halophile category — spans → 2–5% NaCl | Nesrine et al., *World Journal of Biology and Biotechnology* (2020), DOI: https://doi.org/10.33865/wjb.005.02.0294 | (nesrine2020phylogeneticcharacterizationand pages 1-2) | “slight halophiles = 0.2–0.85 M (2–5% NaCl)” | Useful definitional edge; classification-level, not mechanistic. | subject: slight halophile (label-only); object: sodium chloride 2–5% w/v (CHEBI:26710) |
| moderate halophile category — spans → 5–20% NaCl | Nesrine et al., *World Journal of Biology and Biotechnology* (2020), DOI: https://doi.org/10.33865/wjb.005.02.0294 | (nesrine2020phylogeneticcharacterizationand pages 1-2) | “moderate halophiles = 0.85–3.4 M (5–20% NaCl)” | Useful definitional edge; classification-level, not mechanistic. | subject: moderate halophile (label-only); object: sodium chloride 5–20% w/v (CHEBI:26710) |
| NaCl delta mid2 breadth (3–8% NaCl) — overlaps → slight/moderate halophile boundary | Derived from category ranges in Nesrine et al. (2020), DOI: https://doi.org/10.33865/wjb.005.02.0294 | (nesrine2020phylogeneticcharacterizationand pages 1-2) | “a reported growth breadth of 3–8% (w/v) would overlap the slight category (2–5%) and the moderate category (5–20%)” | Interpretive mapping rather than direct source quote; useful for scope notes, but should be marked uncertain if curated as an edge. | subject: METPO:1000481; object: slight halophile / moderate halophile (label-only) |


*Table: This table compiles evidence-backed candidate subject–predicate–object edges relevant to the NaCl delta mid2 trait, emphasizing experimentally supported osmoadaptation mechanisms and quantitative salinity boundaries. It is useful as a direct starting point for TraitMech curation because each edge includes a source, snippet, uncertainty note, and suggested grounding.*

## 7) Mechanistic schematic (visual evidence)
The following figure (from Foster et al. 2024) summarizes how **c-di-AMP integrates osmoadaptation** by regulating K+ uptake/export and compatible-solute transport systems.

Cropped figure evidence: (foster2024bacterialcellvolume media 91e74369)

## 8) Warnings / claims not yet ready for curation
1. **Transporter-level specificity varies by taxon.** Compatible solutes like glycine betaine are broadly used but not uniformly protective across all taxa; salt-tolerance mechanisms can be species-specific (rain‐franco2022nichebreadthaffects pages 8-9). Avoid curating “universal” osmolyte efficacy edges without taxon qualifiers.
2. **Composite engineering edges.** In the proline engineering study, the strongest tolerance phenotype involved *multiple edits* (feedback-insensitive proline biosynthesis plus **putA** deletion). If curating “putA deletion → tolerance,” mark uncertainty unless the full text provides separable causal tests (khanh2024metabolicpathwayengineering pages 6-9).
3. **Assay dependence for breadth.** Temperature/media can shift apparent breadth (e.g., *V. diabolicus* at 37°C vs 30°C; 7% NaCl boundary) (lichty2024compatiblesolutesare pages 74-78). Curate NaCl delta mid2 as an assay-observed phenotype tied to standardized conditions where possible.
4. **Classification systems differ.** Numeric cutoffs for “halotolerant/slight/moderate” vary across classification schemes; ensure the chosen scheme is consistent across traits (nesrine2020phylogeneticcharacterizationand pages 1-2, lach2023charakterystykabioróżnorodnościi pages 41-42).

---

# DOI-first bibliography (publication date + URL)

1. Foster AJ, van den Noort M, Poolman B. **Bacterial cell volume regulation and the importance of cyclic di-AMP**. *Microbiology and Molecular Biology Reviews*. **Jun 2024**. DOI: **10.1128/mmbr.00181-23**. https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume media 91e74369)
2. Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H. **Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in an ectoine-deficient Halomonas elongata**. *Applied and Environmental Microbiology*. **Jan 2024**. DOI: **10.1128/aem.01905-23**. https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)
3. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata**. *Applied and Environmental Microbiology*. **Sep 2024**. DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 6-9, khanh2024metabolicpathwayengineering pages 1-2)
4. Rain-Franco A, Mouquet N, Gougat-Barbera C, Bouvier T, Beier S. **Niche breadth affects bacterial transcription patterns along a salinity gradient**. *Molecular Ecology*. **Dec 2022**. DOI: **10.1111/mec.16316**. https://doi.org/10.1111/mec.16316 (rain‐franco2022nichebreadthaffects pages 8-9, rain‐franco2022nichebreadthaffects pages 8-8, rain‐franco2022nichebreadthaffects pages 14-14)
5. Lichty KB. **Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria** (Dissertation). **2024**. DOI: **10.58088/07hg-r941**. https://doi.org/10.58088/07hg-r941 (lichty2024compatiblesolutesare pages 74-78)
6. Nesrine L, et al. **Phylogenetic characterization and screening of halophilic bacteria…** *World Journal of Biology and Biotechnology* (indexed as ArXiv in retrieval). **Aug 2020**. DOI: **10.33865/wjb.005.02.0294**. https://doi.org/10.33865/wjb.005.02.0294 (nesrine2020phylogeneticcharacterizationand pages 1-2)
7. Lach J. **Charakterystyka bioróżnorodności i potencjału biotechnologicznego mikroorganizmów halofilnych**. **2023** (journal unspecified in retrieval). (lach2023charakterystykabioróżnorodnościi pages 41-42)



References

1. (nesrine2020phylogeneticcharacterizationand pages 1-2): Lenchi Nesrine, Kebbouche Salima, Khelfaoui Mohamed Lamine, Laddada Belaid, BKhemili Souad, Gana Mohamed Lamine, Akmoussi Sihem, and Ferioune Imène. Phylogenetic characterization and screening of halophilic bacteria from algerian salt lake for the production of biosurfactant and enzymes. ArXiv, 5:1-9, Aug 2020. URL: https://doi.org/10.33865/wjb.005.02.0294, doi:10.33865/wjb.005.02.0294. This article has 10 citations.

2. (lach2023charakterystykabioróżnorodnościi pages 41-42): J Lach. Charakterystyka bioróżnorodności i potencjału biotechnologicznego mikroorganizmów halofilnych. Unknown journal, 2023.

3. (lichty2024compatiblesolutesare pages 74-78): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

4. (rain‐franco2022nichebreadthaffects pages 8-9): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Molecular Ecology, 31:1216-1233, Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

5. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

6. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

8. (foster2024bacterialcellvolume media 91e74369): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (khanh2024metabolicpathwayengineering pages 6-9): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

10. (rain‐franco2022nichebreadthaffects pages 8-8): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Molecular Ecology, 31:1216-1233, Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

11. (schiavo2025proposalfornew pages 1-4): Ana Paula Muche Schiavo, Roberta Almeida Vincenzi, and Fabio Rodrigues. Proposal for new halophile classification system based on statistical rarity definition of extremophiles. Unknown journal, Nov 2025. URL: https://doi.org/10.21203/rs.3.rs-8012852/v1, doi:10.21203/rs.3.rs-8012852/v1.

12. (schiavo2025proposalfornew pages 4-7): Ana Paula Muche Schiavo, Roberta Almeida Vincenzi, and Fabio Rodrigues. Proposal for new halophile classification system based on statistical rarity definition of extremophiles. Unknown journal, Nov 2025. URL: https://doi.org/10.21203/rs.3.rs-8012852/v1, doi:10.21203/rs.3.rs-8012852/v1.

13. (lichty2024compatiblesolutesare pages 10-14): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

14. (goszcz2025bacterialosmoprotectants—away pages 5-5): Aleksandra Goszcz, Karolina Furtak, Robert Stasiuk, Joanna Wójtowicz, Marcin Musiałowski, Michela Schiavon, and Klaudia Dębiec-Andrzejewska. Bacterial osmoprotectants—a way to survive in saline conditions and potential crop allies. FEMS Microbiology Reviews, May 2025. URL: https://doi.org/10.1093/femsre/fuaf020, doi:10.1093/femsre/fuaf020. This article has 45 citations and is from a domain leading peer-reviewed journal.

15. (rain‐franco2022nichebreadthaffects pages 14-14): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Molecular Ecology, 31:1216-1233, Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.