---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:12:35.598545'
end_time: '2026-06-18T12:25:48.963810'
duration_seconds: 793.37
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: persister cell formation
  trait_identifier: traitmech:000082
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: persister_cell_formation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: Formation of dormant phenotypic variants (persister cells) that are
    transiently tolerant to antibiotics and other lethal stresses without carrying
    genetic resistance, arising stochastically in a population.
  parent_traits: traitmech:000080
  synonyms: persistence
  evidence_summary: 'DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister
    cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis
    links persister-cell dormancy to the recalcitrance of chronic infections.)'
  causal_graph_summary: 'persister_dormancy_tolerance: 3 nodes, 2 edges'
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
- **Trait label:** persister cell formation
- **METPO identifier:** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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
- **Trait label:** persister cell formation
- **METPO identifier:** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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


# Persister Cell Formation (METPO: traitmech:000082) — Curation-Focused Research Report (2023–2024 emphasis)

## 0) Trait scope summary (what to curate)

**Trait label:** persister cell formation (syn. persistence)  
**Definition (curation target):** formation of dormant phenotypic variants (persister cells) that are **transiently tolerant** to antibiotics/lethal stresses **without genetic resistance**, arising stochastically in a population.

**Operational phenotype / assay readouts.** Persistence is classically identified by **(i) a biphasic killing curve** under bactericidal antibiotic exposure, and **(ii) non-heritable survival** where re-growth yields a population similar to the original. A recent EcoSal Plus review reiterates that “**A hallmark of persistence is the biphasic killing curve**” and that the persister state is “**of transient nature**” (shore2024typeitoxinantitoxin pages 18-20). In a 2024 BMC Microbiology review, persisters are described as having “**the same minimum inhibitory concentration (MIC) as the susceptible**” population, distinguishing them from resistant cells (yuan2024molecularmechanismand pages 3-6).

**Boundary cases / nearby traits to exclude or mark carefully.**
- **Resistance**: genetically acquired, population grows at antibiotic concentrations that kill susceptible cells; typically **elevated MIC** and heritable (shore2024typeitoxinantitoxin pages 18-20, yuan2024molecularmechanismand pages 3-6).
- **Tolerance**: slower killing at lethal antibiotic concentrations, often driven by slowed growth; importantly, this review emphasizes that “**tolerance is for the microbiota as a whole**” whereas persisters are a subpopulation (yuan2024molecularmechanismand pages 3-6). Some mechanistic studies measure “tolerance” rather than persister frequency; these edges should be curated as tolerance-related unless persister assays are shown.
- **VBNC**: dormant and non-culturable on standard media; recovery may require specific stimuli. The review notes that “**recovery of VBNC often requires… specific factors, such as pyruvate and glutamate**” (yuan2024molecularmechanismand pages 3-6). Conflation with persisters should be avoided unless the experimental definition is explicit.

## 1) Key concepts and current understanding (mechanistic modules)

### 1.1 Stress response control and signaling
**Stringent response/(p)ppGpp** is frequently positioned as a central integrator of nutrient limitation, stress physiology, and growth arrest programs in persistence models (shore2024typeitoxinantitoxin pages 18-20, yuan2024molecularmechanismand pages 3-6). In the Brucella system below, a stringent-response enzyme causally regulates a TA module that increases persister formation (liu2024the(p)ppgppsynthetase pages 9-11).

### 1.2 Toxin–antitoxin (TA) modules as persister “switches” (with ongoing debate)
Recent reviews remain explicit that multiple factors can contribute to persister formation (stationary phase regulators, (p)ppGpp, oxidative stress, low membrane potential/ATP depletion, nutrient limitation, etc.) and that **TA systems are implicated but not universally accepted as the sole explanation** (shore2024typeitoxinantitoxin pages 18-20). TA modules nonetheless provide curation-ready nodes because specific TA systems are shown experimentally to increase survival/persistence in defined contexts (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3, liu2024the(p)ppgppsynthetase pages 9-11).

