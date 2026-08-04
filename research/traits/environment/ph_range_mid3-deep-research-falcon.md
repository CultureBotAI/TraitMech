---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:58:26.816972'
end_time: '2026-08-04T03:06:36.862985'
duration_seconds: 490.05
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid3
  trait_identifier: METPO:1000463
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 8\u201310, characteristic of alkaliphile physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile,
    pHR_8_to_10
  evidence_summary: "DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review\
    \ supports alkaliphile physiology growing across pH 8\u201310.)"
  causal_graph_summary: 'ph_range_mid3_alkaliphile_range: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000463
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 8–10, characteristic of alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile, pHR_8_to_10
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile physiology growing across pH 8–10.)
- **Existing causal graph summary:** ph_range_mid3_alkaliphile_range: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **pH range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid3.yaml`.

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
- **Trait label:** pH range mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000463
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 8–10, characteristic of alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile, pHR_8_to_10
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile physiology growing across pH 8–10.)
- **Existing causal graph summary:** ph_range_mid3_alkaliphile_range: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **pH range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid3.yaml`.

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


# Curation report: microbial trait **pH range mid3**

## 1. Scope summary

**Target:** `"METPO:1000463"`  
**Parent:** `METPO:1000332`  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED

### Recommended interpretation

`"METPO:1000463"` should represent an **assay-observed capacity for microbial growth across an external-pH interval of approximately pH 8–10**. It is a range phenotype, not a molecular mechanism and not simply an optimum at pH 9. The mechanistic graph should therefore terminate in a node such as **growth supported across external pH 8–10**, with upstream processes explaining how cells preserve cytoplasmic pH, ion balance, membrane energetics, and ATP production.

The phenotype is consistent with alkaliphile physiology: alkaliphilic bacteria commonly grow well near pH 9, while more extreme model organisms extend beyond this class. For example, *Bacillus pseudofirmus* OF4 grows optimally around external pH 10.5 and can grow above pH 11; *Caldalkalibacillus thermarum* TA2.A1 grows from pH 7.5 to 11. These wider ranges overlap `"METPO:1000463"` but should not redefine its upper boundary. In *B. pseudofirmus*, cytoplasmic pH remains about 7.5 while external pH rises from 7.5 to 9.5, reaches approximately 8.3 at the pH 10.5 optimum, and rises to at least 9.5 only when external pH exceeds 11. This illustrates that the core physiological capacity is **maintaining a cytoplasm appreciably more acidic than the environment**. (krulwich2011molecularaspectsof pages 12-14, jong2023membraneproteomeof pages 1-2)

### Boundary cases

- **Include:** reproducible growth, biomass increase, colony formation, or sustained metabolic growth over approximately pH 8–10.
- **Do not equate with:** a single alkaline optimum, transient survival after alkaline shock, enzyme activity at alkaline pH, or environmental isolation from alkaline habitat without growth testing.
- **Alkali-tolerant versus obligately alkaliphilic:** both may display the range, but an alkali-tolerant organism can retain a neutral optimum, whereas an alkaliphile prefers alkaline conditions.
- **Extreme alkaliphiles:** growth extending to pH 11–13 is a neighboring, broader phenotype. Evidence obtained at pH 10.5 is mechanistically informative but slightly exceeds the nominal pH 8–10 endpoint and should be annotated accordingly.
- **Facultative acidophile:** this supplied synonym is potentially misleading. Acidophily concerns growth at low pH and is not equivalent to an alkaliphilic pH range; it should be reviewed before retention.
- **Salt and temperature:** haloalkaliphily and thermoalkaliphily are compound phenotypes. NaCl and temperature must be retained as assay modifiers rather than folded into `"METPO:1000463"` itself. The 2024 comparison of *B. aequororis* and *B. subtilis*, for example, found strong interactions among pH, NaCl, ATP content, and ΔpH. (maksimova2024metabolicandmorphological pages 9-10)

## 2. Current mechanistic model

The strongest current model is a coupled bioenergetic cycle:

1. Respiratory complexes export protons and establish membrane potential.
2. Electrogenic Na⁺/H⁺ antiport—especially MrpABCDEFG in alkaliphilic bacilli—uses that energetic state to import H⁺ while expelling Na⁺.
3. Na⁺ re-enters through Na⁺/solute symporters, MotPS and voltage-gated NavBP channels, sustaining antiporter cycling.
4. Acidic cell-surface components may retain protons near the membrane.
5. Specialized F₁F₀-ATP synthase captures scarce protons and produces ATP despite an outwardly unfavorable bulk ΔpH.
6. These processes preserve a relatively acidic cytoplasm, ion homeostasis, respiration, and growth across alkaline external pH. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 5-6)

This is not a universal single pathway. Recent chemostat proteomics shows that oxygen availability changes terminal-oxidase use and can reduce Mrp abundance, implying that the mechanism is conditional on respiratory state and carbon-product export. (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2)

## 3. Candidate nodes grouped by type

### A. Trait and physiological-process nodes

- `"METPO:1000463"` — pH range mid3 / growth-supporting external pH range approximately 8–10.
- Cytoplasmic pH homeostasis — candidate GO grounding; verify exact current GO term in the project resolver.
- Cellular ion homeostasis — candidate GO process.
- Na⁺/H⁺ antiport.
- Proton transmembrane transport.
- Sodium-ion transmembrane transport.
- Proton-motive force and membrane potential.
- Oxidative phosphorylation.
- ATP synthesis coupled to proton transport.
- Aerobic respiration.
- Sodium-dependent solute uptake.
- Flagellar motility and chemotaxis.
- Osmotic-stress adaptation.
- Growth at alkaline pH.

### B. Genes, proteins, transporters, and complexes

- **MrpABCDEFG multisubunit Na⁺/H⁺ antiporter**; individual nodes *mrpA–mrpG* where the evidence resolves subunit effects.
- **NhaA/NhaC-family Na⁺/H⁺ antiporters**; useful as broader alternatives but should not be asserted as universal alkaliphile determinants.
- **F₁F₀-ATP synthase**, including membrane a- and c-subunits and alkaliphile-associated `AxAxAxA` and `PxxExxP` motifs.
- **Respiratory Complex I**, alternative NADH dehydrogenase type II (**Ndh-2**), succinate dehydrogenase, cytochrome *bc₁* complex.
- Terminal oxidases: cytochrome *c*:oxygen **aa₃**, **ba₃**, **caa₃**, **bb₃**, and menaquinol:oxygen **bd** complexes. Presence and utilization are taxon- and oxygen-specific.
- **CtaD/CtaC** components of the caa₃ terminal oxidase.
- **BpOF4_01690**, a 59-amino-acid hydrophobic protein reported only among alkaliphiles in the studied comparison; retain as a label-only strain-specific node until a stable accession is resolved. (takahashi2018ahydrophobicsmall pages 1-2)
- **MotPS** flagellar Na⁺ channel and **NavBP** voltage-gated Na⁺ channel.
- Na⁺/solute symporters.
- Glycine-betaine and ectoine transporters.
- **NatABC** ATP-powered cation transporter and **TrkAH** low-affinity K⁺ uptake system.
- Candidate sodium:acetate exporter; this remains a proposed compensatory mechanism under oxygen limitation.

### C. Chemicals, metabolites, and environmental variables

- Proton/H⁺ — candidate `CHEBI:15378`.
- Sodium cation/Na⁺ — candidate `CHEBI:29101`.
- Potassium cation/K⁺, oxygen/O₂, ATP, ADP, phosphate, acetate, ectoine, and glycine betaine; resolve exact ChEBI CURIEs before YAML insertion.
- External pH, internal pH, ΔpH, NaCl concentration, dissolved oxygen, temperature, growth substrate, and buffer composition.
- Glucose and malate as assay carbon sources.
- Putative inhibitors/perturbations: proton-motive-force collapse, antiporter mutation/deletion, ATP-synthase mutation/deletion, respiratory-oxidase deletion, and insufficient Na⁺. These are experimental factors rather than constitutive graph nodes unless TraitMech models interventions.

### D. Cellular locations and structures

- Cytoplasmic/plasma membrane — candidate `GO:0005886`.
- Cytoplasm.
- Cell wall and S-layer.
- Membrane-localized respiratory chain.
- Membrane-localized F₁F₀-ATP synthase.
- Acidic secondary cell-wall polymers, including teichuronic-acid-like polymers and SlpA-associated surface architecture; retain label-only unless the exact polymer is experimentally identified.

