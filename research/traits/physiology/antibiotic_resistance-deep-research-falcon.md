---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:28:54.930594'
end_time: '2026-06-18T10:52:38.077436'
duration_seconds: 1423.15
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: antibiotic resistance
  trait_identifier: traitmech:000088
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: antibiotic_resistance
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological capacity to grow in the presence of antibiotic concentrations
    that inhibit susceptible cells, mediated by efflux, target modification, drug
    inactivation, or reduced permeability.
  parent_traits: METPO:1000059
  synonyms: antimicrobial resistance
  evidence_summary: 'DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular
    mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation,
    reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits
    molecular mechanisms of antibiotic resistance.)'
  causal_graph_summary: 'antibiotic_resistance_mechanisms: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** antibiotic resistance
- **METPO identifier:** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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
- **Trait label:** antibiotic resistance
- **METPO identifier:** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Antibiotic Resistance (METPO: traitmech:000088)

## Executive scope summary
**Trait definition (METPO-aligned):** Antibiotic resistance is the **physiological capacity of microbial cells to survive and replicate (i.e., grow) in the presence of antibiotic concentrations that would inhibit susceptible cells**, typically operationalized in susceptibility testing as an elevated MIC or growth on inhibitory antibiotic concentrations. Mechanistically, recent reviews consistently emphasize four core cellular routes: **reduced permeability/decreased uptake, increased efflux, enzymatic drug inactivation, and target modification** (belay2024mechanismofantibacterial media 58316221, belay2024mechanismofantibacterial pages 3-4, chiang2024effluxpumpmediatedresistance pages 1-2).

**Boundary cases that should be separated during curation:**
- **Tolerance**: survival during transient exposure to lethal antibiotic concentrations **without an elevated MIC**; often seen as reduced killing kinetics (time–kill/MDK) (salzer2023roleof(p)ppgpp pages 1-1, bollen2023environmentalmechanisticand pages 1-2).
- **Persistence**: a **small subpopulation** (“persisters”) with high tolerance producing **biphasic killing**; persisters can regrow after treatment ends and are often protected in biofilms (bollen2023environmentalmechanisticand pages 1-2, bollen2023environmentalmechanisticand pages 2-3).
These phenomena can contribute to treatment failure and facilitate later resistance evolution, but they are not equivalent to MIC-defined resistance and should be marked as adjacent/uncertain if included in a resistance trait graph (bollen2023environmentalmechanisticand pages 1-2, salzer2023roleof(p)ppgpp pages 1-1).

## Key concepts and definitions (current understanding)
### Resistance vs tolerance vs persistence
- **Resistance**: cells “survive otherwise lethal doses of antibiotics” and “can also replicate in the presence of antibiotics” (salzer2023roleof(p)ppgpp pages 1-1).
- **Tolerance**: “the ability to survive transient exposure to lethal concentrations of antibiotics without exhibiting an elevated MIC,” with regrowth after drug removal (salzer2023roleof(p)ppgpp pages 1-1).
- **Persistence**: “a small subpopulation (persister cells) … highly tolerant,” yielding biphasic killing; persisters can recover/regrow and contribute to relapse/chronic infection (bollen2023environmentalmechanisticand pages 1-2).

### Canonical mechanistic classes (cell-intrinsic)
A 2024 schematic synthesis depicts the commonly curated core mechanisms: **(1) enzymatic inactivation, (2) efflux, (3) decreased permeability (decreased influx/entry), (4) target modification** (belay2024mechanismofantibacterial media 58316221). These same categories are reiterated across multiple 2024 reviews with representative gene/protein examples (belay2024mechanismofantibacterial pages 3-4, zhang2024bacterialeffluxpump pages 2-4, chiang2024effluxpumpmediatedresistance pages 1-2).

## Recent developments and latest research (prioritizing 2023–2024)
### 1) Efflux systems as underappreciated drivers (including for newer β-lactams)
Efflux is highlighted both as a dominant mechanism class and as a therapeutically actionable target, with specific multi-component pumps and families enumerated (e.g., AcrAB-TolC, MexAB-OprM; RND, ABC, MFS, MATE, SMR, PACE) (zhang2024bacterialeffluxpump pages 2-4). A 2024 Communications Medicine review emphasizes RND pumps as important determinants of efflux-mediated resistance in Gram-negative bacteria, with relevance to resistance against newer β-lactams and β-lactam/β-lactamase inhibitor combinations (chiang2024effluxpumpmediatedresistance pages 1-2).

### 2) Expanded molecular specificity for target modification
Recent synthesis sources list multiple target modification mechanisms with explicit loci:
- **Fluoroquinolone resistance** via **QRDR mutations** in DNA gyrase/topoisomerase IV (belay2024mechanismofantibacterial pages 3-4).
- **Ribosome-associated resistance** via **23S rRNA mutations/methylation** and changes in ribosomal proteins (L3/L4) that affect macrolides/oxazolidinones and others (belay2024mechanismofantibacterial pages 3-4).

### 3) Biofilms as a mechanistic bridge between tolerance and resistance
Biofilm formation is repeatedly identified as a major pathway linked to reduced antibiotic efficacy; it is often best treated as **context-dependent reduced susceptibility/tolerance** rather than MIC-defined resistance, but it can facilitate resistance evolution and gene exchange (zhao2024multidrugresistancein pages 1-2, bollen2023environmentalmechanisticand pages 2-3).

### 4) Persistence and stringent response alarmones as contributors to tolerance (and possibly resistance emergence)
A 2023 microLife review provides mechanistic entities that connect stress physiology to antibiotic outcomes: the stringent response is “characterized by the synthesis of … pppGpp and ppGpp,” and in Firmicutes is orchestrated by **Rel** plus accessory synthetases **SasA/RelP** and **SasB/RelQ**; a key protective mechanism is “(p)ppGpp-mediated restriction of GTP accumulation” (salzer2023roleof(p)ppgpp pages 1-1). Evidence supports a role for elevated (p)ppGpp in tolerance/survival and some persistent infection contexts, but persister formation can be (species/condition) dependent and not always strictly (p)ppGpp-required—important for curation uncertainty marking (salzer2023roleof(p)ppgpp pages 6-7, salzer2023roleof(p)ppgpp pages 7-8).

