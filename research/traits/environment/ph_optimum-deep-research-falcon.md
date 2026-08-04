---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:34:11.433934'
end_time: '2026-08-04T02:41:02.249242'
duration_seconds: 410.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum
  trait_identifier: METPO:1000331
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits that represents the external pH
    conditions at which an organism exhibits the most efficient growth and reproduction.
  parent_traits: METPO:1000531, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports the external pH at which cytoplasmic pH is best maintained as the operational
    definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force
    (pH-homeostasis review supports the balanced proton motive force at the optimal
    external pH as the mechanism enabling maximal growth.)'
  causal_graph_summary: 'ph_optimum_balanced_homeostasis: 12 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000331
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that represents the external pH conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000531, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic pH is best maintained as the operational definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the balanced proton motive force at the optimal external pH as the mechanism enabling maximal growth.)
- **Existing causal graph summary:** ph_optimum_balanced_homeostasis: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **pH optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum.yaml`.

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
- **Trait label:** pH optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000331
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that represents the external pH conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000531, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic pH is best maintained as the operational definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the balanced proton motive force at the optimal external pH as the mechanism enabling maximal growth.)
- **Existing causal graph summary:** ph_optimum_balanced_homeostasis: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **pH optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum.yaml`.

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


# Curation report: microbial pH optimum

## Executive scope

**Target:** `METPO:1000331` (**pH optimum**; ENVIRONMENT; CLASS; REVIEWED).

The trait should represent the **external pH at which a microorganism exhibits maximal growth or reproduction under a specified assay**. Operationally, it is the argmax of a growth-response curve—such as maximum specific growth rate, biomass yield, colony expansion, or another explicitly stated reproductive endpoint—while medium composition, temperature, oxygen regime, salinity, buffering, and growth phase are controlled.

The most defensible generic mechanism is not that one universal “pH-optimum gene” fixes the optimum. Rather, external pH sets the proton gradient and acid–base burden across the cytoplasmic membrane; transport, membrane permeability, metabolism, and buffering then determine cytoplasmic pH and proton-motive-force homeostasis; these determine energetic and macromolecular performance and hence the observed growth maximum. Neutralophiles can grow over approximately external pH 5.5–9.0 while maintaining cytoplasmic pH around 7.5–7.7, illustrating that external optimum and intracellular pH are distinct variables. PMF comprises ΔpH and membrane potential Δψ and is a central energy currency. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5)

### Boundaries

Do **not** conflate `METPO:1000331` with:

1. **pH growth range:** all external pH values permitting growth, rather than the maximum.
2. **Acid/alkali tolerance or survival:** recovery after non-growing exposure can occur outside the growth range. The authoritative review explicitly distinguishes growth from survival. (krulwich2011molecularaspectsof pages 1-3)
3. **Cytoplasmic pH or its optimum:** an internal state and mediator, not the environmental trait.
4. **Environmental pH preference:** pH at maximal abundance in nature is a *realized niche* affected by competitors, dispersal, nutrients, and other covariates; it is not necessarily culture-measured optimal growth pH. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)
5. **Optimum pH of an enzyme, pathway, community, or industrial process:** these may help explain or exploit the organismal phenotype but are not equivalent to it.
6. **Endpoint-dependent optima:** maximum growth rate and maximum yield may occur at different pH values. The endpoint and curve-fitting method should therefore be retained as assay metadata.
7. **Nominal versus experienced pH:** weak organic acids can cross membranes in protonated form and dissociate internally; identical bulk pH values can consequently impose different intracellular stresses depending on acid identity and concentration. (lund2020understandinghowmicroorganisms pages 1-2, lund2020understandinghowmicroorganisms pages 2-3)

## Recommended graph architecture

Retain the existing `ph_optimum_balanced_homeostasis` concept as the **taxon-neutral core**:

> external pH → transmembrane proton distribution/ΔpH → PMF and cytoplasmic-pH burden → pH-homeostasis performance → ATP/energy and macromolecular function → growth rate → `METPO:1000331`

Attach acid and alkaline response mechanisms as **conditional modules**, not universal parallel causes. Acid-resistance systems often explain survival below the optimum without shifting the optimum, whereas alkaliphile-specific antiporters can be constitutive determinants of high-pH growth.

