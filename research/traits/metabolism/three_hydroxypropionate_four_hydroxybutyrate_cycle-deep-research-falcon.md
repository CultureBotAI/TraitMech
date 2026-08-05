---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:08:29.353219'
end_time: '2026-08-04T07:17:04.169502'
duration_seconds: 514.82
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: 3-hydroxypropionate/4-hydroxybutyrate cycle
  trait_identifier: traitmech:000024
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: three_hydroxypropionate_four_hydroxybutyrate_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate
    per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates
    in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
  parent_traits: traitmech:000019
  synonyms: 3HP/4HB cycle
  evidence_summary: 'DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate
    autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg
    review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation
    pathways.)'
  causal_graph_summary: 'three_hp_four_hb_sulfolobales: 11 nodes, 10 edges'
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
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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


# Curation report: 3-hydroxypropionate/4-hydroxybutyrate cycle

## Trait record

- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **Trait identifier:** `traitmech:000024`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000019`
- **Synonym:** 3HP/4HB cycle

## 1. Scope and current definition

This trait should represent the **physiological capacity for autotrophic inorganic-carbon assimilation through the complete 3HP/4HB cycle**, rather than possession of an isolated enzyme or production of 3-hydroxypropionate. Its defining topology is:

**acetyl-CoA → malonyl-CoA → malonate semialdehyde → 3-hydroxypropionate → 3-hydroxypropionyl-CoA → acryloyl-CoA → propionyl-CoA → methylmalonyl-CoA → succinyl-CoA → succinate semialdehyde → 4-hydroxybutyrate → 4-hydroxybutyryl-CoA → crotonyl-CoA → (S)-3-hydroxybutyryl-CoA → acetoacetyl-CoA → two acetyl-CoA.**

Two bicarbonate/carbon-dioxide equivalents are incorporated as acetyl-CoA is converted to succinyl-CoA. The C4 intermediate is reduced through 4-hydroxybutyrate and ultimately cleaved into two acetyl-CoA molecules: one regenerates the carbon acceptor and the other is available for biosynthesis. The experimentally described *Metallosphaera sedula* cycle comprises 13 enzymes catalyzing 16 reactions. (hawkins2014conversionof4hydroxybutyrate pages 1-2, hawkins2013roleof4hydroxybutyratecoa pages 1-2, liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)

### Validated biological scope

Two independently evolved variants should be represented under this trait:

1. **Crenarchaeal/Sulfolobales variant:** associated with thermoacidophilic, hydrogen-oxidizing, aerobic or microaerophilic organisms such as *Metallosphaera* and *Sulfolobus*.
2. **Thaumarchaeal/Nitrososphaeria variant:** associated with mesophilic, aerobic ammonia-oxidizing archaea such as *Nitrosopumilus maritimus*.

The variants are homologous in overall pathway topology but differ in several enzyme families and energetic costs. In particular, thaumarchaeal 3-hydroxypropionyl-CoA and 4-hydroxybutyryl-CoA synthetases are ADP-forming, whereas corresponding Sulfolobales enzymes are AMP-forming. This saves two ATP equivalents per cycle turn and is interpreted as adaptation to the low-energy, oligotrophic niche of ammonia-oxidizing archaea. (liu2021convergentevolutionof pages 1-2, johnson2024crystalstructureof pages 1-2)

### Boundary cases

- **Not the bacterial 3-hydroxypropionate bicycle.** That pathway shares acetyl-CoA carboxylation and 3HP chemistry but has a different cycle architecture and lacks the defining 4HB-to-two-acetyl-CoA regeneration arm.
- **Not the dicarboxylate/4-hydroxybutyrate cycle.** DC/4HB shares the succinyl-CoA→4HB→two-acetyl-CoA arm, but fixes carbon through ferredoxin-dependent pyruvate synthase and phosphoenolpyruvate carboxylase. The 3HP/4HB cycle instead uses acetyl-CoA/propionyl-CoA carboxylase twice and converts malonyl-CoA through 3HP and propionyl-CoA. DC/4HB is classically associated with anaerobic Thermoproteales and Desulfurococcales. (liu2021convergentevolutionof pages 1-2, liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)
- **Partial 3HP production is insufficient.** Heterologous expression of the acetyl-CoA→3HP module does not establish the complete trait.
- **A single marker gene is insufficient.** Acetyl-CoA/propionyl-CoA carboxylases, enoyl-CoA hydratases, dehydrogenases, and thiolases have functions outside this cycle.
- **Genomic potential is not demonstrated physiology.** Bacterial MAGs predicted to encode the pathway and newly inferred geothermal carriers should remain provisional until pathway completeness, directionality, expression, and carbon-fixation flux are established. (garritano2022carbonfixationpathways pages 1-2, qi2024analysisofnearly pages 7-8)

## 2. Candidate nodes

### A. Pathway and process nodes

- `traitmech:000024` — 3-hydroxypropionate/4-hydroxybutyrate cycle
- `traitmech:000019` — supplied parent trait
- Autotrophic inorganic-carbon fixation — label-only unless the project already specifies its preferred GO/METPO term
- Bicarbonate assimilation
- Acetyl-CoA regeneration
- Biosynthetic acetyl-CoA production
- Crenarchaeal 3HP/4HB variant
- Thaumarchaeal modified 3HP/4HB variant

### B. Chemicals and cofactors

Recommended stable chemical identifiers, where unambiguous:

- Carbon dioxide — `CHEBI:16526`
- Hydrogencarbonate/bicarbonate — `CHEBI:17544`
- Acetyl-CoA — `CHEBI:15351`
- Malonyl-CoA — `CHEBI:15531`
- 3-hydroxypropionic acid/3-hydroxypropionate — `CHEBI:33404`
- Propionyl-CoA — `CHEBI:15539`
- Succinyl-CoA — `CHEBI:15380`
- 4-hydroxybutyrate — use a locally verified ChEBI record; do not assign from name alone because protonation-state records differ
- 4-hydroxybutyryl-CoA — label-only pending registry verification
- Crotonyl-CoA — `CHEBI:15487`
- (S)-3-hydroxybutyryl-CoA — label-only pending registry verification
- Acetoacetyl-CoA — `CHEBI:15345`
- ATP — `CHEBI:15422`
- ADP — `CHEBI:16761`
- AMP — `CHEBI:16027`
- Coenzyme A — `CHEBI:15346`
- NADPH — `CHEBI:16474`
- NADP+ — `CHEBI:18009`
- NAD+ — `CHEBI:15846`
- NADH — `CHEBI:16908`

Additional reaction intermediates that merit nodes but require identifier verification are malonate semialdehyde, 3-hydroxypropionyl-CoA, acryloyl-CoA, methylmalonyl-CoA, succinate semialdehyde, and free phosphate/pyrophosphate.

### C. Enzymes, proteins, and genes

**Pathway-defining or strongly supported classes**

- Acetyl-CoA/propionyl-CoA carboxylase
- Malonyl-CoA reductase
- Malonate-semialdehyde reductase
- 3-hydroxypropionyl-CoA synthetase
- 3-hydroxypropionyl-CoA dehydratase/crotonyl-CoA hydratase
- Acryloyl-CoA reductase
- Methylmalonyl-CoA epimerase and mutase/isomerization module
- Succinyl-CoA reductase
- Succinate-semialdehyde reductase
- 4-hydroxybutyryl-CoA synthetase
- 4-hydroxybutyryl-CoA dehydratase
- (S)-3-hydroxybutyryl-CoA dehydrogenase
- Acetoacetyl-CoA thiolase

**Directly useful locus-tag nodes**

- *M. sedula* acetyl-CoA/propionyl-CoA carboxylase subunits: `Msed_0147`, `Msed_0148`, `Msed_1375`
- *M. sedula* malonyl-CoA/succinyl-CoA reductase: `Msed_0709`
- *M. sedula* malonate-semialdehyde reductase: `Msed_1993`
- *M. sedula* bifunctional dehydratase/hydratase: `Msed_2001`
- *M. sedula* 4-hydroxybutyryl-CoA synthetase: `Msed_0406`; `Msed_0394` is a biochemically active alternative candidate
- *M. sedula* 4-hydroxybutyryl-CoA dehydratase: `Msed_1321`
- *M. sedula* crotonyl-CoA hydratase/(S)-3-hydroxybutyryl-CoA dehydrogenase used in the reconstructed terminal module: `Msed_0399`
- *M. sedula* acetoacetyl-CoA β-ketothiolase: `Msed_0656`
- *N. maritimus* ADP-forming 3-hydroxypropionyl-CoA synthetase: `Nmar_1309`
- *N. maritimus* ADP-forming 4-hydroxybutyryl-CoA synthetase: `Nmar_0206`; structure `PDB:8WZU`
- *N. maritimus* bifunctional dehydratase/hydratase: `Nmar_1308`
- *N. maritimus* NAD-dependent (S)-3-hydroxybutyryl-CoA dehydrogenase: `Nmar_1028`

These locus tags are safer curation identifiers than uncertain UniProt or EC assignments. EC, Rhea, KEGG, and UniProt mappings should be added only after checking the exact organism-specific reaction, cofactor, and product stereochemistry.

### D. Taxon nodes

High-confidence candidates include:

- Archaea — `NCBITaxon:2157`
- Crenarchaeota — `NCBITaxon:28889`
- Sulfolobales — `NCBITaxon:2281`
- *Metallosphaera sedula* — `NCBITaxon:43687`
- *Nitrosopumilus maritimus* — `NCBITaxon:42370`

For “Thaumarchaeota” versus “Nitrososphaeria,” preserve the name used by each source and normalize only after checking the ontology release, because archaeal ranks and names have changed.

### E. Environmental and physiological nodes

- Aerobic environment — candidate `ENVO:00002010`
- Microaerophilic condition — label-only pending preferred ontology term
- Geothermal spring — `ENVO:00000051`
- Acidic environment, high-temperature environment, oligotrophic environment, marine water column, soil, and methane-seep sediment — verify exact ENVO terms before encoding
- Molecular hydrogen as electron donor — `CHEBI:18276`
- Ammonia oxidation/nitrification — biological-process node; use a verified GO/METPO mapping
- Thermoacidophily, chemolithoautotrophy, and ammonia-oxidizing archaeon — phenotype labels if no project-standard ontology record is available

No organelle node is appropriate. These reactions are archaeal cytosolic metabolic chemistry, although enzymes may associate with larger complexes; the retrieved evidence does not justify a more specific subcellular localization.

## 3. Curation-ready causal edges

The following table separates direct biochemical evidence from structural, comparative, and metagenomic inference.

| subject | predicate | object | taxon/variant | evidence strength | DOI/year | short verbatim supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| 3-hydroxypropionate/4-hydroxybutyrate cycle | converts | acetyl-CoA to succinyl-CoA to 4-hydroxybutyrate to two acetyl-CoA | shared HP/HB cycle | strong (biochemical/review synthesis) | 10.3389/fmicb.2021.712030 / 2021 | “acetyl-CoA is carboxylated to succinyl-CoA, which is then reduced to two acetyl-CoA molecules” (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2) | Good top-level pathway edge for trait scope. |
| 3-hydroxypropionate/4-hydroxybutyrate cycle | includes intermediate | 4-hydroxybutyrate | shared HP/HB cycle | strong | 10.3389/fmicb.2021.712030 / 2021 | “with 4-hydroxybutyrate as the key intermediate” (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2) | Supports explicit metabolite node for 4HB. |
| acetyl-CoA/propionyl-CoA carboxylase | catalyzes carboxylation of | acetyl-CoA and propionyl-CoA | HP/HB vs DC/HB distinction | strong | 10.3389/fmicb.2021.712030 / 2021 | “a promiscuous acetyl-CoA/propionyl-CoA carboxylase catalyzes both acetyl-CoA and propionyl-CoA carboxylations in the HP/HB cycle” (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2) | Directly distinguishes HP/HB from DC/HB; curate as key pathway-defining enzyme. |
| acetyl-CoA/propionyl-CoA carboxylase | fixes | two molecules of HCO3− to produce succinyl-CoA | shared HP/HB feature | moderate (review/mechanistic summary) | 10.3389/fmicb.2020.592631 / 2020 | “acetyl-CoA/propionyl-CoA carboxylase fixes two molecules of HCO−3 to produce succinylCoA” (hawkins2013roleof4hydroxybutyratecoa pages 1-2) | Useful overall carbon-fixation edge; wording from review, not direct enzymology in this excerpt. |
| HP/HB cycle | occurs in | thermoacidophilic, (micro)aerobic, hydrogen-oxidizing Sulfolobales | crenarchaeal variant | strong | 10.1128/mSphere.01079-20 / 2021 | “functions in thermoacidophilic, (micro)aerobic, hydrogen-oxidizing Crenarchaeota of the order Sulfolobales” (liu2021convergentevolutionof pages 1-2) | Good environment/physiology edge; taxon-specific. |
| HP/HB cycle | occurs in | mesophilic, aerobic, ammonia-oxidizing Thaumarchaeota | thaumarchaeal variant | strong | 10.1128/mSphere.01079-20 / 2021 | “as well as in mesophilic, aerobic, ammonia-oxidizing Thaumarchaeota” (liu2021convergentevolutionof pages 1-2) | Good environment/physiology edge; taxon-specific. |
| thaumarchaeal HP/HB variant | saves | two ATP equivalents per turn relative to crenarchaeal variant | Thaumarchaeota vs Sulfolobales | strong | 10.1128/mSphere.01079-20 / 2021 | “the thaumarchaeal variant saves two ATP equivalents per turn” (liu2021convergentevolutionof pages 1-2) | Important comparative energetic edge. |
| thaumarchaeal 3HP/4HB cycle | is | most energy-efficient aerobic carbon fixation pathway | Thaumarchaeota | strong | 10.1038/s42003-024-06432-x / 2024 | “currently considered the most energy-efficient aerobic carbon fixation pathway” (johnson2024crystalstructureof pages 1-2) | Strong recent expert framing; trait-level contextual edge. |
| Nmar_0206 | catalyzes | 4-hydroxybutyrate + CoA → 4-hydroxybutyryl-CoA | Nitrosopumilus maritimus / thaumarchaeal variant | strong (structural/mechanistic) | 10.1038/s42003-024-06432-x / 2024 | “catalyzes the conversion of 4HB and CoA to 4HB-CoA” (johnson2024crystalstructureof pages 1-2) | Good gene→reaction edge for thaumarchaeal variant. |
| Nmar_0206 | is | ADP-forming 4-hydroxybutyryl-CoA synthetase | Nitrosopumilus maritimus | strong | 10.1038/s42003-024-06432-x / 2024 | “the ADP-forming 4-hydroxybutyryl-CoA synthetase” (johnson2024crystalstructureof pages 1-2) | Distinguish from AMP-forming crenarchaeal enzymes. |
| ADP-forming 4-hydroxybutyryl-CoA synthetase (Nmar_0206) | conserves phosphate / reduces energetic burden | compared with AMP-forming alternative | thaumarchaeal variant | strong | 10.1038/s42003-024-06432-x / 2024 | “This phosphate conservation results in a reduced energetic burden on the cell” (johnson2024crystalstructureof pages 1-2) | Curate as mechanistic basis for energy efficiency. |
| Msed_0406 | ligates CoA to | 4-hydroxybutyrate | Metallosphaera sedula / crenarchaeal variant | strong (biochemical) | 10.1074/jbc.M112.413195 / 2013 | “Msed_0406 is likely the physiologically relevant enzyme in the cycle” (hawkins2013roleof4hydroxybutyratecoa pages 2-2) | Use cautious wording: biochemically active; physiological relevance inferred from activity + transcriptomics. |
| Msed_1321 | dehydrates | 4-hydroxybutyryl-CoA | Metallosphaera sedula | strong (biochemical pathway reconstruction) | 10.1128/AEM.04146-13 / 2014 | “4-hydroxybutyryl-CoA dehydratase (Msed_1321)” (hawkins2014conversionof4hydroxybutyrate pages 1-2) | Reaction assignment supported in reconstructed terminal pathway. |
| Msed_2001 | catalyzes | 3-hydroxypropionyl-CoA dehydration | Metallosphaera sedula | strong | 10.1128/mSphere.01079-20 / 2021 | “both reactions are catalyzed… by a promiscuous 3-hydroxypropionyl-CoA dehydratase/crotonyl-CoA hydratase (Msed_2001” (liu2021convergentevolutionof pages 1-2) | Curate as bifunctional enzyme. |
| Msed_2001 | catalyzes | crotonyl-CoA hydration | Metallosphaera sedula | strong | 10.1128/mSphere.01079-20 / 2021 | “both reactions are catalyzed… by a promiscuous 3-hydroxypropionyl-CoA dehydratase/crotonyl-CoA hydratase (Msed_2001” (liu2021convergentevolutionof pages 1-2) | Same source supports both catalytic edges. |
| Nmar_1308 | catalyzes | 3-hydroxypropionyl-CoA dehydration | Nitrosopumilus maritimus | strong | 10.1128/mSphere.01079-20 / 2021 | “and Nmar_1308 in thaumarchaeon Nitrosopumilus maritimus” (liu2021convergentevolutionof pages 1-2) | Curate as thaumarchaeal bifunctional homolog. |
| Nmar_1308 | catalyzes | crotonyl-CoA hydration | Nitrosopumilus maritimus | strong | 10.1128/mSphere.01079-20 / 2021 | “both reactions are catalyzed… by a promiscuous 3-hydroxypropionyl-CoA dehydratase/crotonyl-CoA hydratase” (liu2021convergentevolutionof pages 1-2) | Same evidence supports second reaction. |
| Nmar_1028 | catalyzes | (S)-3-hydroxybutyryl-CoA dehydrogenase reaction | Nitrosopumilus maritimus | strong (biochemical) | 10.3389/fmicb.2021.712030 / 2021 | “heterologously produced the protein Nmar_1028 catalyzing this reaction” (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2) | Direct enzyme characterization. |
| Nmar_1028 | is essential for functioning of | 3HP/4HB cycle | Nitrosopumilus maritimus | moderate-strong | 10.3389/fmicb.2021.712030 / 2021 | “is thus essential for the functioning of the 3-hydroxypropionate/4-hydroxybutyrate cycle” (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2) | Organism-specific essentiality inferred because it appears to be the only such dehydrogenase in this genome. |
| archaeal 4-hydroxybutyryl-CoA dehydratase | evolved | oxygen tolerance | aerobic archaea / AOA context | moderate (preprint structural study) | 10.1101/2020.02.05.935528 / 2020 | “4HBD active site evolved oxygen tolerance to support aerobic metabolism” (from search result summary) | Useful but preprint-only in retrieved evidence; flag for caution before hard curation. |
| HP/HB cycle genomic potential | detected in | Bacteria | broad distribution inference | moderate (genome inference) | 10.1093/pnasnexus/pgac226 / 2022 | “the genomic potential for carbon fixation through the 3-hydroxypropionate/4-hydroxybutyrate cycle… was also detected in the Bacteria” (garritano2022carbonfixationpathways pages 1-2) | Do not curate as established phenotype without biochemical validation. |
| Sulfolobales in alkaline springs | may use | 3HP/4HB cycle | geothermal MAG inference | weak-moderate (metagenomic inference) | 10.1038/s41467-024-48498-5 / 2024 | “only possessed the 3HP/4HB cycle, suggesting that 3HP/4HB might also be” (qi2024analysisofnearly pages 7-8) | Keep as ecological hypothesis/inference, not definitive trait assignment. |
| geothermal archaeal community structure | is influenced by | temperature and pH | Tengchong geothermal springs | strong (community genomics) | 10.1038/s41467-024-48498-5 / 2024 | “strongly influenced by temperature and pH” (qi2024analysisofnearly pages 1-2) | Good environmental-context edge, but not specific to this pathway alone. |
| thaumarchaeal 3HP/4HB cycle | may account for | ~1% of global carbon fixation | global biogeochemistry estimate | moderate | 10.1038/s42003-024-06432-x / 2024 | “may be responsible for 1% of global carbon fixation” (johnson2024crystalstructureof pages 1-2) | Useful statistic for report context; not a causal-graph edge unless adding ecosystem-scale node. |


*Table: This table compiles compact, curation-ready candidate causal edges for traitmech:000024, separating direct biochemical evidence from structural, comparative, and metagenomic inference. It is useful as a starting point for selecting graph edges that are strong enough for TraitMech curation and for flagging claims that need caution.*

### Additional reaction-level edges recommended for the YAML

The following can be encoded as a sequential pathway module, but exact enzyme assignments should be variant-specific:

1. `acetyl-CoA/propionyl-CoA carboxylase —catalyzes→ acetyl-CoA + HCO3− + ATP → malonyl-CoA`
2. `malonyl-CoA reductase —catalyzes→ malonyl-CoA → malonate semialdehyde`
3. `malonate-semialdehyde reductase —catalyzes→ malonate semialdehyde → 3-hydroxypropionate`
4. `3-hydroxypropionyl-CoA synthetase —activates→ 3-hydroxypropionate to 3-hydroxypropionyl-CoA`
5. `Msed_2001 or Nmar_1308 —dehydrates→ 3-hydroxypropionyl-CoA to acryloyl-CoA`
6. `acryloyl-CoA reductase —reduces→ acryloyl-CoA to propionyl-CoA`
7. `acetyl-CoA/propionyl-CoA carboxylase —carboxylates→ propionyl-CoA to methylmalonyl-CoA`
8. `methylmalonyl-CoA isomerization module —converts→ methylmalonyl-CoA to succinyl-CoA`
9. `succinyl-CoA reductase —reduces→ succinyl-CoA to succinate semialdehyde`
10. `succinate-semialdehyde reductase —reduces→ succinate semialdehyde to 4-hydroxybutyrate`
11. `Msed_0406 or Nmar_0206 —ligates CoA to→ 4-hydroxybutyrate`
12. `Msed_1321 or corresponding thaumarchaeal 4HBD —dehydrates→ 4-hydroxybutyryl-CoA to crotonyl-CoA`
13. `Msed_2001 or Nmar_1308 —hydrates→ crotonyl-CoA to (S)-3-hydroxybutyryl-CoA`
14. `Nmar_1028 or crenarchaeal counterpart —oxidizes→ (S)-3-hydroxybutyryl-CoA to acetoacetyl-CoA`
15. `acetoacetyl-CoA thiolase —cleaves with CoA→ acetoacetyl-CoA to two acetyl-CoA`
16. `one product acetyl-CoA —regenerates→ cycle carbon acceptor`
17. `second product acetyl-CoA —supplies→ biosynthesis`

The overall sequence and terminal β-oxidation-like reactions are directly described in the biochemical literature: crotonyl-CoA is hydrated to (S)-3-hydroxybutyryl-CoA, oxidized to acetoacetyl-CoA, and cleaved into two acetyl-CoA molecules. (hawkins2014conversionof4hydroxybutyrate pages 1-2, liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)

## 4. Recent developments, applications, and quantitative findings

### 2024 structural mechanism

Johnson et al., published in October 2024, solved the 2.8-Å crystal structure of the *N. maritimus* ADP-forming 4-hydroxybutyryl-CoA synthetase Nmar_0206 (`PDB:8WZU`). The enzyme forms a homodimer and uses an ATP-grasp architecture and phosphohistidine intermediate. Unlike AMP-forming Sulfolobales enzymes, it preserves ADP and therefore expends one rather than two ATP equivalents for 4HB activation. Together with ADP-forming Nmar_1309, this explains the two-ATP-per-turn advantage of the thaumarchaeal pathway. The authors describe this variant as the most energy-efficient known aerobic carbon-fixation pathway. (johnson2024crystalstructureof pages 2-3, johnson2024crystalstructureof pages 1-2)

That study also states that thaumarchaeal 3HP/4HB fixation “may be responsible for 1% of global carbon fixation.” This is an ecosystem-scale estimate, not a directly measured universal fraction, and should not become a mechanistic graph edge. (johnson2024crystalstructureof pages 1-2)

### 2024 geothermal ecology

Qi et al., accepted 2 May 2024, analyzed **152 metagenomes from 48 Tengchong geothermal springs**, reconstructed **2,949 archaeal MAGs spanning 12 phyla**, and reported **392 newly identified species**, increasing represented archaeal species diversity by approximately **48.6%**. Temperature and pH strongly structured the communities. Sulfolobales MAGs in acidic springs encoded 3HP/4HB or DC/4HB pathways; some abundant Sulfolobales from alkaline springs were inferred to possess only 3HP/4HB, suggesting a broader geothermal niche than the conventional thermoacidophilic description. These are genome-resolved and transcriptomic ecological observations, not biochemical validation in each MAG. (qi2024analysisofnearly pages 7-8, qi2024analysisofnearly pages 1-2)

### Distribution beyond established archaeal carriers

A 2022 analysis screened **52,515 MAGs**, confidently identified carbon-fixation pathways in **1,007 genomes**, and reported putative 3HP/4HB genomic potential in Bacteria, including association with photosynthesis in *Luminiphilus*. This expands candidate distribution but does not by itself demonstrate that a complete pathway operates in vivo; promiscuous enzymes and incorrect directionality remain important risks. (garritano2022carbonfixationpathways pages 1-2)

### Current applications

The complete cycle is not yet a mature industrial carbon-capture implementation. Current uses are principally:

- **Enzyme discovery and synthetic-pathway design.** Its oxygen tolerance and the phosphate-conserving thaumarchaeal enzymes are attractive components for engineered aerobic carbon fixation. Nmar_0206 and Nmar_1309 are especially relevant because they reduce ATP demand. (johnson2024crystalstructureof pages 1-2)
- **Partial-module production of chemicals.** A three-enzyme *M. sedula* acetyl-CoA→3HP module transferred into *Pyrococcus furiosus* produced approximately **0.5 g L−1 3HP at 72°C**. This demonstrates application of a subpathway, not transfer of the complete autotrophic cycle. (straub2018biotechnologyofextremely pages 11-14)
- **Heterologous production of value-added compounds.** Enzyme-level knowledge is explicitly viewed as necessary to transfer the cycle into heterologous hosts, but pathway burden, cofactor supply, oxygen sensitivity of some components, and competition with central metabolism remain barriers. (liu2021convergentevolutionof pages 1-2)
- **Environmental interpretation.** The pathway connects nitrification to dark-ocean and soil carbon assimilation in ammonia-oxidizing archaea. AOA are described as abundant controllers of oceanic and soil nitrification and important contributors to dark-ocean primary production. (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)

## 5. Expert interpretation

The strongest modern interpretation is that “3HP/4HB cycle” denotes a **family of two independently evolved archaeal solutions with the same metabolic topology**, not a single conserved enzyme cassette. Mechanistically difficult reactions tend to retain related enzymes, whereas many apparently simpler reactions use nonhomologous proteins in Sulfolobales and Thaumarchaeota. Therefore, TraitMech should model a shared pathway core plus taxon-specific enzyme alternatives rather than requiring one universal marker set. (liu2021convergentevolutionof pages 1-2)

For phenotype prediction, a robust rule should require multiple diagnostic elements: the bifunctional acetyl-CoA/propionyl-CoA carboxylase chemistry; enzymes connecting malonyl-CoA through 3HP to propionyl-CoA; and the 4HB regeneration arm. The shared 4HB arm alone cannot distinguish 3HP/4HB from DC/4HB, and individual hydratases or dehydrogenases are not diagnostic. (liu2021convergentevolutionof pages 1-2, liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)

## 6. Warnings: claims not yet ready for hard curation

1. **Do not curate all Sulfolobales, Thaumarchaeota/Nitrososphaeria, or AOA as trait-positive.** Use strain/genome-specific evidence.
2. **Do not treat bacterial MAG predictions as experimentally established 3HP/4HB phenotypes.** Mark them `uncertain: true` or omit them pending isotope-flux or biochemical confirmation. (garritano2022carbonfixationpathways pages 1-2)
3. **Do not use “pyruvate synthase + PEP carboxylase” as positive markers for 3HP/4HB.** Those define DC/4HB carbon entry. The 2024 geothermal study’s pathway-marker wording should be checked against its methods and supplement before importing marker-level edges. (qi2024analysisofnearly pages 7-8, liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)
4. **Do not curate Nmar_1028 as universally diagnostic.** It appears essential in *N. maritimus* because it is the only suitable enzyme there, but the activity is neither unique nor characteristic of 3HP/4HB. (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)
5. **Represent Msed_0406 physiological assignment cautiously.** Both Msed_0406 and Msed_0394 exhibit 4HB-CoA synthetase activity; transcriptomic and kinetic evidence favors Msed_0406. (hawkins2013roleof4hydroxybutyratecoa pages 2-2)
6. **Do not assert a single ATP cost for both variants.** Sulfolobales and thaumarchaeal cycles differ by two ATP equivalents per turn. Older reviews may report the crenarchaeal cost without making this distinction. (straub2018biotechnologyofextremely pages 11-14, liu2021convergentevolutionof pages 1-2)
7. **Do not encode oxygen as a universal obligate substrate.** The established carriers are aerobic or microaerophilic, but oxygen is environmental/respiratory context rather than a stoichiometric substrate of the carbon-fixation cycle.
8. **Do not equate 3HP synthesis with the full trait.** Industrial 3HP modules terminate before propionyl-CoA, succinyl-CoA, 4HB, and acceptor regeneration.
9. **Verify all ontology mappings locally.** In particular, archaeal taxonomy, protonation-state-specific ChEBI records, EC numbers for promiscuous enzymes, and Rhea reaction directionality should be checked against current releases.

## 7. DOI-first bibliography

1. Berg IA, Kockelkorn D, Buckel W, Fuchs G. “A 3-hydroxypropionate/4-hydroxybutyrate autotrophic carbon dioxide assimilation pathway in Archaea.” *Science*. **14 December 2007**. https://doi.org/10.1126/science.1149976
2. Hawkins AS, Han Y, Bennett RK, Adams MWW, Kelly RM. “Role of 4-Hydroxybutyrate-CoA Synthetase in the CO2 Fixation Cycle in Thermoacidophilic Archaea.” *Journal of Biological Chemistry*. **February 2013**. https://doi.org/10.1074/jbc.M112.413195 (hawkins2013roleof4hydroxybutyratecoa pages 2-2, hawkins2013roleof4hydroxybutyratecoa pages 1-2)
3. Hawkins AB, Adams MWW, Kelly RM. “Conversion of 4-Hydroxybutyrate to Acetyl Coenzyme A and Its Anapleurosis in the Metallosphaera sedula 3-Hydroxypropionate/4-Hydroxybutyrate Carbon Fixation Pathway.” *Applied and Environmental Microbiology*. **April 2014**. https://doi.org/10.1128/AEM.04146-13 (hawkins2014conversionof4hydroxybutyrate pages 1-2)
4. Otte J et al. “Malonic Semialdehyde Reductase from the Archaeon Nitrosopumilus maritimus Is Involved in the Autotrophic 3-Hydroxypropionate/4-Hydroxybutyrate Cycle.” *Applied and Environmental Microbiology*. **March 2015**. https://doi.org/10.1128/AEM.03390-14
5. Straub CT et al. “Biotechnology of extremely thermophilic archaea.” *FEMS Microbiology Reviews*. **June 2018**. https://doi.org/10.1093/femsre/fuy012 (straub2018biotechnologyofextremely pages 11-14)
6. Liu L et al. “Convergent Evolution of a Promiscuous 3-Hydroxypropionyl-CoA Dehydratase/Crotonyl-CoA Hydratase in Crenarchaeota and Thaumarchaeota.” *mSphere*. **20 January 2021**. https://doi.org/10.1128/mSphere.01079-20 (liu2021convergentevolutionof pages 1-2)
7. Liu L et al. “(S)-3-Hydroxybutyryl-CoA Dehydrogenase From the Autotrophic 3-Hydroxypropionate/4-Hydroxybutyrate Cycle in Nitrosopumilus maritimus.” *Frontiers in Microbiology*. **5 July 2021**. https://doi.org/10.3389/fmicb.2021.712030 (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2)
8. Garritano AN, Song W, Thomas T. “Carbon fixation pathways across the bacterial and archaeal tree of life.” *PNAS Nexus*. **4 October 2022**. https://doi.org/10.1093/pnasnexus/pgac226 (garritano2022carbonfixationpathways pages 1-2)
9. Bierbaumer S et al. “Enzymatic Conversion of CO2: From Natural to Artificial Utilization.” *Chemical Reviews*. **2023**. https://doi.org/10.1021/acs.chemrev.2c00581 (bierbaumer2023enzymaticconversionof pages 19-21)
10. Qi Y-L et al. “Analysis of nearly 3000 archaeal genomes from terrestrial geothermal springs sheds light on interconnected biogeochemical processes.” *Nature Communications*. **Accepted 2 May 2024; published May 2024**. https://doi.org/10.1038/s41467-024-48498-5 (qi2024analysisofnearly pages 7-8, qi2024analysisofnearly pages 1-2)
11. Johnson J et al. “Crystal structure of the 4-hydroxybutyryl-CoA synthetase (ADP-forming) from Nitrosopumilus maritimus.” *Communications Biology*. **October 2024**. https://doi.org/10.1038/s42003-024-06432-x (johnson2024crystalstructureof pages 2-3, johnson2024crystalstructureof pages 1-2)

### Recommended minimum graph expansion

For an immediate, conservative update beyond the existing 11-node/10-edge Sulfolobales graph, add: (i) the two bicarbonate-fixing carboxylation events; (ii) explicit malonyl-CoA→3HP→propionyl-CoA and succinyl-CoA→4HB modules; (iii) terminal regeneration to two acetyl-CoA; (iv) alternative crenarchaeal versus thaumarchaeal synthetases; (v) bifunctional Msed_2001/Nmar_1308; and (vi) evidence qualifiers distinguishing direct biochemistry from MAG-based predictions.

References

1. (hawkins2014conversionof4hydroxybutyrate pages 1-2): Aaron B. Hawkins, Michael W. W. Adams, and Robert M. Kelly. Conversion of 4-hydroxybutyrate to acetyl coenzyme a and its anapleurosis in the metallosphaera sedula 3-hydroxypropionate/4-hydroxybutyrate carbon fixation pathway. Applied and Environmental Microbiology, 80:2536-2545, Apr 2014. URL: https://doi.org/10.1128/aem.04146-13, doi:10.1128/aem.04146-13. This article has 45 citations and is from a peer-reviewed journal.

2. (hawkins2013roleof4hydroxybutyratecoa pages 1-2): Aaron S. Hawkins, Yejun Han, Robert K. Bennett, Michael W.W. Adams, and Robert M. Kelly. Role of 4-hydroxybutyrate-coa synthetase in the co2 fixation cycle in thermoacidophilic archaea. Feb 2013. URL: https://doi.org/10.1074/jbc.m112.413195, doi:10.1074/jbc.m112.413195. This article has 51 citations and is from a domain leading peer-reviewed journal.

3. (liu2021(s)3hydroxybutyrylcoadehydrogenasefrom pages 1-2): Li Liu, Daniel M. Schubert, Martin Könneke, and Ivan A. Berg. (s)-3-hydroxybutyryl-coa dehydrogenase from the autotrophic 3-hydroxypropionate/4-hydroxybutyrate cycle in nitrosopumilus maritimus. Frontiers in Microbiology, Jul 2021. URL: https://doi.org/10.3389/fmicb.2021.712030, doi:10.3389/fmicb.2021.712030. This article has 15 citations and is from a peer-reviewed journal.

4. (liu2021convergentevolutionof pages 1-2): Li Liu, Philip C. Brown, Martin Könneke, Harald Huber, Simone König, and Ivan A. Berg. Convergent evolution of a promiscuous 3-hydroxypropionyl-coa dehydratase/crotonyl-coa hydratase in <i>crenarchaeota</i> and <i>thaumarchaeota</i>. Feb 2021. URL: https://doi.org/10.1128/msphere.01079-20, doi:10.1128/msphere.01079-20. This article has 8 citations and is from a peer-reviewed journal.

5. (johnson2024crystalstructureof pages 1-2): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 6 citations and is from a peer-reviewed journal.

6. (garritano2022carbonfixationpathways pages 1-2): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 130 citations and is from a peer-reviewed journal.

7. (qi2024analysisofnearly pages 7-8): Yan-Ling Qi, Ya-Ting Chen, Yuan-Guo Xie, Yu-Xian Li, Yang-Zhi Rao, Meng-Meng Li, Qi-Jun Xie, Xing-Ru Cao, Lei Chen, Yan-Ni Qu, Zhen-Xuan Yuan, Zhi-Chao Xiao, Lu Lu, Jian-Yu Jiao, Wen-Sheng Shu, Wen-Jun Li, Brian P. Hedlund, and Zheng-Shuang Hua. Analysis of nearly 3000 archaeal genomes from terrestrial geothermal springs sheds light on interconnected biogeochemical processes. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48498-5, doi:10.1038/s41467-024-48498-5. This article has 61 citations and is from a highest quality peer-reviewed journal.

8. (hawkins2013roleof4hydroxybutyratecoa pages 2-2): Aaron S. Hawkins, Yejun Han, Robert K. Bennett, Michael W.W. Adams, and Robert M. Kelly. Role of 4-hydroxybutyrate-coa synthetase in the co2 fixation cycle in thermoacidophilic archaea. Feb 2013. URL: https://doi.org/10.1074/jbc.m112.413195, doi:10.1074/jbc.m112.413195. This article has 51 citations and is from a domain leading peer-reviewed journal.

9. (qi2024analysisofnearly pages 1-2): Yan-Ling Qi, Ya-Ting Chen, Yuan-Guo Xie, Yu-Xian Li, Yang-Zhi Rao, Meng-Meng Li, Qi-Jun Xie, Xing-Ru Cao, Lei Chen, Yan-Ni Qu, Zhen-Xuan Yuan, Zhi-Chao Xiao, Lu Lu, Jian-Yu Jiao, Wen-Sheng Shu, Wen-Jun Li, Brian P. Hedlund, and Zheng-Shuang Hua. Analysis of nearly 3000 archaeal genomes from terrestrial geothermal springs sheds light on interconnected biogeochemical processes. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48498-5, doi:10.1038/s41467-024-48498-5. This article has 61 citations and is from a highest quality peer-reviewed journal.

10. (johnson2024crystalstructureof pages 2-3): Jerome Johnson, Bradley B. Tolar, Bilge Tosun, Yasuo Yoshikuni, Christopher A. Francis, Soichi Wakatsuki, and Hasan DeMirci. Crystal structure of the 4-hydroxybutyryl-coa synthetase (adp-forming) from nitrosopumilus maritimus. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06432-x, doi:10.1038/s42003-024-06432-x. This article has 6 citations and is from a peer-reviewed journal.

11. (straub2018biotechnologyofextremely pages 11-14): Christopher T Straub, James A. Counts, Diep Nguyen, Chang-Hao Wu, Benjamin Zeldes, James R. Crosby, Jonathan M. Conway, J. Otten, G. Lipscomb, G. Schut, M. Adams, and R. Kelly. Biotechnology of extremely thermophilic archaea. FEMS microbiology reviews, 42 5:543-578, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy012, doi:10.1093/femsre/fuy012. This article has 132 citations and is from a domain leading peer-reviewed journal.

12. (bierbaumer2023enzymaticconversionof pages 19-21): Sarah Bierbaumer, Maren Nattermann, Luca Schulz, Reinhard Zschoche, Tobias J. Erb, Christoph K. Winkler, Matthias Tinzl, and Silvia M. Glueck. Enzymatic conversion of co2: from natural to artificial utilization. Chemical Reviews, 123:5702-5754, Jan 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00581, doi:10.1021/acs.chemrev.2c00581. This article has 308 citations and is from a highest quality peer-reviewed journal.