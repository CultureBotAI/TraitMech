---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:55:40.754033'
end_time: '2026-06-18T08:19:53.445030'
duration_seconds: 1452.69
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gliding
  trait_identifier: METPO:1000706
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gliding
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motile in which an organism moves smoothly along solid surfaces without
    flagella or pili.
  parent_traits: METPO:1000702
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces
    (Supports gliding as active surface movement without flagella.)'
  causal_graph_summary: 'gliding_surface_motility: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gliding
- **METPO identifier:** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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
- **Trait label:** gliding
- **METPO identifier:** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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


## Microbial trait causal graph report: **gliding** (METPO:1000706)

### Scope summary (TraitMech curation view)
**Gliding** refers to **active motility on solid surfaces** that occurs **without flagella or pili**. In Bacteroidota (e.g., *Flavobacterium johnsoniae*), gliding is achieved by **mobile cell-surface adhesins** (notably SprB) that move along a helical/multirail track on/under the outer membrane; adhesin engagement with the substratum produces propulsion and often cell rotation. In *Myxococcus xanthus*, “A-motility” (gliding) is mechanistically distinct and is mediated by **trans-envelope focal-adhesion (bFA) complexes** (Agl–Glt) that couple an inner-membrane proton-driven motor to outer-membrane adhesins to generate traction. (vincent2022dynamicprotondependentmotors pages 1-2, shibata2023filamentousstructuresin pages 1-2, islam2023unmaskingofthe pages 1-2)

**Boundary cases / nearby traits**
*Flavobacterium* gliding is explicitly contrasted with swimming (flagella) and twitching (type IV pili), and is stated to be unrelated to several other motility systems (including myxobacterial gliding and mycoplasma gliding) in terms of machinery, emphasizing that “gliding” is a phenotype category spanning multiple non-homologous mechanisms. Therefore, causal edges must be curated **with taxon/system qualifiers** (e.g., “Bacteroidota-type gliding” vs “Myxococcus A-motility”). (vincent2022dynamicprotondependentmotors pages 1-2, shibata2023filamentousstructuresin pages 1-2)

---

### Key concepts & current mechanistic understanding (2023–2024 prioritized)

#### 1) Bacteroidota gliding: SprB adhesin conveyor + Type IX secretion system (T9SS)
**Concept**: T9SS is a Bacteroidota outer-membrane secretion machine whose motors and envelope structures are shared with gliding. SprB is a major motility adhesin secreted by T9SS and then propelled along tracks on the cell surface; adhesion to the substrate converts adhesin movement into cell propulsion. (paillat2023ajourneywith pages 1-3, vincent2022dynamicprotondependentmotors pages 1-2)

**Energy coupling**: A conserved inner-membrane motor (GldLM/PorLM) uses the proton motive force—specifically the proton (pH) gradient—to power both secretion and adhesin motion in *F. johnsoniae*. (vincent2022dynamicprotondependentmotors pages 1-2)

**Structural track / “multirail” model (2023)**: Electron microscopy and single-molecule tracking support a **multirail structure underneath the outer membrane** associated with SprB filaments and containing GldJ; SprB foci can overtake each other, consistent with multiple lanes/rails. (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin pages 5-6)

**Recent structural biology of T9SS (2024)**: Cryo-EM work captured a substrate-bound “Extended Translocon” that includes SprE, PorD and a Skp-like chaperone (SkpA), and inferred that **release of a substrate–carrier complex** is the energy-requiring step in T9SS transport. This directly strengthens mechanistic edges linking the PMF-driven energy chain to both secretion and gliding. (lauber2024structuralinsightsinto pages 1-2)

#### 2) Myxococcus gliding (A-motility): Agl–Glt bacterial focal adhesions
**Concept**: *M. xanthus* gliding uses **helically trafficked Agl–Glt complexes** that become immobilized at **bacterial focal adhesions (bFAs)** to generate traction. A proton-driven inner-membrane motor module (AglRQS) powers directional motion of the motility machinery; a dedicated outer-membrane platform recruits and regulates exposure of adhesins that couple to the substrate. (islam2023unmaskingofthe pages 1-2)

**Adhesin-mediated traction**: CglB (a VWA-domain OM lipoprotein adhesin) is essential for substratum coupling; deletion prevents immobilization of motility complexes at bFAs, abolishing traction. (islam2023unmaskingofthe pages 1-2, islam2023unmaskingofthe pages 3-5)

**Assembly/disassembly regulation (2024)**: A molecular switch centered on GltJ links MglA-GTP and AglZ and recruits MreB, controlling bFA assembly and turnover via the MglA GTP cycle and MglB-mediated disassembly at the lagging pole. (attia2024amolecularswitch pages 1-1, attia2024amolecularswitch pages 1-3)

**Environmental/cofactor dependence (evidence present but system-specific)**: A preprint reports Ca2+-dependent stabilization of bFAs via an integrin-like component CglD; CglB contains a MIDAS-like motif consistent with divalent-cation mediated adhesion, and a MIDAS mutant fails to complement motility. These edges are promising but should be tagged as **uncertain/preprint** for curation until peer reviewed. (jolivet2023integrinlikeadhesincgld pages 1-3, islam2023unmaskingofthe pages 3-5)

