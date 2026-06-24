---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:44:28.953971'
end_time: '2026-06-17T22:56:07.950903'
duration_seconds: 699.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: metal tolerant
  trait_identifier: traitmech:000012
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: metal_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism grows in the presence
    of elevated concentrations of toxic heavy-metal or metalloid ions, typically via
    efflux-based resistance determinants (RND-family CBA pumps, P-type ATPases, and
    cation diffusion facilitators).
  parent_traits: METPO:1000059
  synonyms: metallophilic, heavy metal resistant
  evidence_summary: 'PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell
    division superfamily, P-type ATPases, cation diffusion facilitator and chromate
    proteins (Review of efflux-mediated heavy-metal resistance supports active metal
    export as the dominant prokaryotic tolerance mechanism.) | DOI:10.3389/fmicb.2020.00047:
    This metallophilic strain BS1, harbors numerous gene clusters encoding metal-resistance
    determinants enabling detoxification of transition metal ions and complexes (Organism
    example: Cupriavidus metallidurans is the model metallophilic bacterium tolerating
    many toxic metals via dedicated resistance gene clusters.)'
  causal_graph_summary: 'metal_tolerance_efflux_detoxification: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metal tolerant
- **METPO identifier:** traitmech:000012
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism grows in the presence of elevated concentrations of toxic heavy-metal or metalloid ions, typically via efflux-based resistance determinants (RND-family CBA pumps, P-type ATPases, and cation diffusion facilitators).
- **Parent traits:** METPO:1000059
- **Synonyms:** metallophilic, heavy metal resistant
- **Existing evidence:** PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Review of efflux-mediated heavy-metal resistance supports active metal export as the dominant prokaryotic tolerance mechanism.) | DOI:10.3389/fmicb.2020.00047: This metallophilic strain BS1, harbors numerous gene clusters encoding metal-resistance determinants enabling detoxification of transition metal ions and complexes (Organism example: Cupriavidus metallidurans is the model metallophilic bacterium tolerating many toxic metals via dedicated resistance gene clusters.)
- **Existing causal graph summary:** metal_tolerance_efflux_detoxification: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **metal tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/metal_tolerant.yaml`.

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
- **Trait label:** metal tolerant
- **METPO identifier:** traitmech:000012
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism grows in the presence of elevated concentrations of toxic heavy-metal or metalloid ions, typically via efflux-based resistance determinants (RND-family CBA pumps, P-type ATPases, and cation diffusion facilitators).
- **Parent traits:** METPO:1000059
- **Synonyms:** metallophilic, heavy metal resistant
- **Existing evidence:** PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Review of efflux-mediated heavy-metal resistance supports active metal export as the dominant prokaryotic tolerance mechanism.) | DOI:10.3389/fmicb.2020.00047: This metallophilic strain BS1, harbors numerous gene clusters encoding metal-resistance determinants enabling detoxification of transition metal ions and complexes (Organism example: Cupriavidus metallidurans is the model metallophilic bacterium tolerating many toxic metals via dedicated resistance gene clusters.)
- **Existing causal graph summary:** metal_tolerance_efflux_detoxification: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **metal tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/metal_tolerant.yaml`.

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


## Microbial TraitMech Curation Report: **metal tolerant** (METPO: traitmech:000012)

### 0) Executive scope summary
The METPO trait **metal tolerant** represents an **assay-observed phenotype** in which a microorganism **grows and/or maintains viability** in the presence of **toxic, elevated concentrations of heavy-metal or metalloid ions** (above typical trace homeostasis ranges). Current mechanistic understanding emphasizes that tolerance commonly emerges from **active export (efflux)** combined with **compartment-specific detoxification/redox transformations** and **buffering/sequestration by cytoplasmic or periplasmic ligands**; regulation is frequently mediated by **metal-sensing transcription factors and two-component systems** that couple **metal exposure → induced expression** of tolerance determinants. This trait should be distinguished from (i) *metal requirement/trace-metal homeostasis* (growth needs) and (ii) *immobilization-only processes* (e.g., extracellular precipitation) that may reduce bioavailable metal without demonstrating **cell growth under exposure**. Evidence across model systems supports efflux-based determinants as dominant contributors to tolerance, with additional layers (oxidation, buffering, repair) providing robustness and network effects. (shafiq2024mechanismsoftoxicity pages 9-10, nies2024aflowequilibrium pages 1-3, hirth2023fullcopperresistance pages 9-11)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Phenotype definition (what is being measured)
*Metal tolerance* is operationally quantified via **growth curves**, **MIC**, or **IC50-like dose–response metrics** under defined metal exposures. For example, copper resistance in *Cupriavidus metallidurans* is quantified using IC50 values (Table 1 in the source includes IC50 (mM) for multiple mutants), enabling attribution of phenotype contributions to specific resistance subsystems. (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance media af275243)

