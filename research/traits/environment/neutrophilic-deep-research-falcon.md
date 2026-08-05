---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:59:47.060365'
end_time: '2026-08-04T02:08:12.157983'
duration_seconds: 505.1
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: neutrophilic
  trait_identifier: METPO:1003001
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: neutrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by optimal growth at near-neutral
    pH values, typically between pH 6.5 and 7.5.
  parent_traits: METPO:1003000
  synonyms: neutralophile, neutralophilic, neutrophile
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for
    growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)'
  causal_graph_summary: 'neutrophilic_neutral_ph_homeostasis: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** neutrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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
- **Trait label:** neutrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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


# Curation report: microbial **neutrophilic** trait

## 1. Scope and recommended interpretation

**Target:** `METPO:1003001`  
**Label:** neutrophilic  
**Category:** ENVIRONMENT; **kind:** CLASS; **mapping:** REVIEWED  
**Operational definition supplied:** optimal growth near neutral pH, typically pH 6.5–7.5.

The trait should represent a **growth-optimum phenotype**, not merely survival at neutral pH and not every mechanism activated during acid or alkaline shock. A foundational review uses *neutralophile* more broadly for bacteria capable of growth over approximately external pH 5.5–9.0 while generally maintaining cytoplasmic pH around 7.5–7.7. That broader growth range is compatible with, but should not replace, the supplied narrower optimum of pH 6.5–7.5. (krulwich2011molecularaspectsof pages 1-3)

The central mechanistic interpretation is therefore:

> near-neutral extracellular pH → modest transmembrane ΔpH and compatible proton-motive force → cytoplasmic pH maintained in the range required by enzymes and macromolecular processes → maximal or near-maximal population growth.

This interpretation is supported by the observation that proteins have restricted functional pH ranges and that proton concentration is integral to cellular bioenergetics. In neutralophiles, cytoplasmic pH homeostasis and proton-motive-force management are thus proximal physiological requirements for growth. (krulwich2011molecularaspectsof pages 1-3)

### Boundary cases

1. **Acid tolerance is not neutrophily.** Enteric bacteria can survive gastric acidity without growing there; recovery after return to permissive pH measures survival, not an acidic growth optimum. Likewise, *S. aureus* growth at pH 4.5 is acid-stress adaptation, useful as mechanistic boundary evidence but not evidence that the organism’s defining optimum is acidic or neutral. (krulwich2011molecularaspectsof pages 1-3, beetham2024histidinetransportis pages 7-8)
2. **Alkali tolerance is not alkaliphily.** A 2024 Bacillus study classifies alkali-tolerant organisms as having optimal growth around pH 7–9 and failing above approximately 9.5, whereas alkaliphiles grow optimally around pH 10–12. Facultative alkaliphiles can grow near neutrality but retain an alkaline optimum. (maksimova2024metabolicandmorphological pages 1-2)
3. **Broad pH range does not establish the optimum.** Growth rates or yields must be measured across buffered pH values. Endpoint viability, metabolic dye reduction, ATP, or membrane integrity alone establish tolerance or physiological activity, not neutrophilic preference.
4. **“Neutrophile” is lexically hazardous.** In biomedical text it commonly denotes the leukocyte. For microbial curation, use **neutralophile**, **neutralophilic microorganism**, or the exact trait label **neutrophilic**, while excluding immune-cell records.
5. **pH is conditional.** Temperature, medium composition, aeration, salt, weak acids/bases, growth phase, and buffer chemistry can shift the measured optimum. The 2024 Bacillus work, for example, jointly varied pH and NaCl and found broader resistance in an alkaliphile, illustrating confounding by mineralization. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 5-6)

## 2. Current mechanistic model and expert assessment

