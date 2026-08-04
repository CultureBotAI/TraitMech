---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:42:20.943072'
end_time: '2026-08-04T01:50:40.879924'
duration_seconds: 499.94
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum mid1
  trait_identifier: METPO:1000466
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration approximately
    between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Slight halophile, NaO_1_to_3
  evidence_summary: "DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review\
    \ supports the 1\u20133% NaCl optimum range as the slight-halophile category.)"
  causal_graph_summary: 'nacl_optimum_mid1_slight_halophile: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000466
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Slight halophile, NaO_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl optimum range as the slight-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid1_slight_halophile: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid1.yaml`.

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
- **Trait label:** NaCl optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000466
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 1 and 3% (w/v), corresponding to slight-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Slight halophile, NaO_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl optimum range as the slight-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid1_slight_halophile: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid1.yaml`.

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


# Curation report: NaCl optimum mid1

## Executive assessment

**Trait:** NaCl optimum mid1  
**Identifier:** **METPO:1000466**  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** METPO:1000333  
**Proposed interpretation:** an assay-observed growth optimum at approximately **1–3% (w/v) NaCl**, equivalent to about **10–30 g L⁻¹** or **0.17–0.51 M NaCl**. It is best treated as a quantitative environmental-preference phenotype, not as a generic salt-resistance mechanism.

The most defensible small causal graph is:

> increased extracellular NaCl → hyperosmotic water loss/reduced hydration and turgor → osmoadaptive ion and compatible-solute responses → restored hydration/turgor and growth; conversely, hypoosmotic downshift → mechanosensitive-channel opening → rapid solute release and protection from lysis.

This framework is authoritative and broadly conserved, but it does **not by itself explain why a particular strain’s optimum lies specifically at 1–3% NaCl**. That narrower conclusion requires strain-level growth curves plus perturbation evidence under the same salinity range. The current literature is much stronger for generic osmoadaptation or moderate/extreme halophiles than for causal determination of a slight-halophile optimum.

## 1. Trait scope and boundaries

### 1.1 Included phenotype

METPO:1000466 should represent the NaCl concentration interval producing the best measured growth—ideally maximum specific growth rate, biomass yield, or another explicitly defined growth endpoint. The supplied interval overlaps a commonly used slight-halophile boundary of approximately 0.2–0.5 M NaCl. A recent growth study reported the same classification interval, although that source is a 2026 preprint and should be used only as supporting boundary evidence. (schiavo2026shouldescherichiacoli pages 1-5)

A useful operational curation rule is:

- **Positive assignment:** the measured optimum, or statistically indistinguishable optimal plateau, substantially overlaps 1–3% NaCl.
- **Preferred evidence:** at least three NaCl conditions bracketing the optimum, including a condition below 1% and one above 3%, with temperature, pH, medium, aeration, and growth metric reported.
- **Do not infer from:** isolation from saline habitat, presence of osmoadaptation genes, survival at 3% NaCl, or maximum tolerated salinity alone.

### 1.2 Boundary cases

1. **Halotolerant versus slight halophile.** “Halotolerant” often means growth is possible at elevated salt without an obligate salt requirement; “slight halophile” implies that low salt improves or optimizes growth. A strain growing equally well from 0–3% should be annotated as having a broad/flat optimum only if the assay supports that conclusion.
2. **Salt requirement versus optimum.** Failure at 0% NaCl supports a requirement but does not locate the optimum. Conversely, growth without added NaCl does not exclude an optimum within 1–3%.
3. **Moderate halophily.** Optima above roughly 3–5% enter classification-dependent slight/moderate boundary territory. The literature uses nonidentical cutoffs, so preserve the measured concentration rather than relying only on a verbal category.
4. **Extreme halophily.** Mechanisms measured at molar salt concentrations cannot be automatically transferred to METPO:1000466.
5. **NaCl versus total salinity/osmolality.** Seawater, mixed salts, sucrose, and polyethylene glycol impose different ionic and osmotic effects. The trait specifically concerns added or measured **NaCl**.
6. **Tolerance phenotypes.** Maximum tolerated NaCl, lag-time recovery, survival after salt shock, and biofilm persistence are related but distinct traits.