In cadmium-resistant *Pseudomonas aeruginosa* CD3, phenotyping was performed via **liquid MIC determination** in a modified medium designed to avoid Cd-phosphate precipitation, and the study linked growth/survival at high Cd concentrations to an **efflux-dependent mechanism** supported by metal partitioning measurements. (chatterjee2024multimodalcadmiumresistance pages 14-15)

### 1.2 Mechanistic classes relevant to TraitMech
**(A) Efflux/export (dominant in many bacteria):**
- **RND/CBA (CzcCBA, CusCBA)** transenvelope systems in Gram-negative bacteria export metals from the periplasm to the extracellular milieu. (nies2024aflowequilibrium pages 1-3, hirth2023fullcopperresistance pages 16-18)
- **P-type ATPases** (e.g., CupA, ZntA, CadA) export metal ions across the inner membrane (often cytoplasm → periplasm or out). (hirth2023fullcopperresistance pages 16-18, hirth2023fullcopperresistance pages 1-3, nies2024aflowequilibrium pages 1-3)
- **CDF (cation diffusion facilitator) family exporters** also contribute to divalent metal tolerance in some taxa. (nies2024aflowequilibrium pages 1-3)

**(B) Enzymatic detoxification / redox transformation:**
- **Arsenate reduction**: ArsC reduces As(V) to As(III), which is then extruded by arsenite efflux pumps, forming a canonical detoxification loop. (shafiq2024mechanismsoftoxicity pages 9-10)
- **Copper detox via periplasmic oxidation**: CopA oxidizes periplasmic Cu(I) to Cu(II), reducing Cu(I)-associated damage and interacting functionally with efflux and buffering systems. (hirth2023fullcopperresistance pages 16-18, hirth2023fullcopperresistance pages 1-3)

**(C) Sequestration/buffering:**
- **Glutathione** and **polyphosphate** are described as cytoplasmic metal-binding components that influence zinc homeostasis/tolerance through effects on metal pools and turnover. (nies2024aflowequilibrium pages 1-3)
- Copper resistance in *C. metallidurans* involves **network interactions** in which glutathione contributes to resistance alongside efflux/oxidation systems. (hirth2023fullcopperresistance pages 11-12, hirth2023fullcopperresistance pages 1-3)

