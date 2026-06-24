---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:34:04.497969'
end_time: '2026-06-18T03:47:45.318923'
duration_seconds: 820.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: plasmid carriage
  trait_identifier: traitmech:000090
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: plasmid_carriage
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing possession of one or more plasmids \u2014\
    \ extrachromosomal, typically circular DNA replicons that carry accessory genes\
    \ such as resistance, virulence, or metabolic functions and can transfer by conjugation."
  parent_traits: traitmech:000089
  synonyms: plasmid-bearing
  evidence_summary: 'DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility,
    classifying conjugative and mobilizable plasmids as key vectors of horizontal
    gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among
    the principal mobile genetic elements.)'
  causal_graph_summary: 'plasmid_conjugation_hgt: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plasmid carriage
- **METPO identifier:** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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
- **Trait label:** plasmid carriage
- **METPO identifier:** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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


# Research report: plasmid carriage (TraitMech: traitmech:000090)

## Executive scope summary
**Plasmid carriage** is best treated as a *state trait*—possession of one or more **extrachromosomal** DNA replicons (“plasmids”)—independent of whether the plasmid is conjugative, what cargo genes it carries, or what its copy number is. Plasmid carriage is therefore distinct from (i) **conjugation/transfer proficiency** (a process trait), (ii) a **horizontal gene transfer (HGT) event** (an event trait), and (iii) **plasmid copy number** (a quantitative trait). This separation is important for causal graph curation, because maintenance mechanisms (partition, toxin–antitoxin addiction, etc.) are causal determinants of carriage but are not part of the definition. (orlek2023factorsassociatedwith pages 1-2, tokuda2024microbialevolutionthrough pages 6-8, xue2024theevolutionarylandscape pages 6-6)