Krulwich, Sachs, and Padan’s authoritative synthesis frames pH homeostasis as a coordinated system involving proton-motive force (PMF), primary proton pumps, ATPases, cation/proton antiporters, metabolic proton consumption or production, and envelope permeability. PMF comprises ΔpH and electrical potential Δψ; under standard conditions the review gives the approximation **PMF (mV) = Δψ − 59ΔpH**. Neutralophilic *E. coli* growing around pH 7 has only a small alkaline-inside ΔpH but a substantial negative-inside Δψ. (krulwich2011molecularaspectsof pages 1-3)

This is not a single conserved “neutrophily pathway.” It is a **systems phenotype** emerging from ordinary cellular machinery tuned to keep cytoplasmic physicochemistry compatible with growth. The strongest universal graph core is consequently small: extracellular pH, cytoplasmic pH, ΔpH/Δψ, PMF, macromolecular function, and growth. Specific pumps, antiporters, decarboxylases, and envelope factors should be attached as taxon- and condition-specific branches rather than universal prerequisites.

The source’s mechanistic figure independently depicts acid-challenged *E. coli* and *Streptococcus mutans*, and alkali-challenged *E. coli* and *Enterococcus hirae*. It confirms that the direction and identity of ATPase and ion-transport responses vary by organism and metabolic mode. (krulwich2011molecularaspectsof media 27b96047)

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

- **neutrophilic** — `METPO:1003001`
- **parent trait** — `METPO:1003000`
- near-neutral extracellular pH, pH 6.5–7.5 — label-only environmental/experimental condition
- acidic challenge / low extracellular pH — label-only condition
- alkaline challenge / high extracellular pH — label-only condition
- sodium-poor condition — label-only experimental modifier
- oxygen availability, medium buffer, temperature, NaCl concentration, weak organic acids — label-only covariates

### Cellular state, localization, and process nodes

- cytoplasm — `GO:0005737`
- plasma membrane — `GO:0005886`
- cell wall — `GO:0005618`
- cytoplasmic pH homeostasis — `GO:0030641`
- proton transmembrane transport — `GO:1902600`
- cellular response to pH — `GO:0071467`
- growth / population growth — preferably use the project’s established microbial-growth term; otherwise label-only
- proton-motive force, transmembrane ΔpH, membrane potential Δψ — label-only unless the project has an established electrochemical-gradient ontology
- protein folding/function, enzyme activity, nutrient transport, ATP synthesis — GO grounding should be selected only at the granularity represented in the final graph

### Chemicals and metabolites

- proton — `CHEBI:15378`
- sodium cation — `CHEBI:29101`
- potassium cation — `CHEBI:29103`
- ATP — `CHEBI:15422`
- ADP — `CHEBI:16761`
- L-glutamate — `CHEBI:29985`
- 4-aminobutanoate/GABA — `CHEBI:16865`
- carbon dioxide — `CHEBI:16526`
- ammonia — `CHEBI:16134`
- tryptophan, pyruvate, organic acids, histidine — candidate metabolite nodes; verify exact protonation-state CURIEs before YAML insertion

### Transporters, enzymes, and complexes

- F-type H+-transporting ATP synthase / F1Fo ATPase — complex label; use `GO:0045263` for the proton-transporting ATP synthase complex if appropriate
- respiratory proton-pumping chain complexes, including Nuo and Cyo in *E. coli* — labels; taxon-specific subunits require verified UniProt accessions
- cytochrome bd oxidase (Cyd), non-proton-pumping branch in the cited *E. coli* model — label
- NhaA Na+/H+ antiporter — label; do not assign a universal UniProt accession
- K+/H+ antiporter — label
- GadB glutamate decarboxylase — `EC:4.1.1.15`; taxon-specific protein accession requires verification
- GadC glutamate/GABA antiporter — label
- hydrogenase-3 — label; complex composition is taxon-specific
- tryptophan deaminase/TnaA — label; reaction wording should follow the exact taxon-specific biochemical annotation
- SAUSA300_0846 histidine transporter — locus/protein label only pending stable strain-specific accession verification
- QoxA/QoxB aa3-type quinol oxidase subunits, SrrA regulator — label or verified strain-specific accessions
- cell-wall-associated GraS, VraG, VraR, VraS, MprF, FmtA, DltD — labels; retain *S. aureus* context

