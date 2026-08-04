---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:41:19.815652'
end_time: '2026-08-04T01:50:06.262601'
duration_seconds: 526.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum low
  trait_identifier: METPO:1000465
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration at
    or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant
    physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Non-halophile, NaO_<=1
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports low-salt optima as the non-halophilic / halotolerant end of the halophily
    axis.)'
  causal_graph_summary: 'nacl_optimum_low_non_halophile_setpoint: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000465
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration at or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Non-halophile, NaO_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports low-salt optima as the non-halophilic / halotolerant end of the halophily axis.)
- **Existing causal graph summary:** nacl_optimum_low_non_halophile_setpoint: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_low.yaml`.

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
- **Trait label:** NaCl optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000465
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration at or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Non-halophile, NaO_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports low-salt optima as the non-halophilic / halotolerant end of the halophily axis.)
- **Existing causal graph summary:** nacl_optimum_low_non_halophile_setpoint: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_low.yaml`.

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


# Curation-focused research report: NaCl optimum low

## Trait record and scope

- **Trait label:** NaCl optimum low
- **Trait identifier:** **METPO:1000465**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** METPO:1000333
- **Operational definition:** best measured growth at **≤ approximately 1% (w/v) NaCl**—about **10 g L⁻¹ or 0.17 M NaCl**—under the stated assay conditions.

This is primarily an **assay-derived environmental optimum**, i.e., the NaCl concentration at which a growth response such as specific growth rate, yield, colony size, or activity is maximal. It is not itself a molecular mechanism. The biologically defensible mechanism is that low external NaCl avoids the energetic, hydration, ionic-strength, and proteome-level costs incurred when a salt-out organism must compensate for hyperosmotic stress.

### Essential boundaries

1. **Optimum is not maximum tolerance.** A low-optimum organism can remain halotolerant at substantially higher NaCl. In freshwater *“Candidatus Methanoperedens”*, acute exposure to 0.5% salinity caused approximately 50% activity loss, 1% permitted slower methane oxidation, and 2% eliminated activity, yet gradual acclimation over about 12 weeks preserved methane oxidation at 3%. Thus acclimation history can strongly separate the measured optimum from the upper tolerance limit. (medrano2024osmoregulationinfreshwater pages 6-7, medrano2024osmoregulationinfreshwater pages 1-2)
2. **Non-halophile is not synonymous with salt-sensitive.** “Halotolerant” means able to tolerate high salinity without requiring it; such an organism may still have its growth optimum at ≤1% NaCl. The synonyms in the record should therefore be treated as search labels, not strict equivalences. (bremer2019responsesofmicroorganisms pages 3-5)
3. **NaCl concentration is not total osmotic pressure.** Sucrose, other salts, medium nutrients, pH, and temperature can alter osmolality and water activity. NaCl additionally imposes Na⁺/Cl⁻-specific ionic effects.
4. **The threshold is approximate.** A coarse concentration series containing only 0%, 1%, and 3% cannot localize an optimum precisely. Percentage must be recorded as w/v, w/w, or seawater-equivalent salinity.
5. **Acute challenge, chronic growth, and evolutionary habitat preference are different endpoints.** They should not be merged into one causal edge.

## Current mechanistic understanding

A hyperosmotic NaCl upshift draws water from the cell on a millisecond timescale. Cytoplasmic volume can decrease by several percent to as much as 50%, causing loss of turgor, increased macromolecular crowding, and increased intracellular solute concentration and ionic strength. Model bacteria contain roughly 200–250 mg mL⁻¹ cytoplasmic macromolecules, corresponding to about 20% excluded volume, making further crowding physiologically consequential. (foster2024bacterialcellvolume pages 6-8)

Salt-out bacteria first accumulate K⁺, with glutamate imported or synthesized as a counterion. They subsequently replace much of this ionic osmolyte pool with compatible organic solutes—such as glycine betaine, trehalose, proline, ectoine, and carnitine—to restore hydration and turgor without maintaining damaging cytoplasmic ionic strength. Under downshift, MscL/MscS-family mechanosensitive channels act as emergency-release valves for ions and osmolytes. (bremer2019responsesofmicroorganisms pages 3-5, bremer2019responsesofmicroorganisms pages 5-6)

