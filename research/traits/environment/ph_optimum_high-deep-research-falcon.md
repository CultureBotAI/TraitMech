---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:27:06.376699'
end_time: '2026-06-18T00:53:39.497965'
duration_seconds: 1593.12
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum high
  trait_identifier: METPO:1000458
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH above approximately
    8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
  evidence_summary: 'DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review
    supports alkaliphile and extreme-alkaliphile physiology growing at high external
    pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review
    supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism
    sustaining the proton motive force at high external pH.)'
  causal_graph_summary: 'ph_optimum_high_alkaliphile_setpoint: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum high
- **METPO identifier:** METPO:1000458
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH above approximately 8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile and extreme-alkaliphile physiology growing at high external pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism sustaining the proton motive force at high external pH.)
- **Existing causal graph summary:** ph_optimum_high_alkaliphile_setpoint: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_high.yaml`.

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
- **Trait label:** pH optimum high
- **METPO identifier:** METPO:1000458
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH above approximately 8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile and extreme-alkaliphile physiology growing at high external pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism sustaining the proton motive force at high external pH.)
- **Existing causal graph summary:** ph_optimum_high_alkaliphile_setpoint: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_high.yaml`.

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


## Microbial Trait Causal Graph Curation Report
### Target trait
- **Trait label:** pH optimum high (alkaliphile / extreme alkaliphile)
- **Identifier:** METPO:1000458
- **Definition (given):** best-growth external pH above ~8; alkaliphilic/extreme-alkaliphilic physiology

## 1) Scope summary (trait meaning, assay context, boundaries)
**What the trait represents.** “pH optimum high” is best curated as an **organismal growth optimum** at alkaline external pH (commonly ≥9), rather than mere survival or maintenance of metabolic activity at high pH. A recent extremophile review explicitly defines **alkaliphiles** as organisms that “**Tolerate high pH levels above 9.0**” (Table 1) and lists Na+/H+ antiporters and other strategies as survival mechanisms. (adetunji2024unravelingthepotentials pages 3-4)

**Boundary cases / nearby traits.**
- **Alkali-tolerant / alkali-resistant** organisms may **grow** at high pH (e.g., pH 9–10) without having their **optimum** there. A 2024 experimental study tested growth at **pH 7–10** and concluded that the presence of an **Mrp antiporter operon** “**may enable continuous growth even under high pH conditions (~pH 10)**,” implying a genotype-supported high-pH growth boundary but not necessarily a growth optimum at pH 10. (kim2024lineagespecificevolutionof pages 9-12)
- **Extreme alkaliphily** can extend beyond pH 10. A 2024 enzymes/extremophile review notes microorganisms surviving at “**pH > 11**” and classifies **alkaliphilic enzymes** as having “**optimal pH > 9.0**.” (mao2024enzymeengineeringperformance pages 17-18)

**Recommended curation distinction for METPO:1000458.**
- Curate as **growth optimum at high pH** (preferably supported by measured growth curves/optima).
- Treat “growth at pH 9–10” evidence as supportive but distinguish from “optimum at pH 9–10,” unless explicitly stated.

## 2) Current understanding: mechanistic concepts that causally support high-pH growth
Alkaliphiles must maintain near-neutral cytoplasmic pH and sufficient bioenergetic driving force despite low external [H+]. The strongest, repeatedly supported modules in the retrieved literature are:

### 2.1 Ion homeostasis and pH homeostasis via monovalent cation/proton antiport
A core and widely cited alkaliphile strategy is **importing protons while exporting Na+** through Na+/H+ antiporters.
- A 2024 haloalkaliphile study states: “**Monovalent cation/proton antiporters play a key role in regulating the influx of H+ and the efflux of Na+** … essential for the growth of various halophilic and alkaliphilic bacteria” and categorizes them into **CPA (including Mrp-type)** and **Nha (NhaA/B/C/D)** families. (xing2024thepolyextremophilenatranaerobius pages 19-21)
- In *Natranaerobius thermophilus* (optimum pH **9.5**), three **NhaC** antiporters were upregulated and two showed “**significant Na+-dependent antiport activity**.” (xing2024thepolyextremophilenatranaerobius pages 19-21, xing2024thepolyextremophilenatranaerobius pages 1-2)
- In aquatic lineages, a seven-gene **Mrp (mrpABCDEFG)** complex is described as crucial for saline–alkaline stress; its presence is linked to growth up to ~pH 10. (kim2024lineagespecificevolutionof pages 9-12)

### 2.2 Sodium cycle bioenergetics and ATP synthase adaptations
At high pH, the proton motive force (pmf) can be small; some alkaliphiles rely heavily on **sodium motive force** and **Na+-coupled ATPases/ATP synthases**.
- *N. thermophilus* is described as possessing “**a large group of Na+ (K+)/H+ antiporters and Na+-translocating FOF1-ATPase**” to adapt to multiple extremes. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- Structural/biochemical evidence for Na+-coupled ATP synthases includes a conserved **c-subunit Na+ binding motif “Q….ET”** proposed to form the Na+ binding site. (brandt2015hybridrotorsin pages 4-6)
- The same ATP synthase review includes a mechanistic coupling partner: the **Rnf complex**, described as expelling Na+ to establish a sodium gradient (“**expel sodium ions… establishing a transmembrane sodium ion gradient**”). (brandt2015hybridrotorsin pages 4-6)

