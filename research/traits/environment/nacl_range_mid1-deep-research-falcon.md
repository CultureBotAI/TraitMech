---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:55:05.413666'
end_time: '2026-08-04T02:03:20.015185'
duration_seconds: 494.6
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range mid1
  trait_identifier: METPO:1000470
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl range phenotype in which the growth-supporting NaCl range spans\
    \ approximately 1\u20133% (w/v), characteristic of slight-halophilic or halotolerant\
    \ organisms."
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Slight halophile, NaR_1_to_3
  evidence_summary: "DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review\
    \ supports the 1\u20133% NaCl growth range as the slight-halophile/halotolerant\
    \ category.)"
  causal_graph_summary: 'nacl_range_mid1_slight_halophile: 10 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000470
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 1–3% (w/v), characteristic of slight-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Slight halophile, NaR_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl growth range as the slight-halophile/halotolerant category.)
- **Existing causal graph summary:** nacl_range_mid1_slight_halophile: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid1.yaml`.

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
- **Trait label:** NaCl range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000470
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 1–3% (w/v), characteristic of slight-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Slight halophile, NaR_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl growth range as the slight-halophile/halotolerant category.)
- **Existing causal graph summary:** nacl_range_mid1_slight_halophile: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid1.yaml`.

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


# Curation report: NaCl range mid1

## Trait record and scope

- **Trait label:** NaCl range mid1
- **Trait identifier:** **METPO:1000470**
- **Category / kind:** ENVIRONMENT / CLASS
- **Parent:** METPO:1000334
- **Operational definition:** growth is supported over an approximately **1–3% (w/v) NaCl** interval (about **10–30 g L⁻¹**, or **0.17–0.51 M NaCl**).

This should be curated primarily as an **assay-observed growth-range phenotype**, not as a single molecular mechanism. The range depends on medium composition, temperature, pH, inoculum, growth endpoint, and whether “growth” means detectable growth, a defined growth-rate threshold, or optimum growth.

### Critical terminology issue

“Halotolerant” and “slight halophile” should not be treated as exact synonyms without assay metadata. **Halotolerant** usually means that NaCl is tolerated but not required; **halophilic** implies preferential or required growth in saline conditions. Moreover, many classification schemes define slight halophiles by an **optimum** near 1–3% NaCl, whereas the supplied trait definition concerns the complete **growth-supporting range** spanning approximately 1–3%. Therefore, an organism growing from 0 to 10% NaCl with an optimum at 2% and an organism growing only from 1 to 3% would not have equivalent phenotypes, although both might be informally called “slightly halophilic.”

### Boundary cases

1. **Growth at 0% NaCl:** supports a halotolerant interpretation; it argues against an obligate NaCl requirement.
2. **Optimum at 1–3%, but growth well above 3%:** this is an optimum phenotype, not necessarily `NaCl range mid1` as presently defined.
3. **Growth only at 1–3%:** consistent with a narrow slight-halophile range, but both lower and upper endpoints must be tested.
4. **Marine medium:** total salinity and other ions must not be conflated with NaCl concentration.
5. **Osmolarity controls:** NaCl imposes both osmotic and ionic stress. An iso-osmotic nonionic-solute control is needed to separate these effects.
6. **Taxonomic breadth:** bacterial, archaeal, fungal, and algal salt strategies differ; a single universal gene set should not be asserted.

## Current mechanistic interpretation

The best-supported generic model is that increased external NaCl drives water out of the cell, reduces hydration and turgor, and increases macromolecular crowding. Microorganisms initially adjust inorganic-ion flux—often including transient K⁺ accumulation—and subsequently accumulate compatible organic solutes such as glycine betaine, ectoine, proline, glutamate, or trehalose. These solutes raise cytoplasmic osmotic potential while remaining comparatively compatible with cellular biochemistry. During a sudden decrease in salinity, mechanosensitive channels release intracellular solutes to limit water influx and lysis. This is an authoritative general model, but it explains **osmoadaptation**, not by itself why a strain’s measured upper boundary is specifically 3% NaCl. (bremer2019responsesofmicroorganisms pages 3-5)