## Candidate nodes grouped by type

### Trait and assay nodes

- **pH optimum:** `METPO:1000331`.
- External pH; pH growth-response curve; maximum specific growth rate; biomass yield; reproduction rate; pH growth range; acid survival; alkaline survival — retain as label-only candidates until exact project-compatible ontology terms are verified.
- Experimental modifiers: buffer identity/capacity, mineral versus organic acid, medium composition, oxygen, temperature, salinity, inoculum history, adaptation state, planktonic/biofilm state, and sampling time.

### Environmental and chemical nodes

- Hydron/proton: `CHEBI:15378`.
- Sodium(1+): `CHEBI:29101`.
- Urea: `CHEBI:16199`.
- Ammonia: `CHEBI:16134`.
- L-glutamate: `CHEBI:29985`.
- 4-aminobutanoate/GABA: `CHEBI:16865`.
- Arginine, lysine, ornithine, CO₂, ATP, ADP, weak organic acid, organic-acid anion, and cyclopropane fatty acids: use label-only nodes unless identifiers are independently checked during YAML implementation.

### Compartments and biophysical states

- Plasma membrane: `GO:0005886`.
- Cytoplasm; periplasm; extracellular region.
- Cytoplasmic pH, transmembrane ΔpH, membrane potential Δψ, proton motive force, membrane proton permeability, membrane fluidity, intracellular ionic strength.

### Transport and energy modules

- F₁F₀ ATP synthase/ATPase complex.
- Respiratory proton pumps.
- Na⁺/H⁺ antiporter; Mrp multisubunit Na⁺/H⁺ antiporter; NhaA.
- Na⁺-pumping V₁V₀ ATPase.
- ATP biosynthetic process: `GO:0006754`.

NhaA is reported with 2 H⁺/1 Na⁺ stoichiometry in *E. coli*. At high pH, cation/proton antiporters drive proton entry using membrane potential; under low pH, respiratory proton extrusion or ATP-driven F₁F₀ hydrolysis can support pH homeostasis. (krulwich2011molecularaspectsof pages 5-6)

### Acid-neutralization modules

- Glutamate decarboxylase GadA/GadB and GadC glutamate/GABA antiporter.
- Arginine decarboxylase AdiA and AdiC.
- Lysine decarboxylase CadA and associated antiporter.
- Ornithine decarboxylase SpeF and PotE.
- Arginine deiminase pathway.
- Urease complex; ammonia production.
- Hydrogenase-3/proton-consuming H₂ production.

These reactions consume cytoplasmic protons or generate alkaline products. Their strongest generic interpretation is **acid survival/homeostasis**, not direct determination of organismal pH optimum. (krulwich2011molecularaspectsof pages 15-17, lund2014copingwithlow pages 7-9, lund2020understandinghowmicroorganisms pages 1-2)

### Envelope, protein, and repair modules

- Cyclopropane-fatty-acid membrane remodeling.
- Surface-protein charge/proton capture.
- DnaK, GroEL, HdeA/HdeB, and Clp proteases.
- Protein functional-pH range and acid-induced protein damage.

Cyclopropane-fatty-acid enrichment is repeatedly linked to reduced membrane proton permeability, while chaperones and proteases protect or repair acid-damaged proteins. These are useful conditional nodes but normally require taxon-specific evidence. (lund2014copingwithlow pages 7-9, lund2020understandinghowmicroorganisms pages 2-3, guo2019recentadvancesof pages 3-4)

## Candidate causal edges

The compact table below gives the strongest core and module-level candidates.

