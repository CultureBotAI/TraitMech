---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:10:33.492238'
end_time: '2026-06-18T00:20:17.106312'
duration_seconds: 583.61
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid3
  trait_identifier: METPO:1000477
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 4\u20135 pH units, characteristic of organisms with wide pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_4_5
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)'
  causal_graph_summary: 'ph_delta_mid3_wide_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid3
- **METPO identifier:** METPO:1000477
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 4–5 pH units, characteristic of organisms with wide pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_4_5
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)
- **Existing causal graph summary:** ph_delta_mid3_wide_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid3.yaml`.

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
- **Trait label:** pH delta mid3
- **METPO identifier:** METPO:1000477
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 4–5 pH units, characteristic of organisms with wide pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_4_5
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)
- **Existing causal graph summary:** ph_delta_mid3_wide_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid3.yaml`.

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


## Microbial Trait Causal Graph Curation Report: pH delta mid3 (METPO:1000477)

### Scope summary (trait meaning and boundaries)
The trait **pH delta mid3** (synonym **pHd_4_5**) represents a **growth-supporting pH breadth of ~4–5 pH units**, characteristic of microbes that can **grow** (not merely survive) across a wide range of external pH while still maintaining internal physicochemical conditions compatible with metabolism. A useful operational interpretation is that many neutralophiles can **grow across external pH ~5.5–9.0** (≈3.5 pH units) and some extend further depending on physiology/lineage and medium; critically, they keep **cytoplasmic pH in a much narrower band** (e.g., near ~7.5–7.7 in cited examples), implying active homeostatic control. (krulwich2011molecularaspectsof pages 1-3)

Boundary cases to distinguish:
- **Survival-only acid/alkali resistance**: enterics may **survive** gastric acidity without growth; this should not be curated as pH delta breadth unless growth is shown. (krulwich2011molecularaspectsof pages 1-3)
- **Extreme acidophiles/alkaliphiles**: organisms specialized for pH 1–3 or 10–13 growth represent extremophily rather than the mid3 “wide breadth” class, though their mechanisms inform candidate nodes. (krulwich2011molecularaspectsof pages 3-5)
- **Assay-dependent breadth artifacts**: measured breadth depends on **buffering capacity**, weak acids/bases, and readout methods for pHin/ΔpH/Δψ. (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2)

### Key concepts and current understanding (mechanistic framing)
1. **pH homeostasis is a systems property**: cells regulate the **proton motive force (PMF)**, consisting of **Δψ (membrane potential)** and **ΔpH**, to support transport and maintain intracellular pH. PMF can be approximated as **PMF (mV) = Δψ − 59 ΔpH**. (krulwich2011molecularaspectsof pages 1-3)
2. **Homeostatic setpoints are near-neutral** even when external pH varies: neutralophiles can grow across broad external pH while maintaining **cytoplasmic pH near ~7.5–7.7**, and alkaliphiles can maintain elevated but still moderated pHin (example: *Bacillus pseudofirmus* OF4 grows at pH 10.5 with **pHin ~8.3**). (krulwich2011molecularaspectsof pages 1-3)
3. **Buffering is essential at cellular scale**: with a bacterial cytoplasmic volume on the order of ~1 fL, at **pH ~7.2** the cytosol contains only **~10 free protons**, so **buffer capacity** (e.g., phosphate pools) is crucial; *Lactococcus lactis* is cited with ~**100 mM** cytoplasmic phosphate buffering. (poolman2023physicochemicalhomeostasisin pages 1-2)

### Recent developments (prioritizing 2023–2024)
**Genome-based prediction and comparative genomics of pH preference (2023).** A 2023 *Science Advances* study compiled multi-environment distribution data and identified gene categories associated with pH preference, emphasizing that **no single gene is universal** across datasets, implying that broad pH breadth likely arises from **multiple alternative solutions** (transport, metabolic proton consumption/production, membrane/envelope modifications). This supports modeling pH delta mid3 as a multi-node, multi-edge causal graph rather than a single-marker trait. (ramoneda2023buildingagenomebased pages 3-5)

**Physicochemical homeostasis synthesis (2023).** A 2023 *FEMS Microbiology Reviews* synthesis emphasizes the coupling among intracellular pH, PMF, buffering, transport, and decarboxylation-based energy conservation; it provides quantitative anchors (proton counts; buffer levels; **~3–5 H+ per ATP** for F0F1-ATP synthase usage). (poolman2023physicochemicalhomeostasisin pages 1-2)

