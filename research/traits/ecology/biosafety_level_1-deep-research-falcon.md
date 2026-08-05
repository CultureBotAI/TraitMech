---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:47:33.478987'
end_time: '2026-08-03T22:55:48.255387'
duration_seconds: 494.78
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 1
  trait_identifier: METPO:1001102
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that poses minimal potential hazard to laboratory
    workers and the environment, requiring only standard microbiological practices.
  parent_traits: METPO:1001101
  synonyms: '1'
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports the absence or low expression of virulence factors
    in BSL-1 agents (non-pathogenic to healthy adults).)'
  causal_graph_summary: 'biosafety_level_1_minimal_hazard: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 1
- **METPO identifier:** METPO:1001102
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses minimal potential hazard to laboratory workers and the environment, requiring only standard microbiological practices.
- **Parent traits:** METPO:1001101
- **Synonyms:** 1
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the absence or low expression of virulence factors in BSL-1 agents (non-pathogenic to healthy adults).)
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **biosafety level 1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_1.yaml`.

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
- **Trait label:** biosafety level 1
- **METPO identifier:** METPO:1001102
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses minimal potential hazard to laboratory workers and the environment, requiring only standard microbiological practices.
- **Parent traits:** METPO:1001101
- **Synonyms:** 1
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the absence or low expression of virulence factors in BSL-1 agents (non-pathogenic to healthy adults).)
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **biosafety level 1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_1.yaml`.

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


# Curation-focused research report: biosafety level 1

## Executive interpretation

**Trait:** biosafety level 1 (BSL-1), **METPO:1001102**, ecology class.

BSL-1 should be modeled primarily as a **protocol-level containment outcome**, not as a unitary microbial phenotype. It describes work with agents presenting minimal potential hazard, generally organisms not known to consistently cause disease in healthy immunocompetent adults, under standard microbiological practices. Risk Group 1 (RG1), by contrast, characterizes an agent’s intrinsic hazard. The containment assignment additionally depends on the manipulation, concentration and volume, aerosol or splash potential, exposure route, host range, genetic modifications, personnel, and available controls. ASM teaching guidance explicitly distinguishes risk group from biosafety level and illustrates that required containment changes with the procedure rather than following organism identity alone. (biosafety2013biosafetyguidelinesfor pages 1-2, gao2024frombiosafetyto pages 5-6)

Accordingly, a defensible TraitMech graph should have two linked layers:

1. **Agent-hazard layer:** limited pathogenicity, toxin production, adhesion/invasion, immune evasion, host colonization, persistence, antimicrobial resistance, and horizontal gene transfer.
2. **Protocol/control layer:** experimental operation, exposure generation, standard practices, physical containment, decontamination, and—where organisms are engineered—auxotrophy, kill switches, or genetic firewalls.

The graph should end in an intermediate node such as **“minimal assessed hazard under specified laboratory conditions”**, which supports BSL-1 assignment. It should not imply that any single gene deletion or safety circuit automatically makes an organism BSL-1.

## 1. Trait scope and boundaries

### Positive scope

The trait represents an **assay- and context-observed biorisk classification**: work can be conducted safely using basic laboratory facilities and standard microbiological practices because the combined agent and procedural risk is minimal. Typical BSL-1 settings include basic teaching and research laboratories. The recent historical review describes BSL-1 as applying to minimal/low-risk agents unlikely to cause disease in healthy adults, with general or standard practices. (gao2024frombiosafetyto pages 5-6)

### Nearby concepts that must remain separate

- **Risk Group 1:** an agent-hazard category; it is evidence feeding into—but not synonymous with—BSL-1.
- **Nonpathogenicity/avirulence:** microbial phenotypes that can lower hazard but do not determine containment independently.
- **GRAS or qualified-presumption-of-safety status:** food/regulatory safety concepts, not laboratory containment assignments.
- **Attenuation:** a strain-relative reduction in virulence; attenuated derivatives still require procedure-specific assessment.
- **Biocontainment:** engineered limitation of survival, replication, or gene flow. It can reduce risk but does not itself establish BSL-1.
- **BSL-2:** the next containment level, used for moderate-hazard agents or activities associated with human disease and additional exposure controls. (gao2024frombiosafetyto pages 5-6)

