window.searchData = [
 {
  "discussion_id": "kgscan-30bcdf4a32b0",
  "prompt": "This record routes two independent paths to immune evasion -- complement-regulator binding by surface proteins, and effector delivery through the T3SS. In a given host, is either route sufficient on its own, or does established infection require both?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "animal pathogen",
  "source_id": "METPO:1004002",
  "source_file": "animal_pathogen.yaml",
  "attaches_to": [
   "causal_graphs#immune_evasion"
  ],
  "rationale": "The graph draws both arrows into the same node without saying whether they are alternatives or partners. If either is sufficient, single-target antivirulence strategies are viable; if evasion needs both, only combination approaches will work, and the two edges should carry that dependency rather than reading as parallel routes.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/animal_pathogen.html#kgscan-30bcdf4a32b0"
 },
 {
  "discussion_id": "kgscan-aa46cc9b34ab",
  "prompt": "This record draws nitric oxide straight to biofilm dispersal with nothing in between, while c-di-GMP sits in the same graph wired only to the sessile state. Is the NO effect on dispersal mediated by lowering c-di-GMP, and should that intermediate be on the edge?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "biofilm formation",
  "source_id": "traitmech:000053",
  "source_file": "biofilm_formation.yaml",
  "attaches_to": [
   "causal_graphs#biofilm_dispersal",
   "causal_graphs#nitric_oxide",
   "causal_graphs#c_di_gmp"
  ],
  "rationale": "A bare `induces` edge from a diffusible signal to a community-scale outcome is a placeholder where a mechanism should be. The graph already carries c_di_gmp, but only as a promoter of sessile_state, so it cannot currently express the route most often proposed for this effect. The distinction is not academic: if dispersal runs through the c-di-GMP pool, then strains holding that pool high are intrinsically refractory to the NO-releasing antibiofilm agents now in development -- a resistance mechanism this graph has no way to represent while the edge stays bare.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/biofilm_formation.html#kgscan-aa46cc9b34ab"
 },
 {
  "discussion_id": "kgscan-93e87bc8aba3",
  "prompt": "This record's graph enumerates bsl1 through bsl5, but BSL-5 is not an assigned containment level in any current national framework -- it appears in proposals for hypothetical agents beyond BSL-4. Is the bsl5 node a real classification this record should carry, or a seeded artefact to retract?",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "biosafety level",
  "source_id": "METPO:1001101",
  "source_file": "biosafety_level.yaml",
  "attaches_to": [
   "causal_graphs#bsl5"
  ],
  "rationale": "A containment level that does not exist in regulation is not a value the trait can take, and anything downstream that enumerates levels from this graph -- a risk-assessment form, an ontology mapping, a facility-capability query -- would inherit a level with no requirements attached to it. Note what the resolution is NOT: the node is already labelled a proposal and grounded to METPO:1001106, which the corpus carries as its own seeded record at ecology/biosafety_level_5.yaml, so deleting it here would desynchronise this graph from an upstream-seeded record rather than fix anything. A METPO class is not a citable proposal, so the question stands -- but it is answered by finding the source behind METPO:1001106, and any retraction belongs upstream in METPO, not in this graph.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/biosafety_level.html#kgscan-93e87bc8aba3"
 },
 {
  "discussion_id": "kgscan-066a51aacfb6",
  "prompt": "BSL-2 requires a biosafety cabinet specifically for procedures with aerosol or splash potential, while other work may go on the open bench. Which procedures actually generate an infectious dose at the breathing zone, and does the current procedure list match them?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "biosafety level 2",
  "source_id": "METPO:1001103",
  "source_file": "biosafety_level_2.yaml",
  "attaches_to": [
   "causal_graphs#aerosol_splash_procedure",
   "causal_graphs#biosafety_cabinet"
  ],
  "rationale": "The bench/cabinet boundary is the single control that most BSL-2 work turns on, and it is drawn from procedure lists that long predate quantitative aerosol measurement. A procedure that is on the open bench but does generate respirable particles is an unrecognised exposure; one needlessly in the cabinet costs throughput. Either way the edge into biosafety_cabinet is asserting something measurable that has not been measured.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/biosafety_level_2.html#kgscan-066a51aacfb6"
 },
 {
  "discussion_id": "kgscan-2ee31ba13f9c",
  "prompt": "BSL-3 boundary integrity is verified by pressure-decay testing of the room envelope. Does passing a pressure-decay test predict containment of an airborne agent under real operating conditions, with doors cycling and equipment running?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "biosafety level 3",
  "source_id": "METPO:1001104",
  "source_file": "biosafety_level_3.yaml",
  "attaches_to": [
   "causal_graphs#boundary_integrity_testing",
   "causal_graphs#pressure_decay_testing"
  ],
  "rationale": "The graph routes verification the other way round from the claim it supports: bsl3_trait is `verified by` boundary_integrity_testing, which `utilizes` pressure_decay_testing. So the decay test stands in for containment without any node asserting that containment holds. The test is also performed on a sealed, static room, and the room only matters when it is occupied and in use. If the two diverge, facilities are certified against a condition they never operate in.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/biosafety_level_3.html#kgscan-2ee31ba13f9c"
 },
 {
  "discussion_id": "kgscan-e770cf01677c",
  "prompt": "Every BSL-4 control this record requires assumes terrestrial gravity and somewhere to put contaminated air, water and waste -- suit overpressure, airlocks, chemical showers, specialized waste disposal. Which still contain an agent in a closed-loop habitat that recycles all three?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "biosafety level 4",
  "source_id": "METPO:1001105",
  "source_file": "biosafety_level_4.yaml",
  "attaches_to": [
   "causal_graphs#positive_pressure_suit",
   "causal_graphs#airlock",
   "causal_graphs#decontamination_shower",
   "causal_graphs#specialized_waste_disposal"
  ],
  "rationale": "Sample-return and crewed-habitat missions need containment for agents with no countermeasure, which is exactly what BSL-4 is for. But every control edge runs outward from bsl4_trait to a piece of equipment -- `requires` an airlock, a decontamination shower, specialized waste disposal; `necessitates use of` a positive pressure suit -- so the controls are named as hardware rather than as the physics they rely on, and it is the physics that does or does not transfer. Sedimentation-dependent controls behave differently in microgravity, and a shower and a waste stream that both feed a recycling loop are not disposal. As written the record cannot distinguish a control that survives the move from one that does not, because it never says what any of them do.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/biosafety_level_4.html#kgscan-e770cf01677c"
 },
 {
  "discussion_id": "kgscan-3606bdcc991b",
  "prompt": "Commensalism is defined in this record by a neutral effect on host fitness. Has neutrality ever been measured for these associations, or is it inferred from the absence of visible disease -- and does it hold when the host is stressed, starved, or co-infected?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "commensalism",
  "source_id": "traitmech:000042",
  "source_file": "commensalism.yaml",
  "attaches_to": [
   "causal_graphs#neutral_host_fitness"
  ],
  "rationale": "Neutral_host_fitness is the node that makes this trait different from mutualism and parasitism, and it is the one node stated as a definition rather than an observation. If neutrality is only ever the null result of an underpowered comparison in an unstressed host, then commensalism is a measurement category rather than a biological one, and records assigned to it are provisional in a way the corpus does not currently mark.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/commensalism.html#kgscan-3606bdcc991b"
 },
 {
  "discussion_id": "kgscan-a6758e26f5a6",
  "prompt": "Two edges reach genome reduction here: confined habitat through metabolic gene loss, and the trait itself, whose description bundles drift in as `with small Ne`. The nodes that would give drift a mechanism -- transmission bottleneck, limited recombination -- connect to neither. Should they feed the drift edge, and which mechanism dominates?",
  "kind": "CONTROVERSY",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "endosymbiosis",
  "source_id": "traitmech:000045",
  "source_file": "endosymbiosis.yaml",
  "attaches_to": [
   "causal_graphs#reductive_genome_evolution",
   "causal_graphs#transmission_bottleneck",
   "causal_graphs#limited_recombination",
   "causal_graphs#metabolic_gene_loss"
  ],
  "rationale": "The record asserts both mechanisms but at different resolutions, which is what makes them impossible to weigh. Drift arrives bundled into a trait-level edge as a parenthetical -- `with small Ne` inside a description -- while selection is spelled out as a two-step path through metabolic_gene_loss. transmission_bottleneck and limited_recombination attach to each other and to nothing else, so the drift claim has no mechanism under it, and host_symbiont_aa_complementarity -> nutritional_compensation is likewise its own disconnected pair, so compensation is not wired into reduction either. The two predict opposite loss spectra -- drift removes genes roughly regardless of function, compensation removes exactly the genes whose products the host supplies -- so until they are stated at the same resolution the graph cannot say what a newly sequenced symbiont will have lost, which is most of what a reduction model is for.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/endosymbiosis.html#kgscan-a6758e26f5a6"
 },
 {
  "discussion_id": "kgscan-d5aefedf82bb",
  "prompt": "Ectoine and glycine betaine both enable osmotic stress tolerance here, but trehalose is wired instead to environmental stress tolerance -- a node with no outgoing edge. Is that split a real distinction, or does trehalose belong on the osmotic route too?",
  "kind": "KNOWLEDGE_GAP",
  "status": "RESOLVED",
  "is_gap": "Knowledge gap",
  "source_name": "free-living",
  "source_id": "traitmech:000048",
  "source_file": "free_living.yaml",
  "attaches_to": [
   "causal_graphs#osmotic_stress_tolerance",
   "causal_graphs#environmental_stress_tolerance",
   "causal_graphs#ectoine_biosynthesis",
   "causal_graphs#glycine_betaine_system",
   "causal_graphs#trehalose_biosynthesis"
  ],
  "rationale": "Because environmental_stress_tolerance has no outgoing edge, nothing downstream depends on trehalose at all: this record currently predicts the trait's osmotolerance from two systems and leaves the third dangling. Either reading has a consequence. If trehalose does serve osmotic tolerance, a genome carrying only trehalose scores as non-osmotolerant when it is not, which is exactly the inference anything reading habitat range off gene content would make. If the split is real -- trehalose for desiccation and thermal stress rather than osmolarity -- then the dangling node needs its own edge onward to the trait. The second question, whether the two routes that do converge are redundant or condition-partitioned, rides along on the same experiment: their costs differ sharply, since de novo ectoine synthesis is carbon-expensive where betaine uptake is cheap given a precursor.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/free_living.html#kgscan-d5aefedf82bb"
 },
 {
  "discussion_id": "kgscan-4fc1a06fa1e3",
  "prompt": "This record commits to luminal oxygen limitation contributing to the primary fermenter community. Does the reverse arm hold too -- do the fermenters and the epithelium maintain the anoxia -- making this a feedback loop rather than the one-way edge drawn?",
  "kind": "KNOWLEDGE_GAP",
  "status": "RESOLVED",
  "is_gap": "Knowledge gap",
  "source_name": "gut-associated",
  "source_id": "traitmech:000052",
  "source_file": "gut_associated.yaml",
  "attaches_to": [
   "causal_graphs#luminal_oxygen_limitation",
   "causal_graphs#primary_fermenter_community"
  ],
  "rationale": "The existing edge is not wrong so much as half: it says the anoxic lumen permits the fermenters, and stops. If the return arm also holds, the two nodes are a self-reinforcing loop, and losing the fermenters raises luminal oxygen and admits facultative pathogens -- the collapse that follows antibiotic depletion. That is the clinically load-bearing half, and a graph of one-way edges can only carry it if someone draws it.",
  "num_experiments": 1,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "claude",
  "page_url": "../../pages/traits/ecology/gut_associated.html#kgscan-4fc1a06fa1e3"
 },
 {
  "discussion_id": "abi2-family-boundary-gap",
  "prompt": "Resolve the natural Abi2 locus breadth, phage trigger, and AbiD/F-group mapping before minting narrower Abi2 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Abi2 system",
  "source_id": "traitmech:000338",
  "source_file": "abi2_system.yaml",
  "attaches_to": [
   "causal_graphs#abi2_locus_restricts_phage"
  ],
  "rationale": "The DefenseFinder Abi2 model namespace requires the Abi2__Abi_2 PF07751 profile; InterPro treats PF07751 as an Abi-like family, and UniProt maps the AbiD1 protein onto the same Pfam family. This first record leaves unresolved whether DefenseFinder Abi2 exactly corresponds to AbiD1, the broader AbiD/F group, or a different subset of Abi-like loci; it therefore avoids protein-level chemistry and records only the genome-level model namespace.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abi2_system.html#abi2-family-boundary-gap"
 },
 {
  "discussion_id": "abia-defensefinder-subrule-gap",
  "prompt": "Resolve the AbiA_large and AbiA_small system boundaries, phage trigger, direct DNA-replication target, and molecular effector output before minting narrower AbiA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiA system",
  "source_id": "traitmech:000344",
  "source_file": "abia_system.yaml",
  "attaches_to": [
   "causal_graphs#abia_locus_inhibits_phage_dna_replication"
  ],
  "rationale": "Dinsmore and Klaenhammer support AbiA as a lactococcal abortive-infection determinant whose copy number or expression changes phage resistance and whose leucine-repeat region is required for activity against multiple phage species. DefenseFinder models AbiA through AbiA_large and AbiA_small subrules, but this first system-level record leaves those subrules' natural locus boundaries, the direct phage trigger, the molecular effector output, the exact phage-DNA-replication target, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "PMID:16349225",
   "PMID:9661658",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abia_system.html#abia-defensefinder-subrule-gap"
 },
 {
  "discussion_id": "abialpha-lysis-route-gap",
  "prompt": "Resolve the AbiAlpha direct molecular target, Idefix trigger, lysis route, natural host range, and phage escape routes before minting narrower AbiAlpha mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiAlpha system",
  "source_id": "traitmech:000322",
  "source_file": "abialpha_system.yaml",
  "attaches_to": [
   "causal_graphs#abialpha_locus_causes_enterococcal_premature_lysis"
  ],
  "rationale": "Lossouarn et al. support AbiAlpha as a prophage-encoded Enterococcus faecalis abortive-infection system that maps to DUF4393/PF14337 and perturbs Idefix lysis timing. DefenseFinder represents AbiAlpha with a one-profile HMM inventory row but does not resolve the direct phage trigger, DUF4393-family molecular function, Idefix lysis target, natural host range, or escape routes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abialpha_system.html#abialpha-lysis-route-gap"
 },
 {
  "discussion_id": "abib-trigger-and-rnase-gap",
  "prompt": "Resolve the AbiB phage trigger, AbiB molecular function, and RNase effector before minting narrower AbiB mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiB system",
  "source_id": "traitmech:000319",
  "source_file": "abib_system.yaml",
  "attaches_to": [
   "causal_graphs#abib_locus_degrades_sensitive_phage_transcripts"
  ],
  "rationale": "Parreira et al. support AbiB as a named lactococcal abortive-infection determinant that prevents bIL170 growth and promotes sensitive phage transcript degradation. DefenseFinder represents AbiB with a one-profile rule, but this first system-level record leaves the phage trigger, AbiB molecular function, RNase effector identity, natural locus breadth, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abib_system.html#abib-trigger-and-rnase-gap"
 },
 {
  "discussion_id": "abic-trigger-and-death-route-gap",
  "prompt": "Resolve the AbiC phage trigger, AbiC molecular function, and infected-cell death route before minting narrower AbiC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiC system",
  "source_id": "traitmech:000320",
  "source_file": "abic_system.yaml",
  "attaches_to": [
   "causal_graphs#abic_locus_aborts_lactococcal_phage_p2_infection"
  ],
  "rationale": "Durmaz et al. support AbiC as a named lactococcal abortive-infection determinant that reduces p2 plating, plaque size, and burst size while killing most Prf-positive infected cells. DefenseFinder represents AbiC with a one-profile rule, but this first system-level record leaves the phage trigger, AbiC molecular function, cell-death route, natural locus breadth, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abic_system.html#abic-trigger-and-death-route-gap"
 },
 {
  "discussion_id": "abid-trigger-and-effector-gap",
  "prompt": "Resolve the AbiD phage trigger, molecular activity, and direct arrest target before minting narrower AbiD mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiD system",
  "source_id": "traitmech:000318",
  "source_file": "abid_system.yaml",
  "attaches_to": [
   "causal_graphs#abid_locus_reduces_lactococcal_phage_burst"
  ],
  "rationale": "McLandsborough et al. support AbiD as a named lactococcal abortive-infection determinant whose cloned pBF61 fragment reduces sk1 plating efficiency and c2 burst size, whose abiD open reading frame is required for the Abi phenotype, and whose activity does not primarily block phage adsorption. DefenseFinder represents AbiD with a one-profile rule, but this first system-level record leaves the phage trigger, AbiD molecular function, direct host or phage target, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abid_system.html#abid-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abif-function-and-host-breadth-gap",
  "prompt": "Resolve the exact AbiF protein function, phage trigger, host target, AbiD/AbiD1 homology-derived family boundary, and natural locus breadth before minting narrower AbiF mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiF system",
  "source_id": "traitmech:000504",
  "source_file": "abif_system.yaml",
  "attaches_to": [
   "causal_graphs#abif_locus_inhibits_lactococcal_phage_dna_replication"
  ],
  "rationale": "Garvey et al. support AbiF as a pNP40 determinant cloned on pCG1 that conforms to abortive-infection criteria, depends on a single complete open reading frame, and inhibits the rate of phage phi 712 DNA replication; the FEMS review retains AbiF among confirmed two-component lactococcal Abi-like systems. This first system-level record therefore leaves the direct phage trigger, exact AbiF molecular activity, relevant host target, AbiD/AbiD1-related family boundary, natural locus breadth, cell-death or growth-arrest route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "DOI:10.1128/AEM.61.12.4321-4328.1995",
   "DOI:10.1128/AEM.61.12.4321-4328.1995",
   "DOI:10.1093/femsre/fuag009"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abif_system.html#abif-function-and-host-breadth-gap"
 },
 {
  "discussion_id": "abig-primary-target-gap",
  "prompt": "Resolve the AbiG phage trigger, AbiGi and AbiGii molecular functions, and primary arrest target before minting narrower AbiG mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiG system",
  "source_id": "traitmech:000306",
  "source_file": "abig_system.yaml",
  "attaches_to": [
   "causal_graphs#abig_inhibits_lactococcal_phage_rna_synthesis"
  ],
  "rationale": "O'Connor et al. support AbiG as a named lactococcal abortive-infection system encoded by two adjacent pCI750 open reading frames, and DefenseFinder represents AbiG with a two-profile rule. The 1999 transcription study connects AbiG to inhibited phage sk1 and late c2 RNA synthesis, but it explicitly leaves unresolved whether transcription is the system's primary target or a secondary effect.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "DOI:10.1128/aem.65.1.330-335.1999"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abig_system.html#abig-primary-target-gap"
 },
 {
  "discussion_id": "abih-trigger-and-effector-gap",
  "prompt": "Resolve the AbiH phage trigger, molecular activity, and direct arrest target before minting narrower AbiH mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiH system",
  "source_id": "traitmech:000304",
  "source_file": "abih_system.yaml",
  "attaches_to": [
   "causal_graphs#abih_locus_restricts_lactococcal_phages"
  ],
  "rationale": "Prevots et al. support AbiH as a named lactococcal abortive-infection gene whose cloned S94 locus reduces or blocks plating by tested lactococcal phages, and DefenseFinder represents AbiH with a one-profile rule. This system-level record leaves the phage trigger, AbiH molecular function, direct cellular target, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abih_system.html#abih-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abii-trigger-and-effector-gap",
  "prompt": "Resolve the AbiI phage trigger, molecular activity, and direct arrest target before minting narrower AbiI mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiI system",
  "source_id": "traitmech:000316",
  "source_file": "abii_system.yaml",
  "attaches_to": [
   "causal_graphs#abii_locus_reduces_lactococcal_phage_burst"
  ],
  "rationale": "Su et al. support AbiI as a named lactococcal abortive-infection locus whose cloned pND852 fragment reduces phi 712 burst size and whose abiI frameshift abolishes phage resistance. DefenseFinder represents AbiI with a one-profile rule, but this first system-level record leaves the phage trigger, AbiI molecular function, direct host or phage target, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:9195753"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abii_system.html#abii-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abij-trigger-and-effector-gap",
  "prompt": "Resolve the AbiJ phage trigger, molecular activity, and exact AbiA escape-mutant overlap before minting narrower AbiJ mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiJ system",
  "source_id": "traitmech:000339",
  "source_file": "abij_system.yaml",
  "attaches_to": [
   "causal_graphs#abij_locus_restricts_lactococcal_phage"
  ],
  "rationale": "Deng et al. support AbiJ as a lactococcal plasmid-encoded abortive-infection system, and DefenseFinder represents AbiJ with a one-profile rule. Mosterd et al. show that AbiJ escape behavior overlaps with AbiA escape mutants, but the FEMS review notes that AbiJ still lacks a resolved mechanism. This first system-level record therefore leaves AbiJ's direct phage trigger, molecular effector activity, natural locus breadth, exact HEPN-domain interpretation, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/femsre/fuag009"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abij_system.html#abij-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abil-trigger-and-effector-gap",
  "prompt": "Resolve the AbiL phage trigger, AbiLi and AbiLii activities, AbiLi2 and AbiLii2 HMM row relationships, and ATPase-plus-TOPRIM mechanism before minting narrower AbiL mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiL system",
  "source_id": "traitmech:000340",
  "source_file": "abil_system.yaml",
  "attaches_to": [
   "causal_graphs#abil_locus_restricts_lactococcal_phage"
  ],
  "rationale": "Deng et al. support AbiL as a lactococcal phage abortive infection system, the FEMS review lists AbiL among confirmed two-component lactococcal Abi-like systems, and DefenseFinder represents AbiL with mandatory AbiL__AbiLi and AbiL__AbiLii profiles. The same pinned HMM inventory also contains AbiL__AbiLi2 and AbiL__AbiLii2 rows that are not in the pinned two-profile rule, and the FEMS review summarizes unresolved ATPase and TOPRIM predictions. This first system-level record therefore leaves the direct phage trigger, exact AbiLi and AbiLii molecular activities, accessory-model interpretation, AbiL-to-PARIS similarity, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/femsre/fuag009"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abil_system.html#abil-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abin-trigger-and-effector-gap",
  "prompt": "Resolve the AbiN phage trigger, molecular activity, predicted ligand-binding sensor interpretation, and growth-arrest or cell-death route before minting narrower AbiN mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiN system",
  "source_id": "traitmech:000341",
  "source_file": "abin_system.yaml",
  "attaches_to": [
   "causal_graphs#abin_locus_restricts_lactococcal_phage"
  ],
  "rationale": "Prevots et al. support AbiN as a chromosomal lactococcal abortive infection gene, the FEMS review retains AbiN among confirmed lactococcal Abi-like systems, and DefenseFinder represents AbiN with a mandatory AbiN__AbiN profile. The FEMS table leaves the affected phage lytic-cycle step, phage escape mutants, and mechanism of cell arrest or death unknown, and the FEMS structural discussion predicts a putative ligand-binding sensor fold while explicitly calling for further research on the AbiN mechanism. This first system-level record therefore leaves the direct phage trigger, sensor ligand, exact molecular activity, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/femsre/fuag009",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abin_system.html#abin-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abio-trigger-and-effector-gap",
  "prompt": "Resolve the AbiO phage trigger, restriction-endonuclease and helicase activity, and growth-arrest or cell-death route before minting narrower AbiO mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiO system",
  "source_id": "traitmech:000342",
  "source_file": "abio_system.yaml",
  "attaches_to": [
   "causal_graphs#abio_locus_restricts_lactococcal_phage"
  ],
  "rationale": "Prevots and Ritzenthaler support AbiO as a lactococcal abortive phage resistance gene, the FEMS review retains AbiO among confirmed lactococcal Abi-like systems, and DefenseFinder represents AbiO with a mandatory AbiO__AbiO profile. The FEMS table leaves the AbiO effect on the cell and phage escape proteins unknown for the tested phages, and the FEMS structural discussion predicts restriction-endonuclease-like and SF1B-helicase-like domains while not resolving the molecular trigger or effector activity. This first system-level record therefore leaves the direct phage trigger, exact molecular activity, growth-arrest or cell-death route, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/femsre/fuag009",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abio_system.html#abio-trigger-and-effector-gap"
 },
 {
  "discussion_id": "abip2-ug-abi-mechanism-gap",
  "prompt": "Resolve the AbiP2 natural locus breadth, phage trigger, protein-primed polymerase output, and growth-arrest or cell-death route before minting narrower AbiP2 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiP2 system",
  "source_id": "traitmech:000343",
  "source_file": "abip2_system.yaml",
  "attaches_to": [
   "causal_graphs#abip2_locus_restricts_phage_propagation"
  ],
  "rationale": "Odegrip et al. support a P2-like-coliphage reverse transcriptase gene that blocks phage T5 infection, Mestre et al. describe the UG/Abi reverse-transcriptase family, the FEMS review places AbiP2 in that family rather than the unrelated lactococcal AbiP family, Figiel et al. structurally characterize Abi-P2 as a template-independent Abi polymerase, and DefenseFinder represents AbiP2 with a mandatory AbiP2__AbiP2 profile. This first system-level record therefore leaves the direct phage trigger, in vivo DNA product, exact relationship to broader UG/Abi systems, prophage host breadth, and growth-arrest or cell-death route unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1128/JB.188.4.1643-1647.2006",
   "DOI:10.1093/nar/gkac467",
   "DOI:10.1093/femsre/fuag009",
   "DOI:10.1093/nar/gkac772",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abip2_system.html#abip2-ug-abi-mechanism-gap"
 },
 {
  "discussion_id": "abip2-defensefinder-article-registry-gap",
  "prompt": "Resolve the DefenseFinder AbiP2 article-registry mapping before using List_system_article.md as positive system literature evidence.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "AbiP2 system",
  "source_id": "traitmech:000343",
  "source_file": "abip2_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned DefenseFinder HMM inventory and rules table support AbiP2 as a one-profile model namespace, but its article registry row maps AbiP2 to a 2005 lactococcal abortive-infection review that predates Odegrip et al. 2006. This record therefore leaves the registry-to-primary link unresolved and relies on Odegrip et al., Mestre et al., the FEMS review, Figiel et al., and pinned DefenseFinder HMM/rule rows for AbiP2 identity and system coverage.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abip2_system.html#abip2-defensefinder-article-registry-gap"
 },
 {
  "discussion_id": "abir-component-activity-gap",
  "prompt": "Resolve the AbiR phage trigger, profile-to-locus mapping, and AbiRa, AbiRb, and AbiRc molecular functions before minting narrower AbiR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiR system",
  "source_id": "traitmech:000317",
  "source_file": "abir_system.yaml",
  "attaches_to": [
   "causal_graphs#abir_loci_impede_phage_dna_replication"
  ],
  "rationale": "Twomey et al. support AbiR as a multicomponent abortive-infection system encoded by two separated pKR223 loci, and DefenseFinder represents AbiR with a three-profile rule. This first system-level record leaves the phage trigger, the mapping from the two original genetic loci to AbiRa, AbiRb, and AbiRc profiles, the component molecular activities, and the direct reason that AbiR impedes phage DNA replication unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:10831451"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abir_system.html#abir-component-activity-gap"
 },
 {
  "discussion_id": "abiu-orf-and-transcription-gap",
  "prompt": "Resolve the AbiU phage trigger, direct AbiU1 and AbiU2 functions, and phage-transcription-delay route before minting narrower AbiU mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiU system",
  "source_id": "traitmech:000321",
  "source_file": "abiu_system.yaml",
  "attaches_to": [
   "causal_graphs#abiu_locus_delays_lactococcal_phage_transcription"
  ],
  "rationale": "Dai et al. support AbiU as a named lactococcal abortive-infection system that reduces plaquing of c2, 936, and P335 phages and delays 712 and c2 phage transcription. DefenseFinder represents AbiU with a one-profile rule, but this first system-level record leaves the phage trigger, AbiU1 molecular function, AbiU2 downregulation route, natural locus breadth, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abiu_system.html#abiu-orf-and-transcription-gap"
 },
 {
  "discussion_id": "abiv-mechanism-gap",
  "prompt": "Resolve the host translational target of the AbiV-SaV complex before minting narrower AbiV mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AbiV system",
  "source_id": "traitmech:000300",
  "source_file": "abiv_system.yaml",
  "attaches_to": [
   "causal_graphs#abiv_sav_translation_block"
  ],
  "rationale": "Haaber et al. identify phage sav as the determinant of AbiV sensitivity and support direct AbiV-SaV complex formation followed by inhibition of phage protein translation, but the precise host translational target and complete route from the AbiV-SaV complex to abortive infection remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abiv_system.html#abiv-mechanism-gap"
 },
 {
  "discussion_id": "abortive-infection-subfamily-split-gap",
  "prompt": "Resolve other abortive-infection families before minting narrower children under the broad abortive infection system parent.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "abortive infection system",
  "source_id": "traitmech:000214",
  "source_file": "abortive_infection_system.yaml",
  "attaches_to": [],
  "rationale": "ToxIN, AbiQ, AbiE, AbiF, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, CmdTAC, Abi2, AbiJ, AbiL, AbiN, AbiO, AbiP2, AbiA, and PD-T4-10 are split out as traitmech:000226, traitmech:000225, traitmech:000227, traitmech:000504, traitmech:000228, traitmech:000229, traitmech:000230, traitmech:000300, traitmech:000301, traitmech:000303, traitmech:000304, traitmech:000306, traitmech:000316, traitmech:000317, traitmech:000318, traitmech:000319, traitmech:000320, traitmech:000321, traitmech:000322, traitmech:000323, traitmech:000324, traitmech:000325, traitmech:000335, traitmech:000338, traitmech:000339, traitmech:000340, traitmech:000341, traitmech:000342, traitmech:000343, traitmech:000344, and traitmech:000394, respectively. Lopatina et al., Fineran et al., Dy et al., Garvey et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., Haaber et al., Owen et al., Depardieu et al., Prevots et al., O'Connor et al., Su et al., Twomey et al., McLandsborough et al., Parreira et al., Durmaz et al., Dai et al., Lossouarn et al., Cram et al., Parma et al., Johnson et al., Vassallo et al., Chopin et al., Anba et al., Deng et al., Prevots et al., Prevots and Ritzenthaler, Odegrip et al., Dinsmore and Klaenhammer, and Dinsmore et al. still support abortive infection as a genomically encoded phage defense strategy that spans mechanistically diverse toxin-antitoxin, pNP40-derived lactococcal AbiF DNA-replication-inhibition, premature-lysis, RT-related polymerase, two-component, translation-inhibition, prophage-encoded DNA-replication-inhibition, staphylococcal-kinase-triggered cell death, lactococcal AbiH phage resistance, two-gene lactococcal AbiG RNA-synthesis interference, single-ORF lactococcal AbiI burst-size reduction, two-separated-locus lactococcal AbiR DNA-replication impediment, pBF61-derived lactococcal AbiD burst-size reduction, lactococcal AbiB phage-transcript decay, lactococcal AbiC Prf infected-cell death, lactococcal AbiU phage-transcription delay, enterococcal AbiAlpha premature lysis, F-plasmid pif-region T7 abortive infection, lambda Rex two-component phage exclusion, ICEBs1 SpbK abortive SP\u03b2 defense, CmdTAC mRNA ADP-ribosyltransferase abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, single-profile lactococcal AbiJ loci, two-component lactococcal AbiL ATPase/TOPRIM-family loci, single-gene lactococcal AbiN loci, single-profile lactococcal AbiO loci, single-profile coliphage AbiP2 reverse-transcriptase-like loci, lactococcal AbiA loci represented by DefenseFinder AbiA-large and AbiA-small subrules, DefenseFinder PD-T4-10 two-profile loci, and other families. Additional narrower TraitRecords need separate review to ground each subfamily's trigger, effector, growth-arrest or cell-death mechanism, and phage escape routes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/abortive_infection_system.html#abortive-infection-subfamily-split-gap"
 },
 {
  "discussion_id": "aditi-mechanism-gap",
  "prompt": "Resolve Aditi phage triggers and effector outputs before minting narrower Aditi mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Aditi system",
  "source_id": "traitmech:000247",
  "source_file": "aditi_system.yaml",
  "attaches_to": [
   "causal_graphs#aditi_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Aditi as a named anti-phage system with DitA and DitB profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/aditi_system.html#aditi-mechanism-gap"
 },
 {
  "discussion_id": "ambrosia-regulatory-mechanism-gap",
  "prompt": "Resolve Ambrosia phage triggers, DNA targets, and model coverage before minting narrower Ambrosia mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ambrosia system",
  "source_id": "traitmech:000329",
  "source_file": "ambrosia_system.yaml",
  "attaches_to": [
   "causal_graphs#ambrosia_locus_restricts_phage"
  ],
  "rationale": "Keesman et al. support Ambrosia as a five-gene anti-phage system with tightly regulated RM-like components, but the direct phage trigger, the AbrB/AbrC regulatory chain, the exact AbrA/AbrD substrate and DNA modification, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ambrosia_system.html#ambrosia-regulatory-mechanism-gap"
 },
 {
  "discussion_id": "apsab-substrate-and-guide-source-gap",
  "prompt": "Resolve ApsAB guide sources, plasmid substrates, and model coverage before minting narrower ApsAB mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ApsAB system",
  "source_id": "traitmech:000328",
  "source_file": "apsab_system.yaml",
  "attaches_to": [
   "causal_graphs#apsab_locus_destabilizes_plasmids"
  ],
  "rationale": "Zongo et al. support ApsAB as a two-component E. coli anti-plasmid system and report activity against high- and low-copy-number plasmids, but the direct ApsB guide source, the target-recognition rule, exact plasmid-degradation chemistry, natural substrate range, family-level breadth, and profile-to-component model are not resolved enough here to assert narrower mechanistic or subtype traits.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/apsab_system.html#apsab-substrate-and-guide-source-gap"
 },
 {
  "discussion_id": "aristaios-mechanism-gap",
  "prompt": "Resolve Aristaios phage triggers and effector outputs before minting narrower Aristaios mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Aristaios system",
  "source_id": "traitmech:000313",
  "source_file": "aristaios_system.yaml",
  "attaches_to": [
   "causal_graphs#aristaios_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al. and DefenseFinder support Aristaios as a named anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/aristaios_system.html#aristaios-mechanism-gap"
 },
 {
  "discussion_id": "armada-subtype-model-and-mechanism-gap",
  "prompt": "Resolve exact ARMADA Type I and Type II boundaries, DefenseFinder HMM/rules coverage, profile-to-component mapping, direct phage triggers or outputs, and native host breadth before minting narrower ARMADA mechanism, subtype, or protein-component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ARMADA system",
  "source_id": "traitmech:000477",
  "source_file": "armada_system.yaml",
  "attaches_to": [
   "causal_graphs#armada_locus_phage_protection"
  ],
  "rationale": "Bell et al. support ARMADA as a broad YprA-like-helicase system family that shares BrxHII-like and PglX-like components with DISARM Class I systems and splits into Type I and Type II subclades, and the article experimentally validates Type II protection from E. coli NCTC 12900 and ATCC 8739 loci. The pinned DefenseFinder article registry names Armada and maps it to the Bell et al. preprint, but the pinned HMM inventory and rules table do not contain Armada rows, leaving profile coverage and detection criteria unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2026.05.015",
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC12458937/",
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC12458937/",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/armada_system.html#armada-subtype-model-and-mechanism-gap"
 },
 {
  "discussion_id": "audmula-mechanism-gap",
  "prompt": "Resolve Audmula phage triggers and effector outputs before minting narrower Audmula mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Audmula system",
  "source_id": "traitmech:000312",
  "source_file": "audmula_system.yaml",
  "attaches_to": [
   "causal_graphs#audmula_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al., Mosterd et al., and DefenseFinder support Audmula as a named anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/audmula_system.html#audmula-mechanism-gap"
 },
 {
  "discussion_id": "avast-subtype-effector-gap",
  "prompt": "Resolve AVAST subtype sensors, phage triggers, and effector outputs before minting narrower Avs1-Avs5 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "AVAST system",
  "source_id": "traitmech:000239",
  "source_file": "avast_system.yaml",
  "attaches_to": [],
  "rationale": "Gao et al. support phage-protein pattern recognition by Avs1 through Avs4, while Muralidharan et al. support Avs5 immunity against nucleus-forming jumbo phages through phage-triggered Sir2-like effector activation. The first TraitRecord therefore stays at the AVAST-system level until separate review resolves which phage cues, effector domains, and antiviral substrates generalize across AVAST loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avast_system.html#avast-subtype-effector-gap"
 },
 {
  "discussion_id": "avs-i-component-and-effector-gap",
  "prompt": "Resolve Avs1A, Avs1B, and Avs1C component roles, direct effector chemistry, exact phage-trigger mapping, native host breadth, and sensitive-phage breadth before minting Avs I mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Avs I system",
  "source_id": "traitmech:000534",
  "source_file": "avs_i_system.yaml",
  "attaches_to": [
   "causal_graphs#avs_i_locus_phage_protein_recognition"
  ],
  "rationale": "Gao et al. support Avs1 phage-protein recognition and Avs activation during antiviral defense, and the pinned DefenseFinder HMM inventory and rules table support Avs_I as a subtype I model with Avs1A, Avs1B, and Avs1C profiles. This first-pass record leaves the exact component functions, downstream effector chemistry, native host breadth, sensitive-phage breadth, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1126/science.abm4096",
   "DOI:10.1126/science.abm4096",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avs_i_system.html#avs-i-component-and-effector-gap"
 },
 {
  "discussion_id": "avs-ii-component-and-effector-gap",
  "prompt": "Resolve the Avs2A component role, direct effector chemistry, exact phage-trigger mapping, native host breadth, and sensitive-phage breadth before minting Avs II mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Avs II system",
  "source_id": "traitmech:000535",
  "source_file": "avs_ii_system.yaml",
  "attaches_to": [
   "causal_graphs#avs_ii_locus_phage_protein_recognition"
  ],
  "rationale": "Gao et al. support Avs2 phage-protein recognition and Avs activation during antiviral defense, and the pinned DefenseFinder HMM inventory and rules table support Avs_II as a subtype II model with an Avs2A profile. This first-pass record leaves the exact component role, downstream effector chemistry, native host breadth, sensitive-phage breadth, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.abm4096",
   "DOI:10.1126/science.abm4096",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avs_ii_system.html#avs-ii-component-and-effector-gap"
 },
 {
  "discussion_id": "avs-iii-component-and-effector-gap",
  "prompt": "Resolve the Avs3A and Avs3B component roles, direct effector chemistry, exact phage-trigger mapping, native host breadth, and sensitive-phage breadth before minting Avs III mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Avs III system",
  "source_id": "traitmech:000536",
  "source_file": "avs_iii_system.yaml",
  "attaches_to": [
   "causal_graphs#avs_iii_locus_phage_protein_recognition"
  ],
  "rationale": "Gao et al. support Avs3 phage-protein recognition and Avs activation during antiviral defense, and the pinned DefenseFinder HMM inventory and rules table support Avs_III as a subtype III model with Avs3A and Avs3B profiles. This first-pass record leaves the exact component roles, downstream effector chemistry, native host breadth, sensitive-phage breadth, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1126/science.abm4096",
   "DOI:10.1126/science.abm4096",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avs_iii_system.html#avs-iii-component-and-effector-gap"
 },
 {
  "discussion_id": "avs-iv-component-and-effector-gap",
  "prompt": "Resolve the Avs4A component role, direct effector chemistry, exact phage-trigger mapping, native host breadth, and sensitive-phage breadth before minting Avs IV mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Avs IV system",
  "source_id": "traitmech:000537",
  "source_file": "avs_iv_system.yaml",
  "attaches_to": [
   "causal_graphs#avs_iv_locus_phage_portal_recognition"
  ],
  "rationale": "Gao et al. support Avs4 phage-portal recognition and Avs activation during antiviral defense, and the pinned DefenseFinder HMM inventory and rules table support Avs_IV as a subtype IV model with an Avs4A profile. This first-pass record leaves the exact component role, downstream effector chemistry, native host breadth, sensitive-phage breadth, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.abm4096",
   "DOI:10.1126/science.abm4096",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avs_iv_system.html#avs-iv-component-and-effector-gap"
 },
 {
  "discussion_id": "avs-v-component-and-host-gap",
  "prompt": "Resolve the Avs5A component role, exact JADA trigger breadth, native host breadth, sensitive jumbo-phage breadth, and DefenseFinder profile-to-activity requirements before minting Avs V mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Avs V system",
  "source_id": "traitmech:000538",
  "source_file": "avs_v_system.yaml",
  "attaches_to": [
   "causal_graphs#avs_v_locus_sir2_effector_activation"
  ],
  "rationale": "Muralidharan et al. support Avs5 Sir2-like effector activation during jumbo-phage defense, and the pinned DefenseFinder HMM inventory and rules table support Avs_V as a subtype V model with an Avs5A profile. This first-pass record leaves the exact component role, JADA trigger breadth, native host breadth, sensitive jumbo-phage breadth, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.molcel.2026.01.004",
   "DOI:10.1016/j.molcel.2026.01.004",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/avs_v_system.html#avs-v-component-and-host-gap"
 },
 {
  "discussion_id": "azaca-mechanism-gap",
  "prompt": "Resolve Azaca phage triggers and effector outputs before minting narrower Azaca mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Azaca system",
  "source_id": "traitmech:000251",
  "source_file": "azaca_system.yaml",
  "attaches_to": [
   "causal_graphs#azaca_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Azaca as a named anti-phage system with ZacA, ZacB, and ZacC profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/azaca_system.html#azaca-mechanism-gap"
 },
 {
  "discussion_id": "belenos-mechanism-gap",
  "prompt": "Resolve Belenos phage triggers and effector outputs before minting narrower Belenos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Belenos system",
  "source_id": "traitmech:000268",
  "source_file": "belenos_system.yaml",
  "attaches_to": [
   "causal_graphs#belenos_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Belenos as a named anti-phage system with a VCA0457 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/belenos_system.html#belenos-mechanism-gap"
 },
 {
  "discussion_id": "belisama-mechanism-gap",
  "prompt": "Resolve Belisama phage triggers and effector outputs before minting narrower Belisama mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Belisama system",
  "source_id": "traitmech:000269",
  "source_file": "belisama_system.yaml",
  "attaches_to": [
   "causal_graphs#belisama_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Belisama as a named anti-phage system with a VCA0458 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/belisama_system.html#belisama-mechanism-gap"
 },
 {
  "discussion_id": "bil-defensefinder-profile-gap",
  "prompt": "Resolve Bil HMM profiles and rule rows before minting component-specific Bil mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Bil system",
  "source_id": "traitmech:000369",
  "source_file": "bil_system.yaml",
  "attaches_to": [
   "causal_graphs#bil_locus_impairs_phage_assembly"
  ],
  "rationale": "Hor et al. support Bil as a bacterial ubiquitin-like conjugation antiphage system that modifies the phage central tail fibre, and the pinned DefenseFinder article registry maps Bil to the Millman et al. discovery preprint. The same pinned HMM inventory and rules table do not include exact Bil rows, so the exact DefenseFinder profile set, component rule, and model coverage remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/bil_system.html#bil-defensefinder-profile-gap"
 },
 {
  "discussion_id": "borvo-mechanism-gap",
  "prompt": "Resolve Borvo phage triggers and effector outputs before minting narrower Borvo mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Borvo system",
  "source_id": "traitmech:000249",
  "source_file": "borvo_system.yaml",
  "attaches_to": [
   "causal_graphs#borvo_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Borvo as a named anti-phage system with BovA profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/borvo_system.html#borvo-mechanism-gap"
 },
 {
  "discussion_id": "brc113-defensefinder-model-gap",
  "prompt": "Resolve Brc113 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder article/HMM/rules coverage before minting narrower Brc113 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc113 system",
  "source_id": "traitmech:000522",
  "source_file": "brc113_system.yaml",
  "attaches_to": [
   "causal_graphs#brc113_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc113 as a bacteriophage-resistance integron cassette. The pinned DefenseFinder article registry, HMM inventory, and rules table have no exact gcu113 or Brc113 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc113_system.html#brc113-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc142-defensefinder-model-gap",
  "prompt": "Resolve Brc142 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower Brc142 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc142 system",
  "source_id": "traitmech:000515",
  "source_file": "brc142_system.yaml",
  "attaches_to": [
   "causal_graphs#brc142_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify gcu142/Brc142 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcu142 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcu142 or Brc142 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc142_system.html#brc142-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc167-defensefinder-model-gap",
  "prompt": "Resolve Brc167 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower Brc167 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc167 system",
  "source_id": "traitmech:000517",
  "source_file": "brc167_system.yaml",
  "attaches_to": [
   "causal_graphs#brc167_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc167 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcu167 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcu167 or Brc167 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc167_system.html#brc167-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc217-defensefinder-model-gap",
  "prompt": "Resolve Brc217 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder article/HMM/rules coverage before minting narrower Brc217 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc217 system",
  "source_id": "traitmech:000521",
  "source_file": "brc217_system.yaml",
  "attaches_to": [
   "causal_graphs#brc217_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc217 as a bacteriophage-resistance integron cassette. The pinned DefenseFinder article registry, HMM inventory, and rules table have no exact gcu217 or Brc217 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc217_system.html#brc217-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc22-defensefinder-model-gap",
  "prompt": "Resolve Brc22 native host breadth, exact sensitive-phage breadth, molecular output, Tragantia-family boundaries, and DefenseFinder article/HMM/rules coverage before minting narrower Brc22 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc22 system",
  "source_id": "traitmech:000523",
  "source_file": "brc22_system.yaml",
  "attaches_to": [
   "causal_graphs#brc22_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc22 as a bacteriophage-resistance integron cassette. The pinned DefenseFinder article registry, HMM inventory, and rules table have no exact gcu22 or Brc22 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, direct molecular output, and Brc22/Brc23 Tragantia-family scope unresolved.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc22_system.html#brc22-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc233-defensefinder-model-gap",
  "prompt": "Resolve Brc233 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower Brc233 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc233 system",
  "source_id": "traitmech:000518",
  "source_file": "brc233_system.yaml",
  "attaches_to": [
   "causal_graphs#brc233_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc233 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcu233 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcu233 or Brc233 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc233_system.html#brc233-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc23-defensefinder-model-gap",
  "prompt": "Resolve Brc23 native host breadth, exact sensitive-phage breadth, molecular output, Tragantia-family boundaries, and DefenseFinder article/HMM/rules coverage before minting narrower Brc23 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc23 system",
  "source_id": "traitmech:000524",
  "source_file": "brc23_system.yaml",
  "attaches_to": [
   "causal_graphs#brc23_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc23 as a bacteriophage-resistance integron cassette. The pinned DefenseFinder article registry, HMM inventory, and rules table have no exact gcu23 or Brc23 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, direct molecular output, and Brc22/Brc23 Tragantia-family scope unresolved.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc23_system.html#brc23-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc24-defensefinder-model-gap",
  "prompt": "Resolve Brc24 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower Brc24 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc24 system",
  "source_id": "traitmech:000516",
  "source_file": "brc24_system.yaml",
  "attaches_to": [
   "causal_graphs#brc24_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify gcu24/Brc24 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcu24 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcu24 or Brc24 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc24_system.html#brc24-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc59-defensefinder-model-gap",
  "prompt": "Resolve Brc59 native host breadth, exact sensitive-phage breadth, molecular output, normalized source-key naming, and DefenseFinder article/HMM/rules coverage before minting narrower Brc59 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc59 system",
  "source_id": "traitmech:000525",
  "source_file": "brc59_system.yaml",
  "attaches_to": [
   "causal_graphs#brc59_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc59 as a bacteriophage-resistance integron cassette. The pinned DefenseFinder article registry, HMM inventory, and rules table have no exact gcu59 or Brc59 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, direct molecular output, and normalized gcu59 source-key status unresolved.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://www.science.org/doi/suppl/10.1126/science.ads0915/suppl_file/science.ads0915_sm.pdf",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc59_system.html#brc59-defensefinder-model-gap"
 },
 {
  "discussion_id": "brc76-defensefinder-model-gap",
  "prompt": "Resolve Brc76 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower Brc76 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brc76 system",
  "source_id": "traitmech:000519",
  "source_file": "brc76_system.yaml",
  "attaches_to": [
   "causal_graphs#brc76_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brc76 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcu76 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcu76 or Brc76 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brc76_system.html#brc76-defensefinder-model-gap"
 },
 {
  "discussion_id": "brcwgs21-defensefinder-model-gap",
  "prompt": "Resolve BrcWGS21 native host breadth, exact sensitive-phage breadth, molecular output, and DefenseFinder HMM/rules coverage before minting narrower BrcWGS21 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "BrcWGS21 system",
  "source_id": "traitmech:000520",
  "source_file": "brcwgs21_system.yaml",
  "attaches_to": [
   "causal_graphs#brcwgs21_integron_cassette_confers_phage_resistance"
  ],
  "rationale": "Kieffer et al. identify brcWGS21 as a bacteriophage-resistance integron cassette, and the pinned DefenseFinder article registry maps the gcuWGS21 source key to the same Science article. The pinned HMM inventory and rules table have no exact gcuWGS21 or BrcWGS21 row, so the first-pass record leaves native-host breadth, profile boundaries, exact phage target breadth, and direct molecular output unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "DOI:10.1126/science.ads0915",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brcwgs21_system.html#brcwgs21-defensefinder-model-gap"
 },
 {
  "discussion_id": "brex-molecular-coupling-gap",
  "prompt": "Resolve the molecular coupling between BREX-guided host methylation and phage-DNA replication arrest before adding more specific BREX mechanism edges.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "BREX system",
  "source_id": "traitmech:000210",
  "source_file": "brex_system.yaml",
  "attaches_to": [],
  "rationale": "Goldfarb et al. showed that methylation is essential and that BREX blocks phage DNA replication after adsorption, but the exact biochemical coupling between the methylation mark and blocked phage replication remains insufficient for a more specific causal edge.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brex_system.html#brex-molecular-coupling-gap"
 },
 {
  "discussion_id": "brig1-natural-host-and-profile-gap",
  "prompt": "Resolve natural Brig1 host taxa, broader Brig1-family specificity, and the Brig1__ADP_ribosyl DefenseFinder profile before minting narrower Brig1 children, adding canonical examples, or curating the protein-resolved glycosylase mechanism.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brig1 system",
  "source_id": "traitmech:000307",
  "source_file": "brig1_system.yaml",
  "attaches_to": [
   "causal_graphs#brig1_locus_restricts_t_even_phages"
  ],
  "rationale": "Hallinan et al. functionally isolated the first brig1 gene from a soil metagenomic fragment rather than a sequenced natural isolate, and they showed that experimentally tested Brig1 homologues can protect against T-even phages. The first TraitRecord therefore covers Brig1-family antiphage DNA-glycosylase-system possession at locus level while leaving natural host exemplars, accession-level Brig1-family proteins, the protein-grounded glycosylase mechanism, the full sequence-level system architecture, and the relationship between the DefenseFinder Brig1__Brig1 and Brig1__ADP_ribosyl profiles to separate subtype review.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "DOI:10.1038/s41586-024-07329-9",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brig1_system.html#brig1-natural-host-and-profile-gap"
 },
 {
  "discussion_id": "brigantia-mechanism-gap",
  "prompt": "Resolve Brigantia phage triggers and effector outputs before minting narrower Brigantia mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Brigantia system",
  "source_id": "traitmech:000270",
  "source_file": "brigantia_system.yaml",
  "attaches_to": [
   "causal_graphs#brigantia_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Brigantia as a named anti-phage system with a VCA0419 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/brigantia_system.html#brigantia-mechanism-gap"
 },
 {
  "discussion_id": "bsta-mechanism-gap",
  "prompt": "Resolve the direct phage trigger of BstA localization, the direct DNA-replication target, the physical BstA-aba interaction, and the basis of cognate aba specificity before minting narrower BstA-aba mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "BstA system",
  "source_id": "traitmech:000301",
  "source_file": "bsta_system.yaml",
  "attaches_to": [
   "causal_graphs#bsta_locus_suppresses_phage_dna_replication"
  ],
  "rationale": "Owen et al. and DefenseFinder support BstA as a named abortive-infection system with a BstA HMM profile and a cognate aba self-immunity element, but the direct phage trigger that recruits BstA to phage DNA, the precise target by which BstA suppresses lytic phage DNA replication, the physical interaction between aba DNA and BstA, and the molecular basis of BstA-aba specificity remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/bsta_system.html#bsta-mechanism-gap"
 },
 {
  "discussion_id": "bunzi-mechanism-gap",
  "prompt": "Resolve Bunzi phage triggers and effector outputs before minting narrower Bunzi mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Bunzi system",
  "source_id": "traitmech:000248",
  "source_file": "bunzi_system.yaml",
  "attaches_to": [
   "causal_graphs#bunzi_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Bunzi as a named anti-phage system with BnzA and BnzB profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/bunzi_system.html#bunzi-mechanism-gap"
 },
 {
  "discussion_id": "butters_gp30_gp31-mechanism-gap",
  "prompt": "Resolve the Butters gp30 biochemical output, the gp31 modulatory role, the gp30-gp31 stoichiometry, the direct PurpleHaze or Alma trigger, the Island3 gp30-independent defense, and homolog breadth before minting narrower Butters gp30-gp31 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Butters gp30-gp31 system",
  "source_id": "traitmech:000298",
  "source_file": "butters_gp30_gp31_system.yaml",
  "attaches_to": [
   "causal_graphs#butters_gp30_gp31_locus_restricts_phage"
  ],
  "rationale": "Mageeney et al. and DefenseFinder support Butters gp30-gp31 as a named anti-phage system with Butters gp30 and gp31 profiles, but the direct phage trigger, gp30 biochemical output, gp31 modulatory activity, stoichiometry of the possible gp30-gp31 complex, gp30-independent Island3-targeting defense, and relationship to CarolAnn and Sbash homologous systems are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/butters_gp30_gp31_system.html#butters_gp30_gp31-mechanism-gap"
 },
 {
  "discussion_id": "butters_gp57r-mechanism-gap",
  "prompt": "Resolve the Butters gp57r direct phage trigger, primary molecular target, HEPN-associated RX4-6H motif requirement, DNA-amplification defect, PurpleHaze minor-tail escape route, and homolog breadth before minting narrower Butters gp57r mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Butters gp57r system",
  "source_id": "traitmech:000299",
  "source_file": "butters_gp57r_system.yaml",
  "attaches_to": [
   "causal_graphs#butters_gp57r_locus_restricts_phage"
  ],
  "rationale": "Mohammed et al. and DefenseFinder support Butters gp57r as a named anti-phage system with a gp57r profile, but the direct phage trigger, the biochemical role of its predicted HEPN domain and RX4-6H motif, the primary event leading to failed Island3 DNA amplification, and the defense scope of gp57r homologs in other mycobacteriophages or clinical Mycobacterium abscessus isolates are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/butters_gp57r_system.html#butters_gp57r-mechanism-gap"
 },
 {
  "discussion_id": "caprel-trigger-and-family-breadth-gap",
  "prompt": "Resolve CapRel trigger breadth, phage escape routes, and family-specific activation before minting narrower CapRel mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CapRel system",
  "source_id": "traitmech:000244",
  "source_file": "caprel_system.yaml",
  "attaches_to": [],
  "rationale": "Zhang et al. support CapRelSJ46 sensing of a major capsid protein and an unrelated Gp54 trigger, but fused CapRel homologs need separate review before TraitMech asserts one universal phage trigger, CapRel escape route, tRNA target spectrum, or phage specificity across the family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/caprel_system.html#caprel-trigger-and-family-breadth-gap"
 },
 {
  "discussion_id": "card-nlr-endonuclease-activity-gap",
  "prompt": "Resolve the CARD_NLR_Endonuclease phage triggers, native hosts, endonuclease effector substrate, CARD-to-effector activation sequence, and profile-to-activity criteria before minting enzyme, trigger, or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CARD-NLR endonuclease system",
  "source_id": "traitmech:000550",
  "source_file": "card_nlr_endonuclease_system.yaml",
  "attaches_to": [
   "causal_graphs#card_nlr_endonuclease_locus_subtype_defense"
  ],
  "rationale": "Wein et al. support CARD-like anti-phage defense systems, and the pinned DefenseFinder HMM inventory and rules table support CARD_NLR_Endonuclease as a subtype with a CARD_NLR__Endonuclease mandatory profile. This first-pass record leaves exact phage triggers, native hosts, accessory-profile requirements, nuclease substrate, and CARD-to-endonuclease activation unresolved.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "https://europepmc.org/article/PPR/PPR668921",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/card_nlr_endonuclease_system.html#card-nlr-endonuclease-activity-gap"
 },
 {
  "discussion_id": "card-nlr-phospho-activity-gap",
  "prompt": "Resolve the CARD_NLR_Phospho phage triggers, native hosts, phosphorylated substrate, CARD-to-effector activation sequence, and profile-to-activity criteria before minting enzyme, trigger, or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CARD-NLR phospho system",
  "source_id": "traitmech:000551",
  "source_file": "card_nlr_phospho_system.yaml",
  "attaches_to": [
   "causal_graphs#card_nlr_phospho_locus_subtype_defense"
  ],
  "rationale": "Wein et al. support CARD-like anti-phage defense systems, and the pinned DefenseFinder HMM inventory and rules table support CARD_NLR_Phospho as a subtype with a CARD_NLR__Trypsin_Phospho mandatory profile. This first-pass record leaves exact phage triggers, native hosts, accessory-profile requirements, phosphorylated substrate, and CARD-to-phospho-effector activation unresolved.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "https://europepmc.org/article/PPR/PPR668921",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/card_nlr_phospho_system.html#card-nlr-phospho-activity-gap"
 },
 {
  "discussion_id": "card-nlr-subtype-mechanism-gap",
  "prompt": "Resolve CARD-NLR subtype effectors, phage triggers, natural-host examples, and GasderMIN subtype boundaries before minting narrower CARD-NLR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CARD-NLR system",
  "source_id": "traitmech:000337",
  "source_file": "card_nlr_system.yaml",
  "attaches_to": [
   "causal_graphs#card_nlr_loci_activate_cell_death_effectors"
  ],
  "rationale": "Wein et al. support CARD-like domains in multiple anti-phage defense systems that activate cell-death effectors, and DefenseFinder models CARD_NLR subtypes with gasdermin, endonuclease, CARD_NLR_Phospho, and Subtilase effector profiles. This first system-level record leaves the exact phage triggers, CARD-to-effector activation sequence, accession-level natural-host components, and boundaries between standalone GasderMIN and CARD_NLR_GasderMIN contexts unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/card_nlr_system.html#card-nlr-subtype-mechanism-gap"
 },
 {
  "discussion_id": "cbass-subtype-mechanism-gap",
  "prompt": "Resolve CBASS subtype-specific sensing and effector mechanisms before splitting cGAMP-phospholipase, cAAA-nuclease, ancillary-gene, or individual CD-NTase protein-family edges into reviewed graph groundings.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CBASS system",
  "source_id": "traitmech:000212",
  "source_file": "cbass_system.yaml",
  "attaches_to": [],
  "rationale": "Cohen et al. resolved a phage-triggered cGAMP-phospholipase CBASS system and Millman et al. classified CBASS loci into four major types with multiple signaling molecules, effectors, and ancillary genes; exact phage sensors and subtype-specific effector families remain shifted from this first organism-level trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/cbass_system.html#cbass-subtype-mechanism-gap"
 },
 {
  "discussion_id": "ceres-mechanism-gap",
  "prompt": "Resolve Ceres phage triggers and effector outputs before minting narrower Ceres mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ceres system",
  "source_id": "traitmech:000288",
  "source_file": "ceres_system.yaml",
  "attaches_to": [
   "causal_graphs#ceres_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Ceres as a named anti-phage system with CrsA1 and CrsA2 HMM profile entries, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ceres_system.html#ceres-mechanism-gap"
 },
 {
  "discussion_id": "cernunnos-mechanism-gap",
  "prompt": "Resolve Cernunnos phage triggers and effector outputs before minting narrower Cernunnos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Cernunnos system",
  "source_id": "traitmech:000271",
  "source_file": "cernunnos_system.yaml",
  "attaches_to": [
   "causal_graphs#cernunnos_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Cernunnos as a named anti-phage system with a VCA0410 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/cernunnos_system.html#cernunnos-mechanism-gap"
 },
 {
  "discussion_id": "charlie_gp32-mechanism-gap",
  "prompt": "Resolve the Charlie gp32 membrane target, Che9c specificity, and homolog breadth before minting narrower Charlie gp32 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Charlie gp32 system",
  "source_id": "traitmech:000295",
  "source_file": "charlie_gp32_system.yaml",
  "attaches_to": [
   "causal_graphs#charlie_gp32_locus_blocks_phage_entry"
  ],
  "rationale": "Dedrick et al. and DefenseFinder support Charlie gp32 as a named anti-phage system with a gp32 profile, but the direct membrane target, determinants of its Che9c specificity, and breadth of homologous loci are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/charlie_gp32_system.html#charlie_gp32-mechanism-gap"
 },
 {
  "discussion_id": "clover-defensefinder-model-gap",
  "prompt": "Resolve Clover native host breadth, sensitive-phage breadth, profile-to-component coverage, and DefenseFinder HMM/rules coverage before minting narrower Clover mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Clover system",
  "source_id": "traitmech:000415",
  "source_file": "clover_system.yaml",
  "attaches_to": [
   "causal_graphs#clover_dttp_p3dit_regulated_dgtpase"
  ],
  "rationale": "Yu and Kranzusch support Clover as a bacterial anti-phage defence system whose CloA dGTPase is activated and suppressed by nucleotide signals, while the pinned DefenseFinder article registry names a Clover system. The pinned DefenseFinder HMM inventory and rules table have no Clover rows, and the evidence does not yet resolve native host breadth, full target-phage breadth, or profile-to-activity modeling.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41586-026-10135-0",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/clover_system.html#clover-defensefinder-model-gap"
 },
 {
  "discussion_id": "cmdtac-family-and-model-coverage-gap",
  "prompt": "Resolve CmdTAC family breadth and phage escape routes before minting narrower CmdTAC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CmdTAC system",
  "source_id": "traitmech:000335",
  "source_file": "cmdtac_system.yaml",
  "attaches_to": [
   "causal_graphs#cmdtac_mrna_adp_ribosylation_aborts_phage"
  ],
  "rationale": "Vassallo et al. support CmdTAC as a toxin-antitoxin-chaperone abortive-infection system in which CmdC senses viral capsid proteins and liberates the CmdT mRNA ADP-ribosyltransferase. Vassallo et al. also state that PD-T4-9 was renamed CmdTAC, and the pinned DefenseFinder HMM inventory and rules table record PD-T4-9 with required PD-T4-9__PD-T4-9_A and PD-T4-9__PD-T4-9_C profiles plus accessory PD-T4-9__PD-T4-9_B. Phage specificity beyond Tevenvirinae, escape routes, and natural family breadth remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41586-024-08102-8",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-9.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-9.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/cmdtac_system.html#cmdtac-family-and-model-coverage-gap"
 },
 {
  "discussion_id": "coconut-defensefinder-model-gap",
  "prompt": "Resolve exact CoCoNuT type and subtype boundaries, native host breadth, direct RNA and DNA substrates, phage range, pseudo-CoCoNuT scope, CARF-regulated superoperon scope, and rule-level detection criteria before minting narrower CoCoNuT mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "CoCoNuT system",
  "source_id": "traitmech:000422",
  "source_file": "coconut_system.yaml",
  "attaches_to": [
   "causal_graphs#coconut_system_family_hierarchy"
  ],
  "rationale": "Bell et al. support CoCoNuTs as a computationally defined McrBC/Type IV restriction branch predicted to target RNA and, for many loci, DNA; the pinned DefenseFinder HMM inventory records custom CoCoNut-I, CoCoNut-II, and CoCoNut-III profile rows. The pinned rules table has no CoCoNut row, and the first-pass record leaves exact profile-to-protein boundaries, pseudo-CoCoNuT inclusion, natural host breadth, phage range, and substrate-level mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.7554/eLife.94800.3",
   "DOI:10.7554/eLife.94800.3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/coconut_system.html#coconut-defensefinder-model-gap"
 },
 {
  "discussion_id": "crouga-mechanism-and-modelling-gap",
  "prompt": "Resolve Crouga locus breadth, exact phage triggers, restriction-modification-like molecular roles, direct antiviral output, source-system table rows, and DefenseFinder HMM/rule coverage before minting narrower Crouga mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Crouga system",
  "source_id": "traitmech:000500",
  "source_file": "crouga_system.yaml",
  "attaches_to": [
   "causal_graphs#crouga_locus_restricts_phage"
  ],
  "rationale": "de Sousa et al. support Crouga as one of the novel P4-encoded systems with experimental phage-protection activity, and the pinned DefenseFinder article registry maps the Crouga source key to the corresponding preprint. The pinned HMM inventory and rules table have no exact Crouga rows, and this first-pass record does not resolve the tested source locus, complete phage breadth, exact trigger, molecular output, or detection rule.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1093/nar/gkag898",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/crouga_system.html#crouga-mechanism-and-modelling-gap"
 },
 {
  "discussion_id": "dag-defensefinder-profile-gap",
  "prompt": "Resolve exact Dag1 and Dag2 family boundaries, natural host exemplars, modified-guanine phage target breadth, and DefenseFinder HMM/rules coverage before minting narrower Dag mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dag system",
  "source_id": "traitmech:000507",
  "source_file": "dag_system.yaml",
  "attaches_to": [
   "causal_graphs#dag_effectors_target_modified_guanine_phages"
  ],
  "rationale": "Getz et al. support Dag1 and Dag2 as widespread families of anti-phage DNA glycosylases that selectively target phages carrying modified guanine bases, and the pinned DefenseFinder article registry maps the Dag key to the Getz et al. preprint DOI. The pinned HMM inventory and rules table have no exact Dag rows. This first-pass record therefore does not resolve exact Dag1 versus Dag2 family boundaries, natural host exemplars, accession-level Dag proteins, full modified-guanine phage target breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02441-0",
   "DOI:10.1038/s41564-026-02441-0",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dag_system.html#dag-defensefinder-profile-gap"
 },
 {
  "discussion_id": "damona-mechanism-gap",
  "prompt": "Resolve Damona phage triggers and effector outputs before minting narrower Damona mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Damona system",
  "source_id": "traitmech:000272",
  "source_file": "damona_system.yaml",
  "attaches_to": [
   "causal_graphs#damona_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Damona as a named anti-phage system with a VCA0399 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/damona_system.html#damona-mechanism-gap"
 },
 {
  "discussion_id": "darna-model-profile-gap",
  "prompt": "Resolve DARNA component profiles and locus architecture before minting component-profile synonyms or narrower DARNA subsystem traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DARNA system",
  "source_id": "traitmech:000273",
  "source_file": "darna_system.yaml",
  "attaches_to": [
   "causal_graphs#darna_phage_ssb_ssdna_cleaves_trna"
  ],
  "rationale": "Puteikiene et al. support DARNA as an anti-phage system with a resolved phage-SSB single-stranded-DNA trigger and host-tRNA cleavage output, and DefenseFinder lists DARNA in its article registry. The pinned DefenseFinder snapshot does not yet expose DARNA HMM or rule rows, so this first record does not assert a component-profile synonym or universal locus architecture.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/darna_system.html#darna-model-profile-gap"
 },
 {
  "discussion_id": "dazbog-mechanism-gap",
  "prompt": "Resolve Dazbog phage triggers and effector outputs before minting narrower Dazbog mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dazbog system",
  "source_id": "traitmech:000245",
  "source_file": "dazbog_system.yaml",
  "attaches_to": [],
  "rationale": "Millman et al. and DefenseFinder support Dazbog as a named DzbA/DzbB anti-phage locus, but the trigger, molecular substrate, antiviral effector output, and death-or-survival phenotype are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dazbog_system.html#dazbog-mechanism-gap"
 },
 {
  "discussion_id": "dctpdeaminase-activation-profile-gap",
  "prompt": "Resolve dCTPdeaminase activation, locus boundaries, and representative enzyme accessions before asserting narrower component or subtype traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "dCTPdeaminase system",
  "source_id": "traitmech:000274",
  "source_file": "dctpdeaminase_system.yaml",
  "attaches_to": [
   "causal_graphs#dctpdeaminase_dctp_depletion_defense"
  ],
  "rationale": "Tal et al. support dCTPdeaminase as a phage-responsive dCTP-depletion defense and DefenseFinder models the system with a custom dCTPdeaminase HMM profile, but this first system-level record does not resolve the universal phage sensor, activation route, strain-level accessions, or whether additional unmodeled components define some natural loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dctpdeaminase_system.html#dctpdeaminase-activation-profile-gap"
 },
 {
  "discussion_id": "ddmde-substrate-and-guide-source-gap",
  "prompt": "Resolve DdmDE natural guide sources, plasmid-substrate breadth, and DdmABC cooperation before minting narrower DdmDE mechanism or subtype traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DdmDE system",
  "source_id": "traitmech:000275",
  "source_file": "ddmde_system.yaml",
  "attaches_to": [
   "causal_graphs#ddmde_pago_helicase_plasmid_destruction"
  ],
  "rationale": "Jaskolska et al. support DdmDE as a V. cholerae plasmid-defense system and Bravo et al. resolve how DdmE and DdmD cooperate for plasmid destruction, but this first system-level record does not assert a universal guide-maturation route, full natural plasmid substrate range, or whether cooperation with DdmABC is required in some hosts.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ddmde_system.html#ddmde-substrate-and-guide-source-gap"
 },
 {
  "discussion_id": "detocs-component-mechanism-gap",
  "prompt": "Resolve Detocs phage triggers, component-specific phosphotransfer events, and DtcC-family effector outputs before minting narrower Detocs mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Detocs system",
  "source_id": "traitmech:000302",
  "source_file": "detocs_system.yaml",
  "attaches_to": [
   "causal_graphs#detocs_locus_depletes_atp"
  ],
  "rationale": "Rousset et al. support Detocs as a named family of two-component phosphotransfer-signaling bacterial defense systems, and DefenseFinder represents Detocs with required dtcA and dtcB profiles plus optional dtcC-family profiles. This system-level record leaves the direct phage trigger, component-specific activation route, exact ATP nucleosidase effector architecture, and DtcC-variant outputs unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/detocs_system.html#detocs-component-mechanism-gap"
 },
 {
  "discussion_id": "dgtpase-activation-profile-gap",
  "prompt": "Resolve dGTPase activation, locus boundaries, and representative enzyme accessions before asserting narrower component or subtype traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "dGTPase system",
  "source_id": "traitmech:000276",
  "source_file": "dgtpase_system.yaml",
  "attaches_to": [
   "causal_graphs#dgtpase_dgtp_depletion_defense"
  ],
  "rationale": "Tal et al. support dGTPase as a phage-responsive dGTP-depletion defense and DefenseFinder models the system with a custom Sp_dGTPase HMM profile, but this first system-level record does not resolve the universal phage sensor, activation route, strain-level accessions, or whether additional unmodeled components define some natural loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dgtpase_system.html#dgtpase-activation-profile-gap"
 },
 {
  "discussion_id": "dionysus-jumbo-phage-mechanism-gap",
  "prompt": "Resolve Dionysus phage triggers, EPI-vesicle pore formation, and model coverage before minting narrower Dionysus mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dionysus system",
  "source_id": "traitmech:000330",
  "source_file": "dionysus_system.yaml",
  "attaches_to": [
   "causal_graphs#dionysus_locus_restricts_phage"
  ],
  "rationale": "Keesman et al. support Dionysus as a three-gene anti-jumbo-phage system that disrupts the jumbo-phage EPI vesicle stage, but the direct phage trigger, exact DinA/DinB/DinC interaction sequence, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dionysus_system.html#dionysus-jumbo-phage-mechanism-gap"
 },
 {
  "discussion_id": "disarm1-profile-activity-gap",
  "prompt": "Resolve DISARM1 effector chemistry, exact native hosts, sensitive-phage breadth, shared-core component roles, and DISARM_1 profile-to-activity criteria before minting DISARM1 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DISARM1 system",
  "source_id": "traitmech:000548",
  "source_file": "disarm1_system.yaml",
  "attaches_to": [
   "causal_graphs#disarm1_locus_subtype_defense"
  ],
  "rationale": "Ofir et al. support DISARM as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DISARM_1 as a subtype with drmD, drmMI, drmA, drmB, and drmC profiles. This first-pass record leaves exact DISARM1 effector chemistry, native host breadth, sensitive-phage breadth, shared-core component roles, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "DOI:10.1038/s41564-017-0051-0",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/disarm1_system.html#disarm1-profile-activity-gap"
 },
 {
  "discussion_id": "disarm2-profile-activity-gap",
  "prompt": "Resolve DISARM2 effector chemistry, exact native hosts, sensitive-phage breadth, shared-core component roles, and DISARM_2 profile-to-activity criteria before minting DISARM2 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DISARM2 system",
  "source_id": "traitmech:000549",
  "source_file": "disarm2_system.yaml",
  "attaches_to": [
   "causal_graphs#disarm2_locus_subtype_defense"
  ],
  "rationale": "Ofir et al. support DISARM as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DISARM_2 as a subtype with drmE, drmMII, drmA, drmB, and drmC profiles. This first-pass record leaves exact DISARM2 effector chemistry, native host breadth, sensitive-phage breadth, shared-core component roles, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "DOI:10.1038/s41564-017-0051-0",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/disarm2_system.html#disarm2-profile-activity-gap"
 },
 {
  "discussion_id": "disarm-downstream-effector-gap",
  "prompt": "Resolve the downstream nuclease or replication-blocking effector coupled to activated DrmAB before adding a more specific DISARM phage-DNA degradation edge.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DISARM system",
  "source_id": "traitmech:000211",
  "source_file": "disarm_system.yaml",
  "attaches_to": [],
  "rationale": "Ofir et al. inferred phage DNA degradation and showed that DrmC is partially redundant across phages; Bravo et al. resolved DrmAB recognition and activation but left the downstream nuclease or physical replication block as a model.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/disarm_system.html#disarm-downstream-effector-gap"
 },
 {
  "discussion_id": "divona-mechanism-gap",
  "prompt": "Resolve Divona phage triggers and effector outputs before minting narrower Divona mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Divona system",
  "source_id": "traitmech:000277",
  "source_file": "divona_system.yaml",
  "attaches_to": [
   "causal_graphs#divona_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Divona as a named anti-phage system with a VCA0374 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/divona_system.html#divona-mechanism-gap"
 },
 {
  "discussion_id": "dodola-mechanism-gap",
  "prompt": "Resolve Dodola phage triggers and effector outputs before minting narrower Dodola mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dodola system",
  "source_id": "traitmech:000252",
  "source_file": "dodola_system.yaml",
  "attaches_to": [
   "causal_graphs#dodola_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Dodola as a named anti-phage system with DolA and DolB profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dodola_system.html#dodola-mechanism-gap"
 },
 {
  "discussion_id": "dpd-restriction-mechanism-gap",
  "prompt": "Resolve Dpd restriction targets, phage specificity, and DpdA-K component functions before minting narrower Dpd mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dpd system",
  "source_id": "traitmech:000278",
  "source_file": "dpd_system.yaml",
  "attaches_to": [
   "causal_graphs#dpd_dna_modification_defense"
  ],
  "rationale": "Thiaville et al. support dpdA-K-dependent installation of 7-deazaguanine derivatives into DNA and a likely restriction-modification role, and DefenseFinder supports Dpd as a named multi-profile defense model. This first record does not yet resolve the universal restriction target, modified motif, antiphage substrate breadth, or the necessity of each profiled component across natural Dpd loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dpd_system.html#dpd-restriction-mechanism-gap"
 },
 {
  "discussion_id": "drt1-profile-activity-gap",
  "prompt": "Resolve the DRT1 reverse-transcriptase products, direct phage trigger, host breadth, partner-feature requirements, and DRT_1__drt1a/DRT_1__drt1b profile-to-activity criteria before minting DRT1 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT1 system",
  "source_id": "traitmech:000543",
  "source_file": "drt1_system.yaml",
  "attaches_to": [
   "causal_graphs#drt1_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT_1 as a DRT subsystem with two mandatory profiles. This first-pass record leaves the exact DRT1 RT products, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt1_system.html#drt1-profile-activity-gap"
 },
 {
  "discussion_id": "drt2-profile-activity-gap",
  "prompt": "Resolve the DRT2 reverse-transcriptase product, direct phage trigger, host breadth, partner-feature requirements, and DRT_2 profile-to-activity criteria before minting DRT2 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT2 system",
  "source_id": "traitmech:000544",
  "source_file": "drt2_system.yaml",
  "attaches_to": [
   "causal_graphs#drt2_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT_2 as a single-profile DRT subsystem. This first-pass record leaves the exact DRT2 RT product, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt2_system.html#drt2-profile-activity-gap"
 },
 {
  "discussion_id": "drt3-profile-activity-gap",
  "prompt": "Resolve the DRT3 reverse-transcriptase products, direct phage trigger, host breadth, non-coding RNA or DRT_3__SLATT partner-feature role, and DRT_3 profile-to-activity criteria before minting DRT3 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT3 system",
  "source_id": "traitmech:000545",
  "source_file": "drt3_system.yaml",
  "attaches_to": [
   "causal_graphs#drt3_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family and the two RT components of DRT type 3, while the pinned DefenseFinder HMM inventory and rules table support DRT_3 as a two-required-profile DRT subsystem. This first-pass record leaves the exact DRT3 RT products, phage trigger, host breadth, DRT_3__SLATT role, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt3_system.html#drt3-profile-activity-gap"
 },
 {
  "discussion_id": "drt4-profile-activity-gap",
  "prompt": "Resolve the DRT4 reverse-transcriptase product, direct phage trigger, host breadth, partner-feature requirements, and DRT_4 profile-to-activity criteria before minting DRT4 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT4 system",
  "source_id": "traitmech:000546",
  "source_file": "drt4_system.yaml",
  "attaches_to": [
   "causal_graphs#drt4_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT_4 as a single-profile DRT subsystem. This first-pass record leaves the exact DRT4 RT product, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt4_system.html#drt4-profile-activity-gap"
 },
 {
  "discussion_id": "drt5-profile-activity-gap",
  "prompt": "Resolve the DRT5 reverse-transcriptase product, direct phage trigger, host breadth, partner-feature requirements, and DRT_5 profile-to-activity criteria before minting DRT5 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT5 system",
  "source_id": "traitmech:000547",
  "source_file": "drt5_system.yaml",
  "attaches_to": [
   "causal_graphs#drt5_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT_5 as a single-profile DRT subsystem. This first-pass record leaves the exact DRT5 RT product, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt5_system.html#drt5-profile-activity-gap"
 },
 {
  "discussion_id": "drt6-profile-activity-gap",
  "prompt": "Resolve the DRT6 reverse-transcriptase product, direct phage trigger, host breadth, partner-feature requirements, and DefenseFinder profile-to-activity criteria before minting DRT6 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT6 system",
  "source_id": "traitmech:000539",
  "source_file": "drt6_system.yaml",
  "attaches_to": [
   "causal_graphs#drt6_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT6 as a single-profile DRT subsystem. This first-pass record leaves the exact DRT6 RT product, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt6_system.html#drt6-profile-activity-gap"
 },
 {
  "discussion_id": "drt7-profile-activity-gap",
  "prompt": "Resolve the DRT7 reverse-transcriptase product, direct phage trigger, host breadth, partner-feature requirements, and DRT7__DRT7 versus DRT7__DRT7_small profile-to-activity criteria before minting DRT7 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT7 system",
  "source_id": "traitmech:000540",
  "source_file": "drt7_system.yaml",
  "attaches_to": [
   "causal_graphs#drt7_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT7 as a DRT subsystem with two alternative profiles. This first-pass record leaves the exact DRT7 RT product, phage trigger, host breadth, partner-feature requirements, and profile-to-activity requirements unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt7_system.html#drt7-profile-activity-gap"
 },
 {
  "discussion_id": "drt8-profile-activity-gap",
  "prompt": "Resolve the DRT8 reverse-transcriptase product, direct phage trigger, host breadth, DRT8__DRT8b accessory role, and DRT8__DRT8a HMM-row status before minting DRT8 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT8 system",
  "source_id": "traitmech:000541",
  "source_file": "drt8_system.yaml",
  "attaches_to": [
   "causal_graphs#drt8_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT8 as a DRT subsystem with a mandatory DRT8__DRT8 profile and an accessory DRT8__DRT8b profile. This first-pass record leaves the exact DRT8 RT product, phage trigger, host breadth, DRT8__DRT8b accessory role, and DRT8__DRT8a inventory-row status unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt8_system.html#drt8-profile-activity-gap"
 },
 {
  "discussion_id": "drt9-profile-activity-gap",
  "prompt": "Resolve the DRT9 reverse-transcriptase product, direct phage trigger, host breadth, and DRT9__SLATT HMM-row status before minting DRT9 mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT9 system",
  "source_id": "traitmech:000542",
  "source_file": "drt9_system.yaml",
  "attaches_to": [
   "causal_graphs#drt9_locus_reverse_transcriptase_defense"
  ],
  "rationale": "Gao et al. support defense-associated reverse transcriptases as a broad antiphage-system family, and the pinned DefenseFinder HMM inventory and rules table support DRT9 as a DRT subsystem with a mandatory DRT9__DRT9 profile. This first-pass record leaves the exact DRT9 RT product, phage trigger, host breadth, and DRT9__SLATT inventory-row status unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1126/science.aba0372",
   "DOI:10.1126/science.aba0372",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt9_system.html#drt9-profile-activity-gap"
 },
 {
  "discussion_id": "drt-subtype-mechanism-gap",
  "prompt": "Resolve DRT subtype products, partner RNAs or proteins, phage triggers, and antiphage substrates before minting narrower DRT subtype mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DRT system",
  "source_id": "traitmech:000279",
  "source_file": "drt_system.yaml",
  "attaches_to": [
   "causal_graphs#drt_reverse_transcriptase_antiphage_defense"
  ],
  "rationale": "Gao et al. support several active reverse-transcriptase-containing antiphage systems, and DefenseFinder models DRT subtypes such as DRT_1. This first record stays at DRT-family level because the direct products of DRT RT activity, the exact phage triggers, the non-coding RNA role in DRT type 3, and the mechanisms for additional DRT subtypes are not resolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/drt_system.html#drt-subtype-mechanism-gap"
 },
 {
  "discussion_id": "druantia-subtype-mechanism-gap",
  "prompt": "Resolve Druantia subtype composition and activation mechanisms before minting narrower Type I, Type II, or Type III Druantia-system children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Druantia system",
  "source_id": "traitmech:000234",
  "source_file": "druantia_system.yaml",
  "attaches_to": [],
  "rationale": "Doron et al. separated Type I DruABCDE, Type II DruMFGE, and Type III DruHE architectures and validated one Type I locus, while Wu et al. define a Type III mechanism in which DruH likely senses infection and DruE engages ssDNA-containing intermediates. The first TraitRecord therefore stays at the DruE-core family level until separate review resolves Type I/II partner functions, Type III-specific DruH activation, exact phage triggers, and Zorya-coupled versus standalone outputs across Druantia loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/druantia_system.html#druantia-subtype-mechanism-gap"
 },
 {
  "discussion_id": "ds-10-defensefinder-model-gap",
  "prompt": "Resolve DS-10 native host breadth, exact DS-10 component function, sensitive-phage breadth, molecular output, HHPred domain support, per-phage Table S7 readouts, and rule-level detection criteria before minting narrower DS-10 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-10 system",
  "source_id": "traitmech:000434",
  "source_file": "ds_10_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_10_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-10 as the defensive ZAPB transcriptional unit that reduced plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records one DS-10 profile row. The final Table S7 and HHPred-domain sheets have no ZAPB rows, the pinned rules table has no DS-10 row, and the first-pass record does not resolve native host breadth, exact component activity, phage target breadth, the direct molecular output, or endogenous DS-10 activity.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_10_system.html#ds-10-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-11-defensefinder-model-gap",
  "prompt": "Resolve DS-11 native host breadth, profile-to-protein mapping, sensitive-phage breadth, direct viral trigger, direct HEPN-family nuclease substrate, CBS-ligand or ATP-dependent activation model, and rule-level detection criteria before minting narrower DS-11 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-11 system",
  "source_id": "traitmech:000435",
  "source_file": "ds_11_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_11_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-11 as the defensive IMPD transcriptional unit that reduced T3 and Bas67 plaquing when cloned in E. coli MG1655, and the final Table S8 HHpred sheet reports HEPN and CBS hits for the single IMPD product. The pinned DefenseFinder HMM inventory records one DS-11 profile row, the pinned rules table has no DS-11 row, and the first-pass record does not resolve native host breadth, exact profile-to-protein correspondence, the direct HEPN substrate, the activation ligand, phage target breadth, or endogenous DS-11 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_11_system.html#ds-11-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-12-defensefinder-model-gap",
  "prompt": "Resolve DS-12 native host breadth, DS-12A model coverage, DS-12B profile-to-protein mapping, sensitive-phage breadth, direct viral trigger or substrate, exact ABC ATPase and PDDEXK/nSTAND nuclease chemistry, and rule-level detection criteria before minting narrower DS-12 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-12 system",
  "source_id": "traitmech:000436",
  "source_file": "ds_12_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_12_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-12 as the defensive PD3A transcriptional unit that reduced Bas25 plaquing when cloned in E. coli MG1655, and the final Table S8 HHpred sheet reports ABC ATPase, PDDEXK, and NACHT hits across the two PD3A products. The pinned DefenseFinder HMM inventory records one DS-12B profile row, the pinned article registry names DS-12B rather than DS-12, the pinned rules table has no DS-12 row, and the first-pass record does not resolve native host breadth, DS-12A model coverage, exact profile-to-protein correspondence, direct ATPase or nuclease activity, phage target breadth, or endogenous DS-12 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_12_system.html#ds-12-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-13-defensefinder-model-gap",
  "prompt": "Resolve DS-13 working-identifier rows, preprint Table S5 and S6 context, final Science supplement omission, native host breadth, DS-13A/DS-13B profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-13 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-13 system",
  "source_id": "traitmech:000437",
  "source_file": "ds_13_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_13_locus_profile_model"
  ],
  "rationale": "The DeWeirdt et al. preprint supports the DefensePredictor discovered System naming convention, the pinned DefenseFinder article registry names DS-13 and maps it to that preprint, and the pinned HMM inventory records DS-13A and DS-13B custom profile rows. DS-13 is absent from the final Science Table S6, S7, and S8 files checked during this curation pass, the exact preprint per-TU rows were not recovered, the pinned DefenseFinder rules table has no DS-13 row, and the first-pass record does not resolve the working identifier, assayed phages, phage readout, native host, profile-to-component mapping, component activities, or complete detection criteria.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_13_system.html#ds-13-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-14-defensefinder-model-gap",
  "prompt": "Resolve DS-14 native host breadth, exact single-component activity, DS-14 remote-defense-homolog family identity, DS-14 profile-to-protein mapping, sensitive-phage breadth, exact AAA+ ATPase and PDDEXK nuclease chemistry, and rule-level detection criteria before minting narrower DS-14 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-14 system",
  "source_id": "traitmech:000429",
  "source_file": "ds_14_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_14_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-14 as the defensive RMOR transcriptional unit that reduced Bas50 plaquing when cloned in E. coli MG1655, the final Table S6 classes RMOR as a Remote defense homolog, and the pinned DefenseFinder HMM inventory records one DS-14 profile row. The pinned rules table has no DS-14 row, and the first-pass record does not resolve native host breadth, exact component activity, remote defense family relationship, profile-to-protein mapping, phage target breadth, or endogenous DS-14 activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_14_system.html#ds-14-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-15-defensefinder-model-gap",
  "prompt": "Resolve DS-15 native host breadth, exact profile-to-protein mapping, DS-15A/DS-15B/DS-15C component activities, sensitive-phage breadth, exact AAA family ATPase and DUF6988 chemistry, and rule-level DefenseFinder criteria before minting narrower DS-15 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-15 system",
  "source_id": "traitmech:000438",
  "source_file": "ds_15_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_15_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-15 as the defensive AAA1 transcriptional unit that reduced Bas1 plaquing when cloned in E. coli MG1655, the final Table S8 HHpred sheet reports MinD ATPase and DUF6988 hits across two AAA1 products, and the pinned DefenseFinder HMM inventory records DS-15A, DS-15B, and DS-15C custom profile rows. The pinned rules table has no DS-15 row, and the first-pass record does not resolve native host breadth, exact profile-to-protein correspondence, direct ATPase or DUF6988 activity, phage target breadth, or endogenous DS-15 activity.",
  "num_experiments": 0,
  "num_evidence": 12,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_15_system.html#ds-15-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-16-defensefinder-model-gap",
  "prompt": "Resolve DS-16 native host breadth, exact profile-to-protein mapping, DS-16A/DS-16B component activities, RelE and ABC ATPase chemistry, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-16 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-16 system",
  "source_id": "traitmech:000439",
  "source_file": "ds_16_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_16_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-16 as the defensive PLIK transcriptional unit and final Science Tables S6/S7/S8 map it to product accessions WP_001676492.1 and WP_001676491.1, Bas26 and T4 phage readouts, display name DS-16, and RelE/ABC ATPase HHpred rows. The pinned DefenseFinder HMM inventory records DS-16A and DS-16B custom profile rows. The pinned rules table has no DS-16 row, and the first-pass record does not resolve native host breadth, phage breadth, direct profile-to-protein correspondence, RelE nuclease or ABC ATPase activity, molecular output, or endogenous DS-16 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_16_system.html#ds-16-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-17-defensefinder-model-gap",
  "prompt": "Resolve DS-17 native host breadth, exact profile-to-protein mapping, component chemistry, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-17 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-17 system",
  "source_id": "traitmech:000440",
  "source_file": "ds_17_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_17_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-17 as the defensive NUCS transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_001240354.1, a T4 phage readout, display name DS-17, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-17 custom profile row. The pinned rules table has no DS-17 row, and the first-pass record does not resolve native host breadth, phage breadth, direct profile-to-protein correspondence, PDDEXK nuclease activity, molecular output, or endogenous DS-17 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_17_system.html#ds-17-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-18-defensefinder-model-gap",
  "prompt": "Resolve DS-18 native host breadth, exact profile-to-protein mapping, component chemistry, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-18 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-18 system",
  "source_id": "traitmech:000441",
  "source_file": "ds_18_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_18_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-18 as the defensive 6602 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_021529611.1, a Candy phage readout, display name DS-18, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-18 custom profile row. The pinned rules table has no DS-18 row, and the first-pass record does not resolve native host breadth, phage breadth, direct profile-to-protein correspondence, PDDEXK nuclease activity, molecular output, or endogenous DS-18 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_18_system.html#ds-18-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-19-defensefinder-model-gap",
  "prompt": "Resolve DS-19 native host breadth, exact profile-to-protein mapping, low-confidence HHpred-domain interpretation, component chemistry, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-19 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-19 system",
  "source_id": "traitmech:000444",
  "source_file": "ds_19_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_19_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-19 as the defensive PDP4 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_000020904.1, a Bas19 phage readout, display name DS-19, and a lower-probability PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-19 custom profile row. The pinned rules table has no DS-19 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK nuclease activity, molecular output, or endogenous DS-19 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_19_system.html#ds-19-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-1-defensefinder-model-gap",
  "prompt": "Resolve DS-1 native host breadth, exact DS-1A/DS-1B component functions, profile-to-component mapping, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower DS-1 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-1 system",
  "source_id": "traitmech:000424",
  "source_file": "ds_1_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_1_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-1 as the defensive D390 transcriptional unit that reduced plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records DS-1A and DS-1B profile rows. The pinned rules table has no DS-1 row, and the first-pass record does not resolve native host breadth, exact component activities, profile-to-component mapping, phage target breadth, the direct molecular output, or endogenous DS-1 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_1_system.html#ds-1-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-20-defensefinder-model-gap",
  "prompt": "Resolve DS-20 native host breadth, exact profile-to-protein mapping, HHpred-domain interpretation, component chemistry, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-20 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-20 system",
  "source_id": "traitmech:000445",
  "source_file": "ds_20_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_20_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-20 as the defensive PDX1 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_032291790.1, a Bas3 phage readout, display name DS-20, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-20 custom profile row. The pinned rules table has no DS-20 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK nuclease activity, molecular output, or endogenous DS-20 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_20_system.html#ds-20-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-21-defensefinder-model-gap",
  "prompt": "Resolve DS-21 native host breadth, exact profile-to-protein mapping, HHpred-domain interpretation, component chemistry, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-21 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-21 system",
  "source_id": "traitmech:000446",
  "source_file": "ds_21_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_21_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-21 as the defensive TOXO transcriptional unit and final Science Tables S6/S7/S8 map it to three product accessions, a Bas1 phage readout, display name DS-21, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records three DS-21 custom profile rows. The pinned rules table has no DS-21 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK nuclease activity, molecular output, or endogenous DS-21 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_21_system.html#ds-21-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-22-defensefinder-model-gap",
  "prompt": "Resolve DS-22 native host breadth, exact single-component activity, profile-to-protein mapping, sensitive-phage breadth, low-confidence HHpred-domain interpretation, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-22 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-22 system",
  "source_id": "traitmech:000447",
  "source_file": "ds_22_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_22_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-22 as the defensive MVB1 transcriptional unit that reduced Bas11 plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records one DS-22 profile row. The pinned rules table has no DS-22 row, and the first-pass record does not resolve native host breadth, exact component activity, direct profile-to-protein correspondence, the Mvb12 and JAB HHpred-domain rows, phage target breadth, molecular output, or endogenous DS-22 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_22_system.html#ds-22-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-23-defensefinder-model-gap",
  "prompt": "Resolve DS-23 native host breadth, exact single-component activity, profile-to-protein mapping, ZF and PDDEXK HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-23 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-23 system",
  "source_id": "traitmech:000448",
  "source_file": "ds_23_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_23_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-23 as the defensive E2DP transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_020231147.1, a Bas19 phage readout, display name DS-23, and ZF and PDDEXK HHpred rows. The pinned DefenseFinder HMM inventory records one DS-23 custom profile row. The pinned rules table has no DS-23 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, ZF or PDDEXK activity, molecular output, or endogenous DS-23 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_23_system.html#ds-23-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-24-defensefinder-model-gap",
  "prompt": "Resolve DS-24 native host breadth, exact single-component activity, profile-to-protein mapping, PDDEXK HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-24 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-24 system",
  "source_id": "traitmech:000449",
  "source_file": "ds_24_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_24_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-24 as the defensive RED2 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_000183405.1, a Bas1 phage readout, display name DS-24, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-24 custom profile row. The pinned rules table has no DS-24 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK activity, molecular output, or endogenous DS-24 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_24_system.html#ds-24-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-25-defensefinder-model-gap",
  "prompt": "Resolve DS-25 working-identifier rows, preprint Table S5 and S6 context, final Science supplement omission, native host breadth, DS-25A/DS-25B profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-25 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-25 system",
  "source_id": "traitmech:000473",
  "source_file": "ds_25_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_25_locus_profile_model"
  ],
  "rationale": "The DeWeirdt et al. preprint supports the DefensePredictor discovered System naming convention, the pinned DefenseFinder article registry names DS-25 and maps it to that preprint, and the pinned HMM inventory records DS-25A and DS-25B custom profile rows. DS-25 is absent from the final Science Table S6, S7, and S8 files checked during this curation pass, the exact preprint per-TU rows were not recovered, the pinned DefenseFinder rules table has no DS-25 row, and the first-pass record does not resolve the working identifier, assayed phages, phage readout, native host, profile-to-component mapping, component activities, or complete detection criteria.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_25_system.html#ds-25-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-26-defensefinder-model-gap",
  "prompt": "Resolve DS-26 native host breadth, exact component activity, PDDEXK/FokI HHpred-domain interpretation, nuclease chemistry, complete phage breadth, molecular output, and DefenseFinder model coverage before minting narrower DS-26 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-26 system",
  "source_id": "traitmech:000472",
  "source_file": "ds_26_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_26_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-26 as the defensive NERD transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas25 and Bas19 phage readouts, display name DS-26, and a PDDEXK/FokI cleavage-domain HHpred row. A first-pass pinned DefenseFinder review found no exact DS-26 article, HMM, or rules row, and the first-pass record therefore does not resolve native host breadth, complete phage breadth, domain interpretation, nuclease chemistry, molecular output, or endogenous DS-26 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_26_system.html#ds-26-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-27-defensefinder-model-gap",
  "prompt": "Resolve DS-27 native host breadth, exact single-component activity, profile-to-protein mapping, HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-27 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-27 system",
  "source_id": "traitmech:000451",
  "source_file": "ds_27_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_27_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-27 as the defensive SMEK transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_087896215.1, an RB69 phage readout, and display name DS-27. The pinned DefenseFinder HMM inventory records one DS-27 custom profile row. The pinned rules table has no DS-27 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, HHpred-domain interpretation, molecular output, or endogenous DS-27 activity.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_27_system.html#ds-27-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-28-defensefinder-model-gap",
  "prompt": "Resolve DS-28 native host breadth, exact component activities, profile-to-protein mappings, HEPN and transcription-factor HHpred-domain interpretations, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-28 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-28 system",
  "source_id": "traitmech:000452",
  "source_file": "ds_28_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_28_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-28 as the defensive ANEX transcriptional unit and final Science Tables S6/S7/S8 map it to product accessions WP_000494510.1 and WP_000528930.1, a Bas60 phage readout, display name DS-28, a high-probability HEPN HHpred row, and a lower-probability TF HHpred row. The pinned DefenseFinder HMM inventory records two DS-28 custom profile rows. The pinned rules table has no DS-28 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, HEPN or transcription-factor activity, molecular output, or endogenous DS-28 activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_28_system.html#ds-28-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-29-defensefinder-model-gap",
  "prompt": "Resolve DS-29 native host breadth, exact single-component activity, profile-to-protein mapping, HEPN-like HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-29 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-29 system",
  "source_id": "traitmech:000453",
  "source_file": "ds_29_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_29_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-29 as the defensive HEP3 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_061089765.1, a Bas60 phage readout, display name DS-29, and a HEPN-like HHpred row. The pinned DefenseFinder HMM inventory records one DS-29 custom profile row. The pinned rules table has no DS-29 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, HEPN-like activity, molecular output, or endogenous DS-29 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_29_system.html#ds-29-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-2-defensefinder-model-gap",
  "prompt": "Resolve DS-2 native host breadth, exact DS-2 component functions, DS-2C profile-to-component mapping, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower DS-2 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-2 system",
  "source_id": "traitmech:000425",
  "source_file": "ds_2_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_2_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-2 as the defensive DISA transcriptional unit that reduced plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records a DS-2C profile row. The pinned rules table has no DS-2 row, and the first-pass record does not resolve native host breadth, exact component activities, profile-to-component mapping, phage target breadth, the direct molecular output, or endogenous DS-2 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_2_system.html#ds-2-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-30-lamassu-family-model-gap",
  "prompt": "Resolve DS-30 native host breadth, exact profile-to-protein correspondence, DS-30/Lamassu-Fam component activities, Lamassu subtype and effector chemistry, LmuC requirement, complete phage breadth, and DS-30-specific DefenseFinder rule-level criteria before minting narrower DS-30 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-30 system",
  "source_id": "traitmech:000470",
  "source_file": "ds_30_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_30_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-30 as the defensive ABC3 transcriptional unit and final Science Tables S6/S7/S8 map it to four product accessions, a SECphi27 phage readout, four HHpred-domain rows, and display name DS-30. The pinned DefenseFinder HMM inventory records four Lamassu-Fam DS-30 custom profile rows. The pinned DefenseFinder rules table only lists generic Lamassu-Fam effector-subtype rows, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, LmuC requirement, molecular output, subtype-specific Lamassu chemistry, or endogenous DS-30 activity.",
  "num_experiments": 0,
  "num_evidence": 13,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_30_system.html#ds-30-lamassu-family-model-gap"
 },
 {
  "discussion_id": "ds-31-defensefinder-model-gap",
  "prompt": "Resolve DS-31 native host breadth, exact single-component activity, profile-to-protein mapping, PDDEXK HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-31 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-31 system",
  "source_id": "traitmech:000454",
  "source_file": "ds_31_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_31_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-31 as the defensive RED7 transcriptional unit and final Science Tables S6/S7/S8 map it to product accession WP_001703029.1, a Bas19 phage readout, display name DS-31, and a PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-31 custom profile row. The pinned rules table has no DS-31 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK activity, molecular output, or endogenous DS-31 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_31_system.html#ds-31-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-32-defensefinder-model-gap",
  "prompt": "Resolve DS-32 native host breadth, exact component activities, profile-to-protein mapping, RecR, PRTase, and NADAR HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-32 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-32 system",
  "source_id": "traitmech:000455",
  "source_file": "ds_32_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_32_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-32 as the defensive NADR transcriptional unit and final Science Tables S6/S7/S8 map it to two product accessions, a Bas26 phage readout, display name DS-32, and three HHpred rows. The pinned DefenseFinder HMM inventory records two DS-32 custom profile rows. The pinned rules table has no DS-32 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, component activities, molecular output, or endogenous DS-32 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_32_system.html#ds-32-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-33-defensefinder-model-gap",
  "prompt": "Resolve DS-33 native host breadth, exact component activities, profile-to-protein mapping, Csa3 and HEPN HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-33 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-33 system",
  "source_id": "traitmech:000456",
  "source_file": "ds_33_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_33_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-33 as the defensive GNAT transcriptional unit and final Science Tables S6/S7/S8 map it to two product accessions, a Bas26 phage readout, display name DS-33, and two HHpred rows. The pinned DefenseFinder HMM inventory records one DS-33 custom profile row. The pinned rules table has no DS-33 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, component activities, molecular output, or endogenous DS-33 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_33_system.html#ds-33-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-34-defensefinder-model-gap",
  "prompt": "Resolve DS-34 native host breadth, exact component activities, profile-to-protein mapping, phage-repressor and HTH HHpred-domain interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-34 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-34 system",
  "source_id": "traitmech:000457",
  "source_file": "ds_34_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_34_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-34 as the defensive CITO transcriptional unit and final Science Tables S6/S7/S8 map it to two product accessions, a Bas19 phage readout, display name DS-34, and two HHpred rows. The pinned DefenseFinder HMM inventory records two DS-34 custom profile rows. The pinned rules table has no DS-34 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, component activities, molecular output, or endogenous DS-34 activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_34_system.html#ds-34-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-35-defensefinder-model-gap",
  "prompt": "Resolve DS-35 native host breadth, exact component activity, profile-to-protein mapping, PDDEXK HHpred-domain interpretation, nuclease chemistry, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-35 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-35 system",
  "source_id": "traitmech:000458",
  "source_file": "ds_35_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_35_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-35 as the defensive RED5 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, RB69 and T4 phage readouts, display name DS-35, and one PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-35 custom profile row. The pinned rules table has no DS-35 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK domain interpretation, nuclease chemistry, molecular output, or endogenous DS-35 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_35_system.html#ds-35-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-36-defensefinder-model-gap",
  "prompt": "Resolve DS-36 working-identifier rows, preprint Table S5 and S6 context, final Science supplement omission, native host breadth, DS-36 profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-36 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-36 system",
  "source_id": "traitmech:000474",
  "source_file": "ds_36_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_36_locus_profile_model"
  ],
  "rationale": "The DeWeirdt et al. preprint supports the DefensePredictor discovered System naming convention, the pinned DefenseFinder article registry names DS-36 and maps it to that preprint, and the pinned HMM inventory records a DS-36 custom profile row. DS-36 is absent from the final Science Table S6, S7, and S8 files checked during this curation pass, the exact preprint per-TU row was not recovered, the pinned DefenseFinder rules table has no DS-36 row, and the first-pass record does not resolve the working identifier, assayed phages, phage readout, native host, profile-to-component mapping, component activities, or complete detection criteria.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_36_system.html#ds-36-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-37-defensefinder-model-gap",
  "prompt": "Resolve DS-37 native host breadth, exact component activity, profile-to-protein mapping, low-probability PDDEXK HHpred-domain interpretation, nuclease chemistry, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-37 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-37 system",
  "source_id": "traitmech:000459",
  "source_file": "ds_37_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_37_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-37 as the defensive SC24 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas1 and Bas9 phage readouts, display name DS-37, and one low-probability PDDEXK HHpred row. The pinned DefenseFinder HMM inventory records one DS-37 custom profile row. The pinned rules table has no DS-37 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, PDDEXK domain interpretation, nuclease chemistry, molecular output, or endogenous DS-37 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_37_system.html#ds-37-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-38-defensefinder-model-gap",
  "prompt": "Resolve DS-38 native host breadth, exact component activity, profile-to-protein mapping, HEPN ribonuclease interpretation, zinc-finger DNA-binding interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-38 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-38 system",
  "source_id": "traitmech:000460",
  "source_file": "ds_38_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_38_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-38 as the defensive HEP2 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas25 and Bas19 phage readouts, display name DS-38, and high-probability HEPN and zinc-finger HHpred rows. The pinned DefenseFinder HMM inventory records one DS-38 custom profile row. The pinned rules table has no DS-38 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, HEPN ribonuclease activity, zinc-finger DNA-binding activity, molecular output, or endogenous DS-38 activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_38_system.html#ds-38-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-39-defensefinder-model-gap",
  "prompt": "Resolve DS-39 native host breadth, exact component activity, profile-to-protein mapping, AAA+ ATPase interpretation, HTH/zinc-finger interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-39 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-39 system",
  "source_id": "traitmech:000461",
  "source_file": "ds_39_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_39_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-39 as the defensive AAA5 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas1 and Bas3 phage readouts, display name DS-39, high-probability AAA+ ATPase and HTH HHpred rows, and a moderate-probability zinc-finger HHpred row. The pinned DefenseFinder HMM inventory records one DS-39 custom profile row. The pinned rules table has no DS-39 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, AAA+ ATPase activity, HTH or zinc-finger interpretation, molecular output, or endogenous DS-39 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_39_system.html#ds-39-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-3-defensefinder-model-gap",
  "prompt": "Resolve DS-3 native host breadth, exact PIN ribonuclease activity, DS-3 profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower DS-3 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-3 system",
  "source_id": "traitmech:000426",
  "source_file": "ds_3_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_3_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-3 as the defensive PIN8 transcriptional unit that reduced plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records a DS-3 profile row. The pinned rules table has no DS-3 row, and the first-pass record does not resolve native host breadth, exact PIN substrate or output, profile-to-protein mapping, phage target breadth, or endogenous DS-3 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_3_system.html#ds-3-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-40-defensefinder-model-gap",
  "prompt": "Resolve DS-40 native host breadth, exact component activity, profile-to-protein mapping, DUF6680 interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-40 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-40 system",
  "source_id": "traitmech:000462",
  "source_file": "ds_40_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_40_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-40 as the defensive D295 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, a Bas26 phage readout, display name DS-40, and a moderate-probability DUF6680 HHpred row. The pinned DefenseFinder HMM inventory records one DS-40 custom profile row. The pinned rules table has no DS-40 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, DUF6680 activity, molecular output, or endogenous DS-40 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_40_system.html#ds-40-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-41-defensefinder-model-gap",
  "prompt": "Resolve DS-41 native host breadth, exact component activity, profile-to-protein mapping, AAA+ ATPase interpretation, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-41 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-41 system",
  "source_id": "traitmech:000463",
  "source_file": "ds_41_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_41_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-41 as the defensive AAA2 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas1 and T4 phage readouts, display name DS-41, and a high-probability AAA+ ATPase HHpred row. The pinned DefenseFinder HMM inventory records one DS-41 custom profile row. The pinned rules table has no DS-41 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, AAA+ ATPase activity, molecular output, or endogenous DS-41 activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_41_system.html#ds-41-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-42-defensefinder-model-gap",
  "prompt": "Resolve DS-42 native host breadth, exact component activity, profile-to-protein mapping, MBL hydrolase and CHS5_N interpretations, WP_249925928.1 function, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-42 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-42 system",
  "source_id": "traitmech:000464",
  "source_file": "ds_42_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_42_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-42 as the defensive PRO1 transcriptional unit and final Science Tables S6/S7/S8 map it to three product accessions, a Bas1 phage readout, display name DS-42, a high-probability MBL hydrolase HHpred row, and a moderate-probability CHS5_N/Dimerization HHpred row. The pinned DefenseFinder HMM inventory records three DS-42 custom profile rows. The pinned rules table has no DS-42 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, component activities, molecular output, or endogenous DS-42 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_42_system.html#ds-42-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-43-defensefinder-model-gap",
  "prompt": "Resolve DS-43 native host breadth, exact component activity, profile-to-protein mapping, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-43 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-43 system",
  "source_id": "traitmech:000468",
  "source_file": "ds_43_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_43_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-43 as the defensive D668 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, Bas19 and SECphi18 phage readouts, and display name DS-43. The pinned DefenseFinder HMM inventory records one DS-43 custom profile row. The pinned rules table has no DS-43 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous DS-43 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_43_system.html#ds-43-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-44-defensefinder-model-gap",
  "prompt": "Resolve DS-44 working-identifier rows, preprint Table S5 and S6 context, final Science supplement omission, native host breadth, DS-44 profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-44 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-44 system",
  "source_id": "traitmech:000475",
  "source_file": "ds_44_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_44_locus_profile_model"
  ],
  "rationale": "The DeWeirdt et al. preprint supports the DefensePredictor discovered System naming convention, the pinned DefenseFinder article registry names DS-44 and maps it to that preprint, and the pinned HMM inventory records a DS-44 custom profile row. DS-44 is absent from the final Science Table S6, S7, and S8 files checked during this curation pass, the exact preprint per-TU row was not recovered, the pinned DefenseFinder rules table has no DS-44 row, and the first-pass record does not resolve the working identifier, assayed phages, phage readout, native host, profile-to-component mapping, component activities, or complete detection criteria.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "DOI:10.1101/2025.01.08.631726",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_44_system.html#ds-44-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-45-defensefinder-model-gap",
  "prompt": "Resolve DS-45 native host breadth, DUF2971-domain activity, profile-to-protein mapping, complete phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower DS-45 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-45 system",
  "source_id": "traitmech:000469",
  "source_file": "ds_45_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_45_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-45 as the defensive 2971 transcriptional unit and final Science Tables S6/S7/S8 map it to one product accession, a Bas50 phage readout, one DUF2971 HHpred-domain row, and display name DS-45. The pinned DefenseFinder HMM inventory records one DS-45 custom profile row. The pinned rules table has no DS-45 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous DS-45 activity.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_45_system.html#ds-45-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-46-model-coverage-gap",
  "prompt": "Resolve DS-46 phage-specific readouts, display-name and domain rows, DefenseFinder model coverage, native host breadth, exact component activities, molecular output, complete phage breadth, and endogenous activity before minting narrower DS-46 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-46 system",
  "source_id": "traitmech:000471",
  "source_file": "ds_46_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_46_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-46 as the defensive RMRT transcriptional unit and final Science Table S6 maps RMRT to two product accessions. A first-pass final Science Table S7/S8 review found no exact RMRT/DS-46 phage-specific readout, display-name row, or HHpred-domain row. The pinned DefenseFinder article, HMM, and rules registries also do not list DS-46 or RMRT, and the first-pass record therefore does not resolve native host breadth, complete phage breadth, exact component activities, molecular output, or endogenous DS-46 activity.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_46_system.html#ds-46-model-coverage-gap"
 },
 {
  "discussion_id": "ds-4-defensefinder-model-gap",
  "prompt": "Resolve DS-4 native host breadth, exact five-component activities, DS-4 profile-to-protein mapping, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower DS-4 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-4 system",
  "source_id": "traitmech:000427",
  "source_file": "ds_4_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_4_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-4 as the defensive NTTI transcriptional unit that reduced plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records five DS-4 profile rows. The pinned rules table has no DS-4 row, and the first-pass record does not resolve native host breadth, exact component activities, profile-to-protein mapping, phage target breadth, or endogenous DS-4 activity.",
  "num_experiments": 0,
  "num_evidence": 12,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_4_system.html#ds-4-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-5-defensefinder-model-gap",
  "prompt": "Resolve DS-5 native host breadth, exact two-component activities, DS-5 profile-to-protein mapping, sensitive-phage breadth, DS-5 PIN nuclease target, AcrIF4-like component function, and rule-level detection criteria before minting narrower DS-5 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-5 system",
  "source_id": "traitmech:000428",
  "source_file": "ds_5_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_5_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-5 as the defensive PN12 transcriptional unit that reduced Bas60 plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records two DS-5 profile rows. The pinned rules table has no DS-5 row, and the first-pass record does not resolve native host breadth, exact component activities, profile-to-protein mapping, phage target breadth, or endogenous DS-5 activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_5_system.html#ds-5-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-6-defensefinder-model-gap",
  "prompt": "Resolve DS-6 native host breadth, exact two-component activities, DS-6 profile-to-protein mapping, sensitive-phage breadth, DUF3037 and DUF1829 activity, HipA-like kinase substrates, and rule-level detection criteria before minting narrower DS-6 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-6 system",
  "source_id": "traitmech:000430",
  "source_file": "ds_6_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_6_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-6 as the defensive HIPA transcriptional unit that reduced Bas1 plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records two DS-6 profile rows. The pinned rules table has no DS-6 row, and the first-pass record does not resolve native host breadth, exact profile-to-protein correspondence, DUF3037 or HipA-like kinase activity, phage target breadth, or endogenous DS-6 activity.",
  "num_experiments": 0,
  "num_evidence": 16,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_6_system.html#ds-6-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-7-defensefinder-model-gap",
  "prompt": "Resolve DS-7 native host breadth, exact single-component activity, DS-7 profile-to-protein mapping, sensitive-phage breadth, HNH endonuclease activity, the role of the H52 residue, the phage-baseplate-like hit, and rule-level detection criteria before minting narrower DS-7 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-7 system",
  "source_id": "traitmech:000431",
  "source_file": "ds_7_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_7_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-7 as the defensive SVIR transcriptional unit that reduced Bas60 plaquing when cloned in E. coli MG1655, and the pinned DefenseFinder HMM inventory records one DS-7 profile row. The pinned rules table has no DS-7 row, and the first-pass record does not resolve native host breadth, exact profile-to-protein correspondence, HNH endonuclease activity, the function of the H52 residue, phage target breadth, or endogenous DS-7 activity.",
  "num_experiments": 0,
  "num_evidence": 12,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_7_system.html#ds-7-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-8-defensefinder-model-gap",
  "prompt": "Resolve DS-8 native host breadth, DS-8 profile-to-protein mapping, sensitive-phage breadth, direct cyclic-nucleotide substrate, NACHT-mediated activation route, relationship to NLR-like bNACHT systems, and rule-level detection criteria before minting narrower DS-8 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-8 system",
  "source_id": "traitmech:000432",
  "source_file": "ds_8_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_8_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-8 as the defensive MNAC transcriptional unit that reduced Bas1 plaquing when cloned in E. coli MG1655, identify DS-8 as a single-protein system with metallophosphatase and NACHT domains, and report that D52A, N84A, and K375A mutations ablated Bas1 protection. The pinned DefenseFinder HMM inventory records one DS-8 profile row. The pinned rules table has no DS-8 row, and the first-pass record does not resolve native host breadth, exact profile-to-protein correspondence, direct cyclic-nucleotide substrate, exact NACHT-mediated activation route, phage target breadth, endogenous DS-8 activity, or whether DS-8 should be related to the broader NLR-like bNACHT system family.",
  "num_experiments": 0,
  "num_evidence": 14,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_8_system.html#ds-8-defensefinder-model-gap"
 },
 {
  "discussion_id": "ds-9-defensefinder-model-gap",
  "prompt": "Resolve DS-9 native host breadth, DS-9A/DS-9B profile-to-protein mapping, sensitive-phage breadth, direct metallophosphoesterase substrate, HAD phosphatase target, and rule-level detection criteria before minting narrower DS-9 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DS-9 system",
  "source_id": "traitmech:000433",
  "source_file": "ds_9_system.yaml",
  "attaches_to": [
   "causal_graphs#ds_9_locus_reduces_phage_plaquing"
  ],
  "rationale": "DeWeirdt et al. support DS-9 as the defensive MHAD transcriptional unit that reduced Bas1 plaquing when cloned in E. coli MG1655, identify DS-9 as a two-gene system with metallophosphatase and HAD phosphatase domains, and report that DS-9A predicted catalytic-residue mutations caused a loss of defense. Final Science Table S7 mutant rows show D207A and N292A Bas1 protection loss relative to wild-type MHAD in a matched panel. The pinned DefenseFinder HMM inventory records two DS-9 profile rows. The pinned rules table has no DS-9 row, and the first-pass record does not resolve native host breadth, exact DS-9A/DS-9B profile-to-protein correspondence, direct metallophosphoesterase substrate, HAD phosphatase target, phage target breadth, endogenous DS-9 activity, or DefenseFinder rule-level detection criteria.",
  "num_experiments": 0,
  "num_evidence": 15,
  "evidence_refs": [
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "DOI:10.1126/science.adv7924",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S6.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S7.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/NIHMS2163519-supplement-Table_S8.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ds_9_system.html#ds-9-defensefinder-model-gap"
 },
 {
  "discussion_id": "dsr-sirtuin-mechanism-gap",
  "prompt": "Map DefenseFinder Dsr_I and Dsr_II profiles onto experimentally resolved DSR1 and DSR2 NADase triggers, host ranges, anti-defense proteins, and Dsr naming collisions before minting narrower Dsr mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Dsr system",
  "source_id": "traitmech:000280",
  "source_file": "dsr_system.yaml",
  "attaches_to": [
   "causal_graphs#dsr_sirtuin_antiphage_defense"
  ],
  "rationale": "Gao et al. support defense-associated sirtuin proteins as antiphage system components, Garb et al. resolved NAD+ depletion for multiple SIR2-dependent defense systems and tail tube-triggered NADase activation for B. subtilis DSR2, and DefenseFinder models Dsr_I and Dsr_II. This first record stays at Dsr-family level until the DefenseFinder subtype profiles can be aligned to specific experimental DSR1/DSR2 systems, trigger proteins, host ranges, and phage-encoded anti-DSR proteins. The DefenseFinder Dsr system is also lexically distinct from metabolic DsrAB dissimilatory sulfite reductase systems.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/dsr_system.html#dsr-sirtuin-mechanism-gap"
 },
 {
  "discussion_id": "duf262-schlafen-defensefinder-profile-gap",
  "prompt": "Resolve exact DUF262_Schlafen locus architecture, DUF262-associated domain boundaries, natural host exemplars, phage trigger breadth, and DefenseFinder HMM/rules coverage before minting narrower DUF262 Schlafen mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DUF262 Schlafen system",
  "source_id": "traitmech:000530",
  "source_file": "duf262_schlafen_system.yaml",
  "attaches_to": [
   "causal_graphs#duf262_schlafen_phage_defense"
  ],
  "rationale": "Perez Taboada et al. support prokaryotic Schlafen nucleases as widespread antiviral effectors fused to phage-sensing domains, and the pinned DefenseFinder article registry maps the DUF262_Shlafen key to the same article. The pinned HMM inventory and rules table have no exact DUF262_Schlafen or DUF262 rows for this source key. This first-pass record therefore does not resolve whether the exact DUF262_Schlafen architecture is a single-protein fusion or multi-gene locus, its exact DUF262-associated domain boundaries, natural host exemplars, accession-level Schlafen proteins, full phage trigger breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/duf262_schlafen_system.html#duf262-schlafen-defensefinder-profile-gap"
 },
 {
  "discussion_id": "ecokmcra-defensefinder-model-gap",
  "prompt": "Resolve EcoKMcrA-family breadth, methylcytosine and hydroxymethylcytosine sequence-context specificity across natural hosts, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower EcoKMcrA mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "EcoKMcrA system",
  "source_id": "traitmech:000509",
  "source_file": "ecokmcra_system.yaml",
  "attaches_to": [
   "causal_graphs#ecokmcra_restricts_modified_cytosine_dna"
  ],
  "rationale": "Czapinska et al. support E. coli EcoKMcrA as a methylcytosine- and hydroxymethylcytosine-dependent restriction endonuclease with cellular modified-DNA restriction activity tied to the nuclease active site, and the pinned DefenseFinder article registry maps EcoKMcrA to that paper. The pinned HMM inventory and rules table have no exact EcoKMcrA rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of EcoKMcrA-like systems beyond E. coli K strains, or the complete set of natural methylcytosine and hydroxymethylcytosine sequence contexts.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1093/nar/gky731",
   "DOI:10.1093/nar/gky731",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ecokmcra_system.html#ecokmcra-defensefinder-model-gap"
 },
 {
  "discussion_id": "eleos-mechanism-gap",
  "prompt": "Resolve Eleos phage triggers and effector outputs before minting narrower Eleos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Eleos system",
  "source_id": "traitmech:000250",
  "source_file": "eleos_system.yaml",
  "attaches_to": [
   "causal_graphs#eleos_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Eleos as a named anti-phage system with LeoA, LeoB, LeoBC, and LeoC profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/eleos_system.html#eleos-mechanism-gap"
 },
 {
  "discussion_id": "endpacf1-host-modification-and-model-gap",
  "prompt": "Resolve ENDPaCF1 Pseudomonas host breadth, complete phage-DNA hypermodification breadth, direct iEndoIII sensing-to-cleavage coupling, phage inhibitor specificity, and DefenseFinder HMM/rules coverage before minting narrower END nuclease mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ENDPaCF1 system",
  "source_id": "traitmech:000503",
  "source_file": "endpacf1_system.yaml",
  "attaches_to": [
   "causal_graphs#endpacf1_targets_hypermodified_phage_dna"
  ],
  "rationale": "Yee et al. support ENDPaCF1 as a Type IIS restriction endonuclease-like Pseudomonas phage-defense system that can recognize diverse hypermodified phage genomes, and the pinned DefenseFinder article registry maps the ENDPaCF1 source key to the Yee et al. preprint. The pinned HMM inventory and rules table have no exact ENDPaCF1 rows. This first-pass record therefore does not resolve a complete profile model, the direct domain coupling between iEndoIII sensing and cleavage, or the full natural host, phage, and inhibitor breadth.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1101/2025.03.31.646159",
   "DOI:10.1101/2025.03.31.646159",
   "DOI:10.1101/2025.03.31.646159",
   "DOI:10.1101/2025.03.31.646159",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/endpacf1_system.html#endpacf1-host-modification-and-model-gap"
 },
 {
  "discussion_id": "epona-mechanism-gap",
  "prompt": "Resolve Epona phage triggers and effector outputs before minting narrower Epona mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Epona system",
  "source_id": "traitmech:000281",
  "source_file": "epona_system.yaml",
  "attaches_to": [
   "causal_graphs#epona_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Epona as a named anti-phage system with a VCA0366 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/epona_system.html#epona-mechanism-gap"
 },
 {
  "discussion_id": "erebus-mechanism-gap",
  "prompt": "Resolve Erebus phage triggers and effector outputs before minting narrower Erebus mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Erebus system",
  "source_id": "traitmech:000308",
  "source_file": "erebus_system.yaml",
  "attaches_to": [
   "causal_graphs#erebus_locus_restricts_phage"
  ],
  "rationale": "van den Berg et al. and DefenseFinder support Erebus as a named anti-phage system with an Erebus__EruA HMM profile entry, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/erebus_system.html#erebus-mechanism-gap"
 },
 {
  "discussion_id": "esos-mechanism-gap",
  "prompt": "Resolve Esos phage triggers and effector outputs before minting narrower Esos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Esos system",
  "source_id": "traitmech:000282",
  "source_file": "esos_system.yaml",
  "attaches_to": [
   "causal_graphs#esos_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Esos as a named anti-phage system with a VCA0450 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/esos_system.html#esos-mechanism-gap"
 },
 {
  "discussion_id": "fliodhais-mechanism-gap",
  "prompt": "Resolve Fliodhais phage triggers and effector outputs before minting narrower Fliodhais mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Fliodhais system",
  "source_id": "traitmech:000326",
  "source_file": "fliodhais_system.yaml",
  "attaches_to": [
   "causal_graphs#fliodhais_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al. and DefenseFinder support Fliodhais as a named two-component anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fliodhais_system.html#fliodhais-mechanism-gap"
 },
 {
  "discussion_id": "fs-giy-yig-mechanism-gap",
  "prompt": "Resolve FS_GIY_YIG natural hosts, helper-phage triggers, GIY-YIG substrates, and effector activity before minting narrower FS_GIY_YIG mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-GIY-YIG system",
  "source_id": "traitmech:000346",
  "source_file": "fs_giy_yig_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_giy_yig_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_GIY_YIG as a single-profile system. Its exact natural host breadth, helper-phage trigger, nuclease substrate, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_giy_yig_system.html#fs-giy-yig-mechanism-gap"
 },
 {
  "discussion_id": "fs-hepn-tm-mechanism-gap",
  "prompt": "Resolve FS_HEPN_TM natural hosts, helper-phage triggers, HEPN-family substrates, and transmembrane partner activity before minting narrower FS_HEPN_TM mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-HEPN-TM system",
  "source_id": "traitmech:000347",
  "source_file": "fs_hepn_tm_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_hepn_tm_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_HEPN_TM as a two-profile HEPN/transmembrane system. Its exact natural host breadth, helper-phage trigger, substrate, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_hepn_tm_system.html#fs-hepn-tm-mechanism-gap"
 },
 {
  "discussion_id": "fs-hp-sdh-sah-mechanism-gap",
  "prompt": "Resolve FS_HP_SDH_sah natural hosts, helper-phage triggers, HP component identity, and SDH_sah partner activity before minting narrower FS_HP_SDH_sah mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-HP-SDH-sah system",
  "source_id": "traitmech:000349",
  "source_file": "fs_hp_sdh_sah_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_hp_sdh_sah_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_HP_SDH_sah as a two-profile system. Its exact natural host breadth, helper-phage trigger, HP component identity, SDH_sah partner activity, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_hp_sdh_sah_system.html#fs-hp-sdh-sah-mechanism-gap"
 },
 {
  "discussion_id": "fs-hp-mechanism-gap",
  "prompt": "Resolve FS_HP natural hosts, helper-phage triggers, HP component identity, and effector activity before minting narrower FS_HP mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-HP system",
  "source_id": "traitmech:000348",
  "source_file": "fs_hp_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_hp_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_HP as a single-profile system. Its exact natural host breadth, helper-phage trigger, component identity, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_hp_system.html#fs-hp-mechanism-gap"
 },
 {
  "discussion_id": "fs-hsdr-like-mechanism-gap",
  "prompt": "Resolve FS_HsdR_like natural hosts, helper-phage triggers, DUF6731 activity, HP component identity, HdrR activity, and the profile-to-activity mapping before minting narrower FS_HsdR_like mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-HsdR-like system",
  "source_id": "traitmech:000350",
  "source_file": "fs_hsdr_like_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_hsdr_like_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_HsdR_like as a two-gene system drawing from three custom profile keys. Its exact natural host breadth, helper-phage trigger, component activities, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_hsdr_like_system.html#fs-hsdr-like-mechanism-gap"
 },
 {
  "discussion_id": "fs-sma-mechanism-gap",
  "prompt": "Resolve FS_Sma natural hosts, helper-phage triggers, Sma component identity, and effector activity before minting narrower FS_Sma mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "FS-Sma system",
  "source_id": "traitmech:000351",
  "source_file": "fs_sma_system.yaml",
  "attaches_to": [
   "causal_graphs#fs_sma_locus_restricts_phage"
  ],
  "rationale": "Fillol-Salom et al. support phage-inducible chromosomal islands as carriers of defense systems that provide broad immunity, and DefenseFinder models FS_Sma as a single-profile system. Its exact natural host breadth, helper-phage trigger, component identity, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/fs_sma_system.html#fs-sma-mechanism-gap"
 },
 {
  "discussion_id": "gabija-activation-and-antidefense-gap",
  "prompt": "Resolve Gabija activation, stoichiometry, cell-outcome, and phage anti-defense breadth before minting narrower Gabija mechanistic children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gabija system",
  "source_id": "traitmech:000215",
  "source_file": "gabija_system.yaml",
  "attaches_to": [],
  "rationale": "Cheng et al. support nucleotide depletion and DNA cleavage as Gabija outputs, and Antine et al. support GajAB complex assembly plus Gad1-mediated inhibition, but Gabija family members need separate review before TraitMech asserts one universal trigger, exact GajA:GajB stoichiometry, host death program, DNA substrate, or anti-Gabija phage inhibitor.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gabija_system.html#gabija-activation-and-antidefense-gap"
 },
 {
  "discussion_id": "apea-trigger-and-homolog-scope-gap",
  "prompt": "Resolve ApeA natural-host loci, homolog-specific DNA-phage versus RNA-phage triggers, phage nuclease inputs, phage genomic RNA targets, abortive versus non-abortive outputs, and subtype activity before minting narrower ApeA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ApeA system",
  "source_id": "traitmech:000334",
  "source_file": "gao_ape_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_ape_hepn_rnase_restricts_phage"
  ],
  "rationale": "Juozapaitis et al. support DNA-phage ApeA abortive infection through host tRNA anticodon-loop cleavage, Drobysheva et al. support non-abortive RNA-phage defense through phage-genomic-RNA cleavage, and DefenseFinder models Gao_Ape with the Gao_Ape__ApeA profile. This first record stays at system level because the curated evidence leaves homolog- and phage-class-specific trigger logic, the full DNA-versus-RNA substrate split, activity of additional homologs, and accession-level natural-host breadth unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_ape_system.html#apea-trigger-and-homolog-scope-gap"
 },
 {
  "discussion_id": "gao-her-duf-mechanism-gap",
  "prompt": "Resolve Gao_Her_DUF natural hosts, DUF4297/HerA_DUF component functions, phage triggers, and effector activity before minting narrower Gao_Her_DUF mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Her-DUF system",
  "source_id": "traitmech:000361",
  "source_file": "gao_her_duf_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_her_duf_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Her_DUF as a two-profile system under the Gao_Her family key. The exact natural host breadth, DUF4297/HerA_DUF component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_her_duf_system.html#gao-her-duf-mechanism-gap"
 },
 {
  "discussion_id": "gao-her-sir-mechanism-gap",
  "prompt": "Resolve Gao_Her_SIR natural hosts, HerA_SIR2/SIR2 component functions, phage triggers, and effector activity before minting narrower Gao_Her_SIR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Her-SIR system",
  "source_id": "traitmech:000362",
  "source_file": "gao_her_sir_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_her_sir_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Her_SIR as a two-profile system under the Gao_Her family key. The exact natural host breadth, HerA_SIR2/SIR2 component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_her_sir_system.html#gao-her-sir-mechanism-gap"
 },
 {
  "discussion_id": "gao-her-family-mechanism-gap",
  "prompt": "Resolve Gao_Her natural host breadth, subtype boundaries, phage triggers, and the effector outputs of Gao_Her_DUF and Gao_Her_SIR before minting narrower Gao-Her mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Her system",
  "source_id": "traitmech:000409",
  "source_file": "gao_her_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_her_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support bacteriophage protection by widespread antiviral gene cassettes, and DefenseFinder models Gao_Her_DUF and Gao_Her_SIR as two-profile subsystems under the Gao_Her family key. This first parent record captures the Gao_Her family while leaving subtype-specific triggers, natural host breadth, and direct effector activities unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_her_system.html#gao-her-family-mechanism-gap"
 },
 {
  "discussion_id": "gao-hhe-mechanism-gap",
  "prompt": "Resolve Gao_Hhe natural hosts, HheA component function, phage triggers, and effector activity before minting narrower Gao_Hhe mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Hhe system",
  "source_id": "traitmech:000353",
  "source_file": "gao_hhe_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_hhe_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Hhe as a single-profile system. The exact natural host breadth, HheA component identity, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_hhe_system.html#gao-hhe-mechanism-gap"
 },
 {
  "discussion_id": "gao-iet-mechanism-gap",
  "prompt": "Resolve Gao_Iet natural hosts, IetA/IetS component functions, phage triggers, and effector activity before minting narrower Gao_Iet mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Iet system",
  "source_id": "traitmech:000354",
  "source_file": "gao_iet_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_iet_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Iet as a two-profile system. The exact natural host breadth, Iet component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_iet_system.html#gao-iet-mechanism-gap"
 },
 {
  "discussion_id": "gao-mza-mechanism-gap",
  "prompt": "Resolve Gao_Mza natural hosts, MzaA/MzaB/MzaC/MzaD/MzaE component functions, phage triggers, and effector activity before minting narrower Gao_Mza mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Mza system",
  "source_id": "traitmech:000355",
  "source_file": "gao_mza_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_mza_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Mza as a five-profile system. The exact natural host breadth, Mza component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_mza_system.html#gao-mza-mechanism-gap"
 },
 {
  "discussion_id": "gao-ppl-mechanism-gap",
  "prompt": "Resolve Gao_Ppl natural hosts, PplA component function, phage triggers, and effector activity before minting narrower Gao_Ppl mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Ppl system",
  "source_id": "traitmech:000356",
  "source_file": "gao_ppl_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_ppl_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Ppl as a single-profile system. The exact natural host breadth, PplA component identity, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_ppl_system.html#gao-ppl-mechanism-gap"
 },
 {
  "discussion_id": "gao-qat-mechanism-gap",
  "prompt": "Resolve Gao_Qat natural hosts, Qat component functions, phage triggers, and effector activity before minting narrower Gao_Qat mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Qat system",
  "source_id": "traitmech:000359",
  "source_file": "gao_qat_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_qat_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Qat as a four-profile system. The exact natural host breadth, QatA/QatB/QatC/QatD component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_qat_system.html#gao-qat-mechanism-gap"
 },
 {
  "discussion_id": "gao-rl-mechanism-gap",
  "prompt": "Resolve Gao_RL natural hosts, RL_A/RL_B/RL_C/RL_D component functions, phage triggers, and effector activity before minting narrower Gao_RL mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-RL system",
  "source_id": "traitmech:000352",
  "source_file": "gao_rl_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_rl_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_RL as a four-profile system. The exact natural host breadth, RL component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_rl_system.html#gao-rl-mechanism-gap"
 },
 {
  "discussion_id": "gao-tery-mechanism-gap",
  "prompt": "Resolve Gao_TerY natural hosts, TerY component functions, phage triggers, and effector activity before minting narrower Gao_TerY mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-TerY system",
  "source_id": "traitmech:000360",
  "source_file": "gao_tery_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_tery_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_TerY as a three-profile system. The exact natural host breadth, TerYA/TerYB/TerYC component identities, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_tery_system.html#gao-tery-mechanism-gap"
 },
 {
  "discussion_id": "gao-tmn-mechanism-gap",
  "prompt": "Resolve Gao_Tmn natural hosts, TmnA component function, phage triggers, and effector activity before minting narrower Gao_Tmn mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Tmn system",
  "source_id": "traitmech:000357",
  "source_file": "gao_tmn_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_tmn_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Tmn as a single-profile system. The exact natural host breadth, TmnA component identity, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_tmn_system.html#gao-tmn-mechanism-gap"
 },
 {
  "discussion_id": "gao-upx-mechanism-gap",
  "prompt": "Resolve Gao_Upx natural hosts, UpxA component function, phage triggers, and effector activity before minting narrower Gao_Upx mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Gao-Upx system",
  "source_id": "traitmech:000358",
  "source_file": "gao_upx_system.yaml",
  "attaches_to": [
   "causal_graphs#gao_upx_locus_restricts_phage"
  ],
  "rationale": "Gao et al. support widespread antiviral gene cassettes that mediate protection against specific bacteriophages, and DefenseFinder models Gao_Upx as a single-profile system. The exact natural host breadth, UpxA component identity, phage trigger, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gao_upx_system.html#gao-upx-mechanism-gap"
 },
 {
  "discussion_id": "gaps1-trigger-sibling-gap",
  "prompt": "Resolve GAPS1 component activity and natural-host exemplars before minting narrower GAPS traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GAPS1 system",
  "source_id": "traitmech:000371",
  "source_file": "gaps1_system.yaml",
  "attaches_to": [
   "causal_graphs#gaps1_capsid_triggered_dormancy"
  ],
  "rationale": "Mahata et al. support GAPS1 as one GMT-island anti-phage defense system triggered by a phage capsid protein to induce cell dormancy, and DefenseFinder represents GAPS1 as one GAPS1__GAPS1 profile. This first system-level record does not assert the GAPS1 component's molecular activity, the capsid trigger identity, or a universal GAPS1 host range.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "DOI:10.1038/s41564-024-01840-5",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gaps1_system.html#gaps1-trigger-sibling-gap"
 },
 {
  "discussion_id": "gaps2-mechanism-gap",
  "prompt": "Resolve GAPS2 natural host breadth, BRCT-domain activity, phage trigger specificity, and exact GAPS2__GAPS2 profile-to-protein correspondence before minting narrower GAPS2 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GAPS2 system",
  "source_id": "traitmech:000380",
  "source_file": "gaps2_system.yaml",
  "attaches_to": [
   "causal_graphs#gaps2_locus_restricts_phages"
  ],
  "rationale": "Mahata et al. support GAPS2 as a GMT-encoded anti-phage defense system that protects E. coli against P1-vir and lambda-vir when expressed from a Vibrio parahaemolyticus locus, and DefenseFinder represents GAPS2 as a single-profile system. Natural host breadth, BRCT-domain activity, the phage trigger, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps2.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gaps2_system.html#gaps2-mechanism-gap"
 },
 {
  "discussion_id": "gaps4-mechanism-gap",
  "prompt": "Resolve GAPS4 natural host breadth, lambda-vir host-DNA-degradation triggers, abortive-infection mechanism, and exact GAPS4a/GAPS4b profile-to-protein correspondence before minting narrower GAPS4 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GAPS4 system",
  "source_id": "traitmech:000379",
  "source_file": "gaps4_system.yaml",
  "attaches_to": [
   "causal_graphs#gaps4_locus_restricts_phages"
  ],
  "rationale": "Mahata et al. support GAPS4 as a GMT-encoded anti-phage defense system that protects E. coli against T7, T4, P1-vir, and lambda-vir when expressed from a Vibrio parahaemolyticus locus, and DefenseFinder represents GAPS4 as a two-profile system. Natural host breadth, the lambda-vir-specific trigger of host DNA degradation, the abortive-infection mechanism, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps4.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gaps4_system.html#gaps4-mechanism-gap"
 },
 {
  "discussion_id": "gaps6-mechanism-gap",
  "prompt": "Resolve GAPS6 natural host breadth, GAPS6a activity, GAPS6b sufficiency and trigger specificity, and exact GAPS6a/GAPS6b profile-to-protein correspondence before minting narrower GAPS6 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GAPS6 system",
  "source_id": "traitmech:000381",
  "source_file": "gaps6_system.yaml",
  "attaches_to": [
   "causal_graphs#gaps6_locus_restricts_phages"
  ],
  "rationale": "Mahata et al. support GAPS6 as a GMT-encoded anti-phage defense system that protects E. coli against T7, T4, P1-vir, and lambda-vir when expressed from a Vibrio parahaemolyticus locus, and DefenseFinder represents GAPS6 as a two-profile system. Natural host breadth, GAPS6a activity, GAPS6b sufficiency, the phage trigger, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps6.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps6.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps6.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/gaps6.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gaps6_system.html#gaps6-mechanism-gap"
 },
 {
  "discussion_id": "gasdermin-family-breadth-and-card-nlr-scope-gap",
  "prompt": "Resolve natural GasderMIN family breadth and CARD-NLR gasdermin context before minting narrower gasdermin subfamily traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GasderMIN system",
  "source_id": "traitmech:000336",
  "source_file": "gasdermin_system.yaml",
  "attaches_to": [
   "causal_graphs#gasdermin_proteolysis_triggers_pore_cell_death"
  ],
  "rationale": "Johnson et al. experimentally tested a Lysobacter bGSDM-containing operon and mechanistically dissected Runella bGSDM protease-triggered toxicity, while some bacterial gasdermins showed no discernible phage restriction in Escherichia coli and the GasderMIN__bGSDM profile is also used in CARD-NLR detector contexts in the pinned DefenseFinder rules table. This record captures the standalone GasderMIN detector namespace and leaves CARD-NLR-associated gasdermins, natural phage triggers, and broader family boundaries unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gasdermin_system.html#gasdermin-family-breadth-and-card-nlr-scope-gap"
 },
 {
  "discussion_id": "geb-mechanism-gap",
  "prompt": "Resolve Geb phage triggers and effector outputs before minting narrower Geb mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Geb system",
  "source_id": "traitmech:000287",
  "source_file": "geb_system.yaml",
  "attaches_to": [
   "causal_graphs#geb_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Geb as a named anti-phage system with GebA1 and GebA2 HMM profile entries, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/geb_system.html#geb-mechanism-gap"
 },
 {
  "discussion_id": "gmrsd-defensefinder-model-gap",
  "prompt": "Resolve exact GmrS/GmrD domain activities, complete sugar-modified HMC substrate breadth, split-versus-fused host breadth, phage IPI inhibition, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower GmrSD mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "GmrSD system",
  "source_id": "traitmech:000506",
  "source_file": "gmrsd_system.yaml",
  "attaches_to": [
   "causal_graphs#gmrsd_restricts_glucosylated_hmc_dna"
  ],
  "rationale": "Bair and Black support split GmrS/GmrD as a Type IV modification-dependent restriction nuclease that targets glucosylated hydroxymethylcytosine DNA, Machnicka et al. support GmrSD homologs as either split or fused double-domain systems, and the pinned DefenseFinder article registry maps GmrSD_RM_Type_IV to Bair and Black. The pinned HMM inventory and rules table have no exact GmrSD or GmrSD_RM_Type_IV rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact split-versus-fused prevalence across natural hosts, the complete set of sugar-modified HMC targets, the exact domain contributions of GmrS and GmrD, or the relationship between phage IPI inhibition and the organism-level GmrSD system trait.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1016/j.jmb.2006.11.051",
   "DOI:10.1016/j.jmb.2006.11.051",
   "DOI:10.1186/s12859-015-0773-z",
   "DOI:10.1186/s12859-015-0773-z",
   "DOI:10.1186/s12859-015-0773-z",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/gmrsd_system.html#gmrsd-defensefinder-model-gap"
 },
 {
  "discussion_id": "hachiman-subtype-and-trigger-gap",
  "prompt": "Resolve Hachiman subtype effectors, DNA substrates, and activation triggers before minting narrower Hachiman mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hachiman system",
  "source_id": "traitmech:000219",
  "source_file": "hachiman_system.yaml",
  "attaches_to": [],
  "rationale": "Tuck et al. support DNA-damage-triggered type I-A HamAB activation and Cui et al. support type I-B HamAB ATPase and DNA-cleavage activity, but Hachiman variants need separate review before TraitMech asserts one universal triggering DNA substrate, HamA catalytic domain, HamC accessory role, Cap4 fusion architecture, phage range, or abortive-infection output.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hachiman_system.html#hachiman-subtype-and-trigger-gap"
 },
 {
  "discussion_id": "hailong-mechanism-and-family-breadth-gap",
  "prompt": "Resolve Hailong ODA transfer, phage-trigger breadth, HalA ion specificity, and family architecture before minting narrower Hailong mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hailong system",
  "source_id": "traitmech:000242",
  "source_file": "hailong_system.yaml",
  "attaches_to": [],
  "rationale": "Tan et al. support HalB oligodeoxyadenylate synthesis, HalA repression by inhibitory DNA signals, and viral DNA-exonuclease-triggered release of HalA effector function, but Hailong homologs need separate review before TraitMech asserts one complete ODA-transfer pathway, phage nuclease trigger, HalA ion selectivity, host-processing factor, or ancillary-gene architecture across the full Hailong family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hailong_system.html#hailong-mechanism-and-family-breadth-gap"
 },
 {
  "discussion_id": "hec-02-defensefinder-model-gap",
  "prompt": "Resolve HEC-02 native host breadth, exact HEC-02A/HEC-02B component functions, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower HEC-02 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-02 system",
  "source_id": "traitmech:000417",
  "source_file": "hec_02_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_02_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-02 as an Hma-embedded candidate anti-phage system whose two genes are both required for defense, and the pinned DefenseFinder HMM inventory records HEC-02A and HEC-02B profile rows. The pinned rules table has no HEC-02 row, and the first-pass record does not yet resolve natural host breadth, HEC-02 profile-to-component mapping, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_02_system.html#hec-02-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-03-defensefinder-model-gap",
  "prompt": "Resolve HEC-03 native host breadth, exact HEC-03A/HEC-03B component functions, sensitive-phage breadth, molecular output, and rule-level detection criteria before minting narrower HEC-03 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-03 system",
  "source_id": "traitmech:000418",
  "source_file": "hec_03_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_03_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-03 as an Hma-embedded candidate anti-phage system whose two genes are both required for defense, and the pinned DefenseFinder HMM inventory records HEC-03A and HEC-03B profile rows. The pinned rules table has no HEC-03 row, and the first-pass record does not yet resolve natural host breadth, HEC-03 profile-to-component mapping, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_03_system.html#hec-03-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-04-defensefinder-model-gap",
  "prompt": "Resolve HEC-04 native host breadth, sensitive-phage breadth, ATPase-TOPRIM molecular output, and rule-level detection criteria before minting narrower HEC-04 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-04 system",
  "source_id": "traitmech:000465",
  "source_file": "hec_04_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_04_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-04 as a single-gene Hma-embedded candidate anti-phage system whose ABC ATPase and nuclease domains are both required for defense, and the pinned DefenseFinder HMM inventory records one HEC-04 profile row. The pinned rules table has no HEC-04 row, and the first-pass record does not yet resolve natural host breadth, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_04_system.html#hec-04-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-05-defensefinder-model-gap",
  "prompt": "Resolve HEC-05 native host breadth, sensitive-phage breadth, BrxU synonymy, GmrSD-like molecular output, and rule-level detection criteria before minting narrower HEC-05 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-05 system",
  "source_id": "traitmech:000466",
  "source_file": "hec_05_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_05_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-05 as a single-gene Hma-embedded candidate anti-phage system closely matching BrxU, and the pinned DefenseFinder HMM inventory records one HEC-05 profile row. The pinned rules table has no HEC-05 row, and the first-pass record does not yet resolve natural host breadth, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_05_system.html#hec-05-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-06-defensefinder-model-gap",
  "prompt": "Resolve HEC-06 native host breadth, sensitive-phage breadth, GmrSD-like molecular output, and rule-level detection criteria before minting narrower HEC-06 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-06 system",
  "source_id": "traitmech:000467",
  "source_file": "hec_06_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_06_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-06 as a single-gene Hma-embedded candidate anti-phage system encoding a GmrSD-like protein, and the pinned DefenseFinder HMM inventory records one HEC-06 profile row. The pinned rules table has no HEC-06 row, and the first-pass record does not yet resolve natural host breadth, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_06_system.html#hec-06-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-07-defensefinder-model-gap",
  "prompt": "Resolve HEC-07 native host breadth, sensitive-phage breadth, RelE-domain molecular output, and rule-level detection criteria before minting narrower HEC-07 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-07 system",
  "source_id": "traitmech:000478",
  "source_file": "hec_07_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_07_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-07 as a single-gene Hma-embedded candidate anti-phage system encoding a RelE-domain protein, and the pinned DefenseFinder HMM inventory records one HEC-07 profile row. The pinned rules table has no HEC-07 row, and the first-pass record does not yet resolve natural host breadth, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_07_system.html#hec-07-defensefinder-model-gap"
 },
 {
  "discussion_id": "hec-08-defensefinder-model-gap",
  "prompt": "Resolve HEC-08 native host breadth, sensitive-phage breadth, HEPN-domain molecular output, and rule-level detection criteria before minting narrower HEC-08 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "HEC-08 system",
  "source_id": "traitmech:000479",
  "source_file": "hec_08_system.yaml",
  "attaches_to": [
   "causal_graphs#hec_08_locus_reduces_phage_plaquing"
  ],
  "rationale": "Payne et al. support HEC-08 as a single-gene Hma-embedded candidate anti-phage system encoding a HEPN-domain protein, and the pinned DefenseFinder HMM inventory records one HEC-08 profile row. The pinned rules table has no HEC-08 row, and the first-pass record does not yet resolve natural host breadth, phage target breadth, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1101/2024.01.29.577857",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hec_08_system.html#hec-08-defensefinder-model-gap"
 },
 {
  "discussion_id": "hesat-mechanism-gap",
  "prompt": "Resolve Hesat phage triggers and effector outputs before minting narrower Hesat mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hesat system",
  "source_id": "traitmech:000327",
  "source_file": "hesat_system.yaml",
  "attaches_to": [
   "causal_graphs#hesat_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al. and DefenseFinder support Hesat as a named single-gene anti-phage system, but the direct trigger, experimentally validated molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hesat_system.html#hesat-mechanism-gap"
 },
 {
  "discussion_id": "hma-defensefinder-rule-and-component-gap",
  "prompt": "Resolve HmaB/HmaC contributions, complete HmaABC system requirements, hma-region accessory systems, sensitive-phage breadth, native host breadth, and DefenseFinder rule-level criteria before minting Hma mechanism or component children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hma system",
  "source_id": "traitmech:000533",
  "source_file": "hma_system.yaml",
  "attaches_to": [
   "causal_graphs#hma_locus_phage_defense"
  ],
  "rationale": "Payne et al. predicted Hma as a three-gene candidate defense system, Liu et al. showed that the HmaA nuclease domain is essential for T4 phage defense, and the pinned DefenseFinder HMM inventory records HmaA, HmaB, and HmaC profiles. However, Liu et al. state that HmaB/HmaC regulation of HmaA was not known, and the pinned DefenseFinder rules table lacks an Hma row. This first-pass record therefore does not resolve exact HmaB or HmaC activities, complete-system genetic requirements, accessory defense systems inserted near hma, full sensitive-phage breadth, endogenous native-host activity, or reusable rule-level detection criteria.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1093/nar/gkab883",
   "DOI:10.1111/1751-7915.14524",
   "DOI:10.1111/1751-7915.14524",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hma_system.html#hma-defensefinder-rule-and-component-gap"
 },
 {
  "discussion_id": "hna-trigger-and-family-breadth-gap",
  "prompt": "Resolve Hna trigger breadth, phage escape routes, and family architecture before minting narrower Hna mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hna system",
  "source_id": "traitmech:000241",
  "source_file": "hna_system.yaml",
  "attaches_to": [],
  "rationale": "Sather et al. support Sinorhizobium Hna abortive infection after phage infection or phage SSB expression, and Hooper et al. support 5A SSB stimulation of nuclease activation, but Hna homologs need separate review before TraitMech asserts one universal phage trigger, ATP-dependent activation gate, DNA substrate, escape route, or host death timing across the full Hna family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hna_system.html#hna-trigger-and-family-breadth-gap"
 },
 {
  "discussion_id": "hypnos-mechanism-gap",
  "prompt": "Resolve Hypnos phage triggers and effector outputs before minting narrower Hypnos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Hypnos system",
  "source_id": "traitmech:000309",
  "source_file": "hypnos_system.yaml",
  "attaches_to": [
   "causal_graphs#hypnos_locus_restricts_phage"
  ],
  "rationale": "van den Berg et al. and DefenseFinder support Hypnos as a named anti-phage system with a Hypnos__HyoA HMM profile entry, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/hypnos_system.html#hypnos-mechanism-gap"
 },
 {
  "discussion_id": "ig-like-schlafen-defensefinder-profile-gap",
  "prompt": "Resolve exact pSlfn5 family boundaries, natural host exemplars, T5-like tail chaperone trigger breadth, and DefenseFinder HMM/rules coverage before minting narrower Ig-like Schlafen mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ig-like Schlafen system",
  "source_id": "traitmech:000508",
  "source_file": "ig_like_schlafen_system.yaml",
  "attaches_to": [
   "causal_graphs#ig_like_schlafen_trna_cleavage"
  ],
  "rationale": "Perez Taboada et al. support prokaryotic Schlafen nucleases as widespread antiviral effectors and experimentally characterize the Ig-like RorSlfn5 nuclease as a T5-like tail chaperone-triggered tRNase, and the pinned DefenseFinder article registry maps the Shlafen_Ig-like key to the same article. The pinned HMM inventory and rules table have no exact Schlafen rows. This first-pass record therefore does not resolve exact pSlfn5 family boundaries, natural host exemplars, accession-level Schlafen proteins, full phage trigger breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ig_like_schlafen_system.html#ig-like-schlafen-defensefinder-profile-gap"
 },
 {
  "discussion_id": "ice-family-resolution-gap",
  "prompt": "Resolve bacterial ICE subfamilies, Actinomycete ICE boundaries, integrase/relaxase/T4SS signatures, and cargo-phenotype scope before minting narrower ICE mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "integrative conjugative element",
  "source_id": "traitmech:000410",
  "source_file": "integrative_conjugative_element.yaml",
  "attaches_to": [
   "causal_graphs#ice_excision_conjugation_integration"
  ],
  "rationale": "Johnson and Grossman define ICEs by host-genome integration and a functional type IV secretion conjugation system, while Bioteau et al. classify ICEs as self-transmissible genomic islands. This first record captures the genome-level possession trait without claiming exact molecular groundings for heterogeneous integrases, relaxases, T4SS variants, Actinomycete ICE machinery, or adaptive cargo phenotypes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/integrative_conjugative_element.html#ice-family-resolution-gap"
 },
 {
  "discussion_id": "jukab-vesicle-effector-family-gap",
  "prompt": "Resolve JukB vesicle-destabilization chemistry and the boundaries of other JukA-containing systems before minting narrower mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "JukAB system",
  "source_id": "traitmech:000305",
  "source_file": "jukab_system.yaml",
  "attaches_to": [
   "causal_graphs#jukab_recruits_effector_to_block_jumbo_phage"
  ],
  "rationale": "Li et al. resolve gp241/EPI-vesicle sensing by JukA and direct recruitment of JukB as a two-component JukAB strategy, but the exact chemistry of JukB-mediated vesicle destabilization and the relationship between canonical JukAB and JukA homologs paired with diverse other putative effectors still need narrower review.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/jukab_system.html#jukab-vesicle-effector-family-gap"
 },
 {
  "discussion_id": "kamadhenu-mechanism-gap",
  "prompt": "Resolve Kamadhenu phage triggers and effector outputs before minting narrower Kamadhenu mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Kamadhenu system",
  "source_id": "traitmech:000310",
  "source_file": "kamadhenu_system.yaml",
  "attaches_to": [
   "causal_graphs#kamadhenu_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al., Mosterd et al., and DefenseFinder support Kamadhenu as a named anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/kamadhenu_system.html#kamadhenu-mechanism-gap"
 },
 {
  "discussion_id": "kiwa-activation-and-counterdefense-gap",
  "prompt": "Resolve Kiwa activation, phage counter-defense, and RecBCD-rescue details before minting narrower Kiwa mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Kiwa system",
  "source_id": "traitmech:000231",
  "source_file": "kiwa_system.yaml",
  "attaches_to": [],
  "rationale": "Zhang et al. support a KwaA/KwaB membrane-associated antiviral supercomplex and also describe the phage Gam DNA-mimic counter-defense and RecBCD-dependent restoration of Kiwa protection, but the first TraitRecord stays at the system level until separate review resolves the activation conformational change, exact DNA-binding state, phage counter-defense breadth, and RecBCD connection.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/kiwa_system.html#kiwa-activation-and-counterdefense-gap"
 },
 {
  "discussion_id": "kongming-profile-host-and-component-gap",
  "prompt": "Resolve Kongming natural host breadth, exact locus composition, phage nucleotide-kinase inputs, KomA/KomB/KomC profile boundaries, and DefenseFinder HMM/rule coverage before minting narrower Kongming mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Kongming system",
  "source_id": "traitmech:000501",
  "source_file": "kongming_system.yaml",
  "attaches_to": [
   "causal_graphs#kongming_ditp_nadase_defense"
  ],
  "rationale": "Zeng et al. support a bacterial antiphage system that uses system-encoded adenosine deaminase and phage nucleotide kinases to produce dITP messengers, and Li et al. connect the named Kongming system to dITP-driven activation of the KomBC NADase effector. The pinned DefenseFinder article registry maps the Kongming source key to the Zeng et al. Science paper, but the pinned HMM inventory and rules table have no exact Kongming rows. This first-pass record therefore does not resolve the complete locus model, direct HMM/profile mapping, or native host breadth.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1126/science.ads6055",
   "DOI:10.1038/s41467-026-74710-9",
   "DOI:10.1038/s41467-026-74710-9",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/kongming_system.html#kongming-profile-host-and-component-gap"
 },
 {
  "discussion_id": "lamassu-subtype-and-effector-gap",
  "prompt": "Resolve Lamassu subtype architecture, effector diversity, and viral-DNA trigger specificity before minting narrower Lamassu mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Lamassu system",
  "source_id": "traitmech:000232",
  "source_file": "lamassu_system.yaml",
  "attaches_to": [],
  "rationale": "Haudiquet et al. support a structurally characterized Vibrio cholerae Lamassu Vc-Cap4 system with LmuABC DNA-end sensing and LmuA Cap4 nuclease activation, but the first TraitRecord stays at the system level until separate review resolves long-versus-short LmuB clades, LmuC-independent subfamilies, effector-domain diversity, viral DNA triggers, and cell-death outputs across Lamassu loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/lamassu_system.html#lamassu-subtype-and-effector-gap"
 },
 {
  "discussion_id": "lanthivirin-defensefinder-model-gap",
  "prompt": "Resolve Lanthiphage HMM-to-component coverage, rule-level detection criteria, sensitive-phage breadth, and exact lanthivirin effector identity before minting narrower lanthivirin mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "lanthivirin system",
  "source_id": "traitmech:000416",
  "source_file": "lanthivirin_system.yaml",
  "attaches_to": [
   "causal_graphs#lanthivirin_bgc_inhibits_phage_dna_replication"
  ],
  "rationale": "Serra et al. support lanthivirin biosynthetic gene clusters as anti-phage systems, and the pinned DefenseFinder HMM inventory records Lanthiphage profile rows. The pinned rules table has no Lanthiphage row, and the first-pass record does not yet resolve exact profile-to-component mapping, full native host breadth, phage target breadth, or the direct mature lanthivirin effector.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2026.06.017",
   "DOI:10.1016/j.chom.2026.06.017",
   "DOI:10.1016/j.chom.2026.06.017",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/lanthivirin_system.html#lanthivirin-defensefinder-model-gap"
 },
 {
  "discussion_id": "lit-mechanism-gap",
  "prompt": "Resolve natural Lit loci, host breadth beyond Escherichia coli K-12 e14, Gol-activation contexts, and Lit__Lit profile-to-activity mapping before minting narrower Lit mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Lit system",
  "source_id": "traitmech:000363",
  "source_file": "lit_system.yaml",
  "attaches_to": [
   "causal_graphs#lit_locus_restricts_t4_phage"
  ],
  "rationale": "Copeland et al. support the T4-triggered e14 Lit peptidase as a bacteriophage-exclusion determinant, Uzan et al. summarize Gol-Lit as a T4 phage-exclusion system, and DefenseFinder models Lit as a single-profile system. The natural host breadth and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/lit_system.html#lit-mechanism-gap"
 },
 {
  "discussion_id": "lugos-mechanism-gap",
  "prompt": "Resolve Lugos phage triggers and effector outputs before minting narrower Lugos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Lugos system",
  "source_id": "traitmech:000283",
  "source_file": "lugos_system.yaml",
  "attaches_to": [
   "causal_graphs#lugos_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Lugos as a named anti-phage system with a VCA0409 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/lugos_system.html#lugos-mechanism-gap"
 },
 {
  "discussion_id": "mads-profile-activity-gap",
  "prompt": "Resolve MADS subtype boundaries, MADS3-4 relationships, and Mad1-Mad8 profile-to-activity mappings before minting narrower MADS mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MADS system",
  "source_id": "traitmech:000370",
  "source_file": "mads_system.yaml",
  "attaches_to": [
   "causal_graphs#mads_methylation_restricts_phage"
  ],
  "rationale": "Maestri et al. support MADS as a methylation-associated defense system active against DNA phages, and DefenseFinder models MADS as an eight-profile rule. The pinned model does not resolve which combinations of MADS__mad profiles correspond to methylation, specificity, nuclease, ATPase, or kinase activities, so this first record stays at system level.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2024.07.005",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mads_system.html#mads-profile-activity-gap"
 },
 {
  "discussion_id": "mazef-activation-breadth-gap",
  "prompt": "Resolve MazEF activation, direct MazF RNA targets, and RNA- versus DNA-phage breadth before minting narrower MazEF mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MazEF system",
  "source_id": "traitmech:000345",
  "source_file": "mazef_system.yaml",
  "attaches_to": [
   "causal_graphs#mazef_rna_phage_defense"
  ],
  "rationale": "Nikolic et al. support native MazEF protection against RNA phages and argue that direct interference predominates in those assays, but the phage-induced route to active MazF, the relative contributions of phage-RNA cleavage and host-RNA degradation, the breadth of MazEF DNA-phage defense, and the DefenseFinder MazEF model boundaries remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mazef_system.html#mazef-activation-breadth-gap"
 },
 {
  "discussion_id": "mcrbc-defensefinder-model-gap",
  "prompt": "Resolve exact McrB/McrC component activities, complete modified-cytosine target breadth, natural host breadth, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower McrBC mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "McrBC system",
  "source_id": "traitmech:000505",
  "source_file": "mcrbc_system.yaml",
  "attaches_to": [
   "causal_graphs#mcrbc_restricts_methylated_cytosine_dna"
  ],
  "rationale": "Panne et al. support McrBC from Escherichia coli K-12 as a restriction endonuclease complex that cuts DNA containing modified cytosines, and Loenen and Raleigh place mcrBC in the modified-cytosine restriction branch of Type IV modification-dependent restriction systems. The pinned DefenseFinder article registry maps the McrBC source key to Panne et al., but the pinned HMM inventory and rules table have no exact McrBC rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, the exact relationship between individual McrB and McrC molecular functions and organism-level McrBC possession, the complete set of modified-cytosine targets, or the natural host breadth of McrBC systems.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1093/emboj/20.12.3210",
   "DOI:10.1093/emboj/20.12.3210",
   "DOI:10.1093/emboj/20.12.3210",
   "DOI:10.1093/nar/gkt747",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mcrbc_system.html#mcrbc-defensefinder-model-gap"
 },
 {
  "discussion_id": "menshen-mechanism-gap",
  "prompt": "Resolve Menshen phage triggers and effector outputs before minting narrower Menshen mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Menshen system",
  "source_id": "traitmech:000253",
  "source_file": "menshen_system.yaml",
  "attaches_to": [
   "causal_graphs#menshen_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Menshen as a named anti-phage system with NsnA, NsnB, and NsnC profile choices, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/menshen_system.html#menshen-mechanism-gap"
 },
 {
  "discussion_id": "metis-subtype-and-model-coverage-gap",
  "prompt": "Resolve Metis type I and type II locus composition, native host breadth, profile-to-component mapping, subtype-specific effector biochemistry, and DefenseFinder HMM/rule coverage before minting narrower Metis mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Metis system",
  "source_id": "traitmech:000502",
  "source_file": "metis_system.yaml",
  "attaches_to": [
   "causal_graphs#metis_m6damp_toxic_effector_defense"
  ],
  "rationale": "Osterman et al. support Metis as a bacterial defense system that senses m6dAMP from phage-mediated host-genome degradation and activates type-specific toxic effectors. The pinned DefenseFinder article registry maps the Metis source key to the Osterman et al. preprint, but the pinned HMM inventory and rules table have no exact Metis rows. This first-pass record therefore does not resolve the complete locus model, subtype component boundaries, direct HMM/profile mapping, or native host breadth.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1126/science.aed6782",
   "DOI:10.1126/science.aed6782",
   "DOI:10.1126/science.aed6782",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/metis_system.html#metis-subtype-and-model-coverage-gap"
 },
 {
  "discussion_id": "mksbefg-activation-and-substrate-gap",
  "prompt": "Resolve MksBEFG plasmid substrate breadth, MksBEF ATPase-to-MksG coupling, MksG activation state, and accession-level protein examples before minting narrower MksBEFG mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MksBEFG system",
  "source_id": "traitmech:000526",
  "source_file": "mksbefg_system.yaml",
  "attaches_to": [
   "causal_graphs#mksbefg_degrades_plasmid_dna"
  ],
  "rationale": "Weiss et al. support MksBEFG as a bacterial plasmid-defense system with an MksBEF ATPase core and MksG plasmid-DNA-degradation nuclease, and Liu et al. place MksBEFG in the broader Wadjet derivative-SMC family. This first-pass record leaves exact plasmid substrate breadth, MksBEF-to-MksG coupling, cellular MksG loading, and accession-level component examples unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1093/nar/gkad130",
   "DOI:10.1093/nar/gkad130",
   "DOI:10.1093/nar/gkad130",
   "DOI:10.1093/nar/gkad130",
   "DOI:10.1016/j.molcel.2022.11.015"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mksbefg_system.html#mksbefg-activation-and-substrate-gap"
 },
 {
  "discussion_id": "mmb_gp29_gp30-mechanism-gap",
  "prompt": "Resolve the MMB gp29 biochemical activity, MMB gp30 regulatory role, lytic trigger, gp29-gp30 interaction, counter-defense specificity, and homolog breadth before minting narrower MMB gp29-gp30 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MMB gp29-gp30 system",
  "source_id": "traitmech:000297",
  "source_file": "mmb_gp29_gp30_system.yaml",
  "attaches_to": [
   "causal_graphs#mmb_gp29_gp30_locus_restricts_phage"
  ],
  "rationale": "Dedrick et al. and DefenseFinder support MMB gp29-gp30 as a named anti-phage system with gp29 and gp30 profiles, but the MMB gp29 biochemical activity, direct gp29-gp30 interaction, triggering Tweety early lytic gene or genes, MMB-specific counter-defense tuning, and relationship to Squirty homologs are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mmb_gp29_gp30_system.html#mmb_gp29_gp30-mechanism-gap"
 },
 {
  "discussion_id": "mok-hok-sok-natural-context-gap",
  "prompt": "Resolve the natural host range, Sok antisense-RNA representation, Hok toxin activation, and Hok/Mok profile-to-activity mapping before minting narrower Mok-Hok-Sok mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Mok-Hok-Sok system",
  "source_id": "traitmech:000372",
  "source_file": "mok_hok_sok_system.yaml",
  "attaches_to": [
   "causal_graphs#mok_hok_sok_locus_restricts_t4_phage"
  ],
  "rationale": "Pecota and Wood support T4 exclusion by the plasmid R1 hok/sok locus carried on a pBR322-based plasmid, and DefenseFinder models Mok_Hok_Sok with Hok and Mok protein profiles. This first record leaves the native biological breadth, RNA antitoxin representation, Hok triggering, and profile-to-activity mapping unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mok_hok_sok_system.html#mok-hok-sok-natural-context-gap"
 },
 {
  "discussion_id": "mokosh-mechanism-gap",
  "prompt": "Resolve Mokosh phage triggers and effector outputs before minting narrower Mokosh mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Mokosh system",
  "source_id": "traitmech:000246",
  "source_file": "mokosh_system.yaml",
  "attaches_to": [
   "causal_graphs#mokosh_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Mokosh as a named anti-phage system with type I and type II profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mokosh_system.html#mokosh-mechanism-gap"
 },
 {
  "discussion_id": "mqsrac-breadth-and-profile-gap",
  "prompt": "Resolve MqsRAC natural phage breadth, phage-activation signals, the exact DefenseFinder profile-to-MqsR/MqsA/MqsC relationship, and cooperating restriction/modification contexts before minting narrower MqsRAC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MqsRAC system",
  "source_id": "traitmech:000368",
  "source_file": "mqsrac_system.yaml",
  "attaches_to": [
   "causal_graphs#mqsrac_locus_promotes_persister_phage_defense"
  ],
  "rationale": "Fernandez-Garcia et al. support MqsR/MqsA/MqsC as an Escherichia coli C496_10 toxin-antitoxin-chaperone system that inhibits T2 phage through persister-cell formation and in concert with restriction/modification systems, while DefenseFinder models MqsRAC through MqsRAC__mqsC and MqsRAC__mqsR markers. Natural phage breadth, the phage signal that activates MqsRAC, MqsA coverage in the DefenseFinder model, and cooperating restriction/modification contexts remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:38054715"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mqsrac_system.html#mqsrac-breadth-and-profile-gap"
 },
 {
  "discussion_id": "mspji-defensefinder-model-gap",
  "prompt": "Resolve MspJI-family breadth, methylcytosine and hydroxymethylcytosine sequence-context specificity across natural hosts, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower MspJI mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "MspJI system",
  "source_id": "traitmech:000510",
  "source_file": "mspji_system.yaml",
  "attaches_to": [
   "causal_graphs#mspji_restricts_modified_cytosine_dna"
  ],
  "rationale": "Zheng et al. support MspJI as a methylcytosine- and hydroxymethylcytosine-dependent restriction endonuclease, Cohen-Karni et al. support MspJI homologs as a family of C5-modified-cytosine-dependent restriction endonucleases, and the pinned DefenseFinder article registry maps MspJI to the Cohen-Karni et al. paper. The pinned HMM inventory and rules table have no exact MspJI rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of MspJI-like systems across natural hosts, or the complete set of natural methylcytosine and hydroxymethylcytosine sequence contexts.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1073/pnas.1018448108",
   "DOI:10.1073/pnas.1018448108",
   "DOI:10.1093/nar/gkq327",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/mspji_system.html#mspji-defensefinder-model-gap"
 },
 {
  "discussion_id": "nantosuelta-mechanism-gap",
  "prompt": "Resolve Nantosuelta phage triggers and effector outputs before minting narrower Nantosuelta mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Nantosuelta system",
  "source_id": "traitmech:000284",
  "source_file": "nantosuelta_system.yaml",
  "attaches_to": [
   "causal_graphs#nantosuelta_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Nantosuelta as a named anti-phage system with a VCA0322 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/nantosuelta_system.html#nantosuelta-mechanism-gap"
 },
 {
  "discussion_id": "nemetona-mechanism-gap",
  "prompt": "Resolve Nemetona phage triggers and effector outputs before minting narrower Nemetona mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Nemetona system",
  "source_id": "traitmech:000285",
  "source_file": "nemetona_system.yaml",
  "attaches_to": [
   "causal_graphs#nemetona_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Nemetona as a named anti-phage system with a VCA0441 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/nemetona_system.html#nemetona-mechanism-gap"
 },
 {
  "discussion_id": "nhi-trigger-and-substrate-gap",
  "prompt": "Resolve the Nhi phage trigger, exact replication-intermediate substrate, accession-level natural host protein, and homolog breadth before minting narrower mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Nhi system",
  "source_id": "traitmech:000332",
  "source_file": "nhi_system.yaml",
  "attaches_to": [
   "causal_graphs#nhi_locus_restricts_staphylococcal_phages"
  ],
  "rationale": "Bari et al. support Nhi as a compact single-enzyme nuclease-helicase immunity system that prevents phage DNA accumulation and is inferred to target and degrade phage-specific replication intermediates. DefenseFinder models Nhi with a one-profile rule, but this first system-level record leaves the direct phage trigger, exact substrate, natural-host accession, and full taxonomic breadth of functional homologs unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/nhi_system.html#nhi-trigger-and-substrate-gap"
 },
 {
  "discussion_id": "nixi-stix-and-satellite-scope-gap",
  "prompt": "Resolve NixI satellite self-protection, optional Stix profile scope, natural-host protein accessions, and divergent-homolog activity before minting narrower NixI mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "NixI system",
  "source_id": "traitmech:000333",
  "source_file": "nixi_system.yaml",
  "attaches_to": [
   "causal_graphs#nixi_locus_inhibits_icp1_replication"
  ],
  "rationale": "LeGault et al. support NixI as a PLE-encoded nicking endonuclease that cleaves ICP1 DNA and inhibits ICP1 genome replication, and DefenseFinder models NixI with a required NixI__NixI profile plus optional NixI__Stix. This first system-level record leaves the exact PLE self-protection mechanism, the optional Stix profile's experimental scope, the accession-level PLE1 NixI protein, the breadth of divergent homolog activity, and additional PLE anti-ICP1 mechanisms unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/nixi_system.html#nixi-stix-and-satellite-scope-gap"
 },
 {
  "discussion_id": "nlr-like-bnacht-mechanism-gap",
  "prompt": "Resolve the exact mapping between DefenseFinder NLR_like_bNACHT01 and NLR_like_bNACHT09 profiles and the experimentally tested bNACHT proteins, natural host breadth, phage triggers, and bNACHT effector mechanisms before minting narrower bNACHT subtype traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "NLR-like bNACHT system",
  "source_id": "traitmech:000408",
  "source_file": "nlr_like_bnacht_system.yaml",
  "attaches_to": [
   "causal_graphs#nlr_like_bnacht_loci_restrict_phage"
  ],
  "rationale": "Kibby et al. support bacterial NACHT proteins as NLR-related phage-defense proteins and DefenseFinder models NLR_like_bNACHT01 and NLR_like_bNACHT09 as single-profile NLR-family subsystems. This first system-level record leaves profile-to-assayed-protein correspondence and subtype-specific trigger and effector mechanisms unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/",
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/nlr_like_bnacht_system.html#nlr-like-bnacht-mechanism-gap"
 },
 {
  "discussion_id": "ogmios-mechanism-gap",
  "prompt": "Resolve Ogmios phage triggers and effector outputs before minting narrower Ogmios mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ogmios system",
  "source_id": "traitmech:000286",
  "source_file": "ogmios_system.yaml",
  "attaches_to": [
   "causal_graphs#ogmios_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Ogmios as a named anti-phage system with a VCA0308 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ogmios_system.html#ogmios-mechanism-gap"
 },
 {
  "discussion_id": "old-exonuclease-tin-trigger-mechanism-gap",
  "prompt": "Resolve Old_exonuclease natural host breadth, Tin accessory dependence, RecBCD-triggered activation, profile-to-protein mapping, and lambda interference mechanism before minting narrower Old nuclease mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Old exonuclease system",
  "source_id": "traitmech:000399",
  "source_file": "old_exonuclease_system.yaml",
  "attaches_to": [
   "causal_graphs#old_exonuclease_locus_interferes_with_lambda"
  ],
  "rationale": "The 1995 P2 Old paper supports Old nuclease activity and phage-lambda interference, and DefenseFinder represents Old_exonuclease as a required single-profile model. This first system-level record leaves Tin dependence in the Rousset et al. assay, natural host breadth, RecBCD-linked activation, profile-to-protein mapping, and the exact phage-interference mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1128/jb.177.3.497-501.1995",
   "DOI:10.1128/jb.177.3.497-501.1995",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/old_exonuclease.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/old_exonuclease.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/old_exonuclease_system.html#old-exonuclease-tin-trigger-mechanism-gap"
 },
 {
  "discussion_id": "olokun-mechanism-gap",
  "prompt": "Resolve Olokun phage triggers and effector outputs before minting narrower Olokun mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Olokun system",
  "source_id": "traitmech:000254",
  "source_file": "olokun_system.yaml",
  "attaches_to": [
   "causal_graphs#olokun_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Olokun as a named anti-phage system with OloA and OloB profile choices, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/olokun_system.html#olokun-mechanism-gap"
 },
 {
  "discussion_id": "ophion-jumbo-phage-mechanism-gap",
  "prompt": "Resolve Ophion phage triggers, nucleotide-modification products, and model coverage before minting narrower Ophion mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ophion system",
  "source_id": "traitmech:000331",
  "source_file": "ophion_system.yaml",
  "attaches_to": [
   "causal_graphs#ophion_locus_restricts_phage"
  ],
  "rationale": "Keesman et al. support Ophion as a three-gene anti-jumbo-phage system that blocks progression from the early phage infection vesicle to the phage nucleus, but the direct phage trigger, exact OpnA/OpnB/OpnC interaction sequence, modified nucleotide product, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ophion_system.html#ophion-jumbo-phage-mechanism-gap"
 },
 {
  "discussion_id": "oshun-mechanism-gap",
  "prompt": "Resolve Oshun phage triggers and effector outputs before minting narrower Oshun mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Oshun system",
  "source_id": "traitmech:000293",
  "source_file": "oshun_system.yaml",
  "attaches_to": [
   "causal_graphs#oshun_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Oshun as a named anti-phage system with an OsnA2 HMM profile entry, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/oshun_system.html#oshun-mechanism-gap"
 },
 {
  "discussion_id": "pago-subfamily-boundary-gap",
  "prompt": "Resolve pAgo subfamily boundaries, accessory-protein requirements, and substrate breadth before minting narrower long-pAgo or APAZ-associated defense children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "prokaryotic Argonaute defense system",
  "source_id": "traitmech:000419",
  "source_file": "pago_system.yaml",
  "attaches_to": [
   "causal_graphs#pago_system_family_hierarchy"
  ],
  "rationale": "SPARTA and DdmDE support prokaryotic Argonaute defense systems as a reusable genomics family, and DefenseFinder models a pAgo namespace with long pAgo, SPARTA, and optional APAZ-associated profiles. This parent does not yet resolve whether every DefenseFinder pAgo submodel has the same plasmid or phage substrate range, whether standalone APAZ-associated profiles are exact children, or which native-host examples support each subfamily.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "DOI:10.1016/j.cell.2022.03.012",
   "DOI:10.1038/s41586-024-07515-9",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pago_system.html#pago-subfamily-boundary-gap"
 },
 {
  "discussion_id": "panchino_gp28-mechanism-gap",
  "prompt": "Resolve the Panchino gp28 restriction target, methylation requirements, and homolog breadth before minting narrower Panchino gp28 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Panchino gp28 system",
  "source_id": "traitmech:000294",
  "source_file": "panchino_gp28_system.yaml",
  "attaches_to": [
   "causal_graphs#panchino_gp28_locus_restricts_phage"
  ],
  "rationale": "Dedrick et al. and DefenseFinder support Panchino gp28 as a named anti-phage system with a gp28 profile, but the restriction target, methylation context, and full target-phage breadth are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/panchino_gp28_system.html#panchino_gp28-mechanism-gap"
 },
 {
  "discussion_id": "panoptes-defensefinder-model-gap",
  "prompt": "Recheck DefenseFinder Panoptes rules and HMM profiles before using DefenseFinder model rows as optSE profile evidence.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "Panoptes system",
  "source_id": "traitmech:000407",
  "source_file": "panoptes_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned DefenseFinder article registry maps Panoptes to Sullivan et al. and the Nature article title, but the pinned DefenseFinder rules and HMM inventories do not include Panoptes rows. This record therefore cites the DOI-backed article and treats the article registry as name-to-paper evidence rather than as profile support.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/panoptes_system.html#panoptes-defensefinder-model-gap"
 },
 {
  "discussion_id": "panoptes-natural-host-gap",
  "prompt": "Find a native endogenous microbial isolate with direct chromosomal Panoptes antiphage validation beyond the heterologous VnOptSE source-species exemplar.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Panoptes system",
  "source_id": "traitmech:000407",
  "source_file": "panoptes_system.yaml",
  "attaches_to": [
   "causal_graphs#panoptes_decoy_cyclic_nucleotide_defense"
  ],
  "rationale": "Sullivan et al. investigated a candidate Vibrio navarrensis optSE operon and showed that VnOptSE defended against Straboviridae phages when expressed in E. coli MG1655 from its endogenous promoter. V. navarrensis is retained as the operon source for mechanistic protein examples, but that heterologous challenge assay does not establish a direct endogenous V. navarrensis chromosomal Panoptes assay.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "DOI:10.1038/s41586-025-09557-z",
   "DOI:10.1038/s41586-025-09557-z"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/panoptes_system.html#panoptes-natural-host-gap"
 },
 {
  "discussion_id": "paris-trigger-and-counterdefense-gap",
  "prompt": "Resolve PARIS trigger specificity, AriA/AriB stoichiometry, phage T5 lysine-tRNA suppression, and non-Ocr phage triggers before minting narrower PARIS subtype children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PARIS system",
  "source_id": "traitmech:000237",
  "source_file": "paris_system.yaml",
  "attaches_to": [],
  "rationale": "Rousset et al. discovered PARIS as an abortive infection system triggered by T7 Ocr; Deep et al. resolved Ocr-dependent AriA release of AriB for the E. coli B185 system; and Burman et al. showed that T5 Ptr1 and Ptr2 can activate PARIS while a phage T5 lysine tRNA variant can evade AriB cleavage. The first TraitRecord therefore stays at the broad PARIS-system level until separate subtype review resolves which foreign-protein triggers, AriB activities, and anti-defense suppressors apply across each PARIS family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/paris_system.html#paris-trigger-and-counterdefense-gap"
 },
 {
  "discussion_id": "pd-lambda-1-mechanism-gap",
  "prompt": "Resolve PD-Lambda-1 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-Lambda-1 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-1 system",
  "source_id": "traitmech:000404",
  "source_file": "pd_lambda_1_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_1_locus_restricts_lambda_vir"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-1 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to LambdaVir protection, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-1.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-1.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-1.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_1_system.html#pd-lambda-1-mechanism-gap"
 },
 {
  "discussion_id": "pd-lambda-1-defensefinder-article-registry-gap",
  "prompt": "Recheck whether DefenseFinder adds a PD-Lambda-1 List_system_article.md row before using the article registry as direct PD-Lambda-1 model-to-paper evidence.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "PD-Lambda-1 system",
  "source_id": "traitmech:000404",
  "source_file": "pd_lambda_1_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned DefenseFinder wiki, rules table, and HMM inventory all represent PD-Lambda-1, but the pinned List_system_article.md registry omits a PD-Lambda-1 row. The PD-Lambda-1 record therefore cites the pinned wiki plus the DOI-backed Vassallo et al. screen instead of inventing a missing article-registry entry.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-1.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_1_system.html#pd-lambda-1-defensefinder-article-registry-gap"
 },
 {
  "discussion_id": "pd-lambda-2-mechanism-gap",
  "prompt": "Resolve PD-Lambda-2 natural host breadth, direct phage trigger, effector mechanism, and exact profile-to-protein correspondence before minting narrower PD-Lambda-2 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-2 system",
  "source_id": "traitmech:000378",
  "source_file": "pd_lambda_2_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_2_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-2 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against LambdaVir, SECphi17, SECphi18, SECphi27, and T3, and DefenseFinder represents the system with A, B, and C profiles. Natural host breadth, the direct phage trigger, effector logic, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-2.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_2_system.html#pd-lambda-2-mechanism-gap"
 },
 {
  "discussion_id": "pd-lambda-3-mechanism-gap",
  "prompt": "Resolve PD-Lambda-3 natural host breadth, direct phage trigger, effector mechanism, the third protein in the experimental source locus, and exact profile-to-protein correspondence before minting narrower PD-Lambda-3 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-3 system",
  "source_id": "traitmech:000382",
  "source_file": "pd_lambda_3_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_3_locus_restricts_lambda_vir"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-3 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against LambdaVir, and DefenseFinder represents the system with A and B profiles. Natural host breadth, the direct phage trigger, effector logic, the third protein in the experimental source locus, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-3.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_3_system.html#pd-lambda-3-mechanism-gap"
 },
 {
  "discussion_id": "pd-lambda-4-mechanism-gap",
  "prompt": "Resolve PD-Lambda-4 natural host breadth, direct phage trigger, effector mechanism, and profile-to-protein correspondence before minting narrower PD-Lambda-4 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-4 system",
  "source_id": "traitmech:000384",
  "source_file": "pd_lambda_4_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_4_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-4 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T4, LambdaVir, SECphi27, and T7, and DefenseFinder represents the system with two mandatory profiles. Natural host breadth, the direct phage trigger, effector logic, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-4.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_4_system.html#pd-lambda-4-mechanism-gap"
 },
 {
  "discussion_id": "pd-lambda-5-mechanism-gap",
  "prompt": "Resolve PD-Lambda-5 natural host breadth, direct phage trigger, effector mechanism, and profile-to-protein correspondence before minting narrower PD-Lambda-5 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-5 system",
  "source_id": "traitmech:000385",
  "source_file": "pd_lambda_5_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_5_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-5 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, LambdaVir, SECphi17, SECphi18, SECphi27, T3, and T7, and DefenseFinder represents the system with two mandatory profiles. Natural host breadth, the direct phage trigger, effector logic, and exact profile-to-protein correspondence remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-5.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_5_system.html#pd-lambda-5-mechanism-gap"
 },
 {
  "discussion_id": "pd-lambda-6-mechanism-gap",
  "prompt": "Resolve PD-Lambda-6 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-Lambda-6 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-Lambda-6 system",
  "source_id": "traitmech:000383",
  "source_file": "pd_lambda_6_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_lambda_6_locus_restricts_lambda_vir_and_t5"
  ],
  "rationale": "Vassallo et al. support PD-Lambda-6 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against LambdaVir and T5, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-6.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-lambda-6.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_lambda_6_system.html#pd-lambda-6-mechanism-gap"
 },
 {
  "discussion_id": "pd-t2-1-mechanism-and-model-coverage-gap",
  "prompt": "Resolve the PD-T2-1 direct sensor, effector output, native host breadth, and DefenseFinder HMM/rules model coverage before minting narrower PD-T2-1 mechanism or protein-component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T2-1 system",
  "source_id": "traitmech:000476",
  "source_file": "pd_t2_1_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t2_1_locus_phage_protection"
  ],
  "rationale": "The final Goedecke et al. article supports PD-T2-1 as a two-gene operon activated by multiple phage tail-fiber proteins, links heterologous expression to protection against T2, T6, Bas18, T4, and T5, and argues that the system is not a canonical toxin-antitoxin system. The pinned DefenseFinder article registry names PD-T2-1 and maps it to the Goedecke et al. preprint, but the pinned HMM inventory and rules table do not contain PD-T2-1 rows, leaving profile coverage and detection criteria unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/",
   "https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t2_1_system.html#pd-t2-1-mechanism-and-model-coverage-gap"
 },
 {
  "discussion_id": "pd-t4-10-mechanism-gap",
  "prompt": "Resolve PD-T4-10 natural host breadth, direct phage trigger, the toxic PD-T4-10_B target, and PD-T4-10_A neutralization logic before minting narrower PD-T4-10 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-10 system",
  "source_id": "traitmech:000394",
  "source_file": "pd_t4_10_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_10_locus_restricts_t2_t4_t6_t5_and_secphi27"
  ],
  "rationale": "Vassallo et al. support PD-T4-10 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, T5, and SECphi27, and DefenseFinder represents the system with two mandatory profiles and an abortive-infection mechanism assignment. Natural host breadth, the direct phage trigger, the toxic PD-T4-10_B target, and the PD-T4-10_A neutralization logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-10.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-10.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-10.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_10_system.html#pd-t4-10-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-1-mechanism-gap",
  "prompt": "Resolve PD-T4-1 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-1 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-1 system",
  "source_id": "traitmech:000386",
  "source_file": "pd_t4_1_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_1_locus_restricts_t2_t4_and_t6"
  ],
  "rationale": "Vassallo et al. support PD-T4-1 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, and T6, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-1.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-1.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_1_system.html#pd-t4-1-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-2-mechanism-gap",
  "prompt": "Resolve PD-T4-2 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-2 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-2 system",
  "source_id": "traitmech:000387",
  "source_file": "pd_t4_2_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_2_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-T4-2 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, T5, and SECphi27, and DefenseFinder represents the system with two mandatory profiles. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-2.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_2_system.html#pd-t4-2-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-3-mechanism-gap",
  "prompt": "Resolve PD-T4-3 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-3 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-3 system",
  "source_id": "traitmech:000388",
  "source_file": "pd_t4_3_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_3_locus_restricts_t2_t4_and_t6"
  ],
  "rationale": "Vassallo et al. support PD-T4-3 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, and T6, and DefenseFinder represents the system with one mandatory profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-3.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_3_system.html#pd-t4-3-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-4-mechanism-gap",
  "prompt": "Resolve PD-T4-4 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-4 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-4 system",
  "source_id": "traitmech:000389",
  "source_file": "pd_t4_4_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_4_locus_restricts_t2_t4_t6_and_secphi17"
  ],
  "rationale": "Vassallo et al. support PD-T4-4 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, and SECphi17, and DefenseFinder represents the system with two mandatory profiles. Natural host breadth, the direct phage trigger, and direct effector logic remain unresolved, so the likely abortive-infection hypothesis is left unmodeled.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-4.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_4_system.html#pd-t4-4-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-5-mechanism-gap",
  "prompt": "Resolve PD-T4-5 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-5 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-5 system",
  "source_id": "traitmech:000390",
  "source_file": "pd_t4_5_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_5_locus_restricts_t4_t6_lambdavir_and_t5"
  ],
  "rationale": "Vassallo et al. support PD-T4-5 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T4, T6, LambdaVir, and T5, and DefenseFinder represents the system with one mandatory profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-5.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_5_system.html#pd-t4-5-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-6-mechanism-gap",
  "prompt": "Resolve PD-T4-6 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T4-6 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-6 system",
  "source_id": "traitmech:000391",
  "source_file": "pd_t4_6_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_6_locus_restricts_t2_t4_and_t6"
  ],
  "rationale": "Vassallo et al. support PD-T4-6 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, and T6, and DefenseFinder represents the system with one mandatory profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-6.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-6.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_6_system.html#pd-t4-6-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-7-mechanism-gap",
  "prompt": "Resolve PD-T4-7 natural host breadth, direct phage trigger, and direct abortive-infection effector logic before minting narrower PD-T4-7 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-7 system",
  "source_id": "traitmech:000392",
  "source_file": "pd_t4_7_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_7_locus_restricts_t2_t4_and_t6"
  ],
  "rationale": "Vassallo et al. support PD-T4-7 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, and T6, and DefenseFinder represents the system with one mandatory profile and an abortive-infection mechanism assignment. Natural host breadth, the direct phage trigger, and direct effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-7.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-7.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-7.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_7_system.html#pd-t4-7-mechanism-gap"
 },
 {
  "discussion_id": "pd-t4-8-mechanism-gap",
  "prompt": "Resolve PD-T4-8 natural host breadth, direct phage trigger, and effector logic before minting narrower PD-T4-8 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T4-8 system",
  "source_id": "traitmech:000393",
  "source_file": "pd_t4_8_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t4_8_locus_restricts_t2_t4_t6_secphi18_and_secphi27"
  ],
  "rationale": "Vassallo et al. support PD-T4-8 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, SECphi18, and SECphi27, and DefenseFinder represents the system with one mandatory profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-8.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-8.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t4-8.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t4_8_system.html#pd-t4-8-mechanism-gap"
 },
 {
  "discussion_id": "pd-t7-1-mechanism-gap",
  "prompt": "Resolve PD-T7-1 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T7-1 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T7-1 system",
  "source_id": "traitmech:000395",
  "source_file": "pd_t7_1_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t7_1_locus_restricts_t7"
  ],
  "rationale": "Vassallo et al. support PD-T7-1 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T7, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-1.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-1.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-1.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_1_system.html#pd-t7-1-mechanism-gap"
 },
 {
  "discussion_id": "pd-t7-2-mechanism-gap",
  "prompt": "Resolve PD-T7-2 natural host breadth, direct phage trigger, effector mechanism, and profile-to-protein correspondence before minting narrower PD-T7-2 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T7-2 system",
  "source_id": "traitmech:000396",
  "source_file": "pd_t7_2_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t7_2_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-T7-2 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to broad phage protection, and DefenseFinder represents the system with two profiles. Natural host breadth, the direct phage trigger, exact effector logic, and the exact correspondence between the two profiles and proteins remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-2.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-2.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_2_system.html#pd-t7-2-mechanism-gap"
 },
 {
  "discussion_id": "pd-t7-3-mechanism-gap",
  "prompt": "Resolve PD-T7-3 natural host breadth, direct phage trigger, and effector mechanism before minting narrower PD-T7-3 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T7-3 system",
  "source_id": "traitmech:000405",
  "source_file": "pd_t7_3_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t7_3_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-T7-3 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against T2, T4, T6, T5, SECphi17, T3, and T7, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-3.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-3.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_3_system.html#pd-t7-3-mechanism-gap"
 },
 {
  "discussion_id": "pd-t7-3-defensefinder-article-registry-gap",
  "prompt": "Recheck whether DefenseFinder adds a PD-T7-3 List_system_article.md row before using the article registry as direct PD-T7-3 model-to-paper evidence.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "PD-T7-3 system",
  "source_id": "traitmech:000405",
  "source_file": "pd_t7_3_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned DefenseFinder wiki, rules table, and HMM inventory all represent PD-T7-3, but the pinned List_system_article.md registry omits a PD-T7-3 row. The PD-T7-3 record therefore cites the pinned wiki plus the DOI-backed Vassallo et al. screen instead of inventing a missing article-registry entry.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-3.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_3_system.html#pd-t7-3-defensefinder-article-registry-gap"
 },
 {
  "discussion_id": "pd-t7-4-mechanism-gap",
  "prompt": "Resolve PD-T7-4 natural host breadth, direct phage trigger, and PF13643-associated effector mechanism before minting narrower PD-T7-4 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T7-4 system",
  "source_id": "traitmech:000406",
  "source_file": "pd_t7_4_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t7_4_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-T7-4 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against SECphi18, SECphi27, T3, and T7, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and effector logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-4.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-4.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_4_system.html#pd-t7-4-mechanism-gap"
 },
 {
  "discussion_id": "pd-t7-4-defensefinder-article-registry-gap",
  "prompt": "Recheck whether DefenseFinder adds a PD-T7-4 List_system_article.md row before using the article registry as direct PD-T7-4 model-to-paper evidence.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "PD-T7-4 system",
  "source_id": "traitmech:000406",
  "source_file": "pd_t7_4_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned DefenseFinder wiki, rules table, and HMM inventory all represent PD-T7-4, but the pinned List_system_article.md registry omits a PD-T7-4 row. The PD-T7-4 record therefore cites the pinned wiki plus the DOI-backed Vassallo et al. screen instead of inventing a missing article-registry entry.",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-4.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_4_system.html#pd-t7-4-defensefinder-article-registry-gap"
 },
 {
  "discussion_id": "pd-t7-5-mechanism-gap",
  "prompt": "Resolve PD-T7-5 natural host breadth, direct phage trigger, and PD(D/E)XK effector mechanism before minting narrower PD-T7-5 mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PD-T7-5 system",
  "source_id": "traitmech:000397",
  "source_file": "pd_t7_5_system.yaml",
  "attaches_to": [
   "causal_graphs#pd_t7_5_locus_restricts_phages"
  ],
  "rationale": "Vassallo et al. support PD-T7-5 as one of the conserved systems from an E. coli pangenome phage-defense selection, the DefenseFinder wiki maps the source locus to protection against SECphi17, T3, and T7, and DefenseFinder represents the system with one profile. Natural host breadth, the direct phage trigger, and the PD(D/E)XK effector mechanism remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1038/s41564-022-01219-4",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-5.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/pd-t7-5.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pd_t7_5_system.html#pd-t7-5-mechanism-gap"
 },
 {
  "discussion_id": "pfiat-mechanism-gap",
  "prompt": "Resolve natural PfiAT host breadth, the PfiT cellular target in Pseudomonas, Pf prophage production and immunity coupling, and PfiAT profile-to-activity mapping before minting narrower PfiAT mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PfiAT system",
  "source_id": "traitmech:000365",
  "source_file": "pfiat_system.yaml",
  "attaches_to": [
   "causal_graphs#pfiat_locus_regulates_pf4_phage"
  ],
  "rationale": "Li et al. support PA0729/PfiT and Rorf0727/PfiA in the Pf4 prophage as a type II toxin-antitoxin pair that regulates Pf4 production and phage immunity, and DefenseFinder models PfiAT as a two-profile system with PfiAT__PfiA and PfiAT__PfiT markers. Natural host breadth, the cellular target of PfiT, Pf4 immunity coupling, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:32246813"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pfiat_system.html#pfiat-mechanism-gap"
 },
 {
  "discussion_id": "phage-defense-system-xref-gap",
  "prompt": "Resolve exact ontology xrefs for organism-level phage defense system possession before adding TraitRecord xrefs.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "phage defense system",
  "source_id": "traitmech:000209",
  "source_file": "phage_defense_system.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot retains only obsolete phage defense, and GO:0051607 defense response to virus is a biological process rather than this GENOMICS possession trait. CRISPR-Cas, restriction-modification, BREX, DISARM, abortive-infection, and other mechanism terms are narrower than the umbrella parent curated here.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/phage_defense_system.html#phage-defense-system-xref-gap"
 },
 {
  "discussion_id": "phosphorothioate-subfamily-split-gap",
  "prompt": "Resolve archaeal phosphorothioate-based antiviral systems before minting additional narrower children under the phosphorothioate defense parent.",
  "kind": "KNOWLEDGE_GAP",
  "status": "RESOLVED",
  "is_gap": "Knowledge gap",
  "source_name": "phosphorothioate defense system",
  "source_id": "traitmech:000213",
  "source_file": "phosphorothioate_defense_system.yaml",
  "attaches_to": [],
  "rationale": "Dnd, SspABCD-SspE, SspABCD-SspFGH, and archaeal DndCDEA-PbeABCD PT antiviral architectures have all been split out as narrower phosphorothioate defense system children.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/phosphorothioate_defense_system.html#phosphorothioate-subfamily-split-gap"
 },
 {
  "discussion_id": "phrann_gp29_gp30-mechanism-gap",
  "prompt": "Resolve the Phrann gp29-gp30 contribution to TM4 defense, Phrann gp30 regulator role, lytic trigger, (p)ppGpp synthetase activity, and remaining target-phage breadth before minting narrower Phrann gp29-gp30 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Phrann gp29-gp30 system",
  "source_id": "traitmech:000296",
  "source_file": "phrann_gp29_gp30_system.yaml",
  "attaches_to": [
   "causal_graphs#phrann_gp29_gp30_locus_restricts_phage"
  ],
  "rationale": "Dedrick et al. and DefenseFinder support Phrann gp29-gp30 as a named anti-phage system with gp29 and gp30 profiles, but the Phrann gp30 regulatory role, lytic-phage trigger, direct (p)ppGpp activation mechanism, relative contribution to TM4 defense, and remaining target breadth are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/phrann_gp29_gp30_system.html#phrann_gp29_gp30-mechanism-gap"
 },
 {
  "discussion_id": "pif-output-gap",
  "prompt": "Resolve the direct T7 trigger, PifA and PifC molecular functions, host-cell output, and phage escape routes before minting narrower Pif mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Pif system",
  "source_id": "traitmech:000323",
  "source_file": "pif_system.yaml",
  "attaches_to": [
   "causal_graphs#pif_locus_specifies_t7_abortive_infection"
  ],
  "rationale": "Cram et al. support an F-plasmid pif-region abortive-infection system that maps to a two-profile DefenseFinder model, but the direct T7 trigger, the molecular functions of PifA and PifC, the host-cell growth-arrest or cell-death output, and phage escape routes remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pif_system.html#pif-output-gap"
 },
 {
  "discussion_id": "prithvi-mechanism-gap",
  "prompt": "Resolve Prithvi phage triggers and effector outputs before minting narrower Prithvi mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Prithvi system",
  "source_id": "traitmech:000290",
  "source_file": "prithvi_system.yaml",
  "attaches_to": [
   "causal_graphs#prithvi_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Prithvi as a named anti-phage system with a PtvA HMM profile entry, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/prithvi_system.html#prithvi-mechanism-gap"
 },
 {
  "discussion_id": "prometheus-mechanism-gap",
  "prompt": "Resolve Prometheus phage triggers and effector outputs before minting narrower Prometheus mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Prometheus system",
  "source_id": "traitmech:000291",
  "source_file": "prometheus_system.yaml",
  "attaches_to": [
   "causal_graphs#prometheus_locus_restricts_phage"
  ],
  "rationale": "van den Berg et al. and DefenseFinder support Prometheus as a named anti-phage system with a Prometheus__ProA HMM profile entry, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/prometheus_system.html#prometheus-mechanism-gap"
 },
 {
  "discussion_id": "prrc-mechanism-gap",
  "prompt": "Resolve natural PrrC homolog substrate specificity, exact EcoprrI accessory composition and profile matching, and phage trigger logic before minting narrower PrrC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PrrC system",
  "source_id": "traitmech:000364",
  "source_file": "prrc_system.yaml",
  "attaches_to": [
   "causal_graphs#prrc_locus_restricts_t4_phage"
  ],
  "rationale": "Uzan et al. summarize PrrC as a T4 phage-exclusion system, Blanga-Kanfi et al. support PrrC and EcoprrI homologs as genetically linked restriction RNases, and DefenseFinder models PrrC as a two-profile system with EcoprrI and PrrC markers plus type I restriction-modification accessories. The natural substrates, accessory composition, and phage trigger logic remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/prrc_system.html#prrc-mechanism-gap"
 },
 {
  "discussion_id": "psyrta-mechanism-gap",
  "prompt": "Resolve PsyrTA phage triggers and effector outputs before minting narrower PsyrTA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PsyrTA system",
  "source_id": "traitmech:000257",
  "source_file": "psyrta_system.yaml",
  "attaches_to": [
   "causal_graphs#psyrta_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support PsyrTA as a named anti-phage system with required PsyrA and PsyrT profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/psyrta_system.html#psyrta-mechanism-gap"
 },
 {
  "discussion_id": "pvurts1i-defensefinder-model-gap",
  "prompt": "Resolve PvuRts1I-family breadth, 5hmC and 5ghmC target selectivity across natural hosts, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower PvuRts1I mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "PvuRts1I system",
  "source_id": "traitmech:000511",
  "source_file": "pvurts1i_system.yaml",
  "attaches_to": [
   "causal_graphs#pvurts1i_restricts_modified_hmc_dna"
  ],
  "rationale": "Wang et al. support PvuRts1I as the founding member of a family of 5hmC- and 5ghmC-recognizing modification-dependent restriction endonucleases, and the pinned DefenseFinder article registry maps PvuRts1I to the Wang et al. paper. The pinned HMM inventory and rules table have no exact PvuRts1I rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of PvuRts1I-like systems across natural hosts, or the complete set of natural 5hmC and 5ghmC target contexts.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1093/nar/gkr607",
   "DOI:10.1093/nar/gkr607",
   "DOI:10.1093/nar/gkr607",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pvurts1i_system.html#pvurts1i-defensefinder-model-gap"
 },
 {
  "discussion_id": "pycsar-signal-and-effector-gap",
  "prompt": "Resolve Pycsar cyclase clades, cyclic pyrimidine specificity, receptor-effector folds, activating phage triggers, and effector outputs before minting narrower Pycsar subtype children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Pycsar system",
  "source_id": "traitmech:000236",
  "source_file": "pycsar_system.yaml",
  "attaches_to": [],
  "rationale": "Tal et al. support Pycsar systems as widespread PycC-containing antiphage systems whose phage-induced cyclic CMP or cyclic UMP second messengers activate immune effectors, and Hou et al. resolve a uridylate-cyclase/PycTIR branch with zinc-finger and cUMP-recognition determinants. The first TraitRecord therefore stays at the broad Pycsar-system level until separate subtype review resolves which cyclase clades, second messengers, receptor folds, phage triggers, and outputs apply across each family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/pycsar_system.html#pycsar-signal-and-effector-gap"
 },
 {
  "discussion_id": "radar-trigger-and-substrate-gap",
  "prompt": "Resolve RADAR phage triggers, RdrA activation, ATP-versus-RNA deamination, and inosine nucleotide toxicity before minting narrower RADAR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RADAR system",
  "source_id": "traitmech:000238",
  "source_file": "radar_system.yaml",
  "attaches_to": [],
  "rationale": "Gao et al. support an RNA translocation and deamination model for RdrA/RdrB RADAR assemblies, whereas Duncan-Lowey et al. found that ATP and dATP mononucleotide deamination rather than robust RNA editing mediates RADAR immunity. The first TraitRecord therefore stays at the RADAR-system level until separate review resolves which activating phage cues, RdrA sensor states, deaminase substrates, and inosine toxicity routes generalize across RADAR loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/radar_system.html#radar-trigger-and-substrate-gap"
 },
 {
  "discussion_id": "razr-trigger-model-gap",
  "prompt": "Resolve RAZR natural hosts, phage ring triggers, RNA-substrate breadth, and model coverage before minting narrower RAZR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RAZR system",
  "source_id": "traitmech:000411",
  "source_file": "razr_system.yaml",
  "attaches_to": [
   "causal_graphs#razr_ring_trigger_restricts_phage"
  ],
  "rationale": "Zhang et al. support RAZR as a ring-activated zinc-finger HEPN RNase that can oligomerize around unrelated phage ring scaffolds, but natural locus breadth, the full phage-trigger set, exact RNA-substrate preference, and absence from the pinned DefenseFinder HMM/rules rows need further review.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/razr_system.html#razr-trigger-model-gap"
 },
 {
  "discussion_id": "resolvase-duf5677-defensefinder-profile-gap",
  "prompt": "Resolve exact Resolvase_DUF5677 locus architecture, DUF5677-associated domain boundaries, natural host exemplars, phage trigger breadth, and DefenseFinder HMM/rules coverage before minting narrower Resolvase DUF5677 mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Resolvase DUF5677 system",
  "source_id": "traitmech:000531",
  "source_file": "resolvase_duf5677_system.yaml",
  "attaches_to": [
   "causal_graphs#resolvase_duf5677_phage_defense"
  ],
  "rationale": "Perez Taboada et al. support prokaryotic Schlafen nucleases as widespread antiviral effectors fused to phage-sensing domains, and the pinned DefenseFinder article registry maps the Resolvase_DUF5677 key to the same article. The pinned HMM inventory and rules table have no exact Resolvase_DUF5677 or DUF5677 rows for this source key. This first-pass record therefore does not resolve whether the exact Resolvase_DUF5677 architecture is a single-protein fusion or multi-gene locus, its exact DUF5677-associated domain boundaries, natural host exemplars, accession-level Schlafen proteins, full phage trigger breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/resolvase_duf5677_system.html#resolvase-duf5677-defensefinder-profile-gap"
 },
 {
  "discussion_id": "resolvase-kap-ntpase-defensefinder-profile-gap",
  "prompt": "Resolve exact Resolvase_KAP_NTPase locus architecture, KAP NTPase-associated domain boundaries, natural host exemplars, phage trigger breadth, and DefenseFinder HMM/rules coverage before minting narrower Resolvase KAP NTPase mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Resolvase KAP NTPase system",
  "source_id": "traitmech:000532",
  "source_file": "resolvase_kap_ntpase_system.yaml",
  "attaches_to": [
   "causal_graphs#resolvase_kap_ntpase_phage_defense"
  ],
  "rationale": "Perez Taboada et al. support prokaryotic Schlafen nucleases as widespread antiviral effectors fused to phage-sensing domains, and the pinned DefenseFinder article registry maps the Resolvase_KAP_NTPase key to the same article. The pinned HMM inventory and rules table have no exact Resolvase_KAP_NTPase or KAP_NTPase rows for this source key. This first-pass record therefore does not resolve whether the exact Resolvase_KAP_NTPase architecture is a single-protein fusion or multi-gene locus, its exact KAP NTPase-associated domain boundaries, natural host exemplars, accession-level Schlafen proteins, full phage trigger breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/resolvase_kap_ntpase_system.html#resolvase-kap-ntpase-defensefinder-profile-gap"
 },
 {
  "discussion_id": "resolvase-schlafen-defensefinder-profile-gap",
  "prompt": "Resolve exact Resolvase_Schlafen locus architecture, resolvase-associated domain boundaries, natural host exemplars, phage trigger breadth, and DefenseFinder HMM/rules coverage before minting narrower Resolvase Schlafen mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Resolvase Schlafen system",
  "source_id": "traitmech:000529",
  "source_file": "resolvase_schlafen_system.yaml",
  "attaches_to": [
   "causal_graphs#resolvase_schlafen_phage_defense"
  ],
  "rationale": "Perez Taboada et al. support prokaryotic Schlafen nucleases as widespread antiviral effectors fused to phage-sensing domains, and the pinned DefenseFinder article registry maps the Resolvase_Schlafen key to the same article. The pinned HMM inventory and rules table have no exact Schlafen rows. This first-pass record therefore does not resolve whether the exact Resolvase_Schlafen architecture is a single-protein fusion or multi-gene locus, its exact resolvase-associated domain boundaries, natural host exemplars, accession-level Schlafen proteins, full phage trigger breadth, or a reusable DefenseFinder profile model.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1038/s41564-026-02277-8",
   "DOI:10.1038/s41564-026-02277-8",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/resolvase_schlafen_system.html#resolvase-schlafen-defensefinder-profile-gap"
 },
 {
  "discussion_id": "retron-effector-trigger-gap",
  "prompt": "Resolve retron effector, phage-trigger, and hybrid-system diversity before minting narrower Retron-Sen2, Ec48, or Retron-Septu mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Retron system",
  "source_id": "traitmech:000235",
  "source_file": "retron_system.yaml",
  "attaches_to": [],
  "rationale": "Millman et al. support multiple RT/ncRNA/effector retron systems as abortive-infection antiphage systems, and Bobonis et al. resolve the Retron-Sen2 RcaT example in which a reverse-transcriptase-msDNA antitoxin complex responds to phage-triggered msDNA modification. The first TraitRecord therefore stays at the broad retron-system level until separate subtype review resolves which effectors, guarded host targets, phage triggers, direct-msDNA modification steps, and Septu-coupled architectures apply across each retron family.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/retron_system.html#retron-effector-trigger-gap"
 },
 {
  "discussion_id": "reve-mechanism-and-modelling-gap",
  "prompt": "Resolve Reve locus breadth, exact phage triggers, ATPase/P-loop molecular roles, direct antiviral output, source-system table rows, and DefenseFinder HMM/rule coverage before minting narrower Reve mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Reve system",
  "source_id": "traitmech:000499",
  "source_file": "reve_system.yaml",
  "attaches_to": [
   "causal_graphs#reve_locus_restricts_phage"
  ],
  "rationale": "de Sousa et al. support Reve as one of the novel single-gene P4-encoded systems with experimental phage-protection activity, and the pinned DefenseFinder article registry maps the Reve source key to the corresponding preprint. The pinned HMM inventory and rules table have no exact Reve rows, and this first-pass record does not resolve the tested source locus, complete phage breadth, exact trigger, molecular output, or detection rule.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1093/nar/gkag898",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/reve_system.html#reve-mechanism-and-modelling-gap"
 },
 {
  "discussion_id": "rexab-mechanism-gap",
  "prompt": "Resolve the direct RexAB phage trigger, RexA and RexB molecular coupling, ion-channel activity, lambda self-exclusion control, and sensitive-phage escape routes before minting narrower RexAB mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RexAB system",
  "source_id": "traitmech:000324",
  "source_file": "rexab_system.yaml",
  "attaches_to": [
   "causal_graphs#rexab_locus_mediates_rex_exclusion"
  ],
  "rationale": "Parma et al. support bacteriophage-lambda rexA and rexB as a two-component system that aborts lytic growth of bacterial viruses, and DefenseFinder maps RexAB to RexAB__RexA and RexAB__RexB profiles. The direct phage trigger, RexA/RexB molecular coupling, ion-channel output, lambda self-exclusion control, and sensitive-phage escape routes remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rexab_system.html#rexab-mechanism-gap"
 },
 {
  "discussion_id": "rhea-mechanism-gap",
  "prompt": "Resolve Rhea phage triggers and effector outputs before minting narrower Rhea mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rhea system",
  "source_id": "traitmech:000311",
  "source_file": "rhea_system.yaml",
  "attaches_to": [
   "causal_graphs#rhea_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al., Mosterd et al., and DefenseFinder support Rhea as a named anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rhea_system.html#rhea-mechanism-gap"
 },
 {
  "discussion_id": "rloc-mechanism-gap",
  "prompt": "Resolve natural RloC host breadth, endogenous RloC activation triggers, phage restriction strength, and RloC profile-to-activity mapping before minting narrower RloC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RloC system",
  "source_id": "traitmech:000366",
  "source_file": "rloc_system.yaml",
  "attaches_to": [
   "causal_graphs#rloc_locus_triggers_dna_break_responsive_activation"
  ],
  "rationale": "Davidov and Kaufmann support RloC as a bacterial wobble nucleotide-excising tRNase, Bitton et al. show that Acinetobacter baylyi RloC responds to phage T4 host DNA degradation in an Escherichia coli expression context, and DefenseFinder models RloC as a one-profile system with an RloC__RloC marker. Natural host breadth, native phage triggers, restriction strength, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:26031711"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rloc_system.html#rloc-mechanism-gap"
 },
 {
  "discussion_id": "rnlab-phage-breadth-evasion-gap",
  "prompt": "Resolve natural RnlAB phage breadth, wild-type T4 evasion through Dmd, induction or activation routes in non-T4 contexts, and RnlAB profile-to-activity mapping before minting narrower RnlAB mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RnlAB system",
  "source_id": "traitmech:000367",
  "source_file": "rnlab_system.yaml",
  "attaches_to": [
   "causal_graphs#rnlab_locus_antagonizes_t4_dmd_mutants"
  ],
  "rationale": "Koga et al. support RnlA/RnlB as an Escherichia coli K-12 toxin-antitoxin system whose RNase LS activity can antagonize T4 dmd mutants, Otsuka and Yonesaki show that T4 phage Dmd suppresses RnlA toxicity, and DefenseFinder models RnlAB as a two-profile system with RnlAB__RnlA and RnlAB__RnlB markers. Natural phage breadth, wild-type T4 evasion, non-T4 activation contexts, and profile-to-activity mapping remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:22403819"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rnlab_system.html#rnlab-phage-breadth-evasion-gap"
 },
 {
  "discussion_id": "rosmerta-mechanism-gap",
  "prompt": "Resolve RosmerTA phage triggers and effector outputs before minting narrower RosmerTA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "RosmerTA system",
  "source_id": "traitmech:000256",
  "source_file": "rosmerta_system.yaml",
  "attaches_to": [
   "causal_graphs#rosmerta_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support RosmerTA as a named anti-phage system with required RmrA and RmrT profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rosmerta_system.html#rosmerta-mechanism-gap"
 },
 {
  "discussion_id": "rst-2tm-1tm-tir-mechanism-gap",
  "prompt": "Resolve Rst_2TM_1TM_TIR native host breadth, accession-level components, the proposed TIR-derived nucleotide messenger, and the downstream transmembrane activation mechanism before minting narrower Rst_2TM_1TM_TIR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_2TM_1TM_TIR system",
  "source_id": "traitmech:000400",
  "source_file": "rst_2tm_1tm_tir_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_2tm_1tm_tir_locus_restricts_phages"
  ],
  "rationale": "The pinned DefenseFinder wiki supports a three-component AC1 Rst_2TM_1TM_TIR system that protects Escherichia coli C against multiple phages, and DefenseFinder represents Rst_2TM_1TM_TIR as a required three-profile model. Rousset et al. proposed that the TIR-containing protein could generate a nucleotide messenger to activate associated transmembrane proteins, but the wiki still records the molecular mechanism as unknown.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_2tm_1tm_tir.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_2tm_1tm_tir.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_2tm_1tm_tir.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_2tm_1tm_tir_system.html#rst-2tm-1tm-tir-mechanism-gap"
 },
 {
  "discussion_id": "rst-3hp-host-mechanism-gap",
  "prompt": "Resolve Rst_3HP native host breadth, Hp1/Hp2/Hp3 molecular activities, profile-to-gene mapping, and the mechanism of P1 restriction before minting narrower Rst_3HP mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_3HP system",
  "source_id": "traitmech:000398",
  "source_file": "rst_3hp_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_3hp_locus_restricts_p1"
  ],
  "rationale": "Rousset et al. support a three-gene P2-hotspot system with no clear predicted domains that protects against P1, and DefenseFinder represents Rst_3HP as a required Hp1/Hp2/Hp3 three-profile model. This first system-level record leaves native host breadth, profile-to-gene mapping, the molecular activities of Hp1, Hp2, and Hp3, and the P1 restriction mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_3hp.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_3hp.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_3hp_system.html#rst-3hp-host-mechanism-gap"
 },
 {
  "discussion_id": "rst-duf4238-host-mechanism-gap",
  "prompt": "Resolve Rst_DUF4238 native host breadth, accession-level DUF4238 proteins, and the molecular mechanism of T7 restriction before minting narrower Rst_DUF4238 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_DUF4238 system",
  "source_id": "traitmech:000374",
  "source_file": "rst_duf4238_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_duf4238_locus_restricts_t7"
  ],
  "rationale": "Rousset et al. support a one-protein DUF4238 P2-hotspot system that provides strong T7 resistance when expressed in Escherichia coli, and DefenseFinder represents Rst_DUF4238 as a single-profile Rst_DUF4238__DUF4238_Pers model. This first system-level record leaves native host breadth, accession-level component grounding, the profile-to-activity mapping, and the T7 restriction mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_duf4238.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_duf4238.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_duf4238_system.html#rst-duf4238-host-mechanism-gap"
 },
 {
  "discussion_id": "rst-gop-beta-cll-mechanism-gap",
  "prompt": "Resolve Rst_gop_beta_cll natural host breadth, exact beta and cll gene correspondence, direct phage trigger, and Gop or beta toxin-antitoxin activities before minting narrower P4 gop-beta-cII mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst gop-beta-cII system",
  "source_id": "traitmech:000376",
  "source_file": "rst_gop_beta_cll_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_gop_beta_cll_locus_restricts_lambda_p1"
  ],
  "rationale": "Rousset et al. support a canonical P4 gop-beta-cII system that protects against lambda and P1, and DefenseFinder represents Rst_gop_beta_cll as a required beta/cll/gop three-profile model. This first system-level record leaves natural host breadth, profile-to-gene mapping, the direct phage trigger, and the gop, beta, or cII effector logic unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "DOI:10.1016/j.chom.2022.02.018",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_gop_beta_cll_system.html#rst-gop-beta-cll-mechanism-gap"
 },
 {
  "discussion_id": "rst-helicaseduf2290-host-mechanism-gap",
  "prompt": "Resolve Rst_HelicaseDUF2290 native host breadth, accession-level DUF2290/helicase roles, the DUF2290_Pers profile relationship, and the mechanism of T7 restriction before minting narrower Rst_HelicaseDUF2290 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_HelicaseDUF2290 system",
  "source_id": "traitmech:000401",
  "source_file": "rst_helicaseduf2290_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_helicaseduf2290_locus_restricts_t7"
  ],
  "rationale": "Rousset et al. support a two-gene ATP-dependent helicase plus DUF2290 P4-hotspot system that inhibits T7 growth, and DefenseFinder represents Rst_HelicaseDUF2290 as a required two-profile model. This first system-level record leaves native host breadth, profile-to-gene mapping, the role of the extra DUF2290_Pers HMM profile, the molecular activities of the DUF2290 and helicase components, and the T7 restriction mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/223cf269/content/3.defense-systems/rst_helicaseduf2290.md",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/223cf269/content/3.defense-systems/rst_helicaseduf2290.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_helicaseduf2290_system.html#rst-helicaseduf2290-host-mechanism-gap"
 },
 {
  "discussion_id": "rst-hydrolase-3tm-host-mechanism-gap",
  "prompt": "Resolve Rst_Hydrolase-3Tm native host breadth, the Rst_Hydrolase-3Tm and Rst_Hydrolase-Tm namespace relationship, accession-level Hydrolase/Hydrolase-Tm roles, and the mechanism of T7 restriction before minting narrower Rst_Hydrolase-3Tm mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_Hydrolase-3Tm system",
  "source_id": "traitmech:000402",
  "source_file": "rst_hydrolase_3tm_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_hydrolase_3tm_locus_restricts_t7"
  ],
  "rationale": "Rousset et al. support a two-gene HAD-like hydrolase plus transmembrane-protein P4-hotspot system that inhibits T7 growth, and DefenseFinder maps Rst_Hydrolase-3Tm to a required two-profile Rst_Hydrolase-Tm model. This first system-level record leaves native host breadth, profile-to-gene mapping, the model-namespace mismatch, the molecular activities of the Hydrolase and Hydrolase-Tm components, and the T7 restriction mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/223cf269/content/3.defense-systems/rst_hydrolase-3tm.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_hydrolase_3tm_system.html#rst-hydrolase-3tm-host-mechanism-gap"
 },
 {
  "discussion_id": "rst-rt-nitrilase-tm-host-mechanism-gap",
  "prompt": "Resolve Rst_RT-nitrilase-Tm native host breadth, the Rst_RT-nitrilase-Tm and Rst_RT-Tm namespace relationship, accession-level RT/RT-Tm roles, the relationship to UG5-large source naming, and the mechanism of AL505_P2 restriction before minting narrower Rst_RT-nitrilase-Tm mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst_RT-nitrilase-Tm system",
  "source_id": "traitmech:000403",
  "source_file": "rst_rt_nitrilase_tm_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_rt_nitrilase_tm_locus_restricts_al505_p2"
  ],
  "rationale": "Rousset et al. support a two-gene P4-hotspot system that combines a group-5 reverse transcriptase with a C-terminal nitrilase domain and a transmembrane effector, and DefenseFinder maps Rst_RT-nitrilase-Tm to a required two-profile Rst_RT-Tm model. This first system-level record leaves native host breadth, exact profile-to-gene mapping, the model-namespace mismatch, the relationship to UG5-large source naming, the molecular activities of the RT and RT-Tm components, and the AL505_P2 restriction mechanism unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/content/3.defense-systems/rst_rt-nitrilase-tm.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_rt_nitrilase_tm_system.html#rst-rt-nitrilase-tm-host-mechanism-gap"
 },
 {
  "discussion_id": "rst-tir-nlr-mechanism-gap",
  "prompt": "Resolve Rst_TIR-NLR natural host breadth, exact profile-to-gene correspondence, direct phage trigger, and TIR/STAND activation before minting narrower Rst TIR-NLR mechanism traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rst TIR-NLR system",
  "source_id": "traitmech:000377",
  "source_file": "rst_tir_nlr_system.yaml",
  "attaches_to": [
   "causal_graphs#rst_tir_nlr_locus_restricts_phages"
  ],
  "rationale": "Rousset et al. support a P4-like TIR-NLR system that protects against virulent and P2-like phages, and DefenseFinder represents Rst_TIR-NLR as a single-profile model. This first system-level record leaves natural host breadth, profile-to-gene mapping, the direct phage trigger, and TIR/STAND effector logic unresolved.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1016/j.chom.2022.02.018",
   "DOI:10.1016/j.chom.2022.02.018",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rst_tir_nlr_system.html#rst-tir-nlr-mechanism-gap"
 },
 {
  "discussion_id": "rugutis-mechanism-gap",
  "prompt": "Resolve Rugutis phage triggers and effector outputs before minting narrower Rugutis mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Rugutis system",
  "source_id": "traitmech:000315",
  "source_file": "rugutis_system.yaml",
  "attaches_to": [
   "causal_graphs#rugutis_locus_restricts_phage"
  ],
  "rationale": "Grafakou et al., Mosterd et al., and DefenseFinder support Rugutis as a named anti-phage system, but the direct trigger, molecular substrate, antiviral effector output, natural locus breadth, and profile-to-component model are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/rugutis_system.html#rugutis-mechanism-gap"
 },
 {
  "discussion_id": "sanata-host-trigger-profile-gap",
  "prompt": "Resolve SanaTA native host breadth, SanaA/SanaT molecular activities, T7 Gp4.5/Lon anti-defense logic, and the SanaTA__SanaT_1 profile before minting narrower SanaTA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SanaTA system",
  "source_id": "traitmech:000373",
  "source_file": "sanata_system.yaml",
  "attaches_to": [
   "causal_graphs#sanata_locus_restricts_t7_mutants"
  ],
  "rationale": "Sberro et al. support sanaTA as a Shewanella sp. ANA-3 two-gene toxin-antitoxin family that confers resistance to T7 phage mutants lacking gene 4.5 when expressed in Escherichia coli, and DefenseFinder models SanaTA with SanaTA__SanaA and SanaTA__SanaT. This first system-level record leaves the natural host range, SanaA/SanaT activities, T7 Gp4.5/Lon counter-defense sequence, and the extra non-rule SanaTA__SanaT_1 HMM unresolved.",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "PMID:23478446",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sanata_system.html#sanata-host-trigger-profile-gap"
 },
 {
  "discussion_id": "scomcra-defensefinder-model-gap",
  "prompt": "Resolve ScoMcrA-family breadth, phosphorothioated-DNA sequence-context specificity across natural hosts, methylated-DNA target breadth, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower ScoMcrA mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ScoMcrA system",
  "source_id": "traitmech:000512",
  "source_file": "scomcra_system.yaml",
  "attaches_to": [
   "causal_graphs#scomcra_restricts_phosphorothioated_dna"
  ],
  "rationale": "Liu et al. support ScoA3McrA as a Type IV McrA homolog that cleaves S-modified DNA in vitro and support ScoMcrA as a PT-dependent endonuclease with a sulfur-binding domain. The pinned DefenseFinder article registry maps ScoMcrA to the sulfur-recognition paper, but the pinned HMM inventory and rules table have no exact ScoMcrA rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of ScoMcrA-like systems across natural hosts, the complete set of natural phosphorothioated-DNA contexts, or the breadth of methylated-DNA target contexts.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "DOI:10.1371/journal.pgen.1001253",
   "DOI:10.1371/journal.pgen.1001253",
   "DOI:10.1371/journal.pgen.1001253",
   "DOI:10.1038/s41467-018-07093-1",
   "DOI:10.1038/s41467-018-07093-1",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/scomcra_system.html#scomcra-defensefinder-model-gap"
 },
 {
  "discussion_id": "sdic1-defensefinder-model-gap",
  "prompt": "Resolve SDIC1 natural host breadth, SDIC1A/SDIC1B component functions, phage triggers, ubiquitination substrates, population-immunity mechanism, and rule-level detection criteria before minting narrower SDIC1 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SDIC1 system",
  "source_id": "traitmech:000420",
  "source_file": "sdic1_system.yaml",
  "attaches_to": [
   "causal_graphs#sdic1_locus_restricts_phage"
  ],
  "rationale": "Cummins et al. support SDIC1 as a TIR-domain-containing anti-phage system with a ubiquitin-ligase-like component, and the pinned DefenseFinder HMM inventory records SDIC1A and SDIC1B profile rows. The pinned rules table has no SDIC1 row, and the first-pass record does not resolve natural host breadth, sensitive-phage breadth, the exact profile-to-component mapping, phage triggers, the direct TIR-dependent output, or the ubiquitination substrate.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1016/j.celrep.2024.115055",
   "DOI:10.1016/j.celrep.2024.115055",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sdic1_system.html#sdic1-defensefinder-model-gap"
 },
 {
  "discussion_id": "sdic3-defensefinder-model-gap",
  "prompt": "Resolve SDIC3 natural host breadth, SDIC3A status, exact SDIC3B/SDIC3C/SDIC3D/SDIC3E/SDIC3F component functions, sensitive-phage breadth, ECOR61-system subtype scope, the direct trigger and molecular output, and rule-level detection criteria before minting narrower SDIC3 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SDIC3 system",
  "source_id": "traitmech:000423",
  "source_file": "sdic3_system.yaml",
  "attaches_to": [
   "causal_graphs#sdic3_locus_restricts_phage"
  ],
  "rationale": "Cummins et al. support SDIC3 as a Serratia defense-island candidate anti-phage system that can strongly protect E. coli when plasmid expressed, and the pinned DefenseFinder HMM inventory records SDIC3B, SDIC3C, SDIC3D, SDIC3E, and SDIC3F profile rows. The pinned rules table has no SDIC3 row, and the first-pass record does not resolve natural host breadth, whether SDIC3A is part of the DefenseFinder-detectable system, phage target breadth, ECOR61 anti-phage-system boundaries, or the direct molecular output.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1016/j.celrep.2024.115055",
   "DOI:10.1016/j.celrep.2024.115055",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sdic3_system.html#sdic3-defensefinder-model-gap"
 },
 {
  "discussion_id": "sdic4-defensefinder-model-gap",
  "prompt": "Resolve SDIC4 natural host breadth, sensitive-phage breadth, type I versus type II component scope, SDIC4A/SDIC4B component functions, receptor or phage target, and rule-level detection criteria before minting narrower SDIC4 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SDIC4 system",
  "source_id": "traitmech:000421",
  "source_file": "sdic4_system.yaml",
  "attaches_to": [
   "causal_graphs#sdic4_locus_reduces_phage_adsorption"
  ],
  "rationale": "Cummins et al. support SDIC4 as a VasI-like anti-phage system that reduces phage adsorption, and the pinned DefenseFinder HMM inventory records SDIC4A and SDIC4B profile rows. The pinned rules table has no SDIC4 row, and the first-pass record does not resolve natural host breadth, sensitive-phage breadth, type I versus type II system boundaries, the exact profile-to-component mapping, the SDIC4A/SDIC4B relationship, or the phage-adsorption target.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1016/j.celrep.2024.115055",
   "DOI:10.1016/j.celrep.2024.115055",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sdic4_system.html#sdic4-defensefinder-model-gap"
 },
 {
  "discussion_id": "sefir-mechanism-gap",
  "prompt": "Resolve SEFIR phage triggers and effector outputs before minting narrower SEFIR mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SEFIR system",
  "source_id": "traitmech:000259",
  "source_file": "sefir_system.yaml",
  "attaches_to": [
   "causal_graphs#sefir_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support SEFIR as a named anti-phage system with a bSEFIR profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sefir_system.html#sefir-mechanism-gap"
 },
 {
  "discussion_id": "septu-standalone-retron-regulation-gap",
  "prompt": "Resolve standalone Septu activation, Retron-Septu release, and DNA-substrate specificity before minting narrower Septu mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Septu system",
  "source_id": "traitmech:000233",
  "source_file": "septu_system.yaml",
  "attaches_to": [],
  "rationale": "Yang et al. support a standalone Escherichia coli PtuAB system in which ATP modulates PtuA/PtuB nuclease activity through an incompletely resolved phage trigger, and Wang et al. support Retron-Septu Ec83/Ec78 complexes in which retron RT-msDNA association keeps PtuAB inactive until disassembly. The first TraitRecord therefore stays at the PtuA/PtuB system level until separate review resolves standalone activation, retron-dependent release, target DNA classes, and phage-specific activity across Septu loci.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/septu_system.html#septu-standalone-retron-regulation-gap"
 },
 {
  "discussion_id": "shango-mechanism-gap",
  "prompt": "Resolve Shango phage triggers and effector outputs before minting narrower Shango mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Shango system",
  "source_id": "traitmech:000255",
  "source_file": "shango_system.yaml",
  "attaches_to": [
   "causal_graphs#shango_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Shango as a named anti-phage system with SngA, SngB, and SngC profile choices, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/shango_system.html#shango-mechanism-gap"
 },
 {
  "discussion_id": "shedu-sensor-and-substrate-gap",
  "prompt": "Resolve Shedu sensor classes and DNA substrate preferences before minting narrower Shedu subtype or mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Shedu system",
  "source_id": "traitmech:000220",
  "source_file": "shedu_system.yaml",
  "attaches_to": [],
  "rationale": "Loeff et al. support free-DNA-end recognition and end-directed DNA nicking by SduA, and Gu et al. support a common Shedu nuclease core regulated by diverse N-terminal domains, but Shedu homologs need separate review before TraitMech asserts one universal N-terminal sensor class, activating DNA substrate, overhang preference, phage target, or escape strategy.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/shedu_system.html#shedu-sensor-and-substrate-gap"
 },
 {
  "discussion_id": "shosta-mechanism-gap",
  "prompt": "Resolve ShosTA phage triggers and effector outputs before minting narrower ShosTA mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ShosTA system",
  "source_id": "traitmech:000258",
  "source_file": "shosta_system.yaml",
  "attaches_to": [
   "causal_graphs#shosta_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support ShosTA as a named anti-phage system with required ShosA and ShosT profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/shosta_system.html#shosta-mechanism-gap"
 },
 {
  "discussion_id": "sirona-mechanism-gap",
  "prompt": "Resolve Sirona phage triggers and effector outputs before minting narrower Sirona mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Sirona system",
  "source_id": "traitmech:000264",
  "source_file": "sirona_system.yaml",
  "attaches_to": [
   "causal_graphs#sirona_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Sirona as a named anti-phage system with a VCA0356 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sirona_system.html#sirona-mechanism-gap"
 },
 {
  "discussion_id": "six-a-mbl-mechanism-gap",
  "prompt": "Resolve 6A-MBL phage triggers and effector outputs before minting narrower 6A-MBL mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "6A-MBL system",
  "source_id": "traitmech:000314",
  "source_file": "six_a_mbl_system.yaml",
  "attaches_to": [
   "causal_graphs#six_a_mbl_locus_restricts_phage"
  ],
  "rationale": "van den Berg et al. and DefenseFinder support 6A-MBL as a named anti-phage system with 6A_MBL__cap2_3 and 6A_MBL__MblB HMM profile entries, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/six_a_mbl_system.html#six-a-mbl-mechanism-gap"
 },
 {
  "discussion_id": "snipe-defensefinder-model-gap",
  "prompt": "Resolve SNIPE host breadth, sensitive-phage breadth, direct tape-measure interaction specificity, and DefenseFinder HMM/rules coverage before minting narrower SNIPE mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SNIPE system",
  "source_id": "traitmech:000414",
  "source_file": "snipe_system.yaml",
  "attaches_to": [
   "causal_graphs#snipe_cleaves_injected_phage_dna"
  ],
  "rationale": "Saxton et al. support SNIPE as a membrane-localized anti-bacteriophage system that directly cleaves phage DNA during genome injection, while the pinned DefenseFinder article registry names a SNIPE system. The pinned DefenseFinder HMM inventory and rules table have no SNIPE rows, and the evidence does not yet resolve full host breadth, full target-phage breadth, direct tape-measure protein specificity, or profile-to-activity modeling.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41586-026-10207-1",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/snipe_system.html#snipe-defensefinder-model-gap"
 },
 {
  "discussion_id": "sofic-mechanism-gap",
  "prompt": "Resolve SoFIC phage triggers and effector outputs before minting narrower SoFIC mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SoFIC system",
  "source_id": "traitmech:000260",
  "source_file": "sofic_system.yaml",
  "attaches_to": [
   "causal_graphs#sofic_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support SoFIC as a named anti-phage system with a SoFic profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sofic_system.html#sofic-mechanism-gap"
 },
 {
  "discussion_id": "sparta-native-host-and-substrate-gap",
  "prompt": "Resolve SPARTA natural-host substrates before adding canonical examples or narrower short-pAgo defense children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SPARTA system",
  "source_id": "traitmech:000240",
  "source_file": "sparta_system.yaml",
  "attaches_to": [],
  "rationale": "Koopal et al. support strong high-copy plasmid activation and only limited, NADase-independent phage effects; Kottur et al. support C. thermophila SPARTA structural activation. This first record therefore stays broad until natural-host activity, phage scope, and whether SIR2-APAZ or nuclease-APAZ relatives should be separate children are resolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sparta_system.html#sparta-native-host-and-substrate-gap"
 },
 {
  "discussion_id": "spbk-mechanism-gap",
  "prompt": "Resolve the direct SP\u03b2 YonE trigger, SpbK TIR-domain output, essential host target, and broader SpbK homolog scope before minting narrower SpbK mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "SpbK system",
  "source_id": "traitmech:000325",
  "source_file": "spbk_system.yaml",
  "attaches_to": [
   "causal_graphs#spbk_locus_mediates_spb_defense"
  ],
  "rationale": "Johnson et al. support ICEBs1 spbK as a YonE-dependent abortive infection gene that inhibits SP\u03b2 and causes cell death, and DefenseFinder maps SpbK to the SpbK__SpbK profile. The direct SpbK-YonE coupling event, TIR-domain output, essential host target, and homolog breadth remain unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/spbk_system.html#spbk-mechanism-gap"
 },
 {
  "discussion_id": "stk2-activator-and-death-target-gap",
  "prompt": "Resolve the Stk2-activating phage protein and lethal host-phosphorylation target before minting narrower Stk2 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Stk2 system",
  "source_id": "traitmech:000303",
  "source_file": "stk2_system.yaml",
  "attaches_to": [
   "causal_graphs#stk2_activation_aborts_phage_infection"
  ],
  "rationale": "Depardieu et al. support Stk2 as a named phage-activated serine/threonine kinase system whose activation causes host-protein phosphorylation, bacterial host-cell death, and abortive infection, and DefenseFinder represents Stk2 with a one-profile model. This system-level record leaves the direct phage activator, the lethal Stk2 phosphorylation target, target conservation across Stk2 loci, and phage escape routes unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/stk2_system.html#stk2-activator-and-death-target-gap"
 },
 {
  "discussion_id": "sucellos-mechanism-gap",
  "prompt": "Resolve Sucellos phage triggers and effector outputs before minting narrower Sucellos mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Sucellos system",
  "source_id": "traitmech:000266",
  "source_file": "sucellos_system.yaml",
  "attaches_to": [
   "causal_graphs#sucellos_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Sucellos as a named anti-phage system with SclA_VCA0367 and SclB_VCA0368 profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/sucellos_system.html#sucellos-mechanism-gap"
 },
 {
  "discussion_id": "tab-defensefinder-model-gap",
  "prompt": "Resolve Tab host breadth, sensitive-phage breadth, counter-defence specificity, and DefenseFinder HMM/rules coverage before minting narrower Tab mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Tab system",
  "source_id": "traitmech:000413",
  "source_file": "tab_system.yaml",
  "attaches_to": [
   "causal_graphs#tab_blocks_virion_assembly"
  ],
  "rationale": "Patel et al. support Tab as a prophage-encoded anti-phage defence protein that blocks invading phage-tail assembly and prevents release of infectious phage progeny, while the pinned DefenseFinder article registry names a Tab system. The pinned DefenseFinder HMM inventory and rules table have no Tab rows, and the evidence does not yet resolve host breadth, target-phage breadth, counter-defence specificity, or profile-to-activity modeling.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-45892-x",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tab_system.html#tab-defensefinder-model-gap"
 },
 {
  "discussion_id": "tagi-defensefinder-model-gap",
  "prompt": "Resolve TagI-family breadth, modified-cytosine sequence-context specificity across natural hosts, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower TagI mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TagI system",
  "source_id": "traitmech:000513",
  "source_file": "tagi_system.yaml",
  "attaches_to": [
   "causal_graphs#tagi_restricts_modified_cytosine_dna"
  ],
  "rationale": "Kisiala et al. support TagI as an SRA-HNH modification-dependent restriction endonuclease that recognizes 5mC/5hmC bases and restricts phage in assays. The pinned DefenseFinder article registry maps TagI to that paper, but the pinned HMM inventory and rules table have no exact TagI rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of TagI-like systems across natural hosts, or the complete set of natural modified-cytosine sequence contexts.",
  "num_experiments": 0,
  "num_evidence": 8,
  "evidence_refs": [
   "PMID:30202937",
   "PMID:30202937",
   "PMID:30202937",
   "PMID:30202937",
   "PMID:30202937",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tagi_system.html#tagi-defensefinder-model-gap"
 },
 {
  "discussion_id": "taranis-mechanism-gap",
  "prompt": "Resolve Taranis phage triggers and effector outputs before minting narrower Taranis mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Taranis system",
  "source_id": "traitmech:000265",
  "source_file": "taranis_system.yaml",
  "attaches_to": [
   "causal_graphs#taranis_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Taranis as a named anti-phage system with a VCA0396 profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/taranis_system.html#taranis-mechanism-gap"
 },
 {
  "discussion_id": "tgvab-defensefinder-rule-gap",
  "prompt": "Resolve TgvAB native host breadth, TgvA/TgvB biochemical roles, phage substrate breadth, and DefenseFinder rule or model coverage before minting narrower TgvAB mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TgvAB system",
  "source_id": "traitmech:000412",
  "source_file": "tgvab_system.yaml",
  "attaches_to": [
   "causal_graphs#tgvab_type_iv_restriction"
  ],
  "rationale": "Vizzarro et al. and Gomez and Waters support TgvAB as a two-component VPI-2 type IV restriction system that restricts glucosylated hmC-containing T-even phage DNA, and the pinned DefenseFinder HMM inventory carries TgvA and TgvB custom profiles. The pinned DefenseFinder rules table has no TgvAB row, and the evidence does not yet resolve native host breadth, the individual TgvA versus TgvB biochemical roles, full phage substrate breadth, or a rule-level profile combination.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1128/jb.00145-24",
   "DOI:10.1128/jb.00143-24",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tgvab_system.html#tgvab-defensefinder-rule-gap"
 },
 {
  "discussion_id": "tha-variant-profile-rule-gap",
  "prompt": "Resolve Tha variant boundaries, exact minor-tail-protein triggers, Ith inhibitor relationships, native host breadth, and DefenseFinder rule/profile coverage before minting narrower Tha mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Tha system",
  "source_id": "traitmech:000497",
  "source_file": "tha_system.yaml",
  "attaches_to": [
   "causal_graphs#tha_tail_activated_hepn_rnase_defense"
  ],
  "rationale": "Rostol et al. support Tha-1 and Tha-2 as S. aureus prophage-encoded Tha systems activated by distinct incoming-phage minor tail proteins. The pinned DefenseFinder registries map the Tha source key to the same primary paper and list one Tha__Tha custom HMM row, but no exact Tha system rule row was present in the pinned rules table. The first TraitRecord therefore stays at Tha-system scope until separate review resolves variant boundaries, exact activators, Ith inhibitor relationships, native host breadth, and model coverage.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41564-024-01661-6",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tha_system.html#tha-variant-profile-rule-gap"
 },
 {
  "discussion_id": "thoeris-family-signal-and-trigger-gap",
  "prompt": "Resolve Thoeris family architecture, signal chemistry, and phage triggering before minting narrower Thoeris mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Thoeris system",
  "source_id": "traitmech:000216",
  "source_file": "thoeris_system.yaml",
  "attaches_to": [],
  "rationale": "Ka et al. support the B. cereus ThsA/ThsB two-gene system and Ofir et al. support the TIR-produced cADPR-like signal that activates ThsA NAD depletion, but Thoeris variants need separate review before TraitMech asserts one exact number of TIR-domain proteins, cADPR-isomer chemistry, TIR target, ThsA activation state, cell-death pathway, or phage-triggering mechanism.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/thoeris_system.html#thoeris-family-signal-and-trigger-gap"
 },
 {
  "discussion_id": "tiamat-mechanism-gap",
  "prompt": "Resolve Tiamat phage triggers and effector outputs before minting narrower Tiamat mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Tiamat system",
  "source_id": "traitmech:000261",
  "source_file": "tiamat_system.yaml",
  "attaches_to": [
   "causal_graphs#tiamat_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Tiamat as a named anti-phage system with a TmtA profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tiamat_system.html#tiamat-mechanism-gap"
 },
 {
  "discussion_id": "tir-i-detection-trigger-gap",
  "prompt": "Resolve TIR-I native host breadth, the TIR-I__TIR-I_A and TIR-I__TIR-I_B profile-to-component mapping, phage-trigger specificity, TIR-domain output chemistry, and rule-level DefenseFinder detection criteria before minting narrower TIR-I mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TIR-I system",
  "source_id": "traitmech:000480",
  "source_file": "tir_i_system.yaml",
  "attaches_to": [
   "causal_graphs#tir_i_locus_inhibits_phage_plaquing"
  ],
  "rationale": "Wang et al. support TIR-I as one of nine newly named TIR-domain anti-phage defense systems and note that TIR-I occurs in diverse domain contexts. The pinned DefenseFinder HMM inventory records TIR-I__TIR-I_A and TIR-I__TIR-I_B custom profile rows, but the pinned DefenseFinder rules table has no TIR-I row. This first record therefore does not assert profile requirement logic, accession-level components, a universal domain architecture, or a direct phage trigger.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-51738-3",
   "DOI:10.1038/s41467-024-51738-3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tir_i_system.html#tir-i-detection-trigger-gap"
 },
 {
  "discussion_id": "tir-iii-detection-trigger-gap",
  "prompt": "Resolve TIR-III native host breadth, the TIR-III__TIR-III_A and TIR-III__TIR-III_B profile-to-component mapping, phage-trigger specificity, TIR-domain output chemistry, and rule-level DefenseFinder detection criteria before minting narrower TIR-III mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TIR-III system",
  "source_id": "traitmech:000481",
  "source_file": "tir_iii_system.yaml",
  "attaches_to": [
   "causal_graphs#tir_iii_locus_inhibits_phage_plaquing"
  ],
  "rationale": "Wang et al. support TIR-III as one of nine newly named TIR-domain anti-phage defense systems and note that TIR-III occurs in diverse domain contexts. The pinned DefenseFinder HMM inventory records TIR-III__TIR-III_A and TIR-III__TIR-III_B custom profile rows, but the pinned DefenseFinder rules table has no TIR-III row. This first record therefore does not assert profile requirement logic, accession-level components, a universal domain architecture, or a direct phage trigger.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-51738-3",
   "DOI:10.1038/s41467-024-51738-3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tir_iii_system.html#tir-iii-detection-trigger-gap"
 },
 {
  "discussion_id": "tir-iv-detection-trigger-gap",
  "prompt": "Resolve TIR-IV native host breadth, the TIR-IV__TIR-IV_A and TIR-IV__TIR-IV_B profile-to-component mapping, phage-trigger specificity, TIR-domain output chemistry, and rule-level DefenseFinder detection criteria before minting narrower TIR-IV mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TIR-IV system",
  "source_id": "traitmech:000482",
  "source_file": "tir_iv_system.yaml",
  "attaches_to": [
   "causal_graphs#tir_iv_locus_inhibits_phage_plaquing"
  ],
  "rationale": "Wang et al. support TIR-IV as one of nine newly named TIR-domain anti-phage defense systems and note that TIR-IV occurs in diverse domain contexts. The pinned DefenseFinder HMM inventory records TIR-IV__TIR-IV_A and TIR-IV__TIR-IV_B custom profile rows, but the pinned DefenseFinder rules table has no TIR-IV row. This first record therefore does not assert profile requirement logic, accession-level components, a universal domain architecture, or a direct phage trigger.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-51738-3",
   "DOI:10.1038/s41467-024-51738-3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tir_iv_system.html#tir-iv-detection-trigger-gap"
 },
 {
  "discussion_id": "tir-vii-detection-trigger-gap",
  "prompt": "Resolve TIR-VII native host breadth, the TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B profile-to-component mapping, phage-trigger specificity, TIR-domain output chemistry, and rule-level DefenseFinder detection criteria before minting narrower TIR-VII mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TIR-VII system",
  "source_id": "traitmech:000483",
  "source_file": "tir_vii_system.yaml",
  "attaches_to": [
   "causal_graphs#tir_vii_locus_inhibits_phage_plaquing"
  ],
  "rationale": "Wang et al. support TIR-VII as one of nine newly named TIR-domain anti-phage defense systems and note that TIR-VII was recovered in a single form with TIR-VIII. The pinned DefenseFinder HMM inventory records TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B custom profile rows, but the pinned DefenseFinder rules table has no TIR-VII row. This first record therefore does not assert profile requirement logic, accession-level components, a direct phage trigger, or TIR-domain output chemistry.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-51738-3",
   "DOI:10.1038/s41467-024-51738-3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tir_vii_system.html#tir-vii-detection-trigger-gap"
 },
 {
  "discussion_id": "tir-viii-detection-trigger-gap",
  "prompt": "Resolve TIR-VIII native host breadth, the TIR-VIII__TIR-VIII_A and TIR-VIII__TIR-VIII_B profile-to-component mapping, phage-trigger specificity, TIR-domain output chemistry, and rule-level DefenseFinder detection criteria before minting narrower TIR-VIII mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "TIR-VIII system",
  "source_id": "traitmech:000484",
  "source_file": "tir_viii_system.yaml",
  "attaches_to": [
   "causal_graphs#tir_viii_locus_inhibits_phage_plaquing"
  ],
  "rationale": "Wang et al. support TIR-VIII as one of nine newly named TIR-domain anti-phage defense systems and note that TIR-VIII was recovered in a single form with TIR-VII. The pinned DefenseFinder HMM inventory records TIR-VIII__TIR-VIII_A and TIR-VIII__TIR-VIII_B custom profile rows, but the pinned DefenseFinder rules table has no TIR-VIII row. This first record therefore does not assert profile requirement logic, accession-level components, a direct phage trigger, or TIR-domain output chemistry.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1038/s41467-024-51738-3",
   "DOI:10.1038/s41467-024-51738-3",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/tir_viii_system.html#tir-viii-detection-trigger-gap"
 },
 {
  "discussion_id": "toga-mechanism-and-modelling-gap",
  "prompt": "Resolve Toga locus breadth, exact phage triggers, direct molecular output, source-system table rows, and DefenseFinder HMM/rule coverage before minting narrower Toga mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Toga system",
  "source_id": "traitmech:000498",
  "source_file": "toga_system.yaml",
  "attaches_to": [
   "causal_graphs#toga_locus_restricts_phage"
  ],
  "rationale": "de Sousa et al. support Toga as one of the novel P4-encoded systems with experimental phage-protection activity, and the pinned DefenseFinder article registry maps the Toga source key to the corresponding preprint. The pinned HMM inventory and rules table have no exact Toga rows, and this first-pass record does not resolve the tested source locus, complete phage breadth, exact trigger, molecular output, or detection rule.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1093/nar/gkag898",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/toga_system.html#toga-mechanism-and-modelling-gap"
 },
 {
  "discussion_id": "toutatis-mechanism-gap",
  "prompt": "Resolve Toutatis phage triggers and effector outputs before minting narrower Toutatis mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Toutatis system",
  "source_id": "traitmech:000267",
  "source_file": "toutatis_system.yaml",
  "attaches_to": [
   "causal_graphs#toutatis_locus_restricts_phage"
  ],
  "rationale": "Darracq et al. and DefenseFinder support Toutatis as a named anti-phage system with TutA_VCA0446 and TutB_VCA0447 profiles, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/toutatis_system.html#toutatis-mechanism-gap"
 },
 {
  "discussion_id": "type-i-rm-profile-interpretation-gap",
  "prompt": "Resolve the accession-level relationships between DefenseFinder RM Type I custom methyltransferase, restriction-endonuclease, and specificity-subunit profiles and characterized HsdR, HsdM, and HsdS families before minting narrower Type I protein or custom-profile traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "type I restriction-modification system",
  "source_id": "traitmech:000494",
  "source_file": "type_i_restriction_modification_system.yaml",
  "attaches_to": [
   "causal_graphs#type_i_rm_locus_restricts_foreign_dna"
  ],
  "rationale": "Loenen et al. support Type I R-M system architecture and restriction/modification activity, while the pinned DefenseFinder registry supports an RM_Type_I namespace with broad Type_I_MTases, Type_I_REases, and Type_I_S custom profile groups. The evidence does not yet map individual custom profile rows to exact characterized Hsd families or resolve whether each source-model boundary corresponds to a reusable organism-level trait below this class.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1093/nar/gkt847",
   "DOI:10.1093/nar/gkt847",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/type_i_restriction_modification_system.html#type-i-rm-profile-interpretation-gap"
 },
 {
  "discussion_id": "type-ii-rm-profile-interpretation-gap",
  "prompt": "Resolve the accession-level relationships between DefenseFinder RM_Type_II custom methyltransferase and restriction-endonuclease profiles, characterized Type II enzyme families, and Type IIG subclass boundaries before minting narrower Type II protein or custom-profile traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "type II restriction-modification system",
  "source_id": "traitmech:000493",
  "source_file": "type_ii_restriction_modification_system.yaml",
  "attaches_to": [
   "causal_graphs#type_ii_rm_locus_restricts_foreign_dna"
  ],
  "rationale": "Kirillov et al. and Pingoud et al. support Type II R-M system architecture and Type II restriction-endonuclease activity, while the pinned DefenseFinder registry supports an RM_Type_II namespace with broad custom MTase and REase profile groups. The evidence does not yet map individual custom profile rows to exact characterized enzyme families or resolve whether each source-model boundary corresponds to a reusable organism-level trait below this class.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1093/nar/gkac1124",
   "DOI:10.1093/nar/gku447",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/type_ii_restriction_modification_system.html#type-ii-rm-profile-interpretation-gap"
 },
 {
  "discussion_id": "type-iig-rm-profile-interpretation-gap",
  "prompt": "Resolve the accession-level relationships between DefenseFinder RM_Type_IIG custom profiles, characterized BpuSI- or Tth111II-like enzymes, and companion methyltransferases before minting narrower Type IIG protein or subfamily traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "type IIG restriction-modification system",
  "source_id": "traitmech:000375",
  "source_file": "type_iig_restriction_modification_system.yaml",
  "attaches_to": [
   "causal_graphs#type_iig_rm_locus_restricts_foreign_dna"
  ],
  "rationale": "Shen et al. and Zhu et al. support Type IIG R-M system architecture and experimentally characterized BpuSI and Tth111II examples, while the pinned DefenseFinder registry supports an RM_Type_IIG system-level namespace with eight custom HMM rows. The evidence does not yet map each custom profile row to exact characterized enzyme families or resolve companion methyltransferase requirements.",
  "num_experiments": 0,
  "num_evidence": 4,
  "evidence_refs": [
   "DOI:10.1093/nar/gkr543",
   "DOI:10.1038/srep03838",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/type_iig_restriction_modification_system.html#type-iig-rm-profile-interpretation-gap"
 },
 {
  "discussion_id": "type-iii-rm-profile-interpretation-gap",
  "prompt": "Resolve the accession-level relationships between DefenseFinder RM_Type_III custom methyltransferase and restriction-endonuclease profiles and characterized Mod and Res families before minting narrower Type III protein or custom-profile traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "type III restriction-modification system",
  "source_id": "traitmech:000495",
  "source_file": "type_iii_restriction_modification_system.yaml",
  "attaches_to": [
   "causal_graphs#type_iii_rm_locus_restricts_foreign_dna"
  ],
  "rationale": "Butterer et al. support Type III R-M Res/Mod architecture, while the pinned DefenseFinder registry supports an RM_Type_III namespace with broad Type_III_MTases and Type_III_REases custom profile groups. The evidence does not yet map individual custom profile rows to exact characterized Res or Mod families or resolve whether each source-model boundary corresponds to a reusable organism-level trait below this class.",
  "num_experiments": 0,
  "num_evidence": 5,
  "evidence_refs": [
   "DOI:10.1093/nar/gku122",
   "DOI:10.1093/nar/gku122",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/type_iii_restriction_modification_system.html#type-iii-rm-profile-interpretation-gap"
 },
 {
  "discussion_id": "type-iv-rm-profile-interpretation-gap",
  "prompt": "Resolve the accession-level relationships between DefenseFinder RM_Type_IV custom Type_IV_REases profiles and the characterized McrA family before minting narrower Type IV custom-profile traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "type IV modification-dependent restriction system",
  "source_id": "traitmech:000496",
  "source_file": "type_iv_modification_dependent_restriction_system.yaml",
  "attaches_to": [
   "causal_graphs#type_iv_modification_dependent_restriction"
  ],
  "rationale": "Loenen and Raleigh support the broad Type IV modification-dependent restriction class, and the pinned DefenseFinder registries support an RM_Type_IV namespace with a broad Type_IV_REases custom profile group. The evidence does not yet map any of the eight pinned RM_Type_IV HMM rows to the characterized McrA family or resolve whether the Other_Type_IV article-registry row corresponds to a reusable organism-level trait below this class.",
  "num_experiments": 0,
  "num_evidence": 6,
  "evidence_refs": [
   "DOI:10.1093/nar/gkt747",
   "DOI:10.1093/nar/gkt747",
   "DOI:10.1016/j.jmb.2006.11.051",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/type_iv_modification_dependent_restriction_system.html#type-iv-rm-profile-interpretation-gap"
 },
 {
  "discussion_id": "ukko-mechanism-gap",
  "prompt": "Resolve Ukko phage triggers and effector outputs before minting narrower Ukko mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Ukko system",
  "source_id": "traitmech:000292",
  "source_file": "ukko_system.yaml",
  "attaches_to": [
   "causal_graphs#ukko_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Ukko as a named anti-phage system with UkkA1, UkkA2, UkkB1, UkkB2, UkkC1, UkkC2, UkkD1, and UkkD2 HMM profile entries, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/ukko_system.html#ukko-mechanism-gap"
 },
 {
  "discussion_id": "uzume-mechanism-gap",
  "prompt": "Resolve Uzume phage triggers and effector outputs before minting narrower Uzume mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Uzume system",
  "source_id": "traitmech:000262",
  "source_file": "uzume_system.yaml",
  "attaches_to": [
   "causal_graphs#uzume_locus_restricts_phage"
  ],
  "rationale": "Millman et al. and DefenseFinder support Uzume as a named anti-phage system with a UzuA profile, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/uzume_system.html#uzume-mechanism-gap"
 },
 {
  "discussion_id": "vcam4i-defensefinder-model-gap",
  "prompt": "Resolve VcaM4I-family breadth, modified-cytosine sequence-context specificity across natural hosts, accession-level protein examples, and DefenseFinder RM_Type_IV HMM/rules mapping before minting narrower VcaM4I mechanism or component traits.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VcaM4I system",
  "source_id": "traitmech:000514",
  "source_file": "vcam4i_system.yaml",
  "attaches_to": [
   "causal_graphs#vcam4i_restricts_modified_cytosine_dna"
  ],
  "rationale": "Mierzejewska et al. support VcaM4I as an EVE-HNH modification-dependent restriction endonuclease that recognizes 5mC/5hmC DNA and validate EVE-domain modified-base binding plus HNH catalytic residues by digestion and restriction assays. The pinned DefenseFinder article registry maps VcaM4I to that paper, but the pinned HMM inventory and rules table have no exact VcaM4I rows. This first-pass record therefore does not resolve a reusable DefenseFinder profile model, exact accession-level protein examples, the breadth of VcaM4I-like systems across natural hosts, or the complete set of natural modified-cytosine sequence contexts.",
  "num_experiments": 0,
  "num_evidence": 7,
  "evidence_refs": [
   "DOI:10.1093/nar/gkaa1218",
   "DOI:10.1093/nar/gkaa1218",
   "DOI:10.1093/nar/gkaa1218",
   "DOI:10.1093/nar/gkaa1218",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vcam4i_system.html#vcam4i-defensefinder-model-gap"
 },
 {
  "discussion_id": "veles-mechanism-gap",
  "prompt": "Resolve Veles phage triggers and effector outputs before minting narrower Veles mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Veles system",
  "source_id": "traitmech:000289",
  "source_file": "veles_system.yaml",
  "attaches_to": [
   "causal_graphs#veles_locus_restricts_phage"
  ],
  "rationale": "Mordret et al. and DefenseFinder support Veles as a named anti-phage system with VlsA1, VlsA2, VlsB1, VlsB2, VlsC1, and VlsC2 HMM profile entries, but the trigger, molecular substrate, antiviral effector output, and subtype-specific mechanism are not resolved enough here to assert a narrower mechanistic child trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/veles_system.html#veles-mechanism-gap"
 },
 {
  "discussion_id": "viperin-product-and-subtype-gap",
  "prompt": "Resolve Viperin nucleotide products, accessory genes, and phage-target breadth before minting narrower Viperin mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Viperin system",
  "source_id": "traitmech:000263",
  "source_file": "viperin_system.yaml",
  "attaches_to": [
   "causal_graphs#viperin_modified_ribonucleotides_restrict_phage"
  ],
  "rationale": "Bernheim et al. support prokaryotic viperins as phage-protective producers of modified ribonucleotides, and DefenseFinder models Viperin through the pVip profile, but Viperin-family loci need separate review before TraitMech asserts one universal antiviral nucleotide, polymerase target, or accessory-gene architecture.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/viperin_system.html#viperin-product-and-subtype-gap"
 },
 {
  "discussion_id": "vp1796-defensefinder-model-gap",
  "prompt": "Resolve VP1796 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1796 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1796 system",
  "source_id": "traitmech:000486",
  "source_file": "vp1796_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1796_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1796 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1796 to VP_RS08620/Vp1796, WP_005477844.1, VSV105-vp1796, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1796 custom profile row. The pinned rules table has no VP1796 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1796_system.html#vp1796-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1817-defensefinder-model-gap",
  "prompt": "Resolve VP1817 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1817 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1817 system",
  "source_id": "traitmech:000487",
  "source_file": "vp1817_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1817_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1817 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1817 to VP_RS08765/VP1817, WP_024699215.1, VSV105-vp1817, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1817 custom profile row. The pinned rules table has no VP1817 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1817_system.html#vp1817-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1823-defensefinder-model-gap",
  "prompt": "Resolve VP1823 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1823 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1823 system",
  "source_id": "traitmech:000485",
  "source_file": "vp1823_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1823_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1823 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1823 to VP_RS08795/VP1823, WP_079749463.1, VSV105-vp1823, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1823 custom profile row. The pinned rules table has no VP1823 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1823_system.html#vp1823-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1826-defensefinder-model-gap",
  "prompt": "Resolve VP1826 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1826 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1826 system",
  "source_id": "traitmech:000488",
  "source_file": "vp1826_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1826_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1826 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1826 to VP_RS08820/Vp1826, WP_005464673.1, VSV105-vp1826, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1826 custom profile row. The pinned rules table has no VP1826 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1826_system.html#vp1826-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1839-defensefinder-model-gap",
  "prompt": "Resolve VP1839 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1839 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1839 system",
  "source_id": "traitmech:000489",
  "source_file": "vp1839_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1839_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1839 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1839 to VP_RS08915/Vp1839, WP_024699234.1, VSV105-vp1839, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1839 custom profile row. The pinned rules table has no VP1839 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 11,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1839_system.html#vp1839-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1840-defensefinder-model-gap",
  "prompt": "Resolve VP1840 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1840 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1840 system",
  "source_id": "traitmech:000450",
  "source_file": "vp1840_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1840_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1840 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1840 to VP_RS08920/Vp1840, WP_005483293.1, VSV105-vp1840, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1840 custom profile row. The pinned rules table has no VP1840 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1840_system.html#vp1840-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1848-defensefinder-model-gap",
  "prompt": "Resolve VP1848 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1848 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1848 system",
  "source_id": "traitmech:000490",
  "source_file": "vp1848_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1848_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1848 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1848 to VP_RS08970/Vp1848, WP_005483286.1, VSV105-vp1848, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1848 custom profile row. The pinned rules table has no VP1848 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1848_system.html#vp1848-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1851-defensefinder-model-gap",
  "prompt": "Resolve VP1851 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1851 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1851 system",
  "source_id": "traitmech:000491",
  "source_file": "vp1851_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1851_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1851 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1851 to VP_RS09000/Vp1851, WP_005483174.1, VSV105-vp1851, and phage-plating fold changes, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1851 custom profile row. The pinned rules table has no VP1851 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 10,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1851_system.html#vp1851-defensefinder-model-gap"
 },
 {
  "discussion_id": "vp1853-defensefinder-model-gap",
  "prompt": "Resolve VP1853 native host breadth, exact single-component activity, profile-to-protein mapping, homolog boundary, full phage breadth, molecular output, and rule-level DefenseFinder criteria before minting narrower VP1853 mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "VP1853 system",
  "source_id": "traitmech:000492",
  "source_file": "vp1853_system.yaml",
  "attaches_to": [
   "causal_graphs#vp1853_locus_reduces_bacteriophage_plaquing"
  ],
  "rationale": "Getz et al. support VP1853 as one of nine RIMD 2210633 integron-encoded cassettes whose cloned expression reduced phage plaquing, Supplementary Tables 8, 9, and 12 map VP1853 to VP_RS09025/Vp1853, WP_005483178.1, VSV105-vp1853, and a phage-plating fold change, and Supplementary Data 1 reports PSI-BLAST homologs. The pinned DefenseFinder HMM inventory records one VP1853 custom profile row. The pinned rules table has no VP1853 row, and the first-pass record does not resolve native host breadth, complete phage breadth, direct profile-to-protein correspondence, molecular output, or endogenous activity.",
  "num_experiments": 0,
  "num_evidence": 9,
  "evidence_refs": [
   "DOI:10.1038/s41564-025-01927-7",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM2_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/41564_2025_1927_MOESM3_ESM.xlsx",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/Liste_hmm_system.md",
   "https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/DefenseFinder_rules.tsv"
  ],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/vp1853_system.html#vp1853-defensefinder-model-gap"
 },
 {
  "discussion_id": "wadjet-subfamily-and-substrate-gap",
  "prompt": "Resolve JetABCD, EptABCD, DefenseFinder Wadjet subtype boundaries, plasmid substrate specificity, and activation cues before minting additional narrower Wadjet mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Wadjet system",
  "source_id": "traitmech:000218",
  "source_file": "wadjet_system.yaml",
  "attaches_to": [],
  "rationale": "Deep et al. and Liu et al. support JetABCD-mediated topology- or shape-biased circular plasmid cleavage and the broad JetABCD/MksBEFG/EptABCD Wadjet family, while the MksBEFG child now captures the Weiss et al. plasmid-degradation branch. The parent still leaves JetABCD, EptABCD, DefenseFinder Wadjet I-III boundaries, exact target size threshold, linear-plasmid escape rule, loop-extrusion endpoint, polar localization pattern, and nuclease activation models for additional Wadjet variants unresolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/wadjet_system.html#wadjet-subfamily-and-substrate-gap"
 },
 {
  "discussion_id": "zorya-subtype-effector-and-trigger-gap",
  "prompt": "Resolve Zorya subtype effectors, ion usage, and phage triggers before minting narrower Zorya mechanism children.",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Zorya system",
  "source_id": "traitmech:000217",
  "source_file": "zorya_system.yaml",
  "attaches_to": [],
  "rationale": "Hu et al. support Type I ZorAB activation and ZorC/ZorD-mediated phage-DNA degradation, and Mariano et al. support Type I/II ZorAB architecture plus a recruited Type II ZorE nickase, but Zorya variants need separate review before TraitMech asserts one universal ion substrate, effector composition, nuclease target, cell-death pathway, Type III mechanism, or anti-defense breadth.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/genomics/zorya_system.html#zorya-subtype-effector-and-trigger-gap"
 },
 {
  "discussion_id": "acetoclastic-methanogenesis-xref-gap",
  "prompt": "Resolve an exact external ontology xref for acetate-splitting methanogenesis before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "acetoclastic methanogenesis",
  "source_id": "traitmech:000191",
  "source_file": "acetoclastic_methanogenesis.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete METPO:1000865 Acetoclastic methanogenesis. GO:0015948 methane biosynthetic process is exact only for the broader methanogenesis parent, and no exact active external class has yet been resolved for the acetate-splitting branch.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/acetoclastic_methanogenesis.html#acetoclastic-methanogenesis-xref-gap"
 },
 {
  "discussion_id": "acetone-butanol-ethanol-fermentation-xref-gap",
  "prompt": "Resolve an exact external ontology class for acetone-butanol-ethanol fermentation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "acetone-butanol-ethanol fermentation",
  "source_id": "traitmech:000180",
  "source_file": "acetone_butanol_ethanol_fermentation.yaml",
  "attaches_to": [],
  "rationale": "No exact GO or external metabolism class was resolved for the organism-level ABE fermentation phenotype; broader fermentation classes and individual solvent-production reactions are shifted relative to this product-specific fermentation class.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html#acetone-butanol-ethanol-fermentation-xref-gap"
 },
 {
  "discussion_id": "anaerobic-ammonium-oxidation-xref-gap",
  "prompt": "Resolve an exact external ontology class for anaerobic ammonium oxidation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "anaerobic ammonium oxidation",
  "source_id": "traitmech:000188",
  "source_file": "anaerobic_ammonium_oxidation.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only METPO:1000812 obsolete Anaerobic ammonium oxidation. Candidate GO classes should be checked against the primary Gene Ontology release before adding an exact xref because component ammonium- or nitrite-oxidation processes are narrower than the whole anammox metabolism.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/anaerobic_ammonium_oxidation.html#anaerobic-ammonium-oxidation-xref-gap"
 },
 {
  "discussion_id": "arsenate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level arsenate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "arsenate respiration",
  "source_id": "traitmech:000195",
  "source_file": "arsenate_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains obsolete arsenate reduction and arsenate-reducing classes but no active organism-level arsenate respiration class. Potential GO, Rhea, EC, and protein-family terms for respiratory arsenate reductase are narrower than the whole-organism anaerobic respiration phenotype, and future groundings must keep ArrAB respiratory reduction separate from ArsC cytosolic detoxification.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/arsenate_respiration.html#arsenate-respiration-xref-gap"
 },
 {
  "discussion_id": "arsenite-oxidation-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level arsenite oxidation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "arsenite oxidation",
  "source_id": "traitmech:000189",
  "source_file": "arsenite_oxidation.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only METPO:1000840 obsolete Arsenite oxidation. Potential external molecular function terms for arsenite oxidase activity are narrower than the organism-level As(III)-to-As(V) metabolism, and a future mechanism graph should distinguish aerobic AioBA oxidation from anaerobic ArxAB-mediated arsenite oxidation.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/arsenite_oxidation.html#arsenite-oxidation-xref-gap"
 },
 {
  "discussion_id": "butanediol-fermentation-xref-gap",
  "prompt": "Resolve an exact external ontology class for 2,3-butanediol fermentation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "2,3-butanediol fermentation",
  "source_id": "traitmech:000181",
  "source_file": "butanediol_fermentation.yaml",
  "attaches_to": [],
  "rationale": "No exact GO or external metabolism class was resolved for the organism-level 2,3-butanediol fermentation phenotype; Voges-Proskauer assay terms, acetoin or butanediol chemical production reactions, and individual dehydrogenase molecular functions are shifted relative to this product-specific fermentation class.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/butanediol_fermentation.html#butanediol-fermentation-xref-gap"
 },
 {
  "discussion_id": "butyric-acid-fermentation-xref-gap",
  "prompt": "Resolve an exact external ontology class for butyric acid fermentation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "butyric acid fermentation",
  "source_id": "traitmech:000179",
  "source_file": "butyric_acid_fermentation.yaml",
  "attaches_to": [],
  "rationale": "No exact GO or external metabolism class was resolved for the organism-level butyrate-producing fermentation phenotype; butyrate-synthesis enzyme molecular functions and chemical production relations are shifted relative to this product-specific fermentation class.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/butyric_acid_fermentation.html#butyric-acid-fermentation-xref-gap"
 },
 {
  "discussion_id": "chlorate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level chlorate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "chlorate respiration",
  "source_id": "traitmech:000198",
  "source_file": "chlorate_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only the obsolete broad (Per)chlorate respiration class and no active exact organism-level chlorate respiration class. Candidate EC, Rhea, and protein-family terms for chlorate reductase or chlorite dismutase are narrower than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/chlorate_respiration.html#chlorate-respiration-xref-gap"
 },
 {
  "discussion_id": "citrate-fermentation-xref-gap",
  "prompt": "Resolve an exact external ontology class for citrate fermentation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "citrate fermentation",
  "source_id": "traitmech:000182",
  "source_file": "citrate_fermentation.yaml",
  "attaches_to": [],
  "rationale": "No exact GO or external metabolism class was resolved for anaerobic citrate fermentation; generic citrate metabolic process terms, citrate lyase or transporter molecular functions, and citrate-test assay terms are shifted relative to this pathway-scoped fermentation class.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/citrate_fermentation.html#citrate-fermentation-xref-gap"
 },
 {
  "discussion_id": "complete-ammonia-oxidation-xref-gap",
  "prompt": "Resolve an exact external ontology class for one-organism complete ammonia oxidation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "complete ammonia oxidation",
  "source_id": "traitmech:000187",
  "source_file": "complete_ammonia_oxidation.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only METPO:1000862 obsolete Complete ammonia oxidation. METPO:1005001 denotes nitrification without requiring both oxidation steps to occur in one organism, while GO:0019329 ammonia oxidation and GO:0019332 nitrite oxidation each cover only one component of the comammox phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/complete_ammonia_oxidation.html#complete-ammonia-oxidation-xref-gap"
 },
 {
  "discussion_id": "dimethyl-sulfoxide-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level dimethyl sulfoxide respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "dimethyl sulfoxide respiration",
  "source_id": "traitmech:000201",
  "source_file": "dimethyl_sulfoxide_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot has only an obsolete dimethyl sulfoxide respiration class. Candidate EC, Rhea, KEGG, and protein-family terms for DMSO reductase or DmsABC are narrower than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/dimethyl_sulfoxide_respiration.html#dimethyl-sulfoxide-respiration-xref-gap"
 },
 {
  "discussion_id": "fumarate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level fumarate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "fumarate respiration",
  "source_id": "traitmech:000196",
  "source_file": "fumarate_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete Fumarate respiration and no active organism-level class for anaerobic respiration using fumarate as the terminal electron acceptor. Potential GO, Rhea, EC, and protein-family terms for fumarate reductase or the fumarate-to-succinate reaction are narrower than the whole-organism anaerobic respiration phenotype and should be checked separately before grounding FrdABCD-level causal nodes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/fumarate_respiration.html#fumarate-respiration-xref-gap"
 },
 {
  "discussion_id": "iodate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level iodate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "iodate respiration",
  "source_id": "traitmech:000203",
  "source_file": "iodate_respiration.yaml",
  "attaches_to": [],
  "rationale": "Candidate Idr, DmsAB, EC, Rhea, and protein-family terms describe narrower iodate reductase activities, reactions, or enzymes rather than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/iodate_respiration.html#iodate-respiration-xref-gap"
 },
 {
  "discussion_id": "lipolysis-xref-gap",
  "prompt": "Resolve an exact external ontology xref for organism-level microbial lipolysis before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "lipolysis",
  "source_id": "traitmech:000190",
  "source_file": "lipolysis.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete METPO:1000175 lipolysis, and GO:0016298 denotes the lipase molecular function rather than the organism-level lipid-hydrolysis trait. GO lipid catabolic process classes also include downstream fatty-acid catabolism and are broader than lipase-driven triacylglycerol hydrolysis.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/lipolysis.html#lipolysis-xref-gap"
 },
 {
  "discussion_id": "methyl-based-methanogenesis-xref-gap",
  "prompt": "Resolve an exact external ontology xref for methyl-substrate methanogenesis before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "methyl-based methanogenesis",
  "source_id": "traitmech:000192",
  "source_file": "methyl_based_methanogenesis.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete METPO:1000866 Methylotrophic methanogenesis. The existing methylotrophic record is the broader reduced-one-carbon trophic type, and GO:0015948 methane biosynthetic process is exact only for the broader methanogenesis parent, so no exact active external class has yet been resolved for this methyl-substrate branch.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/methyl_based_methanogenesis.html#methyl-based-methanogenesis-xref-gap"
 },
 {
  "discussion_id": "nitrification-component-go-xref-gap",
  "prompt": "Resolve an exact external ontology class for the complete nitrification process before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "nitrification",
  "source_id": "METPO:1005001",
  "source_file": "nitrification.yaml",
  "attaches_to": [],
  "rationale": "METPO cites GO:0019329 ammonia oxidation and GO:0019332 nitrite oxidation as definition components, but each GO term covers only one half of the full two-step nitrification trait and is not exact enough for TraitRecord xrefs.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/nitrification.html#nitrification-component-go-xref-gap"
 },
 {
  "discussion_id": "organohalide-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level organohalide respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "organohalide respiration",
  "source_id": "traitmech:000204",
  "source_file": "organohalide_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete Halogenated compound respiration and Organohalide respiration classes. Candidate reductive dehalogenase protein-family and enzyme terms are narrower than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/organohalide_respiration.html#organohalide-respiration-xref-gap"
 },
 {
  "discussion_id": "perchlorate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level perchlorate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "perchlorate respiration",
  "source_id": "traitmech:000197",
  "source_file": "perchlorate_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only obsolete (Per)chlorate respiration, Perchlorate respiration, and Perchlorate-reducing classes. Candidate GO, EC, and protein-family terms for perchlorate reductase and chlorite dismutase are narrower than the whole-organism anaerobic respiration phenotype and should be checked separately before grounding PcrABCD- or Cld-level causal nodes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/perchlorate_respiration.html#perchlorate-respiration-xref-gap"
 },
 {
  "discussion_id": "photoferrotrophy-xref-gap",
  "prompt": "Resolve an exact external ontology class for photoferrotrophy before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "photoferrotrophy",
  "source_id": "traitmech:000193",
  "source_file": "photoferrotrophy.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot has no active photoferrotrophy or anoxygenic phototrophic Fe(II) oxidation class. Candidate GO classes for photosynthesis, photosynthetic electron transport, and carbon fixation are broader than this Fe(II)-donor organismal metabolism, so no exact external class has yet been resolved.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/photoferrotrophy.html#photoferrotrophy-xref-gap"
 },
 {
  "discussion_id": "photoferrotrophy-protein-example-gap",
  "prompt": "Resolve a live, audit-clean UniProt protein example for a taxon-specific photoferrotrophy branch.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "photoferrotrophy",
  "source_id": "traitmech:000193",
  "source_file": "photoferrotrophy.yaml",
  "attaches_to": [],
  "rationale": "R. palustris TIE-1 PioA and R. ferrooxidans SW2 FoxE have DOI-backed primary evidence, but their current exact UniProtKB accessions are unreviewed entries without live Proteomes cross-references. The first graph therefore stays process-level until a reviewed or audit-verifiable exact entry is available.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/photoferrotrophy.html#photoferrotrophy-protein-example-gap"
 },
 {
  "discussion_id": "selenate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level selenate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "selenate respiration",
  "source_id": "traitmech:000202",
  "source_file": "selenate_respiration.yaml",
  "attaches_to": [],
  "rationale": "Candidate EC, Rhea, and protein-family terms for selenate reductase describe narrower molecular functions, reactions, or enzymes rather than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/selenate_respiration.html#selenate-respiration-xref-gap"
 },
 {
  "discussion_id": "tetrathionate-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level tetrathionate respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "tetrathionate respiration",
  "source_id": "traitmech:000200",
  "source_file": "tetrathionate_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot has no active organism-level class for tetrathionate respiration. Candidate EC, Rhea, and protein-family terms for tetrathionate reductase or the TtrA/TtrB/TtrC complex are narrower than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/tetrathionate_respiration.html#tetrathionate-respiration-xref-gap"
 },
 {
  "discussion_id": "trimethylamine-n-oxide-respiration-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level trimethylamine N-oxide respiration before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "trimethylamine N-oxide respiration",
  "source_id": "traitmech:000199",
  "source_file": "trimethylamine_n_oxide_respiration.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot has no active organism-level class for trimethylamine N-oxide respiration. Candidate EC, Rhea, and protein-family terms for TorA or broader trimethylamine N-oxide reductases are narrower than the whole-organism anaerobic respiration phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/metabolism/trimethylamine_n_oxide_respiration.html#trimethylamine-n-oxide-respiration-xref-gap"
 },
 {
  "discussion_id": "akinete-exact-xref-gap",
  "prompt": "Resolve exact external ontology xrefs for the cyanobacterial akinete morphology trait.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "akinete",
  "source_id": "traitmech:000185",
  "source_file": "akinete.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only deprecated akinete classes, including METPO:1000012 obsolete akinete; no active METPO, GO, or OBO class was accepted as an exact equivalent for this cyanobacterial dormant-cell trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/morphology/akinete.html#akinete-exact-xref-gap"
 },
 {
  "discussion_id": "ferrosome-xref-gap",
  "prompt": "Resolve exact external ontology xrefs for the bacterial ferrosome morphology trait.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "ferrosome",
  "source_id": "traitmech:000527",
  "source_file": "ferrosome.yaml",
  "attaches_to": [],
  "rationale": "No exact active METPO, GO, or OBO class was accepted for the organism-level ferrosome morphology trait. GO:0110143 magnetosome, GO:0031411 gas vesicle, GO:0031470 carboxysome, and GO:0070088 PHA granule are sibling organelles or inclusions rather than ferrosome equivalents.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/morphology/ferrosome.html#ferrosome-xref-gap"
 },
 {
  "discussion_id": "holdfast-exact-xref-gap",
  "prompt": "Resolve exact external ontology xrefs for the bacterial holdfast morphology trait.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "holdfast",
  "source_id": "traitmech:000184",
  "source_file": "holdfast.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only the deprecated METPO:1000158 obsolete holdfast class; no active METPO, GO, or OBO class was accepted as an exact equivalent for this bacterial adhesive-matrix trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/morphology/holdfast.html#holdfast-exact-xref-gap"
 },
 {
  "discussion_id": "catalase-negative-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for negative catalase-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "catalase negative",
  "source_id": "METPO:1007084",
  "source_file": "catalase_negative.yaml",
  "attaches_to": [],
  "rationale": "METPO:1007080 is now represented as the seeded catalase-test assay parent, so this negative assay-outcome phenotype can use its source superclass rather than a temporary direct phenotype parent.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/catalase_negative.html#catalase-negative-assay-parent-gap"
 },
 {
  "discussion_id": "indole-test-negative-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for negative indole-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "indole test negative",
  "source_id": "METPO:1005012",
  "source_file": "indole_test_negative.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005010 is the seeded superclass of METPO:1005012, but METPO:1005010 defines an assay rather than a broader microbial trait class, so this record is temporarily parented directly to METPO:1000059 phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/indole_test_negative.html#indole-test-negative-assay-parent-gap"
 },
 {
  "discussion_id": "indole-test-positive-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for positive indole-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "indole test positive",
  "source_id": "METPO:1005011",
  "source_file": "indole_test_positive.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005010 is the seeded superclass of METPO:1005011, but METPO:1005010 defines an assay rather than a broader microbial trait class, so this record is temporarily parented directly to METPO:1000059 phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/indole_test_positive.html#indole-test-positive-assay-parent-gap"
 },
 {
  "discussion_id": "methyl-red-test-negative-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for negative methyl-red-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "methyl red test negative",
  "source_id": "METPO:1005015",
  "source_file": "methyl_red_test_negative.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005013 is the seeded superclass of METPO:1005015, but METPO:1005013 defines an assay rather than a broader microbial trait class, so this record is temporarily parented directly to METPO:1000059 phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/methyl_red_test_negative.html#methyl-red-test-negative-assay-parent-gap"
 },
 {
  "discussion_id": "methyl-red-test-positive-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for positive methyl-red-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "methyl red test positive",
  "source_id": "METPO:1005014",
  "source_file": "methyl_red_test_positive.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005013 is the seeded superclass of METPO:1005014, but METPO:1005013 defines an assay rather than a broader microbial trait class, so this record is temporarily parented directly to METPO:1000059 phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/methyl_red_test_positive.html#methyl-red-test-positive-assay-parent-gap"
 },
 {
  "discussion_id": "non-hemolytic-parent-gap",
  "prompt": "Resolve a neutral parent axis for absence of hemolysis before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "non-hemolytic",
  "source_id": "METPO:1005027",
  "source_file": "non_hemolytic.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005025 is the seeded superclass of METPO:1005027, but METPO:1005025 defines the ability to lyse red blood cells; this absence phenotype is temporarily parented directly to METPO:1000059 phenotype until METPO has a neutral hemolysis axis or another broader parent for hemolysis-test outcomes.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/non_hemolytic.html#non-hemolytic-parent-gap"
 },
 {
  "discussion_id": "voges-proskauer-test-positive-assay-parent-gap",
  "prompt": "Resolve a non-assay parent for positive Voges-Proskauer-test phenotypes before narrowing parent_traits below phenotype.",
  "kind": "CURATION_TODO",
  "status": "RESOLVED",
  "is_gap": "Other discussion",
  "source_name": "Voges-Proskauer test positive",
  "source_id": "METPO:1005017",
  "source_file": "voges_proskauer_test_positive.yaml",
  "attaches_to": [],
  "rationale": "METPO:1005016 is the seeded superclass of METPO:1005017, but METPO:1005016 defines an assay rather than a broader microbial trait class, so this record is temporarily parented directly to METPO:1000059 phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/other/voges_proskauer_test_positive.html#voges-proskauer-test-positive-assay-parent-gap"
 },
 {
  "discussion_id": "acid-phosphatase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for acid phosphatase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "acid phosphatase activity",
  "source_id": "traitmech:000142",
  "source_file": "acid_phosphatase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0003993 carries the same acid phosphatase activity label but denotes the enzyme molecular function rather than the organism-level phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/acid_phosphatase_activity.html#acid-phosphatase-activity-xref-gap"
 },
 {
  "discussion_id": "aerobic-anoxygenic-phototrophy-xref-gap",
  "prompt": "Resolve an exact external ontology class for aerobic anoxygenic phototrophy before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "aerobic anoxygenic phototrophy",
  "source_id": "traitmech:000194",
  "source_file": "aerobic_anoxygenic_phototrophy.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot carries aerobic_anoxygenic_phototrophy only as a related synonym on broad phototrophic, and GO photosynthetic electron transport classes denote the intracellular pathway rather than this organism-level aerobic photoheterotrophic trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/aerobic_anoxygenic_phototrophy.html#aerobic-anoxygenic-phototrophy-xref-gap"
 },
 {
  "discussion_id": "alanine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alanine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alanine arylamidase activity",
  "source_id": "traitmech:000161",
  "source_file": "alanine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016285 alanyl aminopeptidase activity denotes the catalytic molecular function rather than the organism-level alanine arylamidase/alanyl aminopeptidase phenotype, so it is appropriate as a causal-node grounding for that enzyme activity and not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alanine_arylamidase_activity.html#alanine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "alkaline-phosphatase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alkaline phosphatase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alkaline phosphatase activity",
  "source_id": "traitmech:000141",
  "source_file": "alkaline_phosphatase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004035 carries the same alkaline phosphatase activity label but denotes the enzyme molecular function rather than the organism-level phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alkaline_phosphatase_activity.html#alkaline-phosphatase-activity-xref-gap"
 },
 {
  "discussion_id": "alpha-chymotrypsin-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alpha-chymotrypsin activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alpha-chymotrypsin activity",
  "source_id": "traitmech:000159",
  "source_file": "alpha_chymotrypsin_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004263 chymotrypsin activity is obsolete, and its replacement GO:0004252 denotes broader serine-type endopeptidase molecular function rather than the organism-level chymotrypsin-like serine endopeptidase phenotype. GO:0004252 is appropriate as a causal-node grounding for generic serine-type endopeptidase activity, not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alpha_chymotrypsin_activity.html#alpha-chymotrypsin-activity-xref-gap"
 },
 {
  "discussion_id": "alpha-fucosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alpha-fucosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alpha-fucosidase activity",
  "source_id": "traitmech:000152",
  "source_file": "alpha_fucosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004560 carries the alpha-L-fucosidase activity label but denotes the enzyme molecular function rather than the organism-level alpha-fucosidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alpha_fucosidase_activity.html#alpha-fucosidase-activity-xref-gap"
 },
 {
  "discussion_id": "alpha-galactosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alpha-galactosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alpha-galactosidase activity",
  "source_id": "traitmech:000149",
  "source_file": "alpha_galactosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004557 denotes the alpha-galactosidase/melibiase molecular function rather than the organism-level alpha-galactosidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alpha_galactosidase_activity.html#alpha-galactosidase-activity-xref-gap"
 },
 {
  "discussion_id": "alpha-glucosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alpha-glucosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alpha-glucosidase activity",
  "source_id": "traitmech:000145",
  "source_file": "alpha_glucosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0090599 carries the same alpha-glucosidase activity label but denotes the enzyme molecular function rather than the organism-level alpha-glucosidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alpha_glucosidase_activity.html#alpha-glucosidase-activity-xref-gap"
 },
 {
  "discussion_id": "alpha-mannosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for alpha-mannosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "alpha-mannosidase activity",
  "source_id": "traitmech:000150",
  "source_file": "alpha_mannosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004559 carries the same alpha-mannosidase activity label but denotes the enzyme molecular function rather than the organism-level alpha-mannosidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/alpha_mannosidase_activity.html#alpha-mannosidase-activity-xref-gap"
 },
 {
  "discussion_id": "amylase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for amylase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "amylase activity",
  "source_id": "traitmech:000162",
  "source_file": "amylase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016160 carries the same amylase activity label but denotes the enzyme molecular function rather than the organism-level amylolytic enzyme production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/amylase_activity.html#amylase-activity-xref-gap"
 },
 {
  "discussion_id": "arginine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for arginine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "arginine arylamidase activity",
  "source_id": "traitmech:000167",
  "source_file": "arginine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 denotes broad aminopeptidase molecular function, and EC 3.4.11.6 denotes the aminopeptidase B/arginyl aminopeptidase molecular function rather than the organism-level arginine arylamidase assay phenotype. Both remain causal-node grounding leads rather than equivalent TraitRecord xrefs.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/arginine_arylamidase_activity.html#arginine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "arginine-dihydrolase-activity-xref-gap",
  "prompt": "Resolve exact external ontology mappings for arginine dihydrolase activity before adding TraitRecord xrefs.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "arginine dihydrolase activity",
  "source_id": "traitmech:000164",
  "source_file": "arginine_dihydrolase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016990 arginine deiminase activity and EC 3.5.3.6 denote the first-step molecular function in the arginine deiminase pathway rather than the full organism-level pathway-activity phenotype, so GO:0016990 is a close mechanism grounding for the source node and not an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/arginine_dihydrolase_activity.html#arginine-dihydrolase-activity-xref-gap"
 },
 {
  "discussion_id": "beta-galactosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for beta-galactosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "beta-galactosidase activity",
  "source_id": "traitmech:000148",
  "source_file": "beta_galactosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004565 carries the same beta-galactosidase activity label but denotes the enzyme molecular function rather than the organism-level beta-galactosidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/beta_galactosidase_activity.html#beta-galactosidase-activity-xref-gap"
 },
 {
  "discussion_id": "beta-glucosidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for beta-glucosidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "beta-glucosidase activity",
  "source_id": "traitmech:000146",
  "source_file": "beta_glucosidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0008422 denotes the beta-D-glucosidase molecular function rather than the organism-level beta-glucosidase production phenotype, so it belongs as a causal-node grounding when a mechanistic graph needs the catalytic activity but not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/beta_glucosidase_activity.html#beta-glucosidase-activity-xref-gap"
 },
 {
  "discussion_id": "beta-glucuronidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for beta-glucuronidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "beta-glucuronidase activity",
  "source_id": "traitmech:000151",
  "source_file": "beta_glucuronidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004566 carries the same beta-glucuronidase activity label but denotes the enzyme molecular function rather than the organism-level beta-glucuronidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/beta_glucuronidase_activity.html#beta-glucuronidase-activity-xref-gap"
 },
 {
  "discussion_id": "beta-n-acetylhexosaminidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for beta-N-acetylhexosaminidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "beta-N-acetylhexosaminidase activity",
  "source_id": "traitmech:000157",
  "source_file": "beta_n_acetylhexosaminidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004563 denotes beta-N-acetylhexosaminidase molecular function rather than the organism-level beta-N-acetylhexosaminidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html#beta-n-acetylhexosaminidase-activity-xref-gap"
 },
 {
  "discussion_id": "carboxylesterase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for carboxylesterase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "carboxylesterase activity",
  "source_id": "traitmech:000156",
  "source_file": "carboxylesterase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0106435 denotes carboxylesterase molecular function rather than the organism-level carboxylesterase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/carboxylesterase_activity.html#carboxylesterase-activity-xref-gap"
 },
 {
  "discussion_id": "caseinase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for caseinase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "caseinase activity",
  "source_id": "traitmech:000137",
  "source_file": "caseinase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0008233 is a generic peptidase-activity class and is too broad for caseinase activity as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/caseinase_activity.html#caseinase-activity-xref-gap"
 },
 {
  "discussion_id": "cellular-buoyancy-xref-gap",
  "prompt": "Resolve exact external ontology xrefs for gas-vesicle-mediated cellular buoyancy.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "cellular buoyancy",
  "source_id": "traitmech:000528",
  "source_file": "cellular_buoyancy.yaml",
  "attaches_to": [],
  "rationale": "No exact active local METPO class was accepted for the organism-level cellular-buoyancy physiology trait. The only buoyancy hit in the local METPO snapshot is obsolete buoyancy structure, and GO:0031411 denotes the gas vesicle organelle rather than the gas-vesicle-conferred physiological disposition.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/cellular_buoyancy.html#cellular-buoyancy-xref-gap"
 },
 {
  "discussion_id": "cold-shock-response-xref-gap",
  "prompt": "Resolve exact ontology xrefs for organism-level microbial cold shock response before adding TraitRecord xrefs.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "cold shock response",
  "source_id": "traitmech:000206",
  "source_file": "cold_shock_response.yaml",
  "attaches_to": [],
  "rationale": "GO:0009409 response to cold can ground broad biological-process response nodes but is broader than the rapid temperature-downshift cold-shock response curated here. Cold-shock-domain signatures and CspA-family terms describe narrower molecular machinery rather than the whole organism-level stress-response trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/cold_shock_response.html#cold-shock-response-xref-gap"
 },
 {
  "discussion_id": "cystine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for cystine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "cystine arylamidase activity",
  "source_id": "traitmech:000147",
  "source_file": "cystine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers aminopeptidase activity at molecular-function scope and no live GO class provides an exact residue-specific cystine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/cystine_arylamidase_activity.html#cystine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "dnase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for DNase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "DNase activity",
  "source_id": "traitmech:000138",
  "source_file": "dnase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004536 denotes the DNA nuclease molecular function rather than the organism-level DNase production phenotype, so it is too scope-shifted for an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/dnase_activity.html#dnase-activity-xref-gap"
 },
 {
  "discussion_id": "gamma-glutamyltransferase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for gamma-glutamyltransferase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "gamma-glutamyltransferase activity",
  "source_id": "traitmech:000160",
  "source_file": "gamma_glutamyltransferase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0003840 gamma-glutamyltransferase activity is obsolete, and its replacement GO:0036374 glutathione hydrolase activity denotes a glutathione-hydrolysis molecular function rather than the organism-level gamma-glutamyltransferase/glutathione-hydrolase phenotype. GO:0036374 is appropriate as a causal-node grounding when a graph needs that hydrolysis half-reaction, not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/gamma_glutamyltransferase_activity.html#gamma-glutamyltransferase-activity-xref-gap"
 },
 {
  "discussion_id": "gelatinase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for gelatinase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "gelatinase activity",
  "source_id": "traitmech:000136",
  "source_file": "gelatinase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0008233 is the generic peptidase-activity class and MICRO:0000649 denotes a gelatinase assay, so both are too broad or assay-level for equivalent TraitRecord xrefs.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/gelatinase_activity.html#gelatinase-activity-xref-gap"
 },
 {
  "discussion_id": "glutamyl-glutamic-acid-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for glutamyl glutamic acid arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "glutamyl glutamic acid arylamidase activity",
  "source_id": "traitmech:000173",
  "source_file": "glutamyl_glutamic_acid_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016805 covers broad dipeptidase activity at molecular-function scope, and no live GO class provides an exact glutamyl-glutamic-acid-specific arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html#glutamyl-glutamic-acid-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "glycine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for glycine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "glycine arylamidase activity",
  "source_id": "traitmech:000170",
  "source_file": "glycine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers broad aminopeptidase activity at molecular-function scope, and no live GO class provides an exact residue-specific glycine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/glycine_arylamidase_activity.html#glycine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "heat-shock-response-xref-gap",
  "prompt": "Resolve exact ontology xrefs for organism-level microbial heat shock response before adding TraitRecord xrefs.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "heat shock response",
  "source_id": "traitmech:000205",
  "source_file": "heat_shock_response.yaml",
  "attaches_to": [],
  "rationale": "GO:0009408 response to heat can ground biological-process nodes but is broader than this organism-level stress response trait. Candidate heat-shock-protein, chaperone, and ATP-dependent-protease terms describe narrower molecular machinery rather than the whole response phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/heat_shock_response.html#heat-shock-response-xref-gap"
 },
 {
  "discussion_id": "histidine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for histidine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "histidine arylamidase activity",
  "source_id": "traitmech:000171",
  "source_file": "histidine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers broad aminopeptidase activity at molecular-function scope, and no live GO class provides an exact residue-specific histidine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/histidine_arylamidase_activity.html#histidine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "homeoviscous-adaptation-xref-gap",
  "prompt": "Resolve an exact external ontology class for organism-level homeoviscous adaptation before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "homeoviscous adaptation",
  "source_id": "traitmech:000208",
  "source_file": "homeoviscous_adaptation.yaml",
  "attaches_to": [],
  "rationale": "No exact GO, PATO, or METPO class is present in the pinned local snapshot for homeoviscous adaptation. Related lipid metabolism, fatty-acid desaturation, membrane-fluidity, and cold-response terms are narrower, broader, or shifted from the whole-organism membrane-acclimation trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/homeoviscous_adaptation.html#homeoviscous-adaptation-xref-gap"
 },
 {
  "discussion_id": "lecithinase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for lecithinase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "lecithinase activity",
  "source_id": "traitmech:000140",
  "source_file": "lecithinase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004629 denotes C-type glycerophospholipase molecular function rather than the organism-level lecithinase production phenotype, so it is too scope-shifted for an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/lecithinase_activity.html#lecithinase-activity-xref-gap"
 },
 {
  "discussion_id": "leucine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for leucine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "leucine arylamidase activity",
  "source_id": "traitmech:000143",
  "source_file": "leucine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers aminopeptidase activity at molecular-function scope and the obsolete GO leucyl aminopeptidase term no longer provides a live exact class for leucine arylamidase production as an organism-level phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/leucine_arylamidase_activity.html#leucine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "leucyl-glycine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for leucyl glycine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "leucyl glycine arylamidase activity",
  "source_id": "traitmech:000178",
  "source_file": "leucyl_glycine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016805 covers broad dipeptidase activity at molecular-function scope, and no live GO class provides an exact leucyl-glycine-specific arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/leucyl_glycine_arylamidase_activity.html#leucyl-glycine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "lipase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for lipase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "lipase activity",
  "source_id": "traitmech:000139",
  "source_file": "lipase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016298 denotes the lipase molecular function rather than the organism-level lipase production phenotype, so it is too scope-shifted for an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/lipase_activity.html#lipase-activity-xref-gap"
 },
 {
  "discussion_id": "lysine-decarboxylase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for lysine decarboxylase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "lysine decarboxylase activity",
  "source_id": "traitmech:000153",
  "source_file": "lysine_decarboxylase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0008923 carries the same lysine decarboxylase activity label but denotes the enzyme molecular function rather than the organism-level lysine decarboxylase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/lysine_decarboxylase_activity.html#lysine-decarboxylase-activity-xref-gap"
 },
 {
  "discussion_id": "nad-dependent-alcohol-dehydrogenase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for NAD-dependent alcohol dehydrogenase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "NAD-dependent alcohol dehydrogenase activity",
  "source_id": "traitmech:000165",
  "source_file": "nad_dependent_alcohol_dehydrogenase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004022 and EC 1.1.1.1 denote the NAD-dependent molecular function rather than the organism-level NAD-dependent alcohol dehydrogenase production phenotype; the GO term remains an appropriate causal-node grounding lead but not an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html#nad-dependent-alcohol-dehydrogenase-activity-xref-gap"
 },
 {
  "discussion_id": "naphthol-as-bi-phosphohydrolase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for naphthol-AS-BI-phosphohydrolase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "naphthol-AS-BI-phosphohydrolase activity",
  "source_id": "traitmech:000174",
  "source_file": "naphthol_as_bi_phosphohydrolase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016791 covers broad phosphatase activity at molecular-function scope, and no live GO class provides an exact naphthol-AS-BI-phosphate-specific phosphohydrolase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html#naphthol-as-bi-phosphohydrolase-activity-xref-gap"
 },
 {
  "discussion_id": "ornithine-decarboxylase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for ornithine decarboxylase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "ornithine decarboxylase activity",
  "source_id": "traitmech:000154",
  "source_file": "ornithine_decarboxylase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004586 carries the same ornithine decarboxylase activity label but denotes the enzyme molecular function rather than the organism-level ornithine decarboxylase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/ornithine_decarboxylase_activity.html#ornithine-decarboxylase-activity-xref-gap"
 },
 {
  "discussion_id": "phenylalanine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for phenylalanine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "phenylalanine arylamidase activity",
  "source_id": "traitmech:000168",
  "source_file": "phenylalanine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers broad aminopeptidase activity at molecular-function scope, and no live GO class provides an exact residue-specific phenylalanine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/phenylalanine_arylamidase_activity.html#phenylalanine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "prolyl-aminopeptidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for prolyl aminopeptidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "prolyl aminopeptidase activity",
  "source_id": "traitmech:000166",
  "source_file": "prolyl_aminopeptidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 denotes broad aminopeptidase molecular function and EC 3.4.11.5 denotes a prolyl aminopeptidase molecular function; both are scope-shifted relative to the organism-level prolyl aminopeptidase production phenotype, so they remain causal-node grounding leads rather than equivalent TraitRecord xrefs.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/prolyl_aminopeptidase_activity.html#prolyl-aminopeptidase-activity-xref-gap"
 },
 {
  "discussion_id": "pyrazinamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for pyrazinamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "pyrazinamidase activity",
  "source_id": "traitmech:000163",
  "source_file": "pyrazinamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0008936 nicotinamidase activity denotes the catalytic molecular function rather than the organism-level pyrazinamidase/nicotinamidase phenotype, so it is appropriate as a causal-node grounding for the source label and not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/pyrazinamidase_activity.html#pyrazinamidase-activity-xref-gap"
 },
 {
  "discussion_id": "pyrrolidonyl-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for pyrrolidonyl arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "pyrrolidonyl arylamidase activity",
  "source_id": "traitmech:000155",
  "source_file": "pyrrolidonyl_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0016920 denotes pyroglutamyl-peptidase molecular function rather than the organism-level pyrrolidonyl arylamidase production phenotype, so it is appropriate as a causal-node grounding rather than an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html#pyrrolidonyl-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "serine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for serine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "serine arylamidase activity",
  "source_id": "traitmech:000172",
  "source_file": "serine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers broad aminopeptidase activity at molecular-function scope, and no live GO class provides an exact residue-specific serine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/serine_arylamidase_activity.html#serine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "siderophore-production-xref-gap",
  "prompt": "Resolve exact external ontology xrefs for the bacterial siderophore production phenotype.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "siderophore production",
  "source_id": "traitmech:000186",
  "source_file": "siderophore_production.yaml",
  "attaches_to": [],
  "rationale": "The pinned METPO snapshot contains only METPO:1000277 obsolete siderophore. GO:0019290 is limited to the siderophore biosynthetic process, GO:0015891 is a siderophore transport process, and CHEBI:26672 denotes the siderophore molecule rather than the organism-level biosynthesis-and-release trait.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/siderophore_production.html#siderophore-production-xref-gap"
 },
 {
  "discussion_id": "sos-response-xref-gap",
  "prompt": "Resolve exact ontology xrefs for organism-level microbial SOS response before adding TraitRecord xrefs.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "SOS response",
  "source_id": "traitmech:000207",
  "source_file": "sos_response.yaml",
  "attaches_to": [],
  "rationale": "GO:0009432 SOS response exactly grounds biological-process nodes in causal graphs but is shifted from this organism-level response trait. RecA, LexA, SulA, translesion-polymerase, prophage-induction, DNA-repair, and DNA-damage terms describe narrower machinery, downstream processes, or related triggers rather than the whole microbial SOS-response phenotype.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/sos_response.html#sos-response-xref-gap"
 },
 {
  "discussion_id": "trypsin-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for trypsin activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "trypsin activity",
  "source_id": "traitmech:000158",
  "source_file": "trypsin_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004295 trypsin activity is obsolete, and its replacement GO:0004252 denotes broader serine-type endopeptidase molecular function rather than the organism-level trypsin-like serine endopeptidase phenotype. GO:0004252 is appropriate as a causal-node grounding for generic serine endopeptidase activity, not as an equivalent TraitRecord xref.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/trypsin_activity.html#trypsin-activity-xref-gap"
 },
 {
  "discussion_id": "tyrosine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for tyrosine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "tyrosine arylamidase activity",
  "source_id": "traitmech:000169",
  "source_file": "tyrosine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers broad aminopeptidase activity at molecular-function scope, and no live GO class provides an exact residue-specific tyrosine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/tyrosine_arylamidase_activity.html#tyrosine-arylamidase-activity-xref-gap"
 },
 {
  "discussion_id": "valine-arylamidase-activity-xref-gap",
  "prompt": "Resolve an exact external ontology class for valine arylamidase activity before adding a TraitRecord xref.",
  "kind": "CURATION_TODO",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "valine arylamidase activity",
  "source_id": "traitmech:000144",
  "source_file": "valine_arylamidase_activity.yaml",
  "attaches_to": [],
  "rationale": "GO:0004177 covers aminopeptidase activity at molecular-function scope and no live GO class provides an exact residue-specific valine arylamidase production phenotype at organism-level scope.",
  "num_experiments": 0,
  "num_evidence": 0,
  "evidence_refs": [],
  "posed_by": "codex",
  "page_url": "../../pages/traits/physiology/valine_arylamidase_activity.html#valine-arylamidase-activity-xref-gap"
 }
];
window.searchMetrics = {
 "total_discussions": 423,
 "total_knowledge_gaps": 335,
 "total_source_entries": 417,
 "kinds": [
  "CONTROVERSY",
  "CURATION_TODO",
  "KNOWLEDGE_GAP"
 ]
};
window.repoName = "TraitMech";
