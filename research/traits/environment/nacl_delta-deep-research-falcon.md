---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:15:29.970122'
end_time: '2026-08-04T01:34:06.595558'
duration_seconds: 1116.63
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta
  trait_identifier: METPO:1000335
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits expressing the breadth (maximum
    minus minimum) of NaCl concentrations supporting growth of an organism.
  parent_traits: METPO:1000532, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta)
    reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2:
    cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive
    capacity as the basis of a wide NaCl-delta phenotype.)'
  causal_graph_summary: 'nacl_delta_euryhaline_breadth: 13 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000335
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits expressing the breadth (maximum minus minimum) of NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta) reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive capacity as the basis of a wide NaCl-delta phenotype.)
- **Existing causal graph summary:** nacl_delta_euryhaline_breadth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta.yaml`.

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
- **Trait label:** NaCl delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000335
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits expressing the breadth (maximum minus minimum) of NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta) reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive capacity as the basis of a wide NaCl-delta phenotype.)
- **Existing causal graph summary:** nacl_delta_euryhaline_breadth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta.yaml`.

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


# Curation report: microbial **NaCl delta**

## Executive summary

**Trait:** **NaCl delta**  
**Identifier:** **METPO:1000335**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED

NaCl delta is an assay-derived breadth trait:

\[
\text{NaCl delta}=\text{maximum NaCl supporting growth}-\text{minimum NaCl supporting growth}.
\]

It is therefore a property of the **entire observed growth interval**, not simply salt tolerance, the optimum NaCl concentration, or the maximum tolerated concentration. Biologically, a large delta approximates euryhaline physiology, whereas a small delta approximates stenohaline specialization. Current evidence supports a graph in which regulated compatible-solute uptake/synthesis and ion transport preserve osmotic and ionic homeostasis at the high-salinity boundary, while the salt dependence of proteins and other cellular structures can raise the low-salinity boundary. Only mechanisms affecting one or both boundaries can ultimately alter the delta.

The strongest graph-level interpretation is that flexible “salt-out” physiology often supports a broad salinity interval, whereas obligate “salt-in” specialization can constrain low-salt growth because its proteins require high intracellular salt. This is an authoritative synthesis, but it is not a universal rule: some organisms combine both strategies, and most mechanistic experiments measure high-salt growth rather than delta directly. (oren2008microbiallifeat pages 10-11, saum2008regulationofosmoadaptation pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)

---

## 1. Trait scope and boundary rules

### 1.1 Included phenotype

Curate **METPO:1000335** when a study reports—or permits calculation of—the difference between the highest and lowest **NaCl concentrations at which microbial growth occurs under one defined protocol**. The growth criterion may be optical density increase, colony formation, biomass, cell-number increase, or another validated proliferation endpoint, but the same criterion should define both limits.

The euryhaline/stenohaline distinction is conceptually aligned with this trait. A 2024 estuarine study defines stenohaline organisms as thriving within a narrow salinity range and euryhaline organisms as adapting to wide salinity fluctuations. However, its operational classification used environmental relative abundance rather than laboratory NaCl growth endpoints, so those labels are ecological proxies—not direct METPO:1000335 measurements. (wu2024metagenomicinsightsinto pages 1-2)

### 1.2 Nearby traits that must remain separate

| Nearby observation | Why it is not NaCl delta |
|---|---|
| Minimum NaCl for growth | One endpoint only; may reflect obligate halophily or low-salt instability. |
| Maximum NaCl for growth | One endpoint only; represents the upper growth limit. |
| Optimal NaCl | Position of best growth, not interval width. |
| Growth rate or yield at one NaCl level | Performance at a point, not breadth. |
| Survival after salt shock | Viability is not necessarily growth. |
| Generic “salt tolerance” | Often lacks both numerical limits. |
| Osmolarity range produced with sucrose or other solutes | Not specifically an NaCl interval; ionic and osmotic effects differ. |
| Seawater percentage or total salinity | Curatable only with an explicit conversion to NaCl-equivalent concentration and adequate medium description. |
| Environmental occurrence across a salinity gradient | Evidence of realized niche breadth, not necessarily intrinsic NaCl growth breadth. |

NaCl concentration changes both water activity/osmotic pressure and Na⁺/Cl⁻ chemistry. Hyperosmotic conditions drive water out of cells, causing dehydration and altered turgor; accordingly, an NaCl assay cannot automatically be interpreted as a pure osmolarity assay. (yang2024structureandmechanism pages 1-2)

### 1.3 Assay metadata required for defensible delta values

