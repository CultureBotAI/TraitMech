---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:53:37.954523'
end_time: '2026-08-04T14:59:40.959175'
duration_seconds: 363.0
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum mid2
  trait_identifier: METPO:1000457
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH between approximately
    7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
  evidence_summary: "DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review\
    \ supports the 7\u20138 external-pH range as the common neutrophile / moderately\
    \ alkaline-tolerant optimum.)"
  causal_graph_summary: 'ph_optimum_mid2_alkaline_tolerant_setpoint: 12 nodes, 9 edges'
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
- **Trait label:** pH optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000457
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the 7–8 external-pH range as the common neutrophile / moderately alkaline-tolerant optimum.)
- **Existing causal graph summary:** ph_optimum_mid2_alkaline_tolerant_setpoint: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **pH optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid2.yaml`.

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
- **Trait label:** pH optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000457
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the 7–8 external-pH range as the common neutrophile / moderately alkaline-tolerant optimum.)
- **Existing causal graph summary:** ph_optimum_mid2_alkaline_tolerant_setpoint: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **pH optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid2.yaml`.

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


# Curation report: microbial **pH optimum mid2**

## 1. Scope summary

**Target:** “pH optimum mid2”  
**Identifier:** `METPO:1000457`  
**Category/kind/status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** `METPO:1000331`

This trait should denote an **assay-observed external-pH optimum**: the pH, or narrow pH interval, at which a microbial strain exhibits its best measured growth, with the optimum falling approximately between **pH 7 and 8**. It is therefore an organism-level environmental preference, not a molecular activity.

The trait must be distinguished from:

1. **Cytoplasmic pH.** Neutralophilic bacteria may grow over approximately pH 5.5–9.0 while maintaining cytoplasmic pH near 7.5–7.7. A cytoplasmic value in this interval does not establish an external growth optimum of 7–8. (krulwich2011molecularaspectsof pages 1-3)
2. **Growth range.** Growth at pH 7–8 is insufficient if maximal growth occurs elsewhere. In a 2023 isolate study, Paeni-Cedars grew over pH 7–10 but had a reported optimum around pH 9; it therefore should not be assigned `METPO:1000457` merely because it grows at pH 7–8. Ali-BS5-314 had an optimum at pH 11 and range pH 10–12, clearly representing alkaliphily outside this class. (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe pages 3-4)
3. **Alkali tolerance or survival.** Survival after an alkaline challenge, maintenance of ATP, or maintenance of ΔpH is a stress-resistance phenotype, not necessarily an optimum.
4. **Extreme alkaliphily.** Mechanisms established at pH 10–12 can provide plausible upstream nodes, but cannot by themselves establish a best-growth setpoint at pH 7–8.
5. **Assay-dependent apparent optima.** Medium composition, buffer, sodium concentration, oxygen, temperature, carbon source, growth phase, and the pH sampling grid can shift the observed optimum. If a study reports “pH 7–9” as equally optimal, the value overlaps but does not unambiguously resolve the 7–8 bin.

A practical curation rule is to require an explicitly reported optimum within 7–8, or quantitative growth measurements showing the maximum in that interval under stated conditions. A broad-range or endpoint survival measurement should be represented separately.

## 2. Current mechanistic understanding

The core explanatory process is **cytoplasmic pH homeostasis**. Rising external pH lowers proton availability and can reverse or diminish the favorable ΔpH component of proton motive force. Cells compensate through coordinated ion antiport, respiratory-chain regulation, ATP synthase activity, membrane potential, and cell-envelope proton retention. Proton motive force comprises both ΔpH and electrical potential, so external pH cannot be interpreted independently of ion gradients and membrane energetics. (krulwich2011molecularaspectsof pages 1-3)

At alkaline pH in *Escherichia coli*, NhaA carries out electrogenic Na⁺/H⁺ exchange with a reported 2 H⁺:1 Na⁺ stoichiometry, permitting proton entry driven by membrane potential. NhaA loss compromises high-pH growth in the presence of sodium, providing direct gene-level support for an antiporter-to-homeostasis edge. Under sodium-poor conditions, K⁺/H⁺ exchange can become more important. (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 5-6)

In aerobic alkaliphilic *Bacillus*, the multisubunit Mrp Na⁺/H⁺ antiporter is especially important. A point mutation in *mrpA* in *Bacillus halodurans* C-125 caused loss of alkaline pH homeostasis and of the alkaliphilic phenotype. ATP-synthase subunit mutations likewise reduced activity and correlated with failure of pH homeostasis during alkaline shifts. These are strong causal observations, but their direct evidence concerns stronger alkaliphily rather than a 7–8 optimum. (krulwich2011molecularaspectsof pages 12-14)

