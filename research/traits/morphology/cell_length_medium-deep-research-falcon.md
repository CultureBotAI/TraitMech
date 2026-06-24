---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:41:00.583405'
end_time: '2026-06-18T06:56:26.937825'
duration_seconds: 926.35
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length medium
  trait_identifier: METPO:1000885
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length_medium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-length phenotype in which the longer cell dimension lies approximately
    between 2 and 3 micrometers.
  parent_traits: METPO:1000881
  synonyms: L_2_3
  evidence_summary: 'DOI:10.1126/science.aaa1313: cell size scales with growth rate
    (Growth-rate-dependent size law supports medium cell length as a typical outcome
    at moderate growth rates.)'
  causal_graph_summary: 'cell_length_medium_growth_rate: 4 nodes, 3 edges'
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
- **Trait label:** cell length medium
- **METPO identifier:** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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
- **Trait label:** cell length medium
- **METPO identifier:** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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


# Research Report: Microbial Trait “cell length medium” (METPO:1000885)

## Scope summary (TraitMech curation focus)
**Trait definition (given):** *A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.* (METPO:1000885)

### What the trait represents
This trait is best interpreted as an **assay-observed morphological state** of bacterial cells (typically rods or mildly elongated forms) in which measured cell length clusters in the ~2–3 µm range. Mechanistically, this “medium length” state can be viewed as an outcome of **balanced elongation (sidewall peptidoglycan insertion) and division (septation)**.

### Boundary cases and distinctions
* **Shorter than 2 µm:** smaller rods/coccobacilli; can result from nutrient limitation or altered size-control strategies (not directly evidenced in retrieved texts).
* **Longer than 3 µm:** elongated/filamentous cells, often due to **division failure** while elongation continues (e.g., regulatory disruption of envelope constriction or divisome function) (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18).
* **Spherical/ovoid:** “cell length” becomes less meaningful; these states can arise when elongation machinery is compromised (e.g., PBP2 loss in *Salmonella* causes giant spherical cells at neutral pH) (castanheira2023evidenceoftwo pages 1-2).

## Key concepts and definitions (current understanding)
### 1) Elongasome / Rod complex (rod-shaped growth)
Rod-shaped bacteria elongate mainly through the **Rod complex (elongasome)**, which coordinates cytoskeletal scaffolding with peptidoglycan (PG) synthesis. In *E. coli*, key components include **MreB, MreC, MreD, RodZ, RodA, and PBP2**; RodA provides glycosyltransferase activity and PBP2 provides transpeptidase activity required for elongation (ago2023relationshipbetweenthe pages 1-3). RodZ functions as an interaction hub connecting several of these elements (ago2023relationshipbetweenthe pages 1-3).

### 2) Divisome and septation
Division depends on a multi-protein complex (divisome) with central roles for **FtsZ** and associated factors. When division fails but elongation continues, cells can become filamentous (lakey2023theroleof pages 16-18).

### 3) Cell-envelope coordination modules (Tol-Pal, Pal) and regulation
In Gram-negative bacteria, envelope remodeling during constriction requires coordination between inner membrane, PG, and outer membrane. In *Rhodobacter sphaeroides*, the **CenKR two-component system (TCS)** regulates envelope/division genes (including Tol-Pal-related components) and, when overactivated, causes filamentation and chaining consistent with failed constriction coordination (lakey2023theroleof pages 1-2, lakey2023theroleof pages 2-4).

### 4) Membrane fluidity, fatty acids, and stringent response (ppGpp)
Membrane lipid composition (saturated vs unsaturated fatty acids) influences membrane physical properties and can create division stress. In *E. coli*, **(p)ppGpp** is required to buffer cell division when membrane fluidity decreases (e.g., reduced unsaturated fatty acids), preventing filamentation/lysis; divisome gene overexpression (ftsQAZ) can rescue defects (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17).

## Recent developments and latest research (prioritize 2023–2024)
### A) 2023: Rod complex integrity links to PG architecture in *E. coli*
Ago et al. (2023) connect Rod-complex perturbation (RodZ chimera) to abnormal morphology and altered PG structure (“holes” and muropeptide composition changes), supporting the idea that elongation machinery integrity affects wall density/strength, which underpins stable rod morphology (ago2023relationshipbetweenthe pages 1-3).