| Aspect | Included in trait? | Excluded/nearby trait | Notes | Supporting citation |
|---|---|---|---|---|
| Possession of one or more extrachromosomal plasmids | Yes | None; this is the core trait | Plasmid carriage is best scoped as the state of harboring plasmid DNA replicons, independent of what accessory genes they encode. Reviews and large-scale analyses describe plasmids as extrachromosomal DNA elements whose self-replication supports vertical inheritance. | (orlek2023factorsassociatedwith pages 1-2, xue2024theevolutionarylandscape pages 6-6) |
| Plasmid carriage regardless of mobility class | Yes | Conjugative plasmid trait; mobilizable plasmid trait | The trait should include carriage of conjugative, mobilizable, and non-mobilizable plasmids; mobility affects spread, not whether a cell is plasmid-bearing. Tokuda distinguishes conjugative and mobilizable plasmids as horizontal-transfer classes, while Orlek discusses plasmids generally as ARG carriers with multiple mobility modes. | (orlek2023factorsassociatedwith pages 1-2, tokuda2024microbialevolutionthrough pages 6-8) |
| Conjugation ability / transfer proficiency | No | Separate trait: plasmid conjugation, transfer rate, host permissiveness | A cell can carry a plasmid yet transfer it poorly or not at all. Transfer is a nearby mechanistic trait driven by tra genes, host background, and environmental conditions rather than by plasmid possession alone. | (xiang2024porindeficiencyor pages 1-2, wright2024achromosomalmutation pages 22-23) |
| Horizontal gene transfer event | No | Separate process trait: plasmid acquisition, conjugation event, transformation, transduction | Plasmid carriage is a state; HGT is an event/process that may generate that state. Tokuda treats HGT as the mechanism by which MGEs move, distinct from the resulting persistence of plasmids in hosts. | (tokuda2024microbialevolutionthrough pages 6-8) |
| Plasmid persistence / maintenance after acquisition | Partly nearby, not identical | Separate but causally upstream/downstream maintenance traits | Persistence mechanisms such as partition, addiction, or compensatory evolution are core causal graph entities for plasmid carriage, but are not identical to the trait label itself. They explain stable inheritance of the carried plasmid. | (xue2024theevolutionarylandscape pages 6-6, fraikin2024singlecellevidencefor pages 3-5, liu2024compensatoryevolutionof pages 6-6) |
| Plasmid copy number | No, as a separate quantitative trait | Separate quantitative trait: low-copy/high-copy plasmid state | Copy number modulates burden, expression, and resistance, but the presence/absence trait remains plasmid carriage. Xue and Fraikin both treat copy number as mechanistically important yet separable from whether a plasmid is present at all. | (xue2024theevolutionarylandscape pages 6-6, fraikin2024singlecellevidencefor pages 3-5) |
| Plasmid-borne ARG or virulence gene carriage | No, not required | Separate traits: ARG carriage, virulence plasmid carriage, metabolic plasmid carriage | Accessory gene content can make carriage clinically or ecologically important, but plasmid carriage does not require resistance or virulence genes. Orlek explicitly analyzes ARG carriage as a property associated with some plasmids, not all plasmids. | (orlek2023factorsassociatedwith pages 1-2) |
| Host benefit or cost from plasmid carriage | No, not definitional | Separate traits/processes: fitness cost, compensatory adaptation, co-selection | A plasmid can be beneficial, neutral, or costly depending on context. These outcomes influence maintenance but should not be collapsed into the definition of plasmid carriage. | (xue2024theevolutionarylandscape pages 6-6, xiang2024porindeficiencyor pages 1-2, liu2024compensatoryevolutionof pages 6-6) |
| Chromids / secondary chromosomes derived from plasmids | Boundary case; usually exclude unless curated explicitly as plasmid replicons | Secondary chromosome / chromid trait | Xue discusses chromosome/plasmid balance, while related genome-maintenance literature notes plasmid domestication into secondary chromosomes. Once a replicon functions as an integrated secondary chromosome/chromid rather than a dispensable plasmid, it is better treated as a distinct nearby replicon class. | (xue2024theevolutionarylandscape pages 6-6) |
| Integrated plasmids (episomes inserted into chromosome) | Usually exclude from strict plasmid carriage | Integrated mobile element / chromosomal integration trait | The definition emphasizes extrachromosomal replicons. If a plasmid is stably integrated and no longer maintained as an autonomous extrachromosomal replicon, it falls outside a strict plasmid-carriage scope. | (orlek2023factorsassociatedwith pages 1-2, xue2024theevolutionarylandscape pages 6-6) |
| Phage-plasmids / plasmid-like prophage-plasmids | Boundary case; include only if autonomously maintained as plasmid replicons | Phage carriage / prophage trait | Some elements behave both as plasmids and phages. They are relevant only when the plasmid aspect—autonomous extrachromosomal replication/segregation—is the observed property; otherwise they belong under phage-related traits. | (xue2024theevolutionarylandscape pages 6-6) |
| Restriction-modification resistance or anti-RM strategies | No, causal mechanism only | Separate mechanism trait affecting transfer success | Anti-RM genes, methylases, and recognition-site architecture affect establishment of incoming plasmids but do not define the carried state itself. They belong as graph nodes/edges, not as scope-defining criteria. | (dimitriu2024variousplasmidstrategies pages 1-2) |
| Toxin-antitoxin addiction / post-segregational killing | No, causal mechanism only | Separate maintenance mechanism trait | Fraikin shows TA systems increase vertical stability and cause damage/SOS induction after plasmid loss. These are maintenance mechanisms that support carriage rather than the trait definition. | (fraikin2024singlecellevidencefor pages 3-5, fraikin2024singlecellevidencefor pages 2-3) |
| Detection by sequencing-based assembly or read mapping | Assay/readout only | None | Genomic detection is evidence for plasmid carriage, not the trait itself. Large-scale plasmid studies such as Orlek rely on plasmid genome curation and metadata linkage to infer carriage patterns. | (orlek2023factorsassociatedwith pages 1-2, tokuda2024microbialevolutionthrough pages 6-8) |
| Detection by plasmid extraction / plasmid capture / exogenous capture | Assay/readout only | None | Experimental recovery of a plasmid indicates carriage or transferability, but method-specific recovery biases exist; Tokuda notes exogenous capture only recovers plasmids able to replicate in the recipient. | (tokuda2024microbialevolutionthrough pages 6-8) |
| Detection by fluorescence foci (e.g., SopB-mNeonGreen mini-F tracking) | Assay/readout only | None | Fluorescent partition foci are a direct single-cell assay for plasmid localization/segregation and loss, but they should be modeled as evidence channels rather than as the trait. | (fraikin2024singlecellevidencefor pages 3-5, fraikin2024singlecellevidencefor media be7de704) |


*Table: This table defines the scope of the plasmid carriage trait and separates it from nearby traits such as conjugation, HGT events, copy number, and maintenance mechanisms. It also marks important biological boundary cases and assay-specific readouts relevant for TraitMech curation.*

## 1) Key concepts and definitions (current understanding)

### 1.1 Definitions relevant to plasmid carriage
- **Plasmids** are extrachromosomal DNA elements that **control self-replication** to maintain a stable copy number, enabling vertical inheritance while also potentially enabling horizontal spread depending on mobility class. This “self-replication to maintain a stable copy number” is a central mechanistic anchor that differentiates plasmids from transient DNA uptake. (orlek2023factorsassociatedwith pages 1-2)
- **Mobility classes** (conjugative/mobilizable/non-mobilizable) affect *spread* but not whether a cell is plasmid-bearing; thus they should be modeled as causal graph context variables or separate traits rather than defining plasmid carriage. (orlek2023factorsassociatedwith pages 1-2, tokuda2024microbialevolutionthrough pages 6-8)

