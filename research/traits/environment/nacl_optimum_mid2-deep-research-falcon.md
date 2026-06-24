---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T13:17:15.538789'
end_time: '2026-06-18T13:26:34.986274'
duration_seconds: 559.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum mid2
  trait_identifier: METPO:1000467
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration approximately
    between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Moderate halophile, NaO_3_to_8
  evidence_summary: "DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation\
    \ review supports the 3\u20138% NaCl optimum range as the moderate-halophile category.)"
  causal_graph_summary: 'nacl_optimum_mid2_moderate_halophile: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum mid2
- **METPO identifier:** METPO:1000467
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Moderate halophile, NaO_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl optimum range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid2_moderate_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid2.yaml`.

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
- **Trait label:** NaCl optimum mid2
- **METPO identifier:** METPO:1000467
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration approximately between 3 and 8% (w/v), corresponding to moderate-halophile or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Moderate halophile, NaO_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl optimum range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_optimum_mid2_moderate_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_mid2.yaml`.

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


## Research Report: Microbial Trait “NaCl optimum mid2” (METPO:1000467)

### Scope summary (trait meaning and boundaries)
**NaCl optimum mid2** denotes a best-growth salinity **~3–8% (w/v) NaCl**, corresponding to a subset of the broader **moderate-halophile** category. Multiple recent sources operationalize **moderate halophiles** as organisms preferring **~3–15% NaCl**, distinguishing them from slight halophiles (≈1–3%) and extreme halophiles (≈15–25% or higher). This directly places the 3–8% optimum window within “moderate halophily,” while also overlapping with some **halotolerant** organisms that do not require salt but tolerate it. (benitezmateos2023halomonaselongataa pages 1-3, neagu2025novelhalotolerantbacteria pages 1-2)

Boundary cases important for curation:
- **Halotolerant vs moderate halophile:** halotolerant organisms can grow without NaCl but tolerate high NaCl; moderate halophiles often show improved growth at intermediate NaCl. Category thresholds are frequently reported as ranges rather than strict cutoffs (taxon- and assay-dependent). (neagu2025novelhalotolerantbacteria pages 1-2, benitezmateos2023halomonaselongataa pages 1-3)
- **Salt-out (compatible solutes) vs salt-in:** moderate halophilic bacteria frequently maintain relatively “non-hypersaline” cytoplasm and instead accumulate compatible solutes (salt-out), whereas many haloarchaea and extreme halophiles use “salt-in” (intracellular KCl) requiring global protein adaptation (acidic proteome). This mechanistic distinction matters because the same NaCl optimum class can arise via different physiological strategies in different taxa. (benitezmateos2023halomonaselongataa pages 1-3, borst2026studyingthelongterm pages 1-2, neagu2025novelhalotolerantbacteria pages 1-2)

### Key concepts and definitions (current understanding)
**1) Osmoadaptation strategies**
- **Compatible-solute (salt-out) strategy:** cells counter external osmotic pressure by accumulating **organic osmolytes** (compatible solutes) that do not disrupt macromolecular function. Compatible solutes cited across recent sources include **ectoine**, **glycine betaine**, and amino acids/derivatives such as **proline**. (neagu2025novelhalotolerantbacteria pages 1-2, coimbra2025establishinghalomonasas pages 1-2)
- **Salt-in strategy:** cells accumulate **inorganic ions (notably KCl)** to balance osmotic pressure, which requires broad proteome adaptations (e.g., acidic proteomes) to maintain protein solubility and function at high ionic strength. (borst2026studyingthelongterm pages 1-2)

**2) Moderate halophile definition relevant to NaCl optimum mid2**
Recent sources explicitly define moderate halophiles as requiring/prefering **~3–15% NaCl**, which includes the mid2 optimum range. (benitezmateos2023halomonaselongataa pages 1-3, neagu2025novelhalotolerantbacteria pages 1-2)

