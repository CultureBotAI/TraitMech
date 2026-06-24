---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:41:25.656856'
end_time: '2026-06-18T09:52:24.719093'
duration_seconds: 659.06
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spore forming
  trait_identifier: METPO:1000871
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spore_forming
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A sporulation in which an organism has the ability to produce endospores.
  parent_traits: METPO:1000870
  synonyms: spore, yes
  evidence_summary: 'DOI:10.1038/nrmicro2921: production of a highly resistant dormant
    cell type known as the spore (Supports spore forming as the ability to produce
    dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis
    (Organism example: Bacillus subtilis is described as endospore-forming.)'
  causal_graph_summary: 'spore_forming_endospore_assembly: 6 nodes, 5 edges'
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
- **Trait label:** spore forming
- **METPO identifier:** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

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
- **Trait label:** spore forming
- **METPO identifier:** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Spore forming** (METPO:1000871)

### Scope summary (TraitMech-ready)
**Trait label:** spore forming (endospore formation)  
**METPO identifier:** METPO:1000871  
**Definition (curation-ready):** capacity to execute the **endospore differentiation program**, producing a **highly resistant, dormant endospore** via a regulated developmental process (initiation → asymmetric division → engulfment → cortex/coat assembly → maturation and release). (m.2023sporulationstructureassembly pages 4-6, matavacas2023proteostasisinbacillus pages 21-25)

**Trait boundaries / nearby traits to exclude**  
*Spore forming* here should be restricted to **bacterial endospores** (Firmicutes lineages such as *Bacillus*/*Clostridium*), not:
- **Fungal spores** or other eukaryotic sporulation programs (different cell biology). 
- **Exospores/conidia** in Actinobacteria (different morphogenesis). 
- **Persisters/VBNC** states (dormancy without endospore morphogenesis and specialized layers). 

**Downstream but mechanistically coupled modules:** spore **germination/outgrowth** is downstream of the trait but uses spore-built structures (cortex, coat) and chemistry (CaDPA/DPA), so germination-linked nodes/edges can be included as a connected module (useful for TraitMech graphs that span “formation → function”). (m.2023sporulationstructureassembly pages 12-13, m.2023sporulationstructureassembly pages 4-6)

---

## 1) Key concepts and current understanding

### 1.1 Canonical developmental stages and compartmentalization
A commonly curated representation is the **seven-stage** sporulation program: axial filamentation → **asymmetric (polar) septation** → **forespore engulfment** → cortex/coat assembly → maturation → mother-cell lysis/release (with later germination). (m.2023sporulationstructureassembly pages 4-6)

A schematic summarizing the major stages and the sigma-factor cascade is available as Figure 1(A) in Guerrero 2023. (m.2023sporulationstructureassembly media d9d8eb94)

### 1.2 Central regulatory architecture: phosphorelay and Spo0A
In *Bacillus*-type systems, sporulation entry is controlled by a **multicomponent phosphorelay**:
- Environmental inputs (e.g., nutrient limitation) are sensed by **histidine kinases** that phosphorylate **Spo0F**, and phosphotransfer proceeds to **Spo0B** and then to **Spo0A**, the master regulator. (m.2023sporulationstructureassembly pages 6-7)
- Negative controls include **Rap phosphatases** (dephosphorylate Spo0F~P) and **Spo0E-family phosphatases** (Spo0A-specific). (m.2023sporulationstructureassembly pages 6-7)

Spo0A~P can participate in **positive feedback** by stimulating transcription of spo0F (“the dimeric phosphorylated form of Spo0A stimulates spo0F transcription”). (bidnenko2024complexsporulationspecificexpression pages 17-17)

### 1.3 Sigma-factor cascade (compartment-specific transcription)
A conserved organizing principle is the **sigma cascade**:
**σF → σE → σG → σK**, coordinating forespore vs mother-cell programs across time. (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94)

In *Clostridium botulinum*, alternative sigma factors **SigF, SigE, and SigG** are reported as essential for sporulation (species-specific details may differ from *Bacillus*). (rawson2023pathogenicityandvirulence pages 26-28)

### 1.4 Morphogenetic modules: engulfment, cortex, coat
- **Engulfment** requires **spoIID, spoIIM, spoIIP** (“required for engulfment”). (m.2023sporulationstructureassembly pages 4-6)
- **Cortex and coat** assembly proceeds after engulfment, contributing to dormancy and resistance; coat proteins influence “core protection, spore-core dehydration and dormancy.” (m.2023sporulationstructureassembly pages 6-7)

### 1.5 Spore chemistry enabling resistance and germination competence
A key chemical signature is **dipicolinic acid** (often present as CaDPA):
- Starvation/nutrient depletion is associated with sporulation and **DPA synthesis**. (m.2023sporulationstructureassembly pages 12-13)
- **SpoVA** proteins form channels mediating CaDPA handling (“SpoVAC, SpoVAD, SpoVAEb… implicated in CaDPA release”). (m.2023sporulationstructureassembly pages 12-13)

Germination linkage (useful for connected graphs): completion of CaDPA release is explicitly described as a trigger: “Once CaDPA release is complete in stage I, it triggers entry into stage II.” (m.2023sporulationstructureassembly pages 12-13)

---

## 2) Recent developments (prioritizing 2023–2024)

### 2.1 Translation stress as an upstream determinant of sporulation entry (2023)
Feaga et al. showed that loss of **elongation factor P (EF-P)** delays sporulation initiation by reducing **Spo0A** levels: ribosome profiling indicates Spo0A expression is lower in Δefp, and “Ectopic expression of Spo0A rescues the sporulation initiation phenotype.” (feaga2023elongationfactorp pages 1-2)

This provides a mechanistic “physiology → master regulator abundance → trait execution” axis suitable for causal graph expansion beyond the canonical phosphorelay. (feaga2023elongationfactorp pages 1-2, feaga2023elongationfactorp pages 2-4)

### 2.2 Active cell–cell signaling that amplifies sporulation heterogeneity via glycerol (2024)
Updegrove et al. (Science Advances, 2024) identified a pathway where early sporulators use **ShfP** (calcineurin-like phosphoesterase) to generate **extracellular glycerol**, which:
- “serves as a nutrient” for noncommitted cells and 
- “acts through a sensor kinase (KinD) to actively delay cells from entering the sporulation program,” i.e., delaying Spo0A phosphorylation dynamics. (updegrove2024altruisticfeedingand pages 9-10)

The same work reports that glycerol “inhibits cortex assembly,” and ShfA provides protection to producer cells, creating an inhibitor–immunity-like interaction relevant to population-level trait expression. (updegrove2024altruisticfeedingand pages 9-10)

### 2.3 Compartment-specific gene regulation influencing spore properties (2024)
Bidnenko et al. (JBC, 2024) describes sporulation-stage and compartment-linked regulation (including sigma-factor context) and highlights spore resistance features including “small acid-soluble proteins (SASPs)” and resistance to “radiation, heat, and chemicals,” reinforcing the mechanistic tie between developmental program execution and resistance phenotype. (bidnenko2024complexsporulationspecificexpression pages 17-18)

---

## 3) Current applications and real-world implementations

### 3.1 Agriculture/biocontrol: *Bacillus thuringiensis* spore–crystal formulations
*B. thuringiensis* is a spore-forming soil bacterium whose sporulation is associated with production of insecticidal crystalline proteins; this is foundational to commercial biopesticides relying on environmental persistence of spores and crystals. (m.2023sporulationstructureassembly pages 4-6)

### 3.2 Food safety and public health: spore-forming pathogens
In *Clostridium botulinum*, “the ability to form endospores is critical to the pathogenicity,” enabling persistence and transmission; infant and wound botulism can be initiated when ingested spores germinate into toxin-producing vegetative cells. (rawson2023pathogenicityandvirulence pages 26-28)

These application contexts motivate curation of edges linking environmental stresses to sporulation/germination competence and resistance traits.

---

## 4) Candidate causal-graph nodes (grouped) with ontology grounding suggestions

### 4.1 Trait / processes
- **Endospore formation / sporulation** (target phenotype; METPO:1000871)  
- Asymmetric septation / polar division (GO label candidate) (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94)
- Engulfment (GO label candidate) (m.2023sporulationstructureassembly pages 4-6)
- Cortex formation; spore coat assembly (GO label candidates) (m.2023sporulationstructureassembly pages 6-7, matavacas2023proteostasisinbacillus pages 21-25)
- Germination (linked module) (m.2023sporulationstructureassembly pages 12-13)

### 4.2 Environmental & experimental factors
- Nutrient limitation / starvation (ENVO label candidate) (matavacas2023proteostasisinbacillus pages 21-25, updegrove2024altruisticfeedingand pages 1-2)
- Extracellular glycerol (chemical; CHEBI candidate) (updegrove2024altruisticfeedingand pages 9-10)
- Temperature modulation (mentioned as affecting spore structure/germination cues in review context) (bidnenko2024complexsporulationspecificexpression pages 17-18, m.2023sporulationstructureassembly pages 12-13)

### 4.3 Regulatory proteins and signaling
- **Spo0A** (master regulator; phosphorylated Spo0A~P state) (bidnenko2024complexsporulationspecificexpression pages 17-17, matavacas2023proteostasisinbacillus pages 21-25)
- **Spo0F, Spo0B** (phosphorelay components) (m.2023sporulationstructureassembly pages 6-7)
- Sporulation sensor kinases (histidine kinases; includes **KinD** in heterogeneity pathway) (m.2023sporulationstructureassembly pages 6-7, updegrove2024altruisticfeedingand pages 9-10)
- **Rap** phosphatases; **Phr** peptides (quorum-sensing modulation of entry) (m.2023sporulationstructureassembly pages 6-7)
- **Spo0E-family** Spo0A-specific phosphatases (m.2023sporulationstructureassembly pages 6-7)
- **EF-P** (translation factor; upstream control of Spo0A abundance) (feaga2023elongationfactorp pages 1-2)
- **ShfA (YabQ)**, **ShfP (YvnB)** (cell–cell signaling/heterogeneity) (updegrove2024altruisticfeedingand pages 2-3, updegrove2024altruisticfeedingand pages 4-5)

### 4.4 Sigma factors (compartmental transcription)
- **σH** (early sporulation transcription of kinA/spo0F/spo0A) (bidnenko2024complexsporulationspecificexpression pages 17-17)
- **σF, σE, σG, σK** (cascade; Bacillus) (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94)
- **SigF, SigE, SigG** (essential in *C. botulinum* context) (rawson2023pathogenicityandvirulence pages 26-28)

### 4.5 Morphogenetic machinery
- **spoIID, spoIIM, spoIIP** (engulfment) (m.2023sporulationstructureassembly pages 4-6)
- **SpoIIE** (early regulator referenced as influencing septum structure, upstream of σF activation in Feaga 2023) (m.2023sporulationstructureassembly pages 4-6, feaga2023elongationfactorp pages 2-4)
- Coat morphogenetic proteins (e.g., CotE/CotH/CotO referenced in review context) (m.2023sporulationstructureassembly pages 4-6, bidnenko2024complexsporulationspecificexpression pages 17-18)

### 4.6 Chemicals / spore components / energetics
- **Dipicolinic acid (DPA)** and **CaDPA** (CHEBI candidate) (m.2023sporulationstructureassembly pages 12-13)
- **ppGpp/pGpp** (alarmones; CHEBI candidates) (updegrove2024altruisticfeedingand pages 9-10)
- ATP / energetic remodeling during sporulation (m.2023sporulationstructureassembly pages 12-13, updegrove2024altruisticfeedingand pages 9-10)

### 4.7 Germination-linked functional nodes
- **SpoVA (SpoVAC/SpoVAD/SpoVAEb)** channels (CaDPA release) (m.2023sporulationstructureassembly pages 12-13)
- **GerP** proteins (coat permeability / nutrient access) (m.2023sporulationstructureassembly pages 12-13)
- Cortex-lytic enzymes **CwlJ**, **SleB** (cortex degradation) (m.2023sporulationstructureassembly pages 12-13, m.2023sporulationstructureassembly pages 4-6)

---

## 5) Evidence-backed candidate causal edges (curation table)
The following table is curation-oriented and can be transcribed into `data/traits/morphology/spore_forming.yaml` as candidate edges (with uncertainty annotations where needed).

| Edge (subject–predicate–object) | Entity types/grounding suggestions | Evidence snippet | Source (DOI + year + URL) | Notes/uncertainty |
|---|---|---|---|---|
| Nutrient limitation/starvation → increases activity of → sporulation sensor kinases | environmental factor: nutrient limitation/starvation [label; ENVO candidate unavailable]; proteins: sporulation histidine kinases [label] | “prolonged nutrient limitation initiates sporulation” and “nutrient limitation is sensed by several protein kinases” leading to Spo0A activation (matavacas2023proteostasisinbacillus pages 21-25) | 2023, J. Matavacas, *Proteostasis in Bacillus subtilis* (source metadata incomplete in context) | Strong conceptually, but source metadata incomplete; curate cautiously unless replaced with primary/review DOI-backed source. |
| Sporulation sensor kinases → phosphorylate/activate → Spo0F | proteins: histidine kinases [label]; response regulator: Spo0F [label/UniProt candidate] | “sporulation initiation is controlled by increasing Spo0A activity; Spo0A is phosphorylated by a multicomponent phosphorelay in which kinases phosphorylate Spo0F” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Bacillus-centric phosphorelay; not universal across all clostridia. |
| Spo0F~P → transfers phosphoryl group to → Spo0B | proteins: Spo0F, Spo0B [label/UniProt candidates] | “Spo0B transfers phosphoryl groups to Spo0A” after kinases phosphorylate Spo0F in the multicomponent phosphorelay (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Close paraphrase of relay sequence; explicit intermediate Spo0F~P→Spo0B is inferred from canonical relay. |
| Spo0B → phosphorylates/activates → Spo0A | proteins: Spo0B, Spo0A [label/UniProt candidates]; process: sporulation initiation [GO candidate] | “Spo0B transfers phosphoryl groups to Spo0A” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Canonical Bacillus phosphorelay edge. |
| Spo0A~P → positively regulates → sporulation initiation program | protein state: phosphorylated Spo0A [label]; biological process: sporulation initiation [GO candidate] | “high levels of Spo0A~P induce transcription of hundreds of genes” and Spo0A is the “master regulator” of sporulation (matavacas2023proteostasisinbacillus pages 21-25, bidnenko2024complexsporulationspecificexpression pages 17-17) | 2023, J. Matavacas, *Proteostasis in Bacillus subtilis*; 10.1016/j.jbc.2024.107905 (2024) https://doi.org/10.1016/j.jbc.2024.107905 | Strong, but one supporting source has incomplete metadata; second source supports master-regulator role. |
| Spo0A~P → stimulates transcription of → spo0F | protein state: Spo0A~P [label]; gene: spo0F [label] | “the dimeric phosphorylated form of Spo0A stimulates spo0F transcription” (bidnenko2024complexsporulationspecificexpression pages 17-17) | 10.1016/j.jbc.2024.107905 (2024) https://doi.org/10.1016/j.jbc.2024.107905 | Positive-feedback edge in Bacillus subtilis phosphorelay; taxon-specific. |
| Rap phosphatases → dephosphorylate/inhibit → Spo0F~P | proteins: Rap family phosphatases [label]; protein state: Spo0F-P [label] | “Rap family phosphatases inhibit the pathway by dephosphorylating Spo0F-P” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Good negative-regulation edge for initiation control. |
| Phr peptides → inhibit → Rap phosphatases | peptides: Phr quorum-sensing peptides [label]; proteins: Rap phosphatases [label] | “Rap activity is inhibited by Phr peptides (mature length 5–7 aa) that are secreted, processed and re-imported” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Supports quorum-sensing modulation of sporulation entry. |
| Spo0E-family phosphatases → dephosphorylate/inhibit → Spo0A~P | proteins: Spo0E family [label]; protein state: Spo0A~P [label] | “A second negative control is provided by Spo0E-family Spo0A-specific phosphatases” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Strong negative-regulation edge. |
| σH-containing RNA polymerase → transcribes → kinA/spo0F/spo0A | sigma factor: SigH/σH [label/GO molecular function candidate]; genes: kinA, spo0F, spo0A [labels] | “Early sporulation genes kinA, spo0F and spo0A are transcribed by RNA polymerase containing sigma H” (bidnenko2024complexsporulationspecificexpression pages 17-17) | 10.1016/j.jbc.2024.107905 (2024) https://doi.org/10.1016/j.jbc.2024.107905 | Early transcriptional control edge; Bacillus subtilis-focused. |
| Asymmetric cell division → produces → mother cell | process: asymmetric cell division/polar septation [GO candidate]; cellular component: mother cell [label] | “asymmetric cell division produces a mother cell and forespore” (matavacas2023proteostasisinbacillus pages 21-25) | 2023, J. Matavacas, *Proteostasis in Bacillus subtilis* | Canonical morphology edge; replace with DOI-backed source if possible. |
| Asymmetric cell division → produces → forespore | process: asymmetric cell division/polar septation [GO candidate]; cellular component: forespore [label] | “asymmetric cell division produces a mother cell and forespore” (matavacas2023proteostasisinbacillus pages 21-25) | 2023, J. Matavacas, *Proteostasis in Bacillus subtilis* | Canonical morphology edge; metadata incomplete. |
| σF → precedes/activates stage leading to → σE | sigma factors: SigF/σF, SigE/σE [labels] | “sigma F → sigma E → sigma G → sigma K” cascade is conserved across Bacillus (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Figure-backed summary; directional activation is schematic/conserved, but exact mechanism should be grounded with primary literature if curated as direct activation. |
| σE → precedes/activates stage leading to → σG | sigma factors: SigE/σE, SigG/σG [labels] | “sigma F → sigma E → sigma G → sigma K” (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Figure-backed cascade; conserve as stage-order edge if direct activation wording feels too strong. |
| σG → precedes/activates stage leading to → σK | sigma factors: SigG/σG, SigK/σK [labels] | “sigma F → sigma E → sigma G → sigma K” (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly media d9d8eb94) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Same caution as above; suitable as ordered developmental cascade. |
| σF and σE → regulate → forespore engulfment | sigma factors: SigF/σF, SigE/σE [labels]; process: engulfment [GO candidate] | “SigF/SigE implicated in forespore engulfment (stage 3)” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Support is review-level and stage-associative; directness may be somewhat inferred. |
| spoIID → required for → engulfment | gene/protein: spoIID [label]; process: engulfment [GO candidate] | “Genes spoIID, spoIIM, spoIIP are required for engulfment” (m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Strong morphogenetic edge. |
| spoIIM → required for → engulfment | gene/protein: spoIIM [label]; process: engulfment [GO candidate] | “Genes spoIID, spoIIM, spoIIP are required for engulfment” (m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Strong morphogenetic edge. |
| spoIIP → required for → engulfment | gene/protein: spoIIP [label]; process: engulfment [GO candidate] | “Genes spoIID, spoIIM, spoIIP are required for engulfment” (m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Strong morphogenetic edge. |
| Mother-cell membrane engulfment → enables → forespore enclosure | process: engulfment [GO candidate]; cellular component: forespore [label] | “the mother cell membrane engulfs the forespore” (matavacas2023proteostasisinbacillus pages 21-25) | 2023, J. Matavacas, *Proteostasis in Bacillus subtilis* | Core morphogenetic edge; metadata incomplete. |
| Cortex synthesis → contributes to → mature spore formation | process: cortex formation [GO candidate]; phenotype: endospore formation [METPO:1000871] | “then cortex synthesis within the intermembrane space and coat assembly” follows engulfment (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Broad process edge; not gene-specific. |
| Spore coat assembly → contributes to → spore core protection/dehydration/dormancy | process: coat assembly [GO candidate]; phenotype/property: core protection, dehydration, dormancy [labels] | “coat proteins influence core protection, spore-core dehydration and dormancy” (m.2023sporulationstructureassembly pages 6-7) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Good high-level phenotype edge. |
| SpoVA proteins → mediate uptake/release of → Ca2+-dipicolinic acid (CaDPA) | proteins: SpoVA family [label]; chemical: calcium dipicolinate/CaDPA [CHEBI candidate if available] | “SpoVA proteins mediate uptake/release during uptake of Ca2+ dipicolinic acid (DPA)” and SpoVAC/SpoVAD/SpoVAEb form channels implicated in CaDPA release (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Spans sporulation/germination linkage; chemistry grounding may need curator confirmation. |
| Completion of CaDPA release → triggers → entry into germination stage II | chemical/process: CaDPA release [label]; process: germination stage II [label] | “Once CaDPA release is complete in stage I, it triggers entry into stage II” (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Downstream of spore formation, but useful for linked graph/module. |
| GerP proteins → favor nutrient access to → inner membrane | proteins: GerP family [label]; cellular component: inner membrane [GO/label] | “GerP proteins… favor nutrient access to the inner membrane” (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Germination-focused; peripheral to core trait. |
| gerP mutation → decreases → spore-coat permeability to germinants | gene: gerP [label]; property: spore-coat permeability [label]; chemicals: germinants [label] | “Mutations in gerP reduce spore-coat permeability to germinants” (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Germination linkage; not initiation/assembly. |
| CwlJ → hydrolyzes → cortex peptidoglycan | enzyme: CwlJ [label]; substrate: cortex peptidoglycan [GO/CHEBI candidate] | “Lytic enzymes SleB and CwlJ hydrolyze the cortex during germination” and “degrade cortex peptidoglycan” (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Germination enzyme edge, but directly tied to functional spore biology. |
| SleB → hydrolyzes → cortex peptidoglycan | enzyme: SleB [label]; substrate: cortex peptidoglycan [label] | “Lytic enzymes SleB and CwlJ hydrolyze the cortex during germination” (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Same as above. |
| Nutrient depletion/starvation → induces → dipicolinic acid (DPA) synthesis | environmental factor: starvation [label]; chemical: dipicolinic acid/DPA [label/CHEBI candidate] | “nutrient depletion/starvation induces sporulation and dipicolinic acid (DPA) synthesis” (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Valuable edge linking environment to spore chemical composition. |
| Spore state → associated with → low mRNA copy number per transcript | phenotype: mature spore [label]; nucleic acid property: mRNA abundance [label] | “only ~6% of spore mRNAs are present at >1 molecule per spore” (m.2023sporulationstructureassembly pages 6-7, m.2023sporulationstructureassembly pages 4-6) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Quantitative descriptive fact, not a causal edge; better as annotation/metadata. |
| Sporulation/spore-crystal formation program → downregulates → atpC (>20-fold) | process: sporulation developmental program [label]; gene: atpC [label] | “atpC down >20-fold” during sporulation-associated remodeling (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Quantitative expression change from B. thuringiensis context; likely assay- and taxon-specific. |
| Sporulation/spore-crystal formation program → downregulates → other atp genes (2–5-fold) | process: sporulation developmental program [label]; genes: ATP synthase genes [label] | “other atp genes 2–5 fold down” (m.2023sporulationstructureassembly pages 12-13) | 10.3390/microbiolres14020035 (2023) https://doi.org/10.3390/microbiolres14020035 | Descriptive systems-level trend; avoid overgeneralizing beyond studied strain/conditions. |
| Sporulation conditions → alter → spore coat protein composition | environmental factor: sporulation conditions [label]; structure: spore coat [label] | Bidnenko 2024 excerpt cites studies on “how sporulation conditions influence spore coat protein composition” (bidnenko2024complexsporulationspecificexpression pages 17-17) | 10.1016/j.jbc.2024.107905 (2024) https://doi.org/10.1016/j.jbc.2024.107905 | Indirect/citation-mediated in excerpt; useful as warning or future expansion rather than direct curation. |


*Table: This table lists curation-ready candidate causal edges for the microbial trait 'spore forming' focused on endospore initiation, regulation, morphogenesis, and linked germination mechanisms. It includes grounding suggestions, evidence snippets, DOI-first sources, and uncertainty notes to help decide what is ready for TraitMech curation.*

Additionally, recent (2023–2024) edges suitable for inclusion (not all appear in the artifact table):
- **EF-P deletion → lower Spo0A expression/abundance → reduced/delayed sporulation initiation**, with rescue by ectopic Spo0A expression. (feaga2023elongationfactorp pages 1-2)
- **ShfP activity → extracellular glycerol → KinD-mediated delay of sporulation entry / inhibition of Spo0A phosphorylation**, plus glycerol inhibition of cortex assembly and ShfA-mediated protection. (updegrove2024altruisticfeedingand pages 9-10)

---

## 6) Relevant statistics and recent data points (for curation metadata)

### Sporulation initiation perturbations
- Δefp sporulation efficiency: “Wild-type cells sporulated with an efficiency of ~85%… whereas Δefp cells… ~15%”; doubling times similar (~22 ± 4 min vs ~23 ± 4 min), supporting a sporulation-specific regulatory effect rather than general growth defect. (feaga2023elongationfactorp pages 1-2)

### Population heterogeneity pathway perturbations
- shfA deletion: reported “~1000-fold reduction in sporulation efficiency,” with genetic interactions (ΔshfAΔshfP restoring near wild-type). (updegrove2024altruisticfeedingand pages 2-3)

### Spore transcriptome quantitative note (descriptive)
- Only “~6% of spore mRNAs are present at >1 molecule per spore” (contextualized as many low-copy transcripts contributing to germination-related proteins). (m.2023sporulationstructureassembly pages 6-7, m.2023sporulationstructureassembly pages 4-6)

### Energetics / global physiology context in 2024 heterogeneity paper
- Reported physiological shifts accompanying sporulation: “approximately twofold… increase in adenosine triphosphate,” “30-fold increase in… ppGpp and pGpp,” and “up to 40% of total cellular phosphorous is present in lipoteichoic acid” (supporting plausibility of cell-envelope phosphoester substrates for ShfP). (updegrove2024altruisticfeedingand pages 9-10)

### Sporulation-linked expression remodeling in Bt context (assay/taxon-specific)
- Transcriptional remodeling examples include “atpC down >20-fold” and other atp genes “2–5 fold down” under sporulation-associated conditions. (m.2023sporulationstructureassembly pages 12-13)

---

## 7) Expert opinions / authoritative synthesis (from recent sources)
- Sporulation is framed as a **stress/starvation-triggered committed differentiation program** that is **irreversible once initiated** and requires reaching a Spo0A~P threshold. (updegrove2024altruisticfeedingand pages 1-2)
- Recent authoritative reviews emphasize endospores as critical to pathogen ecology and transmission; for *C. botulinum*, endospore formation is explicitly stated to be “critical to the pathogenicity.” (rawson2023pathogenicityandvirulence pages 26-28)

---

## 8) Warnings / curation caveats (do not curate without stronger support)
1. **Sigma-factor cascade edges:** Sources here provide a conserved order (σF→σE→σG→σK) and a schematic; if your graph semantics require **direct activation**, represent these as **“precedes / enables stage leading to”** rather than “activates,” unless supported by additional mechanistic papers. (m.2023sporulationstructureassembly media d9d8eb94, m.2023sporulationstructureassembly pages 4-6)
2. **Metadata-incomplete source:** One B. subtilis proteostasis text chunk used for general statements lacks complete bibliographic metadata in the retrieved context; avoid curating edges that depend solely on that source until replaced by a DOI-backed review/primary paper. (matavacas2023proteostasisinbacillus pages 21-25)
3. **Taxon-specific generalization risks:** Rap-Phr regulation and the canonical Bacillus phosphorelay may not map 1:1 onto all clostridia; retain NCBITaxon scoping where possible (e.g., NCBITaxon:1423 *Bacillus subtilis*, NCBITaxon:1428 *B. thuringiensis*, NCBITaxon:1491 *Clostridium botulinum*). (m.2023sporulationstructureassembly pages 6-7, rawson2023pathogenicityandvirulence pages 26-28)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Guerrero, G.G.** (2023-04). *Sporulation, Structure Assembly, and Germination in the Soil Bacterium Bacillus thuringiensis: Survival and Success in the Environment and the Insect Host.* **Microbiology Research** 14:466–491. DOI: **10.3390/microbiolres14020035**. URL: https://doi.org/10.3390/microbiolres14020035 (m.2023sporulationstructureassembly pages 4-6, m.2023sporulationstructureassembly pages 6-7, m.2023sporulationstructureassembly pages 12-13, m.2023sporulationstructureassembly media d9d8eb94)

2. **Feaga, H.A. et al.** (2023-02). *Elongation Factor P Is Important for Sporulation Initiation.* **Journal of Bacteriology** 205(2). DOI: **10.1128/jb.00370-22**. URL: https://doi.org/10.1128/jb.00370-22 (feaga2023elongationfactorp pages 1-2, feaga2023elongationfactorp pages 2-4)

3. **Rawson, A.M. et al.** (2023-05). *Pathogenicity and virulence of Clostridium botulinum.* **Virulence** 14(1). DOI: **10.1080/21505594.2023.2205251**. URL: https://doi.org/10.1080/21505594.2023.2205251 (rawson2023pathogenicityandvirulence pages 26-28)

4. **Bidnenko, V. et al.** (2024-12). *Complex sporulation-specific expression of transcription termination factor Rho highlights its involvement in Bacillus subtilis cell differentiation.* **Journal of Biological Chemistry** 300:107905. DOI: **10.1016/j.jbc.2024.107905**. URL: https://doi.org/10.1016/j.jbc.2024.107905 (bidnenko2024complexsporulationspecificexpression pages 17-17, bidnenko2024complexsporulationspecificexpression pages 17-18)

5. **Updegrove, T.B. et al.** (2024-10). *Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity.* **Science Advances** 10. DOI: **10.1126/sciadv.adq0791**. URL: https://doi.org/10.1126/sciadv.adq0791 (updegrove2024altruisticfeedingand pages 1-2, updegrove2024altruisticfeedingand pages 2-3, updegrove2024altruisticfeedingand pages 9-10, updegrove2024altruisticfeedingand pages 4-5)


References

1. (m.2023sporulationstructureassembly pages 4-6): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 21 citations.

2. (matavacas2023proteostasisinbacillus pages 21-25): J Matavacas. Proteostasis in bacillus subtilis: chaperones and stress-response mechanisms. Unknown journal, 2023.

3. (m.2023sporulationstructureassembly pages 12-13): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 21 citations.

4. (m.2023sporulationstructureassembly media d9d8eb94): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 21 citations.

5. (m.2023sporulationstructureassembly pages 6-7): Gloria G. Guerrero M. Sporulation, structure assembly, and germination in the soil bacterium bacillus thuringiensis: survival and success in the environment and the insect host. Microbiology Research, 14:466-491, Apr 2023. URL: https://doi.org/10.3390/microbiolres14020035, doi:10.3390/microbiolres14020035. This article has 21 citations.

6. (bidnenko2024complexsporulationspecificexpression pages 17-17): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 9 citations and is from a domain leading peer-reviewed journal.

7. (rawson2023pathogenicityandvirulence pages 26-28): Alexander M. Rawson, Andrew W. Dempster, Christopher M. Humphreys, and Nigel P. Minton. Pathogenicity and virulence of clostridium botulinum. Virulence, May 2023. URL: https://doi.org/10.1080/21505594.2023.2205251, doi:10.1080/21505594.2023.2205251. This article has 138 citations and is from a peer-reviewed journal.

8. (feaga2023elongationfactorp pages 1-2): Heather A. Feaga, Hye-Rim Hong, Cassidy R. Prince, Ananda Rankin, Allen R. Buskirk, and Jonathan Dworkin. Elongation factor p is important for sporulation initiation. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00370-22, doi:10.1128/jb.00370-22. This article has 17 citations and is from a peer-reviewed journal.

9. (feaga2023elongationfactorp pages 2-4): Heather A. Feaga, Hye-Rim Hong, Cassidy R. Prince, Ananda Rankin, Allen R. Buskirk, and Jonathan Dworkin. Elongation factor p is important for sporulation initiation. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00370-22, doi:10.1128/jb.00370-22. This article has 17 citations and is from a peer-reviewed journal.

10. (updegrove2024altruisticfeedingand pages 9-10): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (bidnenko2024complexsporulationspecificexpression pages 17-18): Vladimir Bidnenko, Arnaud Chastanet, Christine Péchoux, Yulia Redko-Hamel, Olivier Pellegrini, Sylvain Durand, Ciarán Condon, Marc Boudvillain, Matthieu Jules, and Elena Bidnenko. Complex sporulation-specific expression of transcription termination factor rho highlights its involvement in bacillus subtilis cell differentiation. Journal of Biological Chemistry, 300:107905, Dec 2024. URL: https://doi.org/10.1016/j.jbc.2024.107905, doi:10.1016/j.jbc.2024.107905. This article has 9 citations and is from a domain leading peer-reviewed journal.

12. (updegrove2024altruisticfeedingand pages 1-2): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (updegrove2024altruisticfeedingand pages 2-3): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

14. (updegrove2024altruisticfeedingand pages 4-5): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.