### B) 2023: Environment-conditional elongation systems in *Salmonella*
Castanheira & García-del Portillo (2023) provide evidence for **two elongasomes** in *Salmonella enterica*: one directed by canonical **PBP2** under neutral pH and an alternative directed by **PBP2SAL** under acidic conditions, with distinct assembly/activity properties. Loss of *mrdA* (PBP2) yields giant spherical cells and major viability loss in neutral conditions, but PBP2 is dispensable in acidic media where the alternative system maintains rod morphology (castanheira2023evidenceoftwo pages 1-2).

### C) 2023: Regulatory control of elongation/division coupling via CenKR in α-proteobacteria
Lakey et al. (2023) demonstrate that increased CenKR activity drives filamentation/chaining and propose a mechanistic model in which elevated CenKR decreases Pal mobility, delaying outer membrane constriction and disrupting the proper spatial organization of MreB and FtsZ, perturbing PG synthesis/remodeling (lakey2023theroleof pages 1-2). Quantitatively, CenKR overactivity is associated with increased densities of mislocalized cytoskeletal foci: **MreB foci density 1.04 ± 0.36 foci/µm vs 0.65 ± 0.35**, and **FtsZ foci density 0.8 ± 0.15 foci/µm vs 0.6 ± 0.3** (lakey2023theroleof pages 16-18). Figure evidence shows filamentation upon cenK induction and altered MreB/FtsZ localization patterns (lakey2023theroleof media 33ed0e40, lakey2023theroleof media edf1e84c).

### D) 2024: ppGpp buffers division under low membrane fluidity (E. coli)
Singh & Harinarayanan (2024) show that when membrane unsaturated fatty-acid (UFA) content drops (e.g., ΔfadR background), cell division becomes dependent on (p)ppGpp; ppGpp-deficient strains filament and lyse under reduced fluidity. The work includes quantitative membrane composition: UFAs **56% (WT) → 37% (ΔfadR) → 32% (ppGpp-depleted ΔfadR)** correlated with division disruption and lysis, and shows rescue by expressing **ftsQAZ** and by supplementing **UFAs (16:1/18:1)** or increasing temperature (42°C) (singh2024(p)ppgppbufferscell pages 14-17).

### E) 2024: Morphogenesis determinants in ovococci (S. aureus)
Costa et al. (2024) highlight that *S. aureus* (classically considered spherical) undergoes measurable pre-division elongation, driven by **RodA/PBP3** and modulated by additional factors including **GpsB** and **RodZ**. GpsB affects septal localization of PBP2/PBP4; its loss increases peripheral PG insertion/crosslinking and yields more spherical cells (costa2024theroleof pages 1-2).

## Current applications and real-world implementations
### 1) Pathogenesis and niche adaptation via shape maintenance
*Salmonella*’s alternative elongasome under acidic conditions provides a concrete mechanism for maintaining rod-like morphology across environments relevant to infection biology (acidic intracellular/vacuolar conditions) (castanheira2023evidenceoftwo pages 1-2).

### 2) Antibiotic/chemical perturbations as tools to manipulate length and reveal mechanisms
Studies use **A22 (MreB inhibitor)** and **amdinocillin/mecillinam (PBP2-targeting)** to perturb elongation/division coordination in *R. sphaeroides* (lakey2023theroleof pages 2-4). In *E. coli*, membrane-composition perturbations (e.g., palmitic acid 16:0, cerulenin, temperature shifts) reveal ppGpp-dependent division robustness pathways (singh2024(p)ppgppbufferscell pages 14-17).

### 3) Biotechnology and envelope-balance engineering
In *Bacillus subtilis*, decreasing fatty-acid synthesis (genetically via **fapR*** or chemically via **cerulenin**) can rescue growth when PG synthesis capacity is limited, emphasizing that envelope synthesis balance can be engineered to tune physiology and (indirectly) morphology/size (willdigg2023adecreasein pages 1-3).

## Expert opinions / authoritative interpretations (from the sources)
* Lakey et al. present an explicit **model** for how elevated CenKR activity leads to filamentation via envelope constriction defects and mispositioning of MreB/FtsZ, i.e., a regulatory-to-structure causal chain (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18).
* Ago et al. interpret Rod complex function as determining not only gross PG shape but also **PG density** supporting mechanical strength, connecting molecular complex integrity to physical wall properties (ago2023relationshipbetweenthe pages 1-3).
* Singh & Harinarayanan interpret their rescue experiments (ftsQAZ, UFA supplementation, temperature) as evidence that ppGpp is required to maintain **divisome function when membrane fluidity decreases**, conceptually linking lipid homeostasis to cell division robustness (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17).

