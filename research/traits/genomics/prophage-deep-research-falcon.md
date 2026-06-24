---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:34:58.261223'
end_time: '2026-06-18T03:52:33.751363'
duration_seconds: 1055.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: prophage
  trait_identifier: traitmech:000091
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: prophage
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing possession of an integrated (or extrachromosomal)
    temperate bacteriophage genome (a prophage) maintained in the host during lysogeny,
    often contributing genes that alter host phenotype.
  parent_traits: traitmech:000089
  synonyms: lysogen
  evidence_summary: 'DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review
    prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.)
    | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature,
    the maintenance of temperate phage genomes within hosts.)'
  causal_graph_summary: 'prophage_lysogeny: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prophage
- **METPO identifier:** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **prophage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/prophage.yaml`.

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
- **Trait label:** prophage
- **METPO identifier:** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **prophage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/prophage.yaml`.

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


## Prophage (traitmech:000091) — curation-focused research report (2023–2024 emphasis)

### Scope summary (TraitMech interpretation)
A **prophage** is the genome of a temperate bacteriophage maintained in a bacterial host during lysogeny, classically by **chromosomal integration** and repression of lytic genes by a phage repressor (e.g., cI/CI), but in important boundary cases by **extrachromosomal (episomal) maintenance** in “phage–plasmid” states. Mechanistically, prophage carriage is a *genomics trait* with downstream phenotypic consequences that can be latent (no virion production) or inducible under specific cues. Recent work stresses that prophage induction is not exclusively DNA-damage driven; **SOS-independent sensory modules** (including quorum sensing) can selectively trigger lysis in polylysogens. (silpe2023smallproteinmodules pages 1-2, pfeifer2024phageplasmidspromoterecombination pages 1-2)

**Boundary cases and distinctions for curation**
- **Prophage vs. lytic phage infection:** prophage implies maintenance of a temperate phage genome without ongoing lysis; lytic infection is not part of the trait. (silpe2023smallproteinmodules pages 1-2)
- **Integrated vs. extrachromosomal prophage:** while classic definitions emphasize integration, phage–plasmids can behave as temperate phages while persisting as low-copy extrachromosomal elements; this should be explicitly supported in node/edge selection to avoid “integration-only” bias. (pfeifer2024phageplasmidspromoterecombination pages 1-2, nair2024presenceofphageplasmids pages 1-2)
- **Cryptic/defective prophages:** elements like **E. coli e14** can be strongly SOS/LexA inducible at the transcriptional level but may not produce active virions; curate “prophage gene induction” separately from “virion production” edges. (sass2024thednadamage pages 2-3)

---

## 1) Key concepts and current understanding

### 1.1 Core maintenance logic (lysogeny)
A common mechanistic model is that prophage genomes are stably inherited because lytic genes are transcriptionally repressed by a **phage-encoded master repressor** (e.g., cI/CI) that binds a lysis promoter (PR) to block lytic gene expression. (silpe2023smallproteinmodules pages 1-2)

### 1.2 Canonical induction: DNA damage → SOS → CI inactivation
In many studied prophages, induction is coupled to the host DNA-damage response: DNA damage generates activated **RecA (RecA\*)**, triggering **LexA autoproteolysis** and activation of SOS genes, and RecA\* can also trigger **autoproteolysis/inactivation of CI-like prophage repressors**, derepressing lytic genes and promoting prophage induction. (sweet2023exposureofshewanella pages 2-4, silpe2023smallproteinmodules pages 1-2, herediaponce2023genotoxicstressstimulates pages 1-2)

### 1.3 Updated mechanistic refinement (2023): CI fragment clearance as a required final step
A key 2023 development is that **CI autocleavage may be insufficient** if cleavage fragments retain DNA-binding function. In *Staphylococcus aureus* temperate phages (Φ11, 80α), the AAA+ protease specificity factor **ClpX** directly recognizes the **N-terminal CI fragment (CI-NTD)** generated by SOS-mediated cleavage; ClpX binding/activity is **necessary and sufficient** to relieve residual repression and complete prophage induction. Strong functional effects are reported: clpX mutants show **~10^8–10^9-fold reductions in phage titre** after induction, while clpP mutants show smaller (but still major) decreases and altered kinetics. (thabet2023theclpxprotease pages 1-2, thabet2023theclpxprotease pages 2-3)

### 1.4 SOS-independent induction and polylysogeny logic (2023)
A 2023 Nature study identified prophage regulatory modules that trigger induction **independently of DNA-damage cues**, including quorum sensing. These modules share a logic: a transcription factor induces a neighboring gene encoding a small protein; the small protein inactivates the prophage master repressor, triggering induction. Importantly, in polylysogens, the induction cue determines whether one or multiple prophages enter lysis, providing a mechanism for **inter-prophage competition** and cue-specific release. (silpe2023smallproteinmodules pages 1-2)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Prophage induction by physical stress: ionizing radiation as a biomarker signal (2023)
In *Shewanella oneidensis* MR-1, sublethal **ionizing radiation (IR)** triggers short-term SOS activation and longer-term **prophage (So Lambda) activation**. RNA-seq and qPCR indicate that at 300 min, So Lambda lysis genes can show higher activation than SOS markers (recA, sulA), and plaque production increased after 1 Gy exposures. This supports a practical concept: prophage lytic-cycle transcripts/phenotypes can be sensitive biomarkers of low-dose DNA damage. (sweet2023exposureofshewanella pages 2-4)