---

### Candidate graph entities (nodes) grouped by type (curation candidates)

A consolidated curation table of candidate nodes and evidence-backed edges is provided as **artifact-00** below.

| Section | Group | Subject / Node | Type | Suggested grounding / identifier | Predicate / Attribute | Object / Value | Evidence snippet / quote | Citation(s) |
|---|---|---|---|---|---|---|---|---|
| Node | Phenotype | gliding motility | phenotype | METPO:1000706 | definition | active surface motility without flagella or pili | “gliding bacteria do not rely on obvious surface appendages to move on solid surfaces” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Node | Phenotype | Bacteroidota gliding motility | phenotype subclass | label-only candidate | distinguished_from | flagellar motility; type IV pilus-mediated twitching; myxobacterial gliding; Mycoplasma gliding | “unrelated to… flagellar motility, type IV pilus-mediated twitching motility, myxobacterial gliding motility, and Mycoplasma gliding motility” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Phenotype | Myxococcus A-motility / bacterial focal-adhesion gliding | phenotype subclass | label-only candidate | mechanism_class | Agl-Glt focal-adhesion motility | “A-motility… driven by helically-trafficked Agl–Glt complexes that form bacterial focal adhesions” | (islam2023unmaskingofthe pages 1-2) |
| Node | Complex | T9SS | complex | GO:0098797 | involved_in | gliding motility and secretion | “The T9SS is involved in… gliding motility” | (paillat2023ajourneywith pages 1-3) |
| Node | Complex | GldLM / PorLM rotary motor | complex | label-only candidate | energy_source | proton motive force / proton gradient | “The PorLM/GldLM rotary motor” and “Flavobacterium gliding motility is energized by the PMF” | (paillat2023ajourneywith pages 1-3) |
| Node | Complex | GldKN / PorKN ring | complex | label-only candidate | connected_to | GldLM motor and SprA/Sov translocon | “connected to a membrane-associated ring and outer membrane translocons” | (paillat2023ajourneywith pages 1-3) |
| Node | Complex | SprA / Sov translocon | complex | label-only candidate | function | outer membrane translocon for T9SS substrates | “The translocon comprises a very large 36-strand β-barrel protein, Sov/SprA” | (paillat2023ajourneywith pages 1-3) |
| Node | Complex | Extended T9SS translocon | complex | label-only candidate | components | SprA + PorV/PPI + SprE + PorD + SkpA | “Extended Translocon… includes SprE, PorD and an Skp homologue” | (lauber2024structuralinsightsinto pages 1-2) |
| Node | Complex | Agl-Glt machinery | complex | label-only candidate | spans | cell envelope | “Agl-Glt… a multiprotein assembly… spanning envelope layers” | (attia2024amolecularswitch pages 1-1) |
| Node | Complex | GltABCHK outer-membrane platform | complex | label-only candidate | recruits | CglB adhesin | “heteroligomeric complex containing… GltA, GltB, and GltH… GltC and… GltK” | (islam2023unmaskingofthe pages 1-2) |
| Node | Complex | multirail / helical loop track | structural complex | label-only candidate | location | underneath outer membrane | “possible multi-rail structure underneath the outer membrane” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Protein | SprB | adhesin protein | label-only candidate | role | major motility adhesin | “SprB… is the major motility adhesin” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Protein | RemA / RemZ | adhesin / T9SS substrate | label-only candidate | role | semiredundant motility adhesin / gliding adhesin homolog | “other semiredundant motility adhesins, such as RemA” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Protein | GldJ | lipoprotein / track-associated protein | label-only candidate | associated_with | multirail structure | “contained GldJ protein” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Protein | SprF | accessory protein / shuttle | label-only candidate | supports | SprB secretion / connection to motility machinery | “SprF is thought to connect SprB to the rest of the motility machinery” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Protein | PorV | outer membrane shuttle | label-only candidate | role | carries Type A substrates; not required for SprB secretion | “PorV does not appear to be required for secretion of… SprB” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Protein | SprE / PorW | lipoprotein | label-only candidate | required_for | T9SS function | “deletion of SprE abolished T9SS function” | (lauber2024structuralinsightsinto pages 5-6) |
| Node | Protein | PorD | periplasmic T9SS component | label-only candidate | binds | SprE finger region | “PorD interaction occurs within this disordered Finger Region” | (lauber2024structuralinsightsinto pages 5-6) |
| Node | Protein | SkpA | periplasmic chaperone homolog | label-only candidate | forms | periplasmic extension of translocon | “SprE plus a SkpA trimer form a dish-shaped periplasmic extension” | (lauber2024structuralinsightsinto pages 2-3) |
| Node | Protein | CglB | adhesin protein | label-only candidate | role | essential substratum-coupling adhesin | “CglB as an essential substratum-coupling adhesin” | (islam2023unmaskingofthe pages 1-2) |
| Node | Protein | CglD | adhesin-associated lipoprotein | label-only candidate | role | stabilizes bacterial focal adhesions | “CglD… stabilizing and efficiently anchoring this assembly at bFAs” | (jolivet2023integrinlikeadhesincgld pages 1-3) |
| Node | Protein | GltJ | inner membrane / scaffold protein | label-only candidate | binds | MglA-GTP and AglZ | “GltJ… binds MglA-GTP and AglZ” | (attia2024amolecularswitch pages 1-1) |
| Node | Protein | AglRQS | proton channel motor | label-only candidate | analogous_to | TolQR/ExbBD/MotAB-like channel | “AglR, AglQ, and AglS… form a proton-driven… channel” | (islam2023unmaskingofthe pages 1-2) |
| Node | Protein | MglA-GTP | polarity regulator | label-only candidate | promotes | bFA assembly and directionality | “MglA-GTP promotes bFA assembly and directionality” | (attia2024amolecularswitch pages 1-3) |
| Node | Protein | MglB | GAP-like regulator | label-only candidate | promotes | disassembly at lagging pole | “MglB… acts as a GAP to disassemble complexes at the rear” | (attia2024amolecularswitch pages 1-3) |
| Node | Protein | AglZ | cytosolic platform protein | label-only candidate | links_to | GltJ via proline-rich sequence | “GYFGltJ interacts with the AglZ PRS sequence” | (attia2024amolecularswitch pages 1-3) |
| Node | Protein | MreB | cytoskeletal regulator | label-only candidate | recruited_by | GltJ / gliding platform | “recruits MreB to initiate movement” | (attia2024amolecularswitch pages 1-1) |
| Node | Process | T9SS-dependent secretion | process | GO:0046903 | coupled_to | gliding in many Bacteroidota | “secretion and helicoidal motion of the main adhesin SprB are intimately linked” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Node | Process | adhesin surface translocation | process | label-only candidate | substrate | SprB | “SprB filaments are propelled along a helical loop on the cell surface” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Process | bacterial focal adhesion formation | process | label-only candidate | outcome | substratum coupling / traction | “becomes immobilized at bFA” | (attia2024amolecularswitch pages 1-3) |
| Node | Process | OM adhesive complex treadmilling | process | label-only candidate | drives | traction and cell rotation | “OM adhesive complex treadmill through the IM motor” | (attia2024amolecularswitch pages 1-3) |
| Node | Process | substrate–carrier release from translocon | process | label-only candidate | energy_requirement | PMF-dependent | “release of the substrate–carrier protein complex… is the energy-dependent step” | (lauber2024structuralinsightsinto pages 1-2) |
| Node | Environmental factor | solid surface contact | environmental factor | ENVO:01000922 (surface, broad candidate) | required_for | gliding motility | “Gliding motility requires cell contact with a solid surface” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Environmental factor | hard substratum | environmental factor | label-only candidate | favors | Myxococcus gliding observations | “gliding occurs on harder substrata” | (islam2023unmaskingofthe pages 1-2) |
| Node | Environmental factor | agar surface | assay environment | ENVO:01001871 (agar medium, candidate broad) | used_in | colony spreading / gliding assay | “Spreading… on agar” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Environmental factor | glass coverslip | assay surface | label-only candidate | used_in | single-cell gliding assay | “Gliding… cells on glass coverslips” | (thunes2024glidingmotilityproteins pages 2-5) |
| Node | Environmental factor | calcium / divalent cations | chemical/environment factor | CHEBI:29108 (calcium(2+)) | modulates | CglD/CglB adhesion functions | “calcium-dependent manner” and “MIDAS… Ca2+/Mg2+/Mn2+” | (jolivet2023integrinlikeadhesincgld pages 1-3, islam2023unmaskingofthe pages 3-5) |
| Node | Chemical | proton motive force | energy currency | GO:0015988 | powers | T9SS and gliding | “T9SS-dependent secretion and gliding motility is a process energized by the IM proton motive force” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Node | Chemical | proton gradient / pH gradient | energy component | GO:0009090 (proton transmembrane transport, broad related) | powers | GldLM-dependent motility | “gliding motility is powered by the pH gradient component of the PMF” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Node | Chemical | CCCP | inhibitor | CHEBI:34253 | inhibits | SprB dynamics / gliding | “SprB dynamics halted almost immediately after the addition of carbonyl cyanide m-chlorophenyl hydrazine” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Node | Quantitative datum | SprB translocation speed | measurement node | label-only candidate | value | ~2 µm/s | “SprB filaments are propelled at ~2 µm per second” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Quantitative datum | cell gliding speed | measurement node | label-only candidate | value | ~1–5 µm/s | “move over surfaces at ~1–5 µm per second” | (shibata2023filamentousstructuresin pages 1-2) |
| Node | Quantitative datum | predicted gliding-positive genomes | dataset statistic | label-only candidate | value | 327/693 Bacteroidetes genomes | “identified 402… to have T9SS, of which 327 were found to also have gliding motility” | (sahoo2023t9gpredacomprehensive pages 2-4) |
| Node | Quantitative datum | mandatory gliding component set | dataset statistic | label-only candidate | value | 11 proteins | “a total of 11 proteins as mandatory protein components to predict the presence of gliding motility” | (sahoo2023t9gpredacomprehensive pages 2-4) |
| Edge | Causal edge | proton gradient | chemical | CHEBI:15378 (H+) candidate for proton) | powers | GldLM motor | “GldL and GldM assemble dynamic membrane channels that use the proton gradient” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | GldLM motor | complex | label-only candidate | enables | T9SS-dependent SprB secretion | “power both T9SS-dependent secretion of SprB” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | GldLM motor | complex | label-only candidate | enables | SprB motion at cell surface | “and its motion at the cell surface” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | SprB surface motion | process | label-only candidate | causes | cell propulsion / forward screw-like motion | “binding of SprB to the substratum generates adhesion points… displaces the cell body in a forward screw-like motion” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | T9SS | complex | GO:0098797 | secretes | SprB | “SprB… transported to the cell surface by… T9SS” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | T9SS | complex | GO:0098797 | contributes_to | gliding motility | “The T9SS is involved in… gliding motility” | (paillat2023ajourneywith pages 1-3) |
| Edge | Causal edge | GldK/GldN ring + SprE | complex/module | label-only candidate | transduces_energy_from | GldLM motor to SprA translocon | “GldK−GldN ring and SprE facilitate energy transduction from the inner membrane GldLM motor to the outer membrane translocon SprA” | (sahoo2023t9gpredacomprehensive pages 2-4) |
| Edge | Causal edge | SprA translocon | complex | label-only candidate | exports | CTD-bearing substrates | “translocon comprises… Sov/SprA” and substrate is “transferred to the PorV shuttle” | (paillat2023ajourneywith pages 1-3) |
| Edge | Causal edge | PorV | protein | label-only candidate | shuttles | Type A T9SS substrates | “Type A substrates… are carried from the translocon by PorV” | (lauber2024structuralinsightsinto pages 1-2) |
| Edge | Causal edge | PorV | protein | label-only candidate | not_required_for | SprB secretion / gliding in Flavobacterium johnsoniae | “PorV does not appear to be required for secretion of proteins that have type B CTDs, such as… SprB… deletion of porV… does not eliminate gliding” | (thunes2024glidingmotilityproteins pages 2-5) |
| Edge | Causal edge | SprF | protein | label-only candidate | supports | SprB function / secretion / motility | “SprF is thought to connect SprB to the rest of the motility machinery” | (thunes2024glidingmotilityproteins pages 2-5) |
| Edge | Causal edge | GldJ | protein | label-only candidate | component_of | multirail track | “multirail structure… contained GldJ protein” | (shibata2023filamentousstructuresin pages 1-2) |
| Edge | Causal edge | Gld proteins (gldJ, gldK, gldL, gldM, gldNO) | protein set | label-only candidate | required_for | multirail formation and surface SprB filaments | “mutants… lacked both multirail structures and surface SprB filaments” | (shibata2023filamentousstructuresin pages 5-6) |
| Edge | Causal edge | multirail track | structural complex | label-only candidate | guides | SprB helical translocation | “SprB filaments are propelled along tracks that may form a multi-rail system” | (shibata2023filamentousstructuresin pages 1-2) |
| Edge | Causal edge | AglRQS proton channel | complex | label-only candidate | powers | Agl-Glt trafficking | “AglR, AglQ, and AglS form a proton-driven… channel that powers directional… movement” | (islam2023unmaskingofthe pages 1-2) |
| Edge | Causal edge | Agl-Glt machinery | complex | label-only candidate | forms | bacterial focal adhesions | “Agl–Glt complexes that form bacterial focal adhesions” | (islam2023unmaskingofthe pages 1-2) |
| Edge | Causal edge | CglB | protein | label-only candidate | couples_to | substratum at bFAs | “essential substratum-coupling adhesin” | (islam2023unmaskingofthe pages 1-2) |
| Edge | Causal edge | GltABCHK platform | complex | label-only candidate | recruits_and_retains | CglB | “CglB… is recruited by the OM module… containing… GltA, GltB, GltH… GltC… GltK” | (islam2023unmaskingofthe pages 1-2) |
| Edge | Causal edge | CglB | protein | label-only candidate | immobilizes | Agl-Glt complexes to generate traction | “CglB is required to immobilize trafficked Agl–Glt complexes to generate traction” | (islam2023unmaskingofthe pages 3-5) |
| Edge | Causal edge | CglD | protein | label-only candidate | stabilizes | bacterial focal adhesions | “CglD… stabilizing… this assembly at bFAs” | (jolivet2023integrinlikeadhesincgld pages 1-3) |
| Edge | Causal edge | calcium(2+) | chemical | CHEBI:29108 | modulates | CglD-dependent bFA stabilization | “stabilizing bFAs in a calcium-dependent manner” | (jolivet2023integrinlikeadhesincgld pages 1-3) |
| Edge | Causal edge | MIDAS motif of CglB | protein feature | label-only candidate | required_for | gliding motility | “CglBD56A MIDAS mutant… fails to complement gliding deficiency” | (islam2023unmaskingofthe pages 3-5) |
| Edge | Causal edge | GltJ | protein | label-only candidate | binds | AglZ proline-rich sequence | “Complex formation was observed with micromolar affinity” | (attia2024amolecularswitch pages 1-3) |
| Edge | Causal edge | GltJ | protein | label-only candidate | binds | MglA-GTP | “GltJ… binds MglA-GTP” | (attia2024amolecularswitch pages 1-1) |
| Edge | Causal edge | GltJ | protein | label-only candidate | recruits | MreB | “recruits MreB to initiate movement” | (attia2024amolecularswitch pages 1-1) |
| Edge | Causal edge | MglA-GTP | protein/regulator | label-only candidate | promotes | bFA assembly and directionality | “MglA-GTP promotes bFA assembly and directionality” | (attia2024amolecularswitch pages 1-3) |
| Edge | Causal edge | MglB | protein/regulator | label-only candidate | triggers_disassembly_of | motility complex at lagging pole | “MglB… acts as a GAP to disassemble complexes at the rear” | (attia2024amolecularswitch pages 1-3) |
| Edge | Causal edge | removal of GldLM energetic input | perturbation | label-only candidate | causes_accumulation_of | substrate-bound translocons | “As transport intermediates accumulate… when energetic input is removed” | (lauber2024structuralinsightsinto pages 1-2) |
| Edge | Causal edge | solid surface contact | environmental factor | ENVO candidate | required_for | gliding motility | “requires cell contact with a solid surface” | (shibata2023filamentousstructuresin pages 1-2) |
| Edge | Causal edge | CCCP treatment | inhibitor exposure | CHEBI:34253 | inhibits | SprB dynamics / cell gliding | “prevent substrate secretion and halt cell displacement” | (vincent2022dynamicprotondependentmotors pages 1-2) |
| Edge | Causal edge | ΔsprB or ΔsprF | genotype perturbation | label-only candidate | decreases | gliding motility but not general secretion | “defective for motility but competent for secretion” | (thunes2024glidingmotilityproteins pages 2-5) |
| Edge | Causal edge | ΔgldJ | genotype perturbation | label-only candidate | abolishes | gliding and secretion | “a ΔgldJ mutant lacked gliding and secretion” | (thunes2024glidingmotilityproteins pages 2-5) |
| Edge | Causal edge | gltJ mutant | genotype perturbation | label-only candidate | impairs | bFA-dependent motility | “a gltJ mutant is defective in bFA-dependent motility” | (attia2024amolecularswitch pages 1-3) |
| Edge | Measurement edge | SprB translocation speed assay | assay node | label-only candidate | measures | SprB speed ~2 µm/s | “propelled at ~2 µm per second” | (shibata2023filamentousstructuresin pages 1-2) |
| Edge | Measurement edge | single-cell gliding microscopy | assay node | label-only candidate | measures | cell gliding speed ~1–5 µm/s | “move over surfaces at ~1–5 µm per second” | (shibata2023filamentousstructuresin pages 1-2) |
| Edge | Measurement edge | T9GPred HMM pipeline | computational assay | label-only candidate | predicts | 327/693 gliding-positive genomes | “identified 402… of which 327 were found to also have gliding motility” | (sahoo2023t9gpredacomprehensive pages 2-4) |


