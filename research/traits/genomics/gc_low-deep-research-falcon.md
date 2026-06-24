---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:05:58.257996'
end_time: '2026-06-18T03:19:38.081537'
duration_seconds: 819.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC low
  trait_identifier: METPO:1000429
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A GC-content phenotype with genome-wide GC composition between approximately
    42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label
    'low' does not match this mid-range numeric threshold, but the synonym is preserved
    as the authoritative bin definition).
  parent_traits: METPO:1000127
  synonyms: GC_42.65_57.0
  evidence_summary: 'DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports
    the mid-range GC content as a distinct genomic-composition phenotype.)'
  causal_graph_summary: 'gc_low_mid_low_gc_bin: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC low
- **METPO identifier:** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_low.yaml`.

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
- **Trait label:** GC low
- **METPO identifier:** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_low.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **GC low** (METPO:1000429; GC_42.65_57.0)

### Scope summary (trait meaning and boundaries)
**Trait label:** GC low (synonym: **GC_42.65_57.0**)

**Operational definition (METPO bin):** genome-wide GC composition between approximately **42.65% and 57.0%** (METPO bin `GC_42.65_57.0`). This corresponds to a **mid-range** genomic base-composition phenotype even though the upstream label “low” is preserved; for curation, the numeric bin should be treated as authoritative.

**What the phenotype represents:** a *genome-wide compositional class* used in comparative genomics (e.g., codon usage, mutation spectrum comparisons, ecological/selection analyses), not a direct physiological assay readout.

**Boundary cases / nearby traits:**
- **Bin-edge genomes**: organisms with genome-wide GC near 42.65% or 57% will be sensitive to assembly/QC differences and may switch bins with updated sequences.
- **Non-uniform composition**: some genomes can exhibit large within-genome heterogeneity (replichore or domain-level biases). For example, bacterial chromosome architecture can include large regions with unusual organization and low recombination; such heterogeneity means the *mean genome GC%* may mask local extremes relevant to mechanisms (e.g., strand/domain effects) (tomasch2024ontheevolution pages 1-2).

### Key concepts and current mechanistic understanding (curation-focused)
Genome-wide GC content is widely understood as emerging from the interplay of:
1. **Mutational processes and mutational spectra** (e.g., transition/transversion biases; cytosine deamination).
2. **DNA repair capacity and biases** (MMR, BER, homologous recombination-related processes), which can reshape the realized mutation spectrum.
3. **Selection and ecological context** (e.g., nutrient limitation and genome streamlining in marine photic zones).
4. **Environmental mutagens** (e.g., UV) and lifestyle correlates (oxygen tolerance) that associate with compositional differences.

In the 2023–2024 literature retrieved here, the strongest direct mechanistic evidence relates to **mutational spectra and DNA repair**, plus **marine ecological selection**.

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Mutational spectra + DNA repair defects as drivers of base-composition tendencies
A large-scale Nature Communications study (2023) reconstructs **single-base substitution (SBS) spectra** for **84 clades across 31 bacterial species**, showing spectra are diverse and can be decomposed into signatures attributable to **DNA repair defects** and **niche-associated mutagens** (ruis2023mutationalspectraare pages 1-2).
- Quantitative details from the paper excerpt include: transitions are more common than transversions (e.g., **~52–55%** in *Klebsiella pneumoniae* to **>90%** in *Campylobacter jejuni*), and **C→T** is the most common change in **69/84** spectra, potentially reflecting **cytosine deamination** (ruis2023mutationalspectraare pages 1-2).
- The same work attributes contextual mutational signatures to defects in **11 DNA repair genes** spanning **MMR, BER, and homologous recombination** (ruis2023mutationalspectraare pages 1-2).
- It also reports **correlations between genomic G+C content and mutation types**, including a **negative correlation** with the proportion of **C→A/T** mutations and a **positive correlation** with **C→G** mutations (ruis2023mutationalspectraare pages 2-3).

**Curation interpretation:** for GC_42.65_57.0, a mechanistically defensible model is that *GC content is mediated by mutation spectra*, which are in turn influenced by repair pathways and environmental exposures. The trait bin itself should usually be downstream of an intermediate node like “AT-enriching mutation spectrum” or “GC-enriching mutation spectrum,” rather than directly downstream of single genes.

#### 2) Replication/repair enzyme biases (mechanistic micro-edges)
A 2024 Frontiers in Microbiology study (proteobacteria codon usage/tRNA modification) explicitly links genome GC% to mutational bias and repair biases, giving a concrete example: “**in E. coli, MutL protects preferentially from A:T to G:C mutations**” (delgado2024impactofthe pages 1-2). It also notes that “**UV promotes G:C to A:T**” as an environmental mutation trend (delgado2024impactofthe pages 1-2).

**Curation interpretation:** these are useful mechanistic edges, but the phrasing is example-based (E. coli) and should be marked as potentially taxon-specific unless corroborated across taxa.

#### 3) Ecological selection: nutrient limitation and streamlined, lower-GC marine genomes
A 2023 Nature Communications study on global-ocean microbial genome size discusses that “**nutrient limitation is considered a strong selective force that causes the relatively low guanine and cytosine content and genome streamlining in pelagic bacterioplankton**” (ngugi2023abioticselectionof pages 1-2).

**Curation interpretation:** this provides a direct environment→GC directionality suitable for the graph, but it is scoped to **pelagic bacterioplankton** and should be curated with habitat constraints.

#### 4) Associations with oxygen tolerance (composition correlates used in prediction)
A 2024 bioRxiv preprint describing genome-based prediction of growth conditions states: “**For oxygen sensitivity, aerobic organisms tend to have higher G+C content compared to anaerobic relatives**” (barnum2024predictingmicrobialgrowth pages 1-3).

**Curation interpretation:** this supports an oxygen-related association node. It is not a mechanistic proof, and the source is a preprint; curate as association or hypothesis unless supported by additional primary evidence.

### Candidate nodes (grouped by type) with grounding suggestions
#### Phenotype node
- **GC low / GC_42.65_57.0** — METPO:1000429 (provided by user template; numeric bin definition is authoritative).

#### Genome-level intermediate phenotypes (often needed for TraitMech)
- **Mutational spectrum / mutational signature (SBS spectrum)** — label-only (no stable ontology commonly used)
- **AT-enriching substitutions** (e.g., C→T, G:C→A:T) — label-only
- **GC-enriching substitutions** (e.g., C→G) — label-only

#### Molecular processes / pathways
- **Mismatch repair (MMR)** — GO:0006298 (process)
- **Base excision repair (BER)** — GO:0006284
- **Homologous recombination** — GO:0035825

#### Genes/proteins (examples explicitly mentioned in retrieved evidence)
- **MutL** — label-only (protein; could be grounded to UniProt per taxon during curation) (delgado2024impactofthe pages 1-2)
- (Ruis 2023 references multiple DNA repair genes, but the excerpt available here does not enumerate them by name beyond pathway-level; capture as “DNA repair genes (MMR/BER/HR set)” unless full text is later mined) (ruis2023mutationalspectraare pages 1-2).

#### Environmental/exposure factors
- **Ultraviolet radiation** — ENVO:01000243 (candidate grounding)
- **Nutrient limitation / oligotrophy** — label-only (ENVO terms could be added later)
- **Photic ocean / epipelagic zone** — ENVO:01000036 (candidate)
- **Oxygen availability / aerobic vs anaerobic lifestyle** — label-only (could map to environmental oxygen concentration terms later)

#### Genome architecture / evolutionary context (secondary, indirect)
- **Recombination frequency (reduced)** — label-only; linked to mobile elements underrepresentation in a chromosome domain context (tomasch2024ontheevolution pages 1-2)

### Evidence-backed candidate causal edges (curation-ready)
The following table is formatted to support direct translation into a TraitMech YAML edge list, with uncertainty notes.

| Edge (S–P–O) | Candidate node grounding (CURIEs where possible) | Evidence (first author year, DOI, URL) | Supporting snippet (short quote) | Notes for curation (including uncertainty/taxon-specific flags) |
|---|---|---|---|---|
| DNA repair defect → causes → distinct bacterial mutational signature or spectrum | DNA repair defect label-only; mutational spectrum label-only; MMR GO:0006298; BER GO:0006284; homologous recombination GO:0035825 | Ruis 2023; DOI 10.1038/s41467-023-42916-w; https://doi.org/10.1038/s41467-023-42916-w | “defects in DNA repair create distinctive mutational signatures” and “attribute mutational signatures to defects in 11 DNA repair genes that function in mismatch repair (MMR), base excision repair (BER), or homologous recombination (HR)” (ruis2023mutationalspectraare pages 1-2) | Strong mechanistic upstream edge. Best curated as driver of mutation spectrum, not direct deterministic assignment to the GC_42.65_57.0 bin. |
| Cytosine deamination or C→T transition bias → shifts toward → AT-enriching mutation spectrum | cytosine deamination label-only; C→T transition label-only; AT-enriching mutation spectrum label-only | Ruis 2023; DOI 10.1038/s41467-023-42916-w; https://doi.org/10.1038/s41467-023-42916-w | “cytosine to thymine (C > T) was typically the most common mutation type identified (in 69 of 84 SBS spectra examined), potentially due to cytosine deamination” (ruis2023mutationalspectraare pages 1-2, ruis2023mutationalspectraare pages 2-3) | Strong evidence for GC-lowering mutational pressure. Suitable as edge to an intermediate AT-biased spectrum node; edge to the specific METPO bin remains inferred. |
| MutL activity → preferentially protects against → A:T→G:C mutations | MutL label-only; mismatch repair GO:0006298; A:T→G:C mutation class label-only | Delgado 2024; DOI 10.3389/fmicb.2024.1412318; https://doi.org/10.3389/fmicb.2024.1412318 | “in E. coli, MutL protects preferentially from A:T to G:C mutations” (delgado2024impactofthe pages 1-2) | Mechanistic but likely example-specific to E. coli in the cited wording. Curate as enzyme-bias affecting mutation spectrum; downstream effect on genome GC is indirect and inferred. |
| DNA replication or repair enzyme bias → shapes → genomic GC percent | DNA replication or repair enzyme bias label-only; genomic GC content phenotype label-only | Delgado 2024; DOI 10.3389/fmicb.2024.1412318; https://doi.org/10.3389/fmicb.2024.1412318 | “enzymes involved in DNA replication and/or repair are known to present biases” and “The GC% of genomes depends in part on the mutation rates between each nucleotide” (delgado2024impactofthe pages 1-2) | Useful high-level mechanistic summary. Evidence is broad and review-like rather than direct perturbation evidence; mark partly inferred for TraitMech. |
| UV exposure → promotes → G:C→A:T mutations | ultraviolet radiation ENVO:01000243 candidate; G:C→A:T mutation label-only | Delgado 2024; DOI 10.3389/fmicb.2024.1412318; https://doi.org/10.3389/fmicb.2024.1412318 | “environmental conditions also favor some mutation trends [e.g., in E. coli, UV promotes G:C to A:T” (delgado2024impactofthe pages 1-2) | Supports environmental mutagen to AT-enriching substitutions. Example is E. coli-specific in wording; broad generalization should be marked uncertain. |
| Aerobic lifestyle or oxygen tolerance → associated with → higher genomic GC content than anaerobic relatives | aerobic respiration GO:0009060 candidate; oxygen tolerance label-only; higher GC content label-only | Barnum 2024; DOI 10.1101/2024.03.22.586313; https://doi.org/10.1101/2024.03.22.586313 | “For oxygen sensitivity, aerobic organisms tend to have higher G+C content compared to anaerobic relatives” (barnum2024predictingmicrobialgrowth pages 1-3) | Explicit association, but mechanism unresolved here. Preprint only. Negative implication for GC low is plausible, but curate cautiously as association rather than direct causation. |
| Nutrient limitation in photic ocean → selects for → low GC content and genome streamlining | photic zone ENVO:01000036 candidate; nutrient limitation label-only; low GC content label-only | Ngugi 2023; DOI 10.1038/s41467-023-36988-x; https://doi.org/10.1038/s41467-023-36988-x | “Nutrient limitation is considered a strong selective force that causes the relatively low guanine and cytosine content and genome streamlining in pelagic bacterioplankton” (ngugi2023abioticselectionof pages 1-2) | Strong and directly relevant environmental edge, especially for pelagic marine microbes. Retain habitat scope and avoid overgeneralizing to all bacteria. |
| Reduced recombination frequency → contributes to → conserved high strand-bias genome architecture | homologous recombination GO:0035825; gene strand bias label-only; genome architecture label-only | Tomasch 2024; DOI 10.1128/mbio.00602-24; https://doi.org/10.1128/mbio.00602-24 | “Repetitive and mobile elements are underrepresented, suggesting reduced recombination frequency by structural isolation from other parts of the chromosome” (tomasch2024ontheevolution pages 1-2) | Indirect for GC. Useful contextual edge for chromosome architecture, but not ready for direct GC-low TraitMech curation without additional evidence linking recombination or architecture to GC bin membership. |
| C>A or C>T enriched and C>G depleted mutation spectrum → associated with → lower genomic G+C content | mutation spectrum label-only; lower genomic G+C content label-only | Ruis 2023; DOI 10.1038/s41467-023-42916-w; https://doi.org/10.1038/s41467-023-42916-w | “Genomic G+C content correlates with specific mutation types: a negative correlation with the proportion of C>A/T mutations and a positive correlation with C>G mutations” (ruis2023mutationalspectraare pages 2-3) | Strong intermediate edge connecting spectrum composition to GC composition. Correlative rather than intervention-based, but highly useful for curation. |


*Table: This table lists candidate causal edges relevant to GC low (METPO:1000429; GC_42.65_57.0), emphasizing DNA repair, mutation-spectrum, and environmental determinants. It is formatted for curation use and flags indirect or uncertain claims.*

### Expert synthesis and analysis (how to interpret edges for GC_42.65_57.0)
1. **Prefer a two-step causal structure** for GC phenotypes: *environment/repair → mutation spectrum → genome-wide GC bin*. This matches evidence where GC associations are most directly demonstrated via correlations with mutation categories (ruis2023mutationalspectraare pages 2-3) and via repair-defect-driven signature changes (ruis2023mutationalspectraare pages 1-2).
2. **Use habitat scoping for selection edges**: nutrient limitation driving “relatively low GC” is compelling for pelagic bacterioplankton, but should not be generalized beyond similar ecological contexts without additional evidence (ngugi2023abioticselectionof pages 1-2).
3. **Treat oxygen–GC as an association node** unless strengthened by causal/interventional evidence: the 2024 preprint uses this as a known correlation supporting prediction, not as mechanistic proof (barnum2024predictingmicrobialgrowth pages 1-3).
4. **Taxon specificity flags**: explicit enzymatic bias statements (MutL; UV) are provided as E. coli examples in a broader codon usage discussion and should be tagged as “example-based” until corroborated broadly (delgado2024impactofthe pages 1-2).

### Current applications and real-world implementations (with recent statistics)
#### 1) Genome-resolved metagenomics and bioprospecting (real-world implementation)
A 2024 Nature study reports recovery of **43,191 bacterial and archaeal genomes** from public marine metagenomes spanning **138 phyla**, using these genomic resources for in silico bioprospecting and experimental validation of outputs (e.g., novel CRISPR–Cas9, antimicrobial peptides, PET-degrading enzymes) (chen2024globalmarinemicrobial pages 1-2). While not focused on GC bins, such catalogs routinely use compositional features (including GC) in genome QC and comparative analyses.
- Publication date: **Published online 4 Sep 2024** (as shown in the article header) (chen2024globalmarinemicrobial pages 1-2).
- URL: https://doi.org/10.1038/s41586-024-07891-2 (chen2024globalmarinemicrobial pages 1-2).

#### 2) Genome-based prediction of cultivation conditions (tool-like implementation)
A 2024 bioRxiv preprint presents models predicting microbial growth requirements from sequence composition using **15,596 bacteria and archaea** for training, predicting oxygen tolerance with **92% balanced accuracy**, temperature with **R²=0.73**, salinity with **R²=0.81**, and pH with **R²=0.48**; it also applies models to **85,205** sequenced species and **3,349** environmental samples (MAGs) (barnum2024predictingmicrobialgrowth pages 1-3). The work explicitly uses GC content among DNA sequence features and notes an oxygen–GC association used as rationale (barnum2024predictingmicrobialgrowth pages 1-3).
- Posted: **22 Mar 2024** (bioRxiv version date in header) (barnum2024predictingmicrobialgrowth pages 1-3).
- URL: https://doi.org/10.1101/2024.03.22.586313 (barnum2024predictingmicrobialgrowth pages 1-3).

#### 3) Microbial ecology: nutrient limitation, streamlining, and base composition
The 2023 global-ocean study frames nutrient limitation as a selective driver of “relatively low” GC and streamlining in pelagic bacterioplankton, contextualizing base composition as part of ecological strategy (ngugi2023abioticselectionof pages 1-2).
- Accepted: **27 Feb 2023** (article header) (ngugi2023abioticselectionof pages 1-2).
- URL: https://doi.org/10.1038/s41467-023-36988-x (ngugi2023abioticselectionof pages 1-2).

### Warnings / claims not yet ready for curation into TraitMech
1. **Direct mapping of mechanisms to the specific METPO bin** (42.65–57.0%) is not established in the retrieved texts; the evidence supports GC-shifting mechanisms generally (mutation spectrum, repair, selection), but not bin-threshold causal cutoffs.
2. **gBGC / recombination-driven GC shifts** are not well supported by the retrieved evidence snippets. Tomasch et al. discuss reduced recombination frequency in a chromosomal region, but not a direct causal connection to genome-wide GC% (tomasch2024ontheevolution pages 1-2).
3. **Oxygen → GC** is presented as an association in a preprint and should be curated as “associated_with” unless additional primary causal evidence is added (barnum2024predictingmicrobialgrowth pages 1-3).
4. **MutL and UV edges** are given as example statements (E. coli); curate with taxon-specific qualifiers or mark uncertain until corroborated (delgado2024impactofthe pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates where available)
1. Ruis C, et al. *Mutational spectra are associated with bacterial niche.* **Nature Communications**. Accepted **25 Oct 2023**. DOI: **10.1038/s41467-023-42916-w**. URL: https://doi.org/10.1038/s41467-023-42916-w (ruis2023mutationalspectraare pages 1-2, ruis2023mutationalspectraare pages 2-3)
2. Delgado S, et al. *Impact of the chemical modification of tRNAs anticodon loop on the variability and evolution of codon usage in proteobacteria.* **Frontiers in Microbiology**. Published **05 Aug 2024**. DOI: **10.3389/fmicb.2024.1412318**. URL: https://doi.org/10.3389/fmicb.2024.1412318 (delgado2024impactofthe pages 1-2)
3. Ngugi DK, et al. *Abiotic selection of microbial genome size in the global ocean.* **Nature Communications**. Accepted **27 Feb 2023**. DOI: **10.1038/s41467-023-36988-x**. URL: https://doi.org/10.1038/s41467-023-36988-x (ngugi2023abioticselectionof pages 1-2)
4. Barnum TP, et al. *Predicting microbial growth conditions from amino acid composition.* **bioRxiv** (preprint). Posted **22 Mar 2024**. DOI: **10.1101/2024.03.22.586313**. URL: https://doi.org/10.1101/2024.03.22.586313 (barnum2024predictingmicrobialgrowth pages 1-3)
5. Chen J, et al. *Global marine microbial diversity and its potential in bioprospecting.* **Nature**. Published online **04 Sep 2024**. DOI: **10.1038/s41586-024-07891-2**. URL: https://doi.org/10.1038/s41586-024-07891-2 (chen2024globalmarinemicrobial pages 1-2)
6. Tomasch J, et al. *On the evolution of chromosomal regions with high gene strand bias in bacteria.* **mBio**. Published **16 May 2024** (per article header). DOI: **10.1128/mbio.00602-24**. URL: https://doi.org/10.1128/mbio.00602-24 (tomasch2024ontheevolution pages 1-2)

References

1. (tomasch2024ontheevolution pages 1-2): Jürgen Tomasch, Karel Kopejtka, Sahana Shivaramu, Izabela Mujakić, and Michal Koblížek. On the evolution of chromosomal regions with high gene strand bias in bacteria. Jun 2024. URL: https://doi.org/10.1128/mbio.00602-24, doi:10.1128/mbio.00602-24. This article has 2 citations and is from a domain leading peer-reviewed journal.

2. (ruis2023mutationalspectraare pages 1-2): Christopher Ruis, Aaron Weimann, Gerry Tonkin-Hill, Arun Prasad Pandurangan, Marta Matuszewska, Gemma GR Murray, Roger C Lévesque, Tom L Blundell, R Andres Floto, and Julian Parkhill. Mutational spectra are associated with bacterial niche. JournalArticle, Nov 2023. URL: https://doi.org/10.17863/cam.102279, doi:10.17863/cam.102279. This article has 15 citations.

3. (ruis2023mutationalspectraare pages 2-3): Christopher Ruis, Aaron Weimann, Gerry Tonkin-Hill, Arun Prasad Pandurangan, Marta Matuszewska, Gemma GR Murray, Roger C Lévesque, Tom L Blundell, R Andres Floto, and Julian Parkhill. Mutational spectra are associated with bacterial niche. JournalArticle, Nov 2023. URL: https://doi.org/10.17863/cam.102279, doi:10.17863/cam.102279. This article has 15 citations.

4. (delgado2024impactofthe pages 1-2): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

5. (ngugi2023abioticselectionof pages 1-2): David K. Ngugi, Silvia G. Acinas, Pablo Sánchez, Josep M. Gasol, Susana Agusti, David M. Karl, and Carlos M. Duarte. Abiotic selection of microbial genome size in the global ocean. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-36988-x, doi:10.1038/s41467-023-36988-x. This article has 53 citations and is from a highest quality peer-reviewed journal.

6. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

7. (chen2024globalmarinemicrobial pages 1-2): Jianwei Chen, Yangyang Jia, Ying Sun, Kun Liu, Changhao Zhou, Chuan Liu, Denghui Li, Guilin Liu, Chengsong Zhang, Tao Yang, Lei Huang, Yunyun Zhuang, Dazhi Wang, Dayou Xu, Qiaoling Zhong, Yang Guo, Anduo Li, Inge Seim, Ling Jiang, Lushan Wang, Simon Ming Yuen Lee, Yujing Liu, Dantong Wang, Guoqiang Zhang, Shanshan Liu, Xiaofeng Wei, Zhen Yue, Shanmin Zheng, Xuechun Shen, Sen Wang, Chen Qi, Jing Chen, Chen Ye, Fang Zhao, Jun Wang, Jie Fan, Baitao Li, Jiahui Sun, Xiaodong Jia, Zhangyong Xia, He Zhang, Junnian Liu, Yue Zheng, Xin Liu, Jian Wang, Huanming Yang, Karsten Kristiansen, Xun Xu, Thomas Mock, Shengying Li, Wenwei Zhang, and Guangyi Fan. Global marine microbial diversity and its potential in bioprospecting. Nature, 633:371-379, Sep 2024. URL: https://doi.org/10.1038/s41586-024-07891-2, doi:10.1038/s41586-024-07891-2. This article has 182 citations and is from a highest quality peer-reviewed journal.