A 2026 *E. coli* MG1655 preprint illustrates the distinction: growth rate was reportedly highest over 0–0.5 M NaCl, at 0.81–0.94 h⁻¹. Because the optimum is broad and includes zero added NaCl, this is adjacent evidence for the interval but not a clean demonstration of salt dependence. (schiavo2026shouldescherichiacoli pages 5-8)

## 2. Current mechanistic understanding

Hyperosmotic exposure drives water out of bacterial cells, altering hydration, molecular crowding, turgor, and cellular integrity. Salt-out bacteria compensate mainly by accumulating compatible organic osmolytes while tightly controlling cytoplasmic K⁺ and Na⁺. Common osmolytes include glycine betaine, proline, ectoine/hydroxyectoine, trehalose, carnitine, and glucosylglycerol. During sudden hypoosmotic downshift, mechanosensitive channels rapidly release organic and inorganic solutes, preventing excessive swelling and rupture. This is the strongest general mechanistic backbone available for TraitMech. (bremer2019responsesofmicroorganisms pages 3-5)

Recent work also emphasizes that “salt-in” and “salt-out” are not always mutually exclusive. In 2024, *Natranaerobius thermophilus* was shown by transcript/protein measurements and intracellular metabolite and ion quantification to combine K⁺ retention with compatible-solute accumulation. However, it grows at approximately 3.3–3.9 M Na⁺ and is therefore an extreme-halophile model, not direct evidence for a 1–3% NaCl optimum. (xing2024thepolyextremophilenatranaerobius pages 14-17)

## 3. Candidate graph nodes

### 3.1 Trait and environmental nodes

- **NaCl optimum mid1:** METPO:1000466
- Extracellular NaCl concentration — **CHEBI:26710** for sodium chloride
- Hyperosmotic condition / increased external osmolality — label-level environmental node unless a verified project-standard CURIE is selected
- Hypoosmotic downshift — label-level experimental-event node
- Water availability/activity — label-level quantitative environmental node
- Medium composition, temperature, pH, aeration, carbon source, and growth-assay endpoint — experimental-context nodes

### 3.2 Chemicals and ions

- Sodium ion — **CHEBI:29101**
- Potassium ion — **CHEBI:29103**
- Chloride — **CHEBI:17996**
- Water — **CHEBI:15377**
- L-proline — **CHEBI:17203**
- L-glutamate — **CHEBI:29985**
- Glycine betaine — **CHEBI:17750**
- Trehalose — **CHEBI:27082**
- Ectoine — use a verified CHEBI record during implementation; retain label-only if the release used by TraitMech has not been checked
- Hydroxyectoine, carnitine, glucosylglycerol, and GABA — secondary candidate osmolytes; ground only after checking the ontology release

### 3.3 Processes and cellular properties

- Response to osmotic stress — **GO:0006970**
- Osmoregulation — **GO:0006971**
- Water efflux and reduced cytoplasmic hydration
- Turgor reduction and restoration
- Compatible-solute biosynthesis
- Compatible-solute uptake
- Potassium uptake/homeostasis
- Sodium extrusion / Na⁺–H⁺ antiport
- Mechanosensitive-channel opening
- Solute efflux following hypoosmotic shock
- Growth rate / biomass accumulation
- Cytoplasmic membrane — **GO:0005886** where applicable
- Cytoplasm — **GO:0005737**

### 3.4 Genes, proteins, and modules

**Ion homeostasis**

- **nhaA, nhaB:** Na⁺/H⁺ antiporters
- **kdpA, kdpB, kdpD, kdpE:** high-affinity K⁺ uptake and regulation
- **trkA, trkH, trkG:** K⁺ uptake/homeostasis
- **clcA, clcB:** chloride transport/channel candidates

**Compatible-solute uptake**