Cell-envelope architecture can create a proton-retaining surface microenvironment. Acidic wall polymers and low-isoelectric-point surface proteins have been proposed to concentrate protons near the membrane. Deleting the S-layer protein *slpA* from *Bacillus pseudofirmus* OF4 reduced adaptation after a shift from pH 7.5 to 11, supporting the envelope-to-alkaline-adaptation link in that organism. (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 5-6)

Respiration is an important context variable. In *Caldalkalibacillus thermarum* TA2.A1 chemostats spanning 0.25–4.2% O₂, type I and II NADH dehydrogenases were constitutive, terminal oxidase abundance varied with oxygen, and Mrp abundance decreased under lower oxygen. Thus, oxygen supply can alter the expression of pH-homeostasis machinery; the result is proteomic association, not proof that oxygen determines the pH optimum. (jong2024quantitativeproteomicsreveals pages 1-2)

## 3. Candidate nodes

### Trait and environmental nodes

- **pH optimum mid2:** `METPO:1000457`
- **Parent pH-optimum trait:** `METPO:1000331`
- External pH 7–8 — label-only unless the project has a validated pH-quality representation
- Alkaline pH challenge — label-only
- Sodium concentration
- Potassium concentration
- Oxygen concentration
- Temperature
- Medium buffering capacity
- Growth medium composition
- Growth rate / biomass yield / lag time — assay-output nodes

### Chemicals and energetic quantities

- Proton: `CHEBI:15378`
- Sodium ion: `CHEBI:29101`
- Potassium ion: `CHEBI:29103`
- Oxygen: `CHEBI:15379`
- ATP: `CHEBI:15422`
- Proton motive force — label-only candidate
- Transmembrane pH gradient, ΔpH — label-only candidate
- Membrane potential, Δψ — label-only candidate

The CHEBI identifiers above are standard candidates, but should still be validated against the ontology release used by TraitMech before committing the YAML.

### Genes, proteins, and complexes

- NhaA Na⁺/H⁺ antiporter — label-only generic node; use a taxon-specific UniProt accession only when the strain/protein is explicit
- Mrp/Mnh multisubunit Na⁺/H⁺ antiporter complex
- *mrpA* antiporter subunit
- K⁺/H⁺ antiporter
- F-type H⁺-transporting ATP synthase complex
- Proton-pumping respiratory-chain complexes
- Type I NADH dehydrogenase
- Type II NADH dehydrogenase
- Cytochrome *aa*3 oxidase
- Cytochrome *ba*3 oxidase
- SlpA S-layer protein

### Cellular structures and processes

- Cytoplasmic membrane
- Cell wall / S-layer
- Acidic cell-wall polymers
- Cytoplasmic pH homeostasis
- Sodium-ion homeostasis
- Potassium-ion homeostasis
- Proton transmembrane transport
- Oxidative phosphorylation
- Aerobic respiration
- Proton retention at the cell surface
- Growth under external pH 7–8

Useful GO candidates to validate during implementation include **ATP synthesis coupled proton transport**, **proton transmembrane transport**, **cellular pH reduction**, **sodium ion transport**, and **plasma membrane**. Exact GO CURIEs are deliberately not supplied here because the retrieved evidence did not verify current identifiers; label-only nodes are preferable to invented or obsolete mappings.

### Taxon/context nodes

- *Escherichia coli* — `NCBITaxon:562`
- *Bacillus halodurans* C-125 — use a verified strain-level NCBITaxon record if available
- *Bacillus pseudofirmus* OF4 — use a verified strain-level record if available
- *Caldalkalibacillus thermarum* TA2.A1 — verify current accepted taxonomy and NCBITaxon identifier
- *Bacillus aequororis* 5-DB
- Paeni-Cedars and Ali-BS5-314 isolate contexts

## 4. Candidate causal edges

The following evidence-tagged triples are proposed as a starting point. They should not all be connected directly to the trait endpoint.