Record the strain, medium composition, NaCl units, concentration series and step size, temperature, pH, oxygen regime, incubation time, inoculum, growth threshold, and whether osmoprotectants were supplied. Also retain minimum and maximum values as separate provenance-bearing observations. A reported delta is resolution-limited: if concentrations were tested every 0.5 M, both boundaries—and hence the delta—are interval-censored by the assay grid.

A useful example is *Spiribacter salinus* M19-40: no growth was detected below 0.4 M NaCl, optimum growth occurred at 0.8 M, and growth was observed over approximately 0.6–2.0 M. Under that protocol, the observed delta is approximately **1.4 M**, but the true lower and upper limits are only bounded by the tested series. (leon2018compatiblesolutesynthesis pages 4-5)

---

## 2. Current mechanistic model

A tractable TraitMech graph should distinguish three levels:

1. **Primary stress:** increased extracellular NaCl → water efflux, dehydration, turgor perturbation, Na⁺ stress.
2. **Homeostatic responses:** compatible-solute accumulation, K⁺ uptake, Na⁺ extrusion, regulated transport, metabolic and proteome adaptation.
3. **Boundary effects:** restored growth at high NaCl lowers growth inhibition at the upper boundary; salt-dependent proteins or structures can prevent low-NaCl growth and raise the lower boundary. The resulting difference determines **METPO:1000335**.

The evidence-ranked core is summarized below.

| subject | predicate | object | evidence class | taxon/context | reference DOI |
|---|---|---|---|---|---|
| High NaCl / hyperosmotic stress | causes | water efflux / cellular dehydration | Direct physiological principle from review/intro; broad, not trait-specific | General microbial osmoadaptation | 10.1126/sciadv.ado6229 (yang2024structureandmechanism pages 1-2) |
| Compatible-solute accumulation | promotes | osmotic homeostasis / growth at high salinity | Direct physiological + review support; breadth effect inferred | General bacteria; Halobacillus, Spiribacter, Halomonas contexts | 10.1186/1746-1448-4-4 (saum2008regulationofosmoadaptation pages 1-2), 10.3389/fmicb.2018.00108 (leon2018compatiblesolutesynthesis pages 1-2), 10.3389/fmicb.2022.846677 (hobmeier2022adaptationtovarying pages 1-2) |
| BetT hyperosmotic activation | increases | choline uptake | Direct functional transport evidence with mutational support | *Pseudomonas syringae* BetT; 0.5 M NaCl activation assay | 10.1126/sciadv.ado6229 (yang2024structureandmechanism pages 5-6, yang2024structureandmechanism pages 1-2) |
| Choline uptake | enables | glycine betaine synthesis | Direct pathway evidence; functional but not range-breadth specific | General bacterial choline–betaine pathway | 10.1126/sciadv.ado6229 (yang2024structureandmechanism pages 1-2) |
| Ectoine accumulation | promotes | high-salt resistance / osmoregulation | Direct physiological support; impact on NaCl delta usually inferred unless range tested | *Halomonas elongata* and other halophiles | 10.3389/fmicb.2022.846677 (hobmeier2022adaptationtovarying pages 1-2) |
| Glycine betaine / ectoine / choline addition | stimulates | growth under saline conditions | Direct growth effect; supports upper-salt growth more than full delta | *Schmidingerothrix salinarum* | 10.1371/journal.pbio.2003892 (weinisch2018identificationofosmoadaptive pages 1-2) |
| Trk-type K+ uptake system | promotes | ion / osmotic homeostasis under salinity | Strong association in natural communities; direct functional breadth evidence lacking | Estuarine MAGs across salinity gradient; feature COG0168 | 10.1186/s40168-024-01817-w (wu2024metagenomicinsightsinto pages 1-2) |
| TrkG/TrkH potassium uptake | contributes to | salt homeostasis | Genome/physiology inference, not knockout | *Spiribacter salinus* M19-40; grows 0.6–2.0 M NaCl, optimum 0.8 M | 10.3389/fmicb.2018.00108 (leon2018compatiblesolutesynthesis pages 4-5) |
| Mrp sodium extrusion system | promotes | high-salinity growth | Inference from genome/physiology; no direct mutant in cited context | *Spiribacter salinus* M19-40 | 10.3389/fmicb.2018.00108 (leon2018compatiblesolutesynthesis pages 4-5) |
| Upregulated Na+/K+/H+ transporters | maintain | intracellular K+ homeostasis under high salinity | Direct multi-omics correlation; breadth effect inferred | *Natranaerobius thermophilus* under 2.5–4.3 M Na+ | 10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Acidic, salt-dependent proteome / salt-in specialization | restricts | growth in low-salt conditions | Review-based mechanistic inference; strong for specialists | Halobacteriales, *Salinibacter* and other salt-in strategists | 10.1186/1746-1448-4-2 (oren2008microbiallifeat pages 10-11), 10.1186/1746-1448-4-4 (saum2008regulationofosmoadaptation pages 1-2) |
| Salt-out strategy (organic solutes) | broadens | salinity tolerance range / euryhalinity | Foundational review inference; strongest breadth-level concept | General halophilic bacteria vs salt-in specialists | 10.1186/1746-1448-4-2 (oren2008microbiallifeat pages 10-11) |