- **OpuA/OpuB-family systems**
- **ProU / proV-proW-proX:** ABC-type osmoprotectant uptake
- **BetT:** choline transporter
- **PutP:** Na⁺/proline symporter
- BCCT-family transporters

**Compatible-solute synthesis and metabolism**

- **betA, betB:** choline → glycine betaine pathway
- **ectA, ectB, ectC** and context-dependent **ectD:** ectoine/hydroxyectoine pathway
- **otsA, otsB:** trehalose synthesis
- **proC** and other proline-biosynthesis genes
- **gsmt, sdmt:** glycine methylation route to glycine betaine in selected taxa

**Hypoosmotic protection**

- **MscL, MscS**, and taxon-specific Msc-family channels

These gene names should be represented as taxon-specific gene/protein entities or orthologous families—not as universally interchangeable proteins. The *E. coli* source reports genomic conservation of nhaA/B, kdp/trk, otsAB, proVWX, and betABT, but gene presence alone is not causal evidence for the optimum. (schiavo2026shouldescherichiacoli pages 5-8)

## 4. Candidate causal edges

The following table separates generally curatable physiological edges from provisional, taxon-specific, or genomic-only claims.

| subject | predicate | object | evidence snippet (short exact or close quote) | DOI/date | evidence class and curation status |
|---|---|---|---|---|---|
| Increased external NaCl / external osmolality | causes | hyperosmotic stress with water efflux and reduced cellular hydration/turgor | “Both increases and decreases in the external osmolarity inevitably trigger water fluxes… thus impinging on the degree of cellular hydration… and magnitude of turgor” (bremer2019responsesofmicroorganisms pages 3-5) | 10.1146/annurev-micro-020518-115504; Sep 2019 | General review synthesis; high-confidence background edge; curate as broad mechanism, not trait-specific proof |
| Compatible-solute accumulation | maintains | physiological hydration/turgor across salinity changes | “physiological hydration and turgor are maintained through compatible solute accumulation rather than ion accumulation” (bremer2019responsesofmicroorganisms pages 3-5) | 10.1146/annurev-micro-020518-115504; Sep 2019 | General review synthesis; high-confidence background edge; curate as broad mechanism |
| Hypoosmotic downshift | activates | mechanosensitive channels (Msc) | “Mechanosensitive channels (Msc) rapidly expel organic and inorganic compounds during hypoosmotic downshifts” (bremer2019responsesofmicroorganisms pages 3-5) | 10.1146/annurev-micro-020518-115504; Sep 2019 | General review synthesis; high-confidence background edge; curate as broad mechanism |
| Mechanosensitive channels (Msc) | mediates release of | organic and inorganic solutes | “rapidly expel organic and inorganic compounds during hypoosmotic downshifts” (bremer2019responsesofmicroorganisms pages 3-5) | 10.1146/annurev-micro-020518-115504; Sep 2019 | General review synthesis; high-confidence background edge; curate as broad mechanism |
| Increased salinity in *Natranaerobius thermophilus* | increases expression of | gsmt/sdmt glycine betaine synthesis genes | “genes gsmt and sdmt (upregulated 1.56- to 3.36-fold at 3.5 M Na+)” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24; May 2024 | Direct experiment in extreme halophile; taxon/salinity-range specific; uncertain transfer to 1–3% optimum trait |
| Increased salinity in *Natranaerobius thermophilus* | increases expression/activity of | Opu/ProU/BetT/PutP compatible-solute uptake systems | “employs the glycine betaine ABC transporters (Opu and ProU families)… and Na+/proline symporter PutP” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24; May 2024 | Direct experiment in extreme halophile; taxon/salinity-range specific; uncertain transfer |
| Increased salinity in *Natranaerobius thermophilus* | increases intracellular accumulation of | glycine betaine, glutamate, and proline | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24; May 2024 | Direct experiment in extreme halophile; strong within taxon; uncertain for METPO:1000466 |
| Increased salinity in *Natranaerobius thermophilus* | increases intracellular accumulation of | K+ | “simultaneously accumulating compatible solutes and K+” and “upregulation of Na+/K+/H+ transporters facilitates the maintenance of intracellular K+ concentration” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24; May 2024 | Direct experiment in extreme halophile; strong within taxon; uncertain transfer |
| *Escherichia coli* MG1655 genome | encodes candidate for | Na+/H+ antiport (nhaA, nhaB) | “ion homeostasis (Na+/H+ antiporters nhaA, nhaB)” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Genomic presence only; candidate node/edge, not causal proof; preprint and outside preferred date |
| *Escherichia coli* MG1655 genome | encodes candidate for | K+ uptake systems (kdpA/B/D/E, trkA/H/G) | “K+ transporters kdpA, kdpB, kdpD, kdpE, trkA, trkH, trkG” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Genomic presence only; candidate node/edge, not causal proof; preprint and outside preferred date |
| *Escherichia coli* MG1655 genome | encodes candidate for | trehalose biosynthesis (otsA, otsB) | “trehalose genes otsA, otsB” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Genomic presence only; candidate node/edge, not causal proof; preprint and outside preferred date |
| *Escherichia coli* MG1655 genome | encodes candidate for | proline uptake/metabolism (proC, proV, proW, proX) | “proline genes proC, proV, proW, proX” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Genomic presence only; candidate node/edge, not causal proof; preprint and outside preferred date |
| *Escherichia coli* MG1655 genome | encodes candidate for | choline/glycine betaine pathway (betA, betB, betT) | “glycine betaine operon betA, betB, betT” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Genomic presence only; candidate node/edge, not causal proof; preprint and outside preferred date |
| 0.00–0.50 M NaCl in *Escherichia coli* MG1655 | associated with optimal growth | slight-halophile phenotype / NaCl optimum mid1-adjacent evidence | “optimal growth at 0.00–0.50 mol·L⁻¹ NaCl… Growth rate (µ) was highest at 0.00–0.50 mol·L⁻¹ (0.81–0.94 h⁻¹)” (schiavo2026shouldescherichiacoli pages 5-8) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Direct phenotype assay, but preprint and outside preferred date; useful boundary evidence, curate cautiously |
| Slight-halophile classification | has optimum range of | ~0.2–0.5 M NaCl | “slight halophiles grow optimally at 0.2–0.5 mol·L⁻¹ NaCl” (schiavo2026shouldescherichiacoli pages 1-5) | 10.21203/rs.3.rs-8882295/v1; Mar 2026 | Classification statement from preprint; boundary aid only, not mechanistic edge |