### 1.3 Energetics and metabolism (ATP, NAD/NADP, PMF) as proximate mechanisms
Energy state appears in both “entry” and “maintenance” models. In Brucella, Rsh→TA regulation is accompanied by ATP decreases in rifampicin-tolerant persister formation (liu2024the(p)ppgppsynthetase pages 9-11), including explicit ATP measurements (Figures 9–10) (liu2024the(p)ppgppsynthetase media e87841c0, liu2024the(p)ppgppsynthetase media 322feabc). In Pseudomonas aeruginosa, a TA toxin generates drug-tolerant phenotypes via targeted depletion of NAD/NADP (santi2024toxinmediateddepletionof pages 3-4).

In parallel, a 2024 mini-review synthesizes recent work arguing that long-term phenotypic tolerance/persistence likely requires **active defense** (e.g., efflux, repair) supported by **maintenance of proton motive force (PMF)**; it states that “**persisters still actively generated PMF by undergoing a certain level of oxidative phosphorylation**” after starvation and that deletion of electron transport chain components can lead to “**rapid and complete killing of persisters**” in cited work (wan2024protonmotiveforce pages 6-7). Because this is review-level synthesis, its edges should be curated with a weaker evidence code unless the cited primary papers are also curated.

## 2) Recent developments (2023–2024) prioritized for curation

### 2.1 (p)ppGpp synthetase Rsh → mbcTA TA module → ATP decrease → rifampicin-tolerant persisters (*Brucella abortus*)
A 2024 Frontiers in Microbiology primary paper provides a direct mechanistic chain suitable for a TraitMech graph in a specific organism/condition. The authors conclude: “**the (p)ppGpp synthetase Rsh promotes persister cell formation by positive regulation of mbcTA after rifampicin exposure in stationary phase**” (liu2024the(p)ppgppsynthetase pages 9-11). They further report ATP differences: “**the Δrsh mutant in stationary phase exhibited an increase in ATP levels but overexpression of the mbcTA promoter in this background reduced ATP levels**” (liu2024the(p)ppgppsynthetase pages 9-11), and interpret the phenotype as “**associated with a decrease in ATP concentrations**” (liu2024the(p)ppgppsynthetase pages 9-11).

**Statistics/data:** The ATP measurements are presented explicitly in Figure 9 (group comparisons across wild-type, Δrsh, and Δrsh-mbcTAp) (liu2024the(p)ppgppsynthetase media e87841c0). A mechanistic summary schematic is presented in Figure 10 (Rsh regulation of mbcTA with ATP decrease during persister formation) (liu2024the(p)ppgppsynthetase media 322feabc).

### 2.2 TA toxin NatT drives NAD+/NADP+ depletion and large survival increases under antibiotics (*Pseudomonas aeruginosa*)
A 2024 EMBO Journal paper demonstrates a metabolic-toxin mechanism: “**NatT is a NAD+/NADP+ phosphorylase, which leads to the depletion of both cofactors**” (santi2024toxinmediateddepletionof pages 3-4). It also reports very large antibiotic survival differences: stationary-phase dilution into antibiotic-containing medium showed “**up to 10,000-fold increased survival compared to wild-type**” while MIC/resistance levels were not increased (santi2024toxinmediateddepletionof pages 3-4). The authors emphasize condition dependence: NatT-mediated tolerance was “**strongly increased when cells entered the stationary phase, indicating that NatT-mediated tolerance is coupled to nutrient limitations**” (santi2024toxinmediateddepletionof pages 3-4).

**Curation note:** This study uses “tolerance/survival” language in the excerpt; unless the full text operationally defines persisters (e.g., biphasic killing, regrowth phenotype), curate NatT edges as **drug tolerance / persister-like survival** with uncertainty.

### 2.3 Phage attack induces persistence via TA system MqsR/MqsA/MqsC (*E. coli*) — a 2023–2024 expansion of triggers
A Microbiology Spectrum paper (published 2023-12-06; issue dated 2024) reports a novel trigger class (phage attack) linked to persistence: “**persister cells… are formed and survive using the… toxin/antitoxin system MqsR/MqsA/MqsC to inhibit T2 phage**” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3). The study also reports large phage-inhibition effects: MqsR/MqsA/MqsC inhibited T2 phage by “**105-fold**” and reduced titers by “**3,000-fold**” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3). The authors generalize: “**a phage attack invokes a stress response… which leads to persistence**” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3).