**(D) Regulation and sensing:**
- **CusSR** in *E. coli* directly connects periplasmic Cu sensing to expression of cus efflux genes; the study concludes that CusSR controlling **cusF and cusCBA** “does indeed sense periplasmic copper ions.” (rismondo2023thesensoryhistidine pages 1-2)
- In *P. aeruginosa* CD3, **CzcS/CzcR** regulates **czcCBA**, linking metal sensing to efflux activation. (chatterjee2024multimodalcadmiumresistance pages 14-15)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Quantitative causal evidence for horizontal gene transfer (HGT) as a tolerance accelerator (2024)
A strong, direct causal demonstration comes from mercury tolerance in nitrogen-fixing rhizobia: **only strains possessing a Mer operon exhibited “10-fold increased tolerance to Hg,”** and **plasmid transfer of the Mer operon** to low-tolerant strains caused an **immediate increase in Hg tolerance**, indicating the operon is sufficient to confer hyper-tolerance. (BMC Microbiology; published Jul 2024; https://doi.org/10.1186/s12866-024-03391-5) (bhat2024horizontalgenetransfer pages 1-2)

This provides high-confidence edges for TraitMech: *HGT of operon → tolerance phenotype* and *Hg stress → induced operon expression*. (bhat2024horizontalgenetransfer pages 1-2)

### 2.2 Systems-level view of metal tolerance as a network property (2023–2024)
Copper resistance in *C. metallidurans* is explicitly framed as the emergent product of multiple interacting determinants, including a **PIB1-type Cu(I)-exporting ATPase (CupA)**, **periplasmic Cu(I)-oxidase (CopA)**, **CusCBA transenvelope efflux**, **glutathione (GSH)**, and **Gig**. The paper ranks the contributions and emphasizes that “Copper resistance is thus the result of an interplay of many systems.” (Applied and Environmental Microbiology; published Jun 2023; https://doi.org/10.1128/aem.00567-23) (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 9-11)

A complementary 2024 study on zinc in *C. metallidurans* advances a **kinetic/flux perspective** (“flow equilibrium”) where **simultaneous uptake and efflux reactions** plus **cytoplasmic binding components** yield stable cellular Zn pools, showing tolerance/homeostasis can be modeled with quantitative transport turnover rather than single determinants. (Journal of Bacteriology; published May 2024; https://doi.org/10.1128/jb.00080-24) (nies2024aflowequilibrium pages 1-3)

### 2.3 Mechanistic granularity in metal sensing (2023)
A 2023 mechanistic study provides direct evidence for the widely used regulatory motif **two-component system → periplasmic metal signal → efflux gene induction**: CusSR in *E. coli* “controls expression of cusF and cusCBA” and “does indeed sense periplasmic copper ions.” (Microbiology Spectrum; published Apr 2023; https://doi.org/10.1128/spectrum.00291-23) (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 8-10)

### 2.4 New phenotype/assay considerations: medium chemistry and inoculum effects (2024)
In cadmium tolerance studies, investigators explicitly addressed metal speciation artifacts (Cd-phosphate precipitation) by using phosphate-eliminated medium and showed **inoculum density effects** on measured MIC, emphasizing that metal-tolerance traits can be **assay-sensitive** and require careful standardization for curation. (Scientific Reports; published Dec 2024; https://doi.org/10.1038/s41598-024-80754-y) (chatterjee2024multimodalcadmiumresistance pages 14-15)

---

## 3) Current applications and real-world implementations

### 3.1 Bioremediation and mine/industrial waste contexts
Genomes of mine-isolated strains often encode multiple tolerance determinants, consistent with deployment/selection in contaminated environments. For example, *Cupriavidus necator* C39 (isolated from a gold/copper mine) is reported to tolerate multiple metals/metalloids and carries diverse efflux systems (RND/czc, Cus-like, P-type ATPases, CDF transporters) and arsenic-related genes (including ars cluster components and ArsB), consistent with multi-metal tolerance as a combined trait set. (Microorganisms; published Jun 2023; https://doi.org/10.3390/microorganisms11061518) (xie2023wholegenomesequence pages 9-10)

### 3.2 Rhizosphere-assisted remediation
A 2023 Frontiers review emphasizes rhizospheric bacteria as practical agents in heavy-metal detoxification and highlights canonical operons (mer, ars, czc) used for microbial mitigation strategies. This supports how the metal tolerant trait is used in applied contexts (plant growth promotion + detoxification). (Frontiers in Microbiology; published Jul 2023; https://doi.org/10.3389/fmicb.2023.1229828) (joshi2023rhizosphericbacteriathe pages 11-12)

### 3.3 Clinical and engineered-context relevance (cross-domain)
Metal tolerance mechanisms intersect with infection biology and materials/antibacterial strategies, especially for copper. Copper’s antimicrobial pressure motivates targeting bacterial copper homeostasis and efflux (e.g., Cus/Cop/Cup-like systems) to sensitize bacteria, indicating translational relevance of mechanistic nodes used in environmental tolerance. (rismondo2023thesensoryhistidine pages 1-2, hirth2023fullcopperresistance pages 1-3)

---

## 4) Expert synthesis and analysis (authoritative perspectives)

### 4.1 “Efflux-first” architecture with layered defenses
Across the 2023–2024 sources, efflux is repeatedly presented as a core tolerance strategy, with **P-type ATPases, CDF, and RND systems** as recurrent motifs. (shafiq2024mechanismsoftoxicity pages 9-10, nies2024aflowequilibrium pages 1-3)

However, a key expert-level insight is that *efflux rarely acts alone*: the copper system in *C. metallidurans* demonstrates that detoxification (periplasmic oxidation) and small-molecule buffering (GSH) interact non-additively, producing network-dependent increases in resistance/IC50. This argues for curating **interaction edges** (e.g., Cop + GSH → higher IC50) rather than only single-gene → phenotype edges. (hirth2023fullcopperresistance pages 11-12, hirth2023fullcopperresistance pages 9-11)

### 4.2 Regulation is compartment-aware
CusSR demonstrates a direct periplasmic-signal paradigm: sensing periplasmic Cu triggers expression of periplasm-facing detox/efflux components. This compartment specificity is important for trait graphs: it motivates explicit nodes for **periplasmic metal pool** vs **cytoplasmic metal pool**, rather than a single “intracellular metal” node. (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 8-10)

### 4.3 HGT creates punctuated jumps in tolerance
The Mer operon study provides rare, clean evidence that **a single horizontally transferred operon can produce a large tolerance shift (10×)** and rapidly reshape global transcriptional response patterns under stress. This supports inclusion of **mobile genetic element / plasmid carriage** as a causal upstream factor in metal tolerance graphs. (bhat2024horizontalgenetransfer pages 1-2)

---

## 5) Statistics and data points from recent studies (curation-relevant)

- **Mercury tolerance effect size (2024):** strains with a Mer operon show **“10-fold increased tolerance to Hg”**; plasmid transfer yields **immediate tolerance gain**. (bhat2024horizontalgenetransfer pages 1-2)
- **Copper resistance quantification (2023):** IC50 values for copper resistance are reported across *C. metallidurans* mutants; the work quantifies contributions of Cup/Cop/Cus/GSH/Gig and reports interaction effects such as **“Cop plus GSH… increased the IC50 level 4-fold”** in a defined mutant background. (hirth2023fullcopperresistance pages 11-12, hirth2023fullcopperresistance pages 1-3)
- **Zinc homeostasis/tolerance quantitative transport (2024):** a Zn uptake kinetic parameter is reported (e.g., **Km 137 ± 87 µM** and **vmax 3.7 ± 2.1 µmol min−1 g−1**), and gene deletions shift zinc tolerance dramatically (IC50 reductions with transporter deletions are described), supporting quantitative “flow equilibrium” modeling. (nies2024aflowequilibrium pages 1-3)
- **Cadmium efflux partitioning (2024):** atomic absorption spectroscopy supports efflux with measured **extracellular Cd accumulation (~85.33 ppm)** and lower **intracellular Cd (~13 ppm)** in a Cd-resistant strain. (chatterjee2024multimodalcadmiumresistance pages 14-15)

---

## 6) Candidate nodes for `metal_tolerant.yaml` (grouped by type)

### 6.1 Environmental / experimental factor nodes
- Elevated heavy-metal ion exposure (label-only; consider ENVO label-only “metal-contaminated soil” if needed)
- Metal mixture shock / metal starvation (label-only; relevant in *C. metallidurans* studies) (nies2024aflowequilibrium pages 1-3)
- Assay medium chemistry affecting metal bioavailability (e.g., phosphate-eliminated medium to prevent Cd precipitation) (label-only) (chatterjee2024multimodalcadmiumresistance pages 14-15)

### 6.2 Chemical nodes (suggested CHEBI where clear)
- Zn(II): CHEBI:27375 (nies2024aflowequilibrium pages 1-3)
- Cd(II): CHEBI:22977 (chatterjee2024multimodalcadmiumresistance pages 14-15)
- Cu(I): CHEBI:29036; Cu(II): CHEBI:29033 (hirth2023fullcopperresistance pages 16-18)
- Arsenate As(V): CHEBI:30667; arsenite As(III): CHEBI:27563 (shafiq2024mechanismsoftoxicity pages 9-10)
- Glutathione: CHEBI:16856 (hirth2023fullcopperresistance pages 11-12)
- Polyphosphate: label-only (nies2024aflowequilibrium pages 1-3)

### 6.3 Gene/protein/complex nodes (label-only unless curated separately)
**Efflux/export:**
- RND/CBA complexes: CzcCBA, CusCBA (nies2024aflowequilibrium pages 1-3, hirth2023fullcopperresistance pages 16-18)
- P-type ATPases: CupA, ZntA, CadA (hirth2023fullcopperresistance pages 1-3, nies2024aflowequilibrium pages 1-3, chatterjee2024multimodalcadmiumresistance pages 14-15)
- CDF exporters: DmeF, FieF (nies2024aflowequilibrium pages 1-3)
- CusF periplasmic copper chaperone (hirth2023fullcopperresistance pages 16-18)

**Detoxification:**
- CopA periplasmic Cu(I) oxidase (hirth2023fullcopperresistance pages 16-18, hirth2023fullcopperresistance pages 1-3)
- ArsC arsenate reductase (shafiq2024mechanismsoftoxicity pages 9-10)
- Mer operon (mer genes, operon-level node appropriate for HGT edge) (bhat2024horizontalgenetransfer pages 1-2)

**Regulation:**
- CusS/CusR two-component system (rismondo2023thesensoryhistidine pages 1-2)
- CzcS/CzcR two-component system (chatterjee2024multimodalcadmiumresistance pages 14-15)

### 6.4 Process/phenotype output nodes
- Metal efflux (label-only; possibly GO:0044765 single-organism transport [broad])
- Periplasmic copper oxidation (label-only)
- Arsenate reduction / arsenite export loop (label-only)
- Growth under metal stress / MIC / IC50 (assay nodes) (hirth2023fullcopperresistance pages 1-3, chatterjee2024multimodalcadmiumresistance pages 14-15)

---

## 7) Evidence-backed candidate causal edges (curation table)
The table below is designed as a direct input to TraitMech edge review.

| Edge (subject—predicate→object) | Mechanism class | Example taxa (NCBITaxon label only) | Suggested grounding | Evidence snippet | Reference (DOI, year, URL) | Strength/notes |
|---|---|---|---|---|---|---|
| elevated heavy-metal concentration—causes→ growth inhibition / metal stress | assay | label-only | CHEBI: heavy metal ion (label-only); GO:0050896 response to stimulus (broad, tentative) | “Changes in expression was noted for genes related to general stress responses… DNA repair” under copper/heavy metal stress | 10.1186/s12866-024-03206-7, 2024, https://doi.org/10.1186/s12866-024-03206-7 (xie2023wholegenomesequence pages 9-10) | Broad phenotype framing; useful as environmental input node, but not metal-specific enough for a curated mechanistic edge without assay context. |
| CzcCBA transenvelope efflux system—enables→ zinc/cadmium/cobalt tolerance | efflux | *Cupriavidus metallidurans* | GO:0043215 metal ion transmembrane transporter activity (broad); CzcCBA complex label-only; CHEBI:27375 Zn(2+), CHEBI:22977 Cd(2+) | “the most prominent polypeptides were… particularly the CzcCBA transenvelope efflux system” | 10.1093/mtomcs/mfae058, 2024, https://doi.org/10.1093/mtomcs/mfae058 (xie2023wholegenomesequence pages 9-10) | Strong, but taxon-specific; direct proteomic support in metal shock. |
| czc determinant / CzcCBA—confers→ high zinc resistance | efflux | *Cupriavidus metallidurans* | CzcCBA label-only; CHEBI:27375 Zn(2+) | “high-level resistance is mediated by the plasmid pMOL30-encoded czc determinant including the transenvelope RND-like complex CzcCBA” | 10.1128/jb.00080-24, 2024, https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) | Strong; quantitative context in same study supports contribution to IC50. |
| ZntA P-type ATPase—exports→ Zn(II) / Cd(II) | efflux | *Cupriavidus metallidurans* | ZntA label-only; GO:0005388 zinc-transporting ATPase activity (tentative); CHEBI:27375 Zn(2+), CHEBI:22977 Cd(2+) | “inner-membrane PIB2-type P-type ATPases ZntA and CadA… function as exporters” | 10.1128/jb.00080-24, 2024, https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) | Strong for exporter role; substrate breadth partly inferred from nomenclature/homeostasis context. |
| CadA P-type ATPase—exports→ Zn(II) / Cd(II) to periplasm | efflux | *Pseudomonas aeruginosa* | CadA label-only; CHEBI:27375 Zn(2+), CHEBI:22977 Cd(2+) | “a Cd2+-transporting P-type ATPase (CadA) moves Zn2+ from cytoplasm to periplasm” | 10.1038/s41598-024-80754-y, 2024, https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 14-15) | Strong but species-specific; wording mixes Cd resistance and Zn movement. |
| CzcS/CzcR two-component system—upregulates→ czcCBA operon | regulation | *Pseudomonas aeruginosa* | CzcS/CzcR label-only; GO:0000160 phosphorelay signal transduction system (broad) | “activation of CzcS/CzcR stimulates transcription of the czcCBA operon” | 10.1038/s41598-024-80754-y, 2024, https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 14-15) | Strong regulatory edge; likely portable to other Gram-negatives but curate as taxon-tested. |
| czcCBA operon expression—causes→ Cd2+ efflux from cytoplasm/periplasm | efflux | *Pseudomonas aeruginosa* | czcCBA label-only; CHEBI:22977 Cd(2+) | “upregulates the czcCBA operon to expel Cd2+ from cytoplasm and periplasm” | 10.21203/rs.3.rs-4733845/v1, 2024, https://doi.org/10.21203/rs.3.rs-4733845/v1 (chatterjee2024pseudomonasaeruginosastrain pages 21-23) | Mechanistically explicit, but preprint; mark uncertain until peer-reviewed equivalent used. |
| efflux mechanism—causes→ low intracellular cadmium during growth in Cd | assay | *Pseudomonas aeruginosa* | CHEBI:22977 Cd(2+); assay label-only | “extracellular Cd2+ accumulation (85.33 ppm) with low intracellular Cd (13 ppm)” | 10.1038/s41598-024-80754-y, 2024, https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 14-15) | Strong quantitative phenotype support for active efflux. |
| ArsC arsenate reductase—converts→ arsenate to arsenite | detox | label-only | GO:0018808 arsenate reductase (glutaredoxin) activity (tentative class only); CHEBI:30667 arsenate, CHEBI:27563 arsenite | “ArsC converting As(V) to As(III) followed by extrusion” | 10.52700/jmmg.v5i1.155, 2024, https://doi.org/10.52700/jmmg.v5i1.155 (shafiq2024mechanismsoftoxicity pages 9-10) | Strong review-level support; general across bacteria. |
| ArsB / Acr3 arsenite efflux pump—exports→ arsenite | efflux | *Cupriavidus necator* | ArsB label-only; Acr3 label-only; CHEBI:27563 arsenite | “the putative arsenite efflux pump ArsB… may provide the bacterium a robust capability for arsenic resistance” | 10.3390/microorganisms11061518, 2023, https://doi.org/10.3390/microorganisms11061518 (xie2023wholegenomesequence pages 9-10) | Moderate; genome-based inference in one strain. |
| ars operon (arsC + arsB/acr3)—enables→ arsenic tolerance | detox | soil/agricultural microbiomes (mixed taxa) | ars operon label-only; CHEBI:30667 arsenate; CHEBI:27563 arsenite | “The large proportion of arsC, arsA, arsB, and acr3 genes” and “a cooperative mechanism involving detoxification through arsenate reduction” | 10.7717/peerj.18383, 2024, https://doi.org/10.7717/peerj.18383 (xie2023wholegenomesequence pages 9-10) | Useful community-scale support; not strain-resolved, so weaker for direct causal curation. |
| Mer operon—confers→ increased mercury tolerance | detox | *Sinorhizobium medicae*, *Rhizobium leguminosarum* | mer operon label-only; CHEBI:16170 mercury atom / Hg(II) label-only | “only the strains that possessed a Mer operon exhibited 10-fold increased tolerance to Hg” | 10.1186/s12866-024-03391-5, 2024, https://doi.org/10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransfer pages 1-2) | Strong quantitative causal evidence. |
| horizontal transfer of Mer operon—causes→ immediate increase in Hg tolerance | detox | *Sinorhizobium medicae*, *Rhizobium leguminosarum* | mer operon label-only; horizontal gene transfer label-only | “Transfer of a plasmid containing the Mer operon… resulted in an immediate increase in Hg tolerance” | 10.1186/s12866-024-03391-5, 2024, https://doi.org/10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransfer pages 1-2) | Very strong; direct gain-of-function evidence. |
| Mer operon genes—are upregulated by→ Hg stress | regulation | *Sinorhizobium medicae*, *Rhizobium leguminosarum* | mer operon label-only; CHEBI:Hg label-only | “nearly all genes in the Mer operon were significantly up-regulated in response to Hg stress” | 10.1186/s12866-024-03391-5, 2024, https://doi.org/10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransfer pages 1-2) | Strong transcriptional support; complements tolerance phenotype. |
| CupA PIB1-type ATPase—exports→ cytoplasmic Cu(I) | efflux | *Cupriavidus metallidurans* | CupA label-only; CHEBI:29036 copper(1+) | “the PIB1-type Cu(I) exporter CupA” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 1-3) | Strong, central candidate node for copper tolerance subgraph. |
| CopA periplasmic Cu(I) oxidase—oxidizes→ Cu(I) to Cu(II) | detox | *Cupriavidus metallidurans* | CopA oxidase label-only; GO:0016722 oxidoreductase activity (broad); CHEBI:29036 copper(1+), CHEBI:29033 copper(2+) | “the periplasmic Cu(I)-oxidase CopA” and “CopA oxidizes Cu(I) to Cu(II)” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 16-18) | Strong, taxon-specific but mechanistically explicit. |
| CusF—delivers→ Cu(I) to CusCBA efflux complex | efflux | *Cupriavidus metallidurans*, *Escherichia coli* | CusF label-only; CusCBA label-only; CHEBI:29036 copper(1+) | “CusF delivers copper ions directly to this protein complex” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 16-18) | Strong for copper-handling chain; mostly Cu-specific, not generic metal tolerance. |
| CusCBA transenvelope efflux system—exports→ periplasmic Cu(I) | efflux | *Cupriavidus metallidurans*, *Escherichia coli* | CusCBA label-only; CHEBI:29036 copper(1+) | “CusCBA exports periplasmic Cu(I) to the outside” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 16-18) | Strong; explicit substrate and compartment. |
| CusSR two-component system—controls expression of→ cusF and cusCBA | regulation | *Escherichia coli* | CusS label-only; CusR label-only; cusF/cusCBA label-only | “the two-component regulatory system CusSR that controls expression of cusF and cusCBA” | 10.1128/spectrum.00291-23, 2023, https://doi.org/10.1128/spectrum.00291-23 (rismondo2023thesensoryhistidine pages 1-2) | Strong direct wording. |
| CusS histidine kinase—senses→ periplasmic copper ions | regulation | *Escherichia coli* | CusS label-only; CHEBI:29036 copper(1+) | “CusS from E. coli indeed senses periplasmic copper ions” | 10.1128/spectrum.00291-23, 2023, https://doi.org/10.1128/spectrum.00291-23 (rismondo2023thesensoryhistidine pages 1-2) | Strong direct evidence; valuable regulation edge. |
| periplasmic copper ions—activate→ cusCFBA expression via CusS | regulation | *Escherichia coli* | cusCFBA label-only; CHEBI:29036 copper(1+) | “a copper-dependent activation of CusS was required for cusCFBA expression” | 10.1128/spectrum.00291-23, 2023, https://doi.org/10.1128/spectrum.00291-23 (rismondo2023thesensoryhistidine pages 8-10) | Strong, slightly more assay-specific/anoxic-context in source. |
| glutathione—supports→ full copper resistance | sequestration | *Cupriavidus metallidurans* | CHEBI:16856 glutathione | “Copper resistance… [ranked as] Cup, Cop, Cus, GSH, and Gig” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 1-3) | Moderate; supportive role rather than standalone determinant. |
| Cop plus glutathione—raises→ copper IC50 | sequestration | *Cupriavidus metallidurans* | CopA label-only; CHEBI:16856 glutathione | “Cop plus GSH protected and increased the IC50 level 4-fold” | 10.1128/aem.00567-23, 2023, https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 11-12) | Strong quantitative interaction, but copper-specific and network-dependent. |
| polyphosphate—binds→ zinc and influences zinc flow equilibrium | sequestration | *Cupriavidus metallidurans* | polyphosphate label-only; CHEBI:27375 Zn(2+) | “cytoplasmic metal-binding components glutathione and polyphosphate bind metals and influence zinc flow equilibrium” | 10.1128/jb.00080-24, 2024, https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) | Moderate; supportive systems-level evidence, not a direct mutant edge in quoted text. |
| glutathione and polyphosphate—modulate→ cellular zinc homeostasis | sequestration | *Cupriavidus metallidurans* | CHEBI:16856 glutathione; polyphosphate label-only | “the absence of the metal-binding cytoplasmic components, polyphosphate and glutathione… influenced the flow equilibrium” | 10.1128/jb.00080-24, 2024, https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) | Good systems-level support; phenotype is zinc homeostasis rather than broad tolerance per se. |
| metallothionein / thiol-rich proteins—sequester→ cadmium and support tolerance | sequestration | *Pseudomonas aeruginosa* | metallothionein label-only; CHEBI:22977 Cd(2+) | “The genome encodes… metallothionein, and thiol-rich proteins consistent with sequestration mechanisms” | 10.21203/rs.3.rs-4733845/v1, 2024, https://doi.org/10.21203/rs.3.rs-4733845/v1 (chatterjee2024pseudomonasaeruginosastrain pages 21-23) | Weak-to-moderate; genome inference from preprint, not experimentally isolated mechanism. |
| metal efflux pumps / transporters—mediate→ bacterial heavy-metal resistance | efflux | label-only | GO:0006820 anion transport / metal ion transport (broad); label-only preferred | “resistance in most bacteria is mediated by P-type ATPase efflux, diffusion facilitator transporters of cations and RND” | 10.52700/jmmg.v5i1.155, 2024, https://doi.org/10.52700/jmmg.v5i1.155 (shafiq2024mechanismsoftoxicity pages 9-10) | High-level review support; useful parent edge but broad for direct TraitMech curation. |
| metal tolerance phenotype—measured by→ MIC / growth under metal stress | assay | *Pseudomonas aeruginosa*, *Cupriavidus necator* | assay label-only | “MIC determination” and “survival and growth… dependent on efflux mechanism” | 10.1038/s41598-024-80754-y, 2024, https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 14-15); 10.3390/microorganisms11061518, 2023, https://doi.org/10.3390/microorganisms11061518 (xie2023wholegenomesequence pages 9-10) | Strong as assay framing, but should not be treated as mechanism. |