| module | representative subject-predicate-object edge | evidence strength | applicability to 1–3% NaCl | curation decision |
|---|---|---|---|---|
| Osmotic challenge | increased external NaCl **decreases** cellular turgor via water efflux (bremer2019responsesofmicroorganisms pages 3-5) | **Strong, general** review-supported mechanism | **High**; core mechanism for any salt-upshift phenotype, including 1–3% w/v | **Curate** as a general upstream edge |
| Transient potassium uptake | hyperosmotic upshift **increases** K+ uptake/accumulation as an early response (bremer2019responsesofmicroorganisms pages 3-5) | **Moderate-strong, general** review-supported; transient sequence emphasized | **High**; broadly plausible in slight-halophile/halotolerant growth, but usually not sufficient alone | **Curate with note** that effect is often early/transient |
| Compatible-solute accumulation | hyperosmotic stress **increases** compatible-solute accumulation (e.g., glycine betaine, ectoine, proline, trehalose, glutamate) (bremer2019responsesofmicroorganisms pages 3-5) | **Strong, general** review-supported | **High**; best-supported broad mechanism for 1–3% w/v growth support | **Curate** as central mechanism |
| BetT / choline / glycine betaine | hyperosmotic stress **activates** BetT-mediated choline uptake; imported choline **enables** glycine betaine synthesis (yang2024structureandmechanism pages 1-2) | **Strong for transporter mechanism**, but structurally resolved in specific taxa | **Moderate-high**; highly relevant where betT/choline pathway is present, not universal | **Curate conditionally** at gene/module level, taxon-specific presence required |
| Sodium–proton antiport | elevated NaCl **increases** Na+/H+ antiporter activity/expression, which **promotes** Na+ extrusion and ion homeostasis (nie2025ahalophilicbacterium pages 13-15, xing2024thepolyextremophilenatranaerobius pages 1-2) | **Moderate**; direct omics support but mostly taxon-specific and often high-salt | **Moderate**; likely relevant, but strongest data come from >1–3% systems | **Curate as uncertain/taxon-sensitive** |
| Ectoine / proline genetic replacement | ectABC loss **reduces** high-salt growth; engineered proline biosynthesis plus putA deletion **restores/promotes** growth by intracellular proline accumulation (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) | **Strong causal genetic evidence** | **Low-moderate** for METPO:1000470 specifically; experiment demonstrates osmolyte substitutability, but at 4–8% NaCl in Halomonas elongata | **Use as supporting mechanistic exemplar only**; do not overgeneralize to 1–3% trait |
| Mechanosensitive-channel downshock | hypoosmotic downshift **activates** mechanosensitive channels, which **release** ions/compatible solutes to prevent lysis (bremer2019responsesofmicroorganisms pages 3-5) | **Strong, general** for downshock physiology | **Low-direct** for growth at 1–3% NaCl; relevant to fluctuations, not primary cause of growth in mid1 range | **Do not prioritize** for core trait graph; add only if modeling salinity transitions |
| Chaperone / oxidative-stress responses | high salt **increases** chaperone and antioxidant stress-response systems (e.g., GroES/GroEL, catalase-like functions) (nie2025ahalophilicbacterium pages 13-15, srivastava2022transcriptomeanalysisto pages 1-2) | **Moderate**; transcriptomic/proteomic evidence, taxon-specific | **Moderate-low** for trait core; likely secondary protective responses rather than defining mechanism of 1–3% support | **Curate only as auxiliary/uncertain** nodes |
| Dual salt-in + compatible-solute strategy | high salinity **can induce** simultaneous compatible-solute accumulation and K+ maintenance (xing2024thepolyextremophilenatranaerobius pages 1-2) | **Moderate** but restricted to extreme polyextremophile context | **Low**; evidence comes from 2.5–4.3 M Na+ systems far above 1–3% w/v NaCl | **Do not curate directly** for METPO:1000470 except as background warning |
| Glycine betaine synthesis/uptake transcriptomic response | increased NaCl **upregulates** glycine betaine biosynthesis and uptake genes (srivastava2022transcriptomeanalysisto pages 1-2, nie2025ahalophilicbacterium pages 13-15) | **Moderate**; omics association with some direct mechanistic coherence | **Moderate**; pathway is likely relevant but data derive from moderate/high-salt taxa and assays | **Curate selectively** when grounded to specific taxa/genes |
| Ectoine induction | NaCl stress **increases** ectoine-related osmoadaptation programs (srivastava2022transcriptomeanalysisto pages 1-2) | **Moderate**; transcriptomic support, limited direct phenotype causality in supplied evidence | **Moderate**; ectoine is a major bacterial osmolyte, but direct 1–3% evidence is limited here | **Curate with caution** and avoid claiming universality |


