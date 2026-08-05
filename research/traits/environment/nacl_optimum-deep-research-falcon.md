---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:34:12.481770'
end_time: '2026-08-04T01:41:03.221284'
duration_seconds: 410.74
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum
  trait_identifier: METPO:1000333
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits that supports the most efficient
    growth and reproduction of an organism.
  parent_traits: METPO:1000532, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports the NaCl concentration at which growth rate is maximal as a standard
    halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high
    salt concentrations (Saline-Systems review supports osmotic balance at the optimal
    NaCl as the mechanistic basis of the NaCl-optimum phenotype.)'
  causal_graph_summary: 'nacl_optimum_balanced_osmoadaptation: 16 nodes, 11 edges'
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
- **Trait label:** NaCl optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000333
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that supports the most efficient growth and reproduction of an organism.
- **Parent traits:** METPO:1000532, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the NaCl concentration at which growth rate is maximal as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic balance at the optimal NaCl as the mechanistic basis of the NaCl-optimum phenotype.)
- **Existing causal graph summary:** nacl_optimum_balanced_osmoadaptation: 16 nodes, 11 edges

## Research Objective

Research the microbial trait **NaCl optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum.yaml`.

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
- **Trait label:** NaCl optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000333
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that supports the most efficient growth and reproduction of an organism.
- **Parent traits:** METPO:1000532, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the NaCl concentration at which growth rate is maximal as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic balance at the optimal NaCl as the mechanistic basis of the NaCl-optimum phenotype.)
- **Existing causal graph summary:** nacl_optimum_balanced_osmoadaptation: 16 nodes, 11 edges

## Research Objective

Research the microbial trait **NaCl optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum.yaml`.

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


# Curation report: NaCl optimum

**Trait:** NaCl optimum  
**Identifier:** `METPO:1000333`  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Definition supplied:** “A salinity phenotype with numerical limits that supports the most efficient growth and reproduction of an organism.”

## 1. Scope and current interpretation

`METPO:1000333` should represent the **assay-conditional NaCl concentration, or narrow concentration plateau, at which a microbial growth-performance endpoint is maximal**. Preferred endpoints are maximum specific growth rate during exponential growth, minimum doubling time, or—if those are unavailable—maximum biomass yield or colony radial-growth rate. In *Wallemia ichthyophaga*, for example, growth rates were calculated from exponential-phase doubling times; its optimum was 15–20% NaCl, whereas its full growth range extended from 10% to saturated NaCl (32%). Thus, optimum and range are distinct observations. (zajc2014osmoadaptationstrategyof pages 6-7, zajc2014osmoadaptationstrategyof pages 7-8, zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3)

The trait is conditional on medium composition, temperature, pH, oxygen regime, carbon source, incubation duration, inoculum, and measurement endpoint. Oren explicitly separates “the minimum salt concentration required for growth, the salinity optimum, and the upper salt limit tolerated,” while warning that all three depend on medium and temperature. (oren2008microbiallifeat pages 1-2)

### Boundary cases

- **Not NaCl growth range:** the interval permitting detectable growth.
- **Not maximum NaCl tolerated:** the upper concentration allowing any growth or survival.
- **Not minimum NaCl requirement:** especially important for obligate halophiles.
- **Not halotolerance:** halotolerant organisms can grow without an absolute salt requirement; halophily denotes preferential or required growth at elevated salinity. A traditional operational classification places moderate-halophile optima at 0.5–2.5 M salt and extreme-halophile optima at 2.5–5.2 M, but these categories are conventions rather than mechanistic boundaries. (oren2008microbiallifeat pages 2-4, oren2008microbiallifeat pages 1-2)
- **Not acute salt-shock tolerance:** short-term survival, transcription, or metabolite release after hyperosmotic shock does not establish a steady-state growth optimum.
- **Not generic salinity optimum:** NaCl concentration must not be silently equated with total dissolved salts, conductivity, or water activity. The Dead Sea, for example, contains over 35% total dissolved salts with substantial divalent-ion content; such exposure is chemically different from an NaCl-defined medium. (ionescu2024extremefluctuationsin pages 1-2)
- **Not merely water-activity optimum:** NaCl changes both water activity and ion composition. *W. ichthyophaga* grew across reported water activities of approximately 0.959–0.771, but this does not make water activity and NaCl interchangeable traits. (zajc2014osmoadaptationstrategyof pages 1-2)