This compensation has a fitness cost. The reviewed estimate for ectoine synthesis is approximately 40–50 high-energy bonds, whereas ABC-mediated import costs about two ATP hydrolyses. A low-salt optimum can therefore arise because stress-free growth avoids both osmolyte-production costs and ionic/proteostatic damage, even though inducible systems permit survival at higher salt. (bremer2019responsesofmicroorganisms pages 5-6)

A major 2024 synthesis identifies cyclic di-AMP as a master regulator of bacterial cell volume. It inhibits K⁺ and compatible-solute influx and promotes K⁺ efflux. Trk/Ktr gating components bind c-di-AMP with reported affinities of approximately 40 nM–8 μM. Excess c-di-AMP reduces K⁺ uptake and causes hypertonic sensitivity and easier plasmolysis; deficient c-di-AMP causes toxic K⁺ accumulation, larger cells, slower growth, and greater lysis after hypotonic challenge. These effects demonstrate that osmolyte control is causal for salt fitness, although c-di-AMP is lineage-restricted and is not a universal marker of low NaCl optimum. (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 12-13)

## Candidate nodes and ontology grounding

Only identifiers that can be stated confidently are supplied; otherwise label-only nodes are preferable to invented CURIEs.

### Trait and environmental/assay nodes

| Candidate node | Type | Suggested grounding or status |
|---|---|---|
| NaCl optimum low | trait endpoint | **METPO:1000465** |
| Parent NaCl-optimum trait | trait | **METPO:1000333** |
| sodium chloride | chemical/exposure | **CHEBI:26710** |
| sodium ion | chemical | **CHEBI:29101** |
| chloride | chemical | **CHEBI:17996** |
| water | chemical | **CHEBI:15377** |
| potassium ion | chemical | **CHEBI:29103** |
| low external NaCl, hyperosmotic upshift, hypoosmotic downshift | experimental/environmental factors | Label-only unless the project has approved ENVO/OBI assay terms |
| growth rate, biomass yield, methane-oxidation activity | assay outputs | Label-only; do not collapse distinct outputs |

### Processes, states, and cellular locations

| Candidate node | Type | Suggested grounding/status |
|---|---|---|
| response to osmotic stress | biological process | **GO:0006970** |
| potassium-ion transport | biological process | **GO:0006813** |
| transmembrane transport | biological process | **GO:0055085** |
| plasma/cytoplasmic membrane | cellular component | **GO:0005886** |
| cytoplasm | cellular component | **GO:0005737** |
| water efflux; cytoplasmic dehydration; cell-volume reduction; loss/restoration of turgor; macromolecular crowding; compatible-solute accumulation; hypoosmotic solute release | process/state | Label-only candidates; verify exact ontology terms before YAML insertion |

### Genes, proteins, transporters, and regulatory modules

- **K⁺ influx:** TrkAH, KtrAB/KtrCD, KimA, KdpFABC, KupA/KupB.
- **K⁺ regulation:** KdpDE; c-di-AMP cyclases/phosphodiesterases such as CdaA and GdpP; c-di-AMP-responsive riboswitches.
- **Compatible-solute import:** OpuA/OpuC, ProP, ProU, BetP, BusAA–BusAB.
- **Na⁺ export:** NhaA and NhaB Na⁺/H⁺ antiporters.
- **Downshift protection:** MscL, MscS, MscM and YnaI-family mechanosensitive channels.
- **Taxon-specific ANME module:** **kamA** (KEGG **K01843**), **ablB** (KEGG **K21935**), and neighboring **ynaI**. The 2024 study reports these genes in an operon associated with N(ε)-acetyl-β-L-lysine synthesis and salt response. (medrano2024osmoregulationinfreshwater pages 3-4, medrano2024osmoregulationinfreshwater pages 10-13)

Protein identifiers should be assigned at the strain level. Gene symbols alone should not be mapped to a single UniProt accession across taxa.

### Metabolites and chemical modules

- **Broad compatible solutes:** glycine betaine, trehalose, proline, ectoine/hydroxyectoine, carnitine, glucosylglycerol, and dimethylsulfoniopropionate.
- **Primary ionic phase:** K⁺ and glutamate.
- **Taxon-specific osmolyte:** N(ε)-acetyl-β-L-lysine.
- **Potential ancillary modules:** polyhydroxyalkanoates and nonulosonic/sialic acids; these require conservative interpretation.
- **Second messenger:** cyclic di-AMP.

