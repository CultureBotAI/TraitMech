---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:21:55.284106'
end_time: '2026-08-03T23:30:42.121807'
duration_seconds: 526.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: host-associated
  trait_identifier: traitmech:000049
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: host_associated
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A habitat association in which an organism lives persistently on or
    in a plant or animal host (e.g. as a member of a host microbiome), spanning commensal,
    mutualistic, and pathogenic relationships.
  parent_traits: traitmech:000047
  synonyms: ''
  evidence_summary: "DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document the\
    \ ubiquity of host-associated microbial communities across the animal kingdom.)\
    \ | DOI:10.1126/science.1104816:  (B\xE4ckhed et al. characterize the host-associated\
    \ gut microbiota as a dense, coevolved community.)"
  causal_graph_summary: 'host_associated_microbiome: 11 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** host-associated
- **METPO identifier:** traitmech:000049
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives persistently on or in a plant or animal host (e.g. as a member of a host microbiome), spanning commensal, mutualistic, and pathogenic relationships.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document the ubiquity of host-associated microbial communities across the animal kingdom.) | DOI:10.1126/science.1104816:  (Bäckhed et al. characterize the host-associated gut microbiota as a dense, coevolved community.)
- **Existing causal graph summary:** host_associated_microbiome: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **host-associated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/host_associated.yaml`.

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
- **Trait label:** host-associated
- **METPO identifier:** traitmech:000049
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives persistently on or in a plant or animal host (e.g. as a member of a host microbiome), spanning commensal, mutualistic, and pathogenic relationships.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document the ubiquity of host-associated microbial communities across the animal kingdom.) | DOI:10.1126/science.1104816:  (Bäckhed et al. characterize the host-associated gut microbiota as a dense, coevolved community.)
- **Existing causal graph summary:** host_associated_microbiome: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **host-associated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/host_associated.yaml`.

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


# TraitMech curation report: **host-associated**

## Executive scope

**Target:** `traitmech:000049` — host-associated; ecology class; reviewed mapping.

The defensible operational phenotype is **persistent residence on or in a living plant or animal host**, including epithelial surfaces, mucus, gut lumen, rhizoplane, and internal host tissues. The interaction outcome is orthogonal: pathogenic, commensal, and mutualistic organisms can all be host-associated. Wiesmann and colleagues state that “regardless of the outcome of symbiosis… bacteria must first colonize their hosts” and identify host sensing, nutrient acquisition, competition, immune tolerance, and physiological remodeling as shared requirements (published 15 December 2022 online; 2023 issue). (wiesmann2023originsofsymbiosis pages 1-2)

The causal graph should therefore terminate in **persistent host colonization/host-associated lifestyle**, not in host benefit, disease, or virulence. Those are possible downstream outcomes. Modern expert synthesis further emphasizes that host association is bidirectional: host immunity, barriers, physiological homeostasis, and transit actively select microbial residents, making the microbiome an “ecosystem on a leash” rather than a community controlled only by microbial genes or diet. (wilde2024hostcontrolof pages 1-5)

### Boundary cases

Include:

- Stable gut, skin, oral, respiratory, reproductive, leaf, root-surface, nodule, or endophytic residence.
- Commensals, mutualists, pathobionts, and persistent pathogens.
- Rhizosphere organisms only when persistence in the root-influenced compartment is demonstrated; the current plant literature explicitly uses “rhizosphere colonization” for stable communities in rhizosphere soil, rhizoplane, or root endosphere. (liu2024rootcolonizationby pages 1-2)

Exclude or qualify:

- Transient contamination, brief passage through a gut, or detection based only on environmental DNA.
- Mere proximity to a host without evidence of persistence.
- Adhesion in vitro as a synonym for the complete trait; adhesion is one possible enabling mechanism.
- “Intracellular,” “pathogenic,” “mutualistic,” “commensal,” and “host-specific” as equivalents. Each is a narrower or independent trait.
- Genes associated with one host species as universal determinants of host association.

## Current mechanistic model

A useful graph architecture is:

**host-derived signals and environmental conditions → sensing/chemotaxis and physiological response → host approach → surface attachment → access to host nutrients + resistance to host defenses + competition with resident microbes → biofilm or niche persistence → persistent host association.**

This is not a single obligatory pathway. Nonmotile vertically transmitted symbionts, intracellular specialists, and organisms lacking classical biofilms can reach the same ecological phenotype through different mechanisms. Thus, most nodes below should be modeled as context-dependent contributors rather than necessary-and-sufficient universal causes.

## Candidate nodes grouped by type

### Trait and ecological-state nodes