**Visual evidence.** Figure 3 from Brandt & Müller (2015) shows Na+ coordination and ion binding sites in a hybrid rotor ATP synthase, supporting the structural basis for Na+ coupling. (brandt2015hybridrotorsin media 5f90e0a3)

### 2.3 Potassium uptake and membrane potential control
Maintaining Δψ and ion balance contributes to pH homeostasis.
- The **TrkAH (TrkH–TrkA)** potassium uptake system is stated to be responsible for K+ uptake and “**maintaining pH homeostasis**,” and it is “**involved in the adjustment of membrane potential**.” (xing2024thepolyextremophilenatranaerobius pages 19-21)

### 2.4 Respiratory chain flexibility to support chemiosmotic energy conservation at high pH
Some thermoalkaliphiles (e.g., *Caldalkalibacillus thermarum*) appear to use a **branched proton-mediated ETC** to cope with environmental variability.
- *C. thermarum* is from a hot spring at **pH 10** and has multiple terminal oxidases (aa3/ba3/bb3/bd) with different proton-pumping efficiencies; Cyt aa3 is described as pumping with **0.7 H+/electron**, while ba3 and bb3 pump with **0.5 H+/electron**, and bd does not pump protons. (jong2024quantitativeproteomicsreveals pages 1-2)
- The same study notes the **Mrp sodium-proton antiporter** is “normally… crucial for sodium homeostasis” in alkaliphiles, but was downregulated under strong oxygen limitation, suggesting condition-dependent modularity (and highlighting that alternative exporters can reduce Mrp demand). (jong2024quantitativeproteomicsreveals pages 1-2)

### 2.5 Cell envelope and surface chemistry
Review-level evidence suggests alkaliphiles can build more **acidic envelope structures** to retain protons near the membrane.
- A 2024 review reports alkaliphilic *Bacillus* “enhances proton motive force generation” by synthesis of an “**acidic plasma membrane, consisting of teichurono-peptide, peptidoglycan, and teichuronic acid**,” supporting pH balance and ATP production. (adetunji2024unravelingthepotentials pages 6-7)

### 2.6 Metabolic pH balancing by organic acid secretion
- The same review states: “**The secretion of organic acids by alkaliphilic microbes is a crucial metabolic activity that permits pH balance**.” (adetunji2024unravelingthepotentials pages 6-7)

## 3) Candidate nodes for graph curation (grouped)
The following node inventory is directly supported by the retrieved sources and is intended to seed `data/traits/environment/ph_optimum_high.yaml`.

