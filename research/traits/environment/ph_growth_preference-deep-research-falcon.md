---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:18:57.621107'
end_time: '2026-06-18T00:29:44.560707'
duration_seconds: 646.94
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH growth preference
  trait_identifier: METPO:1003000
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_growth_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes how the rate and extent of population growth
    are affected by environmental pH.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH values that are outside
    the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition
    requiring pH homeostasis.)'
  causal_graph_summary: 'ph_growth_preference_homeostasis: 6 nodes, 5 edges'
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
- **Trait label:** pH growth preference
- **METPO identifier:** METPO:1003000
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes how the rate and extent of population growth are affected by environmental pH.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH values that are outside the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition requiring pH homeostasis.)
- **Existing causal graph summary:** ph_growth_preference_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **pH growth preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_growth_preference.yaml`.

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
- **Trait label:** pH growth preference
- **METPO identifier:** METPO:1003000
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes how the rate and extent of population growth are affected by environmental pH.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH values that are outside the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition requiring pH homeostasis.)
- **Existing causal graph summary:** ph_growth_preference_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **pH growth preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_growth_preference.yaml`.

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


# Microbial Trait Causal Graph Curation Report: pH growth preference (METPO:1003000)

## Scope summary (trait definition and boundaries)
**pH growth preference** (METPO:1003000) should be curated as a *growth phenotype* describing how microbial population growth rate and extent depend on **external/environmental pH** (e.g., optimal pH, growth range limits, and shifts in growth kinetics across pH). Mechanistically, this phenotype is constrained by the need to maintain cytoplasmic pH within a narrow range compatible with enzyme function and bioenergetics (krulwich2011molecularaspectsof pages 1-3).

**Distinguish from nearby traits**:
- **Acid/alkali survival (tolerance/resistance)**: many studies quantify *survival* at extreme pH (e.g., hours at pH 2–3) without growth; these are best treated as related traits unless growth is measured (li2024responseofescherichia pages 2-4).
- **pH homeostasis capacity**: a mechanistic capability (e.g., antiporters/ATPases), which is a primary determinant of pH growth preference but is not the growth phenotype itself (krulwich2011molecularaspectsof pages 5-6).
- **Organic-acid tolerance**: overlaps with low pH but includes weak-acid permeation/toxicity mechanisms; should not be conflated with pH preference unless explicitly tied to external pH growth curves.

## Key concepts and current understanding (mechanistic framing)
### 1) pH homeostasis as the core constraint
External pH challenges microbial growth because cells must keep cytoplasmic pH within bounds compatible with macromolecular function and membrane energetics (krulwich2011molecularaspectsof pages 1-3). A unifying concept is that pH homeostasis reshapes components of the proton motive force (PMF) and demands coordinated activity of primary proton pumps (respiratory complexes/ATPases) and secondary transporters (e.g., cation/proton antiporters) (krulwich2011molecularaspectsof pages 3-5).

### 2) Major mechanistic “modules” that determine pH growth preference
Across diverse microbes, determinants repeatedly involve:
- **Bioenergetic proton cycling and ATPases** (F1F0-ATPase; sometimes Na+-coupled ATPase in alkaliphiles) (krulwich2011molecularaspectsof pages 5-6, xing2024thepolyextremophilenatranaerobius pages 1-2).
- **Cation/proton antiport systems** (Na+/H+, Na+(K+)/H+ antiport; Mrp/Mnh/Nha families) supporting alkaline pH homeostasis and ion balance (krulwich2011molecularaspectsof pages 12-14, wang2023characterizationoftwo pages 10-12).
- **Proton-consuming metabolism** (amino-acid decarboxylation systems) supporting growth/survival at low pH (atasoy2024exploitationofmicrobial pages 3-4, li2024responseofescherichia pages 2-4).
- **Base generation (ammonia) pathways** (urease, glutaminase routes) that increase buffering/neutralize protons (ramoneda2023buildingagenomebased pages 3-5, li2024responseofescherichia pages 2-4).
- **Cell envelope adaptations** (membrane lipid remodeling, surface charge/S-layer features) tuning proton permeability and local proton availability (yao2023howmethanotrophsrespond pages 5-7, jong2023membraneproteomeof pages 1-2).