### Taxa useful as contextual nodes

- *Escherichia coli* — `NCBITaxon:562`
- *Staphylococcus aureus* — `NCBITaxon:1280`
- *Streptococcus mutans* — `NCBITaxon:1309`
- *Enterococcus hirae* — `NCBITaxon:1354`
- *Bacillus subtilis* — `NCBITaxon:1423`

Strain-level identifiers should be added only after matching the exact strain used by each experiment.

## 4. Candidate causal edges

The compact table below summarizes the strongest graph candidates. The expanded evidence notes that follow provide curation-ready snippets and qualifications.

| subject | predicate | object | context/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| near-neutral external pH (pH 6.5–7.5) | enables growth of | neutrophilic microorganism | trait-level scope; neutralophile definition, near-neutral optimum | Strong, constitutive trait definition | METPO:1003001; review support from 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3) |
| cytoplasmic pH homeostasis (~pH 7.5–7.7 in neutralophiles) | enables | growth across external pH ~5.5–9.0 in neutralophiles | trait-level, broad bacteria | Strong, constitutive but broad review statement | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3) |
| acid challenge | increases expression of | proton-pumping respiratory chain complexes | *Escherichia coli*; acid-stress response | Strong, contextual/auxiliary stress-response edge | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media 27b96047) |
| proton-pumping respiratory chain complexes | causes | H+ efflux from cytoplasm | broad bacteria; primary proton pumps | Strong, mechanistic but broad | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, guo2019recentadvancesof pages 3-4) |
| acidic conditions | induce | proton-consuming amino-acid decarboxylation pathways | broad bacteria; acid-stress response | Strong, contextual/auxiliary stress-response edge | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6); 10.1007/s00253-019-10226-1 (guan2020microbialresponseto pages 2-4) |
| glutamate decarboxylase GadB | consumes | cytoplasmic H+ | enteric bacteria, especially *E. coli*; acid challenge | Strong, mechanistic; taxon-enriched | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6) |
| glutamate decarboxylase GadB | produces | GABA (γ-aminobutyrate) | enteric bacteria, especially *E. coli*; acid challenge | Strong, mechanistic; taxon-enriched | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6) |
| alkaline challenge | activates/upregulates | cation/H+ antiporters | broad bacteria; alkaline-stress response | Strong, contextual/auxiliary stress-response edge | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media 27b96047) |
| NhaA Na+/H+ antiporter | exchanges | 1 Na+ out for 2 H+ in | *E. coli*; alkaline pH homeostasis | Strong, specific mechanistic stoichiometry | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6) |
| alkaline challenge | increases expression of | F1Fo ATP synthase | *E. coli*; alkaline-stress response | Strong, contextual/auxiliary stress-response edge | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media 27b96047) |
| alkaline challenge | induces | amino-acid deaminase / organic-acid-producing pathways | broad bacteria; e.g., tryptophan deaminase in *E. coli* | Moderate-to-strong, contextual/auxiliary stress-response edge | 10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6); 10.1007/s11274-019-2770-2 (guo2019recentadvancesof pages 3-4) |
| SAUSA300_0846 histidine transporter | supports maintenance of | cytosolic pH | *Staphylococcus aureus* at pH 4.5; 2024 acid-stress study | Strong, recent, taxon- and condition-specific boundary evidence | 10.1371/journal.ppat.1011927 (beetham2024histidinetransportis pages 1-2) |
| SAUSA300_0846 histidine transporter | supports | growth at low pH | *Staphylococcus aureus* at pH 4.5; mutant phenotype, no major neutral-pH defect | Strong, recent, taxon- and condition-specific boundary evidence | 10.1371/journal.ppat.1011927 (beetham2024histidinetransportis pages 7-8) |
| cell-wall assembly/maintenance genes (e.g., graS, vraG, vraR, vraS, mprF, fmtA, dltD) | support | growth at pH 4.5 | *Staphylococcus aureus*; 2024 Tn-seq plus mutant validation | Strong, recent, taxon- and condition-specific boundary evidence | 10.1371/journal.ppat.1011927 (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2) |


