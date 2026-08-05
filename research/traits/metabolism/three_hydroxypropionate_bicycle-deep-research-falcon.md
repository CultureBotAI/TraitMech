---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:07:34.358868'
end_time: '2026-08-04T07:14:56.996802'
duration_seconds: 442.64
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: 3-hydroxypropionate bicycle
  trait_identifier: traitmech:000023
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: three_hydroxypropionate_bicycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway in which two molecules of bicarbonate
    are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It
    is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
  parent_traits: traitmech:000019
  synonyms: 3-hydroxypropionate cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate\
    \ bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert include the 3-hydroxypropionate pathway among autotrophic\
    \ carbon-fixation strategies.)"
  causal_graph_summary: 'three_hp_bicycle_chloroflexus: 14 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate bicycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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
- **Trait label:** 3-hydroxypropionate bicycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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


# TraitMech curation report: 3-hydroxypropionate bicycle

## Record and scope

- **Trait:** 3-hydroxypropionate bicycle
- **Identifier:** `traitmech:000023`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Synonym:** 3-hydroxypropionate cycle
- **Parent:** `traitmech:000019`

This trait should represent the **complete bacterial Fuchs–Holo 3-hydroxypropionate bicycle**: an autotrophic, cytosolic carbon-assimilation capacity in which two linked cycles fix inorganic carbon through CoA-bound intermediates and generate pyruvate for central metabolism. The first cycle regenerates acetyl-CoA while producing glyoxylate; the second assimilates glyoxylate and again regenerates acetyl-CoA. Overall, three bicarbonate molecules yield one pyruvate, with reported consumption of five ATP and six NADPH at the pathway level. Thirteen enzymes catalyze 19 reactions because several enzymes are multifunctional. (berg2011ecologicalaspectsof pages 7-8, min2022crystalstructureof pages 1-2, hugler2011beyondthecalvin pages 9-10)

The canonical experimentally characterized organism is the filamentous anoxygenic phototroph *Chloroflexus aurantiacus*. It preferentially grows photoheterotrophically but can grow autotrophically in laboratory cultures and hot-spring microbial mats. The bicycle also permits co-assimilation of fermentation products such as acetate, propionate, and succinate and contains no intrinsically oxygen-sensitive step, although a B12-dependent methylmalonyl-CoA mutase may be vulnerable under combined high oxygen and light. (berg2011ecologicalaspectsof pages 8-9, berg2011ecologicalaspectsof pages 7-8)

### Boundary cases

1. **Exclude the archaeal 3-hydroxypropionate/4-hydroxybutyrate cycle.** Its acetyl-CoA-to-succinyl-CoA segment is formally related, but its regeneration arm converts succinyl-CoA through 4-hydroxybutyrate and acetoacetyl-CoA to two acetyl-CoA molecules. It lacks the glyoxylate-assimilation half of the bacterial bicycle and evolved with substantially different enzymes. (berg2011ecologicalaspectsof pages 7-8, hugler2011beyondthecalvin pages 9-10)
2. **Exclude isolated 3HP enzymes or partial modules.** Malonyl-CoA reductase, propionyl-CoA synthase, or related reactions can support assimilation or production of organic compounds without conferring autotrophy. In 27 Actinobacteriota MAGs, average pathway completeness was only 68.6%, and the authors favored organic-substrate assimilation rather than a functional bicycle. (garritano2022carbonfixationpathways pages 2-3)
3. **Do not equate genomic prediction with demonstrated physiology.** Comparative genomics identified candidate complete pathways beyond Chloroflexota—including Ga0077523, Burkholderiaceae, and Gemmatimonadota MAGs—but these remain predictions unless growth, isotope incorporation, flux, or enzyme evidence is available. (garritano2022carbonfixationpathways pages 2-3)
4. **Exclude synthetic HOPAC and Lcm routes.** They borrow 3HP chemistry but are new-to-nature pathways with different topology and products. (schulzmirbach2024newtonatureco2dependentacetylcoa pages 1-2, mclean2023exploringalternativepathways pages 1-2)

## Candidate nodes grouped by type

### Trait and pathway modules