*Table: This table summarizes curation-ready candidate nodes and causal edges for microbial gliding, emphasizing 2023–2024 evidence and including quantitative measurement nodes. It is useful as a draft source for TraitMech YAML curation and for separating broadly supported edges from taxon-specific mechanisms.*

---

### Evidence-backed candidate causal edges (triple-style; highlights)
Below are key edges suitable for `gliding.yaml` candidate insertion, with notes about generality.

#### A. Core mechanistic edges: Bacteroidota (T9SS/SprB)
1) **proton gradient (PMF component)** → *powers* → **GldLM motor** (Bacteroidota) (vincent2022dynamicprotondependentmotors pages 1-2)
2) **GldLM motor** → *enables* → **T9SS-dependent secretion of SprB** (vincent2022dynamicprotondependentmotors pages 1-2)
3) **T9SS** → *secretes* → **SprB adhesin** (vincent2022dynamicprotondependentmotors pages 1-2)
4) **SprB surface translocation** → *causes* → **cell propulsion / forward screw-like motion** (vincent2022dynamicprotondependentmotors pages 1-2)
5) **GldJ** → *component_of / associated_with* → **multirail track under OM** (shibata2023filamentousstructuresin pages 1-2)
6) **gld mutants (gldJ/gldK/gldL/gldM/gldNO)** → *abolish* → **multirail structures and surface SprB filaments** (shibata2023filamentousstructuresin pages 5-6)