*Table: This table prioritizes candidate mechanisms and edges for curating the NaCl range mid1 trait, separating broadly supported osmoadaptation processes from taxon-specific or high-salt-only evidence. It is useful for deciding which nodes and edges are safe to include now versus which should remain qualified or deferred.*

## Candidate nodes grouped by type

### Trait and environmental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| NaCl range mid1 | **METPO:1000470** | Target phenotype; retain verbatim CURIE. |
| Parent NaCl-range phenotype | **METPO:1000334** | Supplied parent. |
| Sodium chloride | **CHEBI:26710** | Chemical exposure; encode concentration and units as assay attributes. |
| Hyperosmotic environment / hyperosmotic stress | GO:0006972, response to hyperosmotic stress | Use for biological response, not as a synonym for NaCl exposure. |
| Osmotic downshock | Label-only candidate | Relevant only where salinity transitions are modeled. |
| Extracellular osmolarity | Label-only candidate | Experimental/environmental variable. |
| Water activity | Label-only candidate | Prefer measured value when available; NaCl percentage is only a proxy. |
| Growth-supporting NaCl lower and upper bounds | Label-only assay attributes | Record separately rather than reducing the phenotype to one concentration. |
| Growth rate / biomass / colony formation | Assay-specific labels | State the endpoint establishing “growth.” |

### Chemicals and metabolites

| Node | Suggested grounding | Role |
|---|---|---|
| Sodium ion | CHEBI:29101 | Ionic stress and electrochemical homeostasis. |
| Potassium ion | CHEBI:29103 | Early osmotic adjustment and intracellular ion balance. |
| Proton | CHEBI:15378 | Coupled substrate in Na⁺/H⁺ antiport. |
| Glycine betaine | CHEBI:17750 | Compatible solute. |
| Choline | CHEBI:15354 | BetT substrate and glycine-betaine precursor. |
| L-proline | CHEBI:17203 | Compatible solute and engineered ectoine substitute. |
| L-glutamate | CHEBI:29985 | Compatible solute/counterion in some taxa. |
| Trehalose | CHEBI:27082 | Compatible solute in multiple microbial groups. |
| Ectoine | CHEBI:14341 | Major bacterial compatible solute. |
| Water | CHEBI:15377 | Moves across the membrane following osmotic gradients. |

### Genes, proteins, transporters, and complexes

These symbols are **family or taxon-context labels**, not universal ortholog identifiers. UniProt accessions should be added only after selecting a specific organism and strain.

- **BetT:** osmoregulated choline transporter.
- **BetA/BetB:** choline-to-glycine-betaine oxidation pathway.
- **Opu and ProU family ABC transporters; OpuD/BetH:** compatible-solute uptake.
- **EctABC:** ectoine biosynthesis module.
- **ProB/ProA/ProC:** proline biosynthesis module.
- **PutA:** proline catabolism.
- **TrkA/TrkH and Kdp:** K⁺ uptake systems.
- **Nha, Cha, Mnh/Mrp-family Na⁺/H⁺ antiporters:** Na⁺ extrusion/ion homeostasis.
- **MscL/MscS-family mechanosensitive channels:** solute release during downshock.
- **GroES/GroEL, catalase, thioredoxin/peroxiredoxin systems:** auxiliary protein-folding and oxidative-damage responses.

### Processes, functions, and cellular locations

- Compatible-solute biosynthesis and transmembrane import.
- Potassium-ion uptake and homeostasis.
- Sodium-ion export and proton-coupled antiport.
- Cellular response to hyperosmotic stress — **GO:0006972**.
- Maintenance of turgor, cytoplasmic hydration, and ion homeostasis.
- Mechanosensitive-channel-mediated solute release.
- Protein folding/chaperone response and reactive-oxygen-species detoxification.
- Cytoplasm and plasma membrane as the principal relevant locations.

## Candidate causal edges

Predicates below are deliberately simple and YAML-friendly. “Core” means suitable for a generic osmoadaptation subgraph; it does not mean that the edge alone establishes the exact 1–3% range.