### 1.2 Boundary cases that require explicit curation policy
- **Chromids/secondary chromosomes** (plasmid-derived replicons domesticated into chromosome-like essential replicons) are a boundary case. For strict plasmid carriage, these are typically excluded unless TraitMech explicitly models them as plasmid replicons; the chromosome/plasmid balance literature treats them as part of a broader chromosome–plasmid interplay rather than simple plasmid presence/absence. (xue2024theevolutionarylandscape pages 6-6)
- **Integrated plasmids** (no longer maintained as autonomous extrachromosomal replicons) are typically excluded from strict plasmid-carriage scope. (orlek2023factorsassociatedwith pages 1-2, xue2024theevolutionarylandscape pages 6-6)
- **Phage-plasmid hybrids** may be included only if the *autonomous plasmid-replicon state* is the curated observation; otherwise they belong to phage/prophage traits. (xue2024theevolutionarylandscape pages 6-6)

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Single-cell mechanistic confirmation of toxin–antitoxin “addiction” and SOS response after plasmid loss (2024)
A key recent development is **direct single-cell observation** of post-segregational effects supporting the plasmid addiction model. Fraikin & Van Melderen (Jan 2024) tracked a mini-F plasmid using fluorescently labeled partition complexes and quantified outcomes after loss of a ccdAB-encoding plasmid. They report:
- The mini-F replicon is maintained at **~two copies per chromosome equivalent** and is actively segregated by the **SopABC** partition system. (fraikin2024singlecellevidencefor pages 3-5)
- **Bulk plasmid loss rate** in this system was **0.09% per generation**. (fraikin2024singlecellevidencefor pages 3-5)
- Loss of a **ccdAB** plasmid triggers **DNA damage hallmarks and SOS induction** (reported by a *sulA* transcriptional reporter), accompanied by **filamentation**; median cell length reached **7 μm after 5 h** versus **2 μm** after empty-plasmid loss. (fraikin2024singlecellevidencefor pages 3-5)
These results are important for TraitMech because they validate an often-assumed edge: *plasmid loss → toxin activation → DNA damage/SOS response → growth arrest/filamentation → increased effective plasmid stability at the population level*. (fraikin2024singlecellevidencefor pages 3-5)

**Visual evidence (figure panels)** supporting the above is available from the same paper, including the SopB-foci tracking schematic/time-lapse and quantitative SOS/cell-length plots. (fraikin2024singlecellevidencefor media be7de704, fraikin2024singlecellevidencefor media e0eb2b9c, fraikin2024singlecellevidencefor media 18e6fdb1, fraikin2024singlecellevidencefor media 7bfc9856, fraikin2024singlecellevidencefor media 700da9e2)

### 2.2 Quantitative evaluation of restriction–modification (RM) barriers and common plasmid counter-strategies (2024)
Dimitriu et al. (Oct 2024) directly quantify the ability of bacterial **RM systems** to block conjugative plasmid transfer and highlight plasmid traits that mitigate restriction:
- Testing **10 RM systems** against **13 natural plasmids** in *E. coli*, defence ranged from **none to 10^5-fold reduction in transfer**, showing that the barrier is **highly variable** and depends on plasmid–RM pairing. (dimitriu2024variousplasmidstrategies pages 1-2)
- Mechanistic correlates include: (i) **more RM recognition sites on plasmids correlate with stronger defence**, (ii) **plasmid-encoded methylases** that protect incoming plasmid DNA, and (iii) **plasmid anti-restriction genes** that protect against multiple RM types. (dimitriu2024variousplasmidstrategies pages 1-2)
- RM systems are highly prevalent, reported as **>2 RM systems per genome on average**, affecting the baseline probability that an incoming plasmid becomes established (and thus becomes “carried”). (dimitriu2024variousplasmidstrategies pages 1-2)

### 2.3 Copy-number evolution and antibiotic-driven selection during plasmid establishment (2024)
A recurring theme in 2024 studies is **adaptive modulation of plasmid copy number** and plasmid region architecture under antibiotic pressure:
- Xiang et al. (May 2024) evolved *E. coli* carrying an IncX3 **blaNDM-5** plasmid under meropenem pressure, identifying a **repA D140Y** mutation linked to **increased plasmid copy number**, with associated **increased MIC** and **higher conjugation frequency** under specific sub-MIC conditions. (xiang2024porindeficiencyor pages 1-2)
- Cheng et al. (Nov 2024) experimentally evolved a large IncHI2 MDR plasmid in *Salmonella* across ~600 generations under different antibiotic regimes and found that modifications in MDR/transfer regions can **mitigate fitness cost and enhance maintenance**; selection could **maintain/amplify** ARGs and **co-select** nearby ARGs, while other drug regimens promoted **loss of the MDR region**. (cheng2024evolutionandmaintenance pages 1-2)

### 2.4 Compensatory evolution as a general solution to plasmid fitness costs (2024)
The persistence of plasmids despite fitness burdens is a major unresolved problem (“plasmid paradox” framing). A recent review (Liu et al., Aug 2024) synthesizes mechanisms by which **chromosomal and plasmid mutations** counteract the **plasmid fitness cost**, supporting explicit causal graph edges from compensatory evolution to carriage/persistence. (liu2024compensatoryevolutionof pages 6-6)

## 3) Current applications and real-world implementations