## Recent developments and latest research (prioritized 2023–2024)
### Genome-based prediction and gene associations (2023)
A key 2023 advance is a genome-informed, cross-environment approach to *inferring bacterial pH preferences* and identifying genomic features associated with those preferences. Ramoneda et al. (Science Advances, Apr 2023) used **five soil and freshwater datasets totaling 1,470 samples** to infer pH preferences from distributions across pH gradients and connect them to genomes (ramoneda2023buildingagenomebased pages 1-1). They report gene types consistently associated with inferred pH preferences across multiple datasets and group these into mechanistic classes that include (i) proton-consuming reactions (decarboxylases/deaminases), (ii) base production (urease-related), (iii) ion transport (Kdp K+ pumps at low pH; Na+/H+ antiporters at higher pH), and (iv) membrane/protein quality-control functions (ramoneda2023buildingagenomebased pages 3-5). This supports curating *genomic determinants* as candidate nodes for TraitMech while clearly flagging association-vs-causation.

### Applied acid-pH knowledge consolidation (2024)
Atasoy et al. (FEMS Microbiology Reviews, Nov 2024) synthesize acid-pH impacts and applied exploitation in food systems, waste valorization, and microbial technologies. They highlight conserved acid-stress mechanisms including **F1F0-ATPase-mediated pH homeostasis**, **amino-acid decarboxylase systems**, **membrane fatty-acid remodeling**, and **stress proteins/chaperones** (atasoy2024exploitationofmicrobial pages 3-4). They also emphasize pH as a controllable lever in real-world processes (food preservation, plasma-activated water, selection of robust strains) (atasoy2024exploitationofmicrobial pages 2-3).

### 2023–2024 examples at alkaline pH and extremes
- Methanotroph ecophysiology reviews emphasize that, while many methanotrophs are neutralophiles, some taxa have **alkaline growth optima** (e.g., *M. buryatense* pH 8.5–9.5; growth range 6.8–11.0; *M. kenyense* pH 9.0–10.0; range 9.0–11.0) and link adaptation to ion transport, membrane/surface modifications, and lipid remodeling (yao2023howmethanotrophsrespond pages 5-7).
- A 2023 experimental study of NhaC-family antiporters shows pH-dependent Na+(K+,Li+)/H+ antiport activity with an **optimal activity at pH 9.5** (tested pH 7.0–10.0) and functional complementation conferring alkaline tolerance to an antiporter-deficient *E. coli* host up to pH 8.5/9.5 depending on antiporter (wang2023characterizationoftwo pages 10-12).
- A 2024 multi-omics/proteomics study of the alkalithermophile *Natranaerobius thermophilus* (thrives at **pH ~9.5**) reports upregulation/presence of **Na+(K+)/H+ transporters** and a **Na+-translocating FOF1-ATPase**, supporting ion homeostasis under combined extremes (xing2024thepolyextremophilenatranaerobius pages 1-2).

## Current applications and real-world implementations
### Food fermentation and preservation (low-pH systems)
- Food fermentation frequently leverages LAB acidification (lactic acid production) to increase shelf life and microbiological safety and to shape texture/flavor; fermentation communities can suppress pathogens and spoilage organisms (atasoy2024exploitationofmicrobial pages 4-5).
- Low pH is used in processing (e.g., canning pretreatments) to inhibit bacterial spore germination and reduce heat resistance (atasoy2024exploitationofmicrobial pages 2-3).
- **Plasma-activated water** rapidly acidifies to ~pH 3.0 and induces acid-stress-like responses while also delivering reactive antimicrobial species (atasoy2024exploitationofmicrobial pages 2-3).

### Probiotics and formulation strategies
Probiotic selection commonly includes in vitro resistance testing at **pH 2.5** as a proxy for gastric passage survival (atasoy2024exploitationofmicrobial pages 5-6). Adaptive conditioning of probiotic strains at sublethal pH (e.g., pH 4.5–5.0) can improve viability in fermented products during storage (atasoy2024exploitationofmicrobial pages 3-4).

### Circular economy / waste valorization and bioprocessing
Food and agricultural wastes are frequently acidic (**often pH < 4.0**), and this can be used to structure microbial consortia for robust processes; Atasoy et al. describe pH < 5 enabling consortia (LAB plus ethanol producers) for robust ethanol production (atasoy2024exploitationofmicrobial pages 5-6).