**Recommended assay representation:** retain concentration value, unit and basis (`% w/v`, `g L−1`, molarity, or total Na+), medium, temperature, pH, atmosphere, endpoint, time point, and whether the result is a single optimum or plateau. Avoid converting percentages to molarity unless the original concentration basis is explicit.

## 2. Mechanistic model

External NaCl raises extracellular osmotic pressure and lowers water availability. Uncompensated cells lose water and turgor and experience ionic and macromolecular dysfunction. Efficient growth therefore occurs where osmotic and ionic homeostasis are restored without excessive energetic, transport, biosynthetic, or protein-folding costs. The optimum is an **emergent system-level outcome**, not the product of one universal “NaCl-optimum gene.”

Two canonical strategies dominate authoritative interpretations:

1. **Salt-in:** cells accumulate mainly KCl to balance external osmotic pressure. This requires a proteome adapted to molar salt—typically enriched in acidic proteins—and can impose a lower-salt growth defect because many proteins lose stability in dilute conditions.
2. **Salt-out/compatible-solute strategy:** cells limit cytoplasmic inorganic salt and synthesize or import compatible solutes such as ectoine, glycine betaine, proline, glutamate, sugars, and polyols. This generally supports a broader salinity range but consumes metabolic energy and/or transport capacity. (oren2008microbiallifeat pages 1-2, ionescu2024extremefluctuationsin pages 1-2)

Recent evidence shows that this dichotomy is not absolute. *Natranaerobius thermophilus* and organisms from fluctuating Dead Sea spring biofilms appear to use hybrid strategies combining compatible-solute and inorganic-ion mechanisms. The Dead Sea study’s conclusion is genomic and ecological—selection for hybrid capacity remains a hypothesis rather than a demonstrated determinant of a species-level NaCl optimum. (xing2024thepolyextremophilenatranaerobius pages 1-2, ionescu2024extremefluctuationsin pages 1-2, ionescu2024extremefluctuationsin pages 4-6)

## 3. Candidate graph nodes

### Trait and assay nodes

- NaCl optimum — `METPO:1000333`
- NaCl concentration — candidate chemical grounding: `CHEBI:26710` (sodium chloride); concentration itself should be represented as a measurement with value/unit
- maximal specific growth rate; doubling time; biomass yield; colony radial-growth rate — retain as label-only assay nodes unless the project’s measurement ontology supplies mappings
- growth range; minimum NaCl requirement; maximum tolerated NaCl — neighboring traits, not synonyms
- water activity — label-only candidate
- total dissolved salts / environmental salinity — label-only candidate; do not merge with NaCl concentration

### Environmental and physicochemical nodes

- extracellular osmotic pressure
- hyperosmotic environment / osmotic stress
- water availability and cellular water loss
- medium composition, temperature, pH, oxygen availability, incubation duration
- saline or hypersaline environment — ENVO grounding should be selected only after confirming the exact ENVO term required by the curation schema

### Ions and compatible solutes

- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- chloride — `CHEBI:17996`
- glycine betaine — `CHEBI:17750`
- L-proline — `CHEBI:17203`
- L-glutamate — `CHEBI:29985`
- ectoine — stable ChEBI grounding should be registry-verified before insertion
- glutamine, trehalose, hydroxyectoine, glycerol — candidate metabolite nodes; verify exact ChEBI forms

### Genes, proteins, and transport systems

- `ectA`, `ectB`, `ectC` / EctABC ectoine-biosynthesis module
- `proB`, `proA`, `proC` / proline-biosynthesis module
- `putA` / bifunctional proline-utilization enzyme
- feedback-insensitive γ-glutamate kinase ProB D118N/D119N
- Opu- and ProU-family glycine-betaine ABC transporters
- BCCT-family betaine/carnitine/choline transporters
- SSS-family Na+/solute symporters
- PutP sodium/proline symporter
- Trk potassium-uptake system
- Na+/K+/H+ transporters or antiporters
- GlsA glutaminase, GudB glutamate dehydrogenase, FctD glutamate formimidoyltransferase
- acidic-proteome adaptation