### Boundary cases

A nominally low-risk strain should not be assumed to remain BSL-1 when it contains an expressed toxin, virulence determinant, broad-host-range vector, clinically important resistance marker, or a modification increasing survival, host range, aerosol stability, or environmental persistence. Conversely, a strain with an auxotrophy or kill switch is not necessarily BSL-1 if its payload or procedure creates a moderate hazard. Host susceptibility is also a boundary: “not known to cause disease in healthy adults” does not mean incapable of opportunistic infection in immunocompromised persons.

## 2. Candidate nodes grouped by type

### Trait and assessment nodes

- **biosafety level 1** — METPO:1001102.
- **minimal assessed laboratory hazard** — label-only candidate.
- **risk-group classification** — label-only candidate.
- **protocol-specific microbial risk assessment** — label-only candidate.
- **worker exposure** and **environmental exposure** — label-only candidates.
- **containment escape frequency** — assay measurement; label-only candidate.

### Organisms and chassis

Use strain-level NCBITaxon identifiers only after confirming the exact strain record.

- *Escherichia coli* K-12 derivatives — model/industrial chassis; strain-specific.
- *Escherichia coli* Nissle 1917 — probiotic and therapeutic chassis; not interchangeable with K-12.
- *Lactococcus lactis* — food/therapeutic chassis.
- *Saccharomyces cerevisiae* — industrial and teaching yeast chassis.
- *Bacteroides thetaiotaomicron* and *B. ovatus* — engineered gut-therapeutic chassis; clinical context does not imply BSL-1 laboratory handling.
- Cyanobacterial and *Pseudomonas putida* synthetic-auxotrophy systems — taxon-specific experimental examples.

### Genes, proteins, and complexes

- **thyA / thymidylate synthase** — EC:2.1.1.45; deletion can create thymidine dependence.
- **dapA / 4-hydroxy-tetrahydrodipicolinate synthase** — EC:4.3.3.7; inactivation is used in diaminopimelate-dependent therapeutic strains.
- **relA** — strain-dependent contributor to laboratory-chassis physiology; do not curate as a universal BSL-1 determinant.
- **phosphate transporters** — label or verified organism-specific gene identifiers; knockout can support phosphite dependence.
- **fluoride exporters** — organism-specific genes; knockout increases environmental fluoride sensitivity.
- **aminoacyl-tRNA synthetase/orthogonal tRNA pair** — enables noncanonical-amino-acid dependence.
- **Cas nuclease + guide RNA complex** — candidate GO grounding: GO:0004519 for endonuclease activity; use a more specific term only after construct confirmation.
- **toxin–antitoxin module**, **suicide gene**, **essential-gene control circuit** — label-only unless a construct is specified.
- **virulence factors**, including toxins, adhesins, invasion systems and immune-evasion proteins — curate only as specific strain-specific absences or deletions, not as a generic “virulence-factor gene.”

### Processes and molecular functions

- **pathogenesis** — GO:0009405.
- **toxin activity** — GO:0090729.
- **cell adhesion** — GO:0007155.
- **DNA-mediated transformation** — GO:0009294, where specifically applicable.
- Host invasion, immune evasion, colonization, biofilm formation, environmental persistence, antimicrobial resistance, and horizontal gene transfer — use verified specific ontology terms during YAML implementation; label-only is safer where the exact relation is unclear.
- DNA double-strand break generation, essential-gene expression, translation, replication, cell death, and growth arrest.

### Chemicals, nutrients, and environmental factors

- **thymidine** — CHEBI:17748.
- **phosphite** — verify protonation-specific ChEBI term before curation.
- **noncanonical amino acid (ncAA)** — class node; ground individual compounds separately.
- **3-nitro-L-tyrosine**, **3-iodo-L-tyrosine**, **O-methyl-L-tyrosine**, **p-benzoyl-L-phenylalanine**, **N-acetyl-L-lysine**, and synthetic phenylalanine derivatives — confirm exact ChEBI stereochemical entries before use.
- **benzothiazole-dependent ligand** — the exact SLiDE ligand must be recovered from the primary construct paper before chemical grounding.
- **estradiol** — CHEBI:16469; used in a yeast essential-gene control example.
- Environmental nutrient availability, microbial cross-feeding, aerosol-generating manipulation, culture volume/concentration, sharps, surface contamination, and decontamination.