## Relevant statistics and data (recent studies)
* **CenKR overactivity in *R. sphaeroides***: MreB foci density **1.04 ± 0.36 foci/µm** vs **0.65 ± 0.35**; FtsZ foci density **0.8 ± 0.15 foci/µm** vs **0.6 ± 0.3** (lakey2023theroleof pages 16-18). Filamentation and redistributed localization are visible in key figures (lakey2023theroleof media 33ed0e40, lakey2023theroleof media edf1e84c).
* **Membrane UFA% vs division defect in *E. coli***: UFA fraction **56% (WT)**, **37% (ΔfadR)**, **32% (ppGpp-depleted ΔfadR)**; lower UFA% correlates with division disruption/lysis, and is rescued by ftsQAZ overexpression and UFA supplementation (singh2024(p)ppgppbufferscell pages 14-17).

## Candidate nodes (grouped by type; ontology grounding suggestions)
### Phenotype node
* **cell length medium** — METPO:1000885 (given)
  *Synonym:* L_2_3

### Cellular processes / complexes
* **Peptidoglycan biosynthesis / cell wall organization** — GO:0009252; GO:0071555 (suggested)
* **Elongasome / Rod complex** — label-only candidate (complex)
* **Divisome / septation** — GO:0000917 (division septum assembly; suggested)
* **Tol-Pal system / Pal dynamics** — label-only candidate (complex and process)

### Genes/proteins (examples; often taxon-specific identifiers)
* **MreB** (actin homolog) — UniProt placeholder; GO-linked cytoskeletal scaffold for elongation (ago2023relationshipbetweenthe pages 1-3, lakey2023theroleof pages 16-18)
* **RodZ** — interaction hub in Rod complex (ago2023relationshipbetweenthe pages 1-3)
* **MreC, MreD** — Rod complex components modulating PBP2 activity (ago2023relationshipbetweenthe pages 1-3)
* **RodA (SEDS family)** — glycosyltransferase in elongation machinery (ago2023relationshipbetweenthe pages 1-3, costa2024theroleof pages 1-2)
* **PBP2 / MrdA** — elongation transpeptidase; essential for rod morphology in neutral pH in *Salmonella* (ago2023relationshipbetweenthe pages 1-3, castanheira2023evidenceoftwo pages 1-2)
* **PBP2SAL** — pathogen-specific alternative bPBP in *Salmonella* acidic conditions (label-only candidate) (castanheira2023evidenceoftwo pages 1-2)
* **FtsZ** — division ring protein; mislocalized in filamentation state (lakey2023theroleof pages 16-18)
* **ftsQAZ operon** — division genes; rescue of filamentation under low fluidity (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17)
* **CenK/CenR (CenKR TCS)** — regulator of envelope/division genes; filamentation on overexpression (lakey2023theroleof pages 1-2)
* **Pal** — OM-associated protein implicated in OM constriction and septation coordination (lakey2023theroleof pages 1-2)
* **RelA/SpoT** — ppGpp synthesis/hydrolysis (label-only candidates in evidence) (singh2024(p)ppgppbufferscell pages 1-4)
* **FadR; fabA; fabB** — lipid homeostasis regulators/enzymes relevant to membrane fluidity (singh2024(p)ppgppbufferscell pages 14-17, singh2024(p)ppgppbufferscell pages 4-8)
* **GpsB; PBP2/PBP4; PBP3** (Gram-positive morphogenesis context) — *S. aureus* elongation/shape determinants (costa2024theroleof pages 1-2)

### Environmental / experimental factors (ENVO label-only where needed)
* **pH (neutral vs acidic)** — controls *Salmonella* elongasome choice (castanheira2023evidenceoftwo pages 1-2)
* **Temperature (25°C–42°C)** — modulates membrane fluidity and ppGpp requirement (singh2024(p)ppgppbufferscell pages 14-17)
* **Nutrient/condition shifts** — implied via stringent response and host-like conditions (castanheira2023evidenceoftwo pages 1-2, singh2024(p)ppgppbufferscell pages 1-4)