*Table: This table compiles the strongest candidate causal edges relevant to neutrophilic growth and the supporting pH-homeostasis machinery. It distinguishes constitutive trait-level edges from contextual acid/alkaline stress-response edges that are useful for curation but should be marked auxiliary.*

| # | Proposed subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | near-neutral extracellular pH **enables** neutrophilic growth | Krulwich et al.: neutralophiles “can grow at pHout values from ~5.5–9.0” while maintaining a narrow pHin; the supplied trait definition places the optimum at 6.5–7.5. (krulwich2011molecularaspectsof pages 1-3) | **Core**, but the exact 6.5–7.5 interval comes from the reviewed METPO definition, not this paper. Encode as the trait-defining environmental edge rather than a molecular mechanism. |
| 2 | cytoplasmic pH homeostasis **enables** neutrophilic growth | “Living cells are critically dependent upon pH homeostasis because most proteins have distinct ranges of pH for function.” Neutralophiles generally maintain pHin “~7.5–7.7.” (krulwich2011molecularaspectsof pages 1-3) | **Core, strong review evidence.** Avoid asserting that every neutralophile has exactly the same pHin. |
| 3 | extracellular pH **determines/modulates** transmembrane ΔpH | Neutralophiles maintain pHin above pHout at the acidic end and below pHout at the alkaline end; *E. coli* has a small ΔpH near pH 7. (krulwich2011molecularaspectsof pages 1-3) | **Core physiology.** “Modulates” is safer than deterministic “determines” because transport and metabolism also control pHin. |
| 4 | ΔpH and Δψ **compose** proton-motive force | The review identifies ΔpH and electrical potential as the two PMF components and gives PMF ≈ Δψ − 59ΔpH. (krulwich2011molecularaspectsof pages 1-3) | **Core physical relation.** Prefer `has_component` rather than a biological causal predicate if the graph schema permits. |
| 5 | proton-motive force **energizes** transport, synthesis, and motility | Primary pumps generate PMF; secondary transporters, ATP synthase, and flagellar machinery harness it for active transport, synthetic, and mechanical processes. (krulwich2011molecularaspectsof pages 1-3) | **Broad supporting branch**, not specific to neutrophiles. |
| 6 | acid challenge **increases expression of** proton-pumping respiratory complexes | “Under conditions of acid challenge, the neutralophile E. coli increases expression of respiratory chain complexes that pump protons out.” (krulwich2011molecularaspectsof pages 5-6) | **Strong; *E. coli*-specific stress edge.** Not constitutive neutrophilic identity. |
| 7 | proton-pumping respiratory complexes **increase** cytoplasmic H+ efflux | The respiratory complexes are explicitly described as pumping protons out of the cell. (krulwich2011molecularaspectsof pages 5-6) | **Strong mechanistic edge**, but identify the exact complex if making a gene-level assertion. |
| 8 | acid challenge **decreases expression of** F1Fo ATP synthase in *E. coli* | Expression of ATP synthase, “that brings protons into the cell during ATP synthesis,” is decreased. (krulwich2011molecularaspectsof pages 5-6) | **Strong, taxon-specific.** Direction reverses in nonrespiring organisms where ATP hydrolysis drives proton export. |
| 9 | F1Fo ATPase hydrolysis **drives** H+ extrusion in *S. mutans* | In nonrespiratory *S. mutans*, increased hydrolytic F1Fo activity “promotes ATP-dependent H+ extrusion under acidic conditions.” (krulwich2011molecularaspectsof pages 5-6) | **Strong but taxon/metabolic-state-specific.** Keep separate from the *E. coli* ATP-synthesis edge. |
| 10 | alkaline challenge **activates/upregulates** cation/H+ antiporters | Active inward proton transport is described as crucial under alkaline conditions and usually involves activation and transcriptional upregulation of key cation/proton antiporters. (krulwich2011molecularaspectsof pages 5-6) | **Strong broad mechanism**, but particular antiporter families are not universal. |
| 11 | *E. coli* NhaA **imports 2 H+ in exchange for exporting 1 Na+** | The review gives an electrogenic stoichiometry of “2H+/1Na+,” enabling Δψ-driven proton entry. (krulwich2011molecularaspectsof pages 5-6) | **Strong, specific.** Encode direction relative to the cytoplasmic membrane and alkaline-homeostasis context. |
| 12 | sodium-poor conditions or inward Na+ gradient **increase reliance on** K+/H+ antiport | Na+/H+ antiporters often dominate, but K+/H+ antiporters “assume dominance” under Na+-poor conditions or a large inward Na+ gradient. (krulwich2011molecularaspectsof pages 5-6) | **Moderate-to-strong comparative review claim.** Context-dependent; not universal gene necessity. |
| 13 | alkaline challenge **increases expression of** *E. coli* F1Fo ATP synthase | Increased expression enhances proton capture during ATP synthesis. (krulwich2011molecularaspectsof pages 5-6) | **Strong, *E. coli*-specific stress edge.** |
| 14 | alkaline challenge **increases** non-proton-pumping cytochrome bd and **decreases** proton-pumping respiratory complexes | This remodeling is described as minimizing cytoplasmic proton loss during PMF generation. (krulwich2011molecularaspectsof pages 5-6) | **Strong, *E. coli*-specific.** This is a regulatory module, not a universal neutralophile marker. |
| 15 | acidic conditions **induce** proton-consuming enzymes | Acid challenge increases expression of hydrogenases and amino-acid decarboxylases whose reactions consume cytoplasmic protons. (krulwich2011molecularaspectsof pages 5-6) | **Strong broad strategy**, with taxon-specific implementations. |
| 16 | hydrogenase-3 **converts** cytoplasmic H+ to H2 and **supports** survival at pH 2–2.5 | Anaerobic acid-challenged *E. coli* upregulates hydrogenase-3; H2 production from cytoplasmic protons contributes to survival at pH 2–2.5. (krulwich2011molecularaspectsof pages 5-6) | **Strong but survival-only boundary edge. Do not connect directly to neutrophilic optimum.** |
| 17 | GadB-catalyzed glutamate decarboxylation **consumes** H+ and **produces** GABA | GadB “consumes a proton during decarboxylation to…GABA”; GadC exchanges GABA for glutamate to continue the cycle. (krulwich2011molecularaspectsof pages 5-6) | **Strong; enteric acid-resistance module.** The source’s “γ-aminoglutarate” wording should be normalized biochemically to GABA/4-aminobutanoate. |
| 18 | GadC glutamate/GABA exchange **sustains** GadB-mediated proton consumption | GadB partners with an antiporter that exports GABA in exchange for additional glutamate. (krulwich2011molecularaspectsof pages 5-6) | **Strong pathway edge**, taxon-specific. |
| 19 | alkaline challenge **induces** deaminase/organic-acid-producing metabolism | Alkaline conditions upregulate amino-acid deaminases or pathways producing organic acids; tryptophan deaminase in *E. coli* is the stated example. (krulwich2011molecularaspectsof pages 5-6) | **Moderate-to-strong.** Verify the exact reaction and proton-generating consequence before reaction-level curation. |
| 20 | reduced proton permeability / envelope remodeling **supports** pH homeostasis | Membrane lipid and porin changes minimize proton leakage; altered surface charge is proposed to delay proton entry or loss. (krulwich2011molecularaspectsof pages 5-6, guan2020microbialresponseto pages 2-4) | **Mixed evidence.** Broad envelope statement is supportable; individual lipid→neutrophily edges remain taxon- and assay-specific. |
| 21 | SAUSA300_0846 histidine transport **supports** cytosolic-pH maintenance at pH 4.5 | The mutant maintained histidine through biosynthetic induction but “is…unable to maintain its cytosolic pH to the same extent as a WT strain.” (beetham2024histidinetransportis pages 1-2) | **Strong 2024 causal evidence; *S. aureus*- and acid-specific.** Mechanism linking imported histidine to pH remains unresolved. |
| 22 | SAUSA300_0846 **supports** *S. aureus* growth at pH 4.5 | Transporter mutants had reduced growth on pH 4.5 plates but no drastic CFU difference at pH 7.3. (beetham2024histidinetransportis pages 7-8) | **Strong 2024 mutant evidence.** Use as an acid-adaptation branch, not a core neutrophily cause. |
| 23 | QoxA/QoxB proton-pumping oxidase and SrrA-regulated respiration **support** *S. aureus* growth at pH 4.5 | qoxA/qoxB and srrA were identified as required; srrA inactivation caused a severe phenotype and qox mutants slight reductions at pH 4.5. (beetham2024histidinetransportis pages 7-8) | **Recent and causal but phenotype strengths differ.** Preserve gene-specific effect sizes qualitatively. |
| 24 | cell-wall maintenance genes **support** *S. aureus* growth at pH 4.5 | Most of 31 Tn-seq hits involved cell-wall assembly/maintenance; graS, vraG, vraR, vraS, mprF, fmtA, and dltD mutants showed defects at pH 4.5. Fifteen of 20 tested “essential” hits were validated. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2) | **Strong recent evidence, taxon/assay-specific.** Avoid a universal “cell wall causes neutrophily” edge. |
| 25 | alkaline environment plus Na+ gradient **drives** Na+/H+ antiport-mediated reverse ΔpH in alkaliphilic Bacillus | The 2024 Bacillus paper states that Na+/H+ antiporters use an electrochemical Na+ gradient to exchange sodium for protons and maintain pHin below alkaline pHout. (maksimova2024metabolicandmorphological pages 1-2) | **Boundary comparison only.** It concerns alkaliphile physiology, not the core neutralophile graph. |

