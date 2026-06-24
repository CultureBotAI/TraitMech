---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:41:54.918915'
end_time: '2026-06-18T05:59:46.100403'
duration_seconds: 1071.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: proteolysis
  trait_identifier: traitmech:000116
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: proteolysis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism secretes proteases
    to hydrolyze extracellular proteins and peptides into amino acids and short peptides
    for nutrition.
  parent_traits: traitmech:000110
  synonyms: proteolytic, protein degradation
  evidence_summary: 'DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial
    proteases, noting that secreted (extracellular) proteases play a major nutritional
    role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review
    of Bacillus proteases covers extracellular protease activities and their functions.)'
  causal_graph_summary: 'proteolysis_extracellular_protease: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 68
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteolysis
- **METPO identifier:** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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
- **Trait label:** proteolysis
- **METPO identifier:** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Proteolysis (traitmech:000116)

### Executive scope summary
**Proteolysis (METPO: traitmech:000116)**, as defined here, is a *nutritional* metabolism in which microorganisms secrete extracellular (or cell-envelope/cell-surface-associated) proteases/peptidases that hydrolyze environmental proteins into peptides and amino acids that can be transported into the cell and assimilated. This extracellular step is required because polymeric proteins are typically too large for direct uptake by prokaryotic transporters, imposing a mechanistic boundary between **extracellular depolymerization** and **cellular import + intracellular peptidolysis** (zhao2024decouplingbetweenthe pages 1-2, tinta2023jellyfishdetritussupports pages 15-17).

In curated causal-graph terms, the trait is best represented as a coordinated *system* comprising: (i) extracellular/cell-envelope proteases; (ii) peptide transporters (often Opp/Dpp and related systems in Gram-positives; diverse uptake systems in Gram-negatives); and (iii) intracellular peptidases completing peptide-to-amino-acid conversion for growth (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).

### 1) Trait scope and boundary cases

#### What the trait represents
Operationally, the trait can be observed as:
- **Capacity**: encoding and expressing secreted or surface-associated proteases/peptidases that initiate extracellular protein hydrolysis into transportable oligomers (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).
- **Physiological function**: enabling growth on proteinaceous substrates (e.g., protein-rich detritus or food proteins), with downstream uptake and catabolism (tinta2023jellyfishdetritussupports pages 15-17, rizwan2023bioactivepeptidesfrom pages 6-8).
- **Assay-observed property (example)**: clearing/halo zones on skim-milk plates, and measurable extracellular vs cell-surface-bound protease activity units (U/mL defined via tyrosine release from casein) (phupaboon2023molecularandbiotechnological pages 3-5).

#### Boundary cases / nearby traits (do not conflate)
- **Intracellular protein turnover/proteasome-like processes**: not the trait (no extracellular depolymerization step).
- **Cell-wall remodeling peptidases / peptidoglycan lyases**: can overlap mechanistically (secreted peptidases), but primary function may be structural remodeling or antagonism; treat as adjacent unless evidence ties to nutrition (zhao2024decouplingbetweenthe pages 7-9).
- **Virulence-associated secreted proteases (e.g., LasB)**: clearly extracellular proteolysis but often curated under virulence rather than nutrition; include only if your trait model allows “extracellular protein cleavage” independent of ecological intent, or mark as *context-specific* (ren2024quercetinapromising pages 1-2, ren2024quercetinapromising pages 15-17).
- **Extracellular proteolysis of quorum-sensing propeptides**: extracellular protease action on peptides is real but primarily signaling; include only as mechanistic analogs or separate trait branch (feliperuiz2024extracellularproteolysisof pages 1-2, feliperuiz2024extracellularproteolysisof pages 5-7).

### 2) Key concepts and definitions (current understanding)

#### Conceptual mechanism (nutrition-focused)
1. **Extracellular or cell-envelope protease action** initiates hydrolysis of intact extracellular proteins into peptides short enough for uptake (moyo2024urgingbioactivepeptide pages 8-10, rizwan2023bioactivepeptidesfrom pages 6-8).
2. **Transport limitation**: “proteins are too large for direct uptake by prokaryotic transporter systems,” necessitating extracellular cleavage (zhao2024decouplingbetweenthe pages 1-2). In a marine detritus model, “bacterial transporters can only import substrates <600 Da” (tinta2023jellyfishdetritussupports pages 15-17).
3. **Peptide uptake** commonly uses dedicated transporters such as Opp (ATP-driven), DtpT (PMF-driven), and Dpp (ABC-type) (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).
4. **Intracellular peptidases** (endo- and exopeptidases) convert imported peptides to free amino acids for growth (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).

#### Definitions useful for node/edge curation
- **Cell-envelope protease (CEP/CEPE)**: a cell-surface/cell-wall-associated proteinase that initiates protein degradation external to the cytoplasm, releasing oligopeptides (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).
- **Secretory peptidases**: extracellular enzymes (cell-associated or released) that cleave proteins/peptides in the environment; their expression can be strongly filtered by substrate availability and C:N stoichiometry (zhao2024decouplingbetweenthe pages 9-12, zhao2024decouplingbetweenthe pages 1-2).
- **Oligopeptide permease (Opp/OPP)**: an ATP-dependent uptake system for oligopeptides (rizwan2023bioactivepeptidesfrom pages 6-8). Note: in Bacillus quorum-sensing, mature signaling peptides are also reimported via OPP (feliperuiz2024extracellularproteolysisof pages 1-2), illustrating mechanistic reuse of peptide uptake.

