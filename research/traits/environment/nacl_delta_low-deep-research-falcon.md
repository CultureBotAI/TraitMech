---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:34:11.374356'
end_time: '2026-08-04T01:41:18.000137'
duration_seconds: 426.63
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta low
  trait_identifier: METPO:1000479
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl delta phenotype with a narrow growth-supporting NaCl breadth
    of at most approximately 1% (w/v), characteristic of stenohaline organisms.
  parent_traits: METPO:1000335
  synonyms: Nad_<=1
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted
    with euryhaline organisms.)'
  causal_graph_summary: 'nacl_delta_low_stenohaline: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000479
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a narrow growth-supporting NaCl breadth of at most approximately 1% (w/v), characteristic of stenohaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted with euryhaline organisms.)
- **Existing causal graph summary:** nacl_delta_low_stenohaline: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_low.yaml`.

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
- **Trait label:** NaCl delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000479
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a narrow growth-supporting NaCl breadth of at most approximately 1% (w/v), characteristic of stenohaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted with euryhaline organisms.)
- **Existing causal graph summary:** nacl_delta_low_stenohaline: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_low.yaml`.

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


# Curation report: NaCl delta low

## Executive summary

**Trait:** “NaCl delta low”  
**Trait CURIE:** **METPO:1000479**  
**Parent:** **METPO:1000335**  
**Synonym:** `Nad_<=1`

This trait should represent an **assay-derived narrow breadth of NaCl concentrations supporting microbial growth**, conventionally no more than approximately **1% (w/v) NaCl** between the lower and upper growth boundaries. It is therefore a *breadth* phenotype—not the organism’s NaCl optimum, minimum, maximum, or requirement. “Stenohaline” is the ecological interpretation of this narrow breadth.

The strongest mechanistic model is that NaCl changes disturb water balance and turgor; organisms normally compensate first with K⁺ uptake and then with compatible-solute synthesis or import. Weak, absent, poorly regulated, or environmentally substrate-dependent compensation can restrict the growth window. However, direct evidence that any single gene *causes* **METPO:1000479** is scarce. Most available studies measure tolerance at one or several salt concentrations rather than a complete growth-supporting interval. Consequently, the initial TraitMech graph should emphasize proximal osmoadaptation mechanisms and retain explicit uncertainty on edges connecting those mechanisms to the final narrow-breadth phenotype.

## 1. Trait scope and boundary cases

### Recommended interpretation

A positive annotation requires growth measurements across enough NaCl concentrations to identify both boundaries of the supported-growth interval. The relevant quantity is:

> **NaCl delta = upper growth-supporting NaCl boundary − lower growth-supporting NaCl boundary**

The phenotype is **METPO:1000479** when that interval is at most approximately 1% NaCl (w/v), subject to the assay’s resolution. The threshold is about 0.171 M NaCl if converted using 58.44 g mol⁻¹, but conversion should not imply greater precision than the original assay.

### Distinguish from nearby concepts

- **Low maximum NaCl tolerance:** an organism may have a low upper limit but a broad interval below it.
- **High minimum or obligate NaCl requirement:** a halophile may fail below its minimum yet tolerate a broad high-salt interval.
- **NaCl optimum:** a narrow optimum does not establish a narrow growth interval.
- **Salt sensitivity at one dose:** inhibition at one NaCl concentration does not locate both boundaries.
- **Osmolarity tolerance:** NaCl has ionic as well as osmotic effects; sucrose or sorbitol assays are not automatically equivalent.
- **Field stenohalinity:** abundance restricted to one estuarine salinity category is an ecological proxy, not the same measurement as a ≤1% laboratory growth breadth.
- **Acclimation versus constitutive breadth:** inoculum history, compatible solutes in the medium, growth phase, and exposure rate can alter apparent boundaries.

Wu et al. defined organisms thriving within a narrow salinity range as stenohaline and euryhaline organisms as those adapting to wide fluctuations. Their operational MAG criterion was ecological: average abundance in one salinity category had to exceed both other categories by an order of magnitude. This should not be substituted for the METPO assay threshold without a mapping rule (wu2024metagenomicinsightsinto pages 1-2).