#### B. Core mechanistic edges: Myxococcus (Agl–Glt bFA)
1) **AglRQS proton-driven motor** → *powers* → **Agl–Glt machinery trafficking** (islam2023unmaskingofthe pages 1-2)
2) **Agl–Glt machinery** → *forms* → **bacterial focal adhesions (bFAs)** (islam2023unmaskingofthe pages 1-2)
3) **GltABCHK OM platform** → *recruits/retains* → **CglB adhesin at bFAs** (islam2023unmaskingofthe pages 1-2)
4) **CglB** → *immobilizes / couples to substratum* → **motility complexes to generate traction** (islam2023unmaskingofthe pages 3-5)
5) **GltJ** → *binds* → **AglZ** and **MglA-GTP**; **recruits MreB** → *initiates* bFA assembly and controls turnover (attia2024amolecularswitch pages 1-1, attia2024amolecularswitch pages 1-3)

#### C. Quantitative/statistical edges useful for curation context
1) **T9GPred mandatory component set (11 proteins)** → *predicts* → **gliding motility potential in genomes** (327/693 Bacteroidetes genomes predicted gliding-positive) (sahoo2023t9gpredacomprehensive pages 2-4)
2) **SprB translocation** → *has_speed* → **~2 µm/s**; **cells** → *glide_at* → **~1–5 µm/s** (shibata2023filamentousstructuresin pages 1-2)

