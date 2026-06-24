---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:32:48.695668'
end_time: '2026-06-17T23:47:57.163580'
duration_seconds: 908.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range mid2
  trait_identifier: METPO:1000471
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl range phenotype in which the growth-supporting NaCl range spans\
    \ approximately 3\u20138% (w/v), characteristic of moderate-halophile organisms."
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Moderate halophile, NaR_3_to_8
  evidence_summary: "DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation\
    \ review supports the 3\u20138% NaCl growth range as the moderate-halophile category.)"
  causal_graph_summary: 'nacl_range_mid2_moderate_halophile: 3 nodes, 2 edges'
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
- **Trait label:** NaCl range mid2
- **METPO identifier:** METPO:1000471
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 3–8% (w/v), characteristic of moderate-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Moderate halophile, NaR_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl growth range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_range_mid2_moderate_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid2.yaml`.

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
- **Trait label:** NaCl range mid2
- **METPO identifier:** METPO:1000471
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 3–8% (w/v), characteristic of moderate-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Moderate halophile, NaR_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl growth range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_range_mid2_moderate_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid2.yaml`.

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


## Microbial Trait Causal Graph Curation Report: NaCl range mid2 (METPO:1000471)

### Scope summary (trait meaning and boundaries)
**Trait label:** *NaCl range mid2* (METPO:1000471) denotes a **growth-supporting NaCl range spanning ~3–8% (w/v)**, intended to capture organisms in the **moderate-halophile / moderate-halotolerant** regime rather than low-salt or extreme-halophile regimes. A widely used salt-classification scheme defines **mild halophiles (1–3% NaCl), moderate halophiles (3–15% NaCl), and extreme halophiles (15–25% NaCl)**; organisms that tolerate high salt without requiring it are described as **halotolerant**. (benitezmateos2023halomonaselongataa pages 1-3)

A 2023 genome-based physiology report further anchors the **3–8% (w/v)** mid2 window by stating that an organism’s **optimum growth range of 0.5–1.35 M NaCl corresponds to ~3–8% (w/v)**. (sharma2023genomeanalysisof pages 2-3)

**Boundary cases to distinguish during curation**
- **Halotolerant but not “mid2”**: organisms that grow best at low salinity yet tolerate higher salinity may not belong in mid2 unless their **growth-supporting range includes ~3–8%**. Example: *Halomonas elongata* is described as a moderate halophile/halotolerant organism that can tolerate **5–25% NaCl**, but “tolerance” does not necessarily imply optimum growth at 3–8%. (benitezmateos2023halomonaselongataa pages 1-3)
- **Moderate halophile broader class vs. mid2**: “moderate halophile” is often used for **3–15% NaCl**, which is broader than METPO mid2; therefore mid2 should be treated as a **subclass / narrower phenotype**. (benitezmateos2023halomonaselongataa pages 1-3)
- **Assay dependence**: reported ranges depend on medium composition (osmoprotectants, yeast extract), temperature, and whether the phenotype is “growth range” vs “shock tolerance.” For example, a “tolerable NaCl shock range” is not identical to sustained-growth range. (yu2024temporaldynamicsof pages 1-2)

### Key concepts and current mechanistic understanding (salt-out centered, with ion-homeostasis support)
Across many moderate halophiles, the dominant mechanistic framing is **“salt-out” osmoadaptation**: maintaining low cytosolic inorganic salt while accumulating **compatible solutes** (osmolytes) such as **ectoine** and **glycine betaine**, supported by transport systems and precursor-supply metabolism. (galisteo2023astepinto pages 13-14)

A 2024 multi-omics study in *Halomonas elongata* highlights a time-resolved version of this: during NaCl upshift (within a tolerable range), cells rapidly buffer osmotic pressure via **Na⁺/K⁺ uptake** and **amino-acid pool increases (notably glutamate/glutamine)**, followed later by accumulation of **ectoine as the dominant osmoprotectant**. (yu2024temporaldynamicsof pages 1-2)

### Candidate nodes (grouped by type) with ontology grounding suggestions