**Application relevance:** The paper explicitly links this to phage therapy, stating results “**imply that if phage therapy is to be successful, anti-persister compounds need to be administered along with phages**” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3).

### 2.4 Convergent persister cell states and causal driver identification (systems biology; *E. coli*)
A 2024 Nature paper provides single-cell and genetic dissection evidence for convergent persister states across models. It reports that “**ampicillin treatment increased persister cluster occupancy fourfold and made persisters the most abundant cell type**” in their atlas (blattman2024identificationandgenetic pages 4-5). This is valuable for defining transcriptional-state nodes upstream/downstream of persister formation and for prioritizing driver genes (e.g., proteostasis/regulators) for follow-up curation.

## 3) Candidate causal-graph entities (nodes) for `persister_cell_formation.yaml`

### 3.1 Phenotype/assay nodes
- Persister cell formation (METPO:traitmech:000082)
- Biphasic killing curve (assay readout; label-only) (shore2024typeitoxinantitoxin pages 18-20)
- Same MIC as susceptible (scope constraint; label-only) (yuan2024molecularmechanismand pages 3-6)

### 3.2 Environmental & experimental factors
- Antibiotic exposure: rifampicin, enrofloxacin; tobramycin, ciprofloxacin; ampicillin (label-only) (liu2024the(p)ppgppsynthetase pages 9-11, santi2024toxinmediateddepletionof pages 3-4, blattman2024identificationandgenetic pages 4-5)
- Stationary phase / nutrient limitation / starvation (label-only) (liu2024the(p)ppgppsynthetase pages 9-11, santi2024toxinmediateddepletionof pages 3-4, wan2024protonmotiveforce pages 6-7)
- Phage attack (label-only) (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3)
- Intracellular macrophage milieu (RAW264.7 context; label-only) (liu2024the(p)ppgppsynthetase pages 9-11)

### 3.3 Molecular mechanisms / pathways
- Stringent response alarmone (p)ppGpp (label-only) (liu2024the(p)ppgppsynthetase pages 9-11, shore2024typeitoxinantitoxin pages 18-20)
- Proton motive force (PMF) (label-only) and oxidative phosphorylation/ETC (label-only) (wan2024protonmotiveforce pages 6-7)

### 3.4 Genes/proteins/complexes (label-only unless curated in organism-specific subgraphs)
- Rsh (p)ppGpp synthetase; *Brucella abortus*) (liu2024the(p)ppgppsynthetase pages 9-11)
- mbcTA TA module (RES-Xre type II TA locus; *Brucella*) (liu2024the(p)ppgppsynthetase pages 9-11)
- NatR–NatT TA system; NatT toxin (*P. aeruginosa*) (santi2024toxinmediateddepletionof pages 3-4)
- MqsR/MqsA/MqsC tripartite TA system (*E. coli* C496_10) (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3)
- PspA, nuoL, ndh (PMF/ETC-related tolerance maintenance; review-synthesized) (wan2024protonmotiveforce pages 6-7)

### 3.5 Chemicals/metabolites (grounded)
- ATP (CHEBI:15422) (liu2024the(p)ppgppsynthetase pages 9-11)
- NAD+ (CHEBI:57540) and NADP+ (CHEBI:58349) (santi2024toxinmediateddepletionof pages 3-4)
- Pyruvate (CHEBI:15361) and L-glutamate (CHEBI:29985) (VBNC recovery context) (yuan2024molecularmechanismand pages 3-6)

## 4) Evidence-backed candidate causal edges (triples)

The following table is designed to be directly translated into curated edges for a TraitMech causal graph; each includes a verbatim snippet, DOI, and uncertainty notes.

