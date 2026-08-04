---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:49:31.942943'
end_time: '2026-08-04T05:58:55.974162'
duration_seconds: 564.03
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dicarboxylate/4-hydroxybutyrate cycle
  trait_identifier: traitmech:000025
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dicarboxylate_four_hydroxybutyrate_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway that fixes one molecule of CO2
    and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate
    stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus
    and Thermoproteales.
  parent_traits: traitmech:000019
  synonyms: DC/4HB cycle
  evidence_summary: 'DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate
    cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg
    et al.''s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry
    shared by this cycle in Crenarchaeota.)'
  causal_graph_summary: 'dc_four_hb_anaerobic_archaeal_co2_fixation: 14 nodes, 12
    edges'
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
- **Trait label:** dicarboxylate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000025
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes one molecule of CO2 and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus and Thermoproteales.
- **Parent traits:** traitmech:000019
- **Synonyms:** DC/4HB cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg et al.'s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry shared by this cycle in Crenarchaeota.)
- **Existing causal graph summary:** dc_four_hb_anaerobic_archaeal_co2_fixation: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **dicarboxylate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`.

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
- **Trait label:** dicarboxylate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000025
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes one molecule of CO2 and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus and Thermoproteales.
- **Parent traits:** traitmech:000019
- **Synonyms:** DC/4HB cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg et al.'s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry shared by this cycle in Crenarchaeota.)
- **Existing causal graph summary:** dc_four_hb_anaerobic_archaeal_co2_fixation: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **dicarboxylate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`.

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


# Curation report: dicarboxylate/4-hydroxybutyrate cycle

**Trait:** dicarboxylate/4-hydroxybutyrate cycle  
**Trait identifier:** `traitmech:000025`  
**Category / term kind / status:** METABOLISM / CLASS / REVIEWED  
**Parent:** `traitmech:000019`  
**Synonym:** DC/4HB cycle

## 1. Scope summary

The DC/4HB cycle is an autotrophic inorganic-carbon-assimilation pathway in which acetyl-CoA accepts one CO₂ and one bicarbonate ion through a dicarboxylate-forming arm, producing succinyl-CoA. A second, 4-hydroxybutyrate arm converts succinyl-CoA into two acetyl-CoA molecules. One acetyl-CoA regenerates the initial acceptor and the other is the net fixed-carbon product. The experimentally reconstructed sequence is:

**acetyl-CoA → pyruvate → phosphoenolpyruvate → oxaloacetate → malate → fumarate → succinate → succinyl-CoA → succinate semialdehyde → 4-hydroxybutyrate → 4-hydroxybutyryl-CoA → crotonyl-CoA → (S)-3-hydroxybutyryl-CoA → acetoacetyl-CoA → 2 acetyl-CoA.** (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 1-2)

The pathway was established biochemically and by isotope labeling in the strictly anaerobic, hyperthermophilic archaeon *Ignicoccus hospitalis*, which grows chemolithoautotrophically at approximately 90°C using H₂ as electron donor and elemental sulfur as electron acceptor. It was subsequently demonstrated in *Thermoproteus/Pyrobaculum neutrophilus* and associated with anaerobic or microaerobic Desulfurococcales and Thermoproteales. Oxygen-sensitive pyruvate synthase and dependence on low-potential ferredoxin provide a mechanistic explanation for this ecological association. It should nevertheless be represented as an enabling environmental context rather than an absolute taxonomic rule. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 5-5, ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2011identificationofmissing pages 1-2)

### Defining boundaries

