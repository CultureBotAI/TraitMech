---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:25:35.467141'
end_time: '2026-08-04T08:34:38.282569'
duration_seconds: 542.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: flask shaped
  trait_identifier: METPO:1000675
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: flask_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a bulbous body with a narrower
    neck-like extension at one pole.
  parent_traits: METPO:1000666
  synonyms: flask, flask-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape
    review supports polarized peptidoglycan growth as a mechanism producing asymmetric
    flask-like morphology.)'
  causal_graph_summary: 'flask_shaped_asymmetric_polar_growth: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flask shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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
- **Trait label:** flask shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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


# Curation report: microbial “flask shaped” morphology

## Executive assessment

**Target:** `METPO:1000675` (“flask shaped”; morphology class; reviewed). The trait denotes a **cell-body geometry** with a bulbous body narrowing into a neck-like extension at one pole. In the literature, the closest operational descriptors are **pear-shaped**, **tear-drop-shaped**, or a cell with one rounded pole and one tapered pole.

The strongest mechanistic model is not yet a direct knockout-to-flask-shape pathway in a canonical flask-shaped planctomycete. Rather, it is a taxon-specific model from the stalked budding alphaproteobacterium *Hyphomonas neptunium*: cell-cycle-regulated switching among dispersed and zonal peptidoglycan (PG) insertion sites generates an asymmetric cell with a rounded old pole and tapered new/stalked pole. By contrast, deletion of `mreB`, `ftsI`, or `ftsW` in pear-shaped *Planctopirus limnophila* caused no observable phenotype under the tested conditions, arguing against importing the *H. neptunium* pathway wholesale into Planctomycetota (cserti2017dynamicsofthe pages 7-9, cserti2017dynamicsofthe pages 4-7, wiegand2020cultivationandfunctional pages 5-6).

The user-supplied DOI `10.1146/annurev-cellbio-101011-155745` is **not a bacterial cell-shape review**; it resolves to Lamkanfi and Dixit’s 2012 review, *Inflammasomes and Their Roles in Health and Disease*. It should therefore be removed from the existing causal graph unless a different DOI was intended.

## 1. Trait scope and boundaries

### Included phenotype

A cell should be annotated `METPO:1000675` when microscopy shows:

- a conspicuously bulbous or rounded main body;
- unilateral narrowing toward one pole;
- a neck-like or tapered polar region;
- a stable or developmentally defined pear/tear-drop/flask outline.

In *H. neptunium*, newborn cells were quantitatively asymmetric, with a round old pole and tapered new pole; the reported round:tapered pole-curvature ratio was **0.4 ± 0.1 (n = 10)**. The stalk diameter was **131 ± 3 nm (n = 50)**, with an internal cytoplasmic space of **60 ± 2 nm (n = 50)** (cserti2017dynamicsofthe pages 7-9).

### Boundary cases

1. **Pear- or tear-drop-shaped:** normally include when the main body narrows unilaterally. *P. limnophila* is explicitly described as pear-shaped and is a strong positive exemplar (wiegand2020cultivationandfunctional pages 5-6).
2. **Stalked/prosthecate:** do not equate a stalk with flask shape. A rod or coccus may bear a stalk without having a bulbous, tapered body.
3. **Budding:** budding is a division mode, not a shape. The 2020 survey observed budding in both elongated and coccoid cells; therefore, budding is neither necessary nor sufficient for flask morphology (wiegand2020cultivationandfunctional pages 5-6).
4. **Ovoid:** include only when one pole is demonstrably narrower; a symmetric oval lacks the defining neck-like polarity.
5. **Pyriform:** often compatible, but image-level review is advisable because taxonomic descriptions use “pyriform” inconsistently.
6. **Pleomorphic/amoeboid/shapeshifting:** exclude unless a reproducible flask-shaped state is explicitly observed. The absence of a rigid stable outline is a different phenotype.
7. **Flask culture:** exclude lexical matches in which “flask” describes a vessel rather than cell morphology.

## 2. Current mechanistic understanding

PG is the primary structural polymer that maintains bacterial shape. Planctomycetota were historically claimed to lack PG, but biochemical assays, isolated sacculi, lysozyme sensitivity, microscopy, and cryo-electron tomography demonstrated a typical PG wall in representatives including *Planctopirus limnophila*. The authors explicitly characterize PG as critical for maintenance of shape and division (jeske2015planctomycetesdopossess pages 1-2).

