---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:33:52.792459'
end_time: '2026-06-18T07:55:35.993947'
duration_seconds: 1303.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dumbbell shaped
  trait_identifier: METPO:1000672
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: dumbbell_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism consists of two rounded cell bodies
    connected by a narrower central isthmus, often resulting from incomplete or snapping
    cell division.
  parent_traits: METPO:1000666
  synonyms: S_star_dumbbell_pleomorphic, dumbbell-shaped
  evidence_summary: 'DOI:10.1111/j.1574-6976.2011.00298.x: snapping cell division
    (Corynebacterineae review supports snapping/V-form division producing transient
    dumbbell pairs.)'
  causal_graph_summary: 'dumbbell_shaped_snapping_division: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dumbbell shaped
- **METPO identifier:** METPO:1000672
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism consists of two rounded cell bodies connected by a narrower central isthmus, often resulting from incomplete or snapping cell division.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, dumbbell-shaped
- **Existing evidence:** DOI:10.1111/j.1574-6976.2011.00298.x: snapping cell division (Corynebacterineae review supports snapping/V-form division producing transient dumbbell pairs.)
- **Existing causal graph summary:** dumbbell_shaped_snapping_division: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **dumbbell shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/dumbbell_shaped.yaml`.

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
- **Trait label:** dumbbell shaped
- **METPO identifier:** METPO:1000672
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism consists of two rounded cell bodies connected by a narrower central isthmus, often resulting from incomplete or snapping cell division.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, dumbbell-shaped
- **Existing evidence:** DOI:10.1111/j.1574-6976.2011.00298.x: snapping cell division (Corynebacterineae review supports snapping/V-form division producing transient dumbbell pairs.)
- **Existing causal graph summary:** dumbbell_shaped_snapping_division: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **dumbbell shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/dumbbell_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **dumbbell shaped** (METPO:1000672)

**Target trait:** dumbbell shaped (METPO:1000672) — MORPHOLOGY — CLASS.  
**Definition (given):** two rounded cell bodies connected by a narrower central isthmus, often from incomplete or snapping cell division.

### 1) Scope summary (current understanding)

**Phenotype represented.** In Corynebacterineae/Mycobacteriales (Actinobacteria), a central mechanistic context for “dumbbell shaped” is **incomplete daughter-cell separation** during/after septation, where two nascent daughter compartments remain connected by a narrow hinge/isthmus. This incomplete-separation intermediate can manifest as a two-lobed cell body that is consistent with “dumbbell” morphology, and frequently resolves via **rapid mechanically driven separation (“snapping”/“V-snapping”)** (chimileski2024tipextensionand pages 5-7, chimileski2024tipextensionand pages 10-10).

**Distinguishing from nearby traits/boundary cases.**
- **V-shaped pairs / angular arrangements / palisades** are characteristic outcomes of snapping division; they can be viewed as *post-separation* or *partially separated* morphologies rather than a true stable dumbbell form (hett2008bacterialgrowthand pages 14-15, chimileski2024tipextensionand pages 10-10).
- **Chains / multiseptated elongated cells** represent stronger separation failure (e.g., hydrolase/regulator mutants), and are boundary phenotypes that can include transient dumbbell-like intermediates but should not be conflated with the dumbbell class itself (gaday2022ftsexindependentcontrolof pages 1-2, lim2019identificationofnew pages 6-7).
- **Filamentous/hyphal growth with multiple septa** (e.g., *Corynebacterium matruchotii* “multiple fission”) can generate hinge-like partial attachments, but these states mix growth-mode and division-mode phenotypes; curate cautiously as context rather than direct equivalence to dumbbell-shaped single-cell morphology (chimileski2024tipextensionand pages 7-8, chimileski2024tipextensionand pages 5-7).

**Assay/observation context.** Dumbbell-like incomplete separation is most reliably captured by **time-lapse microscopy** and **septal-envelope reporters** that timestamp late division events (e.g., 6-TMR-Tre septal infiltration followed by V-snapping) (lim2019identificationofnew pages 7-11, lim2019identificationofnew pages 11-12, lim2019identificationofnew pages 16-18).

### 2) Key concepts & mechanistic model (definitions)

#### 2.1 Snapping / V-snapping division
In Corynebacterineae and mycobacteria, daughter separation often occurs via a fast “snapping” step. A key conceptual model from authoritative review literature is:
1) **Septal peptidoglycan (PG)** is synthesized and then cleaved by PG hydrolases.
2) However, **outer envelope layers** (e.g., arabinogalactan and mycolic-acid–containing layers) can remain continuous/intertwined across the septum.
3) Final separation can therefore occur by **rupture of outer layers**, producing an uneven, mechanical “snap” and characteristic angular morphologies (hett2008bacterialgrowthand pages 14-15).

This model provides a direct route to a **two-lobed, isthmus-connected intermediate** (candidate dumbbell-shaped) before the mechanical fracture resolves separation.

#### 2.2 Septal envelope assembly as a mechanistic precursor to snapping
In *Corynebacterium glutamicum*, septal envelope layers assemble **sequentially** (PG first, then mycolate-linked layers, then trehalose glycolipids infiltrate the septum), and trehalose glycolipid diffusion correlates with **perforations in peripheral septal PG** that precede snapping (lim2019identificationofnew pages 16-18). This provides a curatable mechanistic chain from envelope biogenesis → septal weakening → snapping separation.

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Structural mechanism: FtsEX regulation of RipC (2023)
A 2023 *Nature Communications* cryo-EM study provides high-resolution evidence for how the **FtsEX complex** interacts with and regulates a cell-division hydrolase **RipC** in *Mycobacterium tuberculosis*, describing a “Match and Fit” recognition mode and asymmetric rearrangements in FtsX upon RipC binding (li2023regulationofthe pages 1-2, li2023regulationofthe pages 3-5). This strengthens a curatable edge: **FtsEX → regulates → septal PG hydrolase (RipC-family)**.

#### 3.2 Filamentous Corynebacterium lifecycle and V-snapping-like hinge connections (2024)
A 2024 *PNAS* study of *Corynebacterium matruchotii* (a dental-plaque-associated filamentous bacterium) reports a lifecycle with **V-snapping-like division** where compartments can remain connected by a **hinge-like structure** and later separate, in addition to a “simultaneous multiple fission” mode (chimileski2024tipextensionand pages 7-8, chimileski2024tipextensionand pages 5-7). This provides contemporary observational support for a **hinge/isthmus-connected intermediate**, aligning with the dumbbell-shaped definition (though the paper does not use the “dumbbell” label explicitly).

#### 3.3 Envelope perturbations and septal hydrolysis context (2024)
A 2024 dissertation synthesizes evidence that **regulated septal hydrolysis** allows inflow of **trehalose mono-/dimycolates (TMM/TDM)** just prior to v-snapping in *C. glutamicum*, and reports that **ethambutol** disrupts mycolic membrane integrity and induces major morphological changes (meyer2024understandingthegrowth pages 64-68). This is supportive but lower authority than peer-reviewed primary articles; curate as “context/uncertain” unless corroborated by a primary publication.

### 4) Current applications / real-world implementations

1) **Antimicrobial target discovery (cell-wall remodeling).** The RipA/RipC-family PG hydrolases and their regulators (e.g., FtsEX; Cg1604/SteB activation mechanisms) are framed as drug-relevant because they control septal PG hydrolysis and therefore successful division and survival (gaday2022ftsexindependentcontrolof pages 1-2, li2023regulationofthe pages 1-2).

2) **Quantitative microscopy phenotyping for envelope/antibiotic studies.** V-snapping timing can be quantified using septal trehalose reporters; mutants in *steA/steB/ripC/ftsEX* show strong delays (lim2019identificationofnew pages 11-12). Such phenotyping supports systematic mapping from gene perturbation → division mechanics → morphology.

3) **Biofilm and microbiome spatial organization.** The 2024 *PNAS* work connects unusual division modes and morphology in an oral biofilm structural bacterium, implying that division-linked morphologies can shape community architecture in situ (chimileski2024tipextensionand pages 7-8).

### 5) Candidate causal-graph nodes (grouped by type)

#### 5.1 Taxa (NCBITaxon; label-level where not resolved)
- *Corynebacterium glutamicum* (NCBITaxon:1718)
- *Mycobacterium tuberculosis* (NCBITaxon:1773)
- *Corynebacterium matruchotii* (NCBITaxon: not grounded here)
- Corynebacteriales / Corynebacterineae (label-level)

#### 5.2 Cellular processes / structures (GO; label-level where needed)
- Cytokinetic ring / Z-ring (GO:0000921 cytokinetic ring) (lim2019identificationofnew pages 11-12)
- Septal peptidoglycan hydrolysis (GO label-level; general PG metabolism GO:0000270) (gaday2022ftsexindependentcontrolof pages 1-2)
- Polar growth / apical elongation (label-level; DivIVA/Wag31-associated) (kieser2014howsistersgrow pages 2-3)
- Cell envelope layers: peptidoglycan, arabinogalactan, mycolic-acid membrane/mycomembrane (label-level) (hett2008bacterialgrowthand pages 14-15, lim2019identificationofnew pages 16-18)

#### 5.3 Genes/proteins/complexes (UniProt/EC label-level; IDs taxon-specific)
- **FtsZ** (tubulin-like cytokinesis protein; GO:0000917) (kieser2014howsistersgrow pages 2-3)
- **FtsEX complex** (FtsE ATPase + FtsX TM/regulator) (li2023regulationofthe pages 1-2, li2023regulationofthe pages 3-5)
- **RipC** (septal PG hydrolase; NlpC/P60 family) (li2023regulationofthe pages 1-2)
- **RipA / Cg1735** (RipA-family hydrolase; C. glutamicum homologue Cg1735) (gaday2022ftsexindependentcontrolof pages 1-2)
- **SteA/SteB (cgp_1603/cgp_1604)** (septal regulators; SteAB complex) (lim2019identificationofnew pages 1-2)
- **Cg1604/SteB** (transmembrane septal activator of Cg1735) (gaday2022ftsexindependentcontrolof pages 1-2)
- **Wag31/DivIVA** (polar growth scaffold; taxa-specific naming) (kieser2014howsistersgrow pages 2-3)

#### 5.4 Chemicals / perturbations (CHEBI where clear)
- Trehalose (CHEBI:61589); trehalose glycolipid reporters (label-level) (lim2019identificationofnew pages 16-18)
- Ethambutol (CHEBI:4877) (meyer2024understandingthegrowth pages 64-68)

### 6) Evidence-backed candidate causal edges (curation-ready)

The table below is intended to be directly reusable for TraitMech/TraitGraph curation (subject–predicate–object, evidence snippet, and curation notes).

| Edge (Subject—predicate→Object) | Node types | Suggested ontology grounding | Evidence snippet/quote | Reference (DOI + URL + year) | Notes on strength/uncertainty and taxonomy/assay context |
|---|---|---|---|---|---|
| Septal peptidoglycan hydrolysis — enables→ daughter-cell separation / V-snapping | process → process/morphology | GO:0009252 peptidoglycan biosynthetic process; GO:0000270 peptidoglycan metabolic process; label: V-snapping | “daughter cell separation that requires precisely timed and localized peptidoglycan (PG) hydrolysis at the septal junction” (gaday2022ftsexindependentcontrolof pages 1-2) | 10.1073/pnas.2214599119 · https://doi.org/10.1073/pnas.2214599119 · 2022 | Strong mechanistic support in Corynebacteriales; directly relevant to incomplete separation states that can appear dumbbell-like before full snap. |
| Peripheral septal peptidoglycan perforations — precede→ trehalose glycolipid infiltration of the septum | structure/process → chemical/localization process | CHEBI:61589 trehalose; label: peripheral septal PG perforations | “free labeled trehalose glycolipids were observed to infiltrate the septum” and this “correlates with visualization of ‘perforations in the peripheral PG layer’” (lim2019identificationofnew pages 16-18) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong in *Corynebacterium glutamicum* time-lapse assay; useful as an upstream structural state for transient dumbbell/interconnected daughters. |
| Trehalose glycolipid infiltration of septum — precedes→ V-snapping | chemical/localization process → morphology/process | CHEBI:61589 trehalose; label: trehalose glycolipid infiltration; label: V-snapping | “The interval between 6-TMR-Tre infiltration and V-snapping is a measurable kinetic parameter of cell separation efficiency” (lim2019identificationofnew pages 7-11) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong assay-specific temporal edge in *C. glutamicum*; supports a late pre-separation connected morphology. |
| RipC/Cg1735 peptidoglycan endopeptidase activity — promotes→ septal peptidoglycan remodeling | protein/enzyme → process | EC:3.4.-.-; label: RipC/Cg1735; GO:0000270 | “RipC is a peptidoglycan (PG) cleaving enzyme required for proper cell division” (lim2019identificationofnew pages 1-2) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong, but naming differs by taxon/source (RipC vs Cg1735 homologue vs RipA-family context). |
| RipC/Cg1735 loss or depletion — causes→ elongated multi-septated / chained cells with unresolved septa | protein perturbation → morphology | label: RipC/Cg1735; label: elongated multi-septated cells; label: chained cells | “loss or depletion of RipA/Cg1735 produces elongated, multi-septated cells and chain-like separation defects” (gaday2022ftsexindependentcontrolof pages 1-2) | 10.1073/pnas.2214599119 · https://doi.org/10.1073/pnas.2214599119 · 2022 | Strong phenotype edge for failed separation; morphology is adjacent to, but not identical with, dumbbell-shaped. Curate as related/boundary phenotype. |
| FtsEX complex — regulates/activates→ RipC-family cell division hydrolase | protein complex → protein/enzyme | label: FtsE; label: FtsX; label: RipC; GO:0009252 | “The FtsEX complex regulates… peptidoglycan-hydrolases” and in *M. tuberculosis* structures “RipC is recognized” by FtsEX (li2023regulationofthe pages 1-2, li2023regulationofthe pages 3-5) | 10.1038/s41467-023-43770-6 · https://doi.org/10.1038/s41467-023-43770-6 · 2023 | Strong structural evidence in *Mycobacterium tuberculosis*; transfer to other Corynebacterineae is plausible but taxon-specific details vary. |
| FtsEX or RipC deletion — delays→ V-snapping | protein perturbation → process/morphology | label: FtsEX; label: RipC; label: V-snapping delay | “deletion of FtsEX or its associated hydrolase delays V-snapping” (li2023regulationofthe pages 1-2) | 10.1038/s41467-023-43770-6 · https://doi.org/10.1038/s41467-023-43770-6 · 2023 | Strong but summarized across Corynebacterineae literature; assay/mutant phenotype context. |
| SteA/SteB complex — localizes to→ cytokinetic ring | protein complex → cellular structure | label: SteA/Cg1603; label: SteB/Cg1604; GO:0000921 cytokinetic ring | “SteA and SteB form a complex that localizes to the cytokinetic ring” (lim2019identificationofnew pages 1-2) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong localization evidence in *C. glutamicum*. |
| SteAB complex — promotes→ cell separation by RipC–FtsEX module | protein complex → process/pathway | label: SteA/Cg1603; label: SteB/Cg1604; label: RipC-FtsEX cell separation pathway | “SteA and SteB form a complex that localizes to the cytokinetic ring and promotes cell separation by the RipC-FtsEX module” (lim2019identificationofnew pages 1-2) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong pathway-level evidence; likely central to curatable graph. |
| SteA, SteB, RipC, or FtsEX deletion — prolongs→ V-snap delay | protein perturbation → process phenotype | label: V-snap delay | “ΔsteA, ΔsteB, ΔripC and ΔftsEX mutants show a markedly prolonged V-snap delay (31.7–45 min versus ~4–8 min in wild type)” (lim2019identificationofnew pages 11-12) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong quantitative evidence in *C. glutamicum*; among the best direct statistics for this trait neighborhood. |
| Cg1604 (SteB) extracellular domain — relieves autoinhibition of→ Cg1735/RipA-family hydrolase | protein → protein/enzyme | label: Cg1604/SteB; label: Cg1735; label: RipA-family NlpC/P60 endopeptidase | “This autoinhibition is relieved by the extracellular core domain of the transmembrane septal protein Cg1604” (gaday2022ftsexindependentcontrolof pages 1-2) | 10.1073/pnas.2214599119 · https://doi.org/10.1073/pnas.2214599119 · 2022 | Strong structural/biochemical evidence in *C. glutamicum* homologue system; naming between SteB and Cg1604 should be harmonized carefully. |
| Cg1735/RipA-family N-terminal coiled-coil autoinhibition — inhibits→ catalytic NlpC/P60 domain | protein structural feature → molecular function | label: Cg1735; label: NlpC/P60 catalytic domain | “full-length Cg1735 is autoinhibited: its C-terminal NlpC/P60 catalytic domain is occluded by an N-terminal conserved coiled-coil” (gaday2022ftsexindependentcontrolof pages 1-2) | 10.1073/pnas.2214599119 · https://doi.org/10.1073/pnas.2214599119 · 2022 | Strong mechanistic edge; useful upstream of cell separation phenotype but not specific by itself to dumbbell morphology. |
| FtsEX–RipC–SteAB septal complex — promotes→ enlargement of initial septal perforations / septal PG remodeling | protein complex → process/structure | label: FtsEX-RipC-SteAB complex; label: septal PG remodeling | “SteAB forms part of the FtsEX-RipC complex… to promote septal PG remodeling and daughter cell separation via V-snapping” (lim2019identificationofnew pages 16-18) | 10.1371/journal.pgen.1008284 · https://doi.org/10.1371/journal.pgen.1008284 · 2019 | Strong integrative model; direct biochemical contacts partly incomplete, so represent as complex/pathway-level edge. |
| Septal peptidoglycan cleavage followed by continuity of AG/MA outer layers — leads to→ mechanical snapping separation | process + structure → process/morphology | label: arabinogalactan; label: mycolic acids; label: mechanical snapping | “overlying envelope layers — notably arabinogalactan (AG), mycolic acids (MA), and other lipids — remain continuous across the septum… separation frequently occurs by rupture of these outer layers, producing an uneven mechanical ‘snapping’” (hett2008bacterialgrowthand pages 14-15) | 10.1128/mmbr.00028-07 · https://doi.org/10.1128/mmbr.00028-07 · 2008 | Strong review synthesis for Corynebacterineae/Mycobacteriales; highly relevant to transient two-lobed/dumbbell intermediates, but morphology term itself is inferred rather than explicitly named in this source. |
| Mechanical rupture of intertwined outer envelope layers — produces→ V-shaped attached daughters / palisade-like arrangements | structure/process → morphology | label: outer envelope rupture; label: V-shaped daughters; label: palisade arrangement | “uneven rupturing produces the V-shape” (hett2008bacterialgrowthand pages 14-15); “Snapping division produces angular and palisade arrangements of cells” (bernard2020 snippet in search results) | 10.1128/mmbr.00028-07 · https://doi.org/10.1128/mmbr.00028-07 · 2008 | Strong for V-shapes from review; palisade claim present in search snippet but not grounded to a context ID here, so curate V-shape edge confidently and palisade aspect cautiously. |
| V-snapping-like hinge attachment — yields→ partially separated two-lobed daughters (candidate dumbbell-shaped state) | morphology/process → morphology | METPO:1000672 dumbbell shaped; label: hinge attachment | “daughter cells remain partially attached via a hinge-like connection after septation” (chimileski2024tipextensionand pages 5-7); “partial attachment of daughter cells by a hinge-like structure” (chimileski2024tipextensionand pages 5-7) | 10.1073/pnas.2408654121 · https://doi.org/10.1073/pnas.2408654121 · 2024 | Moderate support: source explicitly supports hinge-linked incomplete separation in *Corynebacterium matruchotii*, but does not use the term dumbbell-shaped. Good candidate phenotype-level mapping, mark as inferred. |
| Regulated hydrolysis near septum — allows inflow of→ trehalose monomycolate/dimycolate (TMM/TDM) | process → chemical/localization process | CHEBI:61589 trehalose; label: trehalose monomycolate; label: trehalose dimycolate | “regulated hydrolysis of the surface proximal the septum allows for an inflow of trehalose mono- and dimycolates (TMM / TDM)” (meyer2024understandingthegrowth pages 64-68) | 10.5282/edoc.33534 · https://doi.org/10.5282/edoc.33534 · 2024 | Moderate evidence from dissertation synthesis; useful but lower authority than peer-reviewed primary papers. |
| Ethambutol treatment — impairs→ mycolic membrane integrity and alters septation-associated morphology | chemical perturbation → structure/morphology | CHEBI:4877 ethambutol | “the integrity of the MM becomes impaired upon EMB treatment,” producing “lemon-shaped morphology” and “a much higher fraction of cells with a forming septum” (meyer2024understandingthegrowth pages 64-68) | 10.5282/edoc.33534 · https://doi.org/10.5282/edoc.33534 · 2024 | Moderate, assay/drug specific and not directly dumbbell-shaped; better as perturbation context than core causal edge. |
| RipA and RpfB — cleave→ septum to separate daughter cells | proteins/enzymes → process | label: RipA; label: RpfB | “RipA and RpfB… ‘cleave the septum to separate the daughter cells’” (kieser2014howsistersgrow pages 5-6) | 10.1038/nrmicro3299 · https://doi.org/10.1038/nrmicro3299 · 2014 | Strong review statement for mycobacteria; useful broader support for septal hydrolase role. |
| Polar growth from nascent septum — aggravates→ rupture/snapping of outer layers | process → process/morphology | GO:0071709 membrane assembly?; label: polar growth | “Polar growth from the nascent septum can aggravate rupture” (hett2008bacterialgrowthand pages 14-15) | 10.1128/mmbr.00028-07 · https://doi.org/10.1128/mmbr.00028-07 · 2008 | Moderate review-derived mechanistic hypothesis; relevant to why attached daughters may transiently assume a dumbbell-like two-bulb form before full snap. |


*Table: This table compiles curation-ready candidate causal edges for the microbial morphology trait 'dumbbell shaped' in Corynebacterineae/Actinobacteria, using only evidence from sources already discussed. It emphasizes septal peptidoglycan hydrolysis, envelope-layer mechanics, and regulatory complexes that can generate transient incomplete-separation morphologies relevant to TraitMech curation.*

### 7) Key data/statistics from recent studies

**Quantitative separation phenotype (best available):** In *C. glutamicum*, deletion of **steA, steB, ripC, or ftsEX** dramatically prolongs the time between septal trehalose infiltration and the snapping event (**V-snap delay**), reported as **31.7–45 min vs ~4–8 min in wild type** (lim2019identificationofnew pages 11-12). This is a strong quantitative marker of incomplete separation likely increasing the dwell time of dumbbell-like intermediates.

**Filamentous multiple-septation quantitative context (2024):** In *C. matruchotii*, individual filaments ranged from **1 to >30 µm**, with an extreme example of **93 µm** with **28 septa** poised to yield **29 daughters**, illustrating that incomplete separation and multiseptation can co-occur in certain Corynebacterium lifestyles (chimileski2024tipextensionand pages 5-7).

### 8) Expert synthesis / analysis (authoritative opinions)

A consistent expert-level synthesis across reviews and mechanistic studies is that Corynebacterineae cell separation is **not merely enzymatic cleavage of septal PG**, but rather a **two-layer problem**: (i) localized PG hydrolysis, tightly regulated to avoid lysis, and (ii) resolution of continuity/intertwining in outer envelope layers (AG/mycolates), which can force a final **mechanical rupture (“snap”)** (hett2008bacterialgrowthand pages 14-15, lim2019identificationofnew pages 16-18, gaday2022ftsexindependentcontrolof pages 1-2). This integrated view is particularly important for curating “dumbbell shaped,” because a dumbbell-like intermediate is most plausibly explained as a **failure/delay in one or more steps of this coupled process**.

### 9) Real-world curation warnings (do-not-curate-yet / uncertain)

1) **Trait mapping uncertainty:** Several sources strongly support hinge-linked incomplete separation and V-shaped pairs, but do **not** explicitly use the term “dumbbell-shaped” for Corynebacterineae. Mapping hinge-linked daughters → METPO:1000672 should be flagged as **inferred** unless a source explicitly labels this morphology as dumbbell-shaped in bacteria (chimileski2024tipextensionand pages 5-7).

2) **Taxon transfer caution:** Structural regulation of RipC by FtsEX in *M. tuberculosis* is high-confidence, but specific pathway wiring (e.g., SteAB involvement) may differ among Corynebacteriales; edges should be either taxon-scoped or marked “conserved/inferred” (li2023regulationofthe pages 1-2, li2023regulationofthe pages 3-5).

3) **Lower-authority sources:** Dissertation-derived claims about TMM/TDM inflow and drug-induced morphologies are useful but should be curated as **supporting context** unless independently corroborated by peer-reviewed primary literature (meyer2024understandingthegrowth pages 64-68).

4) **2011 Corynebacterineae review not retrieved:** The provided prior evidence DOI (10.1111/j.1574-6976.2011.00298.x) could not be obtained within the current tool run; do not cite it as direct evidence until retrieved and verified.

### 10) DOI-first bibliography (with URLs and publication dates where available)

- **Hett EC, Rubin EJ.** *Bacterial Growth and Cell Division: a Mycobacterial Perspective.* **Microbiology and Molecular Biology Reviews** (Mar **2008**). DOI: **10.1128/mmbr.00028-07**. https://doi.org/10.1128/mmbr.00028-07 (hett2008bacterialgrowthand pages 14-15)
- **Kieser KJ, Rubin EJ.** *How sisters grow apart: mycobacterial growth and division.* **Nature Reviews Microbiology** (Jul **2014**). DOI: **10.1038/nrmicro3299**. https://doi.org/10.1038/nrmicro3299 (kieser2014howsistersgrow pages 2-3, kieser2014howsistersgrow pages 5-6)
- **Lim HC, Sher JW, Rodriguez-Rivera FP, et al.** *Identification of new components of the RipC–FtsEX cell separation pathway of Corynebacterineae.* **PLOS Genetics** (Aug **2019**). DOI: **10.1371/journal.pgen.1008284**. https://doi.org/10.1371/journal.pgen.1008284 (lim2019identificationofnew pages 7-11, lim2019identificationofnew pages 11-12, lim2019identificationofnew pages 16-18, lim2019identificationofnew media 9d23e710, lim2019identificationofnew media c50a270b, lim2019identificationofnew media 13aaf867)
- **Gaday Q, Megrian D, Carloni G, et al.** *FtsEX-independent control of RipA-mediated cell separation in Corynebacteriales.* **PNAS** (Dec **2022**). DOI: **10.1073/pnas.2214599119**. https://doi.org/10.1073/pnas.2214599119 (gaday2022ftsexindependentcontrolof pages 1-2)
- **Li J, Xu X, Shi J, et al.** *Regulation of the cell division hydrolase RipC by the FtsEX system in Mycobacterium tuberculosis.* **Nature Communications** (Dec **2023**). DOI: **10.1038/s41467-023-43770-6**. https://doi.org/10.1038/s41467-023-43770-6 (li2023regulationofthe pages 1-2, li2023regulationofthe pages 3-5)
- **Chimileski S, Borisy GG, Dewhirst FE, Welch JLM.** *Tip extension and simultaneous multiple fission in a filamentous bacterium.* **PNAS** (Sep **2024**). DOI: **10.1073/pnas.2408654121**. https://doi.org/10.1073/pnas.2408654121 (chimileski2024tipextensionand pages 7-8, chimileski2024tipextensionand pages 5-7)
- **Meyer FM.** *Understanding the growth of Corynebacterium glutamicum.* Dissertation (Jan **2024**). DOI: **10.5282/edoc.33534**. https://doi.org/10.5282/edoc.33534 (meyer2024understandingthegrowth pages 64-68)


References

1. (chimileski2024tipextensionand pages 5-7): Scott Chimileski, Gary G. Borisy, Floyd E. Dewhirst, and Jessica L. Mark Welch. Tip extension and simultaneous multiple fission in a filamentous bacterium. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2408654121, doi:10.1073/pnas.2408654121. This article has 12 citations and is from a highest quality peer-reviewed journal.

2. (chimileski2024tipextensionand pages 10-10): Scott Chimileski, Gary G. Borisy, Floyd E. Dewhirst, and Jessica L. Mark Welch. Tip extension and simultaneous multiple fission in a filamentous bacterium. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2408654121, doi:10.1073/pnas.2408654121. This article has 12 citations and is from a highest quality peer-reviewed journal.

3. (hett2008bacterialgrowthand pages 14-15): Erik C. Hett and Eric J. Rubin. Bacterial growth and cell division: a mycobacterial perspective. Microbiology and Molecular Biology Reviews, 72:126-156, Mar 2008. URL: https://doi.org/10.1128/mmbr.00028-07, doi:10.1128/mmbr.00028-07. This article has 661 citations and is from a domain leading peer-reviewed journal.

4. (gaday2022ftsexindependentcontrolof pages 1-2): Quentin Gaday, Daniela Megrian, Giacomo Carloni, Mariano Martinez, Bohdana Sokolova, Mathilde Ben Assaya, Pierre Legrand, Sebastien Brûlé, Ahmed Haouz, Anne Marie Wehenkel, and Pedro M. Alzari. Ftsex-independent control of ripa-mediated cell separation in corynebacteriales. Proceedings of the National Academy of Sciences of the United States of America, Dec 2022. URL: https://doi.org/10.1073/pnas.2214599119, doi:10.1073/pnas.2214599119. This article has 19 citations and is from a highest quality peer-reviewed journal.

5. (lim2019identificationofnew pages 6-7): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

6. (chimileski2024tipextensionand pages 7-8): Scott Chimileski, Gary G. Borisy, Floyd E. Dewhirst, and Jessica L. Mark Welch. Tip extension and simultaneous multiple fission in a filamentous bacterium. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2408654121, doi:10.1073/pnas.2408654121. This article has 12 citations and is from a highest quality peer-reviewed journal.

7. (lim2019identificationofnew pages 7-11): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

8. (lim2019identificationofnew pages 11-12): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

9. (lim2019identificationofnew pages 16-18): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

10. (li2023regulationofthe pages 1-2): Jianwei Li, Xin Xu, Jian Shi, Juan A. Hermoso, Lok-To Sham, and Min Luo. Regulation of the cell division hydrolase ripc by the ftsex system in mycobacterium tuberculosis. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43770-6, doi:10.1038/s41467-023-43770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

11. (li2023regulationofthe pages 3-5): Jianwei Li, Xin Xu, Jian Shi, Juan A. Hermoso, Lok-To Sham, and Min Luo. Regulation of the cell division hydrolase ripc by the ftsex system in mycobacterium tuberculosis. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43770-6, doi:10.1038/s41467-023-43770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

12. (meyer2024understandingthegrowth pages 64-68): Fabian Mark Meyer. Understanding the growth of corynebacterium glutamicum. Dissertation, Jan 2024. URL: https://doi.org/10.5282/edoc.33534, doi:10.5282/edoc.33534. This article has 0 citations.

13. (kieser2014howsistersgrow pages 2-3): Karen J. Kieser and Eric J. Rubin. How sisters grow apart: mycobacterial growth and division. Nature Reviews Microbiology, 12:550-562, Jul 2014. URL: https://doi.org/10.1038/nrmicro3299, doi:10.1038/nrmicro3299. This article has 358 citations and is from a highest quality peer-reviewed journal.

14. (lim2019identificationofnew pages 1-2): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

15. (kieser2014howsistersgrow pages 5-6): Karen J. Kieser and Eric J. Rubin. How sisters grow apart: mycobacterial growth and division. Nature Reviews Microbiology, 12:550-562, Jul 2014. URL: https://doi.org/10.1038/nrmicro3299, doi:10.1038/nrmicro3299. This article has 358 citations and is from a highest quality peer-reviewed journal.

16. (lim2019identificationofnew media 9d23e710): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

17. (lim2019identificationofnew media c50a270b): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.

18. (lim2019identificationofnew media 13aaf867): Hoong Chuin Lim, Joel W. Sher, Frances P. Rodriguez-Rivera, Coralie Fumeaux, Carolyn R. Bertozzi, and Thomas G. Bernhardt. Identification of new components of the ripc-ftsex cell separation pathway of corynebacterineae. PLOS Genetics, 15:e1008284, Aug 2019. URL: https://doi.org/10.1371/journal.pgen.1008284, doi:10.1371/journal.pgen.1008284. This article has 58 citations and is from a domain leading peer-reviewed journal.