## 5. Recent developments and quantitative evidence

The most directly relevant recent mechanistic advance retrieved was Beetham et al. (published **16 January 2024**). Their genome-wide screen identified **31 genes** required for *S. aureus* growth at **pH 4.5**. Of 20 candidate essential genes tested individually, **15** were confirmed as important under low-pH growth. Mutant testing used TSA at pH 7.3 versus 4.5; the candidates did not show severe neutral-pH growth defects, supporting acid-specific rather than general essentiality. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2)

That study assigned SAUSA300_0846 as a previously uncharacterized histidine transporter. Its loss impaired cytosolic-pH maintenance even though compensatory histidine biosynthesis preserved cytosolic histidine. This separates the transporter’s pH-homeostasis function from simple nutrient provisioning, but the biochemical coupling remains unknown. Aerobic respiration and cell-wall maintenance also emerged as major acid-growth determinants. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2)

Maksimova et al. (**2024**) compared facultatively alkaliphilic *Bacillus aequororis* 5-DB with weakly alkali-resistant *B. subtilis* ATCC 6633 across pH and salinity. The alkaliphile showed broader resistance, including growth reported at pH 11 and 50 g/L NaCl; intracellular pH was measured with a carboxyfluorescein probe, alongside ATP, dehydrogenase activity, and AFM morphology. This study is valuable methodologically and as a boundary comparison, but it does not establish universal causal determinants of neutrophily. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 5-6)