*Table: This table lists evidence-backed candidate causal edges for curating the microbial trait “metal tolerant,” spanning efflux, detoxification, sequestration, regulation, and phenotype assay edges. It uses only supported context IDs and flags where claims are broad, taxon-specific, or still uncertain.*

---

## 8) Visual evidence (mechanism schematic + quantitative mutant table)
Hirth et al. (2023) provides a schematic model of copper homeostasis in *C. metallidurans* and a table of IC50 values for mutants, supporting both mechanistic structure and quantitative trait contribution (Figure 1; Table 1). (hirth2023fullcopperresistance media e7230e68, hirth2023fullcopperresistance media af275243)

---

## 9) Warnings / curation notes (what not to curate yet)
1. **Genome-annotation-only claims** (e.g., “presence of ArsB may provide robust resistance”) should be curated as **uncertain** unless linked to expression/knockout/phenotype evidence in the same study. (xie2023wholegenomesequence pages 9-10)
2. **Preprints** (e.g., Research Square cadmium networking manuscript) should be used cautiously; prefer peer-reviewed equivalents when possible. (chatterjee2024pseudomonasaeruginosastrain pages 21-23)
3. **Community metagenomic gene abundance** (e.g., ars gene prevalence in soil microbiomes) supports ecological relevance but is often **not host-resolved**; curate these edges as **weak/indirect** for TraitMech unless strain-level linkage exists. (xie2023wholegenomesequence pages 9-10)
4. **“Resistance vs tolerance” wording** varies across literature; for TraitMech, anchor edges to **measured growth/viability under exposure** (MIC/IC50) rather than gene presence alone. (hirth2023fullcopperresistance pages 1-3, chatterjee2024multimodalcadmiumresistance pages 14-15)