*Table: This table summarizes the strongest candidate causal edges for curating NaCl-delta, separating direct functional evidence from association and inference. It highlights mechanisms most plausibly affecting breadth of growth-supporting NaCl concentrations rather than only single high-salt endpoints.*

Crucially, “promotes high-salt growth” is not logically identical to “increases NaCl delta.” Delta increases only if the upper boundary rises without an equal rise in the lower boundary, or if the lower boundary falls without an equal fall in the upper boundary.

---

## 3. Candidate nodes grouped by type

### 3.1 Trait and environmental nodes

- **NaCl delta — METPO:1000335**
- **NaCl concentration / sodium chloride — CHEBI:26710**
- Hyperosmotic environment — label-only candidate
- Low-NaCl condition — label-only candidate
- High-NaCl condition — label-only candidate
- Water activity — label-only candidate
- Growth-supporting NaCl minimum and maximum — preferably the corresponding METPO parent traits supplied in the template: **METPO:1000532** and **METPO:1000534**; verify which identifier denotes which endpoint before encoding.

### 3.2 Chemicals and metabolites

- Sodium ion — **CHEBI:29101**
- Potassium ion — **CHEBI:29103**
- Chloride — **CHEBI:17996**
- Water — **CHEBI:15377**
- Choline — **CHEBI:15354**
- Glycine betaine — **CHEBI:17750**
- L-proline — **CHEBI:17203**
- Ectoine — label-only unless the project’s ontology resolver validates a CHEBI record
- Glutamate, glutamine, trehalose, hydroxyectoine and alanine — label-only here; validate protonation-specific CHEBI records before use.

### 3.3 Genes, proteins and transport systems

- **BetT**, osmoregulated choline transporter; BCCT family
- **Opu**-family compatible-solute ABC transporters
- **ProU** glycine-betaine/proline ABC uptake system
- SSS-family Na⁺/solute symporters
- **EctA/EctB/EctC** ectoine-biosynthesis enzymes; pathway node “ectoine biosynthesis” may be safer than individual proteins across taxa
- Proline-biosynthesis module
- Glutamate/glutamine-biosynthesis module; **glnA2** is taxon-specific evidence in *Halobacillus halophilus*
- **TrkA/TrkH/TrkG** K⁺ uptake system
- **Kdp** and **Kup** K⁺ import systems—candidate comparative nodes, but absent from the cited *S. salinus* genome
- **KefC** K⁺ efflux system
- **Mrp** multisubunit Na⁺/H⁺ antiporter
- Na⁺/K⁺/H⁺ antiporters—retain family-level naming when the experiment does not resolve exact subunits
- Cytochrome bo′ and cytochrome bd quinol oxidases—secondary salt-response candidates
- Malate dehydrogenase and isocitrate dehydrogenase—possible salt-sensitive enzyme nodes in the ciliate evidence

Use label-only nodes for transporter families unless a study identifies an exact sequence and stable UniProt accession. Do not assign one species’ UniProt identifier to a homologous family-level node.

### 3.4 Processes, functions and cellular states

- Response to osmotic stress — **GO:0006970**
- Cellular ion homeostasis — **GO:0006873**
- Compatible-solute accumulation
- Choline transmembrane transport
- Glycine-betaine biosynthesis
- Ectoine biosynthesis
- Potassium-ion uptake
- Sodium-ion export / Na⁺:H⁺ antiport
- Cytoplasmic osmotic adjustment
- Water efflux and cellular dehydration
- Turgor maintenance
- Cytoplasmic acidification
- Acidic-proteome adaptation
- Protein folding/activity at high intracellular salt
- Oxidative phosphorylation, chemotaxis, motility, membrane remodeling and general stress response—secondary candidates only, because present evidence does not establish their effect on range breadth.

### 3.5 Taxon/context nodes

