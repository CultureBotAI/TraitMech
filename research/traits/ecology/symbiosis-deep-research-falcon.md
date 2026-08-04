---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:50:07.518256'
end_time: '2026-08-03T23:57:55.701900'
duration_seconds: 468.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: symbiosis
  trait_identifier: traitmech:000040
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: symbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An ecological lifestyle in which a microorganism lives in persistent
    physical association with a host or partner organism. It encompasses mutualism,
    commensalism, and parasitism, which form an evolutionary continuum.
  parent_traits: METPO:1000059
  synonyms: symbiotic
  evidence_summary: 'DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al., "Animals in
    a bacterial world", supports persistent host-microbe association (symbiosis) as
    a pervasive microbial lifestyle; parent of the mutualism/commensalism/parasitism
    sub-variants.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. frame symbioses
    as a parasite-mutualist continuum, supporting symbiosis as the umbrella lifestyle
    for these interaction modes.)'
  causal_graph_summary: 'symbiosis_host_interaction: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000040
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which a microorganism lives in persistent physical association with a host or partner organism. It encompasses mutualism, commensalism, and parasitism, which form an evolutionary continuum.
- **Parent traits:** METPO:1000059
- **Synonyms:** symbiotic
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al., "Animals in a bacterial world", supports persistent host-microbe association (symbiosis) as a pervasive microbial lifestyle; parent of the mutualism/commensalism/parasitism sub-variants.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. frame symbioses as a parasite-mutualist continuum, supporting symbiosis as the umbrella lifestyle for these interaction modes.)
- **Existing causal graph summary:** symbiosis_host_interaction: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/symbiosis.yaml`.

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
- **Trait label:** symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000040
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which a microorganism lives in persistent physical association with a host or partner organism. It encompasses mutualism, commensalism, and parasitism, which form an evolutionary continuum.
- **Parent traits:** METPO:1000059
- **Synonyms:** symbiotic
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al., "Animals in a bacterial world", supports persistent host-microbe association (symbiosis) as a pervasive microbial lifestyle; parent of the mutualism/commensalism/parasitism sub-variants.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. frame symbioses as a parasite-mutualist continuum, supporting symbiosis as the umbrella lifestyle for these interaction modes.)
- **Existing causal graph summary:** symbiosis_host_interaction: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/symbiosis.yaml`.

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


# Curation report: microbial symbiosis (`traitmech:000040`)

## Executive curation recommendation

The supplied reviewed class should remain an **umbrella ecological-lifestyle trait**: a microorganism lives in persistent physical association with a host or partner, while the interaction outcome—mutualism, commensalism, or parasitism—is represented separately. Recent synthesis supports a continuum of outcomes but also shows that host finding, attachment, competition, immune accommodation, physiological adaptation, and persistence are shared mechanistic stages across that continuum. Therefore, no single gene or pathway is either necessary or sufficient for “symbiosis” across microorganisms. The graph should consist of **taxon-qualified alternative mechanism modules**, not one universal linear pathway. (wiesmann2023originsofsymbiosis pages 6-8, wiesmann2023originsofsymbiosis pages 1-2)

The strongest additions are: (i) a host-specific adhesin/alternative-secretion module in *Lactiplantibacillus plantarum*–*Drosophila*; (ii) an *mglB*–type-IV-pilus motility module in bee-associated *Snodgrassella*; (iii) a Nod-factor/NFR signaling and root-exudate module in *Lotus japonicus*–rhizobia; and (iv) an ApGLNT1-controlled metabolic-integration module in the pea aphid–*Buchnera* system. These are supported by live imaging, mutant or knockdown experiments, host mutants, serial passage, and competition assays. (gutierrezgarcia2024aconservedbacterial pages 6-7, gutierrezgarcia2024aconservedbacterial pages 9-13, meng2024identificationofthe pages 1-2, duncan2023cooptionofa pages 7-8, tao2024nitrogenandnod pages 1-2)

