---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:36:04.008051'
end_time: '2026-06-17T23:50:54.599716'
duration_seconds: 890.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: non halophilic
  trait_identifier: METPO:1000624
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: non_halophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism does not require or prefer
    elevated salt concentrations for growth.
  parent_traits: METPO:1000629
  synonyms: non-halophilic
  evidence_summary: 'DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection
    (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.)
    | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism
    example: Vibrio cholerae non-O1 is described as non-halophilic.)'
  causal_graph_summary: 'non_halophilic_salt_stress_response: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non halophilic
- **METPO identifier:** METPO:1000624
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** non-halophilic
- **Existing evidence:** DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.) | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism example: Vibrio cholerae non-O1 is described as non-halophilic.)
- **Existing causal graph summary:** non_halophilic_salt_stress_response: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **non halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/non_halophilic.yaml`.

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
- **Trait label:** non halophilic
- **METPO identifier:** METPO:1000624
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** non-halophilic
- **Existing evidence:** DOI:10.1128/AEM.01934-12: B. subtilis can attain cellular protection (Supports salt-stress protection mechanisms in a non-halophilic bacterial model.) | PMID:11583854: Vibrio cholerae non-O1, a non-halophilic bacterium (Organism example: Vibrio cholerae non-O1 is described as non-halophilic.)
- **Existing causal graph summary:** non_halophilic_salt_stress_response: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **non halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/non_halophilic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **non halophilic** (METPO:1000624)

### Scope summary (TraitMech-ready)
**Trait definition (curation target):** *Non-halophilic* organisms do **not require** elevated salt for growth and are operationally described as requiring **<1% NaCl** (w/v) for growth. (benaissa2023halotolerantbacillusspecies pages 1-2)

**Distinguish from nearby traits (boundary cases):**
- **Slight halophiles:** optimal growth at **1–3% NaCl**. (aldaghistani2024microbialcommunitiesin pages 3-4)
- **Moderate halophiles:** optimal growth at **3–15% NaCl**. (aldaghistani2024microbialcommunitiesin pages 3-4)
- **Extreme halophiles:** optimal growth at **15–30% NaCl** (and literature also reports optima in molar ranges up to **2.5–5.2 M NaCl ≈ 14.63–30.45%**). (benaissa2023halotolerantbacillusspecies pages 1-2, aldaghistani2024microbialcommunitiesin pages 3-4)
- **Halotolerant:** *no absolute salt requirement* but can tolerate very broad NaCl ranges (reported as ~**1.17–30.45% NaCl**); boundary labels include **“weak halophilic”** (optimum ~**1.17–2.93%**) and **“extremely halotolerant”** (growth interval extends above **2.5 M**). (benaissa2023halotolerantbacillusspecies pages 1-2)

**Interpretation for TraitMech:** Non-halophily is an **environmental preference/requirement trait**, not identical to “salt sensitive” or “lacks osmoadaptation.” Many non-halophiles can transiently tolerate osmotic upshift and deploy conserved osmostress responses; those responses should be captured as mechanistic edges that *support survival without halophily* rather than defining halophily class membership. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12)

---

## 1) Key concepts and current mechanistic understanding (2024 emphasis)

### 1.1 Core osmostress sequence in non-halophilic bacteria
A current synthesis from a 2024 *Microbiology and Molecular Biology Reviews* article frames **cell volume control** as the organizing principle for bacterial osmoregulation, with **cyclic di-AMP** acting as a master regulator in many lineages. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)

**Physical trigger:** On osmotic upshift (e.g., NaCl addition), **water exits the cell within milliseconds**, leading to cytoplasmic volume losses “**up to ~50%**,” reduced turgor, increased macromolecular crowding, and increased intracellular ionic strength. (foster2024bacterialcellvolume pages 6-8)

**Primary ionic response:** Cells rapidly accumulate **K+** (principal cytoplasmic cation), often with **glutamate as counterion** to preserve electroneutrality. Representative cytoplasmic K+ levels summarized include ~**250 mM** (*E. coli*), ~**300 mM** (*B. subtilis*), and ~**500 mM** (*C. glutamicum*, *L. lactis*). (foster2024bacterialcellvolume pages 6-8)

**Secondary osmolyte response:** To avoid toxicity from high ionic strength/K+ overload, many non-halophiles **replace K+ with neutral compatible solutes** (e.g., glycine betaine, trehalose, ectoine, proline). In *B. subtilis*, proline is reported to increase from ~**20 mM to ~500 mM** under osmotic stress. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12)

### 1.2 Molecular systems (transporters, regulators, and parameters)
**Potassium uptake systems:** Reviewed K+ uptake modules include Trk/Ktr systems, KUP-family importers (KimA, KupA, KupB), and high-affinity **Kdp** (P-type ATPase). Quantitative parameters include Ktr/Trk apparent **KM ~1 mM**, Kdp **KM ~2 µM**, and KimA apparent **KM ~140–350 µM**. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)

**Compatible solute transporters and regulation:** Osmotic upshift activates pre-existing compatible-solute transporters (e.g., OpuA and BetP in the review’s scope). Cyclic di-AMP provides an important regulatory layer: it binds target proteins with **KD ~40 nM–8 µM** (depending on target) and can inhibit K+ influx by destabilizing gating interactions. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)

**Transcriptional regulation via cyclic di-AMP:** The review describes cyclic di-AMP binding to **KdpD** (KD ~**2 µM**) to repress **kdpFABC** transcription; cyclic di-AMP-dependent **riboswitches** upstream of kdp/kimA can inhibit transcription. (foster2024bacterialcellvolume pages 8-10)

**OpuA repression via BusR:** BusR binding to cyclic di-AMP (KD ~**10 µM**) inhibits **opuA** transcription and reduces glycine betaine uptake, supporting a mechanistic edge from signaling nucleotide → osmoprotectant uptake. (foster2024bacterialcellvolume pages 10-12)

**Visual schematic support:** Foster et al. provide a schematic of osmoregulation highlighting K+ uptake systems, compatible-solute transporters (OpuA/OpuC), and cyclic-di-AMP-associated regulatory connections. (foster2024bacterialcellvolume media 94161572)

---

## 2) Recent developments (prioritize 2023–2024)

### 2.1 2024: cyclic di-AMP as a quantitative cell-volume master regulator
The 2024 MMBR review integrates biochemical binding constants, transporter kinetics, and phenotypes to argue that cyclic di-AMP is a **master regulator of cell volume**, connecting osmoregulation, cell wall remodeling, and broader physiology. Phenotype-level consequences include:
- **High cyclic di-AMP → reduced K+ import → smaller cells and hypertonic sensitivity**.
- **Low cyclic di-AMP → toxic K+ accumulation → increased cell size, slowed growth, and hypotonic-lysis phenotypes**.
(foster2024bacterialcellvolume pages 6-8)

### 2.2 2024: salt-shock temporal dynamics (omics) and delayed osmolyte switch
A 2024 study of *Halomonas elongata* (moderately halophilic; included here as mechanistic comparator) emphasizes that NaCl shock induces **osmotic stress and oxidative stress**; within an early tolerance range (reported **1–8% NaCl shock**) cells urgently balance osmotic pressure via **Na+/K+ uptake** and increased intracellular amino acids (notably **glutamate/glutamine**). Ectoine accumulation is **delayed** until ~**20 min** post-shock, after which it becomes dominant; reported maximum ectoine productivity was **1450 ± 99 mg/L/h**. (yu2024temporaldynamicsof pages 1-2)

**Curation note:** This is not direct evidence for non-halophily, but it strengthens conserved edges for “salt shock → rapid K+ uptake” and “early ionic response → delayed compatible-solute dominance.” (yu2024temporaldynamicsof pages 1-2)

### 2.3 2024: engineered compatible solutes beyond ectoine (GABA as osmolyte)
A 2024 *Applied and Environmental Microbiology* paper demonstrates that in an ectoine-deficient *H. elongata* background, **Glu overproduction** could restore salt tolerance up to **6% NaCl**, and engineering a salt-inducible glutamate decarboxylase system enabled **GABA accumulation** as a major osmolyte, improving tolerance and reaching **176.94 µmol/g cell dry weight** at **7% NaCl**. (zou2024metabolicengineeringof pages 1-2)

**Curation note:** Taxon- and construct-specific; best used as a “possible osmolyte node/edge” rather than a core non-halophilic mechanism. (zou2024metabolicengineeringof pages 1-2)

### 2.4 2023: mechanosensitive channels and osmolysis susceptibility (real-world bioprocess)
A 2023 *Microbial Cell Factories* study provides experimental evidence linking mechanosensitive channels to survival under hypotonic shock and shows how engineering can repurpose osmoregulation for downstream processing:
- Osmolysis assay: cells grown at elevated salt are “resuspended in distilled water,” increasing turgor pressure and lysing membranes. (adams2023engineeringosmolysissusceptibility pages 2-4)
- **mscL** (and **mscS** in *E. coli*) deletions limit osmolyte export, increasing susceptibility to osmotic lysis. (adams2023engineeringosmolysissusceptibility pages 2-4)
- Quantitative outcomes: ALE increased *Cupriavidus necator* halotolerance from **1.5% to 3.25% NaCl**; engineered strains achieved **47%** to **>90%** osmolytic efficiency in water after growth at elevated NaCl; engineered *E. coli* showed ~**75%** lysis after growth at **4% NaCl**. (adams2023engineeringosmolysissusceptibility pages 1-2)

---

## 3) Current applications and real-world implementations

1. **Industrial downstream processing by osmolysis:** Engineering mechanosensitive channels (MscL/MscS) and evolving higher halotolerance enables efficient cell lysis by hypoosmotic shock, potentially reducing energy/reagent costs relative to mechanical/chemical lysis. (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 2-4)

2. **Osmolyte biotechnology and “compatible solute” platforms:** Salt-stress biology is exploited for production/accumulation of osmoprotectants (ectoine and engineered alternatives such as GABA), including strategies that couple salt-inducible expression with osmolyte accumulation. (zou2024metabolicengineeringof pages 1-2, yu2024temporaldynamicsof pages 1-2)

3. **Trait-informed chassis selection:** Mechanistic distinctions between non-halophilic and salt-adapted organisms inform which chassis are suitable for processes involving high osmolarity or saline waste streams. For example, extreme halophiles can grow at ~**15–30% NaCl**, making them uniquely suited to osmotic shock-based operations that non-halophilic strains resist. (adams2023engineeringosmolysissusceptibility pages 1-2)

---

## 4) Candidate nodes grouped by type (for `non_halophilic.yaml`)

| Node type | Label | Brief definition / role | Recommended grounding(s) | Notes on taxon specificity or uncertainty | Citation |
|---|---|---|---|---|---|
| Trait/phenotype | non-halophilic | Organism does not require or prefer elevated salt concentrations for growth; boundary trait for this curation target | METPO:1000624 | Definition-level node; should be distinguished from halotolerant and halophilic classes | (benaissa2023halotolerantbacillusspecies pages 1-2, aldaghistani2024microbialcommunitiesin pages 3-4) |
| Trait/phenotype | halotolerant | Can tolerate elevated salt without an absolute salt requirement | label-only | Important neighboring trait; not equivalent to non-halophilic | (benaissa2023halotolerantbacillusspecies pages 1-2) |
| Trait/phenotype | slight halophile | Best growth at low but elevated salinity | label-only | Boundary class; useful exclusion from non-halophilic | (aldaghistani2024microbialcommunitiesin pages 3-4) |
| Trait/phenotype | osmotic lysis susceptibility | Increased likelihood of cell lysis after osmotic downshock | label-only | Assay-derived phenotype; not a core definition of non-halophily | (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 2-4) |
| Environmental factors/assays | osmotic upshift | Increase in extracellular osmolality/salinity causing water efflux from cells | GO:0006970 | Generic stress input node; often operationalized by salt addition | (foster2024bacterialcellvolume pages 6-8) |
| Environmental factors/assays | NaCl shock | Sudden increase in sodium chloride concentration | CHEBI:26710 | Assay-style environmental perturbation; widely used in osmoadaptation studies | (yu2024temporaldynamicsof pages 1-2) |
| Environmental factors/assays | hypotonic downshock | Sudden decrease in extracellular osmolality, e.g. resuspension in water | label-only | Common osmolysis assay condition; grounding left label-only | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Environmental factors/assays | osmolysis | Lysis caused by osmotic downshock | label-only | Experimental/industrial process node rather than natural preference trait | (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 2-4) |
| Environmental factors/assays | high salinity environment | Elevated environmental salt concentration | ENVO:candidate | ENVO identifier not confirmed from evidence; candidate environment node only | (adams2023engineeringosmolysissusceptibility pages 1-2, aldaghistani2024microbialcommunitiesin pages 3-4) |
| Biological processes | response to osmotic stress | Cellular response to altered osmotic conditions | GO:0006970 | Broad parent process for osmoadaptation | (foster2024bacterialcellvolume pages 6-8) |
| Biological processes | response to salt stress | Cellular response to elevated salt | GO:0009651 | Broad salt-response process; overlaps with osmotic stress | (foster2024bacterialcellvolume pages 6-8, yu2024temporaldynamicsof pages 1-2) |
| Biological processes | potassium ion transport | Import/export of K+ to regulate osmotic balance and cell volume | GO:0006813 | Strong central process for non-halophilic salt-stress adaptation | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) |
| Biological processes | compatible solute transport | Uptake of organic osmolytes such as glycine betaine/proline/ectoine | GO:candidate | GO term not confirmed from evidence; process is strongly supported conceptually | (foster2024bacterialcellvolume pages 10-12) |
| Biological processes | compatible solute accumulation | Build-up of neutral osmolytes that replace high intracellular K+ | label-only | Mechanistically central, but label-level node may be safer than forcing a GO term | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12) |
| Biological processes | osmolyte efflux during hypotonic shock | Release of intracellular osmolytes to avoid rupture after downshock | label-only | Strongly supported by mechanosensitive-channel experiments | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Biological processes | turgor pressure increase | Physical increase in internal pressure after hypotonic shock | label-only | Biophysical state/process node; no stable ontology ID confirmed from evidence | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Biological processes | macromolecular crowding increase | Increased intracellular crowding after water loss during hypertonic stress | label-only | Biophysical consequence of osmotic upshift | (foster2024bacterialcellvolume pages 6-8) |
| Biological processes | glutamate counterion balancing | Glutamate accumulation/synthesis accompanying K+ uptake to maintain electroneutrality | label-only | Supported mechanistically, but best kept label-only as a sub-process | (foster2024bacterialcellvolume pages 6-8, yu2024temporaldynamicsof pages 1-2) |
| Genes/proteins/complexes | MscL | Large-conductance mechanosensitive channel aiding survival during hypotonic shock | label-only | Gene/protein identity is clear, but no UniProt accession specified in evidence | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Genes/proteins/complexes | MscS | Small-conductance mechanosensitive channel contributing to osmolyte release on downshock | label-only | Evidence from engineered E. coli assay context | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Genes/proteins/complexes | KdpFABC | High-affinity K+ uptake ATPase complex | label-only | Strongly supported transporter complex; lineage-specific use varies | (foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | KdpD | Sensor/regulatory protein controlling kdp expression and binding cyclic di-AMP | label-only | Regulatory protein node; no stable accession in evidence | (foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | KimA | KUP-family potassium importer involved in osmoadaptation | label-only | Best supported in some Gram-positive systems; not universal | (foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | KupA | KUP-family potassium importer | label-only | Taxon distribution varies; leave label-only | (foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | KupB | KUP-family potassium importer | label-only | Taxon distribution varies; leave label-only | (foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | TrkAH | Potassium uptake system active during osmotic upshift | label-only | Broadly used label for transporter/system; accession not specified | (foster2024bacterialcellvolume pages 6-8) |
| Genes/proteins/complexes | KtrAB | Potassium uptake system regulated by cyclic di-AMP in some bacteria | label-only | Strong evidence in c-di-AMP-producing taxa; not universal | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | KtrCD | Potassium uptake system regulated by cyclic di-AMP in some bacteria | label-only | Strong evidence in c-di-AMP-producing taxa; not universal | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) |
| Genes/proteins/complexes | OpuA | Compatible-solute ABC transporter; imports osmoprotectants such as glycine betaine | label-only | Strong evidence especially in Bacillus-related systems | (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume media 94161572) |
| Genes/proteins/complexes | OpuC | Compatible-solute transporter associated with cyclic di-AMP regulation | label-only | Mentioned in review figure/text; taxon distribution varies | (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume media 94161572) |
| Genes/proteins/complexes | BusR | Transcriptional regulator linking cyclic di-AMP to opuA repression | label-only | Strong but lineage-specific regulatory node | (foster2024bacterialcellvolume pages 10-12) |
| Genes/proteins/complexes | glutamate decarboxylase (GAD / gadB / HopgadBmut) | Enzyme converting glutamate to GABA; engineered variant improved salt tolerance in Halomonas study | label-only | Strong engineered-system evidence, but halophile-specific and not a core non-halophilic marker | (zou2024metabolicengineeringof pages 1-2) |
| Transport systems | Trk/Ktr family K+ uptake systems | Rapid-response potassium importers used during osmotic upshift | label-only | Good grouped node if graph avoids over-fragmentation | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) |
| Transport systems | Kdp high-affinity K+ uptake system | High-affinity ATP-driven potassium uptake under low K+/osmotic stress | label-only | Particularly useful when modeling regulatory edges from KdpD and c-di-AMP | (foster2024bacterialcellvolume pages 8-10) |
| Transport systems | KUP family K+ uptake systems (KimA/KupA/KupB) | Potassium uptake transporters contributing to osmoregulation | label-only | Taxon-specific repertoire differs | (foster2024bacterialcellvolume pages 8-10) |
| Transport systems | mechanosensitive channel system | Channel-mediated osmolyte release during hypotonic shock | label-only | Useful grouped node for MscL/MscS branch | (adams2023engineeringosmolysissusceptibility pages 2-4) |
| Small molecules/ions/compatible solutes | cyclic di-AMP | Signaling nucleotide regulating K+ uptake and compatible-solute transport | CHEBI:20198 | Key regulator in many Gram-positive and related bacteria, but not universal across all bacteria | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12) |
| Small molecules/ions/compatible solutes | sodium chloride | Salt used in classification and shock experiments | CHEBI:26710 | Core environmental chemical for this trait class | (benaissa2023halotolerantbacillusspecies pages 1-2, yu2024temporaldynamicsof pages 1-2) |
| Small molecules/ions/compatible solutes | sodium(1+) | Inorganic cation taken up or excluded during salt stress | CHEBI:29101 | Role differs across taxa and salt-adaptation strategies | (yu2024temporaldynamicsof pages 1-2) |
| Small molecules/ions/compatible solutes | potassium(1+) | Principal cytoplasmic cation rapidly accumulated after osmotic upshift | CHEBI:29103 | Central ionic osmoadaptation node | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10) |
| Small molecules/ions/compatible solutes | chloride | Major inorganic counterion in saline environments | CHEBI:17996 | Included as relevant environmental ion; direct mechanistic evidence here is limited | (gaikwad2024soilmicrobiomeapplications pages 10-11) |
| Small molecules/ions/compatible solutes | glycine betaine | Canonical compatible solute protecting cells from osmotic stress | CHEBI:17750 | Strong general osmoprotectant node | (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12) |
| Small molecules/ions/compatible solutes | trehalose | Neutral compatible solute accumulated in some non-halophiles | CHEBI:27082 | Strong general osmolyte, but taxon usage varies | (foster2024bacterialcellvolume pages 6-8) |
| Small molecules/ions/compatible solutes | ectoine | Compatible solute prominent in many halophiles and some bacteria under salt stress | CHEBI:17685 | Strong osmoprotectant, but often more characteristic of halophiles/halotolerant taxa than classic non-halophiles | (zou2024metabolicengineeringof pages 1-2, yu2024temporaldynamicsof pages 1-2) |
| Small molecules/ions/compatible solutes | L-proline | Compatible solute/osmoprotectant accumulated under osmotic stress | CHEBI:26271 | Strong node; can be synthesized or imported depending on taxon | (foster2024bacterialcellvolume pages 10-12) |
| Small molecules/ions/compatible solutes | L-glutamate | Counterion and osmoadaptive metabolite during early salt-stress response | CHEBI:29985 | Strong mechanistic node for electroneutrality and osmoadaptation | (foster2024bacterialcellvolume pages 6-8, yu2024temporaldynamicsof pages 1-2) |
| Small molecules/ions/compatible solutes | L-glutamine | Amino acid pool expanded during NaCl shock response in Halomonas study | CHEBI:58359 | Strong as supportive osmotic-response metabolite, but less universal than glutamate | (yu2024temporaldynamicsof pages 1-2) |
| Small molecules/ions/compatible solutes | GABA | Osmolyte produced from glutamate in engineered salt-tolerance system | CHEBI:16865 | Useful cautionary node: strong experimental support but highly engineered and taxon-specific | (zou2024metabolicengineeringof pages 1-2) |
| Regulatory molecules | high cyclic di-AMP state | Regulatory state associated with reduced K+ import and hypertonic sensitivity | label-only | Phenotypic regulatory-state node; may be too abstract for final graph | (foster2024bacterialcellvolume pages 6-8) |
| Regulatory molecules | low cyclic di-AMP state | Regulatory state associated with toxic K+ accumulation and hypotonic lysis risk | label-only | Phenotypic regulatory-state node; may be too abstract for final graph | (foster2024bacterialcellvolume pages 6-8) |
| Regulatory molecules | c-di-AMP-regulated OpuA repression | Regulatory module linking cyclic di-AMP/BusR to reduced compatible-solute uptake | label-only | Good module-level node if graph uses regulatory modules rather than separate molecular entities | (foster2024bacterialcellvolume pages 10-12) |
| Regulatory molecules | c-di-AMP-regulated Kdp repression | Regulatory module linking cyclic di-AMP/KdpD/riboswitches to reduced K+ uptake gene expression | label-only | Strong but lineage-specific; consider curating only if target graph includes c-di-AMP systems | (foster2024bacterialcellvolume pages 8-10) |


*Table: This table groups candidate TraitMech nodes for the non-halophilic trait by type, with concise roles, suggested ontology grounding, and curation notes. It is useful for selecting which entities are generic enough for a core graph versus taxon-specific, assay-specific, or engineered-system nodes.*

---

## 5) Evidence-backed candidate causal edges (subject–predicate–object triples)

| Subject | Predicate | Object | Node type(s) | Suggested grounding | Evidence snippet / quote | Reference | Curator notes |
|---|---|---|---|---|---|---|---|
| osmotic upshift / NaCl upshift | causes | water efflux and cytoplasmic volume decrease | environmental factor → process/phenotype | ENVO: high salinity environment (candidate); GO:0006970 response to osmotic stress; GO:0009651 response to salt stress | “Under hypertonic stress water exits cells within milliseconds, causing cytoplasmic volume decreases of several percent up to ~50%, a rapid fall in turgor pressure and increased macromolecular crowding and intracellular ionic strength.” (foster2024bacterialcellvolume pages 6-8) | Foster et al., *MMBR*, Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong mechanistic edge for non-halophilic bacteria generally; curate as generic osmotic-stress mechanism associated with, but not defining, non-halophily. |
| osmotic upshift / NaCl shock | induces | rapid K+ uptake | environmental factor → transport process | GO:0006813 potassium ion transport; CHEBI:29103 potassium(1+) | “Cells commonly import large amounts of K+ during osmotic upshift…” (foster2024bacterialcellvolume pages 6-8); “Many microorganisms swiftly uptake K+ ions as an emergency reaction after salt shock” (yu2024temporaldynamicsof pages 1-2) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23; Yu et al., Mar 2024. DOI: 10.1186/s12934-024-02358-5. https://doi.org/10.1186/s12934-024-02358-5 | Strong, broadly supported. Relevant to non-halophiles and halotolerant taxa; not specific enough alone to classify non-halophily. |
| K+ uptake | requires counterion balancing by | glutamate accumulation/synthesis | transport process → metabolite accumulation | CHEBI:29985 L-glutamate; GO:1902476 potassium ion homeostasis (candidate broader process) | “…with glutamate commonly imported or synthesized as the counterion to maintain electroneutrality.” (foster2024bacterialcellvolume pages 6-8); H. elongata shows uptake of Na+/K+ and increased “glutamate and glutamine” after shock (yu2024temporaldynamicsof pages 1-2) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23; Yu et al., Mar 2024. DOI: 10.1186/s12934-024-02358-5. https://doi.org/10.1186/s12934-024-02358-5 | Good edge. Generic in non-halophilic osmoadaptation; Yu evidence is from halophile and should be marked taxon-specific/supporting. |
| high intracellular K+ / high ionic strength | promotes replacement by | compatible solute accumulation | state/process → process | GO:0015948 glycine betaine transport; CHEBI:17750 glycine betaine; CHEBI:27082 trehalose; CHEBI:26271 L-proline; CHEBI:17685 ectoine | “To mitigate cytotoxic effects and high ionic strength, bacteria such as E. coli and B. subtilis accumulate or synthesize neutral compatible solutes… to replace K+ ions.” (foster2024bacterialcellvolume pages 6-8); “osmotic upshift triggers activation of pre-existing compatible solute transporters… compatible solute accumulation is a secondary response following a primary K+ accumulation.” (foster2024bacterialcellvolume pages 10-12) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong conceptual edge. Good candidate parent mechanism node: “compatible solute accumulation.” |
| cyclic di-AMP binding to Trk/Ktr/Kup/Kdp regulators | inhibits | K+ uptake | signaling molecule → transport inhibition | CHEBI:20198 cyclic di-AMP; GO:0006813 potassium ion transport; genes/proteins label-only candidates: TrkAH, KtrAB, KtrCD, KimA, KupA, KupB, KdpFABC | “Many Trk/Ktr gating subunits bind cyclic di-AMP with high affinity (KD 40 nM–8 µM)… high c-di-AMP reduces K+ import” (foster2024bacterialcellvolume pages 6-8); “binding destabilizes gating-transmembrane interactions and inhibits K+ influx” (foster2024bacterialcellvolume pages 8-10) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong for c-di-AMP-producing bacteria; taxon-limited mostly Firmicutes/Actinobacteria/Cyanobacteria per review context. Mark as not universal across all non-halophiles. |
| cyclic di-AMP binding to KdpD / riboswitches | represses transcription of | kdpFABC / kimA | signaling molecule → gene expression regulation | gene labels only: kdpD, kdpFABC, kimA; GO:0019229 regulation of vasculature? no suitable specific GO for bacterial transcription edge here; keep label-based | “KdpD specifically binds cyclic di-AMP… to repress kdpFABC transcription, and riboswitches upstream of kdp and kimA mediate cyclic di-AMP-dependent transcriptional inhibition.” (foster2024bacterialcellvolume pages 8-10) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong but lineage-specific. Good gene-level edges if TraitMech allows labeled bacterial genes without stable cross-taxon IDs. |
| cyclic di-AMP binding / BusR-mediated regulation | inhibits | OpuA-compatible solute uptake / opuA transcription | signaling molecule/regulator → transport/gene expression | CHEBI:20198 cyclic di-AMP; transporter label-only: OpuA; regulator label-only: BusR; GO:0015850 organic osmolyte transport (candidate) | “c-di-AMP binds CBS and RCK_C domains of compatible solute importers (OpuA/OpuC) and negatively regulates their transport. Specifically, BusR binds cyclic di-AMP with KD ~10 µM, inhibiting opuA transcription and reducing glycine betaine uptake.” (foster2024bacterialcellvolume pages 10-12) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong in Bacillus-related systems. Taxon-specific; likely not universal marker of non-halophily. |
| hypotonic shock / osmotic downshock | increases | turgor pressure | environmental factor → physical state | GO:0071470 cellular response to osmotic stress (broad candidate) | “cells are then resuspended in distilled water, causing an increase of turgor pressure due to osmotic shock…” (adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., *Microbial Cell Factories*, Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong assay-specific edge for downshock/osmolysis context; useful for reverse phenotype graph branch. |
| increased turgor pressure after hypotonic shock | causes | cell lysis | physical state → phenotype | label-only phenotype node: osmolysis | “…causing an increase of turgor pressure due to osmotic shock, which lyses the cell membrane.” (adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong in assay context. Lysis is not a normal non-halophilic trait but an experimental phenotype after downshock. |
| MscL / MscS mechanosensitive channel function | enables | osmolyte efflux during hypotonic shock | protein/channel → transport process | gene labels: mscL, mscS; GO:1902600 proton? not suitable; label-only candidate for mechanosensitive channel activity | “mscL is described as ‘a membrane protein that facilitates cell survival during hypotonic shock,’ and deletion of mscL (and mscS in E. coli BL21) ‘limits the ability of cells to export osmolytes in hypotonic solutions’…” (adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong functional edge; mechanism relevant to non-halophilic survival after downshock rather than high-salt growth preference. |
| osmolyte efflux via MscL/MscS | promotes | survival during hypotonic shock | transport process → phenotype | label-only phenotype node: survival under hypotonic shock | “a membrane protein that facilitates cell survival during hypotonic shock” (adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong but assay-context edge. |
| deletion of mscL / mscS | reduces | osmolyte efflux in hypotonic solution | genetic perturbation → transport reduction | gene labels: mscL, mscS | “deletion of mscL (and mscS in E. coli BL21) limits the ability of cells to export osmolytes in hypotonic solutions” (adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong perturbation evidence from engineered strains; curate as assay-specific. |
| deletion of mscL / mscS | increases | osmotic lysis susceptibility | genetic perturbation → phenotype | gene labels: mscL, mscS | “…increasing their susceptibility to osmotic lysis.” E. coli BL21 ΔmscL ΔmscS grown in 4% NaCl showed “75% cell lysis”; combined ALE + ΔmscL in C. necator gave “>90% osmolytic efficiency.” (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 2-4) | Adams et al., Apr 2023. DOI: 10.1186/s12934-023-02064-8. https://doi.org/10.1186/s12934-023-02064-8 | Strong quantitative perturbation edge. Taxa: *E. coli* BL21, *Cupriavidus necator*. |
| NaCl shock | triggers immediate uptake of | Na+ and K+ and augmentation of glutamate/glutamine pools | environmental factor → ion/amino acid accumulation | CHEBI:29101 sodium(1+); CHEBI:29103 potassium(1+); CHEBI:29985 L-glutamate; CHEBI:58359 L-glutamine | “within the cell’s tolerable range (1–8% NaCl shock), H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions and augmenting intracellular amino acid pools, particularly glutamate and glutamine.” (yu2024temporaldynamicsof pages 1-2) | Yu et al., *Microbial Cell Factories*, Mar 2024. DOI: 10.1186/s12934-024-02358-5. https://doi.org/10.1186/s12934-024-02358-5 | Strong primary data, but from moderately halophilic *Halomonas elongata*; curate only as supportive analogy, not direct evidence of non-halophily. |
| NaCl shock | delays then induces | ectoine accumulation | environmental factor → metabolite accumulation | CHEBI:17685 ectoine | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant, and reaching the maximum productivity (1450 ± 99 mg/L/h).” (yu2024temporaldynamicsof pages 1-2) | Yu et al., Mar 2024. DOI: 10.1186/s12934-024-02358-5. https://doi.org/10.1186/s12934-024-02358-5 | Strong but halophile-specific; likely not appropriate as direct non-halophilic trait edge unless graph captures general osmoadaptation alternatives. |
| ectoine deficiency in *Halomonas elongata* | leads to | glutamate accumulation supporting partial salt tolerance | genotype/state → phenotype-supporting metabolite | NCBITaxon:2746 (candidate genus-level not species-specific if unavailable); CHEBI:29985 L-glutamate | “we obtained a mutant, which tolerates 6% NaCl in minimal medium by overproducing L-glutamic acid (Glu). However, this Glu-overproducing strain has a lower tolerance level than the wild-type H. elongata…” (zou2024metabolicengineeringof pages 1-2) | Zou et al., *AEM*, Jan 2024. DOI: 10.1128/aem.01905-23. https://doi.org/10.1128/aem.01905-23 | Strong primary data but clearly halophile-engineering specific; do **not** overgeneralize to non-halophilic trait. |
| engineered glutamate decarboxylase (GAD; HopgadBmut) expression | causes | GABA accumulation | engineered gene/protein → metabolite accumulation | CHEBI:16865 GABA; enzyme label-only: glutamate decarboxylase / gadB | “introduced an engineered salt-inducible HopgadBmut gene… resulting strain exhibits higher salt tolerance… by accumulating high concentration of GABA as an osmolyte in the cell (176.94 µmol/g cell dry weight in minimal medium containing 7% NaCl).” (zou2024metabolicengineeringof pages 1-2) | Zou et al., Jan 2024. DOI: 10.1128/aem.01905-23. https://doi.org/10.1128/aem.01905-23 | Strong engineering edge with numeric phenotype. Taxon- and construct-specific. |
| GABA accumulation | increases | salt tolerance | metabolite accumulation → phenotype | CHEBI:16865 GABA | “the resulting H. elongata GOP-Gad strain exhibits higher salt tolerance than the GOP strain by accumulating high concentration of GABA as an osmolyte…” (zou2024metabolicengineeringof pages 1-2) | Zou et al., Jan 2024. DOI: 10.1128/aem.01905-23. https://doi.org/10.1128/aem.01905-23 | Strong but engineered halophile evidence only; uncertain for curation into a non-halophilic core graph. |
| non-halophilic trait | defined by | requirement for <1% NaCl | trait class → environmental preference | METPO:1000624; CHEBI:26710 sodium chloride | “Non-halophilic organisms require less than 1% NaCl.” (benaissa2023halotolerantbacillusspecies pages 1-2) | Benaissa et al., Dec 2023. DOI: 10.15832/ankutbd.1249228. https://doi.org/10.15832/ankutbd.1249228 | Useful scope/boundary definition rather than mechanistic edge. Supports trait curation metadata. |
| slight halophily | has optimum growth at | 1–3% NaCl | trait class → environmental range | CHEBI:26710 sodium chloride | “slight halophiles (1–3% NaCl), moderate halophiles (3–15% NaCl), and extreme halophiles (15–30% NaCl)” (aldaghistani2024microbialcommunitiesin pages 3-4) | Al-Daghistani et al., Jun 2024. DOI: 10.1080/19420889.2024.2369782. https://doi.org/10.1080/19420889.2024.2369782 | Boundary-case row; helps distinguish non-halophilic from neighboring classes. Not a causal mechanism. |
| halotolerant trait | does not require but tolerates | elevated NaCl | trait class → environmental range | CHEBI:26710 sodium chloride | “halotolerant organisms — no absolute salt requirement but tolerate ~1.17–30.45% NaCl” (benaissa2023halotolerantbacillusspecies pages 1-2) | Benaissa et al., Dec 2023. DOI: 10.15832/ankutbd.1249228. https://doi.org/10.15832/ankutbd.1249228 | Important exclusion criterion: non-halophilic ≠ halotolerant, though many non-halophiles may show limited salt tolerance. |
| high c-di-AMP level | decreases | cell size / increases hypertonic sensitivity | signaling state → phenotype | CHEBI:20198 cyclic di-AMP | “high c-di-AMP reduces K+ import (cells shrink, are hypertonic-sensitive…) whereas low c-di-AMP leads to toxic K+ accumulation, increased cell size, slowed growth and lysis under hypotonic conditions.” (foster2024bacterialcellvolume pages 6-8) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Useful phenotype-level consequence edge if graph includes regulatory state nodes. |
| low c-di-AMP level | causes | toxic K+ accumulation and lysis under hypotonic conditions | signaling state → phenotype | CHEBI:20198 cyclic di-AMP; CHEBI:29103 potassium(1+) | “low c-di-AMP leads to toxic K+ accumulation, increased cell size, slowed growth and lysis under hypotonic conditions.” (foster2024bacterialcellvolume pages 6-8) | Foster et al., Jun 2024. DOI: 10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 | Strong for c-di-AMP-containing taxa; not universal across all bacteria. |


*Table: This table lists candidate TraitMech-style causal edges for the non-halophilic trait, centered on osmotic/salt stress responses, with grounded identifiers, supporting quotes, citations, and curation notes. It is designed to help decide which edges are strong, generic candidates versus taxon-specific or assay-specific observations.*

**Schematic support for curation:** A figure in Foster et al. summarizes K+ uptake systems, compatible-solute uptake (OpuA/OpuC), and cyclic di-AMP regulatory points, providing a visual cross-check for node inclusion and connectivity. (foster2024bacterialcellvolume media 94161572)

---

## 6) Relevant recent statistics and quantitative data points (curation-relevant)

- **Non-halophilic definition threshold:** <**1% NaCl** requirement (operational). (benaissa2023halotolerantbacillusspecies pages 1-2)
- **Halophile optima classes:** slight **1–3%**, moderate **3–15%**, extreme **15–30% NaCl** (optimum-based). (aldaghistani2024microbialcommunitiesin pages 3-4)
- **Osmotic upshift physical effect:** cytoplasmic volume decrease “up to **~50%**”. (foster2024bacterialcellvolume pages 6-8)
- **Typical cytoplasmic K+:** ~**250 mM** (*E. coli*), ~**300 mM** (*B. subtilis*), ~**500 mM** (*C. glutamicum*, *L. lactis*). (foster2024bacterialcellvolume pages 6-8)
- **Transport kinetics:** Ktr/Trk **KM ~1 mM**; Kdp **KM ~2 µM**; KimA **KM ~140–350 µM**. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)
- **Signaling binding constants:** c-di-AMP target binding **KD ~40 nM–8 µM**; BusR–c-di-AMP **KD ~10 µM**; KdpD–c-di-AMP **KD ~2 µM**. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12)
- **Compatible solute magnitude example:** proline ~**20 mM → ~500 mM** in *B. subtilis* under osmotic stress. (foster2024bacterialcellvolume pages 10-12)
- **Salt shock timing/productivity example (halophile comparator):** ectoine delayed until ~**20 min**, max productivity **1450 ± 99 mg/L/h** in *H. elongata*. (yu2024temporaldynamicsof pages 1-2)
- **Industrial osmolysis outcomes:** ALE increased halotolerance **1.5% → 3.25% NaCl**; lysis efficiencies **47%**, **>90%**, and **~75%** in engineered hosts/conditions. (adams2023engineeringosmolysissusceptibility pages 1-2)
- **Engineered osmolyte statistic (halophile comparator):** GABA accumulation **176.94 µmol/g CDW** at **7% NaCl** and improved tolerance. (zou2024metabolicengineeringof pages 1-2)

---

## 7) Expert interpretation / analysis (authoritative source synthesis)

A 2024 expert review synthesizes that bacterial osmoregulation is not only a stress response but a quantitatively tuned **cell-volume control system**, where (i) rapid K+ uptake is an emergency response, (ii) compatible solutes provide a lower-toxicity replacement strategy, and (iii) cyclic di-AMP in many lineages functions as a central regulator coordinating K+ influx, osmolyte uptake, and downstream phenotypes such as osmotic sensitivity and viability. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12)

For TraitMech, this supports a mechanistic view: **non-halophily** can be consistent with robust osmostress machinery; the trait is best curated as an **environmental preference** node connected to **salt/osmotic-stress response capacity**, rather than as a direct mechanistic absence. (benaissa2023halotolerantbacillusspecies pages 1-2, foster2024bacterialcellvolume pages 6-8)

---

## 8) Curation warnings (do-not-curate / curate-as-uncertain)

1. **Do not equate non-halophilic with salt-intolerant.** The core osmostress pathway (water efflux → K+ uptake → compatible solute accumulation) is broadly conserved and is explicitly discussed for non-halophiles such as *E. coli* and *B. subtilis* in a 2024 authoritative review. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 10-12)

2. **Lineage specificity of cyclic di-AMP.** Cyclic di-AMP regulation is strong evidence in taxa that use this nucleotide (Firmicutes/Actinobacteria/Cyanobacteria emphasized in the review), but it is not universal across all bacteria; curate c-di-AMP branches as conditional modules if TraitMech is meant to be pan-bacterial. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)

3. **Mechanosensitive channel edges are assay- and context-specific.** MscL/MscS deletion → lysis susceptibility is strong evidence but pertains to **hypotonic downshock/osmolysis** (industrial/experimental), not directly to growth preference at low salt. Curate under an “osmotic downshock” subgraph if included. (adams2023engineeringosmolysissusceptibility pages 2-4, adams2023engineeringosmolysissusceptibility pages 1-2)

4. **Halophile-focused osmolyte engineering (ectoine/GABA) should be marked taxon-specific.** Zou 2024 and Yu 2024 are compelling mechanistic examples but are centered on *Halomonas elongata* (moderately halophilic). Use as supporting evidence for general osmolyte nodes (ectoine, glutamate, GABA) but mark edges as taxon-/system-specific. (zou2024metabolicengineeringof pages 1-2, yu2024temporaldynamicsof pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)

1. Foster AJ, van den Noort M, Poolman B. **Bacterial cell volume regulation and the importance of cyclic di-AMP.** *Microbiology and Molecular Biology Reviews.* **Jun 2024**. DOI: **10.1128/mmbr.00181-23**. URL: https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume media 94161572)

2. Yu J, Zhang Y, Liu H, et al. **Temporal dynamics of stress response in Halomonas elongata to NaCl shock: physiological, metabolomic, and transcriptomic insights.** *Microbial Cell Factories.* **Mar 2024**. DOI: **10.1186/s12934-024-02358-5**. URL: https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2)

3. Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H. **Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in an ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology.* **Jan 2024**. DOI: **10.1128/aem.01905-23**. URL: https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)

4. Al-Daghistani HI, Zein S, Abbas MA. **Microbial communities in the Dead Sea and their potential biotechnological applications.** *Communicative & Integrative Biology.* **Jun 2024**. DOI: **10.1080/19420889.2024.2369782**. URL: https://doi.org/10.1080/19420889.2024.2369782 (aldaghistani2024microbialcommunitiesin pages 3-4)

5. Adams JD, Sander KB, Criddle CS, Arkin AP, Clark DS. **Engineering osmolysis susceptibility in Cupriavidus necator and Escherichia coli for recovery of intracellular products.** *Microbial Cell Factories.* **Apr 2023**. DOI: **10.1186/s12934-023-02064-8**. URL: https://doi.org/10.1186/s12934-023-02064-8 (adams2023engineeringosmolysissusceptibility pages 1-2, adams2023engineeringosmolysissusceptibility pages 2-4)

6. Benaïssa A, Basseddik A, Chegga A, Djebbar R. **Halotolerant Bacillus Species as Plant Growth Promoting Rhizobacteria from Hyper–Arid Area of Algeria.** *Tarım Bilimleri Dergisi.* **Dec 2023**. DOI: **10.15832/ankutbd.1249228**. URL: https://doi.org/10.15832/ankutbd.1249228 (benaissa2023halotolerantbacillusspecies pages 1-2, benaissa2023halotolerantbacillusspecies pages 2-4)


References

1. (benaissa2023halotolerantbacillusspecies pages 1-2): Asmaa BENAİSSA, Aida BASSEDDİK, Abdallah CHEGGA, and Réda DJEBBAR. Halotolerant bacillus species as plant growth promoting rhizobacteria from hyper – arid area of algeria. Tarım Bilimleri Dergisi, Dec 2023. URL: https://doi.org/10.15832/ankutbd.1249228, doi:10.15832/ankutbd.1249228. This article has 5 citations.

2. (aldaghistani2024microbialcommunitiesin pages 3-4): Hala I. Al-Daghistani, Sima Zein, and Manal A. Abbas. Microbial communities in the dead sea and their potential biotechnological applications. Communicative & Integrative Biology, Jun 2024. URL: https://doi.org/10.1080/19420889.2024.2369782, doi:10.1080/19420889.2024.2369782. This article has 23 citations and is from a peer-reviewed journal.

3. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

4. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

5. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (foster2024bacterialcellvolume media 94161572): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

8. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

9. (adams2023engineeringosmolysissusceptibility pages 2-4): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

10. (adams2023engineeringosmolysissusceptibility pages 1-2): Jeremy David Adams, Kyle B. Sander, Craig S. Criddle, Adam P. Arkin, and Douglas S. Clark. Engineering osmolysis susceptibility in cupriavidus necator and escherichia coli for recovery of intracellular products. Microbial Cell Factories, Apr 2023. URL: https://doi.org/10.1186/s12934-023-02064-8, doi:10.1186/s12934-023-02064-8. This article has 16 citations and is from a peer-reviewed journal.

11. (gaikwad2024soilmicrobiomeapplications pages 10-11): Aniket Sunil Gaikwad, BD Bhakare, BM Kamble, RS Thakare, and AG Durgude. Soil microbiome: applications and mechanisms for salinity stress mitigation in plant and soil ecology: a review. International Journal of Advanced Biochemistry Research, 8:923-946, Jan 2024. URL: https://doi.org/10.33545/26174693.2024.v8.i3k.875, doi:10.33545/26174693.2024.v8.i3k.875. This article has 5 citations.

12. (benaissa2023halotolerantbacillusspecies pages 2-4): Asmaa BENAİSSA, Aida BASSEDDİK, Abdallah CHEGGA, and Réda DJEBBAR. Halotolerant bacillus species as plant growth promoting rhizobacteria from hyper – arid area of algeria. Tarım Bilimleri Dergisi, Dec 2023. URL: https://doi.org/10.15832/ankutbd.1249228, doi:10.15832/ankutbd.1249228. This article has 5 citations.