These family labels should remain label-only unless the source identifies a specific locus and the curator verifies the corresponding UniProt, GO, KEGG, or transporter-classification record. A family-level omics signal must not be assigned to a particular gene without sequence-level evidence.

### Pathways, functions, and cellular processes

- compatible-solute biosynthesis and uptake
- ectoine biosynthesis
- proline biosynthesis and catabolism
- potassium accumulation / salt-in osmoadaptation
- ion homeostasis
- osmotic adjustment
- ATP production and energy metabolism
- protein folding, solubility, and stability at high ionic strength
- cytoplasmic acidification
- cell-wall thickening and extracellular-polysaccharide production

Useful broad GO candidates include response to osmotic stress (`GO:0006970`) and cellular ion homeostasis (`GO:0006873`). More specific mappings should be verified against the current ontology release before committing them to YAML.

## 4. Candidate causal edges

The table below prioritizes direct perturbation evidence, then quantitative multi-omics evidence, and finally authoritative review-level mechanisms.

| subject | predicate | object | taxon/assay context | DOI | short exact supporting snippet | confidence/curation note |
|---|---|---|---|---|---|---|
| external NaCl concentration | increases | external osmotic pressure | General halophile physiology; review context | 10.3389/frmbi.2023.1329925 | “To account for the external osmotic pressure halophile microorganisms have adopted two main strategies.” (ionescu2024extremefluctuationsin pages 1-2) | Review-general. Supports salinity→osmotic challenge, but object is phrased as osmotic pressure rather than a directly assayed node. Curate as broad mechanistic context. |
| compatible-solute accumulation | contributes to | osmotic balance / osmoadaptation | General halophile physiology; review context | 10.1186/1746-1448-4-2 | “Halophilic microorganisms use two strategies to balance their cytoplasm osmotically with their medium… to synthesize and/or accumulate organic 'compatible' solutes” (oren2008microbiallifeat pages 1-2) | Strong review-general edge. Good high-level TraitMech edge for many bacteria/archaea using salt-out strategy. |
| ectABC operon | enables biosynthesis of | ectoine | *Halomonas elongata* OUT30018 and derivatives; genomic engineering study | 10.1128/aem.01195-24 | “H. elongata OUT30018’s Ect biosynthetic operon” and “ectA: a gene that encodes a DAA. ectB: a gene that encodes a DAT. ectC: a gene that encodes an ES.” (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | Strong, near-direct gene→metabolite edge. Taxon-specific but highly curation-ready. |
| ΔectABC::mCherry-proBm1AC plus ΔputA | increases | intracellular proline accumulation | *H. elongata* engineered strains grown in 15% NaCl LB | 10.1128/aem.01195-24 | “H. elongata HN6 (ΔectABC::mCherry-proBm1AC ΔputA) accumulated much higher Pro… 123.03 µmol/g CFW” (khanh2024metabolicpathwayengineering pages 6-9) | Strong direct perturbation edge from engineering intervention to proline accumulation. Curate with assay context. |
| increased intracellular proline accumulation | improves | high-salinity growth | *H. elongata* M63 media with different salinity levels | 10.1128/aem.01195-24 | “the increase in high-salinity tolerance observed in H. elongata HN6 was a result of an increase in the intracellular accumulation of Pro” (khanh2024metabolicpathwayengineering pages 6-9) | Strong direct mechanistic claim within one study; assay-specific and engineered-strain specific. |
| glycine betaine ABC transporters (Opu/ProU families) | facilitate adaptation to | high salinity | *Natranaerobius thermophilus* long-term salinity adaptation, 2.5–4.3 M Na+ | 10.1128/aem.00145-24 | “N. thermophilus employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong taxon-specific omics-supported edge; not a knockout perturbation. Curate as species-specific unless generalized carefully. |
| Na+/solute symporters (SSS family) | facilitate adaptation to | high salinity | *N. thermophilus* long-term salinity adaptation, 2.5–4.3 M Na+ | 10.1128/aem.00145-24 | “N. thermophilus employs… Na+/solute symporters (SSS family)… to adapt to high salinity.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong taxon-specific transporter edge from multi-omics study; mechanism plausible but not individually validated by genetics. |
| rising salinity | increases | intracellular compatible solutes (glycine betaine, glutamate, proline) | *N. thermophilus* across 2.5–4.3 M Na+ | 10.1128/aem.00145-24 | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong species-specific phenotype→metabolite edge with quantitative backing in study. |
| Na+/K+/H+ transporters | maintain | intracellular K+ concentration / ion homeostasis | *N. thermophilus* under varying salinities | 10.1128/aem.00145-24 | “the upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration, ensuring cellular ion homeostasis” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong species-specific edge, omics-plus-metabolite supported. Good candidate ion-homeostasis mechanism. |
| KCl accumulation | requires adaptation of | intracellular enzymatic machinery / acidic proteome | General extreme halophiles; review context | 10.1186/1746-1448-4-2 | “The first involves accumulation of molar concentrations of KCl. This strategy requires adaptation of the intracellular enzymatic machinery… The proteome of such organisms is highly acidic” (oren2008microbiallifeat pages 1-2) | Strong review-general mechanistic edge. Good for high-level graph; not universal to all halophiles. |
| acidic proteome | supports | protein conformation/activity at high salt | General extreme halophiles; review context | 10.1186/1746-1448-4-2 | “proteins should maintain their proper conformation and activity at near-saturating salt concentrations. The proteome of such organisms is highly acidic” (oren2008microbiallifeat pages 1-2) | Review-general and slightly inferred as causal; curate with note that source states association/requirement rather than direct perturbation. |
| low salt | causes loss of | protein stability in salt-in strategists | Haloarchaea/extreme halophiles; review context | 10.1186/1746-1448-4-2 | “most proteins denature when suspended in low salt” (oren2008microbiallifeat pages 1-2) | Strong review-general edge for salt-in taxa; helpful boundary-case mechanism distinguishing NaCl optimum from low-salt growth failure. |
| carbohydrate and energy metabolism | increases ATP production for | osmoprotective functions | *N. thermophilus* at 3.7 M Na+ vs 2.5 M Na+ | 10.1128/aem.00145-24 | “Carbohydrate and energy metabolism pathways… are enriched to increase ATP production for osmoprotective functions.” (xing2024thepolyextremophilenatranaerobius pages 10-14) | Strong species-specific systems-level edge, but wording is interpretive from pathway enrichment. Curate as omics-inferred, not direct biochemical proof. |
| salinity optimum | corresponds to | maximal growth readout | General phenotype definition; experimental growth-curve context | 10.1128/aem.02702-13 | “to determine the salinity growth optimum” and “The growth rates were calculated from the doubling times obtained from the growth curves during the exponential growth phase.” (zajc2014osmoadaptationstrategyof pages 2-3) | Strong assay-definition edge. Supports trait semantics: optimum is the NaCl condition with best growth performance, distinct from range/tolerance. |
| growth optimum / salt relationships | is distinct from | minimum required salt and upper salt limit tolerated | General classification; review context | 10.1186/1746-1448-4-2 | “the minimum salt concentration required for growth, the salinity optimum, and the upper salt limit tolerated” (oren2008microbiallifeat pages 1-2) | Strong scope/boundary edge for curation. Important to avoid conflating optimum with tolerance range. |


*Table: This table lists compact, source-backed candidate causal edges for curating microbial NaCl optimum mechanisms, emphasizing direct perturbation evidence where available and clearly marking broader review-based or uncertain edges.*

### Highest-priority curation chain

For a compact initial graph, the strongest experimentally causal chain is taxon-specific:

`proBm1AC expression + putA deletion` → `increased intracellular proline` → `improved growth at elevated NaCl`.

In engineered *Halomonas elongata* HN6, replacing `ectABC` with feedback-insensitive `proBm1AC` and deleting `putA` produced 123.03 µmol proline g−1 cell fresh weight in 15% NaCl LB. In minimal medium, HN6 accumulated 115.9 ± 7.8 µmol g−1 at 6% NaCl; its growth IC50 shifted to 6.1% NaCl versus 4.2% for HN1, and it could thrive at 8% NaCl while the ectoine-deficient parent failed above 4%. The study also reported 353.1 ± 40.5 µmol proline g−1 fresh weight under its 8% NaCl condition. These results directly connect a defined genetic intervention, osmolyte accumulation, and altered high-salinity growth. They demonstrate **movement of the growth response**, although an IC50 or improved tolerance is not automatically equivalent to a rigorously re-estimated NaCl optimum. (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9)

### Recent systems-level evidence

The 2024 *N. thermophilus* study compared 2.5, 3.1, 3.7, and 4.3 M Na+ at pH 9.5 and 53°C; the organism’s reported optimum is 3.3–3.9 M Na+. Glycine betaine increased from 52.7 to 893.1 mM across the gradient, while glutamate rose from 11.0 to 221.3 mM. Proline was non-monotonic, falling to 67.0 mM at 3.1 M before increasing to 130 mM at 4.3 M. Opu/ProU, BCCT/SSS systems, PutP, glutamate/proline pathways, and Na+/K+/H+ transport were implicated; several solute-synthesis or transport proteins increased more than 100-fold. Carbohydrate and energy metabolism represented 14.3% of differentially expressed proteins, consistent with energetic support for osmoadaptation. These are strong concentration-response and multi-omics associations but not individual-gene knockout evidence. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14)