## Candidate causal-graph nodes (grouped; with grounding suggestions)
### Environmental and experimental factors
- **External environmental pH** (node label only; could link to ENVO “pH” if used in your ontology stack)
- **Acidic pH** (low external pH; node label)
- **Alkaline pH** (high external pH; node label)
- **Acidified food matrix / acidic waste stream** (node label; applied context) (atasoy2024exploitationofmicrobial pages 5-6)

### Biological processes / functions
- **Cytoplasmic pH homeostasis** (GO:0006885) (krulwich2011molecularaspectsof pages 1-3)
- **Proton motive force** (node label; PMF concept used in Krulwich 2011) (krulwich2011molecularaspectsof pages 1-3)
- **Ion homeostasis (Na+, K+)** (node label; supported by antiporter/transport evidence) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Acid stress response** (node label; reviewed for low-pH mechanisms) (atasoy2024exploitationofmicrobial pages 3-4)

### Complexes / transport systems
- **F1F0-ATPase / ATP synthase** (GO:0046961; EC:7.1.2.2) (atasoy2024exploitationofmicrobial pages 3-4, li2024responseofescherichia pages 2-4)
- **Na+/H+ antiporters** (GO:0015385; families include Mrp/Mnh/Nha) (krulwich2011molecularaspectsof pages 12-14, wang2023characterizationoftwo pages 10-12)
- **Mrp antiporter complex** (label-only for subunit set; strong alkaliphily determinant in Bacillus example) (krulwich2011molecularaspectsof pages 12-14)
- **NhaC-family Na+(K+,Li+)/H+ antiporter** (label-only; mechanistic and assay evidence) (wang2023characterizationoftwo pages 10-12)
- **Kdp K+ uptake system (KdpACD)** (KEGG label set; association with low pH preference in comparative study) (ramoneda2023buildingagenomebased pages 3-5)

### Pathways / metabolic modules
- **Glutamate decarboxylase (GAD) system (GadA/GadB/GadC)** (EC:4.1.1.15; glutamate↔GABA cycling) (li2024responseofescherichia pages 2-4)
- **Ammonia production / base generation** (urease-related; glutaminase YbaS route in *E. coli*) (ramoneda2023buildingagenomebased pages 3-5, li2024responseofescherichia pages 2-4)

### Chemicals / metabolites (CHEBI where stable)
- Proton (H+) (CHEBI:24636)
- Sodium ion (Na+) (CHEBI:29101)
- Potassium ion (K+) (CHEBI:29103)
- L-glutamate (CHEBI:18237)
- GABA (CHEBI:16865)
- Glutamine (CHEBI:18050)
- Ammonia (CHEBI:16134)
- Ectoine (CHEBI:27689)
- Glycine betaine (CHEBI:17750)
- Membrane phospholipids as labels (PG/PC/CL/PE/PS/PA) (yao2023howmethanotrophsrespond pages 5-7)

## Evidence-backed candidate causal edges (curation table)
The following edge table is formatted to support curation into `data/traits/environment/ph_growth_preference.yaml`.