A 2024 Chemical Reviews synthesis further emphasizes that cytoplasmic pH acts jointly with ionic strength, energy status, macromolecular crowding, and phase behavior. This reinforces the expert interpretation that pH preference is an integrated physicochemical phenotype rather than a single-gene trait; however, no retrieved passage provided a neutrophily-specific perturbation suitable for a new atomic edge.

## 6. Applications and real-world relevance

- **Pathogenesis and antimicrobial development:** pH-homeostasis systems permit pathogens to traverse acidic host niches or grow in skin, dental plaque, and phagocytic compartments. The 2024 *S. aureus* screen identifies histidine uptake, respiration, and cell-wall systems as candidate vulnerabilities under acidic host conditions. (beetham2024histidinetransportis pages 1-2)
- **Food and probiotic microbiology:** Proton extrusion, decarboxylation systems, envelope remodeling, and biofilm formation influence survival through acidic foods and gastric transit. These are tolerance applications rather than evidence of a neutral optimum. (guan2020microbialresponseto pages 2-4)
- **Industrial biotechnology:** Engineering acid resistance can improve organic-acid or GABA fermentation. Reviews describe synthetic-biology use of proton pumps and decarboxylase systems, although such engineering may broaden tolerance without changing the organism’s preferred pH. (guan2020microbialresponseto pages 2-4)
- **Bioprocess design and strain selection:** Growth curves across controlled pH, combined with intracellular-pH probes, ATP assays, and metabolic measurements, distinguish optimum growth from stress survival. The Bacillus study demonstrates this multimodal approach and notes potential biotechnology value of broad pH and salt tolerance. (maksimova2024metabolicandmorphological pages 1-2)