### 3) Candidate causal-graph entities (nodes), grouped by type

#### A. Pathways / modules (conceptual)
- Extracellular protein depolymerization → peptide uptake → intracellular peptidolysis → amino acid assimilation (rizwan2023bioactivepeptidesfrom pages 6-8, zhao2024decouplingbetweenthe pages 1-2).
- Secretory enzyme export modules (Sec/Tat signal peptides; ecosystem-specific usage) (zhao2024decouplingbetweenthe pages 9-12).

#### B. Environmental / experimental factors
- Proteinaceous organic matter availability; substrate source/concentration; C:N stoichiometry (zhao2024decouplingbetweenthe pages 9-12, zhao2024decouplingbetweenthe pages 1-2).
- Substrate size constraint / transporter MW cutoff (<600 Da) (tinta2023jellyfishdetritussupports pages 15-17, zhao2024decouplingbetweenthe pages 1-2).
- Fermentation processing parameters affecting proteolysis assays (e.g., conditions affecting units/halo) (phupaboon2023molecularandbiotechnological pages 3-5).

#### C. Genes / proteins / enzyme classes
- Extracellular proteases / peptidases (GO:0008233 proteinase activity; label-only extracellular protease) (wasmund2024thepredictedsecreted pages 1-2, tinta2023jellyfishdetritussupports pages 15-17).
- LAB CEP variants (label-only): PrtP/PrtB/PrtH/PrtS/PrtR/PrtL; S. thermophilus prtS (rizwan2023bioactivepeptidesfrom pages 6-8, phupaboon2023molecularandbiotechnological pages 1-3).
- Intracellular peptidases: endopeptidases and exopeptidases (e.g., PepN aminopeptidase N) (moyo2024urgingbioactivepeptide pages 8-10, rizwan2023bioactivepeptidesfrom pages 6-8).

#### D. Transporters / complexes
- Opp (KEGG oppABCDF; GO:0015410 ATPase-coupled oligopeptide transporter activity) (rizwan2023bioactivepeptidesfrom pages 6-8).
- Dpp (KEGG dppABCDF; peptide ABC transporter) (rizwan2023bioactivepeptidesfrom pages 6-8).
- DtpT (label-only; proton-motive-force peptide transporter) (rizwan2023bioactivepeptidesfrom pages 6-8).
- ABC/TRAP transporters and periplasmic substrate binding proteins (label-only; important in activated sludge niches) (wasmund2024thepredictedsecreted pages 1-2).

#### E. Chemicals / nutrients / metabolites
- Proteins (CHEBI:36080), peptides/oligopeptides (CHEBI:16670 / CHEBI:25676), amino acids (CHEBI:33709) (rizwan2023bioactivepeptidesfrom pages 6-8, moyo2024urgingbioactivepeptide pages 8-10).

#### F. Ecosystems / real-world settings
- Wastewater treatment plants (activated sludge microbiomes; secreted peptidases widespread) (wasmund2024thepredictedsecreted pages 1-2, wasmund2024thepredictedsecreted pages 10-15).
- Marine detritus degradation (protein-rich jellyfish OM; extracellular proteases prominent) (tinta2023jellyfishdetritussupports pages 15-17, tinta2023jellyfishdetritussupports media 6e417b3b).
- Food fermentation (LAB proteolytic systems; peptide uptake; measurable activity) (rizwan2023bioactivepeptidesfrom pages 6-8, phupaboon2023molecularandbiotechnological pages 3-5).

### 4) Evidence-backed causal edges (curation candidates)
The following table is designed to be directly portable into a TraitMech causal-graph YAML curation workflow.