| Edge (subject — predicate — object) | Mechanistic category | Grounding suggestions (CURIEs) | Evidence (first author year) | DOI | Publication date (month/year) | URL | Supporting snippet (verbatim or near-verbatim from evidence provided) | Curation notes (strength/uncertainty, taxon/assay specificity) |
|---|---|---|---|---|---|---|---|---|
| external acidic pH — increases requirement for — cytoplasmic pH homeostasis to sustain growth | trait scope / homeostasis | METPO:1003000; GO:0006885 | Krulwich 2011 | 10.1038/nrmicro2549 | May/2011 | https://doi.org/10.1038/nrmicro2549 | “low external pH challenges bacterial growth by forcing cells to maintain a cytoplasmic pH within a narrow range compatible with protein function and bioenergetics” (krulwich2011molecularaspectsof pages 1-3) | Foundational, broad and strong; good scope edge for trait definition, but not a specific gene-level edge. |
| proton-translocating F1F0-ATPase — contributes to — pH homeostasis under low pH | bioenergetics / proton export | GO:0015991; GO:0046961; EC:7.1.2.2; KEGG:K02111 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “pH homeostasis mediated by the proton-translocating F1F0-ATPase” (atasoy2024exploitationofmicrobial pages 3-4) | Strong review support for low-pH growth mechanisms; general across taxa, not species-specific. |
| F0F1-ATPase ATP hydrolysis — consumes intracellular H+ and maintains — acid homeostasis | acid resistance / ATPase | GO:0015991; GO:0046961; EC:7.1.2.2 | Li 2024 | 10.3390/microorganisms12091774 | Aug/2024 | https://doi.org/10.3390/microorganisms12091774 | “F0F1-ATPase is associated with AR1 and under acid stress hydrolyzes ATP to consume intracellular H+ to maintain homeostasis” (li2024responseofescherichia pages 2-4) | Strong but E. coli AR1-specific; more directly acid survival/resistance than preference. Mark as acid-side submechanism. |
| glutamate decarboxylase system (GadA/GadB/GadC) — increases — survival/growth capacity at very low pH | amino-acid decarboxylation | GO:0004351; GO:0015179; EC:4.1.1.15; CHEBI:18237; CHEBI:16865 | Li 2024 | 10.3390/microorganisms12091774 | Aug/2024 | https://doi.org/10.3390/microorganisms12091774 | “GadA and GadB decarboxylate intracellular glutamate to GABA + CO2 while consuming H+, and GadC antiporter exports GABA in exchange for extracellular glutamate” (li2024responseofescherichia pages 2-4) | Strong mechanistic support; E. coli-specific evidence but widely relevant. Better curated as acid-growth/acid-resistance contributor than global pH preference determinant. |
| gadA/gadB/gadC deletion — decreases — survival at pH 2–3 | gene loss phenotype | gene:gadA; gene:gadB; gene:gadC | Li 2024 | 10.3390/microorganisms12091774 | Aug/2024 | https://doi.org/10.3390/microorganisms12091774 | “deletion of gadA/gadB/gadC markedly reduces survival at pH 2–3” (li2024responseofescherichia pages 2-4) | Strong causal genetics, but assay is survival at extreme acid, not measured growth optimum. Curate with uncertainty flag for trait fit. |
| YbaS glutaminase — produces — glutamate plus ammonia that can neutralize protons | ammonia-generating acid response | GO:0006547; EC:3.5.1.2; CHEBI:58359; CHEBI:16134 | Li 2024 | 10.3390/microorganisms12091774 | Aug/2024 | https://doi.org/10.3390/microorganisms12091774 | “glutaminase YbaS (active when ambient pH <6.0 and glutamine is high), which produces glutamate and gaseous ammonia that can neutralize protons” (li2024responseofescherichia pages 2-4) | Strong for acid response in E. coli; may support low-pH growth indirectly. |
| low external pH — induces — amino-acid decarboxylase systems | acid response regulation | GO:0019752; GO:0009268 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “amino-acid decarboxylase systems (including GAD and pathways linked to agmatine/arginine decarboxylation) that consume protons and raise cytoplasmic alkalinity” (atasoy2024exploitationofmicrobial pages 3-4) | Strong review support; pathway-level rather than specific gene evidence. |
| amino-acid decarboxylation — consumes — protons and raises cytoplasmic alkalinity | proton-consuming metabolism | GO:0019752 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “consume protons and raise cytoplasmic alkalinity” (atasoy2024exploitationofmicrobial pages 3-4) | Good generic mechanistic edge for acid-preferring growth. |
| membrane fatty-acid composition changes — support — growth/robustness at low pH | membrane adaptation | GO:0006633; GO:0016042 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “membrane adaptations via modifications of fatty-acid composition” (atasoy2024exploitationofmicrobial pages 3-4) | Moderate review-level support; not tied to a single conserved gene set. |
| stress proteins / chaperones — support — survival and function at low pH | proteostasis | GO:0006457 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “production of stress proteins (chaperones)” (atasoy2024exploitationofmicrobial pages 3-4) | Moderate, broad review evidence; likely too generic unless paired with stronger gene-specific support. |
| gene categories for proton-consuming reactions (decarboxylases/deaminases) — associate with — lower pH preference | comparative genomics association | label:decarboxylase; label:deaminase | Ramoneda 2023 | 10.1126/sciadv.adf8998 | Apr/2023 | https://doi.org/10.1126/sciadv.adf8998 | “four mechanistic classes… (1) proton-consuming reactions (decarboxylases, deaminases…)” and these gene types were “consistently associated with pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Strong comparative association across datasets; association not direct experimental causation. Good candidate edge with uncertainty flag. |
| urease / ammonia-production genes — associate with — lower pH preference | ammonia production | EC:3.5.1.5; CHEBI:16134 | Ramoneda 2023 | 10.1126/sciadv.adf8998 | Apr/2023 | https://doi.org/10.1126/sciadv.adf8998 | “production of basic compounds (ureide_permeases, urease UreE_C producing ammonia)” (ramoneda2023buildingagenomebased pages 3-5) | Strong comparative genomic association; good node family, but specific gene grounding may vary. |
| KdpACD K+ uptake system — associates with — low pH preference | cation transport / acid-side association | KEGG:KdpA/KdpC/KdpD; GO:0006813 | Ramoneda 2023 | 10.1126/sciadv.adf8998 | Apr/2023 | https://doi.org/10.1126/sciadv.adf8998 | “KdpACD K+ pumps associated with low pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Strong cross-environment association; mechanism plausible via membrane potential/pH homeostasis, but direct causal experiments not in source. |
| Na+/H+ antiporters (PhaGF/MnhG/MrpF/YufB) — associate with — higher pH preference | cation/proton antiport | GO:0015385; label:Mrp; label:Mnh; label:Nha | Ramoneda 2023 | 10.1126/sciadv.adf8998 | Apr/2023 | https://doi.org/10.1126/sciadv.adf8998 | “Na+/H+ antiporters PhaGF, MnhG, MrpF, YufB… associated with higher pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Strong comparative genomic evidence; especially useful for alkaline side of trait. Association, not universal causal sufficiency. |
| Na+/H+ antiport — is major mechanism for — alkaline pH homeostasis | alkaline homeostasis | GO:0015385; label:Mrp complex | Krulwich 2011 | 10.1038/nrmicro2549 | May/2011 | https://doi.org/10.1038/nrmicro2549 | “Na+/H+ antiporters (notably the multicomponent Mrp system) are the major mechanism for alkaliphile pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | Foundational and strong; broad mechanistic edge widely reused in later studies. |
| Mrp antiporter complex — is required for — alkaline growth | multimeric transporter | label:MrpA/MrpB/MrpC/MrpD/MrpE/MrpF/MrpG | Krulwich 2011 | 10.1038/nrmicro2549 | May/2011 | https://doi.org/10.1038/nrmicro2549 | “a point mutation in mrpA abolishes Na+/H+ antiport and alkaline growth” (krulwich2011molecularaspectsof pages 12-14) | Strong causal genetics; species-specific to alkaliphilic Bacillus but highly informative. |
| NhaC-family Na+(K+,Li+)/H+ antiporters — confer — tolerance up to alkaline pH 8.5–9.5 | antiporter activity / alkaline tolerance | label:NhaC; GO:0015385 | Wang 2023 | 10.3390/ijms241310786 | Jun/2023 | https://doi.org/10.3390/ijms241310786 | complementation “could make KNabc tolerate… a pH of up to 8.5/9.5, respectively” (wang2023characterizationoftwo pages 10-12) | Strong functional assay, but heterologous complementation in E. coli; tolerance/growth assay rather than native trait measurement. |
| NhaC1/NhaC2 antiport activity — has optimum at — pH 9.5 | pH-dependent transporter activity | label:NhaC1; label:NhaC2; GO:0015385 | Wang 2023 | 10.3390/ijms241310786 | Jun/2023 | https://doi.org/10.3390/ijms241310786 | “antiport activities… are both pH-dependent in the range of pH 7.0–10.0, and the optimal pH is 9.5” (wang2023characterizationoftwo pages 10-12) | Strong biochemical evidence; transporter-level pH optimum, not whole-organism growth preference. Curate carefully. |
| multiple Na+/H+ antiporters plus ATP synthase adaptations — enable — growth of alkaliphiles at pHout ~10.5 and above | alkaline bioenergetics | label:Mrp; GO:0046961; GO:0015385 | Krulwich 2011 | 10.1038/nrmicro2549 | May/2011 | https://doi.org/10.1038/nrmicro2549 | “grows optimally to ~pHout 10.5… and can still grow (slower) with pHin ≥9.5 at pHout ≥11” (krulwich2011molecularaspectsof pages 12-14) | Strong quantitative foundational support; species-specific example (B. pseudofirmus OF4). |
| saturated fatty-acid membrane composition — minimizes — proton permeability | membrane permeability control | GO:0016042; GO:0006633 | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “acidophiles… have saturated fatty-acid membranes to minimize proton permeability, supporting growth at low pH” (yao2023howmethanotrophsrespond pages 5-7) | Moderate-to-strong review evidence from methanotrophs; likely taxon-enriched rather than universal. |
| potassium uptake systems and secondary antiporters — stabilize — cytoplasmic pH | ion homeostasis | GO:0006813; GO:0015299; GO:0015385 | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “secondary symporters/antiporters and potassium uptake systems generate internal positive potential and actively remove protons to stabilize cytoplasmic pH” (yao2023howmethanotrophsrespond pages 5-7) | Good mechanistic edge; review-level and partly inferred across methanotrophs. |
| S-layer glycoproteins / negatively charged cell-surface polymers — attract — protons in alkaline environments | cell envelope adaptation | GO:0009276; GO:0046658 | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “S-layer glycoproteins and changes in cell-wall polymers increase net negative surface charge to attract protons in alkaline environments” (yao2023howmethanotrophsrespond pages 5-7) | Moderate review support; useful for alkaline growth preference graph, but envelope chemistry can be hard to ground specifically. |
| lipid remodeling (PG/PC/CL increase; PE/PS/PA decrease) — supports — high-pH adaptation | membrane lipid remodeling | CHEBI:17001; CHEBI:64482; CHEBI:17962 | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “documented in Methylomicrobium alcaliphilum 20Z (increases in PG, PC, CL; decreases in PE, PS, PA) linked to high-pH adaptation” (yao2023howmethanotrophsrespond pages 5-7) | Strong within this taxon; likely too species-specific for generic curation unless marked uncertain. |
| methanotroph strain M. buryatense — has pH optimum — 8.5–9.5 | phenotype example | NCBITaxon candidate only | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “M. buryatense 8.5–9.5, range 6.8–11.0” (yao2023howmethanotrophsrespond pages 5-7) | Useful quantitative phenotype example; do not generalize as mechanism. |
| methanotroph strain M. kenyense — has pH optimum — 9.0–10.0 | phenotype example | NCBITaxon candidate only | Yao 2023 | 10.3389/fmicb.2022.1034164 | Jan/2023 | https://doi.org/10.3389/fmicb.2022.1034164 | “M. kenyense 9.0–10.0, range 9.0–11.0” (yao2023howmethanotrophsrespond pages 5-7) | Useful phenotype datum; not a mechanism edge. |
| compatible-solute transporters for ectoine and glycine betaine — help maintain — near-neutral intracellular pH at high external pH | osmolytes / alkaline adaptation | CHEBI:27689; CHEBI:17750; GO:0015238 | de Jong 2023 | 10.3389/fmicb.2023.1228266 | Jul/2023 | https://doi.org/10.3389/fmicb.2023.1228266 | “transporters for ectoine and glycine betaine… may assist in maintaining a near neutral internal pH when the external pH is highly alkaline” (jong2023membraneproteomeof pages 1-2) | Moderate evidence from proteomics and interpretation; species-specific to C. thermarum TA2.A1. |
| membrane lipid saturation/branching — increases — membrane rigidity and reduces proton leakage at high pH | membrane biophysics | GO:0016042 | de Jong 2023 | 10.3389/fmicb.2023.1228266 | Jul/2023 | https://doi.org/10.3389/fmicb.2023.1228266 | “more saturated or branched lipids to increase rigidity” and alkaliphiles are “highly susceptible to proton leakage” (jong2023membraneproteomeof pages 1-2) | Moderate mechanistic interpretation; not direct gene-level evidence. |
| Na+(K+)/H+ antiporters — help maintain — intracellular K+ concentration and ion homeostasis under alkaline/high-salt conditions | ion homeostasis / antiport | label:Na+(K+)/H+ antiporter; GO:0015385 | Xing 2024 | 10.1128/aem.00145-24 | May/2024 | https://doi.org/10.1128/aem.00145-24 | “upregulation of Na+/K+/H+ transporters helps maintain intracellular K+ and overall ion homeostasis” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong omics support in Natranaerobius thermophilus; condition includes salinity and temperature, so not pH-only. |
| Na+-translocating FOF1-ATPase — contributes to — growth at alkaline pH ~9.5 | sodium bioenergetics | label:Na+-FOF1-ATPase; GO:0046961 | Xing 2024 | 10.1128/aem.00145-24 | May/2024 | https://doi.org/10.1128/aem.00145-24 | “a large complement of Na+(K+)/H+ antiporters and a Na+-translocating FOF1-ATPase are present and upregulated” in an organism that “thrives as an alkalithermophile at alkaline pH ~9.5” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Moderate-to-strong, but combined-stress adaptation in a polyextremophile; not pH-isolated. |
| low pH fermentation by LAB — suppresses — pathogenic and spoilage bacteria | application / community ecology | GO:0019681; CHEBI:lactic_acid | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “Fermentation generates communities that suppress pathogenic and spoilage bacteria” (atasoy2024exploitationofmicrobial pages 4-5) | Applied edge relevant to real-world importance of trait, but not a direct intrinsic mechanism of preference. |
| adaptive evolution at sublethal pH 4.5–5.0 — improves — viability of probiotic strains in yogurt | application / strain improvement | label:adaptive evolution; label:Lacticaseibacillus rhamnosus GG; label:Bifidobacterium animalis subsp. lactis BB12 | Atasoy 2024 | 10.1093/femsre/fuad062 | Nov/2024 | https://doi.org/10.1093/femsre/fuad062 | “adaptation of L. rhamnosus GG and B. animalis subsp. lactis BB12 at pH 4.5–5.0 improved viability in yogurt during refrigerated storage” (atasoy2024exploitationofmicrobial pages 3-4) | Useful application evidence; strain- and food-matrix-specific, likely not a TraitMech edge. |
| gene presence/absence patterns — can predict — bacterial pH preference across environments | comparative genomics / ML | METPO:1003000 | Ramoneda 2023 | 10.1126/sciadv.adf8998 | Apr/2023 | https://doi.org/10.1126/sciadv.adf8998 | “identified genes consistently associated with pH preference across environments and developed a validated machine-learning model to estimate pH preference from genomic data alone” (ramoneda2023buildingagenomebased pages 1-1) | Important recent development and expert-level framing; not a biological causal edge, but useful report context. |