| Edge (subject–predicate–object) | Evidence snippet (verbatim quote) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs) |
|---|---|---|---|---|
| Rsh/(p)ppGpp synthetase — positively regulates — mbcTA promoter/activity | “the (p)ppGpp synthetase Rsh promotes persister cell formation by positive regulation of mbcTA after rifampicin exposure in stationary phase.” (liu2024the(p)ppgppsynthetase pages 9-11) | 10.3389/fmicb.2024.1395504 (2024), https://doi.org/10.3389/fmicb.2024.1395504 | Strong primary evidence, but taxon/condition specific: *Brucella abortus*, stationary phase, rifampicin exposure. Subject may be grounded as Rsh rather than generic (p)ppGpp. | subject: label-only `Rsh`; object: label-only `mbcTA type II TA module` |
| mbcTA promoter overexpression — decreases — intracellular ATP level | “the Δrsh mutant in stationary phase exhibited an increase in ATP levels but overexpression of the mbcTA promoter in this background reduced ATP levels.” (liu2024the(p)ppgppsynthetase pages 9-11, liu2024the(p)ppgppsynthetase media e87841c0) | 10.3389/fmicb.2024.1395504 (2024), https://doi.org/10.3389/fmicb.2024.1395504 | Strong within-study evidence; promoter overexpression is assay-specific and may not equal native regulation strength. Figure 9 supports the ATP change. | subject: label-only `mbcTA promoter overexpression`; object: CHEBI:15422 (ATP) |
| decreased intracellular ATP level — associated with increased — rifampicin-tolerant persister cell formation | “the formation of stationary phase antibiotic-tolerant persister cells in B. abortus is associated with a decrease in ATP concentrations.” (liu2024the(p)ppgppsynthetase pages 9-11, liu2024the(p)ppgppsynthetase media 322feabc) | 10.3389/fmicb.2024.1395504 (2024), https://doi.org/10.3389/fmicb.2024.1395504 | Association is explicit; causal direction is inferred from study design/mechanistic model, so curate as uncertain if strict causality is required. | subject: CHEBI:15422 (ATP); object: METPO:traitmech:000082 |
| NatT toxin activity — depletes — NAD+ and NADP+ pools | “NatT is a NAD+/NADP+ phosphorylase, which leads to the depletion of both cofactors” (santi2024toxinmediateddepletionof pages 3-4) | 10.1038/s44318-024-00248-5 (2024), https://doi.org/10.1038/s44318-024-00248-5 | Strong primary evidence in *Pseudomonas aeruginosa*; biochemical mechanism demonstrated. | subject: label-only `NatT toxin`; object: CHEBI:57540 (NAD+), CHEBI:58349 (NADP+) |
| NatT toxin activity — increases — survival during antibiotic treatment / drug tolerance | “ectopic expression of natT from a plasmid increased P. aeruginosa survival during drug treatment without affecting growth rates” (santi2024toxinmediateddepletionof pages 3-4) | 10.1038/s44318-024-00248-5 (2024), https://doi.org/10.1038/s44318-024-00248-5 | Strong evidence for drug tolerance; mapping from tolerance to persister formation is plausible but should be marked uncertain unless explicitly assayed as persisters under curation criteria. | subject: label-only `NatT toxin`; object: label-only `drug tolerance` |
| nutrient limitation / stationary phase — increases — NatT-mediated tolerance | “NatT-mediated tolerance was low in rapidly growing cells but strongly increased when cells entered the stationary phase, indicating that NatT-mediated tolerance is coupled to nutrient limitations.” (santi2024toxinmediateddepletionof pages 3-4) | 10.1038/s44318-024-00248-5 (2024), https://doi.org/10.1038/s44318-024-00248-5 | Strong condition-dependent effect; useful environmental edge. | subject: GO:0007568 (aging/stationary-phase not exact; better label-only `nutrient limitation/stationary phase`); object: label-only `NatT-mediated drug tolerance` |
| MqsR/MqsA/MqsC TA system — induces — persister cell formation | “we show here that persister cells, i.e., transiently-tolerant, dormant, antibiotic-insensitive cells, are formed and survive using the Escherichia coli C496_10 tripartite toxin/antitoxin system MqsR/MqsA/MqsC to inhibit T2 phage.” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3) | 10.1128/spectrum.03388-23 (2024 issue; published 2023-12-06), https://doi.org/10.1128/spectrum.03388-23 | Strong primary evidence in *E. coli* C496_10 during phage attack; not antibiotic-triggered, so broader stress-induced persistence edge. | subject: label-only `MqsR/MqsA/MqsC TA system`; object: METPO:traitmech:000082 |
| phage attack — triggers — persistence / persister state | “Hence, a phage attack invokes a stress response similar to antibiotics, starvation, and oxidation, which leads to persistence” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3) | 10.1128/spectrum.03388-23 (2024 issue; published 2023-12-06), https://doi.org/10.1128/spectrum.03388-23 | Strong in this system; taxon- and phage-specific. Environmental factor edge. | subject: label-only `phage attack`; object: METPO:traitmech:000082 |
| PspA — maintains — proton motive force (PMF) during starvation-induced tolerance | “We found that the PspA protein was responsible for maintaining the PMF during nutrient starvation” (wan2024protonmotiveforce pages 6-7) | 10.1111/1751-7915.70042 (2024), https://doi.org/10.1111/1751-7915.70042 | Review-level synthesis citing prior experiments; not a new primary study in this excerpt. Good mechanistic support for tolerance-maintenance node, but weaker for direct persister formation edge. | subject: label-only `PspA`; object: GO:0015986 (proton motive force-driven ATP synthesis, approximate) / label-only `proton motive force` |
| persisters — actively generate — proton motive force via oxidative phosphorylation | “persisters still actively generated PMF by undergoing a certain level of oxidative phosphorylation, even after they had encountered complete nutrient starvation for 24 h.” (wan2024protonmotiveforce pages 6-7) | 10.1111/1751-7915.70042 (2024), https://doi.org/10.1111/1751-7915.70042 | Review-level summary; supports maintenance rather than initiation of persistence. | subject: METPO:traitmech:000082; object: label-only `proton motive force` |
| nuoL and ndh (ETC components) — mediate — tolerance formation | “the enzymes NADH dehydrogenase I and NADH dehydrogenase II, which are the key components of the ETC encoded by the genes nuoL and ndh ... play a key role in mediating tolerance formation” (wan2024protonmotiveforce pages 6-7) | 10.1111/1751-7915.70042 (2024), https://doi.org/10.1111/1751-7915.70042 | Review-level synthesis; direct edge is to tolerance, not necessarily persister formation. Consider curating as tolerance-maintenance unless supported by primary persister assay. | subject: label-only `nuoL`, label-only `ndh`; object: label-only `tolerance formation` |
| deletion of ETC components — causes rapid/complete killing of — persisters | “deletion of genes encoding the ETC components results in the rapid and complete killing of persisters” (wan2024protonmotiveforce pages 6-7) | 10.1111/1751-7915.70042 (2024), https://doi.org/10.1111/1751-7915.70042 | Strongly relevant to persister survival/maintenance, but from review text rather than directly quoted primary paper. | subject: label-only `ETC components`; object: METPO:traitmech:000082 |
| persister cells — have same MIC as — susceptible cells | “persisters had the same minimum inhibitory concentration (MIC) as the susceptible” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024), https://doi.org/10.1186/s12866-024-03628-3 | Definition/scope edge, not mechanistic. Important boundary condition distinguishing persistence from resistance. | subject: METPO:traitmech:000082; object: label-only `same MIC as susceptible cells` |
| resistant bacteria — have higher MIC than — susceptible/persister cells | “the MIC of resistant bacteria was significantly higher.” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024), https://doi.org/10.1186/s12866-024-03628-3 | Definition edge useful for excluding resistance from this trait scope. | subject: label-only `antibiotic resistance`; object: label-only `elevated MIC` |
| tolerance — applies to — whole population, not small subpopulation | “persisters are a smaller proportion of subpopulations in the microbiota, whereas tolerance is for the microbiota as a whole” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024), https://doi.org/10.1186/s12866-024-03628-3 | Scope/boundary edge distinguishing persistence from tolerance. | subject: label-only `antibiotic tolerance`; object: label-only `whole population phenotype` |
| VBNC state — differs from persisters by requiring — specific resuscitation factors | “persisters will gradually recover and proliferate, while the recovery of VBNC often requires the stimulation of some specific factors, such as pyruvate and glutamate” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024), https://doi.org/10.1186/s12866-024-03628-3 | Scope/boundary edge; useful warning against conflating dormancy states. | subject: label-only `VBNC state`; object: CHEBI:15361 (pyruvate), CHEBI:29985 (L-glutamate) |
| persistence — is characterized by — biphasic killing curve | “A hallmark of persistence is the biphasic killing curve” (shore2024typeitoxinantitoxin pages 18-20) | 10.1128/ecosalplus.esp-0025-2022 (2024), https://doi.org/10.1128/ecosalplus.esp-0025-2022 | Definition/assay edge; useful for curation of phenotype readout. | subject: METPO:traitmech:000082; object: label-only `biphasic killing curve` |