---

## 10) DOI-first bibliography (with publication dates and URLs)

1. **Horizontal gene transfer of the Mer operon is associated with large effects on the transcriptome and increased tolerance to mercury in nitrogen-fixing bacteria.**
   - Bhat A. et al., *BMC Microbiology*, **Jul 2024**.
   - DOI: **10.1186/s12866-024-03391-5**
   - URL: https://doi.org/10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransfer pages 1-2)

2. **The sensory histidine kinase CusS of Escherichia coli senses periplasmic copper ions.**
   - Rismondo J. et al., *Microbiology Spectrum*, **Apr 2023**.
   - DOI: **10.1128/spectrum.00291-23**
   - URL: https://doi.org/10.1128/spectrum.00291-23 (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 8-10)

3. **Full Copper Resistance in Cupriavidus metallidurans Requires the Interplay of Many Resistance Systems.**
   - Hirth N. et al., *Applied and Environmental Microbiology*, **Jun 2023**.
   - DOI: **10.1128/aem.00567-23**
   - URL: https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 1-3)

4. **A flow equilibrium of zinc in cells of Cupriavidus metallidurans.**
   - Nies D.H. et al., *Journal of Bacteriology*, **May 2024**.
   - DOI: **10.1128/jb.00080-24**
   - URL: https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3)