*Table: This table lists candidate causal edges, supporting snippets, and curation notes for the microbial trait pH growth preference. It combines recent comparative genomics and physiology with foundational mechanistic literature to help decide which nodes and edges are strong enough for TraitMech curation.*

## Expert synthesis / analysis (authoritative interpretations)
- A strong expert consensus is that **pH growth preference is constrained by the energetic cost and effectiveness of pH homeostasis**, including coordination between ATPases, respiratory pumps, and antiporters, plus membrane/surface adaptations that tune proton permeability and local proton availability (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3).
- For alkaliphiles, **Mrp-type antiporters and ATP synthase adaptations** are repeatedly emphasized as core determinants enabling growth in high-pH environments (krulwich2011molecularaspectsof pages 12-14).
- For low pH systems in applied microbiology, the 2024 FEMS Microbiology Reviews synthesis highlights a recurring “toolkit” (F1F0-ATPase, decarboxylases, membrane remodeling, chaperones) that can be leveraged in strain selection/engineering and process design (atasoy2024exploitationofmicrobial pages 3-4).

## Relevant statistics and quantitative data (from included sources)
- **Cross-environment inference dataset size**: five datasets spanning soil and freshwater pH gradients; **1,470 samples** (Ramoneda 2023) (ramoneda2023buildingagenomebased pages 1-1).
- **Quantitative pH optima/ranges (examples)**:
  - Methanotrophs: *M. buryatense* optimum pH **8.5–9.5** (range **6.8–11.0**); *M. kenyense* optimum pH **9.0–10.0** (range **9.0–11.0**) (yao2023howmethanotrophsrespond pages 5-7).
  - NhaC antiporter activity: pH-dependent activity tested **pH 7.0–10.0**, with **optimal activity pH 9.5** (wang2023characterizationoftwo pages 10-12).
  - Polyextremophile lifestyle: *N. thermophilus* thrives at alkaline pH **~9.5** (xing2024thepolyextremophilenatranaerobius pages 1-2).
  - Applied thresholds: plasma-activated water reported to acidify rapidly to **~pH 3.0** (atasoy2024exploitationofmicrobial pages 2-3); acidic wastes “often” **pH < 4.0** (atasoy2024exploitationofmicrobial pages 5-6).
  - Probiotic screening examples: resistance tests at **pH 2.5** cited as relevant for gastric survival (atasoy2024exploitationofmicrobial pages 5-6).