- **host-associated** — `traitmech:000049`
- persistent host colonization — label-only candidate
- long-term host association — label-only candidate
- host-surface colonization — label-only candidate
- rhizosphere colonization — label-only; scope includes rhizosphere soil, rhizoplane, and endosphere in the cited review (liu2024rootcolonizationby pages 1-2)
- intestinal colonization — label-only candidate
- microbial competition within host niche — label-only candidate
- colonization resistance — label-only candidate

### Host environments and experimental factors

- animal host; plant host — broad label-only classes
- intestinal mucus / mucin — label-only unless a specific mucin is used
- intestinal epithelium; plant root; rhizoplane; root endosphere — label-only candidates
- rhizosphere — `ENVO:00005801`
- root exudates — label-only mixture; do not represent as one chemical
- host innate immune response — `GO:0045087`
- host antimicrobial peptide exposure — label-only environmental factor
- reactive oxygen species exposure — label-only; individual ROS can receive CHEBI identifiers
- reactive nitrogen species / nitric oxide exposure — nitric oxide `CHEBI:16480`
- oxygen availability — oxygen `CHEBI:15379`
- host transit or expulsion — label-only process
- in-vivo host colonization assay; adhesion assay; TnSeq fitness assay; RNA-seq response assay — experimental-factor nodes

### Biological processes and modules

- chemotaxis — `GO:0006935`
- bacterial-type flagellum-dependent motility — `GO:0071973`
- cell adhesion — `GO:0007155`
- biofilm formation — `GO:0042710`
- carbohydrate catabolic process — `GO:0016052`
- iron acquisition / siderophore-mediated iron uptake — label or a more specific GO term after organism-level review
- purine biosynthetic process — `GO:0006164`
- tryptophan biosynthetic process — `GO:0000162`
- nitric-oxide detoxification — `GO:0071732`
- response to oxidative stress — `GO:0006979`
- response to antibiotic — `GO:0046677`
- interspecies competition / competitor killing — label-only candidate
- immune evasion or suppression — label-only unless a suitable ontology term is selected during implementation

### Genes, proteins, and complexes

- chemoreceptors / methyl-accepting chemotaxis proteins — family-level labels
- flagellar apparatus — label-only complex
- adhesins; pili/fimbriae; mucus-binding surface proteins — family-level labels
- extracellular polymeric-substance machinery — label-only module
- type VI secretion system (T6SS) — label-only complex; organism-specific component genes should be curated only in taxon-specific subgraphs
- siderophore biosynthesis and uptake systems — label-only module
- pyoverdine system — taxon-specific to pseudomonads
- lipopolysaccharide O-antigen biosynthesis machinery — label-only module
- lipid A modification systems, including `arn`-dependent aminoarabinose modification — taxon-specific module
- `nan-9` nine-gene cluster — label-only, *E. coli*-specific
- core *E. coli* sialoregulon `nanRATEK-yhcH`, `nanXY`, `nanCMS` — label-only
- MexE RND-type efflux pump — taxon/strain-specific
- cytochrome bd oxidase — label-only complex pending organism-specific grounding
- bacterioferritin — protein-family label

### Chemicals and nutrients

- iron — `CHEBI:18248`
- siderophore — `CHEBI:26672`
- N-acetylneuraminic acid (Neu5Ac) — `CHEBI:17012`
- N-glycolylneuraminic acid (Neu5Gc) — `CHEBI:62084`
- amino acids, sugars, organic acids, and host glycans — use individual CHEBI terms only when a source identifies the molecule
- tryptophan — `CHEBI:27897`
- purines — `CHEBI:26386`
- lipopolysaccharide — `CHEBI:16412`
- lipid A — `CHEBI:145480`
- antimicrobial peptides — class label unless a particular peptide is tested

Identifiers above are suggested only where confidence is high; they should be checked against the ontology release used by TraitMech before committing. No CURIE should be inferred for `nan-9`, root-exudate mixtures, or multicomponent secretion systems without registry validation.

## Candidate causal edges

The table below separates broad graph candidates from taxon-specific or uncertain hypotheses.