**Ecophysiology and membrane/structure mechanisms in environmental groups (2023).** A 2023 review on methanotrophs consolidates mechanisms spanning ion transport, Δψ tuning, lipid headgroup shifts, and S-layer surface charge effects, and provides multiple real-world pH ranges observed for taxa in acidic and alkaline habitats. (yao2023howmethanotrophsrespond pages 5-7)

### Candidate causal graph nodes (grouped by type)

#### A) Phenotype / trait nodes
- **METPO:1000477** pH delta mid3 (wide growth-supporting pH breadth ~4–5 units) (label provided)
- Label-only: “wide growth-supporting pH breadth” (operationalized by growth across ≥~4 pH units)

#### B) Environmental and experimental factor nodes
- Label-only: **external pH (growth medium pH)**
- Label-only: **buffering capacity of medium** (affects external pH stability during growth)
- Label-only: weak permeant acids/bases used in ΔpH assays (methodological factor) (krulwich2011molecularaspectsof pages 3-5)

#### C) Processes / pathways
- Label-only: **pH homeostasis** (process-level node)
- Label-only: **proton motive force (PMF)** with subnodes **Δψ** and **ΔpH** (krulwich2011molecularaspectsof pages 1-3)
- **Amino-acid decarboxylation** (GO:0016831 carboxy-lyase activity; pathway-level) (poolman2023physicochemicalhomeostasisin pages 1-2)
- Label-only: **amino-acid deamination / alkaline response metabolism** (krulwich2011molecularaspectsof pages 5-6)

#### D) Genes / proteins / complexes (mechanistic entities)
Transporters and ion-coupled systems:
- **Na+/H+ antiporters** (GO:0015385 sodium:proton antiporter activity) e.g., **NhaA** (example with stoichiometry) (krulwich2011molecularaspectsof pages 5-6)
- **K+/H+ antiporters** (label-only; class supported) (krulwich2011molecularaspectsof pages 5-6)
- **Mrp antiporter complex / mrp operon (7 genes)** (label-only complex; functional role supported) (krulwich2011molecularaspectsof pages 27-28)
- Label-only: **K+ uptake transporters** that contribute to Δψ (yao2023howmethanotrophsrespond pages 5-7)

Energy transduction:
- **F0F1-ATPase / ATP synthase** (GO:0046933 proton-transporting ATP synthase activity) (poolman2023physicochemicalhomeostasisin pages 1-2, krulwich2011molecularaspectsof pages 5-6)
- Label-only: **proton-pumping respiratory complexes** (primary proton pumps) (krulwich2011molecularaspectsof pages 1-3)

Metabolic pH-stress modules:
- **Glutamate decarboxylase GadB** (GO:0004351) (krulwich2011molecularaspectsof pages 5-6)
- Label-only: associated antiport component in amino-acid decarboxylation modules (krulwich2011molecularaspectsof pages 5-6)
- Label-only: **hydrogenase-3** (proton-consuming) (krulwich2011molecularaspectsof pages 5-6)
- **Urease** (EC:3.5.1.5) and label-only **UreI urea channel** (acid acclimation in *H. pylori*) (krulwich2011molecularaspectsof pages 27-28)
- **Carbonic anhydrase** (EC:4.2.1.1; α/β forms noted in context) (krulwich2011molecularaspectsof pages 27-28)

#### E) Cellular structures / envelope
- Label-only: **membrane lipid composition** (saturation; headgroup composition) controlling proton permeability (yao2023howmethanotrophsrespond pages 5-7)
- Label-only: **S-layer glycoproteins** contributing net negative charge and proton attraction (yao2023howmethanotrophsrespond pages 5-7)

#### F) Chemicals / ions / metabolites
- **CHEBI:15378** hydron (H+)
- **CHEBI:3311** sodium ion (Na+)
- **CHEBI:29103** potassium ion (K+)
- **CHEBI:16199** urea (krulwich2011molecularaspectsof pages 27-28)
- **CHEBI:16526** carbon dioxide; **CHEBI:17544** bicarbonate (krulwich2011molecularaspectsof pages 27-28)
- **CHEBI:16134** ammonia; **CHEBI:28938** ammonium (krulwich2011molecularaspectsof pages 27-28)
- **CHEBI:18367** phosphate (buffer component) (poolman2023physicochemicalhomeostasisin pages 1-2)

