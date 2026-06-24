---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:32:25.409842'
end_time: '2026-06-17T20:43:34.349000'
duration_seconds: 668.94
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: parasitism
  trait_identifier: traitmech:000043
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: parasitism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism benefits at the expense of its
    host's fitness, deriving resources from the host while causing it harm.
  parent_traits: traitmech:000040
  synonyms: parasitic
  evidence_summary: 'DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism
    as the harmful pole of the parasite-mutualist continuum and describe evolutionary
    transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support
    host-exploitative associations as one outcome of the shared host-colonization
    toolkit.)'
  causal_graph_summary: 'parasitism_host_fitness_cost: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** parasitism
- **METPO identifier:** traitmech:000043
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits at the expense of its host's fitness, deriving resources from the host while causing it harm.
- **Parent traits:** traitmech:000040
- **Synonyms:** parasitic
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism as the harmful pole of the parasite-mutualist continuum and describe evolutionary transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support host-exploitative associations as one outcome of the shared host-colonization toolkit.)
- **Existing causal graph summary:** parasitism_host_fitness_cost: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **parasitism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/parasitism.yaml`.

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
- **Trait label:** parasitism
- **METPO identifier:** traitmech:000043
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits at the expense of its host's fitness, deriving resources from the host while causing it harm.
- **Parent traits:** traitmech:000040
- **Synonyms:** parasitic
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism as the harmful pole of the parasite-mutualist continuum and describe evolutionary transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support host-exploitative associations as one outcome of the shared host-colonization toolkit.)
- **Existing causal graph summary:** parasitism_host_fitness_cost: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **parasitism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/parasitism.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **Parasitism** (METPO:traitmech:000043)

## 1. Scope summary (trait meaning, boundaries, and current understanding)

### 1.1 Operational trait meaning
Parasitism (TraitMech: **traitmech:000043**) is best operationalized as a *symbiotic* (inter-species, intimate) association in which the microbe’s growth/transmission is enabled by **host exploitation** and yields a **net cost to host fitness** (reduced survival, fertility, or other fitness components). A recent synthesis of textbook definitions emphasizes that “most definitions declare parasitism is a long-lasting relationship between individuals of different species harming the hosts,” and that evolutionary ecologists operationalize host harm as a “reduction of host’s fitness (longevity, fertility or both)” (rozsa2023definitionsofparasitism pages 1-2).

A minimal TraitMech causal-graph interpretation consistent with this literature is:
- **Host resource use → host harm/fitness cost**, because “parasites harm their hosts by utilizing them as nutrient resources” (rozsa2023definitionsofparasitism pages 1-2).

### 1.2 Boundary cases and distinctions
**(i) Parasitism–mutualism continuum and context dependence.** Endosymbiont effects can “extend from parasitic to mutualistic,” with transitions influenced by transmission mode and ecological context (hoffmann2024describingendosymbiont–hostinteractions pages 1-2). This supports modeling parasitism as a *conditional* ecological trait, not a fixed property.

**(ii) Multilevel ambiguity (cell vs individual vs lineage vs population).** Parasitism labels can depend on which organizational level is evaluated; infections can show “opposite effects at different levels of biological organization” (rozsa2023definitionsofparasitism pages 1-2). This creates curation risk if “host fitness” is not explicitly defined (e.g., individual survival vs population growth).

**(iii) Distinguish from parasitoidism/lethal exploitation.** The Rózsa & Garay synthesis highlights a continuum “from non-lethal … parasitism to lethal parasitism (properly called parasitoidism)” (rozsa2023definitionsofparasitism pages 2-3). For TraitMech curation, lethal host-killing strategies may be out-of-scope unless the trait definition explicitly includes parasitoids.

**(iv) Distinguish from commensalism and mutualism.** Newly introduced/facultative endosymbionts “are often seen as parasites, gaining resources from their hosts,” whereas “vertical transmission favors coevolution toward mutualism” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2). Thus, *transmission mode* is a boundary-condition node for parasitism classification.

## 2. Recent developments and mechanistic themes (priority 2023–2024)

This section summarizes mechanistic entities/edges with strong recent evidence suitable for a TraitMech causal graph.

### 2.1 Colonization as an upstream requirement for parasitism
A 2024 FEMS Microbiology Reviews synthesis of bacterial host adaptation emphasizes adhesion as a general prerequisite: “The expression of bacterial surface molecules termed adhesins is critical for adherence to host tissues” (barber2024mechanismsofhost pages 3-5). Host receptor specificity (e.g., CEACAM- or E-cadherin-binding) becomes a mechanism determining host range and colonization success (barber2024mechanismsofhost pages 3-5).

### 2.2 Host tissue invasion/dissemination via hijacking host coagulation/fibrinolysis
The same review highlights dissemination mechanisms that directly contribute to host damage/pathology and within-host spread. Pathogens can bind fibrinogen and modulate coagulation; attachment can promote “biofilm or abscess formation, exacerbating disease pathology” (barber2024mechanismsofhost pages 3-5). Additionally, “By binding to and activating plasminogen, pathogens are able to break down clots and host extracellular matrix components to promote dissemination during systemic infection” (barber2024mechanismsofhost pages 3-5).

### 2.3 Nutritional immunity interface: metal and hemoglobin/heme acquisition
Barber & Fitzgerald (2024) frames transition-metal acquisition (iron, zinc, manganese) as a major barrier to growth within hosts and a driver of host-pathogen adaptation (barber2024mechanismsofhost pages 5-6). Key curated mechanisms include:
- **Transferrin binding by bacterial receptors (TbpA)** (barber2024mechanismsofhost pages 5-6).
- **Calprotectin binding for zinc scavenging (TdfH)** (barber2024mechanismsofhost pages 5-6).
- **Hemoglobin as a major iron pool**: “Roughly 70% of the iron in the human body is bound within red blood cells in the hemoglobin protein complex as the porphyrin cofactor heme” (barber2024mechanismsofhost pages 5-6).
- **Species-biased hemoglobin uptake** via S. aureus IsdB (barber2024mechanismsofhost pages 5-6).

In eukaryotic parasites, a 2023 Frontiers review emphasizes hemoglobin/heme as host-derived nutrients, and identifies **parasite-derived proteases** as “major virulence factors… essential for host tissue degradation, immune evasion, and nutrient acquisition”; specifically, “The production of Hb-degrading proteases is a Hb uptake mechanism that degrades globin… and facilitates heme release” (reyeslopez2023hemoglobinuptakeand pages 1-2).

### 2.4 Immune manipulation via ubiquitin pathways and pathogen deubiquitinases
A 2023 Frontiers in Immunology mini-review concludes that “Deubiquitinating enzymes (DUBs) are emerging as key factors for the infection of human cells by pathogens such as bacteria and parasites,” acting through “exploiting and manipulating ubiquitin (Ub)-dependent host processes during infection” (wehrmann2023theemergingrole pages 1-2). For Legionella, “Lot class DUBs are localized in the vacuolar membrane to establish the replication vacuole during infection” (wehrmann2023theemergingrole pages 1-2), supporting an edge from pathogen DUB activity → intracellular niche establishment.

### 2.5 Intracellular parasitism under IFNγ: functional genomics of parasite fitness determinants
A 2023 mBio CRISPR screen identifies parasite genes determining **Toxoplasma fitness** in IFNγ-stimulated human cells, explicitly linking immune stress to parasite survival strategies (krishnamurthy2023crisprscreensidentify pages 1-2). Mechanistic statements suitable for edges include:
- Host restriction: “IFNg upregulates tryptophan catabolism via induction of the enzyme Indoleamine-2,3-dioxygenase (IDO), which inhibits growth of Toxoplasma” (krishnamurthy2023crisprscreensidentify pages 1-2).
- Parasite countermeasures and vacuolar survival: “ROPs and GRAs together ensure parasite survival within the PV” (krishnamurthy2023crisprscreensidentify pages 1-2).
- Fitness determinant: “prevention of early egress is an important Toxoplasma fitness determinant in IFNg-stimulated human cells” (krishnamurthy2023crisprscreensidentify pages 1-2).

### 2.6 Secretion systems as causal drivers of host signaling manipulation and persistence
In Bordetella respiratory infection, host immunomodulatory signaling is directly linked to bacterial persistence. The 2023 study reports that VPAC2-deficient mice show reduced colonization: “VPAC2-/- mice… hinder the ability of the bacteria to colonize the lungs, resulting in decreased bacterial burden,” and concludes that manipulation “appears to be mediated by the type 3 secretion system (T3SS)” (first2023bordetellaspp.utilize pages 1-2). This supports a mechanism node: T3SS → host signaling manipulation → colonization/persistence.

### 2.7 Parasite–microbiota interactions as modulators of parasitism outcomes
A 2024 Pathogens review states that parasites can influence local microbes “by sequestering resources and through the direct action of parasite-produced antimicrobial agents such as excretory–secretory products (ESPs) and extracellular vesicles (ECVs)” (grondin2024interactionbetweenintestinal pages 2-3). The same review summarizes that helminth ESPs participate in “evasion” and have microbiota-modulating effects (grondin2024interactionbetweenintestinal pages 2-3), supporting edges from parasite secretions → microbiome shifts → altered infection outcomes.

### 2.8 Abiotic environmental stress as a switch increasing parasitic colonization and host damage
In a 2024 ISME Journal study, copper is treated as an abiotic modifier of amoeba–bacteria symbiosis. Under copper stress, “parasitic symbionts exhibited enhanced colonization of amoebae,” and “the pathogenic effects of parasitic symbionts on hosts were exacerbated under copper stress” (shi2024copperstressshapes pages 1-2). This is a high-value curation anchor for ENVO/CHEBI-grounded environmental edges.

## 3. Candidate nodes for `data/traits/ecology/parasitism.yaml`

A curation-oriented node inventory (with suggested grounding where feasible) is provided below.

| Node label | Group/type | Suggested CURIE | Support/evidence basis |
|---|---|---|---|
| parasitism | Processes/traits | METPO:traitmech:000043 | Trait definition: microorganism benefits at expense of host fitness; long-lasting harmful symbiosis (rozsa2023definitionsofparasitism pages 1-2) |
| host fitness reduction | Processes/traits |  | Core definitional outcome of parasitism; host harm, reduced longevity/fertility (rozsa2023definitionsofparasitism pages 1-2) |
| host colonization | Processes/traits | GO:0044412 | Central step in pathogenic adaptation and parasitic establishment (barber2024mechanismsofhost pages 3-5, first2023bordetellaspp.utilize pages 1-2) |
| host cell/tissue adherence | Processes/traits | GO:0044406 | Adhesins are critical for adherence to host tissues (barber2024mechanismsofhost pages 3-5) |
| immune evasion | Processes/traits | GO:0044416 | Parasites/pathogens manipulate or evade host immune responses (wehrmann2023theemergingrole pages 1-2, krishnamurthy2023crisprscreensidentify pages 1-2, reyeslopez2023hemoglobinuptakeand pages 1-2) |
| nutrient acquisition from host | Processes/traits | GO:0044402 | Parasites harm hosts by using them as nutrient resources (rozsa2023definitionsofparasitism pages 1-2, reyeslopez2023hemoglobinuptakeand pages 1-2, barber2024mechanismsofhost pages 5-6) |
| dissemination within host | Processes/traits |  | Plasminogen activation promotes dissemination during infection (barber2024mechanismsofhost pages 3-5) |
| replication vacuole establishment | Processes/traits |  | Legionella DUBs establish replication vacuole during infection (wehrmann2023theemergingrole pages 1-2) |
| parasitophorous vacuole survival | Processes/traits |  | Toxoplasma GRAs/ROPs ensure parasite survival in PV (krishnamurthy2023crisprscreensidentify pages 1-2) |
| early parasite egress prevention | Processes/traits |  | Important determinant of Toxoplasma fitness in IFNγ-stimulated cells (krishnamurthy2023crisprscreensidentify pages 1-2) |
| biofilm/abscess formation | Processes/traits |  | Fibrinogen-binding interactions promote biofilm or abscess formation (barber2024mechanismsofhost pages 3-5) |
| microbiota modulation | Processes/traits |  | Parasite ESPs/ECVs alter microbial composition and function (grondin2024interactionbetweenintestinal pages 2-3) |
| type III secretion system | Pathways/modules |  | T3SS mediates host signaling manipulation and persistence in Bordetella; broad effector-delivery paradigm (first2023bordetellaspp.utilize pages 1-2) |
| ubiquitin-dependent host process manipulation | Pathways/modules |  | Pathogen DUBs exploit ubiquitin-dependent host pathways (wehrmann2023theemergingrole pages 1-2) |
| hemoglobin uptake/utilization | Pathways/modules |  | Human protozoan parasites use Hb/heme uptake mechanisms to survive in host (reyeslopez2023hemoglobinuptakeand pages 1-2) |
| heme release from hemoglobin | Pathways/modules |  | Hb-degrading proteases facilitate heme release (reyeslopez2023hemoglobinuptakeand pages 1-2) |
| siderophore-mediated metal acquisition | Pathways/modules |  | Secreted siderophores compete for host metals and are reacquired by bacteria (barber2024mechanismsofhost pages 5-6) |
| transferrin-dependent iron scavenging | Pathways/modules |  | TbpA-mediated acquisition from host transferrin (barber2024mechanismsofhost pages 5-6) |
| calprotectin-dependent zinc scavenging | Pathways/modules |  | TdfH binds calprotectin to mediate zinc scavenging (barber2024mechanismsofhost pages 5-6) |
| tryptophan catabolism by host IDO | Pathways/modules |  | IFNγ-induced IDO depletes tryptophan and restricts Toxoplasma growth (krishnamurthy2023crisprscreensidentify pages 1-2) |
| CEACAM-binding adhesin | Genes/proteins/complexes |  | Bacterial adhesins binding epithelial CEACAM mediate host colonization (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 5-6) |
| InlA | Genes/proteins/complexes |  | Listeria surface protein with host-specific E-cadherin binding (barber2024mechanismsofhost pages 3-5) |
| fibrinogen-binding proteins | Genes/proteins/complexes |  | Promote clot interaction, colonization, and abscess formation (barber2024mechanismsofhost pages 3-5) |
| staphylocoagulase (Coa) | Genes/proteins/complexes |  | Coagulation-related virulence factor in staphylococci (barber2024mechanismsofhost pages 3-5) |
| von Willebrand-binding protein (vWbp) | Genes/proteins/complexes |  | Host-specific coagulation activity in staphylococci (barber2024mechanismsofhost pages 3-5) |
| streptokinase | Genes/proteins/complexes |  | Activates host plasminogen to promote dissemination (barber2024mechanismsofhost pages 3-5) |
| staphylokinase | Genes/proteins/complexes |  | Host plasminogen-activating factor promoting dissemination (barber2024mechanismsofhost pages 3-5) |
| transferrin-binding protein A (TbpA) | Genes/proteins/complexes |  | TonB-dependent receptor for host transferrin (barber2024mechanismsofhost pages 5-6) |
| TdfH | Genes/proteins/complexes |  | Outer-membrane receptor binding calprotectin for zinc scavenging (barber2024mechanismsofhost pages 5-6) |
| IsdB | Genes/proteins/complexes |  | Hemoglobin receptor enabling heme/iron acquisition (barber2024mechanismsofhost pages 5-6) |
| pathogen deubiquitinating enzymes (DUBs) | Genes/proteins/complexes |  | Key infection factors manipulating host ubiquitin pathways (wehrmann2023theemergingrole pages 1-2) |
| LotA | Genes/proteins/complexes |  | Legionella DUB important for replication vacuole establishment (wehrmann2023theemergingrole pages 1-2) |
| LotB | Genes/proteins/complexes |  | Legionella DUB reversing K63-linked ubiquitination of Sec22b (wehrmann2023theemergingrole pages 1-2) |
| LotC | Genes/proteins/complexes |  | Legionella DUB controlling Rab10 ubiquitination (wehrmann2023theemergingrole pages 1-2) |
| GRA32-related dense-granule complex | Genes/proteins/complexes |  | Toxoplasma complex preventing early egress in IFNγ-stimulated cells (krishnamurthy2023crisprscreensidentify pages 1-2) |
| GRAs | Genes/proteins/complexes |  | Dense granule effectors that alter host signaling and promote PV survival (krishnamurthy2023crisprscreensidentify pages 1-2) |
| ROPs | Genes/proteins/complexes |  | Rhoptry effectors important for host modulation and PV survival (krishnamurthy2023crisprscreensidentify pages 1-2) |
| GRA15 | Genes/proteins/complexes |  | Recruits host ubiquitin ligases to PVM (krishnamurthy2023crisprscreensidentify pages 1-2) |
| parasite-derived Hb-degrading proteases | Genes/proteins/complexes |  | Major virulence factors for tissue degradation, immune evasion, nutrient acquisition (reyeslopez2023hemoglobinuptakeand pages 1-2) |
| excretory-secretory products (ESPs) | Genes/proteins/complexes |  | Parasite-derived products affecting microbes and host immunity (grondin2024interactionbetweenintestinal pages 2-3) |
| extracellular vesicles (ECVs) | Genes/proteins/complexes |  | Parasite-produced antimicrobial/microbiota-modulating factors (grondin2024interactionbetweenintestinal pages 2-3) |
| hemoglobin | Chemicals/metabolites/nutrients | CHEBI:35143 | Major source of iron and amino acids for pathogens (reyeslopez2023hemoglobinuptakeand pages 1-2, barber2024mechanismsofhost pages 5-6) |
| heme | Chemicals/metabolites/nutrients | CHEBI:30413 | Released from Hb and used as essential iron source (reyeslopez2023hemoglobinuptakeand pages 1-2) |
| iron | Chemicals/metabolites/nutrients | CHEBI:18248 | Essential nutrient; major target of host-pathogen competition (reyeslopez2023hemoglobinuptakeand pages 1-2, barber2024mechanismsofhost pages 5-6) |
| zinc | Chemicals/metabolites/nutrients | CHEBI:27363 | Scavenged from calprotectin by pathogens (barber2024mechanismsofhost pages 5-6) |
| manganese | Chemicals/metabolites/nutrients | CHEBI:29035 | Sequestered by calprotectin as part of nutritional immunity (barber2024mechanismsofhost pages 5-6) |
| transferrin | Chemicals/metabolites/nutrients |  | Host iron-binding protein targeted by TbpA (barber2024mechanismsofhost pages 5-6) |
| lactoferrin | Chemicals/metabolites/nutrients |  | Host iron-binding protein under pathogen-driven selection (barber2024mechanismsofhost pages 5-6) |
| calprotectin | Chemicals/metabolites/nutrients |  | Host metal-sequestering protein targeted by TdfH (barber2024mechanismsofhost pages 5-6) |
| plasminogen | Chemicals/metabolites/nutrients |  | Host protease precursor hijacked for dissemination (barber2024mechanismsofhost pages 3-5) |
| fibrinogen | Chemicals/metabolites/nutrients |  | Host coagulation protein bound by pathogen virulence factors (barber2024mechanismsofhost pages 3-5) |
| L-tryptophan | Chemicals/metabolites/nutrients |  | Nutrient limited by host IDO during IFNγ response (krishnamurthy2023crisprscreensidentify pages 1-2) |
| cholesterol | Chemicals/metabolites/nutrients |  | Host nutrient whose availability affects Toxoplasma (krishnamurthy2023crisprscreensidentify pages 1-2) |
| copper | Environmental/experimental factors | CHEBI:28694 | Elevated copper stress enhances colonization by parasitic symbionts and worsens host damage (shi2024copperstressshapes pages 1-2) |
| copper stress | Environmental/experimental factors |  | Abiotic condition shifting symbiosis toward more pathogenic outcomes (shi2024copperstressshapes pages 1-2) |
| IFNγ stimulation | Environmental/experimental factors |  | Host immune activation state restricting parasite growth and revealing fitness determinants (krishnamurthy2023crisprscreensidentify pages 1-2) |
| VPAC2 antagonist treatment | Environmental/experimental factors |  | Reduced lung pathology in Bordetella model (first2023bordetellaspp.utilize pages 1-2) |
| vertical transmission | Environmental/experimental factors |  | Favors coevolution toward mutualism rather than parasitism (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) |
| newly acquired facultative endosymbiont state | Environmental/experimental factors |  | Often associated with parasitic interactions (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) |
| host CEACAM proteins | Host factors |  | Epithelial receptors for pathogen adhesins; affect colonization and immune recognition (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 5-6) |
| E-cadherin | Host factors |  | Human target of Listeria InlA (barber2024mechanismsofhost pages 3-5) |
| decoy CEACAMs on neutrophils | Host factors |  | Mediate opsonization and phagocytosis, shaping evasion pressure (barber2024mechanismsofhost pages 5-6) |
| VIP/VPAC2 signaling axis | Host factors |  | Anti-inflammatory host pathway manipulated by Bordetella T3SS (first2023bordetellaspp.utilize pages 1-2) |
| interferon gamma (IFNγ) | Host factors |  | Induces toxoplasmacidal mechanisms and nutrient restriction (krishnamurthy2023crisprscreensidentify pages 1-2) |
| indoleamine-2,3-dioxygenase (IDO) | Host factors |  | Host enzyme depleting tryptophan to inhibit Toxoplasma growth (krishnamurthy2023crisprscreensidentify pages 1-2) |
| TRAF2 | Host factors |  | Host ubiquitin ligase/recruitment factor at Toxoplasma PVM (krishnamurthy2023crisprscreensidentify pages 1-2) |
| TRAF6 | Host factors |  | Host ubiquitin ligase/recruitment factor at Toxoplasma PVM (krishnamurthy2023crisprscreensidentify pages 1-2) |
| RNF213 | Host factors |  | Host ubiquitin ligase mediating PV ubiquitination (krishnamurthy2023crisprscreensidentify pages 1-2) |
| p62/NDP52 ubiquitin receptors | Host factors |  | Recruited to ubiquitinated PVM during restriction (krishnamurthy2023crisprscreensidentify pages 1-2) |
| LC3B/GABARAP | Host factors |  | Ubiquitin-like molecules recruited during PV restriction (krishnamurthy2023crisprscreensidentify pages 1-2) |
| IRGs | Host factors |  | Murine IFNγ-induced factors destroying PV (krishnamurthy2023crisprscreensidentify pages 1-2) |
| GBPs | Host factors |  | Murine/human restriction factors in anti-Toxoplasma responses (krishnamurthy2023crisprscreensidentify pages 1-2) |
| ASC | Host factors |  | Mediates atypical apoptotic response in infected macrophages (krishnamurthy2023crisprscreensidentify pages 1-2) |
| caspase-8 | Host factors |  | Acts with ASC in IFNγ-induced atypical apoptosis (krishnamurthy2023crisprscreensidentify pages 1-2) |
| AIM2 | Host factors |  | Sensor involved in macrophage response to Toxoplasma (krishnamurthy2023crisprscreensidentify pages 1-2) |
| gut microbiota | Microbiota factors |  | Competes with parasites and shapes infection outcomes (grondin2024interactionbetweenintestinal pages 2-3) |
| Escherichia coli | Microbiota factors |  | Growth/survival affected by helminth ESPs (grondin2024interactionbetweenintestinal pages 2-3) |
| Bacillus subtilis | Microbiota factors |  | Growth/survival affected by helminth ESPs (grondin2024interactionbetweenintestinal pages 2-3) |
| Lactobacillaceae | Microbiota factors |  | Increased in some helminth-infected mice (grondin2024interactionbetweenintestinal pages 2-3) |
| Bacteroidetes | Microbiota factors |  | Reduced during T. muris infection in mice (grondin2024interactionbetweenintestinal pages 2-3) |
| Proteobacteria | Microbiota factors |  | Increased in some protozoan/helminth infection settings (grondin2024interactionbetweenintestinal pages 2-3) |
| Paraburkholderia symbionts | Microbiota factors |  | Amoeba-associated bacteria ranging from mutualistic to pathogenic (shi2024copperstressshapes pages 1-2) |
| parasitic symbiont colonization of amoebae | Microbiota factors |  | Enhanced under copper stress (shi2024copperstressshapes pages 1-2) |


*Table: This table lists evidence-supported candidate nodes for a microbial parasitism causal graph, grouped by biological role and grounded to identifiers where possible. It is useful as a curation starter set for selecting graph entities before assigning causal edges.*

## 4. Evidence-backed candidate causal edges (triples)

The following table is directly usable as a starting point for TraitMech edge curation, including snippets and uncertainty notes.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| bacterial adhesin activity (GO:0044406 candidate) | promotes | host colonization (GO:0044412) | “The expression of bacterial surface molecules termed adhesins is critical for adherence to host tissues.” (barber2024mechanismsofhost pages 3-5) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Broad bacterial mechanism; useful high-level parasitism edge. |
| CEACAM-binding adhesin | mediates | epithelial host colonization (GO:0044412) | “Binding of bacterial adhesins to epithelial CEACAM subsequently mediates host colonization.” (barber2024mechanismsofhost pages 3-5) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Taxon-specific examples in Helicobacter/Neisseria/Moraxella, but mechanism generalizable to receptor-mediated colonization. |
| CEACAM-binding adhesin | promotes | immune evasion (GO:0044416 candidate) | adhesins “also impact recognition by primate neutrophils that express ‘decoy’ CEACAMs, which mediate bacterial opsonization and phagocytosis” (barber2024mechanismsofhost pages 5-6) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Inferred direction: altered CEACAM recognition can aid evasion while supporting colonization. |
| fibrinogen-binding protein | promotes | abscess/biofilm formation | “attachment further promotes biofilm or abscess formation, exacerbating disease pathology” (barber2024mechanismsofhost pages 3-5) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Specific proteins differ by taxon; curate as candidate process-level edge. |
| plasminogen binding/activation | promotes | pathogen dissemination (GO:0044407 candidate) | “By binding to and activating plasminogen, pathogens are able to break down clots and host extracellular matrix components to promote dissemination” (barber2024mechanismsofhost pages 3-5) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Strong evidence for host exploitation after colonization. |
| type III secretion system (T3SS) | mediates | VIP/VPAC2 signaling manipulation | “the ability of Bordetella spp. to manipulate VIP/VPAC signaling pathway appears to be mediated by the type 3 secretion system (T3SS)” (first2023bordetellaspp.utilize pages 1-2) | First et al. 2023. DOI:10.3389/fcimb.2023.1111502 · https://doi.org/10.3389/fcimb.2023.1111502 · 2023 | Strong but Bordetella-focused. |
| VIP/VPAC2 signaling manipulation | promotes | lung colonization/persistence | “VPAC2-/- mice… hinder the ability of the bacteria to colonize the lungs, resulting in decreased bacterial burden” (first2023bordetellaspp.utilize pages 1-2) | First et al. 2023. DOI:10.3389/fcimb.2023.1111502 · https://doi.org/10.3389/fcimb.2023.1111502 · 2023 | Host signaling axis; useful host-side node for parasitism graph. |
| pathogen-derived deubiquitinating enzyme activity | promotes | exploitation of Ub-dependent host pathways | “DUBs are emerging as key factors… exploiting and manipulating ubiquitin (Ub)-dependent host processes during infection” (wehrmann2023theemergingrole pages 1-2) | Wehrmann & Vilchez 2023. DOI:10.3389/fimmu.2023.1303072 · https://doi.org/10.3389/fimmu.2023.1303072 · 2023 | Cross-bacteria/parasite review; broad but strong conceptual edge. |
| Legionella LotA/LotB/LotC DUBs | promotes | replication vacuole establishment/maintenance | “Lot class DUBs are localized in the vacuolar membrane to establish the replication vacuole during infection” (wehrmann2023theemergingrole pages 1-2) | Wehrmann & Vilchez 2023. DOI:10.3389/fimmu.2023.1303072 · https://doi.org/10.3389/fimmu.2023.1303072 · 2023 | Taxon-specific; do not overgeneralize beyond intracellular pathogens using DUBs. |
| dense-granule/rhoptry effectors (GRA/ROP) | promotes | parasite survival within parasitophorous vacuole | “ROPs and GRAs together ensure parasite survival within the PV” (krishnamurthy2023crisprscreensidentify pages 1-2) | Krishnamurthy et al. 2023. DOI:10.1128/mbio.00060-23 · https://doi.org/10.1128/mbio.00060-23 · 2023 | Strong Toxoplasma-specific intracellular parasitism mechanism. |
| Toxoplasma GRA32-related dense-granule complex | inhibits | early parasite egress | “Deletion of individual members of this complex leads to early parasite egress” (krishnamurthy2023crisprscreensidentify pages 1-2) | Krishnamurthy et al. 2023. DOI:10.1128/mbio.00060-23 · https://doi.org/10.1128/mbio.00060-23 · 2023 | Supported by knockout data in IFNγ-stimulated human fibroblasts. |
| inhibition of early parasite egress | promotes | parasite fitness in IFNγ-stimulated human cells | “prevention of early egress is an important Toxoplasma fitness determinant” (krishnamurthy2023crisprscreensidentify pages 1-2) | Krishnamurthy et al. 2023. DOI:10.1128/mbio.00060-23 · https://doi.org/10.1128/mbio.00060-23 · 2023 | Assay-specific but mechanistically clear. |
| host IFNγ-induced IDO activity (GO:0036376 candidate) | inhibits | Toxoplasma growth | “IFNg upregulates tryptophan catabolism via induction of the enzyme Indoleamine-2,3-dioxygenase (IDO), which inhibits growth of Toxoplasma” (krishnamurthy2023crisprscreensidentify pages 1-2) | Krishnamurthy et al. 2023. DOI:10.1128/mbio.00060-23 · https://doi.org/10.1128/mbio.00060-23 · 2023 | Host defense edge; relevant as negative control/constraint in parasitism graph. |
| hemoglobin uptake mechanism | promotes | parasite survival inside host | “Hb and heme-uptake mechanisms utilized by human pathogenic protozoa to survive inside the host” (reyeslopez2023hemoglobinuptakeand pages 1-2) | Reyes-López et al. 2023. DOI:10.3389/fcimb.2023.1150054 · https://doi.org/10.3389/fcimb.2023.1150054 · 2023 | Broad review statement; suitable as process-level edge. |
| parasite-derived Hb-degrading proteases | promotes | nutrient acquisition | “parasite-derived proteases, essential for host tissue degradation, immune evasion, and nutrient acquisition” (reyeslopez2023hemoglobinuptakeand pages 1-2) | Reyes-López et al. 2023. DOI:10.3389/fcimb.2023.1150054 · https://doi.org/10.3389/fcimb.2023.1150054 · 2023 | Good cross-protozoan nutrient-exploitation mechanism. |
| parasite-derived Hb-degrading proteases | promotes | heme release from hemoglobin | “The production of Hb-degrading proteases is a Hb uptake mechanism that degrades globin… and facilitates heme release.” (reyeslopez2023hemoglobinuptakeand pages 1-2) | Reyes-López et al. 2023. DOI:10.3389/fcimb.2023.1150054 · https://doi.org/10.3389/fcimb.2023.1150054 · 2023 | Mechanistically precise; protozoan-focused. |
| transferrin-binding protein A (TbpA) | mediates | iron scavenging from transferrin | “rapidly evolving regions of the protein match closely with the binding surface of transferrin-binding protein A (TbpA)” (barber2024mechanismsofhost pages 5-6) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Iron acquisition edge; receptor well established but examples are Gram-negative taxa. |
| TdfH outer membrane receptor | mediates | zinc scavenging from calprotectin | “TdfH… binds calprotectin to mediate zinc scavenging” (barber2024mechanismsofhost pages 5-6) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Specific to N. gonorrhoeae; strong nutrient-immunity interface. |
| siderophore secretion | promotes | metal acquisition | “siderophores… can effectively compete with host proteins for metals. Metal-bound siderophores are subsequently reacquired” (barber2024mechanismsofhost pages 5-6) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | General pathogen nutrient-acquisition mechanism. |
| IsdB hemoglobin receptor | promotes | heme/iron acquisition from hemoglobin | “the hemoglobin receptor IsdB in S. aureus had previously been shown to bind human hemoglobin more effectively than mouse” (barber2024mechanismsofhost pages 5-6) | Barber & Fitzgerald 2024. DOI:10.1093/femsre/fuae019 · https://doi.org/10.1093/femsre/fuae019 · 2024 | Species-specific receptor example; useful as candidate grounded protein node. |
| excretory–secretory products (ESPs) | modulates | gut microbiota composition | “ESPs released by helminths have been shown to have microbiota-modulating effects” (grondin2024interactionbetweenintestinal pages 2-3) | Grondin et al. 2024. DOI:10.3390/pathogens13080608 · https://doi.org/10.3390/pathogens13080608 · 2024 | Mostly intestinal parasites; process-level node appropriate. |
| ESPs | inhibits | bacterial growth/survival | “ESPs released by the helminth Teladorsagia circumcincta impacted Escherichia coli and Bacillus subtilis growth and survival in vitro” (grondin2024interactionbetweenintestinal pages 2-3) | Grondin et al. 2024. DOI:10.3390/pathogens13080608 · https://doi.org/10.3390/pathogens13080608 · 2024 | Assay-specific and helminth-focused; mark uncertain for microbial-trait generalization. |
| parasite-produced antimicrobial agents / resource sequestration | promotes | establishment of infection | “strategies employed by parasites… play a role in the establishment of infection” and parasites influence microbes “by sequestering resources” (grondin2024interactionbetweenintestinal pages 2-3) | Grondin et al. 2024. DOI:10.3390/pathogens13080608 · https://doi.org/10.3390/pathogens13080608 · 2024 | Composite mechanism; curate cautiously as a high-level edge. |
| vertical transmission | promotes | evolution toward mutualism | “vertical transmission favors coevolution toward mutualism” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) | Hoffmann & Cooper 2024. DOI:10.1002/ece3.11705 · https://doi.org/10.1002/ece3.11705 · 2024 | Important boundary-case edge showing when parasitism may shift away; relevant warning for trait scope. |
| newly acquired facultative endosymbiont state | promotes | parasitic interaction with host | “Newly acquired facultative endosymbionts are often seen as parasites, gaining resources from their hosts” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) | Hoffmann & Cooper 2024. DOI:10.1002/ece3.11705 · https://doi.org/10.1002/ece3.11705 · 2024 | Good trait-scope edge for parasitism onset. |
| high endosymbiont density in host tissues | promotes | host harm/death | “High endosymbiont densities in host tissues are often seen as having particularly strong negative effects that can even kill hosts” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) | Hoffmann & Cooper 2024. DOI:10.1002/ece3.11705 · https://doi.org/10.1002/ece3.11705 · 2024 | Strong host-fitness-cost edge; density effects context dependent. |
| copper stress (CHEBI:49415 candidate) | promotes | colonization of amoebae by parasitic symbionts | “parasitic symbionts exhibited enhanced colonization of amoebae” under copper stress (shi2024copperstressshapes pages 1-2) | Shi et al. 2024. DOI:10.1093/ismejo/wrae100 · https://doi.org/10.1093/ismejo/wrae100 · 2024 | Environmental modifier; amoeba-bacteria system. |
| copper stress (CHEBI:49415 candidate) | exacerbates | pathogenic effects on host | “the pathogenic effects of parasitic symbionts on hosts were exacerbated under copper stress” (shi2024copperstressshapes pages 1-2) | Shi et al. 2024. DOI:10.1093/ismejo/wrae100 · https://doi.org/10.1093/ismejo/wrae100 · 2024 | Strong environmental context edge for host fitness cost. |
| parasitism | causes | host fitness reduction | “parasitism is a long-lasting relationship between individuals of different species harming the hosts” (rozsa2023definitionsofparasitism pages 1-2) | Rózsa & Garay 2023. DOI:10.1017/S0031182023000598 · https://doi.org/10.1017/S0031182023000598 · 2023 | Foundational definition edge; very suitable for top-level trait graph. |
| parasite nutrient use of host | causes | host harm | “Almost all authors agree that parasites harm their hosts by utilizing them as nutrient resources” (rozsa2023definitionsofparasitism pages 1-2) | Rózsa & Garay 2023. DOI:10.1017/S0031182023000598 · https://doi.org/10.1017/S0031182023000598 · 2023 | High-level definitional mechanism linking exploitation to harm. |


*Table: This table lists candidate subject-predicate-object edges for curating microbial parasitism into a TraitMech causal graph. It emphasizes evidence-backed mechanisms spanning colonization, secretion/effectors, nutrient acquisition, immune modulation, microbiota interactions, transmission mode, symbiont density, and copper stress.*

## 5. Applications and real-world implementations (evidence-backed)

### 5.1 Host-directed therapy / immunomodulatory targeting
- **Blocking host VPAC2 signaling as adjunct therapy for bacterial persistence/pathology.** The Bordetella study suggests VPAC2 antagonists as a therapeutic strategy: treatment “decrease[s] lung pathology,” and the pathway is linked to T3SS-mediated manipulation (first2023bordetellaspp.utilize pages 1-2). This exemplifies a host-directed intervention strategy grounded in a causal chain from secretion system → host signaling axis → colonization and disease.

### 5.2 Biocontrol and symbiont engineering (parasitism–mutualism management)
- In arthropods, deliberate symbiont transinfection programs illustrate applied management of symbiont effects. Hoffmann & Cooper discuss “deliberate artificial transinfections… such as Wolbachia in Aedes mosquitoes for biocontrol of arboviruses” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2). While these interventions aim at public health benefit, the same source emphasizes that “newly acquired facultative endosymbionts are often seen as parasites” and that density/tissue distribution can drive host costs (hoffmann2024describingendosymbiont–hostinteractions pages 1-2), underscoring safety/efficacy requirements.

### 5.3 Nutritional immunity as an anti-parasitism design principle
- The Barber & Fitzgerald review frames metal sequestration as a host defense (“nutritional immunity”), and documents pathogen counter-adaptations such as TbpA and TdfH receptors (barber2024mechanismsofhost pages 5-6). For curation, this supports actionable edges where disrupting metal acquisition modules is a plausible anti-parasitism strategy.

## 6. Expert synthesis and analysis (curation guidance)

### 6.1 Recommended “core” curatable mechanisms (high generality)
The most generalizable, cross-system causal backbone supported in recent sources is:
1. **Adhesion/colonization modules** (adhesins; receptor-binding) enabling establishment (barber2024mechanismsofhost pages 3-5).
2. **Host resource exploitation** (metals, hemoglobin/heme; nutrient acquisition) as a proximate cause of fitness costs (barber2024mechanismsofhost pages 5-6, reyeslopez2023hemoglobinuptakeand pages 1-2, rozsa2023definitionsofparasitism pages 1-2).
3. **Host defense interaction modules** (immune evasion/manipulation, including ubiquitin-pathway manipulation) enabling persistence (wehrmann2023theemergingrole pages 1-2, krishnamurthy2023crisprscreensidentify pages 1-2).
4. **Environmental modifiers** shifting interaction outcomes along the parasitism–mutualism continuum (copper stress, symbiont density) (shi2024copperstressshapes pages 1-2, hoffmann2024describingendosymbiont–hostinteractions pages 1-2).

### 6.2 Statistics and recent data points from the included sources
- Pertussis is described as causing “over 160,000 childhood deaths in 2014,” with “30% being in neonates” (first2023bordetellaspp.utilize pages 1-2).
- Protozoan diseases: amoebiasis/leishmaniasis/Chagas/sleeping sickness “affect several million people worldwide, leading to millions of deaths annually” (reyeslopez2023hemoglobinuptakeand pages 1-2).
- Amoebiasis burden details: “Five hundred million people worldwide are infected with amoebiasis… 50 million people are infected with E. histolytica, leading to 40,000–100,000 deaths each year” (reyeslopez2023hemoglobinuptakeand pages 1-2).
- Toxoplasma virulence in mice: type I strain “lethal dose (LD100) <10” (krishnamurthy2023crisprscreensidentify pages 1-2).

(These values are suitable as contextual metadata for trait importance, not as mechanistic edge evidence.)

## 7. Warnings and “do not curate yet” items

1. **Avoid overgeneralizing taxon-specific nodes as universal parasitism mechanisms.** Examples such as Bordetella VIP/VPAC2 manipulation (first2023bordetellaspp.utilize pages 1-2), Legionella Lot DUBs (wehrmann2023theemergingrole pages 1-2), and Toxoplasma GRA32-related complexes (krishnamurthy2023crisprscreensidentify pages 1-2) are highly mechanistic but may be best curated as **child edges** under broader parent nodes (e.g., “secretion system effector delivery,” “pathogen DUB activity,” “parasitophorous vacuole maintenance”).

2. **Explicitly encode the organizational level for ‘host fitness’ where possible.** Rózsa & Garay emphasize that effects can differ across cell/individual/lineage/population levels (rozsa2023definitionsofparasitism pages 1-2). Without level annotation, graph assertions may become internally inconsistent.

3. **Treat mutualism-shift drivers as boundary conditions, not as parasitism mechanisms.** “Vertical transmission favors coevolution toward mutualism” (hoffmann2024describingendosymbiont–hostinteractions pages 1-2) and should typically appear as a **modifier/constraint** edge rather than a direct parasitism-enabling mechanism.

4. **Environmental context edges require careful grounding.** Copper stress effects are directly shown in an amoeba–bacteria system (shi2024copperstressshapes pages 1-2). Curate with ENVO/CHEBI grounding and mark as *context-dependent* unless additional taxa confirm generality.

---

# DOI-first bibliography (2023–2024 prioritized)

1. Rózsa L, Garay J. **Definitions of parasitism, considering its potentially opposing effects at different levels of hierarchical organization.** *Parasitology.* Published online 3 Jul 2023. DOI: **10.1017/S0031182023000598**. https://doi.org/10.1017/S0031182023000598 (rozsa2023definitionsofparasitism pages 1-2)

2. Hoffmann AA, Cooper BS. **Describing endosymbiont–host interactions within the parasitism–mutualism continuum.** *Ecology and Evolution.* Accepted 21 Jun 2024 (published 2024). DOI: **10.1002/ece3.11705**. https://doi.org/10.1002/ece3.11705 (hoffmann2024describingendosymbiont–hostinteractions pages 1-2)

3. Barber MF, Fitzgerald JR. **Mechanisms of host adaptation by bacterial pathogens.** *FEMS Microbiology Reviews.* Jul 2024. DOI: **10.1093/femsre/fuae019**. https://doi.org/10.1093/femsre/fuae019 (barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 5-6)

4. First NJ, Pedreira-Lopez J, San-Silvestre MRF, et al. **Bordetella spp. utilize the type 3 secretion system to manipulate the VIP/VPAC2 signaling and promote colonization and persistence…** *Frontiers in Cellular and Infection Microbiology.* 29 Mar 2023. DOI: **10.3389/fcimb.2023.1111502**. https://doi.org/10.3389/fcimb.2023.1111502 (first2023bordetellaspp.utilize pages 1-2)

5. Reyes-López M, Aguirre-Armenta B, Piña-Vázquez C, de la Garza M, Serrano-Luna J. **Hemoglobin uptake and utilization by human protozoan parasites: a review.** *Frontiers in Cellular and Infection Microbiology.* 9 Jun 2023. DOI: **10.3389/fcimb.2023.1150054**. https://doi.org/10.3389/fcimb.2023.1150054 (reyeslopez2023hemoglobinuptakeand pages 1-2)

6. Wehrmann M, Vilchez D. **The emerging role and therapeutic implications of bacterial and parasitic deubiquitinating enzymes.** *Frontiers in Immunology.* 22 Nov 2023. DOI: **10.3389/fimmu.2023.1303072**. https://doi.org/10.3389/fimmu.2023.1303072 (wehrmann2023theemergingrole pages 1-2)

7. Krishnamurthy S, Maru P, Wang Y, et al. **CRISPR Screens Identify Toxoplasma Genes That Determine Parasite Fitness in Interferon Gamma-Stimulated Human Cells.** *mBio.* 14 Mar 2023. DOI: **10.1128/mbio.00060-23**. https://doi.org/10.1128/mbio.00060-23 (krishnamurthy2023crisprscreensidentify pages 1-2)

8. Grondin JA, Jamal A, Mowna S, Seto T, Khan WI. **Interaction between Intestinal Parasites and the Gut Microbiota: Implications for the Intestinal Immune Response and Host Defence.** *Pathogens.* Jul 2024. DOI: **10.3390/pathogens13080608**. https://doi.org/10.3390/pathogens13080608 (grondin2024interactionbetweenintestinal pages 2-3)

9. Shi Y, Ma L, Zhou M, et al. **Copper stress shapes the dynamic behavior of amoebae and their associated bacteria.** *The ISME Journal.* Advance access 7 Jun 2024. DOI: **10.1093/ismejo/wrae100**. https://doi.org/10.1093/ismejo/wrae100 (shi2024copperstressshapes pages 1-2)

10. Kotsaridis K, Tsakiri D, Sarris PF. **Understanding enemy’s weapons to an effective prevention: common virulence effects across microbial phytopathogens kingdoms.** *Critical Reviews in Microbiology.* Jun 2023. DOI: **10.1080/1040841x.2022.2083939**. https://doi.org/10.1080/1040841x.2022.2083939 (kotsaridis2023understandingenemy’sweapons pages 1-3)

11. Price CTD, Hanford HE, Al‑Quadan T, et al. **Amoebae as training grounds for microbial pathogens.** *mBio.* Aug 2024. DOI: **10.1128/mbio.00827-24**. https://doi.org/10.1128/mbio.00827-24 (price2024amoebaeastraining pages 1-2)


References

1. (rozsa2023definitionsofparasitism pages 1-2): Lajos Rózsa and József Garay. Definitions of parasitism, considering its potentially opposing effects at different levels of hierarchical organization. Parasitology, 150:761-768, Jul 2023. URL: https://doi.org/10.1017/s0031182023000598, doi:10.1017/s0031182023000598. This article has 39 citations and is from a peer-reviewed journal.

2. (hoffmann2024describingendosymbiont–hostinteractions pages 1-2): Ary A. Hoffmann and Brandon S. Cooper. Describing endosymbiont–host interactions within the parasitism–mutualism continuum. Ecology and Evolution, Jul 2024. URL: https://doi.org/10.1002/ece3.11705, doi:10.1002/ece3.11705. This article has 27 citations and is from a peer-reviewed journal.

3. (rozsa2023definitionsofparasitism pages 2-3): Lajos Rózsa and József Garay. Definitions of parasitism, considering its potentially opposing effects at different levels of hierarchical organization. Parasitology, 150:761-768, Jul 2023. URL: https://doi.org/10.1017/s0031182023000598, doi:10.1017/s0031182023000598. This article has 39 citations and is from a peer-reviewed journal.

4. (barber2024mechanismsofhost pages 3-5): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

5. (barber2024mechanismsofhost pages 5-6): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 46 citations and is from a domain leading peer-reviewed journal.

6. (reyeslopez2023hemoglobinuptakeand pages 1-2): Magda Reyes-López, Beatriz Aguirre-Armenta, Carolina Piña-Vázquez, Mireya de la Garza, and Jesús Serrano-Luna. Hemoglobin uptake and utilization by human protozoan parasites: a review. Frontiers in Cellular and Infection Microbiology, Jun 2023. URL: https://doi.org/10.3389/fcimb.2023.1150054, doi:10.3389/fcimb.2023.1150054. This article has 19 citations.

7. (wehrmann2023theemergingrole pages 1-2): Markus Wehrmann and David Vilchez. The emerging role and therapeutic implications of bacterial and parasitic deubiquitinating enzymes. Frontiers in Immunology, Nov 2023. URL: https://doi.org/10.3389/fimmu.2023.1303072, doi:10.3389/fimmu.2023.1303072. This article has 9 citations and is from a peer-reviewed journal.

8. (krishnamurthy2023crisprscreensidentify pages 1-2): Shruthi Krishnamurthy, Parag Maru, Yifan Wang, Mebratu A. Bitew, Debanjan Mukhopadhyay, Yoshiki Yamaryo-Botté, Tatiana C. Paredes-Santos, Lamba O. Sangaré, Christopher Swale, Cyrille Y. Botté, and Jeroen P. J. Saeij. Crispr screens identify <i>toxoplasma</i> genes that determine parasite fitness in interferon gamma-stimulated human cells. mBio, Apr 2023. URL: https://doi.org/10.1128/mbio.00060-23, doi:10.1128/mbio.00060-23. This article has 30 citations and is from a domain leading peer-reviewed journal.

9. (first2023bordetellaspp.utilize pages 1-2): Nicholas J. First, Jose Pedreira-Lopez, Manuel R. F. San-Silvestre, Katelyn M. Parrish, Xiao-Hong Lu, and Monica C. Gestal. Bordetella spp. utilize the type 3 secretion system to manipulate the vip/vpac2 signaling and promote colonization and persistence of the three classical bordetella in the lower respiratory tract. Frontiers in Cellular and Infection Microbiology, Mar 2023. URL: https://doi.org/10.3389/fcimb.2023.1111502, doi:10.3389/fcimb.2023.1111502. This article has 9 citations.

10. (grondin2024interactionbetweenintestinal pages 2-3): Jensine A. Grondin, Asif Jamal, Sadrina Mowna, Tyler Seto, and Waliul I. Khan. Interaction between intestinal parasites and the gut microbiota: implications for the intestinal immune response and host defence. Pathogens, 13:608, Jul 2024. URL: https://doi.org/10.3390/pathogens13080608, doi:10.3390/pathogens13080608. This article has 50 citations.

11. (shi2024copperstressshapes pages 1-2): Yijing Shi, Lu Ma, Min Zhou, Zhili He, Yuanchen Zhao, Junyue Hong, Xinyue Zou, Lin Zhang, and Longfei Shu. Copper stress shapes the dynamic behavior of amoebae and their associated bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae100, doi:10.1093/ismejo/wrae100. This article has 12 citations.

12. (kotsaridis2023understandingenemy’sweapons pages 1-3): Konstantinos Kotsaridis, Dimitra Tsakiri, and Panagiotis F. Sarris. Understanding enemy’s weapons to an effective prevention: common virulence effects across microbial phytopathogens kingdoms. Critical Reviews in Microbiology, 49:528-542, Jun 2023. URL: https://doi.org/10.1080/1040841x.2022.2083939, doi:10.1080/1040841x.2022.2083939. This article has 10 citations and is from a peer-reviewed journal.

13. (price2024amoebaeastraining pages 1-2): Christopher T. D. Price, Hannah E. Hanford, Tasneem Al-Quadan, Marina Santic, Cheon J. Shin, Manal S. J. Da'as, and Yousef Abu Kwaik. Amoebae as training grounds for microbial pathogens. Aug 2024. URL: https://doi.org/10.1128/mbio.00827-24, doi:10.1128/mbio.00827-24. This article has 46 citations and is from a domain leading peer-reviewed journal.