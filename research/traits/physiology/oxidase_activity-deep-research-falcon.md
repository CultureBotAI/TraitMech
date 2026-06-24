---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:01:27.626682'
end_time: '2026-06-18T12:15:35.635688'
duration_seconds: 848.01
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: oxidase activity
  trait_identifier: traitmech:000076
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: oxidase_activity
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological enzyme-activity phenotype in which a cell produces a
    terminal respiratory oxidase (notably cytochrome c oxidase); it is the basis of
    the diagnostic oxidase test.
  parent_traits: METPO:1000059
  synonyms: oxidase-positive
  evidence_summary: 'DOI:10.3390/microorganisms10050926:  (Hederstedt reviews bacterial
    cytochrome c oxidase, the terminal respiratory oxidase detected by the oxidase
    test.) | DOI:10.1089/ars.2020.8039:  (Borisov et al. review cytochrome bd-family
    terminal oxidases of prokaryotic respiratory chains.)'
  causal_graph_summary: 'oxidase_activity_terminal_oxidase: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxidase activity
- **METPO identifier:** traitmech:000076
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces a terminal respiratory oxidase (notably cytochrome c oxidase); it is the basis of the diagnostic oxidase test.
- **Parent traits:** METPO:1000059
- **Synonyms:** oxidase-positive
- **Existing evidence:** DOI:10.3390/microorganisms10050926:  (Hederstedt reviews bacterial cytochrome c oxidase, the terminal respiratory oxidase detected by the oxidase test.) | DOI:10.1089/ars.2020.8039:  (Borisov et al. review cytochrome bd-family terminal oxidases of prokaryotic respiratory chains.)
- **Existing causal graph summary:** oxidase_activity_terminal_oxidase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **oxidase activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/oxidase_activity.yaml`.

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
- **Trait label:** oxidase activity
- **METPO identifier:** traitmech:000076
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces a terminal respiratory oxidase (notably cytochrome c oxidase); it is the basis of the diagnostic oxidase test.
- **Parent traits:** METPO:1000059
- **Synonyms:** oxidase-positive
- **Existing evidence:** DOI:10.3390/microorganisms10050926:  (Hederstedt reviews bacterial cytochrome c oxidase, the terminal respiratory oxidase detected by the oxidase test.) | DOI:10.1089/ars.2020.8039:  (Borisov et al. review cytochrome bd-family terminal oxidases of prokaryotic respiratory chains.)
- **Existing causal graph summary:** oxidase_activity_terminal_oxidase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **oxidase activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/oxidase_activity.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Oxidase Activity (traitmech:000076)

### Scope summary (trait meaning, test basis, boundary cases)
**Oxidase activity** (METPO traitmech:000076) is best treated as an *assay-observed physiological enzyme-activity phenotype* indicating that a microbe can catalyze oxidation of the **oxidase test reagent** (commonly **TMPD, N,N,N′,N′-tetramethyl-p-phenylenediamine**) via a terminal respiratory oxidase pathway, producing a characteristic **dark blue/purple** signal (blue indophenol). The oxidase test is described as detecting “cytochrome oxidase (also called indophenol oxidase)” using TMPD as an artificial electron donor, where oxidation yields a dark color change interpreted as a positive reaction. (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetest pages 3-4)

Mechanistically, the phenotype most directly maps to the presence of a **heme–copper terminal oxidase** branch (classically a **cytochrome c oxidase**), because canonical bacterial cytochrome c oxidase electron flow is from reduced cytochrome c to a **CuA** center, then to **heme a**, then to the **dioxygen reduction site** (heme a3 + CuB). (hederstedt2022diversityofcytochrome pages 1-2)

**Boundary cases / distinctions:**
1. **Heme–copper oxidases vs bd-type oxidases:** Reviews distinguish heme–copper oxidases (cytochrome c oxidases; with **CuB** and a high-spin heme) from **copper-lacking bd-type quinol oxidases** (with **heme d** as O2-reducing site). Bd-type oxidases support aerobic respiration and stress resistance but are not the canonical target of the TMPD/cytochrome c-linked oxidase test. (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4)
2. **Quinol oxidase bo3 (E. coli):** **bo3 quinol oxidase** is a heme–copper oxidase (CuB-containing) but accepts electrons from quinol rather than cytochrome c. It is therefore a plausible boundary mechanism that may not be reliably captured by a cytochrome c/TMPD test in all contexts; it should be curated as a nearby node unless assay linkage is explicitly demonstrated for the taxon/test format. (khalfaouihassani2023theescherichiacoli pages 1-2)
3. **Expression/assembly and environment can generate false negatives:** cbb3-type oxidase activity depends on copper trafficking and is affected by sulfide and growth conditions, meaning an organism with the genetic capacity could test “oxidase-negative” if the enzyme is not expressed/assembled under test conditions (e.g., copper limitation; sulfide exposure; oxygen regime). (garg2021geneslinkingcopper pages 7-8, garg2021geneslinkingcopper pages 1-2)
4. **Assay procedural constraints:** The oxidase test description includes dependence on culture conditions and cautions about colony source; for example, the cited oxidase-test paper recommends specific culture ages/media and warns that colony collection conditions can affect interpretation. (baldea2023theoxidasetesta pages 1-3, baldea2023theoxidasetest pages 1-3)

### Key concepts and current mechanistic understanding
#### 1) Canonical cytochrome c oxidase mechanism (family A heme–copper oxidase)
A bacterial **family A cytochrome c oxidase** has a conserved 3-subunit core and contains **two heme A prosthetic groups (heme a and heme a3)** and **three copper atoms** (a **dicopper CuA** site in subunit II and **CuB** in subunit I). Electron transfer proceeds from **reduced cytochrome c → CuA → heme a → O2 reduction site (heme a3 + CuB)**. (hederstedt2022diversityofcytochrome pages 1-2)

These core cofactor/flow statements are strong anchors for TraitMech nodes and edges because they explicitly tie (i) cytochrome c and (ii) a terminal oxidase metal-center architecture to (iii) oxygen reduction—matching the trait definition and assay proxy. (hederstedt2022diversityofcytochrome pages 1-2)

#### 2) cbb3-type cytochrome c oxidase (microaerophilic/high-O2-affinity oxidase)
The **cbb3-type cytochrome c oxidase (Cco)** is described as a **heme–copper oxidase** with **high oxygen affinity typical of microaerophiles**. Its redox cofactors are distributed across subunits: **CcoN** contains the **CuB–heme b3** binuclear center; **CcoO** is a monoheme c-type; **CcoP** is a diheme c-type. (garg2021geneslinkingcopper pages 1-2)

A key curation-relevant finding is that **cbb3 oxidase assembly and activity are copper-dependent** and require specific accessory genes; in Campylobacter jejuni, deletion of **ccoI** and **ccoS** abolishes Cco activity and can be partially rescued by copper addition in some cases. (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17)

#### 3) Terminal oxidase diversity and inhibitor sensitivity (bd vs bo3)
Recent work highlights physiological specialization of terminal oxidases. In E. coli, cytochrome **bo3** is preferentially expressed at high aeration, while **bd-type oxidases** are induced in low oxygen; bd oxidases lack copper and contain **heme d** as the oxygen-reducing site. (nastasi2024membraneboundredoxenzyme pages 2-4)

This specialization is important for oxidase-activity interpretation: oxidase-test positivity is a proxy for a particular terminal oxidase/electron transfer setup, whereas an organism may respire via bd-type oxidases and still present differently in oxidase assays depending on test chemistry and electron donors. (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4)

### Recent developments (prioritizing 2023–2024)
#### A) 2024 quantitative physiology: cytochrome bd-I confers CO-resistant respiration
A 2024 study quantitatively compared CO sensitivity across E. coli mutants expressing only one terminal oxidase. At **96.3 µM CO** and **[O2] = 100 µM**, inhibition of O2 consumption was **11.6 ± 1.1%** for **bd-I-only** cells, versus **43.3 ± 7.6%** for **bd-II-only** and **44.3 ± 1.5%** for **bo3-only** cells. (nastasi2024membraneboundredoxenzyme pages 2-4)

This provides a strong, numeric, experimentally grounded edge candidate linking **CO exposure → differential inhibition of terminal oxidases → altered respiration (and potentially altered “oxidase activity” readouts depending on assay).** (nastasi2024membraneboundredoxenzyme pages 2-4)

The same 2024 source also reports kinetic parameters relevant to stress recovery: bd oxidases show fast NO dissociation from heme d (koff **0.133 s−1** and **0.163 s−1**), supporting a mechanistic basis for resilience to NO. (nastasi2024membraneboundredoxenzyme pages 2-4)

#### B) 2024 anti-TB drug discovery: cytochrome bd oxidase as a prokaryote-specific target
A 2024 review emphasizes that **cytochrome bd oxidase** is absent in eukaryotic cells, motivating its selection as an antimicrobial target, and discusses the need for regimens that inhibit terminal oxidases to obtain bactericidal effects in Mycobacterium tuberculosis. (saha2024cytochromebdoxidase pages 2-3)

A 2024 medicinal-chemistry/computational study reports **six new inhibitor scaffolds** for cytochrome bd oxidase and notes synergy between bd inhibition and bedaquiline, positioning terminal oxidase inhibition as a practical therapeutic strategy. (seitz2024targetingtuberculosisnovel pages 1-3)

These sources support curation of *application nodes/edges* (drug targeting; inhibitor discovery), which may be stored in a separate “applications” layer if TraitMech graphs are intended to represent intrinsic cellular mechanism only. (saha2024cytochromebdoxidase pages 2-3, seitz2024targetingtuberculosisnovel pages 1-3)

#### C) 2023 oxidase biogenesis: transporters required for active bo3 quinol oxidase
A 2023 PLOS ONE paper identified three E. coli MFS-type transporter genes (**yhjE, ydiM, yfcJ**) required to “produce an active bo3 quinol oxidase,” connecting metal transport/homeostasis to heme–copper oxidase biogenesis. (khalfaouihassani2023theescherichiacoli pages 1-2)

This is relevant as a *causal upstream layer* for oxidase-related phenotypes: disrupted cofactor supply/handling can alter terminal oxidase activity (and thus the oxidase test outcome), even if structural genes are intact. (khalfaouihassani2023theescherichiacoli pages 1-2)

### Current applications and real-world implementations
1. **Clinical and environmental microbiology identification:** The oxidase test is used as a routine biochemical identification assay; mechanistically it relies on TMPD oxidation to a dark blue/purple product and is interpreted as indicating cytochrome oxidase activity. (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetest pages 3-4)
2. **Functional phenotyping and respiration assays:** TMPD is also used in quantitative oxygen-consumption assays as an artificial electron donor for cytochrome c oxidase activity measurements, including in studies linking gene deletions (e.g., ccoI/ccoS) to loss of oxidase activity. (garg2021geneslinkingcopper pages 7-8, garg2021geneslinkingcopper pages 1-2)
3. **Drug discovery and antimicrobial strategy:** Terminal oxidases—particularly cytochrome bd (prokaryote-specific)—are active targets for anti-TB lead discovery and for combination regimens aimed at achieving bactericidal synergy and reducing resistance emergence. (saha2024cytochromebdoxidase pages 2-3, seitz2024targetingtuberculosisnovel pages 1-3)

### Expert opinions / authoritative analysis (source-backed)
- **Cytochrome bd as an “emerging anti-tubercular drug target”:** The 2024 RSC Med Chem review frames cytochrome bd as indispensable under stress and argues for combination strategies targeting both terminal oxidase branches to achieve a desired bactericidal response, with redundancy between branches motivating dual inhibition. (saha2024cytochromebdoxidase pages 2-3)
- **Terminal oxidase heterogeneity as adaptive physiology:** The 2024 IJMS study frames terminal oxidase expression as oxygen-regulated and emphasizes distinct inhibitor/stress sensitivities, supporting the idea that “oxidase activity” is context-dependent and should be curated with environmental/expression modifiers. (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 1-2)

### Candidate nodes (grouped by type)
A consolidated, curation-ready node list with suggested grounding and curator notes is provided in:

| Node label | Node type | Suggested ontology grounding | Notes for curation | Key supporting citations |
|---|---|---|---|---|
| oxidase activity | assay/phenotype | METPO:traitmech:000076 | Assay-observed phenotype; best interpreted as the ability to oxidize TMPD/Kovács reagent via a terminal respiratory oxidase, usually a cytochrome c oxidase branch rather than all aerobic terminal oxidases. | (hederstedt2022diversityofcytochrome pages 1-2, baldea2023theoxidasetesta pages 3-4) |
| oxidase test | assay/phenotype |  | Diagnostic biochemical test based on oxidation of tetramethyl-p-phenylenediamine to a dark blue/purple product; useful phenotype node distinct from the underlying enzyme complex. | (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetesta pages 1-3) |
| TMPD oxidation / blue indophenol formation | assay/phenotype |  | Direct assay readout; oxidation of TMPD gives dark blue/purple signal indicating positive oxidase reaction. | (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetest pages 1-3) |
| cytochrome c oxidase (heme-copper oxygen reductase) | proteins/complexes | GO:0004129 | Central mechanistic node for the trait; terminal oxidase reducing O2 to H2O; in canonical family A enzymes electrons arrive from cytochrome c. | (hederstedt2022diversityofcytochrome pages 1-2, hederstedt2022diversityofcytochrome pages 2-4) |
| family A cytochrome c oxidase | proteins/complexes |  | Best-supported canonical oxidase-test target; contains heme a/heme a3 and CuA/CuB centers. | (hederstedt2022diversityofcytochrome pages 1-2, hederstedt2022diversityofcytochrome pages 2-4) |
| cbb3-type cytochrome c oxidase (Cco) | proteins/complexes |  | High-O2-affinity heme-copper oxidase common in microaerophiles; taxon-specific but important positive-mechanism node for oxidase activity in some bacteria. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| cytochrome bo3 quinol oxidase (bo3-Qox) | proteins/complexes |  | Heme-copper quinol oxidase with CuB; relevant boundary case because it is a terminal oxidase but not the classic cytochrome-c-dependent oxidase-test target. Mark as uncertain for direct curation to trait unless assay linkage is shown. | (khalfaouihassani2023theescherichiacoli pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2) |
| cytochrome bd-I oxidase | proteins/complexes |  | Copper-lacking bd-type terminal oxidase; important nearby trait/boundary node because it supports aerobic respiration and stress resistance but is not the canonical oxidase-test target. | (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4) |
| cytochrome bd-II oxidase | proteins/complexes |  | As above; useful comparator node for inhibitor sensitivity/expression context. | (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 1-2) |
| CcoN catalytic subunit | proteins/complexes |  | cbb3 catalytic subunit containing the CuB-haem b3 binuclear center where O2 reduction occurs. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| CcoO subunit | proteins/complexes |  | Monohaem c-type subunit of cbb3 oxidase. | (garg2021geneslinkingcopper pages 1-2) |
| CcoP subunit | proteins/complexes |  | Dihaem c-type subunit of cbb3 oxidase. | (garg2021geneslinkingcopper pages 1-2) |
| CuA center | proteins/complexes |  | Electron-entry copper center in family A cytochrome c oxidases; absent from some other oxidase families. | (hederstedt2022diversityofcytochrome pages 1-2, hederstedt2022diversityofcytochrome pages 2-4) |
| CuB-heme binuclear center | proteins/complexes |  | Catalytic O2-reduction center in heme-copper oxidases; represented in CcoN and bo3/family A oxidases. | (garg2021geneslinkingcopper pages 1-2, khalfaouihassani2023theescherichiacoli pages 1-2) |
| ccoNOQP operon | genes/operons |  | Structural gene set for cbb3-type cytochrome c oxidase; strong causal candidate for oxidase-positive phenotype in taxa using Cco. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| ccoI | genes/operons |  | Cu-translocating P-type ATPase required for Cco biogenesis/activity; deletion abolishes Cco activity in Campylobacter jejuni. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| ccoS | genes/operons |  | Cco biogenesis factor; deletion abolishes activity though complex may still assemble. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| ccoG | genes/operons |  | Accessory oxidoreductase/cupric-reductase-like factor; loss partially reduces Cco activity. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| ccoH | genes/operons |  | Accessory assembly factor linked to cbb3 oxidase production; keep as candidate assembly node. | (garg2021geneslinkingcopper pages 16-17) |
| PCuAC | genes/operons |  | Periplasmic copper chaperone homologue needed for full Cco activity. | (garg2021geneslinkingcopper pages 16-17) |
| Sco | genes/operons |  | Periplasmic copper chaperone homologue needed for full Cco activity. | (garg2021geneslinkingcopper pages 16-17) |
| ctaA | genes/operons |  | Heme A biosynthesis/assembly factor for family A cytochrome c oxidase; general assembly node, not assay-specific. | (hederstedt2022diversityofcytochrome pages 1-2) |
| ctaB | genes/operons |  | Heme A biosynthesis/assembly factor for family A cytochrome c oxidase. | (hederstedt2022diversityofcytochrome pages 1-2) |
| surf1 / shy1 family | genes/operons |  | Assembly factor implicated in heme insertion/maturation of cytochrome c oxidase. | (hederstedt2022diversityofcytochrome pages 1-2, khalfaouihassani2023theescherichiacoli pages 1-2) |
| cox11 / ctaG family | genes/operons |  | Cu-center assembly factor for cytochrome c oxidase. | (hederstedt2022diversityofcytochrome pages 1-2) |
| yhjE | genes/operons |  | E. coli MFS transporter gene required for active bo3 quinol oxidase production; boundary-case support for oxidase biogenesis outside cco systems. | (khalfaouihassani2023theescherichiacoli pages 1-2) |
| ydiM | genes/operons |  | As above; linked to slower 64Cu uptake and bo3-dependent respiratory growth defect. | (khalfaouihassani2023theescherichiacoli pages 1-2) |
| yfcJ | genes/operons |  | As above; required for active bo3 quinol oxidase in E. coli. | (khalfaouihassani2023theescherichiacoli pages 1-2) |
| cyoABCDE | genes/operons |  | bo3 oxidase operon; expression favored under fully aerobic conditions. | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| cydABX | genes/operons |  | bd-I oxidase gene set; expression favored at intermediate/low aeration. | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| appCBX | genes/operons |  | bd-II oxidase gene set; expression favored at very low aeration. | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| heme a | cofactors/metals | CHEBI:30413 | Prosthetic group unique to family A heme-copper oxidases; strong positive mechanistic node for canonical oxidase-test target. | (hederstedt2022diversityofcytochrome pages 1-2) |
| heme a3 | cofactors/metals | CHEBI:36173 | High-spin catalytic heme in family A cytochrome c oxidase. | (hederstedt2022diversityofcytochrome pages 1-2) |
| heme b3 | cofactors/metals |  | Catalytic heme paired with CuB in cbb3 oxidase. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| heme c | cofactors/metals | CHEBI:61717 | Cofactor of CcoO/CcoP cytochrome c subunits in cbb3 oxidase. | (garg2021geneslinkingcopper pages 1-2) |
| heme d | cofactors/metals |  | O2-reducing site in bd-type oxidases; useful boundary node. | (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4) |
| copper ion | cofactors/metals | CHEBI:28694 | Essential for CuA/CuB center formation and full oxidase activity; copper limitation can cause false-negative phenotype. | (hederstedt2022diversityofcytochrome pages 1-2, garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| CuA dicopper center | cofactors/metals |  | Electron-accepting copper site in family A oxidases. | (hederstedt2022diversityofcytochrome pages 1-2) |
| CuB center | cofactors/metals |  | Catalytic copper site in heme-copper oxidases including cbb3 and bo3. | (garg2021geneslinkingcopper pages 1-2, khalfaouihassani2023theescherichiacoli pages 1-2) |
| molecular oxygen | small molecules/inhibitors | CHEBI:15379 | Terminal electron acceptor reduced to water by terminal oxidases. | (hederstedt2022diversityofcytochrome pages 1-2, borisov2025carbonmonoxideand pages 5-7) |
| water | small molecules/inhibitors | CHEBI:15377 | Product of O2 reduction by terminal oxidases. | (hederstedt2022diversityofcytochrome pages 1-2) |
| cytochrome c | small molecules/inhibitors |  | Physiological electron donor to canonical cytochrome c oxidase; TMPD serves as artificial electron donor in assay context. | (hederstedt2022diversityofcytochrome pages 1-2, baldea2023theoxidasetesta pages 3-4) |
| TMPD (N,N,N',N'-tetramethyl-p-phenylenediamine) | small molecules/inhibitors | CHEBI:9568 | Core assay reagent/artificial electron donor for oxidase test and quantitative oxidase activity assays. | (baldea2023theoxidasetesta pages 3-4, garg2021geneslinkingcopper pages 7-8) |
| potassium cyanide / cyanide | small molecules/inhibitors | CHEBI:17514 | Classic oxidase inhibitor; bo3 is highly cyanide-sensitive, bd oxidases comparatively resistant. | (khalfaouihassani2023theescherichiacoli pages 1-2, nastasi2024membraneboundredoxenzyme pages 2-4) |
| carbon monoxide | small molecules/inhibitors | CHEBI:17245 | Potent inhibitor/ligand of heme terminal oxidases; useful environmental and pharmacological perturbation node. | (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4) |
| nitric oxide | small molecules/inhibitors | CHEBI:16480 | Stressor/inhibitor; bd-I shows rapid recovery due to fast NO dissociation from heme d. | (nastasi2024membraneboundredoxenzyme pages 2-4) |
| hydrogen sulfide / sulfide | small molecules/inhibitors | CHEBI:16134 | Sulfide sensitivity affects Cco activity; bd oxidases can confer sulfide resistance. | (garg2021geneslinkingcopper pages 7-8, nastasi2024membraneboundredoxenzyme pages 2-4) |
| peroxynitrite | small molecules/inhibitors | CHEBI:16453 | Stress molecule detoxification/resistance linked to bd oxidase physiology; nearby trait node rather than direct oxidase-test node. | (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 18-19) |
| hydrogen peroxide | small molecules/inhibitors | CHEBI:16240 | bd oxidases increase resistance to H2O2; contextual stress-resistance node. | (nastasi2024membraneboundredoxenzyme pages 2-4) |
| microaerobic conditions | environmental/experimental factors | ENVO:01000203 | Favors cbb3/bd oxidase expression and relevance; important environment for oxidase phenotype expression in some taxa. | (garg2021geneslinkingcopper pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2) |
| fully aerobic / high aeration conditions | environmental/experimental factors |  | Favors bo3 oxidase expression in E. coli. | (nastasi2024membraneboundredoxenzyme pages 1-2) |
| oxygen-limited conditions | environmental/experimental factors |  | Shift expression toward bd/cbb3-type high-affinity oxidases. | (garg2021geneslinkingcopper pages 1-2, nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 1-2) |
| exogenous copper supplementation | environmental/experimental factors |  | Can partially rescue loss of Cco activity in copper-trafficking mutants; important assay-condition node. | (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) |
| blood agar colony source | environmental/experimental factors |  | Practical oxidase-test caveat; colony source/media can distort interpretation and should be marked assay-specific. | (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetesta pages 1-3) |
| culture age | environmental/experimental factors |  | Oxidase-test interpretation depends on growth time/medium; mark as assay-specific condition node. | (baldea2023theoxidasetesta pages 1-3, baldea2023theoxidasetest pages 1-3) |
| anti-TB terminal oxidase targeting | environmental/experimental factors |  | Application node capturing current use of cytochrome bd / bcc-aa3 inhibition in drug discovery rather than intrinsic phenotype mechanism. | (saha2024cytochromebdoxidase pages 2-3, seitz2024targetingtuberculosisnovel pages 1-3) |


*Table: This table lists curation-ready candidate nodes for a TraitMech causal graph of oxidase activity, grouped by biological and assay-relevant type. It highlights the most defensible entities from the cited evidence while flagging nearby boundary cases such as bd- and bo3-type oxidases.*

### Candidate causal edges (evidence-backed triples)
A consolidated, evidence-backed edge list (subject–predicate–object), with snippets, DOI/URL/year, and uncertainty flags is provided in:

| Edge (S–P–O) | Evidence snippet (short quote) | Reference (DOI + URL + year) and pqac citation id | Notes/uncertainty |
|---|---|---|---|
| TMPD oxidase test — has_input — TMPD (N,N,N',N'-tetramethyl-p-phenylenediamine) | “TMPD is frequently used as the artificial electron donor” | Baldea & Popvici 2023, DOI unavailable, year 2023; (baldea2023theoxidasetest pages 3-4) | Assay-specific edge; supports phenotype readout rather than native physiology. |
| TMPD oxidation — produces_readout — blue/purple indophenol signal | “when TMPD is oxidized by cytochrome c it changes from colorless to a dark blue or purple compound (blue indophenol)” | Baldea & Popvici 2023, DOI unavailable, year 2023; (baldea2023theoxidasetest pages 3-4) | Assay chemistry edge for oxidase-test node. |
| oxidase test positive result — indicates_presence_of — cytochrome oxidase / cytochrome c oxidase activity | “detects cytochrome oxidase… when TMPD is oxidized by cytochrome c” | Baldea & Popvici 2023, DOI unavailable, year 2023; (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetest pages 3-4) | Use cautiously: positive test is a proxy for a compatible terminal oxidase/electron-transfer chain, not a complete mechanistic proof in all taxa. |
| reduced cytochrome c — donates_electrons_to — CuA center | “reduced cytochrome c donates electrons to the CuA center in subunit II” | Hederstedt 2022. DOI:10.3390/microorganisms10050926. https://doi.org/10.3390/microorganisms10050926. 2022; (hederstedt2022diversityofcytochrome pages 1-2) | Core mechanistic edge for canonical cytochrome c oxidase. |
| CuA center — transfers_electrons_to — heme a | “then to low-spin heme a” | Hederstedt 2022. DOI:10.3390/microorganisms10050926. https://doi.org/10.3390/microorganisms10050926. 2022; (hederstedt2022diversityofcytochrome pages 1-2) | Strong mechanistic support for family A oxidase electron flow. |
| heme a3 + CuB binuclear center — reduces — molecular oxygen | “the dioxygen reduction site (heme a3 + CuB)” | Hederstedt 2022. DOI:10.3390/microorganisms10050926. https://doi.org/10.3390/microorganisms10050926. 2022; (hederstedt2022diversityofcytochrome pages 1-2) | Supports O2-reduction terminal step. |
| family A cytochrome c oxidase — has_cofactor — heme a | “contains two heme A prosthetic groups (heme a and heme a3)” | Hederstedt 2022. DOI:10.3390/microorganisms10050926. https://doi.org/10.3390/microorganisms10050926. 2022; (hederstedt2022diversityofcytochrome pages 1-2) | Good candidate node for canonical oxidase-positive mechanism. |
| family A cytochrome c oxidase — has_cofactor — CuA/CuB copper centers | “three copper atoms (CuA is di-copper in subunit II; CuB in subunit I)” | Hederstedt 2022. DOI:10.3390/microorganisms10050926. https://doi.org/10.3390/microorganisms10050926. 2022; (hederstedt2022diversityofcytochrome pages 1-2) | Strong cofactor edge. |
| ccoNOQP operon — enables_assembly/activity_of — cbb3-type cytochrome c oxidase | “genes ccoG, ccoI and ccoS are involved… deletion of ccoI and ccoS abolishes Cco activity” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) | Structural-operon implication is strong, but snippet emphasizes accessory genes more explicitly than all four structural genes. |
| ccoI — positively_regulates — cbb3-type cytochrome c oxidase activity | “CcoI is a Cu-translocating P-type ATPase… deletion of ccoI… abolishes Cco activity” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) | Strong, experimentally supported; taxon demonstrated in Campylobacter jejuni. |
| ccoS — positively_regulates — cbb3-type cytochrome c oxidase activity | “deletion of ccoS abolishes Cco activity” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17) | Strong, but taxon-specific. |
| PCuAC — positively_regulates — cbb3-type cytochrome c oxidase activity | “loss of PCuAC/Sco chaperone homologues reduces activity” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2) | Strong but partial-loss phenotype; assembly/metalation factor rather than structural subunit. |
| Sco — positively_regulates — cbb3-type cytochrome c oxidase activity | “loss of PCuAC/Sco chaperone homologues reduces activity” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2) | Same caveat as PCuAC. |
| copper ion availability — positively_regulates — cbb3-type cytochrome c oxidase activity | “partially rescued by added copper” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2) | Important environmental/assay-condition edge; likely relevant to false negatives under Cu limitation. |
| microaerobic conditions — select_for/use_of — cbb3-type cytochrome c oxidase | “cbb3-type cytochrome c oxidases, as proton-translocating respiratory complexes with high oxygen affinity typical of microaerophiles” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 1-2) | Strong ecological/physiological edge; useful for expression context. |
| sulfide — inhibits — cbb3-type cytochrome c oxidase activity | “Cco activity is reported as… sulphide sensitive” | Garg et al. 2021. DOI:10.3389/fmicb.2021.683260. https://doi.org/10.3389/fmicb.2021.683260. 2021; (garg2021geneslinkingcopper pages 7-8, garg2021geneslinkingcopper pages 16-17) | Strong but species/assay-context specific. |
| cytochrome bo3 — is_highly_sensitive_to — cyanide | “bo3 is highly sensitive to cyanide, sulfide, NO and ammonia” | Nastasi et al. 2024. DOI:10.3390/ijms25021277. https://doi.org/10.3390/ijms25021277. 2024; (nastasi2024membraneboundredoxenzyme pages 2-4) | Comparative inhibitor-sensitivity edge. |
| bd-type oxidases — increase_resistance_to — cyanide | “Bd oxidases also increase resistance to cyanide, H2O2 and sulfide” | Nastasi et al. 2024. DOI:10.3390/ijms25021277. https://doi.org/10.3390/ijms25021277. 2024; (nastasi2024membraneboundredoxenzyme pages 2-4) | Comparative edge; nearby trait rather than canonical oxidase-test mechanism. |
| carbon monoxide — inhibits — heme–copper cytochrome c oxidases | “CO is a potent inhibitor of heme–copper cytochrome c oxidase (Ki ~0.3 µM)” | Borisov & Forte 2025. DOI:10.3390/ijms26062809. https://doi.org/10.3390/ijms26062809. 2025; (borisov2025carbonmonoxideand pages 5-7) | General inhibitor edge; 2025 review summarizing broader evidence. |
| cytochrome bd-I — confers — CO-resistant aerobic respiration | “96.3 µM CO at [O2]=100 µM inhibited O2 consumption of bd-I-only E. coli by 11.6±1.1%, versus 43.3±7.6% and 44.3±1.5% for bd-II-only and bo3-only strains respectively” | Nastasi et al. 2024. DOI:10.3390/ijms25021277. https://doi.org/10.3390/ijms25021277. 2024; (nastasi2024membraneboundredoxenzyme pages 2-4) | Strong quantitative edge; very useful for comparative physiology and inhibitor-response nodes. |
| cytochrome bd-I — promotes — CO-resistant growth | “cells expressing only cytochrome bd-I show minimal growth inhibition after CO addition” | Nastasi et al. 2024. DOI:10.3390/ijms25021277. https://doi.org/10.3390/ijms25021277. 2024; (nastasi2024membraneboundredoxenzyme pages 1-2) | Qualitative growth phenotype; complements quantitative respiration data. |
| cytochrome bd oxidase — absent_in — eukaryotes | “absence of this oxidase in eukaryotic cells allows researchers to select it as a potential drug target” | Saha et al. 2024. DOI:10.1039/d3md00587a. https://doi.org/10.1039/d3md00587a. 2024; (saha2024cytochromebdoxidase pages 2-3) | Strong application edge; not direct oxidase-test mechanism but high-value context. |
| cytochrome bd oxidase absence in eukaryotes — enables — anti-TB drug-target application | “allows researchers to select it as a potential drug target” | Saha et al. 2024. DOI:10.1039/d3md00587a. https://doi.org/10.1039/d3md00587a. 2024; Seitz et al. 2024. DOI:10.1021/acs.jcim.4c00344. https://doi.org/10.1021/acs.jcim.4c00344. 2024; (saha2024cytochromebdoxidase pages 2-3, seitz2024targetingtuberculosisnovel pages 1-3) | Application edge; curate separately from core trait graph if TraitMech is restricted to intrinsic mechanism. |
| yhjE — required_for_production_of — active bo3 quinol oxidase | “three candidate genes, yhjE, ydiM, and yfcJ, were found to be critical for E. coli growth” and “required to produce an active bo3 quinol oxidase” | Khalfaoui-Hassani et al. 2023. DOI:10.1371/journal.pone.0293015. https://doi.org/10.1371/journal.pone.0293015. 2023; (khalfaouihassani2023theescherichiacoli pages 1-2) | Boundary-case edge for bo3 branch; not canonical oxidase-test target. |
| ydiM — required_for_production_of — active bo3 quinol oxidase | “three candidate genes, yhjE, ydiM, and yfcJ, were found to be critical” | Khalfaoui-Hassani et al. 2023. DOI:10.1371/journal.pone.0293015. https://doi.org/10.1371/journal.pone.0293015. 2023; (khalfaouihassani2023theescherichiacoli pages 1-2) | Same caveat as above. |
| yfcJ — required_for_production_of — active bo3 quinol oxidase | “three candidate genes, yhjE, ydiM, and yfcJ, were found to be critical” | Khalfaoui-Hassani et al. 2023. DOI:10.1371/journal.pone.0293015. https://doi.org/10.1371/journal.pone.0293015. 2023; (khalfaouihassani2023theescherichiacoli pages 1-2) | Same caveat as above. |
| CalT-family / MFS copper transport function — positively_regulates — heme-Cu oxidase biogenesis | “Cu import/assembly for cbb3-Cox depends on MFS-type CalT transporters (e.g., CcoA)” | Khalfaoui-Hassani et al. 2023. DOI:10.1371/journal.pone.0293015. https://doi.org/10.1371/journal.pone.0293015. 2023; (khalfaouihassani2023theescherichiacoli pages 1-2) | Generalized from cbb3 literature; relevant to oxidase biogenesis, but not directly oxidase-test specific. |


*Table: This table lists evidence-backed subject–predicate–object edges for a TraitMech causal graph of oxidase activity, using only the pqac evidence snippets gathered in the session. It prioritizes assay chemistry, terminal oxidase mechanism, assembly factors, environmental modulation, and inhibitor/application edges with explicit uncertainty notes.*

### Warnings / claims that should not yet be curated (or should be marked uncertain)
1. **Do not equate “oxidase-positive” with “aerobic” or with “presence of any terminal oxidase.”** Bd-type oxidases are terminal oxidases enabling aerobic respiration but are mechanistically distinct (copper-lacking) and may not map cleanly to a TMPD/cytochrome c-based oxidase test. Treat bd nodes as boundary/nearby traits unless direct assay linkage is curated. (borisov2025carbonmonoxideand pages 5-7, nastasi2024membraneboundredoxenzyme pages 2-4)
2. **bo3 quinol oxidase linkage to oxidase test is uncertain without assay evidence.** bo3 is a heme–copper oxidase but uses quinol as electron donor; include as boundary node or curate with an explicit “uncertain assay mapping” note. (khalfaouihassani2023theescherichiacoli pages 1-2)
3. **Assay sensitivity to culture conditions and cofactor availability can yield false negatives.** Copper trafficking/availability and sulfide sensitivity can abolish or reduce cbb3 oxidase activity, which can affect oxidase test outcomes; curate these as modifiers and consider “assay-specific false-negative risk” notes. (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 7-8)
4. **Non-peer-reviewed/unclear-journal oxidase-test sources:** The Baldea & Popvici oxidase-test writeup provides clear assay chemistry statements but appears in an “unknown journal” in the retrieved metadata; it is useful for defining the test chemistry but should be corroborated with a standard diagnostic microbiology reference before high-confidence curation if strict evidence standards are required. (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetesta pages 1-3)

### DOI-first bibliography (with URLs and publication dates where available)
1. **Nastasi MR, Borisov VB, Forte E.** *Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant Escherichia coli Growth and Respiration.* **International Journal of Molecular Sciences**. **2024-01**. DOI: **10.3390/ijms25021277**. https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 1-2)
2. **Seitz C, Ahn S-H, Wei H, et al.** *Targeting Tuberculosis: Novel Scaffolds for Inhibiting Cytochrome bd Oxidase.* **Journal of Chemical Information and Modeling**. **2024-06**. DOI: **10.1021/acs.jcim.4c00344**. https://doi.org/10.1021/acs.jcim.4c00344 (seitz2024targetingtuberculosisnovel pages 1-3)
3. **Saha P, Das S, Indurthi HK, et al.** *Cytochrome bd oxidase: an emerging anti-tubercular drug target.* **RSC Medicinal Chemistry**. **2024-03**. DOI: **10.1039/d3md00587a**. https://doi.org/10.1039/d3md00587a (saha2024cytochromebdoxidase pages 2-3)
4. **González-Montalvo MA, Sorescu JM, Baltes G, Juárez O, Tuz K.** *The respiratory chain of Klebsiella aerogenes in urine-like conditions: critical roles of NDH-2 and bd-terminal oxidases.* **Frontiers in Microbiology**. **2024-11**. DOI: **10.3389/fmicb.2024.1479714**. https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 1-2)
5. **Khalfaoui-Hassani B, Blaby-Haas CE, Verissimo A, Daldal F.** *The Escherichia coli MFS-type transporter genes yhjE, ydiM, and yfcJ are required to produce an active bo3 quinol oxidase.* **PLOS ONE**. **2023-10**. DOI: **10.1371/journal.pone.0293015**. https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2)
6. **Hederstedt L.** *Diversity of Cytochrome c Oxidase Assembly Proteins in Bacteria.* **Microorganisms**. **2022-04**. DOI: **10.3390/microorganisms10050926**. https://doi.org/10.3390/microorganisms10050926 (hederstedt2022diversityofcytochrome pages 1-2, hederstedt2022diversityofcytochrome pages 2-4)
7. **Garg N, Taylor AJ, Pastorelli F, et al.** *Genes Linking Copper Trafficking and Homeostasis to the Biogenesis and Activity of the cbb3-Type Cytochrome c Oxidase in the Enteric Pathogen Campylobacter jejuni.* **Frontiers in Microbiology**. **2021-06**. DOI: **10.3389/fmicb.2021.683260**. https://doi.org/10.3389/fmicb.2021.683260 (garg2021geneslinkingcopper pages 1-2, garg2021geneslinkingcopper pages 16-17, garg2021geneslinkingcopper pages 7-8)

**Additional contextual review (not 2023–2024 but provides inhibitor constants and superfamily distinctions):**
8. **Borisov VB, Forte E.** *Carbon Monoxide and Prokaryotic Energy Metabolism.* **International Journal of Molecular Sciences**. **2025-03**. DOI: **10.3390/ijms26062809**. https://doi.org/10.3390/ijms26062809 (borisov2025carbonmonoxideand pages 5-7)

**Oxidase test chemistry source (metadata suggests unclear journal venue):**
9. **Baldea C, Popvici R.** *The oxidase test for Staphylococus aureus.* **2023**. DOI not available in retrieved metadata. (baldea2023theoxidasetesta pages 3-4, baldea2023theoxidasetesta pages 1-3)


References

1. (baldea2023theoxidasetesta pages 3-4): C Baldea and R Popvici. The oxidase test for staphylococus aureus. Unknown journal, 2023.

2. (baldea2023theoxidasetest pages 3-4): C Baldea and R Popvici. The oxidase test for staphylococus aureus. Unknown journal, 2023.

3. (hederstedt2022diversityofcytochrome pages 1-2): Lars Hederstedt. Diversity of cytochrome c oxidase assembly proteins in bacteria. Microorganisms, 10:926, Apr 2022. URL: https://doi.org/10.3390/microorganisms10050926, doi:10.3390/microorganisms10050926. This article has 29 citations.

4. (borisov2025carbonmonoxideand pages 5-7): Vitaliy B. Borisov and Elena Forte. Carbon monoxide and prokaryotic energy metabolism. International Journal of Molecular Sciences, 26:2809, Mar 2025. URL: https://doi.org/10.3390/ijms26062809, doi:10.3390/ijms26062809. This article has 8 citations.

5. (nastasi2024membraneboundredoxenzyme pages 2-4): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

6. (khalfaouihassani2023theescherichiacoli pages 1-2): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 7 citations and is from a peer-reviewed journal.

7. (garg2021geneslinkingcopper pages 7-8): Nitanshu Garg, Aidan J. Taylor, Federica Pastorelli, Sarah E. Flannery, Phillip J. Jackson, Matthew P. Johnson, and David J. Kelly. Genes linking copper trafficking and homeostasis to the biogenesis and activity of the cbb3-type cytochrome c oxidase in the enteric pathogen campylobacter jejuni. Frontiers in Microbiology, Jun 2021. URL: https://doi.org/10.3389/fmicb.2021.683260, doi:10.3389/fmicb.2021.683260. This article has 11 citations and is from a peer-reviewed journal.

8. (garg2021geneslinkingcopper pages 1-2): Nitanshu Garg, Aidan J. Taylor, Federica Pastorelli, Sarah E. Flannery, Phillip J. Jackson, Matthew P. Johnson, and David J. Kelly. Genes linking copper trafficking and homeostasis to the biogenesis and activity of the cbb3-type cytochrome c oxidase in the enteric pathogen campylobacter jejuni. Frontiers in Microbiology, Jun 2021. URL: https://doi.org/10.3389/fmicb.2021.683260, doi:10.3389/fmicb.2021.683260. This article has 11 citations and is from a peer-reviewed journal.

9. (baldea2023theoxidasetesta pages 1-3): C Baldea and R Popvici. The oxidase test for staphylococus aureus. Unknown journal, 2023.

10. (baldea2023theoxidasetest pages 1-3): C Baldea and R Popvici. The oxidase test for staphylococus aureus. Unknown journal, 2023.

11. (garg2021geneslinkingcopper pages 16-17): Nitanshu Garg, Aidan J. Taylor, Federica Pastorelli, Sarah E. Flannery, Phillip J. Jackson, Matthew P. Johnson, and David J. Kelly. Genes linking copper trafficking and homeostasis to the biogenesis and activity of the cbb3-type cytochrome c oxidase in the enteric pathogen campylobacter jejuni. Frontiers in Microbiology, Jun 2021. URL: https://doi.org/10.3389/fmicb.2021.683260, doi:10.3389/fmicb.2021.683260. This article has 11 citations and is from a peer-reviewed journal.

12. (saha2024cytochromebdoxidase pages 2-3): Pallavi Saha, Samarpita Das, Harish K. Indurthi, Rohit Kumar, Arnab Roy, Nitin Pal Kalia, and Deepak K. Sharma. Cytochrome bd oxidase: an emerging anti-tubercular drug target. RSC medicinal chemistry, 15 3:769-787, Mar 2024. URL: https://doi.org/10.1039/d3md00587a, doi:10.1039/d3md00587a. This article has 23 citations and is from a peer-reviewed journal.

13. (seitz2024targetingtuberculosisnovel pages 1-3): Christian Seitz, Surl-Hee Ahn, Haixin Wei, Matson Kyte, Gregory M. Cook, Kurt L. Krause, and J. Andrew McCammon. Targeting tuberculosis: novel scaffolds for inhibiting cytochrome <i>bd</i> oxidase. Journal of Chemical Information and Modeling, 64:5232-5241, Jun 2024. URL: https://doi.org/10.1021/acs.jcim.4c00344, doi:10.1021/acs.jcim.4c00344. This article has 11 citations and is from a peer-reviewed journal.

14. (nastasi2024membraneboundredoxenzyme pages 1-2): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

15. (hederstedt2022diversityofcytochrome pages 2-4): Lars Hederstedt. Diversity of cytochrome c oxidase assembly proteins in bacteria. Microorganisms, 10:926, Apr 2022. URL: https://doi.org/10.3390/microorganisms10050926, doi:10.3390/microorganisms10050926. This article has 29 citations.

16. (nastasi2024membraneboundredoxenzyme pages 18-19): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

17. (gonzalezmontalvo2024therespiratorychain pages 1-2): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.