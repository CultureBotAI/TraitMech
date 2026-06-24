---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:23:50.603561'
end_time: '2026-06-17T23:54:00.310657'
duration_seconds: 1809.71
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range low
  trait_identifier: METPO:1000469
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl range phenotype in which the upper bound of growth-supporting
    NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic
    or halotolerant organisms.
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Non-halophile, NaR_<=1
  evidence_summary: "DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review\
    \ supports growth limited to \u2264 ~1% NaCl as the non-halophilic / halotolerant\
    \ range.)"
  causal_graph_summary: 'nacl_range_low_non_halophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range low
- **METPO identifier:** METPO:1000469
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the upper bound of growth-supporting NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Non-halophile, NaR_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports growth limited to ≤ ~1% NaCl as the non-halophilic / halotolerant range.)
- **Existing causal graph summary:** nacl_range_low_non_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_low.yaml`.

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
- **Trait label:** NaCl range low
- **METPO identifier:** METPO:1000469
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the upper bound of growth-supporting NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Non-halophile, NaR_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports growth limited to ≤ ~1% NaCl as the non-halophilic / halotolerant range.)
- **Existing causal graph summary:** nacl_range_low_non_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_low.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **NaCl range low** (METPO:1000469)

## Scope summary (trait meaning and boundary cases)

**Trait definition (curation target).** *NaCl range low* is an environmental growth-range phenotype whose **upper bound** of growth-supporting NaCl concentration is **≤ ~1% (w/v)** (≈0.17–0.2 M), characteristic of **non-halophilic** or only weakly **halotolerant** organisms. This corresponds to classification schemes in which **non-halophilic microorganisms show optimum growth at <1% NaCl**, while **slight halophiles** begin at **~1–3% (w/v)** NaCl. (reang2022plantgrowthpromoting pages 1-2, reang2022plantgrowthpromoting media f999e5a2)

**Distinguishing from nearby traits.**
- **Halotolerant** organisms are defined by the ability to grow *with or without* salt and may tolerate substantially higher NaCl (e.g., up to 6–8% or more depending on scheme); thus, halotolerance is **not equivalent** to *NaCl range low* unless the **growth upper bound** itself remains ≤1%. (reang2022plantgrowthpromoting pages 1-2, reang2022plantgrowthpromoting media f999e5a2)
- **Halophiles** have growth optima above this range (e.g., moderate halophiles at 3–15% w/v; extreme halophiles at 15–30% w/v). (reang2022plantgrowthpromoting pages 1-2, reang2022plantgrowthpromoting media f999e5a2)

**Boundary cases to watch during curation.**
1. **“Optimum <1% NaCl” vs “upper bound ≤1% NaCl”:** A strain can have an optimum below 1% but still grow above 1%; such cases should **not** be curated as *NaCl range low*. (reang2022plantgrowthpromoting pages 1-2)
2. **Medium composition artifacts:** rich media may contain osmoprotectants (e.g., glycine betaine from yeast extract), effectively shifting apparent salt tolerance; these should be treated as **assay factors** rather than intrinsic trait mechanisms. (xing2024thepolyextremophilenatranaerobius pages 17-19)

## Key concepts and current mechanistic understanding (with 2023–2024 emphasis)

### Osmotic challenge and layered bacterial responses
**Hyperosmotic upshift (increasing NaCl)** typically causes water efflux and loss of turgor, prompting a staged response: rapid **K+ import** (ionic “first response”) followed by **compatible-solute accumulation** and subsequent reduction of cytoplasmic ionic strength (export of K+ as needed). A Streptomyces-focused 2023 review reports quantitative examples of the K+ emergency response (e.g., *B. subtilis* intracellular K+ rising from ~350–700 mM within 1 hour when exposed to 400 mM NaCl). (bhowmick2023osmoticstressresponses pages 3-4)

**Hypoosmotic shock (decreasing osmolarity)** risks cell rupture from excess turgor; mechanosensitive channels (notably **MscL/MscS**) open transiently to release solutes and prevent lysis. (bhowmick2023osmoticstressresponses pages 3-4)

### Master regulation of cell volume by **c-di-AMP** (2024 synthesis)
A 2024 *Microbiology and Molecular Biology Reviews* article argues that **c-di-AMP is a master regulator of cell volume**, largely by coordinating K+ homeostasis and compatible-solute uptake. It reports (i) **high-affinity c-di-AMP binding** to gating subunits of Trk/Ktr systems (KD ~40 nM–8 µM) that inhibits K+ influx, (ii) inhibition of **KUP-family** K+ import (e.g., **KimA**), and (iii) regulation of compatible-solute ABC importers (e.g., **OpuA/OpuC**) and transcriptional control via **BusR** (an opuA repressor that binds c-di-AMP, KD ≈ 10 µM). (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13)

This regulatory layer matters for *NaCl range low* curation because it explains why many non-halophiles are **not configured** to sustain growth at higher salinity: they may lack effective compatible-solute uptake/biosynthesis capacity and/or have tightly regulated uptake to avoid lethal over-accumulation. (foster2024bacterialcellvolume pages 12-13)

### Osmoprotectants and transport: glycine betaine pathway and BetT (2024 mechanistic advance)
A 2024 *Science Advances* study resolves the osmoregulated **choline transporter BetT** structure/mechanism in *Pseudomonas syringae*, supporting the canonical pathway: **choline uptake → glycine betaine synthesis → osmoprotection**. It reports that BetT is held in a **low-activity autoinhibited state** (via a C-terminal domain) under non-stress conditions, and **hyperosmotic activation releases** this autoinhibition. (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 5-6)

## Candidate causal-graph nodes (grouped)

A curation-oriented set of nodes (environmental factors, processes, regulators, transporters/channels, osmolytes, and phenotypic outcomes) is provided here:

| Node label | Node type | Role in graph | Evidence | Suggested grounding |
|---|---|---|---|---|
| **Environmental / assay factors** |||||
| NaCl concentration | environmental factor | upstream stressor | (reang2022plantgrowthpromoting pages 1-2, bhowmick2023osmoticstressresponses pages 3-4, adams2023engineeringosmolysissusceptibility pages 1-2) | CHEBI:26710 |
| NaCl range low (<=~1% w/v) | phenotype | outcome / target trait | (reang2022plantgrowthpromoting pages 1-2, reang2022plantgrowthpromoting media f999e5a2) | METPO:1000469 |
| Hyperosmotic stress | process | upstream stressor | (bhowmick2023osmoticstressresponses pages 3-4, yang2024structureandmechanism pages 1-2) | GO:0006970 |
| Hypoosmotic shock | process | upstream stressor | (bhowmick2023osmoticstressresponses pages 3-4, adams2023engineeringosmolysissusceptibility pages 1-2, marjan2024experimentalandtheoretical pages 18-22) | label-only |
| Osmotic stress | process | upstream stressor / integrative process | (foster2024bacterialcellvolume pages 8-10, warneke2024dara—thecentralprocessing pages 1-2) | GO:0006970 |
| Distilled water downshock | assay factor | assay-specific stressor | (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 7-8) | label-only |
| 4% NaCl pre-growth condition | assay factor | assay-specific sensitizing condition | (adams2023engineeringosmolysissusceptibility pages 1-2) | label-only |
| **Processes** |||||
| Potassium uptake | process | mediator | (bhowmick2023osmoticstressresponses pages 3-4, foster2024bacterialcellvolume pages 8-10, warneke2024dara—thecentralprocessing pages 1-2) | GO:0006813 |
| Compatible solute accumulation | process | mediator | (bhowmick2023osmoticstressresponses pages 3-4, foster2024bacterialcellvolume pages 6-8, yang2024structureandmechanism pages 1-2) | label-only |
| Glycine betaine uptake | process | mediator | (foster2024bacterialcellvolume pages 10-12, yang2024structureandmechanism pages 1-2) | label-only |
| Choline uptake | process | mediator | (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 2-3) | label-only |
| Glycine betaine biosynthesis | process | mediator | (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 7-8) | label-only |
| Mechanosensitive channel opening | process | mediator | (bhowmick2023osmoticstressresponses pages 3-4, marjan2024experimentalandtheoretical pages 18-22, morra2023arfaantisenserna pages 1-4) | label-only |
| Solute release after downshock | process | mediator | (marjan2024experimentalandtheoretical pages 18-22, morra2023arfaantisenserna pages 1-4) | label-only |
| Cell volume regulation | process | mediator | (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 12-13) | label-only |
| **Regulators / signaling molecules** |||||
| c-di-AMP | metabolite | mediator / regulator | (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12, warneke2024dara—thecentralprocessing pages 1-2) | CHEBI:90853 |
| c-di-AMP riboswitch | process | mediator / regulator | (foster2024bacterialcellvolume pages 8-10, warneke2024dara—thecentralprocessing pages 1-2) | label-only |
| BusR | protein | mediator / transcriptional regulator | (foster2024bacterialcellvolume pages 10-12) | label-only |
| **Transporters and channel proteins / complexes** |||||
| MscL | protein | mediator | (adams2023engineeringosmolysissusceptibility pages 1-2, marjan2024experimentalandtheoretical pages 18-22, morra2023arfaantisenserna pages 1-4) | label-only |
| MscS | protein | mediator | (adams2023engineeringosmolysissusceptibility pages 1-2, marjan2024experimentalandtheoretical pages 18-22, morra2023arfaantisenserna pages 1-4) | label-only |
| KdpFABC | complex | mediator | (hu2024cdiampaccumulationimpairs pages 13-14, hu2024cdiampaccumulationimpairs pages 2-6, warneke2024dara—thecentralprocessing pages 1-2) | label-only |
| KdpD | protein | mediator / regulator | (hu2024cdiampaccumulationimpairs pages 13-14, foster2024bacterialcellvolume pages 8-10, hu2024cdiampaccumulationimpairs pages 2-6) | label-only |
| Ktr system | complex | mediator | (hu2024cdiampaccumulationimpairs pages 13-14, foster2024bacterialcellvolume pages 8-10, hu2024cdiampaccumulationimpairs pages 2-6) | label-only |
| KtrC | protein | mediator | (foster2024bacterialcellvolume pages 10-12, hu2024cdiampaccumulationimpairs pages 2-6) | label-only |
| Trk/Ktr gating subunits | protein | mediator | (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8) | label-only |
| KimA (KUP-family K+/H+ symporter) | protein | mediator | (foster2024bacterialcellvolume pages 8-10, warneke2024dara—thecentralprocessing pages 1-2) | label-only |
| OpuA | complex | mediator | (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) | label-only |
| OpuC | complex | mediator | (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) | label-only |
| BetT | protein | mediator | (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 5-6, yang2024structureandmechanism pages 2-3) | label-only |
| **Metabolites / osmolytes / ions** |||||
| Potassium ion (K+) | metabolite | mediator | (bhowmick2023osmoticstressresponses pages 3-4, foster2024bacterialcellvolume pages 8-10, warneke2024dara—thecentralprocessing pages 1-2) | CHEBI:29103 |
| Choline | metabolite | mediator | (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 2-3) | CHEBI:15354 |
| Glycine betaine | metabolite | mediator | (foster2024bacterialcellvolume pages 10-12, yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 7-8) | CHEBI:17750 |
| Trehalose | metabolite | mediator | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12) | CHEBI:16588 |
| Proline | metabolite | mediator | (bhowmick2023osmoticstressresponses pages 3-4, foster2024bacterialcellvolume pages 10-12) | CHEBI:26271 |
| Glutamate | metabolite | mediator | (warneke2024dara—thecentralprocessing pages 1-2) | CHEBI:29985 |
| **Phenotypes / outcomes** |||||
| Cell growth | phenotype | outcome | (foster2024bacterialcellvolume pages 10-12, hu2024cdiampaccumulationimpairs pages 2-6, adams2023engineeringosmolysissusceptibility pages 1-2) | GO:0040007 |
| Osmotic sensitivity | phenotype | outcome | (foster2024bacterialcellvolume pages 6-8, hu2024cdiampaccumulationimpairs pages 2-6) | label-only |
| Cell survival after downshock | phenotype | outcome | (adams2023engineeringosmolysissusceptibility pages 1-2, marjan2024experimentalandtheoretical pages 18-22) | label-only |
| Cell lysis / osmolysis | phenotype | outcome | (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 7-8) | label-only |


*Table: This table lists candidate nodes for a TraitMech-style causal graph around the NaCl range low phenotype, emphasizing stress inputs, osmoadaptation mediators, transport systems, osmolytes, and growth/lysis outcomes. It is useful for turning the literature into curation-ready graph components with suggested ontology grounding.*

## Evidence-backed candidate causal edges (triples)

The following table provides proposed causal edges with **direct evidence snippets**, **DOI URLs**, **dates**, and **curation notes** (including uncertainty flags and scope mismatches with the <=1% phenotype).

| Edge (Subject —predicate→ Object) | Direction | Evidence source | DOI URL | Publication date | Quote/snippet | Notes for curation | Suggested ontology grounding |
|---|---|---|---|---|---|---|---|
| increased NaCl concentration —causes→ hyperosmotic stress | NaCl increase | Bhowmick 2023, *microLife* | https://doi.org/10.1093/femsml/uqad020 | Apr 2023 | “Hyperosmotic upshift elicits rapid K+ import as an emergency response” (bhowmick2023osmoticstressresponses pages 3-4) | General bacterial/osmotic-stress edge; evidence text is from streptomycete-focused review, so phenotype context is taxon-biased. Useful as upstream environmental edge, but not specific to `NaCl range low` organisms. | sodium chloride: CHEBI:26710; osmotic stress: GO:0006970 |
| hyperosmotic stress —induces→ potassium uptake | NaCl increase | Bhowmick 2023, *microLife* | https://doi.org/10.1093/femsml/uqad020 | Apr 2023 | “B. subtilis raises intracellular K+ from ~350–700 mM within 1 hour when exposed to 400 mM NaCl” and “S. griseus shows a sharp intracellular K+ rise at NaCl >0.75 M” (bhowmick2023osmoticstressresponses pages 3-4) | Strong mechanistic edge for osmotic adaptation. Quantitative but from salt stress above the `<=1%` trait threshold; curate as general mechanism, not as defining mechanism for low-NaCl trait itself. | potassium ion: CHEBI:29103; potassium ion transport: GO:0006813; K+ uptake system label node |
| increased Na+ concentration —upregulates→ Trk potassium transporter (TrkH/TrkA) | NaCl increase | Xing 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00145-24 | May 2024 | “trkH (Nther_0255) and trkA (Nther_0254) are upregulated (notably trkH 1.81 at 3.1 vs 2.5 M)” (xing2024thepolyextremophilenatranaerobius pages 6-7) | Taxon-specific to *Natranaerobius thermophilus*, a polyextremophile growing at 2.5–5.0 M Na+. Good transporter-level edge, but very weak candidate for direct curation into `NaCl range low` because it reflects high-salt adaptation in an extreme halophile. | trkH gene label; trkA gene label; potassium transport: GO:0006813 |
| hyperosmotic stress —induces→ compatible solute accumulation | NaCl increase | Bhowmick 2023, *microLife* | https://doi.org/10.1093/femsml/uqad020 | Apr 2023 | “After K+ import, cells synthesize or import compatible solutes and export K+ to reduce cytoplasmic ionic strength” (bhowmick2023osmoticstressresponses pages 3-4) | Broad, review-level edge; useful backbone relation for osmoadaptation graph. | compatible solute accumulation: GO label candidate; osmotic stress: GO:0006970 |
| hyperosmotic stress —increases→ proline accumulation | NaCl increase | Bhowmick 2023, *microLife* | https://doi.org/10.1093/femsml/uqad020 | Apr 2023 | “Proline is a major compatible solute in streptomycetes: in S. griseus proline rose from <6% to ~50% of the free amino acid pool under 1 M salt” (bhowmick2023osmoticstressresponses pages 3-4) | Good quantitative edge, but assay/taxon specific and at high salt (1 M). Supportive for general mechanism only. | L-proline: CHEBI:26271; response to osmotic stress: GO:0006970 |
| increased Na+ concentration —increases→ intracellular glycine betaine | NaCl increase | Xing 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00145-24 | May 2024 | “intracellular glycine betaine rises strongly with salinity (52.7 → 893.1 mM at 2.5 → 4.3 M Na+)” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Strong quantitative evidence for compatible-solute accumulation, but only in an extreme halophile at very high Na+. Not suitable as a low-NaCl trait-defining edge without strong caution. | glycine betaine: CHEBI:17750 |
| increased Na+ concentration —increases→ intracellular glutamate | NaCl increase | Xing 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00145-24 | May 2024 | “glutamate increased (11.0 → 221.3 mM from 2.5 → 4.3 M Na+)” (xing2024thepolyextremophilenatranaerobius pages 17-19); “L-glutamate rising from 11.0 to 221.3 mM” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Strong quantitative edge, but again high-salt specific and taxon specific. | L-glutamate: CHEBI:29985 |
| increased Na+ concentration —modulates→ intracellular proline | NaCl increase | Xing 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00145-24 | May 2024 | “proline falls to 67.0 mM at 3.1 M Na+ then rises to 130 mM at 4.3 M Na+” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Non-monotonic response; curate only if modeling osmolyte switching. Relationship should be `modulates` rather than simple `increases`. | L-proline: CHEBI:26271 |
| increased Na+ concentration —upregulates→ glycine betaine biosynthesis enzymes GSMT/SDMT | NaCl increase | Xing 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00145-24 | May 2024 | “at 3.5 M Na+ (vs 2.5 M) GSMT and SDMT proteins increased ~2.1- and ~3.16-fold” (xing2024thepolyextremophilenatranaerobius pages 14-17) | Specific biosynthetic mechanism for betaine production; high-salt, archaeal/anaerobic taxon context. | gsmt gene label; sdmt gene label; glycine betaine biosynthetic process label candidate |
| hypoosmotic shock —opens→ mechanosensitive channels MscL/MscS | NaCl decrease | Bhowmick 2023, *microLife* | https://doi.org/10.1093/femsml/uqad020 | Apr 2023 | “Hypoosmotic shock triggers transient opening of mechanosensitive channels (MscL/MscS) to prevent turgor-driven cell rupture” (bhowmick2023osmoticstressresponses pages 3-4) | Strong review-supported edge; broad across bacteria. Appropriate core edge in graph. | MscL protein label; MscS protein label; response to osmotic stress: GO:0006970 |
| mechanosensitive channel opening —causes→ solute release | NaCl decrease | Darabi 2024, dissertation/text | https://doi.org/10.7939/r3-mn4e-hf88 | 2024 | “MS channels sense tension in the lipid bilayer and gate to permit rapid release of osmotically active solutes and ions” (marjan2024experimentalandtheoretical pages 18-22) | Useful mechanistic edge, but source is dissertation/repository rather than primary journal article; treat as supportive/secondary. | solute export label candidate; mechanosensitive channel activity: GO label candidate |
| MscL opening —causes→ release of water/solutes and cytoplasmic proteins | NaCl decrease | Morra 2023, *Life Science Alliance* | https://doi.org/10.1101/2022.11.21.517365 | Nov 2023 | “because of its large pore, MscL releases water and solutes and can also eject cytoplasmic proteins during gating” (morra2023arfaantisenserna pages 1-4) | Strong mechanistic specificity for MscL; excretion of proteins may be separate from canonical osmoadaptation and should be modeled carefully. | mscL gene label; protein export label candidate |
| mechanosensitive channels MscL/MscS —promote→ survival during hypoosmotic shock | NaCl decrease | Darabi 2024, dissertation/text | https://doi.org/10.7939/r3-mn4e-hf88 | 2024 | “strains possessing either MscS or MscL can survive hypoosmotic gradients” and channels are “emergency release valves that prevent cell lysis” (marjan2024experimentalandtheoretical pages 18-22) | Good phenotype edge; supportive source is non-journal repository. Still consistent with other evidence. | cell survival: GO:001 survival label candidate; hypoosmotic response label candidate |
| deletion of mscL/mscS —increases→ osmolysis/cell lysis after downshock | NaCl decrease | Adams 2023, *Microbial Cell Factories* | https://doi.org/10.1186/s12934-023-02064-8 | Apr 2023 | “deletion of both mscL and mscS… followed by resuspension in distilled water yielded ~75% cell lysis” (adams2023engineeringosmolysissusceptibility pages 1-2); “combining mscL knockout with an evolved halotolerant background produced >90% osmolytic efficiency” (adams2023engineeringosmolysissusceptibility pages 1-2) | Strong applied/engineering evidence confirming protective function of channels. Assay-specific and engineered strains. | mscL gene label; mscS gene label; cell lysis label candidate |
| c-di-AMP —inhibits→ Ktr/Trk-family potassium uptake systems | regulatory | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “Gating subunits of Trk/Ktr/Ktr-like systems bind c-di-AMP… inhibiting potassium influx” (foster2024bacterialcellvolume pages 8-10) | Strong review synthesis with affinity data; good high-level edge for Gram-positive/osmoregulatory network. | cyclic di-AMP: CHEBI:90853; KtrC/KtrA label; potassium ion transport: GO:0006813 |
| c-di-AMP —inhibits→ KimA (KUP-family K+/H+ symporter) activity | regulatory | Fuss 2023, *Nature Communications* | https://doi.org/10.1038/s41467-023-38944-1 | Jun 2023 | “KimA of the KUP family is inactivated by c-di-AMP” and c-di-AMP “traps KimA in an inward-occluded conformation” (foster2024bacterialcellvolume pages 8-10) | Strong direct mechanistic edge; suitable for transporter-specific node. | KimA protein label; KUP family transporter label; potassium ion transmembrane transporter activity: GO:0015079 |
| c-di-AMP riboswitch —inhibits→ kimA transcription | regulatory | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “kimA transcription is stimulated by low external K+… but inhibited by a c-di-AMP riboswitch” (foster2024bacterialcellvolume pages 8-10) | Regulatory edge at transcriptional level; mainly Bacillus model context. | c-di-AMP riboswitch label; kimA gene label |
| c-di-AMP —inhibits→ KdpD/KdpFABC-dependent potassium uptake | regulatory | Hu 2024, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03786-23 | Aug 2024 | “c-di-AMP binds KdpD and ‘down-regulates the expression of KdpFABC significantly’” (hu2024cdiampaccumulationimpairs pages 13-14); “Transcription of kdp genes was downregulated 5- to 56-fold” (hu2024cdiampaccumulationimpairs pages 2-6) | Strong direct evidence, but *Bacillus anthracis* specific. Excellent for specific edge with taxon note. | KdpD protein label; KdpFABC complex label; potassium-transporting ATPase activity label candidate |
| c-di-AMP accumulation —causes→ osmotic sensitivity / impaired growth under salt | regulatory | Hu 2024, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03786-23 | Aug 2024 | “elevated c-di-AMP caused increased osmotic sensitivity (unable to grow at mild salt)” and growth could be partially rescued in “2.5% NaCl” by KtrC/KdpD expression (hu2024cdiampaccumulationimpairs pages 2-6) | Valuable phenotype edge linking regulator to growth. Assay-specific in pathogen model; not directly low-NaCl trait-defining. | cyclic di-AMP: CHEBI:90853; growth label candidate |
| c-di-AMP —binds/inhibits→ OpuA/OpuC compatible-solute importers | regulatory | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “c-di-AMP binds CBS-containing importers (OpuA/OpuC) and negatively regulates their transport activity” (foster2024bacterialcellvolume pages 10-12) | Strong review-level regulatory edge for osmolyte uptake control. | OpuA transporter label; OpuC transporter label; glycine betaine transport label candidate |
| c-di-AMP-bound BusR —represses→ opuA transcription | regulatory | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “BusR, the repressor of opuA, binds c-di-AMP… causing inhibition of opuA transcription and decreased glycine betaine uptake” (foster2024bacterialcellvolume pages 10-12) | Good direct regulatory edge with named transcription factor. | BusR protein label; opuA gene label; transcriptional repression label candidate |
| hyperosmotic stress —activates→ BetT choline transporter | NaCl increase | Yang 2024, *Science Advances* | https://doi.org/10.1126/sciadv.ado6229 | Aug 2024 | “BetT is maintained in a low-activity state via C-terminal domain (CTD)-mediated autoinhibition under nonstress conditions, and hyperosmotic activation involves release of this autoinhibition” (yang2024structureandmechanism pages 1-2) | Strong recent mechanistic edge; species context is *Pseudomonas* BetT. Good for choline-uptake branch. | BetT transporter label; response to osmotic stress: GO:0006970 |
| BetT —imports→ choline | NaCl increase | Yang 2024, *Science Advances* | https://doi.org/10.1126/sciadv.ado6229 | Aug 2024 | “BetT mediates uptake of external choline used to synthesize glycine betaine” (yang2024structureandmechanism pages 1-2) | Strong direct transport edge. | choline: CHEBI:15354; BetT transporter label |
| choline uptake —enables→ glycine betaine synthesis | NaCl increase | Yang 2024, *Science Advances* | https://doi.org/10.1126/sciadv.ado6229 | Aug 2024 | “BetT mediates uptake of external choline used to synthesize glycine betaine, a key compatible solute for bacterial survival in hyperosmotic environments” (yang2024structureandmechanism pages 1-2) | Good pathway edge; broad bacterial relevance, but direct enzymatic steps not shown in this paper. | glycine betaine: CHEBI:17750; choline: CHEBI:15354; glycine betaine biosynthetic process label candidate |
| glycine betaine —supports→ survival/growth in hyperosmotic environments | NaCl increase | Yang 2024, *Science Advances* | https://doi.org/10.1126/sciadv.ado6229 | Aug 2024 | glycine betaine is “a key compatible solute for bacterial survival in hyperosmotic environments” (yang2024structureandmechanism pages 1-2) | Useful downstream phenotype edge, but broad and not exclusive to low-NaCl phenotype. | glycine betaine: CHEBI:17750; cell survival label candidate |
| glycine betaine —enhances→ growth under salt stress | NaCl increase | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “glycine betaine enhances growth under 0.4 M NaCl” (foster2024bacterialcellvolume pages 10-12) | Quantitative phenotype support for osmoprotectant benefit; salt concentration is above low-NaCl threshold. | glycine betaine: CHEBI:17750; growth label candidate |
| high intracellular K+ / ionic strength —promotes→ neutral compatible-solute accumulation | regulatory | Foster 2024, *Microbiology and Molecular Biology Reviews* | https://doi.org/10.1128/mmbr.00181-23 | Jun 2024 | “Cells respond to excessive intracellular K+ and ionic strength by accumulating neutral compatible solutes (e.g., glycine betaine, trehalose)” (foster2024bacterialcellvolume pages 6-8) | Good bridge edge linking early ionic response to later osmolyte response; supportive for layered graph. | trehalose: CHEBI:16588; glycine betaine: CHEBI:17750; osmotic stress: GO:0006970 |


*Table: This table lists curation-ready candidate causal edges relevant to the 'NaCl range low' trait and nearby osmoadaptation mechanisms. It prioritizes direct evidence from the conversation context, while flagging high-salt, taxon-specific, and assay-specific findings that may be inappropriate for direct TraitMech curation without qualification.*

## Recent developments (2023–2024) most relevant to NaCl-range phenotyping

1. **c-di-AMP-centered osmoregulation framework (2024):** c-di-AMP integrates potassium import/export and compatible-solute uptake; dysregulation produces salt sensitivity, lysis, and growth defects, and selection of suppressor mutations in transporter systems. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13)
2. **Transporter structural mechanism for osmotic activation (2024 BetT):** CTD-mediated autoinhibition/release provides a specific mechanistic model for osmoregulated compatible-solute precursor uptake. (yang2024structureandmechanism pages 1-2, yang2024structureandmechanism pages 5-6)
3. **Quantitative pathogen-relevant regulation under salt (2024 *B. anthracis*):** c-di-AMP binds potassium-uptake regulators (KdpD/KtrC), downregulates kdp genes, and Ktr is induced 13–15× under 4.5% NaCl with corresponding growth phenotypes; while above the <=1% range, it provides a clear mechanistic link between osmotic stress, K+ transport, and growth outcomes. (hu2024cdiampaccumulationimpairs pages 13-14, hu2024cdiampaccumulationimpairs pages 2-6)
4. **Engineering use of osmotic downshock (2023):** deletion of mechanosensitive channels (mscL ± mscS) plus pre-growth at higher salt enables predictable, high-efficiency osmolysis, reframing MscL/MscS as both stress-protection mechanisms and bioprocessing levers. (adams2023engineeringosmolysissusceptibility pages 1-2)

## Current applications and real-world implementations

### 1) Bioprocessing: engineered osmolysis for intracellular product recovery
A 2023 study engineered non-halotolerant industrial hosts to become susceptible to hypoosmotic lysis for downstream processing. Key quantitative outcomes:
- **Adaptive laboratory evolution (ALE)** increased *Cupriavidus necator* halotolerance from **1.5% to 3.25% (w/v) NaCl**; the evolved strain achieved **47% osmolytic efficiency** after growth in **3% NaCl**. (adams2023engineeringosmolysissusceptibility pages 1-2)
- **mscL knockout** combined with evolved halotolerance yielded **>90% osmolytic efficiency** upon downshock. (adams2023engineeringosmolysissusceptibility pages 1-2)
- In **E. coli BL21**, deleting **mscL and mscS** and growing cells in **4% NaCl** produced **~75% cell lysis** after resuspension in distilled water. (adams2023engineeringosmolysissusceptibility pages 1-2)

These are real implementations of osmotic physiology, demonstrating mechanosensitive channels as actionable “controls” over robustness vs lysis. (adams2023engineeringosmolysissusceptibility pages 1-2)

### 2) Pathogen and environmental fitness: BetT-mediated choline uptake
The BetT/osmoprotection pathway has direct relevance to microbes encountering osmotic stress in hosts or environmental niches. The 2024 *Science Advances* study notes BetT homologs in pathogens (e.g., *P. aeruginosa*, *A. baumannii*) and states that BetT is critical for *P. syringae* leaf colonization and implicated in survival of nosocomial pathogens, connecting osmoregulated choline uptake to real-world microbial fitness. (yang2024structureandmechanism pages 1-2)

### 3) Compatible solutes as biotechnological products and stabilizers (contextual)
While not 2023–2024 in the retrieved full-text evidence, the broader compatible-solute literature supports ectoine/hydroxyectoine use as stress protectants and industrial targets. Examples cited in retrieved context include engineered production and protein/enzyme stabilization. (richter2019biosynthesisofthe pages 16-17, czech2019exploitingsubstratepromiscuity pages 17-17)

## Statistics and quantitative data points suitable for graph annotation

- **Phenotype thresholds (definition-level):** non-halophilic optimum growth at **<1% (w/v) NaCl**; slight halophiles at **1–3%**, moderate **3–15%**, extreme **15–30%**. (reang2022plantgrowthpromoting pages 1-2, reang2022plantgrowthpromoting media f999e5a2)
- **K+ emergency response under salt:** intracellular K+ in *B. subtilis* rises from **~350–700 mM within 1 hour** after exposure to **400 mM NaCl** (reviewed example). (bhowmick2023osmoticstressresponses pages 3-4)
- **c-di-AMP binding affinities and regulatory scale:** c-di-AMP binding to Trk/Ktr gating subunits reported with **KD ~40 nM–8 µM**; KdpD binding with **KD ~2 µM**; BusR binds c-di-AMP with **KD ≈ 10 µM**. (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12)
- **Pathogen salt phenotype linkage:** *B. anthracis* **ktrC/D induced 13–15×** under **4.5% NaCl**, with **ΔktrC** showing impaired growth at that condition. (hu2024cdiampaccumulationimpairs pages 13-14)
- **Engineered osmolysis metrics:** **47%**, **>90%**, and **75%** lysis/osmolysis efficiency outcomes depending on strain engineering and pre-growth salt. (adams2023engineeringosmolysissusceptibility pages 1-2)

## Warnings / claims not ready (or only conditionally ready) for TraitMech curation

1. **Mechanisms derived from high-salt specialists may not define the <=1% trait.** Many mechanistic studies (e.g., extreme halophiles or assays at 0.4 M NaCl and above) inform general osmoadaptation but do **not** directly explain why a microbe’s growth upper bound is ≤1% NaCl. Such edges should be curated with an **“uncertain / general mechanism”** flag if used. (foster2024bacterialcellvolume pages 10-12, bhowmick2023osmoticstressresponses pages 3-4)
2. **Assay composition confounding (osmoprotectants in media).** Apparent salt tolerance depends on the presence of compatible solutes in media; for trait definition, conditions should be standardized or captured as assay nodes. (xing2024thepolyextremophilenatranaerobius pages 17-19)
3. **Repository/dissertation sources:** mechanistic channel-tension thresholds from non-journal sources should be treated as supportive only unless corroborated by primary peer-reviewed studies in the curation set. (marjan2024experimentalandtheoretical pages 18-22)

## DOI-first bibliography (with URLs and dates)

- Reang L. et al. (Mar 2022). *Scientific Reports*. “Plant growth promoting characteristics of halophilic and halotolerant bacteria isolated from coastal regions of Saurashtra Gujarat.” https://doi.org/10.1038/s41598-022-08151-x (reang2022plantgrowthpromoting pages 1-2)
- Bhowmick S. et al. (Apr 2023). *microLife*. “Osmotic stress responses and the biology of the second messenger c-di-AMP in Streptomyces.” https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 3-4)
- Adams J.D. et al. (Apr 2023). *Microbial Cell Factories*. “Engineering osmolysis susceptibility in Cupriavidus necator and Escherichia coli for recovery of intracellular products.” https://doi.org/10.1186/s12934-023-02064-8 (adams2023engineeringosmolysissusceptibility pages 1-2)
- Fuss M.F. et al. (Jun 2023). *Nature Communications*. “Cyclic di-AMP traps proton-coupled K+ transporters of the KUP family in an inward-occluded conformation.” https://doi.org/10.1038/s41467-023-38944-1 (foster2024bacterialcellvolume pages 8-10)
- Foster A.J. et al. (Jun 2024). *Microbiology and Molecular Biology Reviews*. “Bacterial cell volume regulation and the importance of cyclic di-AMP.” https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 8-10)
- Warneke R. et al. (Jul 2024). *Journal of Bacteriology*. “DarA—the central processing unit for the integration of osmotic with potassium and amino acid homeostasis in Bacillus subtilis.” https://doi.org/10.1128/jb.00190-24 (warneke2024dara—thecentralprocessing pages 1-2)
- Hu J. et al. (Aug 2024). *Microbiology Spectrum*. “c-di-AMP accumulation impairs toxin expression of Bacillus anthracis by down-regulating potassium importers.” https://doi.org/10.1128/spectrum.03786-23 (hu2024cdiampaccumulationimpairs pages 2-6)
- Yang T. et al. (Aug 2024). *Science Advances*. “Structure and mechanism of the osmoregulated choline transporter BetT.” https://doi.org/10.1126/sciadv.ado6229 (yang2024structureandmechanism pages 1-2)

(Additional contextual sources used for compatible-solute applications in this evidence set: Richter et al. 2019 https://doi.org/10.3389/fmicb.2019.02811; Czech et al. 2019 https://doi.org/10.3389/fmicb.2019.02745.) (richter2019biosynthesisofthe pages 16-17, czech2019exploitingsubstratepromiscuity pages 17-17)

References

1. (reang2022plantgrowthpromoting pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, U. M. Vyas, and Jasmin Kumar Kheni. Plant growth promoting characteristics of halophilic and halotolerant bacteria isolated from coastal regions of saurashtra gujarat. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-08151-x, doi:10.1038/s41598-022-08151-x. This article has 70 citations and is from a peer-reviewed journal.

2. (reang2022plantgrowthpromoting media f999e5a2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, U. M. Vyas, and Jasmin Kumar Kheni. Plant growth promoting characteristics of halophilic and halotolerant bacteria isolated from coastal regions of saurashtra gujarat. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-08151-x, doi:10.1038/s41598-022-08151-x. This article has 70 citations and is from a peer-reviewed journal.

3. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

4. (bhowmick2023osmoticstressresponses pages 3-4): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

5. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 12-13): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

8. (yang2024structureandmechanism pages 1-2): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

9. (yang2024structureandmechanism pages 5-6): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (adams2023engineeringosmolysissusceptibility pages 1-2): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

11. (marjan2024experimentalandtheoretical pages 18-22): Marjan Darabi. Experimental and theoretical investigation of mechanical responses of bacteria under hypoosmotic pressure. Text, 2024. URL: https://doi.org/10.7939/r3-mn4e-hf88, doi:10.7939/r3-mn4e-hf88. This article has 0 citations and is from a peer-reviewed journal.

12. (warneke2024dara—thecentralprocessing pages 1-2): Robert Warneke, Christina Herzberg, Martin Weiß, Thorben Schramm, Dietrich Hertel, Hannes Link, and Jörg Stülke. Dara—the central processing unit for the integration of osmotic with potassium and amino acid homeostasis in <i>bacillus subtilis</i>. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00190-24, doi:10.1128/jb.00190-24. This article has 3 citations and is from a peer-reviewed journal.

13. (adams2023engineeringosmolysissusceptibility pages 7-8): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

14. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

15. (yang2024structureandmechanism pages 2-3): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

16. (yang2024structureandmechanism pages 7-8): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (morra2023arfaantisenserna pages 1-4): Rosa Morra, Fenryco Pratama, Thomas Butterfield, Geizecler Tomazetto, Kate Young, Ruth Lopez, and Neil Dixon. Arfa antisense rna regulates mscl excretory activity. Life Science Alliance, Nov 2023. URL: https://doi.org/10.1101/2022.11.21.517365, doi:10.1101/2022.11.21.517365. This article has 2 citations and is from a peer-reviewed journal.

18. (hu2024cdiampaccumulationimpairs pages 13-14): Jia Hu, Junmin Yao, Chengfeng Lei, and Xiulian Sun. C-di-amp accumulation impairs toxin expression of <i>bacillus anthracis</i> by down-regulating potassium importers. Aug 2024. URL: https://doi.org/10.1128/spectrum.03786-23, doi:10.1128/spectrum.03786-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

19. (hu2024cdiampaccumulationimpairs pages 2-6): Jia Hu, Junmin Yao, Chengfeng Lei, and Xiulian Sun. C-di-amp accumulation impairs toxin expression of <i>bacillus anthracis</i> by down-regulating potassium importers. Aug 2024. URL: https://doi.org/10.1128/spectrum.03786-23, doi:10.1128/spectrum.03786-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

20. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

21. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

22. (richter2019biosynthesisofthe pages 16-17): Alexandra A. Richter, Christopher-Nils Mais, Laura Czech, Kyra Geyer, Astrid Hoeppner, Sander H. J. Smits, Tobias J. Erb, Gert Bange, and Erhard Bremer. Biosynthesis of the stress-protectant and chemical chaperon ectoine: biochemistry of the transaminase ectb. Frontiers in Microbiology, Dec 2019. URL: https://doi.org/10.3389/fmicb.2019.02811, doi:10.3389/fmicb.2019.02811. This article has 89 citations and is from a peer-reviewed journal.

23. (czech2019exploitingsubstratepromiscuity pages 17-17): Laura Czech, Sarah Wilcken, Oliver Czech, Uwe Linne, Jarryd Brauner, Sander H. J. Smits, Erwin A. Galinski, and Erhard Bremer. Exploiting substrate promiscuity of ectoine hydroxylase for regio- and stereoselective modification of homoectoine. Frontiers in Microbiology, Nov 2019. URL: https://doi.org/10.3389/fmicb.2019.02745, doi:10.3389/fmicb.2019.02745. This article has 17 citations and is from a peer-reviewed journal.