In *H. neptunium*, flask/pear-like polarity emerges from a **spatiotemporal morphogenetic program** rather than from a single dedicated “flask-shape gene.” HADA labeling revealed sequential PG incorporation throughout the swarmer body, at the new pole/stalk base, throughout the stalk during bud initiation, in the nascent bud, and finally at the bud neck. The authors conclude that morphology is determined by multiple cell-cycle-regulated zones of dispersed and zonal PG growth (cserti2017dynamicsofthe pages 7-9).

The MreB-controlled elongasome and PBP2 are critical in this organism. This differs from polarly growing Rhizobiales, which commonly lack MreB, MreCD, RodA, RodZ, and PBP2. Thus, “polar growth” is mechanistically heterogeneous across bacterial lineages and should be represented by taxon-qualified subgraphs rather than one universal pathway (cserti2017dynamicsofthe pages 4-7).

## 3. Candidate nodes

### Trait and organism nodes

- **flask shaped** — `METPO:1000675`
- pear-shaped cell — label-only synonym/near-equivalent pending ontology review
- tapered cell pole — label-only
- bulbous cell body — label-only
- *Hyphomonas neptunium* — use a verified NCBITaxon identifier during implementation
- *Planctopirus limnophila* — use a verified NCBITaxon identifier during implementation
- Planctomycetota — taxonomic context node; verify current NCBITaxon CURIE

### Structural and localization nodes

- peptidoglycan — `CHEBI:8005`
- peptidoglycan-based cell wall — `GO:0009274`
- cell wall — `GO:0005618`
- cell pole — `GO:0060187`
- new/tapered pole — label-only
- old/rounded pole — label-only
- stalk base — label-only
- stalk — label-only; do not collapse into flask-shaped morphology
- terminal stalk region — label-only
- nascent bud — label-only
- bud neck/division site — label-only
- elongasome — label-only complex unless a verified ontology term is selected
- divisome — label-only complex unless a verified ontology term is selected

### Processes and pathways

- regulation of cell shape — `GO:0008360`
- peptidoglycan biosynthetic process — `GO:0009252`
- cell wall organization or biogenesis — `GO:0071554`
- cell division — `GO:0051301`
- polar peptidoglycan insertion — label-only
- dispersed PG incorporation — label-only
- zonal PG incorporation — label-only
- stalk biogenesis/elongation — label-only
- terminal-stalk remodeling — label-only
- polar budding — label-only
- bud-neck constriction/separation — label-only

### Genes and proteins

Use gene/protein labels below until strain-specific UniProt accessions are verified:

- **MreB** — actin-like cytoskeletal regulator of the elongasome
- **PBP2** — elongation-specific transpeptidase
- **FtsI/PBP3** — division-specific transpeptidase
- **FtsW** — divisome-associated membrane protein/glycosyltransferase-family component
- **AmiC** — division-site amidase
- **LmdE** — LytM-domain protein, probably regulatory because catalytic residues are missing
- **MltA** — membrane-bound lytic transglycosylase candidate
- **DacB** — D-Ala-D-Ala carboxypeptidase
- **DacL** — polar-localized carboxypeptidase candidate; fusion functionality was not verified
- **FtsZ** — divisome organizer; contextual rather than directly demonstrated as the flask-shape determinant here
- **RodZ, MreC, MreD, RodA** — comparison/context nodes, not established positive determinants in *P. limnophila*

### Experimental and chemical nodes

- HADA, hydroxycoumarin-carbonyl-amino-D-alanine — label-only probe; verify chemical identifier before curation
- fluorescent D-amino-acid pulse labeling — assay node
- cryo-electron tomography — assay node
- time-lapse microfluidics — assay node
- phase-contrast microscopy — assay node
- scanning electron microscopy — assay node
- lysozyme treatment — experimental perturbation; lysozyme identifier should be protein-specific
- β-lactam antibiotics — class-level label; not a supported direct inducer of flask shape

No nutrient, electron-donor/acceptor, or environmental factor has sufficiently direct evidence for causing `METPO:1000675` in the retrieved literature.

## 4. Candidate causal edges

The following table summarizes the principal graph candidates; the detailed evidence and curation disposition follow it.