| Subject node (label + suggested CURIEs) | Predicate | Object node (label + CURIEs) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Extracellular/cell-envelope proteases [GO:0008233 proteinase activity; label-only extracellular protease] | enables | Extracellular protein degradation for nutrition [METPO:traitmech:000116] | “CEPs… initiate extracellular degradation of food proteins” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong, fermentation/LAB context but mechanism generalizable. |
| Cell-envelope proteinase/CEPE [label-only; prtS gene in some taxa] | hydrolyzes | Intact extracellular proteins [CHEBI:36080 protein] | “hydrolyse intact proteins into peptides short enough for uptake” (moyo2024urgingbioactivepeptide pages 8-10) | 10.1186/s43014-024-00265-1, 2024, https://doi.org/10.1186/s43014-024-00265-1 | Strong for CEP systems in fermentation microbes. |
| Extracellular proteolytic enzymes [label-only] | produces | Peptides [CHEBI:16670 peptide] | “protein to oligopeptides” / “producing peptides of roughly 4–30 amino acids” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong. Product size range from LAB review. |
| Oligopeptide permease Opp [KEGG:oppABCDF; GO:0015410 ATPase-coupled oligopeptide transmembrane transporter activity] | imports | Oligopeptides [CHEBI:25676 oligopeptide] | “taken up by dedicated transporters: oligopeptide permease (Opp, an ATP-driven system)” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong. Canonical LAB evidence. |
| DtpT transporter [label-only; di/tripeptide transporter] | imports | Small peptides [CHEBI:16670 peptide] | “an ion-linked transporter DtpT (proton-motive-force driven)” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong in LAB systems. |
| Dpp ABC transporter [KEGG:dppABCDF; label-only Dpp] | imports | Peptides [CHEBI:16670 peptide] | “and an ABC-type transporter (Dpp)” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong in LAB systems. |
| Peptide transport systems (Opp/DtpT/Dpp) [label-only aggregate] | mediate uptake of | Peptides short enough for uptake [CHEBI:16670 peptide] | “Peptide transport systems named include oligopeptide permease (Opp), the ion-linked transporter DtpT and ABC transporter Dpp” (moyo2024urgingbioactivepeptide pages 8-10) | 10.1186/s43014-024-00265-1, 2024, https://doi.org/10.1186/s43014-024-00265-1 | Strong corroboration from 2024 review. |
| Intracellular peptidases [GO:0008238 exopeptidase activity; GO:0004175 endopeptidase activity] | hydrolyzes | Imported peptides [CHEBI:16670 peptide] | “Inside the cell, multiple peptidases… further hydrolyze peptides” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong. |
| Intracellular peptidases [GO:0008238; GO:0004175] | produces | Free amino acids [CHEBI:33709 amino acid] | “further hydrolyze peptides to free amino acids used for growth” (rizwan2023bioactivepeptidesfrom pages 6-8) | 10.1186/s43014-023-00165-w, 2023, https://doi.org/10.1186/s43014-023-00165-w | Strong. |
| Exopeptidases such as PepN [label-only; aminopeptidase N family] | releases | Di-/tripeptides and amino acids [CHEBI:46761 dipeptide; CHEBI:47923 tripeptide; CHEBI:33709 amino acid] | “exopeptidases… trim terminal residues and release di-/tripeptides and amino acids” (moyo2024urgingbioactivepeptide pages 8-10) | 10.1186/s43014-024-00265-1, 2024, https://doi.org/10.1186/s43014-024-00265-1 | Strong. |
| Large extracellular proteins [CHEBI:36080 protein] | cannot be directly imported by | Prokaryotic transport systems [label-only] | “proteins are too large for direct uptake by prokaryotic transporter systems” (zhao2024decouplingbetweenthe pages 1-2) | 10.1128/spectrum.03036-23, 2024, https://doi.org/10.1128/spectrum.03036-23 | Strong ecological/mechanistic boundary condition. |
| Environmental size constraint on substrates [label-only] | necessitates | Extracellular hydrolysis [GO:0044248 cellular catabolic process; label-only extracellular hydrolysis] | “polysaccharides and proteins are too large… explaining the need for extracellular cleavage” (zhao2024decouplingbetweenthe pages 1-2) | 10.1128/spectrum.03036-23, 2024, https://doi.org/10.1128/spectrum.03036-23 | Strong. |
| Bacterial transporters [label-only] | can only import | substrates “<600 Da” [label-only small molecules] | “Because bacterial transporters can only import substrates <600 Da” (tinta2023jellyfishdetritussupports pages 15-17) | 10.1186/s40168-023-01598-8, 2023, https://doi.org/10.1186/s40168-023-01598-8 | Strong, marine context. Useful assay/ecology constraint. |
| Secreted hydrolases/cell-surface enzymes [label-only] | generate | partially digested products for assimilation [label-only] | “perform the initial breakdown, producing partially digested products that are transported into the periplasm and cytoplasm” (wasmund2024thepredictedsecreted pages 1-2) | 10.1128/msystems.00301-24, 2024, https://doi.org/10.1128/msystems.00301-24 | Strong, WWTP ecosystem. |
| Periplasmic substrate-binding proteins + ABC/TRAP transporters [label-only; GO:0043190 ATP-binding cassette (ABC) transporter complex] | import | small degradation products [label-only] | “encode few or no secreted hydrolases, but many periplasmic substrate-binding proteins and ABC- and TRAP-transporters, suggesting they are mostly sustained by small molecules” (wasmund2024thepredictedsecreted pages 1-2) | 10.1128/msystems.00301-24, 2024, https://doi.org/10.1128/msystems.00301-24 | Moderate: uptake is clear; exact peptide specificity not always explicit. |
| TonB-dependent receptors [GO:0015344 siderophore transmembrane transporter activity or label-only TonB receptor] | associate with import of | larger organics [label-only] | “TonB receptors associate with import of larger organics” (wasmund2024thepredictedsecreted pages 10-15) | 10.1128/msystems.00301-24, 2024, https://doi.org/10.1128/msystems.00301-24 | Moderate; not peptide-specific. Use as ecosystem accessory node only. |
| Substrate source/concentration/C:N stoichiometry [label-only environmental factor] | filters/controls expression of | extracellular enzymes [label-only secretory peptidases] | “the substrate's source, concentration and stoichiometry impose strong filtering on the expression of extracellular enzymes” (zhao2024decouplingbetweenthe pages 9-12) | 10.1128/spectrum.03036-23, 2024, https://doi.org/10.1128/spectrum.03036-23 | Strong recent regulation evidence. |
| Organic matter characteristics and availability [label-only environmental factor] | shape | expression and export of secretory enzymes [label-only] | “organic matter characteristics and availability shape expression and export of secretory enzymes” (zhao2024decouplingbetweenthe pages 9-12) | 10.1128/spectrum.03036-23, 2024, https://doi.org/10.1128/spectrum.03036-23 | Strong. |
| Pseudoalteromonadaceae [NCBITaxon:186803? label-only family] | secretes | extracellular proteases associated with proteolysis [label-only] | “Pseudoalteromonadaceae synthesized and excreted enzymes associated with proteolysis” (tinta2023jellyfishdetritussupports pages 15-17) | 10.1186/s40168-023-01598-8, 2023, https://doi.org/10.1186/s40168-023-01598-8 | Strong, marine jelly-OM degrader context. Taxon CURIE approximate; keep label-only if needed. |
| Vibrionaceae [NCBITaxon:641? label-only family] | imports via transporters | peptides, amino acids and carbohydrates [label-only] | “Vibrionaceae synthesized transporter proteins for peptides, amino acids and carbohydrates” (tinta2023jellyfishdetritussupports pages 15-17) | 10.1186/s40168-023-01598-8, 2023, https://doi.org/10.1186/s40168-023-01598-8 | Strong. Shows cross-feeding/cheater uptake strategy. |
| Protein-rich jelly-OM [ENVO:marine detritus label-only] | enriches for | extracellular collagenolytic bacterial proteases [label-only; EC:3.4.24.- metalloprotease families M9A/M9B] | “decaying jellyfish blooms are associated with the enrichment in extracellular collagenolytic bacterial proteases” (tinta2023jellyfishdetritussupports pages 15-17) | 10.1186/s40168-023-01598-8, 2023, https://doi.org/10.1186/s40168-023-01598-8 | Strong ecosystem-specific application. |
| Activated-sludge microbiota [ENVO:wastewater sludge label-only] | encode | diverse extracellular peptidases [label-only] | “diverse taxa encode extracellular peptidases, indicating that proteins are widely used nutrients” (wasmund2024thepredictedsecreted pages 1-2) | 10.1128/msystems.00301-24, 2024, https://doi.org/10.1128/msystems.00301-24 | Strong WWTP ecosystem implementation. |
| Phr propeptides in Rap-Phr QS [label-only; GO:0009372 quorum sensing?] | are reimported via | Oligopeptide permease OPP [KEGG:oppABCDF] | “mature pheromones are reimported via the oligopeptide permease (OPP)” (feliperuiz2024extracellularproteolysisof pages 1-2) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Strong, but signaling not nutritional; keep as related mechanism/boundary. |
| Extracellular proteases [label-only] | mature | Phr propeptides into active pheromones [label-only mature pheromone] | “maturation is initiated by the signal peptidase… and is continued by extracellular proteases that produce the active pheromone” (feliperuiz2024extracellularproteolysisof pages 1-2) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Strong, but signaling context rather than nutritional proteolysis. |
| WprA protease [label-only; Bacillus extracellular protease] | required for maturation of | Phr3T/Phr105 immature peptides [label-only] | “only the ΔwprA mutant showed null maturation capability” / “WprA as the protease responsible” (feliperuiz2024extracellularproteolysisof pages 5-7) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Strong for Bacillus QS peptide processing; not nutritional proteolysis. |
| Bpr protease [label-only] | contributes to maturation of | Phr3T/Phr105 immature peptides [label-only] | “ΔwprA and Δbpr supernatants showed impaired generation of the mature peptide” (feliperuiz2024extracellularproteolysisof pages 5-7) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Strong, signaling context. |
| NprE protease [label-only] | contributes to maturation of | Phr105 immature peptide Imat0105 [label-only] | “Imat0105 maturation was reduced/null in ΔnprE, Δbpr, and ΔwprA” (feliperuiz2024extracellularproteolysisof pages 11-13) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Strong, signaling context. |
| AprE/Epr/Vpr extracellular proteases [label-only] | process | canonical Bacillus QS peptides such as CSF/PhrA/PhrC [label-only] | “Specific references identify extracellular proteases involved in producing CSF: subtilisin, Epr and Vpr” (feliperuiz2024extracellularproteolysisof pages 22-23) | 10.1371/journal.pbio.3002744, 2024, https://doi.org/10.1371/journal.pbio.3002744 | Moderate because quoted as cited prior work within 2024 paper. |
| Las/Rhl/Pqs quorum sensing systems [label-only] | co-regulate expression of | lasB / LasB elastase [gene/protein label-only; UniProt label-only] | “lasB is co-regulated by the Las, Rhl and Pqs QS subsystems” (ren2024quercetinapromising pages 15-17) | 10.1007/s00253-023-12890-w, 2024, https://doi.org/10.1007/s00253-023-12890-w | Strong, pathogen/virulence context not nutritional. |
| Quercetin (QS inhibitor) [CHEBI:16243 quercetin] | decreases | LasB production/activity [label-only] | “At 256 μg/ml quercetin, LasB activity dropped by >90%” (ren2024quercetinapromising pages 15-17) | 10.1007/s00253-023-12890-w, 2024, https://doi.org/10.1007/s00253-023-12890-w | Strong, antivirulence application; outside nutritional scope. |
| QS-deficient ΔlasI or ΔlasIΔrhlI mutants [label-only experimental factor] | reduce | lasB expression and LasB activity [label-only] | “PAO1 ΔlasI and ΔlasIΔrhlI mutants produced significantly deficient lasB expression and LasB activity” (ren2024quercetinapromising pages 1-2) | 10.1007/s00253-023-12890-w, 2024, https://doi.org/10.1007/s00253-023-12890-w | Strong assay-specific genetic evidence in pathogen context. |