#### A) Environmental / experimental factors
- **Sodium chloride (NaCl)** — CHEBI:26710 (sharma2023genomeanalysisof pages 2-3)
- **Moderate salinity window: 3–8% (w/v) NaCl** — maps to METPO:1000471 (trait); environment can be represented as label-only “3–8% (w/v) NaCl” (sharma2023genomeanalysisof pages 2-3)
- **NaCl shock (1–8% range cited for *H. elongata* tolerance)** — label-only “NaCl shock 1–8%” (yu2024temporaldynamicsof pages 1-2)

#### B) Compatible solutes / metabolites
- **Ectoine** — CHEBI:22562 (yu2024temporaldynamicsof pages 1-2, galisteo2023astepinto pages 13-14)
- **Glycine betaine** — CHEBI:17750 (galisteo2023astepinto pages 13-14)
- **L-glutamate** — CHEBI:29991 (yu2024temporaldynamicsof pages 1-2, zou2024metabolicengineeringof pages 2-4)
- **L-glutamine** — CHEBI:28300 (yu2024temporaldynamicsof pages 1-2)
- **L-proline** — CHEBI:26271 (engineered substitution evidence; not strictly required for mid2 but mechanistically relevant) (khanh2024metabolicpathwayengineering pages 1-2)
- **γ-aminobutyric acid (GABA)** — CHEBI:16865 (engineered/alternative osmolyte evidence) (zou2024metabolicengineeringof pages 2-4)

#### C) Genes / enzymes / transport systems
**Ectoine biosynthesis pathway (conserved core):**
- **ectA / ectB / ectC operon** — label-only gene nodes; pathway grounding: GO:1901678 (ectoine biosynthetic process) (galisteo2023astepinto pages 13-14)
- **lysC, asd** (precursor supply for ectoine biosynthesis from aspartate) — label-only gene nodes (galisteo2023astepinto pages 13-14)
- **ectD** (5-hydroxyectoine synthesis; not universal) — label-only gene node (galisteo2023astepinto pages 13-14)

**Glycine betaine synthesis and uptake:**
- **BetA (choline → betaine aldehyde)** — KEGG:K00108 (as used in the genomic survey) (galisteo2023astepinto pages 13-14)
- **BetB (betaine aldehyde → glycine betaine)** — KEGG:K00130 (galisteo2023astepinto pages 13-14)
- **OpuABC transporter** — KEGG:K05845/K05846/K05847 (galisteo2023astepinto pages 13-14)
- **ProVWX transporter** — KEGG:K02000/K02001/K02002 (galisteo2023astepinto pages 13-14)
- **OpuD (BCCT family)** — label-only (galisteo2023astepinto pages 13-14)

**Ectoine uptake / salvage:**
- **TeaABC / UehABC (TRAP-family ectoine uptake systems)** — label-only transport systems (galisteo2023astepinto pages 13-14)

**Ion homeostasis / osmotic downshift:**
- **ChaA Na⁺/H⁺ antiporter** — KEGG:K07300 (galisteo2023astepinto pages 13-14)
- **Mechanosensitive channels (Msc)** — KEGG:K16053 and K03282 (galisteo2023astepinto pages 13-14)
- **Na⁺ symporter (Halomonas sp. transcriptomic response)** — label-only (yoo2023insightsintosaline pages 3-5)

**Stress response nodes (often co-induced under salt stress):**
- **cysB transcription factor**, **peroxidase HELO_RS18165**, **POD/CAT enzyme activities** — label-only; process grounding: GO:0006979 response to oxidative stress (yu2024temporaldynamicsof pages 1-2)

#### D) Processes / functions
- **Response to osmotic stress** — GO:0006970 (yu2024temporaldynamicsof pages 1-2)
- **Sodium ion transport** — GO:0006814; **Potassium ion transport** — GO:0006813 (yu2024temporaldynamicsof pages 1-2)

### Evidence-backed candidate causal edges (curation table)
The following artifact compiles candidate edges as **subject–predicate–object triples** with snippets, ontology grounding suggestions, and curation uncertainty notes.