- **Versus the 3HP/4HB cycle:** both pathways share the succinyl-CoA-to-two-acetyl-CoA 4HB regeneration module. DC/4HB reaches succinyl-CoA through pyruvate synthase, PEP carboxylase, and a reductive dicarboxylate sequence; 3HP/4HB uses acetyl-CoA/propionyl-CoA carboxylation and 3-hydroxypropionate chemistry. Thus, 4-hydroxybutyryl-CoA dehydratase alone does not distinguish the two traits. (ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2011identificationofmissing pages 1-2)
- **Versus the reductive TCA cycle:** DC/4HB uses part of the reductive TCA sequence from oxaloacetate to succinyl-CoA but does not continue through the 2-oxoglutarate branch. It regenerates acetyl-CoA through 4HB instead. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2)
- **Versus heterotrophic 4HB degradation:** detection or uptake of 4HB, crotonyl-CoA, or β-oxidation enzymes is insufficient. The trait requires the complete carbon-fixing dicarboxylate arm, the 4HB regeneration arm, and evidence that the system functions autotrophically.
- **Taxonomic boundary:** experimentally validated operation is strongest for *I. hospitalis* and *T./P. neutrophilus*. Pathway calls in other organisms based only on homologs or MAGs should be represented as **genomic potential**, not demonstrated phenotype.

## 2. Physiological and quantitative interpretation

The published net equation for formation of one net acetyl-CoA includes one CO₂, one HCO₃⁻, three ATP, CoA, and reduced electron carriers. Reported reductant accounting differs between organism-specific reconstructions: the *I. hospitalis* formulation assigns six reduced ferredoxins plus NAD(P)H, whereas the *T. neutrophilus* accounting reports two reduced ferredoxins plus two NAD(P)H per acetyl-CoA. This discrepancy likely reflects different assumptions about electron-carrier specificity and should not be collapsed into a universal graph edge. The robust common claim is consumption of **1 CO₂ + 1 HCO₃⁻ + 3 ATP per net acetyl-CoA**, with ferredoxin and pyridine nucleotides supplying reductant. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9)

For *I. hospitalis*, the estimated flux needed to support a two-hour generation time was approximately **0.4 μmol CO₂ fixed min⁻¹ mg⁻¹ protein**. The organism can grow with a minimum generation time of about one hour at 90°C, although the flux estimate and minimum generation time refer to different experimental descriptions and should not be numerically combined. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)

In autotrophically grown *T. neutrophilus* extracts, labeled 4-hydroxybutyrate was converted to labeled acetyl-CoA at **110 nmol min⁻¹ mg⁻¹ protein**, requiring MgATP, CoA, and NAD⁺. Fumarase, fumarate reductase, succinyl-CoA reductase, and 4-hydroxybutyryl-CoA dehydratase showed much higher activities in autotrophic than acetate-grown cells. Acetate strongly repressed characteristic cycle activities, while acetate-CoA ligase was reported as constitutive. These are valuable regulatory edges but are taxon- and growth-condition-specific. (ramosvera2009autotrophiccarbondioxide pages 5-7, ramosvera2009autotrophiccarbondioxide pages 8-9)

## 3. Candidate nodes

### 3.1 Pathways and modules

- `traitmech:000025` — dicarboxylate/4-hydroxybutyrate cycle.
- Dicarboxylate carbon-fixation arm — label-only candidate module.
- 4-hydroxybutyrate acetyl-CoA-regeneration arm — label-only candidate module.
- Autotrophic carbon fixation — candidate process; verify the exact GO or METPO term during ontology validation.
- Incomplete reductive citric-acid segment — label-only candidate; do not identify it as a complete reductive TCA cycle.

### 3.2 Chemicals and cofactors

Candidate metabolite nodes are acetyl-CoA, CO₂, bicarbonate, pyruvate, phosphoenolpyruvate, oxaloacetate, malate, fumarate, succinate, succinyl-CoA, succinate semialdehyde, 4-hydroxybutyrate, 4-hydroxybutyryl-CoA, crotonyl-CoA, (S)-3-hydroxybutyryl-CoA, acetoacetyl-CoA, CoA, ATP, ADP, AMP, phosphate, pyrophosphate, NAD(P)H/NAD(P)⁺, and reduced/oxidized ferredoxin. These should be grounded to CHEBI only after checking exact protonation and stereochemical forms; in particular, do not map generic NAD(P)H to either NADH or NADPH without reaction-specific evidence.