### Cellular localizations and structures

No organelle is a general determinant of BSL-1. Relevant construct-specific localizations include cytosolic translation machinery, chromosome, plasmid, cell envelope, extracellular environment, host-cell surface, and host intracellular compartment. These should only be added when required by a particular mechanistic edge.

## 3. Candidate causal edges

The following table separates intrinsic hazard, engineered safeguards, exposure controls, and failure modes. “Supports BSL-1” means evidence contributing to a risk assessment—not a sufficient or automatic assignment.

| subject | predicate | object | evidence/mechanism | scope/uncertainty | DOI |
|---|---|---|---|---|---|
| low virulence-factor repertoire | decreases | host damage / disease potential | Review evidence notes BSL-1 aligns with agents “unlikely to cause disease in healthy adults”; EcN “lacks typical virulence factors found in UPEC,” supporting reduced pathogenic potential relative to pathogenic strains (gao2024frombiosafetyto pages 5-6, gomeztatay2024xenobiologyforthe pages 4-5) | Inferred for generic BSL-1; strongest when strain-specific virulence-factor absence is demonstrated | 10.3390/laboratories1030013; 10.3390/cancers16172971 |
| essential-gene knockout / auxotrophy | causes | dependence on exogenous nutrient / metabolite | Auxotrophy-based containment works by deleting essential functions so growth requires supplied metabolite; examples include thymidylate synthase knockout causing thymidine dependence and phosphite-dependent cyanobacteria after phosphate transporter knockout (hoffmann2023safetybydesign pages 7-8) | Mechanism general for engineered biocontainment, not intrinsic to all natural BSL-1 microbes | 10.1016/j.isci.2023.106165 |
| exogenous nutrient dependence | decreases | growth outside permissive environment | Synthetic auxotrophy limits growth when required nutrient is absent; laboratory target stringency for contained systems is <10^-8 escape/survival, and ligand-dependent essential-gene systems can reach <3 × 10^-11 under lab conditions (hoffmann2023safetybydesign pages 7-8, pavao2023biocontainmenttechniquesand pages 5-7) | Lab-assay specific; not sufficient alone for BSL-1 assignment | 10.1016/j.isci.2023.106165; 10.3390/fermentation9040341 |
| ncAA-dependent essential proteins | enables | synthetic auxotrophy | Dependency on non-canonical amino acids in essential genes creates “addiction to ncAAs”; reported escape frequencies include ~10^-8, <10^-10, <10^-11, and <10^-12 depending on design; TAG recoding in 22 essential genes gave undetectable escape in culture media (gomeztatay2024xenobiologyforthe pages 4-5, gomeztatay2024xenobiologyforthe pages 5-7, pavao2023biocontainmenttechniquesand pages 5-7) | Strong for engineered strains only; assay/system dependent | 10.3390/life14080996; 10.3390/fermentation9040341 |
| synthetic auxotrophy | decreases | escape / environmental persistence | Orthogonal translation systems placing ncAA dependence in essential genes reduced escape to <10^-11 in E. coli; control of essential genes is more mutation-resistant than suicide-based systems (hoffmann2023safetybydesign pages 8-10) | Engineered-biocontainment edge, not a direct BSL-1 definition | 10.1016/j.isci.2023.106165 |
| toxin-antitoxin system / suicide switch | causes | death under nonpermissive condition | Active containment uses suicide genes and toxin-antitoxin systems triggered under nonpermissive conditions to induce cell death (hoffmann2023safetybydesign pages 7-8) | General mechanism from review; specific toxins often not detailed in gathered evidence | 10.1016/j.isci.2023.106165 |
| CRISPR kill switch | causes | death / loss of viability under nonpermissive condition | Cas proteins with guide RNAs targeting repetitive regions serve as killing effectors via double-strand breaks; CRISPR-based safeguards are cited as genetically stable kill-switch approaches (hoffmann2023safetybydesign pages 7-8, pavao2023biocontainmenttechniquesand pages 13-15) | Some evidence is review-level; exact construct performance varies by design | 10.1016/j.isci.2023.106165; 10.3390/fermentation9040341 |
| death under nonpermissive condition | decreases | survival outside containment | Kill switches are intended to reduce viability when permissive signal is absent; this is the core containment logic of active systems (hoffmann2023safetybydesign pages 7-8, gomeztatay2024xenobiologyforthe pages 7-8) | Mechanistically strong but design-dependent and susceptible to mutation | 10.1016/j.isci.2023.106165; 10.3390/life14080996 |
| orthogonal genetic code / genetic firewall | causes | transferred genes to be nonfunctional in wild recipients | Reassigned codons and orthogonal translation make transferred genes nonfunctional in natural organisms; genetic-code swapping and ncAA-dependent coding act as barriers to HGT (hoffmann2023safetybydesign pages 8-10, gomeztatay2024xenobiologyforthe pages 5-7, pavao2023biocontainmenttechniquesand pages 5-7) | Strong for engineered systems; real-world open-environment validation still limited | 10.1016/j.isci.2023.106165; 10.3390/life14080996; 10.3390/fermentation9040341 |
| nonfunctional transferred genes in wild recipients | decreases | horizontal gene transfer impact | Semantic/orthogonal biocontainment reduces functional expression after transfer, thereby reducing HGT consequences rather than transfer events per se (hoffmann2023safetybydesign pages 8-10, gomeztatay2024xenobiologyforthe pages 5-7) | Important nuance: reduces functional HGT, not necessarily DNA movement itself | 10.1016/j.isci.2023.106165; 10.3390/life14080996 |
| cross-feeding / environmental nutrient availability | rescues | auxotrophy | Reviews explicitly caution that auxotrophies may fail if required nutrients exist in natural environments or via cross-feeding (hoffmann2023safetybydesign pages 7-8, siguenza2024engineeredbacterialtherapeutics pages 6-7) | Strong caution; should be curated as antagonistic edge and marked context-dependent | 10.1016/j.isci.2023.106165; 10.1016/j.trecan.2024.04.001 |
| escape mutation | disables | kill switch / containment circuit | Escape mutations under permissive conditions can eliminate containment; the Deadman kill switch showed escape within days of passaging (hoffmann2023safetybydesign pages 8-10) | Strong cautionary edge; system-specific but broadly relevant | 10.1016/j.isci.2023.106165 |
| standard microbiological practices | decreases | worker / environmental exposure | BSL-1 is used with “general/standard practices”; standard operating procedures and good laboratory practices are central exposure controls (gao2024frombiosafetyto pages 5-6, biosafety2013biosafetyguidelinesfor pages 1-2) | This is a laboratory-practice edge, not a microbial intrinsic mechanism | 10.3390/laboratories1030013; 10.1128/jmbe.v14i1.531 |
| low-risk agent + low-risk procedure | supports assignment of | biosafety level 1 | BSL assignment depends on organism risk group plus procedure/equipment context; teaching guidance shows biosafety levels are distinct from risk groups and depend on laboratory procedures, with low-risk work using BSL-1 (biosafety2013biosafetyguidelinesfor pages 1-2, gao2024frombiosafetyto pages 5-6) | Strongly supported; protocol-specific, not organism-identity-only | 10.1128/jmbe.v14i1.531; 10.3390/laboratories1030013 |