## Current applications and real-world implementations
### Global targets and stewardship implementations
A 2024 Lancet policy analysis proposes global “**10–20–30 by 2030**” targets: **10% reduction in AMR-attributable deaths**, **20% reduction in inappropriate human antibiotic use** (while ensuring access), and **30% reduction in inappropriate animal antibiotic use** (mendelson2024ensuringprogresson pages 1-4). Antibiotic consumption surveillance is positioned as a foundation for stewardship and guideline/policy tailoring (klein2024globaltrendsin pages 1-2).

### Antibiotic consumption monitoring (quantitative) and Access–Watch policies
A 2024 PNAS analysis estimated **49.3 billion defined daily doses (DDDs)** of global human antibiotic use in 2023 (klein2024globaltrendsin pages 6-7). The same paper notes a UNGA AMR declaration target to increase **Access antibiotics to ≥70% of human antibiotic consumption globally by 2030** (klein2024globaltrendsin pages 6-7).

### Diagnostics and surveillance deployment
Implementation-focused synthesis highlights incomplete uptake of genomics: a 2025 review reports **<35% of WHO member states have integrated whole-genome sequencing (WGS) into AMR surveillance** (marino2025theglobalburden pages 13-14). This signals a major infrastructure gap relevant to real-world identification of resistance determinants.

### Therapeutic adjuvants and next-generation approaches
Efflux pump inhibitors are explicitly positioned as small molecules that can restore antibiotic activity, with additional noted effects on biofilm formation and other phenotypes (zhang2024bacterialeffluxpump pages 1-2). These developments motivate graph nodes linking efflux regulation to resistance phenotypes and candidate interventions (zhang2024bacterialeffluxpump pages 2-4).

## Relevant statistics and recent data (2023–2024 emphasized)
### Burden of bacterial AMR
The 2024 Lancet GBD AMR study estimates that in **2021** there were **4.71 million deaths associated with bacterial AMR** and **1.14 million deaths attributable to AMR** (naghavi2024globalburdenof pages 1-2). It forecasts **1.91 million deaths attributable** and **8.22 million deaths associated** with AMR in **2050** (naghavi2024globalburdenof pages 1-2).

### Antibiotic consumption trends
For 67 countries with data, total antibiotic consumption rose **16.3%** from 2016 to 2023; global consumption in 2023 was estimated at **49.3 billion DDDs** (klein2024globaltrendsin pages 1-2).

## Candidate causal graph nodes (grouped by type)

### A) Core mechanistic processes (GO-like)
- Drug efflux / multidrug efflux (e.g., RND, ABC, MFS systems) (zhang2024bacterialeffluxpump pages 2-4, chiang2024effluxpumpmediatedresistance pages 1-2)
- Reduced permeability / porin loss / decreased influx (Gram-negative outer membrane barrier) (zhang2024bacterialeffluxpump pages 2-4, chiang2024effluxpumpmediatedresistance pages 1-2)
- Enzymatic drug inactivation (e.g., β-lactamase-mediated hydrolysis) (chiang2024effluxpumpmediatedresistance pages 1-2)
- Target modification (DNA gyrase/topoisomerase mutations; rRNA methylation/ribosomal protein changes) (belay2024mechanismofantibacterial pages 3-4)

### B) Molecular entities (genes/proteins/complexes; label-first with examples)
- **Efflux complexes**: AcrAB-TolC; MexAB-OprM; NorA; OqxAB; CmeABC (zhang2024bacterialeffluxpump pages 2-4)
- **β-lactamases** (including carbapenemases; AmpC cephalosporinases) (chiang2024effluxpumpmediatedresistance pages 1-2)
- **Ribosomal modification genes**: erm(B), cfr (belay2024mechanismofantibacterial pages 3-4)
- **Fluoroquinolone targets**: DNA gyrase; topoisomerase IV (QRDR mutations) (belay2024mechanismofantibacterial pages 3-4)
- **Pseudomonas regulatory nodes (resistance control)**: mexT, ampR, argR (zhao2024multidrugresistancein pages 1-2)
- **Stringent response enzymes (Firmicutes)**: Rel; SasA/RelP; SasB/RelQ (salzer2023roleof(p)ppgpp pages 1-1)

### C) Mobile genetic elements and dissemination nodes
- Resistance (R) plasmids; other mobile genetic elements (belay2024mechanismofantibacterial pages 3-4, galgano2025acquiredbacterialresistance pages 7-8)
- Integrons (intI1–intI4), resistance cassettes (galgano2025acquiredbacterialresistance pages 7-8)

### D) Environmental/experimental factors (ENVO-like; label-first)
- Antibiotic exposure/selective pressure (galgano2025acquiredbacterialresistance pages 7-8)
- High-density niches (intestine/oral cavity), biofilms facilitating gene transfer (galgano2025acquiredbacterialresistance pages 7-8)

## Candidate evidence-backed causal edges (curation table)
The following table is formatted for direct conversion into candidate TraitMech edges.