## Candidate causal edges

The compact high-confidence graph is summarized below.

| subject | predicate | object | evidence strength/taxon scope | DOI |
|---|---|---|---|---|
| low external NaCl (assay condition; ~<=1% w/v) | permits maximal growth of | NaCl optimum low phenotype endpoint (assay-defined optimum, not max tolerance) | Moderate; phenotype-scope statement supported by reviewed osmoadaptation literature and 2024 acclimation boundary-case data; broad microbes, not a single mechanism (bremer2019responsesofmicroorganisms pages 3-5, medrano2024osmoregulationinfreshwater pages 1-2) | 10.1146/annurev-micro-020518-115504; 10.1093/ismejo/wrae137 |
| hyperosmotic NaCl upshift | causes | water efflux and decreased cytoplasmic volume / cell shrinkage | High; broad bacteria (foster2024bacterialcellvolume pages 6-8, bremer2019responsesofmicroorganisms pages 1-2) | 10.1128/mmbr.00181-23; 10.1146/annurev-micro-020518-115504 |
| K+ uptake | helps restore | osmotic balance / turgor after osmotic upshift | High; broad bacteria (foster2024bacterialcellvolume pages 6-8, bremer2019responsesofmicroorganisms pages 1-2) | 10.1128/mmbr.00181-23; 10.1146/annurev-micro-020518-115504 |
| glutamate uptake or synthesis | counterbalances | imported K+ during osmotic upshift | High; broad bacteria (foster2024bacterialcellvolume pages 6-8, wood1999osmosensingbybacteria pages 14-15) | 10.1128/mmbr.00181-23; 10.1128/mmbr.63.1.230-262.1999 |
| compatible-solute synthesis/import (e.g., glycine betaine, trehalose, ectoine, proline) | restores | cellular hydration/turgor while lowering cytoplasmic ionic strength | High; broad salt-out bacteria (bremer2019responsesofmicroorganisms pages 3-5, bremer2019responsesofmicroorganisms pages 5-6) | 10.1146/annurev-micro-020518-115504 |
| c-di-AMP | inhibits | K+ influx systems (e.g., Trk/Ktr/KimA/Kdp-linked import control) | High; multiple bacterial taxa (foster2024bacterialcellvolume pages 8-10, bremer2019responsesofmicroorganisms pages 11-13, foster2024bacterialcellvolume pages 6-8) | 10.1128/mmbr.00181-23; 10.1146/annurev-micro-020518-115504 |
| high intracellular c-di-AMP | increases | hypertonic sensitivity / plasmolysis propensity | High; multiple bacterial taxa (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) | 10.1128/mmbr.00181-23 |
| hypoosmotic downshift | activates | mechanosensitive channels MscL/MscS | High; broad bacteria, best established in E. coli and related systems (wood1999osmosensingbybacteria pages 17-18, bremer2019responsesofmicroorganisms pages 5-6, bremer2019responsesofmicroorganisms pages 10-11) | 10.1128/mmbr.63.1.230-262.1999; 10.1146/annurev-micro-020518-115504 |
| activated MscL/MscS | releases | osmolytes and ions during downshift | High; broad bacteria, strongest in model systems (wood1999osmosensingbybacteria pages 17-18, bremer2019responsesofmicroorganisms pages 3-5, bremer2019responsesofmicroorganisms pages 5-6) | 10.1128/mmbr.63.1.230-262.1999; 10.1146/annurev-micro-020518-115504 |
| Na+/H+ antiport (NhaA/NhaB) | increases | NaCl tolerance | High; direct mutant evidence in E. coli; taxon-specific but canonical (wood1999osmosensingbybacteria pages 14-15) | 10.1128/mmbr.63.1.230-262.1999 |
| salt stress / increased salinity | induces expression of | kamA and ablB | Moderate-High; taxon-specific to Ca. Methanoperedens enrichment / ANME context (medrano2024osmoregulationinfreshwater pages 10-13, medrano2024osmoregulationinfreshwater pages 1-2) | 10.1093/ismejo/wrae137 |
| kamA + ablB | enables synthesis of | N(ε)-acetyl-β-L-lysine | High; taxon-specific direct biochemical/genomic assignment in Ca. Methanoperedens study (medrano2024osmoregulationinfreshwater pages 10-13, medrano2024osmoregulationinfreshwater pages 6-7) | 10.1093/ismejo/wrae137 |
| N(ε)-acetyl-β-L-lysine accumulation | supports | salt-stress acclimation | Moderate; taxon-specific to Ca. Methanoperedens / ANME, supported by metabolomics + expression (medrano2024osmoregulationinfreshwater pages 9-10, medrano2024osmoregulationinfreshwater pages 1-2) | 10.1093/ismejo/wrae137 |


