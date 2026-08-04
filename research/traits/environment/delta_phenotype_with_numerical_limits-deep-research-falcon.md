---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:14:55.776303'
end_time: '2026-08-04T00:28:41.533182'
duration_seconds: 825.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: delta phenotype with numerical limits
  trait_identifier: METPO:1000534
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: delta_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the difference between maximum and minimum
    values of a growth parameter.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the breadth of a growth-supporting environmental range as a derived quantitative
    descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted
    to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance
    breadth as a comparable derived quantitative descriptor.)'
  causal_graph_summary: 'delta_phenotype_breadth_descriptor: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 70
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** delta phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000534
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the difference between maximum and minimum values of a growth parameter.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the breadth of a growth-supporting environmental range as a derived quantitative descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance breadth as a comparable derived quantitative descriptor.)
- **Existing causal graph summary:** delta_phenotype_breadth_descriptor: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **delta phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/delta_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** delta phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000534
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the difference between maximum and minimum values of a growth parameter.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the breadth of a growth-supporting environmental range as a derived quantitative descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance breadth as a comparable derived quantitative descriptor.)
- **Existing causal graph summary:** delta_phenotype_breadth_descriptor: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **delta phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/delta_phenotype_with_numerical_limits.yaml`.

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


# Curation report: “delta phenotype with numerical limits”

## Executive conclusion

The reviewed trait identifier is **“METPO:1000534”**. It should be modeled primarily as a **derived assay phenotype**, not as a single molecular mechanism:

\[
\Delta x = x_{\max,\mathrm{growth}}-x_{\min,\mathrm{growth}}
\]

Here, *x* is one explicitly identified environmental variable—such as temperature, pH, salinity, pressure, or inhibitor concentration—and both limits must be determined using the same operational definition of microbial growth. Mechanisms generally act on one or both endpoints; the delta is then calculated. A defensible graph should therefore preserve the chain **mechanism → lower/upper growth limit → calculated delta**, rather than asserting that a gene directly “causes delta phenotype breadth.”

The strongest presently curatable mechanistic examples are temperature-dependent membrane remodeling and high-temperature growth in experimentally evolved *Escherichia coli*, and TolC-dependent growth at moderately acidic pH. Compatible-solute and proteome-remodeling literature provides important candidate nodes for salinity breadth, but most available evidence remains associative or concerns adaptation to high salinity rather than a measured change in both growth limits.

## 1. Trait scope and boundary cases

### 1.1 Recommended operational definition

**“METPO:1000534”** represents the numerical distance between the maximum and minimum values of a specified environmental parameter that support growth under a defined assay. Each observation should record:

- environmental axis and units;
- lower and upper tested values;
- culture medium and other held-constant conditions;
- strain and taxonomic identity;
- inoculum and acclimation history;
- incubation duration;
- growth readout and positivity threshold;
- whether endpoints are observed limits or interval-censored by the assay grid;
- calculated delta and uncertainty.

For example, an experimentally confirmed temperature interval of −10°C to 28°C has a nominal delta of 38°C. *Psychrobacter arcticus* 273-4 was reported to grow actively over that interval, with low-temperature transcriptional and membrane responses, although another analyzed portion of the paper described measurements from −6°C to 22°C. The wider value should only be used after checking the primary methods and endpoint criteria in the source (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 1-2).

### 1.2 Nearby traits that must remain distinct

1. **Minimum or maximum growth limit:** These are endpoint phenotypes and should be parent inputs to the calculated delta.
2. **Optimal environmental value:** Moving an optimum does not necessarily widen the growth interval. In evolved *E. coli*, both optimum and maximum temperatures changed, but these are distinct measurements (blaby2012experimentalevolutionof pages 7-8, blaby2012experimentalevolutionof pages 4-5).
3. **Growth rate or biomass yield:** Performance within the interval is not its breadth. A strain may widen or shift an endpoint while growing more slowly elsewhere.
4. **Stress survival:** Transient survival at pH 2 or after heat shock is not growth at that value. Evolved *E. coli* gained high-temperature growth but had poorer transient heat survival, directly demonstrating this distinction (blaby2012experimentalevolutionof pages 7-8, blaby2012experimentalevolutionof pages 4-5).
5. **Tolerance at one challenge concentration:** Colony formation at 9% NaCl establishes an upper observed capability under that assay, not a complete salinity breadth unless the lower limit and growth criterion are also recorded (shi2023mechanismofsalt pages 2-4, shi2023mechanismofsalt pages 1-2).
6. **Ecological niche breadth:** Culture-based growth limits estimate a one-axis component of the fundamental niche. Geographic or community occurrence estimates a realized niche affected by dispersal, competition, facilitation, dormancy, and detection limits (bebber2022specialistsgeneralistsand pages 3-4, bell2021manyroadsto pages 17-18).
7. **Social niche breadth:** A community-co-occurrence metric derived from thousands of environmental samples is conceptually different from a numerical growth interval.
8. **Multidimensional generalism:** Broad temperature tolerance does not establish broad pH, nutrient, host, or habitat breadth. Generalism can be discrete or continuous and can refer separately to resources, habitats, or environmental parameters (bell2021manyroadsto pages 27-28).
9. **Acclimation-induced shift:** A simultaneous shift of both endpoints without a change in their difference is not a change in delta breadth.

## 2. Candidate nodes grouped by type

Only identifiers that can be supplied confidently are included. Gene symbols are retained as label-only candidates because stable identifiers are taxon- and strain-specific and should be resolved during organism-specific curation.

### Trait and measurement nodes

- **“METPO:1000534”** — delta phenotype with numerical limits.
- **“METPO:1000059”** — supplied parent trait.
- Growth-supporting lower numerical limit — label-only candidate.
- Growth-supporting upper numerical limit — label-only candidate.
- Environmental-axis value, unit, assay threshold, incubation duration, and measurement uncertainty — experimental metadata nodes.
- Temperature-growth breadth, pH-growth breadth, and salinity-growth breadth — contextualized subclasses or assay-result labels; do not assign new METPO identifiers without ontology confirmation.

### Environmental and experimental factors

- Temperature; external pH; NaCl concentration/salinity.
- Growth medium, nutrient availability, pressure, oxygen status, culture format, inoculum history, and acclimation state.
- Rich versus minimal medium is potentially causal: evolved *E. coli* displayed medium-dependent high-temperature growth limitations (blaby2012experimentalevolutionof pages 5-6).
- Growth positivity threshold and spacing between tested environmental values.

### Genes, proteins, transporters, and complexes

- **fabA** — candidate temperature-mechanism gene in experimentally evolved *E. coli*.
- **glpF** — deletion improved growth at 43–48°C and shifted the optimum upward in the studied background (blaby2012experimentalevolutionof pages 1-2, blaby2012experimentalevolutionof pages 5-6).
- **tolC** — required for maximal *E. coli* growth at pH 4.5–6.0; direct moderate-acid growth evidence (deininger2011arequirementof pages 1-2, deininger2011arequirementof pages 3-4).
- **gadA, gadB, gadC; adiA, adiC** — acid-survival candidates, but not presently supported as growth-breadth determinants (richard2004escherichiacoliglutamate pages 1-2, li2024responseofescherichia pages 2-4).
- Fatty-acid desaturase; **clpB**, **hsp33**, cold-shock proteins, DnaK/GroEL/GroES — temperature-response candidates. Current evidence is often expression-based or review-level rather than a direct breadth perturbation (sionek2024theimpactof pages 3-5, bergholz2009psychrobacterarcticus2734 pages 1-2).
- F₀F₁ ATP synthase — pH-homeostasis candidate; the cited evidence principally concerns acid resistance/survival rather than growth breadth (li2024responseofescherichia pages 2-4, richard2004escherichiacoliglutamate pages 2-4).

### Chemicals, ions, nutrients, and metabolites

- NaCl; sodium ion; potassium ion.
- Trehalose, glutamate, proline, glycine betaine, mannosylglycerate, and extracellular polysaccharides.
- Arginine and glutamate as substrates for amino-acid-dependent acid-resistance systems.
- Membrane saturated, unsaturated, and cyclopropane fatty acids.
- Reactive oxygen species and oxidized lipids as possible high-temperature constraints; a 2024 Symbiodiniaceae study found reduced growth at 31°C with oxidized-lipid and cell-cycle-stress signatures, but did not measure a changed growth breadth (motta2024diversityoflipid pages 1-2).

### Cellular locations, functions, and processes

- Cytoplasmic membrane; cytoplasm; periplasm; outer membrane.
- Homeoviscous adaptation and membrane-lipid remodeling.
- Compatible-solute biosynthesis/accumulation and osmoadaptation.
- K⁺/Na⁺ homeostasis; extracellular-polysaccharide production.
- Cytoplasmic-pH homeostasis; amino-acid decarboxylation; substrate/product antiport; proton motive force.
- Protein folding, chaperone activity, DNA repair, and macromolecular stabilization.
- Proteome acidification and salt-adapted protein solubility.

### Organisms and population contexts

- *Escherichia coli* K-12/MG1655 and experimentally evolved derivatives.
- *Psychrobacter arcticus* 273-4.
- *Priestia megaterium* ZS-3.
- Ammonia-oxidizing archaea as ecological pH-breadth examples.
- Moderate halophiles, haloarchaea, lactic-acid bacteria, and Symbiodiniaceae only when the exact strain and assay are retained.

## 3. Candidate causal edges

The table below distinguishes edges supported by direct growth perturbations from associations and survival-only mechanisms.

| Environmental axis / taxon | Subject (CURIE only if confident) | Predicate | Object | Evidence type and numerical data | DOI and publication date | Short supporting snippet | Curation status | Rationale |
|---|---|---|---|---|---|---|---|---|
| Generic environmental assay / any microbe | METPO:1000534 | derives_from | growth-parameter maximum minus minimum numerical limits | Definitional; breadth is the delta between assay-defined upper and lower growth-supporting limits | Trait definition; supporting analogy from salinity- and temperature-range reviews: 10.1093/femsre/fuy009 (2018-05), 10.1016/S0300-9629(97)00003-0 (1997-11) | "A phenotype characterized by the difference between maximum and minimum values of a growth parameter." | direct | Safe ontology edge for the trait itself; this is a descriptor edge, not a mechanism edge. |
| Temperature / *Escherichia coli* experimental evolution | fabA | increases | maximum growth temperature / higher-temperature growth capacity | Experimental evolution + genotype/phenotype link; EVG1064 Tmax increased from ~46°C to 48°C; altered fatty acid profile with increased saturated/unsaturated ratio and cyclopropane fatty acids | 10.1128/AEM.05773-11; 2012-01 | "The fabA mutation in the thermotolerant strain EVG1064 altered fatty acid profiles at 48°C, increasing saturated/unsaturated ratios and cyclopropane fatty acids..." (blaby2012experimentalevolutionof pages 7-8) | direct | Strong candidate mechanistic edge for temperature-limit increase; growth, not merely survival, was measured. |
| Temperature / *Escherichia coli* experimental evolution | fabA | associated_with | increased membrane lipid saturation (homeoviscous adaptation at high temperature) | Experimental evolution; complementation restored intermediate fatty-acid profiles | 10.1128/AEM.05773-11; 2012-01 | "fabA mutation, which increased membrane lipid saturation—a known homeoviscous adaptation to elevated temperature" (blaby2012experimentalevolutionof pages 1-2) | direct | Supports a mechanistic intermediate node linking genotype to altered high-temperature growth limit. |
| Temperature / *Escherichia coli* experimental evolution | glpF | deletion_of_increases | optimal growth temperature / growth at 43–48°C | Deletion analysis; Topt shifted from 37°C to ~43°C; improved doubling times at 43–48°C | 10.1128/AEM.05773-11; 2012-01 | "glpF deletion, which improved growth rates in the 43-48°C range and shifted optimal growth temperature from 37°C to 43°C" (blaby2012experimentalevolutionof pages 1-2) | direct | High-confidence growth phenotype edge; relevant because upward movement of one endpoint can expand delta breadth if the lower endpoint is unchanged. |
| pH / *Escherichia coli* | tolC | required_for | maximal exponential growth at pH 4.5–6.0 | Knockout + complementation; tolC deletion slowed growth at pH 4.5–6.0, not at pH 6.5–8.5; functional tolC restored pH 4.5 growth | 10.1371/journal.pone.0018960; 2011-04 | "TolC was required for maximal exponential growth of E. coli K-12 W3110, in LBK medium buffered at pH 4.5–6.0, but not at pH 6.5–8.5." (deininger2011arequirementof pages 1-2) | direct | Strong candidate for pH-range growth mechanism; directly tied to growth below pH 6.5 rather than only survival. |
| pH / *Escherichia coli* | tolC | not_restored_by | Gad-system overexpression for moderate-acid growth | Knockout/complementation distinction between growth and survival; GadE or GadB-C restored pH 2 survival but not pH 5 growth | 10.1371/journal.pone.0018960; 2011-04 | "at pH 5 growth, overexpression of Gad system components... could not restore wild-type growth rates in tolC mutants" (deininger2011arequirementof pages 3-4) | direct | Important exclusion/branching edge: moderate-acid growth mechanism is not reducible to Gad extreme-acid survival. |
| Salinity / *Priestia megaterium* ZS-3 | trehalose | associated_with | salt-stress growth / osmotic adaptation | Correlational physiology; tolerated up to 9% salinity; trehalose increased 56.24%, 87.43%, 466.67% at 3%, 5%, 7% NaCl | 10.3390/ijms242115751; 2023-10 | "trehalose accumulated dose-dependently, increasing 56.24%, 87.43%, and 466.67% at 3%, 5%, and 7% NaCl" (shi2023mechanismofsalt pages 2-4) | uncertain/do not curate | Useful candidate node, but no perturbation demonstrates trehalose causally changes salinity growth breadth. |
| Salinity / *Priestia megaterium* ZS-3 | glutamate | associated_with | salt-stress growth / osmotic adaptation | Correlational physiology; glutamate increased 374-fold, 320-fold, 150-fold at 3%, 5%, 7% NaCl | 10.3390/ijms242115751; 2023-10 | "Glutamate... increased 374-fold, 320-fold, and 150-fold under the same salt treatments." (shi2023mechanismofsalt pages 2-4) | uncertain/do not curate | Strong correlation with salt response, but still not a demonstrated causal breadth determinant. |
| Salinity / *Priestia megaterium* ZS-3 | extracellular polysaccharide | associated_with | salt-stress growth / osmotic response | Correlational physiology; EPS increased ~95-fold and 150-fold at 5% and 7% NaCl | 10.3390/ijms242115751; 2023-10 | "Extracellular polysaccharide (EPS) production showed 95- and 150-fold increases at 5% and 7% NaCl." (shi2023mechanismofsalt pages 2-4) | uncertain/do not curate | Candidate process node only; breadth effect is inferred, not directly perturbed. |
| Salinity / *Priestia megaterium* ZS-3 | potassium cation | associated_with | salt-stress growth / K+/Na+ balance | Correlational physiology; K+ significantly higher at 5% and 7% NaCl while growth still observed | 10.3390/ijms242115751; 2023-10 | "Potassium accumulation was significantly higher at 5% and 7% NaCl treatments, maintaining K+/Na+ balance." (shi2023mechanismofsalt pages 2-4) | uncertain/do not curate | Mechanistically plausible but not yet demonstrated as a causal determinant of delta salinity breadth. |
| pH / *Escherichia coli* | gadA / gadB / gadC | required_for | extreme-acid survival at pH 2–3 | Acid-resistance system; survival-focused, not growth-focused; Gad deletions affect survival at pH 2–3; pHi effects at pH 2.5 | 10.3390/microorganisms12091774; 2024-08 and 10.1128/JB.186.18.6032-6041.2004; 2004-09 | "Deletion of gadA, gadB, and gadC significantly affects bacterial survival at pH 2-3." (li2024responseofescherichia pages 2-4) | uncertain/do not curate | Exclude from growth-range trait unless curated under survival tolerance; evidence is explicitly about survival during extreme acid exposure. |
| pH / *Escherichia coli* | adiA / adiC | increases | internal pH during extreme-acid survival | Mechanistic physiology; at external pH 2.5, arginine system raised pHi to 4.7 | 10.1128/JB.186.18.6032-6041.2004; 2004-09 | "arginine decarboxylase (AdiA) with AdiC antiporter raises pHi to 4.7" (richard2004escherichiacoliglutamate pages 1-2) | uncertain/do not curate | Valuable acid-survival mechanism, but not direct evidence for expanded growth-supporting pH range. |
| Temperature / *Psychrobacter arcticus* 273-4 | homeoviscous adaptation | associated_with | subzero growth | Association from transcriptome/physiology; active growth from −10°C to 28°C experimentally confirmed; increased unsaturated membrane lipids at low temperatures | 10.1128/JB.01377-08; 2009-04 | "homeoviscous adaptation through increased unsaturated membrane fatty acids during growth at 4°C and −2.5°C" (bergholz2009psychrobacterarcticus2734 pages 1-2) | indirect | Good candidate process node for cold-end growth limit, but not isolated by a single perturbation in the excerpt. |
| Temperature / *Psychrobacter arcticus* 273-4 | fatty acid desaturase | upregulated_in | low-temperature active growth | Transcriptome association during growth at 22°C, 17°C, 0°C, −6°C | 10.1128/JB.01377-08; 2009-04 | "upregulation of cold acclimation proteins including RNA and protein chaperones, fatty acid desaturase" (bergholz2009psychrobacterarcticus2734 pages 1-2) | indirect | Supports mechanistic interpretation of cold-endpoint maintenance; still more associative than causal for breadth. |


*Table: This table summarizes candidate causal edges and exclusions for curating METPO:1000534, separating direct growth-range evidence from indirect or survival-only mechanisms. It is useful for deciding which nodes and edges are ready for TraitMech curation and which should be deferred.*

### Recommended minimal graph architecture

The safest generic graph is:

1. **environmental variable** → `is varied in` → **growth assay**;
2. **growth assay** → `determines` → **minimum growth-supporting value**;
3. **growth assay** → `determines` → **maximum growth-supporting value**;
4. **maximum value and minimum value** → `are operands in subtraction yielding` → **“METPO:1000534”**;
5. a molecular mechanism → `increases/decreases` → one endpoint **only where perturbation evidence exists**;
6. endpoint change → `increases/decreases` → delta only when the opposite endpoint is measured or explicitly held unchanged.

Thus, the evolved-*E. coli* evidence securely supports **fabA-associated membrane remodeling → increased high-temperature growth capacity** and **glpF deletion → improved growth at 43–48°C/upward-shifted optimum**. It does not, by itself, prove a larger full temperature delta unless the minimum-growth endpoint is compared in the same strain and assay (blaby2012experimentalevolutionof pages 7-8, blaby2012experimentalevolutionof pages 1-2, blaby2012experimentalevolutionof pages 5-6).

## 4. Recent research and quantitative evidence

### Salinity mechanisms

A 2023 *Science Advances* phylogenomic study analyzed 13,783 metagenome-assembled genomes, including 11,248 quality-filtered bacterial MAGs spanning 72 phyla. More than 95% of genome clusters were restricted to one of the freshwater, brackish, or marine biome classes. Salinity transitions were associated with more acidic proteomes, increased acidic amino acids—particularly glutamate—and convergent gene-content changes including trehalose and polyamine synthesis functions (jurdzinski2023largescalephylogenomicsof pages 10-11, jurdzinski2023largescalephylogenomicsof pages 11-12, jurdzinski2023largescalephylogenomicsof pages 1-2). These results are authoritative evidence for long-term salinity adaptation, but not direct organism-level salinity growth breadth: environmental detection can miss low-abundance populations, and occurrence does not establish growth under controlled salinity conditions (jurdzinski2023largescalephylogenomicsof pages 10-11, jurdzinski2023largescalephylogenomicsof pages 11-12).

In *P. megaterium* ZS-3, colonies were observed up to 9% NaCl, although growth was severely inhibited there. Relative to 0% NaCl, dry weight increased by 78.97%, 78.17%, and 37.08% at 3%, 5%, and 7% NaCl. Trehalose rose 56.24%, 87.43%, and 466.67%; glutamate rose approximately 374-, 320-, and 150-fold; EPS rose approximately 95- and 150-fold at 5% and 7%; and K⁺ accumulation increased at 5% and 7% NaCl (shi2023mechanismofsalt pages 2-4). This is valuable multi-omic/physiological evidence, but the absence of metabolite-pathway knockouts, supplementation rescue, or transporter perturbations means these should currently be represented as `associated_with salt-stress growth`, not as proven causes of delta breadth.

A 2023 Chemical Reviews synthesis further emphasizes a trade-off: high-salt proteome adaptations and osmolyte accumulation can preserve protein function at high salinity, while salt-adapted proteomes may lose stability at low salinity. In *Thermococcus barophilus*, the cited conditions included optimal growth at 3% NaCl and a minimum salt requirement of 1%; mannosylglycerate accumulated under high-salt stress rather than under optimum conditions (peters2023effectsofcrowding pages 44-47). This supports the concept that mechanisms can move opposite endpoints differently and that “greater high-salt tolerance” need not imply a broader interval.

### Temperature mechanisms

The strongest causal evidence comes from experimental evolution of *E. coli*. Maximum growth temperature increased from approximately 46°C to 48°C, and the optimum shifted from 37°C to above 46°C in one evolved strain. A **fabA** mutation changed fatty-acid composition toward a higher saturated/unsaturated ratio and increased cyclopropane fatty acids; complementation produced an intermediate lipid profile. The evolved strain paid a performance cost below 43°C and had lower biomass yield at 37°C (blaby2012experimentalevolutionof pages 7-8). This is a key expert-level lesson for TraitMech: adaptation can shift a performance curve and impose low-temperature costs without necessarily increasing its complete breadth.

A **glpF** deletion improved growth in the 43–48°C interval and shifted the optimum from 37°C to approximately 43°C (blaby2012experimentalevolutionof pages 1-2, blaby2012experimentalevolutionof pages 5-6). Again, this is direct evidence for an upper-end growth mechanism, but delta expansion requires lower-endpoint data.

For cold growth, *P. arcticus* showed increased unsaturated membrane lipids and induction of a fatty-acid desaturase and cold-acclimation factors during active low-temperature growth (bergholz2009psychrobacterarcticus2734 pages 1-2). The evidence supports homeoviscous adaptation as a mechanistic intermediate but is less decisive than a targeted desaturase knockout/rescue experiment for assigning a causal breadth edge.

A 2024 food-microbiology review reported LAB optimal-growth ranges commonly around 30–45°C, growth at 15°C but not 7°C in the discussed examples, harmful heat stress above 50°C, and induction of DnaK, GroEL/GroES, small heat-shock proteins, cold-shock proteins, and lipid remodeling. These values vary by strain and frequently mix growth, viability, and transient survival endpoints; they should not be merged into one taxon-independent delta (sionek2024theimpactof pages 3-5).

### pH mechanisms and ecological breadth

TolC provides unusually clear growth-specific evidence. Deleting **tolC** slowed *E. coli* growth at pH 4.5–6.0 but had no detected growth effect at pH 6.5–9.0; plasmid complementation restored growth at pH 4.5 (deininger2011arequirementof pages 1-2, deininger2011arequirementof pages 3-4). TolC also influences Gad expression and extreme-acid survival, but Gad overexpression did not rescue moderate-acid growth in the tolC mutant. The graph should therefore separate `TolC → moderate-acid growth` from `TolC/Gad → pH 2 survival` (deininger2011arequirementof pages 1-2, deininger2011arequirementof pages 3-4).

At external pH 2.5, glutamate-dependent GadA/GadB–GadC activity raised intracellular pH from about 3.6 to 4.2, while AdiA–AdiC raised it to about 4.7 and reversed membrane potential. These experiments concern transient extreme-acid survival, not growth (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 2-4).

Recent ecological work demonstrates why occurrence-derived pH breadth should remain separate. A 2024 study analyzed 425 ammonia-oxidizing archaeal phylotypes across 47 soils spanning approximately pH 3.5–8.7. It classified 91 specialists, 87 generalists, and 247 putative specialists. Generalists were favored at pH 6.0 and 7.5 after disturbance, whereas specialists were advantaged at pH 4.5 (gubryrangin2024nichebreadthspecialization pages 5-8, gubryrangin2024nichebreadthspecialization pages 1-2, gubryrangin2024nichebreadthspecialization pages 4-5). However, the modified Levins index was based on distributions across soils, confounding environmental factors could not be excluded, and conclusions differed for active versus resident populations (gubryrangin2024nichebreadthspecialization pages 8-10, gubryrangin2024nichebreadthspecialization pages 5-8, gubryrangin2024nichebreadthspecialization pages 2-3). These findings should inform interpretation, not become direct molecular edges for “METPO:1000534.”

## 5. Current applications and implementations

- **Industrial strain engineering:** Endpoint-specific mechanisms can be targeted to build microbial cell factories that remain productive across temperature, pH, salinity, product-toxicity, or feedstock fluctuations. The evolved-*E. coli* example shows both the potential and the need to test low-end trade-offs.
- **Food fermentation and preservation:** LAB selection already uses growth/viability profiles across temperature, acid, salt, and storage conditions. Separate growth from survival and cross-protection when encoding traits (sionek2024theimpactof pages 3-5).
- **High-salt fermentation and green chemistry:** Compatible-solute strategies and salt-adapted enzymes support high-salt bioprocesses, but organismal growth breadth should not be inferred from enzyme stability alone.
- **Bioleaching and bioremediation:** Extremophiles enable operation under acidic, alkaline, saline, or hot conditions. The trait could support strain matching to process windows, provided limits are measured using process-relevant media.
- **Climate and ecosystem modeling:** One-dimensional growth breadth can parameterize laboratory fundamental-niche models, whereas occurrence-derived specialist/generalist indices characterize realized distributions. Combining them without an explicit mapping risks category errors (bebber2022specialistsgeneralistsand pages 3-4, bell2021manyroadsto pages 17-18).

## 6. Ontology-grounding recommendations

### Safe now

- Preserve the identifier exactly as **“METPO:1000534”**.
- Preserve the supplied parent **METPO:1000059**.
- Use gene symbols as labels until organism-specific database records are resolved.
- Use DOI identifiers as evidence references.

### Resolve during YAML curation

- Map environmental variables and media to ENVO only after verifying the exact term.
- Map chemicals such as NaCl, K⁺, glutamate, trehalose, proline, and arginine to ChEBI through an ontology lookup; do not assign IDs from memory.
- Map processes such as growth, pH homeostasis, protein folding, membrane organization, and responses to temperature/osmotic stress to verified GO records.
- Ground proteins to strain-specific UniProt accessions only after selecting the exact organism and allele.
- Ground reactions such as glutamate or arginine decarboxylation to Rhea/EC only after checking substrate, product, and direction.
- Use NCBITaxon identifiers at strain level where available; do not collapse evolved laboratory strains into a species-level mechanism without genotype context.

## 7. Claims not yet ready for TraitMech curation

1. **Compatible solute → wider salinity delta.** Current *Priestia* data are concentration-response correlations, not perturbation evidence (shi2023mechanismofsalt pages 2-4, shi2023mechanismofsalt pages 1-2).
2. **Proteome acidification → wider salinity delta.** The 2023 phylogenomic signal concerns ancient cross-biome adaptation and species distributions, not measured growth limits (jurdzinski2023largescalephylogenomicsof pages 10-11, jurdzinski2023largescalephylogenomicsof pages 11-12).
3. **Gad/Adi systems → wider pH-growth range.** The cited experiments demonstrate survival at pH 2–2.5, not replication (richard2004escherichiacoliglutamate pages 1-2, li2024responseofescherichia pages 2-4).
4. **Heat-shock or cold-shock expression → wider temperature delta.** Expression during stress or acclimation is insufficient without perturbation and both endpoint measurements.
5. **Higher Tmax → larger delta.** This follows only if Tmin is measured and unchanged; evolved strains can incur low-temperature costs (blaby2012experimentalevolutionof pages 7-8).
6. **Environmental occurrence → growth-supporting limit.** Dormancy, relic DNA, dispersal, low abundance, and biotic interactions invalidate this shortcut (bell2021manyroadsto pages 17-18, jurdzinski2023largescalephylogenomicsof pages 10-11).
7. **Enzyme stability range → organismal growth range.** An extremozymal activity interval is not a cellular growth phenotype.
8. **Different studies’ minima and maxima → one delta.** Endpoints must come from the same strain, medium, readout, and threshold.
9. **Exact Psychrobacter breadth without source reconciliation.** Retrieved excerpts gave both −6 to 22°C and −10 to 28°C summaries; verify the primary methods before encoding a numerical delta (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 1-2).

## 8. DOI-first bibliography

1. **Shi L. et al.** “Mechanism of Salt Tolerance and Plant Growth Promotion in *Priestia megaterium* ZS-3 Revealed by Cellular Metabolism and Whole-Genome Studies.” *International Journal of Molecular Sciences* 24, 15751. **October 2023.** DOI: [10.3390/ijms242115751](https://doi.org/10.3390/ijms242115751). (shi2023mechanismofsalt pages 2-4, shi2023mechanismofsalt pages 1-2)
2. **Jurdzinski K.T. et al.** “Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.” *Science Advances* 9. **May 2023.** DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059). (jurdzinski2023largescalephylogenomicsof pages 10-11, jurdzinski2023largescalephylogenomicsof pages 11-12, jurdzinski2023largescalephylogenomicsof pages 1-2)
3. **Peters J. et al.** “Effects of Crowding and Cosolutes on Biomolecular Function at Extreme Environmental Conditions.” *Chemical Reviews* 123:13441–13488. **November 2023.** DOI: [10.1021/acs.chemrev.3c00432](https://doi.org/10.1021/acs.chemrev.3c00432). (peters2023effectsofcrowding pages 44-47)
4. **Sionek B. et al.** “The Impact of Physicochemical Conditions on Lactic Acid Bacteria Survival in Food Products.” *Fermentation* 10, 298. **June 2024.** DOI: [10.3390/fermentation10060298](https://doi.org/10.3390/fermentation10060298). (sionek2024theimpactof pages 3-5)
5. **Li Z., Huang Z., Gu P.** “Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.” *Microorganisms* 12, 1774. **August 2024.** DOI: [10.3390/microorganisms12091774](https://doi.org/10.3390/microorganisms12091774). (li2024responseofescherichia pages 2-4)
6. **Gubry-Rangin C. et al.** “Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change.” *ISME Journal* 18. **2024.** DOI: [10.1093/ismejo/wrae183](https://doi.org/10.1093/ismejo/wrae183). (gubryrangin2024nichebreadthspecialization pages 10-11, gubryrangin2024nichebreadthspecialization pages 1-2, gubryrangin2024nichebreadthspecialization pages 4-5, gubryrangin2024nichebreadthspecialization pages 2-3)
7. **La Motta L.M. et al.** “Diversity of lipid profiles of Symbiodiniaceae under temperature and nutrient stress.” *Frontiers in Protistology* 2. **February 2024.** DOI: [10.3389/frpro.2024.1320353](https://doi.org/10.3389/frpro.2024.1320353). (motta2024diversityoflipid pages 1-2)
8. **Blaby I.K. et al.** “Experimental Evolution of a Facultative Thermophile from a Mesophilic Ancestor.” *Applied and Environmental Microbiology* 78:144–155. **January 2012.** DOI: [10.1128/AEM.05773-11](https://doi.org/10.1128/AEM.05773-11). (blaby2012experimentalevolutionof pages 7-8, blaby2012experimentalevolutionof pages 1-2, blaby2012experimentalevolutionof pages 5-6, blaby2012experimentalevolutionof pages 4-5)
9. **Deininger K.N.W. et al.** “A Requirement of TolC and MDR Efflux Pumps for Acid Adaptation and GadAB Induction in *Escherichia coli*.” *PLoS ONE* 6:e18960. **April 2011.** DOI: [10.1371/journal.pone.0018960](https://doi.org/10.1371/journal.pone.0018960). (deininger2011arequirementof pages 1-2, deininger2011arequirementof pages 3-4)
10. **Bergholz P.W., Bakermans C., Tiedje J.M.** “*Psychrobacter arcticus* 273-4 Uses Resource Efficiency and Molecular Motion Adaptations for Subzero Temperature Growth.” *Journal of Bacteriology* 191:2340–2352. **April 2009.** DOI: [10.1128/JB.01377-08](https://doi.org/10.1128/JB.01377-08). (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 1-2)
11. **Richard H., Foster J.W.** “*Escherichia coli* Glutamate- and Arginine-Dependent Acid Resistance Systems Increase Internal pH and Reverse Transmembrane Potential.” *Journal of Bacteriology* 186:6032–6041. **September 2004.** DOI: [10.1128/JB.186.18.6032-6041.2004](https://doi.org/10.1128/JB.186.18.6032-6041.2004). (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 2-4)
12. **Bebber D.P., Chaloner T.M.** “Specialists, generalists and the shape of the ecological niche in fungi.” *New Phytologist* 234:345–349. **February 2022.** DOI: [10.1111/nph.18005](https://doi.org/10.1111/nph.18005). (bebber2022specialistsgeneralistsand pages 3-4)
13. **Bell T.H., Bell T.** “Many roads to bacterial generalism.” *FEMS Microbiology Ecology* 97. **2021.** DOI: [10.1093/femsec/fiaa240](https://doi.org/10.1093/femsec/fiaa240). (bell2021manyroadsto pages 17-18, bell2021manyroadsto pages 27-28)
14. **Gunde-Cimerman N., Plemenitaš A., Oren A.** “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews* 42:353–375. **May 2018.** DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). Supplied existing evidence; full text was not available through retrieval.
15. **Tolner B., Poolman B., Konings W.N.** “Adaptation of microorganisms and their transport systems to high temperatures.” *Comparative Biochemistry and Physiology Part A* 118:423–428. **November 1997.** DOI: [10.1016/S0300-9629(97)00003-0](https://doi.org/10.1016/S0300-9629(97)00003-0). Supplied existing evidence; full text was not available through retrieval.

## Final curation recommendation

Retain **“METPO:1000534”** as a compact derived descriptor connected to explicit lower and upper growth-limit observations. For the first TraitMech revision, curate the arithmetic/assay scaffold and only the direct endpoint mechanisms supported by perturbation—principally the evolved-*E. coli* temperature examples and TolC-dependent moderate-acid growth. Add salinity compatible-solute, proteome-remodeling, chaperone, and extreme-acid-survival mechanisms as candidate or contextual nodes with uncertainty flags, not as established causes of delta breadth.

References

1. (bergholz2009psychrobacterarcticus2734 pages 1-1): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

2. (bergholz2009psychrobacterarcticus2734 pages 1-2): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

3. (blaby2012experimentalevolutionof pages 7-8): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

4. (blaby2012experimentalevolutionof pages 4-5): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

5. (shi2023mechanismofsalt pages 2-4): Lina Shi, Xiaoxia Zhu, Ting Qian, Jiazhou Du, Yuanyuan Du, and Jianren Ye. Mechanism of salt tolerance and plant growth promotion in priestia megaterium zs-3 revealed by cellular metabolism and whole-genome studies. International Journal of Molecular Sciences, 24:15751, Oct 2023. URL: https://doi.org/10.3390/ijms242115751, doi:10.3390/ijms242115751. This article has 23 citations.

6. (shi2023mechanismofsalt pages 1-2): Lina Shi, Xiaoxia Zhu, Ting Qian, Jiazhou Du, Yuanyuan Du, and Jianren Ye. Mechanism of salt tolerance and plant growth promotion in priestia megaterium zs-3 revealed by cellular metabolism and whole-genome studies. International Journal of Molecular Sciences, 24:15751, Oct 2023. URL: https://doi.org/10.3390/ijms242115751, doi:10.3390/ijms242115751. This article has 23 citations.

7. (bebber2022specialistsgeneralistsand pages 3-4): Daniel P. Bebber and Thomas M. Chaloner. Specialists, generalists and the shape of the ecological niche in fungi. New Phytologist, 234:345-349, Feb 2022. URL: https://doi.org/10.1111/nph.18005, doi:10.1111/nph.18005. This article has 43 citations and is from a highest quality peer-reviewed journal.

8. (bell2021manyroadsto pages 17-18): Terrence H Bell and Thomas Bell. Many roads to bacterial generalism. FEMS microbiology ecology, Nov 2021. URL: https://doi.org/10.1093/femsec/fiaa240, doi:10.1093/femsec/fiaa240. This article has 70 citations and is from a peer-reviewed journal.

9. (bell2021manyroadsto pages 27-28): Terrence H Bell and Thomas Bell. Many roads to bacterial generalism. FEMS microbiology ecology, Nov 2021. URL: https://doi.org/10.1093/femsec/fiaa240, doi:10.1093/femsec/fiaa240. This article has 70 citations and is from a peer-reviewed journal.

10. (blaby2012experimentalevolutionof pages 5-6): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

11. (blaby2012experimentalevolutionof pages 1-2): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

12. (deininger2011arequirementof pages 1-2): Kari N. W. Deininger, Akina Horikawa, Ryan D. Kitko, Ryoko Tatsumi, Judah L. Rosner, Masaaki Wachi, and Joan L. Slonczewski. A requirement of tolc and mdr efflux pumps for acid adaptation and gadab induction in escherichia coli. PLoS ONE, 6:e18960, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018960, doi:10.1371/journal.pone.0018960. This article has 84 citations and is from a peer-reviewed journal.

13. (deininger2011arequirementof pages 3-4): Kari N. W. Deininger, Akina Horikawa, Ryan D. Kitko, Ryoko Tatsumi, Judah L. Rosner, Masaaki Wachi, and Joan L. Slonczewski. A requirement of tolc and mdr efflux pumps for acid adaptation and gadab induction in escherichia coli. PLoS ONE, 6:e18960, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018960, doi:10.1371/journal.pone.0018960. This article has 84 citations and is from a peer-reviewed journal.

14. (richard2004escherichiacoliglutamate pages 1-2): Hope Richard and John W. Foster. Escherichia coli glutamate- and arginine-dependent acid resistance systems increase internal ph and reverse transmembrane potential. Journal of Bacteriology, 186:6032-6041, Sep 2004. URL: https://doi.org/10.1128/jb.186.18.6032-6041.2004, doi:10.1128/jb.186.18.6032-6041.2004. This article has 493 citations and is from a peer-reviewed journal.

15. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

16. (sionek2024theimpactof pages 3-5): Barbara Sionek, Aleksandra Szydłowska, Monika Trząskowska, and Danuta Kołożyn-Krajewska. The impact of physicochemical conditions on lactic acid bacteria survival in food products. Fermentation, 10:298, Jun 2024. URL: https://doi.org/10.3390/fermentation10060298, doi:10.3390/fermentation10060298. This article has 139 citations.

17. (richard2004escherichiacoliglutamate pages 2-4): Hope Richard and John W. Foster. Escherichia coli glutamate- and arginine-dependent acid resistance systems increase internal ph and reverse transmembrane potential. Journal of Bacteriology, 186:6032-6041, Sep 2004. URL: https://doi.org/10.1128/jb.186.18.6032-6041.2004, doi:10.1128/jb.186.18.6032-6041.2004. This article has 493 citations and is from a peer-reviewed journal.

18. (motta2024diversityoflipid pages 1-2): Laura M. La Motta, Matthew P. Padula, Brigitte Sommer, Emma F. Camp, and Jennifer L. Matthews. Diversity of lipid profiles of symbiodiniaceae under temperature and nutrient stress. Frontiers in Protistology, Feb 2024. URL: https://doi.org/10.3389/frpro.2024.1320353, doi:10.3389/frpro.2024.1320353. This article has 14 citations.

19. (jurdzinski2023largescalephylogenomicsof pages 10-11): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

20. (jurdzinski2023largescalephylogenomicsof pages 11-12): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

21. (jurdzinski2023largescalephylogenomicsof pages 1-2): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

22. (peters2023effectsofcrowding pages 44-47): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 49 citations and is from a highest quality peer-reviewed journal.

23. (gubryrangin2024nichebreadthspecialization pages 5-8): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.

24. (gubryrangin2024nichebreadthspecialization pages 1-2): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.

25. (gubryrangin2024nichebreadthspecialization pages 4-5): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.

26. (gubryrangin2024nichebreadthspecialization pages 8-10): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.

27. (gubryrangin2024nichebreadthspecialization pages 2-3): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.

28. (gubryrangin2024nichebreadthspecialization pages 10-11): Cécile Gubry-Rangin, Axel Aigle, Leonel Herrera-Alsina, Lesley T Lancaster, and James I Prosser. Niche breadth specialization impacts ecological and evolutionary adaptation following environmental change. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae183, doi:10.1093/ismejo/wrae183. This article has 26 citations.