---

### Recent developments (2023–2024) and expert-level analysis

1) **Structural consolidation of the Bacteroidota “track” concept**: Shibata et al. provide combined EM + live-tracking evidence for a multirail structure associated with SprB and containing GldJ, offering a tangible substrate for the long-standing helical-track models and strengthening edges from “GldJ complex/track” → “SprB translocation path” → “gliding”. (Publication: 2023-01; URL: https://doi.org/10.1038/s42003-023-04472-3) (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin media 5393c461, shibata2023filamentousstructuresin media 6c4a8be2)

2) **T9SS transport mechanism refined by cryo-EM (2024)**: Lauber et al. show an Extended Translocon state and infer which step is energy-dependent, strengthening a mechanistic edge from “PMF-driven energy chain” → “substrate–carrier release” and clarifying how secretion machinery can be mechanistically integrated with motility systems sharing the same power chain. (Publication: 2024-03; URL: https://doi.org/10.1038/s41564-024-01644-7) (lauber2024structuralinsightsinto pages 1-2)

3) **Myxococcus bFA assembly switch (2024)**: Attia et al. provide an explicit molecular explanation for how polarity regulators (MglA/MglB) and cytoskeletal elements (MreB, AglZ) couple to the envelope-spanning motor via GltJ, suitable for curation edges connecting regulation → complex assembly → motility. (Publication: 2024-05; URL: https://doi.org/10.1126/sciadv.adn2789) (attia2024amolecularswitch pages 1-1, attia2024amolecularswitch pages 1-3)

---

### Current applications and real-world implementations

1) **Pathogenesis/virulence (aquaculture)**: In the fish pathogen *Flavobacterium columnare*, mutants defective in gliding (sprB/sprF; or motility-defective gldJ truncation) show reduced virulence, supporting an applied edge from “gliding capacity” → “virulence contribution” (taxon-specific). (Publication: 2024-04; URL: https://doi.org/10.1128/jb.00068-24) (thunes2024glidingmotilityproteins pages 1-2, thunes2024glidingmotilityproteins pages 2-5)

2) **Genome-based trait prediction**: T9GPred provides an HMM-based pipeline to predict presence of T9SS, gliding motility, and T9SS substrates; this is directly actionable for TraitMech candidate-graph expansion from genomes (e.g., deriving “has gliding machinery” from component presence). (Publication: 2023-09; URL: https://doi.org/10.1021/acsomega.3c05155) (sahoo2023t9gpredacomprehensive pages 2-4)

---

### Relevant statistics and data (recent studies)
- **Kinematics (Bacteroidota; 2023)**: Cells “move over surfaces at ~1–5 µm per second”; SprB filaments are propelled at ~2 µm/s with ~19° tilt; labeled SprB foci can overtake others, suggesting multi-lane dynamics. (shibata2023filamentousstructuresin pages 1-2)
- **Genomics prevalence (2023)**: T9GPred screened **693** complete Bacteroidetes genomes and predicted **402** T9SS-positive, with **327** also predicted to have gliding motility based on an **11-protein mandatory set** (6 T9SS core + 5 additional motility proteins). (sahoo2023t9gpredacomprehensive pages 2-4)

---

### Ontology grounding recommendations (CURIE suggestions; non-exhaustive)
- Trait: METPO:1000706 (given)
- T9SS: GO:0098797 (candidate) (paillat2023ajourneywith pages 1-3)
- Proton motive force: GO:0015988 (vincent2022dynamicprotondependentmotors pages 1-2)
- Calcium(2+): CHEBI:29108 (jolivet2023integrinlikeadhesincgld pages 1-3)
- CCCP: CHEBI:34253 (vincent2022dynamicprotondependentmotors pages 1-2)

Many system-specific protein nodes (SprB, GldJ, GldL/M/K/N; PorV; AglR/Q/S; GltJ; CglB/D; etc.) should be grounded to UniProt accessions during curation using organism-specific sequences.

---

### Warnings / claims not yet ready for strong curation
1) **Cross-taxon generalization risk**: “Gliding” is a phenotype label spanning mechanistically distinct systems; edges must be annotated as **Bacteroidota-type** vs **Myxococcus A-motility** rather than curated as universal. (shibata2023filamentousstructuresin pages 1-2, islam2023unmaskingofthe pages 1-2)
2) **Preprint-only environmental regulation**: Calcium-dependent stabilization via CglD is supported by a bioRxiv preprint; include as **uncertain** until peer-reviewed. (jolivet2023integrinlikeadhesincgld pages 1-3)
3) **Track composition uncertainty**: While GldJ is associated with multirail structures, the exact molecular composition/assembly and how force is transmitted from GldLM to SprB via the track remains partially inferential; curate with appropriate uncertainty tags where needed. (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin pages 5-6)