| Edge (S–P–O) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes (mechanism/assay/taxon specificity, uncertainty) | Suggested ontology grounding |
|---|---|---|---|---|
| Efflux pump overexpression — decreases — intracellular antibiotic concentration | “efflux pumps reduce intracellular antibiotic concentrations” and “their upregulation under antibiotic exposure can produce intermediate resistance phenotypes” (zhang2024bacterialeffluxpump pages 2-4) | 10.3390/pharmaceutics16020170, 2024, https://doi.org/10.3390/pharmaceutics16020170 | Broad mechanism across Gram-positive/Gram-negative bacteria; exemplar pumps named include AcrAB-TolC, MexAB-OprM, NorA, OqxAB, CmeABC. Good high-level curation edge; pump-specific edges should be taxon-specific. | subject: GO:0015559 drug transmembrane transporter activity; label-only “multidrug efflux pump”; examples: AcrAB-TolC (UniProt/taxon-specific), MexAB-OprM; object: CHEBI:33281 antimicrobial drug |
| Outer membrane porin modification/loss — decreases — antibiotic influx | “reduced permeability/porin loss” and “modification of outer membrane porin channels” are listed as major mechanisms (zhang2024bacterialeffluxpump pages 2-4, chiang2024effluxpumpmediatedresistance pages 1-2) | 10.3390/pharmaceutics16020170, 2024, https://doi.org/10.3390/pharmaceutics16020170; 10.1038/s43856-024-00591-y, 2024, https://doi.org/10.1038/s43856-024-00591-y | Best curated as Gram-negative-focused. Often synergizes with efflux and beta-lactamases. Specific porins (e.g., OmpK35, Opr family) may need taxon-specific nodes. | subject: GO:0015288 porin activity; label-only “outer membrane porin”; object: GO:1901475 regulation of membrane permeability; CHEBI:33281 antimicrobial drug |
| Beta-lactamase — hydrolyzes — beta-lactam antibiotic | “drug hydrolysis by beta-lactamases” and β-lactamases “hydrolyze the β-lactam ring” (chiang2024effluxpumpmediatedresistance pages 1-2, singha2024alternativetherapeuticsto pages 3-4) | 10.1038/s43856-024-00591-y, 2024, https://doi.org/10.1038/s43856-024-00591-y; 10.3389/fddsv.2024.1385460, 2024, https://doi.org/10.3389/fddsv.2024.1385460 | Strong canonical mechanism. Can later specialize to AmpC cephalosporinase, carbapenemase, metallo-β-lactamase. | subject: EC:3.5.2.6 beta-lactamase; GO:0008800 beta-lactamase activity; object: CHEBI:35627 beta-lactam antibiotic |
| QRDR mutation in DNA gyrase/topoisomerase IV — confers resistance to — fluoroquinolone | “QRDR mutations in DNA gyrase and topoisomerase IV cause quinolone/fluoroquinolone resistance” (belay2024mechanismofantibacterial pages 3-4) | 10.3389/fphar.2024.1444781, 2024, https://doi.org/10.3389/fphar.2024.1444781 | Strong mechanism, but sequence-variant curation is usually taxon/gene-specific (e.g., gyrA/parC). Suitable as a class-level edge if variant details are omitted. | subject: GO:0003918 DNA topoisomerase type II activity; label-only “QRDR mutation in gyrA/parC”; object: CHEBI:3659 fluoroquinolone |
| 23S rRNA methylation — decreases binding of — macrolide/linezolid | “methylation of 23S rRNA confer[s] linezolid, chloramphenicol, clindamycin, and macrolide resistance” (belay2024mechanismofantibacterial pages 3-4) | 10.3389/fphar.2024.1444781, 2024, https://doi.org/10.3389/fphar.2024.1444781 | Strong mechanism; genes mentioned include erm(B) and cfr. Could be split into separate edges for macrolides vs oxazolidinones if desired. | subject: GO:0031167 rRNA methylation; label-only “23S rRNA methyltransferase”; examples erm(B), cfr; object: CHEBI:25106 macrolide antibiotic / CHEBI:35618 linezolid |
| R plasmid — carries — antibiotic resistance gene | resistance genes are “often carried on resistance (R) plasmids” (belay2024mechanismofantibacterial pages 3-4) | 10.3389/fphar.2024.1444781, 2024, https://doi.org/10.3389/fphar.2024.1444781 | Strong but generic mobile-element edge; cargo genes are diverse and taxon/context dependent. Useful upstream dissemination edge rather than direct phenotype edge. | subject: label-only “R plasmid”; related process: GO:0006310 DNA recombination / GO:0000746 conjugation; object: label-only “antibiotic resistance gene” |
| Integron — captures/assembles — resistance cassette | “integrons … mediate capture and assembly of resistance cassettes” (galgano2025acquiredbacterialresistance pages 7-8) | 10.3390/antibiotics14030222, 2025, https://doi.org/10.3390/antibiotics14030222 | Important dissemination mechanism; better curated as acquisition/spread of determinants than as direct physiological resistance. Class 1–4 integrons named. | subject: label-only “integron”; examples intI1/intI2/intI3/intI4; object: label-only “resistance cassette” |
| Biofilm extracellular matrix — obstructs penetration of — antibiotic | biofilms are associated with “extracellular matrix production” and intrinsic physical factors that make infections “highly recalcitrant to antibiotic therapy” (zhang2024bacterialeffluxpump pages 1-2, zhao2024multidrugresistancein pages 1-2) | 10.3390/pharmaceutics16020170, 2024, https://doi.org/10.3390/pharmaceutics16020170; 10.1186/s43556-024-00221-y, 2024, https://doi.org/10.1186/s43556-024-00221-y | Important boundary case: usually tolerance/intrinsic biofilm-associated reduced susceptibility, not always classical MIC-defined resistance. Mark as assay/context-sensitive. | subject: GO:0042710 biofilm formation; label-only “biofilm extracellular matrix”; object: CHEBI:33281 antimicrobial drug |
| (p)ppGpp accumulation/stringent response — restricts — GTP accumulation | “(p)ppGpp-mediated restriction of GTP accumulation is one major mechanism of protection and survival” (salzer2023roleof(p)ppgpp pages 1-1) | 10.1093/femsml/uqad009, 2023, https://doi.org/10.1093/femsml/uqad009 | Strong mechanistic edge in Firmicutes-focused review; may be indirect relative to resistance and more central to tolerance/survival. | subject: label-only “(p)ppGpp”; process: GO:0006950 response to stress; object: CHEBI:15996 GTP |
| (p)ppGpp accumulation/stringent response — increases — antibiotic tolerance/survival under antibiotic stress | increased (p)ppGpp “limits growth while exerting protective effects” and “contribute[s] to antibiotic tolerance” (salzer2023roleof(p)ppgpp pages 1-1, salzer2023roleof(p)ppgpp pages 6-7) | 10.1093/femsml/uqad009, 2023, https://doi.org/10.1093/femsml/uqad009 | Strong for tolerance/survival; not equivalent to classical resistance. Curate only if TraitMech graph permits neighboring mechanisms contributing to resistance-associated treatment failure. | subject: label-only “stringent response”; object: label-only “antibiotic tolerance/survival” |
| sasA/RelP expression heterogeneity — associated with — tolerant subpopulation formation | “sasA (SasA/RelP) noise correlates with rare cells showing increased antibiotic tolerance” (salzer2023roleof(p)ppgpp pages 7-8) | 10.1093/femsml/uqad009, 2023, https://doi.org/10.1093/femsml/uqad009 | Useful but should be marked uncertain/context-specific: evidence is for phenotypic tolerance heterogeneity, not universal resistance. Likely species- and condition-dependent in Firmicutes. | subject: label-only “sasA/RelP expression heterogeneity”; object: label-only “antibiotic-tolerant subpopulation” |
| Mobile genetic element transfer in high-density niches/biofilms — favors dissemination of — resistance genes | “presence of antibiotics, high-density niches like intestine/oral cavity and biofilms — favor gene transfer and dissemination” (galgano2025acquiredbacterialresistance pages 7-8) | 10.3390/antibiotics14030222, 2025, https://doi.org/10.3390/antibiotics14030222 | Environmental/dissemination edge rather than direct cell-physiology edge; useful for ecosystem-level subgraph. | subject: ENVO: label-only “biofilm/high-density microbial niche”; process: GO:0000746 conjugation; object: label-only “resistance gene dissemination” |