5. **Multimodal cadmium resistance and its regulatory networking in Pseudomonas aeruginosa strain CD3.**
   - Chatterjee S. et al., *Scientific Reports*, **Dec 2024**.
   - DOI: **10.1038/s41598-024-80754-y**
   - URL: https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 14-15)

6. **Rhizospheric bacteria: the key to sustainable heavy metal detoxification strategies.**
   - Joshi S. et al., *Frontiers in Microbiology*, **Jul 2023**.
   - DOI: **10.3389/fmicb.2023.1229828**
   - URL: https://doi.org/10.3389/fmicb.2023.1229828 (joshi2023rhizosphericbacteriathe pages 11-12)

7. **Mechanisms of Toxicity of Heavy Metals and the Microbial Strategies for their Mitigation: A Review.**
   - Shafiq M., Rehman Y., *The Journal of Microbiology and Molecular Genetics*, **Apr 2024**.
   - DOI: **10.52700/jmmg.v5i1.155**
   - URL: https://doi.org/10.52700/jmmg.v5i1.155 (shafiq2024mechanismsoftoxicity pages 9-10)

8. **Whole Genome Sequence Analysis of Cupriavidus necator C39, a Multiple Heavy Metal(loid) and Antibiotic Resistant Bacterium Isolated from a Gold/Copper Mine.**
   - Xie Z. et al., *Microorganisms*, **Jun 2023**.
   - DOI: **10.3390/microorganisms11061518**
   - URL: https://doi.org/10.3390/microorganisms11061518 (xie2023wholegenomesequence pages 9-10)