### 3.1 Clinical and One-Health antimicrobial resistance (AMR) surveillance and risk assessment
- Large-scale plasmid-genome curation can quantify AMR patterns across sources and time. Orlek et al. (Feb 2023) curated **>14,000 plasmid genomes** and modeled ARG carriage versus metadata, reporting pronounced source differences consistent with antibiotic selection: e.g., **carbapenem resistance genes on 12% of human plasmids vs 0.42% of livestock plasmids**, and tetracycline resistance enriched in livestock plasmids. (orlek2023factorsassociatedwith pages 1-2)
- These analyses support real-world implementation in AMR surveillance pipelines: plasmid carriage (and plasmid-borne ARG carriage) is routinely inferred from sequencing/assembly and linked to epidemiological metadata, although the assay is distinct from the trait itself. (orlek2023factorsassociatedwith pages 1-2)

### 3.2 Predicting and controlling plasmid establishment: leveraging barriers and counter-barriers
- RM systems can produce up to **10^5-fold** reduction in plasmid transfer in some pairings, but plasmids frequently encode methylases and anti-restriction genes; therefore, predicting plasmid carriage in microbial communities requires modeling both defence system prevalence and plasmid countermeasures. (dimitriu2024variousplasmidstrategies pages 1-2)

## 4) Expert opinions and authoritative analyses (mechanistic framing)

### 4.1 Multi-level selection and the chromosome/plasmid balance
A recent conceptual synthesis models plasmid carriage as emerging from competing selection pressures (vertical vs horizontal transmission; phenotypic vs non-phenotypic selection) and emphasizes that plasmids can persist by encoding addiction systems and by modulating costs. This supports curating high-level edges like “plasmid carriage imposes resource competition costs” and “maintenance strategies (conjugation, addiction) relax selection against plasmids.” (xue2024theevolutionarylandscape pages 6-6)

### 4.2 Compensatory evolution as a curation-relevant mechanism class
The compensatory evolution literature supports modeling “compensatory mutation(s)” as a mechanistic node class that reduces the fitness cost of plasmid carriage, thus increasing long-term persistence and prevalence of plasmid-bearing cells. (liu2024compensatoryevolutionof pages 6-6, wright2024achromosomalmutation pages 21-22)

## 5) Relevant statistics and data points (recent studies)
- **0.09% plasmid loss per generation** measured for a trackable mini-F plasmid system (single-cell study context). (fraikin2024singlecellevidencefor pages 3-5)
- **SOS/filamentation quantitative phenotype** after ccdAB plasmid loss: median cell length **7 μm** after 5 h vs **2 μm** for empty-plasmid loss. (fraikin2024singlecellevidencefor pages 3-5)
- **RM barrier magnitude**: **none to 10^5-fold** reduction in conjugative transfer across tested RM–plasmid combinations. (dimitriu2024variousplasmidstrategies pages 1-2)
- **RM prevalence**: **>2 RM systems per genome on average**. (dimitriu2024variousplasmidstrategies pages 1-2)
- **AMR surveillance statistic**: among curated plasmid genomes, **carbapenem resistance carriage 12% (human) vs 0.42% (livestock)** in Orlek et al.’s dataset. (orlek2023factorsassociatedwith pages 1-2)

## Curation-focused content for `plasmid_carriage.yaml`

### Candidate nodes grouped by type (curation-oriented)
**A. Biological processes / functions (GO candidates)**
- SOS response (GO:0009432) (fraikin2024singlecellevidencefor pages 3-5)
- DNA damage response (GO candidate; label-only grounded pending) (fraikin2024singlecellevidencefor pages 3-5)
- Plasmid partition/segregation (GO candidate; label-only) (fraikin2024singlecellevidencefor pages 3-5)
- Conjugative transfer / bacterial conjugation (GO candidate; label-only) (dimitriu2024variousplasmidstrategies pages 1-2)
- Restriction–modification system activity (GO candidate; label-only) (dimitriu2024variousplasmidstrategies pages 1-2)

**B. Genes/proteins/complexes (labels; grounding pending unless curated per plasmid family)**
- SopA (ATPase), SopB (centromere-binding), sopC (centromeric repeats) — mini-F sopABC partition system (fraikin2024singlecellevidencefor pages 3-5)
- ccdAB toxin–antitoxin system (ccdA antitoxin, ccdB toxin) (fraikin2024singlecellevidencefor pages 3-5, fraikin2024singlecellevidencefor pages 2-3)
- repA (plasmid replication initiation; IncX3 system example) (xiang2024porindeficiencyor pages 1-2)
- arcA (host regulator; plasmid persistence modifier in *Salmonella* IncHI2 example) (cheng2024evolutionandmaintenance pages 1-2)
- Plasmid methylases (label-only; plasmid-encoded) (dimitriu2024variousplasmidstrategies pages 1-2)
- Plasmid anti-restriction genes (label-only) (dimitriu2024variousplasmidstrategies pages 1-2)