| subject | predicate | object | context/evidence class | DOI | supporting short quote/snippet | curation status |
|---|---|---|---|---|---|---|
| host-derived chemoattractants / root exudates | stimulates | bacterial chemotaxis | General, review-derived across plant and animal hosts | 10.1093/femsre/fuac048 | “Hosts exude a large number of chemoattractants… Bacteria use chemoreceptors to sense these molecules and move towards the host.” (wiesmann2023originsofsymbiosis pages 1-2) | Candidate, broad but review-derived |
| chemotaxis and motility | enables | movement toward host / rhizosphere approach | Plant-focused, review-derived | 10.1093/femsre/fuad066 | “Chemotaxis and motility determine the moving toward rhizosphere, the initial site selection” (liu2024rootcolonizationby pages 1-2) | Candidate, broad plant-host edge |
| adhesins | mediates | attachment to intestinal mucus or epithelial cells | Mammal-gut, review-derived | 10.3390/microorganisms12051026 | “This process primarily relies on adhesins.” / “attachment of bacteria to intestinal mucus or epithelial cells” (lin2024areviewof pages 19-20) | Candidate, broad animal-host edge |
| attachment to host surface | prerequisite_for | long-term colonization | Mammal-gut, review-derived | 10.3390/microorganisms12051026 | “The binding of bacterial adhesins to host receptors is a prerequisite for the long-term colonization of bacteria” (lin2024areviewof pages 19-20) | Candidate, review-derived |
| root exudates | supports | bacterial growth using host carbon resources | Plant-root, review-derived | 10.1093/femsre/fuad066 | “Bacterial growth using root exudates as the carbon resources… is necessary for biofilm formation” (liu2024rootcolonizationby pages 1-2) | Candidate, broad plant-host edge |
| root exudates | promotes | rhizoplane biofilm formation | Plant-root, review-derived | 10.1093/femsre/fuad066 | “Bacterial growth using root exudates as the carbon resources… is necessary for biofilm formation” (liu2024rootcolonizationby pages 1-2) | Candidate, review-derived |
| biofilm formation | protects_against | host-derived stressors / antimicrobial peptides | General, review-derived across hosts | 10.1093/femsre/fuac048 | “Biofilm formation on a plant root or in the gut allows for chronic association… and provides protection against many stressors including host-secreted antimicrobial peptides” (wiesmann2023originsofsymbiosis pages 1-2) | Candidate, broad but review-derived |
| siderophore production | enables | iron acquisition in host environment | General, review-derived | 10.1093/femsre/fuac048 | “the siderophore pyoverdine is essential for virulence and both sequesters iron in a host environment” (wiesmann2023originsofsymbiosis pages 3-4) | Candidate, strong mechanism but taxon exemplified |
| robust iron acquisition | promotes | establishment of host association | Generalized from multiple taxa, review-derived | 10.1093/femsre/fuac048 | “a robust ability to compete for iron is essential to establishing host association across host environments” (wiesmann2023originsofsymbiosis pages 3-4) | Candidate, broad but review-derived |
| type VI secretion system (T6SS) | causes | killing / suppression of microbial competitors | General with insect/plant examples, review-derived | 10.1093/femsre/fuac048 | “T6SS allow bacteria to deliver effectors and toxins directly into the cytoplasm of potential competitors” (wiesmann2023originsofsymbiosis pages 3-4) | Candidate, broad but review-derived |
| competitor suppression | promotes | persistence / colonization in crowded host niches | General with insect/plant examples, review-derived | 10.1093/femsre/fuac048 | “uses its T6SS to kill members of the microbiome and colonize the insect gut” (wiesmann2023originsofsymbiosis pages 3-4) | Candidate, inferred generalization from exemplars |
| O-antigen on LPS | promotes | immune evasion / host immune avoidance | Generalized across plant and animal associations, review-derived | 10.1093/femsre/fuac048 | “The presence of the O-antigen… is most commonly demonstrated to help bacteria… evade host immunity and establish commensalism or infection” (wiesmann2023originsofsymbiosis pages 4-5) | Candidate, broad but review-derived |
| lipid A modification (e.g., aminoarabinose / phosphoethanolamine) | increases | resistance to cationic antimicrobial peptides | General with Salmonella/Pseudomonas examples, review-derived | 10.1093/femsre/fuac048 | “modification… with aminoarabinose (arn) increases bacterial resistance to the antimicrobial cationic peptide polymyxin B” (wiesmann2023originsofsymbiosis pages 4-5) | Candidate, taxon-exemplified |
| nan-9 gene cluster | contributes_to | sialic acid catabolism (Neu5Ac / Neu5Gc use) | E. coli, associative + knockout-supported | 10.1186/s12915-023-01562-w | “Knock-out in vitro studies indicated that this novel nan-9 gene cluster contributes to catabolism of the sialic acids Neu5Ac and Neu5Gc” (tiwari2023genomewideassociationreveals pages 7-9, tiwari2023genomewideassociationreveals pages 1-2) | Candidate, species-specific |
| sialic acid catabolism / nan-9 | may_contribute_to | human-host adaptation in E. coli | E. coli, associative/uncertain | 10.1186/s12915-023-01562-w | “we hypothesize that the human-associated nan-9 gene cluster is one of the factors driving the adaptation of ExPEC to the human intestine” (tiwari2023genomewideassociationreveals pages 7-9) | Uncertain; do not overgeneralize |
| purine biosynthesis and tryptophan metabolism | required_for | in vivo host colonization fitness | Cross-host TnSeq synthesis, review-derived from experimental studies | 10.1128/mbio.00390-24 | “purine biosynthesis and tryptophan metabolism pathways are critical for bacterial colonization fitness across diverse host-pathogen and mutualistic interactions” (torres2024sheddinglighton pages 11-13) | Candidate, broad but synthesis-based |
| host immunity / barrier function / transit | shapes | microbiome selection and host-associated persistence | General host-control framework, high-authority review | 10.1126/science.adi3338 | “Hosts exert control over their symbionts via diverse mechanisms, including immunity, barrier function, physiological homeostasis and transit” (wilde2024hostcontrolof pages 1-5) | Candidate environmental-control edge |
| host oxygen availability / inflammatory oxygen release | selects_for | host-associated colonizers able to exploit oxygen | Gut pathogens, review-derived mechanistic example | 10.1038/s41579-022-00833-7 | “releases oxygen for pathogen respiration while killing oxygen-sensitive symbionts” (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30) | Uncertain, gut-pathogen-specific; not universal |