References

1. (shafiq2024mechanismsoftoxicity pages 9-10): Maria Shafiq and Yasir Rehman. Mechanisms of toxicity of heavy metals and the microbial strategies for their mitigation: a review. THE JOURNAL OF MICROBIOLOGY AND MOLECULAR GENETICS, 5:45-63, Apr 2024. URL: https://doi.org/10.52700/jmmg.v5i1.155, doi:10.52700/jmmg.v5i1.155. This article has 9 citations.

2. (nies2024aflowequilibrium pages 1-3): Dietrich H. Nies, Grit Schleuder, Diana Galea, and Martin Herzberg. A flow equilibrium of zinc in cells of <i>cupriavidus metallidurans</i>. May 2024. URL: https://doi.org/10.1128/jb.00080-24, doi:10.1128/jb.00080-24. This article has 14 citations and is from a peer-reviewed journal.

3. (hirth2023fullcopperresistance pages 9-11): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

4. (hirth2023fullcopperresistance pages 1-3): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

5. (hirth2023fullcopperresistance media af275243): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

6. (chatterjee2024multimodalcadmiumresistance pages 14-15): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

7. (hirth2023fullcopperresistance pages 16-18): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

8. (hirth2023fullcopperresistance pages 11-12): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

9. (rismondo2023thesensoryhistidine pages 1-2): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