## 5. Recent developments and applications

### Metabolic engineering

The 2024 *H. elongata* work demonstrates replacement of ectoine with proline as the dominant osmolyte and proposes a salt-tolerant, proline-rich cell factory for converting biomass waste into aquaculture or livestock feed additives. The host is already relevant to industrial ectoine production; engineering the osmoadaptation module couples product formation to saline growth conditions. (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9)

### Robust high-salinity bioprocessing

Halophilic production hosts can support processing at high salt and potentially reduce sterilization, freshwater, and contamination-control demands. This remains application context rather than a causal edge to NaCl optimum. The Dead Sea study explicitly identifies high-salt, non-sterile bioprocessing as an industrial motivation. (ionescu2024extremefluctuationsin pages 1-2)

### Environmental prediction and community ecology

Salinity-optimum phenotypes help predict taxa selected along salinity gradients and distinguish specialists from broad-range organisms. In fluctuating Dead Sea spring interfaces, MAGs from *Prosthecochloris*, *Flexistipes*, *Izemoplasma*, *Halomonas*, and Halanaerobiales contained capacities associated with both strategies. However, MAG content predicts potential; it does not establish expression, flux, or the growth optimum of each organism. (ionescu2024extremefluctuationsin pages 1-2, ionescu2024extremefluctuationsin pages 4-6)