A useful physiological comparator is *Spiribacter salinus* M19-40: no growth was reported below 0.4 M NaCl, maximal growth at 0.8 M, and impaired growth at 1.0–2.0 M. That study calls its useful range narrow, but its total reported tolerated interval is much wider than 1% w/v; it is thus mechanistically informative but not necessarily a literal positive example of **METPO:1000479** (leon2018compatiblesolutesynthesis pages 4-5).

## 2. Candidate nodes grouped by type

### Trait and assay nodes

| Candidate node | Grounding | Curation note |
|---|---|---|
| NaCl delta low | **METPO:1000479** | Use verbatim as target node. |
| Parent trait | **METPO:1000335** | Preserve asserted parent relation. |
| Lower NaCl growth boundary | Label only | Assay-derived endpoint. |
| Upper NaCl growth boundary | Label only | Assay-derived endpoint. |
| Growth-supporting NaCl breadth | Label only | Calculated difference between endpoints. |
| Stenohaline ecological niche | Label only | Keep separate from the assay phenotype unless METPO explicitly equates them. |

### Environmental and experimental factors

- Extracellular NaCl concentration.
- Hyperosmotic upshift and hypoosmotic downshift.
- Medium osmolarity/osmolality.
- External compatible-solute availability.
- Exposure rate, acclimation time, temperature, pH, medium composition, and inoculum history.
- Stable versus fluctuating salinity habitat.

In *C. difficile*, 100–200 mM added NaCl had little effect, whereas 400 mM severely restricted growth; the tested media ranged from 244 to 1,023 mOsm kg⁻¹. This demonstrates strong assay-context dependence but does not by itself establish the ≤1% breadth trait (michel2022cellularadaptationof pages 2-3).

### Chemicals and metabolites

- Sodium chloride; Na⁺; Cl⁻; K⁺.
- Water and cytoplasmic osmolyte pool.
- Compatible solutes: ectoine, glycine betaine, proline, trehalose, carnitine, arsenobetaine, γ-butyrobetaine, crotonobetaine, homobetaine, and dimethylsulfoniopropionate.
- Cyclic di-AMP.
- Glutamate as a precursor for proline and a component of proteome-level salinity adaptation.

**Grounding policy:** CHEBI identifiers should be added only after direct registry verification. The retrieved literature supports the labels, but this report deliberately does not guess CURIEs.

### Transporters, proteins, and gene modules

- Trk/Ktr-type K⁺ uptake systems; TrkG and TrkH candidates.
- KdpFABC/KdpDE high-affinity K⁺ uptake and regulation.
- KefC-type K⁺ efflux.
- Mrp-type Na⁺ extrusion complex.
- OpuF-type compatible-solute ABC transporter; strain-specific OpuFB substrate-binding/transmembrane subunit.
- OpuA/OpuC, BetP, GbuABC, and OpuD compatible-solute transport systems.
- Ectoine-biosynthetic EctA/EctB/EctC module.
- Trehalose-biosynthetic OtsA/OtsB module.
- CdaA diadenylate cyclase, GdpP-type phosphodiesterase, and c-di-AMP-responsive regulators such as BusR.
- Mechanosensitive channels MscL/MscS.
- GlmM, a regulator of CdaA in several c-di-AMP-using Gram-positive bacteria.

Exact UniProt, KEGG, EC, Rhea, or MetaCyc identifiers should be resolved against the particular strain. Orthologous names are not sufficient to assume identical substrate specificity.

### Processes and cellular states

- Osmotic water efflux and reduced cell volume/turgor.
- Primary K⁺ accumulation after osmotic upshift.
- Secondary compatible-solute accumulation.
- Osmolyte release after hypoosmotic downshift.
- Cell-volume restoration and sustained growth.
- Protein stabilization by compatible solutes.
- Central-energy-metabolism suppression under salt stress.
- Long-term proteome and gene-content adaptation to salinity.

## 3. Candidate causal edges