| Edge (S–P–O) | Node type(s) | Suggested ontology grounding | Evidence (citation id) | Publication year | DOI URL | Supporting snippet (short quote) | Notes/uncertainty for curation |
|---|---|---|---|---|---|---|---|
| NaCl 3–8% (w/v) environment → supports growth of → moderate-halophile phenotype | environmental factor → trait | CHEBI:26710 sodium chloride; METPO:1000471 NaCl range mid2 | (sharma2023genomeanalysisof pages 2-3, benitezmateos2023halomonaselongataa pages 1-3) | 2023 | https://doi.org/10.3389/fmicb.2023.1229955 ; https://doi.org/10.1007/s00253-023-12510-7 | “optimum growth range of 0.5–1.35 M NaCl, which… corresponds to about 3–8% (w/v) NaCl”; “moderate halophiles (3–15% NaCl)” | Strong for scope definition, but this is phenotype-level rather than a molecular mechanism. Trait is a narrower subset within the broader “moderate halophile” class. |
| ectABC operon → enables biosynthesis of → ectoine | gene cluster → pathway/metabolite | label-only: ectABC operon; GO:1901678 ectoine biosynthetic process; CHEBI:22562 ectoine | (galisteo2023astepinto pages 13-14, shu2023metabolicengineeringof pages 6-6) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 ; https://doi.org/10.1038/s41598-023-36975-8 | “ectoine biosynthesis from L-aspartate via lysC, asd, ectB, ectA, ectC”; “The biosynthesis of ectoine relies on the ectABC” | Strong, repeatedly supported across taxa. Good core mechanism node/edge for TraitMech. |
| ectoine accumulation → contributes to → growth/tolerance at 6–8% NaCl | metabolite/process → trait | CHEBI:22562 ectoine; METPO:1000471 NaCl range mid2 | (yu2024temporaldynamicsof pages 1-2, zou2024metabolicengineeringof pages 2-4) | 2024 | https://doi.org/10.1186/s12934-024-02358-5 ; https://doi.org/10.1128/aem.01905-23 | “Within the cell’s tolerable range (1–8% NaCl shock)… ectoine… rapidly becoming the dominant osmoprotectant”; wild type “maintains Glu levels at 6% and 7% NaCl due to ectoine accumulation” | Strong in Halomonas elongata; directly relevant to 3–8% window. Prefer predicate like “positively contributes to” rather than absolute necessity across all taxa. |
| deletion of ectABC → decreases ability to grow in → 6% NaCl | gene cluster perturbation → phenotype | label-only: ΔectABC; METPO:1000471 NaCl range mid2 | (zou2024metabolicengineeringof pages 2-4) | 2024 | https://doi.org/10.1128/aem.01905-23 | “KA1 grows well at 3% NaCl… cannot grow at 6% NaCl” | Strong causal evidence, but from engineered knockout in one taxon. Curate as taxon-specific/experimental support for ectoine dependence. |
| uptake of Na+ and K+ ions → rapidly balances → osmotic pressure after NaCl upshift | ion transport process → biological process | GO:0006814 sodium ion transport; GO:0006813 potassium ion transport; GO:0006970 response to osmotic stress | (yu2024temporaldynamicsof pages 1-2) | 2024 | https://doi.org/10.1186/s12934-024-02358-5 | “Within the cell’s tolerable range (1–8% NaCl shock), H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” | Strong physiological edge, but transporter genes are not specified in this excerpt. Good process-level edge. |
| increased intracellular glutamate/glutamine pools → provide early osmotic buffering during → 1–8% NaCl shock | metabolites/process → phenotype/process | CHEBI:29991 L-glutamate; CHEBI:28300 glutamine; GO:0006970 response to osmotic stress | (yu2024temporaldynamicsof pages 1-2) | 2024 | https://doi.org/10.1186/s12934-024-02358-5 | “augmenting intracellular amino acid pools, particularly glutamate and glutamine” | Good short-timescale adaptation edge; likely transient/early response before ectoine dominance. |
| hom knockout → increases precursor flux toward → ectoine biosynthesis | gene perturbation → pathway | label-only: hom; GO:1901678 ectoine biosynthetic process; CHEBI:15727 L-aspartate-semialdehyde | (shu2023metabolicengineeringof pages 6-6, shu2023metabolicengineeringof pages 6-10) | 2023 | https://doi.org/10.1038/s41598-023-36975-8 | “blocking the metabolic shunt pathway to increase ectoine yields”; “diverting precursor flux to ectoine” | Strong causal engineering evidence for pathway architecture; indirect support for native mechanism. Mark as engineered/flux-redirection context. |
| increased ectoine production → shifts growth optimum toward → higher salinity (~1.5 M NaCl) | metabolite/pathway output → phenotype | CHEBI:22562 ectoine; label-only: 1.5 M NaCl (~8.8% w/v) | (shu2023metabolicengineeringof pages 6-6) | 2023 | https://doi.org/10.1038/s41598-023-36975-8 | “maximum growth shifted to 1.5 mol NaCl” and XH26/Δhom produced more ectoine | Useful but slightly above 8% w/v if converted exactly; curate cautiously as adjacent-support rather than direct mid2 edge. |
| betaine production → is favored at → lower salinity relative to ectoine | metabolite → environmental condition | CHEBI:17750 glycine betaine; CHEBI:22562 ectoine | (shu2023metabolicengineeringof pages 6-6, shu2023metabolicengineeringof pages 6-10) | 2023 | https://doi.org/10.1038/s41598-023-36975-8 | “Betaine is noted as a compatible solute used at low salt”; “at 3.0 mol NaCl both strains produced no betaine while the mutant still produced ectoine” | Strong comparative pattern in H. campaniensis, but exact low-salt boundary for mid2 curation is fuzzy. Mark as context-dependent. |
| BetA + BetB pathway → enables biosynthesis of → glycine betaine from choline | enzymes/pathway → metabolite | EC/label-only BetA (choline dehydrogenase), BetB (betaine aldehyde dehydrogenase); CHEBI:17750 glycine betaine; CHEBI:15354 choline | (galisteo2023astepinto pages 13-14) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 | “choline to glycine betaine via BetA… and BetB” | Strong genomic support across moderate halophiles; direct phenotypic linkage to 3–8% NaCl is inferred unless paired with assay data. |
| OpuABC / OpuD / ProVWX transport systems → mediate uptake of → glycine betaine | transporter complexes → metabolite | KEGG:K05845/K05846/K05847 OpuABC; label-only OpuD; KEGG:K02000/K02001/K02002 ProVWX; CHEBI:17750 glycine betaine | (galisteo2023astepinto pages 13-14) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 | “OpuABC… OpuD… ProVWX ABC glycine betaine transporter… present in all genomes” | Good candidate transport edges; evidence is genomic/potential rather than direct growth assay in 3–8% NaCl. Mark uncertain if curating as generic necessity. |
| TeaABC / UehABC transporters → mediate uptake of → ectoine / 5-hydroxyectoine | transporter complexes → metabolites | label-only TeaABC, UehABC; CHEBI:22562 ectoine; label-only 5-hydroxyectoine | (galisteo2023astepinto pages 13-14) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 | “TeaABC and UehABC TRAP transporters for ectoine/5-hydroxyectoine uptake” | Strong transporter-function assignment from genomics/literature synthesis; direct contribution to mid2 phenotype is likely but not assay-proven here. |
| ectC-containing ectoine gene cluster → supports adaptation to → saline conditions (e.g., 5% NaCl) | gene cluster/enzyme → phenotype | label-only ectC; CHEBI:22562 ectoine | (yoo2023insightsintosaline pages 3-5) | 2023 | https://doi.org/10.3389/fmars.2023.1229444 | “ectoine synthase (ectC) gene cluster was identified… indicating capacity for ectoine-based compatible-solute synthesis” | Useful taxon-specific support in Halomonas sp. YJPS3-2; mostly genomic/transcriptomic inference rather than knockout proof. |
| Na+ symporter activity → contributes to adaptation under → elevated salinity | transporter/process → phenotype | label-only Na+ symporter; GO:0006814 sodium ion transport | (yoo2023insightsintosaline pages 3-5) | 2023 | https://doi.org/10.3389/fmars.2023.1229444 | “many ABC transporters, two-component systems, and a Na+ symporter were affected” | Weak-to-moderate: differential expression implies involvement, but substrate/causal direction not resolved. |
| ChaA antiporter → contributes to → Na+ extrusion / ion homeostasis under salt stress | transporter → process | KEGG:K07300 ChaA; GO:0006814 sodium ion transport | (galisteo2023astepinto pages 13-14) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 | “ChaA antiporter (K07300)” | Genomic support only in subset of strains; valuable candidate node, but insufficient direct phenotype evidence for core graph without further support. |
| Msc mechanosensitive channels → release solutes during → osmotic downshift/homeostasis | channel/protein → process | KEGG:K16053, K03282; GO:0006810 transport | (galisteo2023astepinto pages 13-14) | 2023 | https://doi.org/10.3389/fmicb.2023.1192059 | “Msc mechanosensitive channels K16053/K03282” | Plausible osmoadaptation component, especially downshock rather than sustained mid2 growth. Mark as uncertain for direct trait curation. |
| glutamate overproduction → partially restores growth in → ectoine-deficient cells at 6% NaCl | metabolite/process → phenotype | CHEBI:29991 L-glutamate; METPO:1000471 NaCl range mid2 | (zou2024metabolicengineeringof pages 2-4) | 2024 | https://doi.org/10.1128/aem.01905-23 | “The GOP mutant can grow at 6% NaCl” | Strong causal evidence in an adaptive mutant, but taxon- and background-specific; less effective than ectoine in wild type. |
| gadB-mediated conversion of glutamate to GABA → improves salt tolerance of → ectoine-deficient cells up to ~7% NaCl | enzyme/process → phenotype | label-only gadB / HopGadBmut; CHEBI:16865 GABA; CHEBI:29991 L-glutamate | (zou2024metabolicengineeringof pages 2-4) | 2024 | https://doi.org/10.1128/aem.01905-23 | “produces and accumulates GABA in response to salt and shows higher salt tolerance than GOP” | Good engineered causal edge for alternative osmolyte mechanism; not necessarily native to all moderate halophiles. Mark engineered/taxon-specific. |
| ectA promoter salt induction → increases expression of → gadB transgene under saline stress | promoter/regulatory element → gene expression | label-only ectA promoter; label-only HopGadBmut | (zou2024metabolicengineeringof pages 2-4) | 2024 | https://doi.org/10.1128/aem.01905-23 | “under a salt-inducible ectA promoter” | Valuable only for engineered systems; probably not suitable for generic TraitMech unless modeling synthetic evidence separately. |