Additional physiological chemicals include H₂ as an electron donor and elemental sulfur as an electron acceptor in the validated *Ignicoccus* and *Thermoproteus* culture systems. These relations are not universal requirements of the cycle. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2)

### 3.3 Enzymes, proteins, and genes

High-priority enzyme nodes are:

1. Pyruvate synthase/pyruvate:ferredoxin oxidoreductase — candidate *I. hospitalis* loci `Igni_1075–1078` or `Igni_1256–1259`.
2. Pyruvate:water dikinase — `Igni_1113`.
3. Phosphoenolpyruvate carboxylase — `Igni_0341`.
4. Malate dehydrogenase — `Igni_1263`.
5. Fumarate hydratase — `Igni_0678`.
6. Fumarate reductase — candidate loci `Igni_0276/Igni_0445`.
7. Succinate thiokinase/succinyl-CoA synthetase — `Igni_0085/Igni_0086`.
8. Succinyl-CoA reductase.
9. Succinate-semialdehyde reductase.
10. 4-Hydroxybutyrate-CoA synthetase/ligase — `Igni_0475`.
11. 4-Hydroxybutyryl-CoA dehydratase — `Igni_0595`; a radical, FAD- and [4Fe–4S]-containing enzyme.
12. Crotonyl-CoA hydratase or the hydratase domain of a bifunctional crotonyl-CoA hydratase/(S)-3-hydroxybutyryl-CoA dehydrogenase — `Igni_1058` is associated with hydratase activity.
13. (S)-3-Hydroxybutyryl-CoA dehydrogenase or corresponding domain of the bifunctional protein.
14. β-Ketothiolase/acetoacetyl-CoA thiolase. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2011identificationofmissing pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3)

The retrieved evidence supports these locus assignments as candidates rather than definitive UniProt mappings. Exact EC, UniProt, Rhea, and KEGG identifiers should be imported from reviewed records or reaction databases rather than assigned from enzyme names alone.

### 3.4 Taxa and environmental context

- *Ignicoccus hospitalis* — experimentally validated; use an NCBITaxon CURIE after checking the current taxonomy record.
- *Thermoproteus neutrophilus*, now commonly treated as *Pyrobaculum neutrophilum* — experimentally validated, but preserve the source’s historical organism name in evidence metadata.
- Desulfurococcales and Thermoproteales — broader taxonomic contexts.
- *Pyrobaculum aerophilum*, *P. islandicum*, and *P. caldifontis* — genomic/pathway candidates in the foundational study, not equivalent to direct cycle validation in every species. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 5-5)
- Anaerobic and microaerobic conditions; hyperthermophilic geothermal habitat; H₂/CO₂ atmosphere; elemental sulfur availability — environmental or culture-condition nodes. “90°C” and “85°C” are assay/organism attributes rather than defining universal thresholds. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2)

### 3.5 Cellular localization and molecular features

No organelle is involved. The pathway is archaeal and cytosolic/soluble at the reaction-network level, but individual localization claims should not be curated without protein-specific evidence. Candidate molecular-feature nodes include [4Fe–4S] cluster binding, FAD binding, ferredoxin-dependent oxidoreduction, ATP-dependent CoA ligation, carboxylation, hydration/dehydration, and thiolytic cleavage. The [4Fe–4S]/FAD annotation is particularly well supported for 4-hydroxybutyryl-CoA dehydratase. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2)

## 4. Candidate causal edges

The following table is structured for translation into `data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`. Its snippets are concise evidence summaries derived from the cited source passages; quotation marks should not be interpreted as full-text verbatim quotations unless checked against the original PDF.