*Table: This table compiles curation-ready candidate causal edges for persister cell formation using only the gathered evidence context. It highlights mechanistic links, environmental triggers, and key scope-defining distinctions needed for TraitMech graph curation.*

## 5) Current applications and real-world implementations

1. **Combination/adjunct strategies targeting persister physiology.** Recent mechanistic work supports targeting metabolic nodes that enable persister survival (ATP homeostasis, NAD/NADP pools, PMF maintenance) as adjunctive therapy concepts (liu2024the(p)ppgppsynthetase pages 9-11, santi2024toxinmediateddepletionof pages 3-4, wan2024protonmotiveforce pages 6-7).
2. **Phage therapy context.** Phage attack can induce a persister state via TA-mediated dormancy, and the authors propose combining phages with anti-persister compounds (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3). This is a concrete translational implication for phage-therapy design.
3. **Biofilm and chronic infection relevance (context).** Persistence is linked in reviews to treatment failure and relapse, and repeated therapy can select high-persistence (Hip) phenotypes (shore2024typeitoxinantitoxin pages 18-20). This motivates clinical assay development and anti-persister interventions.

## 6) Expert opinions & synthesis (authoritative sources)

- **No unifying model yet; growth inhibition is a common theme.** The EcoSal Plus review states that “**there is still no unifying model that describes the generation or physiological state of persister cells**” and enumerates multiple candidate drivers including (p)ppGpp, oxidative stress, low membrane potential/ATP depletion, nutrient limitation, and others (shore2024typeitoxinantitoxin pages 18-20). This supports a graph design where multiple upstream stresses converge on a reduced-growth/altered-energetics state.
- **Active maintenance mechanisms may be required.** The PMF mini-review emphasizes that decreased metabolism alone may not explain long-lasting tolerance, highlighting the importance of PMF generation/maintenance for defense and repair systems (wan2024protonmotiveforce pages 6-7). Curationally, this suggests separating **persister entry** edges (growth arrest) from **persister maintenance** edges (PMF-supported repair/efflux).