### Recent developments and latest research (prioritizing 2023–2024)
#### A. Gene–trait links for growth in the 3–8% NaCl window: ectoine (ectABC) as a causal mechanism
Work in *Halomonas elongata* (a model moderate halophile) demonstrates a direct link between NaCl thresholds and ectoine dependence:
- **NaCl >3% induces ectoine biosynthesis/accumulation**, while **ΔectABC mutants** are constrained to **≤3% NaCl**, supporting ectoine as a causal mechanism enabling growth above the lower boundary of NaCl optimum mid2. (zou2024metabolicengineeringof pages 1-2)

In *Halomonas campaniensis*, multi-omics evidence shows strong induction:
- **1.5 M NaCl** caused an approximately **20-fold** increase in ectoine production; the pathway is explicitly attributed to the conserved **ectA/ectB/ectC** cluster (with ectD producing hydroxyectoine). (qiao2024expressionofabc pages 1-2)

#### B. Alternative compatible solutes can substitute for ectoine (engineering evidence at 6–8% NaCl)
Two 2024 studies demonstrate that alternative osmolytes can restore salt tolerance in ectoine-deficient *H. elongata*:
- **Engineered proline biosynthesis** (replacement of ectoine operon plus **putA** deletion) enabled growth at **8% NaCl**, with intracellular proline reaching **353.1 ± 40.5 µmol/g cell fresh weight**; the ectoine-deficient comparator could not grow above **4% NaCl** in minimal medium. (khanh2024metabolicpathwayengineering pages 1-2)
- **Engineered GABA production** (via salt-inducible glutamate decarboxylase in a glutamate-overproducing background) enabled accumulation of **GABA to 176.94 µmol/g cell dry weight at 7% NaCl** and improved salt tolerance compared with ectoine-deficient backgrounds. (zou2024metabolicengineeringof pages 1-2)

These are important for TraitMech curation as **causal rescue experiments** supporting that “compatible-solute accumulation” is mechanistically upstream of growth at NaCl mid2.

#### C. Salt-stress-regulated ectoine production at ~6% NaCl and open/unsterile bioprocessing
A 2024 cell-factory study in *Halomonas cupida* J9 reports:
- **Transcriptomic upregulation** of the ectoine biosynthesis module under salt stress.
- **60 g/L NaCl (~6% w/v)** was reported as **optimal for growth** in their fermentation context.
- Engineering yielded **4.12 g/L ectoine** from xylose (60 h), and **unsterile** fermentation achieved **8.55 g/L ectoine** from a glucose–xylose mixture (and 1.30 g/L from corn straw hydrolysate). (chen2024elucidatingthesalttolerant pages 1-2)

This directly connects the trait’s salinity window to an economically relevant production regime.

### Current applications and real-world implementations
**1) Industrial biotechnology using moderate-halophile chassis**
Moderately halophilic *Halomonas* spp. are increasingly positioned as industrial chassis because growth at elevated salinity enables **open/unsterile cultivation** with reduced contamination risk and supports production of high-value osmolytes (ectoine) and other bioproducts. (chen2024elucidatingthesalttolerant pages 1-2)

**2) Ectoine as a high-value product**
Ectoine is widely used as a protective solute and has applications spanning cosmetics/healthcare and biotechnology; recent work emphasizes increasing titers while managing the challenges of high-salt fermentation. (benitezmateos2023halomonaselongataa pages 1-3, chen2024elucidatingthesalttolerant pages 1-2)

### Expert opinions and analysis from authoritative sources (within retrieved evidence)
- A 2023 mini-review frames *H. elongata* as attractive for biotechnology because, unlike extreme halophiles, its cytoplasm “does not present hypersalinity,” aligning with compatible-solute physiology that can be easier to engineer and to express enzymes heterologously. (benitezmateos2023halomonaselongataa pages 1-3)
- A 2025 review (supporting context for 2023–2024 work) synthesizes that Halomonas salt adaptation and production traits often involve ectoine metabolism and transporter-related responses under high salt; this is consistent with multi-omics signatures linking osmoprotection and transport to salinity adaptation. (coimbra2025establishinghalomonasas pages 1-2)