| subject | predicate | object | suggested grounding | evidence strength/context | DOI |
|---|---|---|---|---|---|
| external pH | determines component balance of | proton motive force (ΔpH/Δψ) | METPO:1000331; CHEBI:15378 hydron; GO:0005886 plasma membrane | Broad mechanistic; foundational review states pH homeostasis demands determine relative PMF components, linking outside pH to bioenergetics and growth range rather than a single taxon (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | 10.1038/nrmicro2549 |
| balanced proton motive force | enables | growth at pH optimum | METPO:1000331; GO:0006754 ATP biosynthetic process | Broad mechanistic; review identifies PMF as central energy currency and ties maintenance of cytoplasmic pH/PMF to growth-supporting external pH (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | 10.1038/nrmicro2549 |
| Mrp Na+/H+ antiporter | causally supports | alkaline cytoplasmic pH homeostasis | GO:0005886 plasma membrane; CHEBI:29101 sodium(1+); CHEBI:15378 hydron | Strong but taxon-enriched; alkaliphile genetic evidence shows mrpA mutations cause loss of alkaliphilic phenotype, alkaline pH homeostasis, and Na+/H+ antiport (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 |
| alkaline cytoplasmic pH homeostasis | supports | growth at high external pH | METPO:1000331; CHEBI:15378 hydron | Strong but mainly from alkaliphile systems; complete pH homeostasis maintains pHi near growth-supporting values, while failure correlates with growth arrest/loss of alkaliphilic phenotype (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 |
| F1F0-ATPase proton translocation | contributes to | cytoplasmic pH homeostasis | GO:0005886 plasma membrane; CHEBI:15378 hydron | Broad mechanistic with mixed context; review supports proton extrusion in acid stress and proton uptake during ATP synthesis in alkaliphiles (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6, lund2014copingwithlow pages 7-9) | 10.1038/nrmicro2549 |
| cytoplasmic pH homeostasis | supports | growth near pH optimum | METPO:1000331 | Broad mechanistic; neutralophiles maintain narrow pHi despite wider external growth range, indicating homeostasis is prerequisite for efficient growth (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549 |
| glutamate decarboxylase system | consumes | hydron | CHEBI:29985 L-glutamate; CHEBI:16865 GABA; CHEBI:15378 hydron | Broad acid-stress mechanism; strong in enteric/neutralophilic bacteria, but more clearly supports low-pH survival/tolerance than optimum per se (krulwich2011molecularaspectsof pages 5-6, lund2014copingwithlow pages 7-9, guan2020microbialresponseto pages 2-4, lund2020understandinghowmicroorganisms pages 1-2) | 10.1038/nrmicro2549 |
| glutamate decarboxylase system | produces | GABA | CHEBI:29985 L-glutamate; CHEBI:16865 GABA | Broad acid-stress mechanism; linked to proton consumption and acid resistance in multiple reviews (lund2014copingwithlow pages 7-9, guan2020microbialresponseto pages 2-4) | 10.1111/1574-6976.12076 |
| urease | produces | ammonia | CHEBI:16199 urea; CHEBI:16134 ammonia | Broad but taxon-variable; well established in acid resistance, especially Helicobacter and other acid-challenged taxa (lund2014copingwithlow pages 7-9, guan2020microbialresponseto pages 2-4, guo2019recentadvancesof pages 3-4) | 10.1111/1574-6976.12076 |
| ammonia | neutralizes | excess hydron | CHEBI:16134 ammonia; CHEBI:15378 hydron | Broad acid-stress mechanism; supports intracellular buffering/proton neutralization, more directly tied to acid tolerance than general pH optimum (guan2020microbialresponseto pages 2-4, lund2020understandinghowmicroorganisms pages 1-2) | 10.1007/s00253-019-10226-1 |
| cyclopropane fatty acids in membrane | decreases | proton permeability of plasma membrane | GO:0005886 plasma membrane; CHEBI:15378 hydron | Broad mechanistic but indirect for optimum; multiple reviews link CFA enrichment/remodeling to reduced proton influx under low pH (lund2014copingwithlow pages 7-9, lund2020understandinghowmicroorganisms pages 2-3, guo2019recentadvancesof pages 3-4) | 10.1111/1574-6976.12076 |
| lower proton permeability of plasma membrane | supports | cytoplasmic pH homeostasis | GO:0005886 plasma membrane; CHEBI:15378 hydron | Broad mechanistic; membrane remodeling is a passive homeostasis mechanism across acid-stressed microbes (krulwich2011molecularaspectsof pages 5-6, lund2020understandinghowmicroorganisms pages 2-3) | 10.1038/nrmicro2549 |


*Table: This table summarizes the strongest candidate causal edges for curating microbial pH optimum, prioritizing mechanisms with direct support from authoritative reviews and recent synthesis. It distinguishes broad mechanisms from taxon-enriched evidence and flags edges that are stronger for acid/alkali tolerance than for pH optimum itself.*

### Expanded evidence notes and supporting snippets

| # | Proposed subject–predicate–object triple | Reference and supporting snippet | Curation assessment |
|---|---|---|---|
| 1 | external pH — **sets** → transmembrane ΔpH and the relative ΔpH/Δψ contribution to PMF | Krulwich et al.: “The proton motive force (PMF) is a central energy currency,” and ΔpH is one of its two components; pH-homeostasis demands determine the relative PMF components. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | **Core; strong synthesis.** The direction is physicochemical, but exact magnitudes are membrane- and taxon-dependent. |
| 2 | maintained cytoplasmic pH — **supports** → growth across external-pH conditions | Neutralophiles grow at approximately pH 5.5–9.0 while maintaining pHi around 7.5–7.7. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 1-3) | **Core; strong.** Prefer “supports/enables,” not “determines optimum,” because this observation does not identify the complete growth-rate maximum. |
| 3 | balanced PMF — **supports** → ATP supply and growth near the pH optimum | PMF is identified as a central energy currency, with ΔpH and Δψ adjusted according to homeostatic demand. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | **Core; mechanistically strong but broad.** ATP synthesis is only one PMF-dependent function. |
| 4 | Mrp Na⁺/H⁺ antiporter — **promotes** → alkaline cytoplasmic-pH homeostasis | In alkaliphiles, point mutations in `mrpA` caused loss of Na⁺/H⁺ antiport, alkaline pH homeostasis, and the alkaliphilic phenotype. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 12-14) | **Strong genetic evidence; taxon-specific.** Suitable for an alkaliphile subgraph, not as a universal node. |
| 5 | Mrp-dependent homeostasis — **enables** → growth at high external pH | *Bacillus pseudofirmus* OF4 and *B. halodurans* C-125 maintain pHi near 7.5 over external pH 7.5–9.5 and grow optimally near external pH 10.5, where pHi is about 8.3. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 12-14) | **Strong but alkaliphile-specific.** Do not generalize the numerical optimum. |
| 6 | F₁F₀ ATP synthase proton uptake during ATP synthesis — **contributes to** → high-pH pHi homeostasis | Alkaliphile ATP synthase contributes by proton uptake; mutations in characteristic proton-translocating-subunit motifs reduce activity more at pH 10.5 than 7.5 and coincide with loss of homeostatic capacity. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 12-14) | **Mechanistic and mutation-supported; alkaliphile module.** Direction depends on physiological mode. |
| 7 | ATP hydrolysis by F₁F₀ ATPase — **drives** → proton extrusion | In acid-stressed bacteria, F₁F₀ ATPase uses ATP hydrolysis for H⁺ extrusion; this was first documented in streptococci and occurs in several neutralophiles. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076), November 2014. (lund2014copingwithlow pages 7-9) | **Conditional acid module.** Never encode F₁F₀ direction without specifying acid versus alkaline/ATP-synthesis context. |
| 8 | glutamate decarboxylase — **consumes** → cytoplasmic H⁺ | GadB converts glutamate to GABA in a coupled antiporter system and consumes cytoplasmic protons during acid challenge. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011. (krulwich2011molecularaspectsof pages 5-6) | **Well established; acid-resistance edge.** Link to pH optimum only through demonstrated growth-rate effects. |
| 9 | amino-acid decarboxylase/antiporter systems — **increase** → low-pH survival/homeostasis | GadAB/GadC, AdiA/AdiC, CadA-associated, and SpeF/PotE systems consume protons and have optima below pH 6. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076), November 2014. (lund2014copingwithlow pages 7-9) | **Taxon- and substrate-dependent.** The review supports survival more directly than shifting `METPO:1000331`. |
| 10 | urease — **converts urea to generate** → ammonia | Urease-derived ammonia buffers intracellular protons; *Helicobacter pylori* is a canonical context. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076), November 2014. (lund2014copingwithlow pages 7-9, guan2020microbialresponseto pages 2-4) | **Strong biochemical edge; taxon-variable.** Requires urea availability and transport. |
| 11 | ammonia — **neutralizes** → excess H⁺ | Ammonia production from urea or amino-acid metabolism is identified as a principal acid-neutralization strategy. DOI: [10.3389/fmicb.2020.556140](https://doi.org/10.3389/fmicb.2020.556140), September 2020. (lund2020understandinghowmicroorganisms pages 1-2) | **Strong chemistry; conditional biology.** Distinguish NH₃/NH₄⁺ speciation in detailed chemical models. |
| 12 | cyclopropane-fatty-acid remodeling — **reduces** → membrane proton permeability | Reviews report conversion of unsaturated to cyclopropane fatty acids and reduced proton permeability during acid adaptation. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076), November 2014. (lund2014copingwithlow pages 7-9, lund2020understandinghowmicroorganisms pages 2-3) | **Plausible conditional edge.** Curate only with organism-specific perturbation evidence if the graph requires direct causality. |
| 13 | protonated weak organic acid — **permeates** → cytoplasmic membrane | At low pH, lactate/acetate and related weak acids become protonated and lipophilic, permitting membrane passage. DOI: [10.3389/fmicb.2020.556140](https://doi.org/10.3389/fmicb.2020.556140), September 2020. (lund2020understandinghowmicroorganisms pages 1-2) | **Strong physicochemical edge.** Acid identity and pKₐ must be modeled; bulk pH alone is insufficient. |
| 14 | intracellular weak-acid dissociation — **increases** → cytoplasmic acidification and anion burden | Weak acids release protons after entry and can collapse proton gradients; anion efflux systems may be induced. DOI: [10.3389/fmicb.2020.556140](https://doi.org/10.3389/fmicb.2020.556140), September 2020. (lund2020understandinghowmicroorganisms pages 1-2, lund2020understandinghowmicroorganisms pages 2-3) | **Strong conditional mechanism.** Better treated as an assay/environment modifier than a universal pH-optimum edge. |
| 15 | acid-induced protein damage — **activates/requires** → chaperone and protease repair | DnaK/GroEL, HdeA/HdeB, and Clp systems protect or repair proteins under acid stress. DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076), November 2014. (lund2014copingwithlow pages 7-9) | **Protective response, not necessarily optimum-setting.** Separate induction from demonstrated benefit. |

## Evidence hierarchy for YAML curation

### Recommended core edges

These are sufficiently generic for the existing balanced-homeostasis graph:

1. external pH → transmembrane ΔpH/proton burden;
2. ΔpH + Δψ → PMF;
3. PMF homeostasis → energy-transduction capacity;
4. cytoplasmic-pH homeostasis → preservation of enzyme/macromolecular function;
5. energy and macromolecular performance → growth rate;
6. maximal growth rate over an external-pH series → `METPO:1000331`.

The final edge is an **assay/derivation relation**, not a molecular causal relation. It should retain endpoint, medium, temperature, oxygen, and pH-step metadata.

### Recommended conditional subgraphs

- **Alkaliphile:** membrane potential → Mrp-mediated Na⁺ export/H⁺ uptake → pHi homeostasis → high-pH growth; F₁F₀-mediated proton capture/ATP synthesis → energy conservation.
- **Acid challenge:** F₁F₀ ATP hydrolysis → H⁺ extrusion; glutamate/arginine/lysine/ornithine reactions → H⁺ consumption; urease → ammonia → buffering; membrane remodeling → lower H⁺ permeability.
- **Weak-organic-acid assay:** protonated acid → membrane entry → intracellular dissociation → pHi decrease/anion stress → growth inhibition.

## Recent developments, applications, and quantitative evidence

### Genome-based prediction

Ramoneda et al. combined five soil/freshwater datasets containing **1,470 samples** across pH 3–10 and analyzed 250,275 ASVs; the final genomic analysis comprised **4,568 ASVs from 38 phyla**. Their model used 56 gene types. Held-out validation achieved **R² = 0.55 and MAE = 0.63 pH units**; external UK-soil validation fell to **R² = 0.21 and MAE = 0.93**, showing substantial domain-transfer limitations. The training phenotype was maximal environmental abundance, not culture-measured optimum. Cultured phenotype data were also strongly biased: **85.4% fell between pH 6 and 8**, and the model was not considered reliable outside pH 4–9. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

A 2024 bioRxiv study trained amino-acid-composition models on **15,596 bacterial and archaeal genomes**, reporting pH-prediction **R² = 0.48**. Protein cellular localization improved pH prediction by **ΔR² = 0.36**, consistent with extracellular and membrane-exposed proteomes carrying stronger environmental-pH signals than the near-neutral cytoplasmic proteome. Models worked with genomes of at least 10% completeness and were applied to **85,205 species** and **3,349 environmental metagenome-assembled genomes**. This is useful for cultivation triage but remains a preprint and a prediction, not causal validation. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313), March 2024. (barnum2024predictingmicrobialgrowth pages 1-3)

