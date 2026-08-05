---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:49:29.857084'
end_time: '2026-08-04T01:57:03.770027'
duration_seconds: 453.91
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range
  trait_identifier: METPO:1000334
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits that bounds the minimum and
    maximum NaCl concentrations supporting growth of an organism.
  parent_traits: METPO:1000532, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the span of NaCl concentrations supporting growth as a standard halophily
    descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations
    (Saline-Systems review supports osmotic-tolerance breadth as the basis of the
    NaCl-range phenotype.)'
  causal_graph_summary: 'nacl_range_tolerance_breadth: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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
- **Trait label:** NaCl range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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


# Curation report: microbial NaCl range

## Executive summary

**Target trait:** **NaCl range**  
**Trait identifier:** **METPO:1000334**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED

The trait should represent the **assay-observed interval bounded by the minimum and maximum NaCl concentrations that support microbial growth**, not merely survival, a single tolerated concentration, an optimum, or salt-stress responsiveness. Each range assertion should therefore preserve medium, units, temperature, pH, oxygenation, incubation time, inoculum/acclimation, and the criterion used to call growth.

The strongest recent causal evidence comes from a 2024 *Halomonas elongata* engineering study. Deleting ectoine-biosynthesis genes made growth above 4% NaCl impossible in the tested minimal medium, whereas installing a feedback-resistant proline-biosynthesis module and deleting proline catabolism restored growth at 8% NaCl. This directly links compatible-solute biosynthesis and accumulation to the upper portion of an NaCl growth range. Most other recent studies are transcriptomic, proteomic, genomic, or comparative and support mechanisms but not causal graph edges without an uncertainty qualifier. (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9)

## 1. Trait scope and boundary cases

### 1.1 Recommended operational interpretation

Curate **METPO:1000334** as a composite quantitative phenotype:

> For organism or strain *x*, under assay context *c*, growth is observed from NaCl concentration *L* through *U*, where *L* and *U* are the tested minimum and maximum concentrations satisfying a stated growth criterion.

A defensible data model should record:

- lower and upper limits separately;
- concentration unit and basis—preferably molarity or % w/v explicitly, never an unqualified “%”;
- whether the reported variable is NaCl itself, total salts, salinity, ionic strength, or Na⁺ concentration;
- growth endpoint, such as OD600 increase, colony formation, biomass, or growth rate;
- medium composition, because compatible solutes or their precursors can materially change apparent tolerance;
- temperature, pH, oxygen regime, duration, inoculum size, and prior salt acclimation;
- whether the limits were directly bracketed by adjacent negative tests.

For example, *Salinicola* sp. DM10 was tested in nutrient broth at 0–33% NaCl, in 2.5-percentage-point increments, for five days at 30°C and 200 rpm, with growth assessed by OD600; the authors reported growth up to 25%. That is a reasonably explicit upper-bound assay, although the precise minimum and the last negative concentration should remain attached to the record. (nguyen2023draftgenomesequencing pages 4-5, nguyen2023draftgenomesequencing pages 1-2)

### 1.2 Distinctions from nearby traits

- **NaCl optimum:** concentration or interval producing maximal growth, not the supported range. *Natranaerobius thermophilus*, for example, has a reported broad high-salt growth interval and a narrower optimum; these must be represented separately. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7)
- **NaCl tolerance at a single concentration:** “grows at 20% NaCl” supplies evidence for a tested positive point or lower bound on the maximum, but not necessarily a complete range. *Bacillus subtilis* ACP81 grew at 20% NaCl, yet its mechanistic transcriptome comparison was only 0% versus the sublethal 6% condition. (li2024integratedgenomicsand pages 1-2)
- **Halophily class:** “halophile,” “moderate halophile,” and “extreme halophile” summarize salt preference or requirement. A widely used working definition places optimum growth at ≥50 g/L NaCl and tolerance at ≥100 g/L, but these labels are not substitutes for strain-level numerical ranges. (oren2008microbiallifeat pages 2-4)
- **Salt requirement/minimum:** some salt-in organisms require substantial salt for structural stability. Halobacteria and *Salinibacter* commonly require >150 g/L NaCl because their cellular machinery is adapted to high intracellular KCl; this explains an elevated lower limit, not merely a high upper limit. (oren2008microbiallifeat pages 10-11)
- **Survival or viability:** persistence after salt exposure without multiplication is outside the trait.
- **Osmotic-stress range:** NaCl imposes both osmotic and ion-specific effects. Results using sucrose, sorbitol, KCl, seawater salts, or Na⁺ concentration should not automatically be asserted as NaCl-range evidence.
- **Environmental salinity:** habitat salinity is exposure metadata, not proof of laboratory growth limits.
- **Enzyme salt tolerance:** activity of an isolated halophilic enzyme does not establish the producing organism’s growth range.