---

## DOI-first bibliography (with dates/URLs)
- Shibata S. et al. **Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery.** *Communications Biology* (2023-01). https://doi.org/10.1038/s42003-023-04472-3 (shibata2023filamentousstructuresin pages 1-2)
- Lauber F. et al. **Structural insights into the mechanism of protein transport by the Type 9 Secretion System translocon.** *Nature Microbiology* (2024-03). https://doi.org/10.1038/s41564-024-01644-7 (lauber2024structuralinsightsinto pages 1-2)
- Paillat M. et al. **A journey with type IX secretion system effectors: selection, transport, processing and activities.** *Microbiology* (2023-04-12). https://doi.org/10.1099/mic.0.001320 (paillat2023ajourneywith pages 1-3)
- Attia B. et al. **A molecular switch controls assembly of bacterial focal adhesions.** *Science Advances* (2024-05-29). https://doi.org/10.1126/sciadv.adn2789 (attia2024amolecularswitch pages 1-1)
- Islam S.T. et al. **Unmasking of the von Willebrand A-domain surface adhesin CglB at bacterial focal adhesions mediates myxobacterial gliding motility.** *Science Advances* (2023-02). https://doi.org/10.1126/sciadv.abq0619 (islam2023unmaskingofthe pages 1-2)
- Thunes N.C. et al. **Gliding motility proteins GldJ and SprB contribute to Flavobacterium columnare virulence.** *Journal of Bacteriology* (2024-04). https://doi.org/10.1128/jb.00068-24 (thunes2024glidingmotilityproteins pages 1-2)
- Sahoo A.K. et al. **T9GPred: A Comprehensive Computational Tool for the Prediction of Type 9 Secretion System, Gliding Motility, and the Associated Secreted Proteins.** *ACS Omega* (2023-09). https://doi.org/10.1021/acsomega.3c05155 (sahoo2023t9gpredacomprehensive pages 2-4)
- Vincent M.S. et al. **Dynamic proton-dependent motors power type IX secretion and gliding motility in Flavobacterium.** *PLOS Biology* (2022-03-25). https://doi.org/10.1371/journal.pbio.3001443 (vincent2022dynamicprotondependentmotors pages 1-2)