*Table: This table summarizes compact, curation-focused candidate causal edges for METPO:1000466, separating broad osmoadaptation mechanisms from taxon-specific or genomic-only claims. It is useful for deciding which edges are ready for TraitMech curation and which should remain provisional or uncertain.*

### Recommended minimal graph for immediate curation

The current 10-node/8-edge graph should preferentially retain only broad, directionally supported physiology unless it already contains strain-specific experimental evidence:

1. extracellular NaCl increase **causes** hyperosmotic stress;
2. hyperosmotic stress **causes** cellular water efflux;
3. cellular water efflux **reduces** cytoplasmic hydration/turgor;
4. hyperosmotic stress **induces** compatible-solute uptake or synthesis;
5. compatible-solute accumulation **increases/restores** cytoplasmic osmotic balance and hydration;
6. restored hydration/turgor **supports** microbial growth under low-moderate NaCl;
7. hypoosmotic downshift **activates** Msc-family channels;
8. Msc activation **causes** rapid osmolyte/ion release and reduces lysis risk.

Edges 1–5 and 7–8 have strong general support. Edge 6 is biologically well founded but should be labeled **general/inferred for this trait** until a slight-halophile perturbation study directly connects a specific module to growth at 1–3% NaCl. (bremer2019responsesofmicroorganisms pages 3-5)

## 5. Recent developments and quantitative evidence

### 5.1 Dual ion/organic-osmolyte strategy