10. (bhat2024horizontalgenetransfer pages 1-2): Aditi Bhat, Reena Sharma, Kumaran Desigan, M. Mercedes Lucas, Ankita Mishra, Robert M. Bowers, Tanja Woyke, Brendan Epstein, Peter Tiffin, José J. Pueyo, and Tim Paape. Horizontal gene transfer of the mer operon is associated with large effects on the transcriptome and increased tolerance to mercury in nitrogen-fixing bacteria. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03391-5, doi:10.1186/s12866-024-03391-5. This article has 25 citations and is from a peer-reviewed journal.

11. (rismondo2023thesensoryhistidine pages 8-10): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

12. (xie2023wholegenomesequence pages 9-10): Zhenchen Xie, Dan Wang, Ibtissem Ben Fekih, Yanshuang Yu, Yuanping Li, Hend Alwathnani, Martin Herzberg, and Christopher Rensing. Whole genome sequence analysis of cupriavidus necator c39, a multiple heavy metal(loid) and antibiotic resistant bacterium isolated from a gold/copper mine. Microorganisms, 11:1518, Jun 2023. URL: https://doi.org/10.3390/microorganisms11061518, doi:10.3390/microorganisms11061518. This article has 12 citations.

13. (joshi2023rhizosphericbacteriathe pages 11-12): Samiksha Joshi, Saurabh Gangola, Geeta Bhandari, Narendra Singh Bhandari, Deepa Nainwal, Anju Rani, Sumira Malik, and Petr Slama. Rhizospheric bacteria: the key to sustainable heavy metal detoxification strategies. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1229828, doi:10.3389/fmicb.2023.1229828. This article has 124 citations and is from a peer-reviewed journal.

14. (chatterjee2024pseudomonasaeruginosastrain pages 21-23): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, Ranadhir Chakraborty, and Ranadhir Chakraborty. Pseudomonas aeruginosa strain cd3 implements cadmium resistance through multimodal systems and its regulatory networking. Unknown journal, Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4733845/v1, doi:10.21203/rs.3.rs-4733845/v1.

15. (hirth2023fullcopperresistance media e7230e68): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.