| # | Subject — predicate — object | Reference and supporting snippet | Interpretation and curation status |
|---:|---|---|---|
| 1 | Increased extracellular NaCl — **increases** — extracellular osmolarity | Bremer & Krämer describe external-osmolarity changes as driving water flux, hydration, crowding, and turgor changes. (bremer2019responsesofmicroorganisms pages 3-5) | **Core; strong/general.** Record concentration and medium. |
| 2 | Increased extracellular osmolarity — **causes** — water efflux / reduced cellular hydration | Review evidence: hyperosmotic stress threatens cells with dehydration and altered turgor. (bremer2019responsesofmicroorganisms pages 3-5) | **Core; strong/general.** The physical link is broader than NaCl. |
| 3 | Hyperosmotic stress — **increases transiently** — intracellular K⁺ accumulation | Review evidence identifies temporary K⁺ elevation as an emergency response before longer-term organic-osmolyte adjustment. (bremer2019responsesofmicroorganisms pages 3-5) | **Core with temporal qualifier.** Do not encode persistent high K⁺ as universal. |
| 4 | Intracellular K⁺ accumulation — **contributes to** — short-term osmotic balance | Same general response sequence. (bremer2019responsesofmicroorganisms pages 3-5) | **Core; mechanistically supported**, but magnitude is taxon-dependent. |
| 5 | Hyperosmotic stress — **increases** — compatible-solute synthesis or import | “Cells prevent dehydration by accumulating compatible solutes (proline, glycine betaine, ectoine, trehalose) via synthesis or import.” (bremer2019responsesofmicroorganisms pages 3-5) | **Core; strongest generic mechanism.** |
| 6 | Compatible-solute accumulation — **promotes** — cytoplasmic hydration and growth under elevated osmolarity | Compatible solutes are described as physiologically compliant organic osmolytes used to sustain hydration. (bremer2019responsesofmicroorganisms pages 3-5) | **Core; strong/general**, although the exact growth-range endpoint remains unproven. |
| 7 | Hyperosmotic stress — **releases autoinhibition of / activates** — BetT | Yang et al.: BetT is locked in a low-activity state by its C-terminal domain without osmotic stress; hyperosmotic activation involves release of autoinhibition. Published August 2024. (yang2024structureandmechanism pages 1-2) | **Strong, current structural/functional evidence; taxon/pathway-specific.** |
| 8 | Activated BetT — **increases uptake of** — choline | Yang et al.: osmotic activation of BetT promotes external choline uptake. (yang2024structureandmechanism pages 1-2) | **Curate conditionally** where BetT is present. |
| 9 | Imported choline — **provides substrate for** — glycine-betaine synthesis | Yang et al. identify the choline–glycine-betaine pathway as important for bacterial survival in hyperosmotic environments. (yang2024structureandmechanism pages 1-2) | **Strong pathway edge**, but downstream BetA/BetB should be strain-grounded. |
| 10 | Glycine-betaine accumulation — **promotes** — osmoprotection | The 2024 BetT study describes glycine betaine as the osmoprotective product of imported choline. (yang2024structureandmechanism pages 1-2) | **Strong but not universal.** Availability of choline/betaine in the medium is a modifier. |
| 11 | ectABC deletion — **reduces** — high-NaCl growth | In *Halomonas elongata*, the ectoine-deficient KA1 strain “could not grow in minimal media containing more than 4% NaCl.” Published September 2024. (khanh2024metabolicpathwayengineering pages 1-2) | **Direct causal genetic evidence; taxon-specific and above target range.** Useful mechanistic support, not proof of METPO:1000470. |
| 12 | Engineered proBm1AC plus putA deletion — **increases** — intracellular proline | Engineered HN6 accumulated **353.1 ± 40.5 µmol proline g⁻¹ fresh cell weight**; the modifications install feedback-resistant biosynthesis and block proline catabolism. (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6) | **Strong causal engineering evidence.** Represent the complete genotype, not proline alone. |
| 13 | Intracellular proline accumulation — **restores/promotes** — growth at 8% NaCl in ectoine-deficient *H. elongata* | HN6 grew at **8% NaCl**, whereas ectoine-deficient KA1 failed above 4%. (khanh2024metabolicpathwayengineering pages 1-2) | **Strong causal exemplar** showing osmolyte substitutability; out of the 1–3% scope. |
| 14 | Elevated NaCl — **increases expression of** — glycine-betaine synthesis and uptake systems | In *Chromohalobacter salexigens* ANJ207, qRT-PCR showed increased transcripts for glycine-betaine biosynthesis and OpuABC uptake genes at high salt. (srivastava2022transcriptomeanalysisto pages 1-2) | **Moderate omics association; taxon-specific**, tested at 5–25% NaCl. |
| 15 | Elevated NaCl — **increases** — ectoine/β-hydroxyectoine and proline-related osmoadaptation programs | ANJ207 transcriptomics identified coordinated compatible-solute systems; 93 transcripts rose and 1,149 fell from 5% to 10% NaCl, while 1,954 rose and 1,287 fell from 10% to 25%. (srivastava2022transcriptomeanalysisto pages 1-2) | **Association, not direct causation; out-of-range.** |
| 16 | Elevated NaCl — **activates** — Trk-mediated K⁺ uptake | *Oceanobacillus picturae* DY09 activated trkA/trkH while Kdp was downregulated under its salt treatments. (nie2025ahalophilicbacterium pages 13-15) | **Taxon-specific.** Supports pathway alternatives rather than a universal Trk/Kdp direction. |
| 17 | Elevated NaCl — **increases expression of** — Na⁺/H⁺ antiporters | DY09 upregulated chaA, nhaC, nhaD, and mnhA–E at 12–20% NaCl, interpreted as Na⁺ extrusion. (nie2025ahalophilicbacterium pages 13-15) | **Uncertain for 1–3%; high-salt transcriptomics.** Curate only with taxon and assay context. |
| 18 | Na⁺/H⁺ antiport — **promotes** — intracellular Na⁺ homeostasis | The DY09 study connects antiporter induction with Na⁺ export and ion homeostasis. (nie2025ahalophilicbacterium pages 13-15) | **Mechanistically credible**, but transcript abundance is not transport-flux measurement. |
| 19 | High salt — **increases** — antioxidant and chaperone responses | DY09 showed ~6-fold/~3-fold groES/groEL induction at 4% and ~12-fold/~2-fold at 20%; antioxidant and repair genes also rose, with yqjC about 15-fold. (nie2025ahalophilicbacterium pages 13-15) | **Auxiliary, taxon-specific response.** Do not make it a defining cause of the target trait. |
| 20 | Hypoosmotic downshock — **activates** — mechanosensitive-channel solute release | The general review states that cells rapidly expel organic and inorganic compounds through mechanosensitive channels after downshock. (bremer2019responsesofmicroorganisms pages 3-5) | **Strong/general but peripheral.** Include only if the graph models changing salinity or recovery from salt. |
| 21 | Simultaneous compatible-solute and K⁺ accumulation — **supports** — long-term adaptation to extreme salinity | *Natranaerobius thermophilus* used Opu/ProU/SSS transport, glutamate/proline synthesis, and K⁺ homeostasis at **2.5–4.3 M Na⁺**. Published May 2024. (xing2024thepolyextremophilenatranaerobius pages 1-2) | **Do not transfer directly.** This is an extreme-halophile, polyextremophile result far above 1–3% NaCl. |