### Real-world uses

- **Cultivation design:** genomic predictions can prioritize media pH for uncultivated taxa, but predictions should seed a measured growth curve rather than populate `METPO:1000331` directly. (ramoneda2023buildingagenomebased pages 1-1, barnum2024predictingmicrobialgrowth pages 1-3)
- **Microbial inoculants and species-distribution models:** genomic pH-preference models can aid inoculant selection and ecological forecasting, provided realized preference is labeled separately. (ramoneda2023buildingagenomebased pages 1-1)
- **Industrial fermentation:** acid tolerance can reduce base demand and contamination risk in organic-acid or biofuel production. In lactic-acid production, LAB growth commonly declines below pH 5, motivating acid-tolerant hosts such as engineered yeasts that perform near pH 3. (lund2020understandinghowmicroorganisms pages 3-5)
- **Food safety and pathogens:** organic acids exploit membrane entry and intracellular dissociation; mechanistic knowledge supports preservation and control of organisms encountering stomach, vaginal, and colonic acidic niches. (lund2020understandinghowmicroorganisms pages 3-5, lund2020understandinghowmicroorganisms pages 1-2)
- **Bioremediation and extreme environments:** alkaline antiport systems and acidophile homeostasis explain growth in soda lakes, mine drainage, and industrially extreme habitats, but their components should be curated at organism or clade level rather than generalized. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 3-5)