*Table: This table lists evidence-backed subject–predicate–object edges for antibiotic resistance and closely adjacent mechanisms relevant to TraitMech curation. It emphasizes canonical resistance mechanisms plus clearly marked tolerance/dissemination edges that may require caution before formal curation.*

## Warnings / claims to treat cautiously before TraitMech curation
1. **Biofilm “resistance” vs tolerance:** Biofilm matrix effects are often better represented as reduced penetration and physiological slowing leading to tolerance; curating this directly into “antibiotic resistance” may conflate MIC-defined resistance with treatment recalcitrance (bollen2023environmentalmechanisticand pages 1-2, bollen2023environmentalmechanisticand pages 2-3).
2. **(p)ppGpp and persister causality is context-dependent:** While (p)ppGpp is supported as contributing to tolerance/survival and some persistent infection phenotypes, evidence that it is a universal causal trigger of persister formation is mixed; curate with uncertainty qualifiers and taxon/condition annotations (Firmicutes vs Proteobacteria; growth phase; antibiotic class) (salzer2023roleof(p)ppgpp pages 6-7, salzer2023roleof(p)ppgpp pages 7-8).
3. **High-level mechanistic classes vs gene-specific edges:** Many edges (e.g., “efflux pump overexpression → resistance”) are broadly valid, but gene/protein complex edges (e.g., AcrAB-TolC) are taxon-specific; curation should either (a) use class-level nodes, or (b) constrain by NCBITaxon and antibiotic class (zhang2024bacterialeffluxpump pages 2-4, chiang2024effluxpumpmediatedresistance pages 1-2).

## DOI-first bibliography (with publication date and URL)
- Belay WY, et al. *Mechanism of antibacterial resistance, strategies and next-generation antimicrobials to contain antimicrobial resistance: a review.* **Frontiers in Pharmacology** (Aug **2024**). DOI: **10.3389/fphar.2024.1444781**. https://doi.org/10.3389/fphar.2024.1444781 (belay2024mechanismofantibacterial pages 3-4, belay2024mechanismofantibacterial media 58316221)
- Zhang L, et al. *Bacterial efflux pump inhibitors reduce antibiotic resistance.* **Pharmaceutics** (Jan **2024**). DOI: **10.3390/pharmaceutics16020170**. https://doi.org/10.3390/pharmaceutics16020170 (zhang2024bacterialeffluxpump pages 2-4, zhang2024bacterialeffluxpump pages 1-2)
- Chiang AD, Dekker JP. *Efflux pump-mediated resistance to new beta lactam antibiotics in multidrug-resistant gram-negative bacteria.* **Communications Medicine** (Aug **2024**). DOI: **10.1038/s43856-024-00591-y**. https://doi.org/10.1038/s43856-024-00591-y (chiang2024effluxpumpmediatedresistance pages 1-2)
- Zhao Y, et al. *Multidrug resistance in Pseudomonas aeruginosa: genetic control mechanisms and therapeutic advances.* **Molecular Biomedicine** (Nov **2024**). DOI: **10.1186/s43556-024-00221-y**. https://doi.org/10.1186/s43556-024-00221-y (zhao2024multidrugresistancein pages 1-2)
- Bollen C, et al. *Environmental, mechanistic and evolutionary landscape of antibiotic persistence.* **EMBO reports** (Jul **2023**). DOI: **10.15252/embr.202357309**. https://doi.org/10.15252/embr.202357309 (bollen2023environmentalmechanisticand pages 1-2, bollen2023environmentalmechanisticand pages 2-3)
- Salzer A, Wolz C. *Role of (p)ppGpp in antibiotic resistance, tolerance, persistence and survival in Firmicutes.* **microLife** (Mar **2023**). DOI: **10.1093/femsml/uqad009**. https://doi.org/10.1093/femsml/uqad009 (salzer2023roleof(p)ppgpp pages 1-1, salzer2023roleof(p)ppgpp pages 6-7, salzer2023roleof(p)ppgpp pages 7-8)
- Mendelson M, et al. *Ensuring progress on sustainable access to effective antibiotics at the 2024 UN General Assembly: a target-based approach.* **The Lancet** (Jun **2024**). DOI: **10.1016/S0140-6736(24)01019-5**. https://doi.org/10.1016/S0140-6736(24)01019-5 (mendelson2024ensuringprogresson pages 1-4)
- Klein EY, et al. *Global trends in antibiotic consumption during 2016–2023 and future projections through 2030.* **PNAS** (Nov **2024**). DOI: **10.1073/pnas.2411919121**. https://doi.org/10.1073/pnas.2411919121 (klein2024globaltrendsin pages 6-7, klein2024globaltrendsin pages 1-2)
- Naghavi M, et al. *Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050.* **The Lancet** (Sep **2024**). DOI: **10.1016/S0140-6736(24)01867-1**. https://doi.org/10.1016/S0140-6736(24)01867-1 (naghavi2024globalburdenof pages 1-2)
- Singha B, et al. *Alternative therapeutics to control antimicrobial resistance: a general perspective.* **Frontiers in Drug Discovery** (Jul **2024**). DOI: **10.3389/fddsv.2024.1385460**. https://doi.org/10.3389/fddsv.2024.1385460 (singha2024alternativetherapeuticsto pages 3-4)
- Galgano M, et al. *Acquired bacterial resistance to antibiotics and resistance genes: from past to future.* **Antibiotics** (Feb **2025**). DOI: **10.3390/antibiotics14030222**. https://doi.org/10.3390/antibiotics14030222 (galgano2025acquiredbacterialresistance pages 7-8)
- Marino A, et al. *The global burden of multidrug-resistant bacteria.* **Epidemiologia** (May **2025**). DOI: **10.3390/epidemiologia6020021**. https://doi.org/10.3390/epidemiologia6020021 (marino2025theglobalburden pages 13-14, marino2025theglobalburden pages 11-13)