### Relevant statistics and data points (recent studies)
- **Moderate halophile definition:** ~**3–15% NaCl** (moderate) in categorization schemes; NaCl optimum mid2 (3–8%) is a subset. (neagu2025novelhalotolerantbacteria pages 1-2, benitezmateos2023halomonaselongataa pages 1-3)
- **Ectoine induction:** **~20-fold increase** with **1.5 M NaCl** in *H. campaniensis*. (qiao2024expressionofabc pages 1-2)
- **Growth dependence on ectoine pathway:** ΔectABC *H. elongata* restricted to **≤3% NaCl** (growth limit). (zou2024metabolicengineeringof pages 1-2)
- **Compatible-solute substitution:** engineered *H. elongata* grows at **8% NaCl** with **353.1 ± 40.5 µmol/g** intracellular proline. (khanh2024metabolicpathwayengineering pages 1-2)
- **Alternative osmolyte (GABA):** **176.94 µmol/g CDW** at **7% NaCl** in engineered *H. elongata*. (zou2024metabolicengineeringof pages 1-2)
- **Ectoine production at mid2 salinity:** *H. cupida* J9 optimal growth at **60 g/L NaCl (~6%)**; engineered strain produced **4.12 g/L ectoine** (xylose, 60 h) and **8.55 g/L ectoine** (unsterile, glucose–xylose mix). (chen2024elucidatingthesalttolerant pages 1-2)

---

## Candidate nodes for `nacl_optimum_mid2.yaml`

### A) Environmental / experimental factor nodes
- **NaCl concentration in growth medium** (CHEBI:26710)
- **Osmotic upshift (salt stress)** (label-only)
- **Osmotic down-shock** (label-only; ectoine secretion after down-shock was noted in *H. elongata*) (zou2024metabolicengineeringof pages 1-2)

### B) Chemicals / metabolites
- **Ectoine** (CHEBI:22563) (benitezmateos2023halomonaselongataa pages 1-3, qiao2024expressionofabc pages 1-2)
- **Glycine betaine** (CHEBI:17750) (neagu2025novelhalotolerantbacteria pages 1-2)
- **L-proline** (CHEBI:26271) (khanh2024metabolicpathwayengineering pages 1-2, neagu2025novelhalotolerantbacteria pages 1-2)
- **Potassium chloride (KCl)** (CHEBI:32588) (borst2026studyingthelongterm pages 1-2)
- **L-glutamate** (label-only grounding not resolved here) (zou2024metabolicengineeringof pages 1-2)
- **GABA (γ-aminobutyric acid)** (label-only grounding not resolved here) (zou2024metabolicengineeringof pages 1-2)

### C) Genes/proteins/complexes (label-only unless a stable ID is curated externally)
- **ectA / ectB / ectC operon (ectoine biosynthesis)** (qiao2024expressionofabc pages 1-2, zou2024metabolicengineeringof pages 1-2)
- **ectD (hydroxyectoine formation)** (qiao2024expressionofabc pages 1-2)
- **putA (proline catabolism; PRODH/P5CDH)** (khanh2024metabolicpathwayengineering pages 1-2)
- **proB / proA / proC (proline biosynthesis enzymes)** (khanh2024metabolicpathwayengineering pages 1-2)
- **glutamate decarboxylase (GAD)** (zou2024metabolicengineeringof pages 1-2)
- **ABC transport complex / ABC transporters (GO-level)** (qiao2024expressionofabc pages 1-2)