### Comparative physiology and taxonomy

Minimum, optimum, and maximum salt relationships remain standard phenotypic descriptors for microbial characterization. *W. ichthyophaga* illustrates the importance of kinetic assays: despite growth from 10% to 32% NaCl, its optimum was only 15–20%, and very slow growth required prolonged observation. (zajc2014osmoadaptationstrategyof pages 6-7, zajc2014osmoadaptationstrategyof pages 7-8, zajc2014osmoadaptationstrategyof pages 1-2)

## 6. Expert analysis for TraitMech design

A defensible graph should separate three layers:

1. **Environmental input:** NaCl concentration under explicitly recorded assay conditions.
2. **Homeostatic mechanisms:** ion transport, compatible-solute synthesis/uptake, water/turgor restoration, proteome adaptation, and energetic support.
3. **Phenotypic readout:** a growth curve whose maximum identifies `METPO:1000333`.

The graph should permit alternative and hybrid branches rather than forcing all taxa through one route. Salt-in organisms can have a high optimum partly because their proteins require high ionic strength; salt-out organisms can shift their response through osmolyte availability and transporter capacity. Hybrid organisms may trade rapid scalability against energetic cost. The optimum therefore reflects a balance between insufficient osmotic support at low salt, successful homeostasis near the optimum, and increasing osmotic/ionic and energetic burden above it. The final “balanced osmoadaptation → maximal growth” edge is biologically compelling but should be marked as a systems-level synthesis unless directly demonstrated through growth curves plus perturbation.

## 7. Claims not yet safe to curate