*Table: This table compiles compact, evidence-backed candidate causal edges for a TraitMech representation of biosafety level 1 and closely related engineered biocontainment mechanisms. It is useful for separating intrinsic low-hazard features from protocol-dependent containment and for flagging limitations such as cross-feeding and escape mutations.*

### Recommended core graph for `biosafety_level_1.yaml`

A conservative first implementation could use the following backbone:

1. `limited demonstrated pathogenic potential -> decreases -> agent-intrinsic hazard`
2. `absence of relevant toxin/virulence activity -> decreases -> host damage potential`
3. `low-aerosol, low-splash procedure -> decreases -> exposure probability`
4. `standard microbiological practices -> decreases -> worker/environmental exposure`
5. `agent-intrinsic hazard + exposure probability -> determines -> assessed protocol risk`
6. `minimal assessed protocol risk -> supports_assignment_of -> METPO:1001102`

Edges 1–2 require strain-specific phenotypic or genomic evidence. Edges 3–6 best represent the actual semantics of BSL-1. Engineered auxotrophy and kill-switch branches should be optional subgraphs rather than defining features.

## 4. Mechanistic evidence and recent developments

### Auxotrophic containment

Conventional auxotrophy deletes or disables a biosynthetic function, making growth depend on an externally supplied metabolite. Reported examples include thymidylate-synthase knockout in *L. lactis*, phosphate-transporter deletion combined with phosphite utilization in cyanobacteria, and `dapA` inactivation in live bacterial therapeutic platforms. These interventions can reduce survival outside a permissive environment. (hoffmann2023safetybydesign pages 7-8, kim2023systemsandsynthetic pages 12-13)