References

1. (belay2024mechanismofantibacterial media 58316221): Wubetu Yihunie Belay, Melese Getachew, Bantayehu Addis Tegegne, Zigale Hibstu Teffera, Abebe Dagne, Tirsit Ketsela Zeleke, Rahel Belete Abebe, Abebaw Abie Gedif, Abebe Fenta, Getasew Yirdaw, Adane Tilahun, and Yibeltal Aschale. Mechanism of antibacterial resistance, strategies and next-generation antimicrobials to contain antimicrobial resistance: a review. Frontiers in Pharmacology, Aug 2024. URL: https://doi.org/10.3389/fphar.2024.1444781, doi:10.3389/fphar.2024.1444781. This article has 230 citations.

2. (belay2024mechanismofantibacterial pages 3-4): Wubetu Yihunie Belay, Melese Getachew, Bantayehu Addis Tegegne, Zigale Hibstu Teffera, Abebe Dagne, Tirsit Ketsela Zeleke, Rahel Belete Abebe, Abebaw Abie Gedif, Abebe Fenta, Getasew Yirdaw, Adane Tilahun, and Yibeltal Aschale. Mechanism of antibacterial resistance, strategies and next-generation antimicrobials to contain antimicrobial resistance: a review. Frontiers in Pharmacology, Aug 2024. URL: https://doi.org/10.3389/fphar.2024.1444781, doi:10.3389/fphar.2024.1444781. This article has 230 citations.

3. (chiang2024effluxpumpmediatedresistance pages 1-2): Augusto Dulanto Chiang and John P. Dekker. Efflux pump-mediated resistance to new beta lactam antibiotics in multidrug-resistant gram-negative bacteria. Communications Medicine, Aug 2024. URL: https://doi.org/10.1038/s43856-024-00591-y, doi:10.1038/s43856-024-00591-y. This article has 72 citations and is from a peer-reviewed journal.

4. (salzer2023roleof(p)ppgpp pages 1-1): Andrea Salzer and Christiane Wolz. Role of (p)ppgpp in antibiotic resistance, tolerance, persistence and survival in firmicutes. microLife, Mar 2023. URL: https://doi.org/10.1093/femsml/uqad009, doi:10.1093/femsml/uqad009. This article has 50 citations and is from a peer-reviewed journal.

5. (bollen2023environmentalmechanisticand pages 1-2): Celien Bollen, Elen Louwagie, Natalie Verstraeten, Jan Michiels, and Philip Ruelens. Environmental, mechanistic and evolutionary landscape of antibiotic persistence. EMBO reports, Jul 2023. URL: https://doi.org/10.15252/embr.202357309, doi:10.15252/embr.202357309. This article has 46 citations and is from a highest quality peer-reviewed journal.

6. (bollen2023environmentalmechanisticand pages 2-3): Celien Bollen, Elen Louwagie, Natalie Verstraeten, Jan Michiels, and Philip Ruelens. Environmental, mechanistic and evolutionary landscape of antibiotic persistence. EMBO reports, Jul 2023. URL: https://doi.org/10.15252/embr.202357309, doi:10.15252/embr.202357309. This article has 46 citations and is from a highest quality peer-reviewed journal.

7. (zhang2024bacterialeffluxpump pages 2-4): Lan Zhang, Xiaoyuan Tian, Lei Sun, Kun Mi, Ru Wang, Fengying Gong, and Lingli Huang. Bacterial efflux pump inhibitors reduce antibiotic resistance. Pharmaceutics, 16:170, Jan 2024. URL: https://doi.org/10.3390/pharmaceutics16020170, doi:10.3390/pharmaceutics16020170. This article has 132 citations.

8. (zhao2024multidrugresistancein pages 1-2): Yuanjing Zhao, Haoran Xu, Hui Wang, Ping Wang, and Simin Chen. Multidrug resistance in pseudomonas aeruginosa: genetic control mechanisms and therapeutic advances. Molecular Biomedicine, Nov 2024. URL: https://doi.org/10.1186/s43556-024-00221-y, doi:10.1186/s43556-024-00221-y. This article has 29 citations and is from a peer-reviewed journal.

9. (salzer2023roleof(p)ppgpp pages 6-7): Andrea Salzer and Christiane Wolz. Role of (p)ppgpp in antibiotic resistance, tolerance, persistence and survival in firmicutes. microLife, Mar 2023. URL: https://doi.org/10.1093/femsml/uqad009, doi:10.1093/femsml/uqad009. This article has 50 citations and is from a peer-reviewed journal.

10. (salzer2023roleof(p)ppgpp pages 7-8): Andrea Salzer and Christiane Wolz. Role of (p)ppgpp in antibiotic resistance, tolerance, persistence and survival in firmicutes. microLife, Mar 2023. URL: https://doi.org/10.1093/femsml/uqad009, doi:10.1093/femsml/uqad009. This article has 50 citations and is from a peer-reviewed journal.

11. (mendelson2024ensuringprogresson pages 1-4): Marc Mendelson, Joseph A Lewnard, Mike Sharland, Aislinn Cook, Koen B Pouwels, Yewande Alimi, Mirfin Mpundu, Evelyn Wesangula, Jeffrey Scott Weese, John-Arne Røttingen, and Ramanan Laxminarayan. Ensuring progress on sustainable access to effective antibiotics at the 2024 un general assembly: a target-based approach. The Lancet, 403:2551-2564, Jun 2024. URL: https://doi.org/10.1016/s0140-6736(24)01019-5, doi:10.1016/s0140-6736(24)01019-5. This article has 124 citations and is from a highest quality peer-reviewed journal.

12. (klein2024globaltrendsin pages 1-2): Eili Y. Klein, Isabella Impalli, Suprena Poleon, Philippe Denoel, Mariateresa Cipriano, Thomas P. Van Boeckel, Simone Pecetta, David E. Bloom, and Arindam Nandi. Global trends in antibiotic consumption during 2016–2023 and future projections through 2030. Proceedings of the National Academy of Sciences of the United States of America, Nov 2024. URL: https://doi.org/10.1073/pnas.2411919121, doi:10.1073/pnas.2411919121. This article has 428 citations and is from a highest quality peer-reviewed journal.