*Table: This compact curation table lists candidate subject-predicate-object edges for the microbial trait host-associated, with DOI-linked supporting snippets and evidence-strength labels. It is useful for deciding which mechanisms are broad enough to curate versus which remain taxon-specific, associative, or uncertain.*

### Recommended minimal backbone

For a compact first revision of `host_associated.yaml`, the strongest broadly reusable chain is:

1. **host-derived chemoattractant → stimulates → chemotaxis**;
2. **chemotaxis/motility → enables → host approach**;
3. **adhesin → mediates → attachment to host surface**;
4. **attachment → promotes → colonization**;
5. **host-derived nutrient → supports → microbial growth in host niche**;
6. **siderophore-mediated iron acquisition → promotes → host-niche fitness**;
7. **competitor-suppression mechanism → increases → host-niche persistence**;
8. **envelope modification → increases → resistance to host immunity/antimicrobial peptides**;
9. **biofilm formation → increases → stress tolerance and chronic persistence**;
10. **persistent colonization → realizes → host-associated trait**.

The literature directly supports the overall sequence but not universal necessity. For example, host chemoattractants can be nutrients and signals; bacteria sense them and move toward a host, whereas biofilm formation protects established populations from antimicrobial peptides and other stresses. (wiesmann2023originsofsymbiosis pages 1-2, wiesmann2023originsofsymbiosis pages 4-5)

## Recent developments and quantitative evidence

### 1. Genome-wide fitness mapping

TnSeq now links disruptions to competitive fitness in host-relevant conditions by comparing mutant abundance before and after selection. Saturated libraries commonly contain approximately **50,000–200,000 mutants**. However, in-vivo host studies remain a small fraction of TnSeq work and are biased toward cultivable, genetically tractable Pseudomonadota and pathogenic models. This limits claims of universality. (torres2024sheddinglighton pages 3-5)

The 2024 mBio synthesis identifies purine biosynthesis and tryptophan metabolism as recurring colonization-fitness modules across animal and plant interactions and across pathogenic and mutualistic outcomes. Essential genes may be absent from mutant libraries, and preselection on minimal medium can erase relevant mutants; a missing TnSeq signal is therefore not evidence that a pathway is dispensable. (torres2024sheddinglighton pages 11-13)

### 2. Host-specific bacterial GWAS plus functional validation

Tiwari et al. analyzed **1,198 whole-genome-sequenced *E. coli*** isolates collected over **16 years** from humans, pigs, cattle, chickens, and wild boar in Germany, Spain, the United Kingdom, and Vietnam. The collection contained 327 human, 337 chicken, 265 cattle, 240 pig, and 29 wild-boar isolates; its pan-genome comprised **77,130 genes**, including 1,956 genes present in at least 99% of isolates. (tiwari2023genomewideassociationreveals pages 1-2)

A nine-gene `nan-9` cluster was associated with human isolates and occurred in 7% of the study collection and 12% of 17,994 screened RefSeq genomes; prevalence reached 83% in ST131 and 82% in ST73. Deleting `nan-9` delayed growth on Neu5Ac by about **3 hours** while producing similar final OD600 values (1.34 mutant versus 1.37 parent). On Neu5Gc, the mutant grew more slowly and reached OD600 1.31 versus 1.43 for the parent. The core `nanRATEK` mutant could not grow on Neu5Ac, showing that `nan-9` contributes to, but cannot replace, core sialic-acid catabolism. (tiwari2023genomewideassociationreveals pages 5-7)

