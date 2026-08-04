---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:33:59.338032'
end_time: '2026-08-04T06:40:32.549997'
duration_seconds: 393.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mixed-acid fermentation
  trait_identifier: traitmech:000027
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: mixed_acid_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which sugars are converted via the glycolytic pathway
    to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and
    H2. Characteristic of enteric bacteria such as Escherichia coli.
  parent_traits: METPO:1002005
  synonyms: ''
  evidence_summary: 'DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy
    conservation lists acetate, ethanol, lactate, succinate and formate as products
    of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation
    pathways describes mixed-acid fermentation by enterobacteria and its characteristic
    acid product spectrum.)'
  causal_graph_summary: 'mixed_acid_fermentation_enterobacterial: 15 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixed-acid fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000027
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which sugars are converted via the glycolytic pathway to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and H2. Characteristic of enteric bacteria such as Escherichia coli.
- **Parent traits:** METPO:1002005
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation lists acetate, ethanol, lactate, succinate and formate as products of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation pathways describes mixed-acid fermentation by enterobacteria and its characteristic acid product spectrum.)
- **Existing causal graph summary:** mixed_acid_fermentation_enterobacterial: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **mixed-acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/mixed_acid_fermentation.yaml`.

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
- **Trait label:** mixed-acid fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000027
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which sugars are converted via the glycolytic pathway to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and H2. Characteristic of enteric bacteria such as Escherichia coli.
- **Parent traits:** METPO:1002005
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation lists acetate, ethanol, lactate, succinate and formate as products of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation pathways describes mixed-acid fermentation by enterobacteria and its characteristic acid product spectrum.)
- **Existing causal graph summary:** mixed_acid_fermentation_enterobacterial: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **mixed-acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/mixed_acid_fermentation.yaml`.

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


# Curation report: mixed-acid fermentation

## Trait record and scope

