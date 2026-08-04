---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:05:52.321922'
end_time: '2026-08-04T12:12:38.225087'
duration_seconds: 405.9
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: urease activity
  trait_identifier: traitmech:000077
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: urease_activity
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological enzyme-activity phenotype in which a cell produces urease,
    which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH;
    it is the basis of the diagnostic urease test.
  parent_traits: METPO:1000059
  synonyms: urease-positive
  evidence_summary: 'DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger
    review the molecular biology of microbial ureases that hydrolyze urea to ammonia
    and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review
    the significance and regulation of microbial ureases.)'
  causal_graph_summary: 'urease_activity_urea_hydrolysis: 11 nodes, 10 edges'
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
- **Trait label:** urease activity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000077
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces urease, which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH; it is the basis of the diagnostic urease test.
- **Parent traits:** METPO:1000059
- **Synonyms:** urease-positive
- **Existing evidence:** DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger review the molecular biology of microbial ureases that hydrolyze urea to ammonia and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review the significance and regulation of microbial ureases.)
- **Existing causal graph summary:** urease_activity_urea_hydrolysis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **urease activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/urease_activity.yaml`.

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
- **Trait label:** urease activity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000077
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces urease, which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH; it is the basis of the diagnostic urease test.
- **Parent traits:** METPO:1000059
- **Synonyms:** urease-positive
- **Existing evidence:** DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger review the molecular biology of microbial ureases that hydrolyze urea to ammonia and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review the significance and regulation of microbial ureases.)
- **Existing causal graph summary:** urease_activity_urea_hydrolysis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **urease activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/urease_activity.yaml`.

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


# Curation report: microbial urease activity

## Trait record and scope

