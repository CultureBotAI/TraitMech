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
  "rationale": "A containment level that does not exist in regulation is not a value the trait can take, and anything downstream that enumerates levels from this graph -- a risk-assessment form, an ontology mapping, a facility-capability query -- would inherit a level with no requirements attached to it. Either the node is grounded in a published proposal and labelled as one, or it comes out.",
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
  "rationale": "The record asserts both mechanisms but at different resolutions, which is what makes them impossible to weigh. Drift arrives bundled into a trait-level edge as a parenthetical -- `with small Ne` inside a description -- while selection is spelled out as a two-step path through metabolic_gene_loss. Neither transmission_bottleneck nor limited_recombination attaches to anything, so the drift claim has no mechanism under it, and host_symbiont_aa_complementarity -> nutritional_compensation is likewise its own disconnected pair, so compensation is not wired into reduction either. The two predict opposite loss spectra -- drift removes genes roughly regardless of function, compensation removes exactly the genes whose products the host supplies -- so until they are stated at the same resolution the graph cannot say what a newly sequenced symbiont will have lost, which is most of what a reduction model is for.",
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
  "status": "OPEN",
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
  "status": "OPEN",
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
 }
];
window.searchMetrics = {
 "total_discussions": 10,
 "total_knowledge_gaps": 8,
 "total_source_entries": 10,
 "kinds": [
  "CONTROVERSY",
  "CURATION_TODO",
  "KNOWLEDGE_GAP"
 ]
};
window.repoName = "TraitMech";