The central failure mode is environmental rescue: the required metabolite can be present naturally or supplied by neighboring organisms through cross-feeding. Thus `cross-feeding -> rescues -> auxotrophic growth` is a high-priority antagonistic edge. (hoffmann2023safetybydesign pages 7-8, siguenza2024engineeredbacterialtherapeutics pages 6-7)

### Synthetic auxotrophy and genetic-code firewalls

2023–2024 reviews describe orthogonal aminoacyl-tRNA synthetase/tRNA systems that place ncAA-dependent residues in essential proteins. Reported laboratory escape frequencies span approximately 10^-8 to below 10^-12, depending on the number and identity of dependency sites. Examples include dual essential-gene systems below 10^-12, TEM-1 systems below 10^-11, and sliding-clamp variants below 10^-10. Recoding TAG codons in 22 essential genes produced no detectable escape in the reported culture assays. (gomeztatay2024xenobiologyforthe pages 4-5, gomeztatay2024xenobiologyforthe pages 5-7)

A ligand-dependent essential-gene system was reported below 3 × 10^-11 escape under laboratory conditions. The NIH contained-system benchmark discussed in these reviews is survival/escape below 10^-8. These values are assay-specific limits or frequencies, not universal probabilities of environmental escape. (hoffmann2023safetybydesign pages 7-8, pavao2023biocontainmenttechniquesand pages 5-7)

Orthogonal coding also reduces the **functional consequence** of HGT: a transferred recoded gene may not be translated correctly in a wild-type recipient. The graph predicate should therefore be `decreases functional expression after transfer`, not the stronger and generally unsupported `prevents DNA transfer`. (hoffmann2023safetybydesign pages 8-10, gomeztatay2024xenobiologyforthe pages 5-7)

### Kill switches and CRISPR safeguards

Active systems sense a nonpermissive condition and induce toxin expression, essential-gene repression, DNA cleavage, or growth arrest. Cas nuclease/guide-RNA systems can target repeated genomic sequences and cause lethal double-strand breaks. (hoffmann2023safetybydesign pages 7-8)

However, suicide circuits often have an evolutionary asymmetry: loss-of-function mutations disable killing while preserving growth. The 2023 safety-by-design review notes escape of the Deadman switch within days of passaging. Essential-gene dependency and redundant independent controls may be more mutation-resistant, although they can impose fitness costs and increase design complexity. (hoffmann2023safetybydesign pages 8-10)

### Xenobiology

Alternative genetic codes and XNA-based systems are proposed as stronger biological firewalls. Yet the 2024 xenobiology review emphasizes that fully orthogonal, permanently maintained organisms have not been achieved, that XNA nutrient dependence is not absolutely validated in complete organisms, and that genetic firewalls do not eliminate ecological interactions. Greater circuit complexity can itself add failure modes. (gomeztatay2024xenobiologyforthe pages 5-7, gomeztatay2024xenobiologyforthe pages 7-8)

## 5. Applications and real-world implementation

### Teaching and basic research