### Chemicals / inhibitors (CHEBI suggestions)
* **(p)ppGpp** — CHEBI:72316 / CHEBI:63529 (suggested) (singh2024(p)ppgppbufferscell pages 1-4)
* **Cerulenin** — CHEBI:34445 (suggested) (willdigg2023adecreasein pages 1-3, singh2024(p)ppgppbufferscell pages 14-17)
* **Palmitic acid (16:0)** — CHEBI:15756 (suggested) (singh2024(p)ppgppbufferscell pages 11-14)
* **Palmitoleic acid (16:1)** — CHEBI:28837 (suggested) (singh2024(p)ppgppbufferscell pages 8-11)
* **Oleic acid (18:1)** — CHEBI:36021 (suggested) (singh2024(p)ppgppbufferscell pages 11-14)
* **A22 (MreB inhibitor)** — label-only candidate; used at sub-MIC 10 µg/mL in *R. sphaeroides* experiments (lakey2023theroleof pages 2-4)
* **Amdinocillin/mecillinam (PBP2-targeting)** — label-only candidate; used at 0.5 µg/mL (lakey2023theroleof pages 2-4)

## Candidate causal edges (evidence-backed)
The table below is intended for direct TraitMech curation review.

| Edge (triple) | Evidence summary | Supporting snippet (short quote) | Source (DOI, year, URL) | Curation notes (strength/uncertainty, taxa/assay specificity) | Suggested ontology grounding |
|---|---|---|---|---|---|
| CenKR activity → negatively regulates → Pal mobility | In *Rhodobacter sphaeroides*, elevated CenKR activity is proposed to reduce Pal mobility via altered Tol-Pal system behavior, initiating downstream division defects and filamentation (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18). | "increased CenKR activity decreases the mobility of Pal" | doi:10.1128/mbio.00631-23 (2023), https://doi.org/10.1128/mbio.00631-23 | Strong within *R. sphaeroides* model; mechanistic model combines direct observations and inferred Tol-Pal behavior. Curate as taxon-specific unless generalized carefully. | CenKR: label-only candidate (TCS); Pal: UniProtKB:P0A912 (generic Pal family placeholder); GO:0009279 cell outer membrane; GO:0007049 cell cycle |
| decreased Pal mobility → delays → outer membrane constriction | The same study links lower Pal mobility to delayed outer membrane constriction during septation, producing chained/filamentous morphologies (lakey2023theroleof pages 1-2). | "delaying OM constriction" | doi:10.1128/mbio.00631-23 (2023), https://doi.org/10.1128/mbio.00631-23 | Moderate-to-strong; direct study organism evidence, but causality is partly model-based. Taxon-specific to Alphaproteobacteria context. | Pal: UniProtKB placeholder; GO:0043198 dendritic cell?; GO:0000917 division septum assembly; GO:0009279 cell outer membrane |
| delayed outer membrane constriction → disrupts localization of → MreB | In CenKR-overexpressing filaments, MreB foci redistribute along the filament length rather than normal positions; density rises to 1.04 ± 0.36 foci/µm vs 0.65 ± 0.35 in basal cells (lakey2023theroleof pages 16-18, lakey2023theroleof media 33ed0e40). | "mCherry-MreB fluorescence becomes dispersed at numerous locations along the length of the cell filament" | doi:10.1128/mbio.00631-23 (2023), https://doi.org/10.1128/mbio.00631-23 | Strong phenotype evidence; exact causal direction from OM constriction to MreB mislocalization is model-supported rather than directly isolated. | MreB: UniProtKB:P0A9X4 (placeholder); GO:0051301 cell division; GO:0071555 cell wall organization |
| delayed outer membrane constriction → disrupts localization of → FtsZ | CenKR elevation causes multiple FtsZ rings along filaments, with 0.8 ± 0.15 foci/µm vs 0.6 ± 0.3 under basal activity, consistent with failed septal progression (lakey2023theroleof pages 16-18, lakey2023theroleof media 33ed0e40). | "FtsZ localization changes ... to multiple rings along the filament" | doi:10.1128/mbio.00631-23 (2023), https://doi.org/10.1128/mbio.00631-23 | Strong phenotype evidence in *R. sphaeroides*; causal order partly inferred. | FtsZ: UniProtKB:P0A9A6 (placeholder); GO:0000921 septin ring organization? label-only for bacterial Z-ring; GO:0000917 division septum assembly |
| MreB/FtsZ mislocalization → causes → filamentation | The CenKR study explicitly links altered localization of elongation/division machinery to filamentation and chaining (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18). | "interfering with the spatial regulation of PG synthesis and remodeling" | doi:10.1128/mbio.00631-23 (2023), https://doi.org/10.1128/mbio.00631-23 | Strong in study organism; good candidate edge for abnormal-long phenotype, but inverse relation to "medium length" is indirect. | GO:0007049 cell cycle; GO:0000917 division septum assembly; METPO:1000885 as target phenotype context |
| RodZ → physically/genetically interacts with → MreB/MreC/MreD/PBP2/RodA | In *E. coli*, RodZ is central to Rod-complex integrity and connects multiple elongation components that govern sidewall synthesis (ago2023relationshipbetweenthe pages 1-3). | "RodZ interacts physically and genetically with MreB, MreC, MreD, PBP2 and RodA" | doi:10.1002/mbo3.1385 (2023), https://doi.org/10.1002/mbo3.1385 | Strong for *E. coli* Rod complex; interaction edge is well supported, but effect on exact 2–3 µm class is indirect. | RodZ: UniProtKB:P0AGA2 (placeholder); MreB: UniProtKB:P0A9X4; MreC: UniProtKB:P0ACF4; MreD: UniProtKB:P0A9Y6; RodA: UniProtKB:P0ABG4; PBP2/MrdA: UniProtKB:P0AD65 |
| MreC/MreD balance → modulates → PBP2 activity | The Rod-complex paper states that the balance between MreC and MreD modulates PBP2, an essential elongation transpeptidase (ago2023relationshipbetweenthe pages 1-3). | "the balance between MreC and MreD modulates PBP2 activity" | doi:10.1002/mbo3.1385 (2023), https://doi.org/10.1002/mbo3.1385 | Moderate-to-strong in *E. coli*; useful mechanistic edge for elongation control. | MreC: UniProtKB:P0ACF4; MreD: UniProtKB:P0A9Y6; PBP2/MrdA: UniProtKB:P0AD65; GO:0009252 peptidoglycan biosynthetic process |
| RodA-PBP2 elongasome → enables → peptidoglycan insertion during elongation | RodA is the glycosyltransferase and PBP2 the transpeptidase required for cell elongation; Rod-complex rotation supports even PG insertion along the cylinder (ago2023relationshipbetweenthe pages 1-3, jain2023understandingelongasomeunit pages 2-4). | "RodA is a glycosyltransferase and PBP2 is a transpeptidase required for cell elongation" | doi:10.1002/mbo3.1385 (2023), https://doi.org/10.1002/mbo3.1385 | Strong general rod-bacterium mechanism; broadly curatable. | RodA: UniProtKB:P0ABG4; PBP2/MrdA: UniProtKB:P0AD65; GO:0009252 peptidoglycan biosynthetic process; GO:0071555 cell wall organization |
| intact Rod complex → increases → peptidoglycan density/mechanical strength | RodZ mutant (RMR) cells had PG with "many large holes" and altered muropeptides, indicating Rod-complex integrity determines dense PG supportive of normal rod morphology (ago2023relationshipbetweenthe pages 1-3). | "The Rod complex may be a determinant not only for the whole shape of peptidoglycan but also for its highly dense structure" | doi:10.1002/mbo3.1385 (2023), https://doi.org/10.1002/mbo3.1385 | Moderate-to-strong; morphological consequence direct, density-to-length class indirect. | GO:0009273 peptidoglycan-based cell wall; GO:0071555 cell wall organization |
| intact Rod complex / dense PG → maintains → rod shape | The Rod-complex study places PG elongation machinery as determinant of whole-cell shape in *E. coli* (ago2023relationshipbetweenthe pages 1-3). | "PG determines bacterial cell shape" | doi:10.1002/mbo3.1385 (2023), https://doi.org/10.1002/mbo3.1385 | Strong but broad; maps to parent rod-shape mechanism rather than specifically medium length. | GO:0009273 peptidoglycan-based cell wall; METPO:1000885 context node |
| neutral pH → activates/permits → PBP2-directed elongasome | *Salmonella* uses a canonical PBP2 elongasome in neutral conditions (castanheira2023evidenceoftwo pages 1-2). | "The PBP2-elongasome responds to neutral pH" | doi:10.1038/s42003-023-05308-w (2023), https://doi.org/10.1038/s42003-023-05308-w | Strong for *Salmonella enterica*; environment-specific and taxon-specific. | ENVO:09200014 neutral pH environment (label-only); PBP2/MrdA: UniProtKB:P0AD65; GO:0009252 |
| acidic pH → activates/permits → PBP2SAL-directed elongasome | In *Salmonella*, an alternative elongasome assembles under acidic conditions, preserving rod morphology when canonical PBP2 is dispensable (castanheira2023evidenceoftwo pages 1-2). | "the PBP2SAL-directed system assembles in acidic conditions" | doi:10.1038/s42003-023-05308-w (2023), https://doi.org/10.1038/s42003-023-05308-w | Strong in pathogen-specific system; should be marked taxon-specific and conditional. | ENVO:09200015 acidic environment (label-only); PBP2SAL: label-only candidate; GO:0009252 |
| PBP2 deletion/inactivation → causes → giant spherical cells at neutral pH | Loss of *mrdA* (PBP2) in *Salmonella* yields giant spherical cells and severe viability loss in neutral media, showing canonical elongasome necessity for elongated morphology (castanheira2023evidenceoftwo pages 1-2). | "Deleting mrdA (PBP2) yields giant spherical Salmonella at neutral pH" | doi:10.1038/s42003-023-05308-w (2023), https://doi.org/10.1038/s42003-023-05308-w | Strong phenotype evidence; useful negative control edge distinguishing medium-length rods from spherical forms. | PBP2/MrdA: UniProtKB:P0AD65; GO:0009252; METPO parent morphology context |
| (p)ppGpp → buffers → cell division under reduced membrane fluidity | In *E. coli*, low UFA/high SFA conditions make division dependent on (p)ppGpp; deficiency causes filamentation and lysis (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17). | "cell division was dependent on ... (p)ppGpp" | doi:10.1111/mmi.15323 (2024), https://doi.org/10.1111/mmi.15323 | Strong in *E. coli* under specific membrane-stress conditions; not a universal direct size edge. | CHEBI:72316 guanosine tetraphosphate(4-); CHEBI:63529 guanosine pentaphosphate(4-); RelA/SpoT: label-only candidate; GO:0009260 response to starvation |
| decreased UFA content / reduced membrane fluidity → impairs → divisome function | Quantitative lipid data: UFA fraction falls from 56% (WT) to 37% (ΔfadR) and to 32% in (p)ppGpp-depleted ΔfadR, correlating with division defects, filamentation, and lysis (singh2024(p)ppgppbufferscell pages 14-17, singh2024(p)ppgppbufferscell pages 4-8). | "UFAs are 56% in wild type, drop to 37% in ΔfadR ... and further drop to 32%" | doi:10.1111/mmi.15323 (2024), https://doi.org/10.1111/mmi.15323 | Strong quantitative support in *E. coli*; divisome impairment inferred from rescue experiments rather than direct divisome biochemistry. | CHEBI:36083 unsaturated fatty acid; CHEBI:26666 saturated fatty acid; GO:0005886 plasma membrane |
| ftsQAZ overexpression → rescues → filamentation/lysis under low-fluidity stress | Expression of *ftsQ*, *ftsA*, and *ftsZ* rescues the growth defect associated with filamentation in low-fluidity/(p)ppGpp-deficient backgrounds (singh2024(p)ppgppbufferscell pages 11-14, singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17). | "Combined expression of cell division genes ftsQ, ftsA and ftsZ from plasmid rescued the growth defect that was associated with cell filamentation" | doi:10.1111/mmi.15323 (2024), https://doi.org/10.1111/mmi.15323 | Strong rescue evidence; assay-specific plasmid overexpression. Good for mechanistic graph if marked experimental. | FtsQ: UniProtKB:P06136 (placeholder); FtsA: UniProtKB:P0A9A6? label-only placeholder recommended; FtsZ: UniProtKB:P0A9A6 (placeholder); GO:0000917 |
| palmitic acid (16:0) → promotes → filamentation/growth inhibition in (p)ppGpp-deficient cells | Supplemental 16:0 worsens growth of ΔrelA ΔspoT, while 16:1 or 18:1 rescues, linking saturated-fat enrichment to division failure (singh2024(p)ppgppbufferscell pages 11-14, singh2024(p)ppgppbufferscell pages 8-11). | "Palmitic acid (16:0) severely inhibited growth of ΔrelA ΔspoT mutant" | doi:10.1111/mmi.15323 (2024), https://doi.org/10.1111/mmi.15323 | Moderate; phenotype is growth + filamentation context, not direct medium-length measurement. | CHEBI:15756 palmitic acid; CHEBI:28837 palmitoleic acid; CHEBI:36021 oleic acid |
| unsaturated fatty acids (16:1/18:1) → rescue → low-fluidity division defects | Supplementing 16:1 or 18:1 rescues growth defects caused by cerulenin or 16:0 enrichment, consistent with restoration of membrane fluidity (singh2024(p)ppgppbufferscell pages 11-14, singh2024(p)ppgppbufferscell pages 8-11). | "supplementation with unsaturated fatty acids (16:1 or 18:1) rescued growth" | doi:10.1111/mmi.15323 (2024), https://doi.org/10.1111/mmi.15323 | Moderate-to-strong; supports environmental/chemical rescue nodes. | CHEBI:28837 palmitoleic acid; CHEBI:36021 oleic acid; GO:0005886 plasma membrane |
| cerulenin → inhibits → fatty acid synthesis | In *Bacillus subtilis*, cerulenin is used as a FAS inhibitor and restores growth of PG-limited cells, supporting the role of membrane synthesis in shape/growth balance (willdigg2023adecreasein pages 1-3, willdigg2023adecreasein pages 9-12). | "inhibition of FAS by cerulenin also restored growth of PG-limited cells" | doi:10.1128/mbio.00475-23 (2023), https://doi.org/10.1128/mbio.00475-23 | Strong chemical perturbation, but outcome is rescue of PG-limited growth rather than direct medium-length quantification. | CHEBI:34445 cerulenin; GO:0006633 fatty acid biosynthetic process |
| decreased fatty acid synthesis (FapR* / cerulenin / ACC-reducing suppressors) → decreases → membrane synthesis | Genetic suppressors predicted to reduce FAS, especially *fapR* super-repressor, alleviate membrane/PG imbalance (willdigg2023adecreasein pages 9-12, willdigg2023adecreasein pages 1-3). | "fapR* acts as a super-repressor decreasing transcription of FAS genes" | doi:10.1128/mbio.00475-23 (2023), https://doi.org/10.1128/mbio.00475-23 | Strong in *B. subtilis* PG-limited strains; indirect for cell-length class. | FapR: label-only candidate; ACC: EC:6.4.1.2; GO:0006633 fatty acid biosynthetic process |
| decreased membrane synthesis → rescues → PG-limited growth/shape state | The *B. subtilis* study argues that reduced membrane synthesis restores balance when PG synthesis capacity is limited; increased elongasome activity is associated with thinner, elongated cells (willdigg2023adecreasein pages 1-3, willdigg2023adecreasein pages 9-12). | "Balanced synthesis of the peptidoglycan cell wall and the cell membrane is critical" | doi:10.1128/mbio.00475-23 (2023), https://doi.org/10.1128/mbio.00475-23 | Moderate; strong concept but exact shape endpoint varies and quantitative length is absent. Suitable as broader envelope-balance mechanism. | GO:0009252 peptidoglycan biosynthetic process; GO:0006633 fatty acid biosynthetic process; GO:0071555 cell wall organization |
| GpsB → promotes septal localization of → PBP2/PBP4 | In *S. aureus*, GpsB helps localize PBPs at the septum; without it, PBPs shift peripherally and cells become more spherical rather than elongated (costa2024theroleof pages 1-2). | "GpsB promotes correct septal localization of PBP2 and PBP4" | doi:10.1128/mbio.03235-23 (2024), https://doi.org/10.1128/mbio.03235-23 | Strong but in ovococcal context; useful warning edge distinguishing elongation maintenance from rod medium-length phenotype. | GpsB: label-only candidate; PBP2/PBP4: label-only candidates; GO:0000917 |
| RodA/PBP3 elongation machinery → supports → predivision elongation | *S. aureus* elongates slightly before division via RodA/PBP3 despite lacking MreB, showing alternative elongation logic (costa2024theroleof pages 1-2). | "S. aureus ... still elongates via a dedicated SEDS/PBP pair: RodA ... and PBP3" | doi:10.1128/mbio.03235-23 (2024), https://doi.org/10.1128/mbio.03235-23 | Strong for ovococci; probably not directly curatable for a generic rod-cell medium-length trait unless taxon constrained. | RodA: UniProtKB placeholder; PBP3/FtsI: UniProtKB:P0AD68 (placeholder); GO:0009252 |