### 2.2 Prophage-triggered community/biofilm phenotypes (2023)
In *Burkholderia cenocepacia* H111, **genotoxic stress** induces prophages, causing **explosive cell lysis** and release of **extracellular DNA (eDNA)** and membrane vesicles; released eDNA enables **biofilm streamer** development, and streamers are enhanced by genotoxic stress. This links prophage induction to biofilm architecture and suggests antibiotic/SOS-inducing treatments can have unintended biofilm consequences. (herediaponce2023genotoxicstressstimulates pages 1-2)

### 2.3 Prophage-encoded SOS-like systems in taxa lacking canonical SOS (2023)
A *Streptococcus* prophage (Φ1207.3) carries an SOS-like cassette induced by **UV-C**; in engineered strains it increases survival **up to 34-fold** and mutation rate (rifampicin-resistance acquisition) **up to 18-fold**, demonstrating a direct prophage cargo mechanism for stress survival and inducible hypermutability in hosts that typically lack canonical LexA/RecA SOS. (fox2023themef(a) pages 1-3)

### 2.4 Large-scale ecological genomics: prophage ARG enrichment with human impact (2024)
A 2024 Nature Communications study combined **38,605 bacterial genomes**, **1,432 metagenomes**, and **1,186 metatranscriptomes** across 12 habitats and reported increased **abundance, diversity, and activity** of **prophage-encoded antibiotic resistance genes (ARGs)** in **human-impacted habitats**, linking anthropogenic antibiotic exposure to globally altered phage–bacteria interactions and ARG mobilization potential (including functional transfer to heterologous *E. coli* hosts for a subset). (liao2024prophageencodedantibioticresistance pages 1-2)

### 2.5 Population-genomic “species-level” prophage diversity and transmission (2024)
A 2024 *mBio* study built a large *Acinetobacter baumannii* (pro)phage dataset: after QC, **4,152 prophages** were retained from >1,600 genomes and clustered into **963 prophage species** using an operational species definition (**≥95% identity and ≥90% coverage**) while explicitly accounting for host population structure (MLST STs). Most prophage species were **singletons (72%)**, while a few cosmopolitan species were extremely abundant (e.g., Ab_PS8 **633** and Ab_PS9 **547**, together ~28% of prophages). The study reports substantial within-ST gain/loss and that polylysogens carry divergent prophages, consistent with superinfection exclusion and frequent turnover. (tenoriocarnalla2024hostpopulationstructure pages 2-5, tenoriocarnalla2024hostpopulationstructure pages 5-7, tenoriocarnalla2024hostpopulationstructure media 91828813)

### 2.6 Prophage gene expression under replication stress: cryptic prophage induction (2024)
In *E. coli* treated with azidothymidine (AZT), many SOS genes are induced, and the **e14 cryptic prophage** shows strong **LexA-dependent induction**: ~17/22 e14 genes are induced with mean ~36-fold, indicating cryptic prophages can be major SOS-responsive transcriptional modules under replication inhibition. (sass2024thednadamage pages 2-3)

### 2.7 Phage–plasmid hybrids as a key boundary case for “prophage” (2024)
Phage-plasmids blur prophage definitions: they occur at appreciable frequency (~5–7% of all plasmids and of all phages in one large-scale analysis), exchange genes more frequently with plasmids than with phages, and can convert into integrative prophages or “plasmid-only” states via gene loss and acquisition (including defense systems and ARGs). (pfeifer2024phageplasmidspromoterecombination pages 1-2)

---

## 3) Current applications and real-world implementations

1. **Genotoxic exposure biomarkers (environmental/space/medical contexts):** Prophage regulon transcripts and plaques can serve as sensitive readouts of sublethal DNA damage, as demonstrated with IR in *S. oneidensis*. (sweet2023exposureofshewanella pages 2-4)
2. **Antibiotic-resistance surveillance and risk assessment:** Prophage-encoded ARGs are globally enriched and active in human-impacted environments; this provides a framework for integrating prophage cargo into AMR surveillance (metagenomes + metatranscriptomes). (liao2024prophageencodedantibioticresistance pages 1-2)
3. **Population genomics and outbreak context:** Species-level prophage clustering integrated with host ST structure (e.g., *A. baumannii*) provides a practical approach for tracking prophage transmission, gain/loss dynamics, and cosmopolitan high-abundance prophage species that may structure adaptation. (tenoriocarnalla2024hostpopulationstructure pages 2-5, tenoriocarnalla2024hostpopulationstructure media 91828813)
4. **Food/industrial microbiology (biofilms):** Prophage induction can modulate biofilm matrix (eDNA) and morphology (streamers), relevant to chronic contamination/flow environments and to interpreting effects of SOS-inducing antimicrobials. (herediaponce2023genotoxicstressstimulates pages 1-2)

---

## 4) Expert opinions / analysis (authority-weighted)