The table below separates experimentally supported edges from review-level mechanisms, inference, and metagenomic association.

| Subject | Predicate | Object | Evidence class | Taxon/scope | Curation status |
|---|---|---|---|---|---|
| NaCl increase | causes | osmotic upshift / water efflux / reduced turgor | review-supported + direct growth context (michel2022cellularadaptationof pages 2-3) | broad bacteria; experimentally contextualized in *Clostridioides difficile* | Curate as generic process edge; trait-specific effect is context-dependent |
| Osmotic upshift | triggers | K+ uptake / increased cytoplasmic potassium | review-supported (michel2022cellularadaptationof pages 2-3, foster2024bacterialcellvolume pages 10-12) | broad bacteria | Curate only as generic osmoadaptation edge, not as specific stenohaline determinant |
| Compatible-solute accumulation or import | restores | cell volume and growth under high NaCl | direct + review-supported (leon2018compatiblesolutesynthesis pages 11-12, michel2022cellularadaptationof pages 9-9, michel2022cellularadaptationof pages 10-11, foster2024bacterialcellvolume pages 10-12) | direct in *Spiribacter salinus* and *C. difficile*; broad bacterial principle | Curate, with taxon-qualified evidence notes |
| OpuF transporter | imports | compatible solutes | direct (michel2022cellularadaptationof pages 13-13, michel2022cellularadaptationof pages 9-9, michel2022cellularadaptationof pages 4-5) | *C. difficile* strain 630Δerm / OpuF-type ABC transporter | Curate as taxon-specific edge |
| Cyclic di-AMP | inhibits | Opu transporter activity / glycine-betaine uptake | review-supported, mechanistically strong (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 1-2) | mainly Firmicutes and related c-di-AMP-using bacteria | Curate as generic regulatory edge with scope restriction |
| Ectoine biosynthesis / ectoine accumulation | supports | high-salinity growth | direct in halophile physiology (leon2018compatiblesolutesynthesis pages 10-11, leon2018compatiblesolutesynthesis pages 11-12) | *Spiribacter salinus*; broader halophiles by review/inference | Curate as taxon-qualified edge; broader generalization uncertain |
| Hypoosmotic downshift | activates | mechanosensitive osmolyte release | review-supported (leon2018compatiblesolutesynthesis pages 1-2, foster2024bacterialcellvolume pages 1-2) | broad bacteria | Curate cautiously as generic osmotic-recovery edge |
| Limited compatible-solute capacity | contributes to | narrow NaCl growth breadth | inferred from direct phenotype plus review (michel2022cellularadaptationof pages 1-1, michel2022cellularadaptationof pages 2-3, foster2024bacterialcellvolume pages 10-12) | strongest in *C. difficile* and freshwater/nonhalophilic comparisons | Mark uncertain/inferred; do not overgeneralize |
| Trk-type K+ transporter abundance | associated with | high-salinity stenohaline MAGs | associative metagenomic / machine-learning feature (wu2024metagenomicinsightsinto pages 1-2) | estuarine bacterial and archaeal MAGs | Do not curate as causal without stronger intervention evidence |
| Proteome reorganization / gene-content shifts | constrains transition into different salinity biomes | stenohaline/euryhaline niche separation | associative evolutionary comparative evidence (jurdzinski2023largescalephylogenomicsof pages 1-2, jurdzinski2023largescalephylogenomicsof pages 11-12, jurdzinski2023largescalephylogenomicsof pages 1-1) | aquatic bacterial lineages across 11,248 MAGs | Keep as background only; not TraitMech-ready causal edge |


*Table: This table summarizes candidate subject-predicate-object edges relevant to the NaCl delta low phenotype, separating direct experimental evidence from review-supported, inferred, and associative claims. It is useful for deciding which edges are strong enough for TraitMech curation and which should remain provisional.*

### Evidence details and supporting snippets