## 2. Current mechanistic understanding

Two canonical strategies dominate. In the **salt-in strategy**, cells accumulate KCl or related inorganic ions and adapt their proteome to high ionic strength. Such proteomes are often acidic and may lose stability at low salt, potentially raising the trait’s lower bound. In the **compatible-solute strategy**, cells limit cytoplasmic salt while synthesizing or importing relatively non-perturbing osmolytes such as ectoine, glycine betaine, proline, glutamate, sugars, and polyols. This strategy is generally associated with broader salinity flexibility. Some organisms combine both strategies. (oren2008microbiallifeat pages 10-11)

The acute physiological sequence described for *B. subtilis* is: increased external osmolarity causes water efflux, cytoplasmic dehydration, loss of turgor, and impaired growth; cells first import K⁺ as an emergency response and subsequently replace it with compatible solutes. *B. subtilis* uses OpuA–OpuE uptake systems, synthesizes proline de novo, and can synthesize glycine betaine from imported choline through GbsAB. (rath2020managementofosmoprotectant pages 1-2)

Recent work complicates the strict two-strategy division. In 2024, *N. thermophilus* was shown to combine compatible-solute accumulation with K⁺-centered ion homeostasis across 2.5, 3.7, and 4.3 M Na⁺ conditions. Glycine betaine, glutamate, and proline increased with salinity, while Opu/ProU-family transporters, sodium/solute symporters, Trk proteins, and Na⁺/H⁺ antiporters were upregulated. The authors validated proteomic results against 109 co-upregulated genes with 98.2% transcript–protein correspondence. These results strongly support a hybrid adaptation module, but they remain largely associative because the transporters were not individually disrupted. (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 10-14)

## 3. Candidate graph nodes

### 3.1 Trait and environmental/assay nodes

- **NaCl range** — `METPO:1000334`
- minimum growth-supporting NaCl concentration — label-only assay datum
- maximum growth-supporting NaCl concentration — label-only assay datum
- NaCl concentration — chemical/environmental exposure; use a verified CHEBI entry during implementation
- extracellular osmolarity — label-only or verified ENVO/PATO/GO-aligned term
- water activity — label-only candidate
- medium composition; carbon source; nitrogen source; compatible-solute availability; choline availability
- temperature, pH, oxygen regime, incubation time, agitation, inoculum history, salt acclimation
- growth by OD600; colony formation; biomass yield; specific growth rate

### 3.2 Chemicals and metabolites

- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- chloride — `CHEBI:17996`
- L-proline — `CHEBI:17203`
- glycine betaine — `CHEBI:17750`
- L-glutamate — `CHEBI:29985`
- choline — `CHEBI:15354`
- ectoine, hydroxyectoine, trehalose, glucosylglycerol, alanine, serine, glucose, KCl — retain as labels until the exact chemical form and verified CURIE are selected
- intracellular compatible-solute pool; intracellular K⁺ concentration; cytoplasmic water; turgor pressure

### 3.3 Genes, proteins, transporters, and regulators

Exact strain-specific database accessions should be verified before YAML entry; gene symbols below are safe labels, not universal identifiers.

- **Ectoine synthesis:** `ectA`, `ectB`, `ectC`; EctABC module
- **Proline synthesis:** `proB`, `proA`, `proC`; γ-glutamyl kinase, γ-glutamyl-phosphate reductase, pyrroline-5-carboxylate reductase
- **Proline catabolism:** `putA`; bifunctional proline utilization protein
- **Compatible-solute transport:** OpuA, OpuB, OpuC, OpuD, OpuE; ProU (`proVWX`); `putP`; BetT/BCCT-family transporters
- **Glycine-betaine synthesis/regulation:** `gbsA`, `gbsB`, `gbsR`, `betB`; SigB; S1290 antisense RNA
- **Ion homeostasis:** TrkA/TrkH K⁺ uptake proteins; NhaC-family Na⁺/H⁺ antiporters; Na⁺/K⁺/H⁺ transport systems
- **Membrane/carbohydrate response:** PTS components; `malL`, `celB`, `celC`
- **Motility/energy allocation:** `flhF`, FlhCD, flagellar-assembly operon—candidate modifiers only

### 3.4 Processes, functions, and locations

- response to osmotic stress — `GO:0006970`
- cellular response to salt stress — `GO:0071472`
- compatible-solute biosynthesis and transmembrane transport — use verified descendant GO terms during curation
- potassium-ion transport, sodium-ion transport, Na⁺/H⁺ antiport, ion homeostasis
- maintenance/recovery of turgor pressure
- proline biosynthetic process; ectoine biosynthetic process; glycine-betaine biosynthetic process
- cytoplasmic membrane/plasma membrane — `GO:0005886`
- cytoplasm — `GO:0005737`
- ABC transporter complex — `GO:0043190`
- flagellar assembly; carbohydrate metabolism; membrane synthesis