## DOI-first bibliography (publication dates and URLs)
1. **Atasoy M**, Álvarez Ordóñez A, Cenian A, et al. *Exploitation of microbial activities at low pH to enhance planetary health*. **FEMS Microbiology Reviews**. **Nov 2024**. DOI: **10.1093/femsre/fuad062**. https://doi.org/10.1093/femsre/fuad062 (atasoy2024exploitationofmicrobial pages 3-4, atasoy2024exploitationofmicrobial pages 4-5, atasoy2024exploitationofmicrobial pages 2-3, atasoy2024exploitationofmicrobial pages 5-6)
2. **Li Z**, Huang Z, Gu P. *Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review*. **Microorganisms**. **Aug 2024**. DOI: **10.3390/microorganisms12091774**. https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4)
3. **Xing Q**, Zhang S, Tao X, et al. *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress…*. **Applied and Environmental Microbiology**. **May 2024**. DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
4. **Ramoneda J**, Stallard-Olivera E, Hoffert M, et al. *Building a genome-based understanding of bacterial pH preferences*. **Science Advances**. **Apr 2023**. DOI: **10.1126/sciadv.adf8998**. https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-1, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 5-6)
5. **Yao X**, Wang J, Hu B. *How methanotrophs respond to pH: A review of ecophysiology*. **Frontiers in Microbiology**. **Jan 2023**. DOI: **10.3389/fmicb.2022.1034164**. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)
6. **de Jong SI**, Sorokin DY, van Loosdrecht MCM, et al. *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1*. **Frontiers in Microbiology**. **Jul 2023**. DOI: **10.3389/fmicb.2023.1228266**. https://doi.org/10.3389/fmicb.2023.1228266 (jong2023membraneproteomeof pages 1-2)
7. **Wang Q**, Qiao M, Song J. *Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense*. **International Journal of Molecular Sciences**. **Jun 2023**. DOI: **10.3390/ijms241310786**. https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 10-12)
8. **Krulwich TA**, Sachs G, Padan E. *Molecular aspects of bacterial pH sensing and homeostasis*. **Nature Reviews Microbiology**. **May 2011**. DOI: **10.1038/nrmicro2549**. https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6)