*Table: This table compiles candidate causal edges for extracellular microbial proteolysis, spanning core nutritional mechanisms, transport and regulation, plus related but cautionary quorum-sensing proteolysis examples. It is useful as a curation-ready evidence map for selecting which edges belong in a TraitMech graph for proteolysis.*

### 5) Recent developments and latest research (prioritize 2023–2024)

#### Multi-omics clarifies regulation is frequently decoupled from genomic potential (2024)
Across ocean, soil, and gut microbiomes, metagenomic potential for secretory peptidases does not necessarily predict transcript/protein expression; instead, “the substrate's source, concentration and stoichiometry impose strong filtering on the expression of extracellular enzymes” (zhao2024decouplingbetweenthe pages 9-12). This is a key curation insight: **presence of extracellular peptidase genes is insufficient** to assert the expressed trait in a given environment without contextual evidence (zhao2024decouplingbetweenthe pages 1-2, zhao2024decouplingbetweenthe pages 9-12).

#### Ecosystem-resolved secreted proteome catalogs protein use as a widespread niche axis (2024)
In activated sludge MAGs from WWTPs, diverse taxa encode extracellular peptidases, supporting that proteins are widely used nutrients in this real-world engineered ecosystem (wasmund2024thepredictedsecreted pages 1-2). The same work links different taxa to distinct strategies: some taxa encode many secreted hydrolases while others rely on transporters for small molecules (wasmund2024thepredictedsecreted pages 1-2).

