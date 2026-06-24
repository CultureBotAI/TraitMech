---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:24:22.810257'
end_time: '2026-06-18T08:40:21.606783'
duration_seconds: 958.8
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lophotrichous
  trait_identifier: traitmech:000058
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: lophotrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with a tuft of multiple flagella at one pole
    of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar
    tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria
    maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar
    filaments acting as locomotory organelles.)'
  causal_graph_summary: 'lophotrichous_polar_tuft: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lophotrichous
- **METPO identifier:** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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
- **Trait label:** lophotrichous
- **METPO identifier:** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **lophotrichous** (METPO: traitmech:000058)

### Executive scope summary
**Trait definition (current use):** *Lophotrichous* describes a **polar flagellar arrangement** in which **multiple flagella emerge as a tuft at (typically) one pole** of a bacterial cell (the trait here is explicitly a *morphology/arrangement* trait, not a motility-mode trait). A leading recent lophotrichous biophysics study (motivated by *Pseudomonas putida*) defines the pattern as “**a tuft of flagella attached near one pole of the cell body**,” with typical *P. putida* counts of **~5–7 flagella per cell** (species-specific statistic). (park2024bundlinginstabilityof pages 2-3)

**Relationship to nearby traits / boundary cases:** Flagellation patterns commonly distinguished in microbiology include **monotrichous** (single polar flagellum), **amphitrichous** (flagella at both poles), **lophotrichous** (polar tuft), and **peritrichous** (flagella distributed across the cell). A widely cited review explicitly lists lophotrichous among the principal patterns and provides representative taxa (e.g., *Helicobacter* spp., some *Pseudomonas*, *Agrobacterium*), while also emphasizing that patterns can be **polar, lateral, medial**, and some bacteria encode **two independent flagellar systems** (e.g., polar + lateral), which can confound simple pattern labels if assay conditions change expression. (schuhmacher2015howbacteriamaintain pages 2-4)

**Boundary cases relevant to curation:**
- **Tuft vs. bundle:** “Tuft” is a morphological arrangement (multiple basal bodies at/near one pole), whereas “bundle” is often a **dynamic functional state** in which multiple filaments rotate coherently; lophotrichous cells frequently show bundling but bundling is not itself the defining morphological criterion. (park2024bundlinginstabilityof pages 2-3, park2024bundlinginstabilityof pages 1-2)
- **Hyperflagellation vs. lophotrichy:** Mutations (e.g., ΔflhG) can yield **hyperflagellated** cells; these may appear “more lophotrichous” but reflect regulatory disruption rather than a stable wild-type pattern. (schuhmacher2015howbacteriamaintain pages 5-7, schuhmacher2015howbacteriamaintain pages 4-5)
- **Taxon-specific outcomes:** The same regulator can have divergent phenotypes in different lophotrichous/polar taxa (e.g., FlhG loss causing hyperflagellation in several γ-proteobacteria, but other outcomes reported in some lophotrichous species). This is a curation warning for universal edges. (schuhmacher2015howbacteriamaintain pages 5-7)

---

## 1) Candidate causal-graph entities (nodes), grouped by type

### A. Phenotype / trait nodes
- **Lophotrichous flagellation** (METPO: traitmech:000058) — polar tuft of multiple flagella. (park2024bundlinginstabilityof pages 2-3)
- **Polar flagellation** (parent concept; METPO parent provided: traitmech:000056) — polar positioning of flagella; includes monotrichous/lophotrichous/amphitrichous patterns. (schuhmacher2015howbacteriamaintain pages 2-4)
- **Flagellar number per cell** (quantitative sub-phenotype; species-specific). (park2024bundlinginstabilityof pages 2-3)

### B. Cellular localizations / structures
- **Cell pole** (label node; consider GO cellular component terms if used consistently in your ontology layer). (arroyoperez2024aconservedcellpole pages 2-3)
- **Bacterial flagellum basal body / MS ring / C ring** (structures; GO terms exist for bacterial-type flagellum organization). (arroyoperez2024aconservedcellpole pages 2-3, schuhmacher2015howbacteriamaintain pages 8-9)