| subject | predicate | object | organism/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| Cell cycle-regulated pattern of peptidoglycan biosynthesis with distinct dispersed and zonal growth zones | shapes | asymmetric round-old-pole/tapered-new-pole pear/flask-like morphology | *Hyphomonas neptunium* | Direct (primary mechanistic study) (cserti2017dynamicsofthe pages 7-9, cserti2017dynamicsofthe pages 4-7) | https://doi.org/10.1111/mmi.13593 |
| MreB-controlled elongasome | is critical for | cell morphogenesis | *Hyphomonas neptunium* | Direct (primary mechanistic study) (cserti2017dynamicsofthe pages 1-4, cserti2017dynamicsofthe pages 4-7) | https://doi.org/10.1111/mmi.13593 |
| PBP2 | is required for | elongation/morphogenesis | *Hyphomonas neptunium* | Direct (primary mechanistic study) (cserti2017dynamicsofthe pages 1-4, cserti2017dynamicsofthe pages 4-7) | https://doi.org/10.1111/mmi.13593 |
| Polar peptidoglycan insertion at the new pole / stalk base | drives | stalk emergence | *Hyphomonas neptunium* | Direct (HADA pulse-labeling + microscopy) (cserti2017dynamicsofthe pages 7-9) | https://doi.org/10.1111/mmi.13593 |
| Remodeling of terminal stalk regions | produces | nascent bud / new daughter cell compartment | *Hyphomonas neptunium* | Direct (cryo-ET + microfluidics time-lapse) (cserti2017dynamicsofthe pages 7-9, cserti2017dynamicsofthe pages 4-7) | https://doi.org/10.1111/mmi.13593 |
| AmiC perturbation | causes | elongated stalks terminated by chains of bud cells | *Hyphomonas neptunium* | Direct (mutant phenotype) (cserti2017dynamicsofthe pages 9-11) | https://doi.org/10.1111/mmi.13593 |
| LmdE perturbation | causes | elongated stalks associated with short chains of bud cells | *Hyphomonas neptunium* | Direct (mutant phenotype) (cserti2017dynamicsofthe pages 9-11) | https://doi.org/10.1111/mmi.13593 |
| MltA perturbation | causes | occasional short chains of buds | *Hyphomonas neptunium* | Direct but weaker phenotype (mutant phenotype) (cserti2017dynamicsofthe pages 9-11) | https://doi.org/10.1111/mmi.13593 |
| DacB perturbation | causes | mild stalk elongation and chaining phenotype | *Hyphomonas neptunium* | Direct but weaker phenotype (mutant phenotype) (cserti2017dynamicsofthe pages 9-11) | https://doi.org/10.1111/mmi.13593 |
| Peptidoglycan cell wall / PG sacculus | maintains | cell shape | Planctomycetota | Direct for PG presence; contextual for flask shape (jeske2015planctomycetesdopossess pages 1-2) | https://doi.org/10.1038/ncomms8116 |
| Pear-shaped cell body | co-occurs with | polar budding division | *Planctopirus limnophila* | Direct for phenotype association, not mechanism (wiegand2020cultivationandfunctional pages 5-6) | https://doi.org/10.1038/s41564-019-0588-1 |
| Deletion of mreB | has no observable phenotype on | cell division / shape under tested conditions | *Planctopirus limnophila* | Direct negative evidence; mechanism uncertain/contextual (wiegand2020cultivationandfunctional pages 5-6) | https://doi.org/10.1038/s41564-019-0588-1 |
| Deletion of ftsI | has no observable phenotype on | cell division / shape under tested conditions | *Planctopirus limnophila* | Direct negative evidence; mechanism uncertain/contextual (wiegand2020cultivationandfunctional pages 5-6) | https://doi.org/10.1038/s41564-019-0588-1 |
| Deletion of ftsW | has no observable phenotype on | cell division / shape under tested conditions | *Planctopirus limnophila* | Direct negative evidence; mechanism uncertain/contextual (wiegand2020cultivationandfunctional pages 5-6) | https://doi.org/10.1038/s41564-019-0588-1 |
| Canonical peptidoglycan/cell-division proteins absent or nonessential | suggests | non-canonical shape-determination and division mechanisms | Planctomycetota, especially *Planctopirus limnophila* | Contextual/inferred (author interpretation) (wiegand2020cultivationandfunctional pages 6-8, wiegand2020cultivationandfunctional pages 5-6) | https://doi.org/10.1038/s41564-019-0588-1 |