- **Trait:** urease activity
- **Identifier:** `traitmech:000077`
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000059`
- **Synonym:** urease-positive

This trait should denote the **demonstrated physiological capacity of a microbial cell or preparation to produce active urease and hydrolyze urea**. The core reaction is commonly summarized as urea + water → ammonia + carbamate, followed by spontaneous carbamate decomposition to additional ammonia and carbon dioxide/bicarbonate. Urease is **EC 3.5.1.5**, generally a cytosolic, dinuclear nickel enzyme. Its ammonia output commonly raises local pH and is the basis of colorimetric diagnostic urease tests. (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1)

### Recommended boundaries

Include:

1. Active enzyme formation, including structural urease subunits and nickel-dependent maturation.
2. Urea access when it is mechanistically necessary for expressed activity.
3. Urea hydrolysis and immediate products.
4. Direct assay observables such as ammonia release or indicator-detected alkalinization.

Treat as **downstream context-specific branches**, rather than defining features:

- acid resistance and gastric colonization in *Helicobacter pylori*;
- urea utilization as a nitrogen source;
- urinary struvite/carbonate-apatite formation;
- calcium-carbonate biocementation;
- host-cell injury from ammonia.

Do not equate urease activity with merely possessing `ure` genes. Activity additionally depends on expression, assembly, nickel availability, accessory proteins, and assay conditions. Conversely, a negative pH-indicator assay does not necessarily prove absence of urease if substrate uptake, nickel, cell density, incubation time, buffering, or enzyme expression is limiting.

Nearby but distinct traits include urea transport, nickel uptake/homeostasis, acid tolerance, ammonia production by other pathways, nitrogen-source utilization, carbonate precipitation, urinary-stone formation, and urea amidolyase activity.

## Candidate nodes

### Trait and process nodes

- urease activity — `traitmech:000077`
- urease activity / urea amidohydrolase activity — `GO:0009039`; `EC:3.5.1.5`
- urea catabolic process — `GO:0019627`
- urease maturation / nickel insertion — label-only candidate pending exact ontology review
- alkalinization, acid resistance, biomineralization, and diagnostic urease-test positivity — label-only or separately grounded downstream nodes

### Genes, proteins, and complexes

- `ureA`, `ureB`, `ureC`: structural genes/subunits. In the canonical bacterial architecture, UreA/γ, UreB/β, and catalytic UreC/α form `(UreABC)3`; *Helicobacter* uses a fused/two-subunit variant, so one universal stoichiometry should not be asserted. (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1)
- UreD, or its homolog UreH; UreE; UreF; UreG: urease-accessory maturation proteins.
- UreG: P-loop GTPase involved in nickel delivery.
- UreE: nickel-binding metallochaperone.
- apo-urease and mature holo-urease complexes.
- UreI: acid-gated urea channel; **taxon-specific to the *H. pylori* mechanistic branch**, not a generic requirement.

Use label-only nodes in the initial YAML unless a taxon is fixed; UniProt identifiers differ among organisms and should not be generalized.

### Chemicals and cofactors

High-confidence candidates include urea, water, ammonia/ammonium, carbamate, carbon dioxide, bicarbonate/carbonate, Ni²⁺, GTP/GDP, and a carbamylated active-site lysine. The mature active site contains two nickel ions coordinated around a carbamylated lysine and other ligands. (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1)

Context-specific candidates include Ca²⁺, Mg²⁺, phosphate, calcium carbonate, struvite, and carbonate apatite. Candidate inhibitors include acetohydroxamic acid, 2-mercaptoacetamide, lactic acid, bismuth compounds, and noncognate metal ions. These should not all be represented as universal physiological regulators. (burne2000bacterialureasesin pages 4-6, nim2019thematurationpathway pages 8-10, szczerbiec2024antibacterialpropertiesand pages 5-7)

### Environmental and experimental factors

- extracellular urea concentration and substrate access;
- nickel availability and competing metals;
- pH, temperature, oxygen regime, buffering capacity, incubation time, and cell density;
- calcium, magnesium, phosphate, and carbonate availability for mineralization;
- gastric acidity for the *H. pylori* branch;
- urine or synthetic urine for the *Proteus* branch;
- phenol-red or equivalent pH indicator for diagnostic assays.

## Candidate causal edges

The following compact table captures the recommended graph backbone and explicitly separates generic mechanisms from taxon- or assay-specific extensions.

| subject | predicate | object | evidence level/scope | DOI |
|---|---|---|---|---|
| urease (EC 3.5.1.5) | catalyzes hydrolysis of | urea to ammonia + carbon dioxide/carbamate-derived bicarbonate | Strong; generic microbial urease mechanism (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1) | 10.3390/inorganics7070085; 10.1074/jbc.r112.446526 |
| urease | requires cofactor | dinuclear Ni2+ metallocenter | Strong; generic (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1) | 10.3390/inorganics7070085; 10.1074/jbc.r112.446526 |
| UreA/UreB/UreC structural subunits | assemble into | active urease enzyme complex | Strong; generic bacterial architecture, with Helicobacter-specific variation noted (nim2019thematurationpathway pages 1-3, farrugia2013biosynthesisofthe pages 1-1) | 10.3390/inorganics7070085; 10.1074/jbc.r112.446526 |
| UreD/UreH + UreE + UreF + UreG | enable maturation of | nickel urease apoprotein | Strong; generic maturation pathway (nim2019thematurationpathway pages 1-3, nim2019thematurationpathway pages 8-10, farrugia2013biosynthesisofthe pages 1-1) | 10.3390/inorganics7070085; 10.1074/jbc.r112.446526 |
| UreE | delivers nickel to | UreG | Moderate-strong; generic model from maturation reviews (nim2019thematurationpathway pages 1-3, nim2019thematurationpathway pages 8-10) | 10.3390/inorganics7070085 |
| GTP binding/hydrolysis by UreG | regulates | nickel delivery and urease activation complex formation | Strong; generic maturation mechanism (nim2019thematurationpathway pages 8-10, farrugia2013biosynthesisofthe pages 1-1) | 10.3390/inorganics7070085; 10.1074/jbc.r112.446526 |
| UreI urea channel | increases substrate access of | urea to urease under acidic conditions | Strong but taxon-specific to *Helicobacter pylori* (nim2019thematurationpathway pages 1-3) | 10.3390/inorganics7070085 |
| urease activity | increases production of | ammonia | Strong; generic (burne2000bacterialureasesin pages 4-6, szczerbiec2024antibacterialpropertiesand pages 1-2, stabnikov2024microbialproducerof pages 1-3) | 10.1016/S1286-4579(00)00312-9; 10.1038/s41598-024-51323-0; 10.24263/2304-974x-2024-13-2-10 |
| ammonia production from ureolysis | raises | local/environmental pH | Strong; generic assay-relevant consequence (burne2000bacterialureasesin pages 4-6, szczerbiec2024antibacterialpropertiesand pages 1-2, stabnikov2024microbialproducerof pages 1-3) | 10.1016/S1286-4579(00)00312-9; 10.1038/s41598-024-51323-0; 10.24263/2304-974x-2024-13-2-10 |
| intrabacterial urease activity | enables | acid resistance | Strong but taxon-specific to *H. pylori* (burne2000bacterialureasesin pages 4-6) | 10.1016/S1286-4579(00)00312-9 |
| ureolytic pH increase in urine | promotes precipitation of | struvite and carbonate apatite | Strong but urinary-pathogen-specific, especially *Proteus mirabilis* and related ureolytic uropathogens (burne2000bacterialureasesin pages 4-6, szczerbiec2024antibacterialpropertiesand pages 1-2, szczerbiec2024antibacterialpropertiesand pages 7-8) | 10.1016/S1286-4579(00)00312-9; 10.1038/s41598-024-51323-0 |
| urease-driven alkalinization + carbonate generation | promotes precipitation of | calcium carbonate (CaCO3) | Moderate; application-focused MICP/biocementation context, not universal phenotype consequence (stabnikov2024microbialproducerof pages 1-3) | 10.24263/2304-974x-2024-13-2-10 |
| lactic acid | competitively inhibits | urease activity | Strong for 2024 experimental study; not universal natural inhibitor claim (szczerbiec2024antibacterialpropertiesand pages 5-7, szczerbiec2024antibacterialpropertiesand pages 8-11) | 10.1038/s41598-024-51323-0 |
| lactic acid inhibition of urease | reduces | ammonia release, pH rise, and urinary crystallization | Strong for *P. mirabilis* synthetic-urine system in 2024 study; assay/system-specific (szczerbiec2024antibacterialpropertiesand pages 5-7, szczerbiec2024antibacterialpropertiesand pages 2-3, szczerbiec2024antibacterialpropertiesand pages 7-8) | 10.1038/s41598-024-51323-0 |


*Table: This table summarizes curation-ready causal edges for microbial urease activity, separating broadly supported generic mechanisms from taxon- or application-specific downstream effects. It is useful as a compact starting point for TraitMech graph curation of traitmech:000077.*

### Supporting snippets and curation notes

| Proposed triple | Source-backed snippet | Curation interpretation |
|---|---|---|
| urease — catalyzes — urea hydrolysis | “Urease catalyzes urea hydrolysis into CO2 and carbamate,” with carbamate decomposing to ammonia and CO2. (nim2019thematurationpathway pages 1-3) | **Curate.** Central defining edge; normalize products consistently with the chosen reaction ontology. |
| urease — has required cofactor — dinuclear Ni²⁺ center | The enzyme contains “two Ni²⁺ ions coordinated by carbamylated lysine.” (nim2019thematurationpathway pages 1-3) | **Curate.** Strong, broadly conserved mechanism. |
| UreA/UreB/UreC — assemble into — urease complex | Bacterial urease is described as three structural subunits, UreC/α, UreB/β, and UreA/γ. (nim2019thematurationpathway pages 1-3) | **Curate with architecture qualifier.** Do not force this organization onto fused or two-subunit ureases. |
| UreD/UreH, UreE, UreF, UreG — enable — apo-urease activation | Nickel insertion is a “GTP-dependent process” assisted by these four accessory proteins. (farrugia2013biosynthesisofthe pages 1-1) | **Curate.** UreD and UreH should be alternatives/homologs, not simultaneous universal requirements. |
| UreE — transfers Ni²⁺ to — UreG | Review model gives the cascade HypA → UreE → UreG → urease. (nim2019thematurationpathway pages 8-10) | **Curate cautiously.** Strong maturation model, but upstream HypA is not universal. |
| UreG GTP hydrolysis — regulates — nickel delivery/activation | GTP-dependent switching governs partner binding and formation of the activation complex; reported *H. pylori* UreG values were Km 13 ± 4 mM and kcat 6.4 ± 0.6 × 10⁻³ s⁻¹. (nim2019thematurationpathway pages 8-10) | **Curate generic edge; retain kinetic values only as taxon-specific evidence annotations.** |
| UreI — promotes — urea access under acid stress | UreI is described as an acid-gated channel enabling acidic gastric colonization. (nim2019thematurationpathway pages 1-3) | **Taxon-specific.** Place only in an *H. pylori* subgraph. |
| ureolysis — increases — ammonia and local pH | Urease-generated ammonia and CO₂ create neutral microenvironments and protect bacteria from acid killing. (burne2000bacterialureasesin pages 4-6) | **Curate ammonia and alkalinization edges.** Acid resistance should remain a contextual consequence. |
| urinary alkalinization — promotes — struvite/carbonate-apatite precipitation | Ureolytic urinary pathogens elevate urine pH, precipitating struvite and carbonate apatite. (burne2000bacterialureasesin pages 4-6) | **Curate only in urinary-environment branch.** Requires Mg²⁺/phosphate or Ca²⁺/phosphate context. |
| urease-driven carbonate and pH increase — promotes — CaCO₃ precipitation | The 2024 biocementation study links ammonia/OH⁻ production, pH rise, carbonate release, and insoluble CaCO₃. (stabnikov2024microbialproducerof pages 1-3) | **Application-specific.** Not an intrinsic consequence without calcium and suitable saturation conditions. |
| lactic acid — competitively inhibits — *P. mirabilis* urease | Km increased from 5.06 to 10.88 mM while Vmax remained 0.44–0.45 mM/min; IC50 was 38 ± 0.45 mM. (szczerbiec2024antibacterialpropertiesand pages 5-7) | **Curate as experimental inhibitor evidence**, not as a universal endogenous regulatory edge. |

## Recent developments and quantitative evidence

### Urinary-stone suppression, 2024

A 2024 *Scientific Reports* study tested urinary *Lactobacillus* strains against *P. mirabilis* in synthetic urine. It followed the chain urease activity → ammonia release → pH rise → struvite/apatite crystallization using time-resolved pH, ammonia, Ca²⁺/Mg²⁺, viable counts, and microscopy. Lactic acid acted competitively, and 22 mM completely suppressed crystallization after 24 h, whereas 1.4–2.8 mM delayed it for about four hours. Docking estimated binding energies of −8.22 kcal/mol for lactic acid and −5.40 kcal/mol for urea. These are promising mechanistic results but remain an in-vitro/synthetic-urine implementation. (szczerbiec2024antibacterialpropertiesand pages 5-7, szczerbiec2024antibacterialpropertiesand pages 2-3)

The same study reports that infectious stones comprise approximately 15% of urinary stones and that *Proteus* species can occur in up to 70% of infectious stones; all urinary *Proteus* isolates were described as urease producers. *L. gasseri* reduced *P. mirabilis* counts ten-fold and showed 72–97% antibacterial activity in tested conditions. These figures are useful context, not universal prevalence estimates across all populations. (szczerbiec2024antibacterialpropertiesand pages 1-2, szczerbiec2024antibacterialpropertiesand pages 7-8)

### Acid-tolerant biocementation, 2024

Stabnikov and colleagues selected *Staphylococcus saprophyticus* AU1 as an acid-urease producer. Reported maximum urease activity was 8.1 mM urea hydrolyzed per minute, with peak activity at pH 4.5–5.5, biomass reaching 6.9 g/L, and growth rate 0.15 h⁻¹. Treated sand reached water permeability of 2 × 10⁻⁵ m/s. Their process reduced urea consumption by 75%, intended to lower ammonia/ammonium emissions. This supports a practical MICP branch but is organism-, formulation-, and engineering-system-specific. (stabnikov2024microbialproducerof pages 1-3)

### Mechanistic and therapeutic interpretation

Authoritative reviews treat urease maturation—not only the catalytic active site—as a potential intervention point. The UreD/UreH–UreF–UreG activation complex, UreE-mediated nickel transfer, and GTP-dependent switching offer targets potentially more selective than broad metal chelation. Nevertheless, the exact nickel-transfer sequence and conformational mechanism remain incompletely resolved, so highly granular transfer edges should be annotated as mechanistic models rather than immutable universal steps. (nim2019thematurationpathway pages 8-10, farrugia2013biosynthesisofthe pages 1-1)

## Current applications

1. **Microbial identification:** rapid urease and Christensen-type tests detect ammonia-associated alkalinization. They measure an indirect output and require appropriate controls.
2. **Clinical pathogenesis:** urease supports *H. pylori* acid survival and drives *Proteus*-associated crystalline biofilms, catheter encrustation, and infection stones. (burne2000bacterialureasesin pages 4-6)
3. **Anti-virulence development:** active-site inhibitors, maturation inhibitors, probiotics, and organic acids can suppress ureolysis without necessarily requiring bactericidal activity. The 2024 lactic-acid study is a recent example. (szczerbiec2024antibacterialpropertiesand pages 5-7, szczerbiec2024antibacterialpropertiesand pages 8-11)
4. **Biogeotechnology:** ureolysis-induced CaCO₃ precipitation is used for soil consolidation, permeability reduction, and crack repair, although ammonia emissions are a major sustainability constraint. (stabnikov2024microbialproducerof pages 1-3)
5. **Agriculture and animal production:** urease controls urea-fertilizer nitrogen loss and ruminal urea turnover. These are important applications, but organism-level microbial trait graphs should not automatically include ecosystem-scale ammonia loss.

## Recommended YAML graph organization

Use a compact **generic backbone**:

`ureABC expression/assembly → apo-urease → UreD/E/F/G + Ni²⁺ + GTP-dependent maturation → active urease → urea hydrolysis → ammonia + carbon dioxide/bicarbonate → local pH increase → assay-positive urease phenotype`.

Add qualified branches for:

- `UreI → acidic urea influx → H. pylori acid resistance`;
- `urinary pH rise + Mg²⁺/phosphate → struvite`;
- `urinary pH rise + Ca²⁺/phosphate/carbonate → carbonate apatite`;
- `carbonate + Ca²⁺ + supersaturation → CaCO₃ biocementation`;
- `lactic acid or defined inhibitor → reduced urease activity`.

## Warnings: claims not yet suitable for unqualified curation

1. **Gene presence → phenotype:** insufficient without expression and maturation evidence.
2. **UreI as universal:** false; retain only for the relevant *Helicobacter* system.
3. **HypA as universal upstream nickel donor:** maturation-network cross-talk is organism-dependent.
4. **Universal UreABC stoichiometry:** contradicted by fused and two-subunit architectures.
5. **Urease activity → mineral precipitation without context:** precipitation requires ions, pH, saturation, and nucleation conditions.
6. **Urease activity → acid resistance or virulence:** supported in particular pathogens but not a defining general microbial consequence.
7. **Urease positivity → urea supports growth:** nitrogen assimilation requires downstream ammonia incorporation and should be represented separately.
8. **Lactic acid as a general physiological inhibitor:** current evidence is compelling but assay- and organism-specific.
9. **Exact CHEBI, Rhea, KEGG, or MetaCyc identifiers not verified here:** do not insert identifiers from memory. Retain label-only nodes until registry validation. `EC:3.5.1.5`, `GO:0009039`, and `GO:0019627` are the safest generic anchors.

## DOI-first bibliography

1. Nim YS, Wong KB. **The Maturation Pathway of Nickel Urease.** *Inorganics*. Published July 2019. DOI: [10.3390/inorganics7070085](https://doi.org/10.3390/inorganics7070085). (nim2019thematurationpathway pages 1-3, nim2019thematurationpathway pages 8-10)
2. Farrugia MA, Macomber L, Hausinger RP. **Biosynthesis of the Urease Metallocenter.** *Journal of Biological Chemistry*. Published May 2013. DOI: [10.1074/jbc.R112.446526](https://doi.org/10.1074/jbc.R112.446526). (farrugia2013biosynthesisofthe pages 1-1)
3. Burne RA, Chen YYM. **Bacterial ureases in infectious diseases.** *Microbes and Infection*. Published April 2000. DOI: [10.1016/S1286-4579(00)00312-9](https://doi.org/10.1016/S1286-4579(00)00312-9). (burne2000bacterialureasesin pages 4-6)
4. Szczerbiec D, Bednarska-Szczepaniak K, Torzewska A. **Antibacterial properties and urease suppression ability of Lactobacillus inhibit the development of infectious urinary stones caused by Proteus mirabilis.** *Scientific Reports*. Published January 2024. DOI: [10.1038/s41598-024-51323-0](https://doi.org/10.1038/s41598-024-51323-0). (szczerbiec2024antibacterialpropertiesand pages 5-7, szczerbiec2024antibacterialpropertiesand pages 1-2)
5. Stabnikov V, Udymovych V, Kovshar I, Stabnikov D. **Microbial producer of acid urease for its application in biocementation.** *Ukrainian Food Journal*. Published June 2024. DOI: [10.24263/2304-974X-2024-13-2-10](https://doi.org/10.24263/2304-974X-2024-13-2-10). (stabnikov2024microbialproducerof pages 1-3)

The supplied foundational reviews—Mobley and Hausinger (1989), DOI [10.1128/MR.53.1.85-108.1989](https://doi.org/10.1128/MR.53.1.85-108.1989), and Mobley, Island, and Hausinger (1995), DOI [10.1128/MR.59.3.451-480.1995](https://doi.org/10.1128/MR.59.3.451-480.1995)—remain appropriate provenance for the existing graph, but the maturation review and 2024 application studies provide more current support for extending and qualifying it.

References

1. (nim2019thematurationpathway pages 1-3): Yap Shing Nim and Kam-Bo Wong. The maturation pathway of nickel urease. Inorganics, 7:85, Jul 2019. URL: https://doi.org/10.3390/inorganics7070085, doi:10.3390/inorganics7070085. This article has 56 citations.

2. (farrugia2013biosynthesisofthe pages 1-1): Mark A. Farrugia, Lee Macomber, and Robert P. Hausinger. Biosynthesis of the urease metallocenter. Journal of Biological Chemistry, 288:13178-13185, May 2013. URL: https://doi.org/10.1074/jbc.r112.446526, doi:10.1074/jbc.r112.446526. This article has 152 citations and is from a domain leading peer-reviewed journal.

3. (burne2000bacterialureasesin pages 4-6): Robert A Burne and Yi-Ywan M Chen. Bacterial ureases in infectious diseases. Microbes and infection, 2 5:533-42, Apr 2000. URL: https://doi.org/10.1016/s1286-4579(00)00312-9, doi:10.1016/s1286-4579(00)00312-9. This article has 491 citations and is from a peer-reviewed journal.

4. (nim2019thematurationpathway pages 8-10): Yap Shing Nim and Kam-Bo Wong. The maturation pathway of nickel urease. Inorganics, 7:85, Jul 2019. URL: https://doi.org/10.3390/inorganics7070085, doi:10.3390/inorganics7070085. This article has 56 citations.

5. (szczerbiec2024antibacterialpropertiesand pages 5-7): Dominika Szczerbiec, Katarzyna Bednarska-Szczepaniak, and Agnieszka Torzewska. Antibacterial properties and urease suppression ability of lactobacillus inhibit the development of infectious urinary stones caused by proteus mirabilis. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-51323-0, doi:10.1038/s41598-024-51323-0. This article has 23 citations and is from a peer-reviewed journal.

6. (szczerbiec2024antibacterialpropertiesand pages 1-2): Dominika Szczerbiec, Katarzyna Bednarska-Szczepaniak, and Agnieszka Torzewska. Antibacterial properties and urease suppression ability of lactobacillus inhibit the development of infectious urinary stones caused by proteus mirabilis. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-51323-0, doi:10.1038/s41598-024-51323-0. This article has 23 citations and is from a peer-reviewed journal.

7. (stabnikov2024microbialproducerof pages 1-3): Viktor Stabnikov, Viktor Udymovych, Iryna Kovshar, and Dmytro Stabnikov. Microbial producer of acid urease for its application in biocementation. Ukrainian Food Journal, 13:331-350, Jun 2024. URL: https://doi.org/10.24263/2304-974x-2024-13-2-10, doi:10.24263/2304-974x-2024-13-2-10. This article has 2 citations.

8. (szczerbiec2024antibacterialpropertiesand pages 7-8): Dominika Szczerbiec, Katarzyna Bednarska-Szczepaniak, and Agnieszka Torzewska. Antibacterial properties and urease suppression ability of lactobacillus inhibit the development of infectious urinary stones caused by proteus mirabilis. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-51323-0, doi:10.1038/s41598-024-51323-0. This article has 23 citations and is from a peer-reviewed journal.

9. (szczerbiec2024antibacterialpropertiesand pages 8-11): Dominika Szczerbiec, Katarzyna Bednarska-Szczepaniak, and Agnieszka Torzewska. Antibacterial properties and urease suppression ability of lactobacillus inhibit the development of infectious urinary stones caused by proteus mirabilis. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-51323-0, doi:10.1038/s41598-024-51323-0. This article has 23 citations and is from a peer-reviewed journal.

10. (szczerbiec2024antibacterialpropertiesand pages 2-3): Dominika Szczerbiec, Katarzyna Bednarska-Szczepaniak, and Agnieszka Torzewska. Antibacterial properties and urease suppression ability of lactobacillus inhibit the development of infectious urinary stones caused by proteus mirabilis. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-51323-0, doi:10.1038/s41598-024-51323-0. This article has 23 citations and is from a peer-reviewed journal.