### Candidate causal edges (evidence-backed triples)
The following artifact consolidates proposed edges as subject–predicate–object triples with grounding, evidence snippets, and curation notes.

| Edge (S–P–O) | Node type(s) | Ontology grounding (CURIEs where known) | Evidence snippet | Reference (DOI, publication date, URL) | Notes/uncertainty for curation |
|---|---|---|---|---|---|
| External alkaline pH — increases reliance on — electrogenic Na+/H+ antiport for cytoplasmic pH homeostasis | environmental factor → process/transporter | CHEBI:3311 (sodium ion); CHEBI:15378 (hydron); GO:0015385 (sodium:proton antiporter activity) | “Multiple Na+/H+ and K+/H+ antiporters (e.g., *E. coli* NhaA with stoichiometry 2H+/1Na+) are critical for alkaline homeostasis, driven by Δψ.” (krulwich2011molecularaspectsof pages 5-6) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong mechanistic edge for alkaline side of broad pH breadth; general to bacteria but not sufficient alone to define 4–5 unit breadth. |
| NhaA Na+/H+ antiporter — mediates — H+/Na+ exchange supporting alkaline homeostasis | protein/transporter → process | GO:0015385; CHEBI:3311; CHEBI:15378 | “NhaA stoichiometry is given as 2H+/1Na+.” and antiporters are “central” in alkaliphiles and many bacteria carry multiple antiporters (krulwich2011molecularaspectsof pages 5-6) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Gene-specific but exemplar-based; curate as representative antiporter mechanism, not universal marker. |
| mrp operon / Mrp antiporter complex — enables — active proton uptake at high pH | gene family/complex → process | GO:0015385 (broadly applicable sodium:proton antiporter activity); CHEBI:3311; CHEBI:15378 | “For extreme alkaliphiles (*Bacillus pseudofirmus* OF4), a hetero-oligomeric Mrp antiporter (7-gene mrp operon… ) is critical for proton uptake” (krulwich2011molecularaspectsof pages 27-28) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong but taxon-focused to alkaliphilic Bacillus; mark as specific mechanism supporting broad pH tolerance on alkaline side. |
| Regulation of Δψ and ΔpH — supports — maintenance of cytoplasmic pH within viable range across external pH changes | process → phenotype | GO:0009091 (generation of precursor metabolites and energy, broad); label-only: proton motive force; label-only: membrane potential Δψ; label-only: pH gradient ΔpH | “Central to pH homeostasis is the proton motive force (PMF), composed of ΔpH and Δψ” and neutralophiles “grow across external pH ~5.5–9.0 while keeping cytoplasmic pH narrowly near ~7.5–7.7” (krulwich2011molecularaspectsof pages 1-3) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | High-value trait-level edge; closest direct support for pH breadth phenotype. |
| Proton-pumping respiratory complexes — contribute to — PMF for pH homeostasis | complex/pathway → process | GO:0015992 (proton transport); GO:0006979 (response to oxidative stress, not exact); label-only: respiratory chain complex | “Cells use primary proton pumps (respiratory-chain pumps… proton-pumping ATPases)… to create or use PMF for transport and pH regulation” (krulwich2011molecularaspectsof pages 1-3) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Broad foundational mechanism; not uniquely diagnostic for mid3 breadth. |
| F0F1-ATPase — extrudes protons / contributes to — pH homeostasis under acid stress | complex/enzyme → process | GO:0046933 (proton-transporting ATP synthase activity, rotational mechanism); GO:0015992 | “F1Fo-ATPase hydrolytic activity can drive H+ extrusion” and in low-pH contexts F0F1-ATPase is a key regulator (krulwich2011molecularaspectsof pages 5-6, poolman2023physicochemicalhomeostasisin pages 1-2) | doi:10.1038/nrmicro2549 (2011-05) https://doi.org/10.1038/nrmicro2549; doi:10.1093/femsre/fuad033 (2023-06) https://doi.org/10.1093/femsre/fuad033 | Strong general mechanism, especially in fermentative/lactic acid bacteria; directionality may vary by physiology and pH regime. |
| Cytoplasmic phosphate buffering capacity — stabilizes — intracellular pH | metabolite/property → phenotype/process | CHEBI:18367 (phosphate ion) | “Bacterial cytoplasm is small… at pH ~7.2 only ≈10 free protons are present, making buffering essential; *L. lactis* cytoplasmic (organic) phosphate buffering is ~100 mM.” (poolman2023physicochemicalhomeostasisin pages 1-2) | doi:10.1093/femsre/fuad033; 2023-06; https://doi.org/10.1093/femsre/fuad033 | Strong physicochemical mechanism; likely generic and not trait-specific, but highly relevant backbone node. |
| Glutamate decarboxylase GadB — consumes protons to support — acid survival / low-pH homeostasis | enzyme/pathway → phenotype | GO:0004351 (glutamate decarboxylase activity); CHEBI:29985 (L-glutamate); CHEBI:15378 | “Acid responses up-regulate proton-consuming enzymes… glutamate decarboxylase GadB and its antiporter… support survival at very low pH” (krulwich2011molecularaspectsof pages 5-6) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong acid-side mechanism; best curated as acid-tolerance contributor, not sole cause of 4–5 unit breadth. |
| Amino-acid decarboxylation pathways — store energy as / contribute to — PMF and intracellular pH control | pathway → process | label-only: amino-acid decarboxylation; GO:0016831 (carboxy-lyase activity) | “Decarboxylation releases ~20 kJ/mol… can be stored as PMF” and key regulators include “metabolite decarboxylation pathways” (poolman2023physicochemicalhomeostasisin pages 1-2) | doi:10.1093/femsre/fuad033; 2023-06; https://doi.org/10.1093/femsre/fuad033 | Good pathway-level edge; less gene-specific than GadB row. |
| Hydrogenase-3 — consumes protons to produce H2, supporting — survival at very low pH | enzyme/complex → phenotype | EC:1.12.5.1 (hydrogenase, tentative family-level grounding); CHEBI:18276 (hydrogen); CHEBI:15378 | “Hydrogenase-3 and GadB activity is linked to survival at pH 2–2.5” (krulwich2011molecularaspectsof pages 5-6) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong for acid survival; may be enteric/acid-stress specific rather than universal broad-breadth mechanism. |
| UreI-mediated urea influx plus urease activity — alkalinizes/buffers — periplasm under acid stress | transporter + enzyme → compartmental pH state | CHEBI:16199 (urea); EC:3.5.1.5 (urease); CHEBI:28938 (ammonium); CHEBI:16134 (ammonia); label-only: UreI | “Urease/UreI-mediated urea access and export of CO2, NH3 and NH4+… buffer and alkalinize the periplasm and medium” (krulwich2011molecularaspectsof pages 27-28) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong mechanism but highly specific to *Helicobacter pylori* and acidophiles; mark taxon-specific. |
| Carbonic anhydrase + urease/UreI system — maintains — periplasmic pH ~6.1 during acid acclimation | enzyme/process → phenotype | EC:4.2.1.1 (carbonic anhydrase); EC:3.5.1.5; CHEBI:16526 (carbon dioxide); CHEBI:17544 (bicarbonate) | “Cytoplasmic β-carbonic anhydrase and membrane-bound α-carbonic anhydrase… maintain periplasmic pH at ~6.1” (krulwich2011molecularaspectsof pages 27-28) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Strong but specialized; probably unsuitable as broad node unless graph allows conditional/taxon-specific edges. |
| Potassium uptake transporters — generate — internal positive membrane potential (Δψ) | transporter → process | CHEBI:29103 (potassium ion); label-only: potassium uptake transporter; label-only: membrane potential Δψ | “Potassium uptake transporters… generate an internal positive membrane potential” (yao2023howmethanotrophsrespond pages 5-7) | doi:10.3389/fmicb.2022.1034164; 2023-01; https://doi.org/10.3389/fmicb.2022.1034164 | Useful alkaline-homeostasis edge from methanotroph review; transporter identity unresolved in excerpt. |
| Internal positive Δψ — supports — pH homeostasis in alkaliphilic cells | process → phenotype | label-only: membrane potential Δψ; METPO:1000477 | Methanotroph mechanisms include “potassium uptake transporters that generate an internal positive membrane potential” within a broader pH-homeostasis scheme (yao2023howmethanotrophsrespond pages 5-7) | doi:10.3389/fmicb.2022.1034164; 2023-01; https://doi.org/10.3389/fmicb.2022.1034164 | Inferred one-step-up edge from same mechanistic description; moderate confidence. |
| Membrane lipid composition shifts — reduce — proton permeability | cellular component/property → process | GO:0005886 (plasma membrane); label-only: membrane lipid composition; CHEBI:166828 (cardiolipin, approximate if needed) | Methanotrophs use “membrane composition adjustments… to limit proton permeability” and alter phospholipid headgroups under high pH (yao2023howmethanotrophsrespond pages 5-7) | doi:10.3389/fmicb.2022.1034164; 2023-01; https://doi.org/10.3389/fmicb.2022.1034164 | Strong process-level edge; exact lipid entities vary by taxon and condition. |
| S-layer glycoproteins with net negative surface charge — attract — external protons near cell surface | cell envelope structure → ion localization/process | GO:0009276 (Gram-positive-bacterium-type cell wall, broad); label-only: S-layer glycoprotein; CHEBI:15378 | Alkaliphiles may develop “S-layer glycoproteins… to present net negative surface charge and attract external protons” (yao2023howmethanotrophsrespond pages 5-7) | doi:10.3389/fmicb.2022.1034164; 2023-01; https://doi.org/10.3389/fmicb.2022.1034164 | Mechanistically plausible and recent, but likely taxon-specific and somewhat inferential from review. |
| Urease / urea transport genes — associate with — low-pH preference taxa | genes/pathway → phenotype association | EC:3.5.1.5; CHEBI:16199 | “Production of basic compounds (e.g., ammonia from urea) with urea transporters and urease… [is one of] four main mechanisms bacteria use to cope with acid stress” (ramoneda2023buildingagenomebased pages 3-5) | doi:10.1126/sciadv.adf8998; 2023-04; https://doi.org/10.1126/sciadv.adf8998 | Association study, not direct causation; useful as weak genomic-support edge only. |
| Kdp K+ transporters — are overrepresented in — low-pH preference taxa | gene family → phenotype association | label-only: KdpA/KdpC/KdpD; CHEBI:29103 | “Kdp K+ transporters KdpACD are overrepresented in low-pH taxa” (ramoneda2023buildingagenomebased pages 3-5) | doi:10.1126/sciadv.adf8998; 2023-04; https://doi.org/10.1126/sciadv.adf8998 | Genomic association only; no direct causality established in excerpt. |
| Na+/H+ antiporter genes (PhaGF, MnhG, MrpF, YufB) — associate with — higher-pH preference | gene family → phenotype association | GO:0015385; label-only: PhaGF/MnhG/MrpF/YufB | “Na+/H+ antiporters PhaGF, MnhG, MrpF, YufB… correlate with higher-pH preference” (ramoneda2023buildingagenomebased pages 3-5) | doi:10.1126/sciadv.adf8998; 2023-04; https://doi.org/10.1126/sciadv.adf8998 | Association not causation; keep as supportive, uncertain edges. |
| Weak permeant acids/bases — enable measurement of — transmembrane ΔpH / intracellular pH | assay factor → measurement | label-only: weak permeant acid; label-only: weak permeant base | “Methodological and assay factors important for assessing cytoplasmic pH/homeostasis include use of weak permeant acids/bases to measure ΔpH” (krulwich2011molecularaspectsof pages 3-5) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Measurement edge only; should not be curated as biological causal mechanism for the trait. |
| Fluorescent dyes and pH-sensitive GFP — enable measurement of — intracellular pH | assay factor → measurement | label-only: BCECF; label-only: Oregon Green; label-only: pH-sensitive GFP/pHluorin | “fluorescent dyes (BCECF, Oregon Green), pH-sensitive GFP” are used to assess cytoplasmic pH/homeostasis (krulwich2011molecularaspectsof pages 3-5) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Include for assay scope only; not a TraitMech biological edge. |
| 31P-NMR — enables measurement of — intracellular pH at high cell density | assay factor → measurement | label-only: 31P-NMR | “31P-NMR (requires high cell density)” is listed among methods to measure cytoplasmic pH/homeostasis (krulwich2011molecularaspectsof pages 3-5) | doi:10.1038/nrmicro2549; 2011-05; https://doi.org/10.1038/nrmicro2549 | Assay metadata; useful for trait operationalization, not mechanism. |