### D) Biological processes / strategies
- **Compatible-solute strategy (salt-out)** (label-only) (neagu2025novelhalotolerantbacteria pages 1-2, borst2026studyingthelongterm pages 1-2)
- **Salt-in strategy** (label-only) (borst2026studyingthelongterm pages 1-2)
- **Acidic proteome adaptation** (label-only) (borst2026studyingthelongterm pages 1-2)

---

## Candidate causal edges (evidence-backed)
The following table is designed to be directly curatable as TraitMech-style triples.

| Edge (subject–predicate–object) | Mechanistic interpretation (1 sentence) | Evidence snippet (quoted) | Source (with DOI URL and publication month/year) | Curation notes/uncertainty | Suggested ontology grounding (CURIEs where possible; otherwise label-only) |
|---|---|---|---|---|---|
| increased external NaCl → induces → ectoine biosynthesis module (ectA/ectB/ectC) in *Halomonas* | In moderate halophiles, elevated salinity triggers the canonical ectoine pathway to raise intracellular compatible-solute pools. | “The excerpt links NaCl concentration to specific osmoadaptation mechanisms in *Halomonas elongata*. Mechanistically, exposure to salt concentrations higher than 3% NaCl triggers biosynthesis and intracellular accumulation of ectoine as a major compatible solute” (zou2024metabolicengineeringof pages 1-2) | Zou et al., *Applied and Environmental Microbiology*, Jan 2024. DOI: https://doi.org/10.1128/aem.01905-23 | Strong for *H. elongata*; taxon-specific but likely generalizable across many moderate halophilic *Halomonas*. | CHEBI:26710 NaCl; label-only: ectoine biosynthesis module; KEGG: ectA/ectB/ectC; CHEBI:22563 ectoine; NCBITaxon:2745 *Halomonas* |
| deletion of ectABC → reduces growth above ∼3% NaCl → ectoine-deficient *H. elongata* | Loss of the core ectoine pathway lowers salt tolerance, implying ectoine causally supports growth in the mid-salinity range. | “Loss of ectoine biosynthesis (ΔectABC; strain KA1) restricts growth to media containing up to 3% NaCl, showing ectABC importance for tolerance above that” (zou2024metabolicengineeringof pages 1-2) | Zou et al., *Applied and Environmental Microbiology*, Jan 2024. DOI: https://doi.org/10.1128/aem.01905-23 | Strong but mutant-based; should be curated as gene-pathway evidence rather than universal species trait. | label-only: ectABC operon; CHEBI:26710 NaCl; CHEBI:22563 ectoine; NCBITaxon:2745 *Halomonas elongata* |
| engineered proline biosynthesis cluster + putA deletion → restores growth at 8% NaCl → ectoine-deficient *H. elongata* | Proline can functionally substitute for ectoine as a compatible solute when biosynthesis/catabolism are engineered appropriately. | “This engineered strain grows at 8% NaCl (where an Ect-deficient KA1 could not grow above 4% NaCl) and accumulates Pro to 353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh et al., *Applied and Environmental Microbiology*, Sep 2024. DOI: https://doi.org/10.1128/aem.01195-24 | Strong for engineered strain; not native mechanism, so mark as engineered/assay-specific rescue evidence. | CHEBI:26271 L-proline; label-only: proBm1AC cluster; label-only: putA; CHEBI:26710 NaCl; NCBITaxon:2745 *Halomonas elongata* |
| 1.5 M NaCl → increases → ectoine production (~20-fold) in *H. campaniensis* | Salt induction quantitatively upregulates ectoine accumulation in another *Halomonas* species, supporting a broader causal pattern. | “NaCl induction resulted in a 20-fold increase,” and “The core biosynthetic operon is ‘the highly conserved gene cluster operons ectA, B, and C’” (qiao2024expressionofabc pages 1-2) | Qiao et al., *BMC Genomics*, Nov 2024. DOI: https://doi.org/10.1186/s12864-024-11003-9 | Strong induction evidence; culture used 1.5 M NaCl (~8.8% w/v), slightly above the target upper bound but still close boundary-relevant evidence. | CHEBI:26710 NaCl; label-only: ectABC operon; CHEBI:22563 ectoine; NCBITaxon:2745 *Halomonas campaniensis* |
| salt stress / 60 g/L NaCl (∼6% w/v) → upregulates → ectoine biosynthesis module in *H. cupida* J9 | The target salinity window directly overlaps with an experimentally optimal growth condition where ectoine-module expression is enhanced. | “Transcriptomics showed the ectoine biosynthesis module is upregulated under salt stress” and “a fermentation medium salt concentration of 60 g/L NaCl (≈6% w/v) was optimal for *H. cupida* J9 growth” (chen2024elucidatingthesalttolerant pages 1-2) | Chen et al., *Microbial Cell Factories*, Aug 2024. DOI: https://doi.org/10.1186/s12934-024-02515-w | Very relevant to NaCl mid2 because 60 g/L falls inside 3–8% w/v; gene names not explicit in excerpt, so module-level curation may be safer than ectABC-specific edge unless full text is checked. | CHEBI:26710 NaCl; label-only: ectoine biosynthesis module; CHEBI:22563 ectoine; NCBITaxon:2745 *Halomonas cupida* J9 |
| salt-in strategy → involves → intracellular KCl accumulation | Salt-in osmoadaptation maintains osmotic balance by using inorganic ions rather than organic solutes. | “the archaeal ‘salt-in strategy,’ characterized by accumulation of KCl to balance external NaCl and generate internal KCl gradients” (borst2026studyingthelongterm pages 1-2) | Borst & Soppa, *Frontiers in Microbiology*, Jan 2026. DOI: https://doi.org/10.3389/fmicb.2025.1697018 | General mechanistic background; mostly relevant as a boundary case because many moderate halophilic bacteria instead use compatible solutes. | CHEBI:26710 NaCl; CHEBI:32588 potassium chloride; GO:0006813 potassium ion transport?; label-only: salt-in strategy |
| salt-in strategy → requires → acidic proteome / salt-adapted proteins | High intracellular KCl selects for proteomes enriched in acidic residues to preserve protein solubility and activity. | “The excerpt notes functional consequences: haloarchaeal proteins require high salt for stability, can denature at low salt, and have very acidic proteomes (pI 4–5) to maintain solubility and function in high-salt cytoplasm” (borst2026studyingthelongterm pages 1-2) | Borst & Soppa, *Frontiers in Microbiology*, Jan 2026. DOI: https://doi.org/10.3389/fmicb.2025.1697018 | Boundary/background evidence rather than direct NaCl mid2 mechanism; better kept as contrast node/edge to avoid overgeneralizing to moderate halophiles. | label-only: acidic proteome; label-only: salt-adapted protein stability; label-only: salt-in strategy |
| compatible-solute strategy → uses → ectoine / glycine betaine / proline | Moderate halophiles and halotolerant microbes often buffer osmotic stress with organic solutes rather than high intracellular salt. | “Two principal osmoadaptation strategies are described… (2) the compatible-solute strategy — accumulation of small organic osmolytes. Identified compatible solutes include… glycine, betaine, and ectoine” (neagu2025novelhalotolerantbacteria pages 1-2); “Many species naturally produce the osmolyte ectoine (plus hydroxyectoine, betaine, glycine, proline)” (coimbra2025establishinghalomonasas pages 1-2) | Neagu & Stancu, *BioTech*, Jun 2025. DOI: https://doi.org/10.3390/biotech14020049; Coimbra et al., *Microbial Cell Factories*, Jun 2025. DOI: https://doi.org/10.1186/s12934-025-02757-2 | Good high-level trait mechanism; broad and not pathway-specific. Useful as a parent edge linking trait to osmoadaptation class. | label-only: compatible-solute strategy; CHEBI:22563 ectoine; CHEBI:17750 glycine betaine; CHEBI:26271 L-proline |
| medium K+ limitation → shifts osmoprotectant use to → glycine betaine in *Halorhodospira halophila* | Osmoadaptation can switch between inorganic-ion and compatible-solute modes depending on medium chemistry, cautioning against overly rigid trait graphs. | “When grown in hypersaline media containing substantial K+ concentrations, *H. halophila* accumulates molar concentrations of KCl. However, at limiting K+ concentrations the organism switches to glycine betaine as its major osmoprotectant” () | Deole & Hoff, *Scientific Reports*, Feb 2020. DOI: https://doi.org/10.1038/s41598-020-59231-9 | Important boundary case but from an extreme halophile, not a canonical NaCl mid2 organism; mark as non-core comparative evidence only. | CHEBI:32588 potassium chloride; CHEBI:17750 glycine betaine; label-only: osmoprotectant switching; NCBITaxon:label-only *Halorhodospira halophila* |