Taxon-specific subgraphs are advisable for *Spiribacter salinus* M19-40, *Halomonas elongata* DSM 2581T, *Natranaerobius thermophilus*, *Halobacillus halophilus*, *Pseudomonas syringae*, *Schmidingerothrix salinarum*, Halobacteriaceae and *Salinibacter*. Stable NCBITaxon identifiers should be resolved against the exact strain names before YAML insertion rather than inferred from species names.

---

## 4. Candidate causal edges with source snippets

| Subject → predicate → object | Supporting snippet | Reference | Curation assessment |
|---|---|---|---|
| High extracellular NaCl → **causes** → water efflux/cellular dehydration | “under hyperosmotic conditions…water will flow out of the cell, resulting in cellular dehydration” | Yang et al., 14 Aug 2024; DOI [10.1126/sciadv.ado6229](https://doi.org/10.1126/sciadv.ado6229) (yang2024structureandmechanism pages 1-2) | **Strong general mechanism.** Curate upstream of homeostatic responses, not as a direct delta edge. |
| Water efflux → **perturbs** → turgor and cell growth | Water influx or efflux “cause[s] changes in turgor pressure and affect[s] cell growth” | Same source (yang2024structureandmechanism pages 1-2) | **Strong general mechanism.** |
| Compatible-solute accumulation → **promotes** → osmotic homeostasis under high NaCl | Compatible solutes “help adjust osmotic potential without impairing normal cellular activities” | Same source (yang2024structureandmechanism pages 1-2) | **Strong mechanism; breadth effect inferred.** |
| Hyperosmotic stress → **releases autoinhibition of** → BetT | BetT is in a “low-activity state” without stress; hyperosmotic activation involves “release of this autoinhibition” | Yang et al., 2024 (yang2024structureandmechanism pages 5-6, yang2024structureandmechanism pages 1-2) | **Direct functional and structural evidence**, *Pseudomonas*-specific. |
| Activated BetT → **increases** → choline uptake | Transport assays used 0.5 M NaCl; CTD deletion and interface/trimer mutations altered transport activity | Yang et al., 2024 (yang2024structureandmechanism pages 5-6) | **Direct transport/mutational evidence.** Do not claim direct delta alteration. |
| Choline uptake → **enables** → glycine-betaine biosynthesis | “choline is taken up through transporters and then converted to glycine betaine via a two-step enzymatic oxidation reaction” | Yang et al., 2024 (yang2024structureandmechanism pages 1-2) | **Strong pathway edge.** |
| Glycine betaine accumulation → **supports** → osmoprotection/protein stabilization | Glycine betaine is described as a potent osmoprotectant that also stabilizes proteins | Yang et al., 2024 (yang2024structureandmechanism pages 1-2) | **Strong general evidence**, but breadth remains inferred. |
| Ectoine accumulation → **promotes** → high-salinity resistance | Ectoine accumulation is “central to osmoregulation and promotes resistance to high salinity” in halophilic bacteria | Hobmeier et al., 30 Mar 2022; DOI [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677) (hobmeier2022adaptationtovarying pages 1-2) | **Moderately strong.** Effect is much smaller in non-halophiles; taxon dependence must be retained. |
| Exogenous glycine betaine/ectoine/choline → **stimulates** → saline growth | Addition of all three compounds “stimulated the cell growth notably” | Weinisch et al., Jan 2018; DOI [10.1371/journal.pbio.2003892](https://doi.org/10.1371/journal.pbio.2003892) (weinisch2018identificationofosmoadaptive pages 1-2) | **Direct growth evidence** in a halophilic ciliate; mostly supports the upper boundary. |
| External salinity → **increases** → intracellular glycine betaine and ectoine | Intracellular concentrations had a significant positive correlation with external salinity | Weinisch et al., 2018 (weinisch2018identificationofosmoadaptive pages 1-2) | **Physiological correlation**, not genetic causality. |
| Ectoine synthesis/import plus glycine-betaine import → **implements** → salt-out osmoadaptation | *S. salinus* synthesizes ectoine; salinity-responsive betaine import accumulates betaine and suppresses ectoine synthesis | León et al., Feb 2018; DOI [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108) (leon2018compatiblesolutesynthesis pages 1-2) | **Strong physiological evidence for flexible osmolyte use.** Direct delta effect not isolated. |
| TrkG/TrkH K⁺ uptake → **contributes to** → salt homeostasis | Trk systems were identified alongside measured growth over 0.6–2.0 M NaCl | León et al., 2018 (leon2018compatiblesolutesynthesis pages 4-5) | **Mechanistic inference**, no cited knockout. |
| Mrp Na⁺ extrusion → **promotes** → high-salinity growth | The Mrp sodium-extrusion system is identified as important for high-salinity growth | León et al., 2018 (leon2018compatiblesolutesynthesis pages 4-5) | **Moderate, taxon-specific inference.** |
| Increasing salinity → **increases** → compatible solutes and K⁺-homeostasis response | Glycine betaine, glutamate and proline increased with salinity; Na⁺/K⁺/H⁺ transporters were upregulated | Xing et al., May 2024; DOI [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24) (xing2024thepolyextremophilenatranaerobius pages 1-2) | **Multi-omics correlation** in *N. thermophilus*, not perturbational causality. |
| Dual compatible-solute plus salt-in strategy → **supports** → growth at extreme Na⁺ | *N. thermophilus* grows at 3.1–4.9 M Na⁺ and combines solute accumulation with K⁺/ion regulation | Xing et al., 2024 (xing2024thepolyextremophilenatranaerobius pages 1-2) | **Strong organism-level model**, but Na⁺ rather than strictly NaCl was profiled; curate as uncertain for NaCl delta. |
| Trk-type K⁺ transporter abundance → **associates with** → salinity adaptation | COG0168 was the most important selected feature and increased with salinity | Wu et al., Jun 2024; DOI [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w) (wu2024metagenomicinsightsinto pages 1-2) | **Association only.** Encode `associated_with`, not `causes`. |
| Moderate NaCl → **induces** → glutamate/glutamine osmolyte strategy | *H. halophilus* accumulates glutamine and glutamate “to adjust turgor”; glnA2 transcription and activity are chloride-dependent | Saum & Müller, 28 Apr 2008; DOI [10.1186/1746-1448-4-4](https://doi.org/10.1186/1746-1448-4-4) (saum2008regulationofosmoadaptation pages 1-2) | **Taxon- and chloride-specific physiological evidence.** |
| High salinity → **switches dominant osmolyte to** → proline | *H. halophilus* “produces proline as the main compatible solute at high salinities” | Same source (saum2008regulationofosmoadaptation pages 1-2) | **Strong regulatory evidence**, but delta effect untested. |
| Glutamate → **is required for** → proline production | Glutamate was a “‘second messenger’ essential for proline production” | Same source (saum2008regulationofosmoadaptation pages 1-2) | **Potentially curatable taxon-specific causal edge.** |
| Salt-in proteome specialization → **restricts** → low-salinity growth | Salt-adapted proteins “always need a quite high intracellular salt concentration for correct protein folding and activity” | Saum & Müller, 2008 (saum2008regulationofosmoadaptation pages 1-2) | **Strong review-level mechanism** for raising the lower boundary; not universal. |
| Organic-solute salt-out strategy → **tends to broaden** → salinity growth range | Organisms using organic solutes “often adapt to a surprisingly broad salt concentration range” | Oren, Apr 2008; DOI [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2) (oren2008microbiallifeat pages 10-11) | **Best breadth-level synthesis**, but encode as a qualified tendency rather than universal causation. |

### Recommended graph endpoint design

Instead of connecting every mechanism directly to **METPO:1000335**, use intermediate boundary nodes:

- compatible-solute accumulation → restores osmotic homeostasis → permits growth at higher NaCl → increases maximum growth-supporting NaCl;
- Na⁺ extrusion/K⁺ uptake → maintains ion homeostasis → permits growth at higher NaCl → increases maximum;
- salt-dependent acidic proteome → impairs function at low intracellular salt → increases minimum growth-supporting NaCl;
- maximum − minimum → determines **METPO:1000335**.

This design avoids the false inference that every high-salt response necessarily broadens the interval.

---

## 5. Recent developments and quantitative evidence, 2023–2024

### 5.1 Natural salinity-gradient genomics

Wu et al. reconstructed **127 MAGs** from the Pearl River Estuary: 33 were low-salinity stenohaline, 36 intermediate-salinity stenohaline, 44 high-salinity stenohaline, and **14 euryhaline**. Among 12,612 COGs analyzed in the detailed results, 40 were selected as distinguishing features; 13 belonged to inorganic-ion transport and metabolism. The abstract reports eight osmoregulatory COGs—four salt-in, three salt-out and one related to water-channel regulation—and ranks the Trk-associated COG0168 first. These results make Trk-mediated K⁺ transport a high-priority hypothesis, but the work is observational and does not demonstrate that adding or deleting Trk changes laboratory NaCl delta. (wu2024metagenomicinsightsinto pages 7-9, wu2024metagenomicinsightsinto pages 1-2)

### 5.2 Structural mechanism for osmotically gated compatible-solute acquisition

The 2024 BetT cryo-EM study provides unusually strong molecular evidence. *P. syringae* BetT forms a domain-swapped trimer whose C-terminal domain autoinhibits transport at low osmolarity. NaCl-induced hyperosmotic conditions release this inhibition; CTD, interface and trimer-disrupting mutants alter choline transport. This establishes a mechanistic chain from osmotic sensing to precursor uptake for glycine-betaine synthesis, although no minimum–maximum growth series was reported. (yang2024structureandmechanism pages 5-6, yang2024structureandmechanism pages 1-2)

### 5.3 Hybrid adaptation in an extreme polyextremophile

In 2024, *Natranaerobius thermophilus* was reported to grow across **3.1–4.9 M Na⁺**, with an optimum around 3.3–3.9 M at pH 9.5 and 53°C. Proteomic profiling across 2.5–4.3 M Na⁺, transcript validation, metabolite measurements and K⁺ measurements supported simultaneous compatible-solute and salt-in responses. Glycine betaine, glutamate and proline rose with salinity, while Opu/ProU, SSS-family and Na⁺/K⁺/H⁺ transport systems were implicated. This challenges an overly binary salt-in versus salt-out graph and supports a hybrid-strategy node. Because the exposure is reported as Na⁺ and the study is taxon-specific, transfer to an NaCl-delta graph should be qualified. (xing2024thepolyextremophilenatranaerobius pages 1-2)

### 5.4 Expert interpretation

The convergent expert view is that broad salinity performance is not governed by one “halotolerance gene.” It emerges from coordinated osmolyte supply, ion transport, proteome compatibility, energy metabolism and regulatory switching. *H. elongata*, for example, grows above 10% NaCl and accumulates ectoine, but transcriptomics at 0.17, 1 and 2 M NaCl led investigators to argue that ion accumulation and alternative respiratory routes contribute more than previously assumed. Thus, ectoine alone is an inadequate graph root. (hobmeier2022adaptationtovarying pages 1-2)

---

## 6. Applications and implementation maturity

NaCl-delta measurements have practical value because processes with changing salinity require organisms that continue growing across a range, not merely organisms with a high optimum.

- **Saline agriculture:** salt-tolerant plant-growth-promoting microbes are being evaluated as bioinoculants. A 2024 hypersaline metagenomic study recovered MAGs in which **91.3%** had annotated salt-tolerance potential, **95.6%** heavy-metal tolerance, **95.6%** exopolysaccharide potential and **60.86%** antioxidant-biosynthesis potential. These are genomic predictions, not proof of field performance or NaCl delta. (dindhoria2024metagenomicassembledgenomes pages 1-2)
- **Saline wastewater and biohydrogen:** reported systems include *Bacillus* sp. B2 producing **1.65 mol H₂ per mol glucose at 0.5 M salinity**, *Halanaerobium* tolerating up to **2.6 M** salt while producing hydrogen from glycerol, and a co-culture producing **1,694 mL H₂/L at 0.5 M**. Reviews nevertheless characterize commercial-scale deployment as developmental and dependent on improved reactors and process control. (guo2024biohydrogenproductionfrom pages 14-16, guo2024biohydrogenproductionfrom pages 18-20)
- **Biomanufacturing:** *Halomonas elongata* is an established ectoine-production organism, while haloarchaea and their enzymes are being developed for robust synthesis under high salt. Much of the broader green-chemistry chassis literature still describes potential rather than mature deployment. (hobmeier2022adaptationtovarying pages 1-2, martinezespinosa2023editorialadaptationof pages 1-2)
- **Bioremediation, food processing and pharmaceuticals:** authoritative 2023 synthesis identifies hydrocarbon degradation, saline wastewater treatment, food processes, extremozymes, biodegradable polymers and bioactive compounds as application areas. These applications motivate selecting organisms with suitable salinity breadth, but they do not themselves validate causal edges for METPO:1000335. (martinezespinosa2023editorialadaptationof pages 2-3, martinezespinosa2023editorialadaptationof pages 1-2)

---

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not curate Trk abundance → increases NaCl delta as causal.** The 2024 estuarine evidence is feature selection and abundance association, not gene perturbation. (wu2024metagenomicinsightsinto pages 1-2)
2. **Do not equate an induced transcript with a necessary mechanism.** Transporter or pathway upregulation in *N. thermophilus* and *H. elongata* supports response models, not necessity or sufficiency. (xing2024thepolyextremophilenatranaerobius pages 1-2, hobmeier2022adaptationtovarying pages 1-2)
3. **Do not infer delta from maximum tolerance alone.** A high maximum can coexist with a high minimum and therefore a narrow delta, as in obligate salt-in specialists. Halobacteriaceae and *Salinibacter* may require more than 150 g/L NaCl despite high optima. (oren2008microbiallifeat pages 10-11)
4. **Do not make salt-out universally euryhaline or salt-in universally stenohaline.** Hybrid mechanisms exist, and *Haloferax volcanii* is reported to adapt from about 1 M to near saturation despite salt-in specialization. (saum2008regulationofosmoadaptation pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)
5. **Do not treat seawater percentage, total salinity or Na⁺ molarity as NaCl molarity without conversion and medium chemistry.** The *N. thermophilus* evidence is especially important but not a clean NaCl-delta assay. (xing2024thepolyextremophilenatranaerobius pages 1-2)
6. **Do not generalize BetT regulation across all bacteria.** CTD deletion affected *Pseudomonas* and *E. coli* BetT differently, indicating lineage-specific regulation. (yang2024structureandmechanism pages 5-6)
7. **Do not curate membrane remodeling, oxidative stress, motility, chemotaxis or respiratory-chain changes as delta determinants yet.** Current evidence is predominantly differential expression and lacks direct range-shift experiments. (hobmeier2022adaptationtovarying pages 1-2)
8. **Do not assign unverified CURIEs.** Gene-family labels and exact strain taxon identifiers should remain label-only until checked in UniProt, NCBITaxon and the project’s ontology release.

---

## 8. Recommended initial YAML graph

A conservative first version of `nacl_delta_euryhaline_breadth` should prioritize:

1. extracellular NaCl concentration → water efflux/cellular dehydration;
2. dehydration → turgor perturbation/growth inhibition;
3. hyperosmotic stress → BetT activation → choline uptake → glycine-betaine synthesis/accumulation;
4. hyperosmotic stress → ectoine, proline and glutamate accumulation;
5. Trk-mediated K⁺ uptake and Mrp-mediated Na⁺ extrusion → ion homeostasis;
6. osmotic/ion homeostasis → growth at higher NaCl → increased upper boundary;
7. salt-in strategy → acidic, salt-dependent proteome → impaired low-salt function → increased lower boundary;
8. upper boundary minus lower boundary → **NaCl delta, METPO:1000335**.

Edges 1–5 should carry taxon and evidence qualifiers. Edges from homeostasis to the numerical boundary should be marked **inferred** unless a mutant or intervention shifts a measured minimum or maximum. The final arithmetic edge is definitional rather than biological causation.

---

## DOI-first bibliography

1. Xing Q. et al. “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy…” *Applied and Environmental Microbiology*. **May 2024**. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. Yang T. et al. “Structure and mechanism of the osmoregulated choline transporter BetT.” *Science Advances*. **14 August 2024**. DOI: [10.1126/sciadv.ado6229](https://doi.org/10.1126/sciadv.ado6229). (yang2024structureandmechanism pages 5-6, yang2024structureandmechanism pages 1-2)
3. Wu Z. et al. “Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.” *Microbiome*. **June 2024**. DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w). (wu2024metagenomicinsightsinto pages 7-9, wu2024metagenomicinsightsinto pages 1-2)
4. Dindhoria K. et al. “Metagenomic assembled genomes indicated the potential application of hypersaline microbiome…” *mSystems*. **March 2024**. DOI: [10.1128/msystems.01050-23](https://doi.org/10.1128/msystems.01050-23). (dindhoria2024metagenomicassembledgenomes pages 1-2)
5. Martínez-Espinosa R.M. et al. “Editorial: Adaptation of halophilic/halotolerant microorganisms and their applications.” *Frontiers in Microbiology*. **August 2023**. DOI: [10.3389/fmicb.2023.1252921](https://doi.org/10.3389/fmicb.2023.1252921). (martinezespinosa2023editorialadaptationof pages 2-3, martinezespinosa2023editorialadaptationof pages 1-2)
6. Hobmeier K. et al. “Adaptation to Varying Salinity in *Halomonas elongata*: Much More Than Ectoine Accumulation.” *Frontiers in Microbiology*. **30 March 2022**. DOI: [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677). (hobmeier2022adaptationtovarying pages 1-2)
7. Gunde-Cimerman N., Plemenitaš A., Oren A. “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews*. **May 2018**. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009).
8. León M.J. et al. “Compatible Solute Synthesis and Import by the Moderate Halophile *Spiribacter salinus*.” *Frontiers in Microbiology*. **February 2018**. DOI: [10.3389/fmicb.2018.00108](https://doi.org/10.3389/fmicb.2018.00108). (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 4-5)
9. Weinisch L. et al. “Identification of osmoadaptive strategies in the halophile…*Schmidingerothrix salinarum*.” *PLOS Biology*. **January 2018**. DOI: [10.1371/journal.pbio.2003892](https://doi.org/10.1371/journal.pbio.2003892). (weinisch2018identificationofosmoadaptive pages 1-2)
10. Oren A. “Microbial life at high salt concentrations: phylogenetic and metabolic diversity.” *Saline Systems*. **April 2008**. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2). (oren2008microbiallifeat pages 10-11)
11. Saum S.H., Müller V. “Regulation of osmoadaptation in the moderate halophile *Halobacillus halophilus*.” *Saline Systems*. **28 April 2008**. DOI: [10.1186/1746-1448-4-4](https://doi.org/10.1186/1746-1448-4-4). (saum2008regulationofosmoadaptation pages 1-2)

**Overall curation judgment:** **METPO:1000335** is suitable for a TraitMech graph, but the graph should be boundary-aware and evidence-graded. The most defensible direct molecular chain is hyperosmotic stress → regulated compatible-solute acquisition/production → osmotic homeostasis → high-salt growth. The strongest proposed determinant of the low-salt boundary is salt-dependent proteome specialization. Direct demonstrations that a defined gene changes the complete numerical NaCl delta remain scarce; most gene-to-delta edges should therefore initially be marked taxon-specific and inferred.

References

1. (oren2008microbiallifeat pages 10-11): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

2. (saum2008regulationofosmoadaptation pages 1-2): Stephan H Saum and Volker Müller. Regulation of osmoadaptation in the moderate halophile halobacillus halophilus: chloride, glutamate and switching osmolyte strategies. Saline Systems, 4:4-4, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-4, doi:10.1186/1746-1448-4-4. This article has 162 citations.

3. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

4. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

5. (yang2024structureandmechanism pages 1-2): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

7. (leon2018compatiblesolutesynthesis pages 1-2): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

8. (hobmeier2022adaptationtovarying pages 1-2): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 53 citations and is from a peer-reviewed journal.

9. (yang2024structureandmechanism pages 5-6): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (weinisch2018identificationofosmoadaptive pages 1-2): Lea Weinisch, Steffen Kühner, Robin Roth, Maria Grimm, Tamara Roth, Daili J. A. Netz, Antonio J. Pierik, and Sabine Filker. Identification of osmoadaptive strategies in the halophile, heterotrophic ciliate schmidingerothrix salinarum. PLOS Biology, 16:e2003892, Jan 2018. URL: https://doi.org/10.1371/journal.pbio.2003892, doi:10.1371/journal.pbio.2003892. This article has 104 citations and is from a highest quality peer-reviewed journal.

11. (wu2024metagenomicinsightsinto pages 7-9): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

12. (dindhoria2024metagenomicassembledgenomes pages 1-2): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.

13. (guo2024biohydrogenproductionfrom pages 14-16): Huiyuan Guo, Zedong Teng, Hexing Han, and Tinggang Li. Biohydrogen production from saline wastewater: an overview. Clean Energy Science and Technology, 2:210, Sep 2024. URL: https://doi.org/10.18686/cest.v2i3.210, doi:10.18686/cest.v2i3.210. This article has 5 citations.

14. (guo2024biohydrogenproductionfrom pages 18-20): Huiyuan Guo, Zedong Teng, Hexing Han, and Tinggang Li. Biohydrogen production from saline wastewater: an overview. Clean Energy Science and Technology, 2:210, Sep 2024. URL: https://doi.org/10.18686/cest.v2i3.210, doi:10.18686/cest.v2i3.210. This article has 5 citations.

15. (martinezespinosa2023editorialadaptationof pages 1-2): Rosa María Martínez-Espinosa, Sumit Kumar, Sudhir K. Upadhyay, and Furkan Orhan. Editorial: adaptation of halophilic/halotolerant microorganisms and their applications. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1252921, doi:10.3389/fmicb.2023.1252921. This article has 15 citations and is from a peer-reviewed journal.

16. (martinezespinosa2023editorialadaptationof pages 2-3): Rosa María Martínez-Espinosa, Sumit Kumar, Sudhir K. Upadhyay, and Furkan Orhan. Editorial: adaptation of halophilic/halotolerant microorganisms and their applications. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1252921, doi:10.3389/fmicb.2023.1252921. This article has 15 citations and is from a peer-reviewed journal.