*Table: This table lists candidate subject–predicate–object edges for curating a TraitMech graph of pH delta mid3, grounded in the gathered evidence only. It separates stronger mechanistic edges from weaker taxon-specific or association-based claims and also records assay-enabling edges relevant to trait measurement.*

### Expert synthesis / interpretive analysis (how to use these edges for pH delta mid3)
A curation-ready interpretation is that **pH delta mid3** emerges when a microbe has **both acid-side and alkaline-side modules** plus sufficient buffering and membrane control to keep intracellular pH in a workable range. The key “backbone” is the **PMF/Δψ/ΔpH control loop** coupled to (i) **proton extrusion systems** under acid stress (e.g., F0F1-ATPase hydrolysis mode; proton-consuming decarboxylation/hydrogenase modules) and (ii) **proton capture/uptake systems** under alkaline stress (e.g., electrogenic Na+/H+ antiporters such as NhaA; Mrp complex in extreme alkaliphiles; Δψ tuning via K+ uptake). (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 27-28, yao2023howmethanotrophsrespond pages 5-7, poolman2023physicochemicalhomeostasisin pages 1-2)

Consistent with this, the genomic association study supports that pH preference is **polygenic and context-dependent**, so TraitMech should represent **mechanistic classes** (antiporters, proton-consuming reactions, envelope permeability control) rather than a single required gene. (ramoneda2023buildingagenomebased pages 3-5)

