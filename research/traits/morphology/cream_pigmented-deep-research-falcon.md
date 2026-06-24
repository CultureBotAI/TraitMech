---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:20:18.289180'
end_time: '2026-06-18T07:36:36.386825'
duration_seconds: 978.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cream pigmented
  trait_identifier: METPO:1003024
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cream_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which colony or cell coloration is a pale,
    off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing
    pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_cream
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid
    pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the
    basis for cream/pale coloration in many bacterial taxa.)'
  causal_graph_summary: 'cream_pigmented_low_carotenoid_density: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cream pigmented
- **METPO identifier:** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cream pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cream_pigmented.yaml`.

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
- **Trait label:** cream pigmented
- **METPO identifier:** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cream pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cream_pigmented.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **cream pigmented** (METPO:1003024)

## Scope summary (TraitMech curation)
**Trait:** *cream pigmented* (METPO:1003024) refers to colony/cell coloration that is pale off-white/cream. Mechanistically, available evidence supports modeling this phenotype primarily as **reduced abundance of light-absorbing pigments**, most often **carotenoids**, rather than the presence of a distinct “cream pigment.” In a recent genetic screen in photochromogenic *Mycobacterium kansasii*, mutants that “failed to develop pigmentation upon light treatment” retained an **“off-white appearance” (WW phenotype)**, and the causal insertions clustered strongly in a **carotenoid biosynthesis (CRT) locus** (janisch2023geneticunderpinningsof pages 4-5). This supports a general causal hypothesis for the trait: **low carotenoid output** (due to biosynthetic gene disruption, regulatory repression, limited precursor supply, or increased degradation) → **cream/off-white appearance**.

### Boundary cases and distinctions
* **Cream vs white/non-pigmented:** “cream” is best treated as a **low-pigment-intensity** state; some assays use “white/off-white” categories (WW) that may conflate cream and fully colorless phenotypes (janisch2023geneticunderpinningsof pages 4-5).
* **Cream vs yellow/orange:** yellow/orange indicates **higher carotenoid accumulation**; in *M. kansasii* and a heterologous *M. smegmatis* transformant, colonies were off-white in the dark but became yellow after light exposure, illustrating **environment-dependent** pigmentation (photochromogenicity) rather than a constitutive cream trait (janisch2023geneticunderpinningsof pages 10-12).
* **Cream vs red/orange from pathway intermediates:** accumulation of carotenoid intermediates (e.g., lycopene) can shift color toward red/orange; this should be curated as a different pigmentation state than cream (janisch2023geneticunderpinningsof pages 10-12).

## Key concepts and current mechanistic understanding
### 1) “Low carotenoid abundance” as a mechanistic intermediate
The most directly supported mechanistic intermediate is **reduced carotenoid biosynthetic flux**. In *M. kansasii*, WW mutants were enriched for insertions in carotenoid biosynthesis genes organized like an operon (crtE, crtI, crtB, crtYc, crtYd) involved in β-carotene synthesis (janisch2023geneticunderpinningsof pages 4-5). In *Corynebacterium glutamicum*, targeted CRISPRi repression of upstream precursor supply (MEP pathway) and crt operon genes significantly reduced the cellular content of the native carotenoid decaprenoxanthin, consistent with visibly reduced pigmentation (gottl2021crisprilibraryguidedtargetidentification pages 8-10).

### 2) Regulatory repression and environmental control
In photochromogenic *M. kansasii*, the MarR-family regulator **CrtR** functions as a key controller of pigment production. **Tn-driven crtR overexpression (~10-fold)** was associated with WW colonies and **crtE downregulation by ≥500-fold under light**, interpreted as “shut down” of pigment production despite light exposure (janisch2023geneticunderpinningsof pages 10-12). Light itself is thus an important environmental node: the CRT locus confers photochromogenicity such that colonies are off-white in the dark but yellow after light (janisch2023geneticunderpinningsof pages 10-12). This is a crucial boundary-case mechanism: an organism can be “cream/off-white” only under specific conditions.

### 3) Pigment loss via degradation (proposed)
Beyond reduced synthesis, pigment can be diminished by increased degradation. In *M. kansasii*, the authors propose that upregulation of a carotenoid cleavage oxygenase (Cco1Mk) can drive carotene degradation and prevent pigment accumulation; this is tied to loss of its regulator ccoRMk and **~100-fold upregulation** of cco1Mk with loss of light-induced pigmentation (janisch2023geneticunderpinningsof pages 17-19). This edge is plausible but should be curated as **uncertain/inferred** because the degradation pathway is proposed rather than directly biochemically demonstrated in the excerpts.

## Recent developments and latest research (prioritizing 2023–2024)
### High-resolution genotype–phenotype mapping of off-white pigmentation (2023)
Janisch et al. (2023) performed a large transposon-mutant screen in *M. kansasii* and classified pigmentation phenotypes into groups including WW (off-white) (janisch2023geneticunderpinningsof pages 4-5). Key quantitative takeaways useful for curation/statistics:
* Screen output: **204 pigmentation mutants** (reported **0.14% mutant isolation rate**) (janisch2023geneticunderpinningsof pages 4-5).
* In the robust second screen phase: **98/121 mutants (81%)** retained an **off-white (WW)** appearance after light treatment (janisch2023geneticunderpinningsof pages 4-5).
* Insertions mapped predominantly to three loci, including a **carotenoid biosynthesis (CRT) locus**, directly tying off-white phenotype to carotenoid genes (janisch2023geneticunderpinningsof pages 4-5).

### Regulatory balance quantified (2023)
CrtR-mediated repression was quantified by RT-qPCR: Tn-driven crtR overexpression increased crtR ~10-fold and reduced crtE (reporter) by ≥500-fold under light, consistent with persistent WW phenotype (janisch2023geneticunderpinningsof pages 10-12). These are unusually strong regulatory effects that justify explicit graph edges for **transcriptional repression → reduced carotenoid biosynthesis → off-white phenotype**.

### 2024 context (limited in retrieved evidence)
Within the retrieved corpus for this run, the most direct trait-relevant advances are concentrated in 2023 genetics/regulation in *M. kansasii*. Additional 2024 papers were retrieved in adjacent areas (e.g., staphyloxanthin inhibition/virulence modulation in *Staphylococcus aureus*), but full-text evidence extraction specific to cream/off-white colony outcomes was not available here.

## Current applications and real-world implementations
### A) Strain engineering and bioproduction: controlling pigment intensity
CRISPRi-based repression screens in *C. glutamicum* identify levers that decrease or increase carotenoid output; repression of **ispG** (MEP pathway) and crt operon genes decreased decaprenoxanthin production (gottl2021crisprilibraryguidedtargetidentification pages 8-10). Such levers are applicable to:
* **Tuning pigment intensity** in industrial strains (to avoid undesired coloration or to modulate color endpoints).
* **Creating “pale” backgrounds** for screening or for expressing heterologous pathways with minimal pigment interference.

### B) Anti-virulence strategies targeting carotenoid pigments (conditional relevance)
In *S. aureus*, the carotenoid staphyloxanthin is linked to stress tolerance; regulatory control involves **SigB** and two-component systems (AirSR). A recent review-style source summarizes that SigB recruits RNA polymerase to promoters of STX pathway genes and **sigB mutants lack STX pigmentation**, while oxidative stress (H2O2) can increase crt operon expression and STX production (nosair2026staphylococcusaureussgoldenyellow pages 16-20). Although this is not directly “cream pigmented,” it supports a generalizable application pattern: **pharmacologic/genetic inhibition of carotenoid pigments** can intentionally shift colony color toward pale/cream and attenuate stress protection.

## Expert synthesis and curation-oriented analysis
### Minimal core causal hypothesis to curate (cross-taxon)
Based on the strongest evidence, a conservative TraitMech causal graph for METPO:1003024 should center on:
1. **Carotenoid biosynthetic process (GO:0016117)**
2. **Carotenoid abundance/output (intermediate node; label-only acceptable)**
3. **Cream/off-white colony appearance (METPO:1003024 / label)**

With primary edges of the form:
* (crt gene function ↓) → (carotenoid biosynthesis ↓) → (carotenoid abundance ↓) → (cream/off-white phenotype ↑)

### Taxon-specific modules (optional subgraphs)
* **Photochromogenic module (mycobacteria):** light (ENVO:01001148) → CRT locus expression; CrtR repression sets dark vs light state; crtR overexpression can lock a WW/off-white phenotype even under light (janisch2023geneticunderpinningsof pages 10-12).
* **Degradation module (proposed):** ccoRMk loss → cco1Mk upregulation → carotenoid degradation → off-white phenotype (janisch2023geneticunderpinningsof pages 17-19) (curate as uncertain).

## Candidate nodes and edges for `cream_pigmented.yaml`
The following two tables are formatted to be directly actionable for curation.

| Node label | Node type | Suggested ontology grounding | Notes |
|---|---|---|---|
| cream pigmented | phenotype/assay | METPO:1003024 | Pale off-white/cream colony or cell coloration; often operationally contrasts with yellow/orange carotenoid-rich phenotypes. |
| off-white colony appearance (WW phenotype) | phenotype/assay |  | Used explicitly in *Mycobacterium kansasii* pigmentation screens for mutants that failed to pigment after light exposure (janisch2023geneticunderpinningsof pages 4-5, janisch2023geneticunderpinningsof pages 10-12). |
| carotenoid biosynthetic process | pathway/process | GO:0016117 | Broad parent process for pigment-forming isoprenoids; reduced flux is a strong candidate mechanism for cream coloration across taxa (janisch2023geneticunderpinningsof pages 4-5, gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| isoprenoid biosynthetic process | pathway/process | GO:0008299 | Upstream source of carotenoid precursors; useful higher-level node when species-specific carotenoid chemistry differs. |
| MEP pathway | pathway/process |  | 2-C-methyl-D-erythritol 4-phosphate pathway supplies IPP/DMAPP in *M. kansasii* and *C. glutamicum* contexts (janisch2023geneticunderpinningsof pages 4-5, gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| carotenoid degradation | pathway/process |  | Candidate process for loss of visible pigmentation where biosynthetic genes are present but pigments are cleaved (janisch2023geneticunderpinningsof pages 17-19). |
| light-induced gene expression | pathway/process | GO:0071490 | Useful for photochromogenic taxa such as *M. kansasii*, where light activates carotenoid locus expression (janisch2023geneticunderpinningsof pages 10-12). |
| oxidative stress response | pathway/process | GO:0006979 | In *S. aureus*, oxidative stress is linked to induction of crt operon expression and increased staphyloxanthin (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| geranylgeranyl diphosphate biosynthetic process | pathway/process | GO:0016108 | Immediate precursor-supply module for many carotenoid pathways; relevant to crtE/idsA-like functions (gottl2021crisprilibraryguidedtargetidentification pages 8-10, janisch2023geneticunderpinningsof pages 4-5). |
| crtE | gene/protein |  | Geranylgeranyl diphosphate synthase in *M. kansasii* CRT locus; reduced expression associated with WW phenotype (janisch2023geneticunderpinningsof pages 4-5, janisch2023geneticunderpinningsof pages 10-12). |
| CrtE protein | gene/protein |  | Enzyme supplying GGPP for carotenoid synthesis; also present in *C. glutamicum* operon context (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| crtB | gene/protein |  | Phytoene synthase; core carotenoid-pathway gene identified in CRT loci and CRISPRi screens (janisch2023geneticunderpinningsof pages 4-5, gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| CrtB protein | gene/protein |  | Catalyzes phytoene formation from GGPP; loss/repression is expected to reduce pigmentation. |
| crtI | gene/protein |  | Phytoene desaturase gene; repeatedly implicated in reduced pigment phenotypes when perturbed (janisch2023geneticunderpinningsof pages 4-5, gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| CrtI protein | gene/protein |  | Converts phytoene toward lycopene-class intermediates. |
| crtYc | gene/protein |  | One subunit of heterodimeric lycopene cyclase in *M. kansasii* CRT locus (janisch2023geneticunderpinningsof pages 4-5). |
| crtYd | gene/protein |  | Second subunit of heterodimeric lycopene cyclase in *M. kansasii* CRT locus (janisch2023geneticunderpinningsof pages 4-5). |
| crtR | gene/protein |  | MarR-family regulator in *M. kansasii*; overexpression shuts down CRT-locus expression and yields WW/off-white phenotype (janisch2023geneticunderpinningsof pages 10-12). |
| CrtR protein | gene/protein |  | Repressor of carotenogenesis in dark/light regulatory balance of photochromogenic mycobacteria (janisch2023geneticunderpinningsof pages 10-12). |
| MarR-family transcriptional regulator | gene/protein |  | Higher-level regulatory node for crtR-like repressors when exact orthology is uncertain. |
| mmpL1 | gene/protein |  | CRT-locus-associated transporter candidate in *M. kansasii*; may affect pigment localization/export rather than biosynthesis directly (janisch2023geneticunderpinningsof pages 10-12). |
| fni / idi | gene/protein |  | IPP isomerase adjacent to CRT locus in *M. kansasii*; balances IPP and DMAPP pools but was not clearly required for abnormal pigmentation in the screen (janisch2023geneticunderpinningsof pages 4-5). |
| ispG | gene/protein |  | MEP-pathway enzyme; CRISPRi repression significantly lowered decaprenoxanthin in *C. glutamicum* (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| idsA | gene/protein |  | GGPP synthase in *C. glutamicum*; candidate compensatory precursor-supply enzyme relative to crtE (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| crtEb | gene/protein |  | Lycopene elongase in *C. glutamicum* decaprenoxanthin pathway; repression reduced carotenoid biosynthesis (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| crtX | gene/protein |  | Decaprenoxanthin glucosyltransferase in *C. glutamicum*; affects carotenoid modification state more than total pigment amount (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| carotenoid cleavage oxygenase (Cco1Mk) | gene/protein |  | Candidate degradation enzyme in *M. kansasii*; overexpression proposed to prevent pigment accumulation (janisch2023geneticunderpinningsof pages 17-19). |
| ccoRMk | gene/protein |  | Repressor/regulator controlling cco1Mk-dependent carotenoid breakdown in *M. kansasii* (janisch2023geneticunderpinningsof pages 17-19). |
| sigB | gene/protein |  | Alternative sigma factor positively regulating staphyloxanthin pathway transcription in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| RsbU | gene/protein |  | Phosphatase activating SigB pathway; reduced activity associated with decreased STX production in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| AirR | gene/protein |  | Response regulator of AirSR system; overexpression enhances pigmentation and activates crtOPQMN in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| AirSR two-component system | gene/protein |  | Oxygen/redox-responsive regulatory module affecting staphyloxanthin biosynthesis in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtM | gene/protein |  | Staphyloxanthin-pathway dehydrosqualene synthase in *S. aureus*; included because reduced STX can yield paler colonies (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtN | gene/protein |  | Staphyloxanthin-pathway desaturase in *S. aureus*; perturbation expected to reduce yellow-orange pigmentation (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtP | gene/protein |  | Staphyloxanthin-pathway oxidase/dehydrogenase module in *S. aureus* operon context (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtQ | gene/protein |  | Staphyloxanthin-pathway glycosyltransferase in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtO | gene/protein |  | Final acyltransferase of staphyloxanthin pathway in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| crtOPQMN operon | gene/protein |  | Compact operon-level node for *S. aureus* staphyloxanthin biosynthesis and its regulation by SigB/AirSR (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| isopentenyl diphosphate | metabolite/chemical | CHEBI:17366 | Core isoprenoid precursor feeding carotenoid pathways (janisch2023geneticunderpinningsof pages 4-5, gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| dimethylallyl diphosphate | metabolite/chemical | CHEBI:17211 | Isomeric precursor interconverted with IPP by Idi/Fni (janisch2023geneticunderpinningsof pages 4-5). |
| geranylgeranyl diphosphate | metabolite/chemical | CHEBI:58057 | Direct precursor for phytoene/carotenoid synthesis via CrtB (gottl2021crisprilibraryguidedtargetidentification pages 8-10, janisch2023geneticunderpinningsof pages 4-5). |
| phytoene | metabolite/chemical | CHEBI:26114 | Colorless carotenoid precursor; low downstream conversion can contribute to weak pigmentation. |
| lycopene | metabolite/chemical | CHEBI:17579 | Red carotenoid intermediate; abnormal accumulation noted in some crtR mutants rather than cream phenotypes (janisch2023geneticunderpinningsof pages 10-12). |
| β-carotene | metabolite/chemical | CHEBI:17579? | Major yellow/orange carotenoid end product in many bacteria; note CHEBI grounding should be verified before curation. |
| decaprenoxanthin | metabolite/chemical |  | Major carotenoid pigment measured in *C. glutamicum* CRISPRi screen (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| diglucosylated decaprenoxanthin | metabolite/chemical |  | Modified *C. glutamicum* carotenoid product; useful when modeling crtX-dependent pigment chemistry (gottl2021crisprilibraryguidedtargetidentification pages 8-10). |
| staphyloxanthin | metabolite/chemical |  | Golden carotenoid pigment of *S. aureus*; reduced abundance can shift colonies toward cream/pale states (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| hydrogen peroxide | metabolite/chemical | CHEBI:16240 | Oxidative-stress cue that increases crt operon expression in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| light | environmental factor | ENVO:01001148 | Environmental trigger for photochromogenic carotenoid production in *M. kansasii* (janisch2023geneticunderpinningsof pages 10-12). |
| darkness | environmental factor |  | Baseline condition under which *M. kansasii* WT and CRT-locus transformants remain off-white (janisch2023geneticunderpinningsof pages 10-12). |
| low-nutrient medium | environmental factor |  | In *S. aureus*, pigmentation is less apparent on low-nutrient media; likely assay-specific modifier of cream/pale appearance (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| nutrient-rich medium | environmental factor |  | Opposite environmental context promoting stronger pigmentation in *S. aureus* (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| oxygen/redox state | environmental factor |  | Relevant to AirSR-mediated regulation of staphyloxanthin synthesis (nosair2026staphylococcusaureussgoldenyellow pages 16-20). |
| photochromogenicity | phenotype/assay |  | Phenotype in which colonies are off-white in dark and become pigmented after light exposure; important boundary case for cream pigmentation (janisch2023geneticunderpinningsof pages 10-12). |
| reduced carotenoid abundance | phenotype/assay |  | Central mechanistic intermediate connecting pathway perturbation to cream/pale appearance across taxa. |
| non-pigmented colony | phenotype/assay |  | Boundary case distinct from cream: fully colorless/white rather than faintly cream. |
| yellow/orange pigmented colony | phenotype/assay |  | Opposing phenotype indicating higher carotenoid accumulation; useful comparator node. |


*Table: This table lists curation-ready candidate nodes for a TraitMech graph of the 'cream pigmented' microbial trait. It groups phenotype, pathway, gene/regulator, metabolite, and environmental nodes, highlighting which are broadly useful versus taxon-specific.*

| Edge (Subject–predicate–Object) | Mechanistic rationale (1 sentence) | Taxon/Context | Evidence (short quote/snippet) | Reference (DOI, year, URL) | Uncertainty/notes |
|---|---|---|---|---|---|
| carotenoid biosynthesis gene disruption — decreases — carotenoid production | Loss of core crt-pathway enzymes blocks synthesis of colored carotenoids, leaving colonies pale/off-white. | *Mycobacterium kansasii* transposon pigmentation screen | “Most of these mutants failed to develop pigmentation upon light treatment and retained an off-white appearance” and insertions mapped to genes “crtE, crtI, crtB, crtYc, and crtYd” involved in “synthesis of β-carotene” (janisch2023geneticunderpinningsof pages 4-5) | 10.3390/pathogens12010086, 2023, https://doi.org/10.3390/pathogens12010086 | Strong for *M. kansasii*; generalized link to cream pigmentation across taxa should be curated as broad but not universal. |
| crtE reduced expression — causes — off-white/white colony phenotype | Lower expression of the first committed carotenoid-locus gene can suppress downstream carotenoid formation and visible pigmentation. | *M. kansasii* CRT-locus insertion mutant MK28 | Opposite Tn orientation upstream of crtE “causes a polar effect that abolishes crtE expression (MK28: no detectable crtE) and drastically reduces transcription of downstream crt genes”; this orientation was associated with “WW” phenotype (janisch2023geneticunderpinningsof pages 12-14) | 10.3390/pathogens12010086, 2023, https://doi.org/10.3390/pathogens12010086 | Strong but locus-specific; mechanism includes polar effects on downstream genes, not crtE alone. |
| CrtR overexpression — represses — carotenoid biosynthesis genes | Overabundant transcriptional repressor shuts down CRT-locus expression and prevents pigment accumulation. | *M. kansasii* crtR-overexpressing mutant MK75 | “Tn-driven expression of crtR led to a ~10-fold upregulation” while “crtE… was downregulated by at least 500-fold” and this “resulted in a drastic downregulation (shut down) of pigment production” with WW phenotype (janisch2023geneticunderpinningsof pages 10-12) | 10.3390/pathogens12010086, 2023, https://doi.org/10.3390/pathogens12010086 | Strong for this taxon; regulatory architecture may differ in other bacteria. |
| light exposure — increases — CRT-locus gene expression | Light induction activates carotenoid gene expression, shifting colonies from off-white toward yellow/orange states. | *M. kansasii* photochromogenicity | CRT genes were “co-regulated by light”; wild type and heterologous CRT-locus strains were “off-white” in dark but developed “light-induced yellow color” after exposure (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof pages 10-12) | 10.3390/pathogens12010086, 2023, https://doi.org/10.3390/pathogens12010086 | Strong for photochromogenic mycobacteria; should be marked taxon-specific, not a universal environmental cause of cream pigmentation. |
| carotenoid cleavage oxygenase Cco1Mk overexpression — increases — carotenoid degradation | Enhanced carotene cleavage can prevent pigment accumulation even when biosynthetic genes are present. | *M. kansasii* ccoR/cco1 regulatory system | “loss of the regulator ccoRMk causes ~100-fold upregulation of cco1Mk and absence of light-induced pigmentation”; authors “propose that Cco1Mk overexpression drives a Cco1Mk-dependent carotene degradation pathway” (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086, 2023, https://doi.org/10.3390/pathogens12010086 | Moderate; degradation mechanism is proposed by authors and should be curated as uncertain/inferred. |
| repression of ispG — decreases — decaprenoxanthin level | Reduced precursor supply from the MEP isoprenoid pathway lowers downstream carotenoid abundance and visible pigmentation. | *Corynebacterium glutamicum* CRISPRi screen | “Repression of ispG lowered the cellular decaprenoxanthin content significantly” and “repression of genes of the MEP pathway and of carotenogenesis was expected to reduce pigmentation” (gottl2021crisprilibraryguidedtargetidentification pages 8-10) | 10.3390/microorganisms9040670, 2021, https://doi.org/10.3390/microorganisms9040670 | Strong for precursor-supply effect; cream phenotype is inferred from reduced pigmentation/decaprenoxanthin rather than explicitly named “cream.” |
| repression of crtE/mmpL/crtB/crtI/crtEb — decreases — decaprenoxanthin biosynthesis | Direct repression of crt-operon genes reduces carotenoid output and yields paler colonies. | *C. glutamicum* CRISPRi screen | “CRISPRi targeting of the crt operon genes crtE, mmpL, crtB, crtI, and crtEb reduced decaprenoxanthin biosynthesis significantly” and “color phenotype… was judged by visual inspection” (gottl2021crisprilibraryguidedtargetidentification pages 8-10) | 10.3390/microorganisms9040670, 2021, https://doi.org/10.3390/microorganisms9040670 | Strong for reduced pigmentation; exact cream/off-white shade not specified. |
| crtX repression — alters — carotenoid modification state | Loss of glycosylation changes carotenoid composition, which may alter visible hue without abolishing pigment production. | *C. glutamicum* CRISPRi screen | “CRISPRi repression of crtX did not reduce the decaprenoxanthin level… unglucosylated instead of diglucosylated decaprenoxanthin accumulated” (gottl2021crisprilibraryguidedtargetidentification pages 8-10) | 10.3390/microorganisms9040670, 2021, https://doi.org/10.3390/microorganisms9040670 | Useful node/edge, but not a direct cream-pigmented mechanism; likely should not be curated as a primary edge for this trait. |
| SigB activity — increases — staphyloxanthin pathway transcription | Positive transcriptional control of the carotenoid operon promotes yellow pigmentation; loss of SigB yields non-pigmented/paler colonies. | *Staphylococcus aureus* staphyloxanthin regulation | “RNA polymerases are recruited to the promoter by SigB, which triggers the transcription of the STX pathway genes” and “STX pigmentation is lacking in S. aureus sigB mutants” (nosair2026staphylococcusaureussgoldenyellow pages 16-20) | 10.1186/s12934-025-02919-2, 2025/2026, https://doi.org/10.1186/s12934-025-02919-2 | Source is in-press/review-like context; still mechanistically plausible and consistent with prior literature, but verify against primary experiments before final curation. |
| rsbU activity — positively regulates — SigB-dependent staphyloxanthin production | Stress-signaling through rsbU promotes SigB activation and thereby carotenoid pigmentation. | *S. aureus* stress-response regulation | “The rsbU mutation is most likely the cause of the decreased STX production” and “the crt biosynthesis operon for STX is subsequently positively regulated by the transcription factor sigB” (nosair2026staphylococcusaureussgoldenyellow pages 16-20) | 10.1186/s12934-025-02919-2, 2025/2026, https://doi.org/10.1186/s12934-025-02919-2 | Secondary-source summary; taxon-specific to staphylococcal STX. |
| AirR overexpression — increases — crtOPQMN operon expression | Oxygen/redox-responsive signaling can raise carotenoid operon output and deepen pigmentation. | *S. aureus* AirSR two-component system | “The crtOPQMN operon is directly transcriptionally activated by the AirSR TCS” and “colony pigmentation was enhanced by the overexpression of the airR response regulator” (nosair2026staphylococcusaureussgoldenyellow pages 16-20) | 10.1186/s12934-025-02919-2, 2025/2026, https://doi.org/10.1186/s12934-025-02919-2 | Good regulatory edge, but effect on cream phenotype is inverse: reduced AirR would be expected to pale colonies. |
| H2O2 exposure — increases — crt operon expression | Oxidative stress can stimulate carotenoid biosynthesis as a protective response, reducing likelihood of cream/off-white appearance. | *S. aureus* oxidative-stress response | “The production of STX was substantially increased as a result of the increased expression of genes in the crt operon under H2O2 exposure” (nosair2026staphylococcusaureussgoldenyellow pages 16-20) | 10.1186/s12934-025-02919-2, 2025/2026, https://doi.org/10.1186/s12934-025-02919-2 | Environmental effect is inverse to cream trait; curate only if representing conditions that suppress or enhance pigmentation contextually. |
| low-nutrient medium — decreases — staphyloxanthin pigmentation | Reduced nutrient availability can lower pigment accumulation and make colonies less intensely colored. | *S. aureus* fermentation/medium optimization | “On low-nutrient media… the pigmentation was less apparent, while it was more prominent on nutrient-rich medium” (nosair2026staphylococcusaureussgoldenyellow pages 16-20) | 10.1186/s12934-025-02919-2, 2025/2026, https://doi.org/10.1186/s12934-025-02919-2 | Assay/medium-specific; may support cream-like phenotype but should be marked condition-dependent rather than intrinsic trait mechanism. |


*Table: This table compiles candidate causal edges linking reduced carotenoid biosynthesis, increased carotenoid degradation, and environmental regulation to cream/off-white pigmentation. It is formatted for TraitMech curation and highlights where evidence is strong, taxon-specific, or still uncertain.*

## Relevant statistics / data points (recent studies)
* *M. kansasii* screen: **204 pigmentation mutants**; **0.14% isolation rate** (janisch2023geneticunderpinningsof pages 4-5).
* Robust screen phase: **98/121 (81%) WW (off-white)** after light treatment (janisch2023geneticunderpinningsof pages 4-5).
* crtR overexpression: **~10× crtR upregulation**; **crtE downregulated by ≥500× under light** (janisch2023geneticunderpinningsof pages 10-12).
* Proposed degradation axis: **~100× upregulation of cco1Mk** associated with loss of light-induced pigmentation when ccoRMk is lost (janisch2023geneticunderpinningsof pages 17-19).

## Visual evidence (figures)
Janisch et al. provide figure panels showing the WW/off-white versus pigmented phenotypes and mapping of transposon insertions in the CRT locus, which visually supports the link between carotenoid genetics and off-white colonies (janisch2023geneticunderpinningsof media 2a9f3364, janisch2023geneticunderpinningsof media 6e38aeae, janisch2023geneticunderpinningsof media 88b91ae0, janisch2023geneticunderpinningsof media a5bd97bd, janisch2023geneticunderpinningsof media 6fa62ca8).

## Warnings / do-not-curate-yet items
1. **Staphyloxanthin regulatory edges** (SigB/RsbU/AirSR, nutrient effects, H2O2 induction) were extracted from a review-like/in-press context in the retrieved text, and should be verified against primary experimental sources before being treated as high-confidence edges for TraitMech (nosair2026staphylococcusaureussgoldenyellow pages 16-20).
2. **Carotenoid degradation by Cco1Mk** is presented as a proposed mechanism; curate as *uncertain* unless supported by direct biochemical/pigment quantification evidence in the full paper (janisch2023geneticunderpinningsof pages 17-19).
3. **Color terms are assay-dependent** (e.g., “off-white,” “white,” “cream”); for curation, keep phenotype nodes explicitly tied to assay descriptions where possible (janisch2023geneticunderpinningsof pages 4-5).

## DOI-first bibliography (with publication dates and URLs)
1. Janisch N, Levendosky K, Budell WC, Quadri LEN. **Genetic Underpinnings of Carotenogenesis and Light-Induced Transcriptome Remodeling in the Opportunistic Pathogen *Mycobacterium kansasii*.** *Pathogens*. **2023-01**. DOI: **10.3390/pathogens12010086**. https://doi.org/10.3390/pathogens12010086 (janisch2023geneticunderpinningsof pages 4-5, janisch2023geneticunderpinningsof pages 10-12)
2. Göttl VL, Schmitt I, Braun K, Peters-Wendisch P, Wendisch VF, Henke NA. **CRISPRi-Library-Guided Target Identification for Engineering Carotenoid Production by *Corynebacterium glutamicum*.** *Microorganisms*. **2021-03**. DOI: **10.3390/microorganisms9040670**. https://doi.org/10.3390/microorganisms9040670 (gottl2021crisprilibraryguidedtargetidentification pages 8-10)
3. Nosair AM, Abo-Kamar AM, Al-Madboly LA. **Staphylococcus aureus' golden-yellow pigment staphyloxanthin: production enhancement, analytical characterization, and biological attributes.** (retrieved as in-press/secondary context). DOI: **10.1186/s12934-025-02919-2**. https://doi.org/10.1186/s12934-025-02919-2 (nosair2026staphylococcusaureussgoldenyellow pages 16-20)


References

1. (janisch2023geneticunderpinningsof pages 4-5): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

2. (janisch2023geneticunderpinningsof pages 10-12): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

3. (gottl2021crisprilibraryguidedtargetidentification pages 8-10): Vanessa L. Göttl, Ina Schmitt, Kristina Braun, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Crispri-library-guided target identification for engineering carotenoid production by corynebacterium glutamicum. Microorganisms, 9:670, Mar 2021. URL: https://doi.org/10.3390/microorganisms9040670, doi:10.3390/microorganisms9040670. This article has 34 citations.

4. (janisch2023geneticunderpinningsof pages 17-19): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

5. (nosair2026staphylococcusaureussgoldenyellow pages 16-20): AM Nosair, AM Abo-Kamar, and LA Al-Madboly. Staphylococcus aureus' sgolden-yellow pigment staphyloxanthin: production enhancement, analytical characterization, and biological attributes. Unknown journal, 2026. URL: https://doi.org/10.1186/s12934-025-02919-2\_reference, doi:10.1186/s12934-025-02919-2\_reference.

6. (janisch2023geneticunderpinningsof pages 12-14): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

7. (janisch2023geneticunderpinningsof pages 5-8): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

8. (janisch2023geneticunderpinningsof media 2a9f3364): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

9. (janisch2023geneticunderpinningsof media 6e38aeae): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

10. (janisch2023geneticunderpinningsof media 88b91ae0): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

11. (janisch2023geneticunderpinningsof media a5bd97bd): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

12. (janisch2023geneticunderpinningsof media 6fa62ca8): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.