- **Trait:** mixed-acid fermentation
- **Identifier:** `traitmech:000027`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1002005`

Mixed-acid fermentation is best modeled as an **anaerobic fermentative capacity**, rather than the production of any single acid. In the canonical enterobacterial implementation represented by *Escherichia coli*, glycolysis supplies pyruvate, ATP, and reducing equivalents; carbon then partitions among formate, acetate, ethanol, lactate, and succinate, while formate may subsequently be converted to H₂ and CO₂. The parallel branches jointly conserve ATP and restore redox balance when oxygen or another usable terminal electron acceptor is unavailable. (fa¶rster2014metabolicengineeringof pages 1-2, taggar2024hydrogenproductionvia pages 5-7)

The phenotype is therefore supported most strongly by a **product spectrum plus anaerobic pathway activity**, not merely by detecting acetate, lactate, or formate. In one anaerobic glucose experiment, *E. coli* produced approximately 35 mM acetate and 15 mM formate, together with lactate and succinate; the exact ratios are medium-, strain-, pH-, and growth-phase-dependent and should not be made definitional. (metcalfe2020onlineanalysisand pages 9-10)

### Boundaries and nearby traits

1. **Homolactic fermentation:** predominantly reduces pyruvate to lactate. Lactate production alone is insufficient to establish mixed-acid fermentation.
2. **2,3-Butanediol fermentation:** common in some enterobacteria but channels pyruvate through acetoin/2,3-butanediol. It should remain a neighboring trait unless the organism demonstrably produces the mixed-acid spectrum.
3. **Alcoholic or solvent fermentation:** ethanol can be one mixed-acid product, but ethanol-dominant engineered strains are not necessarily performing the native mixed-acid phenotype.
4. **Aerobic acetate overflow:** acetate secretion during rapid aerobic growth is not mixed-acid fermentation, despite sharing Pta–AckA chemistry.
5. **Anaerobic respiration:** growth using nitrate, fumarate, or another external terminal electron acceptor is respiration, not fermentation, even if fermentation products coexist.
6. **Formate-hydrogenlyase activity:** H₂/CO₂ production is an important enterobacterial submodule, but it is not universally present in every organism described phenotypically as a mixed-acid fermenter.
7. **Methyl-red phenotype:** sustained acidification is a useful assay proxy, but a positive indicator test is not by itself a complete mechanistic definition.

## Candidate causal-graph nodes

### Trait and process nodes

- `traitmech:000027` — mixed-acid fermentation
- `METPO:1002005` — supplied parent trait
- Glycolysis — `GO:0006096`
- Fermentation — `GO:0006113`
- Anaerobic cellular respiration — `GO:0045333` (**boundary/exclusion node**, not part of the core trait)
- Redox balancing — label-only candidate
- Substrate-level phosphorylation — label-only candidate pending exact ontology review
- Reductive C4-dicarboxylate/succinate branch — label-only candidate
- Formate-hydrogenlyase pathway — label-only candidate

### Environmental and experimental nodes

- Anaerobiosis / oxygen limitation — label-only or ENVO grounding to be checked against the intended graph schema
- Fermentable sugar availability
- Glucose-fed anaerobic culture
- Acidic extracellular pH
- Stationary versus exponential growth phase
- Closed anaerobic bioreactor
- Exogenous formate addition
- FTIR headspace monitoring
- Raman liquid-phase monitoring

Anaerobiosis should be modeled as a **contextual enabling factor**, not as an absolute universal trigger: facultative enterobacteria can use alternative anaerobic respiratory pathways when suitable electron acceptors are present. FNR and ArcAB coordinate the aerobic-to-anaerobic transition, but the available evidence supports a broad regulatory edge more strongly than individual promoter-level edges. (fa¶rster2014metabolicengineeringof pages 1-2)

### Organisms

- *Escherichia coli* — `NCBITaxon:562`
- Enterobacterales/enteric bacteria — use a taxon-level node only after confirming the desired NCBI rank and identifier
- *Citrobacter*, *Enterobacter*, *Salmonella*, and related taxa — candidate examples, not interchangeable mechanistic evidence

The proposed core graph should be explicitly labeled **enterobacterial/*E. coli*-centric**. Gene-level conservation and product ratios must not be generalized automatically to all organisms called mixed-acid fermenters.

### Genes, proteins, enzymes, and complexes

- `pflB` / pyruvate formate-lyase — `EC:2.3.1.54`
- Pyruvate formate-lyase activating enzyme (`pflA`) — candidate node; activation edge requires direct source confirmation before curation
- `focA` / formate channel
- `pta` / phosphate acetyltransferase — `EC:2.3.1.8`
- `ackA` / acetate kinase — `EC:2.7.2.1`
- `adhE` / bifunctional acetaldehyde-CoA/alcohol dehydrogenase
- `ldhA` / fermentative D-lactate dehydrogenase — exact EC/GO grounding should be checked for organism-specific directionality
- `ppc` / phosphoenolpyruvate carboxylase — `EC:4.1.1.31`
- `mdh` / malate dehydrogenase — `EC:1.1.1.37`
- `fumB` / fumarase B — `EC:4.2.1.2`
- `frdABCD` / fumarate reductase complex
- Formate hydrogenlyase complex
- `hyc` operon / hydrogenase-3-associated FHL components
- `fnr` / fumarate and nitrate reduction regulator
- `arcA`–`arcB` two-component regulatory system
- `fhlA` / formate-hydrogenlyase transcriptional activator — candidate regulatory node; direct edge evidence was not sufficiently resolved in the retrieved text

### Chemicals and metabolites

- Glucose — `CHEBI:17234`
- Phosphoenolpyruvate — `CHEBI:18021`
- Pyruvate — `CHEBI:15361`
- Acetyl-CoA — `CHEBI:15351`
- Formate — `CHEBI:15740`
- Acetate — `CHEBI:30089`
- Ethanol — `CHEBI:16236`
- Lactate — stereochemistry should be specified; do not collapse D-/L-lactate without evidence
- Succinate — `CHEBI:30031`
- Fumarate — `CHEBI:29806`
- Malate — stereochemistry-specific grounding should be verified
- Carbon dioxide — `CHEBI:16526`
- Dihydrogen — `CHEBI:18276`
- ATP — `CHEBI:15422`
- ADP — `CHEBI:16761`
- NADH — `CHEBI:16908`
- NAD⁺ — `CHEBI:15846`
- Oxygen — `CHEBI:15379`

## Candidate evidence-backed edges

The following table is the proposed first-pass edge set for conversion into `data/traits/metabolism/mixed_acid_fermentation.yaml`.

| subject | predicate | object | evidence/reference DOI | short supporting snippet | confidence/curation note |
|---|---|---|---|---|---|
| anaerobiosis / low O2 | activates | mixed-acid fermentation program in *Escherichia coli* | 10.3389/fbioe.2014.00016 | “Under anaerobic conditions… mixed-acid fermentation produces succinate, formate, acetate, lactate, and ethanol” (fa¶rster2014metabolicengineeringof pages 1-2) | High for *E. coli*; review-backed, condition-specific. |
| FNR | activates / controls shift to | anaerobic fermentation genes | 10.3389/fbioe.2014.00016 | “The global regulators FNR and ArcAB control the shift from aerobic to anaerobic metabolism, with FNR activating anaerobic genes” (fa¶rster2014metabolicengineeringof pages 1-2) | Medium-high; review statement, not edge-resolved to individual target genes here. |
| ArcAB | controls shift from | aerobic metabolism to anaerobic metabolism | 10.3389/fbioe.2014.00016 | “The global regulators FNR and ArcAB control the shift from aerobic to anaerobic metabolism” (fa¶rster2014metabolicengineeringof pages 1-2) | Medium-high; review-backed regulatory edge, broad process-level claim. |
| glycolysis of glucose | produces | pyruvate + ATP + NADH | 10.3389/fbioe.2014.00016 | “Glycolysis converts glucose to pyruvate… yielding ATP and NADH” (fa¶rster2014metabolicengineeringof pages 1-2) | High; core pathway claim from review. |
| pyruvate-formate lyase (PflB/PFL) | cleaves | pyruvate to acetyl-CoA + formate | 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “pyruvate formate lyase (PFL) cleaves pyruvate into acetyl-CoA and formic acid” (taggar2024hydrogenproductionvia pages 5-7) | High; supported by multiple review sources, canonical *E. coli* anaerobic mechanism. |
| FocA formate channel | transports | formate across the membrane | 10.1007/s00216-020-02865-5 | “Formate transport occurs via FocA channel” (metcalfe2020onlineanalysisand pages 9-10) | Medium; supported in the quantitative *E. coli* study summary, but snippet is paraphrased from extracted evidence. |
| acetyl-CoA | is converted by Pta/AckA to | acetate + ATP | 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “Acetate is produced via phosphotransacetylase (Pta) and acetate kinase (AckA)” (fa¶rster2014metabolicengineeringof pages 1-2) | High; canonical pathway. ATP coupling explicit in 2024 review summary. |
| Pta/AckA acetate branch | contributes to | ATP generation during mixed-acid fermentation | 10.35812/cellulosechemtechnol.2024.58.90; 10.3389/fmicb.2020.00233 | “ATP is generated through phosphotransacetylase and acetate kinase acting on acetyl-CoA” (taggar2024hydrogenproductionvia pages 5-7) | High; strong mechanistic support, especially for anaerobic *E. coli*. |
| AdhE | converts acetyl-CoA branch to | ethanol while oxidizing NADH | 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “Ethanol is synthesized by alcohol dehydrogenase (AdhE) consuming NADH” (fa¶rster2014metabolicengineeringof pages 1-2) | High; canonical redox-balancing edge. |
| LdhA | reduces pyruvate to | lactate | 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “Lactate dehydrogenase (LdhA) reduces pyruvate to lactate” (fa¶rster2014metabolicengineeringof pages 1-2) | High; canonical branch. |
| phosphoenolpyruvate carboxylase (Ppc) / PEP carboxylation | initiates | succinate branch from PEP | 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “Succinate forms through PEP carboxylase (Ppc)” (fa¶rster2014metabolicengineeringof pages 1-2) | High; review-backed, pathway-level edge. |
| reductive TCA succinate branch (Mdh, FumB, Frd) | produces | succinate | 10.3389/fbioe.2014.00016 | “Succinate forms through PEP carboxylase (Ppc), malate dehydrogenase (Mdh), fumarase (FumB), and fumarate reductase (Frd)” (fa¶rster2014metabolicengineeringof pages 1-2) | High; pathway/module edge. |
| acid accumulation during mixed-acid fermentation | decreases | culture pH to ~5.5 during exponential growth | 10.1007/s00216-020-02865-5 | “pH drops to 5.5 during exponential growth due to acid accumulation” (metcalfe2020onlineanalysisand pages 9-10) | High for the reported *E. coli* closed anaerobic glucose system; assay-specific quantitative edge. |
| acidic pH | enhances | FHL activity / formate cleavage | 10.1007/s00216-020-02865-5; 10.3389/fbioe.2014.00016; 10.35812/cellulosechemtechnol.2024.58.90 | “FHL… produces H2 and CO2, with activity enhanced at pH 5.5 versus neutral pH” (metcalfe2020onlineanalysisand pages 9-10) | High for *E. coli*; condition-specific pH effect. |
| formate hydrogenlyase (FHL; Hyd-3/Hyc complex) | cleaves | formate to H2 + CO2 | 10.1007/s00216-020-02865-5; 10.35812/cellulosechemtechnol.2024.58.90 | “The formate:hydrogen lyase (FHL) complex then cleaves formate… to produce H2 and CO2” (taggar2024hydrogenproductionvia pages 5-7) | High; central hallmark branch, especially in enteric bacteria. |
| mixed-acid fermentation in *E. coli* | yields | acetate (~35 mM) and formate (~15 mM), plus lactate/succinate/ethanol/CO2 | 10.1007/s00216-020-02865-5 | “Acetate (35 mM), formate (15 mM), lactate, and succinate were produced” (metcalfe2020onlineanalysisand pages 9-10) | High for this experimental setup; useful quantitative phenotype anchor, not universal stoichiometry. |
| exogenous formate addition | decreases / does not improve | formate decomposition and biohydrogen production rate | 10.1007/s00216-020-02865-5 | “adding exogenous formate… is expected to have no beneficial effect on the rate of formate decomposition and biohydrogen production” (metcalfe2020onlineanalysisand pages 9-10) | Medium-high; assay-specific application edge from one *E. coli* study. |
| deletion of competing mixed-acid branches (e.g., ΔldhA ΔadhE ΔackA/pta or related combinations) | redirects flux toward | engineered target products such as ethanol | 10.3389/fbioe.2014.00016 | “LdhA… and AckA deletions to redirect flux toward ethanol” / engineered strains achieved “85-106% ethanol yields” (fa¶rster2014metabolicengineeringof pages 5-7) | Medium-high; metabolic-engineering edge, not native trait mechanism; curate as application/example, not core causal edge. |


*Table: This table lists curation-ready candidate causal edges for traitmech:000027, linking core anaerobic regulation, branch pathways, pH effects, and applied engineering observations to specific DOI-backed evidence. It is useful for translating the literature into a TraitMech causal graph while marking review-based and condition-specific claims.*

### Recommended compact native core

If the existing graph must remain close to its current 15-node/13-edge size, prioritize these edges:

1. anaerobiosis → **enables** → enterobacterial mixed-acid fermentation;
2. glucose → **is catabolized by** → glycolysis;
3. glycolysis → **produces** → pyruvate + ATP + NADH;
4. PflB → **converts** → pyruvate to formate + acetyl-CoA;
5. Pta/AckA → **converts** → acetyl-CoA to acetate + ATP;
6. AdhE → **converts** → acetyl-CoA-derived acetaldehyde to ethanol while reoxidizing NADH;
7. LdhA → **converts** → pyruvate to lactate while reoxidizing NADH;
8. Ppc/reductive C4 branch/Frd → **converts** → PEP to succinate;
9. acid-product accumulation → **decreases** → extracellular pH;
10. acidic pH + formate → **promotes substrate conditions for** → FHL;
11. FHL/Hyc → **converts** → formate to H₂ + CO₂;
12. mixed-acid branches → **support** → redox balance and anaerobic growth.

Pta–AckA is particularly important mechanistically because acetate production couples to ATP generation. Anaerobic mutations in this pathway cause major growth and product-pattern defects, supporting its role as an energy-conserving branch rather than merely a diagnostic by-product. (taggar2024hydrogenproductionvia pages 5-7)

## Quantitative findings and assay evidence

In the 2020 online-monitoring study, an anaerobic culture started with 30 mM glucose and produced approximately 35 mM acetate and 15 mM formate. Acid accumulation lowered pH to about 5.5 during exponential growth; later formate utilization and FHL activity coincided with recovery to approximately pH 5.9. These are valuable assay anchors but not universal trait thresholds. (metcalfe2020onlineanalysisand pages 9-10)

Formate disappearance followed apparent zero-order kinetics at about **0.42 mM h⁻¹** when exogenous formate was added, compared with **0.66 mM h⁻¹** without that addition. Adding 40 mM potassium formate at 3 h did not improve biohydrogen production and slowed product formation, indicating that FHL turnover, transport, or another downstream constraint—not extracellular formate availability alone—limited the measured rate. (metcalfe2020onlineanalysisand pages 10-11)

The same platform reported noise-equivalent detection limits of approximately **2.6 mM acetate** and **3.6 mM formate** at 5-min integration, improving to **0.75 mM** and **1.0 mM**, respectively, at 1 h. Its phosphate-based in situ pH measurement covered pH 6–8 with accuracy better than 0.1 pH unit. These data support FTIR/Raman monitoring as a real-world implementation for phenotype measurement, although lactate and succinate require complementary analytics. (metcalfe2020onlineanalysisand pages 9-10)

A 2024 dark-fermentation review describes the branch-level redox demands as approximately one NADH per pyruvate reduced to lactate and two reducing equivalents for ethanol formation; it also describes the PEP-carboxylation route to succinate and Pta–AckA-dependent ATP formation. Cofactor notation for the succinate branch varies among pathway summaries and should be checked against reaction-level databases before encoding stoichiometric coefficients. (taggar2024hydrogenproductionvia pages 5-7)

## Recent developments and applications

### Biohydrogen and waste conversion

Recent dark-fermentation research treats enterobacterial mixed-acid metabolism as a route from carbohydrate-rich biomass or waste streams to H₂. The relevant graph module is PflB-generated formate followed by acidic-pH-dependent FHL cleavage to H₂ and CO₂. The 2024 review emphasizes oxygen limitation, substrate, pH, and competing reduced products as major yield determinants. (taggar2024hydrogenproductionvia pages 5-7)

The quantitative *E. coli* study cautions against the simple engineering assumption that supplying more formate necessarily increases H₂ output. Its zero-order behavior and adverse response to exogenous formate instead motivate engineering FHL capacity, formate transport, pH control, and flux partitioning. (metcalfe2020onlineanalysisand pages 10-11)

### Organic-acid and biofuel production

Mixed-acid branches are routinely deleted, amplified, or rebalanced to produce ethanol, lactate, succinate, acetate-derived products, or hydrogen. The authoritative pathway review reports that deleting competing branches—including combinations involving `ldhA`, `adhE`, and `ackA-pta`—can redirect carbon toward desired products; reported engineered ethanol strains reached 85–106% of the cited theoretical-yield benchmark under their respective conditions. These are engineered applications, not evidence that the native trait is ethanol-dominant. (fa¶rster2014metabolicengineeringof pages 5-7)

### Process analytics

Combined headspace FTIR and liquid Raman spectroscopy permits continuous, sampling-free monitoring of CO₂, ethanol, acetaldehyde, acetate, formate, phosphate speciation, pH, and optical density. This implementation is valuable for causal-graph validation because it can align product emergence, acidification, growth phase, and formate turnover in time. (metcalfe2020onlineanalysisand pages 9-10, metcalfe2020onlineanalysisand pages 10-11)

## Expert synthesis

The strongest graph architecture is a **condition–regulation–flux-partition–physiology model**:

- oxygen limitation and global regulation establish the anaerobic state;
- glycolysis generates pyruvate, ATP, and reducing equivalents;
- competing pyruvate/PEP branches partition carbon;
- acetate formation contributes ATP;
- lactate and ethanol branches reoxidize NADH;
- the succinate branch provides another reductive sink;
- acid accumulation changes extracellular pH;
- low pH and formate availability favor the FHL module;
- the combined output spectrum operationalizes the trait.

This representation is preferable to a flat “organism produces metabolite” graph because it captures both why multiple products are formed and how environmental conditions alter their distribution. The literature also shows that pathway deletions change anaerobic growth and product patterns, providing intervention-based support for causal rather than purely associative edges. (fa¶rster2014metabolicengineeringof pages 1-2, fa¶rster2014metabolicengineeringof pages 5-7, taggar2024hydrogenproductionvia pages 5-7)

## Warnings: do not yet curate without additional evidence

1. **Do not encode exact universal product ratios.** The 35 mM acetate/15 mM formate values are specific to one *E. coli* culture protocol. (metcalfe2020onlineanalysisand pages 9-10)
2. **Do not make FHL universal.** Some mixed-acid fermenters lack the same Hyc/FHL implementation or produce little detectable H₂.
3. **Do not equate anaerobiosis with fermentation.** Alternative electron acceptors can support anaerobic respiration.
4. **Do not treat FNR or ArcAB as simple unconditional activators of every branch gene.** Their effects are promoter-, redox-, and condition-specific; direct target edges need primary regulatory evidence.
5. **Hold the `FhlA → activates hyc/FHL` edge.** It is biologically plausible and important, but the retrieved evidence did not provide a sufficiently direct supporting passage for this curation round.
6. **Hold the `PflA → activates PflB` edge** until a primary biochemical or genetic source is attached.
7. **Do not infer transport direction for FocA.** Formate flux can be bidirectional and condition-dependent; curate only “transports formate” from the current evidence.
8. **Do not encode NADPH-specific succinate stoichiometry yet.** The 2024 review uses NADPH language, whereas canonical *E. coli* reaction accounting is enzyme- and cofactor-specific. Validate with Rhea/MetaCyc before adding coefficients. (taggar2024hydrogenproductionvia pages 5-7)
9. **Separate native mechanism from engineering interventions.** Gene deletions used to redirect products belong in application or perturbation subgraphs, not the minimal native trait definition. (fa¶rster2014metabolicengineeringof pages 5-7)
10. **Avoid unverified UniProt, KEGG, Rhea, or MetaCyc identifiers.** Map strain-specific proteins only after the reference strain is fixed, preferably *E. coli* K-12 MG1655.
11. **Use stereochemistry-aware metabolite nodes.** `ldhA` typically concerns D-lactate in *E. coli*; generic “lactate” can conceal a biologically meaningful distinction.
12. **The supplied DOI `10.3390/molecules31020333` appears future-dated relative to the requested 2023–2024 priority and was not independently validated here.** It should not be used for curation until its metadata and publication status are confirmed.

## DOI-first bibliography

1. Taggar MS, Kaur A, Jain C, Kalia A, Sooch SS. **Hydrogen production via dark fermentation: a review of influential factors.** *Cellulose Chemistry and Technology.* Published November 2024;58:1051–1063. DOI: [10.35812/cellulosechemtechnol.2024.58.90](https://doi.org/10.35812/cellulosechemtechnol.2024.58.90). (taggar2024hydrogenproductionvia pages 5-7)
2. Metcalfe GD, Smith TW, Hippler M. **On-line analysis and in situ pH monitoring of mixed acid fermentation by Escherichia coli using combined FTIR and Raman techniques.** *Analytical and Bioanalytical Chemistry.* Published August 2020;412:7307–7319. DOI: [10.1007/s00216-020-02865-5](https://doi.org/10.1007/s00216-020-02865-5). (metcalfe2020onlineanalysisand pages 9-10, metcalfe2020onlineanalysisand pages 10-11)
3. Förster AH, Gescher J. **Metabolic engineering of Escherichia coli for production of mixed-acid fermentation end products.** *Frontiers in Bioengineering and Biotechnology.* Published May 2014;2:16. DOI: [10.3389/fbioe.2014.00016](https://doi.org/10.3389/fbioe.2014.00016). (fa¶rster2014metabolicengineeringof pages 1-2, fa¶rster2014metabolicengineeringof pages 5-7)
4. Buckel W. **Energy conservation in fermentations of anaerobic bacteria.** *Frontiers in Microbiology.* Published September 2021;12:703525. DOI: [10.3389/fmicb.2021.703525](https://doi.org/10.3389/fmicb.2021.703525). This is useful background on fermentative energy conservation but is less specific to the enterobacterial graph than the sources above.
5. Schütze A, Benndorf D, Püttker S, et al. **The impact of ackA, pta, and ackA-pta mutations on growth, gene expression and protein acetylation in Escherichia coli K-12.** *Frontiers in Microbiology.* Published February 2020;11:233. DOI: [10.3389/fmicb.2020.00233](https://doi.org/10.3389/fmicb.2020.00233). This provides intervention evidence for the ATP-conserving importance of the acetate branch.

**Curation recommendation:** retain `traitmech:000027` as a reviewed metabolism class and implement an explicitly *E. coli*/enterobacterial core graph centered on PflB-mediated pyruvate cleavage, Pta–AckA ATP conservation, AdhE/LdhA redox balancing, the Ppc–Mdh–FumB–Frd succinate branch, acidification, and optional FHL-dependent H₂/CO₂ production. Regulatory and activation details should be added only when direct primary evidence is attached.

References

1. (fa¶rster2014metabolicengineeringof pages 1-2): Andreas H. FÃ¶rster and Johannes Gescher. Metabolic engineering of escherichia coli for production of mixed-acid fermentation end products. Frontiers in Bioengineering and Biotechnology, May 2014. URL: https://doi.org/10.3389/fbioe.2014.00016, doi:10.3389/fbioe.2014.00016. This article has 238 citations.

2. (taggar2024hydrogenproductionvia pages 5-7): Monica SACHDEVA TAGGAR, Amanpreet Kaur, Chahak Jain, Anu Kalia, and Sarbjit SINGH SOOCH. Hydrogen production via dark fermentation: a review of influential factors. Cellulose Chemistry and Technology, 58:1051-1063, Nov 2024. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90, doi:10.35812/cellulosechemtechnol.2024.58.90. This article has 12 citations and is from a peer-reviewed journal.

3. (metcalfe2020onlineanalysisand pages 9-10): George D. Metcalfe, Thomas W. Smith, and Michael Hippler. On-line analysis and in situ ph monitoring of mixed acid fermentation by escherichia coli using combined ftir and raman techniques. Analytical and Bioanalytical Chemistry, 412:7307-7319, Aug 2020. URL: https://doi.org/10.1007/s00216-020-02865-5, doi:10.1007/s00216-020-02865-5. This article has 37 citations and is from a peer-reviewed journal.

4. (fa¶rster2014metabolicengineeringof pages 5-7): Andreas H. FÃ¶rster and Johannes Gescher. Metabolic engineering of escherichia coli for production of mixed-acid fermentation end products. Frontiers in Bioengineering and Biotechnology, May 2014. URL: https://doi.org/10.3389/fbioe.2014.00016, doi:10.3389/fbioe.2014.00016. This article has 238 citations.

5. (metcalfe2020onlineanalysisand pages 10-11): George D. Metcalfe, Thomas W. Smith, and Michael Hippler. On-line analysis and in situ ph monitoring of mixed acid fermentation by escherichia coli using combined ftir and raman techniques. Analytical and Bioanalytical Chemistry, 412:7307-7319, Aug 2020. URL: https://doi.org/10.1007/s00216-020-02865-5, doi:10.1007/s00216-020-02865-5. This article has 37 citations and is from a peer-reviewed journal.