*Table: This table summarizes candidate subject–predicate–object edges for curating the NaCl optimum mid2 trait, emphasizing mechanistic evidence around ectoine, proline, compatible solutes, and boundary-case salt-in strategies. It is useful as a first-pass TraitMech edge set with explicit snippets, uncertainty notes, and ontology-grounding suggestions.*

---

## Warnings / curation cautions (do not over-curate yet)
1. **Percent w/v vs molar NaCl units:** some studies report NaCl in molar units (e.g., 1.5 M) which corresponds to ~8.8% w/v; this is near the upper edge of NaCl optimum mid2 but not exactly in the 3–8% window. Curate unit conversions explicitly or annotate as “near-boundary.” (qiao2024expressionofabc pages 1-2)
2. **Engineering vs native mechanism:** proline- and GABA-based rescue of ectoine-deficient strains are strong causal evidence for “compatible solute accumulation → salt tolerance,” but they are **engineered** and should be marked accordingly rather than treated as universal wild-type mechanisms. (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2)
3. **Salt-in strategy evidence is mostly archaeal/extreme-halophile context in this evidence set:** include as contrast/boundary nodes, but avoid asserting salt-in as a mid2 hallmark unless additional mid2-specific taxa evidence is added. (borst2026studyingthelongterm pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)
- Benítez-Mateos AI, Paradisi F. **Halomonas elongata: a microbial source of highly stable enzymes for applied biotechnology.** *Applied Microbiology and Biotechnology.* **Apr 2023**. DOI: **10.1007/s00253-023-12510-7**. https://doi.org/10.1007/s00253-023-12510-7 (benitezmateos2023halomonaselongataa pages 1-3)
- Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H. **Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology.* **Jan 2024**. DOI: **10.1128/aem.01905-23**. https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)
- Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology.* **Sep 2024**. DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)
- Chen Y, Liu Y, Meng Y, et al. **Elucidating the salt-tolerant mechanism of Halomonas cupida J9 and unsterile ectoine production from lignocellulosic biomass.** *Microbial Cell Factories.* **Aug 2024**. DOI: **10.1186/s12934-024-02515-w**. https://doi.org/10.1186/s12934-024-02515-w (chen2024elucidatingthesalttolerant pages 1-2)
- Qiao L, Shen G, Han R, et al. **Expression of ABC transporters negatively correlates with ectoine biosynthesis in Halomonas campaniensis under NaCl and ultraviolet mutagenesis treatments revealed by transcriptomic and proteomics combined analysis.** *BMC Genomics.* **Nov 2024**. DOI: **10.1186/s12864-024-11003-9**. https://doi.org/10.1186/s12864-024-11003-9 (qiao2024expressionofabc pages 1-2)
- Neagu S, Stancu MM. **Novel Halotolerant Bacteria from Saline Environments: Isolation and Biomolecule Production.** *BioTech.* **Jun 2025**. DOI: **10.3390/biotech14020049**. https://doi.org/10.3390/biotech14020049 (neagu2025novelhalotolerantbacteria pages 1-2)
- Borst A, Soppa J. **Studying the long-term adaptation of Haloferax volcanii to low salt conditions: transcriptomic and genetic analyses.** *Frontiers in Microbiology.* **Jan 2026**. DOI: **10.3389/fmicb.2025.1697018**. https://doi.org/10.3389/fmicb.2025.1697018 (borst2026studyingthelongterm pages 1-2)
- Coimbra AAB, Prakash S, Jiménez JI, Rios-Solis L. **Establishing Halomonas as a chassis for industrial biotechnology: advances in synthetic biology tool development and metabolic engineering strategies.** *Microbial Cell Factories.* **Jun 2025**. DOI: **10.1186/s12934-025-02757-2**. https://doi.org/10.1186/s12934-025-02757-2 (coimbra2025establishinghalomonasas pages 1-2)