- A central conceptual update from top-tier 2023 work is that **“universal SOS induction” is incomplete**: prophages can use DNA-damage-independent sensory modules (including quorum sensing) that enable selective prophage activation within polylysogens, shaping inter-prophage competition and output phage populations. (silpe2023smallproteinmodules pages 1-2)
- Mechanistic dissection in 2023 highlights the **importance of host proteostasis systems** (ClpX/ClpP) in prophage induction cascades, revealing an additional “final stage” beyond RecA-triggered repressor cleavage. This is an actionable node for curation and potentially for intervention design. (thabet2023theclpxprotease pages 1-2, thabet2023theclpxprotease pages 2-3)
- Large-scale 2024 genomics argues that prophage content is highly structured: most prophage “species” appear rare/host-restricted, while a small number are globally abundant and broadly distributed; prophage turnover within STs suggests dynamic gain/loss even on relatively short timescales. (tenoriocarnalla2024hostpopulationstructure pages 2-5)

---

## 5) Relevant recent statistics / data points

### Prevalence and diversity
- *A. baumannii* dataset: **4,152 prophages** clustered into **963 prophage species** (≥95% identity, ≥90% coverage) across >1,600 genomes (after QC). (tenoriocarnalla2024hostpopulationstructure pages 2-5)
- **72% singletons** (697/963 prophage species have only one prophage), showing long-tailed prophage diversity; cosmopolitan high-abundance species exist (Ab_PS8 **633**, Ab_PS9 **547**; ~28% together). (tenoriocarnalla2024hostpopulationstructure pages 2-5, tenoriocarnalla2024hostpopulationstructure pages 5-7, tenoriocarnalla2024hostpopulationstructure media 91828813)

### Induction magnitudes and phenotypes
- **ClpX requirement for induction (S. aureus):** ΔclpX yields **~10^8–10^9-fold reduction in phage titres** after induction; ΔclpP shows smaller but still large reductions and altered kinetics. (thabet2023theclpxprotease pages 2-3, thabet2023theclpxprotease pages 1-2)
- **UV-C induced SOS-like prophage cassette:** increases survival up to **34-fold** and mutation rate up to **18-fold**. (fox2023themef(a) pages 1-3)

### Anthropogenic association and datasets
- Prophage-encoded ARG enrichment analysis integrated **38,605 genomes**, **1,432 metagenomes**, **1,186 metatranscriptomes** across 12 habitats and found increased abundance/diversity/activity of prophage-encoded ARGs in **human-impacted habitats**. (liao2024prophageencodedantibioticresistance pages 1-2)

---

## Candidate mechanistic nodes (grouped by type)

### A) Pathways / processes
- SOS response / DNA-damage response (GO:0009432 approximate) (sweet2023exposureofshewanella pages 2-4, sass2024thednadamage pages 6-7)
- Prophage induction / lysogeny-to-lysis transition (label-only) (silpe2023smallproteinmodules pages 1-2)
- Viral integration/excision (label-only; “integration and excision” functions) (sass2024thednadamage pages 2-3, pfeifer2024phageplasmidspromoterecombination pages 9-10)
- Explosive cell lysis; eDNA release; biofilm streamer formation (label-only) (herediaponce2023genotoxicstressstimulates pages 1-2)

### B) Environmental / experimental factors
- Mitomycin C (CHEBI:28146) (herediaponce2023genotoxicstressstimulates pages 1-2, thabet2023theclpxprotease pages 5-6)
- UV-C light (physical factor; label-only) (fox2023themef(a) pages 1-3)
- Ionizing radiation (physical factor; label-only) (sweet2023exposureofshewanella pages 2-4)
- Antibiotics that cause DNA damage/ROS (e.g., quinolones; ciprofloxacin CHEBI:100147) (mahmud2024roleofbacteriophages pages 4-5, bucher2024subtherapeuticconcentrationsof pages 9-11)
- Bile acids / deoxycholate (chemical factor; label-only/CHEBI candidates) (mahmud2024roleofbacteriophages pages 4-5, tenoriocarnalla2024hostpopulationstructure pages 7-11)

### C) Genes/proteins/complexes
- RecA (family anchor UniProt:P0A7G6 in *E. coli*) (sweet2023exposureofshewanella pages 2-4, sass2024thednadamage pages 6-7)
- LexA (family anchor UniProt:P0A7C2 in *E. coli*) (sweet2023exposureofshewanella pages 2-4, sass2024thednadamage pages 2-3)
- CI/cI master repressor (label-only) (silpe2023smallproteinmodules pages 1-2)
- ClpX and ClpP (ClpXP system; label-only) (thabet2023theclpxprotease pages 1-2, thabet2023theclpxprotease pages 2-3)
- Integrase/excisionase exemplars (e14: intE, xisE) (sass2024thednadamage pages 2-3)
- QS-mediated induction modules (VqmAphage–Qtip; DPO cue; label-only) (silpe2023smallproteinmodules pages 1-2)

### D) Chemicals / biomolecules
- DNA (CHEBI:16991) (herediaponce2023genotoxicstressstimulates pages 1-2)
- Extracellular DNA (eDNA; CHEBI:16991 context) (herediaponce2023genotoxicstressstimulates pages 1-2)

---