### C. Genes / proteins / complexes (core mechanistic determinants of polar/tuft patterning)
**Core polarity/number regulators (frequently conserved in polar flagellates):**
- **FlhF** — SRP-type GTPase; positive determinant for polar flagellum localization/assembly. (arroyoperez2024aconservedcellpole pages 2-3, schuhmacher2015howbacteriamaintain pages 4-5)
- **FlhG** (aka FleN / MinD2 / YlxH / MotR in various lineages) — MinD-type ATPase; typically negative regulator restricting flagellar number; modulates FlhF. (schuhmacher2015howbacteriamaintain pages 5-7, dornes2024polarconfinementof pages 1-2)

**Pole landmark / organizer proteins:**
- **HubP** (Vibrio pole landmark) and **FimV** (Pseudomonas homolog) — recruit/organize pole-localized systems, including recruitment of FlhG and influencing FlhF polarity. (arroyoperez2024aconservedcellpole pages 1-2, schuhmacher2015howbacteriamaintain pages 7-8)

**Newly characterized licensing/accessory determinant (2024):**
- **FipA (VP2224; DUF2802, single-pass membrane protein)** — membrane-localized factor interacting with FlhF; required for normal FlhF activity and polar flagellar synthesis in multiple tested polar-flagellated species. (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 3-6)

**Flagellar basal-body / rotor components implicated in polar initiation checkpoint:**
- **FliF (MS-ring protein)**, **FliG (C-ring protein)**, **FliM / FliN** — assembly and checkpoint targets in FlhF/FlhG models. (arroyoperez2024aconservedcellpole pages 2-3, schuhmacher2015howbacteriamaintain pages 8-9)

**Transcriptional regulators (link number control to expression):**
- **FleQ / FlrA** (lineage-dependent naming) — master flagellar regulator; inhibited by FlhG in reviewed models. (schuhmacher2015howbacteriamaintain pages 7-8)

### D. Signaling molecules / chemicals
- **GTP/GDP** (FlhF nucleotide cycle). (schuhmacher2015howbacteriamaintain pages 7-8)
- **ATP/ADP** (FlhG nucleotide cycle; membrane-dependent dimerization). (schuhmacher2015howbacteriamaintain pages 5-7)
- **Cyclic di-GMP (c-di-GMP; CHEBI:47016)** — second messenger linking motility vs biofilm programs and polar assembly in some systems. (guan2024flhfaffectsthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)

### E. Environmental / experimental factors (often indirect for morphology)
- **Surface contact / surface sensing** (activates Wsp system in *P. aeruginosa*; affects c-di-GMP and biofilm/motility). (guan2024flhfaffectsthe pages 1-2)
- **Viscosity / mechanical load** (evidence here primarily links to motility mode rather than morphogenesis; see warnings). (schuhmacher2015howbacteriamaintain pages 2-4)

---

## 2) Evidence-backed causal edges (triples)

The following table is designed for direct translation into `data/traits/morphology/lophotrichous.yaml` (with taxon scoping where appropriate).