---

### Included visual evidence
- EM evidence of multirail structures and schematic gliding model (Shibata et al., 2023). (shibata2023filamentousstructuresin media 5393c461, shibata2023filamentousstructuresin media 6c4a8be2)


References

1. (vincent2022dynamicprotondependentmotors pages 1-2): Maxence S. Vincent, Caterina Comas Hervada, Corinne Sebban-Kreuzer, Hugo Le Guenno, Maïalène Chabalier, Artemis Kosta, Françoise Guerlesquin, Tâm Mignot, Mark J. McBride, Eric Cascales, and Thierry Doan. Dynamic proton-dependent motors power type ix secretion and gliding motility in flavobacterium. Mar 2022. URL: https://doi.org/10.1371/journal.pbio.3001443, doi:10.1371/journal.pbio.3001443. This article has 33 citations and is from a highest quality peer-reviewed journal.

2. (shibata2023filamentousstructuresin pages 1-2): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

3. (islam2023unmaskingofthe pages 1-2): Salim T. Islam, Nicolas Y. Jolivet, Clémence Cuzin, Akeisha M. Belgrave, Laetitia My, Betty Fleuchot, Laura M. Faure, Utkarsha Mahanta, Ahmad A. Kezzo, Fares Saïdi, Gaurav Sharma, Jean-Bernard Fiche, Benjamin P. Bratton, Julien Herrou, Marcelo Nollmann, Joshua W. Shaevitz, Eric Durand, and Tâm Mignot. Unmasking of the von willebrand a-domain surface adhesin cglb at bacterial focal adhesions mediates myxobacterial gliding motility. Science Advances, Feb 2023. URL: https://doi.org/10.1126/sciadv.abq0619, doi:10.1126/sciadv.abq0619. This article has 27 citations and is from a highest quality peer-reviewed journal.

4. (paillat2023ajourneywith pages 1-3): Maëlle Paillat, Ignacio Lunar Silva, Eric Cascales, and Thierry Doan. A journey with type ix secretion system effectors: selection, transport, processing and activities. Apr 2023. URL: https://doi.org/10.1099/mic.0.001320, doi:10.1099/mic.0.001320. This article has 45 citations and is from a peer-reviewed journal.

5. (shibata2023filamentousstructuresin pages 5-6): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