## 7. Recommended minimal TraitMech graph architecture

For `data/traits/environment/neutrophilic.yaml`, the defensible **core** is:

1. near-neutral extracellular pH → supports maintenance of compatible cytoplasmic pH;
2. cytoplasmic-pH homeostasis → preserves protein/enzyme function and bioenergetics;
3. preserved macromolecular function and PMF → supports growth;
4. near-neutral pH → `METPO:1003001` phenotype through maximal/optimal growth.

Add two explicitly contextual subgraphs:

- **Acid-side homeostasis:** respiratory H+ efflux or hydrolytic F1Fo ATPase, proton-consuming decarboxylation, envelope permeability control.
- **Alkali-side homeostasis:** Na+/H+ or K+/H+ antiport-mediated H+ uptake, reduced respiratory proton loss, ATP-synthase-mediated proton capture, and acid-producing metabolism.

Every gene-level edge should include organism, strain where known, pH, medium/assay, and whether the outcome was growth, survival, intracellular pH, or expression.

## 8. Claims not yet suitable for curation

1. **Do not curate any single gene as universally causing neutrophily.** The evidence supports alternative, taxon-dependent solutions.
2. **Do not infer a neutral optimum from acid- or alkali-survival genes.** A mutant phenotype at pH 4.5 or survival at pH 2.5 is not a direct determinant of optimal growth at pH 6.5–7.5.
3. **Do not treat pHin 7.5–7.7 as an invariant threshold.** It is a broad review generalization; species, state, and measurement method matter.
4. **SAUSA300_0846 → cytosolic-pH homeostasis** is curatable only with *S. aureus*, pH 4.5, and mutant context. Its molecular mechanism should remain **uncertain**.
5. **Cell-wall genes → acid growth** should remain a grouped or gene-specific *S. aureus* branch. Their direct physicochemical effects on proton permeability were not individually established in the retrieved experiment.
6. **Tryptophan deaminase → proton production** requires reaction-level verification before adding chemical stoichiometry.
7. **Membrane lipid composition → neutrophily** is too broad. Available evidence concerns acidophiles, alkaliphiles, or acid-tolerant taxa and sometimes gives opposing lipid shifts. (krulwich2011molecularaspectsof pages 5-6, guo2019recentadvancesof pages 3-4)
8. **Bacillus alkaliphile results** are boundary evidence and should not be imported as neutralophile mechanisms without experiments in a neutrally optimized strain.
9. Verify all strain-specific UniProt, Rhea, KEGG, and MetaCyc identifiers before insertion. Label-only nodes are preferable to an incorrect accession.
10. The exact parent semantics of `METPO:1003000` were supplied but not independently retrieved; preserve the CURIE verbatim and validate its label during ontology release checks.