## Recommended minimal graph revision

A conservative TraitMech graph should prioritize the following chain:

1. **NaCl exposure near 1–3% w/v** → increased extracellular osmolarity.
2. Increased extracellular osmolarity → water efflux/reduced hydration and turgor.
3. Hyperosmotic stress → transient K⁺ uptake.
4. Hyperosmotic stress → compatible-solute synthesis/import.
5. Compatible-solute accumulation → improved cytoplasmic hydration and biochemical function.
6. Improved osmotic balance → supports growth within the measured NaCl interval.

Optional branches should be added only when supported for the curated taxon:

- BetT → choline uptake → glycine-betaine synthesis/accumulation.
- EctABC → ectoine synthesis.
- ProBAC and reduced PutA activity → proline accumulation.
- Nha/Cha/Mrp-family antiport → Na⁺ extrusion.
- Trk/Kdp → K⁺ uptake.

The final edge—**osmotic balance supports growth across 1–3% NaCl**—should presently be marked **inferred/general**, unless a strain-level perturbation study measures growth specifically within that interval.

## Recent developments and quantitative evidence

### 2024 structural mechanism

Cryo-EM and functional work resolved the osmoregulated BetT transporter in apo and choline-bound states. The model is not merely expression-based: BetT’s C-terminal domain autoinhibits transport under low stress, and hyperosmotic conditions release this restraint, increasing choline uptake for glycine-betaine production. This provides a precise molecular edge from osmotic signal to compatible-solute precursor transport. (yang2024structureandmechanism pages 1-2)