- **Do not curate a universal gene → NaCl-optimum edge.** Mechanisms are strongly taxon-dependent.
- **Do not equate high-salt tolerance or IC50 with optimum.** The *H. elongata* perturbation establishes improved growth/tolerance, but a full concentration series with specific growth rates is needed to prove that the optimum itself shifted.
- **Do not generalize the *N. thermophilus* hybrid strategy beyond that species or Clostridia.** Its transporter and pathway edges are multi-omics-supported, not genetic perturbations.
- **Do not treat MAG presence as pathway activity.** Dead Sea hybrid-strategy claims are genomic and partly hypothetical.
- **Do not merge NaCl, Na+, total salts, conductivity, osmolarity, and water activity.** They require separate nodes and measurements.
- **Do not omit assay covariates.** Temperature, pH, medium, oxygen and endpoint can change the reported optimum.
- **Do not curate acidic proteome as universal.** It chiefly applies to salt-in lineages; some moderate halophiles use compatible solutes or mixed strategies.
- **Do not treat osmolyte concentration as necessarily monotonic or sufficient.** Proline in *N. thermophilus* was non-monotonic across the tested Na+ gradient. (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **Cell-wall thickening, EPS, chemotaxis, cytoplasmic acidification, and broad energy-pathway enrichment** are plausible supporting modules, but should remain secondary or uncertain unless perturbation evidence links them to a shifted growth optimum.
- **Verify all ontology identifiers against current releases.** Label-only nodes are preferable to invented or over-specific CURIEs.

## 8. DOI-first bibliography

1. Xing Q, et al. **The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.** *Applied and Environmental Microbiology*. Published May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14)
2. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.** *Applied and Environmental Microbiology*. Published 19 August 2024; September 2024 issue. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9)
3. Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y. **Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/“salt-out” osmoregulation strategy.** *Frontiers in Microbiomes*. Published 8 January 2024. DOI: [10.3389/frmbi.2023.1329925](https://doi.org/10.3389/frmbi.2023.1329925). (ionescu2024extremefluctuationsin pages 1-2, ionescu2024extremefluctuationsin pages 4-6)
4. Gunde-Cimerman N, Plemenitaš A, Oren A. **Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.** *FEMS Microbiology Reviews*. Published May 2018. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009).
5. Zajc J, Kogej T, Galinski EA, Ramos J, Gunde-Cimerman N. **Osmoadaptation strategy of the most halophilic fungus, *Wallemia ichthyophaga*, growing optimally at salinities above 15% NaCl.** *Applied and Environmental Microbiology*. Published January 2014. DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13). (zajc2014osmoadaptationstrategyof pages 6-7, zajc2014osmoadaptationstrategyof pages 7-8, zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3)
6. Oren A. **Life at high salt concentrations, intracellular KCl concentrations, and acidic proteomes.** *Frontiers in Microbiology*. Published November 2013. DOI: [10.3389/fmicb.2013.00315](https://doi.org/10.3389/fmicb.2013.00315).
7. Oren A. **Microbial life at high salt concentrations: phylogenetic and metabolic diversity.** *Saline Systems*. Published 15 April 2008. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2). (oren2008microbiallifeat pages 2-4, oren2008microbiallifeat pages 1-2)

**Recommended initial curation:** retain the existing balanced-osmoadaptation backbone, add separate salt-in, salt-out, and hybrid branches, and prioritize the *H. elongata* genetic perturbation chain as direct causal evidence. Represent the *N. thermophilus* transporter/metabolite relations as taxon-specific, omics-supported edges and the broad KCl/acidic-proteome relations as review-supported class-level edges.

References

1. (zajc2014osmoadaptationstrategyof pages 6-7): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

2. (zajc2014osmoadaptationstrategyof pages 7-8): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

3. (zajc2014osmoadaptationstrategyof pages 1-2): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

4. (zajc2014osmoadaptationstrategyof pages 2-3): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

5. (oren2008microbiallifeat pages 1-2): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

6. (oren2008microbiallifeat pages 2-4): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

7. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

8. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

9. (ionescu2024extremefluctuationsin pages 4-6): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

10. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

11. (khanh2024metabolicpathwayengineering pages 6-9): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

12. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

13. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.