| Proposed triple | Reference and supporting snippet | Interpretation |
|---|---|---|
| **Elevated NaCl —inhibits→ microbial growth** | *C. difficile*: “100–200 mM NaCl” had little effect, whereas “400 mM NaCl severely restricts growth” (michel2022cellularadaptationof pages 2-3). | **Direct, taxon- and assay-specific.** Curate as a proximal phenotype edge, not proof of the final breadth class. |
| **Elevated NaCl —reduces→ central energy generation** | At 350 mM NaCl, growth was significantly reduced and central energy pathways, including Stickland fermentation, showed a major reduction (michel2022cellularadaptationof pages 1-1). | **Direct, taxon-specific.** Useful intermediate state for *C. difficile*. |
| **Osmotic upshift —triggers→ K⁺ accumulation** | Current review synthesis: during osmotic upshift cells first accumulate K⁺, then replace part of it with compatible solutes (michel2022cellularadaptationof pages 2-3, foster2024bacterialcellvolume pages 10-12). | **Mechanistically established general response**, but not specific to stenohalinity. |
| **Compatible-solute import/accumulation —promotes→ high-NaCl growth** | In *S. salinus*, 1 mM glycine betaine or arsenobetaine strongly protected growth at 1.6 M NaCl, and glycine betaine protected across 0.8–2.0 M NaCl (leon2018compatiblesolutesynthesis pages 11-12, leon2018compatiblesolutesynthesis pages 12-14). | **Direct supplementation evidence.** Strong edge, but taxon-qualified. |
| **OpuF —imports→ compatible solutes** | The *C. difficile* study experimentally verified the bioinformatically identified OpuF system; compatible-solute protection depended on it (michel2022cellularadaptationof pages 13-13, michel2022cellularadaptationof pages 9-9). | **Direct genetic/physiological evidence.** Appropriate strain-qualified edge. |
| **OpuF-dependent carnitine import —restores→ salt-stressed metabolism/growth** | Carnitine nearly restored the wild-type metabolite profile but did not rescue the `opuFB` mutant; with carnitine, OD600 was 0.77 for wild type versus 0.26 for the mutant (michel2022cellularadaptationof pages 9-9, michel2022cellularadaptationof pages 10-11). | **Strong direct intervention plus mutant evidence.** One of the best graph-ready edges. |
| **Salt stress —increases→ intracellular proline** | Long-term exposure to 400 mM NaCl produced a 5.1-fold increase in intracellular proline in *C. difficile* (michel2022cellularadaptationof pages 10-11). | **Direct response**, but whether proline is cause or consequence requires careful wording. |
| **NaCl concentration —increases→ ectoine accumulation** | *S. salinus* ectoine rose from about 80 μM at 0.6 M NaCl to 170 μM at 0.8 M NaCl; further salt increase did not yield a proportional rise (leon2018compatiblesolutesynthesis pages 10-11). | **Direct dose response**, but non-monotonic at higher stress. Curate the bounded response, not an unlimited positive relation. |
| **Glycine-betaine import —suppresses→ endogenous ectoine synthesis** | Imported glycine betaine remained unmodified and reduced intracellular ectoine pools as much as 17-fold across tested salinities (leon2018compatiblesolutesynthesis pages 11-12). | **Direct metabolic substitution edge** in *S. salinus*. |
| **Cyclic di-AMP —inhibits→ Opu-mediated compatible-solute uptake** | The 2024 MMBR review reports direct binding to CBS domains in OpuA/OpuC systems and negative regulation of transport; c-di-AMP-bound BusR inhibits `opuA` transcription and decreases glycine-betaine uptake (foster2024bacterialcellvolume pages 10-12). | **Mechanistically strong but lineage-limited.** Restrict to c-di-AMP-producing taxa and the demonstrated transporter families. |
| **Compatible-solute capacity limitation —contributes to→ narrow salt tolerance** | *C. difficile* showed no obvious compatible-solute synthesis during its initial 24 h, alongside limited high-salinity tolerance; supplementation and OpuF import restored growth (michel2022cellularadaptationof pages 1-1, michel2022cellularadaptationof pages 9-9). | **Plausible synthesis, not a universal causal law.** Mark uncertain and taxon-specific. |
| **Trk transporter abundance —associates with→ high-salinity specialization** | Among 12,162 COGs, Wu et al. selected 40 features; eight concerned osmoregulation, and COG0168, a Trk-type K⁺ transporter, ranked first and increased with salinity (wu2024metagenomicinsightsinto pages 1-2). | **Association only.** Do not use a causal predicate. |
| **Proteome/gene-content reorganization —constrains→ cross-biome transition** | Analysis of 11,248 bacterial MAGs found systematic proteome changes and convergent gene gains/losses accompanying rare salinity-biome transitions (jurdzinski2023largescalephylogenomicsof pages 1-1, jurdzinski2023largescalephylogenomicsof pages 1-2). | **Evolutionary comparative evidence**, not an intervention. Retain as background or uncertain high-level edge. |