| Proposed mechanism / edge module | Strongest model system | Evidence design | Confidence / curation recommendation | Key quantitative result | DOI |
|---|---|---|---|---|---|
| SRRP adhesins + aSec secretion system -> stable host-specific foregut colonization | *Lactiplantibacillus plantarum* in *Drosophila melanogaster* gut | Live imaging of single cells, experimental evolution, colonization-island loss mutant, CRISPRi of adhesins | **High; curate as taxon-specific direct edge** | Stable wild-type colonization of ~20,000-50,000 CFU per gut; high-affinity binding diffusion coefficient 0.001 µm2/s versus 0.10 µm2/s for transient binders; colonization-island loss increased diffusion to 0.122 µm2/s; CRISPRi colonization defect ****P<0.0001 (gutierrezgarcia2024aconservedbacterial pages 6-7, gutierrezgarcia2024aconservedbacterial pages 3-4, gutierrezgarcia2024aconservedbacterial pages 9-13) | 10.1126/science.adp7748 |
| *mglB* allele / type IV pili-dependent motility -> increased colonization in non-native host | *Snodgrassella* from *Bombus terrestris* serially passaged in *Apis mellifera* | ARTP mutagenesis, in vivo serial passage, gnotobiotic bees, competition assays | **High; curate as taxon-specific direct edge** | Mutant alleles in the mutual gliding locus out-competed the ancestral strain in the non-native honeybee gut but not in the native host; effect interpreted as altered type IV pili-dependent motility (meng2024identificationofthe pages 1-2) | 10.1186/s40168-024-01813-0 |
| Rhizobial Nod factors -> NFR1/NFR5 signaling -> altered root exudate composition -> altered microbiota assembly | *Lotus japonicus* with rhizobial symbionts | Host mutant comparison (*nfr5*, *nfr1/nfre*, *chit5*), metabolomics, microbiome profiling across nitrogen states | **High for plant-side causal chain; curate as taxon-specific direct edge** | Distinct “starved, symbiotic, or inorganic” nitrogen states produced different root/rhizosphere microbiomes; Nod-factor-signaling mutants had altered community assembly and exudate profiles (tao2024nitrogenandnod pages 9-11, tao2024nitrogenandnod pages 1-2) | 10.1038/s41467-024-47752-0 |
| Rhizobial nitrogenase: N2 -> NH4+ and plant photosynthate/carbon exchange supports persistent symbiosis | Legume-rhizobium root nodules | Integrative physiological/genetic review drawing on split-root, metabolomic, transcriptomic, and mutant literature | **Moderate-High; curate only at generic process level unless adding species-specific supporting primary data** | No single effect size extracted here, but source states bacteria reduce N2 to NH4+ and plant supplies photosynthates/dicarboxylates; nitrogen demand and sugar allocation tune nodule function and senescence (lepetit2023controlofthe pages 1-2) | 10.3389/fpls.2023.1114840 |
| Host ApGLNT1 glutamine transporter + arginine feedback -> metabolic integration with *Buchnera* amino-acid biosynthesis | *Acyrthosiphon pisum*–*Buchnera aphidicola* | Functional transporter characterization, modeling, comparative phylogeny, metabolite concentration comparison | **High; curate as taxon-specific direct edge** | Arginine IC50 values for GLNT1 orthologs are within/near phloem sap arginine range of 4.4-15.2 mM; aphid hemolymph arginine was insufficient to inhibit ApGLNT1, whereas hemolymph glutamine approached saturating levels (duncan2023cooptionofa pages 7-8) | 10.1073/pnas.2308448120 |
| Conserved host-association module: chemotaxis/host sensing + TCS + biofilm + secretion systems + immune evasion -> persistent host association across symbiosis continuum | Cross-system review emphasizing *Pseudomonas*, *Sinorhizobium*, *Brucella*, *Agrobacterium* and other plant/animal associates | Comparative review of shared mechanisms; includes mutant examples for TCS/biofilm systems but mostly umbrella synthesis | **Moderate; curate as umbrella background only, not as a single universal edge** | Review identifies five shared features across pathogenic, commensal, and mutualistic bacteria; no unified cross-taxon effect size, though individual TCS mutants show impaired symbiosis/virulence in cited systems (wiesmann2023originsofsymbiosis pages 6-8, wiesmann2023originsofsymbiosis pages 1-2) | 10.1093/femsre/fuac048 |


*Table: This table ranks the strongest candidate mechanism modules for curating microbial symbiosis (traitmech:000040), separating direct taxon-specific causal edges from broader cross-system umbrella claims. It is useful for deciding which nodes and edges are ready for TraitMech curation versus which should remain as background or warning-level context.*

## 1. Trait scope and boundaries

### Intended phenotype

- **Trait:** `traitmech:000040`—quote and retain this identifier verbatim.
- **Category:** ECOLOGY; **term kind:** CLASS; **mapping:** REVIEWED.
- **Parent:** `METPO:1000059`.
- **Operational meaning:** capacity or realized lifestyle of maintaining a spatially persistent association with a host or partner organism.
- **Observable assays:** repeated recovery after washout or transfer, stable CFU burden, microscopy showing niche-localized cells, vertical transmission, long-term intracellular residence, stable biofilm/adhesion, or organ-specific colonization.
- **Outcome is not the trait itself:** benefit, neutrality, or harm to the host should be encoded as context or a child interaction mode. Pathogens, commensals, and mutualists can use homologous colonization machinery. (wiesmann2023originsofsymbiosis pages 1-2)

### Boundary cases

| Case | Curation decision |
|---|---|
| Transient contact, chemotaxis toward a host, or short-lived attachment | **Insufficient alone.** These can be upstream steps but do not establish persistence. |
| Environmental co-occurrence or correlated abundance | **Exclude** unless physical association and persistence are demonstrated. |
| Cross-feeding between spatially separated organisms | **Exclude from this trait alone**; curate as metabolic interaction unless persistent physical association is also shown. |
| Biofilm formation on an abiotic surface | **Not symbiosis by itself.** Include only when it causally supports association with a living partner. |
| Infection/pathogenesis | **Include** when persistent physical host association is present; pathogenic outcome is a contextual subtype, not an exclusion. |
| Microbiome membership detected once by sequencing | **Weak evidence.** Presence does not establish attachment, residence, or activity. |
| Obligate intracellular endosymbiosis | **Clearly included**, but genome reduction or vertical transmission should not be generalized to all symbioses. |
| Facultative or condition-dependent association | **Included** if persistence occurs under the stated host/environmental conditions. |