The 2024 *N. thermophilus* multi-omics study found that increasing salinity elevated intracellular glycine betaine, glutamate, and proline and supported K⁺ retention. Glycine-betaine synthesis genes **gsmt/sdmt** increased approximately **1.56- to 3.36-fold at 3.5 M Na⁺**, while Opu, ProU, BetT, and PutP-family transport systems were implicated in solute uptake. This is direct, multi-layer evidence for the relevant molecular edges, but the extreme salinity makes transfer to METPO:1000466 uncertain. (xing2024thepolyextremophilenatranaerobius pages 14-17)

### 5.2 Genomic prediction versus causal validation

Recent comparative genomics frequently identifies compatible-solute pathways and ion transporters in saline isolates. Such findings are useful for choosing candidate nodes, but they establish **capacity**, not pathway activity, necessity, or the position of the growth optimum. The same caution applies to the *E. coli* report: nhaA/B, kdp/trk, otsAB, pro genes, and betABT are plausible modules, while ectABCD was absent, but none of those observations alone proves causation of the 1–3% phenotype. (schiavo2026shouldescherichiacoli pages 5-8)

### 5.3 Updated view of archaeal and bacterial strategies

A 2024 review describes Na⁺ exclusion through Na⁺/H⁺ antiporters, membrane-potential-driven K⁺ entry, organic-compatible-solute accumulation, and Msc channels as osmotic safety valves. It also reports trehalose-biosynthesis genes in **38** surveyed Halobacteriales genomes and BCCT-family transporters in **60**. These statistics demonstrate broad distribution, not phenotype-specific causality; they should not be used to annotate slight-halophile bacteria without organism-level evidence. (bonnaud2024haloarchaeaaspromising pages 2-4)

## 6. Applications and real-world relevance

Understanding low-to-moderate salt optima has practical value in:

- **Food and industrial fermentation:** selecting hosts that remain productive in saline feedstocks or salt-containing fermentations.
- **Compatible-solute production:** ectoine, glycine betaine, proline, and related osmolytes are products and engineering targets.
- **Agriculture:** halotolerant plant-growth-promoting bacteria are candidates for saline soils, but plant benefit and bacterial salt optimum must be demonstrated separately.
- **Saline wastewater and bioremediation:** organisms with low-to-moderate salt optima may outperform nonadapted strains without requiring hypersaline reactors.
- **Biomanufacturing and downstream processing:** salt adaptation and mechanosensitive-channel engineering can be exploited for robust cultivation or controlled osmotic lysis.

These applications motivate the graph but should generally be represented as annotations rather than causal nodes determining METPO:1000466. The 2026 *E. coli* paper mentions fermentation, carotenoid/ectoine production, and bioremediation as application domains, although its preprint status limits authority. (schiavo2026shouldescherichiacoli pages 1-5)

## 7. Expert interpretation for TraitMech

The major expert-level distinction is between a **mechanism of survival under osmotic stress** and a **mechanism establishing an optimum at 1–3% NaCl**. Compatible-solute systems, K⁺ uptake, Na⁺ extrusion, and Msc channels can broaden tolerance in many organisms. They do not necessarily make 1–3% better than 0% or 4–5%. A true optimum may additionally reflect membrane energetics, transporter coupling, enzyme ion dependence, cell-envelope stability, nutrient transport, or regulatory trade-offs. Those links require strain-specific evidence.

Accordingly, the graph should use two evidence layers:

- **Core physiological layer:** conserved osmotic challenge → water/turgor change → osmoadaptive response → growth maintenance.
- **Trait-determining layer:** strain-specific gene or intervention → measured shift in the NaCl growth-response curve or optimum. At present, this second layer is under-supported for the precise METPO interval.

## 8. Claims not yet ready for curation