## Warnings / “do-not-curate-yet” items
1. **Association vs causation**: Ramoneda et al. identify gene categories associated with inferred pH preference across datasets, but these are not necessarily causal or sufficient in isolation. Curate such edges as *associative/inferred* unless supported by direct perturbation/physiology (ramoneda2023buildingagenomebased pages 3-5).
2. **Survival-only evidence**: many acid-stress mechanisms (e.g., Gad system survival at pH 2–3) primarily support *survival* rather than growth; include only if your trait model explicitly allows survival capacity to influence inferred preference, or mark uncertain (li2024responseofescherichia pages 2-4).
3. **Heterologous complementation caveat**: NhaC alkaline tolerance results are in *E. coli* KNabc complementation; this supports transporter function but not necessarily native-organism growth preference effects (wang2023characterizationoftwo pages 10-12).
4. **Polyextreme confounding**: *N. thermophilus* adaptations are under combined salinity/temperature/pH extremes; treat pH causal attribution as context-dependent (xing2024thepolyextremophilenatranaerobius pages 1-2).
5. **Over-generalizing envelope chemistry**: membrane lipid and S-layer/surface charge mechanisms can be taxon- and environment-specific and may be difficult to ground to stable gene nodes without additional direct sources (yao2023howmethanotrophsrespond pages 5-7).


References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

3. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (wang2023characterizationoftwo pages 10-12): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

8. (atasoy2024exploitationofmicrobial pages 3-4): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

9. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

10. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

11. (jong2023membraneproteomeof pages 1-2): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

12. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

13. (atasoy2024exploitationofmicrobial pages 2-3): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

14. (atasoy2024exploitationofmicrobial pages 4-5): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

15. (atasoy2024exploitationofmicrobial pages 5-6): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

16. (ramoneda2023buildingagenomebased pages 5-6): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.