*Table: This table summarizes the most defensible causal triples for curating METPO:1000465, prioritizing broadly supported osmoadaptation mechanisms and clearly flagging taxon-specific ANME salt-acclimation edges.*

The following expanded table supplies curation snippets and interpretive notes. Snippets are short extracts or tightly faithful source summaries.

| Subject–predicate–object triple | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| Hyperosmotic NaCl upshift **causes** water efflux and cytoplasmic-volume reduction | 10.1128/mmbr.00181-23 | “Under hypertonic conditions, water leaves the cell,” and volume decreases “several percent up to 50%.” | **High confidence**, broad bacterial biophysics; NaCl is one possible hypertonic agent. (foster2024bacterialcellvolume pages 6-8) |
| Water efflux/cell shrinkage **increases** crowding and ionic strength and **decreases** turgor | 10.1128/mmbr.00181-23 | Water movement occurs on the millisecond timescale with “rapid decrease in turgor pressure” and increased crowding, solute concentration, and ionic strength. | **High confidence**, direct physical consequence. (foster2024bacterialcellvolume pages 6-8) |
| Osmotic upshift **stimulates** K⁺ accumulation | 10.1128/mmbr.00181-23 | “Bacterial cells commonly import a lot of potassium during an osmotic upshift.” | **High confidence**, broad but transporter choice is taxon-dependent. (foster2024bacterialcellvolume pages 6-8) |
| K⁺ accumulation **stimulates/requires** glutamate uptake or synthesis for electroneutrality | 10.1128/mmbr.00181-23 | Counterions, “most commonly glutamate, are swiftly imported and/or synthesized.” | **High confidence** as a common model; not universal across all microbes. (foster2024bacterialcellvolume pages 6-8) |
| Compatible-solute synthesis/import **replaces** sustained K⁺ accumulation and **restores** hydration/turgor | 10.1146/annurev-micro-020518-115504 | Salt-out organisms accumulate compatible solutes and “tightly control their intracellular K⁺ and Na⁺ pools”; this permits K⁺ export without compromising cytoplasmic osmotic potential. | **High confidence** for salt-out bacteria; directly relevant to non-halophilic physiology. (bremer2019responsesofmicroorganisms pages 3-5) |
| c-di-AMP **inhibits** Trk/Ktr-mediated K⁺ influx | 10.1128/mmbr.00181-23 | Gating subunits bind c-di-AMP at **40 nM–8 μM**, destabilizing the gating/transmembrane interaction. | **High confidence**, multiple Firmicutes, Actinobacteria, Cyanobacteria, and mycoplasmas; not universal. (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8) |
| High c-di-AMP **causes** reduced K⁺ import and hypertonic sensitivity | 10.1128/mmbr.00181-23 | High-c-di-AMP mutants have reduced K⁺ import, decrease in size, become hypertonically sensitive, and plasmolyze more readily. | **High confidence**, perturbation/suppressor evidence across several bacteria. (foster2024bacterialcellvolume pages 6-8) |
| Low c-di-AMP **causes** excess K⁺ accumulation, slow growth, and hypotonic lysis | 10.1128/mmbr.00181-23 | Low-c-di-AMP mutants accumulate K⁺ to toxic levels, enlarge, grow more slowly, and lyse more readily under hypotonic conditions. | **High confidence**, but this explains volume homeostasis rather than low optimum directly. (foster2024bacterialcellvolume pages 6-8) |
| c-di-AMP **inhibits** OpuA-like compatible-solute import | 10.1128/mmbr.00181-23; 10.1146/annurev-micro-020518-115504 | c-di-AMP binds CBS domains of OpuA/OpuC-family ABC importers and inhibits compatible-solute uptake. | **High/moderate confidence**, direct in selected Gram-positive taxa. (bremer2019responsesofmicroorganisms pages 13-14, foster2024bacterialcellvolume pages 12-13) |
| NhaA/NhaB Na⁺/H⁺ antiport **increases** NaCl tolerance | 10.1128/mmbr.63.1.230-262.1999 | Wild type tolerated 0.7 M NaCl, an **nhaA** mutant <0.4 M, and an **nhaA nhaB** double mutant was sensitive to 0.03 M. | **High confidence**, direct *E. coli* mutant evidence; **taxon-specific**. This is a tolerance edge, not proof of a low optimum. (wood1999osmosensingbybacteria pages 14-15) |
| Hypoosmotic downshift **opens** MscL/MscS/MscM | 10.1146/annurev-micro-020518-115504 | Downshift raises turgor within milliseconds; channels with distinct thresholds open transiently as a graded emergency response. | **High confidence**, broad model-bacterium evidence. (bremer2019responsesofmicroorganisms pages 5-6, bremer2019responsesofmicroorganisms pages 10-11) |
| Open mechanosensitive channels **release** ions and compatible solutes and **prevent** rupture | 10.1146/annurev-micro-020518-115504 | Cells “rapidly jettison” organic and inorganic compounds through mechanosensitive channels to curb water influx. | **High confidence**; supports survival when low-optimum organisms return from saline to dilute conditions. (bremer2019responsesofmicroorganisms pages 3-5) |
| Acute salinity increase **decreases** methane-oxidation activity in freshwater *Ca. Methanoperedens* | 10.1093/ismejo/wrae137 | About 50% activity loss at 0.5%; slower oxidation at 1%; complete acute loss at 2%. | **High confidence but taxon/assay-specific**; directly supports a low-salt performance phenotype. (medrano2024osmoregulationinfreshwater pages 6-7) |
| Gradual acclimation **permits** methane oxidation at 3% salinity | 10.1093/ismejo/wrae137 | A 12-week gradual increase preserved activity under seawater-level salinity. | **High confidence, taxon-specific**; proves tolerance is history-dependent and should not redefine the optimum. (medrano2024osmoregulationinfreshwater pages 6-7, medrano2024osmoregulationinfreshwater pages 1-2) |
| Increased salinity **induces** kamA and ablB expression | 10.1093/ismejo/wrae137 | RT-qPCR showed strong salinity-dependent upregulation across six time points and salinity levels. | **Moderate-high**, enrichment-based and *Ca. Methanoperedens*-specific. (medrano2024osmoregulationinfreshwater pages 10-13) |
| KamA + AblB **produce** N(ε)-acetyl-β-L-lysine | 10.1093/ismejo/wrae137 | **kamA** encodes lysine-2,3-aminomutase and **ablB** β-lysine-N6-acetyltransferase; mass spectrometry identified the product. | **High for pathway assignment**, but organismal attribution partly depends on MAG/operon evidence. (medrano2024osmoregulationinfreshwater pages 10-13, medrano2024osmoregulationinfreshwater pages 6-7) |
| N(ε)-acetyl-β-L-lysine accumulation **supports** salt acclimation | 10.1093/ismejo/wrae137 | Metabolomics and expression identified it as the produced ANME osmolyte during salt stress. | **Moderate**, biologically strong but genetic knockout/rescue was not reported; mark taxon-specific. (medrano2024osmoregulationinfreshwater pages 9-10, medrano2024osmoregulationinfreshwater pages 1-2) |
| Increased salinity **changes** PHA and nonulosonic-acid metabolism | 10.1093/ismejo/wrae137 | PHA per biomass decreased with salt; pseudaminic/legionaminic acids increased while N-acetylneuraminate was unchanged. | **Uncertain as causal adaptation**; retain as associated-response edges only. (medrano2024osmoregulationinfreshwater pages 9-10, medrano2024osmoregulationinfreshwater pages 13-15) |