References

1. (benitezmateos2023halomonaselongataa pages 1-3): Ana I. Benítez-Mateos and Francesca Paradisi. Halomonas elongata: a microbial source of highly stable enzymes for applied biotechnology. Applied Microbiology and Biotechnology, 107:3183-3190, Apr 2023. URL: https://doi.org/10.1007/s00253-023-12510-7, doi:10.1007/s00253-023-12510-7. This article has 29 citations and is from a domain leading peer-reviewed journal.

2. (neagu2025novelhalotolerantbacteria pages 1-2): Simona Neagu and Mihaela Marilena Stancu. Novel halotolerant bacteria from saline environments: isolation and biomolecule production. BioTech, 14:49, Jun 2025. URL: https://doi.org/10.3390/biotech14020049, doi:10.3390/biotech14020049. This article has 12 citations.

3. (borst2026studyingthelongterm pages 1-2): Andreas Borst and Jörg Soppa. Studying the long-term adaptation of haloferax volcanii to low salt conditions: transcriptomic and genetic analyses. Frontiers in Microbiology, Jan 2026. URL: https://doi.org/10.3389/fmicb.2025.1697018, doi:10.3389/fmicb.2025.1697018. This article has 1 citations and is from a peer-reviewed journal.

4. (coimbra2025establishinghalomonasas pages 1-2): André A. B. Coimbra, Satya Prakash, José I. Jiménez, and Leonardo Rios-Solis. Establishing halomonas as a chassis for industrial biotechnology: advances in synthetic biology tool development and metabolic engineering strategies. Microbial Cell Factories, Jun 2025. URL: https://doi.org/10.1186/s12934-025-02757-2, doi:10.1186/s12934-025-02757-2. This article has 13 citations and is from a peer-reviewed journal.

5. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

6. (qiao2024expressionofabc pages 1-2): Lijuan Qiao, Guoping Shen, Rui Han, Rong Wang, Xiang Gao, Jiangwa Xing, Yanbing Lin, and Derui Zhu. Expression of abc transporters negatively correlates with ectoine biosynthesis in halomonas campaniensis under nacl and ultraviolet mutagenesis treatments revealed by transcriptomic and proteomics combined analysis. BMC Genomics, Nov 2024. URL: https://doi.org/10.1186/s12864-024-11003-9, doi:10.1186/s12864-024-11003-9. This article has 1 citations and is from a peer-reviewed journal.

7. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

8. (chen2024elucidatingthesalttolerant pages 1-2): Yaping Chen, Yujie Liu, Yan Meng, Yuting Jiang, Weini Xiong, Shufang Wang, Chao Yang, and Ruihua Liu. Elucidating the salt-tolerant mechanism of halomonas cupida j9 and unsterile ectoine production from lignocellulosic biomass. Microbial Cell Factories, Aug 2024. URL: https://doi.org/10.1186/s12934-024-02515-w, doi:10.1186/s12934-024-02515-w. This article has 16 citations and is from a peer-reviewed journal.