### Recent statistics and quantitative anchors suitable for curation notes
- Neutralophiles: growth across **external pH ~5.5–9.0** with cytoplasmic pH held near **~7.5–7.7**. (krulwich2011molecularaspectsof pages 1-3)
- Alkaliphile example: *B. pseudofirmus* OF4 grows at **pH 10.5** with **pHin ~8.3**. (krulwich2011molecularaspectsof pages 1-3)
- Acidophiles: can maintain cytoplasmic pH around **~6.0** while growing at **external pH <3** (illustrating strong ΔpH and altered Δψ). (krulwich2011molecularaspectsof pages 11-12)
- Cellular-scale constraint: at **pH ~7.2** in ~**1 fL** cytoplasm there are only **~10 free protons**, motivating high buffer dependence. (poolman2023physicochemicalhomeostasisin pages 1-2)
- Buffer example: *L. lactis* cytoplasmic phosphate buffering **~100 mM**. (poolman2023physicochemicalhomeostasisin pages 1-2)
- Methanotroph pH ranges (examples): *Methylomicrobium buryatense* observed/growth ranges include **6.8–11.0**; other methanotroph-related taxa are detected in acidic and alkaline field sites. (yao2023howmethanotrophsrespond pages 5-7)

### Current applications and real-world implementations
- **Cultivation design and inoculant selection**: genome-based inference of bacterial pH preference is positioned as a tool to improve **cultivation strategies**, **species distribution models**, and **microbial inoculant selection** across environments with pH gradients. (ramoneda2023buildingagenomebased pages 3-5)
- **Food and fermentation contexts**: pH homeostasis mechanisms (including F0F1-ATPase involvement and acid survival systems) are explicitly linked to contexts such as **malolactic fermentation** and survival in acidic niches. (krulwich2011molecularaspectsof pages 5-6)