*Table: This table lists evidence-backed subject–predicate–object edges relevant to the microbial morphology trait 'cell length medium (2–3 µm)'. It emphasizes experimentally supported mechanisms that maintain normal elongation or shift cells toward filamentous or spherical boundary phenotypes, helping prioritize edges for TraitMech curation.*

## Warnings / curation caveats
1. **Direct “2–3 µm length” datasets were not retrieved** in the accessible excerpts; many mechanistic claims are supported via **qualitative morphology** (rod vs filament vs sphere) and proxy measurements (foci density, lipid composition), not direct classification into the 2–3 µm bin.
2. Several edges are **taxon- and condition-specific** (e.g., CenKR in α-proteobacteria; PBP2SAL in *Salmonella*; ovococcal elongation in *S. aureus*) and should be curated with explicit taxa/conditions.
3. The foundational reference mentioned in the prompt (Science 2015, doi:10.1126/science.aaa1313) could not be retrieved by the paper search in this run; therefore, **growth-rate dependent “size law” claims are not directly quoted** here.
4. Some edges are **model-structured causal chains** rather than single-step experimental isolations (e.g., CenKR → Pal mobility → OM constriction → MreB/FtsZ mislocalization) and should be marked as *inferred* where appropriate (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18).

## DOI-first bibliography (with dates and URLs)
1. Lakey BD, et al. **The role of CenKR in the coordination of *Rhodobacter sphaeroides* cell elongation and division.** *mBio* (Jun 2023). DOI: **10.1128/mbio.00631-23**. https://doi.org/10.1128/mbio.00631-23 (lakey2023theroleof pages 1-2, lakey2023theroleof pages 16-18, lakey2023theroleof media 33ed0e40)
2. Ago R, et al. **Relationship between the Rod complex and peptidoglycan structure in *Escherichia coli*.** *MicrobiologyOpen* (Oct 2023). DOI: **10.1002/mbo3.1385**. https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3)
3. Castanheira S, García-del Portillo F. **Evidence of two differentially regulated elongasomes in *Salmonella*.** *Communications Biology* (Sep 2023). DOI: **10.1038/s42003-023-05308-w**. https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2)
4. Singh V, Harinarayanan R. **(p)ppGpp buffers cell division when membrane fluidity decreases in *Escherichia coli*.** *Molecular Microbiology* (Oct 2024). DOI: **10.1111/mmi.15323**. https://doi.org/10.1111/mmi.15323 (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 14-17)
5. Willdigg JR, Patel Y, Helmann JD. **A Decrease in Fatty Acid Synthesis Rescues Cells with Limited Peptidoglycan Synthesis Capacity.** *mBio* (Apr 2023). DOI: **10.1128/mbio.00475-23**. https://doi.org/10.1128/mbio.00475-23 (willdigg2023adecreasein pages 1-3)
6. Costa SF, et al. **The role of GpsB in *Staphylococcus aureus* cell morphogenesis.** *mBio* (Mar 2024). DOI: **10.1128/mbio.03235-23**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)