**C. Environmental/experimental factors (ENVO/CHEBI suggestions)**
- Antibiotic exposure / selection (CHEBI: antibiotic [broad class]; ENVO: hospital/clinical environment as context where applicable) (xiang2024porindeficiencyor pages 1-2, cheng2024evolutionandmaintenance pages 1-2, orlek2023factorsassociatedwith pages 1-2)
- Restriction–modification genotype of host population (context variable; no single CURIE) (dimitriu2024variousplasmidstrategies pages 1-2)

### Evidence-backed candidate causal edges (triple table)
| Subject (label + CURIE if known) | Predicate | Object (label + CURIE if known) | Evidence snippet (verbatim/near-verbatim) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| SopABC partition system (label-only; candidate GO: plasmid partitioning) | enables | faithful plasmid segregation (GO candidate) | “the mini-F replicon is maintained at two copies per chromosome equivalent and is actively segregated by the sopABC partition system” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong but mini-F / *E. coli* system-specific. |
| SopB protein (label-only) | binds | sopC centromere-like repeats (label-only) | “SopB binds sopC centromeric repeats to form partition complexes” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong; grounded labels only. Mini-F specific. |
| SopA ATPase (label-only) | drives | segregation of partition complexes (GO candidate) | “partition complexes that are segregated through the ATPase activity of SopA” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong; mini-F specific. |
| SopB–sopC partition complex (label-only) | forms | fluorescent foci / trackable plasmid localization (assay phenotype) | “The authors fused SopB to mNeonGreen to visualize partition complexes as fluorescent foci for tracking plasmid localization” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Assay-specific; useful as experimental node, not core mechanism. |
| Plasmid loss (GO candidate: plasmid loss) | has rate | 0.09% per generation (measurement) | “Bulk plasmid loss rate was measured at 0.09% per generation” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Measurement from mini-F system; context-specific statistic. |
| ccdAB toxin–antitoxin system (label-only) | stabilizes | plasmid vertical inheritance / plasmid addiction (label-only) | “TA systems are small selfish genetic modules that increase vertical stability of their replicons” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Broad claim for TA systems; applies beyond ccdAB. |
| Plasmid loss of ccd-encoding plasmid (GO candidate) | induces | DNA damage response (GO: DNA damage response candidate) | “loss of a ccd-encoding plasmid triggered DNA damage” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong; mechanism shown at single-cell level; ccd model system. |
| Plasmid loss of ccd-encoding plasmid (GO candidate) | induces | SOS response (GO:0009432) | “loss of a ccd-encoding plasmid triggered DNA damage and induction of the SOS response” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong; ccd system-specific. |
| sulA-bfp reporter (assay node) | reports | SOS response (GO:0009432) | “reported by a sulA-bfp transcriptional reporter” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Assay-specific edge; useful to capture evidence provenance. |
| SOS induction after ccd plasmid loss (GO:0009432) | causes/associated with | filamentation (cell morphology phenotype) | “A gradual increase in BFP fluorescence was observed ~2 h after plasmid loss, accompanied by filamentation” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Association in same cells; causal direction plausible but still assay-contextual. |
| ccd-triggered intoxication (label-only) | increases | cell length to median 7 μm after 5 h | “median cell length reached 7 μm after 5 h versus 2 μm for empty-plasmid loss” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Quantitative phenotype; specific to experimental setup. |
| ccdAB system (label-only) | does not prevent | plasmid missegregation (label-only) | “The data show ccd does not prevent missegregation but activates post-segregational killing” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Important boundary case: addiction is distinct from partition. |
| ccdAB system (label-only) | activates | post-segregational killing (label-only) | “ccd does not prevent missegregation but activates post-segregational killing” (fraikin2024singlecellevidencefor pages 3-5) | 10.1093/nar/gkae018, 2024, https://doi.org/10.1093/nar/gkae018 | Strong; model-system specific but canonical. |
| Restriction–modification systems (GO candidate: restriction-modification system) | reduce | conjugative plasmid transfer (GO:0000746 candidate) | “observed a wide range of defence—‘none to 10^5-fold’ reduction in transfer” (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Strong quantitative evidence from *E. coli* test panel; plasmid/RM pair dependent. |
| Restriction–modification recognition site count on plasmid (label-only) | positively correlates with | defence strength against plasmid transfer (label-only) | “the number of RM recognition sites correlating with defence strength” (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Correlative; not a direct manipulation of site count in all cases. |
| Plasmid-encoded methylase (molecular function candidate) | protects | incoming plasmid DNA from restriction (GO candidate) | “plasmid-encoded methylases that protect plasmids from restriction” (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Strong general mechanism; specific methylases not named here. |
| Plasmid-encoded anti-restriction genes (label-only) | protect against | multiple RM system types (label-only) | “plasmid-encoded anti-restriction genes that protect against multiple RM types” (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Strong; specific anti-RM genes not named in snippet. |
| RM systems (GO candidate) | occur at average frequency of | >2 RM systems per genome | “RM systems are highly prevalent (on average >2 RM systems per genome)” (dimitriu2024variousplasmidstrategies pages 1-2) | 10.1093/nar/gkae896, 2024, https://doi.org/10.1093/nar/gkae896 | Background statistic; not itself a causal edge, but relevant ecosystem parameter. |
| repA D140Y mutation (label-only) | increases | plasmid copy number (label-only) | “repA D140Y mutation produced increased copy number” (xiang2024porindeficiencyor pages 1-2) | 10.1080/22221751.2024.2352432, 2024, https://doi.org/10.1080/22221751.2024.2352432 | Strong within IncX3 blaNDM-5 plasmid in *E. coli* evolution experiment. |
| Increased plasmid copy number (label-only) | increases | antibiotic MIC / resistance level (label-only) | “The increased copy number of blaNDM-5 mediated its resistance to cefiderocol” (xiang2024porindeficiencyor pages 1-2) | 10.1080/22221751.2024.2352432, 2024, https://doi.org/10.1080/22221751.2024.2352432 | Strong but ARG/plasmid-specific. |
| Increased plasmid copy number (label-only) | increases | conjugation frequency (label-only) | “all four clones displayed four-fold increase in MIC and higher conjugation frequency… attributing to increasing plasmid copy number” (xiang2024porindeficiencyor pages 1-2) | 10.1080/22221751.2024.2352432, 2024, https://doi.org/10.1080/22221751.2024.2352432 | Strong but specific to evolved IncX3 system under meropenem pressure. |
| Antibiotic selective pressure (CHEBI candidate: antibiotic) | promotes retention of | resistance plasmids / plasmid carriage (traitmech:000090) | “without selection plasmids tend to be lost, whereas antibiotic (or metal) selective pressure promotes retention” (xiang2024porindeficiencyor pages 1-2) | 10.1080/22221751.2024.2352432, 2024, https://doi.org/10.1080/22221751.2024.2352432 | Broad principle supported here and elsewhere; environmental-context edge. |
| Drug selection (antibiotic exposure) | maintains/amplifies | plasmid-encoded ARGs (label-only) | “drug selection was able to maintain and even amplify the corresponding plasmid-encoded ARGs” (cheng2024evolutionandmaintenance pages 1-2) | 10.1128/msystems.01197-24, 2024, https://doi.org/10.1128/msystems.01197-24 | Strong in IncHI2 MDR plasmid evolution experiment. |
| Drug selection (antibiotic exposure) | co-selects | adjacent ARGs in neighboring plasmid regions (label-only) | “with co-selection of ARGs in the adjacent regions” (cheng2024evolutionandmaintenance pages 1-2) | 10.1128/msystems.01197-24, 2024, https://doi.org/10.1128/msystems.01197-24 | Strong in that experimental system; genomic-context specific. |
| Deletions in plasmid MDR and conjugation transfer regions (label-only) | mitigate | fitness cost of plasmid carriage (label-only) | “modifications to MDR and transfer regions could ‘mitigate the fitness cost of plasmid carriage’” (cheng2024evolutionandmaintenance pages 1-2) | 10.1128/msystems.01197-24, 2024, https://doi.org/10.1128/msystems.01197-24 | Strong in evolved IncHI2 plasmid; deletion outcomes may differ across plasmids. |
| Deletions in plasmid MDR and conjugation transfer regions (label-only) | enhance | plasmid maintenance (label-only) | “modifications to MDR and transfer regions could mitigate the fitness cost of plasmid carriage and enhance plasmid maintenance” (cheng2024evolutionandmaintenance pages 1-2) | 10.1128/msystems.01197-24, 2024, https://doi.org/10.1128/msystems.01197-24 | Strong but experimental-evolution specific. |
| arcA inactivation / arcA deletion (label-only; gene symbol) | improves | plasmid persistence without drugs (label-only) | “arcA deletion improved the persistence of pJXP9 plasmid without drugs” (cheng2024evolutionandmaintenance pages 1-2) | 10.1128/msystems.01197-24, 2024, https://doi.org/10.1128/msystems.01197-24 | Strong, host- and plasmid-specific (*Salmonella* IncHI2 pJXP9). |
| Plasmid carriage (traitmech:000090) | imposes | fitness cost / additional material and energy consumption (label-only) | “Plasmid carriage imposes fitness costs (‘additional material and energy consumption’)” (xiang2024porindeficiencyor pages 1-2) | 10.1080/22221751.2024.2352432, 2024, https://doi.org/10.1080/22221751.2024.2352432 | Broad mechanistic claim; suitable high-level edge. |
| Compensatory mutations (GO candidate: compensatory evolution) | reduce | plasmid fitness cost (label-only) | “Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost” (liu2024compensatoryevolutionof pages 6-6) | 10.1002/ece3.70121, 2024, https://doi.org/10.1002/ece3.70121 | Broad review-level claim; strong as synthesis, but generic. |
| Compensatory mutations (chromosomal or plasmid) | increase | host permissiveness / plasmid survival (label-only) | “compensatory mutations… can rapidly ameliorate costs and increase host permissiveness to resistance plasmids, promoting plasmid survival” (wright2024achromosomalmutation pages 21-22) | 10.1371/journal.pbio.3002926, 2024, https://doi.org/10.1371/journal.pbio.3002926 | Synthesis claim from cited literature in discussion; may be better as secondary-support edge. |


*Table: This table lists candidate subject-predicate-object edges for a TraitMech causal graph of plasmid carriage, with supporting snippets, references, and notes about specificity or uncertainty. It emphasizes experimentally supported maintenance, segregation, addiction, transfer-barrier, selection, and compensatory-evolution mechanisms.*

## Warnings / claims that should not yet be curated (or should be curated as uncertain)
1. **Taxon- and plasmid-family specificity**: SopABC partition and the mini-F copy-number values (e.g., ~2 copies per chromosome; 0.09% loss/generation) are strong but primarily represent a *mini-F/*E. coli* model; these should be curated with explicit context (e.g., “F-like plasmids / low-copy plasmids with Sop/Par systems”). (fraikin2024singlecellevidencefor pages 3-5)
2. **Assay artifacts**: Reporter constructs (e.g., SopB-mNeonGreen foci; sulA-bfp SOS reporter) should be represented as evidence channels rather than generalizable biological nodes unless TraitMech models experimental factors explicitly. (fraikin2024singlecellevidencefor pages 3-5)
3. **Copy-number and resistance coupling**: The edge “repA mutation → copy number → increased MIC” is well supported in a specific IncX3 blaNDM-5 system under defined meropenem selection conditions; curate as context-specific (plasmid replicon type, host, antibiotic regimen). (xiang2024porindeficiencyor pages 1-2)
4. **RM-barrier generalization**: Dimitriu et al. show barrier strength varies from none to 10^5-fold depending on RM–plasmid pairing; thus any single edge “RM blocks conjugation” should be annotated with high variability and dependence on recognition sites and plasmid countermeasures. (dimitriu2024variousplasmidstrategies pages 1-2)

## DOI-first bibliography (with publication dates and URLs)
1. Fraikin N, Van Melderen L. **Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems.** *Nucleic Acids Research* (Jan 2024). DOI: **10.1093/nar/gkae018**. URL: https://doi.org/10.1093/nar/gkae018 (fraikin2024singlecellevidencefor pages 3-5)
2. Dimitriu T, Szczelkun MD, Westra ER. **Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation.** *Nucleic Acids Research* (Oct 2024). DOI: **10.1093/nar/gkae896**. URL: https://doi.org/10.1093/nar/gkae896 (dimitriu2024variousplasmidstrategies pages 1-2)
3. Xiang G, Zhao Z, Zhang S, et al. **Porin deficiency or plasmid copy number increase mediated carbapenem-resistant *Escherichia coli* resistance evolution.** *Emerging Microbes & Infections* (May 2024). DOI: **10.1080/22221751.2024.2352432**. URL: https://doi.org/10.1080/22221751.2024.2352432 (xiang2024porindeficiencyor pages 1-2)
4. Cheng M, Dai J-J, Zhang J-F, et al. **Evolution and maintenance of a large multidrug-resistant plasmid in a *Salmonella enterica* Typhimurium host under differing antibiotic selection pressures.** *mSystems* (Nov 2024). DOI: **10.1128/msystems.01197-24**. URL: https://doi.org/10.1128/msystems.01197-24 (cheng2024evolutionandmaintenance pages 1-2)
5. Liu Z, Zhao Q, Xu C, Song H. **Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost.** *Ecology and Evolution* (Aug 2024). DOI: **10.1002/ece3.70121**. URL: https://doi.org/10.1002/ece3.70121 (liu2024compensatoryevolutionof pages 6-6)
6. Xue W, Hong J, Wang T. **The evolutionary landscape of prokaryotic chromosome/plasmid balance.** *Communications Biology* (Nov 2024). DOI: **10.1038/s42003-024-07167-5**. URL: https://doi.org/10.1038/s42003-024-07167-5 (xue2024theevolutionarylandscape pages 6-6)
7. Tokuda M, Shintani M. **Microbial evolution through horizontal gene transfer by mobile genetic elements.** *Microbial Biotechnology* (Jan 2024). DOI: **10.1111/1751-7915.14408**. URL: https://doi.org/10.1111/1751-7915.14408 (tokuda2024microbialevolutionthrough pages 6-8)
8. Orlek A, Anjum M, Mather A, Stoesser N, Walker S. **Factors associated with plasmid antibiotic resistance gene carriage revealed using large-scale multivariable analysis.** *Scientific Reports* (Feb 2023). DOI: **10.1038/s41598-023-29530-y**. URL: https://doi.org/10.1038/s41598-023-29530-y (orlek2023factorsassociatedwith pages 1-2)
9. Wright RCT, Wood AJ, Bottery MJ, et al. **A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation.** *PLOS Biology* (Dec 2024). DOI: **10.1371/journal.pbio.3002926**. URL: https://doi.org/10.1371/journal.pbio.3002926 (wright2024achromosomalmutation pages 22-23, wright2024achromosomalmutation pages 21-22)


References

1. (orlek2023factorsassociatedwith pages 1-2): Alex Orlek, Muna Anjum, Alison Mather, Nicole Stoesser, and Sarah Walker. Factors associated with plasmid antibiotic resistance gene carriage revealed using large-scale multivariable analysis. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29530-y, doi:10.1038/s41598-023-29530-y. This article has 48 citations and is from a peer-reviewed journal.

2. (tokuda2024microbialevolutionthrough pages 6-8): Maho Tokuda and Masaki Shintani. Microbial evolution through horizontal gene transfer by mobile genetic elements. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14408, doi:10.1111/1751-7915.14408. This article has 242 citations and is from a peer-reviewed journal.

3. (xue2024theevolutionarylandscape pages 6-6): Wenzhi Xue, Juken Hong, and Teng Wang. The evolutionary landscape of prokaryotic chromosome/plasmid balance. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07167-5, doi:10.1038/s42003-024-07167-5. This article has 10 citations and is from a peer-reviewed journal.

4. (xiang2024porindeficiencyor pages 1-2): Guoxiu Xiang, Zhiwei Zhao, Shebin Zhang, Yimei Cai, Yuting He, Jian-Ming Zeng, Cha Chen, and Bin Huang. Porin deficiency or plasmid copy number increase mediated carbapenem-resistant <i>escherichia coli</i> resistance evolution. Emerging Microbes &amp; Infections, May 2024. URL: https://doi.org/10.1080/22221751.2024.2352432, doi:10.1080/22221751.2024.2352432. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (wright2024achromosomalmutation pages 22-23): Rosanna C. T. Wright, A. Jamie Wood, Michael J. Bottery, Katie J. Muddiman, Steve Paterson, Ellie Harrison, Michael A. Brockhurst, and James P. J. Hall. A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation. PLOS Biology, 22:e3002926, Dec 2024. URL: https://doi.org/10.1371/journal.pbio.3002926, doi:10.1371/journal.pbio.3002926. This article has 21 citations and is from a highest quality peer-reviewed journal.

6. (fraikin2024singlecellevidencefor pages 3-5): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

7. (liu2024compensatoryevolutionof pages 6-6): Ziyi Liu, Qiuyun Zhao, Chenggang Xu, and Houhui Song. Compensatory evolution of chromosomes and plasmids counteracts the plasmid fitness cost. Ecology and Evolution, Aug 2024. URL: https://doi.org/10.1002/ece3.70121, doi:10.1002/ece3.70121. This article has 20 citations and is from a peer-reviewed journal.

8. (dimitriu2024variousplasmidstrategies pages 1-2): Tatiana Dimitriu, Mark D Szczelkun, and Edze R Westra. Various plasmid strategies limit the effect of bacterial restriction–modification systems against conjugation. Nucleic Acids Research, 52:12976-12986, Oct 2024. URL: https://doi.org/10.1093/nar/gkae896, doi:10.1093/nar/gkae896. This article has 41 citations and is from a highest quality peer-reviewed journal.

9. (fraikin2024singlecellevidencefor pages 2-3): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

10. (fraikin2024singlecellevidencefor media be7de704): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

11. (fraikin2024singlecellevidencefor media e0eb2b9c): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

12. (fraikin2024singlecellevidencefor media 18e6fdb1): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

13. (fraikin2024singlecellevidencefor media 7bfc9856): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

14. (fraikin2024singlecellevidencefor media 700da9e2): Nathan Fraikin and Laurence Van Melderen. Single-cell evidence for plasmid addiction mediated by toxin–antitoxin systems. Nucleic Acids Research, 52:1847-1859, Jan 2024. URL: https://doi.org/10.1093/nar/gkae018, doi:10.1093/nar/gkae018. This article has 30 citations and is from a highest quality peer-reviewed journal.

15. (cheng2024evolutionandmaintenance pages 1-2): Ming Cheng, Jing-Jing Dai, Jin-Fei Zhang, Yu-Ting Su, Si-Qi Guo, Ruan-Yang Sun, Dong Wang, Jian Sun, Xiao-Ping Liao, Sheng Chen, and Liang-Xing Fang. Evolution and maintenance of a large multidrug-resistant plasmid in a <i>salmonella enterica</i> typhimurium host under differing antibiotic selection pressures. Nov 2024. URL: https://doi.org/10.1128/msystems.01197-24, doi:10.1128/msystems.01197-24. This article has 8 citations and is from a peer-reviewed journal.

16. (wright2024achromosomalmutation pages 21-22): Rosanna C. T. Wright, A. Jamie Wood, Michael J. Bottery, Katie J. Muddiman, Steve Paterson, Ellie Harrison, Michael A. Brockhurst, and James P. J. Hall. A chromosomal mutation is superior to a plasmid-encoded mutation for plasmid fitness cost compensation. PLOS Biology, 22:e3002926, Dec 2024. URL: https://doi.org/10.1371/journal.pbio.3002926, doi:10.1371/journal.pbio.3002926. This article has 21 citations and is from a highest quality peer-reviewed journal.