## 9. DOI-first bibliography

1. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343. **Published May 2011.** DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational authoritative synthesis and primary support for the causal architecture. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)
2. **Beetham CM, Schuster CF, Kviatkovski I, et al.** “Histidine transport is essential for the growth of *Staphylococcus aureus* at low pH.” *PLOS Pathogens* 20:e1011927. **Published 16 January 2024.** DOI: [10.1371/journal.ppat.1011927](https://doi.org/10.1371/journal.ppat.1011927). Recent Tn-seq, mutant-growth, and intracellular-pH evidence. (beetham2024histidinetransportis pages 7-8, beetham2024histidinetransportis pages 1-2)
3. **Maksimova YG, Eliseeva A, Maksimov A.** “Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.” *International Journal of Microbiology* 2024:3087296. **Received 10 April; accepted 10 July 2024.** DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). Recent comparative physiology and assay evidence. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 5-6)
4. **Guan N, Liu L.** “Microbial response to acid stress: mechanisms and applications.” *Applied Microbiology and Biotechnology* 104:51–65. **Online November 2019; volume year 2020.** DOI: [10.1007/s00253-019-10226-1](https://doi.org/10.1007/s00253-019-10226-1). Mechanisms and biotechnology applications. (guan2020microbialresponseto pages 2-4)
5. **Guo J, Ma Z, Gao J, et al.** “Recent advances of pH homeostasis mechanisms in *Corynebacterium glutamicum*.” *World Journal of Microbiology and Biotechnology* 35:192. **Published November 2019.** DOI: [10.1007/s11274-019-2770-2](https://doi.org/10.1007/s11274-019-2770-2). Supporting review for proton extrusion, decarboxylation, envelope remodeling, and alkaline homeostasis. (guo2019recentadvancesof pages 3-4)

**Overall curation judgment:** `METPO:1003001` is suitable for a TraitMech graph centered on **near-neutral extracellular pH → cytoplasmic-pH/PMF homeostasis → macromolecular function → optimal growth**. Stress-response modules are biologically important but should be annotated as auxiliary, directional adaptations at the boundaries of the neutralophile growth range rather than as universal defining causes.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (beetham2024histidinetransportis pages 7-8): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

3. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

4. (maksimova2024metabolicandmorphological pages 5-6): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

5. (krulwich2011molecularaspectsof media 27b96047): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (guo2019recentadvancesof pages 3-4): Jing Guo, Zhenping Ma, Jinshan Gao, Jinhua Zhao, Liang Wei, Jun Liu, and Ning Xu. Recent advances of ph homeostasis mechanisms in corynebacterium glutamicum. World Journal of Microbiology and Biotechnology, Nov 2019. URL: https://doi.org/10.1007/s11274-019-2770-2, doi:10.1007/s11274-019-2770-2. This article has 39 citations and is from a peer-reviewed journal.

8. (guan2020microbialresponseto pages 2-4): Ningzi Guan and Long Liu. Microbial response to acid stress: mechanisms and applications. Applied Microbiology and Biotechnology, 104:51-65, Nov 2020. URL: https://doi.org/10.1007/s00253-019-10226-1, doi:10.1007/s00253-019-10226-1. This article has 778 citations and is from a domain leading peer-reviewed journal.

9. (beetham2024histidinetransportis pages 1-2): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.