*Table: This table summarizes the strongest curation-ready and cautionary causal edges for METPO:1000675 flask-shaped morphology. It emphasizes direct mechanistic evidence from *Hyphomonas neptunium* and negative/contextual evidence from planctomycetes such as *Planctopirus limnophila*.*

| Proposed subject–predicate–object | Supporting snippet | Curation note |
|---|---|---|
| peptidoglycan cell wall **maintains** bacterial cell shape | “Most bacteria contain a peptidoglycan (PG) cell wall, which is critical for maintenance of shape”; planctomycetal PG was demonstrated biochemically and microscopically. | **Curate as background edge.** Strong general evidence, but not specific to flask shape (jeske2015planctomycetesdopossess pages 1-2). |
| cell-cycle-regulated dispersed/zonal PG biosynthesis **determines** asymmetric pear/flask-like morphology | “The morphology of *H. neptunium* is determined by a complex cell cycle-regulated pattern of PG biosynthesis” involving distinct dispersed and zonal growth zones. | **Best direct mechanistic edge; taxon-specific.** Connect to `METPO:1000675` with a morphology-match qualifier because the paper does not use the exact METPO term (cserti2017dynamicsofthe pages 7-9). |
| MreB-controlled elongasome **enables** *H. neptunium* cell morphogenesis | Authors “reveal a critical role of the elongasome components MreB and PBP2…in cell morphogenesis.” | **Curate only in the *H. neptunium* branch.** Do not generalize to Planctomycetota (cserti2017dynamicsofthe pages 4-7). |
| PBP2 **enables** elongation/morphogenesis | PBP2 is identified as part of the elongation-specific PG complex, and the study reports a critical morphogenetic role for PBP2. | **Curate, taxon-specific.** Evidence supports morphogenesis more directly than the exact flask endpoint (cserti2017dynamicsofthe pages 1-4, cserti2017dynamicsofthe pages 4-7). |
| PG insertion at new pole/stalk base **produces** stalk emergence | HADA signal condensed at the new pole; “the stalk emerges from the cell body through insertion of new material at its base.” | **Curate as a developmental intermediate**, not as synonymous with flask shape (cserti2017dynamicsofthe pages 7-9). |
| terminal stalk remodeling **produces** daughter bud | Stalk length decreased as bud length increased; the bud “originates from the terminal regions of the stalk structure, which are gradually remodeled.” | **Curate in budding-development branch.** It explains asymmetric polar development, not necessarily steady-state flask shape (cserti2017dynamicsofthe pages 7-9). |
| zonal PG synthesis at bud neck **enables** bud separation | Late PG synthesis included “an additional focus…at the division site before its final separation.” | **Curate with moderate confidence.** The authors phrase the focus as “likely reflecting” PG remodeling (cserti2017dynamicsofthe pages 7-9). |
| `amiC` deletion **causes** elongated stalks and chains of bud cells | “Deletion of amiC led to the formation of elongated stalks terminated by chains of bud cells”; AmiC localized to the late division site. | **Curate as a division/separation defect**, not as a direct flask-shape edge (cserti2017dynamicsofthe pages 9-11). |
| `lmdE` deletion **causes** elongated stalks and short bud chains | “Only the lmdE mutant showed an obvious phenotype, forming elongated stalks…with short chains of bud cells.” | **Curate, taxon-specific.** The inferred regulatory role is less certain than the phenotype (cserti2017dynamicsofthe pages 9-11). |
| `mltA` deletion **causes** occasional bud chaining | The `ΔmltA` mutant “occasionally formed short chains of buds.” | **Weak direct phenotype.** Curate only with low penetrance/uncertain qualifier (cserti2017dynamicsofthe pages 9-11). |
| `dacB` deletion **causes** mild stalk elongation and chaining | “Only the ΔdacB mutant showed obvious morphological defects,” described as mild stalk elongation and chaining. | **Curate as weak/modifier edge**, not as core flask-shape determinant (cserti2017dynamicsofthe pages 9-11). |
| deletion of `mreB` **does not alter** observable morphology under tested conditions | `mreB`, `ftsI`, and `ftsW` “were deleted in *P. limnophila*…without observing a phenotype.” | **Curate as negative evidence** or encode in notes; it directly warns against a universal MreB→flask-shape edge (wiegand2020cultivationandfunctional pages 5-6). |
| deletion of `ftsI` **does not alter** observable morphology under tested conditions | Same deletion result; authors infer that otherwise essential canonical proteins may be nonessential or differently used. | **Negative evidence; condition-specific.** Absence of observed phenotype is not proof of no role under all conditions (wiegand2020cultivationandfunctional pages 6-8, wiegand2020cultivationandfunctional pages 5-6). |
| deletion of `ftsW` **does not alter** observable morphology under tested conditions | Same deletion result. | **Negative evidence; condition-specific** (wiegand2020cultivationandfunctional pages 5-6). |
| pear shape **co-occurs with** polar budding in *P. limnophila* | “Most…planctomycetes, such as the pear-shaped *P. limnophila*, divide by polar budding.” | **Association only.** Do not encode polar budding as sufficient to cause flask shape because coccoid cells also bud (wiegand2020cultivationandfunctional pages 5-6). |