*Table: This table compiles evidence-backed candidate subject–predicate–object edges for curating the NaCl range mid2 trait as a moderate-halophile phenotype. It emphasizes mechanisms with direct support in the 3–8% NaCl range and flags edges that are taxon-specific, engineered, or based mainly on genomic inference.*

### Recent developments (2023–2024) and what changed in the mechanistic picture
1. **Time-resolved osmoadaptation at mid2-relevant salinities (systems biology)**: *H. elongata* shows a tolerable NaCl shock range **1–8%**, with rapid ion uptake and amino-acid accumulation followed by delayed but dominant **ectoine** accumulation; ectoine productivity reached **1450 ± 99 mg/L/h**, and optimal biomass/ectoine accumulation occurred at **8% NaCl**. (yu2024temporaldynamicsof pages 1-2)
2. **Causal “osmolyte substitution” experiments** demonstrate compatibility of different organic osmolytes in mid2 windows:
   - In an *H. elongata* ΔectABC background, **growth at 6% NaCl is lost**, but adaptive/engineered routes that accumulate **glutamate** and then convert it to **GABA** can improve tolerance (GOP grows at 6%; GOP-Gad improves tolerance; GOP fails above ~7%). (zou2024metabolicengineeringof pages 2-4)
   - Replacement of ectoine biosynthesis with an engineered proline pathway can restore growth in **8% NaCl**, with intracellular proline reaching **353.1 ± 40.5 µmol/g cell fresh weight**, supporting the general principle that compatible solutes can be functionally substitutable if accumulated sufficiently. (khanh2024metabolicpathwayengineering pages 1-2)