## 7) Statistics / quantitative findings (from recent studies)

- **Up to 10,000-fold survival increase** in *P. aeruginosa* natTE29D mutant during antibiotic exposure in stationary-phase dilution experiments (santi2024toxinmediateddepletionof pages 3-4).
- **Phage inhibition effects** in *E. coli* with MqsR/MqsA/MqsC: “105-fold” inhibition and “3,000-fold” reduction in T2 titers (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3).
- **Fourfold increase in persister cluster occupancy** following ampicillin treatment in a 2024 Nature single-cell atlas of persister states (blattman2024identificationandgenetic pages 4-5).
- **ATP level differences** across wild-type/Δrsh/Δrsh-mbcTAp in rifampicin-tolerant stationary-phase persisters (Figure 9) (liu2024the(p)ppgppsynthetase media e87841c0).

## 8) Warnings (claims to curate cautiously)

1. **TA systems as universal persister generators remain debated.** The EcoSal Plus review explicitly notes that TA involvement has been “challenged” and remains an “ongoing scientific debate” (shore2024typeitoxinantitoxin pages 18-20). Curate TA→persister edges with taxon/condition qualifiers.
2. **Tolerance vs persistence labeling.** Some primary excerpts use “tolerance” and survival without explicitly demonstrating biphasic killing and non-heritable regrowth. For NatT-related edges, curate as **drug tolerance** or **persister-like survival**, unless full-text confirmation supports persister assays (santi2024toxinmediateddepletionof pages 3-4).
3. **Review-derived mechanistic edges (PMF/ETC) are weaker than primary evidence.** The PMF/ETC claims are presented as synthesis (wan2024protonmotiveforce pages 6-7) and should be tagged as review evidence unless the underlying primary study is added and quoted.
4. **Species- and context-specific mechanisms.** Strong edges such as Rsh→mbcTA→ATP→persisters are shown in *Brucella abortus* stationary phase under rifampicin exposure (liu2024the(p)ppgppsynthetase pages 9-11). Such edges should be curated with explicit NCBITaxon and context qualifiers.

