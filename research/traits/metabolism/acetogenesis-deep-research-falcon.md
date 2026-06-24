---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:49:15.845400'
end_time: '2026-06-18T04:03:05.841953'
duration_seconds: 830.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Acetogenesis
  trait_identifier: METPO:1000845
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: acetogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism that produces acetate as the primary end product through
    the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl
    pathway, typically performed by acetogenic bacteria under anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: Acetate fermentation
  evidence_summary: 'DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl
    Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation
    pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA
    (Supports acetyl-CoA formation from CO2 and CO in acetogens.)'
  causal_graph_summary: 'acetogenesis_wood_ljungdahl: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 84
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Acetogenesis
- **METPO identifier:** METPO:1000845
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that produces acetate as the primary end product through the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl pathway, typically performed by acetogenic bacteria under anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Acetate fermentation
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA (Supports acetyl-CoA formation from CO2 and CO in acetogens.)
- **Existing causal graph summary:** acetogenesis_wood_ljungdahl: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Acetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/acetogenesis.yaml`.

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
- **Trait label:** Acetogenesis
- **METPO identifier:** METPO:1000845
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that produces acetate as the primary end product through the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl pathway, typically performed by acetogenic bacteria under anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Acetate fermentation
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA (Supports acetyl-CoA formation from CO2 and CO in acetogens.)
- **Existing causal graph summary:** acetogenesis_wood_ljungdahl: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Acetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/acetogenesis.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Acetogenesis** (METPO:1000845)

### Scope summary (TraitMech curation)
**Acetogenesis** in METPO:1000845 corresponds to the **physiological capacity** to use the **Wood–Ljungdahl pathway (WLP; reductive acetyl‑CoA pathway)** under **anaerobic conditions** to reduce CO\(_2\) (or other C1 compounds such as CO, formate, methanol) and produce **acetate as the primary end product**, typically via acetyl‑CoA → acetyl‑phosphate → acetate with substrate-level phosphorylation. The WLP comprises a **methyl branch** (CO\(_2\)→formate→THF‑bound C1 units→methyl group) and a **carbonyl branch** (CO\(_2\)→CO), which converge at **CODH/ACS** to form acetyl‑CoA. (jezernik2024designofmicrobial pages 17-20, zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17)

**Boundary cases / distinctions**:
- **Acetate production ≠ canonical acetogenesis**: organisms may produce acetate without a complete WLP (e.g., acetate via glycine-mediated routes), so trait assignment should require WLP completeness and (ideally) coupling to energy conservation machinery (e.g., Rnf/Ech) rather than “acetate detected” alone. (cheng2024explorationofbiogas pages 41-45, cheng2024explorationofbiogasb pages 41-45)
- **WLP in Archaea or non-classical contexts** can be present without methanogenesis (e.g., WLP genomes lacking methyl‑CoM reductase), so “WLP present” is not equivalent to “methanogen.” (jezernik2024designofmicrobial pages 17-20)

### Key concepts and current understanding (mechanistic)
#### 1) Core biochemical definition of WLP-driven acetogenesis
A canonical WLP enzyme set includes **formate dehydrogenase (FDH) / hydrogen-dependent CO\(_2\) reductase (HDCR)**, **Fhs/FTS (formyl‑THF synthetase)**, **FolD/related cyclohydrolase and dehydrogenase activities**, **MTHFR (MetF/MetV)**, **methyltransferase(s)** to **CoFeSP**, and the **CODH/ACS** complex that synthesizes **acetyl‑CoA**. Acetyl‑CoA is converted to acetate by **PTA** and **ACK**, generating ATP via substrate-level phosphorylation. (zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17)

#### 2) Energetics: why redox/ion-pumping modules are part of the trait mechanism
Multiple sources emphasize that **WLP alone is ATP-neutral or yields no net ATP**, because ATP spent in formate activation offsets acetate-kinase ATP; therefore acetogens require **additional energy conservation** via membrane systems such as **Rnf** (ferredoxin:NAD\(^+\) oxidoreductase; ion pumping) or **Ech** (energy-converting hydrogenase; proton pumping) plus **ATP synthase**. (jezernik2024designofmicrobial pages 17-20, zhang2024engineeredacetogenicbacteria pages 2-3, basen2023editorialacetogens pages 1-2)

#### 3) Electron bifurcation/confurcation as a central coupling principle
Electron-bifurcating hydrogenases (e.g., **HydABC**) and transhydrogenases (e.g., **Nfn**) connect carrier pools (**ferredoxin, NAD(H), NADP(H)**), enabling thermodynamically challenging steps (reduced ferredoxin generation) that feed WLP reductions and ion-gradient generation. Structural/mechanistic work on HydABC shows how bifurcation enables low-potential ferredoxin reduction during H\(_2\) oxidation and is described as essential for fixation coupled to ATP synthesis in acetogens. (katsyv2023molecularbasisof pages 1-2, baum2024theenergyconvertinghydrogenase pages 2-5)

### Candidate mechanistic nodes (grouped for acetogenesis.yaml)

#### A) Pathways / modules
- **Wood–Ljungdahl pathway / reductive acetyl‑CoA pathway** (KEGG map00720; label acceptable) (jezernik2024designofmicrobial pages 17-20, zhang2024engineeredacetogenicbacteria pages 2-3)
- **Chemiosmotic energy conservation in acetogens** (Rnf/Ech → ion gradient → ATP synthase) (zhang2024engineeredacetogenicbacteria pages 2-3, basen2023editorialacetogens pages 1-2)
- **Electron bifurcation/confurcation module** (HydABC; Nfn) (katsyv2023molecularbasisof pages 1-2, baum2024theenergyconvertinghydrogenase pages 2-5)

#### B) Enzymes / complexes (gene-level where supported)
- **CODH/ACS** (CODH reduces CO\(_2\) to CO; ACS forms acetyl‑CoA) (zwerger2024aceticacidbioproduction pages 13-17)
- **FDH / HDCR** (CO\(_2\)→formate; in *A. woodii* HDCR includes hydrogenase subunit HydA2 and formate dehydrogenase subunits) (zwerger2024aceticacidbioproduction pages 13-17, moon2024redirectingelectronflow pages 1-2)
- **HydABC** (electron-bifurcating [FeFe]-hydrogenase) (moon2024redirectingelectronflow pages 1-2, katsyv2023molecularbasisof pages 1-2)
- **Rnf complex** (ferredoxin:NAD\(^+\) oxidoreductase; Na\(^+\)/H\(^+\) pumping) (zwerger2024aceticacidbioproduction pages 13-17, zhang2024engineeredacetogenicbacteria pages 2-3)
- **Ech complex** (Ech-type acetogens such as *Thermoanaerobacter kivui*) (baum2024theenergyconvertinghydrogenase pages 1-2, baum2024theenergyconvertinghydrogenase pages 2-5)
- **NfnAB** (ferredoxin/NAD(P) transhydrogenase; redox balancing) (jezernik2024designofmicrobial pages 17-20, baum2024theenergyconvertinghydrogenase pages 2-5)
- **Fhs/FTS, FolD-like activities, MTHFR (MetF/MetV), methyltransferase(s), CoFeSP** (methyl branch machinery) (zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17)
- **PTA, ACK** (acetate-forming ATP-yielding steps) (zhang2024engineeredacetogenicbacteria pages 2-3)

#### C) Chemicals / metabolites (CHEBI where clear)
- Carbon sources / electron acceptors: **CO\(_2\)** (CHEBI:16526), **CO** (CHEBI:17245), **formate** (CHEBI:15740) (zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17)
- Electron donor: **H\(_2\)** (CHEBI:18276) (zwerger2024aceticacidbioproduction pages 13-17, moon2024redirectingelectronflow pages 1-2)
- Key intermediates: **acetyl‑CoA** (CHEBI:15351), **acetyl‑phosphate** (CHEBI:15350) (zhang2024engineeredacetogenicbacteria pages 2-3)
- Products: **acetate** (CHEBI:30089), **ethanol** (CHEBI:16236) (elisiario2023aceticacidgrowth pages 4-6, allaart2023overflowmetabolismat pages 2-4)

#### D) Environmental / experimental factors (candidate nodes)
- **Anaerobiosis** (trait prerequisite) (zhang2024engineeredacetogenicbacteria pages 1-2)
- **pH / undissociated acetic acid** (drives inhibition and product shifts) (elisiario2023aceticacidgrowth pages 10-11, robazza2024acetateshockloads pages 1-2)
- **Gas–liquid mass transfer (CO availability)** (controls WLP flux, formate leakage) (elisiario2023aceticacidgrowth pages 4-6, elisiario2023aceticacidgrowth pages 1-3)
- **CO toxicity / CO-sensitive metalloenzymes** (CODH detox) (allaart2023overflowmetabolismat pages 2-4, allaart2023overflowmetabolismat pages 1-2)
- **Trace metals (W, Mo, Ni)** (required for key enzymes; W notable for FDH/AOR; Ni for CODH) (zwerger2024aceticacidbioproduction pages 13-17, jezernik2024designofmicrobial pages 71-74)

### Evidence-backed candidate causal edges (curation table)
The following table is formatted to support direct translation to `data/traits/metabolism/acetogenesis.yaml` as subject–predicate–object triples with evidence.

| Edge (S–P–O) | Evidence (short quote/snippet) | Reference (DOI + URL + year) | Notes/Uncertainty | Suggested identifiers |
|---|---|---|---|---|
| CO2 —[is reduced by FDH/HDCR to]→ formate | “FDH… reduces CO2 to formate”; “HDCR… catalyzes hydrogen-dependent CO2 reduction to formate” (zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540; Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Core methyl-branch step; exact enzyme architecture varies by taxon (standalone FDH vs HDCR complex). | CO2 CHEBI:16526; formate CHEBI:15740; FDH EC:1.17.1.9 / EC:1.17.98.3 (taxon-dependent); HDCR label-only |
| H2 —[donates electrons to]→ HDCR | “HydA2 oxidizes H2 and transfers electrons… to FdhF2 which reduces CO2 to formate” (zwerger2024aceticacidbioproduction pages 13-17) | Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Strong for A. woodii-type HDCR; taxon-specific architecture. | H2 CHEBI:18276; HydA2 label-only; FdhF/FdhF2 label-only; HDCR label-only |
| formate —[is converted by Fhs to]→ formyl-THF | “FTS (formyl-THF synthetase) converts formate to formyl-THF consuming 1 ATP” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Canonical WLP methyl-branch step. | formate CHEBI:15740; 10-formyl-THF CHEBI:15637; Fhs/FTS EC:6.3.4.3 |
| formyl-THF —[is converted by FolD/FTC-MDH activities to]→ methylene-THF | “5,10-methenyl-THF cyclohydrolase, and a NAD-dependent 5,10-methylene-THF dehydrogenase” (zwerger2024aceticacidbioproduction pages 13-17) | Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Intermediates collapsed for curation convenience; could be split into cyclohydrolase and dehydrogenase edges. | 10-formyl-THF CHEBI:15637; 5,10-methenyl-THF CHEBI:11304; 5,10-methylene-THF CHEBI:15635; FolD/FTC/MDH EC:3.5.4.9 and EC:1.5.1.5 |
| methylene-THF —[is reduced by MTHFR (MetF/MetV) to]→ methyl-THF | “MTHFR reduce methenyl-THF → methylene-THF → methyl-THF” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Common acetogen step; electron donor coupling differs among taxa. | 5,10-methylene-THF CHEBI:15635; 5-methyl-THF CHEBI:15636; MetF/MetV/MTHFR EC:1.5.1.20 |
| methyl-THF —[transfers methyl group via MT to]→ CoFeSP-bound methyl group | “MT transfers methyl to CoFeSP” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Canonical methyl transfer to corrinoid iron-sulfur protein. | methyl-THF CHEBI:15636; CoFeSP label-only; methyltransferase/acsE EC:2.1.1.258 |
| CO2 —[is reduced by CODH to]→ CO | “In the carbonyl branch CODH reduces CO2 to CO” (zwerger2024aceticacidbioproduction pages 13-17) | Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Central carbonyl-branch step. | CO2 CHEBI:16526; carbon monoxide CHEBI:17245; CODH/cooS or acsA EC:1.2.7.4 |
| CO + methyl-CoFeSP + CoA —[are condensed by ACS to form]→ acetyl-CoA | “ACS combines methyl, CoA and carbonyl to form acetyl-CoA” (zwerger2024aceticacidbioproduction pages 13-17) | Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Strong core edge for acetogenesis. | CO CHEBI:17245; CoA CHEBI:15346; acetyl-CoA CHEBI:15351; ACS/acsB EC:2.3.1.169 |
| acetyl-CoA —[is converted by PTA to]→ acetyl-phosphate | “PTA and ACK… convert acetyl-CoA to acetate” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Often modeled as two-step path PTA then ACK. | acetyl-CoA CHEBI:15351; acetyl phosphate CHEBI:15350; PTA EC:2.3.1.8 |
| acetyl-phosphate —[is converted by ACK to]→ acetate + ATP | “ACK (acetate kinase) convert acetyl-CoA to acetate, yielding ATP via SLP” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Trait-defining end-product step for acetate fermentation branch. | acetate CHEBI:30089; ATP CHEBI:15422; ACK EC:2.7.2.1 |
| HydABC —[oxidizes H2 and reduces]→ ferredoxin + NAD(P)H | “HydABC… oxidizes H2 while reducing NAD and ferredoxin”; “reduces low-potential ferredoxins by oxidizing hydrogen gas” (moon2024redirectingelectronflow pages 1-2, katsyv2023molecularbasisof pages 1-2) | Moon 2024, doi:10.1038/s41467-024-49680-5, https://doi.org/10.1038/s41467-024-49680-5; Katsyv 2023, doi:10.1021/jacs.2c11683, https://doi.org/10.1021/jacs.2c11683 | Strong mechanistic support for electron bifurcation; cofactor specificity can vary (NADH/NADPH). | H2 CHEBI:18276; ferredoxin label-only; NADH CHEBI:57945; NADPH CHEBI:16474; HydABC label-only |
| reduced ferredoxin —[drives Rnf to reduce]→ NAD+ | “Rnf transfers electrons from reduced ferredoxin (Fd2-) to NAD+” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | Core redox-balancing edge in Rnf-type acetogens. | ferredoxin(red) label-only; NAD+ CHEBI:57540; Rnf complex label-only |
| Rnf complex —[translocates]→ Na+ / H+ across membrane | “Rnf… pumping Na+ or H+”; “couples… electron flow to Na+ translocation” (zhang2024engineeredacetogenicbacteria pages 2-3, zwerger2024aceticacidbioproduction pages 13-17) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540; Zwerger 2024, doi:10.34726/hss.2024.114566, https://doi.org/10.34726/hss.2024.114566 | Ion specificity is taxon-dependent; Na+-coupling is especially strong for A. woodii. | sodium ion CHEBI:29101; proton CHEBI:15378; Rnf complex label-only |
| ion gradient —[drives]→ ATP synthase-dependent ATP production | “The ion gradient formed by Rnf/Ech drives ATP synthase to generate ATP” (zhang2024engineeredacetogenicbacteria pages 2-3) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540 | General chemiosmotic energy conservation in acetogens. | ATP synthase GO:0046933 / EC:7.1.2.2 or EC:7.1.2.1 (ion-dependent); ATP CHEBI:15422 |
| Ech hydrogenase —[couples ferredoxin/H+ interconversion to]→ proton motive force | “Ech… pumps H+”; “coupled to transmembrane ion-gradient formation” (zhang2024engineeredacetogenicbacteria pages 2-3, baum2024theenergyconvertinghydrogenase pages 1-2) | Zhang 2024, doi:10.3389/fbioe.2024.1395540, https://doi.org/10.3389/fbioe.2024.1395540; Baum 2024, doi:10.1128/spectrum.03380-23, https://doi.org/10.1128/spectrum.03380-23 | Strong for Ech-type acetogens such as T. kivui; not universal across all acetogens. | Ech complex label-only; proton motive force GO:0005739? / label-only |
| NfnAB —[rebalances]→ NADH/NADPH/ferredoxin pools | “Nfn… couples oxidation of two NADPH to reduction of one ferredoxin and one NAD+” (jezernik2024designofmicrobial pages 17-20) | Jezernik 2024 thesis (as gathered context), cited in evidence context pqac-00000023 | Useful redox node, but thesis source and taxon context make this weaker for broad curation. | NfnAB label-only; NADPH CHEBI:16474; NAD+ CHEBI:57540; ferredoxin label-only |
| WLP —[has net]→ zero ATP from substrate-level phosphorylation | “Because the WLP is net-zero ATP”; “WLP alone yields no net ATP” (jezernik2024designofmicrobial pages 17-20, basen2023editorialacetogens pages 1-2) | Jezernik 2024 thesis; Basen & Müller 2023, doi:10.3389/fmicb.2023.1186930, https://doi.org/10.3389/fmicb.2023.1186930 | Supports need for Rnf/Ech nodes in causal graph. | Wood–Ljungdahl pathway KEGG:map00720 / reductive acetyl-CoA pathway label-only |
| deletion of hydBA and hydA2 —[enables growth on]→ CO in A. woodii | “ΔhydBA/hydA2 mutant eventually adapts to grow on CO… tolerates up to 100% CO” (moon2024redirectingelectronflow pages 1-2) | Moon 2024, doi:10.1038/s41467-024-49680-5, https://doi.org/10.1038/s41467-024-49680-5 | Strong but taxon- and mutant-specific; curate as uncertain/contextual edge. | hydBA label-only; hydA2 label-only; carbon monoxide CHEBI:17245; Acetobacterium woodii NCBITaxon:33952 |
| hycB2 mutation —[increases]→ ferredoxin-dependent FDH/HDCR activity | “SNP analysis identified a fixed mutation in HycB2… increased ferredoxin-dependent FDH activities” (moon2024redirectingelectronflow pages 4-6, moon2024redirectingelectronflow pages 2-3) | Moon 2024, doi:10.1038/s41467-024-49680-5, https://doi.org/10.1038/s41467-024-49680-5 | Mutational inference; mechanistically plausible but should be marked uncertain until direct causality is isolated. | hycB2 label-only; FDH/HDCR label-only |
| CO —[is detoxified/oxidized by]→ CODH | “CODH is described as the first step in CO detoxification” (allaart2023overflowmetabolismat pages 2-4, allaart2023overflowmetabolismat pages 1-2) | Allaart 2023, doi:10.1111/1751-7915.14212, https://doi.org/10.1111/1751-7915.14212 | Good environmental/physiological edge for carboxydotrophic acetogens. | CO CHEBI:17245; CODH EC:1.2.7.4 |
| high CO influx —[increases]→ ethanol overflow metabolism | “at higher dilution rates ... more ethanol is produced”; overflow metabolism “to cope with high dissolved CO concentrations” (allaart2023overflowmetabolismat pages 2-4) | Allaart 2023, doi:10.1111/1751-7915.14212, https://doi.org/10.1111/1751-7915.14212 | More application/process than core trait; strongest in C. autoethanogenum. | carbon monoxide CHEBI:17245; ethanol CHEBI:16236; overflow metabolism label-only |
| low CO mass transfer —[causes]→ formate excretion | “Very low CO mass transfer causes excretion of formate” (elisiario2023aceticacidgrowth pages 1-3, elisiario2023aceticacidgrowth pages 10-11) | Elisiário 2023, doi:10.1007/s00253-023-12670-6, https://doi.org/10.1007/s00253-023-12670-6 | Process-specific but well supported; indicates WLP bottleneck. | formate CHEBI:15740; mass transfer label-only |
| increased undissociated acetic acid —[shifts metabolism toward]→ ethanol production | “undissociated acetic acid… governs ethanol yield and production rates”; “requires >20 mmol/L undissociated acetic acid” (elisiario2023aceticacidgrowth pages 1-3, elisiario2023aceticacidgrowth pages 10-11) | Elisiário 2023, doi:10.1007/s00253-023-12670-6, https://doi.org/10.1007/s00253-023-12670-6 | Strong for industrial CO fermentation; not a universal acetogenesis rule across all taxa. | acetic acid CHEBI:15366; ethanol CHEBI:16236 |
| H2-rich syngas —[increases specificity toward]→ acetate | “H2-rich feeding increased specificity toward acetate (86% of C-mol production)” (quintela2024influenceofhydrogen pages 4-5) | Quintela 2024, doi:10.3390/molecules29235653, https://doi.org/10.3390/molecules29235653 | Reactor/community-specific mixed culture result; valuable application edge. | H2 CHEBI:18276; acetate CHEBI:30089; syngas label-only |
| high acetate load + low pH —[suppresses]→ acetogenesis | “high acetate concentrations suppressed acetogenesis in favour of hydrogenogenesis” (robazza2024acetateshockloads pages 1-2) | Robazza 2024, doi:10.1111/1751-7915.70063, https://doi.org/10.1111/1751-7915.70063 | Mixed-culture process context; should be marked environmental/assay-specific. | acetate CHEBI:30089; hydrogenogenesis label-only; pH label-only |
| acetate supplementation at pH 5.5, 55°C —[increases]→ carboxydotrophic conversion rate | “increased carboxydotrophic conversion rates up to about 20-fold” (robazza2024acetateshockloads pages 1-2) | Robazza 2024, doi:10.1111/1751-7915.70063, https://doi.org/10.1111/1751-7915.70063 | Useful application/process edge, not core molecular mechanism. | acetate CHEBI:30089; temperature ENVO/label-only; carboxydotrophy label-only |
| Acetobacterium —[provides acetate/H2 that supports]→ Dehalococcoides dechlorination | “WLP drives anaerobic CO oxidation to produce H2 and acetate… Acetobacterium… carbon-source provider and protector against CO inhibition” (wang2024codrivenelectronand pages 1-3) | Wang 2024, doi:10.1186/s40168-024-01869-y, https://doi.org/10.1186/s40168-024-01869-y | Cross-feeding/application edge; not intrinsic to all acetogens. | Acetobacterium NCBITaxon:33950; acetate CHEBI:30089; H2 CHEBI:18276; Dehalococcoides NCBITaxon:12916 |
| some acetogens / acetogen-like organisms —[lack complete]→ WLP | “Microaceticoccus formicicus does not have a complete WLP but may perform glycine-mediated acetate synthesis” (cheng2024explorationofbiogasb pages 41-45) | Cheng 2024 thesis (as gathered context), cited in evidence context pqac-00000036 | Important boundary-case warning: acetate production ≠ canonical acetogenesis. | Wood–Ljungdahl pathway KEGG:map00720; glycine-mediated acetate synthesis label-only; Microaceticoccus formicicus label-only |


*Table: This table compiles curation-ready subject–predicate–object edges for microbial acetogenesis, spanning the Wood–Ljungdahl pathway, redox/energy conservation modules, and environmentally modulated process behaviors. It is useful as a direct starting artifact for TraitMech graph curation with evidence, uncertainty notes, and suggested ontology grounding.*

### Recent developments (prioritizing 2023–2024)

#### 1) New genotype→phenotype mechanistic insight: enabling CO growth in *Acetobacterium woodii*
A 2024 *Nature Communications* study demonstrated that deleting **two [FeFe]-hydrogenases** (**ΔhydBA/hydA2**) in *A. woodii* (normally unable to grow on CO) enabled **adapted growth on CO** after prolonged transfer/adaptation and tolerance up to 100% CO, supporting a causal link from hydrogenase architecture/CO sensitivity to acetogenic phenotype. Quantitatively, after adaptation the mutant achieved reported growth rates up to **μ ≈ 0.05 h\(^{-1}\)** and produced **~21–25 mM acetate** on CO. SNPs fixed in the population included **hycB2** (HDCR ferredoxin-like subunit) and transport genes; cell-free extracts showed substantially higher **ferredoxin-dependent FDH activities** consistent with rerouting electron flow toward ferredoxin-dependent CO\(_2\) reduction when H\(_2\)-dependent hydrogenase modules are removed. (moon2024redirectingelectronflow pages 1-2, moon2024redirectingelectronflow pages 2-3)

A schematic overview of this WLP/electron-flow architecture (HDCR, HydABC, Rnf) is shown in the paper’s figures. (moon2024redirectingelectronflow media aa062fb8, moon2024redirectingelectronflow media b463087f)

#### 2) High-performance acetogen isolates expanding trait diversity
A 2023 *Frontiers in Microbiology* study describing novel acetogenic isolates (family Eubacteriaceae) reported unusually high tolerance to C1 substrates (e.g., **100% CO at 200 kPa**, **700 mM formate**, **500 mM methanol**) and high growth rates (e.g., **0.45 h\(^{-1}\)** on 50% CO; **0.34 h\(^{-1}\)** on 200 mM formate). These quantitative phenotypes support curation of “acetogenesis” as a capacity that can vary widely by strain and substrate regime. (yu2023genomicpotentialand pages 1-2)

#### 3) Process/mechanism coupling: mass transfer, undissociated acetate, and formate leakage in syngas fermentation
A 2023 *Applied Microbiology and Biotechnology* study systematically tested how **CO mass transfer**, **growth rate**, and **acetic acid (undissociated)** govern product shifts in *Clostridium autoethanogenum* CO fermentation. It reports that low mass transfer led to significant **formate excretion** (interpreted as a WLP bottleneck at formate conversion under low dissolved CO), and identifies a quantitative condition for high ethanol yields: **>20 mmol/L undissociated acetic acid**. (elisiario2023aceticacidgrowth pages 4-6, elisiario2023aceticacidgrowth pages 10-11)

A 2024 mixed-culture syngas trickle-bed study found that **H\(_2\)-rich feeding** increased CO\(_2\) consumption and increased carbon specificity to acetate (**86% of C-mol**), reaching **18.6 g/L acetate** and a productivity of **9.0 g LEBV\(^{-1}\) day\(^{-1}\)**, illustrating how gas composition changes redox supply and WLP product endpoints at reactor scale. (quintela2024influenceofhydrogen pages 4-5)

#### 4) Environmental controls and inhibitors: CO toxicity and acetate/pH stress
A 2023 perspective on carboxydotrophic acetogens frames CO as “highly toxic” due to binding metal centers and argues detoxification relies on **high CODH activity** with turnover near diffusion-limited influx; it links higher growth rates to increased ethanol formation as an **overflow electron sink** to cope with variable CO influx/redox pressure. (allaart2023overflowmetabolismat pages 2-4, allaart2023overflowmetabolismat pages 1-2)

A 2024 mixed-culture study shows acetate can be tolerated at very high levels (up to **64 g/L**) yet shifts community function: high acetate loads and low pH increase undissociated acetic acid toxicity, inhibiting methanogenesis and—in non-methanogenic regimes—suppressing acetogenesis in favor of hydrogenogenesis and alternative carboxylates. It also reports acetate supplementation can increase CO conversion rates up to **~20-fold** at specific conditions (pH 5.5, 55°C, 48 g/L acetate). (robazza2024acetateshockloads pages 1-2)

### Current applications / implementations (real-world context)

1) **Industrial syngas fermentation / waste-gas biomanufacturing**: Syngas fermentation to ethanol has reached industrial production and is widely pursued using acetogens such as *C. autoethanogenum*; quantitative process performance and limitations (gas solubility/mass transfer, inhibition, redox balancing) are emphasized in 2023–2024 reviews and process studies. (ahuja2023aminireviewon pages 10-11, elisiario2023aceticacidgrowth pages 4-6)

2) **Liquid C1 carrier (formate) → acetate in continuous reactors**: A 2024 continuous bioreactor study with *A. woodii* on formate reports operationally relevant performance metrics, including an optimum acetate yield of **0.223 ± 0.002 mol/mol** at 300 mM formate and D=0.1–0.15 h\(^{-1}\), a highest volumetric acetate rate of **12.64 mmol L\(^{-1}\) h\(^{-1}\)** (3.77 g/L) at D=0.2 h\(^{-1}\), and a maximum acetate concentration of **4.1 g/L** at D=0.1 h\(^{-1}\). (zwerger2024aceticacidbioproduction pages 64-67)

3) **Microbiome-enabled remediation via syntrophy**: A 2024 *Microbiome* study shows CO-driven acetogenesis can produce H\(_2\) and acetate that support **reductive dechlorination** by *Dehalococcoides*, and reports CO concentrations >2.2 μM (previously considered detrimental) could still support growth when CO-utilizing partners were present, emphasizing community-context dependence of “CO inhibition.” (wang2024codrivenelectronand pages 1-3)

### Expert opinions / synthesis (authoritative perspectives)
- Basen & Müller (2023) emphasize that WLP alone does not provide net ATP and that acetogens require Rnf/Ech-linked energy conservation and electron bifurcation to connect redox balancing to ATP generation. (basen2023editorialacetogens pages 1-2)
- A 2024 review on acetogen engineering summarizes the canonical WLP enzymology (FDH→Fhs→MTHFR→CODH/ACS→PTA/ACK) and the need for Rnf/Ech to couple ferredoxin oxidation to ion gradients and ATP synthesis, framing these as key bottlenecks for high-value product formation. (zhang2024engineeredacetogenicbacteria pages 2-3)
- Structural enzymology (HydABC) provides mechanistic underpinnings for electron bifurcation as a general principle enabling acetogenesis at low energy yields. (katsyv2023molecularbasisof pages 1-2)

### Warnings / non-curatable or “curate with caution” claims
1) **“Acetate present” is insufficient**: acetate can arise from non-WLP routes; for trait assignment and graph edges, prefer evidence of complete WLP enzyme complement and/or diagnostic genes/complexes plus anaerobic physiology. (cheng2024explorationofbiogasb pages 41-45, cheng2024explorationofbiogas pages 41-45)
2) **Process-dependent edges** (mass transfer, undissociated acetate thresholds, mixed-culture community shifts) are valid causal statements but should be curated as **assay-/environment-specific** modulators rather than universal organism-level mechanisms. (elisiario2023aceticacidgrowth pages 10-11, robazza2024acetateshockloads pages 1-2)
3) **Mutation→mechanism edges** (e.g., hycB2 SNP increasing ferredoxin-dependent FDH activity) are compelling but should be marked **UNCERTAIN** unless causality is isolated (e.g., allele swap). (moon2024redirectingelectronflow pages 4-6, moon2024redirectingelectronflow pages 2-3)

---

## DOI-first bibliography (with URLs and publication dates where available)

- Moon J, Poehlein A, Daniel R, Müller V. **Redirecting electron flow in *Acetobacterium woodii* enables growth on CO and improves growth on formate.** *Nature Communications*. **2024-06**. doi:10.1038/s41467-024-49680-5. https://doi.org/10.1038/s41467-024-49680-5 (moon2024redirectingelectronflow pages 1-2)
- Zhang J-Z, et al. **Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals.** *Frontiers in Bioengineering and Biotechnology*. **2024-07**. doi:10.3389/fbioe.2024.1395540. https://doi.org/10.3389/fbioe.2024.1395540 (zhang2024engineeredacetogenicbacteria pages 2-3)
- Bae J, et al. **Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.** *RSC Chemical Biology*. **2024-07**. doi:10.1039/d4cb00099d. https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 8-9)
- Quintela C, et al. **Influence of Hydrogen and Ethanol Addition in Methanogen-Free Mixed Culture Syngas Fermentations in Trickle Bed Reactors.** *Molecules*. **2024-11**. doi:10.3390/molecules29235653. https://doi.org/10.3390/molecules29235653 (quintela2024influenceofhydrogen pages 4-5)
- Robazza A, et al. **Acetate Shock Loads Enhance CO Uptake Rates of Anaerobic Microbiomes.** *Microbial Biotechnology*. **2024-12**. doi:10.1111/1751-7915.70063. https://doi.org/10.1111/1751-7915.70063 (robazza2024acetateshockloads pages 1-2)
- Wang J, et al. **CO-driven electron and carbon flux fuels synergistic microbial reductive dechlorination.** *Microbiome*. **2024-08**. doi:10.1186/s40168-024-01869-y. https://doi.org/10.1186/s40168-024-01869-y (wang2024codrivenelectronand pages 1-3)
- Baum C, et al. **The energy-converting hydrogenase Ech2 is important for the growth of the thermophilic acetogen *Thermoanaerobacter kivui* on ferredoxin-dependent substrates.** *Microbiology Spectrum*. **2024-04**. doi:10.1128/spectrum.03380-23. https://doi.org/10.1128/spectrum.03380-23 (baum2024theenergyconvertinghydrogenase pages 1-2)
- Yu J, et al. **Genomic potential and physiological characteristics of C1 metabolism in novel acetogenic bacteria.** *Frontiers in Microbiology*. **2023-10**. doi:10.3389/fmicb.2023.1279544. https://doi.org/10.3389/fmicb.2023.1279544 (yu2023genomicpotentialand pages 1-2)
- Elisiário MP, et al. **Acetic acid, growth rate, and mass transfer govern shifts in CO metabolism of *Clostridium autoethanogenum*.** *Applied Microbiology and Biotechnology*. **2023-07**. doi:10.1007/s00253-023-12670-6. https://doi.org/10.1007/s00253-023-12670-6 (elisiario2023aceticacidgrowth pages 1-3)
- Basen M, Müller V. **Editorial: Acetogens – from the origin of life to biotechnological applications.** *Frontiers in Microbiology*. **2023-04**. doi:10.3389/fmicb.2023.1186930. https://doi.org/10.3389/fmicb.2023.1186930 (basen2023editorialacetogens pages 1-2)
- Katsyv A, et al. **Molecular Basis of the Electron Bifurcation Mechanism in the [FeFe]-Hydrogenase Complex HydABC.** *Journal of the American Chemical Society*. **2023-02**. doi:10.1021/jacs.2c11683. https://doi.org/10.1021/jacs.2c11683 (katsyv2023molecularbasisof pages 1-2)
- Allaart MT, et al. **Overflow metabolism at the thermodynamic limit of life: How carboxydotrophic acetogens mitigate carbon monoxide toxicity.** *Microbial Biotechnology*. **2023-01**. doi:10.1111/1751-7915.14212. https://doi.org/10.1111/1751-7915.14212 (allaart2023overflowmetabolismat pages 2-4)
- Ahuja V, et al. **A Mini-Review on Syngas Fermentation to Bio-Alcohols: Current Status and Challenges.** *Sustainability*. **2023-02**. doi:10.3390/su15043765. https://doi.org/10.3390/su15043765 (ahuja2023aminireviewon pages 10-11)
- Zwerger P. **Acetic Acid Bioproduction by *Acetobacterium woodii* in Formate Medium in Continuous Bioreactors.** TU Wien thesis. **2024-01**. doi:10.34726/hss.2024.114566. https://doi.org/10.34726/hss.2024.114566 (zwerger2024aceticacidbioproduction pages 64-67)
- Cheng G. **Exploration of biogas systems to unveil the acetogen community.** (thesis; limited bibliographic metadata in retrieved text). **2024**. (cheng2024explorationofbiogas pages 41-45)


References

1. (jezernik2024designofmicrobial pages 17-20): MI Jezernik. Design of microbial co-cultures for hydrogen and carbon dioxide based chain elongation to medium chain fatty acids. Unknown journal, 2024.

2. (zhang2024engineeredacetogenicbacteria pages 2-3): Jun-Zhe Zhang, Yu-Zhen Li, Zhi-Ning Xi, Hui-Peng Gao, Quan Zhang, Li-Cheng Liu, Fu-Li Li, and Xiao-Qing Ma. Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals. Frontiers in Bioengineering and Biotechnology, Jul 2024. URL: https://doi.org/10.3389/fbioe.2024.1395540, doi:10.3389/fbioe.2024.1395540. This article has 26 citations.

3. (zwerger2024aceticacidbioproduction pages 13-17): Paul Zwerger. Acetic acid bioproduction by acetobacterium woodii in formate medium in continuous bioreactors. Text, Jan 2024. URL: https://doi.org/10.34726/hss.2024.114566, doi:10.34726/hss.2024.114566. This article has 0 citations and is from a peer-reviewed journal.

4. (cheng2024explorationofbiogas pages 41-45): G Cheng. Exploration of biogas systems to unveil the acetogen community. Unknown journal, 2024.

5. (cheng2024explorationofbiogasb pages 41-45): G Cheng. Exploration of biogas systems to unveil the acetogen community. Unknown journal, 2024.

6. (basen2023editorialacetogens pages 1-2): Mirko Basen and Volker Müller. Editorial: acetogens - from the origin of life to biotechnological applications. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1186930, doi:10.3389/fmicb.2023.1186930. This article has 7 citations and is from a peer-reviewed journal.

7. (katsyv2023molecularbasisof pages 1-2): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 74 citations and is from a highest quality peer-reviewed journal.

8. (baum2024theenergyconvertinghydrogenase pages 2-5): Christoph Baum, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. The energy-converting hydrogenase ech2 is important for the growth of the thermophilic acetogen <i>thermoanaerobacter kivui</i> on ferredoxin-dependent substrates. Apr 2024. URL: https://doi.org/10.1128/spectrum.03380-23, doi:10.1128/spectrum.03380-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (moon2024redirectingelectronflow pages 1-2): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

10. (baum2024theenergyconvertinghydrogenase pages 1-2): Christoph Baum, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. The energy-converting hydrogenase ech2 is important for the growth of the thermophilic acetogen <i>thermoanaerobacter kivui</i> on ferredoxin-dependent substrates. Apr 2024. URL: https://doi.org/10.1128/spectrum.03380-23, doi:10.1128/spectrum.03380-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (elisiario2023aceticacidgrowth pages 4-6): Marina P. Elisiário, Wouter Van Hecke, Heleen De Wever, Henk Noorman, and Adrie J. J. Straathof. Acetic acid, growth rate, and mass transfer govern shifts in co metabolism of clostridium autoethanogenum. Applied Microbiology and Biotechnology, 107:5329-5340, Jul 2023. URL: https://doi.org/10.1007/s00253-023-12670-6, doi:10.1007/s00253-023-12670-6. This article has 12 citations and is from a domain leading peer-reviewed journal.

12. (allaart2023overflowmetabolismat pages 2-4): Maximilienne T. Allaart, Martijn Diender, Diana Z. Sousa, and Robbert Kleerebezem. Overflow metabolism at the thermodynamic limit of life: how carboxydotrophic acetogens mitigate carbon monoxide toxicity. Microbial Biotechnology, 16:697-705, Jan 2023. URL: https://doi.org/10.1111/1751-7915.14212, doi:10.1111/1751-7915.14212. This article has 42 citations and is from a peer-reviewed journal.

13. (zhang2024engineeredacetogenicbacteria pages 1-2): Jun-Zhe Zhang, Yu-Zhen Li, Zhi-Ning Xi, Hui-Peng Gao, Quan Zhang, Li-Cheng Liu, Fu-Li Li, and Xiao-Qing Ma. Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals. Frontiers in Bioengineering and Biotechnology, Jul 2024. URL: https://doi.org/10.3389/fbioe.2024.1395540, doi:10.3389/fbioe.2024.1395540. This article has 26 citations.

14. (elisiario2023aceticacidgrowth pages 10-11): Marina P. Elisiário, Wouter Van Hecke, Heleen De Wever, Henk Noorman, and Adrie J. J. Straathof. Acetic acid, growth rate, and mass transfer govern shifts in co metabolism of clostridium autoethanogenum. Applied Microbiology and Biotechnology, 107:5329-5340, Jul 2023. URL: https://doi.org/10.1007/s00253-023-12670-6, doi:10.1007/s00253-023-12670-6. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (robazza2024acetateshockloads pages 1-2): Alberto Robazza, Ada Raya i Garcia, Flávio C. F. Baleeiro, Sabine Kleinsteuber, and Anke Neumann. Acetate shock loads enhance co uptake rates of anaerobic microbiomes. Microbial Biotechnology, Dec 2024. URL: https://doi.org/10.1111/1751-7915.70063, doi:10.1111/1751-7915.70063. This article has 3 citations and is from a peer-reviewed journal.

16. (elisiario2023aceticacidgrowth pages 1-3): Marina P. Elisiário, Wouter Van Hecke, Heleen De Wever, Henk Noorman, and Adrie J. J. Straathof. Acetic acid, growth rate, and mass transfer govern shifts in co metabolism of clostridium autoethanogenum. Applied Microbiology and Biotechnology, 107:5329-5340, Jul 2023. URL: https://doi.org/10.1007/s00253-023-12670-6, doi:10.1007/s00253-023-12670-6. This article has 12 citations and is from a domain leading peer-reviewed journal.

17. (allaart2023overflowmetabolismat pages 1-2): Maximilienne T. Allaart, Martijn Diender, Diana Z. Sousa, and Robbert Kleerebezem. Overflow metabolism at the thermodynamic limit of life: how carboxydotrophic acetogens mitigate carbon monoxide toxicity. Microbial Biotechnology, 16:697-705, Jan 2023. URL: https://doi.org/10.1111/1751-7915.14212, doi:10.1111/1751-7915.14212. This article has 42 citations and is from a peer-reviewed journal.

18. (jezernik2024designofmicrobial pages 71-74): MI Jezernik. Design of microbial co-cultures for hydrogen and carbon dioxide based chain elongation to medium chain fatty acids. Unknown journal, 2024.

19. (moon2024redirectingelectronflow pages 4-6): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

20. (moon2024redirectingelectronflow pages 2-3): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

21. (quintela2024influenceofhydrogen pages 4-5): Cesar Quintela, Iulian-Gabriel Alexe, Yvonne Nygård, Lisbeth Olsson, Ioannis V. Skiadas, and Hariklia N. Gavala. Influence of hydrogen and ethanol addition in methanogen-free mixed culture syngas fermentations in trickle bed reactors. Molecules, 29:5653, Nov 2024. URL: https://doi.org/10.3390/molecules29235653, doi:10.3390/molecules29235653. This article has 3 citations.

22. (wang2024codrivenelectronand pages 1-3): Jingjing Wang, Xiuying Li, Huijuan Jin, Shujing Yang, Lian Yu, Hongyan Wang, Siqi Huang, Hengyi Liao, Xuhao Wang, Jun Yan, and Yi Yang. Co-driven electron and carbon flux fuels synergistic microbial reductive dechlorination. Microbiome, Aug 2024. URL: https://doi.org/10.1186/s40168-024-01869-y, doi:10.1186/s40168-024-01869-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

23. (moon2024redirectingelectronflow media aa062fb8): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

24. (moon2024redirectingelectronflow media b463087f): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

25. (yu2023genomicpotentialand pages 1-2): Jihyun Yu, Mi-Jeong Park, Joungmin Lee, Soo Jae Kwon, Jae Kyu Lim, Hyun Sook Lee, Sung Gyun Kang, Jung-Hyun Lee, Kae Kyoung Kwon, and Yun Jae Kim. Genomic potential and physiological characteristics of c1 metabolism in novel acetogenic bacteria. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1279544, doi:10.3389/fmicb.2023.1279544. This article has 2 citations and is from a peer-reviewed journal.

26. (ahuja2023aminireviewon pages 10-11): Vishal Ahuja, Arvind Kumar Bhatt, Balasubramani Ravindran, Yung-Hun Yang, and Shashi Kant Bhatia. A mini-review on syngas fermentation to bio-alcohols: current status and challenges. Sustainability, 15:3765, Feb 2023. URL: https://doi.org/10.3390/su15043765, doi:10.3390/su15043765. This article has 25 citations.

27. (zwerger2024aceticacidbioproduction pages 64-67): Paul Zwerger. Acetic acid bioproduction by acetobacterium woodii in formate medium in continuous bioreactors. Text, Jan 2024. URL: https://doi.org/10.34726/hss.2024.114566, doi:10.34726/hss.2024.114566. This article has 0 citations and is from a peer-reviewed journal.

28. (bae2024harnessingacetogenicbacteria pages 8-9): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.