13. (klein2024globaltrendsin pages 6-7): Eili Y. Klein, Isabella Impalli, Suprena Poleon, Philippe Denoel, Mariateresa Cipriano, Thomas P. Van Boeckel, Simone Pecetta, David E. Bloom, and Arindam Nandi. Global trends in antibiotic consumption during 2016–2023 and future projections through 2030. Proceedings of the National Academy of Sciences of the United States of America, Nov 2024. URL: https://doi.org/10.1073/pnas.2411919121, doi:10.1073/pnas.2411919121. This article has 428 citations and is from a highest quality peer-reviewed journal.

14. (marino2025theglobalburden pages 13-14): Andrea Marino, Antonino Maniaci, Mario Lentini, Salvatore Ronsivalle, Giuseppe Nunnari, Salvatore Cocuzza, Federica Maria Parisi, Bruno Cacopardo, Salvatore Lavalle, and Luigi La Via. The global burden of multidrug-resistant bacteria. Epidemiologia, 6:21, May 2025. URL: https://doi.org/10.3390/epidemiologia6020021, doi:10.3390/epidemiologia6020021. This article has 93 citations.

15. (zhang2024bacterialeffluxpump pages 1-2): Lan Zhang, Xiaoyuan Tian, Lei Sun, Kun Mi, Ru Wang, Fengying Gong, and Lingli Huang. Bacterial efflux pump inhibitors reduce antibiotic resistance. Pharmaceutics, 16:170, Jan 2024. URL: https://doi.org/10.3390/pharmaceutics16020170, doi:10.3390/pharmaceutics16020170. This article has 132 citations.