## 5. Quantitative evidence and assay implementation

- The 2020 planctomycete study characterized **79 cultivated isolates** and analyzed **150 genomes**; the displayed division phenotypes were selected from **more than 100 cells** across at least two independent experiments. The analyzed genomes ranged from **1.88 to 10.98 Mb** and **34.8–73.2% GC** (wiegand2020cultivationandfunctional pages 5-6).
- In *H. neptunium*, swarmer cells required approximately **4 h** to become stalked and release their first offspring; established mothers subsequently released daughters at roughly **2.5-h intervals**. Cells divided at least **30 times** without an obvious decline in rate or morphology (cserti2017dynamicsofthe pages 7-9).
- The *H. neptunium* wall had **22% crosslinking**, lacked detected 3,3-linked muropeptides, contained **9.6% 1,6-anhydromuropeptides**, had an inferred average glycan-chain length of **11 disaccharides**, and had more than **90% tetrapeptide side chains**. These measurements support high PG turnover and a mechanism distinct from the L,D-transpeptidase-rich polar growth of *Agrobacterium* (cserti2017dynamicsofthe pages 9-11).
- Recommended phenotype workflow: phase contrast or SEM for body outline; cryo-ET for envelope continuity; time-lapse microfluidics for state transitions; FDAA/HADA pulse labeling for growth zones; and targeted depletion/deletion plus quantitative pole curvature, width profiles, and bud/stalk lengths. HADA enters newly synthesized PG through replacement of terminal D-amino acids in lipid-II peptide side chains (cserti2017dynamicsofthe pages 7-9).

## 6. Recent developments, applications, and expert interpretation

### 2023–2024 status

A 2024 *Nature Microbiology* review emphasizes that bacterial envelopes are evolutionarily diverse and that cryo-EM/cryo-ET and genome-resolved approaches have revised older envelope models. It distinguishes monoderm and diderm architectures and highlights the need to infer morphology from experimentally resolved envelope biology rather than simplistic Gram-stain categories (published in 2024; DOI below) (hashimi2024cellenvelopediversity pages 1-2).

However, the search did **not** identify a 2023–2024 primary study that resolves a new gene-to-flask-shape mechanism in *P. limnophila* or another unambiguous flask-shaped microbe. Recent Planctomycetota research expands recognized cell-biological diversity—including extreme shape plasticity and unusual division—but does not supersede the 2017 *H. neptunium* PG-patterning study as the most direct mechanistic evidence. Consequently, older foundational studies remain necessary.

### Real-world and research applications

1. **Morphology-aware taxonomy and phenotyping:** pear/flask shape remains useful in cultivation-based descriptions, but the 79-isolate survey shows that division mode cannot be inferred reliably from body shape alone (wiegand2020cultivationandfunctional pages 5-6).
2. **Antimicrobial target discovery:** PG synthases, hydrolases, elongasome components, and divisome proteins are experimentally tractable shape determinants. Yet the nonessentiality of canonical factors in *P. limnophila* shows that target conservation cannot be assumed across phyla (wiegand2020cultivationandfunctional pages 6-8, wiegand2020cultivationandfunctional pages 5-6).
3. **Synthetic morphogenesis:** spatially retargeting PG synthesis is a plausible route to engineering asymmetric cells, although no retrieved study directly engineered flask shape.
4. **Microscopy and image classification:** the trait can be operationalized using pole-curvature ratios, body-width profiles, and temporal tracking. Static images alone risk confusing a flask-shaped body with transient budding or a terminal bud.
5. **Ecological surface association:** stalks and holdfasts can mediate attachment, but this function belongs in a separate attachment/stalk subgraph unless a source directly links attachment selection to evolution or induction of flask-shaped bodies.