This supports **`nan-9 → contributes to → sialic-acid catabolism`**. It does not establish **`nan-9 → causes → human colonization`** because host association came from GWAS and colonization was not tested by an in-vivo knockout experiment. The authors accordingly use “may promote” and hypothesize that the cluster contributes to human-intestinal adaptation. (tiwari2023genomewideassociationreveals pages 7-9)

### 3. Plant colonization and host-exudate response

The 2024 rhizobacteria review reports that plants release approximately **11–40% of photosynthetic products** into the rhizosphere as root exudates and that bacterial colonization is spatially heterogeneous, covering approximately **10–40% of root surface**. The proposed sequence is chemotaxis/motility, attachment, growth on exudates, competition for scarce elements, and biofilm formation. (liu2024rootcolonizationby pages 1-2)

In *Pseudomonas donghuensis* P482, tomato exudates induced nitric-oxide detoxification, iron-sulfur-cluster repair, cytochrome-bd respiration, and amino/fatty-acid catabolism; maize exudates induced MexE efflux and copper tolerance. Motility genes were induced by maize but repressed by tomato. These are experimentally observed transcriptional responses, but expression changes alone do not demonstrate that each pathway causes persistence. (krzyzanowska2023hostadaptivetraitsin pages 1-2)

Levy et al. compared **3,837 bacterial genomes**, including **484 newly sequenced root isolates**, and found that plant-associated genomes encoded more carbohydrate-metabolism functions and fewer mobile elements than related non-plant-associated genomes. They also identified 64 plant-associated protein domains potentially mimicking plant domains and experimentally validated candidate genes involved in colonization or microbe–microbe competition. These are strong leads for plant-specific subgraphs, not universal host-association nodes. (levy2018genomicfeaturesof pages 1-2)

### 4. Host control as a causal layer

A major 2024 conceptual advance is treating immunity, barrier function, physiological homeostasis, and transit as active ecological filters. Host control can promote beneficial residents (“partner choice”) or alter symbiont behavior/metabolism (“partner manipulation”). Accordingly, the graph should include environmental edges from the host to colonization fitness, rather than depicting host association solely as a microbial autonomous program. (wilde2024hostcontrolof pages 1-5)

## Applications and real-world implementation

- **Bioinoculants and biofertilizers:** efficient root colonization is a prerequisite for beneficial rhizobacteria to deliver growth promotion, stress tolerance, pathogen antagonism, or induced resistance. Colonization-aware formulation can select for chemotaxis, exudate utilization, attachment, and biofilm performance under realistic soil conditions. (liu2024rootcolonizationby pages 1-2)
- **Microbiome engineering:** comparative plant genomics has generated candidate colonization and competition genes that can guide community design for sustainable agriculture. (levy2018genomicfeaturesof pages 1-2)
- **Infection control:** adhesion, nutrient competition, siderophore systems, T6SS-mediated competitor killing, and inflammatory electron-acceptor generation provide intervention points for preventing pathogen establishment. (wiesmann2023originsofsymbiosis pages 3-4, caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30)
- **AMR surveillance and source-risk analysis:** host-associated genomic determinants can improve predictions about whether transmitted *E. coli* lineages will persist in a new host. Tiwari et al. explicitly connect these data to epidemiological monitoring and control of antimicrobial-resistant commensal and zoonotic strains. (tiwari2023genomewideassociationreveals pages 7-9, tiwari2023genomewideassociationreveals pages 1-2)
- **Therapeutic microbiome modulation:** authoritative analysis proposes leveraging evolved host-control mechanisms to reshape microbiotas, though most such approaches remain mechanism- and disease-specific rather than validated universal interventions. (wilde2024hostcontrolof pages 1-5)
- **Experimental prioritization:** pooled TnSeq can screen tens of thousands of mutants in vivo; combining it with RNA-seq and metabolomics is recommended because expression and fitness do not necessarily correlate. (torres2024sheddinglighton pages 3-5)

## Expert interpretation

The strongest current interpretation is that host association is a **convergent ecological outcome supported by modular mechanisms**, not a single conserved molecular pathway. The modules recur across plants and animals—sensing, nutrient use, competition, immune tolerance, and persistence—but their molecular realizations differ markedly. Wiesmann et al. argue that becoming symbiotic may be the initial evolutionary innovation that subsequently predisposes lineages to mutualism or pathogenicity. (wiesmann2023originsofsymbiosis pages 1-2)

At the same time, host control produces reciprocal selection. Host barriers and immunity constrain overgrowth, while microbes evolve adhesion, motility, metabolic specialization, or immune evasion. Consequently, a TraitMech graph should contain both **microbe → colonization** and **host environment → microbial fitness** edges. (wilde2024hostcontrolof pages 1-5)

## Warnings: claims not yet suitable for unqualified curation