BSL-1 is widely used in teaching laboratories for low-risk organisms and low-risk manipulations. ASM guidance was developed after inconsistent teaching-laboratory practices and stresses that organism risk group, procedure, equipment, and containment must be evaluated together. (biosafety2013biosafetyguidelinesfor pages 1-2)

### Industrial and yeast biotechnology

Auxotrophies and simple kill switches remain common containment approaches for genetically modified yeast. Synthetic auxotrophy and XNA/genetic-code systems are more advanced experimentally in bacteria; 2023 analysis cautioned that many had not been tested in uncontrolled open environments and that yeast implementation faces distinct translation-system constraints. (pavao2023biocontainmenttechniquesand pages 5-7)

### Live bacterial and microbiota therapeutics

The field now includes approved microbiota-based therapies for recurrent *Clostridioides difficile* infection—VOWST and Rebyota—as well as defined consortia and engineered therapeutic strains under clinical evaluation. These products demonstrate real-world microbial therapy but should not be used as evidence that the organisms or manufacturing protocols are BSL-1. (kim2023systemsandsynthetic pages 5-6)

NOV-001, incorporating the engineered *B. thetaiotaomicron* strain NB1000S for oxalate degradation, completed a phase 1 study evaluating safety, tolerability, and colonization. Synlogic platforms have used `dapA` inactivation as an auxotrophic safeguard. Persistent concerns include HGT and environmental dissemination. (kim2023systemsandsynthetic pages 12-13)

### Cancer detection and treatment

Engineered *E. coli* Nissle 1917 and attenuated *Salmonella* systems are being developed to sense tumors, report disease-associated signals, and release therapeutic proteins. Mouse studies of synchronized lysis circuits reported tumor-localized induction and delivery of chemokines, hemolysin, pro-apoptotic proteins, and checkpoint-blockade nanobodies. Some experimental nonreplicating bacterial therapies use doses of 10^6–10^7 CFU. These are preclinical/therapeutic implementations requiring dedicated risk assessment, not examples of unqualified BSL-1 work. (siguenza2024engineeredbacterialtherapeutics pages 9-11, siguenza2024engineeredbacterialtherapeutics pages 6-7)

## 6. Expert analysis for TraitMech curation

The strongest conclusion from current literature is that **BSL-1 is an emergent classification of an agent–procedure–control system**. A purely molecular graph ending directly at BSL-1 would overstate causality. Low or absent virulence activity lowers agent hazard; containment engineering lowers survival or functional gene dissemination; standard practices lower exposure. A risk assessment integrates those effects into the final containment assignment. (biosafety2013biosafetyguidelinesfor pages 1-2, gao2024frombiosafetyto pages 5-6)

Quantitative escape frequency is a valuable intermediate phenotype, but it is measured under specified media, duration, population size, detection limit, and evolutionary conditions. A value below 10^-11 in a laboratory assay cannot be generalized to soil, wastewater, the gut, or industrial fermentation without environment-specific validation. Reviews specifically warn that open-environment performance remains unpredictable and that cross-feeding and mutation can defeat otherwise strong systems. (hoffmann2023safetybydesign pages 8-10, pavao2023biocontainmenttechniquesand pages 5-7, gomeztatay2024xenobiologyforthe pages 7-8)

## 7. Claims that should not yet be curated

1. **“BSL-1 is an intrinsic microbial trait.”** Incorrect without a protocol/risk-assessment qualifier.
2. **“RG1 equals BSL-1.”** Risk group informs containment but does not determine it alone.
3. **“Absence of virulence factors causes BSL-1.”** Too broad; absence must be strain- and factor-specific, and unknown virulence cannot be treated as demonstrated absence.
4. **“Auxotrophy guarantees environmental death.”** Cross-feeding or environmental nutrient availability can rescue growth.
5. **“A kill switch prevents escape.”** Escape mutations, circuit loss, and selection under passaging are documented concerns.
6. **“Orthogonal coding prevents HGT.”** It more defensibly reduces functional expression in recipients; it does not necessarily prevent DNA movement.
7. **“GRAS, probiotic, attenuated, or approved therapeutic means BSL-1.”** These are distinct regulatory or phenotypic claims.
8. **Taxon-general gene edges.** `thyA`, `dapA`, transporter, toxin, or adhesin effects should be tied to an exact strain and construct.
9. **Open-environment effectiveness of xenobiological safeguards.** Current support is largely laboratory-based, with explicit validation gaps. (pavao2023biocontainmenttechniquesand pages 5-7, gomeztatay2024xenobiologyforthe pages 7-8)
10. **Exact chemical CURIEs without stereochemical verification.** Preserve label-only nodes rather than inventing identifiers.