## 4. Recent developments, statistics, and expert interpretation

### 2024: natural-gradient metagenomics

Wu et al. reconstructed **127 bacterial and archaeal MAGs** from a short-residence-time subtropical estuary. From **12,162 COGs**, Boruta feature selection identified **40 important features**, including **eight osmoregulation-related COGs**: four salt-in, three salt-out, and one associated with water-channel regulation. COG0168, annotated as a Trk-type K⁺ transporter, ranked highest. This supports K⁺ transport as a priority node, but the machine-learning result remains predictive/associative rather than causal (wu2024metagenomicinsightsinto pages 1-2).

### 2024: cyclic di-AMP as a cell-volume master regulator

Foster, van den Noort, and Poolman synthesize evidence that c-di-AMP regulates K⁺ and compatible-solute transport in Firmicutes, Actinobacteria, Cyanobacteria, and other producing lineages. Compatible solutes can accumulate to molar concentrations with limited physiological disruption; in *Bacillus subtilis*, proline reportedly rises from about **20 mM to 500 mM** under osmotic stress. Glycine-betaine uptake improved *Lactococcus lactis* growth at **0.4 M NaCl**. The review also emphasizes that both c-di-AMP deficiency and overproduction can impair viability, so a simple “more c-di-AMP means greater salt tolerance” edge would be incorrect (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 10-12).

### 2023: salinity barriers at phylogenomic scale

Jurdzinski et al. analyzed **11,248 bacterial MAGs**: 7,643 freshwater, 2,240 brackish, and 1,365 marine. Clustering produced **3,561 species-level genome clusters**, of which **3,547** occurred in only one biome; none spanned all three. Only 14 clusters crossed a pair of biomes. These statistics strongly support generally narrow realized salinity niches among aquatic bacterial species, although realized biogeography is not equivalent to an experimentally measured NaCl delta (jurdzinski2023largescalephylogenomicsof pages 1-1, jurdzinski2023largescalephylogenomicsof pages 1-2).

The authors’ phylogenomic framing is especially relevant to curation: convergently gained or lost functions are more likely adaptive than raw prevalence differences, which may “hitchhike” with taxonomic composition. Nevertheless, they warn that ortholog annotation and causal interpretation remain difficult (jurdzinski2023largescalephylogenomicsof pages 11-12, jurdzinski2023largescalephylogenomicsof pages 1-2).

## 5. Current applications and real-world relevance

1. **Environmental monitoring and estuary modeling.** Stenohaline taxa can act as indicators of salinity zones or salinity disturbance, while euryhaline taxa may track mixing and fluctuating conditions. The Pearl River Estuary study provides an implementation based on abundance categories and MAG features (wu2024metagenomicinsightsinto pages 1-2).
2. **Predicting community turnover under climate and hydrological change.** The rarity of freshwater–marine species overlap implies that altered runoff, drought, seawater intrusion, or desalination discharge can reorganize communities rather than merely shift the abundance of universally tolerant species (jurdzinski2023largescalephylogenomicsof pages 1-1, jurdzinski2023largescalephylogenomicsof pages 1-2).
3. **Industrial fermentation.** Compatible-solute supplementation or engineering of uptake/biosynthesis can extend high-osmolality growth, but the intervention may change the measured trait itself. The *S. salinus* and *C. difficile* supplementation studies demonstrate strong medium dependence (leon2018compatiblesolutesynthesis pages 11-12, michel2022cellularadaptationof pages 9-9).
4. **Food and host-associated microbiology.** Opu-dependent osmoprotection can affect persistence in salt-rich foods or host niches. In *C. difficile*, physiologically relevant intestinal NaCl concentrations reach approximately 350 mM, making transporter-mediated rescue biologically meaningful (michel2022cellularadaptationof pages 1-1, michel2022cellularadaptationof pages 2-2).
5. **Trait prediction from genomes.** Trk, compatible-solute, c-di-AMP, and mechanosensitive-channel genes are useful candidate features, but current evidence does not justify deterministic prediction of **METPO:1000479** from gene presence alone.