A useful graph distinction is: `host encounter → recognition/migration → attachment or invasion → immune accommodation/competition → host-conditioned metabolism → persistence`. Only the final realized association should point directly to `traitmech:000040`; upstream mechanisms should point through colonization or persistence nodes.

## 2. Candidate nodes grouped by type

Identifiers below are deliberately conservative. Organism-specific genes and incompletely verified structures remain label-only rather than receiving invented CURIEs.

### A. Trait and biological-process nodes

- `traitmech:000040` — symbiosis.
- `METPO:1000059` — supplied parent trait.
- Host colonization — label-only candidate.
- Stable host attachment — label-only candidate.
- Host-specific niche recognition — label-only candidate.
- Biofilm formation — candidate GO-grounded process; verify the exact GO term during ingestion.
- Chemotaxis — candidate GO-grounded process; verify exact CURIE.
- Type-IV-pilus-dependent motility — candidate GO-grounded process; verify exact CURIE.
- Protein secretion by alternative Sec system — label-only unless a verified GO term is selected.
- Immune evasion/immune-response modulation — candidate GO processes; outcome and host must be qualified.
- Nitrogen fixation — candidate GO-grounded process; verify exact CURIE.
- Root-nodule development, infection-thread formation, bacteroid differentiation — plant-symbiosis-specific process nodes.
- Root-exudate remodeling and microbiota assembly — label-only composite processes.
- Amino-acid metabolic integration — label-only candidate.

### B. Genes, proteins, transporters, and complexes

- *L. plantarum* `srpA`, `srpB` — serine-rich repeat adhesins; label-only organism-specific genes.
- *L. plantarum* aSec/alternative Sec secretion-system genes — label-only complex/module.
- *Snodgrassella* `mglB` — GTPase-activating protein associated with mutual gliding and type-IV-pilus motility; label-only.
- Type IV pili — cellular complex; select a verified GO cellular-component identifier during curation.
- Rhizobial `nod` genes/Nod-factor biosynthetic machinery — label-only module unless specific KEGG/MetaCyc entries are verified.
- Plant NFR1/NFR5 Nod-factor receptors — organism-specific proteins; use species-specific UniProt accessions only after validation.
- Nitrogenase complex; `nif` genes — verify EC/KEGG/GO identifiers before ingestion.
- Aphid ApGLNT1 — glutamine transporter; label-only organism-specific transporter.
- Two-component systems ExoS/ChvI, BvrR/BvrS, and ChvG/ChvI — taxon-specific sensing/regulatory modules.
- T3SS, T4SS, T6SS and associated effectors — mechanism families, not universally pro-symbiotic nodes.

### C. Chemicals and nutrients

- Dinitrogen, ammonia/ammonium, glutamine, arginine, nitrate, oxygen, iron, phosphate, sugars/photosynthate, and dicarboxylates.
- Nod factors/lipo-chitooligosaccharides — chemical class; verify a suitable CHEBI class before adding a CURIE.
- Flavones/root-exudate metabolites — use individual CHEBI identifiers only where the source resolves the compound.
- Host-derived signals including acidic pH, cationic peptides, and metal ions.

### D. Structures, compartments, and environments

- Drosophila proventriculus/foregut niche.
- Bee gut.
- Plant root surface and rhizosphere.
- Infection thread, root nodule, bacteroid, symbiosome.
- Aphid bacteriocyte and hemolymph.
- Nitrogen-depleted soil and nitrate-supplemented soil.
- Host tissue, mucus, epithelial surface, and intracellular niche.

### E. Taxon/context nodes

Recommended taxon qualifiers include *Lactiplantibacillus plantarum*, *Drosophila melanogaster*, *Snodgrassella*, *Bombus terrestris*, *Apis mellifera*, *Lotus japonicus*, compatible rhizobia, *Acyrthosiphon pisum*, and *Buchnera aphidicola*. NCBITaxon CURIEs should be looked up and validated during YAML preparation rather than inferred here.

## 3. Candidate evidence-backed causal edges

In the table, quotation marks identify concise source-supported snippets or close extracted wording. “High” means direct intervention or mutant evidence; it does not mean universal across taxa.