3. **Metabolic-flux control as an engineering and mechanistic probe**: In *H. campaniensis*, knocking out **hom** to reduce a precursor “shunt” increased ectoine yields and shifted the salinity associated with **maximum growth** toward **1.5 M NaCl**, while also altering betaine output, underscoring precursor supply as a control point in ectoine-linked halotolerance. (shu2023metabolicengineeringof pages 6-6, shu2023metabolicengineeringof pages 6-10)

### Current applications and real-world implementations
1. **Biotechnology using moderate halophiles and their enzymes**: A 2023 mini-review argues that enzymes from the moderate halophile/halotolerant organism *Halomonas elongata* are attractive industrial biocatalysts because they are **more resistant to salt** than mesophilic homologs while being more tractable than extreme halophiles; the paper also visually illustrates protein surface adaptations (enrichment of negatively charged residues) associated with function in saline conditions. (benitezmateos2023halomonaselongataa pages 1-3, benitezmateos2023halomonaselongataa media bc663ed1)
2. **Industrial and open/low-sterility compatible-solute production logic** (mechanistically relevant to mid2): Multiple 2023–2024 studies emphasize **ectoine** as a high-value product and a major osmolyte in *Halomonas* spp., motivating strain and process engineering. For example, a 2023 genomic survey notes a reported ectoine production figure of **28 g/L** in an engineered *Halomonas* (biotech context). (galisteo2023astepinto pages 13-14)