#### Marine detritus studies quantify extracellular protease prominence (2023)
In a protein-rich jellyfish detritus system, extracellular proteases were abundant in exoproteomes; the study reports that proteases constituted ~10% of exoproteome proteins (tinta2023jellyfishdetritussupports pages 15-17) and provides figure evidence for protease pools and transporter profiles (tinta2023jellyfishdetritussupports media 6e417b3b, tinta2023jellyfishdetritussupports media b30265d2).

#### New mechanistic layer: extracellular proteolysis modulates quorum sensing peptides (2024)
Although not nutritional, Bacillus RRNPPA quorum sensing systems demonstrate that secreted peptides are matured by specific extracellular proteases and reimported by OPP, illustrating how extracellular proteolysis and peptide uptake can be tightly coupled in bacterial physiology (feliperuiz2024extracellularproteolysisof pages 1-2, feliperuiz2024extracellularproteolysisof pages 5-7). This may be valuable for graph reuse if TraitMech includes signaling-proteolysis intersections.

### 6) Current applications and real-world implementations

#### Food and fermentation biotechnology
LAB proteolytic systems are used (and engineered/selected) to hydrolyze food proteins into peptides/amino acids during fermentation. The canonical LAB model explicitly couples CEP-mediated protein breakdown to peptide uptake (Opp/DtpT/Dpp) and intracellular peptidases producing amino acids for growth (rizwan2023bioactivepeptidesfrom pages 6-8). This is directly relevant to fermented legumes and other substrates where secreted/CEP proteases determine peptide profiles (moyo2024urgingbioactivepeptide pages 8-10).

#### Wastewater treatment (activated sludge)
WWTP microbiomes are a large-scale implementation where secreted extracellular enzymes initiate degradation of complex macromolecules; extracellular peptidases are widespread in MAGs and are presented as part of niche partitioning among taxa (wasmund2024thepredictedsecreted pages 1-2, wasmund2024thepredictedsecreted pages 10-15).

#### Marine carbon and nitrogen cycling (field-relevant)
Protein-rich detritus (e.g., jellyfish blooms) triggers enrichment of extracellular proteases and specialized collagenolytic proteases, with downstream uptake by other community members (“cheater-type lifestyle” via transporters for peptides/amino acids) (tinta2023jellyfishdetritussupports pages 15-17). The corresponding figures provide visual support for the extracellular enzyme and transporter partitioning across taxa (tinta2023jellyfishdetritussupports media 6e417b3b, tinta2023jellyfishdetritussupports media b30265d2).

### 7) Expert opinions / authoritative analysis (source-grounded)