1. **Do not curate `nan-9 causes human host association`.** Curate its effect on sialic-acid catabolism; represent the host-adaptation edge as uncertain and *E. coli*-specific. (tiwari2023genomewideassociationreveals pages 5-7, tiwari2023genomewideassociationreveals pages 7-9)
2. **Do not treat every transcriptomic induction as causal.** Tomato/maize exudate responses identify candidate adaptations, but require targeted mutants and in-vivo competition assays. (krzyzanowska2023hostadaptivetraitsin pages 1-2)
3. **Do not make T6SS, flagella, adhesins, siderophores, or biofilms universally necessary.** Each has strong exemplars, but vertically transmitted, nonmotile, intracellular, or metabolically dependent symbionts can use alternatives.
4. **Do not collapse host association into virulence.** O-antigen, lipid-A remodeling, secretion systems, and siderophores occur in pathogenic, commensal, and mutualistic contexts. (wiesmann2023originsofsymbiosis pages 1-2, wiesmann2023originsofsymbiosis pages 4-5, wiesmann2023originsofsymbiosis pages 3-4)
5. **Do not curate rhizosphere detection alone as persistent plant association.** Require longitudinal recovery, root attachment/endosphere localization, enrichment relative to bulk soil, or functional colonization evidence.
6. **Do not equate adhesion assays with persistent colonization.** Attachment is often necessary for mucosal colonization but is not sufficient under immune pressure, transit, competition, and nutrient limitation. (lin2024areviewof pages 19-20)
7. **Flag oxygen/inflammation edges as gut-pathogen-specific.** Inflammation-generated oxygen, nitrate, or tetrathionate can favor enteric pathogens but cannot be generalized to all host microbiomes. (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30)
8. **Account for ascertainment bias.** TnSeq disproportionately represents culturable, genetically tractable taxa; essential pathways and bottleneck effects can be missed. (torres2024sheddinglighton pages 3-5, torres2024sheddinglighton pages 11-13)
9. **Keep broad reviews distinct from primary causal evidence.** Many cross-host edges are authoritative syntheses but should ideally be supplemented with organism-specific knockout/complementation references during YAML implementation.

## DOI-first bibliography