### Expert synthesis / interpretations suitable for curation notes
- The combined evidence supports a **core mid2 mechanism**: (i) NaCl imposes osmotic pressure; (ii) cells respond through rapid ion flux adjustments and emergency amino-acid pool changes; (iii) sustained mid2 growth is associated with **dominant compatible solute accumulation**, especially **ectoine** in many *Halomonas* spp., supported by conserved biosynthesis and uptake genes and by metabolic precursor allocation. (yu2024temporaldynamicsof pages 1-2, galisteo2023astepinto pages 13-14, shu2023metabolicengineeringof pages 6-6)

### Relevant statistics and quantitative data (recent studies)
- Classification: mild 1–3%, moderate 3–15%, extreme 15–25% NaCl; halotolerant = tolerates without requiring. (benitezmateos2023halomonaselongataa pages 1-3)
- Mapping to mid2: optimum growth 0.5–1.35 M NaCl corresponds to **~3–8% (w/v)**. (sharma2023genomeanalysisof pages 2-3)
- *H. elongata* NaCl shock: tolerable range **1–8%**; ectoine productivity **1450 ± 99 mg/L/h**; optimum biomass/ectoine at **8%**. (yu2024temporaldynamicsof pages 1-2)
- *H. elongata* ectABC deletion background: KA1 grows at **3%**, suppressed at **4%**, **no growth at 6%**; GOP grows at **6%** but not **>7%**. (zou2024metabolicengineeringof pages 2-4)
- Engineered proline substitution: growth at **8% NaCl** with intracellular proline **353.1 ± 40.5 µmol/g cell fresh weight**. (khanh2024metabolicpathwayengineering pages 1-2)
- *H. campaniensis* Δhom: growth optimum shift to **1.5 M NaCl**; ectoine yields up to **587.09 mg/g CDW** (bioreactor), with altered betaine yields. (shu2023metabolicengineeringof pages 6-6)

### Warnings / items not yet safe to curate as “core” TraitMech edges
1. **Transporters and antiporters (ChaA, Msc, TeaABC/UehABC, Opu systems)** are strongly supported as genomic candidates across taxa, but in the provided evidence they are often supported by **presence/annotation** rather than direct causal knockouts tied specifically to **3–8% NaCl growth**; consider curating these as **candidate/putative** edges unless additional functional studies are added. (galisteo2023astepinto pages 13-14)
2. **Na⁺ symporter and many ABC transporter genes** are linked via differential expression to salinity adaptation in *Halomonas* sp. YJPS3-2, but the directionality (which substrates, necessity for mid2 growth) remains uncertain from transcriptomics alone. (yoo2023insightsintosaline pages 3-5)
3. **Engineered osmolyte substitutions (proline, GABA)** provide strong causal logic that compatible solute accumulation can restore tolerance, but they are **strain-engineering demonstrations** and should be tagged as **taxon-/assay-specific** rather than universal for mid2. (zou2024metabolicengineeringof pages 2-4, khanh2024metabolicpathwayengineering pages 1-2)

---