16. (naghavi2024globalburdenof pages 1-2): Mohsen Naghavi, Stein Emil Vollset, Kevin S Ikuta, Lucien R Swetschinski, Authia P Gray, Eve E Wool, Gisela Robles Aguilar, Tomislav Mestrovic, Georgia Smith, Chieh Han, Rebecca L Hsu, Julian Chalek, Daniel T Araki, Erin Chung, Catalina Raggi, Anna Gershberg Hayoon, Nicole Davis Weaver, Paulina A Lindstedt, Amanda E Smith, Umut Altay, Natalia V Bhattacharjee, Konstantinos Giannakis, Frederick Fell, Barney McManigal, Nattwut Ekapirat, Jessica Andretta Mendes, Tilleye Runghien, Oraya Srimokla, Atef Abdelkader, Sherief Abd-Elsalam, Richard Gyan Aboagye, Hassan Abolhassani, Hasan Abualruz, Usman Abubakar, Hana J Abukhadijah, Salahdein Aburuz, Ahmed Abu-Zaid, Sureerak Achalapong, Isaac Yeboah Addo, Victor Adekanmbi, Temitayo Esther Adeyeoluwa, Qorinah Estiningtyas Sakilah Adnani, Leticia Akua Adzigbli, Muhammad Sohail Afzal, Saira Afzal, Antonella Agodi, Austin J Ahlstrom, Aqeel Ahmad, Sajjad Ahmad, Tauseef Ahmad, Ali Ahmadi, Ayman Ahmed, Haroon Ahmed, Ibrar Ahmed, Mohammed Ahmed, Saeed Ahmed, Syed Anees Ahmed, Mohammed Ahmed Akkaif, Salah Al Awaidy, Yazan Al Thaher, Samer O Alalalmeh, Mohammad T AlBataineh, Wafa A Aldhaleei, Adel Ali Saeed Al-Gheethi, Nma Bida Alhaji, Abid Ali, Liaqat Ali, Syed Shujait Ali, Waad Ali, Kasim Allel, Sabah Al-Marwani, Ahmad Alrawashdeh, Awais Altaf, Alaa B. Al-Tammemi, Jaffar A Al-Tawfiq, Karem H Alzoubi, Walid Adnan Al-Zyoud, Ben Amos, John H Amuasi, Robert Ancuceanu, Jason R Andrews, Abhishek Anil, Iyadunni Adesola Anuoluwa, Saeid Anvari, Anayochukwu Edward Anyasodor, Geminn Louis Carace Apostol, Jalal Arabloo, Mosab Arafat, Aleksandr Y Aravkin, Demelash Areda, Abdulfatai Aremu, Anton A Artamonov, Elizabeth A Ashley, Marvellous O Asika, Seyyed Shamsadin Athari, Maha Moh'd Wahbi Atout, Tewachew Awoke, Sina Azadnajafabad, James Mba Azam, Shahkaar Aziz, Ahmed Y. Azzam, Mahsa Babaei, Francois-Xavier Babin, Muhammad Badar, Atif Amin Baig, Milica Bajcetic, Stephen Baker, Mainak Bardhan, Hiba Jawdat Barqawi, Zarrin Basharat, Afisu Basiru, Mathieu Bastard, Saurav Basu, Nebiyou Simegnew Bayleyegn, Melaku Ashagrie Belete, Olorunjuwon Omolaja Bello, Apostolos Beloukas, James A Berkley, Akshaya Srikanth Bhagavathula, Sonu Bhaskar, Soumitra S Bhuyan, Julia A Bielicki, Nikolay Ivanovich Briko, Colin Stewart Brown, Annie J Browne, Danilo Buonsenso, Yasser Bustanji, Cristina G Carvalheiro, Carlos A Castañeda-Orjuela, Muthia Cenderadewi, Joshua Chadwick, Sandip Chakraborty, Rama Mohan Chandika, Sara Chandy, Vilada Chansamouth, Vijay Kumar Chattu, Anis Ahmad Chaudhary, Patrick R Ching, Hitesh Chopra, Fazle Rabbi Chowdhury, Dinh-Toi Chu, Muhammad Chutiyami, Natalia Cruz-Martins, Alanna Gomes da Silva, Omid Dadras, Xiaochen Dai, Samuel D Darcho, Saswati Das, Fernando Pio De la Hoz, Denise Myriam Dekker, Kuldeep Dhama, Daniel Diaz, Benjamin Felix Rothschild Dickson, Serge Ghislain Djorie, Milad Dodangeh, Sushil Dohare, Klara Georgieva Dokova, Ojas Prakashbhai Doshi, Robert Kokou Dowou, Haneil Larson Dsouza, Susanna J Dunachie, Arkadiusz Marian Dziedzic, Tim Eckmanns, Abdelaziz Ed-Dra, Aziz Eftekharimehrabad, Temitope Cyrus Ekundayo, Iman El Sayed, Muhammed Elhadi, Waseem El-Huneidi, Christelle Elias, Sally J Ellis, Randa Elsheikh, Ibrahim Elsohaby, Chadi Eltaha, Babak Eshrati, Majid Eslami, David William Eyre, Adewale Oluwaseun Fadaka, Adeniyi Francis Fagbamigbe, Ayesha Fahim, Aliasghar Fakhri-Demeshghieh, Folorunso Oludayo Fasina, Modupe Margaret Fasina, Ali Fatehizadeh, Nicholas A Feasey, Alireza Feizkhah, Ginenus Fekadu, Florian Fischer, Ida Fitriana, Karen M Forrest, Celia Fortuna Rodrigues, John E Fuller, Muktar A Gadanya, Márió Gajdács, Aravind P Gandhi, Esteban E Garcia-Gallo, Denise O Garrett, Rupesh K Gautam, Miglas Welay Gebregergis, Mesfin Gebrehiwot, Teferi Gebru Gebremeskel, Christine Geffers, Leonidas Georgalis, Ramy Mohamed Ghazy, Mahaveer Golechha, Davide Golinelli, Melita Gordon, Snigdha Gulati, Rajat Das Gupta, Sapna Gupta, Vijai Kumar Gupta, Awoke Derbie Habteyohannes, Sebastian Haller, Harapan Harapan, Michelle L Harrison, Ahmed I Hasaballah, Ikramul Hasan, Rumina Syeda Hasan, Hamidreza Hasani, Andrea Haekyung Haselbeck, Md Saquib Hasnain, Ikrama Ibrahim Hassan, Shoaib Hassan, Mahgol Sadat Hassan Zadeh Tabatabaei, Khezar Hayat, Jiawei He, Omar E Hegazi, Mohammad Heidari, Kamal Hezam, Ramesh Holla, Marianne Holm, Heidi Hopkins, Md Mahbub Hossain, Mehdi Hosseinzadeh, Sorin Hostiuc, Nawfal R Hussein, Le Duc Huy, Elsa D Ibáñez-Prada, Adalia Ikiroma, Irena M Ilic, Sheikh Mohammed Shariful Islam, Faisal Ismail, Nahlah Elkudssiah Ismail, Chidozie Declan Iwu, Chinwe Juliana Iwu-Jaja, Abdollah Jafarzadeh, Fatoumatta Jaiteh, Reza Jalilzadeh Yengejeh, Roland Dominic G Jamora, Javad Javidnia, Talha Jawaid, Adam W J Jenney, Hyon Jin Jeon, Mohammad Jokar, Nabi Jomehzadeh, Tamas Joo, Nitin Joseph, Zul Kamal, Kehinde Kazeem Kanmodi, Rami S Kantar, James Apollo Kapisi, Ibraheem M Karaye, Yousef Saleh Khader, Himanshu Khajuria, Nauman Khalid, Faham Khamesipour, Ajmal Khan, Mohammad Jobair Khan, Muhammad Tariq Khan, Vishnu Khanal, Feriha Fatima Khidri, Jagdish Khubchandani, Suwimon Khusuwan, Min Seo Kim, Adnan Kisa, Vladimir Andreevich Korshunov, Fiorella Krapp, Ralf Krumkamp, Mohammed Kuddus, Mukhtar Kulimbet, Dewesh Kumar, Emmanuelle A P Kumaran, Ambily Kuttikkattu, Hmwe Hmwe Kyu, Iván Landires, Basira Kankia Lawal, Thao Thi Thu Le, Ingeborg Maria Lederer, Munjae Lee, Seung Won Lee, Alain Lepape, Temesgen Leka Lerango, Virendra S Ligade, Cherry Lim, Stephen S Lim, Liknaw Workie Limenh, Chaojie Liu, Xiaofeng Liu, Xuefeng Liu, Michael J Loftus, Hawraz Ibrahim M Amin, Kelsey Lynn Maass, Sandeep B Maharaj, Mansour Adam Mahmoud, Panagiota Maikanti-Charalampous, Omar M Makram, Kashish Malhotra, Ahmad Azam Malik, Georgia D Mandilara, Florian Marks, Bernardo Alfonso Martinez-Guerra, Miquel Martorell, Hossein Masoumi-Asl, Alexander G Mathioudakis, Juergen May, Theresa A McHugh, James Meiring, Hadush Negash Meles, Addisu Melese, Endalkachew Belayneh Melese, Giuseppe Minervini, Nouh Saad Mohamed, Shafiu Mohammed, Syam Mohan, Ali H Mokdad, Lorenzo Monasta, AmirAli Moodi Ghalibaf, Catrin E Moore, Yousef Moradi, Elias Mossialos, Vincent Mougin, George Duke Mukoro, Francesk Mulita, Berit Muller-Pebody, Efren Murillo-Zamora, Sani Musa, Patrick Musicha, Lillian A Musila, Saravanan Muthupandian, Ahamarshan Jayaraman Nagarajan, Pirouz Naghavi, Firzan Nainu, Tapas Sadasivan Nair, Hastyar Hama Rashid Najmuldeen, Zuhair S Natto, Javaid Nauman, Biswa Prakash Nayak, G Takop Nchanji, Pacifique Ndishimye, Ionut Negoi, Ruxandra Irina Negoi, Seyed Aria Nejadghaderi, QuynhAnh P Nguyen, Efaq Ali Noman, Davis C Nwakanma, Seamus O'Brien, Theresa J Ochoa, Ismail A Odetokun, Oluwaseun Adeolu Ogundijo, Tolulope R Ojo-Akosile, Sylvester Reuben Okeke, Osaretin Christabel Okonji, Andrew T Olagunju, Antonio Olivas-Martinez, Abdulhakeem Abayomi Olorukooba, Peter Olwoch, Kenneth Ikenna Onyedibe, Edgar Ortiz-Brizuela, Olayinka Osuolale, Pradthana Ounchanum, Oyetunde T Oyeyemi, Mahesh Padukudru P A, Jose L Paredes, Romil R Parikh, Jay Patel, Shankargouda Patil, Shrikant Pawar, Anton Y Peleg, Prince Peprah, João Perdigão, Carlo Perrone, Ionela-Roxana Petcu, Koukeo Phommasone, Zahra Zahid Piracha, Dimitri Poddighe, Andrew J Pollard, Ramesh Poluru, Alfredo Ponce-De-Leon, Jagadeesh Puvvula, Farah Naz Qamar, Nameer Hashim Qasim, Clotaire Donatien Rafai, Pankaja Raghav, Leila Rahbarnia, Fakher Rahim, Vafa Rahimi-Movaghar, Mosiur Rahman, Muhammad Aziz Rahman, Hazem Ramadan, Shakthi Kumaran Ramasamy, Pushkal Sinduvadi Ramesh, Pramod W Ramteke, Rishabh Kumar Rana, Usha Rani, Mohammad-Mahdi Rashidi, Devarajan Rathish, Sayaphet Rattanavong, Salman Rawaf, Elrashdy Moustafa Mohamed Redwan, Luis Felipe Reyes, Tamalee Roberts, Julie V Robotham, Victor Daniel Rosenthal, Allen Guy Ross, Nitai Roy, Kristina E Rudd, Cameron John Sabet, Basema Ahmad Saddik, Mohammad Reza Saeb, Umar Saeed, Sahar Saeedi Moghaddam, Weeravoot Saengchan, Mohsen Safaei, Amene Saghazadeh, Narjes Saheb Sharif-Askari, Amirhossein Sahebkar, Soumya Swaroop Sahoo, Maitreyi Sahu, Morteza Saki, Nasir Salam, Zikria Saleem, Mohamed A Saleh, Yoseph Leonardo Samodra, Abdallah M Samy, Aswini Saravanan, Maheswar Satpathy, Austin E Schumacher, Mansour Sedighi, Samroeng Seekaew, Mahan Shafie, Pritik A Shah, Samiah Shahid, Moyad Jamal Shahwan, Sadia Shakoor, Noga Shalev, Muhammad Aaqib Shamim, Mohammad Ali Shamshirgaran, Anas Shamsi, Amin Sharifan, Rajesh P Shastry, Mahabalesh Shetty, Aminu Shittu, Sunil Shrestha, Emmanuel Edwar Siddig, Theologia Sideroglou, Jose Sifuentes-Osornio, Luís Manuel Lopes Rodrigues Silva, Eric A F Simões, Andrew J H Simpson, Amit Singh, Surjit Singh, Robert Sinto, Sameh S M Soliman, Soroush Soraneh, Nicole Stoesser, Temenuga Zhekova Stoeva, Chandan Kumar Swain, Lukasz Szarpak, Sree Sudha T Y, Shima Tabatabai, Celine Tabche, Zanan Mohammed-Ameen Taha, Ker-Kan Tan, Nidanuch Tasak, Nathan Y Tat, Areerat Thaiprakong, Pugazhenthan Thangaraju, Caroline Chepngeno Tigoi, Krishna Tiwari, Marcos Roberto Tovani-Palone, Thang Huu Tran, Munkhtuya Tumurkhuu, Paul Turner, Aniefiok John Udoakang, Arit Udoh, Noor Ullah, Saeed Ullah, Asokan Govindaraj Vaithinathan, Mario Valenti, Theo Vos, Huong T L Vu, Yasir Waheed, Ann Sarah Walker, Judd L Walson, Tri Wangrangsimakul, Kosala Gayan Weerakoon, Heiman F L Wertheim, Phoebe C M Williams, Asrat Arja Wolde, Teresa M Wozniak, Felicia Wu, Zenghong Wu, Mukesh Kumar Kumar Yadav, Sajad Yaghoubi, Zwanden Sule Yahaya, Amir Yarahmadi, Saber Yezli, Yazachew Engida Yismaw, Dong Keon Yon, Chun-Wei Yuan, Hadiza Yusuf, Fathiah Zakham, Giulia Zamagni, Haijun Zhang, Zhi-Jiang Zhang, Magdalena Zielińska, Alimuddin Zumla, Sa'ed H. H Zyoud, Samer H Zyoud, Simon I Hay, Andy Stergachis, Benn Sartorius, Ben S Cooper, Christiane Dolecek, and Christopher J L Murray. Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050. Lancet (London, England), 404:1199-1226, Sep 2024. URL: https://doi.org/10.1016/s0140-6736(24)01867-1, doi:10.1016/s0140-6736(24)01867-1. This article has 3885 citations.