1. **Wiesmann CL et al.** “Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals.” *FEMS Microbiology Reviews* 47 (2023); advance publication **15 December 2022**. DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048). (wiesmann2023originsofsymbiosis pages 1-2)
2. **Wilde J, Slack E, Foster KR.** “Host control of the microbiome: Mechanisms, evolution, and disease.” *Science* 385 (published **July 2024**). DOI: [10.1126/science.adi3338](https://doi.org/10.1126/science.adi3338). (wilde2024hostcontrolof pages 1-5)
3. **Torres M, Paszti S, Eberl L.** “Shedding light on bacteria–host interactions with the aid of TnSeq approaches.” *mBio* 15 (published **June 2024**). DOI: [10.1128/mbio.00390-24](https://doi.org/10.1128/mbio.00390-24). (torres2024sheddinglighton pages 3-5)
4. **Tiwari SK et al.** “Genome-wide association reveals host-specific genomic traits in *Escherichia coli*.” *BMC Biology* 21:76 (published **April 2023**). DOI: [10.1186/s12915-023-01562-w](https://doi.org/10.1186/s12915-023-01562-w). (tiwari2023genomewideassociationreveals pages 1-2)
5. **Liu Y et al.** “Root colonization by beneficial rhizobacteria.” *FEMS Microbiology Reviews* 48 (advance publication **13 December 2023**; 2024 volume). DOI: [10.1093/femsre/fuad066](https://doi.org/10.1093/femsre/fuad066). (liu2024rootcolonizationby pages 1-2)
6. **Krzyżanowska DM et al.** “Host-adaptive traits in the plant-colonizing *Pseudomonas donghuensis* P482 revealed by transcriptomic responses to exudates of tomato and maize.” *Scientific Reports* 13:9445 (published **June 2023**). DOI: [10.1038/s41598-023-36494-6](https://doi.org/10.1038/s41598-023-36494-6). (krzyzanowska2023hostadaptivetraitsin pages 1-2)
7. **Caballero-Flores G, Pickard JM, Núñez G.** “Microbiota-mediated colonization resistance: mechanisms and regulation.” *Nature Reviews Microbiology* 21:347–360 (2023; online **December 2022**). DOI: [10.1038/s41579-022-00833-7](https://doi.org/10.1038/s41579-022-00833-7). (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30)
8. **Lin Q et al.** “A Review of the Mechanisms of Bacterial Colonization of the Mammal Gut.” *Microorganisms* 12:1026 (published **May 2024**). DOI: [10.3390/microorganisms12051026](https://doi.org/10.3390/microorganisms12051026). (lin2024areviewof pages 19-20)
9. **Levy A et al.** “Genomic features of bacterial adaptation to plants.” *Nature Genetics* 50:138–150 (published **January 2018**). DOI: [10.1038/s41588-017-0012-9](https://doi.org/10.1038/s41588-017-0012-9). (levy2018genomicfeaturesof pages 1-2)
10. **McFall-Ngai M et al.** “Animals in a bacterial world, a new imperative for the life sciences.” *PNAS* 110:3229–3236 (published **February 2013**). DOI: [10.1073/pnas.1218525110](https://doi.org/10.1073/pnas.1218525110).
11. **Bäckhed F et al.** “Host-Bacterial Mutualism in the Human Intestine.” *Science* 307:1915–1920 (published **March 2005**). DOI: [10.1126/science.1104816](https://doi.org/10.1126/science.1104816).

References

1. (wiesmann2023originsofsymbiosis pages 1-2): Christina L. Wiesmann, Nicole R. Wang, Yue Zhang, Zhexian Liu, and Cara H. Haney. Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals. FEMS microbiology reviews, Dec 2023. URL: https://doi.org/10.1093/femsre/fuac048, doi:10.1093/femsre/fuac048. This article has 64 citations and is from a domain leading peer-reviewed journal.

2. (wilde2024hostcontrolof pages 1-5): Jacob Wilde, Emma Slack, and Kevin R. Foster. Host control of the microbiome: mechanisms, evolution, and disease. Science, Jul 2024. URL: https://doi.org/10.1126/science.adi3338, doi:10.1126/science.adi3338. This article has 169 citations and is from a highest quality peer-reviewed journal.

3. (liu2024rootcolonizationby pages 1-2): Yunpeng Liu, Zhihui Xu, Lin Chen, Weibing Xun, Xia Shu, Yu Chen, Xinli Sun, Zhengqi Wang, Yi Ren, Qirong Shen, and Ruifu Zhang. Root colonization by beneficial rhizobacteria. FEMS Microbiology Reviews, Dec 2024. URL: https://doi.org/10.1093/femsre/fuad066, doi:10.1093/femsre/fuad066. This article has 220 citations and is from a domain leading peer-reviewed journal.

4. (lin2024areviewof pages 19-20): Qingjie Lin, Shiying Lin, Zitao Fan, Jing Liu, Dingcheng Ye, and Pingting Guo. A review of the mechanisms of bacterial colonization of the mammal gut. Microorganisms, 12:1026, May 2024. URL: https://doi.org/10.3390/microorganisms12051026, doi:10.3390/microorganisms12051026. This article has 43 citations.

5. (wiesmann2023originsofsymbiosis pages 3-4): Christina L. Wiesmann, Nicole R. Wang, Yue Zhang, Zhexian Liu, and Cara H. Haney. Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals. FEMS microbiology reviews, Dec 2023. URL: https://doi.org/10.1093/femsre/fuac048, doi:10.1093/femsre/fuac048. This article has 64 citations and is from a domain leading peer-reviewed journal.

6. (wiesmann2023originsofsymbiosis pages 4-5): Christina L. Wiesmann, Nicole R. Wang, Yue Zhang, Zhexian Liu, and Cara H. Haney. Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals. FEMS microbiology reviews, Dec 2023. URL: https://doi.org/10.1093/femsre/fuac048, doi:10.1093/femsre/fuac048. This article has 64 citations and is from a domain leading peer-reviewed journal.

7. (tiwari2023genomewideassociationreveals pages 7-9): Sumeet K. Tiwari, Boas C. L. van der Putten, Thilo M. Fuchs, Trung N. Vinh, Martin Bootsma, Rik Oldenkamp, Roberto La Ragione, Sebastien Matamoros, Ngo T. Hoa, Christian Berens, Joy Leng, Julio Álvarez, Marta Ferrandis-Vila, Jenny M. Ritchie, Angelika Fruth, Stefan Schwarz, Lucas Domínguez, María Ugarte-Ruiz, Astrid Bethe, Charlotte Huber, Vanessa Johanns, Ivonne Stamm, Lothar H. Wieler, Christa Ewers, Amanda Fivian-Hughes, Herbert Schmidt, Christian Menge, Torsten Semmler, and Constance Schultsz. Genome-wide association reveals host-specific genomic traits in escherichia coli. BMC Biology, Apr 2023. URL: https://doi.org/10.1186/s12915-023-01562-w, doi:10.1186/s12915-023-01562-w. This article has 46 citations and is from a domain leading peer-reviewed journal.

8. (tiwari2023genomewideassociationreveals pages 1-2): Sumeet K. Tiwari, Boas C. L. van der Putten, Thilo M. Fuchs, Trung N. Vinh, Martin Bootsma, Rik Oldenkamp, Roberto La Ragione, Sebastien Matamoros, Ngo T. Hoa, Christian Berens, Joy Leng, Julio Álvarez, Marta Ferrandis-Vila, Jenny M. Ritchie, Angelika Fruth, Stefan Schwarz, Lucas Domínguez, María Ugarte-Ruiz, Astrid Bethe, Charlotte Huber, Vanessa Johanns, Ivonne Stamm, Lothar H. Wieler, Christa Ewers, Amanda Fivian-Hughes, Herbert Schmidt, Christian Menge, Torsten Semmler, and Constance Schultsz. Genome-wide association reveals host-specific genomic traits in escherichia coli. BMC Biology, Apr 2023. URL: https://doi.org/10.1186/s12915-023-01562-w, doi:10.1186/s12915-023-01562-w. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (torres2024sheddinglighton pages 11-13): Marta Torres, Sarah Paszti, and Leo Eberl. Shedding light on bacteria–host interactions with the aid of tnseq approaches. Jun 2024. URL: https://doi.org/10.1128/mbio.00390-24, doi:10.1128/mbio.00390-24. This article has 23 citations and is from a domain leading peer-reviewed journal.

10. (caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30): Gustavo Caballero-Flores, Joseph M. Pickard, and Gabriel Núñez. Microbiota-mediated colonization resistance: mechanisms and regulation. Nature Reviews Microbiology, 21:347-360, Dec 2023. URL: https://doi.org/10.1038/s41579-022-00833-7, doi:10.1038/s41579-022-00833-7. This article has 532 citations and is from a highest quality peer-reviewed journal.

11. (torres2024sheddinglighton pages 3-5): Marta Torres, Sarah Paszti, and Leo Eberl. Shedding light on bacteria–host interactions with the aid of tnseq approaches. Jun 2024. URL: https://doi.org/10.1128/mbio.00390-24, doi:10.1128/mbio.00390-24. This article has 23 citations and is from a domain leading peer-reviewed journal.

12. (tiwari2023genomewideassociationreveals pages 5-7): Sumeet K. Tiwari, Boas C. L. van der Putten, Thilo M. Fuchs, Trung N. Vinh, Martin Bootsma, Rik Oldenkamp, Roberto La Ragione, Sebastien Matamoros, Ngo T. Hoa, Christian Berens, Joy Leng, Julio Álvarez, Marta Ferrandis-Vila, Jenny M. Ritchie, Angelika Fruth, Stefan Schwarz, Lucas Domínguez, María Ugarte-Ruiz, Astrid Bethe, Charlotte Huber, Vanessa Johanns, Ivonne Stamm, Lothar H. Wieler, Christa Ewers, Amanda Fivian-Hughes, Herbert Schmidt, Christian Menge, Torsten Semmler, and Constance Schultsz. Genome-wide association reveals host-specific genomic traits in escherichia coli. BMC Biology, Apr 2023. URL: https://doi.org/10.1186/s12915-023-01562-w, doi:10.1186/s12915-023-01562-w. This article has 46 citations and is from a domain leading peer-reviewed journal.

13. (krzyzanowska2023hostadaptivetraitsin pages 1-2): Dorota M. Krzyżanowska, Magdalena Jabłońska, Zbigniew Kaczyński, Małgorzata Czerwicka-Pach, Katarzyna Macur, and Sylwia Jafra. Host-adaptive traits in the plant-colonizing pseudomonas donghuensis p482 revealed by transcriptomic responses to exudates of tomato and maize. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36494-6, doi:10.1038/s41598-023-36494-6. This article has 9 citations and is from a peer-reviewed journal.

14. (levy2018genomicfeaturesof pages 1-2): Asaf Levy, Isai Salas Gonzalez, Maximilian Mittelviefhaus, Scott Clingenpeel, Sur Herrera Paredes, Jiamin Miao, Kunru Wang, Giulia Devescovi, Kyra Stillman, Freddy Monteiro, Bryan Rangel Alvarez, Derek S. Lundberg, Tse-Yuan Lu, Sarah Lebeis, Zhao Jin, Meredith McDonald, Andrew P. Klein, Meghan E. Feltcher, Tijana Glavina Rio, Sarah R. Grant, Sharon L. Doty, Ruth E. Ley, Bingyu Zhao, Vittorio Venturi, Dale A. Pelletier, Julia A. Vorholt, Susannah G. Tringe, Tanja Woyke, and Jeffery L. Dangl. Genomic features of bacterial adaptation to plants. Nature Genetics, 50:138-150, Dec 2018. URL: https://doi.org/10.1038/s41588-017-0012-9, doi:10.1038/s41588-017-0012-9. This article has 702 citations and is from a highest quality peer-reviewed journal.