### E. Organisms and assay contexts

- *Bacillus pseudofirmus* OF4 — principal causal-genetic model.
- *Bacillus halodurans* C-125 — *mrpA* genetic evidence.
- *Bacillus aequororis* 5-DB and *Bacillus subtilis* ATCC 6633 — 2024 comparative physiology.
- *Caldalkalibacillus thermarum* TA2.A1 — 2023 membrane proteome and 2024 oxygen-controlled chemostat evidence.

NCBITaxon CURIEs should be added only after strain/name resolution against the project’s preferred taxonomy release; none should be inferred from names alone.

## 4. Candidate causal edges

The following shortlist separates direct perturbational evidence from mechanistic synthesis and condition-dependent association.

| subject | predicate | object | evidence type/strength | taxon and assay context | DOI |
|---|---|---|---|---|---|
| MrpABCDEFG complex | mediates | Na+/H+ antiport required for alkaline pH homeostasis | **Strong causal**: gene deletion/mutational evidence; major antiporter in alkaliphilic Bacillus (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23, krulwich2011molecularaspectsof pages 20-22) | *Bacillus pseudofirmus* OF4 and *B. halodurans* C-125; loss of *mrp* subunits or *mrpA* function impairs alkaliphily/high-pH antiport | 10.1038/nrmicro2549 |
| Respiratory proton-pumping complexes | provide driving force for | Mrp-mediated proton uptake / alkaline pH homeostasis | **Moderate mechanistic**: expert synthesis from physiological/biochemical studies, not a single direct deletion chain (krulwich2011molecularaspectsof pages 27-28) | Alkaliphilic *B. pseudofirmus* OF4 model; review states active proton uptake by Mrp is supported by two proton-pumping respiratory complexes | 10.1038/nrmicro2549 |
| Na+/solute symporters, MotPS Na+ channel, NavBP Na+ channel | increase | cytoplasmic Na+ re-entry that supports Na+/H+ antiport cycling | **Moderate mechanistic**: physiological model plus channel/symporter evidence; partly review-level integration (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23, krulwich2011molecularaspectsof pages 27-28) | Alkaliphilic Bacillus systems; Na+ entry via solute uptake, motility channel, and voltage-gated channel proposed to sustain continuous Mrp activity | 10.1038/nrmicro2549 |
| F1Fo-ATP synthase (proton-coupled) | couples proton uptake to | ATP synthesis and contributes to pH homeostasis | **Moderate-strong mechanistic**: canonical bioenergetic role plus alkaliphile-focused analysis (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 5-6) | Alkaliphilic Bacillus; ATP synthase highlighted as aiding proton capture at high external pH | 10.1038/nrmicro2549 |
| Alkaliphile-specific ATP synthase a/c-subunit motifs | enables | oxidative phosphorylation and growth at pH 10.5 | **Strong causal**: motif replacement/mutational evidence causing defective growth/OXPHOS at pH 10.5 (krulwich2011molecularaspectsof pages 22-23) | *B. pseudofirmus* OF4; replacing alkaliphile-specific motifs with consensus residues impaired ATP synthesis-linked growth at high pH | 10.1038/nrmicro2549 |
| BpOF4_01690 | supports | respiratory/OXPHOS function needed for growth at pH 10.5, especially low Na+ | **Strong causal**: deletion phenotype with reduced respiratory activities and weaker high-pH growth (takahashi2018ahydrophobicsmall pages 12-13, takahashi2018ahydrophobicsmall pages 1-2, takahashi2018ahydrophobicsmall pages 9-12) | *B. pseudofirmus* OF4 Δ01690 in KGYE/KMYE at pH 10.5 and 5–400 mM NaCl; phenotype resembles Δ*ctaD* and Δ*atpB-F* mutants | 10.3389/fmicb.2018.01994 |
| Acidic secondary cell wall polymers / acidic surface proteins | promotes | proton retention / enhanced proton capture near cell surface | **Moderate mechanistic**: review synthesis; not direct perturbation in collected sources (krulwich2011molecularaspectsof pages 5-6) | Alkaliphilic Bacillus surface architecture; includes teichuronic-acid-like acidic polymers and low-pI surface components | 10.1038/nrmicro2549 |
| Lower oxygen level | alters abundance of | terminal oxidases (aa3 down, ba3 relatively favored) and lowers Mrp abundance | **Association / condition-response**: quantitative proteomics, not direct causal necessity for alkaliphily (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2) | *Caldalkalibacillus thermarum* TA2.A1 chemostats across 0.25%–4.2% O2; Mrp significantly downregulated under low O2 | 10.3389/fmicb.2024.1468929 |
| Glycine betaine and ectoine transporters | associated with | maintenance of near-neutral internal pH under highly alkaline conditions | **Association / plausible mechanism**: membrane proteomics plus author interpretation, not direct knockout evidence (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8) | *C. thermarum* TA2.A1 membrane proteome; transporters detected among 158 membrane proteins / 1,398 total proteins identified | 10.3389/fmicb.2023.1228266 |