- `traitmech:000023` — 3-hydroxypropionate bicycle
- Glyoxylate-synthesis cycle — label-only module
- Glyoxylate-assimilation cycle — label-only module
- Autotrophic bicarbonate fixation — candidate biological process
- Photoautotrophic growth — candidate phenotype
- Mixotrophic/photoheterotrophic co-assimilation — candidate associated phenotype, not constitutive evidence of the complete bicycle

### Organisms and environments

- *Chloroflexus aurantiacus* — canonical reference taxon; ground to its verified NCBITaxon record during implementation
- *Roseiflexus castenholzii* — source of directly characterized mesaconyl-CoA C1–C4 transferase; taxon-specific supporting evidence
- Chloroflexaceae / Chloroflexota — historically associated clade
- Filamentous anoxygenic phototroph — organismal phenotype/class
- Hot-spring microbial mat — candidate ENVO-grounded environment
- Light — experimental/environmental energy input
- Anoxic or low-oxygen phototrophic conditions — context node
- Oxygen — pathway broadly tolerant, but potentially detrimental to the radical B12 step under intense light

### Chemicals and cofactors

Conservatively ground common metabolites to verified ChEBI records during YAML implementation: bicarbonate, carbon dioxide, acetyl-CoA, malonyl-CoA, 3-hydroxypropionate, propionyl-CoA, methylmalonyl-CoA, succinyl-CoA, glyoxylate, pyruvate, ATP, ADP, NADPH, NADP+, biotin, and cobalamin. Specialized stereochemical intermediates should remain label-only until registry records are checked:

- (S)-malyl-CoA
- (2R,3S)-β-methylmalyl-CoA
- mesaconyl-C1-CoA
- mesaconyl-C4-CoA
- (S)-citramalyl-CoA
- 3-hydroxypropionyl-CoA
- acrylyl-CoA

### Enzymes, proteins, and complexes

- Biotin-dependent acetyl-CoA/propionyl-CoA carboxylase
- Malonyl-CoA reductase (MCR), bifunctional
- Propionyl-CoA synthase (PCS), trifunctional
- Methylmalonyl-CoA epimerase
- B12-dependent methylmalonyl-CoA mutase
- Succinyl-CoA-processing enzymes leading to (S)-malyl-CoA; retain as a composite module unless primary reaction-level evidence is attached
- Malyl-CoA/β-methylmalyl-CoA/citramalyl-CoA lyase (MMC lyase), multifunctional
- β-methylmalyl-CoA dehydratase / mesaconyl-CoA hydratase, exact naming and direction to be registry-verified
- Mesaconyl-CoA C1–C4 CoA transferase (MCT; also called mesaconyl-CoA isomerase in pathway-prediction literature)

The retrieved evidence does not establish stable *C. aurantiacus* locus tags or UniProt accessions for all enzymes. These should therefore not be guessed. The 2022 *R. castenholzii* structure identifies a functional MCT dimer, a 2.5 Å structure, a Rossmann-fold-containing architecture, and catalytic residues Asp165, Arg47, and Arg314′. (min2022crystalstructureof pages 1-2)

### Molecular functions and localization

- Acetyl-CoA carboxylase activity
- Propionyl-CoA carboxylase activity
- Malonyl-CoA reductase activity
- Propionyl-CoA synthase activity
- Carbon–carbon lyase activity
- Intramolecular CoA-transfer activity
- Enoyl-CoA hydratase/dehydratase activity
- Cytosolic soluble metabolism — plausible default, but localization should be curated only where an organism-specific source explicitly establishes it

## Candidate causal edges

The following compact scaffold distinguishes directly assigned enzyme reactions from review-level composite conversions.