17. (galgano2025acquiredbacterialresistance pages 7-8): Michela Galgano, Francesco Pellegrini, Elisabetta Catalano, Loredana Capozzi, Laura Del Sambro, Alessio Sposato, Maria Stella Lucente, Violetta Iris Vasinioti, Cristiana Catella, Amienwanlen Eugene Odigie, Maria Tempesta, Annamaria Pratelli, and Paolo Capozza. Acquired bacterial resistance to antibiotics and resistance genes: from past to future. Antibiotics, 14:222, Feb 2025. URL: https://doi.org/10.3390/antibiotics14030222, doi:10.3390/antibiotics14030222. This article has 82 citations.

18. (singha2024alternativetherapeuticsto pages 3-4): Biplab Singha, Vinayak Singh, and Vijay Soni. Alternative therapeutics to control antimicrobial resistance: a general perspective. Frontiers in Drug Discovery, Jul 2024. URL: https://doi.org/10.3389/fddsv.2024.1385460, doi:10.3389/fddsv.2024.1385460. This article has 81 citations.

19. (marino2025theglobalburden pages 11-13): Andrea Marino, Antonino Maniaci, Mario Lentini, Salvatore Ronsivalle, Giuseppe Nunnari, Salvatore Cocuzza, Federica Maria Parisi, Bruno Cacopardo, Salvatore Lavalle, and Luigi La Via. The global burden of multidrug-resistant bacteria. Epidemiologia, 6:21, May 2025. URL: https://doi.org/10.3390/epidemiologia6020021, doi:10.3390/epidemiologia6020021. This article has 93 citations.