### 3.5 Organism/strain context nodes

- *Halomonas elongata* OUT30018, KA1, HN1–HN6
- *Natranaerobius thermophilus*
- *Bacillus subtilis* ACP81 and BSB1 derivatives
- *Salinicola* sp. DM10
- *Halomonas bluephagenesis* TD1.0

NCBI Taxonomy identifiers should be resolved at the exact strain or lowest reliable species level during implementation rather than inferred here.

## 4. Candidate causal edges

The following compact artifact summarizes the strongest intervention-supported and associative candidates.

| subject | predicate | object | evidence strength | organism/assay | quantitative effect | DOI |
|---|---|---|---|---|---|---|
| ectABC deletion | decreases | growth at elevated NaCl | direct genetic intervention | *Halomonas elongata* KA1; M63 minimal medium with graded NaCl | Ect-deficient KA1 “could not grow in minimal media containing more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24 |
| proBm1AC insertion at ectABC locus | increases | intracellular proline accumulation | direct genetic intervention | *H. elongata* HN2/HN6; LB + 15% NaCl or M63 + 6–8% NaCl | HN6 accumulated 123.03 µmol/g CFW Pro in LB + 15% NaCl; 115.9 ± 7.8 µmol/g CFW in M63 + 6% NaCl; 353.1 ± 40.5 µmol/g CFW in M63 + 8% NaCl (khanh2024metabolicpathwayengineering pages 15-17, khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| putA deletion | increases | intracellular proline accumulation | direct genetic intervention | *H. elongata* HN4/HN5/HN6 vs putA+ counterparts; LB + 15% NaCl | PutA-deficient strains accumulated much higher Pro than putA-expressing counterparts; HN6 123.03 vs HN2 4.09 µmol/g CFW (khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| increased intracellular proline accumulation | increases | NaCl growth tolerance/range upper bound | direct genetic intervention with phenotypic readout | *H. elongata* HN6; M63 minimal medium, 3–9% NaCl, OD600 at 48 h | HN6 “thrived in the medium containing 8% NaCl”; IC50 6.1% NaCl and IC25 7.2% vs HN1 IC50 4.2% and IC25 5.2%; KA1 could not grow >4% NaCl (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| salt-inducible ectA promoter driving proBm1AC | contributes to increased expression under higher salinity | improved growth at 6% NaCl | direct engineered-regulation evidence, partly interpretive | *H. elongata* HN2; M63 + 6.0% NaCl | HN2 became significantly better than KA1/HN1/HN4/HN5 at 6.0% NaCl; authors note this “may be the result of the higher expression of the mCherry-proBm1AC operon, which was put under the control of the salt-inducible ectA promoter” (khanh2024metabolicpathwayengineering pages 6-9) | 10.1128/aem.01195-24 |
| increasing external Na+ / salinity | associated with increased accumulation of glycine betaine, glutamate, and proline | long-term salt adaptation | associative multi-omics, not direct causal intervention | *Natranaerobius thermophilus*; 2.5, 3.7, 4.3 M Na+ proteome/metabolite profiling | Compatible solute content increased with rising salinity; operational growth range 2.5–5.0 M Na+ and optimum 3.1–4.3 M (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/aem.00145-24 |
| upregulation of Opu/ProU/SSS-family transporters and Na+/K+/H+ transporters | associated with | adaptation to high salinity and K+ homeostasis | associative proteomic/transcriptomic, not direct causal intervention | *N. thermophilus*; comparative salinity proteomics | Reported opu/proU, putP, sdcS, trkA/trkH, nhaC upregulation across salinity conditions; interpreted as maintaining intracellular K+ and osmotic balance (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/aem.00145-24 |
| 6% NaCl salt stress | upregulates | compatible-solute transport, betB/gbsB, membrane/PTS/flagellar genes | associative transcriptomics, not direct causal intervention | *Bacillus subtilis* ACP81; 0% vs 6% NaCl transcriptome | ACP81 could grow in 20% NaCl; at 6% NaCl, betB and gbsB increased 76-fold and 81-fold; 932 DEGs total (li2024integratedgenomicsand pages 5-8, li2024integratedgenomicsand pages 1-2) | 10.3390/microorganisms12020285 |
| 6% NaCl salt stress with carbohydrate-hydrolase response | associated with | higher cellulase and β-amylase activity and glucose-mediated stress mitigation | associative transcriptomics/physiology, not direct causal intervention | *B. subtilis* ACP81; sub-lethal 6% NaCl | Growth possible up to 20% NaCl; sub-lethal 6% NaCl; malL/celB/celC upregulated and authors infer accumulated glucose mitigated salt stress (li2024integratedgenomicsand pages 1-2, li2024integratedgenomicsand pages 5-8) | 10.3390/microorganisms12020285 |
| high osmolarity / salt conditions | associated with upregulation of | ectoine synthesis and glycine betaine/proline, glutamine, trehalose/maltose ABC transporters | associative omics, not direct causal intervention | *Halomonas bluephagenesis* TD1.0; LB20/60/100 g/L NaCl multi-omics | Transport pathways differentiated between salt conditions; authors suggest favored osmoprotectant import under osmotic stress (park2023onlineomicsplatform pages 6-7, park2023onlineomicsplatform pages 1-2) | 10.1177/11779322231171779 |


*Table: This table summarizes the most curator-ready causal edges for microbial NaCl range, prioritizing direct 2024 intervention evidence from engineered Halomonas elongata. It also separates associative 2024 omics links in Natranaerobius and Bacillus from true causal manipulations.*

Additional curator-facing triples and evidence are given below.

| Candidate subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|
| **ectABC activity → enables → ectoine accumulation** | Khanh et al. 2024: wild-type OUT30018 has a “salt-tolerant phenotype (0.3%–21% NaCl) due to the ability to produce and accumulate ectoine,” whereas KA1 is `ΔectABC`. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 15-17, khanh2024metabolicpathwayengineering pages 1-2) | Strong mechanistic background; the exact ectoine amount in KA1 versus wild type should be extracted if this edge is curated separately. |
| **ectABC deletion → decreases → upper NaCl growth capacity** | “The Ect-deficient *H. elongata* KA1 could not grow in minimal media containing more than 4% NaCl.” (khanh2024metabolicpathwayengineering pages 1-2) | **High-priority direct edge.** Assay-specific to M63 minimal medium and the tested strain. Do not generalize the numerical cutoff across *H. elongata*. |
| **feedback-resistant proBm1AC expression → increases → proline biosynthesis/accumulation** | The installed cluster encodes feedback-insensitive γ-glutamate kinase, γ-glutamyl-phosphate reductase, and P5C reductase; HN6 accumulated 115.9 ± 7.8 µmol/g fresh weight at 6% NaCl and 353.1 ± 40.5 µmol/g at 8% NaCl. (khanh2024metabolicpathwayengineering pages 15-17, khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | **High-priority direct edge.** Represent the artificial module explicitly; it is not the native proline pathway state. |
| **putA deletion → increases → intracellular proline** | At 15% NaCl, putA-deficient HN6 accumulated 123.03 µmol/g fresh weight compared with 4.09 µmol/g in its putA-positive counterpart HN2. (khanh2024metabolicpathwayengineering pages 6-9) | **High-priority direct edge.** Mechanism is reduced proline catabolism, but flux redistribution also affected alanine and serine in other engineered strains. |
| **intracellular proline accumulation → increases → high-NaCl growth** | HN6 “thrived” at 8% NaCl; its growth IC50 and IC25 were 6.1% and 7.2% NaCl, compared with 4.2% and 5.2% for HN1. Authors state that increased tolerance “was a result of an increase in the intracellular accumulation of Pro.” (khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9) | **Strongest phenotype-proximal edge.** IC50/IC25 are inhibition metrics, not literal range endpoints. Curate the positive 8% growth observation separately from IC values. |
| **hyperosmotic stress → causes → water efflux/cytoplasmic dehydration** | Rath et al. 2020: increased external osmolarity “triggers water efflux from the cell, causes dehydration of the cytoplasm, and a concomitant reduction in vital turgor pressure. Growth is thus impaired.” DOI: [10.3389/fmicb.2020.00622](https://doi.org/10.3389/fmicb.2020.00622). (rath2020managementofosmoprotectant pages 1-2) | Strong physiological edge, but source discusses osmolarity generally. For an NaCl-specific graph, connect through an NaCl→external osmolarity exposure node. |
| **K⁺ uptake → initially counteracts → acute osmotic stress** | Cells “initially take up potassium ions as an emergency stress reaction and subsequently replace this ion with…compatible solutes.” (rath2020managementofosmoprotectant pages 1-2) | Mechanistically accepted, but not a direct range-bound experiment in this paper. Curate as general/uncertain unless backed by a transporter perturbation in the target taxon. |
| **OpuA/OpuC/OpuD transport → increases → glycine-betaine uptake** | *B. subtilis* imports glycine betaine through OpuA, OpuC, and OpuD; OpuB/OpuC import choline, which GbsAB converts to glycine betaine. (rath2020managementofosmoprotectant pages 1-2) | Good module-level biology. A direct edge to NaCl range requires knockout/rescue evidence not supplied here. |
| **S1290 antisense RNA → delays → opuB induction after salt shock** | Promoter inactivation showed that delayed osmotic induction of `opuB` “crucially depends on the S1290 antisense RNA”; the mechanism is transcriptional interference. (rath2020managementofosmoprotectant pages 1-2) | Direct regulatory evidence, but phenotype-proximal effect on the NaCl range was not measured. Keep as an internal mechanistic edge, not a final range edge. |
| **environmental choline → requires conversion by GbsAB → glycine-betaine osmoprotection** | Choline “is not a compatible solute per se, but needs to be converted to glycine betaine to confer osmostress protection.” (rath2020managementofosmoprotectant pages 12-14) | Useful boundary node showing that medium composition can alter apparent NaCl range. |
| **increasing salinity → increases → compatible-solute accumulation in N. thermophilus** | Glycine betaine, glutamate, and proline contents increased with salinity; the organism used compatible-solute and salt-in strategies simultaneously. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), published May 2024. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) | **Associative.** Curate `positively associated with`, not `causes`, pending perturbation. |
| **TrkAH/NhaC and related transporter upregulation → supports → ion homeostasis under salinity** | Proteomic fold changes included TrkAH-family proteins and NhaC antiporters; authors interpret transporter upregulation as maintaining intracellular K⁺. (xing2024thepolyextremophilenatranaerobius pages 6-7) | **Taxon-specific and associative.** Protein abundance is not proof that any individual transporter broadens the range. |
| **6% NaCl exposure → upregulates → betB/gbsB in B. subtilis ACP81** | RT-qPCR found `betB` and `gbsB` expression increased 76- and 81-fold; 932 genes were differentially expressed between 0% and 6% NaCl. DOI: [10.3390/microorganisms12020285](https://doi.org/10.3390/microorganisms12020285), published 29 January 2024. (li2024integratedgenomicsand pages 5-8, li2024integratedgenomicsand pages 1-2) | Strong response evidence but **not causal** for the reported 20% growth capability. Curate as exposure→expression only. |
| **salt stress → alters → membrane, PTS, compatible-solute, and flagellar pathways** | ACP81 showed enrichment of plasma-membrane/flagellar functions and altered ABC transport, PTS, amino-acid, carbohydrate, and lipid pathways under 6% NaCl. (li2024integratedgenomicsand pages 5-8) | Multi-pathway association. Avoid asserting that flagellar upregulation broadens the NaCl range. |
| **high osmolarity → upregulates → ectoine synthesis and osmoprotectant transport in H. bluephagenesis** | Ectoine synthesis increased with salt; glycine-betaine/proline, glutamine, and trehalose/maltose ABC transporters were upregulated. DOI: [10.1177/11779322231171779](https://doi.org/10.1177/11779322231171779), accepted 7 April 2023. (park2023onlineomicsplatform pages 6-7, park2023onlineomicsplatform pages 1-2) | Associative omics. Suggested flagellar knockouts are engineering hypotheses, not demonstrated range determinants. |
| **salt-in strategy → can raise → minimum NaCl requirement** | Oren reports that high-KCl organisms have acidic, salt-adapted proteomes and “generally cannot survive in low salt media”; Halobacteriaceae and *Salinibacter* require >150 g/L NaCl. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2), April 2008. (oren2008microbiallifeat pages 10-11) | Appropriate as a high-level causal model. Avoid applying the minimum requirement to all salt-in organisms without strain evidence. |

## 5. Recent developments and quantitative findings

### 5.1 Direct replacement of one osmolyte system by another

The most important 2024 result is that a genetically engineered proline module can compensate for loss of ectoine synthesis. Wild-type *H. elongata* OUT30018 was reported to grow over 0.3–21% NaCl, while the ectoine-deficient KA1 mutant failed above 4% NaCl in M63 minimal medium. HN6—`ΔectABC::proBm1AC ΔputA`—grew at 8% NaCl while accumulating 353.1 ± 40.5 µmol proline/g fresh cell weight. At 15% NaCl in rich medium, HN6 accumulated over 100-fold more proline than wild type or several controls. This establishes **osmolyte pool size and metabolic retention**, rather than a unique requirement for ectoine itself, as a manipulable determinant of high-salt growth in this strain. (khanh2024metabolicpathwayengineering pages 15-17, khanh2024metabolicpathwayengineering pages 1-2, khanh2024metabolicpathwayengineering pages 6-9)

### 5.2 Hybrid adaptation in an extreme polyextremophile

*N. thermophilus* grows under very high salinity and combines compatible-solute import/synthesis with K⁺ accumulation. The study examined 2.5, 3.7, and 4.3 M Na⁺ and reported an operational range around 2.5–5.0 M Na⁺, with optimum values in the high-molar range. ABC transporters were significantly enriched; four transcripts exceeded 100-fold induction, and 98.2% of the 109 tested co-upregulated genes agreed between transcript and protein measurements. This is strong system-level evidence that NaCl range can emerge from coordinated transport, metabolite, ion-homeostasis, energy, and proteome adaptations rather than a single “salt-tolerance gene.” (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 10-14)

### 5.3 Broad-range phenotyping plus genomic prediction

*Salinicola* sp. DM10 grew at 0–25% NaCl under the reported assay and carried predicted genes for both salt-in and salt-out strategies. However, the genomic annotations are hypotheses: no gene was disrupted to demonstrate a changed range. In a rice assay, DM10 inoculation improved shoot length, root length, and dry weight under 200 mM NaCl compared with salt treatment alone, supporting agricultural application but not proving which DM10 salt-adaptation genes caused the plant effect. DOI: [10.1007/s13205-023-03833-3](https://doi.org/10.1007/s13205-023-03833-3), published 24 November 2023. (nguyen2023draftgenomesequencing pages 1-2)

### 5.4 Salt-responsive enzyme and carbohydrate metabolism

ACP81 grew at 20% NaCl, while 6% NaCl was selected as sublethal for transcriptomics. At 6%, 932 genes were differentially expressed; stringent filtering identified 82 upregulated and 22 downregulated genes. `betB` and `gbsB` rose 76- and 81-fold, and `malL`, `celB`, and `celC` were implicated in starch/sucrose metabolism. Increased cellulase and β-amylase activities suggest opportunities for high-salt enzyme production, but the proposed glucose-mediated protection was not tested by targeted mutation or metabolite rescue. (li2024integratedgenomicsand pages 5-8, li2024integratedgenomicsand pages 1-2)

## 6. Current applications and real-world relevance

- **High-salinity biomanufacturing:** Engineered HN6 is proposed for converting saline biomass waste into proline-rich single-cell feed. High-salt fermentation can lower contamination pressure, and proline/hydroxyproline products have feed, food, cosmetic, and pharmaceutical uses. This is a development-stage application, not evidence of commercial deployment. (khanh2024metabolicpathwayengineering pages 15-17)
- **Ectoine and PHA production:** *Halomonas* chassis are used or developed for ectoine and biodegradable polyhydroxyalkanoate production. Multi-omics analysis indicates that salinity reallocates resources among ectoine synthesis, transport, motility, and butanoate/PHA metabolism, which is relevant to process optimization. (khanh2024metabolicpathwayengineering pages 1-2, park2023onlineomicsplatform pages 6-7, park2023onlineomicsplatform pages 1-2)
- **Saline agriculture:** DM10 improved rice growth metrics under 200 mM NaCl in a controlled inoculation study. ACP81 is proposed for saline-soil reclamation and enzyme production. These applications should be represented outside the core microbial NaCl-range graph unless TraitMech explicitly allows host-benefit branches. (li2024integratedgenomicsand pages 1-2, nguyen2023draftgenomesequencing pages 1-2)
- **High-salt food processing:** Salt-tolerant microbes and enzymes are relevant to fermented foods, but enzyme activity under salt and organismal growth range must remain distinct evidence types.

## 7. Recommended minimal TraitMech graph

A conservative first revision of `nacl_range_tolerance_breadth` should emphasize broadly supported physiological modules while preserving taxon-specific branches:

1. **external NaCl concentration → increases → extracellular osmolarity**
2. **increased extracellular osmolarity → causes → cellular water efflux**
3. **cellular water efflux → decreases → cytoplasmic hydration/turgor**
4. **decreased turgor → inhibits → microbial growth**
5. **K⁺ uptake → restores → osmotic balance** *(general but taxon-dependent)*
6. **compatible-solute synthesis/import → increases → intracellular compatible-solute pool**
7. **intracellular compatible-solute pool → restores → osmotic balance/turgor**
8. **restored osmotic balance → enables → growth at elevated NaCl**
9. **Na⁺/H⁺ antiport and ion transport → maintains → intracellular ion homeostasis** *(uncertain/generalized)*
10. **salt-adapted proteome/high-salt-in strategy → decreases → growth at low NaCl** *(restricted to salt-in taxa)*

The *H. elongata* intervention branch can instantiate nodes 6–8 with direct evidence:

- `ectABC deletion → decreases → ectoine accumulation`
- `ectABC deletion → decreases → growth above 4% NaCl in M63`
- `proBm1AC expression → increases → proline biosynthesis`
- `putA deletion → decreases → proline catabolism`
- `decreased proline catabolism → increases → intracellular proline`
- `increased intracellular proline → enables → growth at 8% NaCl in M63`

## 8. Claims that should not yet be curated as causal

1. **Expression alone is not causation.** Opu/ProU/Trk/NhaC, `betB/gbsB`, PTS, membrane, and flagellar responses are valuable candidates, but most 2023–2024 studies did not perturb them and remeasure NaCl endpoints.
2. **Do not convert a maximum tested positive concentration into a closed maximum** unless growth was absent at a higher adjacent concentration.
3. **Do not treat IC50 or IC25 as range limits.** They measure relative inhibition, not the presence/absence boundary for growth.
4. **Do not mix Na⁺ molarity, NaCl molarity, g/L, and % w/v.** *N. thermophilus* experiments were expressed partly as Na⁺ concentrations; conversion to NaCl is inappropriate unless medium stoichiometry is explicit.
5. **Do not generalize strain-specific engineering.** The >4% failure of KA1 and 8% growth of HN6 apply to the specified strains, M63 medium, temperature, aeration, acclimation, and endpoint.
6. **Do not infer function from gene presence.** DM10’s “salt-in and salt-out” genomic repertoire supports candidate nodes but not causal edges to its 0–25% phenotype.
7. **Do not curate flagellar knockouts as beneficial.** In *H. bluephagenesis*, they were proposed as energy-saving targets; the study did not demonstrate that they broadened NaCl range. (park2023onlineomicsplatform pages 6-7)
8. **Do not merge host salinity tolerance with microbial NaCl range.** Rice or wheat improvement after inoculation is an application phenotype, not a microbial growth-range endpoint.
9. **Avoid universalizing the two-strategy model.** The 2024 *N. thermophilus* study demonstrates that hybrid salt-in/compatible-solute strategies occur. (xing2024thepolyextremophilenatranaerobius pages 1-2)
10. **Verify all ontology and sequence identifiers before YAML insertion.** Gene symbols are taxon-dependent; exact UniProt, NCBI Gene, KEGG Orthology, Rhea, and EC accessions were not established for every strain in the retrieved evidence.

## DOI-first bibliography

1. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.** *Applied and Environmental Microbiology* 90(9). Published 19 August 2024. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 1-2)
2. Xing Q, et al. **The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.** *Applied and Environmental Microbiology* 90(5). May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
3. Li Q, Huang Z, Zhong Z, Bian F, Zhang X. **Integrated Genomics and Transcriptomics Provide Insights into Salt Stress Response in *Bacillus subtilis* ACP81.** *Microorganisms* 12:285. Published 29 January 2024. DOI: [10.3390/microorganisms12020285](https://doi.org/10.3390/microorganisms12020285). (li2024integratedgenomicsand pages 1-2)
4. Nguyen N-L, et al. **Draft genome sequencing of halotolerant bacterium *Salinicola* sp. DM10 unravels plant growth-promoting potentials.** *3 Biotech* 13:416. Published 24 November 2023. DOI: [10.1007/s13205-023-03833-3](https://doi.org/10.1007/s13205-023-03833-3). (nguyen2023draftgenomesequencing pages 1-2)
5. Park H, Faulkner M, Toogood HS, Chen G-Q, Scrutton N. **Online Omics Platform Expedites Industrial Application of *Halomonas bluephagenesis* TD1.0.** *Bioinformatics and Biology Insights* 17. 2023. DOI: [10.1177/11779322231171779](https://doi.org/10.1177/11779322231171779). (park2023onlineomicsplatform pages 1-2)
6. Rath H, et al. **Management of Osmoprotectant Uptake Hierarchy in *Bacillus subtilis* via a SigB-Dependent Antisense RNA.** *Frontiers in Microbiology* 11:622. Published 21 April 2020. DOI: [10.3389/fmicb.2020.00622](https://doi.org/10.3389/fmicb.2020.00622). (rath2020managementofosmoprotectant pages 1-2)
7. Gunde-Cimerman N, Plemenitaš A, Oren A. **Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.** *FEMS Microbiology Reviews* 42:353–375. May 2018. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). This authoritative review supports the supplied trait definition and broad osmoadaptation framework; full text was not retrieved in this run.
8. Oren A. **Microbial life at high salt concentrations: phylogenetic and metabolic diversity.** *Saline Systems* 4:2. April 2008. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2). (oren2008microbiallifeat pages 10-11, oren2008microbiallifeat pages 2-4)

**Curation priority:** implement the direct *H. elongata* intervention chain first; retain the *N. thermophilus*, ACP81, DM10, and TD1.0 findings as taxon-qualified candidate or associative edges until knockout, complementation, chemical rescue, or controlled range-shift experiments establish causality.

References

1. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

2. (khanh2024metabolicpathwayengineering pages 6-9): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

3. (nguyen2023draftgenomesequencing pages 4-5): Ngoc-Lan Nguyen, Vu Van Dung, Nguyen Van Tung, Thi Kim Lien Nguyen, Nguyen Duc Quan, Tran Thi Huong Giang, Nguyen Thi Thanh Ngan, Nguyen Thanh Hien, and Huy-Hoang Nguyen. Draft genome sequencing of halotolerant bacterium salinicola sp. dm10 unravels plant growth-promoting potentials. 3 Biotech, Nov 2023. URL: https://doi.org/10.1007/s13205-023-03833-3, doi:10.1007/s13205-023-03833-3. This article has 7 citations and is from a peer-reviewed journal.

4. (nguyen2023draftgenomesequencing pages 1-2): Ngoc-Lan Nguyen, Vu Van Dung, Nguyen Van Tung, Thi Kim Lien Nguyen, Nguyen Duc Quan, Tran Thi Huong Giang, Nguyen Thi Thanh Ngan, Nguyen Thanh Hien, and Huy-Hoang Nguyen. Draft genome sequencing of halotolerant bacterium salinicola sp. dm10 unravels plant growth-promoting potentials. 3 Biotech, Nov 2023. URL: https://doi.org/10.1007/s13205-023-03833-3, doi:10.1007/s13205-023-03833-3. This article has 7 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

6. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

7. (li2024integratedgenomicsand pages 1-2): Qiaoling Li, Zhiyuan Huang, Zheke Zhong, Fangyuan Bian, and Xiaoping Zhang. Integrated genomics and transcriptomics provide insights into salt stress response in bacillus subtilis acp81 from moso bamboo shoot (phyllostachys praecox) processing waste. Microorganisms, 12:285, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020285, doi:10.3390/microorganisms12020285. This article has 10 citations.

8. (oren2008microbiallifeat pages 2-4): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

9. (oren2008microbiallifeat pages 10-11): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

10. (rath2020managementofosmoprotectant pages 1-2): Hermann Rath, Alexander Reder, Tamara Hoffmann, Elke Hammer, Andreas Seubert, Erhard Bremer, Uwe Völker, and Ulrike Mäder. Management of osmoprotectant uptake hierarchy in bacillus subtilis via a sigb-dependent antisense rna. Frontiers in Microbiology, Apr 2020. URL: https://doi.org/10.3389/fmicb.2020.00622, doi:10.3389/fmicb.2020.00622. This article has 45 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

12. (khanh2024metabolicpathwayengineering pages 15-17): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

13. (li2024integratedgenomicsand pages 5-8): Qiaoling Li, Zhiyuan Huang, Zheke Zhong, Fangyuan Bian, and Xiaoping Zhang. Integrated genomics and transcriptomics provide insights into salt stress response in bacillus subtilis acp81 from moso bamboo shoot (phyllostachys praecox) processing waste. Microorganisms, 12:285, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020285, doi:10.3390/microorganisms12020285. This article has 10 citations.

14. (park2023onlineomicsplatform pages 6-7): Helen Park, Matthew Faulkner, Helen S Toogood, Guo-Qiang Chen, and Nigel Scrutton. Online omics platform expedites industrial application of halomonas bluephagenesis td1.0. Bioinformatics and Biology Insights, Jan 2023. URL: https://doi.org/10.1177/11779322231171779, doi:10.1177/11779322231171779. This article has 2 citations and is from a peer-reviewed journal.

15. (park2023onlineomicsplatform pages 1-2): Helen Park, Matthew Faulkner, Helen S Toogood, Guo-Qiang Chen, and Nigel Scrutton. Online omics platform expedites industrial application of halomonas bluephagenesis td1.0. Bioinformatics and Biology Insights, Jan 2023. URL: https://doi.org/10.1177/11779322231171779, doi:10.1177/11779322231171779. This article has 2 citations and is from a peer-reviewed journal.

16. (rath2020managementofosmoprotectant pages 12-14): Hermann Rath, Alexander Reder, Tamara Hoffmann, Elke Hammer, Andreas Seubert, Erhard Bremer, Uwe Völker, and Ulrike Mäder. Management of osmoprotectant uptake hierarchy in bacillus subtilis via a sigb-dependent antisense rna. Frontiers in Microbiology, Apr 2020. URL: https://doi.org/10.3389/fmicb.2020.00622, doi:10.3389/fmicb.2020.00622. This article has 45 citations and is from a peer-reviewed journal.