| subject | predicate | object | catalyst/module | evidence strength | DOI |
|---|---|---|---|---|---|
| bicarbonate + acetyl-CoA | enables carboxylation to | malonyl-CoA | biotin-dependent acetyl-CoA/propionyl-CoA carboxylase; glyoxylate synthesis cycle | review-supported composite (berg2011ecologicalaspectsof pages 7-8, hugler2011beyondthecalvin pages 9-10) | 10.1128/AEM.02473-10 |
| malonyl-CoA | is reduced to | 3-hydroxypropionate | malonyl-CoA reductase (MCR) | review-supported direct enzyme assignment (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712 |
| 3-hydroxypropionate | is converted to | propionyl-CoA | propionyl-CoA synthase (PCS); trifunctional | review-supported direct enzyme assignment (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712 |
| bicarbonate + propionyl-CoA | enables carboxylation/rearrangement to | succinyl-CoA | biotin-dependent acetyl-CoA/propionyl-CoA carboxylase + downstream rearrangement; glyoxylate synthesis cycle | review-supported composite (berg2011ecologicalaspectsof pages 7-8) | 10.1128/AEM.02473-10 |
| succinyl-CoA | is converted to | (S)-malyl-CoA | glyoxylate synthesis cycle | coarse pathway-level support (berg2011ecologicalaspectsof pages 7-8) | 10.1128/AEM.02473-10 |
| (S)-malyl-CoA | is cleaved to | glyoxylate + acetyl-CoA | MMC lyase | review-supported direct enzyme assignment (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712 |
| glyoxylate + propionyl-CoA | condense to form | β-methylmalyl-CoA | MMC lyase; glyoxylate assimilation cycle | review-supported direct enzyme assignment, product naming simplified from review wording (hugler2011beyondthecalvin pages 9-10, berg2011ecologicalaspectsof pages 7-8) | 10.1146/annurev-marine-120709-142712 |
| β-methylmalyl-CoA | is converted via | mesaconyl-CoA | glyoxylate assimilation cycle | coarse pathway-level support (berg2011ecologicalaspectsof pages 7-8) | 10.1128/AEM.02473-10 |
| mesaconyl-C1-CoA | is intramolecularly converted to | mesaconyl-C4-CoA | mesaconyl-CoA C1-C4 CoA transferase (MCT) | direct structural/biochemical characterization in Roseiflexus castenholzii; taxon-specific support for homologous 3HP-cycle step (min2022crystalstructureof pages 1-2) | 10.3389/fmicb.2022.923367 |
| mesaconyl-CoA | is converted to | citramalyl-CoA | glyoxylate assimilation cycle; includes hydratase/CoA-transfer steps | coarse pathway-level support (hugler2011beyondthecalvin pages 9-10, berg2011ecologicalaspectsof pages 7-8, min2022crystalstructureof pages 1-2) | 10.1128/AEM.02473-10 |
| citramalyl-CoA | is cleaved to | pyruvate + acetyl-CoA | MMC lyase | review-supported direct enzyme assignment (hugler2011beyondthecalvin pages 9-10) | 10.1146/annurev-marine-120709-142712 |
| 3-hydroxypropionate bicycle | fixes | 3 bicarbonate to yield 1 pyruvate | two linked cycles; 19 reactions catalyzed by 13 enzymes | review-supported pathway stoichiometry (berg2011ecologicalaspectsof pages 7-8, min2022crystalstructureof pages 1-2, hugler2011beyondthecalvin pages 9-10) | 10.1128/AEM.02473-10 |


*Table: This table summarizes compact, curation-ready causal edges for the natural 3-hydroxypropionate bicycle, separating coarse review-supported pathway conversions from the more directly characterized mesaconyl-CoA transferase step. It is useful as a starting scaffold for TraitMech graph assembly and uncertainty marking.*

### Additional edge-level evidence and curator notes

| Proposed triple | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| 3HP bicycle —has_part→ glyoxylate-synthesis cycle | DOI:10.1128/AEM.02473-10 | “In the first glyoxylate synthesis cycle, acetyl-CoA is carboxylated to malonyl-CoA…” | Strong pathway-level edge. (berg2011ecologicalaspectsof pages 7-8) |
| 3HP bicycle —has_part→ glyoxylate-assimilation cycle | DOI:10.1128/AEM.02473-10 | “A second glyoxylate assimilation cycle starts with glyoxylate addition to propionyl-CoA…” | Strong pathway-level edge. (berg2011ecologicalaspectsof pages 7-8) |
| acetyl-CoA/propionyl-CoA carboxylase —uses_substrate→ bicarbonate | DOI:10.1128/AEM.02473-10 | The carboxylase “uses bicarbonate as an active inorganic carbon species.” | Strong; distinguish bicarbonate from generic CO2 in reaction nodes. (berg2011ecologicalaspectsof pages 7-8) |
| biotin —cofactor_for→ acetyl-CoA/propionyl-CoA carboxylase | DOI:10.1128/AEM.02473-10 | “biotin-dependent acetyl-CoA/propionyl-CoA carboxylase” | Strong. (berg2011ecologicalaspectsof pages 7-8) |
| acetyl-CoA/propionyl-CoA carboxylase —promotes→ thermodynamic directionality of fixation | DOI:10.1128/AEM.02473-10 | The carboxylase is “virtually irreversible.” | Curate only if TraitMech supports thermodynamic-property nodes. (berg2011ecologicalaspectsof pages 7-8) |
| MCR —catalyzes→ malonyl-CoA to 3-hydroxypropionate | DOI:10.1146/annurev-marine-120709-142712 | “Malonyl-CoA reductase catalyzes the two-step reduction of malonyl-CoA to 3-hydroxypropionate.” | Strong enzyme assignment; represent as two reactions only after consulting the primary biochemical paper. (hugler2011beyondthecalvin pages 9-10) |
| PCS —catalyzes→ 3-hydroxypropionate to propionyl-CoA | DOI:10.1146/annurev-marine-120709-142712 | “the trifunctional enzyme propionyl-CoA synthase transforms 3-hydroxypropionate to propionyl-CoA.” | Strong composite edge; activation, dehydration, and reduction substeps require primary evidence. (hugler2011beyondthecalvin pages 9-10) |
| MMC lyase —cleaves→ malyl-CoA to acetyl-CoA plus glyoxylate | DOI:10.1146/annurev-marine-120709-142712 | “the cleavage of malyl-CoA to acetyl-CoA and glyoxylate” | Strong direct enzyme assignment. (hugler2011beyondthecalvin pages 9-10) |
| MMC lyase —condenses→ glyoxylate plus propionyl-CoA | DOI:10.1146/annurev-marine-120709-142712 | “the condensation of glyoxylate with propionyl-CoA” | Strong catalyst assignment, but the review excerpt calls the product “methylmalonyl-CoA,” whereas pathway descriptions identify β-methylmalyl-CoA. Use the stereospecific product only after checking the primary paper. (hugler2011beyondthecalvin pages 9-10) |
| MCT —converts→ mesaconyl-C1-CoA to mesaconyl-C4-CoA | DOI:10.3389/fmicb.2022.923367 | MCT “specifically catalyzes the reversible transformation of mesaconyl-C1-CoA to mesaconyl-C4-CoA.” | Direct structural/mechanistic evidence in *R. castenholzii*; taxon-specific but highly curatable. (min2022crystalstructureof pages 1-2) |
| MCT —forms_complex→ homodimer | DOI:10.3389/fmicb.2022.923367 | “Two MCT subunits are cross interlocked…to form a functional dimer in solution.” | Direct structural evidence; optional mechanistic node. (min2022crystalstructureof pages 1-2) |
| Asp165/Arg47/Arg314′ —contributes_to→ MCT catalysis/substrate binding | DOI:10.3389/fmicb.2022.923367 | Asp165, Arg47, and a water molecule support catalysis; Arg314′ changes conformation on product binding. | Useful fine-grained protein mechanism, but attach to the *R. castenholzii* protein rather than a generic enzyme class. (min2022crystalstructureof pages 1-2) |
| MMC lyase —cleaves→ citramalyl-CoA to pyruvate plus acetyl-CoA | DOI:10.1146/annurev-marine-120709-142712 | “the cleavage of citramalyl-CoA to pyruvate and acetyl-CoA” | Strong direct enzyme assignment. (hugler2011beyondthecalvin pages 9-10) |
| complete 3HP bicycle —fixes→ three bicarbonate per pyruvate | DOI:10.3389/fmicb.2022.923367 | “absorbs three molecules of bicarbonate and produces one molecule of pyruvate” | Strong pathway stoichiometry. (min2022crystalstructureof pages 1-2) |
| complete 3HP bicycle —consumes→ five ATP and six NADPH per pyruvate | DOI:10.3389/fmicb.2022.923367 | “…with consumption of 5 molecules of ATP and 6 molecules of NADPH.” | Strong review statement tracing to primary pathway work. Distinguish this chemical stoichiometry from the “seven ATP equivalents” accounting below. (min2022crystalstructureof pages 1-2) |
| pyruvate-to-triose-phosphate assimilation —requires→ three additional ATP | DOI:10.1128/AEM.02473-10 | “seven ATP equivalents for the synthesis of pyruvate and three additional ATPs for triose phosphate.” | The difference from five ATP molecules reflects ATP-equivalent accounting; do not merge these values without annotation. (berg2011ecologicalaspectsof pages 7-8) |
| 3HP bicycle —enables→ co-assimilation of acetate/propionate/succinate | DOI:10.1128/AEM.02473-10 | The 19-step route supports “coassimilation of fermentation products (acetate, propionate, succinate).” | Strong physiological association in *C. aurantiacus*; not diagnostic by itself. (berg2011ecologicalaspectsof pages 8-9) |
| absence of oxygen-sensitive steps —supports→ oxygen tolerance | DOI:10.1128/AEM.02473-10 | The pathway “is oxygen-tolerant and lacks oxygen-sensitive steps.” | Strong pathway-level property, with a caveat for light-plus-O2 damage to radical B12 chemistry. (berg2011ecologicalaspectsof pages 8-9, berg2011ecologicalaspectsof pages 7-8) |
| complete 3HP gene complement —supports→ predicted 3HP bicycle | DOI:10.1093/pnasnexus/pgac226 | The study used mesaconyl-CoA isomerase as a key enzyme and an 82% completeness threshold; 21 MAGs were detected. | Genomic inference only; phenotype remains uncertain. (garritano2022carbonfixationpathways pages 2-3) |

## Ontology-grounding recommendations

### Safe high-level candidates

- **Biological process:** carbon fixation — use the current GO carbon-fixation term after registry lookup.
- **Molecular functions:** acetyl-CoA carboxylase, propionyl-CoA carboxylase, malonyl-CoA reductase, and methylmalonyl-CoA mutase activities — map to GO/EC only after confirming substrate specificity and enzyme architecture.
- **Chemicals:** use ChEBI for common metabolites and cofactors listed above.
- **Taxa:** use NCBITaxon for *C. aurantiacus*, *R. castenholzii*, Chloroflexaceae, and Chloroflexota.
- **Environment:** use ENVO for hot spring and microbial mat; use a composite association if no single term captures “hot-spring microbial mat.”

### Identifier cautions

- Do not assign the same EC or GO molecular-function term indiscriminately to the multifunctional MCR, PCS, and MMC proteins; one protein may need several activity annotations.
- “Mesaconyl-CoA isomerase” and “mesaconyl-CoA C1–C4 CoA transferase” may denote the same pathway-defining chemistry in different sources, but synonymy should be confirmed before merging.
- Do not invent UniProt or locus-tag identifiers from enzyme names. Retrieve these from the *C. aurantiacus* reference proteome and verify experimentally studied sequences.
- Preserve stereochemistry for β-methylmalyl-CoA, malyl-CoA, citramalyl-CoA, and mesaconyl-CoA isomers.

## Recent developments and applications

### Expanded predicted taxonomic distribution

A 2022 survey examined **52,515 MAGs** and found carbon-fixation pathways in **1,007 bacterial and archaeal genomes**. For the 3HP bicycle, it reported candidate pathways beyond Chloroflexota, including Proteobacteria and Gemmatimonadota. The pathway model used 26 reactions, an 82% completeness threshold, and mesaconyl-CoA isomerase as a key marker. These findings revise the older view that the trait is restricted to Chloroflexaceae, but remain predominantly genomic predictions. (garritano2022carbonfixationpathways pages 2-3)

### Structural mechanism and enzyme engineering

The 2022 MCT study resolved the *R. castenholzii* enzyme at **2.5 Å**, identified its functional dimer and catalytic residues, and explicitly proposed enzyme engineering and biosynthetic production of fine chemicals as applications. This is the strongest recent source for a fine-grained protein-mechanism subgraph. (min2022crystalstructureof pages 1-2)

### 2023 synthetic carbon fixation

HOPAC is not the natural trait, but it demonstrates current exploitation of related hydroxypropionyl-CoA chemistry. The 2023 system used **11 enzymes from six organisms**, converted approximately **3.0 mM CO2 into glycolate within two hours**, and was optimized by more than one order of magnitude. The paper describes HOPAC as topologically similar to the natural 3HP cycle but designed for greater energetic efficiency. (mclean2023exploringalternativepathways pages 1-2)

### 2024 acetyl-CoA assimilation engineering

The 2024 Lcm module uses a new B12-dependent rearrangement of 3-hydroxypropionyl-CoA to lactyl-CoA. Directed hypermutation and adaptive evolution improved catalytic efficiency approximately **10-fold**, and the complete module was demonstrated in vitro. This is an application of a 3HP-related intermediate, not evidence that the natural bicycle operates in engineered *E. coli*. (schulzmirbach2024newtonatureco2dependentacetylcoa pages 1-2)

### 2024 dissolved-inorganic-carbon supply

A 2024 survey showed that autotrophs using non-Calvin pathways, including the hydroxypropionate bicycle, can encode carbonic anhydrases and putative DIC transporters. Across surveyed autotrophs, growth optima ranged from **pH 1.4 to 11**; CO2 dominates below approximately pH 6.4, whereas bicarbonate dominates around circumneutral pH. However, transporter and carbonic-anhydrase gene presence is not direct evidence of their necessity for the 3HP bicycle. Such nodes should be represented as contextual or uncertain modifiers, not core pathway components. (scott2024widespreaddissolvedinorganic pages 7-10)

## Recommended minimal graph expansion

The existing 14-node/9-edge graph should first be expanded with the highest-confidence nodes and edges:

1. Two explicit modules: glyoxylate synthesis and glyoxylate assimilation.
2. Bicarbonate, ATP, NADPH, biotin, and cobalamin.
3. MCR, PCS, acetyl-/propionyl-CoA carboxylase, MMC lyase, and MCT.
4. The stereospecific CoA intermediates from acetyl-CoA through pyruvate.
5. Taxon-qualified edges to *C. aurantiacus* and, for MCT structural claims, *R. castenholzii*.
6. An oxygen-tolerance edge and a hot-spring-mat association, both explicitly qualified as physiological/environmental rather than reaction edges.

## Claims not yet suitable for TraitMech curation

- **Autotrophy in newly predicted non-Chloroflexota taxa:** MAG completeness and operon organization are suggestive but not equivalent to demonstrated flux or growth.
- **Actinobacteriota pathway presence:** the reported 68.6% mean completeness argues against curating a complete bicycle.
- **DIC transporter or carbonic-anhydrase requirement:** current evidence is comparative-genomic and contextual, not causal for this pathway.
- **Exact gene/locus and UniProt assignments:** not supported by the retrieved passages and must be independently verified.
- **Individual succinyl-CoA-to-malyl-CoA reactions:** the retrieved reviews support the composite conversion, but a reaction-resolved graph requires primary biochemical sources.
- **Exact β-methylmalyl-CoA condensation product naming:** one review excerpt abbreviates it as methylmalonyl-CoA; resolve against the primary MMC-lyase study before curation.
- **Oxygen as a simple inhibitor:** the pathway is generally oxygen tolerant; only the radical B12 step has a context-dependent high-light/high-O2 concern.
- **HOPAC or Lcm as instances of `traitmech:000023`:** both are synthetic neighboring pathways and should be linked only as applications or analogues.

## DOI-first bibliography

1. Berg IA. **Ecological Aspects of the Distribution of Different Autotrophic CO2 Fixation Pathways.** *Applied and Environmental Microbiology*. Published March 2011. DOI: [10.1128/AEM.02473-10](https://doi.org/10.1128/AEM.02473-10). (berg2011ecologicalaspectsof pages 7-8)
2. Hügler M, Sievert SM. **Beyond the Calvin Cycle: Autotrophic Carbon Fixation in the Ocean.** *Annual Review of Marine Science*. Published January 2011. DOI: [10.1146/annurev-marine-120709-142712](https://doi.org/10.1146/annurev-marine-120709-142712). (hugler2011beyondthecalvin pages 9-10)
3. Min Z et al. **Crystal Structure of an Intramolecular Mesaconyl-Coenzyme A Transferase From the 3-Hydroxypropionic Acid Cycle of Roseiflexus castenholzii.** *Frontiers in Microbiology*. Published 26 May 2022. DOI: [10.3389/fmicb.2022.923367](https://doi.org/10.3389/fmicb.2022.923367). (min2022crystalstructureof pages 1-2)
4. Garritano AN, Song W, Thomas T. **Carbon fixation pathways across the bacterial and archaeal tree of life.** *PNAS Nexus*. Published October 2022. DOI: [10.1093/pnasnexus/pgac226](https://doi.org/10.1093/pnasnexus/pgac226). (garritano2022carbonfixationpathways pages 2-3)
5. McLean R et al. **Exploring alternative pathways for the in vitro establishment of the HOPAC cycle for synthetic CO2 fixation.** *Science Advances*. Published 14 June 2023. DOI: [10.1126/sciadv.adh4299](https://doi.org/10.1126/sciadv.adh4299). (mclean2023exploringalternativepathways pages 1-2)
6. Scott KM, Payne RR, Gahramanova A. **Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea.** *Applied and Environmental Microbiology*. Published February 2024. DOI: [10.1128/AEM.01557-23](https://doi.org/10.1128/AEM.01557-23). (scott2024widespreaddissolvedinorganic pages 7-10)
7. Schulz-Mirbach H et al. **New-to-nature CO2-dependent acetyl-CoA assimilation enabled by an engineered B12-dependent acyl-CoA mutase.** *Nature Communications*. Accepted 22 October 2024; published 2024. DOI: [10.1038/s41467-024-53762-9](https://doi.org/10.1038/s41467-024-53762-9). (schulzmirbach2024newtonatureco2dependentacetylcoa pages 1-2)

References

1. (berg2011ecologicalaspectsof pages 7-8): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

2. (min2022crystalstructureof pages 1-2): Zhenzhen Min, Xin Zhang, Wenping Wu, Yueyong Xin, Menghua Liu, Kangle Wang, Xingwei Zhang, Yun He, Chengpeng Fan, Zhiguo Wang, and Xiaoling Xu. Crystal structure of an intramolecular mesaconyl-coenzyme a transferase from the 3-hydroxypropionic acid cycle of roseiflexus castenholzii. Frontiers in Microbiology, May 2022. URL: https://doi.org/10.3389/fmicb.2022.923367, doi:10.3389/fmicb.2022.923367. This article has 8 citations and is from a peer-reviewed journal.

3. (hugler2011beyondthecalvin pages 9-10): Michael Hügler and Stefan M. Sievert. Beyond the calvin cycle: autotrophic carbon fixation in the ocean. Annual review of marine science, 3:261-89, Jan 2011. URL: https://doi.org/10.1146/annurev-marine-120709-142712, doi:10.1146/annurev-marine-120709-142712. This article has 809 citations and is from a highest quality peer-reviewed journal.

4. (berg2011ecologicalaspectsof pages 8-9): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

5. (garritano2022carbonfixationpathways pages 2-3): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 130 citations and is from a peer-reviewed journal.

6. (schulzmirbach2024newtonatureco2dependentacetylcoa pages 1-2): Helena Schulz-Mirbach, Philipp Wichmann, Ari Satanowski, Helen Meusel, Tong Wu, Maren Nattermann, Simon Burgener, Nicole Paczia, Arren Bar-Even, and Tobias J. Erb. New-to-nature co2-dependent acetyl-coa assimilation enabled by an engineered b12-dependent acyl-coa mutase. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53762-9, doi:10.1038/s41467-024-53762-9. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (mclean2023exploringalternativepathways pages 1-2): Richard McLean, Thomas Schwander, Christoph Diehl, Niña Socorro Cortina, Nicole Paczia, Jan Zarzycki, and Tobias J. Erb. Exploring alternative pathways for the in vitro establishment of the hopac cycle for synthetic co <sub>2</sub> fixation. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adh4299, doi:10.1126/sciadv.adh4299. This article has 64 citations and is from a highest quality peer-reviewed journal.

8. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.