1. **“ectABC causes NaCl optimum mid1.”** Ectoine commonly supports salt tolerance, but direct evidence that ectABC positions an optimum at 1–3% is lacking here.
2. **“Any Opu/ProU/BetT system causes slight halophily.”** Transporter substrate range, regulation, and physiological effect vary by taxon.
3. **“K⁺ accumulation is the universal first response.”** It is common but not universal; some lineages tightly restrict ion accumulation or use hybrid strategies.
4. **Extreme-halophile results transferred to slight halophiles.** The *N. thermophilus* edges are strong within that organism but should be tagged taxon-specific and high-salinity-specific. (xing2024thepolyextremophilenatranaerobius pages 14-17)
5. **Genome presence treated as pathway activity.** Genomic hits need expression, metabolite, mutant, or transport data.
6. **NaCl tolerance treated as NaCl optimum.** Survival or maximum growth boundary is not the same as best growth.
7. **NaCl treated as pure osmotic stress.** Na⁺ and Cl⁻ effects can differ from iso-osmotic nonionic solutes.
8. **2026 preprint as primary authority.** It is useful for boundary and candidate-gene context but should not supersede peer-reviewed evidence. (schiavo2026shouldescherichiacoli pages 5-8, schiavo2026shouldescherichiacoli pages 1-5)
9. **Exact CURIE assignment without database verification.** Keep gene-family and specialized-metabolite nodes label-only when the applicable ontology release has not been checked.

## 9. DOI-first bibliography

1. **Xing Q, et al.** “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.” *Applied and Environmental Microbiology* 90, May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 14-17)
2. **Bonnaud E, Oger PM, Ohayon A, Louis Y.** “Haloarchaea as Promising Chassis to Green Chemistry.” *Microorganisms* 12:1738, August 2024. DOI: [10.3390/microorganisms12081738](https://doi.org/10.3390/microorganisms12081738). (bonnaud2024haloarchaeaaspromising pages 2-4)
3. **Bremer E, Krämer R.** “Responses of Microorganisms to Osmotic Stress.” *Annual Review of Microbiology* 73:313–334, September 2019. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). This remains the most authoritative mechanistic synthesis among the retrieved sources. (bremer2019responsesofmicroorganisms pages 3-5)
4. **Schiavo APM, et al.** “Should *Escherichia coli* K-12 substrain MG1655 be classified as NaCl resistant?” Preprint, March 2026. DOI: [10.21203/rs.3.rs-8882295/v1](https://doi.org/10.21203/rs.3.rs-8882295/v1). Use cautiously because it is a preprint and outside the requested 2023–2024 priority window. (schiavo2026shouldescherichiacoli pages 5-8, schiavo2026shouldescherichiacoli pages 1-5)

## Curation conclusion

**METPO:1000466** is suitable for a TraitMech graph, but the present evidence supports a **generic osmoadaptation mechanism more strongly than a mechanism uniquely determining the 1–3% optimum**. Curate the water-flux, compatible-solute, and mechanosensitive-channel backbone now. Add nha/kdp/trk, bet/opu/proU, ots, ect, and taxon-specific hybrid-strategy branches only when organism-level expression, metabolite, transport, mutant, or optimum-shift evidence is available. All extreme-halophile and genomic-only edges should remain explicitly uncertain.

References

1. (schiavo2026shouldescherichiacoli pages 1-5): Ana Paula Muche Schiavo, Roberta Almeida Vincenzi, Isabella Gaião Silva, and Fabio Rodrigues. Should escherichia coli k-12 substrain mg1655 be classified as nacl resistant? Unknown journal, Mar 2026. URL: https://doi.org/10.21203/rs.3.rs-8882295/v1, doi:10.21203/rs.3.rs-8882295/v1.

2. (schiavo2026shouldescherichiacoli pages 5-8): Ana Paula Muche Schiavo, Roberta Almeida Vincenzi, Isabella Gaião Silva, and Fabio Rodrigues. Should escherichia coli k-12 substrain mg1655 be classified as nacl resistant? Unknown journal, Mar 2026. URL: https://doi.org/10.21203/rs.3.rs-8882295/v1, doi:10.21203/rs.3.rs-8882295/v1.

3. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

4. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

5. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 8 citations.