| subject | predicate | object | evidence level | taxon/context | DOI | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| External pH 7–8 | reduces | inward proton availability relative to acidic conditions | inferred, foundational/general | general bacterial physiology | 10.1038/nrmicro2549 | “The pH difference across the membrane and the total proton concentration in the external milieu both decrease as the external pH rises” (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6) | Useful environmental driver node, but this is a physicochemical inference rather than a direct mutant-tested edge for the trait endpoint. |
| Na+/H+ antiporter NhaA | positively regulates | cytoplasmic pH homeostasis | foundational/general with strong gene-specific evidence | *Escherichia coli* under alkaline pH with Na+ present | 10.1038/nrmicro2549 | “NhaA is essential for adaptation of the enteric pathogen E. coli to alkaline pH in the presence of Na+” (krulwich2011molecularaspectsof pages 6-8) | Good mechanistic node; likely taxon-portable as a class of antiporters, but direct curation should avoid assuming NhaA itself is universal for all pH 7–8 organisms. |
| Mrp Na+/H+ antiporter complex | positively regulates | alkaline pH homeostasis | mutant-supported | alkaliphilic *Bacillus* spp. | 10.1038/nrmicro2549 | “a point mutation in the mrpA gene of B. halodurans C-125 causes loss of alkaliphile phenotype and alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | Strong causal evidence, but primarily from extreme alkaliphiles; curate as taxon/context-specific support, not as a universal determinant of METPO:1000457. |
| Proton-pumping respiratory chain | positively regulates | proton motive force (PMF) | foundational/general | general bacteria | 10.1038/nrmicro2549 | “primary pumps… include respiratory chain proton pumps” and PMF comprises ΔpH and Δψ (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6) | Strong background mechanism for pH homeostasis; broad and suitable as upstream process node. |
| Alkaline stress | decreases expression of | respiratory proton-pumping complexes | foundational/general, expression-level | *E. coli* alkaline adaptation | 10.1038/nrmicro2549 | “Under alkaline stress, E. coli decreases expression of proton-pumping respiratory complexes” (krulwich2011molecularaspectsof pages 5-6) | Expression association in one taxon; should be flagged as taxon-specific regulatory strategy, not a universal edge. |
| Alkaline stress | increases expression of | F1Fo ATP synthase / proton capture | foundational/general, expression-level | *E. coli* alkaline adaptation | 10.1038/nrmicro2549 | “while increasing F1Fo ATP synthase expression to enhance proton capture” (krulwich2011molecularaspectsof pages 5-6) | Candidate adaptive edge; do not overgeneralize beyond taxa/settings without further support. |
| K+/H+ antiport | supports | pH homeostasis under Na-poor conditions | foundational/general | bacteria in Na-poor alkaline conditions | 10.1038/nrmicro2549 | “K+/H+ antiporters assume dominance under Na+-poor conditions” (krulwich2011molecularaspectsof pages 5-6) | Good conditional edge with explicit environmental qualifier; likely better encoded with context on low sodium. |
| Acidic cell-surface polymers / SlpA | positively regulates | proton retention and alkaline adaptation | mutant-supported, taxon-specific | alkaliphilic *Bacillus pseudofirmus* OF4 | 10.1038/nrmicro2549 | “Deletion of slpA from B. pseudofirmus OF4 demonstrates reduced adaptation ability following pH shifts from 7.5 to 11” (krulwich2011molecularaspectsof pages 6-8) | Strong for this alkaliphile; likely not a direct determinant of a neutral-to-mildly alkaline optimum and should be marked context-specific. |
| Oxygen limitation | downregulates | Mrp Na+/H+ antiporter complex | proteomic association, taxon-specific | *Caldalkalibacillus thermarum* TA2.A1 chemostat, 0.25–4.2% O2 | 10.3389/fmicb.2024.1468929 | “the sodium-proton antiporter complex Mrp was downregulated under the lower oxygen levels” (jong2024quantitativeproteomicsreveals pages 1-2) | Useful context edge linking respiration state to pH-homeostasis machinery; association only, not direct proof of trait causation. |
| pH homeostasis | enables | best growth at external pH 7–8 | inferred trait-link, do not directly encode endpoint | general neutrophile/moderately alkalitolerant physiology | 10.1038/nrmicro2549 | Neutralophiles “grow over the range of approximately pH 5.5 to 9.0” while maintaining cytoplasmic pH “between pH 7.5 and 7.7” (krulwich2011molecularaspectsof pages 1-3) | Conceptually central, but this is a high-level explanatory edge from review synthesis; avoid curating as a single direct endpoint edge without organism-level assay support. |