- The 2024 cross-microbiome multi-omics synthesis emphasizes that environmental context can “overwrite the genetic potentials” for extracellular enzyme secretion, and therefore trait assertions should incorporate substrate context, not just gene presence (zhao2024decouplingbetweenthe pages 9-12).
- The activated-sludge secretome analysis argues secreted proteins are “critical because many are the first to interact with or degrade external (macro)molecules,” and highlights widespread extracellular peptidases as an indicator that proteins are broadly used nutrients in WWTP ecosystems (wasmund2024thepredictedsecreted pages 1-2).

### 8) Relevant statistics / data points from recent studies
- **Transport constraint**: bacterial transporters “can only import substrates <600 Da,” supporting the necessity of extracellular hydrolysis before assimilation in marine protein degradation contexts (tinta2023jellyfishdetritussupports pages 15-17).
- **Exoproteome allocation**: in the jellyfish detritus study, proteases comprised ~10% of exoproteome proteins (tinta2023jellyfishdetritussupports pages 15-17).
- **Regulatory dependence**: substrate “source, concentration and stoichiometry impose strong filtering” on extracellular enzyme expression across ecosystems (zhao2024decouplingbetweenthe pages 9-12).
- **Applied antivirulence datapoint (contextual/boundary)**: quercetin reduced LasB activity by >90% at 256 μg/mL in vitro; QS mutants also show deficient lasB/LasB, demonstrating strong QS control of a secreted protease (ren2024quercetinapromising pages 15-17, ren2024quercetinapromising pages 1-2). This supports QS–protease edges but should be curated as virulence-associated unless TraitMech explicitly includes such contexts.

### 9) Ontology grounding notes (CURIE suggestions)
- **Trait**: METPO:traitmech:000116 (provided).
- **Molecular function**: GO:0008233 (peptidase activity/proteinase activity; may need specific term selection), GO:0008238 (exopeptidase activity), GO:0004175 (endopeptidase activity).
- **Transport**: GO:0015410 (ATPase-coupled oligopeptide transmembrane transporter activity; for Opp-like systems).
- **Chemicals**: CHEBI:36080 protein; CHEBI:16670 peptide; CHEBI:25676 oligopeptide; CHEBI:33709 amino acid.
- **Pathway databases**: KEGG modules/genes for oppABCDF and dppABCDF are appropriate where organisms are bacteria with annotated systems.

### 10) Warnings: claims not yet ready for TraitMech curation
- **Do not generalize Opp/Dpp/DtpT** beyond taxa/ecological contexts without support; Gram-negative environmental systems may use different peptide uptake architectures than LAB examples (wasmund2024thepredictedsecreted pages 1-2, rizwan2023bioactivepeptidesfrom pages 6-8).
- **Quorum-sensing peptide maturation** (Bacillus Rap-Phr) is extracellular proteolysis but not nutritional; treat as separate branch or annotate as “signaling-associated extracellular proteolysis” (feliperuiz2024extracellularproteolysisof pages 1-2, feliperuiz2024extracellularproteolysisof pages 5-7).
- **Virulence proteases (LasB)**: include only if the trait definition allows extracellular proteolysis regardless of function; otherwise keep as boundary evidence or mark uncertain for nutrition (ren2024quercetinapromising pages 15-17, ren2024quercetinapromising pages 1-2).

---

## DOI-first bibliography (with publication dates/URLs)

1. Wasmund K, et al. *The predicted secreted proteome of activated sludge microorganisms indicates distinct nutrient niches.* **mSystems** (Oct 2024). DOI: **10.1128/msystems.00301-24**. URL: https://doi.org/10.1128/msystems.00301-24 (wasmund2024thepredictedsecreted pages 1-2, wasmund2024thepredictedsecreted pages 10-15)
2. Zhao Z, Baltar F, Herndl GJ. *Decoupling between the genetic potential and the metabolic regulation and expression in microbial organic matter cleavage across microbiomes.* **Microbiology Spectrum** (May 2024). DOI: **10.1128/spectrum.03036-23**. URL: https://doi.org/10.1128/spectrum.03036-23 (zhao2024decouplingbetweenthe pages 9-12, zhao2024decouplingbetweenthe pages 1-2)
3. Tinta T, et al. *Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria.* **Microbiome** (Jul 2023). DOI: **10.1186/s40168-023-01598-8**. URL: https://doi.org/10.1186/s40168-023-01598-8 (tinta2023jellyfishdetritussupports pages 15-17, tinta2023jellyfishdetritussupports media 6e417b3b, tinta2023jellyfishdetritussupports media b30265d2)
4. Rizwan D, et al. *Bioactive peptides from fermented foods and their relevance in COVID-19 mitigation.* **Food Production, Processing and Nutrition** (Sep 2023). DOI: **10.1186/s43014-023-00165-w**. URL: https://doi.org/10.1186/s43014-023-00165-w (rizwan2023bioactivepeptidesfrom pages 6-8)
5. Moyo SM, et al. *Urging bioactive peptide exploration in African fermented legumes: insights from microbial proteolysis to gastrointestinal stability.* **Food Production, Processing and Nutrition** (Dec 2024). DOI: **10.1186/s43014-024-00265-1**. URL: https://doi.org/10.1186/s43014-024-00265-1 (moyo2024urgingbioactivepeptide pages 8-10)
6. Phupaboon S, et al. *Molecular and biotechnological characteristics of proteolytic activity from Streptococcus thermophilus…* **AIMS Microbiology** (Aug 2023). DOI: **10.3934/microbiol.2023031**. URL: https://doi.org/10.3934/microbiol.2023031 (phupaboon2023molecularandbiotechnological pages 1-3, phupaboon2023molecularandbiotechnological pages 3-5)
7. Felipe-Ruiz A, et al. *Extracellular proteolysis of tandemly duplicated pheromone propeptides affords additional complexity to bacterial quorum sensing.* **PLOS Biology** (Aug 2024). DOI: **10.1371/journal.pbio.3002744**. URL: https://doi.org/10.1371/journal.pbio.3002744 (feliperuiz2024extracellularproteolysisof pages 1-2, feliperuiz2024extracellularproteolysisof pages 5-7)
8. Ren Y, et al. *Quercetin: a promising virulence inhibitor of Pseudomonas aeruginosa LasB in vitro.* **Applied Microbiology and Biotechnology** (Jan 2024). DOI: **10.1007/s00253-023-12890-w**. URL: https://doi.org/10.1007/s00253-023-12890-w (ren2024quercetinapromising pages 15-17, ren2024quercetinapromising pages 1-2)
9. D’Aquila P, et al. *Quorum Quenching Approaches against Bacterial-Biofilm-Induced Antibiotic Resistance.* **Antibiotics** (Jul 2024). DOI: **10.3390/antibiotics13070619**. URL: https://doi.org/10.3390/antibiotics13070619 (d’aquila2024quorumquenchingapproaches pages 9-10)