*Table: This table summarizes the strongest candidate causal edges for curating METPO:1000463, separating direct deletion or mutational evidence from review-level mechanisms and proteomic associations. It is useful as a compact shortlist of graph edges that are most defensible for initial TraitMech curation.*

### Detailed evidence table

| # | Proposed subject–predicate–object triple | Evidence and supporting snippet | Curation note |
|---|---|---|---|
| 1 | **MrpABCDEFG complex — enables — Na⁺/H⁺ antiport** | The authoritative review identifies Mrp as the principal alkaliphilic-Bacillus antiporter; supporting excerpt: “**All seven Mrp proteins are required**” for complex formation/activity. Mutations in *B. halodurans* *mrpA* eliminate antiport and the alkaliphilic phenotype. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22) | **High confidence**, although the review summarizes older primary experiments. Taxon-contextualize to alkaliphilic Bacillus rather than all microbes. |
| 2 | **Mrp-mediated Na⁺/H⁺ antiport — promotes — cytoplasmic pH homeostasis at alkaline external pH** | “**Na⁺/H⁺ antiporters play the major role in pH homeostasis of alkaliphiles**.” In the 2024 physiology study, Na⁺ entry and exchange for H⁺ increased ΔpH; maximum ΔpH occurred at pH 11 with 50 g/L NaCl. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 9-10) | **High-to-moderate confidence**. Mechanism is strong, but the 2024 measurements are strain- and salt-dependent. |
| 3 | **Cytoplasmic pH homeostasis — enables — growth across external pH 8–10** | *B. pseudofirmus* keeps pHᵢ near 7.5 while pHₒ rises through 9.5 and has pHᵢ≈8.3 at pHₒ≈10.5; neutralophiles generally arrest near pHᵢ 8. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14) | **Core TraitMech edge**, but supported mainly by physiological correlation and expert synthesis rather than a single intervention. |
| 4 | **Respiratory proton-pumping complexes — energize — Mrp-dependent proton uptake** | Review model: active proton uptake by Mrp is supported by “**two proton-pumping respiratory complexes**.” DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 27-28) | **Moderate confidence**; curate as mechanistic synthesis, not as a universally demonstrated direct edge. |
| 5 | **Na⁺/solute symporters, MotPS, and NavBP — replenish — cytoplasmic Na⁺ available for antiport** | The review identifies Na⁺/solute symport, the flagellar MotPS channel, and voltage-gated NavBP as Na⁺ re-entry routes supporting antiport; NavBP also supports pH homeostasis, motility, and chemotaxis. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23, krulwich2011molecularaspectsof pages 27-28) | **Moderate confidence**. Consider separate edges for each route; avoid implying every alkaliphile contains all three. |
| 6 | **F₁F₀-ATP synthase proton uptake — contributes to — cytoplasmic pH homeostasis and ATP production** | Supporting synthesis: ATP synthase contributes through proton uptake during synthesis, and high-pH responses increase ATP synthase expression for proton capture. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6) | **Moderate confidence** for pH homeostasis; **high confidence** for proton-coupled ATP production. Direction must not be reversed into ATP hydrolysis unless the experiment demonstrates that mode. |
| 7 | **Alkaliphile-specific ATP-synthase a/c-subunit motifs — enable — oxidative phosphorylation and growth at pH 10.5** | Replacement of alkaliphile-associated motifs with consensus sequences caused defective oxidative phosphorylation and “**growth failure at pH 10.5**”; impairment was greater at pH 10.5 than 7.5. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23) | **High confidence, taxon-specific**. Motif sequences should be represented as labels unless exact residue coordinates and protein accessions are resolved. |
| 8 | **Acidic secondary cell-wall polymers/low-pI surface proteins — promote — proton retention near the membrane** | The review states that acidic secondary wall polymers, teichuronic acids, SlpA, and low-pI surface proteins contribute to proton capture. CtaC has reported pI 4.4 in *B. pseudofirmus* versus 8.6 in *B. subtilis*. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6) | **Uncertain-to-moderate**: plausible spatial mechanism, but the collected evidence lacks a clean polymer knockout→pH-range result. |
| 9 | **BpOF4_01690 — supports — respiratory-chain function under low-Na⁺ alkaline growth** | Δ01690 grew significantly more weakly in malate- and glucose-based media at pH 10.5 and low sodium; respiratory enzymatic activity was much lower. The protein is “**59 amino acids**” and hydrophobic. DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 12-13, takahashi2018ahydrophobicsmall pages 1-2) | **High confidence for phenotype**, taxon-specific. Do not generalize beyond organisms carrying a verified homolog. |
| 10 | **BpOF4_01690 — promotes — oxidative phosphorylation/proton transfer between respiration and ATP synthase** | Under pH 10.5 and 25 mM Na⁺, Δ01690 had reduced NADH oxidase, succinate dehydrogenase, TMPD oxidase, and ATPase activities; cytochrome *bc₁* and caa₃ expression fell to approximately 48–70% of wild type. Its phenotype resembled Δ*ctaD* and Δ*atpB–F*. DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 1-2, takahashi2018ahydrophobicsmall pages 9-12) | **Moderate confidence** for the exact proton-transfer mechanism: deletion evidence is causal, but mediation of proton transfer remains the authors’ interpretation. |
| 11 | **External Na⁺ concentration — modulates — alkaline growth and ΔpH** | Δ01690 was tested across 5–400 mM NaCl and was especially impaired at low Na⁺; the 2024 comparison found maximum ΔpH at pH 11 plus 50 g/L NaCl and reduced ATP at 50 versus 0.5 g/L NaCl. (maksimova2024metabolicandmorphological pages 9-10, takahashi2018ahydrophobicsmall pages 9-12) | **Assay-specific, non-monotonic**. Sodium is required for many antiport cycles but high salt imposes osmotic/energetic stress; do not encode a simple universal “Na⁺ increases growth” edge. |
| 12 | **External O₂ level — regulates — aa₃/ba₃ terminal-oxidase abundance** | In chemostats spanning 0.25–4.2% O₂, aa₃ abundance was highest at 4.2%, whereas ba₃ predominated at intermediate levels and declined below 0.42%; bb₃ and bd were not detected. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2) | **Strong condition-response association**, not proof that either oxidase causes the pH-range phenotype. |
| 13 | **Low O₂ — decreases abundance of — Mrp complex** | “**Mrp … was significantly downregulated under low oxygen conditions**.” The authors propose sodium:acetate export reduces the requirement for Mrp. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2) | Curate the measured regulation as **moderate confidence**; retain sodium:acetate compensation as **uncertain/hypothesized**. |
| 14 | **Glycine-betaine/ectoine transporters — may promote — internal-pH and osmotic homeostasis** | The 2023 proteome detected both transporter classes and interpreted the osmolytes as potentially assisting “**maintaining a near neutral internal pH**” under highly alkaline external conditions. DOI: [10.3389/fmicb.2023.1228266](https://doi.org/10.3389/fmicb.2023.1228266). (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8) | **Uncertain**: presence/abundance plus biological plausibility, without knockout or transport-flux evidence. |
| 15 | **Complete respiratory chain — supports — thermoalkaliphile growth** | The 2023 study detected a complete oxidative-phosphorylation pathway, Ndh-2, ba₃ oxidase, Mrp subunits, NatABC, and ATP synthase among 158 membrane proteins. DOI: [10.3389/fmicb.2023.1228266](https://doi.org/10.3389/fmicb.2023.1228266). (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8) | **Association only**. Split into component-presence edges; do not curate “causes pH 8–10 growth” without perturbation. |

## 5. Recent developments and quantitative evidence, 2023–2024

### Membrane proteomics, 2023

The *C. thermarum* TA2.A1 membrane-proteome study identified **1,398 proteins**, corresponding to **45.3%** of predicted proteins. Of these, **158** contained at least one transmembrane helix—**11.3%** of identified proteins and approximately **20.9%** coverage of the predicted membrane proteome. Detected machinery included Mrp subunits, NatABC, TrkAH, a complete oxidative-phosphorylation system, Ndh-2, ba₃ oxidase, ATP synthase, and ectoine/glycine-betaine transporters. The strain grows to 6% NaCl, but hydrophobicity, low abundance, undefined medium, and incomplete membrane coverage constrain causal interpretation. (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8)

### Oxygen-controlled proteomics, 2024

Chemostats across **0.25–4.2% O₂** showed constitutive type-I and type-II NADH dehydrogenases but oxygen-dependent terminal oxidases. aa₃ was most abundant at 4.2% O₂; ba₃ was favored over much of the lower range but declined below 0.42%. Mrp was significantly downregulated under low O₂. CopA increased approximately sixfold, while the Mnt manganese transporter decreased approximately sixfold. These findings revise the simple view that Mrp abundance should always remain high in an alkaliphile and instead support a conditional network governed by respiratory and carbon-export states. (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2)

### Comparative pH/salt physiology, 2024

*B. aequororis* 5-DB displayed broader pH and salt resistance than weakly alkali-resistant *B. subtilis* ATCC 6633, including tolerance to **50 g/L NaCl**. Cytoplasmic pH in *B. aequororis* reached approximately pH 9 after 48 hours, maximum measured ΔpH occurred at external pH 11 with 50 g/L NaCl, and ATP declined significantly at high salt. This study emphasizes that a measured alkaline pH range emerges from coupled pH and osmotic physiology rather than pH alone. (maksimova2024metabolicandmorphological pages 9-10)

## 6. Applications and real-world relevance

The trait itself has practical value because cells displaying it can remain metabolically active in alkaline processes. Established application areas include production of alkaline-stable extracellular enzymes, detergent and leather processing, alkaline waste treatment, bioremediation, bioleaching, and high-pH bioconversion. The most direct graph relevance, however, is that process conditions—pH, Na⁺, oxygen, substrate, and temperature—must be represented explicitly when selecting or engineering a production strain. The 2024 *B. aequororis* study specifically identifies broad pH and salt tolerance as useful for biotechnology, while the recent TA2.A1 work supplies a membrane-protein inventory for engineering respiratory and transport functions. (maksimova2024metabolicandmorphological pages 9-10, jong2023membraneproteomeof pages 1-2)

A cautious expert interpretation is that applications should be linked to **strain-level demonstrated performance**, not inferred solely from possession of *mrp* genes. Mrp is widespread and can support sodium resistance or moderately alkaline growth in non-alkaliphiles; conversely, oxygen-limited TA2.A1 reduces Mrp abundance while continuing growth. Thus, genomic presence is a candidate predictor, whereas growth-range assays and perturbation experiments remain the preferred evidence. (krulwich2011molecularaspectsof pages 5-6, jong2024quantitativeproteomicsreveals pages 6-8)

## 7. Recommended minimal graph for `ph_range_mid3.yaml`

A defensible first-pass graph could contain the following backbone:

1. External alkaline pH 8–10 → **increases challenge to** proton availability / cytoplasmic alkalinization.
2. Respiratory proton pumping → **generates** membrane electrochemical potential.
3. MrpABCDEFG → **enables** Na⁺/H⁺ antiport.
4. Na⁺/H⁺ antiport → **imports** H⁺ and **exports** Na⁺.
5. Na⁺/H⁺ antiport → **promotes** cytoplasmic pH homeostasis.
6. Na⁺/solute symporters and Na⁺ channels → **replenish** cytoplasmic Na⁺.
7. Acidic surface polymers → **may promote** near-membrane proton retention.
8. Alkaliphile-adapted F₁F₀-ATP synthase → **couples** proton uptake to ATP synthesis.
9. Cytoplasmic pH homeostasis + ATP production → **enable** growth across external pH approximately 8–10.
10. External Na⁺ and O₂ → **modulate** the transport/respiration branch.

For a conservative release, edges 3–5 and 8–9 should form the core. Surface proton retention, osmolyte-mediated internal-pH control, BpOF4_01690-mediated proton transfer, and sodium:acetate compensation should be placed in taxon-specific or uncertain extensions.

## 8. Warnings: claims not yet suitable for unqualified TraitMech curation

1. **Do not curate “all alkaliphiles use MrpABCDEFG.”** The strongest evidence concerns alkaliphilic Bacillus and selected taxa.
2. **Do not treat transporter detection as causality.** The 2023 proteome establishes presence, not necessity for the trait. (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8)
3. **Do not curate the sodium:acetate exporter as a proven Mrp replacement.** It is an author-proposed explanation for low-O₂ proteomics. (jong2024quantitativeproteomicsreveals pages 6-8)
4. **Do not state that bb₃ or bd operates below 0.25% O₂ in TA2.A1.** Neither complex was detected; operation was inferred as a possibility. (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2)
5. **Do not generalize BpOF4_01690.** Its deletion phenotype is compelling in *B. pseudofirmus* OF4, but homolog distribution and mechanism require validation. (takahashi2018ahydrophobicsmall pages 1-2, takahashi2018ahydrophobicsmall pages 9-12)
6. **Do not encode acidic wall polymers as proven universal proton reservoirs.** The collected evidence is predominantly review-level mechanistic synthesis. (krulwich2011molecularaspectsof pages 5-6)
7. **Do not encode sodium as monotonically beneficial.** Low Na⁺ can limit antiport, whereas high NaCl can lower ATP and impose osmotic stress. (maksimova2024metabolicandmorphological pages 9-10, takahashi2018ahydrophobicsmall pages 9-12)
8. **Do not treat pH 10.5 or 11 findings as exact measurements of the nominal 8–10 class.** They support the same mechanism but should carry an “upper-bound/extrapolative” annotation.
9. **Do not assign EC, UniProt, KEGG, Rhea, or strain NCBITaxon identifiers without resolver confirmation.** Label-only nodes are preferable to incorrect CURIEs.
10. **Review the synonym “Facultative acidophile.”** It is semantically discordant with the supplied alkaliphile definition.

## 9. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011; 9:330–343. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Authoritative mechanistic review and source of the existing evidence. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6)
2. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology*. Published January 2024. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 9-10)
3. de Jong SI, Wissink M, Yildirim K, et al. **Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology*. Published October 2024. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 6-8, jong2024quantitativeproteomicsreveals pages 1-2)
4. de Jong SI, Sorokin DY, van Loosdrecht MCM, Pabst M, McMillan DGG. **Membrane proteome of the thermoalkaliphile *Caldalkalibacillus thermarum* TA2.A1.** *Frontiers in Microbiology*. Published July 2023. DOI: [10.3389/fmicb.2023.1228266](https://doi.org/10.3389/fmicb.2023.1228266). (jong2023membraneproteomeof pages 1-2, jong2023membraneproteomeof pages 6-8)
5. Takahashi T, Krulwich TA, Ito M. **A Hydrophobic Small Protein, BpOF4_01690, Is Critical for Alkaliphily of Alkaliphilic *Bacillus pseudofirmus* OF4.** *Frontiers in Microbiology*. Published August 2018. DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 12-13, takahashi2018ahydrophobicsmall pages 1-2, takahashi2018ahydrophobicsmall pages 9-12)

**Overall curation assessment:** The most defensible causal core is **respiratory energization → Mrp Na⁺/H⁺ antiport → cytoplasmic pH homeostasis**, coupled to **alkaliphile-adapted F₁F₀-ATP synthesis → growth at alkaline external pH**. Recent 2023–2024 research chiefly adds conditional regulation, membrane-proteome coverage, and pH–salt–oxygen interactions; it does not overturn the foundational mechanism, but it shows that the graph must be condition- and taxon-aware.

References

1. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (jong2023membraneproteomeof pages 1-2): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

3. (maksimova2024metabolicandmorphological pages 9-10): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 22-23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

8. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

9. (takahashi2018ahydrophobicsmall pages 1-2): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

10. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

11. (takahashi2018ahydrophobicsmall pages 12-13): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

12. (takahashi2018ahydrophobicsmall pages 9-12): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

13. (jong2023membraneproteomeof pages 6-8): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.