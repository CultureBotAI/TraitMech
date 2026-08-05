---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:42:15.337113'
end_time: '2026-08-04T11:57:02.115951'
duration_seconds: 886.78
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: persister cell formation
  trait_identifier: traitmech:000082
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: persister_cell_formation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: Formation of dormant phenotypic variants (persister cells) that are
    transiently tolerant to antibiotics and other lethal stresses without carrying
    genetic resistance, arising stochastically in a population.
  parent_traits: traitmech:000080
  synonyms: persistence
  evidence_summary: 'DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister
    cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis
    links persister-cell dormancy to the recalcitrance of chronic infections.)'
  causal_graph_summary: 'persister_dormancy_tolerance: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** persister cell formation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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
- **Trait label:** persister cell formation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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


# Curation report: persister cell formation

## Trait record and recommended scope

- **Trait label:** persister cell formation
- **Trait identifier:** `traitmech:000082`
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000080`
- **Recommended operational definition:** formation or enrichment of a reversible, non-heritable physiological subpopulation that survives an otherwise lethal antimicrobial or stress exposure, retains approximately the parental MIC, and can resume growth and regenerate a predominantly susceptible population after stress removal.

The strongest operational evidence combines: **(i)** survival at a lethal exposure, **(ii)** biphasic or otherwise heterogeneous time-kill kinetics, **(iii)** unchanged susceptibility after recovery, and **(iv)** demonstrable regrowth. Persistence is usually a population-level observation about a rare subpopulation, not a constitutive property of every cell. No unique molecular marker currently identifies all persisters, so a single gene-expression signature, low ATP measurement, or colony count should not alone establish the trait. (yuan2024molecularmechanismand pages 2-3, yuan2024molecularmechanismand pages 7-9, pont2024proteomiccharacterizationof pages 1-2)

### Boundary cases

| Nearby phenomenon | Distinction from `traitmech:000082` |
|---|---|
| Genetic antibiotic resistance | Resistant cells have a heritable increase in MIC or ability to grow under treatment. Persisters usually retain parental susceptibility after recovery. Persistence mutations such as `hipA7` can alter the *frequency* of entering the phenotype without making an individual persister genetically resistant. (niu2024bacterialpersistersmolecular pages 3-4, blattman2024identificationandgenetic pages 1-2) |
| Population-wide tolerance | Tolerance prolongs killing time for most or all of the population without necessarily increasing MIC; persistence denotes a minority with a markedly different killing rate. In practice these can form a continuum, so survival-distribution evidence is preferable to terminology alone. (niu2024bacterialpersistersmolecular pages 3-4, prasetyoputri2019theeagleeffect pages 8-9) |
| Heteroresistance | Heteroresistance comprises subpopulations with different, often unstable but growth-permitting MICs. It should not be curated as persistence unless recovered survivors retain parental MIC and satisfy reversible survival/regrowth criteria. |
| VBNC state | VBNC cells remain viable but do not form colonies on routine medium after removal of the immediate stress; persisters are operationally culturable after recovery. Both can have low ATP and may overlap biologically, making single-cell recovery assays important. (li2024intracellularatpconcentration pages 1-2) |
| Small-colony variants | SCVs can be transient or genetically stable and often have respiratory defects and characteristic small colonies. They may overlap with persisters but are not synonymous; stable SCVs with altered susceptibility belong in a separate phenotype. (goormaghtigh2024understandingstaphylococcusaureus pages 8-9) |
| Dormancy | Dormancy, slow growth, and low metabolism are frequent mechanisms or correlates, not mandatory definitions. Recent single-cell evidence shows distinct persister states and warns against equating every non-growing cell with a persister. (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4) |
| Biofilm tolerance | Matrix restriction, nutrient gradients, altered targets, and community physiology can protect the whole biofilm. Curate biofilm → persister enrichment only when the persister subpopulation itself is measured; do not collapse all biofilm recalcitrance into this trait. (yuan2024molecularmechanismand pages 7-9, vergoz2025antibioticpersistercells pages 3-3) |

## Current mechanistic interpretation

Persister formation is best represented as a **many-to-one causal graph**, not a universal linear pathway. Starvation, growth transition, antibiotic damage, host stress, signaling, and stochastic metabolic fluctuations can initiate different routes. These routes often converge on reduced translation, altered central metabolism and ATP availability, prolonged lag or dormancy, reduced antibiotic-target activity, and reversible survival. The relative importance of each route depends on species, strain, growth phase, antibiotic, concentration, and exposure duration. (niu2024bacterialpersistersmolecular pages 3-4, blattman2024identificationandgenetic pages 3-4)

A major 2024 advance was the single-cell RNA atlas and genome-scale CRISPRi study of *Escherichia coli*. Persisters generated by several genetic and physiological models converged on a state distinct from standard stationary or lag phases and dominated by **translational deficiency**. In wild-type cultures, 6-day starvation increased antibiotic persistence to nearly 1%; 7.4% of those cells occupied the inferred persister transcriptomic cluster. (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4)

That study also identified model-dependent causal drivers. Loss of `lon` strongly reversed `metG*` hyper-persistence; `lon` deletion reduced wild-type survival 5.2-fold, while combined `lon`/`sulA` deletion in the `metG*` background reduced lag-phase antibiotic survival by more than 100,000-fold. `yqgE` promoted post-starvation dormancy, and its expression was sufficient to increase lag and persistence in wild type. These are unusually strong candidates because they are supported by perturbation rather than expression correlation alone. (blattman2024identificationandgenetic pages 5-6, blattman2024identificationandgenetic pages 7-8, blattman2024identificationandgenetic pages 6-6)

A second 2024 primary study found a species-specific regulatory intervention in *Enterococcus faecalis* OG1RF. Under 8 h of 20 mg/mL levofloxacin, the untreated persistence rate was 0.109%; 10–12 ng/mL cCF10 lowered it to approximately 0.047–0.050%. The proposed chain is cCF10 uptake through Opp/Opp2, reduced (p)ppGpp accumulation, maintenance of ATP-generating and DNA-replication activity, and increased levofloxacin susceptibility. Natural extracellular cCF10 concentrations reported in the study were only 0.04–0.08 ng/mL, so this is an experimental intervention rather than an established natural regulator at the tested dose. (zhu2024pheromoneccf10inhibits pages 7-11, zhu2024pheromoneccf10inhibits pages 11-12, zhu2024pheromoneccf10inhibits pages 1-2)

Low ATP remains an important but context-sensitive node. Single-cell QUEEN-7μ measurements showed lower ATP in both *E. coli* persisters and VBNC cells than in sensitive or culturable cells, with overlap between sensitive cells and persisters. The study established a 12.5 µM threshold for separating VBNC from culturable cells, not a universal persister threshold; consequently, “low ATP causes persister formation” is weaker than “low ATP is associated with dormant cell fate.” (li2024intracellularatpconcentration pages 1-2)

| priority | candidate causal chain or edge | organism/context | evidence class | confidence | main caution |
|---|---|---|---|---|---|
| High | starvation / post-stationary transition -> translational deficiency state -> persister formation | *Escherichia coli*; lag-dependent persistence after starvation/growth transition; ampicillin/ciprofloxacin assays (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4) | 2024 primary single-cell transcriptomics + survival assays | High | Convergent state is strong, but exact upstream trigger may vary by strain/model |
| High | **lon** promotes persister formation / long lag; **lon** loss strongly reduces hyper-persistence | *E. coli* metG* model; CRISPRi and deletion; lag-time and antibiotic-survival readouts (blattman2024identificationandgenetic pages 5-6, blattman2024identificationandgenetic pages 7-8, blattman2024identificationandgenetic pages 6-6) | 2024 primary genetic perturbation | High | Strongest in metG* starvation-linked model; taxon/model scope should be retained |
| High | **yqgE** promotes post-starvation dormancy and persistence; **yqgE** expression is sufficient to increase lag and persistence | *E. coli*; metG* and wild-type contexts (blattman2024identificationandgenetic pages 7-8, blattman2024identificationandgenetic pages 1-2) | 2024 primary genetic perturbation | High | Mechanism downstream of YqgE remains incompletely resolved |
| High | cCF10 -> Opp/Opp2 uptake system -> reduced (p)ppGpp accumulation / maintained metabolism -> reduced persister formation | *Enterococcus faecalis* OG1RF; levofloxacin 20 mg/mL for 8 h; cCF10 10-12 ng/mL lowers persistence from 0.109% to ~0.047-0.050% (zhu2024pheromoneccf10inhibits pages 5-7, zhu2024pheromoneccf10inhibits pages 7-11, zhu2024pheromoneccf10inhibits pages 11-12, zhu2024pheromoneccf10inhibits pages 1-2) | 2024 primary intervention study | High | Single strain; pheromone concentrations above natural extracellular levels; not yet generalized |
| High | ciprofloxacin (10x MIC) exposure -> persister formation with biphasic killing and unchanged susceptibility | *Enterococcus faecium* AUS004; MIC 2 ug/mL; >2-log initial kill then plateau (pont2024proteomiccharacterizationof pages 1-2) | 2024 primary induction/phenotyping study | High | Establishes phenotype robustly, but downstream protein changes are mostly associative |
| Medium | HipA activation / hipA7 -> GltX inhibition -> uncharged tRNA -> RelA activation -> (p)ppGpp accumulation -> persister formation | Mainly *E. coli*; foundational model summarized in 2024 reviews (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 3-6) | Review-supported established mechanism | Medium-High | Widely cited but not uniformly dominant across taxa/conditions |
| Medium | TisB toxin activity -> PMF collapse / ATP synthesis inhibition -> dormancy -> increased persistence | Mainly *E. coli* under SOS/antibiotic stress (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 3-6) | Review-supported established mechanism | Medium | Strong within specific TA-module contexts; not a universal persister pathway |
| Medium | low intracellular ATP state -> persister/VBNC fate association | *E. coli* single-cell ATP biosensor study (li2024intracellularatpconcentration pages 1-2) | 2024 primary single-cell physiology | Medium | Clear association; direct causality for persister formation is weaker than for VBNC resuscitation |
| Medium | TCA-cycle / central metabolism activity modulates persister lag and survival | *E. coli* CRISPRi pathway-level effects across models (blattman2024identificationandgenetic pages 5-6, blattman2024identificationandgenetic pages 23-30) | 2024 primary genetic screen | Medium | More pathway-level than node-specific; direction may depend on perturbation and model |
| Low | oxidative-stress and stress-proteostasis proteins (e.g., CspA, PrsA, ClpX) associate with persister state | *E. faecium* ciprofloxacin persisters (pont2024proteomiccharacterizationof pages 1-2) | 2024 primary proteomics, association only | Low | Differential abundance does not establish causal role |
| Low | biofilm formation enriches/promotes persister formation | Cross-species; especially *E. faecalis* and review contexts (zhu2024pheromoneccf10inhibits pages 7-11, vergoz2025antibioticpersistercells pages 3-3, niu2024bacterialpersistersmolecular pages 6-7) | Mixed primary + review contextual evidence | Low-Medium | Community-level tolerance may be confounded with true single-cell persistence; avoid over-curation as direct edge |
| Low | SOS / DNA repair genes promote persistence | Review-supported across taxa; some strain-specific support (yuan2024molecularmechanismand pages 6-7, vergoz2025antibioticpersistercells pages 8-8, niu2024bacterialpersistersmolecular pages 28-29) | Review-supported / indirect primary support | Low-Medium | Often difficult to separate cause of persister entry from damage response after antibiotic exposure |


*Table: This table ranks candidate causal edges for persister cell formation by curation priority, emphasizing direct 2024 perturbation evidence first and separating established review-backed mechanisms from association-only observations. It is useful for deciding which nodes and edges are safest to curate now versus which should remain provisional.*

## Candidate graph nodes

Identifiers below are limited to stable CURIEs that can be assigned confidently; unresolved entities remain label-only rather than receiving invented identifiers.

### Trait and organism nodes

- `traitmech:000082` — persister cell formation
- `NCBITaxon:562` — *Escherichia coli*
- `NCBITaxon:1351` — *Enterococcus faecalis*
- `NCBITaxon:1352` — *Enterococcus faecium*
- Label-only taxon/context candidates: *Staphylococcus aureus*, *Pseudomonas aeruginosa*, *Mycobacterium tuberculosis*, biofilm-associated cells, intracellular bacteria.

### Environmental and experimental factors

- Nutrient starvation / prolonged stationary phase
- Amino-acid limitation
- Acidic pH, oxidative stress, and host intracellular stress
- Antibiotic exposure: ampicillin, ciprofloxacin, levofloxacin; ground individual chemicals only after identifier verification
- Biofilm growth and nutrient/oxygen gradients
- Post-stationary dilution into fresh medium / lag-phase transition
- cCF10 pheromone treatment
- Carbon-metabolite supplementation, including mannitol

### Genes, proteins, and complexes

- `lon` — ATP-dependent Lon protease
- `yqgE` — poorly characterized persistence/dormancy modulator
- `metG` / `metG*` — methionine–tRNA ligase and hypomorphic experimental allele
- `hipA`, `hipB` — HipAB toxin–antitoxin system
- `gltX` — glutamyl–tRNA synthetase
- `relA`, `spoT` — (p)ppGpp metabolism/stringent-response proteins
- `tisB`, `istR-1`; `hokB`, `sokB` — type-I toxin–antitoxin modules
- `recA`, `sulA` — SOS/damage-response components
- `opp2A`, `opp2D`, `opp2F` — Opp2 peptide-uptake components in the reported *E. faecalis* model
- `phoU` — phosphate-regulatory protein implicated in the cCF10 study
- `atpB`, `atpD` — ATP synthase subunits
- `dnaE`, `recG` — DNA replication/repair candidates
- `sucA` and the tricarboxylic-acid-cycle module
- `rmf` — ribosome modulation factor; marker/candidate rather than a high-confidence universal cause
- CspA, PrsA, ClpX and oxidative-stress enzymes — association-only candidates from *E. faecium* proteomics.

Protein CURIEs should be assigned as taxon-specific UniProt accessions during YAML implementation; gene symbols alone are unsafe across species.

### Chemicals, cellular states, and biological processes

- `CHEBI:15422` — ATP
- Label-only pending identifier verification: ppGpp, pppGpp, cCF10, proton motive force, membrane potential
- Stringent response; ATP generation; TCA cycle; translation; translational deficiency; tRNA aminoacylation; protein degradation/proteostasis; SOS response; DNA repair; drug efflux; oxidative-stress response; dormancy/long lag; post-stress awakening
- Cellular localizations: cytoplasm, ribosome, inner/cytoplasmic membrane, membrane transporter complex.

## Evidence-backed candidate edges

“High” denotes direct intervention or genetic perturbation in a primary study. “Medium” denotes a mechanistically detailed model supported by primary literature but recovered here mainly through an authoritative review. “Low/provisional” denotes association, context dependence, or possible phenotype conflation.

| Subject | Predicate | Object | Evidence snippet | Reference | Curation note |
|---|---|---|---|---|---|
| Prolonged starvation/post-stationary transition | promotes | persister-state entry | “starved wild-type *E. coli* for 6 days… increased the persistence rate… to nearly 1%”; 7.4% occupied the persister cluster. | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), published 6 Nov 2024 (blattman2024identificationandgenetic pages 3-4) | **High; *E. coli*, assay-specific.** Use prolonged starvation, not generic starvation, as the subject. |
| Persister-state entry across tested models | has convergent feature | translational deficiency | Persisters from multiple models converged on a distinct state “primarily defined by translational deficiency.” | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), 6 Nov 2024 (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4) | **High for state association; medium for direct causality.** Avoid asserting that all persisters are translation-inactive. |
| `lon` activity | promotes | `metG*` lag-dependent persistence | `lon` knockdown shortened lag; deleting `lon` reversed hyper-persistence, and `metG* Δlon ΔsulA` reduced survival >100,000-fold. | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), 6 Nov 2024 (blattman2024identificationandgenetic pages 5-6, blattman2024identificationandgenetic pages 7-8) | **High; model-specific.** Preserve *E. coli* `metG*` context and avoid universalization. |
| `yqgE` activity | increases | post-starvation dormancy duration | `yqgE` deletion restored stationary-phase translation; expression was sufficient to increase wild-type lag and persistence. | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), 6 Nov 2024 (blattman2024identificationandgenetic pages 7-8) | **High; *E. coli*.** Downstream biochemical mechanism remains unresolved. |
| Longer post-starvation lag/dormancy | promotes | antibiotic persistence | Increased lag coincided with marked increases in survival; genetic shortening of lag reduced survival. | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), 6 Nov 2024 (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 5-6) | **High within tested lag-dependent models.** Not all persistence is lag-dependent. |
| TCA-cycle gene activity | modulates | persister lag and survival | CRISPRi targeting TCA-cycle genes shortened lag across tested cell types; `sucA` was among shared hits. | DOI [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2), 6 Nov 2024 (blattman2024identificationandgenetic pages 5-6, blattman2024identificationandgenetic pages 23-30) | **Medium-high.** Curate pathway-level modulation until individual directions are independently validated. |
| cCF10, 10–12 ng/mL | inhibits | *E. faecalis* persister formation | Persistence fell from 0.109% to approximately 0.047–0.050%. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), published 8 Jul 2024 (zhu2024pheromoneccf10inhibits pages 11-12, zhu2024pheromoneccf10inhibits pages 1-2) | **High; single strain and artificial dose.** |
| cCF10 | activates/upregulates | Opp/Opp2 peptide uptake | cCF10 increased Opp2 components, including `opp2A` 1.61-fold and `opp2D/opp2F` approximately 1.53–3.11-fold. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), 8 Jul 2024 (zhu2024pheromoneccf10inhibits pages 5-7, zhu2024pheromoneccf10inhibits pages 7-11) | **Medium-high.** Expression plus transport model; direct flux evidence is less complete. |
| cCF10 treatment | inhibits | (p)ppGpp accumulation | Authors report suppression of (p)ppGpp and 3.21-fold restoration/upregulation of `phoU` relative to persisters. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), 8 Jul 2024 (zhu2024pheromoneccf10inhibits pages 5-7, zhu2024pheromoneccf10inhibits pages 7-11) | **Medium.** `phoU` is an indirect mechanistic readout; do not encode `phoU directly degrades ppGpp`. |
| cCF10 treatment | increases/maintains | energy metabolism and ATP synthesis | ATP rose approximately 1.16-fold; `atpB` and `atpD` rose 2.82- and 1.29-fold in the reported comparison. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), 8 Jul 2024 (zhu2024pheromoneccf10inhibits pages 7-11) | **Medium-high; dose-dependent.** A higher concentration produced a discordant ATP response. |
| Maintained metabolic activity | reduces | *E. faecalis* persister formation | The authors concluded cCF10 reduced persistence through metabolism rather than suppression of biofilm formation. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), 8 Jul 2024 (zhu2024pheromoneccf10inhibits pages 5-7, zhu2024pheromoneccf10inhibits pages 1-2) | **Medium-high; organism/assay-specific.** |
| Ciprofloxacin, 10× MIC | induces/enriches | *E. faecium* persister population | MIC was 2 µg/mL; treatment produced >2-log initial killing followed by a plateau, while recovered cells retained parental susceptibility and genotype. | DOI [10.1186/s12866-023-03162-8](https://doi.org/10.1186/s12866-023-03162-8), published Jan 2024 (pont2024proteomiccharacterizationof pages 1-2) | **High for phenotype induction/enrichment.** Antibiotic may select pre-existing cells as well as induce states; use “induces/enriches.” |
| HipA | phosphorylates/inhibits | GltX | HipA is described as a kinase targeting glutamyl–tRNA synthetase, generating uncharged tRNA. | DOI [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3), published Nov 2024 (yuan2024molecularmechanismand pages 3-6) | **Medium-high; established *E. coli* mechanism, review-supported here.** |
| Uncharged tRNA | activates | RelA/stringent response | GltX inhibition causes uncharged tRNA accumulation, activating RelA and increasing (p)ppGpp. | Same DOI and date (yuan2024molecularmechanismand pages 3-6) | **Medium-high; *E. coli*.** |
| Elevated (p)ppGpp/stringent response | promotes | persister formation | `relA` or `relA/spoT` mutants produced fewer persisters; starvation-induced (p)ppGpp was linked to TA-module activation. | DOI [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3), Nov 2024 (yuan2024molecularmechanismand pages 6-7) | **Medium; context-dependent and contested as a universal route.** |
| SOS/RecA response | activates | `tisB/istR-1` module | Antibiotic/DNA damage activates the SOS-controlled module; `tisB` deficiency reduced and `istR-1` deficiency increased persisters. | DOI [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3), Nov 2024 (yuan2024molecularmechanismand pages 6-7) | **Medium; *E. coli* and antibiotic-specific.** |
| TisB | dissipates | proton motive force / ATP production | TisB disrupts proton motive force and inhibits ATP synthesis, inducing dormancy. | DOI [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3), Nov 2024 (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 3-6) | **Medium.** Do not generalize to all type-I toxins or taxa. |
| Low intracellular ATP | is associated with | persister state | Single-cell biosensing found lower ATP in persisters than sensitive cells, but distributions overlapped. | DOI [10.1128/jb.00208-24](https://doi.org/10.1128/jb.00208-24), published 12 Nov 2024 (li2024intracellularatpconcentration pages 1-2) | **Provisional association.** The intervention directly resuscitated VBNC cells, not necessarily persisters. |
| Biofilm formation | promotes/enriches | persister formation | In the *E. faecalis* model, biofilm accumulation contributed to persistence; broader reviews report enrichment up to 10% in biofilms versus <1% planktonically. | DOI [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701), 8 Jul 2024; DOI [10.1111/1462-2920.70207](https://doi.org/10.1111/1462-2920.70207), Nov 2025 (zhu2024pheromoneccf10inhibits pages 7-11, vergoz2025antibioticpersistercells pages 3-3) | **Low-medium.** Community tolerance and persister enrichment are easily conflated. |
| Oxidative-stress/proteostasis protein abundance | correlates with | *E. faecium* persister state | Fifty-six proteins differed, including CspA, PrsA, ClpX and oxidative-stress enzymes. | DOI [10.1186/s12866-023-03162-8](https://doi.org/10.1186/s12866-023-03162-8), Jan 2024 (pont2024proteomiccharacterizationof pages 1-2) | **Do not curate as causal yet.** Proteomic association only. |

## Applications and implementation status

### Measurement and research implementation

Time-kill assays remain the principal operational method: a susceptible fraction dies rapidly and a surviving fraction produces a slower second phase. Confirmatory regrowth, repeat susceptibility testing, and preferably genomic checks are needed to exclude resistance. Microfluidics, time-lapse microscopy, fluorescence-activated sorting, ScanLag/colony-appearance analysis, prokaryotic single-cell RNA sequencing, and ATP biosensors now resolve heterogeneity hidden by bulk CFU measurements. These are research platforms rather than routine clinical diagnostics; no universally validated persister biomarker exists. (yuan2024molecularmechanismand pages 7-9, niu2024bacterialpersistersmolecular pages 6-7, li2024intracellularatpconcentration pages 1-2, blattman2024identificationandgenetic pages 1-2)

### Therapeutic strategies

1. **Metabolic potentiation or awakening.** Carbon metabolites can restore aminoglycoside uptake; mannitol reportedly increased tobramycin killing of *P. aeruginosa* persisters by as much as 1,000-fold in experimental systems. cCF10 provides a 2024 example of metabolic maintenance reducing *E. faecalis* persistence, but its effective dose exceeded reported natural extracellular levels by more than two orders of magnitude. These remain largely preclinical strategies. (zhu2024pheromoneccf10inhibits pages 11-12, niu2024bacterialpersistersmolecular pages 20-21)
2. **Killing dormant cells directly.** Membrane-active compounds and antimicrobial peptides can kill independently of active growth. ADEP4 dysregulates ClpP-mediated proteolysis and, with rifampicin, eradicated *S. aureus* biofilm persisters in an early model; a later, more persistent model did not reproduce the result, illustrating model sensitivity. (niu2024bacterialpersistersmolecular pages 15-16)
3. **Targeting signaling.** Relacin and other candidates target (p)ppGpp; quorum-sensing modulators and cis-2-decenoic acid aim to prevent persistence or trigger susceptibility. Most have not entered clinical use. (niu2024bacterialpersistersmolecular pages 20-21, niu2024bacterialpersistersmolecular pages 21-22)
4. **Combination regimens.** Multi-drug regimens are clinically established for tuberculosis, and pyrazinamide helped shorten standard therapy historically from 9–12 to 6 months. Bedaquiline-containing regimens are approved for drug-resistant TB, but these treatments should not be represented as clinically validated interventions specifically for `traitmech:000082` across bacteria. Experimental combinations have cleared persistent infections in animal models, but require clinical validation. (niu2024bacterialpersistersmolecular pages 15-16, niu2024bacterialpersistersmolecular pages 21-22)
5. **Phages and lysins.** Compassionate phage use has been reported for 20 patients with drug-resistant mycobacterial disease, but this is not equivalent to an approved persister-specific treatment. Claims that exebacase/CF-301 provides a successful Phase 3 anti-persister implementation should be treated cautiously: trial-stage status does not establish efficacy against the curated mechanism. (niu2024bacterialpersistersmolecular pages 20-21, niu2024bacterialpersistersmolecular pages 30-31)

## Recent statistics and clinical relevance

- Persisters commonly represent **<1%** of planktonic populations, while a review reports levels **up to 10%** in biofilm mode; *E. coli* stationary-phase cultures reach approximately **1%** in some assays. These are context-dependent experimental estimates, not universal prevalence values. (vergoz2025antibioticpersistercells pages 3-3, niu2024bacterialpersistersmolecular pages 3-4)
- In the 2024 *E. faecium* study, ciprofloxacin at 10× MIC caused an initial viability decrease of **more than two orders of magnitude**, followed by a stable survivor plateau; 56 proteins differed in abundance. (pont2024proteomiccharacterizationof pages 1-2)
- In the 2024 *E. faecalis* model, 8 h of 20 mg/mL levofloxacin yielded **0.109%** persistence; 10–12 ng/mL cCF10 lowered it to about **0.047–0.050%**. (zhu2024pheromoneccf10inhibits pages 11-12, zhu2024pheromoneccf10inhibits pages 1-2)
- Late *P. aeruginosa* isolates from a cystic-fibrosis patient were reported to be **100-fold more persistent** than early isolates. In a Salmonella mouse model, approximately **10–20%** reportedly remained after 10 days of high-dose ciprofloxacin, although survival in vivo cannot automatically be attributed solely to rare persisters. (yuan2024molecularmechanismand pages 1-2)
- SCVs were detected in approximately **1%** of general samples but **17%** of cystic-fibrosis samples in the cited *S. aureus* context; these figures concern SCVs and should not be relabeled as persister prevalence. (goormaghtigh2024understandingstaphylococcusaureus pages 8-9)

Authoritative 2024 analyses therefore support clinical plausibility—persisters are associated with recurrent urinary infection, tuberculosis, typhoid, Lyme disease, biofilms, and intracellular reservoirs—but also emphasize that causal mechanisms are complex and incompletely resolved. Strain, drug, dose, growth phase, and environment can alter both frequency and mechanism. The field still lacks routine clinical detection and quantitative proof that a given rare-persister mechanism, rather than bulk nutrient-limited tolerance or drug penetration, dominates treatment failure in a specific patient. (niu2024bacterialpersistersmolecular pages 1-3, vergoz2025antibioticpersistercells pages 3-3, kunnath2024bacterialpersistercells pages 1-2)

## Warnings: claims not ready for TraitMech curation

1. **Do not encode dormancy → persistence as universal.** Dormancy and slow growth are common but not sufficient; some survivors are metabolically active, and non-growing cells can still die.
2. **Do not encode low ATP as a universal sufficient cause.** The 2024 single-cell study found overlapping ATP distributions, and its strongest intervention concerned VBNC resuscitation. (li2024intracellularatpconcentration pages 1-2)
3. **Do not treat every toxin–antitoxin module as causal.** HipA and TisB have defined evidence in *E. coli*, but TA effects are highly module-, strain-, and assay-specific. (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 3-6)
4. **Do not curate differential abundance as causation.** CspA, PrsA, ClpX, oxidative-stress enzymes, `rmf`, and efflux markers require targeted perturbation in the relevant model. (pont2024proteomiccharacterizationof pages 1-2, blattman2024identificationandgenetic pages 3-4)
5. **Do not merge biofilm formation with persister formation.** Biofilms can enrich persisters, but matrix protection and bulk metabolic restriction are separate causal processes.
6. **Do not infer clinical efficacy from in-vitro persister killing.** ADEP4, metabolic adjuvants, AMPs, QS inhibitors, and most phage approaches remain preclinical or incompletely validated. (niu2024bacterialpersistersmolecular pages 20-21, niu2024bacterialpersistersmolecular pages 15-16)
7. **Do not use biphasic CFU decline alone.** Antibiotic carryover, aggregation, delayed post-exposure death, resistant mutants, and heterogeneous population tolerance can mimic a persister tail.
8. **Do not assign unverified ontology identifiers.** cCF10, ppGpp/pppGpp, strain-specific Opp components, and individual antibiotics should receive CURIEs only after checking the target ontology release.

## Recommended first-pass YAML graph

The safest compact graph is:

`prolonged starvation` → **promotes** → `translationally deficient persister state` → **extends** → `post-starvation lag/dormancy` → **promotes** → `traitmech:000082`

with parallel, scoped branches:

- *E. coli*: `yqgE` and `lon` → **promote** → `post-starvation lag/persistence`;
- *E. coli*: `HipA` → **inhibits** → `GltX` → **activates via uncharged tRNA** → `RelA/(p)ppGpp` → **promotes** → persistence;
- *E. coli*, SOS context: `TisB` → **dissipates** → proton motive force / ATP generation → **promotes** → dormancy and persistence;
- *E. faecalis* OG1RF: `cCF10 treatment` → **activates** → `Opp/Opp2 uptake` → **reduces** → `(p)ppGpp accumulation` → **maintains** → energy metabolism → **inhibits** → `traitmech:000082`;
- *E. faecium* AUS004: `ciprofloxacin exposure` → **induces/enriches** → `traitmech:000082`.

This graph should carry taxon, strain, antibiotic, growth-state, and assay qualifiers on every mechanistic edge.

## DOI-first bibliography

1. Blattman SB et al. **Identification and genetic dissection of convergent persister cell states.** *Nature* 636, 438–446. Published online **6 November 2024**. DOI: [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2). (blattman2024identificationandgenetic pages 1-2)
2. Niu H, Gu J, Zhang Y. **Bacterial persisters: molecular mechanisms and therapeutic development.** *Signal Transduction and Targeted Therapy* 9:174. Published **July 2024**; accepted 13 May 2024. DOI: [10.1038/s41392-024-01866-5](https://doi.org/10.1038/s41392-024-01866-5). (niu2024bacterialpersistersmolecular pages 1-3)
3. Yuan S et al. **Molecular mechanism and application of emerging technologies in study of bacterial persisters.** *BMC Microbiology* 24:480. Published **November 2024**. DOI: [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3). (yuan2024molecularmechanismand pages 1-2)
4. Li B et al. **Intracellular ATP concentration is a key regulator of bacterial cell fate.** *Journal of Bacteriology* 206(12). Published **12 November 2024**. DOI: [10.1128/jb.00208-24](https://doi.org/10.1128/jb.00208-24). (li2024intracellularatpconcentration pages 1-2)
5. Zhu L et al. **Pheromone cCF10 inhibits the antibiotic persistence of Enterococcus faecalis by modulating energy metabolism.** *Frontiers in Microbiology* 15:1408701. Published **8 July 2024**. DOI: [10.3389/fmicb.2024.1408701](https://doi.org/10.3389/fmicb.2024.1408701). (zhu2024pheromoneccf10inhibits pages 1-2)
6. Le Pont C et al. **Proteomic characterization of persisters in Enterococcus faecium.** *BMC Microbiology* 24:9. Published **January 2024**. DOI: [10.1186/s12866-023-03162-8](https://doi.org/10.1186/s12866-023-03162-8). (pont2024proteomiccharacterizationof pages 1-2)
7. Goormaghtigh F, Van Bambeke F. **Understanding Staphylococcus aureus internalisation and induction of antimicrobial tolerance.** *Expert Review of Anti-infective Therapy* 22:87–101. Published **January 2024**. DOI: [10.1080/14787210.2024.2303018](https://doi.org/10.1080/14787210.2024.2303018). (goormaghtigh2024understandingstaphylococcusaureus pages 8-9)
8. Prasetyoputri A et al. **The Eagle Effect and antibiotic-induced persistence: two sides of the same coin?** *Trends in Microbiology* 27:339–354. Published **April 2019**. DOI: [10.1016/j.tim.2018.10.007](https://doi.org/10.1016/j.tim.2018.10.007). (prasetyoputri2019theeagleeffect pages 8-9)

References

1. (yuan2024molecularmechanismand pages 2-3): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 28 citations and is from a peer-reviewed journal.

2. (yuan2024molecularmechanismand pages 7-9): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 28 citations and is from a peer-reviewed journal.

3. (pont2024proteomiccharacterizationof pages 1-2): Charlotte Le Pont, Benoît Bernay, Mattéo Gérard, Anne Dhalluin, François Gravey, and Jean-Christophe Giard. Proteomic characterization of persisters in enterococcus faecium. BMC Microbiology, Jan 2024. URL: https://doi.org/10.1186/s12866-023-03162-8, doi:10.1186/s12866-023-03162-8. This article has 10 citations and is from a peer-reviewed journal.

4. (niu2024bacterialpersistersmolecular pages 3-4): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

5. (blattman2024identificationandgenetic pages 1-2): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

6. (prasetyoputri2019theeagleeffect pages 8-9): Anggia Prasetyoputri, Angie M. Jarrad, Matthew A. Cooper, and Mark A.T. Blaskovich. The eagle effect and antibiotic-induced persistence: two sides of the same coin? Trends in microbiology, 27 4:339-354, Apr 2019. URL: https://doi.org/10.1016/j.tim.2018.10.007, doi:10.1016/j.tim.2018.10.007. This article has 147 citations and is from a domain leading peer-reviewed journal.

7. (li2024intracellularatpconcentration pages 1-2): Bo Li, Xiao Chen, Jin-Yu Yang, Song Gao, and Fan Bai. Intracellular atp concentration is a key regulator of bacterial cell fate. Journal of Bacteriology, Dec 2024. URL: https://doi.org/10.1128/jb.00208-24, doi:10.1128/jb.00208-24. This article has 30 citations and is from a peer-reviewed journal.

8. (goormaghtigh2024understandingstaphylococcusaureus pages 8-9): Frédéric Goormaghtigh and Françoise Van Bambeke. Understanding <i>staphylococcus aureus</i> internalisation and induction of antimicrobial tolerance. Expert Review of Anti-infective Therapy, 22:87-101, Jan 2024. URL: https://doi.org/10.1080/14787210.2024.2303018, doi:10.1080/14787210.2024.2303018. This article has 25 citations and is from a peer-reviewed journal.

9. (blattman2024identificationandgenetic pages 3-4): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

10. (vergoz2025antibioticpersistercells pages 3-3): Delphine Vergoz, Emmanuelle Dé, Corinne Loutelier-Bourhis, and Stéphane Alexandre. Antibiotic persister cells in <scp> <i>acinetobacter baumannii</i> </scp> : overview of molecular mechanisms and removal strategies. Environmental Microbiology, Nov 2025. URL: https://doi.org/10.1111/1462-2920.70207, doi:10.1111/1462-2920.70207. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (blattman2024identificationandgenetic pages 5-6): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

12. (blattman2024identificationandgenetic pages 7-8): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

13. (blattman2024identificationandgenetic pages 6-6): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

14. (zhu2024pheromoneccf10inhibits pages 7-11): Li Zhu, Xiaobo Yang, Xinyue Fu, Panpan Yang, Xiaoli Lin, Feng Wang, Zhiqiang Shen, Jingfeng Wang, Feilong Sun, and Zhigang Qiu. Pheromone ccf10 inhibits the antibiotic persistence of enterococcus faecalis by modulating energy metabolism. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1408701, doi:10.3389/fmicb.2024.1408701. This article has 8 citations and is from a peer-reviewed journal.

15. (zhu2024pheromoneccf10inhibits pages 11-12): Li Zhu, Xiaobo Yang, Xinyue Fu, Panpan Yang, Xiaoli Lin, Feng Wang, Zhiqiang Shen, Jingfeng Wang, Feilong Sun, and Zhigang Qiu. Pheromone ccf10 inhibits the antibiotic persistence of enterococcus faecalis by modulating energy metabolism. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1408701, doi:10.3389/fmicb.2024.1408701. This article has 8 citations and is from a peer-reviewed journal.

16. (zhu2024pheromoneccf10inhibits pages 1-2): Li Zhu, Xiaobo Yang, Xinyue Fu, Panpan Yang, Xiaoli Lin, Feng Wang, Zhiqiang Shen, Jingfeng Wang, Feilong Sun, and Zhigang Qiu. Pheromone ccf10 inhibits the antibiotic persistence of enterococcus faecalis by modulating energy metabolism. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1408701, doi:10.3389/fmicb.2024.1408701. This article has 8 citations and is from a peer-reviewed journal.

17. (zhu2024pheromoneccf10inhibits pages 5-7): Li Zhu, Xiaobo Yang, Xinyue Fu, Panpan Yang, Xiaoli Lin, Feng Wang, Zhiqiang Shen, Jingfeng Wang, Feilong Sun, and Zhigang Qiu. Pheromone ccf10 inhibits the antibiotic persistence of enterococcus faecalis by modulating energy metabolism. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1408701, doi:10.3389/fmicb.2024.1408701. This article has 8 citations and is from a peer-reviewed journal.

18. (yuan2024molecularmechanismand pages 6-7): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 28 citations and is from a peer-reviewed journal.

19. (yuan2024molecularmechanismand pages 3-6): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 28 citations and is from a peer-reviewed journal.

20. (blattman2024identificationandgenetic pages 23-30): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

21. (niu2024bacterialpersistersmolecular pages 6-7): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

22. (vergoz2025antibioticpersistercells pages 8-8): Delphine Vergoz, Emmanuelle Dé, Corinne Loutelier-Bourhis, and Stéphane Alexandre. Antibiotic persister cells in <scp> <i>acinetobacter baumannii</i> </scp> : overview of molecular mechanisms and removal strategies. Environmental Microbiology, Nov 2025. URL: https://doi.org/10.1111/1462-2920.70207, doi:10.1111/1462-2920.70207. This article has 8 citations and is from a domain leading peer-reviewed journal.

23. (niu2024bacterialpersistersmolecular pages 28-29): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

24. (niu2024bacterialpersistersmolecular pages 20-21): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

25. (niu2024bacterialpersistersmolecular pages 15-16): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

26. (niu2024bacterialpersistersmolecular pages 21-22): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

27. (niu2024bacterialpersistersmolecular pages 30-31): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

28. (yuan2024molecularmechanismand pages 1-2): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 28 citations and is from a peer-reviewed journal.

29. (niu2024bacterialpersistersmolecular pages 1-3): Hongxia Niu, Jiaying Gu, and Ying Zhang. Bacterial persisters: molecular mechanisms and therapeutic development. Signal Transduction and Targeted Therapy, Jul 2024. URL: https://doi.org/10.1038/s41392-024-01866-5, doi:10.1038/s41392-024-01866-5. This article has 329 citations and is from a peer-reviewed journal.

30. (kunnath2024bacterialpersistercells pages 1-2): Anil Philip Kunnath, Mohamed Suodha Suoodh, Dinesh Kumar Chellappan, Jestin Chellian, and Kishneth Palaniveloo. Bacterial persister cells and development of antibiotic resistance in chronic infections: an update. British Journal of Biomedical Science, Aug 2024. URL: https://doi.org/10.3389/bjbs.2024.12958, doi:10.3389/bjbs.2024.12958. This article has 97 citations.