References

1. (zhao2024decouplingbetweenthe pages 1-2): Zihao Zhao, Federico Baltar, and Gerhard J. Herndl. Decoupling between the genetic potential and the metabolic regulation and expression in microbial organic matter cleavage across microbiomes. May 2024. URL: https://doi.org/10.1128/spectrum.03036-23, doi:10.1128/spectrum.03036-23. This article has 20 citations and is from a domain leading peer-reviewed journal.

2. (tinta2023jellyfishdetritussupports pages 15-17): Tinkara Tinta, Zihao Zhao, Barbara Bayer, and Gerhard J. Herndl. Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01598-8, doi:10.1186/s40168-023-01598-8. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (rizwan2023bioactivepeptidesfrom pages 6-8): Danish Rizwan, F. A. Masoodi, Shoib Mohmad Wani, and Sajad Ahmad Mir. Bioactive peptides from fermented foods and their relevance in covid-19 mitigation. Food Production, Processing and Nutrition, Sep 2023. URL: https://doi.org/10.1186/s43014-023-00165-w, doi:10.1186/s43014-023-00165-w. This article has 44 citations.

4. (moyo2024urgingbioactivepeptide pages 8-10): Siphosanele M. Moyo, Oluyimika Y. Famuyide, and Eugénie Kayitesi. Urging bioactive peptide exploration in african fermented legumes: insights from microbial proteolysis to gastrointestinal stability. Food Production, Processing and Nutrition, Dec 2024. URL: https://doi.org/10.1186/s43014-024-00265-1, doi:10.1186/s43014-024-00265-1. This article has 10 citations.

5. (phupaboon2023molecularandbiotechnological pages 3-5): Srisan Phupaboon, F. Hashim, P. Phumkhachorn, and Pongsak Rattanachaikunsopon. Molecular and biotechnological characteristics of proteolytic activity from streptococcus thermophilus as a proteolytic lactic acid bacteria to enhance protein-derived bioactive peptides. AIMS Microbiology, 9:591-611, Aug 2023. URL: https://doi.org/10.3934/microbiol.2023031, doi:10.3934/microbiol.2023031. This article has 19 citations and is from a peer-reviewed journal.

6. (zhao2024decouplingbetweenthe pages 7-9): Zihao Zhao, Federico Baltar, and Gerhard J. Herndl. Decoupling between the genetic potential and the metabolic regulation and expression in microbial organic matter cleavage across microbiomes. May 2024. URL: https://doi.org/10.1128/spectrum.03036-23, doi:10.1128/spectrum.03036-23. This article has 20 citations and is from a domain leading peer-reviewed journal.

7. (ren2024quercetinapromising pages 1-2): Yanying Ren, Rui Zhu, Xiaojuan You, Dengzhou Li, Mengyu Guo, Bing Fei, Ying Liu, Ximing Yang, Xinwei Liu, and Yongwei Li. Quercetin: a promising virulence inhibitor of pseudomonas aeruginosa lasb in vitro. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12890-w, doi:10.1007/s00253-023-12890-w. This article has 51 citations and is from a domain leading peer-reviewed journal.

8. (ren2024quercetinapromising pages 15-17): Yanying Ren, Rui Zhu, Xiaojuan You, Dengzhou Li, Mengyu Guo, Bing Fei, Ying Liu, Ximing Yang, Xinwei Liu, and Yongwei Li. Quercetin: a promising virulence inhibitor of pseudomonas aeruginosa lasb in vitro. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12890-w, doi:10.1007/s00253-023-12890-w. This article has 51 citations and is from a domain leading peer-reviewed journal.