References

1. (lakey2023theroleof pages 1-2): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

2. (lakey2023theroleof pages 16-18): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

3. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

4. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

5. (lakey2023theroleof pages 2-4): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (singh2024(p)ppgppbufferscell pages 1-4): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

7. (singh2024(p)ppgppbufferscell pages 14-17): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (lakey2023theroleof media 33ed0e40): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

9. (lakey2023theroleof media edf1e84c): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

11. (willdigg2023adecreasein pages 1-3): Jessica R. Willdigg, Yesha Patel, and John D. Helmann. A decrease in fatty acid synthesis rescues cells with limited peptidoglycan synthesis capacity. mBio, Apr 2023. URL: https://doi.org/10.1128/mbio.00475-23, doi:10.1128/mbio.00475-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (singh2024(p)ppgppbufferscell pages 4-8): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (singh2024(p)ppgppbufferscell pages 11-14): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

14. (singh2024(p)ppgppbufferscell pages 8-11): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (jain2023understandingelongasomeunit pages 2-4): Preeti Jain. Understanding elongasome unit of mycobacterium and its comparative analysis with other model organisms. Journal of Cellular Signaling, 4:142-150, Sep 2023. URL: https://doi.org/10.33696/signaling.4.101, doi:10.33696/signaling.4.101. This article has 0 citations.

16. (willdigg2023adecreasein pages 9-12): Jessica R. Willdigg, Yesha Patel, and John D. Helmann. A decrease in fatty acid synthesis rescues cells with limited peptidoglycan synthesis capacity. mBio, Apr 2023. URL: https://doi.org/10.1128/mbio.00475-23, doi:10.1128/mbio.00475-23. This article has 7 citations and is from a domain leading peer-reviewed journal.