---

## DOI-first bibliography (2023–2024; with URLs and publication dates where available)

1. **Liu X**, et al. *The (p)ppGpp synthetase Rsh promotes rifampicin tolerant persister cell formation in Brucella abortus by regulating the type II toxin-antitoxin module mbcTA.* **Frontiers in Microbiology** (May 2024). DOI: **10.3389/fmicb.2024.1395504**. https://doi.org/10.3389/fmicb.2024.1395504 (liu2024the(p)ppgppsynthetase pages 9-11, liu2024the(p)ppgppsynthetase media e87841c0, liu2024the(p)ppgppsynthetase media 322feabc)
2. **Santi I**, et al. *Toxin-mediated depletion of NAD and NADP drives persister formation in a human pathogen.* **The EMBO Journal** (Nov 2024). DOI: **10.1038/s44318-024-00248-5**. https://doi.org/10.1038/s44318-024-00248-5 (santi2024toxinmediateddepletionof pages 3-4)
3. **Fernández-García L**, et al. *Toxin/antitoxin systems induce persistence and work in concert with restriction/modification systems to inhibit phage.* **Microbiology Spectrum** (Published **6 Dec 2023**; issue Jan 2024). DOI: **10.1128/spectrum.03388-23**. https://doi.org/10.1128/spectrum.03388-23 (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3)
4. **Shore SFH**, et al. *Type I toxin-antitoxin systems in bacteria: from regulation to biological functions.* **EcoSal Plus** (Dec 2024). DOI: **10.1128/ecosalplus.esp-0025-2022**. https://doi.org/10.1128/ecosalplus.esp-0025-2022 (shore2024typeitoxinantitoxin pages 18-20)
5. **Yuan S**, et al. *Molecular mechanism and application of emerging technologies in study of bacterial persisters.* **BMC Microbiology** (Nov 2024). DOI: **10.1186/s12866-024-03628-3**. https://doi.org/10.1186/s12866-024-03628-3 (yuan2024molecularmechanismand pages 3-6)
6. **Wan Y**, et al. *Proton motive force and antibiotic tolerance in bacteria.* **Microbial Biotechnology** (Nov 2024). DOI: **10.1111/1751-7915.70042**. https://doi.org/10.1111/1751-7915.70042 (wan2024protonmotiveforce pages 6-7)
7. **Blattman SB**, et al. *Identification and genetic dissection of convergent persister cell states.* **Nature** (Nov/Dec 2024). DOI: **10.1038/s41586-024-08124-2**. https://doi.org/10.1038/s41586-024-08124-2 (blattman2024identificationandgenetic pages 4-5)
8. **Bustamante P**, et al. *Contribution of Toxin–Antitoxin Systems to Adherent-Invasive E. coli Pathogenesis.* **Microorganisms** (Jun 2024). DOI: **10.3390/microorganisms12061158**. https://doi.org/10.3390/microorganisms12061158 (bustamante2024contributionoftoxin–antitoxin pages 18-19)


References

1. (shore2024typeitoxinantitoxin pages 18-20): Selene F. H. Shore, Florian H. Leinberger, Elizabeth M. Fozo, and Bork A. Berghoff. Type i toxin-antitoxin systems in bacteria: from regulation to biological functions. EcoSal Plus, Dec 2024. URL: https://doi.org/10.1128/ecosalplus.esp-0025-2022, doi:10.1128/ecosalplus.esp-0025-2022. This article has 27 citations.