### 2024 causal metabolic engineering

The strongest recent intervention evidence comes from *H. elongata*. Removing ectoine synthesis caused failure above 4% NaCl, whereas replacing `ectABC` with feedback-resistant `proBm1AC` and deleting proline-catabolic `putA` enabled growth at 8% NaCl and accumulation of **353.1 ± 40.5 µmol proline g⁻¹ fresh cell weight**. The experiment demonstrates that one compatible solute can substitute functionally for another, but it does not establish the natural mechanism of a 1–3% range phenotype. (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6)

### 2024 multi-omics at extreme salinity

Proteomics, transcript measurements, and intracellular metabolite/ion measurements in *N. thermophilus* support a hybrid strategy involving glycine betaine, proline, glutamate, and K⁺. However, the study used **2.5–4.3 M Na⁺**, versus approximately 0.17–0.51 M NaCl for the target interval, so its value is conceptual rather than trait-specific. (xing2024thepolyextremophilenatranaerobius pages 1-2)

### Transcriptomic scale and limitations

In *C. salexigens* ANJ207, shifting from 5% to 10% NaCl yielded **93 upregulated and 1,149 downregulated transcripts**; shifting from 10% to 25% yielded **1,954 upregulated and 1,287 downregulated transcripts**. Glycine-betaine uptake/synthesis, potassium transport, catalase/OsmC-like responses, and other stress systems changed. These statistics illustrate that salt tolerance is a systems phenotype, but differential expression alone does not demonstrate that any one gene determines the growth range. (srivastava2022transcriptomeanalysisto pages 1-2)

## Applications and real-world relevance

1. **Saline bioprocessing and cell factories:** the engineered *H. elongata* strain couples salt tolerance with proline production, suggesting use of saline waste biomass for proline-rich single-cell feed. This is a concrete implementation of causal osmolyte-pathway engineering. (khanh2024metabolicpathwayengineering pages 1-2)
2. **Agriculture and saline-soil inoculants:** salt-tolerant plant-growth-promoting bacteria are being investigated as biofertilizers. Genome-resolved analysis of hypersaline microbiomes recovered 67 MAGs; among medium/high-quality MetaSPAdes MAGs, reported traits included salt tolerance in **91.3%**, exopolysaccharide potential in **95.6%**, and antioxidant potential in **60.86%**. These are genomic predictions and should not be treated as measured NaCl-range phenotypes.
3. **Wastewater and saline-environment biotechnology:** osmoadapted organisms can maintain metabolism where conventional strains lose activity. Nevertheless, performance depends on substrate availability, salinity dynamics, pH, and community interactions, not merely possession of osmolyte genes.
4. **Transporter and antimicrobial research:** BetT and mechanosensitive channels provide structurally tractable examples of stress-gated membrane transport. For this trait graph, these applications are secondary to their mechanistic value.

## Expert synthesis

Authoritative reviews favor a staged and dynamic model rather than a single “salt-tolerance gene”: physical water flux and turgor change occur first, inorganic-ion adjustment follows rapidly, and compatible-solute systems support sustained acclimation. Mechanosensitive channels protect against the reverse transition. (bremer2019responsesofmicroorganisms pages 3-5) Recent studies refine this model by showing transporter autoinhibition and activation at atomic/structural resolution and by genetically replacing one principal osmolyte with another. (khanh2024metabolicpathwayengineering pages 1-2, yang2024structureandmechanism pages 1-2)

For `nacl_range_mid1.yaml`, the most defensible strategy is therefore a **small generic osmotic-balance backbone plus optional taxon-specific modules**. A graph that directly assigns BetT, ectoine, a particular antiporter, or the salt-in strategy to every organism annotated with **METPO:1000470** would overstate the evidence.

## Warnings: claims not yet ready for unqualified curation