*Table: This table compiles compact, evidence-tagged causal triples relevant to microbial optimal growth at external pH 7–8. It highlights which edges are foundational, mutant-supported, taxon-specific, proteomic, or inferred so curators can separate robust mechanism nodes from trait-endpoint overreach.*

### Recommended minimal graph architecture

A conservative TraitMech graph could use the following chain:

1. **External pH 7–8** → *decreases relative extracellular proton availability* → **proton availability near the membrane**.
2. **NhaA or Mrp Na⁺/H⁺ antiport** → *increases* → **proton influx / cytoplasmic pH homeostasis**.
3. **F-type ATP synthase and respiratory-chain regulation** → *modulate* → **proton motive force and proton capture**.
4. **Acidic cell-surface polymers** → *increase* → **local proton retention**.
5. **Cytoplasmic pH homeostasis plus adequate PMF** → *supports* → **growth at external pH 7–8**.
6. **Growth measurements showing a maximum at pH 7–8** → *evidence for* → `METPO:1000457`.

Only step 6 establishes the trait. The preceding mechanisms explain competence under the condition but do not uniquely determine that 7–8 is optimal.

## 5. Recent developments, data, and applications

### Genome-based pH-optimum prediction

A March 2024 preprint used amino-acid composition and protein localization to predict microbial growth conditions. After curation and balancing, its pH dataset contained 756 organisms; the pH values spanned 1.1–12.0 with mean 7.2. The reported held-out pH model reached R² ≈ 0.54 and RMSE ≈ 0.89 pH unit, while cross-validation yielded R² ≈ 0.48 and RMSE ≈ 1.05. Approximately 65% of 1,020 curated organisms with pH information had optima between pH 6 and 8. (barnum2024predictingmicrobialgrowth pages 22-24, barnum2024predictingmicrobialgrowth pages 3-6)

Protein localization materially improved pH prediction, and the difference in glutamate frequency between extracellular and intracellular proteins correlated with optimum pH (ρ = 0.56). This supports the importance of proteome compartmentation and surface chemistry, but such compositional features are **predictors**, not experimentally demonstrated causal nodes. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 3-6, barnum2024predictingmicrobialgrowth pages 16-19)

The model was applied at scale to 85,205 sequenced bacterial and archaeal species and to metagenome-assembled genomes from 3,349 environmental samples. It can operate on genomes reported to be as little as 10% complete, and the associated GenomeSPOT implementation was reported to run in approximately 5–10 seconds per genome per CPU. These tools can prioritize cultivation conditions for uncultivated organisms, although an error near one pH unit is substantial for assigning a narrow 7–8 ontology bin. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 19-22)

### Contemporary organism-level studies

The 2023 Cedars study illustrates why optimum and range must remain separate. Paeni-Cedars grew across pH 7–10 but was reported to have an optimum around pH 9; Ali-BS5-314 grew at pH 10–12 with optimum pH 11; Anaero-CMMVII grew at pH 9–12 but was difficult to cultivate consistently. The study also linked anaerobic growth of Ali-BS5-314 to nitrate as terminal electron acceptor, demonstrating that electron-acceptor conditions belong in assay provenance. (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe pages 3-4)

A 2024 comparison of alkaliphilic *B. aequororis* 5-DB and weakly alkali-resistant *B. subtilis* ATCC 6633 measured intracellular pH, ATP, metabolism, and morphology. *B. aequororis* maintained a non-zero ΔpH even at external pH 3 and showed its largest ΔpH at pH 11 with 50 g/L NaCl; intracellular pH reached approximately 9 after 48 hours. ATP decreased significantly at 50 g/L relative to 0.5 g/L NaCl. These data reinforce the dependence of pH physiology on salinity, growth phase, and exposure duration, but concern broad stress resistance rather than a 7–8 optimum. (maksimova2024metabolicandmorphological pages 9-10)

### Real-world relevance

Current implementations include genome-guided selection of cultivation pH, phenotype prediction for uncultivated microbes, and matching strains to environmental or bioprocess conditions. The same mechanisms matter in wastewater biofilms, alkaline fermentations, high-pH bioremediation, and industrial use of alkalitolerant enzymes. For TraitMech, however, an application paper should contribute an edge only if it reports a manipulable mechanism and a relevant growth phenotype—not merely successful operation at a stated reactor pH.

## 6. Expert assessment and curation priorities

The authoritative mechanistic synthesis supports a **network model**, not a single “pH-optimum gene.” Neutral-to-mildly alkaline growth emerges from interacting transport, bioenergetic, envelope, and regulatory systems. The strongest curatable causal evidence in the retrieved literature is:

- NhaA-dependent alkaline adaptation in sodium-containing media in *E. coli*;
- loss of alkaliphily and pH homeostasis after *mrpA* mutation in *B. halodurans*;
- ATP-synthase subunit mutations associated with loss of alkaline-shift homeostasis;
- impaired alkaline adaptation after *slpA* deletion in *B. pseudofirmus* OF4. (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 12-14)

These mechanisms should initially be represented as **taxon-qualified contributors to alkaline pH homeostasis**, with a separate, weaker link from homeostasis to the 7–8 optimum. This avoids asserting that machinery required at pH 11 causes an organism to prefer pH 7–8.

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not equate cytoplasmic pH 7.5–7.7 with `METPO:1000457`.** The trait concerns external best-growth pH. (krulwich2011molecularaspectsof pages 1-3)
2. **Do not infer an optimum from a growth range.** A strain growing from pH 7–10 may have an optimum at pH 9. (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe pages 3-4)
3. **Do not make NhaA or Mrp universal necessary nodes.** Their importance depends on taxon, sodium availability, and respiratory context. K⁺/H⁺ systems may dominate in sodium-poor media. (krulwich2011molecularaspectsof pages 5-6, jong2024quantitativeproteomicsreveals pages 1-2)
4. **Do not promote expression changes to causal edges without qualification.** Oxygen-dependent Mrp downregulation in *C. thermarum* is proteomic association, not a perturbation test. (jong2024quantitativeproteomicsreveals pages 1-2)
5. **Do not treat proteome composition correlations as mechanisms.** The glutamate-frequency correlation and machine-learning feature importance are valuable hypotheses, not causal validation. (barnum2024predictingmicrobialgrowth pages 3-6, barnum2024predictingmicrobialgrowth pages 16-19)
6. **Do not assign a narrow bin solely from model predictions.** RMSE near 0.9–1.05 pH unit can move an estimate across adjacent bins. (barnum2024predictingmicrobialgrowth pages 22-24)
7. **Do not omit assay context.** Temperature, sodium, oxygen, buffer, carbon source, inoculum state, exposure duration, and measurement endpoint can alter the apparent optimum.
8. **Avoid unverified ontology identifiers.** Use label-only nodes until GO, UniProt, Rhea, KEGG, MetaCyc, EC, and strain-level NCBITaxon mappings are checked against current releases.
9. **Do not curate putrescine, nitrate respiration, or specific terminal oxidases directly into this trait graph without endpoint evidence.** They may affect pH stress or energy metabolism, but the retrieved evidence does not show that they cause a pH 7–8 growth optimum.

## 8. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational authoritative review. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14)
2. Thompson J, et al. **Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system.** *Frontiers in Microbiology*. Published July 2023. DOI: [10.3389/fmicb.2023.1179857](https://doi.org/10.3389/fmicb.2023.1179857). (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe pages 3-4)
3. Barnum TP, et al. **Predicting microbial growth conditions from amino acid composition.** *bioRxiv*. Posted March 2024. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). Preprint; interpret performance and biological associations accordingly. (barnum2024predictingmicrobialgrowth pages 22-24, barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 3-6, barnum2024predictingmicrobialgrowth pages 19-22, barnum2024predictingmicrobialgrowth pages 16-19)
4. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology*. Published January 2024. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 9-10)
5. de Jong SI, et al. **Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology*. Published October 2024. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2)

## Curation recommendation

Retain `METPO:1000457` as an **externally measured optimal-growth-pH class**. Build its first causal graph around proton availability, Na⁺/H⁺ or conditionally K⁺/H⁺ antiport, PMF management, ATP synthase, respiratory regulation, and surface proton retention. Qualify organism-specific mechanisms and keep the final mechanism-to-trait edge uncertain until a study directly couples perturbation of that mechanism to a measured shift into or out of the pH 7–8 optimum bin.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (thompson2023insightsintothe pages 5-7): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

3. (thompson2023insightsintothe pages 3-4): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

8. (barnum2024predictingmicrobialgrowth pages 22-24): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

9. (barnum2024predictingmicrobialgrowth pages 3-6): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

10. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

11. (barnum2024predictingmicrobialgrowth pages 16-19): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

12. (barnum2024predictingmicrobialgrowth pages 19-22): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

13. (maksimova2024metabolicandmorphological pages 9-10): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.