### Warnings / curation cautions (do not over-curate)
1. **Avoid treating association as causation**: Several 2023 genome-based findings are correlations with pH preference, not mechanistic proof (e.g., Kdp transporter overrepresentation; antiporter gene correlations). Curate these as *uncertain* or “supports association with pH preference,” not definitive causal edges. (ramoneda2023buildingagenomebased pages 3-5)
2. **Taxon-specific modules** (curate as conditional): Urease/UreI/carbonic anhydrase periplasm buffering is well-supported for *Helicobacter pylori* acid acclimation but should be tagged as taxon-specific (or conditional) rather than universal for pH delta mid3. (krulwich2011molecularaspectsof pages 27-28)
3. **Do not mix measurement tools with biology**: fluorescent dyes, 31P-NMR, and weak-acid/base methods are **assay nodes**, not biological mechanisms; keep them in an “assay/measurement” section rather than causal physiology. (krulwich2011molecularaspectsof pages 3-5)
4. **Survival vs growth**: edges supporting survival at pH 2–2.5 (e.g., GadB/hydrogenase modules) may not imply growth across 4–5 pH units; curate as contributors to acid-side tolerance. (krulwich2011molecularaspectsof pages 5-6)

---

## DOI-first bibliography (with dates and URLs)
1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. **2011-05**. DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 3-5)
2. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews*. **2023-06**. DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
3. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances*. **2023-04**. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5)
4. Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology*. **2023-01**. DOI: **10.3389/fmicb.2022.1034164**. URL: https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)


References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

5. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.