## Candidate causal edges (evidence-backed)

The following table is designed for direct curator review and potential translation into `data/traits/genomics/prophage.yaml`.

| Subject node (suggested CURIE) | Predicate (causal) | Object node (suggested CURIE) | Evidence (short quote/snippet) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|---|
| temperate phage genome / prophage (METPO:traitmech:000091 candidate; GO:0019068 for viral latency-related process, approximate) | integrates into | bacterial chromosome (GO:0005634 not applicable; label-only) | “temperate phages can remain dormant as prophages passed to host progeny” and prophages are “integrated into the host genome” (silpe2023smallproteinmodules pages 1-2, herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1038/s41586-023-06376-y https://doi.org/10.1038/s41586-023-06376-y (2023); 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Core trait meaning; integration is canonical but some prophages are extrachromosomal, so not universally required. |
| prophage integrase (label-only; often tyrosine recombinase family) | mediates | prophage integration into host genome | e14 induction paper lists “intE, xisE” among prophage genes; prophage/plasmid studies discuss “integration and excision” recombinases as common mobile functions (sass2024thednadamage pages 2-3, pfeifer2024phageplasmidspromoterecombination pages 9-10) | 10.1073/pnas.2407832121 https://doi.org/10.1073/pnas.2407832121 (2024); 10.1038/s41467-024-45757-3 https://doi.org/10.1038/s41467-024-45757-3 (2024) | Mechanistically standard, but direct edge is inferred from integrase/excisionase annotation here rather than a dedicated integration experiment in the retrieved contexts. |
| CI master repressor (label-only; lambda-like cI family) | represses | lytic gene expression / lysis promoter PR (label-only) | “maintained by a phage-encoded repressor (called cI) that binds the lysis promoter (PR) to block lytic gene expression” (silpe2023smallproteinmodules pages 1-2) | 10.1038/s41586-023-06376-y https://doi.org/10.1038/s41586-023-06376-y (2023) | Strong general mechanism for many temperate phages; taxon-specific repressor architectures vary. |
| RecA nucleoprotein filament / RecA* (UniProt:P0A7G6 for E. coli RecA, approximate family grounding) | promotes autocleavage/inactivation of | LexA repressor (UniProt:P0A7C2 for E. coli LexA, approximate family grounding) | “RecA* activation… induces LexA autoproteolysis” (sweet2023exposureofshewanella pages 2-4); SOS response is mediated by “RecA and LexA” (herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1128/aem.01716-22 https://doi.org/10.1128/aem.01716-22 (2023); 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Canonical bacterial SOS edge, important host-side trigger node for prophage induction. |
| DNA damage / replication stress (GO:0006974 approximate) | activates | RecA–LexA SOS response (GO:0009432 DNA repair inducible SOS response) | “AZT treatment blocks replication, creating ssDNA gaps that trigger the classical SOS response” (sass2024thednadamage pages 6-7); IR activates “SOS regulon” (sweet2023exposureofshewanella pages 2-4) | 10.1073/pnas.2407832121 https://doi.org/10.1073/pnas.2407832121 (2024); 10.1128/aem.01716-22 https://doi.org/10.1128/aem.01716-22 (2023) | Strong broad edge; useful upstream environmental/assay factor. |
| RecA* / SOS activation | promotes autocleavage/inactivation of | phage CI repressor (label-only) | “host RecA activation leads to autoproteolysis and inactivation of cI, de-repressing lysis” (silpe2023smallproteinmodules pages 1-2); “RecA also activates self-cleavage of phage repressors” (herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1038/s41586-023-06376-y https://doi.org/10.1038/s41586-023-06376-y (2023); 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Central prophage induction edge; near-universal for classic SOS-inducible prophages, but not all prophages. |
| ClpX AAA+ ATPase/protease specificity factor (label-only; GO:0004176 ATP-dependent peptidase activity, approximate) | inactivates / clears | CI N-terminal cleavage fragment (CI-NTD; label-only) | “ClpX directly recognises the N-terminal DNA-binding fragment (CI NTD)… necessary and sufficient to trigger prophage activation” (thabet2023theclpxprotease pages 1-2); “binding of ClpX to the N-terminal CI fragment is sufficient to inactivate repression” (thabet2023theclpxprotease pages 10-11) | 10.1038/s41467-023-42413-0 https://doi.org/10.1038/s41467-023-42413-0 (2023) | Strong, but demonstrated in Staphylococcus aureus phages Φ11 and 80α; curate as taxon/system-specific unless generalized cautiously. |
| mitomycin C (CHEBI:28146) | induces | SOS response / prophage induction | “MMC... prevents DNA replication and transcription” and is “a common SOS inducer” leading to prophage induction (herediaponce2023genotoxicstressstimulates pages 1-2); reporter assays used MitC to derepress CI (thabet2023theclpxprotease pages 5-6) | 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023); 10.1038/s41467-023-42413-0 https://doi.org/10.1038/s41467-023-42413-0 (2023) | Classic assay trigger; highly curator-relevant as experimental factor. |
| UV-C light (ENVO:01001561 light exposure, approximate; label chemical/physical factor) | induces | prophage SOS-like cassette activity | “SOS-like cassette… induced by UV-C light” and “increases survival up to 34-fold” plus “mutation rate up to 18-fold” (fox2023themef(a) pages 1-3) | 10.1128/jb.00191-23 https://doi.org/10.1128/jb.00191-23 (2023) | Strong but specific to streptococcal prophage Φ1207.3; not a universal prophage response. |
| ionizing radiation (CHEBI:59163 radiation exposure approximate/label-only) | induces | SOS regulon and prophage lytic cycle | “60 min after exposure to acute doses of IR (40, 1, 0.5, and 0.25 Gy), the transcriptional activation of the SOS regulon and the lytic cycle… are comparable” and later prophage transcripts surpass SOS (sweet2023exposureofshewanella pages 2-4) | 10.1128/aem.01716-22 https://doi.org/10.1128/aem.01716-22 (2023) | Good environmental trigger edge with quantitative assay support; species-specific to Shewanella oneidensis MR-1. |
| bile acids / deoxycholate (CHEBI:3098 bile acid, CHEBI:28865 deoxycholate approximate) | induces | prophage activity / induction | gut review notes “bile acids” as non-DNA-damage triggers (mahmud2024roleofbacteriophages pages 4-5); C. difficile study states “DCA presence induces prophages” (tenoriocarnalla2024hostpopulationstructure pages 7-11) | 10.1080/19490976.2024.2390720 https://doi.org/10.1080/19490976.2024.2390720 (2024); 10.3389/fmicb.2024.1374708 https://doi.org/10.3389/fmicb.2024.1374708 (2024) | Trigger may be context- and taxon-dependent; direct mechanistic path remains less resolved than SOS/MMC. |
| antibiotics causing DNA damage or ROS, e.g. quinolones/ciprofloxacin (CHEBI:100147 ciprofloxacin) | induce | prophage activation | quinolones “cause DNA double-strand breaks and can activate Shiga-toxin-encoding E. coli prophages” (mahmud2024roleofbacteriophages pages 4-5); low-dose ciprofloxacin/tetracycline/colistin induce Pf4 via ROS/SOS (bucher2024subtherapeuticconcentrationsof pages 9-11) | 10.1080/19490976.2024.2390720 https://doi.org/10.1080/19490976.2024.2390720 (2024); 10.1101/2024.11.20.624585 https://doi.org/10.1101/2024.11.20.624585 (2024) | Second citation is preprint; curate with caution for specific Pf4 fitness effects. |
| host quorum-sensing autoinducer DPO / VqmAphage pathway (CHEBI label-only for DPO; protein label-only) | activates expression of | Qtip antirepressor / DNA-damage-independent induction module | “Quorum sensing can serve as an SOS-independent trigger… VP882 encodes VqmAPhage, activated by host DPO, which drives qtip expression; Qtip induces lysis” (silpe2023smallproteinmodules pages 1-2) | 10.1038/s41586-023-06376-y https://doi.org/10.1038/s41586-023-06376-y (2023) | Strong recent mechanism, but specific to certain prophages; use as optional branch not universal core. |
| prophage induction (GO:0019076 viral release from host cell approximate) | causes | explosive cell lysis (label-only) | “explosive cell lysis… is a consequence of prophage induction” and functional lytic prophages “cause DNA and MVs release by explosive cell lysis” (herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Good downstream phenotype; evidence from Burkholderia cenocepacia H111. |
| explosive cell lysis | releases | extracellular DNA / eDNA (CHEBI:16991 DNA) | prophage activation “causes DNA and MVs release by explosive cell lysis” (herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Strong within studied system; useful bridge to biofilm-related traits. |
| extracellular DNA (CHEBI:16991) | promotes | biofilm streamer formation (label-only) | “the released DNA enables the strain to develop biofilm streamers, and streamer formation can be enhanced by genotoxic stress” (herediaponce2023genotoxicstressstimulates pages 1-2) | 10.1038/s41522-023-00464-7 https://doi.org/10.1038/s41522-023-00464-7 (2023) | Likely taxon/assay-specific; curator should mark environmental-condition dependence. |
| prophage-encoded SOS-like cassette Φ1207.3 (label-only) | increases | bacterial UV survival and mutation rate | “increases bacterial survival up to 34-fold” and “mutation rate… up to 18-fold” (fox2023themef(a) pages 1-3) | 10.1128/jb.00191-23 https://doi.org/10.1128/jb.00191-23 (2023) | Strong phenotype, but clearly specialized cargo effect rather than defining all prophages. |
| prophage-encoded antibiotic resistance genes (ARG cargo; label-only) | are enriched in | human-impacted environments (ENVO:00000000 label-only) | “significant increase in the abundance, diversity, and activity of prophage-encoded ARGs in human-impacted… habitats”; dataset included “38,605 bacterial genomes, 1,432 metagenomes, 1,186 metatranscriptomes” (liao2024prophageencodedantibioticresistance pages 1-2) | 10.1038/s41467-024-52450-y https://doi.org/10.1038/s41467-024-52450-y (2024) | Ecological association, not single-cell mechanism; valuable higher-level causal context. |
| prophage / superinfection exclusion module (label-only) | reduces susceptibility to | secondary phage infection (superinfection) | review: “Prophages can alter their bacterial hosts to prevent other phages from infecting the same cell” (nair2024presenceofphageplasmids pages 1-2); no same prophage species found twice in one genome, “consistent with superinfection exclusion” (tenoriocarnalla2024hostpopulationstructure pages 5-7) | 10.3390/v16091348 https://doi.org/10.3390/v16091348 (2024); 10.1128/mbio.02377-24 https://doi.org/10.1128/mbio.02377-24 (2024) | First source is review-level, second is genomic consistency rather than direct mechanism. |
| prophage superinfection by Pf4 / SIE state (label-only) | alters / reduces | host fitness and virulence-associated traits | Pf4 superinfection “reduces twitching motility,” changes adhesion, and “increased macrophage uptake and clearance” (bucher2024subtherapeuticconcentrationsof pages 9-11) | 10.1101/2024.11.20.624585 https://doi.org/10.1101/2024.11.20.624585 (2024) | Preprint and Pseudomonas-specific; useful warning/example edge, not yet strong universal curation target. |
| phage-plasmid / prophage-plasmid (label-only) | enables | extrachromosomal prophage maintenance | phage-plasmids are “temperate phages… maintained extrachromosomally” and can persist as “low-copy number, extrachromosomal” prophage forms (pfeifer2024phageplasmidspromoterecombination pages 1-2, nair2024presenceofphageplasmids pages 1-2) | 10.1038/s41467-024-45757-3 https://doi.org/10.1038/s41467-024-45757-3 (2024); 10.1099/mgen.0.001247 https://doi.org/10.1099/mgen.0.001247 (2024) | Important boundary-case edge for trait scope: prophage need not be integrated if maintained episomally. |
| phage-plasmids (label-only) | facilitate dissemination of | ARGs and defense-system genes | P-Ps “mediate transfer of core mobile-element functions, defense systems and antibiotic-resistance genes” (pfeifer2024phageplasmidspromoterecombination pages 1-2); Salmonella screen found repL-positive phage-plasmids including blaCTX-M-15 carrier (nair2024presenceofphageplasmids pages 1-2) | 10.1038/s41467-024-45757-3 https://doi.org/10.1038/s41467-024-45757-3 (2024); 10.1099/mgen.0.001247 https://doi.org/10.1099/mgen.0.001247 (2024) | Strong ecological/evolutionary role but more about hybrid MGEs than all prophages. |
| LexA cleavage / SOS induction | induces expression of | e14 cryptic prophage genes (e.g., intE, xisE, ymf genes) | “virtually 17/22 e14 genes showed LexA-dependent induction (mean ~36-fold)” (sass2024thednadamage pages 2-3) | 10.1073/pnas.2407832121 https://doi.org/10.1073/pnas.2407832121 (2024) | Good evidence for cryptic prophage gene responsiveness; cryptic prophages may be defective and not produce virions. |
| A. baumannii bacterial lineage / ST population structure (NCBITaxon:470) | is associated with gain/loss of | prophage species repertoire | within STs, “prophages are frequently lost and gained” and most prophage species have “narrow host range and are geographically confined” while a few are cosmopolitan (tenoriocarnalla2024hostpopulationstructure pages 2-5, tenoriocarnalla2024hostpopulationstructure pages 1-2) | 10.1128/mbio.02377-24 https://doi.org/10.1128/mbio.02377-24 (2024) | Population-genomic association rather than molecular mechanism; useful macro-scale edge for ecology/transmission subgraph. |


*Table: This table compiles candidate TraitMech causal edges for the microbial trait prophage, spanning core maintenance and induction mechanisms, environmental triggers, downstream phenotypes, and ecological/population-genomic associations. It is designed to support curator review of which edges are strong, taxon-specific, or better treated as higher-level context.*

---

## Warnings / curation cautions

1. **Taxon-specific mechanistic edges:** ClpX-mediated CI-NTD inactivation is strongly supported in *S. aureus* phages Φ11/80α, but it should be curated either as system-specific or as a “possible general mechanism” requiring broader evidence across taxa. (thabet2023theclpxprotease pages 1-2, thabet2023theclpxprotease pages 2-3)
2. **Cryptic prophage induction vs. productive induction:** e14 shows strong LexA-dependent transcriptional induction under replication stress; this should not be equated with virion production without direct evidence in the same context. (sass2024thednadamage pages 2-3)
3. **Preprints:** Some induction/fitness claims (e.g., Pf4 superinfection exclusion impacts under sub-therapeutic antibiotics) are from a 2024 bioRxiv preprint; treat as provisional unless independently corroborated. (bucher2024subtherapeuticconcentrationsof pages 9-11)
4. **Ecological association vs. mechanistic causality:** ARG enrichment in human-impacted environments is robust at scale, but the causal chain from “human impact” → “ARG enrichment in prophages” can involve many mediators (antibiotic exposure, community shifts, selection). Curate as higher-level contextual edges or with “uncertain/associational” flags. (liao2024prophageencodedantibioticresistance pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Silpe JE et al.** *Small protein modules dictate prophage fates during polylysogeny.* Nature. **2023-07**. DOI: **10.1038/s41586-023-06376-y**. https://doi.org/10.1038/s41586-023-06376-y (silpe2023smallproteinmodules pages 1-2)
2. **Thabet MA et al.** *The ClpX protease is essential for inactivating the CI master repressor and completing prophage induction in Staphylococcus aureus.* Nature Communications. **2023-10**. DOI: **10.1038/s41467-023-42413-0**. https://doi.org/10.1038/s41467-023-42413-0 (thabet2023theclpxprotease pages 1-2, thabet2023theclpxprotease pages 2-3)
3. **Sweet P et al.** *Exposure of Shewanella oneidensis MR-1 to Sublethal Doses of Ionizing Radiation Triggers Short-Term SOS Activation and Longer-Term Prophage Activation.* Applied and Environmental Microbiology. **2023-03**. DOI: **10.1128/aem.01716-22**. https://doi.org/10.1128/aem.01716-22 (sweet2023exposureofshewanella pages 2-4)
4. **Heredia-Ponce Z et al.** *Genotoxic stress stimulates eDNA release via explosive cell lysis and thereby promotes streamer formation of Burkholderia cenocepacia H111…* npj Biofilms and Microbiomes. **2023-12**. DOI: **10.1038/s41522-023-00464-7**. https://doi.org/10.1038/s41522-023-00464-7 (herediaponce2023genotoxicstressstimulates pages 1-2)
5. **Fox V et al.** *The mef(A)/msr(D)-carrying streptococcal prophage Φ1207.3 encodes an SOS-like system, induced by UV-C light…* Journal of Bacteriology. **2023-09**. DOI: **10.1128/jb.00191-23**. https://doi.org/10.1128/jb.00191-23 (fox2023themef(a) pages 1-3)
6. **Sass TH, Lovett ST.** *The DNA damage response of Escherichia coli, revisited: Differential gene expression after replication inhibition.* PNAS. **2024-06**. DOI: **10.1073/pnas.2407832121**. https://doi.org/10.1073/pnas.2407832121 (sass2024thednadamage pages 2-3)
7. **Tenorio-Carnalla K et al.** *Host population structure and species resolution reveal prophage transmission dynamics.* mBio. **2024-10**. DOI: **10.1128/mbio.02377-24**. https://doi.org/10.1128/mbio.02377-24 (tenoriocarnalla2024hostpopulationstructure pages 2-5, tenoriocarnalla2024hostpopulationstructure media 91828813)
8. **Liao H et al.** *Prophage-encoded antibiotic resistance genes are enriched in human-impacted environments.* Nature Communications. **2024-09**. DOI: **10.1038/s41467-024-52450-y**. https://doi.org/10.1038/s41467-024-52450-y (liao2024prophageencodedantibioticresistance pages 1-2)
9. **Mahmud MR et al.** *Role of bacteriophages in shaping gut microbial community.* Gut Microbes. **2024-08**. DOI: **10.1080/19490976.2024.2390720**. https://doi.org/10.1080/19490976.2024.2390720 (mahmud2024roleofbacteriophages pages 4-5)
10. **Pfeifer E, Rocha EPC.** *Phage-plasmids promote recombination and emergence of phages and plasmids.* Nature Communications. **2024-02**. DOI: **10.1038/s41467-024-45757-3**. https://doi.org/10.1038/s41467-024-45757-3 (pfeifer2024phageplasmidspromoterecombination pages 1-2)
11. **Nair S et al.** *Presence of phage-plasmids in multiple serovars of Salmonella enterica.* Microbial Genomics. **2024-05**. DOI: **10.1099/mgen.0.001247**. https://doi.org/10.1099/mgen.0.001247 (nair2024presenceofphageplasmids pages 1-2)

---

### Image-supported quantitative evidence
Key quantitative prophage diversity and distribution statistics are supported by figures from Tenorio-Carnalla et al. (Figure set including prophage counts and the singleton-heavy prophage species distribution; cosmopolitan high-abundance Ab_PS8/9). (tenoriocarnalla2024hostpopulationstructure media 91828813)


References

1. (silpe2023smallproteinmodules pages 1-2): Justin E. Silpe, Olivia P. Duddy, Grace E. Johnson, Grace A. Beggs, Fatima A. Hussain, Kevin J. Forsberg, and Bonnie L. Bassler. Small protein modules dictate prophage fates during polylysogeny. Nature, 620:625-633, Jul 2023. URL: https://doi.org/10.1038/s41586-023-06376-y, doi:10.1038/s41586-023-06376-y. This article has 60 citations and is from a highest quality peer-reviewed journal.

2. (pfeifer2024phageplasmidspromoterecombination pages 1-2): Eugen Pfeifer and Eduardo P. C. Rocha. Phage-plasmids promote recombination and emergence of phages and plasmids. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45757-3, doi:10.1038/s41467-024-45757-3. This article has 118 citations and is from a highest quality peer-reviewed journal.

3. (nair2024presenceofphageplasmids pages 1-2): Satheesh Nair, Clare R. Barker, Matthew Bird, David R. Greig, Caitlin Collins, Anaïs Painset, Marie Chattaway, Derek Pickard, Lesley Larkin, Saheer Gharbia, Xavier Didelot, and Paolo Ribeca. Presence of phage-plasmids in multiple serovars of salmonella enterica. May 2024. URL: https://doi.org/10.1099/mgen.0.001247, doi:10.1099/mgen.0.001247. This article has 8 citations and is from a peer-reviewed journal.

4. (sass2024thednadamage pages 2-3): Thalia H. Sass and Susan T. Lovett. The dna damage response of escherichia coli, revisited: differential gene expression after replication inhibition. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2407832121, doi:10.1073/pnas.2407832121. This article has 24 citations and is from a highest quality peer-reviewed journal.

5. (sweet2023exposureofshewanella pages 2-4): Philip Sweet, Jacob Blacutt, Vernita Gordon, and Lydia Contreras. Exposure of shewanella oneidensis mr-1 to sublethal doses of ionizing radiation triggers short-term sos activation and longer-term prophage activation. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01716-22, doi:10.1128/aem.01716-22. This article has 5 citations and is from a peer-reviewed journal.

6. (herediaponce2023genotoxicstressstimulates pages 1-2): Zaira Heredia-Ponce, Eleonora Secchi, Masanori Toyofuku, Gabriela Marinova, Giovanni Savorana, and Leo Eberl. Genotoxic stress stimulates edna release via explosive cell lysis and thereby promotes streamer formation of burkholderia cenocepacia h111 cultured in a microfluidic device. npj Biofilms and Microbiomes, Dec 2023. URL: https://doi.org/10.1038/s41522-023-00464-7, doi:10.1038/s41522-023-00464-7. This article has 14 citations and is from a peer-reviewed journal.

7. (thabet2023theclpxprotease pages 1-2): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

8. (thabet2023theclpxprotease pages 2-3): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

9. (fox2023themef(a) pages 1-3): Valeria Fox, Francesco Santoro, Carmen Apicella, Sara Diaz-Diaz, Josè Manuel Rodriguez-Martínez, Francesco Iannelli, and Gianni Pozzi. The <i>mef</i> (a)/ <i>msr</i> (d)-carrying streptococcal prophage φ1207.3 encodes an sos-like system, induced by uv-c light, responsible for increased survival and increased mutation rate. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00191-23, doi:10.1128/jb.00191-23. This article has 1 citations and is from a peer-reviewed journal.

10. (liao2024prophageencodedantibioticresistance pages 1-2): Hanpeng Liao, Chen Liu, Shungui Zhou, Chunqin Liu, David J. Eldridge, Chaofan Ai, Steven W. Wilhelm, Brajesh K. Singh, Xiaolong Liang, Mark Radosevich, Qiu-e Yang, Xiang Tang, Zhong Wei, Ville-Petri Friman, Michael Gillings, Manuel Delgado-Baquerizo, and Yong-guan Zhu. Prophage-encoded antibiotic resistance genes are enriched in human-impacted environments. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52450-y, doi:10.1038/s41467-024-52450-y. This article has 120 citations and is from a highest quality peer-reviewed journal.

11. (tenoriocarnalla2024hostpopulationstructure pages 2-5): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (tenoriocarnalla2024hostpopulationstructure pages 5-7): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (tenoriocarnalla2024hostpopulationstructure media 91828813): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.

14. (sass2024thednadamage pages 6-7): Thalia H. Sass and Susan T. Lovett. The dna damage response of escherichia coli, revisited: differential gene expression after replication inhibition. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2407832121, doi:10.1073/pnas.2407832121. This article has 24 citations and is from a highest quality peer-reviewed journal.

15. (pfeifer2024phageplasmidspromoterecombination pages 9-10): Eugen Pfeifer and Eduardo P. C. Rocha. Phage-plasmids promote recombination and emergence of phages and plasmids. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45757-3, doi:10.1038/s41467-024-45757-3. This article has 118 citations and is from a highest quality peer-reviewed journal.

16. (thabet2023theclpxprotease pages 5-6): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

17. (mahmud2024roleofbacteriophages pages 4-5): Md. Rayhan Mahmud, Sanjida Khanam Tamanna, Sharmin Akter, Lincon Mazumder, Sumona Akter, Md. Rakibul Hasan, Mrityunjoy Acharjee, Israt Zahan Esti, Md. Saidul Islam, Md. Maksudur Rahman Shihab, Md. Nahian, Rubaiya Gulshan, Sadia Naser, and Anna Maria Pirttilä. Role of bacteriophages in shaping gut microbial community. Gut Microbes, Aug 2024. URL: https://doi.org/10.1080/19490976.2024.2390720, doi:10.1080/19490976.2024.2390720. This article has 63 citations and is from a peer-reviewed journal.

18. (bucher2024subtherapeuticconcentrationsof pages 9-11): Michael J. Bucher, Cristian P. Puente, Naveen Sehdev, and Daniel M. Czyż. Sub-therapeutic concentrations of antibiotics induce prophage-driven superinfection exclusion and fitness cost in pseudomonas aeruginosa. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.20.624585, doi:10.1101/2024.11.20.624585. This article has 4 citations.

19. (tenoriocarnalla2024hostpopulationstructure pages 7-11): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.

20. (thabet2023theclpxprotease pages 10-11): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

21. (tenoriocarnalla2024hostpopulationstructure pages 1-2): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.