9. (feliperuiz2024extracellularproteolysisof pages 1-2): Alonso Felipe-Ruiz, Sara Zamora-Caballero, Shira Omer Bendori, José R. Penadés, Avigdor Eldar, and Alberto Marina. Extracellular proteolysis of tandemly duplicated pheromone propeptides affords additional complexity to bacterial quorum sensing. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002744, doi:10.1371/journal.pbio.3002744. This article has 2 citations and is from a highest quality peer-reviewed journal.

10. (feliperuiz2024extracellularproteolysisof pages 5-7): Alonso Felipe-Ruiz, Sara Zamora-Caballero, Shira Omer Bendori, José R. Penadés, Avigdor Eldar, and Alberto Marina. Extracellular proteolysis of tandemly duplicated pheromone propeptides affords additional complexity to bacterial quorum sensing. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002744, doi:10.1371/journal.pbio.3002744. This article has 2 citations and is from a highest quality peer-reviewed journal.

11. (zhao2024decouplingbetweenthe pages 9-12): Zihao Zhao, Federico Baltar, and Gerhard J. Herndl. Decoupling between the genetic potential and the metabolic regulation and expression in microbial organic matter cleavage across microbiomes. May 2024. URL: https://doi.org/10.1128/spectrum.03036-23, doi:10.1128/spectrum.03036-23. This article has 20 citations and is from a domain leading peer-reviewed journal.

12. (wasmund2024thepredictedsecreted pages 1-2): Kenneth Wasmund, Caitlin Singleton, Morten Kam Dahl Dueholm, Michael Wagner, and Per Halkjær Nielsen. The predicted secreted proteome of activated sludge microorganisms indicates distinct nutrient niches. mSystems, Oct 2024. URL: https://doi.org/10.1128/msystems.00301-24, doi:10.1128/msystems.00301-24. This article has 15 citations and is from a peer-reviewed journal.

13. (phupaboon2023molecularandbiotechnological pages 1-3): Srisan Phupaboon, F. Hashim, P. Phumkhachorn, and Pongsak Rattanachaikunsopon. Molecular and biotechnological characteristics of proteolytic activity from streptococcus thermophilus as a proteolytic lactic acid bacteria to enhance protein-derived bioactive peptides. AIMS Microbiology, 9:591-611, Aug 2023. URL: https://doi.org/10.3934/microbiol.2023031, doi:10.3934/microbiol.2023031. This article has 19 citations and is from a peer-reviewed journal.

14. (wasmund2024thepredictedsecreted pages 10-15): Kenneth Wasmund, Caitlin Singleton, Morten Kam Dahl Dueholm, Michael Wagner, and Per Halkjær Nielsen. The predicted secreted proteome of activated sludge microorganisms indicates distinct nutrient niches. mSystems, Oct 2024. URL: https://doi.org/10.1128/msystems.00301-24, doi:10.1128/msystems.00301-24. This article has 15 citations and is from a peer-reviewed journal.

15. (tinta2023jellyfishdetritussupports media 6e417b3b): Tinkara Tinta, Zihao Zhao, Barbara Bayer, and Gerhard J. Herndl. Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01598-8, doi:10.1186/s40168-023-01598-8. This article has 25 citations and is from a highest quality peer-reviewed journal.

16. (feliperuiz2024extracellularproteolysisof pages 11-13): Alonso Felipe-Ruiz, Sara Zamora-Caballero, Shira Omer Bendori, José R. Penadés, Avigdor Eldar, and Alberto Marina. Extracellular proteolysis of tandemly duplicated pheromone propeptides affords additional complexity to bacterial quorum sensing. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002744, doi:10.1371/journal.pbio.3002744. This article has 2 citations and is from a highest quality peer-reviewed journal.

17. (feliperuiz2024extracellularproteolysisof pages 22-23): Alonso Felipe-Ruiz, Sara Zamora-Caballero, Shira Omer Bendori, José R. Penadés, Avigdor Eldar, and Alberto Marina. Extracellular proteolysis of tandemly duplicated pheromone propeptides affords additional complexity to bacterial quorum sensing. Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002744, doi:10.1371/journal.pbio.3002744. This article has 2 citations and is from a highest quality peer-reviewed journal.

18. (tinta2023jellyfishdetritussupports media b30265d2): Tinkara Tinta, Zihao Zhao, Barbara Bayer, and Gerhard J. Herndl. Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01598-8, doi:10.1186/s40168-023-01598-8. This article has 25 citations and is from a highest quality peer-reviewed journal.

19. (d’aquila2024quorumquenchingapproaches pages 9-10): Patrizia D’Aquila, Elisabetta De Rose, Giada Sena, Angelo Scorza, Bonaventura Cretella, Giuseppe Passarino, and Dina Bellizzi. Quorum quenching approaches against bacterial-biofilm-induced antibiotic resistance. Antibiotics, 13:619, Jul 2024. URL: https://doi.org/10.3390/antibiotics13070619, doi:10.3390/antibiotics13070619. This article has 39 citations.