### Expert interpretation

The authoritative consensus is that pH physiology is a **systems property**. Proton transport, membrane permeability, ion coupling, metabolic proton balance, protein stability, and energy state are coupled; the same complex can reverse direction depending on context. Accordingly, genomic association alone is not enough to assert a causal shift in optimum. The 2023 environmental-genomics study found weak phylogenetic signal and explicitly treated abundance-derived pH preference as realized niche, while the 2024 composition model showed only moderate predictive power. These findings argue for mechanistically conservative, assay-aware curation. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 8-9, barnum2024predictingmicrobialgrowth pages 1-3)

## Claims not yet suitable for TraitMech curation

1. **A gene associated with environmental pH determines pH optimum.** The 56-gene model is predictive/associational, and its external validation was modest. (ramoneda2023buildingagenomebased pages 6-7)
2. **Environmental abundance optimum equals optimal growth pH.** This is explicitly contradicted by the realized-niche distinction. (ramoneda2023buildingagenomebased pages 1-2)
3. **Any acid-resistance mechanism shifts pH optimum.** Gad, urease, chaperones, and membrane remodeling may improve survival without moving the growth-rate maximum.
4. **F₁F₀ ATPase always exports protons.** It can hydrolyze ATP to expel H⁺ under acid stress or admit H⁺ while synthesizing ATP in alkaliphiles. (krulwich2011molecularaspectsof pages 12-14, lund2014copingwithlow pages 7-9)
5. **Mrp is a universal optimum determinant.** The strongest evidence is from extreme alkaliphiles and should be taxonomically scoped. (krulwich2011molecularaspectsof pages 12-14)
6. **Nominal pH is sufficient assay description.** Buffer capacity, acid species, pKₐ, organic-acid concentration, salinity, oxygen, temperature, and adaptation history can change the experienced stress.
7. **A single-point growth measurement establishes an optimum.** Require a pH series bracketing the peak, preferably with biological replication and curve-based uncertainty.
8. **GenomeSPOT predictions are experimentally verified phenotype calls.** The 2024 result is a preprint and reports R² = 0.48 for pH. (barnum2024predictingmicrobialgrowth pages 1-3)
9. **Surface-charge and proteome-composition adaptations are universal causal edges.** They are plausible and predictive but require perturbation evidence before inclusion in a causal graph. (krulwich2011molecularaspectsof pages 5-6, barnum2024predictingmicrobialgrowth pages 1-3)

## DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* 9, 330–343. **May 2011.** DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3)
2. Ramoneda J et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* 9. **April 2023.** DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)
3. Barnum TP et al. **Predicting microbial growth conditions from amino acid composition.** *bioRxiv*. **March 2024.** DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). (barnum2024predictingmicrobialgrowth pages 1-3)
4. Lund P, Tramonti A, De Biase D. **Coping with low pH: molecular strategies in neutralophilic bacteria.** *FEMS Microbiology Reviews* 38, 1091–1125. **November 2014.** DOI: [10.1111/1574-6976.12076](https://doi.org/10.1111/1574-6976.12076). (lund2014copingwithlow pages 7-9, lund2014copingwithlow pages 1-2)
5. Lund PA et al. **Understanding how microorganisms respond to acid pH is central to their control and successful exploitation.** *Frontiers in Microbiology* 11. **September 2020.** DOI: [10.3389/fmicb.2020.556140](https://doi.org/10.3389/fmicb.2020.556140). (lund2020understandinghowmicroorganisms pages 3-5, lund2020understandinghowmicroorganisms pages 1-2)
6. Guan N, Liu L. **Microbial response to acid stress: mechanisms and applications.** *Applied Microbiology and Biotechnology* 104, 51–65. Online **November 2019**; 2020 volume. DOI: [10.1007/s00253-019-10226-1](https://doi.org/10.1007/s00253-019-10226-1). (guan2020microbialresponseto pages 2-4)
7. Guo J et al. **Recent advances of pH homeostasis mechanisms in Corynebacterium glutamicum.** *World Journal of Microbiology and Biotechnology* 35. **November 2019.** DOI: [10.1007/s11274-019-2770-2](https://doi.org/10.1007/s11274-019-2770-2). (guo2019recentadvancesof pages 3-4)

## Bottom-line curation recommendation

Preserve `METPO:1000331` as an **assay-derived external-environment phenotype**. Curate a compact universal backbone from external pH through ΔpH/PMF and cytoplasmic-pH homeostasis to energetic/macromolecular performance and maximal growth. Add Mrp/F₁F₀ alkaliphile machinery, amino-acid decarboxylases, urease, membrane remodeling, and repair systems only as taxon- and condition-qualified modules. Predictions of environmental preference or genome-derived optimum should remain evidence annotations—not asserted phenotype values or causal edges—until validated by controlled pH-growth curves.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

4. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

5. (lund2020understandinghowmicroorganisms pages 1-2): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

6. (lund2020understandinghowmicroorganisms pages 2-3): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

9. (lund2014copingwithlow pages 7-9): Peter Lund, Angela Tramonti, and Daniela De Biase. Coping with low ph: molecular strategies in neutralophilic bacteria. FEMS microbiology reviews, 38 6:1091-125, Nov 2014. URL: https://doi.org/10.1111/1574-6976.12076, doi:10.1111/1574-6976.12076. This article has 655 citations and is from a domain leading peer-reviewed journal.

10. (guo2019recentadvancesof pages 3-4): Jing Guo, Zhenping Ma, Jinshan Gao, Jinhua Zhao, Liang Wei, Jun Liu, and Ning Xu. Recent advances of ph homeostasis mechanisms in corynebacterium glutamicum. World Journal of Microbiology and Biotechnology, Nov 2019. URL: https://doi.org/10.1007/s11274-019-2770-2, doi:10.1007/s11274-019-2770-2. This article has 39 citations and is from a peer-reviewed journal.

11. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

12. (guan2020microbialresponseto pages 2-4): Ningzi Guan and Long Liu. Microbial response to acid stress: mechanisms and applications. Applied Microbiology and Biotechnology, 104:51-65, Nov 2020. URL: https://doi.org/10.1007/s00253-019-10226-1, doi:10.1007/s00253-019-10226-1. This article has 778 citations and is from a domain leading peer-reviewed journal.

13. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

14. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

15. (lund2020understandinghowmicroorganisms pages 3-5): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

16. (ramoneda2023buildingagenomebased pages 8-9): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

17. (lund2014copingwithlow pages 1-2): Peter Lund, Angela Tramonti, and Daniela De Biase. Coping with low ph: molecular strategies in neutralophilic bacteria. FEMS microbiology reviews, 38 6:1091-125, Nov 2014. URL: https://doi.org/10.1111/1574-6976.12076, doi:10.1111/1574-6976.12076. This article has 655 citations and is from a domain leading peer-reviewed journal.