## DOI-first bibliography

- Gao W. et al. “From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories.” *Laboratories* 1, 158–173. **December 2024.** https://doi.org/10.3390/laboratories1030013 (gao2024frombiosafetyto pages 5-6)
- Gómez-Tatay L., Hernández-Andreu J.M. “Xenobiology for the Biocontainment of Synthetic Organisms: Opportunities and Challenges.” *Life* 14, 996. **August 2024.** https://doi.org/10.3390/life14080996 (gomeztatay2024xenobiologyforthe pages 4-5, gomeztatay2024xenobiologyforthe pages 5-7, gomeztatay2024xenobiologyforthe pages 7-8)
- Siguenza N. et al. “Engineered bacterial therapeutics for detecting and treating CRC.” *Trends in Cancer* 10, 588–597. **July 2024.** https://doi.org/10.1016/j.trecan.2024.04.001 (siguenza2024engineeredbacterialtherapeutics pages 6-7, siguenza2024engineeredbacterialtherapeutics pages 9-11)
- Kim K., Kang M., Cho B-K. “Systems and synthetic biology-driven engineering of live bacterial therapeutics.” *Frontiers in Bioengineering and Biotechnology* 11. **October 2023.** https://doi.org/10.3389/fbioe.2023.1267378 (kim2023systemsandsynthetic pages 12-13, kim2023systemsandsynthetic pages 5-6)
- Hoffmann S.A. et al. “Safety by design: Biosafety and biosecurity in the age of synthetic genomics.” *iScience* 26, 106165. **March 2023.** https://doi.org/10.1016/j.isci.2023.106165 (hoffmann2023safetybydesign pages 7-8, hoffmann2023safetybydesign pages 8-10)
- Pavão G., Sfalcin I., Bonatto D. “Biocontainment Techniques and Applications for Yeast Biotechnology.” *Fermentation* 9, 341. **March 2023.** https://doi.org/10.3390/fermentation9040341 (pavao2023biocontainmenttechniquesand pages 5-7, pavao2023biocontainmenttechniquesand pages 13-15)
- Task Committee on Laboratory Biosafety. “Biosafety Guidelines for Handling Microorganisms in the Teaching Laboratory: Development and Rationale.” *Journal of Microbiology & Biology Education* 14, 78–83. **January 2013.** https://doi.org/10.1128/jmbe.v14i1.531 (biosafety2013biosafetyguidelinesfor pages 1-2)

References

1. (biosafety2013biosafetyguidelinesfor pages 1-2): … Task Committee on Laboratory Biosafety. Biosafety guidelines for handling microorganisms in the teaching laboratory: development and rationale†. Journal of Microbiology & Biology Education : JMBE, 14:78-83, Jan 2013. URL: https://doi.org/10.1128/jmbe.v14i1.531, doi:10.1128/jmbe.v14i1.531. This article has 105 citations.

2. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 11 citations.

3. (gomeztatay2024xenobiologyforthe pages 4-5): Lucía Gómez-Tatay and José Miguel Hernández-Andreu. Xenobiology for the biocontainment of synthetic organisms: opportunities and challenges. Aug 2024. URL: https://doi.org/10.3390/life14080996, doi:10.3390/life14080996. This article has 22 citations.

4. (hoffmann2023safetybydesign pages 7-8): Stefan A. Hoffmann, James Diggans, Douglas Densmore, Junbiao Dai, Tom Knight, Emily Leproust, Jef D. Boeke, Nicole Wheeler, and Yizhi Cai. Safety by design: biosafety and biosecurity in the age of synthetic genomics. iScience, 26:106165, Mar 2023. URL: https://doi.org/10.1016/j.isci.2023.106165, doi:10.1016/j.isci.2023.106165. This article has 66 citations and is from a peer-reviewed journal.