## 6. Recommended initial graph architecture

A conservative graph could contain the following mechanistic chain:

1. **extracellular NaCl change** → causes → **osmotic imbalance**
2. **osmotic imbalance** → causes → **water flux / altered turgor and cell volume**
3. **hyperosmotic upshift** → activates → **K⁺ uptake**
4. **K⁺ accumulation** → partially restores → **cytoplasmic osmotic balance**
5. **hyperosmotic upshift** → induces/activates → **compatible-solute synthesis or uptake**
6. **compatible-solute accumulation** → promotes → **cell-volume restoration and sustained high-NaCl growth**
7. **cyclic di-AMP** → negatively regulates → **selected K⁺ and compatible-solute transporters**
8. **hypoosmotic downshift** → activates → **mechanosensitive osmolyte release**
9. **insufficient or poorly regulated osmoadaptation capacity** → may narrow → **growth-supporting NaCl breadth**
10. **narrow growth-supporting NaCl breadth ≤ approximately 1% w/v** → realizes → **METPO:1000479**

Edges 1–8 are general osmoadaptation mechanisms. Edge 9 is the critical trait-linking inference and should remain explicitly uncertain until a study measures a complete NaCl growth window before and after a genetic or chemical intervention.

## 7. Warnings: claims not yet ready for TraitMech

- **Do not curate COG0168/Trk as causing stenohalinity.** Its 2024 support is feature selection and abundance correlation, not gene perturbation (wu2024metagenomicinsightsinto pages 1-2).
- **Do not equate ecological restriction with the ≤1% laboratory threshold.** The abundance-based definition is useful but operationally different.
- **Do not assert that compatible-solute capacity always produces euryhalinity.** Solute availability, energetic costs, membrane/cell-wall properties, proteome chemistry, and ion toxicity also matter.
- **Do not generalize c-di-AMP regulation to all microbes.** It is absent from some lineages, and its targets differ. Both too little and too much can be harmful (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 10-12).
- **Do not assign a causal role to gene presence alone.** Transporters can differ in substrate specificity, regulation, expression, and activity.
- **Do not use *S. salinus* as an unqualified METPO:1000479 positive instance.** Its reported molar range exceeds the stated 1% breadth threshold even though authors describe a narrow ecophysiological range (leon2018compatiblesolutesynthesis pages 4-5).
- **Do not treat NaCl and nonionic osmolytes as interchangeable assay variables.** Separate ionic toxicity from water-activity effects.
- **Do not curate proline accumulation as protective from response data alone.** In *C. difficile*, the 5.1-fold increase is direct, but its causal contribution requires a targeted intervention (michel2022cellularadaptationof pages 10-11).
- **Do not assign exact ontology accessions without registry verification.** Label-only nodes are preferable to invented CHEBI, GO, UniProt, KEGG, EC, Rhea, or MetaCyc identifiers.

## DOI-first bibliography

