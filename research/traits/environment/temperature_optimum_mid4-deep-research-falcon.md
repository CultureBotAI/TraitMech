---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:59:21.034951'
end_time: '2026-08-04T04:15:13.223430'
duration_seconds: 952.19
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid4
  trait_identifier: METPO:1000446
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid4
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 34 and 40 \xB0C, characteristic of warm-mesophilic physiology\
    \ (including many mammalian host-associated bacteria)."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_34_to_40
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports a 34\u201340 \xB0C optimum as the\
    \ warm-mesophile (mammalian-host) setpoint.)"
  causal_graph_summary: 'temperature_optimum_mid4_warm_mesophile: 15 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid4.yaml`.

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
- **Trait label:** temperature optimum mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid4.yaml`.

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


# Microbial Trait Causal Graph Curation Report:  
**Temperature Optimum Mid4 (METPO:1000446)**

---

## 1. Trait Scope Summary

METPO:1000446 (temperature optimum mid4) denotes a **warm-mesophilic growth phenotype** with optimal growth temperature between approximately **34 and 40 °C** (engqvist2018correlatingenzymeannotations pages 1-2). This range captures many host-associated bacteria adapted to mammalian body temperatures, including the model organism *Escherichia coli* (Topt=37 °C) (blaby2012experimentalevolutionof pages 1-2). The trait represents the **assay-derived temperature yielding maximal exponential-phase growth rate** rather than maximum survival temperature or broad growth range (blaby2012experimentalevolutionof pages 1-2, murata2011molecularstrategyfor pages 1-2). 

Literature boundaries between psychrophiles (<15 °C), mesophiles (15–50 °C), thermophiles (>50 °C), and intermediate categories remain inconsistent (engqvist2018correlatingenzymeannotations pages 1-2); METPO:1000446 should therefore be curated as an **assay-observable setpoint** rather than a categorical mesophily designation. A recent large-scale analysis of 21,498 microbes demonstrated a Pearson correlation of up to 0.89 between optimal growth temperature and mean enzyme optima, validating the physiological relevance of this trait (engqvist2018correlatingenzymeannotations pages 1-2).

---

## 2. Candidate Causal Graph Entities

### 2.1 Membrane and Lipid Entities
- **Membrane fluidity** (no CURIE; physiological property)
- **Phospholipid saturation ratio** (saturated/unsaturated)
- **Saturated fatty acids** (C16:0, C18:0 acyl-ACP)
- **Unsaturated fatty acids** (C16:1, C18:1 acyl-ACP)
- **FabI** (β-keto-acyl-ACP reductase; label-only or EC:1.3.1.10)
- **FabB** (β-keto-acyl-ACP synthase I; label-only or EC:2.3.1.179)
- **FabA** (β-hydroxydecanoyl-ACP dehydrase/isomerase; label-only or EC:4.2.1.59)
- **PlsB** (glycerol-3-phosphate acyltransferase; EC:2.3.1.15)
- **PlsC** (1-acylglycerol-3-phosphate acyltransferase; EC:2.3.1.51)

### 2.2 Chaperones and Protein Quality Control
- **DnaK** (chaperone Hsp70; label-only or UniProt:P0A6Y8 for *E. coli*)
- **DnaJ** (chaperone Hsp40 co-chaperone; label-only or UniProt:P08622 for *E. coli*)
- **GroEL** / **GroES** (chaperonins; label-only)
- **ClpXP**, **Lon**, **FtsH** (ATP-dependent proteases; label-only)

### 2.3 Heat-Shock Sigma Factors
- **RpoH** (σ32, heat-shock sigma factor; label-only)
- **RpoE** (σ24, envelope-stress sigma factor; label-only)

### 2.4 tRNA and Translation
- **tRNA modification enzymes** (e.g., tRNA-Gln, tRNA-His modifications; functional category)
- **Ribosomal proteins** (downregulated at critical high temperature; GO:0005840 for ribosome)
- **Translation** (GO:0006412)

### 2.5 Outer Membrane and Cell Envelope
- **Outer-membrane organization** (functional category)
- **Lipopolysaccharide biosynthesis** (early glycosyltransferases; label-only or GO:0009103)
- **DegP** (periplasmic protease; label-only)

### 2.6 Oxidative Stress and Energy
- **Oxidative stress resistance** (functional category; GO:0006979)
- **Catalase**, **superoxide dismutase** (label-only or EC:1.11.1.6, EC:1.15.1.1)
- **DNA double-strand break repair** (label-only or GO:0006302)
- **ATP homeostasis** (functional category)

### 2.7 Environmental and Experimental Factors
- **Ambient temperature** (ENVO:01000152 or similar; environmental factor)
- **Mammalian host environment** (37 °C; ENVO context)

---

## 3. Evidence-Backed Candidate Edges

| subject | predicate | object | evidence class | taxon and assay | curation recommendation | DOI |
|---|---|---|---|---|---|---|
| ambient temperature | alters | membrane fluidity | mechanistic acclimation | *Escherichia coli* and broader bacteria; temperature-shift and review evidence on membrane adaptation (moon2023temperaturemattersbacterial pages 3-5, hoogerland2024atemperaturesensitivemetabolic pages 1-2) | curate | 10.1007/s12275-023-00031-x; 10.1038/s41467-024-53677-5 |
| FabI/FabB branchpoint flux allocation | regulates | saturated/unsaturated fatty acid ratio | mechanistic acclimation | *E. coli*; LCMS quantification across 12–42 °C and temperature-shock experiments (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2) | curate taxon-specific | 10.1038/s41467-024-53677-5 |
| saturated/unsaturated fatty acid ratio | contributes to maintenance of | membrane homeoviscosity | mechanistic acclimation | *E. coli* and broader bacteria; membrane lipid remodeling literature and direct phospholipid measurements (siliakus2017adaptationsofarchaeal pages 8-10, hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2) | curate | 10.1007/s00792-017-0939-x; 10.1038/s41467-024-53677-5 |
| glpF deletion | shifts temperature optimum from 37 °C to 43 °C in | *Escherichia coli* growth | direct perturbation | *E. coli* MG1655 derivative; experimental evolution follow-up growth phenotyping (blaby2012experimentalevolutionof pages 1-2) | curate taxon-specific | 10.1128/AEM.05773-11 |
| fabA mutation | increases | membrane lipid saturation | direct perturbation | *E. coli* evolved thermotolerant strain; fatty-acid profiling at 37 and 48 °C (blaby2012experimentalevolutionof pages 7-8, blaby2012experimentalevolutionof pages 1-2) | curate taxon-specific | 10.1128/AEM.05773-11 |
| DnaJ | supports growth at | 37 °C and higher temperatures | direct perturbation | *Salmonella enterica* serovar Typhimurium; recurrent heat-shock evolution with trade-off in growth at 37 °C and above (berdejo2024evolutionarytradeoffbetween pages 1-2) | curate taxon-specific | 10.1128/mbio.03105-23 |
| RpoH | induces | heat-shock genes / chaperone systems | mechanistic acclimation | *E. coli*; review synthesis of heat-shock regulation under temperature upshift (moon2023temperaturemattersbacterial pages 3-5, murata2011molecularstrategyfor pages 1-2) | curate taxon-specific | 10.1007/s12275-023-00031-x; 10.1371/journal.pone.0020063 |
| RpoE | induces | periplasmic protein quality control and outer-membrane biogenesis functions | mechanistic acclimation | *E. coli*; review synthesis of periplasmic heat-shock response (moon2023temperaturemattersbacterial pages 3-5, murata2011molecularstrategyfor pages 1-2) | curate taxon-specific | 10.1007/s12275-023-00031-x; 10.1371/journal.pone.0020063 |
| tRNA modification systems | support growth at | critical high temperature | direct perturbation | *E. coli* knockout screen at 47 °C; also supported by thermotolerant *Zymomonas mobilis* screen around 39 °C (murata2011molecularstrategyfor pages 1-2, charoensuk2017thermotolerantgenesessential pages 1-2) | curate taxon-specific | 10.1371/journal.pone.0020063; 10.1186/s13068-017-0891-0 |
| outer membrane organization / lipopolysaccharide biosynthesis genes | support growth at | critical high temperature | direct perturbation | *E. coli* knockout screen at 47 °C (murata2011molecularstrategyfor pages 1-2, murata2011molecularstrategyfor pages 6-7) | curate taxon-specific | 10.1371/journal.pone.0020063 |
| optimal growth temperature | correlates with | mean enzyme temperature optimum | association | 21,498 microbes; large-scale comparative dataset (engqvist2018correlatingenzymeannotations pages 1-2) | hold | 10.1186/s12866-018-1320-7 |


*Table: This table prioritizes candidate causal edges for the warm-mesophile trait METPO:1000446, distinguishing direct perturbation evidence from acclimation and association. It is useful for deciding which nodes and edges are strong enough to curate now versus hold for broader or more specific evidence.*

### 3.1 Direct Perturbation Edges (High Curation Priority)

**Edge 1:** glpF deletion → Topt shift from 37 to 43 °C  
**Reference:** DOI:10.1128/AEM.05773-11 (Blaby et al., 2012)  
**Snippet:** "Deletion of glpF in a mesophilic wild-type background conferred significantly improved growth rates in the 43-to-48°C temperature range and altered optimal growth temperature from 37°C to 43°C." (blaby2012experimentalevolutionof pages 1-2)  
**Notes:** This is an *E. coli* MG1655 deletion phenotype, demonstrating that aquaporin-glycerol channel activity limits growth above 37 °C. The mechanism (osmotic homeostasis versus temperature-dependent membrane permeability) requires further characterization. Mark as **taxon-specific (E. coli)** and **uncertain mechanism**.

**Edge 2:** fabA mutation → increased membrane lipid saturation  
**Reference:** DOI:10.1128/AEM.05773-11 (Blaby et al., 2012)  
**Snippet:** "A semiquantitative comparison of fatty acids at 48°C revealed significantly higher ratios of saturated/unsaturated fatty acids in EVG1064 [fabA mutant] than in EVG1058 [wild type]. This difference is due largely to significantly more palmitate (C16:0) and significantly less cis-palmitoleate (C16:1 Δ9c) and cis-vaccenate (C18:1 Δ11c)." (blaby2012experimentalevolutionof pages 7-8)  
**Notes:** Experimental evolution at 48 °C selected a fabA allele that increases saturated fatty-acid production. This is a **direct causal edge** for the adaptive mutation, though the phenotype advantage is inferred from thermotolerant fitness rather than Topt measurement. Curate as **taxon-specific (E. coli)** and note that restoration of wild-type fabA produces intermediate phenotype.

**Edge 3:** DnaJ supports growth at 37 °C and higher temperatures  
**Reference:** DOI:10.1128/mbio.03105-23 (Berdejo et al., 2024)  
**Snippet:** "Counterintuitively, this boost in heat shock resistance was invariantly acquired through loss-of-function mutations in the dnaJ gene... As a trade-off, however, the acquisition of heat shock resistance inevitably led to attenuated growth at 37°C and higher temperatures." (berdejo2024evolutionarytradeoffbetween pages 1-2)  
**Notes:** Salmonella Typhimurium dnaJ mutants show trade-off where heat-shock survival increases but growth at optimal temperature (37 °C) decreases. This is a **direct perturbation edge** showing that DnaJ is necessary for maximal growth rate at the warm-mesophile optimum, though the dnaJ phenotype is complex (virulence downregulation, HilD pathway repression). Mark **taxon-specific (Salmonella)** and **uncertain generality**.

**Edge 4:** tRNA modification genes → growth at critical high temperature (47 °C in *E. coli*, 39.5 °C in *Zymomonas*)  
**Reference:** DOI:10.1371/journal.pone.0020063 (Murata et al., 2011); DOI:10.1186/s13068-017-0891-0 (Charoensuk et al., 2017)  
**Snippet (E. coli):** "Their encoded enzymes or proteins are related to outer membrane organization, DNA double-strand break repair, **tRNA modification**, protein quality control, translation control or cell division." (murata2011molecularstrategyfor pages 1-2)  
**Snippet (Zymomonas):** "Products of these genes were classified into nine categories of metabolism, membrane stabilization, transporter, DNA repair, **tRNA modification**, protein quality control, translation control, cell division, and transcriptional regulation." (charoensuk2017thermotolerantgenesessential pages 1-2)  
**Notes:** Knockout screens at critical high temperature in two Gram-negative species independently identified tRNA modification systems (sulfur-relay for tRNA-Gln, tRNA-His modifications) as essential. This is a **direct perturbation edge**, though it applies to survival at supraoptimal temperature rather than Topt itself. Mark **taxon-specific (E. coli, Zymomonas)** but likely conserved across bacteria.

**Edge 5:** outer-membrane organization / LPS early biosynthesis → growth at critical high temperature  
**Reference:** DOI:10.1371/journal.pone.0020063 (Murata et al., 2011)  
**Snippet:** "Early glycosyltransferases for LPS core biosynthesis for proper outer membrane assembly and permeability barrier function... might have been acquired for the organism to perform a main task to survive at CHT." (murata2011molecularstrategyfor pages 6-7)  
**Notes:** E. coli transposon screen; LPS biosynthesis and outer-membrane organization knockouts are temperature-sensitive. Mark **taxon-specific (E. coli, Gram-negative)** and note potential horizontal gene transfer origin.

### 3.2 Mechanistic Acclimation Edges (Medium Curation Priority)

**Edge 6:** Ambient temperature → membrane fluidity  
**Reference:** DOI:10.1007/s12275-023-00031-x (Moon et al., 2023); DOI:10.1038/s41467-024-53677-5 (Hoogerland et al., 2024)  
**Snippet (Moon 2023):** "Organisms counteract the effects of temperature by varying the proportion of lipids that disrupt membrane packing such as unsaturated or branched-chain fatty acids... by varying fatty acyl chain length. This response, known as homeoviscous adaptation, maintains cell membranes at a fixed viscosity level across all growth temperatures." (moon2023temperaturemattersbacterial pages 3-5)  
**Snippet (Hoogerland 2024):** "All free-living microorganisms homeostatically maintain the fluidity of their membranes by adapting lipid composition to environmental temperatures." (hoogerland2024atemperaturesensitivemetabolic pages 1-2)  
**Notes:** This is a **universal mechanistic acclimation**; ambient temperature directly affects membrane viscosity, triggering compensatory lipid remodeling. The edge is curate-eligible for broad applicability.

**Edge 7:** FabI/FabB branchpoint flux allocation → saturated/unsaturated fatty-acid ratio  
**Reference:** DOI:10.1038/s41467-024-53677-5 (Hoogerland et al., 2024)  
**Snippet:** "FabI and FabB indirectly compete for a common pool of substrates. The FabB reaction initiates synthesis of the unsaturated fatty acid thioester C16:1 ACP... Remarkably, within 5 min of the cold shock C16:0 ACP decreased approximately 5-fold, while C18:1 ACP remained stable... The cold shock immediately altered both acyl-ACP and phospholipid intermediate pools." (hoogerland2024atemperaturesensitivemetabolic pages 3-4)  
**Notes:** Direct LCMS quantification in *E. coli* across 12–42 °C shows a **temperature-sensitive metabolic valve** at the FabI/FabB branchpoint that allocates flux between saturated and unsaturated pathways. This is a **mechanistic acclimation edge** validated by isotope experiments. Mark **taxon-specific (E. coli)** but the principle of branchpoint flux control is likely conserved.

**Edge 8:** Saturated/unsaturated fatty-acid ratio → membrane homeoviscosity  
**Reference:** DOI:10.1007/s00792-017-0939-x (Siliakus et al., 2017); DOI:10.1038/s41467-024-53677-5 (Hoogerland et al., 2024)  
**Snippet (Siliakus 2017):** "Thermophilic bacteria increase branched-chain iso-fatty acids, saturated fatty acids, and long-chain fatty acids to stiffen membranes and decrease permeability... The fatty acid composition ratio appears more important than absolute content." (siliakus2017adaptationsofarchaeal pages 8-10)  
**Snippet (Hoogerland 2024):** "The proportions of 16:0 and 18:1 sn-1 phospholipids closely correspond to the composition of the PlsB substrate pool: C16:0 ACP and 16:0 sn-1 phospholipids increase with temperature, while C18:1 ACP and 18:1 sn-1 phospholipids decrease." (hoogerland2024atemperaturesensitivemetabolic pages 3-4)  
**Notes:** Phospholipid analysis directly shows that lipid saturation ratio determines membrane viscosity at a given temperature. This is a **mechanistic acclimation edge**. Curate broadly but note quantitative details are taxon-specific.

**Edge 9:** RpoH → heat-shock genes (DnaK/DnaJ/GroEL/GroES)  
**Reference:** DOI:10.1007/s12275-023-00031-x (Moon et al., 2023); DOI:10.1371/journal.pone.0020063 (Murata et al., 2011)  
**Snippet (Moon 2023):** "RpoH (sigma factor-32) is a heat-shock-responsive sigma factor, which induces a rapid and transient transcriptional increase in the expressions of heat-shock genes in the cell." (moon2023temperaturemattersbacterial pages 3-5)  
**Notes:** This is a well-established **mechanistic acclimation edge** for heat-shock response, not Topt determination. The RpoH/DnaK system is upregulated when temperature exceeds Topt but is not the direct cause of Topt itself. Mark **taxon-specific (E. coli, Salmonella)** and **acclimation only**.

**Edge 10:** RpoE → periplasmic protein quality and outer-membrane biogenesis  
**Reference:** DOI:10.1007/s12275-023-00031-x (Moon et al., 2023); DOI:10.1371/journal.pone.0020063 (Murata et al., 2011)  
**Snippet:** "RpoE (sigma factor-24) acts as a second heat shock regulator that is activated by unfolded proteins in the periplasm... The activated RpoE not only induces expression of heat-shock-related proteins and periplasmic proteases, such as HtrA and DegP, but also induces genes involved in folding of membrane proteins and biosynthesis of lipopolysaccharides." (moon2023temperaturemattersbacterial pages 3-5)  
**Notes:** RpoE is a **mechanistic acclimation edge** for envelope stress. Mark **taxon-specific (Gram-negative)** and **acclimation/stress response**.

### 3.3 Association Edges (Hold for Broader Evidence)

**Edge 11:** Optimal growth temperature ↔ mean enzyme temperature optimum  
**Reference:** DOI:10.1186/s12866-018-1320-7 (Engqvist, 2018)  
**Snippet:** "I validate the dataset by showing a Pearson correlation of up to 0.89 between growth temperature and mean enzyme optima, a physiological property directly influenced by the growth temperature." (engqvist2018correlatingenzymeannotations pages 1-2)  
**Notes:** Large-scale correlation (21,498 microbes) demonstrates that genome-wide enzyme temperature optima track optimal growth temperature. This is an **association edge** (correlation, not perturbation). Hold for curation until direct enzyme-stability experimental edges are available.

---

## 4. Current Understanding and Recent Developments (2023–2024)

### 4.1 Homeoviscous Adaptation Mechanism (2024)
Hoogerland et al. (2024, DOI:10.1038/s41467-024-53677-5) published the most comprehensive mechanistic dissection of bacterial temperature adaptation to date. Using liquid chromatography–mass spectrometry (LCMS) to quantify enzymes, acyl-ACP intermediates, and phospholipids in *E. coli* across 12–42 °C, they demonstrated a **temperature-sensitive metabolic valve** at the FabI/FabB branchpoint that allocates flux between saturated and unsaturated fatty-acid pathways (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2). Within 5 minutes of a cold shock (37 → 13 °C), C16:0 ACP decreased ~5-fold while C18:1 ACP remained stable, causing transient **overshoot** in unsaturated phospholipid synthesis that accelerates membrane adaptation within one generation. This system combines a post-translational valve with a transcriptional negative-feedback loop (FabA/FabB regulation by FabR-C18:1 complex) to achieve homeostasis. The study provides quantitative validation that membrane composition is determined by acyl-ACP substrate pools and that temperature directly modulates FabI/FabB kinetics independently of transcription.

### 4.2 Trade-offs in Chaperone Evolution (2024)
Berdejo et al. (2024, DOI:10.1128/mbio.03105-23) reported that *Salmonella* Typhimurium exposed to repeated lethal heat shock (55 °C, 20 min) invariantly evolved >1,000-fold heat-shock resistance through loss-of-function mutations in **dnaJ** (berdejo2024evolutionarytradeoffbetween pages 1-2). Counterintuitively, dnaJ mutants show attenuated growth at 37 °C and higher temperatures, revealing a **trade-off** where improved heat-shock survival compromises growth rate at optimal temperature. DnaJ acts as a co-chaperone for DnaK, so loss of DnaJ appears to constitutively induce compensatory heat-shock responses (GroEL upregulation) at the cost of normal protein homeostasis. This study demonstrates that heat-shock-resistance mechanisms and optimal-growth-temperature mechanisms can be antagonistic, an important caveat for TraitMech curation.

### 4.3 tRNA Modifications and Thermotolerance (2024)
Yared et al. (2024, DOI:10.3390/genes15030374) reviewed tRNA core modifications beyond the anticodon loop, emphasizing their role in thermotolerance and translation fidelity (yared2024beyondtheanticodon pages 1-2). They cite evidence that tRNA modifications (e.g., tRNA-His modification by TruB) support cellular thermotolerance and survival at elevated growth temperature; knockout strains show temperature-sensitive phenotypes. This aligns with earlier knockout screens (Murata et al., 2011, DOI:10.1371/journal.pone.0020063; Charoensuk et al., 2017, DOI:10.1186/s13068-017-0891-0) that identified tRNA-modification genes as essential for survival at 47 °C (*E. coli*) and 39.5 °C (*Zymomonas*). The mechanism likely involves improved translation efficiency and ribosome stability at elevated temperature.

### 4.4 Genome-Based Prediction of Optimal Growth Temperature (2024)
Barnum et al. (2024, DOI:10.1101/2024.03.22.586313) developed GenomeSPOT, a machine-learning model predicting optimal growth temperature from amino-acid composition without requiring functional gene annotations (barnum2024predictingmicrobialgrowth pages 1-3). Training on 15,596 bacteria and archaea, the model achieved R² = 0.73 for temperature prediction, demonstrating that genome-wide amino-acid frequencies (aromatic, hydrophobic, acidic residues) correlate with thermal adaptation. This approach complements enzyme-annotation methods (Engqvist, 2018) and provides a scalable tool for predicting cultivation conditions for uncultivated microbes. The success of amino-acid-based prediction supports the hypothesis that protein stability is a major genomic signature of optimal growth temperature.

### 4.5 Comparative Genomics of Temperature Ecotypes (2024)
Shen et al. (2024, DOI:10.1093/ismejo/wrad020) analyzed 85 *Exiguobacterium* genomes spanning psychrophilic, mesophilic, halophilic-mesophilic, and halophilic-thermophilic ecotypes, identifying pathway enrichment and protein structural features associated with thermal adaptation (shen2024genomicbasisof pages 1-2). Pangenome analysis revealed that ecotype-specific genes cluster by temperature optimum, with mesophilic strains showing intermediate fatty-acid biosynthesis and chaperone repertoires. This study demonstrates that temperature ecotypes can be delineated by genomic signatures in a poly-extremophilic clade.

---

## 5. Real-World Applications

### 5.1 High-Temperature Fermentation (HTF) Engineering
Warm-mesophile trait engineering is critical for industrial bioethanol production. Charoensuk et al. (2017, DOI:10.1186/s13068-017-0891-0) demonstrated that thermotolerant *Zymomonas mobilis* TISTR 548 (Topt ~39 °C, 5–10 °C above typical *Zymomonas* strains) enables higher-temperature fermentation, reducing cooling costs and contamination risk (charoensuk2017thermotolerantgenesessential pages 1-2). Transposon mutagenesis identified 26 thermotolerant genes, revealing that >60 % overlap with ethanol tolerance, suggesting that membrane stabilization and protein quality control underpin both traits. Similar adaptive laboratory evolution (ALE) approaches have been applied to *E. coli* (Blaby et al., 2012, DOI:10.1128/AEM.05773-11; Sandberg et al., 2014, DOI:10.1093/molbev/msu209) to engineer strains with Topt raised from 37 °C to 42–46 °C for simultaneous saccharification and fermentation (SSF) processes.

### 5.2 Cultivation Prediction for Uncultivated Microbes
Genome-based prediction tools (Barnum et al., 2024, DOI:10.1101/2024.03.22.586313; Ramoneda et al., 2024, DOI:10.1093/ismejo/wrae195) enable targeted cultivation efforts by predicting optimal growth temperature from metagenome-assembled genomes (MAGs). Applied to 85,205 bacterial/archaeal species, the GenomeSPOT model predicted that uncultivated species are enriched in thermophiles, anaerobes, and acidophiles, guiding medium design for previously uncultivatable taxa. This has direct implications for isolating host-associated microbes from mammalian microbiomes (37 °C optimal).

### 5.3 Host-Associated Bacterial Virulence
The warm-mesophile temperature range (34–40 °C) is characteristic of mammalian host-adapted bacteria. Temperature itself acts as a virulence cue: Salmonella, Listeria, and pathogenic *E. coli* use 37 °C as a signal to activate virulence gene expression via RNA thermometers and two-component systems (Shapiro & Cowen, 2012, DOI:10.1128/mbio.00238-12; Steinmann & Dersch, 2013, DOI:10.2217/fmb.12.129). The DnaJ trade-off study (Berdejo et al., 2024, DOI:10.1128/mbio.03105-23) revealed that heat-shock-resistance evolution inadvertently downregulates HilD virulence, suggesting temperature-adaptation pathways intersect with pathogenicity circuits.

---

## 6. Statistical Validation and Data Sources

- **Engqvist (2018, DOI:10.1186/s12866-018-1320-7):** Curated optimal growth temperature for 21,498 microbes from BacDive and culture collections; validated by Pearson r = 0.89 correlation with mean enzyme temperature optima (engqvist2018correlatingenzymeannotations pages 1-2).
- **Barnum et al. (2024, DOI:10.1101/2024.03.22.586313):** Machine-learning model trained on 15,596 bacteria/archaea; R² = 0.73 for temperature prediction; applied to 85,205 sequenced species (barnum2024predictingmicrobialgrowth pages 1-3).
- **Hoogerland et al. (2024, DOI:10.1038/s41467-024-53677-5):** LCMS quantification of ~40 acyl-ACP and phospholipid species across 5 temperatures (12–42 °C) in *E. coli*; 3 technical replicates per 2 independent cultures (hoogerland2024atemperaturesensitivemetabolic pages 3-4).

---

## 7. Curation Warnings and Limitations

### 7.1 Phenotype Definitions and Assay Confounding
Optimal growth temperature is **assay-dependent**: it differs between liquid and solid media, with and without specific nutrients (e.g., methionine lowers *E. coli* Tmax by ~2 °C; McGuire & Nano, 2023, DOI:10.1186/s12864-023-09266-9) (mcguire2023wholegenomesequencinganalysis pages 1-2), and varies with growth phase (exponential versus stationary). TraitMech curation should annotate medium composition and growth phase for each edge.

### 7.2 Taxon Specificity
Most mechanistic evidence is from *E. coli* or *Salmonella*. While membrane homeoviscous adaptation is universal (Siliakus et al., 2017, DOI:10.1007/s00792-017-0939-x), specific regulatory circuits (RpoH/RpoE, FabR-FabA/B) are Gram-negative-specific. Archaea use ether-linked lipids and different desaturases; Gram-positive bacteria lack outer membranes and RpoE. Mark edges accordingly.

### 7.3 Heat-Shock Survival versus Optimal Growth Temperature
Many studies measure **maximum growth temperature (Tmax)** or **heat-shock survival** rather than Topt. For example, Murata et al. (2011, DOI:10.1371/journal.pone.0020063) screened at 47 °C (well above *E. coli* Topt=37 °C), identifying genes required for survival at critical high temperature rather than optimal growth (murata2011molecularstrategyfor pages 1-2). Do not conflate these phenotypes in the causal graph.

### 7.4 Pleiotropic and Trade-off Effects
Several high-confidence edges involve trade-offs:
- **glpF deletion** raises Topt from 37 to 43 °C but reduces growth rate below 43 °C (blaby2012experimentalevolutionof pages 1-2).
- **dnaJ mutation** increases heat-shock resistance but attenuates growth at 37 °C (berdejo2024evolutionarytradeoffbetween pages 1-2).
- **fabA mutation** increases saturation but intermediate complementation shows partial restoration (blaby2012experimentalevolutionof pages 7-8).

These indicate that isolated gene perturbations may not represent natural evolutionary paths to warm-mesophily.

### 7.5 Inferred versus Direct Causal Mechanisms
Edges labeled "mechanistic acclimation" (e.g., RpoH → chaperones) are well-documented stress responses but are not direct determinants of Topt. They should be curated with lower confidence than direct perturbation edges (e.g., glpF deletion → Topt shift).

---

## 8. Bibliography (DOI-First)

1. **DOI:10.1128/AEM.05773-11** — Blaby, I. K., Lyons, B. J., Wroclawska-Hughes, E., Phillips, G. C. F., Pyle, T. P., Chamberlin, S. G., Benner, S. A., Lyons, T. J., de Crécy-Lagard, V., & de Crécy, E. (2012). Experimental evolution of a facultative thermophile from a mesophilic ancestor. *Applied and Environmental Microbiology*, 78(1), 144–155. https://doi.org/10.1128/aem.05773-11
2. **DOI:10.1038/s41467-024-53677-5** — Hoogerland, L., van den Berg, S. P. H., Suo, Y., Moriuchi, Y. W., Zoumaro-Djayoon, A., Geurken, E., Yang, F., Bruggeman, F., Burkart, M. D., & Bokinsky, G. (2024). A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*. *Nature Communications*, 15, 9386. https://doi.org/10.1038/s41467-024-53677-5
3. **DOI:10.1128/mbio.03105-23** — Berdejo, D., Mortier, J., Cambré, A., Sobota, M., Van Eyken, R., Kim, T. D., Vanoirbeek, K., García Gonzalo, D., Pagán, R., Diard, M., & Aertsen, A. (2024). Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in *Salmonella* Typhimurium. *mBio*, 15(3), e03105-23. https://doi.org/10.1128/mbio.03105-23
4. **DOI:10.1007/s12275-023-00031-x** — Moon, S., Ham, S., Jeong, J., Ku, H., Kim, H., & Lee, C. (2023). Temperature matters: bacterial response to temperature change. *Journal of Microbiology*, 61(3), 343–357. https://doi.org/10.1007/s12275-023-00031-x
5. **DOI:10.1371/journal.pone.0020063** — Murata, M., Fujimoto, H., Nishimura, K., Charoensuk, K., Nagamitsu, H., Raina, S., Kosaka, T., Oshima, T., Ogasawara, N., & Yamada, M. (2011). Molecular strategy for survival at a critical high temperature in *Escherichia coli*. *PLoS ONE*, 6(6), e20063. https://doi.org/10.1371/journal.pone.0020063
6. **DOI:10.1186/s13068-017-0891-0** — Charoensuk, K., Sakurada, T., Tokiyama, A., Murata, M., Kosaka, T., Thanonkeo, P., & Yamada, M. (2017). Thermotolerant genes essential for survival at a critical high temperature in thermotolerant ethanologenic *Zymomonas mobilis* TISTR 548. *Biotechnology for Biofuels*, 10, 204. https://doi.org/10.1186/s13068-017-0891-0
7. **DOI:10.1186/s12866-018-1320-7** — Engqvist, M. K. M. (2018). Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. *BMC Microbiology*, 18, 177. https://doi.org/10.1186/s12866-018-1320-7
8. **DOI:10.3390/genes15030374** — Yared, M.-J., Marcelot, A., & Barraud, P. (2024). Beyond the anticodon: tRNA core modifications and their impact on structure, translation and stress adaptation. *Genes*, 15(3), 374. https://doi.org/10.3390/genes15030374
9. **DOI:10.1007/s00792-017-0939-x** — Siliakus, M. F., van der Oost, J., & Kengen, S. W. M. (2017). Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure. *Extremophiles*, 21(4), 651–670. https://doi.org/10.1007/s00792-017-0939-x
10. **DOI:10.3389/fmicb.2023.1265216** — Lehmann, M., Prohaska, C., Zeldes, B., Poehlein, A., Daniel, R., & Basen, M. (2023). Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. *Frontiers in Microbiology*, 14, 1265216. https://doi.org/10.3389/fmicb.2023.1265216
11. **DOI:10.1101/2024.03.22.586313** — Barnum, T. P., Crits-Christoph, A., Molla, M., Carini, P., Lee, H. H., & Ostrov, N. (2024). Predicting microbial growth conditions from amino acid composition. *bioRxiv*, 2024.03.22.586313. https://doi.org/10.1101/2024.03.22.586313
12. **DOI:10.1093/ismejo/wrad020** — Shen, L., Liu, Y., Chen, L., Lei, T., Ren, P., Ji, M., Song, W., Lin, H., Su, W., Wang, S., Rooman, M., & Pucci, F. (2024). Genomic basis of environmental adaptation in the widespread poly-extremophilic *Exiguobacterium* group. *The ISME Journal*, 18(1), wrad020. https://doi.org/10.1093/ismejo/wrad020
13. **DOI:10.1186/s12864-023-09266-9** — McGuire, B. E., & Nano, F. E. (2023). Whole-genome sequencing analysis of two heat-evolved *Escherichia coli* strains. *BMC Genomics*, 24, 154. https://doi.org/10.1186/s12864-023-09266-9

---

## Summary of Ontology Grounding Recommendations

- **METPO:1000446** (temperature_optimum_mid4): Already curated.
- **GO:0005886** (plasma membrane), **GO:0006412** (translation), **GO:0006979** (oxidative stress response), **GO:0009103** (LPS biosynthesis), **GO:0005840** (ribosome): Use for cellular localization and process edges.
- **CHEBI identifiers**: Request for C16:0 (palmitic acid), C16:1 (palmitoleic acid), C18:1 (oleic acid).
- **EC numbers**: FabI (EC:1.3.1.10), FabB (EC:2.3.1.179), FabA (EC:4.2.1.59), PlsB (EC:2.3.1.15), catalase (EC:1.11.1.6).
- **UniProt**: Consider DnaK (P0A6Y8), DnaJ (P08622) for *E. coli* K-12; mark taxon-specific.
- **ENVO:01000152** or similar for ambient temperature.

Label-only nodes (FabR, RpoH, RpoE, GroEL, tRNA modification enzymes) should be added without CURIEs until stable identifiers are confirmed.

References

1. (engqvist2018correlatingenzymeannotations pages 1-2): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

2. (blaby2012experimentalevolutionof pages 1-2): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

3. (murata2011molecularstrategyfor pages 1-2): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

5. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

6. (hoogerland2024atemperaturesensitivemetabolic pages 3-4): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

7. (siliakus2017adaptationsofarchaeal pages 8-10): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

8. (blaby2012experimentalevolutionof pages 7-8): Ian K. Blaby, Benjamin J. Lyons, Ewa Wroclawska-Hughes, Grier C. F. Phillips, Tyler P. Pyle, Stephen G. Chamberlin, Steven A. Benner, Thomas J. Lyons, Valérie de Crécy-Lagard, and Eudes de Crécy. Experimental evolution of a facultative thermophile from a mesophilic ancestor. Applied and Environmental Microbiology, 78:144-155, Jan 2012. URL: https://doi.org/10.1128/aem.05773-11, doi:10.1128/aem.05773-11. This article has 107 citations and is from a peer-reviewed journal.

9. (berdejo2024evolutionarytradeoffbetween pages 1-2): Daniel Berdejo, Julien Mortier, Alexander Cambré, Malgorzata Sobota, Ronald Van Eyken, Tom Dongmin Kim, Kristof Vanoirbeek, Diego García Gonzalo, Rafael Pagán, Médéric Diard, and Abram Aertsen. Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in <i>salmonella</i> typhimurium. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03105-23, doi:10.1128/mbio.03105-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

10. (charoensuk2017thermotolerantgenesessential pages 1-2): Kannikar Charoensuk, Tomoko Sakurada, Amina Tokiyama, Masayuki Murata, Tomoyuki Kosaka, Pornthap Thanonkeo, and Mamoru Yamada. Thermotolerant genes essential for survival at a critical high temperature in thermotolerant ethanologenic zymomonas mobilis tistr 548. Biotechnology for Biofuels, Aug 2017. URL: https://doi.org/10.1186/s13068-017-0891-0, doi:10.1186/s13068-017-0891-0. This article has 43 citations.

11. (murata2011molecularstrategyfor pages 6-7): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

12. (yared2024beyondtheanticodon pages 1-2): Marcel-Joseph Yared, Agathe Marcelot, and Pierre Barraud. Beyond the anticodon: trna core modifications and their impact on structure, translation and stress adaptation. Genes, 15:374, Mar 2024. URL: https://doi.org/10.3390/genes15030374, doi:10.3390/genes15030374. This article has 58 citations.

13. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

14. (shen2024genomicbasisof pages 1-2): Liang Shen, Yongqin Liu, Liangzhong Chen, Tingting Lei, Ping Ren, Mukan Ji, Weizhi Song, Hao Lin, Wei Su, Sheng Wang, Marianne Rooman, and Fabrizio Pucci. Genomic basis of environmental adaptation in the widespread poly-extremophilic exiguobacterium group. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrad020, doi:10.1093/ismejo/wrad020. This article has 41 citations.

15. (mcguire2023wholegenomesequencinganalysis pages 1-2): Bailey E. McGuire and Francis E. Nano. Whole-genome sequencing analysis of two heat-evolved escherichia coli strains. BMC Genomics, Mar 2023. URL: https://doi.org/10.1186/s12864-023-09266-9, doi:10.1186/s12864-023-09266-9. This article has 10 citations and is from a peer-reviewed journal.