## DOI-first bibliography (with dates and URLs)
- Benítez-Mateos AI, Paradisi F. **Halomonas elongata: a microbial source of highly stable enzymes for applied biotechnology.** *Applied Microbiology and Biotechnology*. **2023-04**. https://doi.org/10.1007/s00253-023-12510-7 (benitezmateos2023halomonaselongataa pages 1-3, benitezmateos2023halomonaselongataa media bc663ed1)
- Sharma A, et al. **Genome analysis of a halophilic Virgibacillus halodenitrificans ASH15 revealed salt adaptation…** *Frontiers in Microbiology*. **2023-09**. https://doi.org/10.3389/fmicb.2023.1229955 (sharma2023genomeanalysisof pages 2-3)
- Yu J, et al. **Temporal dynamics of stress response in Halomonas elongata to NaCl shock…** *Microbial Cell Factories*. **2024-03**. https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2)
- Zou Z, et al. **Metabolic engineering of… GABA improves salt-stress tolerance… in ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology*. **2024-01**. https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 2-4)
- Khanh HC, et al. **Metabolic pathway engineering… overproduction of L-proline… in ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology*. **2024-09**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)
- Shu Z, et al. **Metabolic engineering of Halomonas campaniensis… enhance ectoine production.** *Scientific Reports*. **2023-06**. https://doi.org/10.1038/s41598-023-36975-8 (shu2023metabolicengineeringof pages 6-6, shu2023metabolicengineeringof pages 6-10)
- Galisteo C, et al. **A step into the rare biosphere… Terrihalobacillus… Aquibacillus…** *Frontiers in Microbiology*. **2023-05**. https://doi.org/10.3389/fmicb.2023.1192059 (galisteo2023astepinto pages 13-14)
- Yoo Y, et al. **Insights into saline adaptation strategies… Halomonas…** *Frontiers in Marine Science*. **2023-07**. https://doi.org/10.3389/fmars.2023.1229444 (yoo2023insightsintosaline pages 3-5)


References

1. (benitezmateos2023halomonaselongataa pages 1-3): Ana I. Benítez-Mateos and Francesca Paradisi. Halomonas elongata: a microbial source of highly stable enzymes for applied biotechnology. Applied Microbiology and Biotechnology, 107:3183-3190, Apr 2023. URL: https://doi.org/10.1007/s00253-023-12510-7, doi:10.1007/s00253-023-12510-7. This article has 29 citations and is from a domain leading peer-reviewed journal.

2. (sharma2023genomeanalysisof pages 2-3): Anjney Sharma, Ram Nageena Singh, Xiu-Peng Song, Rajesh Kumar Singh, Dao-Jun Guo, Pratiksha Singh, Krishan K. Verma, and Yang-Rui Li. Genome analysis of a halophilic virgibacillus halodenitrificans ash15 revealed salt adaptation, plant growth promotion, and isoprenoid biosynthetic machinery. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1229955, doi:10.3389/fmicb.2023.1229955. This article has 25 citations and is from a peer-reviewed journal.

3. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

4. (galisteo2023astepinto pages 13-14): Cristina Galisteo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. A step into the rare biosphere: genomic features of the new genus terrihalobacillus and the new species aquibacillus salsiterrae from hypersaline soils. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1192059, doi:10.3389/fmicb.2023.1192059. This article has 12 citations and is from a peer-reviewed journal.

5. (zou2024metabolicengineeringof pages 2-4): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

6. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

7. (yoo2023insightsintosaline pages 3-5): Yeonjae Yoo, Hanbyul Lee, Junghyun Lee, Jong Seong Khim, and Jae-Jin Kim. Insights into saline adaptation strategies through a novel halophilic bacterium isolated from solar saltern of yellow sea. Frontiers in Marine Science, Jul 2023. URL: https://doi.org/10.3389/fmars.2023.1229444, doi:10.3389/fmars.2023.1229444. This article has 28 citations.

8. (shu2023metabolicengineeringof pages 6-6): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.

9. (shu2023metabolicengineeringof pages 6-10): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.

10. (benitezmateos2023halomonaselongataa media bc663ed1): Ana I. Benítez-Mateos and Francesca Paradisi. Halomonas elongata: a microbial source of highly stable enzymes for applied biotechnology. Applied Microbiology and Biotechnology, 107:3183-3190, Apr 2023. URL: https://doi.org/10.1007/s00253-023-12510-7, doi:10.1007/s00253-023-12510-7. This article has 29 citations and is from a domain leading peer-reviewed journal.