6. (lauber2024structuralinsightsinto pages 1-2): Frédéric Lauber, Justin C. Deme, Xiaolong Liu, Andreas Kjær, Helen L. Miller, Felicity Alcock, Susan M. Lea, and Ben C. Berks. Structural insights into the mechanism of protein transport by the type 9 secretion system translocon. Nature Microbiology, 9:1089-1102, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01644-7, doi:10.1038/s41564-024-01644-7. This article has 32 citations and is from a highest quality peer-reviewed journal.

7. (islam2023unmaskingofthe pages 3-5): Salim T. Islam, Nicolas Y. Jolivet, Clémence Cuzin, Akeisha M. Belgrave, Laetitia My, Betty Fleuchot, Laura M. Faure, Utkarsha Mahanta, Ahmad A. Kezzo, Fares Saïdi, Gaurav Sharma, Jean-Bernard Fiche, Benjamin P. Bratton, Julien Herrou, Marcelo Nollmann, Joshua W. Shaevitz, Eric Durand, and Tâm Mignot. Unmasking of the von willebrand a-domain surface adhesin cglb at bacterial focal adhesions mediates myxobacterial gliding motility. Science Advances, Feb 2023. URL: https://doi.org/10.1126/sciadv.abq0619, doi:10.1126/sciadv.abq0619. This article has 27 citations and is from a highest quality peer-reviewed journal.

8. (attia2024amolecularswitch pages 1-1): Bouchra Attia, Laetitia My, Jean Philippe Castaing, Céline Dinet, Hugo Le Guenno, Victoria Schmidt, Leon Espinosa, Vivek Anantharaman, L. Aravind, Corinne Sebban-Kreuzer, Matthieu Nouailler, Olivier Bornet, Patrick Viollier, Latifa Elantak, and Tâm Mignot. A molecular switch controls assembly of bacterial focal adhesions. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adn2789, doi:10.1126/sciadv.adn2789. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (attia2024amolecularswitch pages 1-3): Bouchra Attia, Laetitia My, Jean Philippe Castaing, Céline Dinet, Hugo Le Guenno, Victoria Schmidt, Leon Espinosa, Vivek Anantharaman, L. Aravind, Corinne Sebban-Kreuzer, Matthieu Nouailler, Olivier Bornet, Patrick Viollier, Latifa Elantak, and Tâm Mignot. A molecular switch controls assembly of bacterial focal adhesions. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adn2789, doi:10.1126/sciadv.adn2789. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (jolivet2023integrinlikeadhesincgld pages 1-3): Nicolas Y. Jolivet, Endao Han, Akeisha M. Belgrave, Fares Saïdi, Newsha Koushki, David J. Lemon, Laura M. Faure, Betty Fleuchot, Utkarsha Mahanta, Heng Jiang, Gaurav Sharma, Jean-Bernard Fiche, Benjamin P. Bratton, Mamoudou Diallo, Beiyan Nan, David R. Zusman, Guillaume Sudre, Anthony Garza, Marcelo Nollmann, Allen J. Ehrlicher, Olivier Théodoly, Joshua W. Shaevitz, Tâm Mignot, and Salim T. Islam. Integrin-like adhesin cgld confers traction and stabilizes bacterial focal adhesions involved in myxobacterial gliding motility. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.10.19.562135, doi:10.1101/2023.10.19.562135. This article has 7 citations.

11. (thunes2024glidingmotilityproteins pages 2-5): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 5 citations and is from a peer-reviewed journal.

12. (lauber2024structuralinsightsinto pages 5-6): Frédéric Lauber, Justin C. Deme, Xiaolong Liu, Andreas Kjær, Helen L. Miller, Felicity Alcock, Susan M. Lea, and Ben C. Berks. Structural insights into the mechanism of protein transport by the type 9 secretion system translocon. Nature Microbiology, 9:1089-1102, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01644-7, doi:10.1038/s41564-024-01644-7. This article has 32 citations and is from a highest quality peer-reviewed journal.

13. (lauber2024structuralinsightsinto pages 2-3): Frédéric Lauber, Justin C. Deme, Xiaolong Liu, Andreas Kjær, Helen L. Miller, Felicity Alcock, Susan M. Lea, and Ben C. Berks. Structural insights into the mechanism of protein transport by the type 9 secretion system translocon. Nature Microbiology, 9:1089-1102, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01644-7, doi:10.1038/s41564-024-01644-7. This article has 32 citations and is from a highest quality peer-reviewed journal.

14. (sahoo2023t9gpredacomprehensive pages 2-4): Ajaya Kumar Sahoo, R. P. Vivek-Ananth, Nikhil Chivukula, Shri Vishalini Rajaram, Karthikeyan Mohanraj, Devanshi Khare, Celin Acharya, and Areejit Samal. T9gpred: a comprehensive computational tool for the prediction of type 9 secretion system, gliding motility, and the associated secreted proteins. ACS Omega, 8:34091-34102, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c05155, doi:10.1021/acsomega.3c05155. This article has 10 citations and is from a peer-reviewed journal.

15. (shibata2023filamentousstructuresin media 5393c461): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

16. (shibata2023filamentousstructuresin media 6c4a8be2): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

17. (thunes2024glidingmotilityproteins pages 1-2): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 5 citations and is from a peer-reviewed journal.