| Edge (subject–predicate–object) | Evidence (citation id) | Source (first author year, DOI, URL, pub month/year) | Supporting snippet | Notes |
|---|---|---|---|---|
| FlhF — localizes_to/promotes_assembly_at — cell pole | (arroyoperez2024aconservedcellpole pages 2-3, schuhmacher2015howbacteriamaintain pages 4-5) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024; Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “GTP-bound dimeric FlhF localizes to the cell pole and recruits initial flagellar building blocks”; “FlhF is a GTPase… Deletion of flhF causes absence/mislocalization of flagella” | Strong, broadly supported for polar-flagellated bacteria; central positive regulator of polar/tuft initiation. Candidate CURIEs: GO:0001539 flagellum or cilium-dependent cell motility; GO:0044781 bacterial-type flagellum organization; CHEBI:15996 GTP. UniProt taxon-specific accession should be added during species curation. |
| FlhF — recruits — FliG | (arroyoperez2024aconservedcellpole pages 2-3, dornes2024polarconfinementof pages 1-2) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024; Dornes 2024, doi:10.1038/s41467-024-50274-4, https://doi.org/10.1038/s41467-024-50274-4, Jul 2024 | “FlhF binds the C-ring protein FliG via its N-terminus”; “FlhF… binds to FliG” | Strong mechanistic edge for polar assembly initiation. Candidate CURIEs: GO:0044781; label nodes FliG, FlhF pending species-specific UniProt grounding. |
| FlhF:FliG complex — recruits/captures — FliF (MS-ring protein) | (arroyoperez2024aconservedcellpole pages 2-3, dornes2024polarconfinementof pages 1-2) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024; Dornes 2024, doi:10.1038/s41467-024-50274-4, https://doi.org/10.1038/s41467-024-50274-4, Jul 2024 | “FliG captures FliF to promote MS-ring formation”; “recruits a functional FliF/FliG complex to the pole” | Strong mechanistic edge connecting early basal-body assembly to polar patterning. Candidate CURIEs: GO:0044781. |
| HubP/FimV — recruits/anchors — FlhG to cell pole | (arroyoperez2024aconservedcellpole pages 1-2, schuhmacher2015howbacteriamaintain pages 7-8) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024; Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “HubP serves as a polar landmark that recruits ATPases to the pole — including FlhG”; “In Vibrio spp., the polar landmark protein HubP recruits FlhG to the cell pole” | Strong in Vibrio and related pole-organizer systems; taxon-specific landmark names differ (HubP vs FimV). Candidate CURIEs: GO:0005737 cytoplasm; GO:0016020 membrane; cell pole label node if no precise GO chosen. |
| HubP/FimV — promotes — polar localization of FlhF | (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “HubP/FimV act in a separate pathway affecting FlhF polarity: deletion of hubP/fimV reduces or delays FlhF polar/bipolar localization” | Good evidence, but species-dependent magnitude; curate as positive regulator of FlhF polar localization, not absolute requirement in all taxa. Candidate CURIEs: GO:0044781. |
| FipA — interacts_with/promotes_activity_of — FlhF | (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 3-6) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “a direct FlhF interaction partner”; “promotes FlhF targeting/function”; “FipA… interact[s] with… FlhF” | Strong recent evidence; newly identified factor. Label node acceptable if no stable accession yet. Candidate CURIEs: GO:0005515 protein binding; GO:0016021 integral component of membrane (for membrane-associated FipA, if annotation confirmed per species). |
| FipA — required_for — normal polar flagellar synthesis | (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 3-6) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “FipA… is required for normal FlhF activity and polar flagellar synthesis”; “deletion of fipA… abolishes swimming motility and results in cells lacking surface flagella” | Strong in tested taxa (Vibrio parahaemolyticus, Pseudomonas putida, Shewanella putrefaciens); likely conserved in polar monotrichous/lophotrichous bacteria. Candidate CURIEs: GO:0044781; GO:0001539. |
| FipA homolog presence — associated_with — polar flagellates (monotrichous or lophotrichous) | (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 3-6) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “found exclusively in species that are polar flagellates (monotrichous or lophotrichous)” | Association edge, useful but weaker than direct causation; best marked uncertain/phylogenetic. No ontology grounding needed beyond METPO trait nodes. |
| FlhG — negatively_regulates — flagellar number | (schuhmacher2015howbacteriamaintain pages 5-7, schuhmacher2015howbacteriamaintain pages 4-5, arroyoperez2024aconservedcellpole pages 1-2, pradhan2024thebacterialdivision pages 4-8) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015; Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024; Pradhan 2024, doi:10.1016/j.jbc.2024.107117, https://doi.org/10.1016/j.jbc.2024.107117, Apr 2024 | “loss of FlhG causes hyper-flagellation”; “deletion of flhG produces hyper-flagellated strains” | Strong core edge, but note species-specific exceptions (e.g., some Helicobacter outcomes differ). Candidate CURIEs: GO:0044781; GO:1902100 regulation of organelle assembly (broad), CHEBI:30616 ATP. |
| FlhG — stimulates_GTPase_activity_of — FlhF | (schuhmacher2015howbacteriamaintain pages 7-8, schuhmacher2015howbacteriamaintain pages 5-7, dornes2024polarconfinementof pages 1-2) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015; Dornes 2024, doi:10.1038/s41467-024-50274-4, https://doi.org/10.1038/s41467-024-50274-4, Jul 2024 | “FlhG stimulates conversion of GTP-bound FlhF to GDP-bound FlhF”; “FlhG stimulates the GTPase activity of the SRP-type GTPase FlhF” | Strong mechanistic edge. Candidate CURIEs: CHEBI:15996 GTP; CHEBI:17552 GDP; GO:0003924 GTPase activity; GO:0005524 ATP binding. |
| FlhG — promotes — FlhF monomerization/loss of polar localization | (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “stimulating FlhF GTPase activity, causing FlhF monomerization and loss of polar localization” | Strong in current model; likely immediate causal step linking FlhG to number control. Candidate CURIEs: GO:0003924; GO:0005737. |
| FlhG — binds/promotes_assembly_of — FliM/FliN(Y) in nascent C-ring | (schuhmacher2015howbacteriamaintain pages 8-9, dornes2024polarconfinementof pages 1-2) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015; Dornes 2024, doi:10.1038/s41467-024-50274-4, https://doi.org/10.1038/s41467-024-50274-4, Jul 2024 | “Monomeric FlhG binds FliM/FliN(Y)… and promotes their assembly into the nascent C-ring”; “regulates the interaction of the C-ring protein FliG with FliM-FliN” | Moderate-to-strong; details partly model-derived and may vary by species. Candidate CURIEs: GO:0044781. |
| FlhF — hinders/delays — FliG interaction with FliM/FliN until checkpoint release | (dornes2024polarconfinementof media 5e7822c1, dornes2024polarconfinementof pages 1-2) | Dornes 2024, doi:10.1038/s41467-024-50274-4, https://doi.org/10.1038/s41467-024-50274-4, Jul 2024 | Figure summary: “FlhF hinders the interaction between FliG and its C-ring partners FliM/FliN, serving as a regulatory checkpoint” | Supported by figure/model summary; useful but should be tagged model-based unless directly quoted from text during full-paper verification. Candidate CURIEs: GO:0044781. |
| FlhF — recruits — FliF to cell pole via B-domain | (schuhmacher2015howbacteriamaintain pages 4-5) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “The FlhF B-domain can recruit the MS-ring protein FliF to the pole” | Strong but taxon-specific primary example cited in review is Vibrio cholerae. Candidate CURIEs: GO:0044781. |
| FlhG — represses/inhibits — FleQ/FlrA-dependent flagellar gene expression | (schuhmacher2015howbacteriamaintain pages 7-8, arroyoperez2024aconservedcellpole pages 14-15) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015; Arroyo-Pérez 2024, doi:10.7554/eLife.93004.3, https://doi.org/10.7554/elife.93004.3, Dec 2024 | “FlhG also inhibits the ATPase activity of the transcriptional regulator FleQ”; “by repressing further flagellar gene expression via FlrA/FleQ” | Moderate-to-strong; regulator name differs by lineage (FleQ in Pseudomonas/Vibrio-like systems; FlrA in some Vibrio literature). Candidate CURIEs: GO:0006355 regulation of DNA-templated transcription; CHEBI:30616 ATP. |
| c-di-GMP — stabilizes/promotes_polar_recruitment_of — TipF | (schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 2-4) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “TipF binds c-di-GMP… c-di-GMP binding stabilizes TipF, enabling TipN-dependent polar recruitment” | Not FlhF/FlhG-based and not specific to lophotrichous taxa, but relevant as a comparative polar-flagellation mechanism. Mark as adjacent, not core for lophotrichous YAML unless broader parent trait uses it. Candidate CURIEs: CHEBI:47016 cyclic di-GMP. |
| FlhF — interacts_with — HsbR | (guan2024flhfaffectsthe pages 2-6) | Guan 2024, doi:10.1128/AEM.01548-23, https://doi.org/10.1128/aem.01548-23, Jan 2024 | “FlhF physically interacts with the response regulator HsbR” | Strong within Pseudomonas aeruginosa; connection is to lifestyle signaling more than tuft morphology per se. Candidate CURIEs: GO:0005515. |
| FlhF — negatively_modulates — WspR diguanylate cyclase activity | (guan2024flhfaffectsthe pages 6-8, guan2024flhfaffectsthe pages 1-2) | Guan 2024, doi:10.1128/AEM.01548-23, https://doi.org/10.1128/aem.01548-23, Jan 2024 | “the authors propose FlhF inhibits WspR DGC activity”; “FlhF… influences WspR localization and DGC activity via interaction with HsbR” | Good evidence for regulatory linkage to motility/biofilm state; indirect relevance to lophotrichous morphology. Candidate CURIEs: CHEBI:47016 cyclic di-GMP; GO:0004221? not appropriate—leave WspR as label/UniProt candidate. |
| WspR activity — increases — c-di-GMP level | (guan2024flhfaffectsthe pages 6-8, guan2024flhfaffectsthe pages 1-2) | Guan 2024, doi:10.1128/AEM.01548-23, https://doi.org/10.1128/aem.01548-23, Jan 2024 | “WspR, a diguanylate cyclase (DGC), produces c-di-GMP” | Strong signaling edge; useful if incorporating behavioral regulation around polar flagellates. Candidate CURIEs: CHEBI:47016 cyclic di-GMP. |
| Increased c-di-GMP — promotes — biofilm formation / represses motility | (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6) | Guan 2024, doi:10.1128/AEM.01548-23, https://doi.org/10.1128/aem.01548-23, Jan 2024 | “c-di-GMP is a central second messenger controlling flagellum biosynthesis, motility… and biofilm formation”; “deletion of flhF… increases biofilm formation” | Strong general edge; indirect for morphology. Candidate CURIEs: CHEBI:47016 cyclic di-GMP; GO:0042710 biofilm formation. |
| Surface sensing/contact — activates — WspR phosphorylation/clustering | (guan2024flhfaffectsthe pages 1-2) | Guan 2024, doi:10.1128/AEM.01548-23, https://doi.org/10.1128/aem.01548-23, Jan 2024 | “Surface sensing via the Wsp system (WspA) triggers phosphorylation of WspR” | Environmental/regulatory edge for motility-to-biofilm switch, not direct determinant of lophotrichous arrangement. Candidate CURIEs: ENVO:01000739 surface? tentative only; better label-only if uncertain. |
| Surface contact — increases — flagellar number in some taxa | (schuhmacher2015howbacteriamaintain pages 2-4) | Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “some species increase flagellar number upon surface contact to facilitate swarming” | Weak/conditional and often involves lateral flagella rather than polar tuft; do not curate as lophotrichous-specific without taxon-specific primary data. ENVO surface term uncertain. |
| Increased viscosity — promotes — wrapped-mode motility in lophotrichous Pseudomonas putida | (fast2026swimmingpatternsof pages 1-2) | Fast 2026, doi:10.1016/j.bpj.2026.05.032, https://doi.org/10.1016/j.bpj.2026.05.032, May 2026 | “wrapped-mode formation is promoted by increased medium viscosity” | Behavioral edge in a lophotrichous bacterium, but 2026 source is outside requested priority window and concerns motility mode, not arrangement. Keep as ancillary warning-level note. ENVO medium viscosity has no obvious stable CURIE here; label-only. |
| Coordinated flagellar motor rotation — causes — bundled flagellar tuft (push/pull modes) | (park2024bundlinginstabilityof pages 1-2, park2024bundlinginstabilityof pages 2-3) | Park 2024, doi:10.1063/5.0228395, https://doi.org/10.1063/5.0228395, Oct 2024 | “flagella rotate individually yet are typically bundled”; “synchronous motor rotation… yields a cohesive bundle” | Relevant to lophotrichous function, not morphogenesis; useful for downstream motility graph rather than trait-definition graph. Candidate CURIEs: GO:0001539. |
| Lophotrichous arrangement — has_location — one cell pole | (park2024bundlinginstabilityof pages 2-3, schuhmacher2015howbacteriamaintain pages 2-4) | Park 2024, doi:10.1063/5.0228395, https://doi.org/10.1063/5.0228395, Oct 2024; Schuhmacher 2015, doi:10.1093/femsre/fuv034, https://doi.org/10.1093/femsre/fuv034, Nov 2015 | “a tuft of flagella attached near one pole”; lophotrichous listed among “major bacterial flagellation patterns” | Definitional phenotype edge; should already exist in trait graph as morphology relation. Candidate CURIEs: METPO:traitmech:000058; cell pole label node. |
| Pseudomonas putida — typically_has_flagella_count — 5–7 flagella per cell | (park2024bundlinginstabilityof pages 2-3) | Park 2024, doi:10.1063/5.0228395, https://doi.org/10.1063/5.0228395, Oct 2024 | “typical biological count for P. putida of 5–7 flagella per cell” | Quantitative, species-specific statistic useful for examples but not a universal lophotrichous criterion. Candidate CURIEs: NCBITaxon:303 Pseudomonas putida. |


*Table: This table lists evidence-backed candidate causal edges for a TraitMech graph of lophotrichous (polar tuft) flagellation. It prioritizes 2024 mechanistic studies while flagging taxon-specific, indirect, or non-core edges that may need caution during curation.*

**Visual mechanistic support:** A schematic model figure from Dornes et al. (2024, Nature Communications) summarizes a mechanistic sequence for polar confinement and assembly progression involving **FlhF–HubP/FimV anchoring**, **FlhF–FliG binding**, capture of **FliF**, and **FlhG stimulation of FlhF** enabling C-ring progression. This is useful for curating a *coherent chain* of edges even when individual steps may be distributed across text and prior work. (dornes2024polarconfinementof media 5e7822c1)

---

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Discovery of a conserved polar “licensing” factor (FipA) upstream of FlhF
A 2024 eLife study identifies **FipA (VP2224)** as a **membrane-localized FlhF interaction partner** that is **required for normal FlhF activity and polar flagellar synthesis** in multiple polar-flagellated species; FipA is present at the designated pole **before** flagellar synthesis and is proposed to “license” pole-specific assembly. (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 3-6)

### 3.2 Mechanistic clarification of how FlhF confines assembly to the pole via HubP/FimV and early rotor components
A 2024 Nature Communications paper provides a detailed mechanistic model in which FlhF anchors developing structures to the pole landmark **HubP/FimV**, interacts with **FliG**, and recruits a functional **FliF/FliG** complex to the pole; **FlhG’s** modulation of FlhF controls progression of C-ring assembly. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof media 5e7822c1)

### 3.3 Integration with lifestyle signaling: FlhF links polar flagellation to local c-di-GMP regulation in Pseudomonas
A 2024 Applied and Environmental Microbiology paper reports that **FlhF affects c-di-GMP levels and biofilm formation** in *Pseudomonas aeruginosa* by influencing **WspR** (a diguanylate cyclase) via **HsbR**, linking a pole-localized flagellar positioning protein to localized second-messenger signaling. (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6)

---

## 4) Current applications and real-world implementations (where lophotrichy matters)

### 4.1 Biophysics and microswimmer modeling (bioinspired/engineering-relevant)
Lophotrichous bacteria are used as **model systems for multi-flagellar propulsion** because a polar tuft can produce multiple distinct swimming modes (push/pull/wrapping) depending on coordination of motor rotation and hydrodynamic interactions. A 2024 Physics of Fluids study explicitly frames lophotrichous *P. putida* as a model for understanding how **bundled vs unbundled** configurations yield distinct dynamics. (park2024bundlinginstabilityof pages 2-3)

### 4.2 Pathogenesis contexts (indirectly, via polar flagellar machinery)
While the lophotrichous trait itself is morphological, its mechanistic determinants (e.g., FlhF/FlhG-controlled polar assembly; HubP/FimV polarity hubs) are implicated broadly in bacterial motility systems that contribute to host colonization and environmental dissemination. For example, FlhF/FlhG are described as orchestrating flagellar localization and quantity in bacteria, a feature tied to species-specific flagellation patterns used historically as taxonomic criteria. (dornes2024polarconfinementof pages 1-2)

---

## 5) Expert opinions / authoritative synthesis (from primary and review sources)

### 5.1 Flagellation pattern as a species-specific, replicated cellular program
The 2024 Nature Communications paper emphasizes that number and location of flagella (“flagellation pattern”) are **species-specific** and must be replicated each cell cycle; it positions FlhF/FlhG as the central determinants of this pattern. (dornes2024polarconfinementof pages 1-2)

### 5.2 Conserved FlhF/FlhG module with lineage-specific landmarks and transcriptional wiring
A highly cited review describes FlhF/FlhG as executing **opposing roles** in polar flagellation, with FlhF marking assembly sites and FlhG acting through nucleotide- and membrane-dependent cycling plus interactions with structural and transcriptional partners; it explicitly notes unresolved mechanistic details and species-to-species variation (important for curation). (schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 5-7)

---

## 6) Recent statistics and quantitative data

- **Flagella number (example, lophotrichous *Pseudomonas putida*):** typical biological count **5–7 flagella per cell** in a 2024 biophysical study motivated by *P. putida* lophotrichy. (park2024bundlinginstabilityof pages 2-3)
- **Numerical extremes across bacteria (context, not lophotrichous-specific):** a leading review reports that flagella can range from **as few as 1** to **~25 in *Bacillus subtilis*** and **several hundred in swarming *Vibrio parahaemolyticus***, illustrating that “multiple flagella” spans orders of magnitude and should be interpreted in a taxon- and condition-specific way. (schuhmacher2015howbacteriamaintain pages 2-4)

---

## 7) Ontology grounding suggestions (non-exhaustive)

**Trait (given):**
- METPO: **traitmech:000058** (lophotrichous)

**Processes:**
- GO:0001539 **flagellum- or cilium-dependent cell motility** (broad motility term relevant when linking morphology to function) (candidate; verify use in your ontology layer)
- GO:0044781 **bacterial-type flagellum organization** (candidate; widely used for assembly/patterning processes)

**Chemicals:**
- CHEBI:47016 **cyclic di-GMP** (guan2024flhfaffectsthe pages 1-2)
- CHEBI:15996 **GTP**; CHEBI:17552 **GDP**; CHEBI:30616 **ATP** (schuhmacher2015howbacteriamaintain pages 5-7)

**Taxa (examples for scoping):**
- NCBITaxon:303 **Pseudomonas putida** (example lophotrichous organism used for quantitative count) (park2024bundlinginstabilityof pages 2-3)

**Proteins:**
- Use **UniProt** accessions per taxon/strain during curation (FlhF, FlhG, FliF, FliG, FliM, FliN, HubP/FimV, FipA). Current evidence supports label-level nodes; accession grounding should be done at curation time per organism.

---

## 8) Curation warnings / “do not curate yet” items

1. **Avoid over-curating bundling dynamics as morphogenesis:** Evidence supports that lophotrichous bacteria “typically” have bundled flagella during swimming, but bundling/unbundling is a **dynamic functional state** and not equivalent to the presence of a polar tuft (arrangement). Curate bundling edges only if TraitMech intends to capture *functional motility mechanisms*, not strictly morphology. (park2024bundlinginstabilityof pages 2-3, park2024bundlinginstabilityof pages 1-2)
2. **Taxon-specificity of FlhG phenotypes:** The review reports that ΔflhG yields **hyperflagellation in several taxa** but can yield **non-flagellate cells in some lophotrichous species** (e.g., *Helicobacter pylori* noted in the review). Edges like “FlhG negatively regulates flagellar number” are strong but should be annotated with taxon scope/uncertainty notes. (schuhmacher2015howbacteriamaintain pages 5-7)
3. **Indirect environmental edges:** “Surface contact increases flagellar number” is described as conditional and may reflect induction of **lateral flagella** in species with dual systems rather than direct modulation of polar tuft number. Treat as contextual unless you have primary, lophotrichous-specific experimental evidence. (schuhmacher2015howbacteriamaintain pages 2-4)
4. **Figure-derived checkpoint claims:** The FlhF “checkpoint” hindering FliG–FliM/FliN interaction is strongly suggested by the schematic model but should be verified against explicit textual statements (and ideally direct experimental evidence) if making it a central curated edge. (dornes2024polarconfinementof media 5e7822c1)

---

## DOI-first bibliography (with dates and URLs)

1. **Arroyo-Pérez EE** et al. *A conserved cell-pole determinant organizes proper polar flagellum formation.* **eLife** (vol 13). **Dec 2024**. DOI: **10.7554/eLife.93004.3**. https://doi.org/10.7554/elife.93004.3 (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 3-6)
2. **Dornes A** et al. *Polar confinement of a macromolecular machine by an SRP-type GTPase.* **Nature Communications** 15. **Jul 2024**. DOI: **10.1038/s41467-024-50274-4**. https://doi.org/10.1038/s41467-024-50274-4 (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof media 5e7822c1)
3. **Guan C** et al. *FlhF affects the subcellular clustering of WspR through HsbR in Pseudomonas aeruginosa.* **Applied and Environmental Microbiology** 90(1). **Jan 2024**. DOI: **10.1128/aem.01548-23**. https://doi.org/10.1128/aem.01548-23 (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6)
4. **Pradhan P** et al. *The bacterial division protein MinDE has an independent function in flagellation.* **Journal of Biological Chemistry** 300:107117. **Apr 2024**. DOI: **10.1016/j.jbc.2024.107117**. https://doi.org/10.1016/j.jbc.2024.107117 (pradhan2024thebacterialdivision pages 1-2, pradhan2024thebacterialdivision pages 4-8)
5. **Park J** et al. *Bundling instability of lophotrichous bacteria.* **Physics of Fluids** 36(10). **Oct 2024**. DOI: **10.1063/5.0228395**. https://doi.org/10.1063/5.0228395 (park2024bundlinginstabilityof pages 2-3, park2024bundlinginstabilityof pages 1-2)
6. **Schuhmacher JS** et al. *How bacteria maintain location and number of flagella?* **FEMS Microbiology Reviews** 39(6):812–822. **Nov 2015**. DOI: **10.1093/femsre/fuv034**. https://doi.org/10.1093/femsre/fuv034 (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 5-7)

---

### Minimal YAML-oriented takeaway (for `lophotrichous.yaml`)
The most curation-ready, broadly supported core for a lophotrichous causal graph is a **pole-localization and number-control module** centered on **FlhF (SRP-type GTPase)** and **FlhG (MinD-type ATPase)**, with pole landmark proteins (**HubP/FimV**) and a recently identified licensing factor (**FipA**) controlling FlhF’s effective polar activity. Early basal-body/rotor components (**FliF/FliG/FliM/FliN**) form mechanistic intermediates that connect the polarity module to the physical tufted flagellar arrangement. (arroyoperez2024aconservedcellpole pages 14-15, dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof media 5e7822c1)

References

1. (park2024bundlinginstabilityof pages 2-3): Jeungeun Park, Yongsam Kim, Wanho Lee, Veronika Pfeifer, Valeriia Muraveva, Carsten Beta, and Sookkyung Lim. Bundling instability of lophotrichous bacteria. Physics of Fluids, Oct 2024. URL: https://doi.org/10.1063/5.0228395, doi:10.1063/5.0228395. This article has 6 citations and is from a peer-reviewed journal.

2. (schuhmacher2015howbacteriamaintain pages 2-4): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

3. (park2024bundlinginstabilityof pages 1-2): Jeungeun Park, Yongsam Kim, Wanho Lee, Veronika Pfeifer, Valeriia Muraveva, Carsten Beta, and Sookkyung Lim. Bundling instability of lophotrichous bacteria. Physics of Fluids, Oct 2024. URL: https://doi.org/10.1063/5.0228395, doi:10.1063/5.0228395. This article has 6 citations and is from a peer-reviewed journal.

4. (schuhmacher2015howbacteriamaintain pages 5-7): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

5. (schuhmacher2015howbacteriamaintain pages 4-5): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

6. (arroyoperez2024aconservedcellpole pages 2-3): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (schuhmacher2015howbacteriamaintain pages 8-9): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

8. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

9. (arroyoperez2024aconservedcellpole pages 1-2): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

10. (schuhmacher2015howbacteriamaintain pages 7-8): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

11. (arroyoperez2024aconservedcellpole pages 3-6): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

12. (guan2024flhfaffectsthe pages 1-2): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

13. (arroyoperez2024aconservedcellpole pages 14-15): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (pradhan2024thebacterialdivision pages 4-8): Pinkilata Pradhan, Ashoka Chary Taviti, and Tushar Kant Beuria. The bacterial division protein minde has an independent function in flagellation. Journal of Biological Chemistry, 300:107117, Apr 2024. URL: https://doi.org/10.1016/j.jbc.2024.107117, doi:10.1016/j.jbc.2024.107117. This article has 4 citations and is from a domain leading peer-reviewed journal.

15. (dornes2024polarconfinementof media 5e7822c1): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

16. (guan2024flhfaffectsthe pages 2-6): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

17. (guan2024flhfaffectsthe pages 6-8): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

18. (fast2026swimmingpatternsof pages 1-2): Valeriia Fast, Agniva Datta, Jeungeun Park, Robert Grossmann, Veronika Pfeifer, Yongsam Kim, Wanho Lee, Sookkyung Lim, and Carsten Beta. Swimming patterns of a multi-mode bacterial swimmer in fluid shear flow. Biophysical Journal, May 2026. URL: https://doi.org/10.1016/j.bpj.2026.05.032, doi:10.1016/j.bpj.2026.05.032. This article has 0 citations and is from a domain leading peer-reviewed journal.

19. (pradhan2024thebacterialdivision pages 1-2): Pinkilata Pradhan, Ashoka Chary Taviti, and Tushar Kant Beuria. The bacterial division protein minde has an independent function in flagellation. Journal of Biological Chemistry, 300:107117, Apr 2024. URL: https://doi.org/10.1016/j.jbc.2024.107117, doi:10.1016/j.jbc.2024.107117. This article has 4 citations and is from a domain leading peer-reviewed journal.