2. (yuan2024molecularmechanismand pages 3-6): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 20 citations and is from a peer-reviewed journal.

3. (liu2024the(p)ppgppsynthetase pages 9-11): Xiaofang Liu, Pingping Wang, Ningqiu Yuan, Yunyi Zhai, Yuanhao Yang, Mingyue Hao, Mingxing Zhang, Dong Zhou, Wei Liu, Yaping Jin, and Aihua Wang. The (p)ppgpp synthetase rsh promotes rifampicin tolerant persister cell formation in brucella abortus by regulating the type ii toxin-antitoxin module mbcta. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1395504, doi:10.3389/fmicb.2024.1395504. This article has 11 citations and is from a peer-reviewed journal.

4. (fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3): Laura Fernández-García, Sooyeon Song, Joy Kirigo, Michael E. Battisti, Maiken E. Petersen, María Tomás, and Thomas K. Wood. Toxin/antitoxin systems induce persistence and work in concert with restriction/modification systems to inhibit phage. Microbiology Spectrum, Jan 2024. URL: https://doi.org/10.1128/spectrum.03388-23, doi:10.1128/spectrum.03388-23. This article has 25 citations and is from a domain leading peer-reviewed journal.

5. (liu2024the(p)ppgppsynthetase media e87841c0): Xiaofang Liu, Pingping Wang, Ningqiu Yuan, Yunyi Zhai, Yuanhao Yang, Mingyue Hao, Mingxing Zhang, Dong Zhou, Wei Liu, Yaping Jin, and Aihua Wang. The (p)ppgpp synthetase rsh promotes rifampicin tolerant persister cell formation in brucella abortus by regulating the type ii toxin-antitoxin module mbcta. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1395504, doi:10.3389/fmicb.2024.1395504. This article has 11 citations and is from a peer-reviewed journal.

6. (liu2024the(p)ppgppsynthetase media 322feabc): Xiaofang Liu, Pingping Wang, Ningqiu Yuan, Yunyi Zhai, Yuanhao Yang, Mingyue Hao, Mingxing Zhang, Dong Zhou, Wei Liu, Yaping Jin, and Aihua Wang. The (p)ppgpp synthetase rsh promotes rifampicin tolerant persister cell formation in brucella abortus by regulating the type ii toxin-antitoxin module mbcta. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1395504, doi:10.3389/fmicb.2024.1395504. This article has 11 citations and is from a peer-reviewed journal.

7. (santi2024toxinmediateddepletionof pages 3-4): Isabella Santi, Raphael Dias Teixeira, Pablo Manfredi, Hector Hernandez Gonzalez, Daniel C. Spiess, Guillaume Mas, Alexander Klotz, Andreas Kaczmarczyk, Nicola Zamboni, Sebastian Hiller, and Urs Jenal. Toxin-mediated depletion of nad and nadp drives persister formation in a human pathogen. The EMBO Journal, 43:5211-5236, Sep 2024. URL: https://doi.org/10.1038/s44318-024-00248-5, doi:10.1038/s44318-024-00248-5. This article has 8 citations.

8. (wan2024protonmotiveforce pages 6-7): Yingkun Wan, Jiaqi Zheng, Edward Wai‐Chi Chan, and Sheng Chen. Proton motive force and antibiotic tolerance in bacteria. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70042, doi:10.1111/1751-7915.70042. This article has 15 citations and is from a peer-reviewed journal.

9. (blattman2024identificationandgenetic pages 4-5): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636(8042):438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 41 citations and is from a highest quality peer-reviewed journal.

10. (bustamante2024contributionoftoxin–antitoxin pages 18-19): Paula Bustamante, María Núria Ramos-Corominas, and Margarita Martinez-Medina. Contribution of toxin–antitoxin systems to adherent-invasive e. coli pathogenesis. Microorganisms, 12:1158, Jun 2024. URL: https://doi.org/10.3390/microorganisms12061158, doi:10.3390/microorganisms12061158. This article has 13 citations.