- **Do not equate 1–3% optimum with 1–3% full growth range.** The supplied evidence statement and definition should be checked against the exact wording of DOI **10.1093/femsre/fuy009** before using it as the sole scope authority.
- **Do not assert that halotolerant organisms require NaCl.** Growth at 0% must be measured.
- **Do not transfer mechanisms from extreme halophiles directly.** Evidence at 8–25% NaCl or 2.5–4.3 M Na⁺ is mechanistically informative but outside the target interval. (nie2025ahalophilicbacterium pages 13-15, xing2024thepolyextremophilenatranaerobius pages 1-2, srivastava2022transcriptomeanalysisto pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)
- **Do not infer causality from transcript upregulation alone.** Require deletion, complementation, transport/metabolite measurements, or a controlled growth phenotype.
- **Do not use gene names without taxon grounding.** Trk, Kdp, BetT, Opu, Nha, Cha, and Mrp/Mnh families have paralogs and distinct regulation.
- **Do not make MscL/MscS core causes of growth at elevated NaCl.** Their clearest role is survival during hypoosmotic downshock. (bremer2019responsesofmicroorganisms pages 3-5)
- **Do not conflate total salinity, Na⁺ molarity, and NaCl % w/v.** Convert units and record the complete ionic medium.
- **Do not curate chaperone or antioxidant induction as sufficient for the phenotype.** These are auxiliary responses with primarily taxon-specific expression evidence. (nie2025ahalophilicbacterium pages 13-15, srivastava2022transcriptomeanalysisto pages 1-2)
- **Do not infer trait presence from metagenomic gene content alone.** The target is a measured growth-range phenotype.

## DOI-first bibliography

1. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology*. **September 2024**. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 2-6)
2. **Yang T, et al.** “Structure and mechanism of the osmoregulated choline transporter BetT.” *Science Advances*. **August 2024**. DOI: [10.1126/sciadv.ado6229](https://doi.org/10.1126/sciadv.ado6229). (yang2024structureandmechanism pages 1-2)
3. **Xing Q, et al.** “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.” *Applied and Environmental Microbiology*. **May 2024**. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
4. **Dindhoria K, Kumar R, Bhargava B, Kumar R.** “Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils.” *mSystems*. **March 2024**. DOI: [10.1128/msystems.01050-23](https://doi.org/10.1128/msystems.01050-23).
5. **Srivastava AK, et al.** “Transcriptome Analysis to Understand Salt Stress Regulation Mechanism of *Chromohalobacter salexigens* ANJ207.” *Frontiers in Microbiology*. **June 2022**. DOI: [10.3389/fmicb.2022.909276](https://doi.org/10.3389/fmicb.2022.909276). (srivastava2022transcriptomeanalysisto pages 1-2)
6. **Bremer E, Krämer R.** “Responses of Microorganisms to Osmotic Stress.” *Annual Review of Microbiology* 73:313–334. **September 2019**. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). (bremer2019responsesofmicroorganisms pages 3-5)
7. **Oren A.** “Microbial life at high salt concentrations: phylogenetic and metabolic diversity.” *Saline Systems*. **April 2008**. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2).
8. **Existing supplied evidence:** DOI [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). Its exact definition/range wording should be verified before final ontology-scope curation.

References

1. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

2. (yang2024structureandmechanism pages 1-2): Tianjiao Yang, Yuwei Nian, Huajian Lin, Jing Li, Xiang Lin, Tianming Li, Ruiying Wang, Longfei Wang, Gwyn A. Beattie, Jinru Zhang, and Minrui Fan. Structure and mechanism of the osmoregulated choline transporter bett. Science Advances, Aug 2024. URL: https://doi.org/10.1126/sciadv.ado6229, doi:10.1126/sciadv.ado6229. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (nie2025ahalophilicbacterium pages 13-15): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

4. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

5. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

6. (khanh2024metabolicpathwayengineering pages 2-6): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

7. (srivastava2022transcriptomeanalysisto pages 1-2): Alok Kumar Srivastava, Ruchi Srivastava, Anjney Sharma, Akhilendra Pratap Bharati, Jagriti Yadav, Alok Kumar Singh, Praveen Kumar Tiwari, Anchal Kumar Srivatava, Hillol Chakdar, Prem Lal Kashyap, and Anil Kumar Saxena. Transcriptome analysis to understand salt stress regulation mechanism of chromohalobacter salexigens anj207. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.909276, doi:10.3389/fmicb.2022.909276. This article has 25 citations and is from a peer-reviewed journal.