5. (pavao2023biocontainmenttechniquesand pages 5-7): Guilherme Pavão, Isabela Sfalcin, and Diego Bonatto. Biocontainment techniques and applications for yeast biotechnology. Fermentation, Mar 2023. URL: https://doi.org/10.3390/fermentation9040341, doi:10.3390/fermentation9040341. This article has 19 citations.

6. (gomeztatay2024xenobiologyforthe pages 5-7): Lucía Gómez-Tatay and José Miguel Hernández-Andreu. Xenobiology for the biocontainment of synthetic organisms: opportunities and challenges. Aug 2024. URL: https://doi.org/10.3390/life14080996, doi:10.3390/life14080996. This article has 22 citations.

7. (hoffmann2023safetybydesign pages 8-10): Stefan A. Hoffmann, James Diggans, Douglas Densmore, Junbiao Dai, Tom Knight, Emily Leproust, Jef D. Boeke, Nicole Wheeler, and Yizhi Cai. Safety by design: biosafety and biosecurity in the age of synthetic genomics. iScience, 26:106165, Mar 2023. URL: https://doi.org/10.1016/j.isci.2023.106165, doi:10.1016/j.isci.2023.106165. This article has 66 citations and is from a peer-reviewed journal.

8. (pavao2023biocontainmenttechniquesand pages 13-15): Guilherme Pavão, Isabela Sfalcin, and Diego Bonatto. Biocontainment techniques and applications for yeast biotechnology. Fermentation, Mar 2023. URL: https://doi.org/10.3390/fermentation9040341, doi:10.3390/fermentation9040341. This article has 19 citations.

9. (gomeztatay2024xenobiologyforthe pages 7-8): Lucía Gómez-Tatay and José Miguel Hernández-Andreu. Xenobiology for the biocontainment of synthetic organisms: opportunities and challenges. Aug 2024. URL: https://doi.org/10.3390/life14080996, doi:10.3390/life14080996. This article has 22 citations.

10. (siguenza2024engineeredbacterialtherapeutics pages 6-7): Nicole Siguenza, Arianna Brevi, Joanna T. Zhang, Arman Pabani, Abhinav Bhushan, Moumita Das, Yousong Ding, Jeff Hasty, Pradipta Ghosh, and Amir Zarrinpar. Engineered bacterial therapeutics for detecting and treating crc. Trends in Cancer, 10:588-597, Jul 2024. URL: https://doi.org/10.1016/j.trecan.2024.04.001, doi:10.1016/j.trecan.2024.04.001. This article has 17 citations and is from a peer-reviewed journal.

11. (kim2023systemsandsynthetic pages 12-13): Kangsan Kim, Minjeong Kang, and Byung-Kwan Cho. Systems and synthetic biology-driven engineering of live bacterial therapeutics. Frontiers in Bioengineering and Biotechnology, Oct 2023. URL: https://doi.org/10.3389/fbioe.2023.1267378, doi:10.3389/fbioe.2023.1267378. This article has 46 citations.

12. (kim2023systemsandsynthetic pages 5-6): Kangsan Kim, Minjeong Kang, and Byung-Kwan Cho. Systems and synthetic biology-driven engineering of live bacterial therapeutics. Frontiers in Bioengineering and Biotechnology, Oct 2023. URL: https://doi.org/10.3389/fbioe.2023.1267378, doi:10.3389/fbioe.2023.1267378. This article has 46 citations.

13. (siguenza2024engineeredbacterialtherapeutics pages 9-11): Nicole Siguenza, Arianna Brevi, Joanna T. Zhang, Arman Pabani, Abhinav Bhushan, Moumita Das, Yousong Ding, Jeff Hasty, Pradipta Ghosh, and Amir Zarrinpar. Engineered bacterial therapeutics for detecting and treating crc. Trends in Cancer, 10:588-597, Jul 2024. URL: https://doi.org/10.1016/j.trecan.2024.04.001, doi:10.1016/j.trecan.2024.04.001. This article has 17 citations and is from a peer-reviewed journal.