## Recent developments and quantitative evidence

### 2024: direct acclimation mechanism in freshwater methane oxidizers

The strongest recent phenotype-matched study is the 2024 ISME Journal analysis of freshwater anaerobic methane-oxidizing archaea. It combined activity assays, a 12-week salinity ramp, metagenomics, transcriptomics, proteomics, metabolomics, and physicochemical measurements. At 1.5% salinity, 286 transcripts were upregulated and 264 downregulated; 11 proteins increased and 17 decreased. Methyl-coenzyme M reductase transcripts decreased, while salt-dependent kamA/ablB expression and N(ε)-acetyl-β-L-lysine accumulation implicated a specific compatible-solute pathway. (medrano2024osmoregulationinfreshwater pages 9-10, medrano2024osmoregulationinfreshwater pages 10-13)

This work has direct environmental relevance: freshwater *Ca. Methanoperedens* acts as a methane biofilter in anoxic wetlands, so seawater intrusion may initially inhibit methane oxidation while gradual exposure selects or acclimates a more salt-tolerant state. The authors frame the result in the context of climate-driven sea-level rise and coastal salinization. (medrano2024osmoregulationinfreshwater pages 1-2)

### 2024: c-di-AMP as a cell-volume control hub

The 2024 MMBR review integrates biochemical binding, mutant, suppressor, transport, and morphology studies and argues that c-di-AMP is a master regulator of cell volume. Normal cytoplasmic K⁺ concentrations are approximately 250 mM in *E. coli*, 300 mM in *Bacillus subtilis*, and 500 mM in *Corynebacterium glutamicum* and *Lactococcus lactis*. These values underscore that salt adaptation is not simply exclusion of ions; it is active balancing of a large intracellular osmolyte pool. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 31-33)