The most defensible expert interpretation is therefore a **modular graph**: PG wall → spatially patterned PG synthesis/remodeling → polar asymmetry → flask/pear-shaped body, with separate branches for stalk formation, budding, and daughter separation. Organism-specific implementations should sit beneath that high-level model.

## 7. Recommended YAML strategy

Use two taxon-qualified mechanistic modules rather than merging all evidence:

1. **`hyphomonas_neptunium_spatiotemporal_pg_patterning`**
   - Direct positive mechanism.
   - Include PG, dispersed growth, new-pole zonal growth, MreB-controlled elongasome, PBP2, stalk-base synthesis, terminal-stalk remodeling, bud-neck PG remodeling, and asymmetric body morphology.
   - Mark the mapping from the paper’s round/tapered or pear-like morphology to `METPO:1000675` as curator-reviewed.

2. **`planctopirus_limnophila_noncanonical_shape_determination`**
   - Include pear-shaped phenotype, PG wall, polar budding as an associated process, and negative deletion evidence for `mreB`, `ftsI`, and `ftsW`.
   - End with an **unknown/non-canonical shape-determination mechanism** node rather than asserting a specific causal protein.

Do not place AmiC, LmdE, MltA, or DacB directly upstream of `METPO:1000675`; their demonstrated endpoints are stalk elongation, chaining, and daughter-separation defects.

## 8. Warnings: claims not yet ready for TraitMech

- **Do not curate the supplied Annual Reviews DOI as polar-growth evidence.** It is an inflammasome review unrelated to bacterial shape.
- **Do not assert `MreB → flask shaped` universally.** It is supported in the *H. neptunium* morphogenetic system but contradicted as a simple required edge by the no-phenotype `mreB` deletion in pear-shaped *P. limnophila* (cserti2017dynamicsofthe pages 4-7, wiegand2020cultivationandfunctional pages 5-6).
- **Do not equate polar budding with flask shape.** Coccoid planctomycetes also bud (wiegand2020cultivationandfunctional pages 5-6).
- **Do not equate stalk formation with the target trait.** A stalk is a polar appendage/developmental compartment, whereas `METPO:1000675` describes body geometry.
- **Do not infer environmental causation.** No retrieved experiment establishes nutrient limitation, salinity, surface attachment, temperature, pH, or host association as an inducer of flask morphology.
- **Do not treat no observable deletion phenotype as proof of no molecular role.** Redundancy, culture conditions, assay sensitivity, or noncanonical paralogs could mask effects.
- **Do not curate DacL localization as functional proof.** The authors explicitly note that fusion functionality remained to be verified (cserti2017dynamicsofthe pages 9-11).
- **Do not generalize *H. neptunium* hydrolase phenotypes to Planctomycetota.** They are lineage-specific observations.
- **Do not invent strain-specific UniProt, NCBITaxon, Rhea, or EC identifiers.** Resolve these during database-backed implementation.

## DOI-first bibliography

