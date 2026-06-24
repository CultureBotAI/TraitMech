---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:52:02.546484'
end_time: '2026-06-18T07:20:16.584499'
duration_seconds: 1694.04
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell shape
  trait_identifier: METPO:1000666
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_shape
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes the characteristic three-dimensional morphological
    form of a microbial cell, determined by cell wall structure, cytoskeletal elements,
    and environmental factors.
  parent_traits: METPO:1000059
  synonyms: Morphology.cell morphology.cell shape, cell_shape
  evidence_summary: 'DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role
    in maintaining cell shape (Supports bacterial cell shape as determined by cell
    wall and cytoskeletal elements.)'
  causal_graph_summary: 'cell_shape_peptidoglycan_cytoskeleton: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell shape
- **METPO identifier:** METPO:1000666
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.cell shape, cell_shape
- **Existing evidence:** DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role in maintaining cell shape (Supports bacterial cell shape as determined by cell wall and cytoskeletal elements.)
- **Existing causal graph summary:** cell_shape_peptidoglycan_cytoskeleton: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **cell shape** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_shape.yaml`.

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
- **Trait label:** cell shape
- **METPO identifier:** METPO:1000666
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.cell shape, cell_shape
- **Existing evidence:** DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role in maintaining cell shape (Supports bacterial cell shape as determined by cell wall and cytoskeletal elements.)
- **Existing causal graph summary:** cell_shape_peptidoglycan_cytoskeleton: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **cell shape** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_shape.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Cell Shape (METPO:1000666)

**Target trait:** cell shape (METPO:1000666)  
**Category:** MORPHOLOGY  
**Definition (given):** “A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.”  

This report summarizes current mechanistic understanding (with emphasis on 2023–2024 literature), proposes evidence-backed causal edges suitable for TraitMech curation, suggests ontology grounding, and highlights applications/real-world implementations and quantitative data.

---

## 1) Trait scope (phenotype definition, boundaries, and assay context)

### 1.1 What “cell shape” represents
For most bacteria, **cell shape is a property of the whole-cell 3D outline** (e.g., rod, coccus/sphere, curved/vibrioid, helical, filamentous, pleomorphic). Mechanistically it is largely a **material/architecture phenotype**: the extracellular **peptidoglycan sacculus defines shape** and must be remodeled during growth and division. Multiple sources explicitly state this relationship, including the direct statement “**Peptidoglycan determines cell shape**” (ago2023relationshipbetweenthe pages 1-3) and the view that peptidoglycan “defines cell shape” as an external barrier polymer (micelli2023aconservedzincbinding pages 1-2).

**Key mechanistic distinction:** shape is controlled by **where and how new cell-wall material is inserted** and remodeled. In a 2024 study of *E. coli* L-forms, the authors frame this directly: “**Cell elongation is associated with cell shape determination because cell shape is determined by the shape of the newly synthesized peptidoglycan cell wall**” (hayashi2024septalwallsynthesis pages 1-2).

### 1.2 Boundary cases and nearby traits
* **Cell size vs. cell shape:** size metrics (length, diameter, volume) are related but distinct from shape class. Several mechanisms (e.g., aPBP activity) affect diameter/size without necessarily changing “rod vs sphere” class, and therefore should be curated separately when the phenotype is size-only (zhang2023coordinatedpeptidoglycansynthases pages 1-2).
* **Cell arrangement (chains, clusters) vs. shape:** arrangement reflects post-division separation and adhesion; it can co-occur with shape defects but is not the same trait.
* **Wall-less states (L-forms) as boundary cases:** “wall-less” bacteria challenge the default assumption that peptidoglycan is required for a defined shape. In *E. coli* L-forms, heterogeneous morphology can be converted to a “mostly uniform oval shape solely by FtsZ-dependent division” (hayashi2024septalwallsynthesis pages 1-2). For curation, this suggests a separate conditional branch where **division/geometry constraints can impose shape even with minimal wall synthesis**.

### 1.3 Assay context
Cell shape is typically assayed by **microscopy** (phase contrast, fluorescence, cryo-EM/ET) and quantified via segmentation. Recent mechanistic work relies heavily on **single-molecule imaging** of envelope synthases (schaper2024cellconstrictionrequires pages 1-2, whitley2024peptidoglycansynthesisdrives pages 1-2) and on high-resolution envelope imaging (cryo-ET) for envelope constriction defects (lakey2023theroleof pages 2-4).

---

## 2) Key concepts and current mechanistic understanding (2023–2024 prioritized)

### 2.1 Core architecture: peptidoglycan and its synthesis/remodeling
Peptidoglycan is a mesh-like polymer that “defines cell shape” and is assembled by glycosyltransferase-catalyzed polymerization and transpeptidase-mediated crosslinking (micelli2023aconservedzincbinding pages 1-2). The **mechanistic levers for shape** include:

* **Elongation systems (elongasome/Rod complex):** dispersed lateral-wall insertion supporting rod morphology (micelli2023aconservedzincbinding pages 1-2, garciaheredia2023plasmamembranecellwall pages 6-7).
* **Division systems (divisome):** septal synthesis and remodeling that create new poles and set daughter-cell geometry (schaper2024cellconstrictionrequires pages 1-2, whitley2024peptidoglycansynthesisdrives pages 1-2).
* **Hydrolase–synthase coordination:** insertion requires local cleavage/openings; disrupting coordination can collapse shape (zhang2023coordinatedpeptidoglycansynthases pages 1-2).

### 2.2 Cytoskeletal control: MreB and FtsZ
* **MreB (actin homolog):** directs/organizes sites of wall insertion by “associating and guiding the Rod complex” (garciaheredia2023plasmamembranecellwall pages 6-7), linking cytoskeletal patterning to rod-shape maintenance.
* **FtsZ (tubulin homolog):** organizes divisome assembly and recruits septal synthases; in *S. aureus*, cell constriction depends on processive septal synthase motion even when FtsZ treadmilling is impaired (schaper2024cellconstrictionrequires pages 1-2), reinforcing that **peptidoglycan synthesis can be the primary mechanical driver of constriction**.

### 2.3 Curvature modules beyond the canonical Rod/divisome systems
Cell curvature can be generated by “symmetry-breaking mechanisms” that locally bias envelope growth. A 2024 Nature Communications study identifies an **outer-membrane patterning module**: Por39/Por41 form a helical ribbon recruiting PapS; disrupting PapS or the porin–PapS interface causes “cell straightening,” and the assembly “bias[es] cell growth towards the outer curve” (pohl2024anoutermembrane pages 1-2).

### 2.4 Membrane–cell wall feedback as an upstream regulator of shape
Membrane physical state influences MreB assembly and, therefore, where wall is inserted:
* A22 inhibition reduces MreB filaments; peptidoglycan synthesis continues diffusely, and “uncoordinated peptidoglycan synthesis… results in loss of rod shape and concomitant lysis” (garciaheredia2023plasmamembranecellwall pages 6-7).
* Increased lipid order or cardiolipin interferes with MreB filament assembly (garciaheredia2023plasmamembranecellwall pages 6-7).
* Flotillin absence reduces MreB activity and cell wall synthesis (garciaheredia2023plasmamembranecellwall pages 6-7).

---

## 3) Candidate causal graph entities (nodes) grouped by type

### 3.1 Pathways/modules (process nodes)
* Peptidoglycan biosynthetic process (GO candidate)
* Peptidoglycan metabolic process / cell wall biogenesis (GO candidate)
* Cell division (GO candidate)
* Septal peptidoglycan synthesis (GO candidate)
* Elongasome/Rod system activity (label node; complex/process)
* Divisome activity (label node; complex/process)
* Cell wall remodeling / hydrolase activity (GO candidate)
* Membrane organization / membrane fluidity regulation (GO candidate)

### 3.2 Genes/proteins/complexes (mechanistic nodes)
**Elongation / Rod system:** MreB, RodZ, RodA (SEDS), PBP2 (class B PBP), MreC, MreD (ago2023relationshipbetweenthe pages 18-19, micelli2023aconservedzincbinding pages 1-2)

**Division/divisome:** FtsZ, FtsW, PBP1 (septal PBP in *S. aureus*), PBP2B (*B. subtilis* divisome TPase), DivIB, MurJ (lipid II flippase; mentioned as lipid II flippase in divisome context) (schaper2024cellconstrictionrequires pages 1-2, whitley2024peptidoglycansynthesisdrives pages 1-2)

**Hydrolases/remodeling enzymes:** DacB (hydrolytic peptidase; pole degradation in *M. xanthus*) (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

**Curvature module:** Por39, Por41, PapS (outer-membrane porin–lipoprotein complex) (pohl2024anoutermembrane pages 1-2)

**Archaeal shape determinants (cross-domain microbial):** RdfA, DdfA, volactin (actin homolog) (schiller2024identificationofstructural pages 1-2)

### 3.3 Chemicals, nutrients, ions, inhibitors
* Peptidoglycan-targeting antibiotics: moenomycin (aPBP inhibitor) (zhang2023coordinatedpeptidoglycansynthases pages 1-2), oxacillin/β-lactams affecting PBP recruitment (puls2023inhibitionofpeptidoglycan pages 1-2), carbapenems (PBP2 target context) (micelli2023aconservedzincbinding pages 1-2)
* MreB inhibitor: A22 (garciaheredia2023plasmamembranecellwall pages 6-7)
* Ions: Zn2+ (PBP2 zinc-binding site requirement), Mg2+ (environmental modulator; evidence weaker in this corpus) (micelli2023aconservedzincbinding pages 1-2, middlemiss2023moleculartugofwarregulates pages 114-118)
* Nucleotides: GTP/ATP (FtsZ GTPase; MreB ATP dependence is supported by broader evidence set) (schaper2024cellconstrictionrequires pages 1-2, mao2023ontherole pages 22-23)

### 3.4 Environmental/experimental factors
* Growth phase and motility state affecting archaeal rod/disk states (schiller2024identificationofstructural pages 1-2)
* Membrane lipid order/fluidity (garciaheredia2023plasmamembranecellwall pages 6-7)
* Osmoprotective/isotonic conditions influencing lysis vs morphology (kawai2023onthemechanisms pages 1-2)

---

## 4) Evidence-backed candidate causal edges (triples)

The following table is designed for direct curator use.

| Subject node | Predicate | Object node | Taxon/context | Evidence snippet (short quote) | Reference (DOI, year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| Peptidoglycan | determines | cell shape | Broad bacterial scope | “Peptidoglycan determines cell shape” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | Strong, broad bacterial claim; suitable as a central trait edge. |
| Rod complex | shapes/organizes | peptidoglycan architecture | *Escherichia coli* | Rod complex “may be a determinant not only for the whole shape of peptidoglycan but also for its highly dense structure” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | Supports cell-shape mechanism through wall architecture. |
| MreB | organizes | cell-wall synthesis for rod shape | Rod-shaped bacteria | MreB “coordinate[s] with PG synthases” and is linked to “rod shape” (battaje2023modelsversuspathogens pages 3-4, costa2024theroleof pages 1-2) | 10.1042/bsr20221664, 2023, https://doi.org/10.1042/bsr20221664; 10.1128/mbio.03235-23, 2024, https://doi.org/10.1128/mbio.03235-23 | Generalized from reviews and comparative data; curate as broad bacterial rod-shape mechanism. |
| RodZ | maintains/enables | rod shape | *E. coli* / *Bacillus subtilis* context | RodZ “link[s] MreB to cell wall synthesis” and RodZ structures “maintain rod shape” (ago2023relationshipbetweenthe pages 18-19) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | Strong but mostly bacterial-rod specific. |
| RodA | polymerizes peptidoglycan for | elongasome-directed cell shape | *Acinetobacter baumannii* and broad bacteria | RodA performs PG transglycosylation and the elongasome inserts PG at lateral-wall sites for rod-shaped growth (micelli2023aconservedzincbinding pages 1-2) | 10.1073/pnas.2215237120, 2023, https://doi.org/10.1073/pnas.2215237120 | Strong for rod-shaped bacteria; mechanism extends beyond one taxon but evidence here is pathogen-focused. |
| PBP2 | is required for | elongasome-directed cell shape | *A. baumannii* | “PBP2… required for elongasome-directed bacterial cell shape” and loss causes “rod-to-sphere morphological transition” (micelli2023aconservedzincbinding pages 1-2) | 10.1073/pnas.2215237120, 2023, https://doi.org/10.1073/pnas.2215237120 | Strong, direct edge. |
| MreC/MreD | balance interaction between | PBP2 and RodA | *E. coli* / *B. subtilis* elongasome | MreC and MreD “balance the interaction” between “PBP2 and RodA” (ago2023relationshipbetweenthe pages 18-19, middlemiss2023moleculartugofwarregulates pages 111-114) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | Mechanistic interaction edge; shape effect is indirect via elongasome regulation. |
| FtsZ-dependent division | is sufficient to convert | heterogeneous L-form morphology to oval shape | *E. coli* L-forms | L-forms “can be converted to a mostly uniform oval shape solely by FtsZ-dependent division” (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y, 2024, https://doi.org/10.1038/s42003-024-07279-y | Boundary-case evidence; useful warning that shape can be imposed even without cylindrical wall synthesis. |
| Septal peptidoglycan synthesis | drives | septum constriction / division shape change | *Staphylococcus aureus* | “peptidoglycan synthesis is the essential driving force of septum constriction” (puls2023inhibitionofpeptidoglycan pages 1-2) | 10.1126/sciadv.ade9023, 2023, https://doi.org/10.1126/sciadv.ade9023 | Strong divisome edge; shape outcome mainly septal morphology rather than whole-cell class. |
| FtsW/PBP1 complex | drives | cell constriction | *S. aureus* | “a single population of processively moving FtsW/PBP1… drives cell constriction” (from abstract/evidence summary) (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s41564-024-01629-6, 2024, https://doi.org/10.1038/s41564-024-01629-6 | Supported in conversation summary; use with moderate caution because direct quote is from extracted abstract summary. |
| Moenomycin inhibition of aPBPs | causes | rapid collapse of rod shape | *Myxococcus xanthus* | moenomycin “causes rapid collapse of rod shape” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3, 2023, https://doi.org/10.1038/s41467-023-41082-3 | Strong chemical perturbation edge; taxon-specific implementation should be flagged. |
| Inhibited PBP1a2 | promotes | DacB binding to peptidoglycan | *M. xanthus* under moenomycin | inhibited PBP1a2 “promotes binding between the hydrolase DacB and PG” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3, 2023, https://doi.org/10.1038/s41467-023-41082-3 | Strong mechanistic edge; specific to one aPBP/hydrolase pair. |
| DacB-mediated pole degradation | causes | rod-shape collapse | *M. xanthus* under moenomycin | DacB degradation of poles is linked to “loss of rod shape” (zhang2023coordinatedpeptidoglycansynthases pages 1-2, zhang2023coordinatedpeptidoglycansynthases media 8bf57c47) | 10.1038/s41467-023-41082-3, 2023, https://doi.org/10.1038/s41467-023-41082-3 | Strong, but taxon- and assay-specific; curate with context. |
| A22 (MreB inhibitor) | causes | loss of rod shape and lysis | Broad bacterial / membrane-feedback context | “A22 reduces MreB filaments… leading to loss of rod shape and lysis” (garciaheredia2023plasmamembranecellwall pages 6-7) | 10.1128/jb.00433-22, 2023, https://doi.org/10.1128/jb.00433-22 | Strong perturbation edge; chemical tool, not endogenous mechanism. |
| Cardiolipin / increased lipid order | interferes with | MreB assembly | Broad bacterial / membrane-feedback context | “increased lipid order or… cardiolipin interferes with MreB assembly” (garciaheredia2023plasmamembranecellwall pages 6-7) | 10.1128/jb.00433-22, 2023, https://doi.org/10.1128/jb.00433-22 | Indirect edge to cell shape via MreB; curate as membrane modulation. |
| Flotillins | promote | MreB activity and cell wall synthesis | Broad bacterial / membrane-feedback context | absence of flotillins “downregulates MreB activity and cell wall synthesis” (garciaheredia2023plasmamembranecellwall pages 6-7) | 10.1128/jb.00433-22, 2023, https://doi.org/10.1128/jb.00433-22 | Indirect shape determinant through membrane organization; broad but not universal. |
| Excess Mg2+ | rescues | mreB mutant morphology via hydrolase inhibition | *B. subtilis* / Gram-positive context | “magnesium rescues mreB mutant morphology via inhibition of peptidoglycan hydrolases” (middlemiss2023moleculartugofwarregulates pages 114-118) | thesis/review-derived evidence in conversation, 2023, no stable journal DOI available in extracted text | Useful environmental edge, but source in conversation is secondary/dissertation-style; mark uncertain until verified in primary paper. |
| Por39/Por41–PapS complex | biases growth to establish | cell curvature | *Rhodospirillum rubrum* | PapS inactivation or interface disruption results in “cell straightening”; assemblies “bias cell growth towards the outer curve” (pohl2024anoutermembrane pages 1-2) | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | Strong, novel curvature module; likely taxon-specific rather than universal. |
| PBP2 Zn-binding site | is required for | rod cell shape | *A. baumannii* | mutations disrupting Zn coordination “cause loss of rod shape” (micelli2023aconservedzincbinding pages 1-2) | 10.1073/pnas.2215237120, 2023, https://doi.org/10.1073/pnas.2215237120 | Strong within proteobacterial PBP2 context; broader conservation plausible but still lineage-biased. |
| Volactin | contributes to | disk-shape morphogenesis | *Haloferax volcanii* | volactin “plays a role in disk-shape morphogenesis” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Archaeal, not bacterial; include only if TraitMech scope allows cross-domain microbial curation. |
| RdfA | is required for | rod formation | *H. volcanii* | “RdfA… required for the formation of rods” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Archaeal and species-specific; valuable as non-bacterial comparison. |
| DdfA | is required for | disk formation | *H. volcanii* | “DdfA [is] required for the formation of… disks” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Archaeal and species-specific; likely separate branch from bacterial PG-based mechanisms. |


*Table: This table compiles candidate causal edges for the microbial trait cell shape, emphasizing experimentally supported links among peptidoglycan synthesis, cytoskeletal systems, membrane factors, environmental perturbations, and shape outcomes. It is designed to help curate a TraitMech-style causal graph while flagging taxon-specific or uncertain claims.*

**Visual support:** Zhang et al. (2023) figure panels illustrating moenomycin-induced rod-shape collapse and DacB/PBP1a2-dependent coordination were retrieved (zhang2023coordinatedpeptidoglycansynthases media 8bf57c47, zhang2023coordinatedpeptidoglycansynthases media e87c1d22).

---

## 5) Recent developments (2023–2024 highlights)

### 5.1 Revised view of septal synthase dynamics: synthesis-driven motion
Single-molecule imaging studies in 2024 support that **septal synthase motion can be driven primarily by peptidoglycan synthesis**, with FtsZ treadmilling playing a partial or initiation-phase role depending on species.

* In *Bacillus subtilis*, HT–PBP2B spends **59.0±0.6%** of time in a processive state, **38.1±0.4%** immobile, and **3.0±0.1%** fast-moving; immobile lifetime **48±3 s**, longer than reported FtsZ monomer lifetime (**8.1 s**) (whitley2024peptidoglycansynthesisdrives pages 1-2). This supports a model where a **multimeric** divisome synthesis complex follows an sPG-driven track (whitley2024peptidoglycansynthesisdrives pages 1-2).

* In *Staphylococcus aureus*, the septal synthase complex **FtsW/PBP1** and its putative activator **DivIB** “move with similar velocity,” and “PG synthesis inhibition decelerated or stopped directional movement… and septum constriction,” implying constriction is driven by the processive synthase complex rather than by FtsZ treadmilling (schaper2024cellconstrictionrequires pages 1-2).

### 5.2 Synthase–hydrolase coupling as a druggable vulnerability
A 2023 Nature Communications study shows that **chemical inhibition can be more disruptive than genetic absence** because it perturbs coordination, not just capacity (zhang2023coordinatedpeptidoglycansynthases pages 1-2). Specifically, moenomycin inhibition of aPBPs can collapse rod shape and is mechanistically linked to hydrolase behavior via PBP1a2 and DacB (zhang2023coordinatedpeptidoglycansynthases pages 1-2, zhang2023coordinatedpeptidoglycansynthases media 8bf57c47).

### 5.3 Outer-membrane patterning emerges as a morphogenetic control layer
The Por39/Por41–PapS system demonstrates a mechanistically distinct morphogenetic module in Gram-negative bacteria where **outer-membrane protein patterning constrains the intracellular elongation machinery**, biasing growth and setting curvature (pohl2024anoutermembrane pages 1-2).

### 5.4 Metal ion dependence of elongasome enzymes
A conserved Zn-binding site in *A. baumannii* PBP2 is required for protein stability; exposure to carbapenems or Zn-deprived conditions leads to rod-to-sphere transition resembling RodA–PBP2 deficiency, and mutations in the Zn site cause loss of rod shape and increased β-lactam susceptibility (micelli2023aconservedzincbinding pages 1-2).

---

## 6) Current applications and real-world implementations

### 6.1 Antibiotic discovery and mechanism-of-action (MOA) phenotyping
Morphological outcomes (rod collapse, bulging, cell swelling, constriction arrest) are widely used as MOA signatures.

* In *S. aureus*, antibiotics targeting peptidoglycan synthesis arrest division “within minutes,” with glycopeptides (vancomycin, telavancin) completely inhibiting septum constriction and β-lactam oxacillin preventing recruitment of PBP2 to the septum (puls2023inhibitionofpeptidoglycan pages 1-2).

* Zhang et al. show that inhibiting aPBPs with moenomycin can cause rapid rod-shape collapse through dysregulated hydrolase activity (zhang2023coordinatedpeptidoglycansynthases pages 1-2, zhang2023coordinatedpeptidoglycansynthases media 8bf57c47).

### 6.2 Morphology engineering for sustainable bioprocessing (PHAs)
A 2024 review compiles multiple examples where engineering shape/size improves intracellular biopolymer accumulation and downstream recovery (kalia2024manipulatingmicrobialcell pages 1-2). Quantitative examples include:

* **PHA granules up to 10 µm** in *Halomonas bluephagenesis* TDH4-minCD-ΔphaP1; **4HB mol% increased by 14%** relative to WT (kalia2024manipulatingmicrobialcell pages 7-8).
* **PHB accumulation 100% increase** associated with sulA-linked filamentation strategies (kalia2024manipulatingmicrobialcell pages 7-8).
* Copolymer increases: P(3HB-co-4HB) about **10% higher**, reaching **~78% of cell dry weight**; PHB production increased **from 5.72 g/L to ~9.29 g/L** with reported yield **~73.53%** in a combined strategy (kalia2024manipulatingmicrobialcell pages 7-8).

These represent directly deployable “shape as a process lever” implementations.

### 6.3 High-resolution and single-molecule implementation details (for reproducible phenotyping)
A 2023 study on *Rhodobacter sphaeroides* provides concrete experimental conditions for perturbing elongation/division and imaging envelope phenotypes (e.g., A22 at 10 µg/mL; mecillinam 0.5 µg/mL; cryo-ET dose/tilt parameters) (lakey2023theroleof pages 2-4), illustrating how cell-shape mechanistic studies are operationalized.

---

## 7) Expert opinion and synthesis from authoritative sources

* **Membrane–wall feedback as a unifying control layer:** A 2023 Journal of Bacteriology minireview argues that membrane compartments/lipids are functionally intertwined with peptidoglycan biogenesis; MreB both organizes membrane fluidity domains and is sensitive to membrane fluidity and lipid order, creating feedback that shapes wall synthesis and thus cell shape (garciaheredia2023plasmamembranecellwall pages 6-7).

* **Diversity and evolution of shape regulation across domains:** A 2024 Nature Communications paper frames bacterial shape control largely through peptidoglycan modulation (MreB, crescentin, curvature-promoting modules) but highlights that archaeal shape transitions are environmentally regulated and genetically controlled, identifying new factors (RdfA/DdfA/volactin) (schiller2024identificationofstructural pages 1-2).

---

## 8) Ontology grounding suggestions (CURIEs)

### 8.1 Trait
* **METPO:** METPO:1000666 (cell shape)

### 8.2 Processes (GO; suggest exact terms during curation)
Candidate GO concepts to map nodes/edges (labels provided; curator should select exact GO IDs):
* peptidoglycan biosynthetic process
* cell wall biogenesis
* bacterial-type cell division
* septum formation
* cytoskeleton organization (bacterial actin/tubulin analogs)
* regulation of membrane organization / membrane fluidity

### 8.3 Chemicals/ions (CHEBI; suggest exact terms during curation)
* Zn2+ (CHEBI:29105)
* Mg2+ (CHEBI:18420)
* ATP (CHEBI:15422)
* GTP (CHEBI:15996)
* moenomycin (CHEBI identifier exists; map during curation)
* vancomycin (CHEBI identifier exists)
* oxacillin (CHEBI identifier exists)
* A22 (small-molecule MreB inhibitor; CHEBI identifier may exist; if not, use label node)

### 8.4 Environments (ENVO)
* osmoprotective/isotonic medium (ENVO term likely exists; choose exact)

### 8.5 Taxa (NCBITaxon; examples)
* *Escherichia coli* (NCBITaxon:562)
* *Bacillus subtilis* (NCBITaxon:1423)
* *Staphylococcus aureus* (NCBITaxon:1280)
* *Myxococcus xanthus* (NCBITaxon:34)
* *Acinetobacter baumannii* (NCBITaxon:470)
* *Rhodospirillum rubrum* (NCBITaxon:1085)
* *Haloferax volcanii* (NCBITaxon:2246)

### 8.6 Proteins (UniProt)
Protein identifiers are **organism-specific**; the evidence snippets here did not provide accessions. For YAML curation, use gene symbols plus NCBITaxon and add UniProt IDs in a second pass.

---

## 9) Warnings / claims to treat as uncertain or context-specific

1. **Mg2+ “rescue via hydrolase inhibition”** appears in thesis/review-derived evidence in this corpus and should be verified in a primary research article before hard-curation as a general edge (middlemiss2023moleculartugofwarregulates pages 114-118).
2. **Curvature modules (Por39/Por41–PapS)** are strongly supported but likely **taxon-specific**; curate with NCBITaxon constraint and avoid generalizing to all Gram-negative bacteria (pohl2024anoutermembrane pages 1-2).
3. **Archaeal determinants (RdfA/DdfA/volactin)** are outside bacterial peptidoglycan-based mechanisms; include only if TraitMech’s scope is cross-domain microbial morphology (schiller2024identificationofstructural pages 1-2).
4. **L-form shape control by FtsZ** is a boundary case; curate as conditional on wall-less state and appropriate positioning systems (Min / nucleoid occlusion) rather than as a general rod-shape mechanism (hayashi2024septalwallsynthesis pages 1-2).

---

## 10) DOI-first bibliography (with dates and URLs)

**2024 (priority recent):**
1. Schäper S. et al. *Nature Microbiology* (Published online 13 Mar 2024). “Cell constriction requires processive septal peptidoglycan synthase movement independent of FtsZ treadmilling in Staphylococcus aureus.” DOI:10.1038/s41564-024-01629-6. https://doi.org/10.1038/s41564-024-01629-6 (schaper2024cellconstrictionrequires pages 1-2)
2. Whitley K.D. et al. *Nature Microbiology* (Published online 13 Mar 2024). “Peptidoglycan synthesis drives a single population of septal cell wall synthases during division in Bacillus subtilis.” DOI:10.1038/s41564-024-01650-9. https://doi.org/10.1038/s41564-024-01650-9 (whitley2024peptidoglycansynthesisdrives pages 1-2)
3. Pöhl S. et al. *Nature Communications* (Accepted 14 Aug 2024). “An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in Rhodospirillum rubrum.” DOI:10.1038/s41467-024-51790-z. https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2)
4. Schiller H. et al. *Nature Communications* (Accepted 16 Jan 2024). “Identification of structural and regulatory cell-shape determinants in Haloferax volcanii.” DOI:10.1038/s41467-024-45196-0. https://doi.org/10.1038/s41467-024-45196-0 (schiller2024identificationofstructural pages 1-2)
5. Hayashi M. et al. *Communications Biology* (Nov 2024). “Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in Escherichia coli L-forms.” DOI:10.1038/s42003-024-07279-y. https://doi.org/10.1038/s42003-024-07279-y (hayashi2024septalwallsynthesis pages 1-2)
6. Costa S.F. et al. *mBio* (Mar 2024). “The role of GpsB in Staphylococcus aureus cell morphogenesis.” DOI:10.1128/mbio.03235-23. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)
7. Kalia V.C. et al. *Polymers* (Feb 2024). “Manipulating Microbial Cell Morphology for the Sustainable Production of Biopolymers.” DOI:10.3390/polym16030410. https://doi.org/10.3390/polym16030410 (kalia2024manipulatingmicrobialcell pages 1-2, kalia2024manipulatingmicrobialcell pages 7-8)

**2023:**
8. Zhang H. et al. *Nature Communications* (Sep 2023). “Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall.” DOI:10.1038/s41467-023-41082-3. https://doi.org/10.1038/s41467-023-41082-3 (zhang2023coordinatedpeptidoglycansynthases pages 1-2, zhang2023coordinatedpeptidoglycansynthases media 8bf57c47, zhang2023coordinatedpeptidoglycansynthases media e87c1d22)
9. García-Heredia A. *Journal of Bacteriology* (Mar 2023). “Plasma Membrane-Cell Wall Feedback in Bacteria.” DOI:10.1128/jb.00433-22. https://doi.org/10.1128/jb.00433-22 (garciaheredia2023plasmamembranecellwall pages 6-7)
10. Ago R. et al. *MicrobiologyOpen* (Oct 2023). “Relationship between the Rod complex and peptidoglycan structure in Escherichia coli.” DOI:10.1002/mbo3.1385. https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3, ago2023relationshipbetweenthe pages 18-19)
11. Puls J.-S. et al. *Science Advances* (Mar 2023). “Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division.” DOI:10.1126/sciadv.ade9023. https://doi.org/10.1126/sciadv.ade9023 (puls2023inhibitionofpeptidoglycan pages 1-2)
12. Micelli C. et al. *PNAS* (Published 14 Feb 2023). “A conserved zinc-binding site in Acinetobacter baumannii PBP2 required for elongasome-directed bacterial cell shape.” DOI:10.1073/pnas.2215237120. https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2)
13. Galinier A. et al. *Biomolecules* (Apr 2023). “Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria.” DOI:10.3390/biom13050720. https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 13-14)
14. Kawai Y. et al. *Nature Communications* (Jul 2023). “On the mechanisms of lysis triggered by perturbations of bacterial cell wall biosynthesis.” DOI:10.1038/s41467-023-39723-8. https://doi.org/10.1038/s41467-023-39723-8 (kawai2023onthemechanisms pages 1-2)

---

## 11) Curation-ready next steps for `data/traits/morphology/cell_shape.yaml`

1. **Keep a “core conserved” subgraph** centered on: peptidoglycan → cell shape; Rod system (MreB–RodZ–RodA–PBP2; MreC/MreD modulators); divisome (FtsZ → recruitment/organization; sPG synthesis → constriction). (ago2023relationshipbetweenthe pages 1-3, micelli2023aconservedzincbinding pages 1-2, schaper2024cellconstrictionrequires pages 1-2, whitley2024peptidoglycansynthesisdrives pages 1-2)
2. **Add conditional branches** for:
   * Antibiotic perturbation phenotypes (moenomycin/aPBP inhibition; glycopeptides/β-lactams) (zhang2023coordinatedpeptidoglycansynthases pages 1-2, puls2023inhibitionofpeptidoglycan pages 1-2)
   * Wall-less/L-form boundary case (FtsZ-driven ovalization) (hayashi2024septalwallsynthesis pages 1-2)
3. **Constrain taxon-specific mechanisms** (Por39/Por41–PapS curvature; archaeal RdfA/DdfA/volactin) with NCBITaxon edges or separate subgraphs. (pohl2024anoutermembrane pages 1-2, schiller2024identificationofstructural pages 1-2)
4. **Add quantitative annotations** (optional fields) where available (e.g., PBP2B state occupancy percentages; production yields) to support later benchmarking/validation. (whitley2024peptidoglycansynthesisdrives pages 1-2, kalia2024manipulatingmicrobialcell pages 7-8)


References

1. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

2. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

3. (hayashi2024septalwallsynthesis pages 1-2): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

4. (zhang2023coordinatedpeptidoglycansynthases pages 1-2): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

5. (schaper2024cellconstrictionrequires pages 1-2): Simon Schäper, António D. Brito, Bruno M. Saraiva, Georgia R. Squyres, Matthew J. Holmes, Ethan C. Garner, Zach Hensel, Ricardo Henriques, and Mariana G. Pinho. Cell constriction requires processive septal peptidoglycan synthase movement independent of ftsz treadmilling in staphylococcus aureus. Nature Microbiology, 9:1049-1063, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01629-6, doi:10.1038/s41564-024-01629-6. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (whitley2024peptidoglycansynthesisdrives pages 1-2): Kevin D. Whitley, James Grimshaw, David M. Roberts, Eleni Karinou, Phillip J. Stansfeld, and Séamus Holden. Peptidoglycan synthesis drives a single population of septal cell wall synthases during division in bacillus subtilis. Nature Microbiology, 9:1064-1074, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01650-9, doi:10.1038/s41564-024-01650-9. This article has 24 citations and is from a highest quality peer-reviewed journal.

7. (lakey2023theroleof pages 2-4): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

8. (garciaheredia2023plasmamembranecellwall pages 6-7): Alam García-Heredia. Plasma membrane-cell wall feedback in bacteria. Journal of Bacteriology, Mar 2023. URL: https://doi.org/10.1128/jb.00433-22, doi:10.1128/jb.00433-22. This article has 22 citations and is from a peer-reviewed journal.

9. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (ago2023relationshipbetweenthe pages 18-19): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

11. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

12. (puls2023inhibitionofpeptidoglycan pages 1-2): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 31 citations and is from a highest quality peer-reviewed journal.

13. (middlemiss2023moleculartugofwarregulates pages 114-118): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

14. (mao2023ontherole pages 22-23): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (kawai2023onthemechanisms pages 1-2): Yoshikazu Kawai, Maki Kawai, Eilidh Mackenzie, Bernhard Kepplinger, Kevin Waldron, and Jeff Errington. On the mechanisms of lysis triggered by perturbations of bacterial cell wall biosynthesis. Nature Communications, Jul 2023. URL: https://doi.org/10.1038/s41467-023-39723-8, doi:10.1038/s41467-023-39723-8. This article has 52 citations and is from a highest quality peer-reviewed journal.

16. (battaje2023modelsversuspathogens pages 3-4): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

17. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

18. (middlemiss2023moleculartugofwarregulates pages 111-114): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

19. (zhang2023coordinatedpeptidoglycansynthases media 8bf57c47): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

20. (zhang2023coordinatedpeptidoglycansynthases media e87c1d22): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

21. (kalia2024manipulatingmicrobialcell pages 1-2): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

22. (kalia2024manipulatingmicrobialcell pages 7-8): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

23. (galinier2023recentadvancesin pages 13-14): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.