### 2023: salinity is an evolutionary barrier, not merely an acute stress

A Science Advances phylogenomic study compiled 13,783 aquatic MAGs and retained 11,248 bacterial MAGs after quality filtering. The dataset included 7,643 freshwater, 2,240 brackish, and 1,365 marine bacterial genomes. At 95% ANI, 3,547 of 3,561 genome clusters were confined to one biome; only 14 crossed a biome pair. Among 310 monobiomic sister-group pairs, there were 136 brackish–marine, 119 freshwater–brackish, and only 55 freshwater–marine transitions. (jurdzinski2023largescalephylogenomicsof pages 1-2)

Higher salinity was associated with more acidic proteomes, changes in amino-acid composition, and convergent gene gains/losses. Brackish genomes were enriched in functions related to chemotaxis, transcriptional regulation, trehalose/polyamine synthesis, mobile elements, and competence. These are compelling evolutionary associations but do not establish that any one gene causes **METPO:1000465**. (jurdzinski2023largescalephylogenomicsof pages 10-11, jurdzinski2023largescalephylogenomicsof pages 11-12)

A separate 2024 Dead Sea spring study examined six MAGs from biofilms exposed to salinity shifts over seconds to minutes and proposed hybrid salt-in/salt-out strategies. Some *Halomonas* lineages spanned <1% to 20% salt tolerance, emphasizing again that low-salt growth and broad tolerance can coexist. Because this study is metagenomic and hypothesis-generating, its gene-content claims should be curated as associations rather than direct phenotype mechanisms. (ionescu2024extremefluctuationsin pages 4-6)

## Applications and real-world implementations

1. **Coastal methane-cycle prediction.** Acute salinization may suppress freshwater anaerobic methane oxidation, whereas gradual intrusion can permit acclimation. Models should therefore include exposure rate and history, not salinity alone. (medrano2024osmoregulationinfreshwater pages 6-7, medrano2024osmoregulationinfreshwater pages 1-2)
2. **Freshwater–brackish microbiome forecasting.** The rarity of cross-biome species and transitions indicates that salinity change may restructure communities rather than simply induce existing taxa. This matters for reservoirs, estuaries, aquaculture, wastewater systems, and desalination-impacted waters. (jurdzinski2023largescalephylogenomicsof pages 1-2, jurdzinski2023largescalephylogenomicsof pages 1-1)
3. **Industrial fermentation and cell-factory design.** Medium osmolarity affects turgor, cell division, product formation, and lysis. Supplying an importable osmoprotectant can be energetically cheaper than forcing de novo ectoine synthesis; c-di-AMP and osmolyte transport are possible engineering levers, but interventions will be host-specific. (bremer2019responsesofmicroorganisms pages 5-6, foster2024bacterialcellvolume pages 13-16)
4. **Food preservation and pathogen control.** NaCl preservation exploits osmotic dehydration, but compatible-solute import and Na⁺/H⁺ antiport can generate tolerance. Mechanosensitive channels also support transitions from salty foods or hosts into dilute environments. The authoritative review explicitly identifies food safety, pathogen virulence, and industrial cell factories as major application areas. (bremer2019responsesofmicroorganisms pages 13-14, wood1999osmosensingbybacteria pages 17-18)
5. **Trait prediction from genomes.** K⁺ transport, compatible-solute pathways, Na⁺ antiporters, and mechanosensitive channels are mechanistically relevant features, but their presence alone cannot predict the optimum because expression, regulation, medium composition, taxonomic background, and proteome adaptation matter.