1. Cserti E, et al. “Dynamics of the peptidoglycan biosynthetic machinery in the stalked budding bacterium *Hyphomonas neptunium*.” *Molecular Microbiology* 103:875–895. **Published March 2017.** https://doi.org/10.1111/mmi.13593 (cserti2017dynamicsofthe pages 7-9, cserti2017dynamicsofthe pages 9-11, cserti2017dynamicsofthe pages 4-7)
2. Wiegand S, et al. “Cultivation and functional characterization of 79 planctomycetes uncovers their unique biology.” *Nature Microbiology* 5:126–140. **Published online November 2019; volume year 2020.** https://doi.org/10.1038/s41564-019-0588-1 (wiegand2020cultivationandfunctional pages 6-8, wiegand2020cultivationandfunctional pages 5-6)
3. Jeske O, et al. “Planctomycetes do possess a peptidoglycan cell wall.” *Nature Communications* 6:7116. **Published 12 May 2015.** https://doi.org/10.1038/ncomms8116 (jeske2015planctomycetesdopossess pages 1-2)
4. Boedeker C, et al. “Determining the bacterial cell biology of Planctomycetes.” *Nature Communications* 8:14853. **Published April 2017.** https://doi.org/10.1038/ncomms14853 (boedeker2017determiningthebacterial pages 6-7)
5. Hashimi A, Tocheva EI. “Cell envelope diversity and evolution across the bacterial tree of life.” *Nature Microbiology* 9:2475–2487. **Accepted 16 August 2024; published 2024.** https://doi.org/10.1038/s41564-024-01812-9 (hashimi2024cellenvelopediversity pages 1-2)
6. Kysela DT, et al. “Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.” *PLOS Biology* 14:e1002565. **Published October 2016.** https://doi.org/10.1371/journal.pbio.1002565
7. van Teeseling MCF, de Pedro MA, Cava F. “Determinants of Bacterial Morphology: From Fundamentals to Possibilities for Antimicrobial Targeting.” *Frontiers in Microbiology* 8:1264. **Published July 2017.** https://doi.org/10.3389/fmicb.2017.01264
8. Randich AM, Brun YV. “Molecular mechanisms for the evolution of bacterial morphologies and growth modes.” *Frontiers in Microbiology* 6:580. **Published June 2015.** https://doi.org/10.3389/fmicb.2015.00580

**Bottom line:** the curation-ready core is **PG wall → spatially regulated dispersed/zonal PG synthesis → unilateral pole tapering/asymmetric body → `METPO:1000675`**, supported most directly in *H. neptunium*. *P. limnophila* supplies the strongest explicit pear-shaped exemplar but currently supports a noncanonical, unresolved mechanism rather than the same MreB/PBP2 pathway.

References

1. (cserti2017dynamicsofthe pages 7-9): Emöke Cserti, Sabine Rosskopf, Yi‐Wei Chang, Sabrina Eisheuer, Lars Selter, Jian Shi, Christina Regh, Ulrich Koert, Grant J. Jensen, and Martin Thanbichler. Dynamics of the peptidoglycan biosynthetic machinery in the stalked budding bacterium hyphomonas neptunium. Molecular Microbiology, 103:875-895, Mar 2017. URL: https://doi.org/10.1111/mmi.13593, doi:10.1111/mmi.13593. This article has 50 citations and is from a domain leading peer-reviewed journal.

2. (cserti2017dynamicsofthe pages 4-7): Emöke Cserti, Sabine Rosskopf, Yi‐Wei Chang, Sabrina Eisheuer, Lars Selter, Jian Shi, Christina Regh, Ulrich Koert, Grant J. Jensen, and Martin Thanbichler. Dynamics of the peptidoglycan biosynthetic machinery in the stalked budding bacterium hyphomonas neptunium. Molecular Microbiology, 103:875-895, Mar 2017. URL: https://doi.org/10.1111/mmi.13593, doi:10.1111/mmi.13593. This article has 50 citations and is from a domain leading peer-reviewed journal.

3. (wiegand2020cultivationandfunctional pages 5-6): Sandra Wiegand, Mareike Jogler, Christian Boedeker, Daniela Pinto, John Vollmers, Elena Rivas-Marín, Timo Kohn, Stijn H. Peeters, Anja Heuer, Patrick Rast, Sonja Oberbeckmann, Boyke Bunk, Olga Jeske, Anke Meyerdierks, Julia E. Storesund, Nicolai Kallscheuer, Sebastian Lücker, Olga M. Lage, Thomas Pohl, Broder J. Merkel, Peter Hornburger, Ralph-Walter Müller, Franz Brümmer, Matthias Labrenz, Alfred M. Spormann, Huub J. M. Op den Camp, Jörg Overmann, Rudolf Amann, Mike S. M. Jetten, Thorsten Mascher, Marnix H. Medema, Damien P. Devos, Anne-Kristin Kaster, Lise Øvreås, Manfred Rohde, Michael Y. Galperin, and Christian Jogler. Cultivation and functional characterization of 79 planctomycetes uncovers their unique biology. Nature Microbiology, 5:126-140, Nov 2020. URL: https://doi.org/10.1038/s41564-019-0588-1, doi:10.1038/s41564-019-0588-1. This article has 261 citations and is from a highest quality peer-reviewed journal.