| Node label | Node type (gene/protein complex / pathway/module / chemical / environmental factor / process) | Suggested ontology grounding (CURIEs if known; otherwise 'unresolved') | Evidence/source |
|---|---|---|---|
| Mrp (mrpABCDEFG) Na+/H+ antiporter complex | gene/protein complex | unresolved | Explicitly described as a seven-gene sodium/proton antiporter complex important for saline-alkaline stress and growth at ~pH 10 in Aquibium; also noted as crucial for sodium homeostasis in alkaliphiles (kim2024lineagespecificevolutionof pages 9-12, jong2024quantitativeproteomicsreveals pages 1-2) |
| CPA family monovalent cation/proton antiporters | gene/protein complex | unresolved | CPA families (CPA1/CPA2/CPA3-Mrp type) are named as antiport systems regulating H+ influx and Na+ efflux in haloalkaliphiles (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| NhaA family Na+/H+ antiporter | gene/protein complex | unresolved | NhaA is explicitly listed among Nha families relevant to H+/Na+ exchange in N. thermophilus discussion (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| NhaB family Na+/H+ antiporter | gene/protein complex | unresolved | NhaB is explicitly listed among Nha families relevant to H+/Na+ exchange in N. thermophilus discussion (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| NhaC family Na+/H+ antiporter | gene/protein complex | unresolved | Three NhaC antiporters were upregulated in N. thermophilus; two showed significant Na+-dependent antiport activity (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| NhaD family Na+/H+ antiporter | gene/protein complex | unresolved | NhaD is explicitly listed among Nha families relevant to H+/Na+ exchange in N. thermophilus discussion (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| TrkAH potassium uptake system (TrkA/TrkH) | gene/protein complex | unresolved | TrkAH is described as responsible for K+ uptake, membrane potential adjustment, and maintenance of pH homeostasis in N. thermophilus (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| Opu family glycine betaine ABC transporters | gene/protein complex | unresolved | Opu family transporters are explicitly named for compatible-solute uptake in N. thermophilus (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| ProU family glycine betaine ABC transporters | gene/protein complex | unresolved | ProU family transporters are explicitly named for compatible-solute uptake in N. thermophilus (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| SSS family Na+/solute symporters | gene/protein complex | unresolved | Na+/solute symporters of the SSS family are explicitly described as using the Na+ electrochemical gradient for uptake of extracellular substrates (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21) |
| SdcS Na+/dicarboxylate symporter | gene/protein complex | unresolved | Na+/dicarboxylate symporter (SdcS) is specifically named among regulated SSS-family transporters in N. thermophilus (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| Na+-translocating FOF1-ATPase | gene/protein complex | GO:0046961 | Explicitly reported for N. thermophilus as an adaptation to multiple extremes; Na+-dependent ATPase systems are also discussed structurally (xing2024thepolyextremophilenatranaerobius pages 1-2, brandt2015hybridrotorsin pages 4-6) |
| F1Fo-ATP synthase c-subunit Na+ binding motif Q…ET | gene/protein complex | unresolved | The conserved Q…ET motif is explicitly described as the Na+ binding site motif in Na+-coupled ATP synthase c subunits (brandt2015hybridrotorsin pages 4-6) |
| Rnf complex | gene/protein complex | unresolved | Rnf is described as a major chemiosmotic redox enzyme that establishes a transmembrane sodium ion gradient in organisms with Na+-coupled ATP synthases (brandt2015hybridrotorsin pages 4-6) |
| Nqr complex | gene/protein complex | unresolved | Nqr is identified as a prominent Na+-translocating enzyme in bacteria in the ATP synthase/Rnf discussion (brandt2015hybridrotorsin pages 4-6) |
| Type I NADH dehydrogenase (Ndh-I / Complex I) | gene/protein complex | GO:0008137 | In C. thermarum, Ndh-I is explicitly described as a proton-pumping NADH dehydrogenase within a branched proton-mediated ETC (jong2024quantitativeproteomicsreveals pages 1-2) |
| Type II NADH dehydrogenase (Ndh-II) | gene/protein complex | GO:0008137 | In C. thermarum, Ndh-II is explicitly described as a non-proton-pumping NADH dehydrogenase within a branched proton-mediated ETC (jong2024quantitativeproteomicsreveals pages 1-2) |
| Cytochrome c:oxygen aa3 oxidase | gene/protein complex | unresolved | Explicit terminal oxidase in C. thermarum; described as proton-pumping and most abundant at higher O2 (jong2024quantitativeproteomicsreveals pages 1-2) |
| Cytochrome c:oxygen ba3 oxidase | gene/protein complex | unresolved | Explicit terminal oxidase in C. thermarum; proton-pumping with lower efficiency than aa3 (jong2024quantitativeproteomicsreveals pages 1-2) |
| Cytochrome c:oxygen bb3 oxidase | gene/protein complex | unresolved | Explicit terminal oxidase in C. thermarum; proton-pumping with lower efficiency than aa3 (jong2024quantitativeproteomicsreveals pages 1-2) |
| Cytochrome bd oxidase | gene/protein complex | unresolved | Explicit terminal oxidase in C. thermarum; stated not to pump protons (jong2024quantitativeproteomicsreveals pages 1-2) |
| Cytochrome c | gene/protein complex | CHEBI:29105 | Review-level evidence states cytochrome c in Gram-positive alkaliphiles contributes to pH homeostasis by proton deposition (adetunji2024unravelingthepotentials pages 6-7) |
| Cytochrome c-552 | gene/protein complex | unresolved | Review-level evidence states cytochrome c-552 in Gram-negative alkaliphiles contributes to pH homeostasis by proton deposition (adetunji2024unravelingthepotentials pages 6-7) |
| Glycine betaine uptake/synthesis module | pathway/module | CHEBI:17750 | Compatible-solute accumulation is explicitly supported in N. thermophilus, including Opu/ProU transport and increased intracellular glycine betaine (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 24-25) |
| Glutamate synthesis pathway | pathway/module | CHEBI:29985 | Explicitly named as part of the adaptation program in N. thermophilus under high salinity/alkaline conditions (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Proline synthesis/uptake pathway | pathway/module | CHEBI:26271 | Explicitly named as part of the adaptation program in N. thermophilus under high salinity/alkaline conditions (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21) |
| Organic acid secretion | process | GO:0015891 | Review-level evidence states secretion of organic acids is a crucial activity permitting pH balance in alkaliphilic microbes (adetunji2024unravelingthepotentials pages 6-7, adetunji2024unravelingthepotentials pages 3-4) |
| Cytoplasmic acidification | process | GO:0006885 | Explicitly reported for N. thermophilus in response to high Na+ concentrations (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Acidic proteome | process | unresolved | N. thermophilus proteome is reported as predominantly acidic, with median pI values around 5, supporting adaptation to extreme haloalkaline conditions (xing2024thepolyextremophilenatranaerobius pages 19-21) |
| Teichuronic acid | chemical | CHEBI:61051 | Explicitly named as part of an acidic plasma membrane/cell envelope supporting proton motive force generation in alkaliphilic Bacillus sp. (adetunji2024unravelingthepotentials pages 6-7) |
| Peptidoglycan | chemical | GO:0005618 | Explicitly named as part of the acidic plasma membrane/cell envelope supporting proton motive force generation in alkaliphilic Bacillus sp. (adetunji2024unravelingthepotentials pages 6-7) |
| Teichurono-peptide | chemical | unresolved | Explicitly named as a component of the acidic plasma membrane/cell envelope in alkaliphilic Bacillus sp. (adetunji2024unravelingthepotentials pages 6-7) |
| Sodium ion (Na+) | chemical | CHEBI:29101 | Central ion in Na+/H+ antiport, Na+/solute symport, Na+-ATPase coupling, and soda-lake environments (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21, brandt2015hybridrotorsin pages 4-6) |
| Proton (H+) | chemical | CHEBI:15378 | Central ion in pH homeostasis, proton motive force, proton-coupled oxidases, and antiporter-mediated H+ influx (xing2024thepolyextremophilenatranaerobius pages 19-21, jong2024quantitativeproteomicsreveals pages 1-2, adetunji2024unravelingthepotentials pages 6-7) |
| Potassium ion (K+) | chemical | CHEBI:29103 | Explicitly accumulated via TrkAH and elevated intracellularly in N. thermophilus as part of a salt-in / pH-homeostasis strategy (xing2024thepolyextremophilenatranaerobius pages 19-21, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| High-pH environment (pH 9-11) | environmental factor | ENVO:01000314 | Soda lakes and alkaliphile habitats are explicitly described as alkaline, with pH 9-11 and optimal growth around pH 9.5-9.9 (xing2024thepolyextremophilenatranaerobius pages 1-2, adetunji2024unravelingthepotentials pages 3-4) |
| Sodium carbonate soda lakes | environmental factor | ENVO:00000026 | Soda lakes are explicitly described as stable, highly alkaline natural habitats with high soluble sodium carbonates and as the source habitat for N. thermophilus (xing2024thepolyextremophilenatranaerobius pages 1-2) |


*Table: This table lists candidate mechanistic nodes for curating METPO:1000458 (pH optimum high), with suggested grounding and direct evidence links from the retrieved literature. It is useful for building a TraitMech node inventory before selecting causal edges.*

## 4) Evidence-backed candidate causal edges (triples)
The following proposed edges are expressed as **subject–predicate–object triples**, each supported by a snippet and DOI-first reference. Use the “Curation notes/uncertainty” column to decide whether to include directly or defer pending stronger primary evidence.

| Edge (S–P–O) | Mechanistic meaning for high-pH growth | Evidence snippet (verbatim or near-verbatim) | Source (DOI, year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|
| High external pH / saline–alkaline stress → selects for → Mrp (mrpABCDEFG) sodium/proton antiporter complex | Mrp is a core antiporter module repeatedly associated with alkaline adaptation and sodium homeostasis | “The Mrp complex plays a crucial role in coping with saline–alkaline and hyperosmotic stresses, particularly in alkaliphilic bacteria” (kim2024lineagespecificevolutionof pages 9-12) | 10.1128/AEM.02091-23, 2024, https://doi.org/10.1128/AEM.02091-23 | Strong support for Mrp as a candidate node/edge; direct alkaliphile relevance. |
| Mrp operon presence → enables → continuous growth at ~pH 10 | Direct genotype-to-phenotype link for high-pH growth boundary | “The presence of mrp genes in AL and N-ML may enable continuous growth even under high pH conditions (~pH 10)” (kim2024lineagespecificevolutionof pages 9-12) | 10.1128/AEM.02091-23, 2024, https://doi.org/10.1128/AEM.02091-23 | Very curatable; taxon-specific to Aquibium/Mesorhizobium lineages but mechanistically strong. |
| Alkaline condition (pH 9) → upregulates → mrpA1 / mrpA2 expression | Supports inducible alkaline-stress response via Mrp | “The highest expression of mrpA1… was noted in the stationary phase… under the alkaline condition (pH 9). The expression of mrpA2 gene was continuously upregulated” (kim2024lineagespecificevolutionof pages 9-12) | 10.1128/AEM.02091-23, 2024, https://doi.org/10.1128/AEM.02091-23 | Good evidence for regulation, not alone sufficient to prove causality outside tested taxa. |
| CPA/Nha family Na+/H+ antiporters → decrease → intracellular Na+ concentration | Canonical alkaliphile pH-homeostasis mechanism: export Na+, import H+ | “Monovalent cation/proton antiporters play a key role in regulating the influx of H+ and the efflux of Na+” and “The Na+/H+ antiporters effectively decrease the intracellular Na+ concentration” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong mechanistic edge; family-level rather than single gene. |
| NhaC antiporters → contribute to → salt/alkaline acclimation | Specific antiporter subtype with measured activity in haloalkaliphile | “In N. thermophilus, three Na+/H+ antiporters NhaC were found to be upregulated… two NhaC proteins… exhibited significant Na+-dependent antiport activity” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Good evidence for NhaC; causal link to alkaliphily inferred from activity plus ecological context. |
| TrkAH K+ uptake system → maintains → pH homeostasis | K+ uptake helps membrane potential control and pH homeostasis under multiple extremes | “The TrkAH transport system is responsible for the uptake of K+ in response to osmotic shock and maintaining pH homeostasis. Additionally, this system is involved in the adjustment of membrane potential” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong for node inclusion; edge to alkaliphily is supported in N. thermophilus context. |
| Increasing salinity / alkaline adaptation → increases → intracellular K+ | “Salt-in” component complements antiport-based pH adaptation | “the intracellular K+ concentration was found to increase with increasing salinity, reaching… 227.2, 240.2, 389.0, and 440.2 mM” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong quantitative evidence, but more osmoadaptation than purely pH-optimum; keep as supporting edge. |
| Opu/ProU glycine betaine ABC transporters → mediate uptake of → compatible solutes | Compatible solute uptake supports survival/growth in haloalkaline conditions that co-occur with high pH | “N. thermophilus employs the glycine betaine ABC transporters (Opu and ProU families)… The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong for compatible-solute module; indirect for pH optimum specifically. Mark as supportive, not defining. |
| Glutamate / proline synthesis pathways → increase → compatible-solute pools | Biosynthetic arm of hybrid adaptation aiding growth in soda-lake conditions | “employs… glutamate and proline synthesis pathways… compatible solutes… increase with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Supportive but mostly salinity-focused; likely secondary in pH-optimum graph. |
| SSS family Na+/solute symporters → use → Na+ electrochemical gradient for substrate uptake | Links sodium cycle to nutrient uptake under high-pH conditions | “The Na+/solute symporter (SSS family) was also identified as a secondary active transporter that utilizes the Na+ electrochemical gradients as the driving force for the uptake of extracellular substrates” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Useful systems-level edge; more about exploiting Na+ gradient than pH homeostasis itself. |
| Na+-translocating FOF1-ATPase → supports adaptation to → multiple extremes including high pH | Sodium-coupled ATPase is a hallmark bioenergetic adaptation in some alkaliphiles | “N. thermophilus possesses… Na+-translocating FOF1-ATPase to adapt to multiple extremes” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong candidate node; exact edge to pH optimum should be phrased cautiously because source mentions multiple extremes together. |
| ATP synthase c subunit Q…ET Na+-binding motif → confers → Na+-specific ion coupling | Structural basis for sodium bioenergetics used by many alkaliphile-associated ATP synthases | “c subunits from Na+ ATP synthases have a conserved motif, Q….ET that was postulated to be the Na+ binding site” (brandt2015hybridrotorsin pages 4-6) | 10.1515/hsz-2015-0137, 2015, https://doi.org/10.1515/hsz-2015-0137 | Foundational/structural evidence; not specific to alkaliphiles only, but highly relevant to sodium-cycle model. |
| Rnf complex → generates → transmembrane Na+ gradient | Primary sodium pump can energize Na+-coupled ATP synthesis/transport in high-pH-adapted anaerobes | “Rnf is the major chemiosmotic redox enzyme that transfers electrons from reduced ferredoxin to NAD and uses this redox difference as driving force to expel sodium ions from the cytoplasm thus establishing a transmembrane sodium ion gradient” (brandt2015hybridrotorsin pages 4-6) | 10.1515/hsz-2015-0137, 2015, https://doi.org/10.1515/hsz-2015-0137 | Important mechanistic edge; inferred into alkaliphily from co-occurrence with Na+ ATP synthases, not always directly tested for pH optimum. |
| Branched respiratory chain terminal oxidases (aa3/ba3/bb3) → pump → protons with different efficiencies | Respiratory flexibility helps maintain usable proton motive force at high pH and varying oxygen | “Cyt. aa3… pumps protons at an efficiency of 0.7 H+/electron… Cyt. ba3 and Cyt. bb3 both pump protons, but with a lesser efficiency of 0.5 proton per electron” (jong2024quantitativeproteomicsreveals pages 1-2) | 10.3389/fmicb.2024.1468929, 2024, https://doi.org/10.3389/fmicb.2024.1468929 | Strong systems-level support, especially for C. thermarum; proton-pumping values are from cited biochemical models. |
| Proton-coupled F1Fo-ATP synthase → uses → proton motive force | Shows that some alkaliphiles remain proton-coupled despite extreme external pH | “Finally, completing the ensemble is a proton-coupled F1Fo-ATP synthase” (jong2024quantitativeproteomicsreveals pages 1-2) | 10.3389/fmicb.2024.1468929, 2024, https://doi.org/10.3389/fmicb.2024.1468929 | Good contrast with Na+-ATPase systems; should not be generalized to all alkaliphiles. |
| Acidic plasma membrane polymers (teichurono-peptide / peptidoglycan / teichuronic acid) → enhance → proton motive force generation | Cell-envelope acidification is proposed to aid proton retention and ATP production at high pH | “alkaliphilic Bacillus sp. enhances proton motive force generation by synthesis of acidic plasma membrane, consisting of teichurono-peptide, peptidoglycan, and teichuronic acid” (adetunji2024unravelingthepotentials pages 6-7) | 10.3390/min14090861, 2024, https://doi.org/10.3390/min14090861 | Review-level claim; likely curatable as higher-level envelope feature, but verify in primary Bacillus sources before detailed graphing. |
| Organic acid secretion → permits → pH balance | Metabolic acid release may help counter alkaline stress | “The secretion of organic acids by alkaliphilic microbes is a crucial metabolic activity that permits pH balance” (adetunji2024unravelingthepotentials pages 6-7) | 10.3390/min14090861, 2024, https://doi.org/10.3390/min14090861 | Review-level/general; lacks gene-level grounding. Curate only as broad process unless stronger primary evidence is obtained. |
| High Na+ concentration → causes / is associated with → cytoplasmic acidification | Acidification of cytoplasm is a direct physiological response relevant to high-pH survival | “N. thermophilus exhibits cytoplasmic acidification in response to high Na+ concentrations” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Good physiological edge; note stimulus is high Na+ in a haloalkaliphile, not isolated high pH alone. |
| Cytochrome c-552 / cytochrome c → promote → pH homeostasis by proton deposition | Respiratory cytochromes are proposed contributors to alkaliphile pH homeostasis | “Alkaliphiles survive at high alkalinity due to the presence of cytochrome c-552… and cytochrome c… which regulate pH homeostasis by proton deposition” (adetunji2024unravelingthepotentials pages 6-7) | 10.3390/min14090861, 2024, https://doi.org/10.3390/min14090861 | Interesting but review-level and somewhat broad; needs primary-source validation before strong TraitMech curation. |


*Table: This table summarizes candidate subject–predicate–object edges for the microbial trait “pH optimum high,” with supporting snippets, DOI-first sources, and curation cautions. It emphasizes ion homeostasis, sodium/proton antiport, ATP synthase adaptations, respiratory energetics, and envelope/metabolic features relevant to alkaliphily.*

## 5) Recent developments (2023–2024 emphasis)
### 5.1 New multi-omics quantification in haloalkaliphiles
A 2024 *Applied and Environmental Microbiology* study integrates proteomics, mRNA, and metabolites in the polyextremophile *N. thermophilus* (optimum pH **9.5**) and quantifies key ion/solute pools and bioenergetic parameters. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21)

### 5.2 Quantitative bioenergetics under alkaline conditions
At **3.3 M NaCl, pH 9.5, 53°C**, energized *N. thermophilus* suspensions had **Δψ = −124 mV** and **pmf = −56 mV**, illustrating that high-pH growth can occur with relatively small pmf and thus may rely on Na+ coupling and specialized ion homeostasis. (xing2024thepolyextremophilenatranaerobius pages 19-21)

### 5.3 Comparative genomics linking Mrp operons to high-pH growth
A 2024 AEM comparative genomics paper ties the Mrp operon to growth up to **~pH 10** and shows pH-dependent transcriptional upregulation (pH 9) of mrpA genes. (kim2024lineagespecificevolutionof pages 9-12)

### 5.4 Extreme-environment respiratory chain regulation
A 2024 Frontiers in Microbiology study on the thermoalkaliphile *C. thermarum* examines oxygen-dependent shifts in respiratory chain composition and reports regulated Mrp abundance, supporting a more conditional view of “core” modules in alkaliphile physiology. (jong2024quantitativeproteomicsreveals pages 1-2)

## 6) Current applications and real-world implementations (with recent statistics)
### 6.1 Industrial enzymes active at alkaline pH
**Alkaline proteases** and other alkali-active enzymes are dominant industrial biocatalysts.
- Proteases “hold about **60%** shares of total enzymes sold commercially” and the worldwide protease market was **USD 2.76 billion (2019)** with expected **~6.1% annual growth (2019–2024)**. (pawar2023fungalalkalineproteases pages 1-2)
- Alkaline proteases are highlighted for detergents, leather/tannery, food, silk degumming, waste management and silver recovery in a 2023 Frontiers review. (pawar2023fungalalkalineproteases pages 1-2)

### 6.2 Example implementation data: alkaline cellulase production
An applied 2024 study on alkaliphilic cellulolytic fungi reports cellulase “favoured and was active at high alkaline conditions (**pH 9 and pH 10**)” and provides process-level values (e.g., pH-specific HC metrics; maximum glucose generation at **15% (v/v) enzyme loading** and **1% microcrystalline cellulose**). (zainuddin2024isolationscreeningand pages 11-15)

### 6.3 Industrial adoption indicators
A 2023 national review reports Bangladesh was the **34th largest enzyme importer** in **2021** with enzyme imports valued at **$47.4 million**, illustrating real-world demand for industrial enzymes (including alkaline enzymes commonly produced by microbes). (hossain2023industrialenzymeproduction pages 1-2)

### 6.4 Alkaliphiles in bioleaching/bioextraction contexts
A 2024 Minerals review summarizes the role of extremophiles (including alkaliphiles) in bioextraction of valuable metals from industrial solid wastes and describes alkaliphile survival strategies (Na+/H+ antiporters, organic acids, etc.), supporting the relevance of high-pH physiology in environmental/industrial biotechnology. (adetunji2024unravelingthepotentials pages 3-4, adetunji2024unravelingthepotentials pages 6-7)

## 7) Expert/authoritative analysis synthesis (curation-oriented)
Across 2024 primary studies and authoritative reviews, the most consistently supported causal chain for “pH optimum high” is:
1) **High external pH** reduces available protons and challenges pmf.
2) Organisms deploy **Na+/H+ antiporters** (Mrp/Nha families) to import H+ while exporting Na+, enabling cytoplasmic pH control and Na+ detoxification. (xing2024thepolyextremophilenatranaerobius pages 19-21, kim2024lineagespecificevolutionof pages 9-12)
3) Many systems then exploit **Na+ gradients** for energy coupling and solute uptake (Na+-translocating ATPases/ATP synthases, Na+/solute symporters) and complement with **K+ uptake** and compatible solutes. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21, brandt2015hybridrotorsin pages 4-6)
4) Additional layers (branched respiratory chains, envelope acidification, organic acid secretion) are plausible and supported but in several cases remain review-level and would benefit from primary validation before fine-grained curation. (jong2024quantitativeproteomicsreveals pages 1-2, adetunji2024unravelingthepotentials pages 6-7)

## 8) Statistics & quantitative data extracted (recent)
- *N. thermophilus* optimum pH **9.5** and growth salinity **3.3–3.9 M Na+**; growth range **3.1–4.9 M Na+**. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- Bioenergetics at **pH 9.5**: **Δψ = −124 mV**, **pmf = −56 mV** (3.3 M NaCl, 53°C). (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Intracellular K+ under different salinities: **227.2, 240.2, 389.0, 440.2 mM** at **2.5, 3.1, 3.7, 4.3 M Na+**. (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Protease market: **USD 2.76B (2019)**; **~6.1% annual growth 2019–2024**; proteases ~**60%** of commercial enzyme sales. (pawar2023fungalalkalineproteases pages 1-2)
- Bangladesh enzyme import value **$47.4M (2021)**. (hossain2023industrialenzymeproduction pages 1-2)

## 9) Warnings / claims not ready for strong TraitMech curation
1) **Envelope polymer mechanisms (teichurono-peptide/teichuronic acid)** and **cytochrome c-552 proton deposition** are supported here primarily by a recent review rather than a directly inspected primary mechanistic paper; include as **high-level processes** or mark as **uncertain** until primary sources are gathered. (adetunji2024unravelingthepotentials pages 6-7)
2) **Organic acid secretion** is plausible and cited as crucial for pH balance but lacks gene-level grounding in the retrieved excerpts; curate cautiously as a process node. (adetunji2024unravelingthepotentials pages 6-7)
3) Many data come from **haloalkaliphiles** (e.g., soda lake Clostridia) where salt and pH are coupled; edges should be labeled as potentially **confounded by salinity** unless studies isolate pH as the variable. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21)

## DOI-first bibliography (publication date & URL)
- **Xing Q, et al.** (Published **2024-04-05**). *Applied and Environmental Microbiology.* “The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy…” DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21)
- **Kim M, et al.** (Published **2024-03**, AEM issue). *Applied and Environmental Microbiology.* “Lineage-specific evolution of Aquibium…” DOI: **10.1128/aem.02091-23**. URL: https://doi.org/10.1128/aem.02091-23 (kim2024lineagespecificevolutionof pages 9-12)
- **de Jong SI, et al.** (Published **2024-10-28**). *Frontiers in Microbiology.* “Quantitative proteomics reveals oxygen-induced adaptations…” DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)
- **Adetunji AI, Erasmus M.** (Published **2024-08**). *Minerals.* “Unraveling the potentials of extremophiles in bioextraction…” DOI: **10.3390/min14090861**. URL: https://doi.org/10.3390/min14090861 (adetunji2024unravelingthepotentials pages 3-4, adetunji2024unravelingthepotentials pages 6-7)
- **Hafeez AB, et al.** (Published **2024-01**). *International Journal of Molecular Sciences.* “In Silico Safety Assessment of Bacillus…” DOI: **10.3390/ijms25010666**. URL: https://doi.org/10.3390/ijms25010666 (hafeez2024insilicosafety pages 22-23)
- **Brandt K, Müller V.** (Published **2015-09**). *Biological Chemistry.* “Hybrid rotors in F1Fo ATP synthases…” DOI: **10.1515/hsz-2015-0137**. URL: https://doi.org/10.1515/hsz-2015-0137 (brandt2015hybridrotorsin pages 4-6, brandt2015hybridrotorsin media 5f90e0a3)
- **Pawar KS, et al.** (Published **2023-03-30**). *Frontiers in Microbiology.* “Fungal alkaline proteases…” DOI: **10.3389/fmicb.2023.1138401**. URL: https://doi.org/10.3389/fmicb.2023.1138401 (pawar2023fungalalkalineproteases pages 1-2)
- **Hossain I, et al.** (Published **2023-12-14**). *Asian Journal of Medical and Biological Research.* “Industrial enzyme production in Bangladesh…” DOI: **10.3329/ajmbr.v9i4.69395**. URL: https://doi.org/10.3329/ajmbr.v9i4.69395 (hossain2023industrialenzymeproduction pages 1-2)
- **Zainuddin N, et al.** (Published **2024-01**). *Green Processing and Synthesis.* “Isolation, screening and optimization of alkaliphilic cellulolytic fungi…” DOI: **10.1515/gps-2023-0153**. URL: https://doi.org/10.1515/gps-2023-0153 (zainuddin2024isolationscreeningand pages 11-15)
- **Mao S, et al.** (Published **2024-11**). *Foods.* “Enzyme Engineering: Performance Optimization…” DOI: **10.3390/foods13233846**. URL: https://doi.org/10.3390/foods13233846 (mao2024enzymeengineeringperformance pages 17-18)


References

1. (adetunji2024unravelingthepotentials pages 3-4): Adegoke Isiaka Adetunji and Mariana Erasmus. Unraveling the potentials of extremophiles in bioextraction of valuable metals from industrial solid wastes: an overview. Minerals, 14:861, Aug 2024. URL: https://doi.org/10.3390/min14090861, doi:10.3390/min14090861. This article has 7 citations.

2. (kim2024lineagespecificevolutionof pages 9-12): Minkyung Kim, Wonjae Kim, Yerim Park, Jaejoon Jung, and Woojun Park. Lineage-specific evolution of aquibium, a close relative of mesorhizobium, during habitat adaptation. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02091-23, doi:10.1128/aem.02091-23. This article has 4 citations and is from a peer-reviewed journal.

3. (mao2024enzymeengineeringperformance pages 17-18): Shucan Mao, Jiawen Jiang, Ke Xiong, Yiqiang Chen, Yuyang Yao, Linchang Liu, Hanbing Liu, and Xiang Li. Enzyme engineering: performance optimization, novel sources, and applications in the food industry. Foods, 13:3846, Nov 2024. URL: https://doi.org/10.3390/foods13233846, doi:10.3390/foods13233846. This article has 73 citations.

4. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (brandt2015hybridrotorsin pages 4-6): Karsten Brandt and Volker Müller. Hybrid rotors in f1fo atp synthases: subunit composition, distribution, and physiological significance. Sep 2015. URL: https://doi.org/10.1515/hsz-2015-0137, doi:10.1515/hsz-2015-0137. This article has 16 citations and is from a peer-reviewed journal.

7. (brandt2015hybridrotorsin media 5f90e0a3): Karsten Brandt and Volker Müller. Hybrid rotors in f1fo atp synthases: subunit composition, distribution, and physiological significance. Sep 2015. URL: https://doi.org/10.1515/hsz-2015-0137, doi:10.1515/hsz-2015-0137. This article has 16 citations and is from a peer-reviewed journal.

8. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

9. (adetunji2024unravelingthepotentials pages 6-7): Adegoke Isiaka Adetunji and Mariana Erasmus. Unraveling the potentials of extremophiles in bioextraction of valuable metals from industrial solid wastes: an overview. Minerals, 14:861, Aug 2024. URL: https://doi.org/10.3390/min14090861, doi:10.3390/min14090861. This article has 7 citations.

10. (xing2024thepolyextremophilenatranaerobius pages 24-25): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (pawar2023fungalalkalineproteases pages 1-2): Kadambari Subhash Pawar, Paras Nath Singh, and Sanjay Kumar Singh. Fungal alkaline proteases and their potential applications in different industries. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1138401, doi:10.3389/fmicb.2023.1138401. This article has 67 citations and is from a peer-reviewed journal.

12. (zainuddin2024isolationscreeningand pages 11-15): Nor’Izzah Zainuddin, Muaz Mohd Zaini Makhtar, Ahmad Anas Nagoor Gunny, Subash Chandra Bose Gopinath, Abdul Aziz Ahmad, Kavita Pusphanathan, Masoom Raza Siddiqui, Mahboob Alam, and Mohd Rafatullah. Isolation, screening and optimization of alkaliphilic cellulolytic fungi for production of cellulase. Green Processing and Synthesis, Jan 2024. URL: https://doi.org/10.1515/gps-2023-0153, doi:10.1515/gps-2023-0153. This article has 4 citations and is from a peer-reviewed journal.

13. (hossain2023industrialenzymeproduction pages 1-2): Imam Hossain, Israt Jahan Mitu, Md Rakibul Hasan, and Sumita Rani Saha. Industrial enzyme production in bangladesh: current landscape, scope, and challenges. Asian Journal of Medical and Biological Research, 9:145-159, Dec 2023. URL: https://doi.org/10.3329/ajmbr.v9i4.69395, doi:10.3329/ajmbr.v9i4.69395. This article has 4 citations.

14. (hafeez2024insilicosafety pages 22-23): Ahmer Bin Hafeez, Karolina Pełka, Randy Worobo, and Piotr Szweda. In silico safety assessment of bacillus isolated from polish bee pollen and bee bread as novel probiotic candidates. International Journal of Molecular Sciences, 25:666, Jan 2024. URL: https://doi.org/10.3390/ijms25010666, doi:10.3390/ijms25010666. This article has 15 citations.