1. **Wu Z, Li M, Qu L, Zhang C, Xie W.** “Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.” *Microbiome* 12:115. **Published June 2024.** DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w) (wu2024metagenomicinsightsinto pages 1-2).
2. **Foster AJ, van den Noort M, Poolman B.** “Bacterial cell volume regulation and the importance of cyclic di-AMP.” *Microbiology and Molecular Biology Reviews* 88(2). **Published 10 June 2024.** DOI: [10.1128/mmbr.00181-23](https://doi.org/10.1128/mmbr.00181-23) (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 10-12).
3. **Jurdzinski KT et al.** “Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.” *Science Advances* 9, eadg2059. **Published 26 May 2023; corrected 24 May 2024.** DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059) (jurdzinski2023largescalephylogenomicsof pages 1-1, jurdzinski2023largescalephylogenomicsof pages 1-2).
4. **Michel A-M et al.** “Cellular adaptation of *Clostridioides difficile* to high salinity encompasses a compatible solute-responsive change in cell morphology.” *Environmental Microbiology* 24:1499–1517. **Published February 2022.** DOI: [10.1111/1462-2920.15925](https://doi.org/10.1111/1462-2920.15925) (michel2022cellularadaptationof pages 1-1, michel2022cellularadaptationof pages 9-9, michel2022cellularadaptationof pages 10-11).
5. **León MJ et al.** “Compatible Solute Synthesis and Import by the Moderate Halophile *Spiribacter salinus*: Physiology and Genomics.” *Frontiers in Microbiology* 9:108. **Published February 2018.** DOI: [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108) (leon2018compatiblesolutesynthesis pages 11-12, leon2018compatiblesolutesynthesis pages 10-11).
6. **Gunde-Cimerman N, Plemenitaš A, Oren A.** “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews* 42:353–375. **Published May 2018.** DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). This is the supplied foundational evidence for the stenohaline/euryhaline contrast; its full text was not available in the present retrieval run, so no new edge here relies solely on an unverified quotation from it.

## Curation conclusion

The evidence supports a robust **generic osmoadaptation subgraph**, particularly NaCl/osmotic upshift → K⁺ accumulation → compatible-solute accumulation → restored volume and growth, with c-di-AMP as a lineage-restricted regulator. OpuF-dependent compatible-solute rescue in *C. difficile* and betaine-mediated rescue in *S. salinus* provide the strongest intervention-backed edges. The final connection from failed or limited osmoadaptation to **METPO:1000479**, however, remains an inference because the available genetic studies generally do not measure both NaCl growth boundaries at sufficient resolution. The YAML should therefore curate proximal mechanisms confidently, retain taxon qualifiers, and mark the trait-determining edge uncertain pending full-range mutant or complementation experiments.

References

1. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

2. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

3. (michel2022cellularadaptationof pages 2-3): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

4. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

5. (leon2018compatiblesolutesynthesis pages 11-12): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

6. (michel2022cellularadaptationof pages 9-9): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (michel2022cellularadaptationof pages 10-11): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

8. (michel2022cellularadaptationof pages 13-13): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (michel2022cellularadaptationof pages 4-5): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (foster2024bacterialcellvolume pages 1-2): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 29 citations and is from a domain leading peer-reviewed journal.

11. (leon2018compatiblesolutesynthesis pages 10-11): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

12. (leon2018compatiblesolutesynthesis pages 1-2): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

13. (michel2022cellularadaptationof pages 1-1): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (jurdzinski2023largescalephylogenomicsof pages 1-2): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

15. (jurdzinski2023largescalephylogenomicsof pages 11-12): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

16. (jurdzinski2023largescalephylogenomicsof pages 1-1): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

17. (leon2018compatiblesolutesynthesis pages 12-14): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

18. (michel2022cellularadaptationof pages 2-2): Annika‐Marisa Michel, José Manuel Borrero‐de Acuña, Gabriella Molinari, Can Murat Ünal, Sabine Will, Elisabeth Derksen, Stefan Barthels, Wiebke Bartram, Michel Schrader, Manfred Rohde, Hao Zhang, Tamara Hoffmann, Meina Neumann‐Schaal, Erhard Bremer, and Dieter Jahn. Cellular adaptation of <i>clostridioides difficile</i> to high salinity encompasses a compatible solute‐responsive change in cell morphology. Environmental Microbiology, 24:1499-1517, Feb 2022. URL: https://doi.org/10.1111/1462-2920.15925, doi:10.1111/1462-2920.15925. This article has 13 citations and is from a domain leading peer-reviewed journal.