4. (jeske2015planctomycetesdopossess pages 1-2): Olga Jeske, Margarete Schüler, Peter Schumann, Alexander Schneider, Christian Boedeker, Mareike Jogler, Daniel Bollschweiler, Manfred Rohde, Christoph Mayer, Harald Engelhardt, Stefan Spring, and Christian Jogler. Planctomycetes do possess a peptidoglycan cell wall. Nature Communications, May 2015. URL: https://doi.org/10.1038/ncomms8116, doi:10.1038/ncomms8116. This article has 212 citations and is from a highest quality peer-reviewed journal.

5. (cserti2017dynamicsofthe pages 1-4): Emöke Cserti, Sabine Rosskopf, Yi‐Wei Chang, Sabrina Eisheuer, Lars Selter, Jian Shi, Christina Regh, Ulrich Koert, Grant J. Jensen, and Martin Thanbichler. Dynamics of the peptidoglycan biosynthetic machinery in the stalked budding bacterium hyphomonas neptunium. Molecular Microbiology, 103:875-895, Mar 2017. URL: https://doi.org/10.1111/mmi.13593, doi:10.1111/mmi.13593. This article has 50 citations and is from a domain leading peer-reviewed journal.

6. (cserti2017dynamicsofthe pages 9-11): Emöke Cserti, Sabine Rosskopf, Yi‐Wei Chang, Sabrina Eisheuer, Lars Selter, Jian Shi, Christina Regh, Ulrich Koert, Grant J. Jensen, and Martin Thanbichler. Dynamics of the peptidoglycan biosynthetic machinery in the stalked budding bacterium hyphomonas neptunium. Molecular Microbiology, 103:875-895, Mar 2017. URL: https://doi.org/10.1111/mmi.13593, doi:10.1111/mmi.13593. This article has 50 citations and is from a domain leading peer-reviewed journal.

7. (wiegand2020cultivationandfunctional pages 6-8): Sandra Wiegand, Mareike Jogler, Christian Boedeker, Daniela Pinto, John Vollmers, Elena Rivas-Marín, Timo Kohn, Stijn H. Peeters, Anja Heuer, Patrick Rast, Sonja Oberbeckmann, Boyke Bunk, Olga Jeske, Anke Meyerdierks, Julia E. Storesund, Nicolai Kallscheuer, Sebastian Lücker, Olga M. Lage, Thomas Pohl, Broder J. Merkel, Peter Hornburger, Ralph-Walter Müller, Franz Brümmer, Matthias Labrenz, Alfred M. Spormann, Huub J. M. Op den Camp, Jörg Overmann, Rudolf Amann, Mike S. M. Jetten, Thorsten Mascher, Marnix H. Medema, Damien P. Devos, Anne-Kristin Kaster, Lise Øvreås, Manfred Rohde, Michael Y. Galperin, and Christian Jogler. Cultivation and functional characterization of 79 planctomycetes uncovers their unique biology. Nature Microbiology, 5:126-140, Nov 2020. URL: https://doi.org/10.1038/s41564-019-0588-1, doi:10.1038/s41564-019-0588-1. This article has 261 citations and is from a highest quality peer-reviewed journal.

8. (hashimi2024cellenvelopediversity pages 1-2): Ameena Hashimi and Elitza I. Tocheva. Cell envelope diversity and evolution across the bacterial tree of life. Nature microbiology, 9:2475-2487, Sep 2024. URL: https://doi.org/10.1038/s41564-024-01812-9, doi:10.1038/s41564-024-01812-9. This article has 29 citations and is from a highest quality peer-reviewed journal.

9. (boedeker2017determiningthebacterial pages 6-7): Christian Boedeker, Margarete Schüler, Greta Reintjes, Olga Jeske, Muriel C. F. van Teeseling, Mareike Jogler, Patrick Rast, Daniela Borchert, Damien P. Devos, Martin Kucklick, Miroslava Schaffer, Roberto Kolter, Laura van Niftrik, Susanne Engelmann, Rudolf Amann, Manfred Rohde, Harald Engelhardt, and Christian Jogler. Determining the bacterial cell biology of planctomycetes. Nature Communications, Apr 2017. URL: https://doi.org/10.1038/ncomms14853, doi:10.1038/ncomms14853. This article has 265 citations and is from a highest quality peer-reviewed journal.