| # | Subject | Predicate | Object | Evidence snippet | Reference | Strength and notes |
|---:|---|---|---|---|---|---|
| 1 | Host-derived cues | activates | chemotaxis/host finding | The 2023 synthesis identifies “host-finding via chemotaxis responding to chemoattractants,” including primary and specialized metabolites. | DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048), Dec 2023 | **Moderate; umbrella edge.** Mechanistically plausible across systems, but the retrieved passage is review-level rather than a single causal experiment. (wiesmann2023originsofsymbiosis pages 1-2) |
| 2 | Two-component host-sensing systems | promotes | host-conditioned envelope/biofilm physiology | Orthologous BvrR/S, ExoS/ChvI, and ChvG/ChvI systems respond to host-associated cues and regulate outer-membrane modification or biofilm; loss of *S. meliloti chvI* impaired symbiosis. | DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048), Dec 2023 | **Moderate–high but taxon-specific.** Split into system-specific edges; do not create one universal TCS edge. (wiesmann2023originsofsymbiosis pages 6-8) |
| 3 | *L. plantarum* colonization island | enables | stable Drosophila foregut colonization | Complete-island loss caused “acute colonization deficiency,” loss of spatial localization, and reduced adhesion. Wild types maintained approximately **20,000–50,000 CFU/gut**. | DOI: [10.1126/science.adp7748](https://doi.org/10.1126/science.adp7748), Dec 2024 | **High; curate.** Direct loss-of-function plus live imaging; restricted to tested *L. plantarum* strains and fly niche. (gutierrezgarcia2024aconservedbacterial pages 6-7) |
| 4 | `srpA`/`srpB` adhesins | promotes | stable proventriculus attachment | CRISPRi against either adhesin produced a highly significant colonization defect (**P<0.0001**); fibrils occurred in wild type but not the island deletion. | Same Science article | **High; curate as gene-specific edges.** The exact host receptor remains unresolved. (gutierrezgarcia2024aconservedbacterial pages 9-13) |
| 5 | Stable SRRP-mediated binding | decreases | bacterial movement at attachment site | Bound wild-type cells had diffusion coefficient **0.001 μm²/s**, versus **0.10 μm²/s** for transient binders; the colonization-deficient R3P51 derivative was **0.122 μm²/s**. | Same Science article | **High but assay-specific.** Useful as an assay-evidence edge rather than a general biological relation. (gutierrezgarcia2024aconservedbacterial pages 3-4) |
| 6 | aSec secretion system | exports/enables surface display of | SRRP adhesins | The 82.8-kbp colonization region contained `srpA`, `srpB`, and aSec genes; island deletion eliminated efficient colonization. | Same Science article | **Moderate.** Co-deletion supports the module, but retrieved evidence does not isolate each aSec component’s effect; do not claim aSec alone is sufficient. (gutierrezgarcia2024aconservedbacterial pages 3-4, gutierrezgarcia2024aconservedbacterial pages 1-3) |
| 7 | *Snodgrassella mglB* adaptive alleles | increases | colonization fitness in non-native honeybee gut | “Mutations in the mutual gliding locus conferred competitive advantage”; mutant strains outcompeted ancestors in *Apis* but not native *Bombus*. | DOI: [10.1186/s40168-024-01813-0](https://doi.org/10.1186/s40168-024-01813-0), May 2024 | **High; curate with host qualifier.** Strong serial-passage and competition evidence; explicitly host-specific. (meng2024identificationofthe pages 1-2) |
| 8 | *mglB* alleles | alters | type-IV-pilus-dependent motility | The study concluded that the GTPase-activating protein alleles promoted colonization “potentially by altering” type-IV-pilus motility. | Same Microbiome article | **Uncertain mechanism.** Curate with “inferred/potentially” status; direct link from motility change to fitness is not fully isolated. (meng2024identificationofthe pages 1-2) |
| 9 | Rhizobial Nod factors | activates | host NFR1/NFR5 signaling | “Nod factors produced by symbionts activate host NFR1/NFR5 receptors,” initiating symbiotic development. | DOI: [10.1038/s41467-024-47752-0](https://doi.org/10.1038/s41467-024-47752-0), Apr 2024 | **High in Lotus-compatible-rhizobium context.** Supported by `nfr5`, `nfre`, and `chit5` host-mutant comparisons. (tao2024nitrogenandnod pages 1-2) |
| 10 | Nod-factor signaling | modifies | root-exudate composition | Symbiotic, nitrogen-starved, and nitrate-fed plants had distinct exudate profiles; signaling-impaired mutants altered this response. | Same Nature Communications article | **High, taxon- and treatment-specific.** Keep nitrogen state as an experimental factor. (tao2024nitrogenandnod pages 9-11, tao2024nitrogenandnod pages 1-2) |
| 11 | Nod-factor-dependent exudate remodeling | shapes | root/rhizosphere bacterial assembly | Plants in “starved, symbiotic, or inorganic” nitrogen states developed compositionally and topologically different microbiomes. | Same Nature Communications article | **Moderate–high.** Host-mutant and metabolomic data support causality, but individual responsible metabolites require separate validation. (tao2024nitrogenandnod pages 9-11) |
| 12 | Nitrogen starvation-associated flavones | attracts/induces signaling in | compatible rhizobia | Flavones enriched under nitrogen starvation acted as attractants and inducers of rhizobial symbiosis signaling. | Same Nature Communications article | **Moderate.** Curate compound-specific edges only after identifying the exact flavone and direct assay. (tao2024nitrogenandnod pages 9-11) |
| 13 | Rhizobial nitrogenase | reduces | N₂ to NH₄⁺ | “Bacteria reduce N₂ to NH₄⁺ that is assimilated into amino acids by the plant.” | DOI: [10.3389/fpls.2023.1114840](https://doi.org/10.3389/fpls.2023.1114840), Mar 2023 | **High biochemical consensus; generic process edge.** This supports mutualistic function, not persistence of every rhizobial association. (lepetit2023controlofthe pages 1-2) |
| 14 | Plant photosynthate/dicarboxylates | fuels | symbiotic nitrogen fixation | “The plant provides photosynthates to fuel” fixation; carbon allocation and nodule sugar levels tune symbiotic activity. | Same Frontiers article | **Moderate–high.** Strong physiological synthesis, but add species-specific primary evidence before asserting a transporter-level edge. (lepetit2023controlofthe pages 1-2) |
| 15 | Plant nitrogen satiety/mineral nitrogen sufficiency | inhibits | nodule formation and persistence | N-satiety inhibits nodule formation and activates senescence, whereas N deficit stimulates symbiotic nitrogen foraging. | Same Frontiers article | **Moderate–high, conditional.** Encode nitrate/mineral-N status, developmental stage, and host species. (lepetit2023controlofthe pages 1-2) |
| 16 | Aphid ApGLNT1 | transports | glutamine into the aphid–Buchnera metabolic interface | ApGLNT1 was functionally characterized as a glutamine transporter co-opted for host–symbiont integration; *Buchnera* requires glutamine as amino donor for arginine biosynthesis. | DOI: [10.1073/pnas.2308448120](https://doi.org/10.1073/pnas.2308448120), Oct 2023 | **High; curate in pea aphid–Buchnera context.** Distinguish host transporter from microbial trait machinery. (duncan2023cooptionofa pages 7-8) |
| 17 | Arginine | feedback-inhibits | ApGLNT1-mediated glutamine transport | GLNT1 arginine IC₅₀ values were comparable to or below phloem-sap arginine (**4.4–15.2 mM**); hemolymph arginine was insufficient for inhibition, while glutamine approached transporter saturation. | Same PNAS article | **High biochemical edge, context-specific.** This regulates metabolic exchange, but is not direct proof that ApGLNT1 initiates or maintains physical association. (duncan2023cooptionofa pages 7-8) |
| 18 | Biofilm formation | promotes | persistent host association | The recent cross-taxon review identifies biofilm formation as a shared route to chronic association; plant-holobiont synthesis describes biofilm as a major mode of association. | DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048), Dec 2023; [10.3390/ijms252413601](https://doi.org/10.3390/ijms252413601), Dec 2024 | **Moderate umbrella claim.** Only curate with organism- and host-specific perturbation evidence; biofilm can also be environmental or pathogenic. (wiesmann2023originsofsymbiosis pages 1-2, grzyb2024decipheringmolecularmechanisms pages 20-21) |
| 19 | T6SS/toxin-mediated competitor exclusion | facilitates | access to host space and nutrients | Comparative synthesis identifies competition for space/nutrients using toxins and T6SS as a shared host-association feature. | DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048), Dec 2023 | **Uncertain as a direct symbiosis edge.** T6SS effects can promote or destabilize association and must be strain/community qualified. (wiesmann2023originsofsymbiosis pages 1-2) |
| 20 | Immune evasion or calibrated immune suppression | enables | long-term host residence | Conserved host-association synthesis identifies outer-membrane modification and immune evasion as shared mechanisms; outcomes occur across mutualists and pathogens. | Same FEMS review | **Moderate umbrella edge.** Avoid representing “immune suppression” as invariably beneficial or required. (wiesmann2023originsofsymbiosis pages 6-8, wiesmann2023originsofsymbiosis pages 1-2) |

## 4. Recent developments and authoritative interpretation

### 2024: physical niche recognition resolved at single-cell scale

The strongest recent advance is the Science study separating **transient passage from stable physical attachment**. It combined live imaging, experimental evolution, long-read genomics, island deletion, electron microscopy, and CRISPRi. Its quantitative movement and CFU measurements provide an unusually direct bridge from molecular machinery to assay-observed persistence. It also shows why “adhesion” should not automatically be equated with stable symbiosis: strains can bind transiently, whereas host-specific SRRPs establish a low-mobility, spatially localized population. (gutierrezgarcia2024aconservedbacterial pages 7-9, gutierrezgarcia2024aconservedbacterial pages 6-7, gutierrezgarcia2024aconservedbacterial pages 3-4, gutierrezgarcia2024aconservedbacterial pages 9-13)

### 2024: host specificity can evolve through motility machinery

ARTP mutagenesis and in vivo passage of *Snodgrassella* demonstrated that adaptation to a non-native bee host can involve the mutual-gliding locus. The decisive result was ecological: mutant alleles improved competitive fitness in honeybees but not in the native bumblebee. Thus, a colonization determinant may be beneficial only in a particular host and should not be represented as a globally positive edge. (meng2024identificationofthe pages 1-2)

### 2024: symbiosis reorganizes the surrounding microbiome

The *Lotus* study extends the graph beyond the two principal partners. Nod-factor recognition changed host exudation and, consequently, assembly of other root bacteria. This supports a layered graph: microbial signal → host receptor pathway → host environmental modification → community assembly. It is preferable to a direct and overly broad `Nod factor → symbiosis` edge. (tao2024nitrogenandnod pages 9-11, tao2024nitrogenandnod pages 1-2)

### 2023: metabolic integration uses co-opted ancestral host machinery

Functional work on ApGLNT1 indicates that metabolic integration can evolve by recruiting a conserved transporter rather than inventing a symbiosis-specific protein. The authors found GLNT1 conservation across 12 insect orders spanning more than 400 million years. This argues against treating every required host factor as a microbial “symbiosis gene”; partner-derived support nodes should be explicitly typed as host factors. (duncan2023cooptionofa pages 7-8)

### Expert synthesis

Wiesmann and colleagues’ authoritative review proposes five recurrent requirements across bacterial host-association outcomes: host finding, competition for space and nutrients, immune evasion, biofilm-mediated persistence, and two-component sensing/physiological adaptation. The important expert conclusion is **mechanistic reuse across the mutualist–pathogen continuum**: homologous machinery does not determine whether the host benefits or is harmed. (wiesmann2023originsofsymbiosis pages 6-8, wiesmann2023originsofsymbiosis pages 1-2)

## 5. Applications and real-world implementation

1. **Agricultural inoculants and biofertilizers.** Nod-factor compatibility, root colonization, carbon allocation, nitrogen fixation, and soil nitrogen status determine whether rhizobial inoculation produces durable benefit. The graph can support strain selection and explain why greenhouse performance may not transfer to nitrate-rich or otherwise incompatible field soils. (tao2024nitrogenandnod pages 9-11, tao2024nitrogenandnod pages 1-2, lepetit2023controlofthe pages 1-2)
2. **Microbiome engineering.** Host-specific adhesins or secretion systems offer targets for increasing probiotic residence, while anti-adhesion strategies could reduce pathogenic persistence. Translation requires testing receptor specificity, ecological competition, and reversibility because similar machinery occurs in commensals and pathogens. (gutierrezgarcia2024aconservedbacterial pages 7-9, gutierrezgarcia2024aconservedbacterial pages 6-7)
3. **Pest and vector management.** Host-specific gut colonization loci and metabolite exchange can be exploited to disrupt essential symbionts or develop paratransgenic strains. The *Snodgrassella* result warns that engineered fitness may be host-restricted and should be assessed in native and non-native insects. (meng2024identificationofthe pages 1-2)
4. **Community-level crop management.** Nod-factor-driven exudate changes reshape bacteria beyond rhizobia, suggesting that inoculants should be evaluated against whole-community assembly rather than only nodule number. (tao2024nitrogenandnod pages 9-11)
5. **Trait prediction from genomes.** Adhesin islands, secretion machinery, pili, `nod`/`nif` modules, and transporters are useful candidate features, but none alone predicts realized symbiosis. Host genotype, nutrient state, spatial localization, and competition remain necessary contextual variables. (wiesmann2023originsofsymbiosis pages 1-2, tao2024nitrogenandnod pages 1-2)

## 6. Recommended YAML architecture

Use parallel, context-qualified modules rather than merging all evidence into one path:

- **Generic association backbone:** host cue → host finding → attachment/invasion → host-response accommodation and competitor management → host-conditioned metabolism → persistent association → `traitmech:000040`.
- **Drosophila module:** colonization island → aSec-dependent SRRP display → proventriculus attachment → stable CFU population → symbiosis.
- **Bee module:** *mglB* allele → altered type-IV-pilus motility (**uncertain intermediate**) → host-specific competitive colonization → symbiosis.
- **Legume module:** flavonoid cue → rhizobial Nod-factor production → NFR1/NFR5 signaling → infection/nodule development → nitrogenase activity ↔ plant carbon supply → persistent mutualistic association.
- **Aphid module:** host ApGLNT1-mediated glutamine transport → *Buchnera* arginine biosynthesis → amino-acid exchange/metabolic integration → maintenance of nutritional endosymbiosis.

Each edge should carry fields equivalent to `taxon_context`, `host`, `environment`, `evidence_type`, `assay`, `direction`, `certainty`, and `reference`. Host-derived entities should not be mislabeled as microbial intrinsic traits.

## 7. Claims not ready for TraitMech curation

- **Do not curate a universal `biofilm formation → symbiosis` edge.** Biofilms occur on abiotic surfaces and in both harmful and beneficial associations.
- **Do not assert that aSec alone causes colonization.** The strongest deletion removed an entire 82.8-kbp island; adhesin CRISPRi is direct, but component-resolved aSec evidence was not extracted. (gutierrezgarcia2024aconservedbacterial pages 3-4, gutierrezgarcia2024aconservedbacterial pages 9-13)
- **Do not make `mglB → type-IV-pilus motility → colonization` fully asserted.** The source says “potentially by altering”; retain the mechanistic intermediate as uncertain. (meng2024identificationofthe pages 1-2)
- **Do not generalize Nod factors to every rhizobial or plant symbiosis.** Nod-independent nodulation exists, and the retrieved direct evidence concerns *Lotus* and compatible rhizobia.
- **Do not equate nitrogen fixation with symbiosis.** Free-living diazotrophy exists, while many persistent symbioses do not fix nitrogen.
- **Do not treat T3SS/T4SS/T6SS as inherently mutualistic or pathogenic.** Their effects depend on cargo, recipient, competitors, and host genotype. (wiesmann2023originsofsymbiosis pages 1-2)
- **Do not use omics correlation as a causal edge without perturbation.** Differential expression, abundance, or co-occurrence should be labeled associative.
- **Do not infer persistence from a single microbiome sample.** Stable residence requires temporal, washout, localization, transmission, or competition evidence.
- **Do not assign unverified CURIEs.** Species-specific genes, Nod-factor chemical classes, anatomical niches, and environmental states should remain label-only until ontology lookup is completed.

## DOI-first bibliography

1. Gutiérrez-García K, et al. “A conserved bacterial genetic basis for commensal-host specificity.” *Science* 386:1117–1122. **Published December 2024.** DOI: [10.1126/science.adp7748](https://doi.org/10.1126/science.adp7748). (gutierrezgarcia2024aconservedbacterial pages 7-9, gutierrezgarcia2024aconservedbacterial pages 6-7, gutierrezgarcia2024aconservedbacterial pages 3-4, gutierrezgarcia2024aconservedbacterial pages 9-13)
2. Tao K, et al. “Nitrogen and Nod factor signaling determine *Lotus japonicus* root exudate composition and bacterial assembly.” *Nature Communications* 15. **Published April 2024.** DOI: [10.1038/s41467-024-47752-0](https://doi.org/10.1038/s41467-024-47752-0). (tao2024nitrogenandnod pages 9-11, tao2024nitrogenandnod pages 1-2)
3. Meng Y, et al. “Identification of the mutual gliding locus as a factor for gut colonization in non-native bee hosts using ARTP mutagenesis.” *Microbiome* 12. **Published May 2024.** DOI: [10.1186/s40168-024-01813-0](https://doi.org/10.1186/s40168-024-01813-0). (meng2024identificationofthe pages 1-2)
4. Duncan RP, et al. “Co-option of a conserved host glutamine transporter facilitates aphid/*Buchnera* metabolic integration.” *PNAS* 120. **Published October 2023.** DOI: [10.1073/pnas.2308448120](https://doi.org/10.1073/pnas.2308448120). (duncan2023cooptionofa pages 7-8)
5. Wiesmann CL, et al. “Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals.” *FEMS Microbiology Reviews* 47. **Published December 2023.** DOI: [10.1093/femsre/fuac048](https://doi.org/10.1093/femsre/fuac048). (wiesmann2023originsofsymbiosis pages 6-8, wiesmann2023originsofsymbiosis pages 1-2)
6. Lepetit M, Brouquisse R. “Control of the rhizobium–legume symbiosis by the plant nitrogen demand is tightly integrated at the whole plant level and requires inter-organ systemic signaling.” *Frontiers in Plant Science* 14. **Published March 2023.** DOI: [10.3389/fpls.2023.1114840](https://doi.org/10.3389/fpls.2023.1114840). (lepetit2023controlofthe pages 1-2)
7. Grzyb T, Szulc J. “Deciphering Molecular Mechanisms and Diversity of Plant Holobiont Bacteria.” *International Journal of Molecular Sciences* 25:13601. **Published December 2024.** DOI: [10.3390/ijms252413601](https://doi.org/10.3390/ijms252413601). (grzyb2024decipheringmolecularmechanisms pages 20-21)

## Bottom line

The graph should encode **persistent host association as the shared endpoint**, while preserving mechanistic plurality and host/environment specificity. The most defensible immediate curations are the SRRP adhesion module, host-qualified *mglB* colonization edge, Nod-factor/NFR/exudate chain, nitrogen–carbon exchange module, and ApGLNT1 metabolic-integration module. Broad links involving secretion systems, biofilms, immune modulation, and competition should remain taxon-qualified background or uncertain edges until direct perturbation evidence is attached.

References

1. (wiesmann2023originsofsymbiosis pages 6-8): Christina L. Wiesmann, Nicole R. Wang, Yue Zhang, Zhexian Liu, and Cara H. Haney. Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals. FEMS microbiology reviews, Dec 2023. URL: https://doi.org/10.1093/femsre/fuac048, doi:10.1093/femsre/fuac048. This article has 64 citations and is from a domain leading peer-reviewed journal.

2. (wiesmann2023originsofsymbiosis pages 1-2): Christina L. Wiesmann, Nicole R. Wang, Yue Zhang, Zhexian Liu, and Cara H. Haney. Origins of symbiosis: shared mechanisms underlying microbial pathogenesis, commensalism and mutualism of plants and animals. FEMS microbiology reviews, Dec 2023. URL: https://doi.org/10.1093/femsre/fuac048, doi:10.1093/femsre/fuac048. This article has 64 citations and is from a domain leading peer-reviewed journal.

3. (gutierrezgarcia2024aconservedbacterial pages 6-7): Karina Gutiérrez-García, Kevin Aumiller, Ren Dodge, Benjamin Obadia, Ann Deng, Sneha Agrawal, Xincheng Yuan, Richard Wolff, Haolong Zhu, Ru-Ching Hsia, Nandita Garud, and William B. Ludington. A conserved bacterial genetic basis for commensal-host specificity. Science, 386 6726:1117-1122, Dec 2024. URL: https://doi.org/10.1126/science.adp7748, doi:10.1126/science.adp7748. This article has 30 citations and is from a highest quality peer-reviewed journal.

4. (gutierrezgarcia2024aconservedbacterial pages 9-13): Karina Gutiérrez-García, Kevin Aumiller, Ren Dodge, Benjamin Obadia, Ann Deng, Sneha Agrawal, Xincheng Yuan, Richard Wolff, Haolong Zhu, Ru-Ching Hsia, Nandita Garud, and William B. Ludington. A conserved bacterial genetic basis for commensal-host specificity. Science, 386 6726:1117-1122, Dec 2024. URL: https://doi.org/10.1126/science.adp7748, doi:10.1126/science.adp7748. This article has 30 citations and is from a highest quality peer-reviewed journal.

5. (meng2024identificationofthe pages 1-2): Yujie Meng, Xue Zhang, Yifan Zhai, Yuan Li, Zenghua Shao, Shanshan Liu, Chong Zhang, Xin-Hui Xing, and Hao Zheng. Identification of the mutual gliding locus as a factor for gut colonization in non-native bee hosts using the artp mutagenesis. Microbiome, May 2024. URL: https://doi.org/10.1186/s40168-024-01813-0, doi:10.1186/s40168-024-01813-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

6. (duncan2023cooptionofa pages 7-8): Rebecca P. Duncan, Catriona M. H. Anderson, David T. Thwaites, Charles W. Luetje, and Alex C. C. Wilson. Co-option of a conserved host glutamine transporter facilitates aphid/buchnera metabolic integration. Proceedings of the National Academy of Sciences of the United States of America, Oct 2023. URL: https://doi.org/10.1073/pnas.2308448120, doi:10.1073/pnas.2308448120. This article has 13 citations and is from a highest quality peer-reviewed journal.

7. (tao2024nitrogenandnod pages 1-2): Ke Tao, Ib T. Jensen, Sha Zhang, Eber Villa-Rodríguez, Zuzana Blahovska, Camilla Lind Salomonsen, Anna Martyn, Þuríður Nótt Björgvinsdóttir, Simon Kelly, Luc Janss, Marianne Glasius, Rasmus Waagepetersen, and Simona Radutoiu. Nitrogen and nod factor signaling determine lotus japonicus root exudate composition and bacterial assembly. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47752-0, doi:10.1038/s41467-024-47752-0. This article has 30 citations and is from a highest quality peer-reviewed journal.

8. (gutierrezgarcia2024aconservedbacterial pages 3-4): Karina Gutiérrez-García, Kevin Aumiller, Ren Dodge, Benjamin Obadia, Ann Deng, Sneha Agrawal, Xincheng Yuan, Richard Wolff, Haolong Zhu, Ru-Ching Hsia, Nandita Garud, and William B. Ludington. A conserved bacterial genetic basis for commensal-host specificity. Science, 386 6726:1117-1122, Dec 2024. URL: https://doi.org/10.1126/science.adp7748, doi:10.1126/science.adp7748. This article has 30 citations and is from a highest quality peer-reviewed journal.

9. (tao2024nitrogenandnod pages 9-11): Ke Tao, Ib T. Jensen, Sha Zhang, Eber Villa-Rodríguez, Zuzana Blahovska, Camilla Lind Salomonsen, Anna Martyn, Þuríður Nótt Björgvinsdóttir, Simon Kelly, Luc Janss, Marianne Glasius, Rasmus Waagepetersen, and Simona Radutoiu. Nitrogen and nod factor signaling determine lotus japonicus root exudate composition and bacterial assembly. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47752-0, doi:10.1038/s41467-024-47752-0. This article has 30 citations and is from a highest quality peer-reviewed journal.

10. (lepetit2023controlofthe pages 1-2): Marc Lepetit and Renaud Brouquisse. Control of the rhizobium–legume symbiosis by the plant nitrogen demand is tightly integrated at the whole plant level and requires inter-organ systemic signaling. Frontiers in Plant Science, Mar 2023. URL: https://doi.org/10.3389/fpls.2023.1114840, doi:10.3389/fpls.2023.1114840. This article has 105 citations.

11. (gutierrezgarcia2024aconservedbacterial pages 1-3): Karina Gutiérrez-García, Kevin Aumiller, Ren Dodge, Benjamin Obadia, Ann Deng, Sneha Agrawal, Xincheng Yuan, Richard Wolff, Haolong Zhu, Ru-Ching Hsia, Nandita Garud, and William B. Ludington. A conserved bacterial genetic basis for commensal-host specificity. Science, 386 6726:1117-1122, Dec 2024. URL: https://doi.org/10.1126/science.adp7748, doi:10.1126/science.adp7748. This article has 30 citations and is from a highest quality peer-reviewed journal.

12. (grzyb2024decipheringmolecularmechanisms pages 20-21): Tomasz Grzyb and Justyna Szulc. Deciphering molecular mechanisms and diversity of plant holobiont bacteria: microhabitats, community ecology, and nutrient acquisition. International Journal of Molecular Sciences, 25:13601, Dec 2024. URL: https://doi.org/10.3390/ijms252413601, doi:10.3390/ijms252413601. This article has 18 citations.

13. (gutierrezgarcia2024aconservedbacterial pages 7-9): Karina Gutiérrez-García, Kevin Aumiller, Ren Dodge, Benjamin Obadia, Ann Deng, Sneha Agrawal, Xincheng Yuan, Richard Wolff, Haolong Zhu, Ru-Ching Hsia, Nandita Garud, and William B. Ludington. A conserved bacterial genetic basis for commensal-host specificity. Science, 386 6726:1117-1122, Dec 2024. URL: https://doi.org/10.1126/science.adp7748, doi:10.1126/science.adp7748. This article has 30 citations and is from a highest quality peer-reviewed journal.