## Recommended TraitMech graph design

The current 11-node/9-edge summary should be expanded conservatively into two connected layers:

- **Core low-optimum mechanism:** low external NaCl → minimal osmotic compensation burden → maintained hydration/turgor and lower energetic/ionic cost → maximal growth.
- **Conditional high-salt response:** NaCl upshift → water efflux/cell shrinkage → K⁺/glutamate phase → compatible-solute phase and Na⁺ export → partial restoration of growth.
- **Return-to-low-salt safety branch:** hypoosmotic downshift → MscL/MscS opening → osmolyte release → reduced lysis.
- **Taxon-specific extensions:** c-di-AMP regulation in organisms that encode it; kamA/ablB/N(ε)-acetyl-β-L-lysine in *Ca. Methanoperedens* and validated relatives.

The terminal phenotype edge should be phrased cautiously: **“low external NaCl permits maximal measured growth under assay conditions”**, not “absence of osmoadaptation causes non-halophily.” Most adaptive modules explain performance away from the optimum and do not, individually, determine where the growth optimum lies.

## Warnings: claims not yet suitable for general TraitMech curation

- Do **not** encode “halotolerant,” “non-halophile,” and “NaCl optimum ≤1%” as exact synonyms without qualifier logic.
- Do **not** infer an optimum from one growth point, a habitat salinity, MAG abundance, gene presence, or a maximum tolerated concentration.
- Do **not** curate c-di-AMP as universal; many organisms do not use this messenger.
- Do **not** generalize *Ca. Methanoperedens* kamA/ablB, PHA, sialic-acid, or YnaI results to all low-optimum microbes.
- Do **not** treat phylogenomic enrichment or acidic proteomes as causal edges to METPO:1000465; these are evolutionary associations.
- Do **not** equate NaCl stress with generic osmotic stress where ion-specific effects were not separated experimentally.
- Aquaporin AqpZ should not be a core node: the review states that its physiological role in osmotic shifts is unclear and its absence from many bacteria argues against a universal central role. (bremer2019responsesofmicroorganisms pages 3-5)
- The N(ε)-acetyl-β-L-lysine pathway is strongly supported by multi-omics, but a kamA/ablB knockout-and-rescue test would be preferable before encoding “required for salt acclimation.”
- PHA consumption and altered nonulosonic acids should remain **associated_with salt stress**, not **causes salt tolerance**, pending perturbation evidence. (medrano2024osmoregulationinfreshwater pages 9-10, medrano2024osmoregulationinfreshwater pages 13-15)

## DOI-first bibliography