| subject | predicate | object | catalyst/gene locus (where supported) | evidence type | DOI | confidence/curation note |
|---|---|---|---|---|---|---|
| acetyl-CoA + CO2 | is converted to | pyruvate | pyruvate synthase; Igni_1075–1078 or Igni_1256–1259 | pathway reconstruction + enzyme activity in *I. hospitalis* (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High for pathway step; locus assignment uncertain between the two candidate gene sets in *I. hospitalis*. |
| pyruvate + ATP + Pi | is converted to | phosphoenolpyruvate + AMP + PPi | pyruvate:water dikinase; Igni_1113 | enzyme activity + gene candidate in *I. hospitalis* (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High. |
| phosphoenolpyruvate + HCO3- | is converted to | oxaloacetate | phosphoenolpyruvate carboxylase; Igni_0341 | enzyme activity + pathway reconstruction (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High. Distinguishes DC/4HB from 3HP/4HB carboxylation chemistry. |
| oxaloacetate | is converted to | malate | malate dehydrogenase; Igni_1263 | enzyme activity + pathway reconstruction (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High. |
| malate | is converted to | fumarate | fumarate hydratase; Igni_0678 | enzyme activity + pathway reconstruction (ramosvera2009autotrophiccarbondioxide pages 5-7, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High. Also strongly regulated in *T. neutrophilus*. |
| fumarate + reduced electron donor | is converted to | succinate | fumarate reductase; Igni_0276/0445 | enzyme activity + pathway reconstruction (ramosvera2009autotrophiccarbondioxide pages 5-7, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High. Electron donor is ferredoxin-linked/inferred from pathway energetics; keep donor wording conservative. |
| succinate + CoA + ATP | is converted to | succinyl-CoA | succinate thiokinase; Igni_0085/0086 | enzyme activity + pathway reconstruction (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High. Marks end of dicarboxylate arm. |
| succinyl-CoA | is converted to | succinate semialdehyde | succinyl-CoA reductase | enzyme activity + pathway reconstruction in DC/4HB organisms (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09; https://doi.org/10.1128/JB.01156-10 | High for reaction presence; no exact *I. hospitalis* Igni locus retrieved here. |
| succinate semialdehyde | is converted to | 4-hydroxybutyrate | succinate semialdehyde reductase | pathway reconstruction + enzyme identification in crenarchaeal cycle (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.01156-10 | High for reaction presence; exact *I. hospitalis* locus not retrieved. |
| 4-hydroxybutyrate + CoA + ATP | is converted to | 4-hydroxybutyryl-CoA | 4-hydroxybutyryl-CoA synthetase; Igni_0475 | enzyme activity + gene candidate in *I. hospitalis* (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105 | High. Sometimes described generically as 4-hydroxybutyrate-CoA ligase/synthetase. |
| 4-hydroxybutyryl-CoA | is converted to | crotonyl-CoA | 4-hydroxybutyryl-CoA dehydratase; Igni_0595 | key diagnostic enzyme; enzyme activity + gene candidate (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High. Strong marker for the 4HB regeneration arm. |
| crotonyl-CoA | is converted to | (S)-3-hydroxybutyryl-CoA | crotonyl-CoA hydratase / bifunctional crotonase-(S)-3-hydroxybutyryl-CoA dehydrogenase; Igni_1058 for hydratase activity | pathway reconstruction + enzyme activity (ramosvera2011identificationofmissing pages 1-2, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.01156-10 | Moderate to high. In Thermoproteales/Desulfurococcales this step can be part of a bifunctional fusion enzyme; exact *I. hospitalis* architecture should be curated cautiously. |
| (S)-3-hydroxybutyryl-CoA | is converted to | acetoacetyl-CoA | bifunctional crotonase/(S)-3-hydroxybutyryl-CoA dehydrogenase | pathway reconstruction + enzyme identification (ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1128/JB.01156-10 | Moderate. Core step is well supported, but exact *I. hospitalis* locus was not retrieved in current evidence. |
| acetoacetyl-CoA | is cleaved to yield | 2 acetyl-CoA | beta-ketothiolase | pathway reconstruction + enzyme identification (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.01156-10 | High for reaction presence; exact *I. hospitalis* locus not retrieved. |
| dicarboxylate/4-hydroxybutyrate cycle | has net fixation input | 1 CO2 + 1 HCO3- per turn | pathway-level trait | stoichiometric reconstruction (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High. This is the defining trait-level stoichiometric boundary. |
| dicarboxylate/4-hydroxybutyrate cycle | requires | reduced ferredoxin and NAD(P)H | pathway-level electron carriers | stoichiometric reconstruction + physiological interpretation (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9, ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09; https://doi.org/10.1128/JB.01156-10 | High at pathway level; avoid over-curating donor specificity for each individual reductive step unless separately sourced. |
| pyruvate synthase | contributes to | oxygen sensitivity / anaerobic or microaerobic restriction | oxygen-sensitive enzyme | expert mechanistic interpretation (ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1128/JB.01156-10 | Moderate. Good trait-context edge, but not a direct reaction step. |
| strict anaerobic or microaerophilic conditions | enable | operation of the DC/4HB cycle in crenarchaeota | environmental context | organism physiology + expert interpretation (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2011identificationofmissing pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.01156-10 | High for trait context; phrase as association/enabling context, not universal absolute. |
| hydrogen oxidation with sulfur reduction | supports | autotrophic growth coupled to the DC/4HB cycle | physiological context in *Ignicoccus*/*Thermoproteus* | culture physiology (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High but taxon-specific. Do not generalize to all putative DC/4HB taxa. |
| acetate addition/growth on acetate | downregulates | characteristic DC/4HB enzyme activities | regulatory effect in *T. neutrophilus* | regulation experiment (ramosvera2009autotrophiccarbondioxide pages 5-7, ramosvera2009autotrophiccarbondioxide pages 8-9) | https://doi.org/10.1128/JB.00145-09 | High but assay/taxon-specific; curate as conditional regulation, not universal pathway rule. |
| labeled 4-hydroxybutyrate | is incorporated into | acetyl-CoA / central biomass precursors | pathway operation assay | isotope labeling in cell extracts/cells (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3, ramosvera2009autotrophiccarbondioxide pages 5-7) | https://doi.org/10.1073/pnas.0801043105; https://doi.org/10.1128/JB.00145-09 | High as supporting evidence for the 4HB regeneration arm; this is evidence-of-operation rather than a mechanistic graph edge. |


*Table: This table condenses the evidence-backed core reactions and context edges for the archaeal dicarboxylate/4-hydroxybutyrate cycle. It is designed for TraitMech curation, keeping only supported Igni loci, pathway-defining stoichiometry, and the most important environmental and regulatory relations.*

### Additional recommended pathway-level triples

| Subject | Predicate | Object | Supporting snippet | Reference and curation note |
|---|---|---|---|---|
| DC/4HB cycle | fixes per turn | one CO₂ and one HCO₃⁻ | “Part 1 converts acetyl-CoA, one CO₂, and one bicarbonate to succinyl-CoA.” | Huber et al. 2008. High confidence. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5) |
| DC/4HB cycle | produces net | one acetyl-CoA | “succinyl-CoA … [is converted] back to two acetyl-CoA molecules,” one regenerating the acceptor | High confidence pathway accounting. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2011identificationofmissing pages 1-2) |
| DC/4HB cycle | consumes | three ATP per net acetyl-CoA | Net stoichiometry lists “3 ATP” | High confidence at pathway level; reductant accounting is organism/model dependent. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9) |
| 4-hydroxybutyryl-CoA dehydratase | contains | FAD and [4Fe–4S] cofactors | described as a “key [4Fe-4S] flavin-containing enzyme” | High confidence. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2, ramosvera2009autotrophiccarbondioxide pages 1-2) |
| pyruvate synthase | uses | reduced ferredoxin | oxygen-sensitive enzyme and ferredoxin electron donor explain anaerobic/microaerobic restriction | Moderate-to-high; preserve organism context. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2011identificationofmissing pages 1-2) |
| autotrophic growth condition | increases | characteristic DC/4HB enzyme activities | enzymes showed “high activities only under autotrophic CO₂ fixation conditions” | High confidence for *T. neutrophilus*; not universal regulation. (ramosvera2009autotrophiccarbondioxide pages 5-7) |
| [1-¹⁴C]4-hydroxybutyrate assay | demonstrates | flux through the 4HB arm into acetyl-CoA/biomass | labeled 4HB was converted to labeled acetyl-CoA and incorporated into amino acids | High confidence evidence-of-operation relation. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3, ramosvera2009autotrophiccarbondioxide pages 5-7) |

## 5. Current understanding, recent research, and applications

### Genomic distribution

A 2022 phylogenomic survey screened **52,515 MAGs** and identified carbon-fixation pathways in **1,007 bacterial and archaeal genomes**, substantially expanding the inferred phylogenetic breadth of the DC/4HB cycle. This is important evidence that the trait’s genomic potential may extend beyond the small set of cultivated model organisms. However, it is a computational pathway survey, not biochemical validation in every MAG; the retrieved evidence does not provide a defensible DC/4HB-specific genome count, so one should not be inferred. (garritano2022carbonfixationpathways pages 1-2)

### 2023–2024 literature assessment

The search found no 2023–2024 primary study that revised the core DC/4HB mechanism or experimentally reconstituted the complete pathway. Recent papers predominantly use DC/4HB as a metagenomic carbon-fixation category or discuss it in comparisons of natural and engineered CO₂-fixation routes. Consequently, the foundational 2008–2011 biochemical studies remain the strongest evidence for causal graph edges. This is a case where prioritizing recent sources must not displace older direct mechanistic evidence.

### Current and prospective applications

There is no established industrial or field-deployed implementation of the complete DC/4HB cycle identified in the retrieved literature. Its main present applications are:

1. **Metagenomic annotation of autotrophic potential** in geothermal, anoxic, subsurface, and other extreme microbial communities.
2. **Carbon-cycle modeling**, where the pathway broadens estimates of archaeal primary production and microbial carbon sinks.
3. **Synthetic-biology design space:** the cycle is attractive because it fixes two inorganic-carbon species into acetyl-CoA with relatively modest ATP expenditure. Its practical transfer is constrained by oxygen-sensitive pyruvate synthase, dependence on reduced ferredoxin, multienzyme cofactor balancing, and thermophilic enzyme context. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2011identificationofmissing pages 1-2, garritano2022carbonfixationpathways pages 1-2)
4. **Biomarker and evolutionary studies:** 4-hydroxybutyryl-CoA dehydratase and associated enzyme complements are used to investigate the evolution and distribution of archaeal autotrophy. Because the 4HB arm is shared with 3HP/4HB and several enzymes are not pathway-specific, multi-gene/module evidence is required. (ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2011identificationofmissing pages 1-2)

## 6. Expert interpretation

The foundational investigators interpreted DC/4HB as an ancient archaeal autotrophic strategy, consistent with its occurrence in deep-branching hyperthermophilic lineages and its use of ferredoxin-dependent enzymes. This is an evolutionary hypothesis rather than a direct graph mechanism and should remain outside the core causal YAML unless TraitMech explicitly models evolutionary origin. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 5-5)

Energetically, the pathway was judged less ATP-demanding than the Calvin cycle, but that comparison does not capture oxygen sensitivity, reducing-potential requirements, enzyme replacement costs, or host compatibility. Therefore, “more efficient” should be modeled only with an explicitly defined metric—such as ATP per fixed carbon—not as an unconditional causal edge. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9)

## 7. Curation warnings

1. **Do not curate a DC/4HB phenotype from `abfD`/4-hydroxybutyryl-CoA dehydratase alone.** The enzyme also participates in 3HP/4HB-related 4HB chemistry and potentially other metabolic contexts.
2. **Do not treat the shared 4HB arm as pathway-specific.** Require evidence for pyruvate synthase, PEP carboxylase, the oxaloacetate-to-succinyl-CoA sequence, and the full regeneration arm.
3. **Do not infer experimental operation from a MAG pathway call.** Use predicates such as “has genomic potential for” unless isotope incorporation, expression, or enzyme activity is available.
4. **Do not universalize H₂ oxidation or sulfur reduction.** These are demonstrated energy-metabolism couplings in model organisms, not defining reactions of carbon fixation.
5. **Do not universalize exact temperature or oxygen thresholds.** The strongest models are strict anaerobic hyperthermophiles, while reviews also associate the cycle with microaerobic organisms.
6. **Do not collapse ferredoxin and NAD(P)H stoichiometries across species.** Published reconstructions differ in electron-carrier accounting. Use generic “requires reducing equivalents” at the trait level and organism-specific stoichiometry in evidence annotations. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5, ramosvera2009autotrophiccarbondioxide pages 8-9)
7. **Treat candidate Igni loci cautiously.** Pyruvate synthase has alternative candidate gene sets, and some activities were assigned from genome context plus biochemical assays rather than direct genetic disruption.
8. **Do not invent ontology mappings.** CHEBI forms must preserve stereochemistry/protonation; EC, Rhea, KEGG, UniProt, GO, ENVO, and NCBITaxon identifiers should be validated against their current databases before YAML insertion.
9. **Avoid curating evolutionary antiquity as a mechanistic fact.** It remains an expert interpretation.
10. **Regulation by acetate is taxon- and assay-specific.** Represent it as a conditional edge for *T. neutrophilus*, not a universal characteristic. (ramosvera2009autotrophiccarbondioxide pages 5-7, ramosvera2009autotrophiccarbondioxide pages 8-9)

## 8. DOI-first bibliography

1. **Huber H, et al.** “A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum *Ignicoccus hospitalis*.” *Proceedings of the National Academy of Sciences* 105:7851–7856. **June 2008.** DOI: [10.1073/pnas.0801043105](https://doi.org/10.1073/pnas.0801043105). Foundational biochemical, enzyme-activity, stoichiometric, and isotope-labeling evidence. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3, huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2)
2. **Ramos-Vera WH, Berg IA, Fuchs G.** “Autotrophic carbon dioxide assimilation in Thermoproteales revisited.” *Journal of Bacteriology* 191:4286–4297. **July 2009.** DOI: [10.1128/JB.00145-09](https://doi.org/10.1128/JB.00145-09). Direct evidence in *T. neutrophilus*, including regulation and labeled-4HB conversion. (ramosvera2009autotrophiccarbondioxide pages 5-7, ramosvera2009autotrophiccarbondioxide pages 1-2, ramosvera2009autotrophiccarbondioxide pages 8-9)
3. **Ramos-Vera WH, Weiss M, Strittmatter E, Kockelkorn D, Fuchs G.** “Identification of missing genes and enzymes for autotrophic carbon fixation in Crenarchaeota.” *Journal of Bacteriology* 193:1201–1211. **March 2011.** DOI: [10.1128/JB.01156-10](https://doi.org/10.1128/JB.01156-10). Enzyme/gene completion of the shared 4HB arm and interpretation of oxygen sensitivity. (ramosvera2011identificationofmissing pages 1-2)
4. **Garritano AN, Song W, Thomas T.** “Carbon fixation pathways across the bacterial and archaeal tree of life.” *PNAS Nexus* 1(5). **October 2022.** DOI: [10.1093/pnasnexus/pgac226](https://doi.org/10.1093/pnasnexus/pgac226). Large-scale MAG survey and expansion of inferred pathway distribution. (garritano2022carbonfixationpathways pages 1-2)

## Recommended curation decision

Retain `traitmech:000025` as a reviewed metabolism class. Expand the existing 14-node/12-edge graph to represent both complete pathway arms, but separate **core biochemical edges**, **organism-specific gene assignments**, **environmental enabling conditions**, and **assay evidence**. The highest-confidence additions are the two inorganic-carbon entry steps, the complete succinyl-CoA-to-two-acetyl-CoA sequence, ATP/reductant requirements, the FAD/[4Fe–4S] dependence of 4-hydroxybutyryl-CoA dehydratase, and conditional anaerobic/microaerobic context. Genomic-distribution, regulatory, and evolutionary claims should carry explicit uncertainty or taxon-specific qualifiers.

References

1. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 1-2): Harald Huber, Martin Gallenberger, Ulrike Jahn, Eva Eylert, Ivan A. Berg, Daniel Kockelkorn, Wolfgang Eisenreich, and Georg Fuchs. A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum ignicoccus hospitalis. Proceedings of the National Academy of Sciences, 105:7851-7856, Jun 2008. URL: https://doi.org/10.1073/pnas.0801043105, doi:10.1073/pnas.0801043105. This article has 436 citations and is from a highest quality peer-reviewed journal.

2. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 4-5): Harald Huber, Martin Gallenberger, Ulrike Jahn, Eva Eylert, Ivan A. Berg, Daniel Kockelkorn, Wolfgang Eisenreich, and Georg Fuchs. A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum ignicoccus hospitalis. Proceedings of the National Academy of Sciences, 105:7851-7856, Jun 2008. URL: https://doi.org/10.1073/pnas.0801043105, doi:10.1073/pnas.0801043105. This article has 436 citations and is from a highest quality peer-reviewed journal.

3. (ramosvera2009autotrophiccarbondioxide pages 1-2): W. Hugo Ramos-Vera, Ivan A. Berg, and Georg Fuchs. Autotrophic carbon dioxide assimilation in <i>thermoproteales</i> revisited. Jul 2009. URL: https://doi.org/10.1128/jb.00145-09, doi:10.1128/jb.00145-09. This article has 105 citations and is from a peer-reviewed journal.

4. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 5-5): Harald Huber, Martin Gallenberger, Ulrike Jahn, Eva Eylert, Ivan A. Berg, Daniel Kockelkorn, Wolfgang Eisenreich, and Georg Fuchs. A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum ignicoccus hospitalis. Proceedings of the National Academy of Sciences, 105:7851-7856, Jun 2008. URL: https://doi.org/10.1073/pnas.0801043105, doi:10.1073/pnas.0801043105. This article has 436 citations and is from a highest quality peer-reviewed journal.

5. (ramosvera2011identificationofmissing pages 1-2): W. Hugo Ramos-Vera, Michael Weiss, Eric Strittmatter, Daniel Kockelkorn, and Georg Fuchs. Identification of missing genes and enzymes for autotrophic carbon fixation in <i>crenarchaeota</i>. Mar 2011. URL: https://doi.org/10.1128/jb.01156-10, doi:10.1128/jb.01156-10. This article has 62 citations and is from a peer-reviewed journal.

6. (ramosvera2009autotrophiccarbondioxide pages 8-9): W. Hugo Ramos-Vera, Ivan A. Berg, and Georg Fuchs. Autotrophic carbon dioxide assimilation in <i>thermoproteales</i> revisited. Jul 2009. URL: https://doi.org/10.1128/jb.00145-09, doi:10.1128/jb.00145-09. This article has 105 citations and is from a peer-reviewed journal.

7. (huber2008adicarboxylate4hydroxybutyrateautotrophic pages 2-3): Harald Huber, Martin Gallenberger, Ulrike Jahn, Eva Eylert, Ivan A. Berg, Daniel Kockelkorn, Wolfgang Eisenreich, and Georg Fuchs. A dicarboxylate/4-hydroxybutyrate autotrophic carbon assimilation cycle in the hyperthermophilic archaeum ignicoccus hospitalis. Proceedings of the National Academy of Sciences, 105:7851-7856, Jun 2008. URL: https://doi.org/10.1073/pnas.0801043105, doi:10.1073/pnas.0801043105. This article has 436 citations and is from a highest quality peer-reviewed journal.

8. (ramosvera2009autotrophiccarbondioxide pages 5-7): W. Hugo Ramos-Vera, Ivan A. Berg, and Georg Fuchs. Autotrophic carbon dioxide assimilation in <i>thermoproteales</i> revisited. Jul 2009. URL: https://doi.org/10.1128/jb.00145-09, doi:10.1128/jb.00145-09. This article has 105 citations and is from a peer-reviewed journal.

9. (garritano2022carbonfixationpathways pages 1-2): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 130 citations and is from a peer-reviewed journal.