1. Foster AJ, van den Noort M, Poolman B. **Bacterial cell volume regulation and the importance of cyclic di-AMP.** *Microbiology and Molecular Biology Reviews* 88(2). Published **10 June 2024**. DOI: [10.1128/mmbr.00181-23](https://doi.org/10.1128/mmbr.00181-23). (foster2024bacterialcellvolume pages 1-2)
2. Echeveste Medrano MJ, et al. **Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress.** *The ISME Journal* 18(1), wrae137. Advance publication **20 July 2024**; received 11 March and accepted 18 July 2024. DOI: [10.1093/ismejo/wrae137](https://doi.org/10.1093/ismejo/wrae137). (medrano2024osmoregulationinfreshwater pages 1-2)
3. Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y. **Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/“salt-out” osmoregulation strategy.** *Frontiers in Microbiomes* 2. Published **January 2024**. DOI: [10.3389/frmbi.2023.1329925](https://doi.org/10.3389/frmbi.2023.1329925). (ionescu2024extremefluctuationsin pages 4-6)
4. Jurdzinski KT, et al. **Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.** *Science Advances* 9, eadg2059. Published **26 May 2023**; corrected 24 May 2024. DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059). (jurdzinski2023largescalephylogenomicsof pages 1-2)
5. Bremer E, Krämer R. **Responses of Microorganisms to Osmotic Stress.** *Annual Review of Microbiology* 73:313–334. Published **September 2019**; review online 10 June 2019. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). (bremer2019responsesofmicroorganisms pages 1-2)
6. Wood JM. **Osmosensing by Bacteria: Signals and Membrane-Based Sensors.** *Microbiology and Molecular Biology Reviews* 63:230–262. Published **March 1999**. DOI: [10.1128/mmbr.63.1.230-262.1999](https://doi.org/10.1128/mmbr.63.1.230-262.1999). (wood1999osmosensingbybacteria pages 17-18, wood1999osmosensingbybacteria pages 14-15)

## Curation conclusion

**METPO:1000465** is best represented as a low-NaCl growth optimum produced by the balance between basal cellular performance and the increasing costs of hyperosmotic compensation. The strongest broadly curatable chain is: **NaCl upshift → water loss/cell shrinkage → reduced turgor and increased crowding → K⁺/glutamate accumulation → compatible-solute accumulation and Na⁺ export → partial restoration of hydration and growth**. The complementary downshift chain is **low-osmolality transition → Msc activation → osmolyte release → protection from lysis**. c-di-AMP regulation and the kamA/ablB osmolyte pathway are valuable mechanistic extensions, but they require explicit taxonomic qualifiers and should not define the trait universally.

References

1. (medrano2024osmoregulationinfreshwater pages 6-7): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

2. (medrano2024osmoregulationinfreshwater pages 1-2): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

3. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

4. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

5. (bremer2019responsesofmicroorganisms pages 5-6): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

6. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 12-13): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

8. (medrano2024osmoregulationinfreshwater pages 3-4): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

9. (medrano2024osmoregulationinfreshwater pages 10-13): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

10. (bremer2019responsesofmicroorganisms pages 1-2): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

11. (wood1999osmosensingbybacteria pages 14-15): Janet M. Wood. Osmosensing by bacteria: signals and membrane-based sensors. Microbiology and Molecular Biology Reviews, 63:230-262, Mar 1999. URL: https://doi.org/10.1128/mmbr.63.1.230-262.1999, doi:10.1128/mmbr.63.1.230-262.1999. This article has 850 citations and is from a domain leading peer-reviewed journal.

12. (bremer2019responsesofmicroorganisms pages 11-13): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

13. (wood1999osmosensingbybacteria pages 17-18): Janet M. Wood. Osmosensing by bacteria: signals and membrane-based sensors. Microbiology and Molecular Biology Reviews, 63:230-262, Mar 1999. URL: https://doi.org/10.1128/mmbr.63.1.230-262.1999, doi:10.1128/mmbr.63.1.230-262.1999. This article has 850 citations and is from a domain leading peer-reviewed journal.

14. (bremer2019responsesofmicroorganisms pages 10-11): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

15. (medrano2024osmoregulationinfreshwater pages 9-10): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

16. (bremer2019responsesofmicroorganisms pages 13-14): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

17. (medrano2024osmoregulationinfreshwater pages 13-15): Maider J Echeveste Medrano, Andy O Leu, Martin Pabst, Yuemei Lin, Simon J McIlroy, Gene W Tyson, Jitske van Ede, Irene Sánchez-Andrea, Mike S M Jetten, Robert Jansen, and Cornelia U Welte. Osmoregulation in freshwater anaerobic methane-oxidizing archaea under salt stress. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae137, doi:10.1093/ismejo/wrae137. This article has 20 citations.

18. (foster2024bacterialcellvolume pages 31-33): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

19. (jurdzinski2023largescalephylogenomicsof pages 1-2): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

20. (jurdzinski2023largescalephylogenomicsof pages 10-11): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

21. (jurdzinski2023largescalephylogenomicsof pages 11-12): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

22. (ionescu2024extremefluctuationsin pages 4-6): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

23. (jurdzinski2023largescalephylogenomicsof pages 1-1): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

24. (foster2024bacterialcellvolume pages 13-16): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

25. (foster2024bacterialcellvolume pages 1-2): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.