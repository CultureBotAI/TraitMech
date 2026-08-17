#!/usr/bin/env python3
"""Turn ten scraped sentences into ten answerable, anchored knowledge gaps (#409).

WHAT WAS THERE. The `kg-microbe-kgscan` pass attached one discussion each to ten
ecology records. Every one had `kind: KNOWLEDGE_GAP`, `status: OPEN`, no
`attaches_to`, no `posed_date`, and no `proposed_experiments` -- and a `prompt`
of the form "Knowledge gap for <trait>: <sentence lifted from a paper>".

WHY THEY COULD NOT BE KEPT AS PROMPTS. Read together, the ten sentences are not
gaps about the ten traits. `commensalism` and `gut_associated` got the SAME
sentence, about plant-derived xenomiRs crossing kingdom barriers. `biosafety_level`
and `biosafety_level_3` got the same contentless review boilerplate ("it identifies
ongoing challenges and critical knowledge gaps for future research") -- a sentence
that says a gap exists without saying what it is. `animal_pathogen` got a sentence
about plastisphere prokaryotes; `free_living` got one about protozoan infections
of the gut. The scan found sentences that LOOK like gap statements (the hedging
vocabulary: "remain poorly understood", "unknown to date") in papers retrieved for
the trait, but nothing checked that the sentence was a gap ABOUT the trait.

So rewriting these into research questions, as #409 step 4 proposed, would have
laundered off-topic scraped text into curated-looking content. Instead each
question below was authored from the record's OWN causal graph -- the gap is a
real tension or untested assumption already encoded in the nodes -- and anchored
to the node it concerns. The scan's sentence and its retrieved PMIDs are preserved
verbatim in `notes` so its output is not lost, but they are NOT carried as
`evidence`, because they are evidence for the scraped sentence and not for the
question that replaced it.

The upstream precision problem is filed separately; the scan lives in the
`kg_microbe_kgscan` package, not in this repo, so it cannot be fixed here.

Every question is anchored to a node_id that exists in that record's graph --
`audit_discussion_anchors.py` now enforces that, so these cannot rot silently.

FOUR OF THESE WERE WRONG ON THE FIRST PASS, and the way they were wrong is worth
recording. They were written from the graphs' NODE LISTS without reading the
EDGES, so they described structure that was not there: a NO -> c-di-GMP ->
dispersal chain in biofilm_formation (no such edges; NO goes straight to
dispersal), an "unstated" causal direction in gut_associated (stated, on a
pre-existing edge), three convergent compatible-solute edges in free_living
(two -- trehalose goes to a different node), and a drift arm routed into genome
reduction in endosymbiosis (disconnected). Node names imply a graph; only the
edges are the graph. Each was rewritten against the edges that exist, and in
three cases the true structure gave the BETTER question -- a bare edge where a
mechanism belongs, a one-way edge that should be a loop, a node dangling with no
path to the trait.

The anchor audit cannot catch this class: it checks that a node exists, not that
the prose about it is true. That gap is filed as #415.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

import yaml  # noqa: E402

TRAITS = Path("data/traits")
TIMESTAMP = "2026-08-17T22:14:03Z"
POSED_DATE = "2026-08-17"
CURATOR = "claude"

# The scan's ORIGINAL output, frozen as literals recovered from `main`.
#
# These were first built at runtime from the record's live `prompt` and
# `evidence`, which was correct exactly once -- on a first run against
# un-curated data. The second run then quoted the AUTHORED question as the
# sentence the scan raised, and an already-popped `evidence` list as its empty
# source. A provenance note that is only true on the first run is not
# provenance; it is a claim that decays silently, and it is the one claim here
# nothing downstream can check. Frozen so a rerun is inert.
#
# The SNIPPETS are frozen too, not just the PMIDs. Each scan discussion carried
# four SupportingReference blocks, and only the FIRST holds the sentence that
# became the prompt -- the other three are unrelated passages from other
# retrieved papers (animal_pathogen's second is about regulatory requirements in
# South America). Freezing the bare PMID list lost thirty snippets across the
# ten records while the notes still claimed nothing was lost, so they are kept
# here in full, each beside the reference it came from.
SCAN_OUTPUT: dict[str, tuple[str, list[tuple[str, str]]]] = {
    "kgscan-30bcdf4a32b0": (
        "Knowledge gap for animal pathogen: Prokaryotes in such plastispheres are unknown to date.",
        [
            ("PMID:40891913", "Prokaryotes in such plastispheres are unknown to date."),
            (
                "PMID:42279816",
                "However, in South America, their use is still limited because of complicated regulations and inconsistent evidence requirements.",
            ),
            (
                "PMID:41639266",
                "However, the interacting effects of climate factors and seasonal variations in nutritional components on PMCs remain poorly understood.",
            ),
            (
                "PMID:42197358",
                "While plant growth-promoting bacteria (PGPB) are known to alleviate heavy metal toxicity, their role under MP-HM co-contamination and the differential responses of rhizosphere microbial communities remain unclear.",
            ),
        ],
    ),
    "kgscan-aa46cc9b34ab": (
        "Knowledge gap for biofilm formation: How immune homeostasis is maintained in this constantly challenged environment remains however a central and largely unanswered question.",
        [
            (
                "PMID:42039744",
                "How immune homeostasis is maintained in this constantly challenged environment remains however a central and largely unanswered question.",
            ),
            (
                "PMID:41245847",
                "We present a research agenda identifying key research gaps and organizing them into priority areas to guide future investigations in this high-risk population.",
            ),
            (
                "PMID:41661098",
                "Finally, we identify major knowledge gaps and research priorities necessary to advance a more integrated understanding of maternal microbial influences on reproductive and neonatal health.",
            ),
            (
                "PMID:42125129",
                "However, contradictions persist regarding pH's effect on microbial diversity, with unresolved questions about how specific environmental conditions regulate microbial taxa.",
            ),
        ],
    ),
    "kgscan-93e87bc8aba3": (
        "Knowledge gap for biosafety level: Additionally, it identifies ongoing challenges and critical knowledge gaps for future research.",
        [
            (
                "PMID:41494000",
                "Additionally, it identifies ongoing challenges and critical knowledge gaps for future research.",
            ),
            (
                "PMID:41556562",
                "This review outlines the possibilities, as well as the limitations of their use in food production.",
            ),
            (
                "PMID:41647993",
                "Given the knowledge gap on the characteristics and significance of microbiome in early-onset pancreatic ductal adenocarcinoma (eoPDAC, age 50 years).",
            ),
            (
                "PMID:41683313",
                "Background : Untargeted microbiome modulation has achieved conflicting results in post-infectious irritable bowel syndrome (PI-IBS).",
            ),
        ],
    ),
    "kgscan-066a51aacfb6": (
        "Knowledge gap for biosafety level 2: Background : Untargeted microbiome modulation has achieved conflicting results in post-infectious irritable bowel syndrome (PI-IBS).",
        [
            (
                "PMID:41683313",
                "Background : Untargeted microbiome modulation has achieved conflicting results in post-infectious irritable bowel syndrome (PI-IBS).",
            ),
            (
                "PMID:41413233",
                "Recently, the gut microbiota (GM) has gained attention for its potential involvement in blood pressure regulation; however, polyamine metabolism involvement remains poorly understood.",
            ),
            (
                "PMID:41640410",
                "However, their clinical translation is hampered by challenges within the harsh gastrointestinal milieu, including low viability, poor colonization, and insufficient target specificity.",
            ),
            (
                "PMID:41490313",
                "However, how these core strains interact with each other and with other gut microbes is largely unknown.",
            ),
        ],
    ),
    "kgscan-2ee31ba13f9c": (
        "Knowledge gap for biosafety level 3: Additionally, it identifies ongoing challenges and critical knowledge gaps for future research.",
        [
            (
                "PMID:41494000",
                "Additionally, it identifies ongoing challenges and critical knowledge gaps for future research.",
            ),
            (
                "PMID:40514544",
                "Although T cells are essential for immunity to TB, the mechanisms that provide protective immunity are poorly understood.",
            ),
            (
                "PMID:41552424",
                "In the field of microbiological diagnosis, HTS provides a complementary or alternative approach to traditional diagnostic tests, particularly in cases with non-specific symptoms or when the etiology is unknown.",
            ),
            (
                "PMID:41917383",
                "While its virulence genes critically regulate intracellular survival and replication, the molecular mechanisms underlying pathogenesis remain elusive.",
            ),
        ],
    ),
    "kgscan-e770cf01677c": (
        "Knowledge gap for biosafety level 4: Finally, this review examines the largely unknown microbiology and infection implications of celestial body habitation with an emphasis placed on Mars.",
        [
            (
                "PMID:37362850",
                "Finally, this review examines the largely unknown microbiology and infection implications of celestial body habitation with an emphasis placed on Mars.",
            ),
            (
                "PMID:41914886",
                "Both Old World arenaviruses LASV and LCMV exploit host tyrosine kinase signaling to establish infection, though the molecular mechanisms remain incompletely understood.",
            ),
            (
                "PMID:40044492",
                "However, the comparatively low scientific commitment of countries that are usually among the major players in global scientific publications and the declining scientific interest in NiV research combined with the prevailing knowledge gaps in NiV infectiology in conjunction with the risk of NiV spreading to other areas is extremely threatening.",
            ),
            (
                "PMID:39682751",
                "The COVID-19 pandemic has underscored the limitations of focusing solely on the pathogen-killing strategies of immunology and microbiology to address complex, multisystemic infectious diseases.",
            ),
        ],
    ),
    "kgscan-3606bdcc991b": (
        "Knowledge gap for commensalism: MicroRNAs (miRNAs) are small, noncoding RNAs involved in posttranscriptional gene regulation in both animal and plant. miRNAs derived from edible plants, referred to as xenomiRs, are proposed to cross-kingdom barriers and to modulate mammalian gene expression.",
        [
            (
                "PMID:40945860",
                "MicroRNAs (miRNAs) are small, noncoding RNAs involved in posttranscriptional gene regulation in both animal and plant. miRNAs derived from edible plants, referred to as xenomiRs, are proposed to cross-kingdom barriers and to modulate mammalian gene expression.",
            ),
            (
                "PMID:40574831",
                "Emerging evidence suggests the gut microbiota plays a role in immune regulation, yet its impact on ITP remains unclear.",
            ),
            (
                "PMID:42197356",
                "Examining the existing literature may identify knowledge gaps regarding precise mechanisms through which the development of GM influences the maturation of the immune system.",
            ),
            (
                "PMID:41808832",
                "Given its promising anti-inflammatory properties, further research is warranted.",
            ),
        ],
    ),
    "kgscan-a6758e26f5a6": (
        "Knowledge gap for endosymbiosis: Growth anomalies (GAs) are coral diseases characterised by tumour-like skeletal lesions reported globally, yet their causes remain poorly understood.",
        [
            (
                "PMID:42130304",
                "Growth anomalies (GAs) are coral diseases characterised by tumour-like skeletal lesions reported globally, yet their causes remain poorly understood.",
            ),
            (
                "PMID:41612704",
                "Disrupting this obligate symbiosis represents a promising pest control strategy, yet the molecular mechanisms maintaining host-symbiont homeostasis remain poorly understood.",
            ),
            (
                "PMID:40831140",
                "This review explores the origin and evolution of plastids, their protein-import machinery, compartmentalization, and interactions with other cellular compartments, and highlights key unanswered questions in these areas.",
            ),
            (
                "PMID:41764142",
                "Detritivorous E. murphyi larvae can increase soil nitrogen levels by up to five times compared with similar uncolonized substrates, although the mechanisms involved remain unknown.",
            ),
        ],
    ),
    "kgscan-d5aefedf82bb": (
        "Knowledge gap for free-living: Interactions between parasites and the gut microbiota play a key role in immune responses and susceptibility to zoonotic diseases; however, many aspects of how protozoan infections alter microbial diversity and how these changes influence parasite pathogenicity and host defense remain poorly understood.",
        [
            (
                "PMID:41989588",
                "Interactions between parasites and the gut microbiota play a key role in immune responses and susceptibility to zoonotic diseases; however, many aspects of how protozoan infections alter microbial diversity and how these changes influence parasite pathogenicity and host defense remain poorly understood.",
            ),
            (
                "PMID:42039802",
                "Engineered microbial assemblies tailored to specific host plants and environmental conditions have shown potential in stabilizing crop performance during drought, salinity, and nutrient limitations.",
            ),
            (
                "PMID:41943163",
                "OBJECTIVES: Oxo-polyethylene (oxo-PE) is marketed as a biodegradable plastic, yet its environmental degradation remains poorly understood, particularly in marine contexts.",
            ),
            (
                "PMID:42125129",
                "However, contradictions persist regarding pH's effect on microbial diversity, with unresolved questions about how specific environmental conditions regulate microbial taxa.",
            ),
        ],
    ),
    "kgscan-4fc1a06fa1e3": (
        "Knowledge gap for gut-associated: MicroRNAs (miRNAs) are small, noncoding RNAs involved in posttranscriptional gene regulation in both animal and plant. miRNAs derived from edible plants, referred to as xenomiRs, are proposed to cross-kingdom barriers and to modulate mammalian gene expression.",
        [
            (
                "PMID:40945860",
                "MicroRNAs (miRNAs) are small, noncoding RNAs involved in posttranscriptional gene regulation in both animal and plant. miRNAs derived from edible plants, referred to as xenomiRs, are proposed to cross-kingdom barriers and to modulate mammalian gene expression.",
            ),
            (
                "PMID:42278360",
                "By integrating microbiological, immunological, and clinical perspectives, this review highlights key knowledge gaps and outlines future research directions aimed at harnessing the gut microbiome as a novel therapeutic avenue in HIV management and eradication.",
            ),
            (
                "PMID:41808832",
                "Given its promising anti-inflammatory properties, further research is warranted.",
            ),
            (
                "PMID:42197356",
                "Examining the existing literature may identify knowledge gaps regarding precise mechanisms through which the development of GM influences the maturation of the immune system.",
            ),
        ],
    ),
}
# Keyed by discussion_id so the plan binds to the discussion the scan wrote and
# not to a file position -- a second scan pass appending another discussion must
# not silently shift these onto the wrong object.
PLAN: dict[str, dict] = {
    "kgscan-30bcdf4a32b0": {
        "file": "ecology/animal_pathogen.yaml",
        "prompt": (
            "This record routes two independent paths to immune evasion -- "
            "complement-regulator binding by surface proteins, and effector "
            "delivery through the T3SS. In a given host, is either route "
            "sufficient on its own, or does established infection require both?"
        ),
        "attaches_to": ["causal_graphs#immune_evasion"],
        "rationale": (
            "The graph draws both arrows into the same node without saying "
            "whether they are alternatives or partners. If either is sufficient, "
            "single-target antivirulence strategies are viable; if evasion needs "
            "both, only combination approaches will work, and the two edges "
            "should carry that dependency rather than reading as parallel routes."
        ),
        "experiment": {
            "experiment_id": "x-animal-pathogen-evasion-epistasis",
            "name": "Isogenic single- and double-mutant serum and phagocyte survival",
            "approach": "isogenic mutant panel with ex vivo killing assays",
            "model_systems": [
                "isolate of a T3SS-bearing animal pathogen",
                "naive host serum",
                "primary phagocytes from the same host species",
            ],
            "perturbations": [
                "deletion of the complement-regulator binding protein",
                "deletion of the T3SS structural apparatus",
                "the double deletion",
            ],
            "readouts": [
                "survival in non-heat-inactivated serum",
                "intracellular survival after phagocyte challenge",
                "surface-bound complement regulator by flow cytometry",
            ],
            "decision_criterion": (
                "whether either single mutant is attenuated to the same degree as the double mutant"
            ),
            "would_support": (
                "single mutants retain near-wild-type survival and only the "
                "double is attenuated -- the routes are independently sufficient"
            ),
            "would_refute": (
                "either single mutant is attenuated as severely as the double -- "
                "the routes are not redundant and evasion requires both"
            ),
        },
        "scan_topic": "prokaryotes of marine plastispheres",
    },
    "kgscan-aa46cc9b34ab": {
        "file": "ecology/biofilm_formation.yaml",
        "prompt": (
            "This record draws nitric oxide straight to biofilm dispersal with "
            "nothing in between, while c-di-GMP sits in the same graph wired "
            "only to the sessile state. Is the NO effect on dispersal mediated "
            "by lowering c-di-GMP, and should that intermediate be on the edge?"
        ),
        "attaches_to": [
            "causal_graphs#biofilm_dispersal",
            "causal_graphs#nitric_oxide",
            "causal_graphs#c_di_gmp",
        ],
        "rationale": (
            "A bare `induces` edge from a diffusible signal to a "
            "community-scale outcome is a placeholder where a mechanism should "
            "be. The graph already carries c_di_gmp, but only as a promoter of "
            "sessile_state, so it cannot currently express the route most often "
            "proposed for this effect. The distinction is not academic: if "
            "dispersal runs through the c-di-GMP pool, then strains holding "
            "that pool high are intrinsically refractory to the NO-releasing "
            "antibiofilm agents now in development -- a resistance mechanism "
            "this graph has no way to represent while the edge stays bare."
        ),
        "experiment": {
            "experiment_id": "x-biofilm-no-dispersal-bypass",
            "name": "NO challenge against a c-di-GMP-clamped biofilm",
            "approach": "flow-cell biofilm with an inducible c-di-GMP clamp",
            "model_systems": [
                "flow-cell biofilm of a c-di-GMP-signalling model organism",
                "isogenic strain carrying an inducible diguanylate cyclase",
            ],
            "perturbations": [
                "NO donor at an established dispersal-competent dose",
                "induction of the constitutive diguanylate cyclase",
                "phosphodiesterase deletion background",
            ],
            "readouts": [
                "biomass loss by confocal image analysis",
                "cell counts released into the effluent",
                "intracellular c-di-GMP by LC-MS/MS",
                "a c-di-GMP-responsive transcriptional reporter",
            ],
            "decision_criterion": (
                "whether NO still releases cells when the measured c-di-GMP pool is held high"
            ),
            "would_support": (
                "the clamped biofilm does not disperse -- c-di-GMP is the "
                "necessary intermediate and the bare edge should be replaced "
                "by the two-step route"
            ),
            "would_refute": (
                "the clamped biofilm disperses anyway -- the effect is "
                "c-di-GMP-independent and the direct edge as drawn is right"
            ),
        },
        "scan_topic": "immune homeostasis at the gut mucosa",
    },
    "kgscan-93e87bc8aba3": {
        "file": "ecology/biosafety_level.yaml",
        "kind": "CURATION_TODO",
        "prompt": (
            "This record's graph enumerates bsl1 through bsl5, but BSL-5 is not "
            "an assigned containment level in any current national framework -- "
            "it appears in proposals for hypothetical agents beyond BSL-4. Is "
            "the bsl5 node a real classification this record should carry, or a "
            "seeded artefact to retract?"
        ),
        "attaches_to": ["causal_graphs#bsl5"],
        "rationale": (
            "A containment level that does not exist in regulation is not a "
            "value the trait can take, and anything downstream that enumerates "
            "levels from this graph -- a risk-assessment form, an ontology "
            "mapping, a facility-capability query -- would inherit a level with "
            "no requirements attached to it. Either the node is grounded in a "
            "published proposal and labelled as one, or it comes out."
        ),
        "experiment": {
            "experiment_id": "x-bsl5-provenance-check",
            "name": "Regulatory provenance check for the BSL-5 designation",
            "approach": "documentary review of containment frameworks",
            "model_systems": [
                "WHO Laboratory Biosafety Manual",
                "US CDC/NIH Biosafety in Microbiological and Biomedical Laboratories",
                "national biosafety regulations with assigned containment levels",
            ],
            "readouts": [
                "presence of an assigned BSL-5 level in each framework",
                "any peer-reviewed proposal defining BSL-5 requirements",
            ],
            "decision_criterion": ("whether any binding framework assigns agents to a fifth level"),
            "would_support": (
                "a framework or a citable proposal defines it -- keep the node "
                "and ground it to that source"
            ),
            "would_refute": (
                "no framework or proposal defines it -- retract the node under "
                "the grounding-retraction rule"
            ),
        },
        "scan_topic": "a review's boilerplate statement that gaps exist",
    },
    "kgscan-066a51aacfb6": {
        "file": "ecology/biosafety_level_2.yaml",
        "prompt": (
            "BSL-2 requires a biosafety cabinet specifically for procedures with "
            "aerosol or splash potential, while other work may go on the open "
            "bench. Which procedures actually generate an infectious dose at the "
            "breathing zone, and does the current procedure list match them?"
        ),
        "attaches_to": [
            "causal_graphs#aerosol_splash_procedure",
            "causal_graphs#biosafety_cabinet",
        ],
        "rationale": (
            "The bench/cabinet boundary is the single control that most BSL-2 "
            "work turns on, and it is drawn from procedure lists that long "
            "predate quantitative aerosol measurement. A procedure that is on "
            "the open bench but does generate respirable particles is an "
            "unrecognised exposure; one needlessly in the cabinet costs "
            "throughput. Either way the edge into biosafety_cabinet is asserting "
            "something measurable that has not been measured."
        ),
        "experiment": {
            "experiment_id": "x-bsl2-aerosol-tracer",
            "name": "Surrogate-tracer aerosol survey of routine BSL-2 procedures",
            "approach": "non-infectious tracer release with breathing-zone sampling",
            "model_systems": [
                "bacteriophage or fluorescent-bead surrogate at defined titre",
                "a working BSL-2 laboratory",
                "breathing-zone and area impingers",
            ],
            "perturbations": [
                "each routine procedure performed on the open bench",
                "the same procedure performed inside a class II cabinet",
                "deliberate worst-case variants such as a dropped tube",
            ],
            "readouts": [
                "tracer recovered at the breathing zone per procedure",
                "particle size distribution in the respirable fraction",
                "surface deposition beyond the immediate work area",
            ],
            "decision_criterion": (
                "whether any open-bench procedure exceeds the breathing-zone "
                "tracer recovery of cabinet-required procedures"
            ),
            "would_support": (
                "recovery tracks the existing list -- the procedure boundary is "
                "drawn where the aerosol actually is"
            ),
            "would_refute": (
                "an off-list procedure matches or exceeds a listed one -- the "
                "control boundary is misplaced"
            ),
        },
        "scan_topic": "microbiome modulation in post-infectious IBS",
    },
    "kgscan-2ee31ba13f9c": {
        "file": "ecology/biosafety_level_3.yaml",
        "prompt": (
            "BSL-3 boundary integrity is verified by pressure-decay testing of "
            "the room envelope. Does passing a pressure-decay test predict "
            "containment of an airborne agent under real operating conditions, "
            "with doors cycling and equipment running?"
        ),
        "attaches_to": [
            "causal_graphs#boundary_integrity_testing",
            "causal_graphs#pressure_decay_testing",
        ],
        "rationale": (
            "The graph routes verification the other way round from the claim "
            "it supports: bsl3_trait is `verified by` boundary_integrity_testing, "
            "which `utilizes` pressure_decay_testing. So the decay test stands in "
            "for containment without any node asserting that containment holds. "
            "The test is also performed on a sealed, static room, and the room "
            "only matters when it is occupied and in use. If the two diverge, "
            "facilities are certified against a condition they never operate in."
        ),
        "experiment": {
            "experiment_id": "x-bsl3-decay-vs-tracer",
            "name": "Tracer-gas containment under operation versus decay-test result",
            "approach": "paired tracer-gas release and envelope pressure-decay testing",
            "model_systems": [
                "commissioned BSL-3 suites spanning a range of decay results",
                "SF6 or equivalent inert tracer with anteroom sampling",
            ],
            "perturbations": [
                "static sealed room, as in the certification test",
                "normal operation with personnel entry and exit",
                "a single HEPA-filtered exhaust fan taken offline",
            ],
            "readouts": [
                "tracer concentration outside the containment boundary",
                "directional airflow at the door plane",
                "measured envelope leakage rate",
            ],
            "decision_criterion": (
                "whether tracer escape under operation correlates with the "
                "static decay-test result across suites"
            ),
            "would_support": (
                "suites with better decay results leak less tracer in operation "
                "-- the test predicts what it is used to certify"
            ),
            "would_refute": (
                "escape under operation is uncorrelated with decay result -- "
                "passing certifies the sealed room and not the working one"
            ),
        },
        "scan_topic": "a review's boilerplate statement that gaps exist",
    },
    "kgscan-e770cf01677c": {
        "file": "ecology/biosafety_level_4.yaml",
        "prompt": (
            "Every BSL-4 control this record requires assumes terrestrial "
            "gravity and somewhere to put contaminated air, water and waste -- "
            "suit overpressure, airlocks, chemical showers, specialized waste "
            "disposal. Which still contain an agent in a closed-loop habitat "
            "that recycles all three?"
        ),
        "attaches_to": [
            "causal_graphs#positive_pressure_suit",
            "causal_graphs#airlock",
            "causal_graphs#decontamination_shower",
            "causal_graphs#specialized_waste_disposal",
        ],
        "rationale": (
            "Sample-return and crewed-habitat missions need containment for "
            "agents with no countermeasure, which is exactly what BSL-4 is for. "
            "But every control edge runs outward from bsl4_trait to a piece of "
            "equipment -- `requires` an airlock, a decontamination shower, "
            "specialized waste disposal; `necessitates use of` a positive "
            "pressure suit -- so the controls are named as hardware rather "
            "than as the physics they rely on, and it is the physics that does "
            "or does not transfer. Sedimentation-dependent controls behave differently in "
            "microgravity, and a shower and a waste stream that both feed a "
            "recycling loop are not disposal. As written the record cannot "
            "distinguish a control that survives the move from one that does "
            "not, because it never says what any of them do."
        ),
        "experiment": {
            "experiment_id": "x-bsl4-closed-loop-transfer",
            "name": "Control-by-control containment audit in a closed-loop analogue",
            "approach": "analogue-habitat tracer study with parabolic-flight aerosol runs",
            "model_systems": [
                "sealed closed-loop habitat analogue with recycled atmosphere",
                "parabolic flight or drop-tower reduced-gravity segments",
                "non-infectious spore and fluorescent-particle tracers",
            ],
            "perturbations": [
                "suit breach at defined overpressure",
                "airlock cycling with no atmospheric exhaust available",
                "chemical shower under water-recovery constraints",
            ],
            "readouts": [
                "tracer crossing the containment boundary per control",
                "settling versus suspension time in reduced gravity",
                "tracer persisting in the atmospheric recycling loop",
            ],
            "decision_criterion": (
                "which controls hold tracer escape at terrestrial levels once "
                "gravity and exhaust assumptions are removed"
            ),
            "would_support": (
                "overpressure-based controls transfer intact -- they depend on "
                "pressure differential, not on settling or exhaust"
            ),
            "would_refute": (
                "escape rises for controls that passed on the ground -- the "
                "BSL-4 set does not transfer and needs habitat-specific "
                "equivalents"
            ),
        },
        "scan_topic": "microbiology and infection during celestial body habitation",
    },
    "kgscan-3606bdcc991b": {
        "file": "ecology/commensalism.yaml",
        "prompt": (
            "Commensalism is defined in this record by a neutral effect on host "
            "fitness. Has neutrality ever been measured for these associations, "
            "or is it inferred from the absence of visible disease -- and does "
            "it hold when the host is stressed, starved, or co-infected?"
        ),
        "attaches_to": ["causal_graphs#neutral_host_fitness"],
        "rationale": (
            "Neutral_host_fitness is the node that makes this trait different "
            "from mutualism and parasitism, and it is the one node stated as a "
            "definition rather than an observation. If neutrality is only ever "
            "the null result of an underpowered comparison in an unstressed "
            "host, then commensalism is a measurement category rather than a "
            "biological one, and records assigned to it are provisional in a way "
            "the corpus does not currently mark."
        ),
        "experiment": {
            "experiment_id": "x-commensal-fitness-neutrality",
            "name": "Gnotobiotic mono-association host fitness across stressors",
            "approach": "gnotobiotic mono-association with quantitative fitness readouts",
            "model_systems": [
                "germ-free animal model",
                "mono-association with a designated commensal isolate",
                "germ-free controls held under identical conditions",
            ],
            "perturbations": [
                "protein or caloric restriction",
                "thermal or osmotic stress",
                "co-infection with a defined enteric pathogen",
            ],
            "readouts": [
                "lifetime reproductive output",
                "growth rate and body condition",
                "survival under each stressor",
                "the effect size the design could have detected",
            ],
            "decision_criterion": (
                "whether an adequately powered comparison detects a fitness "
                "difference under any stressor"
            ),
            "would_support": (
                "no difference under any condition at a stated detectable "
                "effect size -- neutrality is measured, not assumed"
            ),
            "would_refute": (
                "a fitness effect appears under stress -- neutrality was a "
                "condition-dependent artefact and the assignment should change"
            ),
        },
        "scan_topic": "plant-derived xenomiRs crossing kingdom barriers",
    },
    "kgscan-a6758e26f5a6": {
        "file": "ecology/endosymbiosis.yaml",
        "kind": "CONTROVERSY",
        "prompt": (
            "Two edges reach genome reduction here: confined habitat through "
            "metabolic gene loss, and the trait itself, whose description "
            "bundles drift in as `with small Ne`. The nodes that would give "
            "drift a mechanism -- transmission bottleneck, limited "
            "recombination -- connect to neither. Should they feed the drift "
            "edge, and which mechanism dominates?"
        ),
        "attaches_to": [
            "causal_graphs#reductive_genome_evolution",
            "causal_graphs#transmission_bottleneck",
            "causal_graphs#limited_recombination",
            "causal_graphs#metabolic_gene_loss",
        ],
        "rationale": (
            "The record asserts both mechanisms but at different resolutions, "
            "which is what makes them impossible to weigh. Drift arrives "
            "bundled into a trait-level edge as a parenthetical -- `with small "
            "Ne` inside a description -- while selection is spelled out as a "
            "two-step path through metabolic_gene_loss. Neither "
            "transmission_bottleneck nor limited_recombination attaches to "
            "anything, so the drift claim has no mechanism under it, and "
            "host_symbiont_aa_complementarity -> nutritional_compensation is "
            "likewise its own disconnected pair, so compensation is not wired "
            "into reduction either. The two predict opposite loss spectra -- "
            "drift removes genes roughly regardless of function, compensation "
            "removes exactly the genes whose products the host supplies -- so "
            "until they are stated at the same resolution the graph cannot say "
            "what a newly sequenced symbiont will have lost, which is most of "
            "what a reduction model is for."
        ),
        "experiment": {
            "experiment_id": "x-endosymbiont-drift-vs-selection",
            "name": "Comparative loss spectra across symbionts of differing bottleneck severity",
            "approach": "comparative genomics across independent symbiotic origins",
            "model_systems": [
                "vertically transmitted symbionts with severe bottlenecks",
                "horizontally acquired symbionts with large inocula",
                "free-living relatives as the unreduced reference",
            ],
            "readouts": [
                "genome size against estimated effective population size",
                "dN/dS across retained genes",
                "whether lost functions are complemented by host pathways",
                "pseudogene load as a marker of ongoing reduction",
            ],
            "decision_criterion": (
                "whether genome size still tracks bottleneck severity once "
                "host complementation of the lost functions is controlled for"
            ),
            "would_support": (
                "reduction tracks bottleneck severity independently of "
                "complementation -- the bottleneck pair belongs under the "
                "trait-level drift edge, as its mechanism"
            ),
            "would_refute": (
                "loss is enriched for host-complemented functions with no "
                "residual bottleneck effect -- selection dominates, and the "
                "dangling pair is context rather than cause"
            ),
        },
        "scan_topic": "growth anomalies in corals",
    },
    "kgscan-d5aefedf82bb": {
        "file": "ecology/free_living.yaml",
        "prompt": (
            "Ectoine and glycine betaine both enable osmotic stress tolerance "
            "here, but trehalose is wired instead to environmental stress "
            "tolerance -- a node with no outgoing edge. Is that split a real "
            "distinction, or does trehalose belong on the osmotic route too?"
        ),
        "attaches_to": [
            "causal_graphs#osmotic_stress_tolerance",
            "causal_graphs#environmental_stress_tolerance",
            "causal_graphs#ectoine_biosynthesis",
            "causal_graphs#glycine_betaine_system",
            "causal_graphs#trehalose_biosynthesis",
        ],
        "rationale": (
            "Because environmental_stress_tolerance has no outgoing edge, "
            "nothing downstream depends on trehalose at all: this record "
            "currently predicts the trait's osmotolerance from two systems and "
            "leaves the third dangling. Either reading has a consequence. If "
            "trehalose does serve osmotic tolerance, a genome carrying only "
            "trehalose scores as non-osmotolerant when it is not, which is "
            "exactly the inference anything reading habitat range off gene "
            "content would make. If the split is real -- trehalose for "
            "desiccation and thermal stress rather than osmolarity -- then the "
            "dangling node needs its own edge onward to the trait. The second "
            "question, whether the two routes that do converge are redundant or "
            "condition-partitioned, rides along on the same experiment: their "
            "costs differ sharply, since de novo ectoine synthesis is "
            "carbon-expensive where betaine uptake is cheap given a precursor."
        ),
        "experiment": {
            "experiment_id": "x-compatible-solute-partitioning",
            "name": "Combinatorial solute-pathway knockouts across an environmental matrix",
            "approach": "combinatorial knockout panel with matrix growth phenotyping",
            "model_systems": [
                "a free-living halotolerant isolate carrying all three systems",
                "single, double, and triple pathway knockouts",
            ],
            "perturbations": [
                "an osmolarity gradient spanning the growth range",
                "low and high temperature at each osmolarity",
                "carbon-replete versus carbon-limited medium",
                "betaine precursor present or absent",
            ],
            "readouts": [
                "growth rate and final yield across the matrix",
                "intracellular solute pools by NMR or LC-MS",
                "the osmolarity limit for each genotype",
            ],
            "decision_criterion": (
                "whether the trehalose knockout loses growth at high osmolarity "
                "specifically, with temperature and water activity held constant"
            ),
            "would_support": (
                "trehalose loss costs nothing osmotically and only shows under "
                "desiccation or heat -- the split in the graph is real and "
                "environmental_stress_tolerance needs its own edge onward"
            ),
            "would_refute": (
                "the trehalose knockout is osmotically impaired -- it belongs "
                "on the osmotic route with the other two"
            ),
        },
        "scan_topic": "protozoan infection and gut microbial diversity",
    },
    "kgscan-4fc1a06fa1e3": {
        "file": "ecology/gut_associated.yaml",
        "prompt": (
            "This record commits to luminal oxygen limitation contributing to "
            "the primary fermenter community. Does the reverse arm hold too -- "
            "do the fermenters and the epithelium maintain the anoxia -- making "
            "this a feedback loop rather than the one-way edge drawn?"
        ),
        "attaches_to": [
            "causal_graphs#luminal_oxygen_limitation",
            "causal_graphs#primary_fermenter_community",
        ],
        "rationale": (
            "The existing edge is not wrong so much as half: it says the anoxic "
            "lumen permits the fermenters, and stops. If the return arm also "
            "holds, the two nodes are a self-reinforcing loop, and losing the "
            "fermenters raises luminal oxygen and admits facultative pathogens "
            "-- the collapse that follows antibiotic depletion. That is the "
            "clinically load-bearing half, and a graph of one-way edges can "
            "only carry it if someone draws it."
        ),
        "experiment": {
            "experiment_id": "x-gut-oxygen-causal-direction",
            "name": "Oxygen microprofiling during staged gnotobiotic colonisation",
            "approach": "staged gnotobiotic colonisation with in situ oxygen microsensing",
            "model_systems": [
                "germ-free animals colonised in defined stages",
                "a defined community with and without obligate anaerobe fermenters",
                "oxygen microelectrodes at the mucosal surface and mid-lumen",
            ],
            "perturbations": [
                "colonisation with facultative organisms alone",
                "subsequent addition of obligate anaerobe fermenters",
                "butyrate supplementation without the producing community",
                "antibiotic depletion of an established fermenter community",
            ],
            "readouts": [
                "luminal and mucosal oxygen partial pressure over time",
                "community composition by shotgun sequencing",
                "short-chain fatty acid concentration",
                "epithelial hypoxia by pimonidazole staining",
            ],
            "decision_criterion": (
                "whether luminal oxygen rises when an established fermenter "
                "community is depleted, with colonisation order held constant"
            ),
            "would_support": (
                "oxygen rises on depletion and falls again on re-colonisation "
                "-- the return arm is real and the pair is a loop"
            ),
            "would_refute": (
                "oxygen is unchanged by depletion -- the habitat sets the "
                "anoxia and the single existing edge is the whole story"
            ),
        },
        "scan_topic": "plant-derived xenomiRs crossing kingdom barriers",
    },
}


def scan_note(discussion_id: str, topic: str) -> str:
    """Preserve the scan's output verbatim, and say why it is not the prompt.

    Reads the frozen SCAN_OUTPUT table, never the record's current state, so
    running this script twice cannot make the note describe the curated question
    instead of the scraped one.

    Every snippet is reproduced, not just the one that became the prompt. The
    first reference is the sentence's actual source; the rest were retrieved
    alongside it and carry unrelated passages, so listing all four after
    "retrieved from" would imply a sentence drawn from four papers. Saying which
    one it came from, and showing what the others actually said, is the only
    version of this note that survives being checked.
    """
    prompt, refs = SCAN_OUTPUT[discussion_id]
    source, *others = refs
    note = [
        f"Scan provenance (#409). The kg-microbe-kgscan pass raised this "
        f"discussion with the prompt {prompt!r}, whose sentence came from "
        f"{source[0]}. That sentence is about {topic}, not about this trait: "
        f"the scan matched the hedging vocabulary of a gap statement without "
        f"checking that the gap was about the trait it was filed under. The "
        f"prompt above was authored instead from this record's own causal "
        f"graph, and none of these references are carried as its evidence, "
        f"because they support the scraped sentence rather than the question."
    ]
    if others:
        note.append(
            "The scan attached three further references whose snippets concern "
            "neither that sentence nor this trait; all four are reproduced here "
            "so nothing it produced is lost: "
            + "; ".join(f"{ref} {snippet!r}" for ref, snippet in refs)
            + "."
        )
    return " ".join(note)


def apply(path: Path, plan_by_id: dict[str, dict]) -> list[str]:
    doc = yaml.safe_load(path.read_text())
    touched = []
    for disc in doc.get("discussions") or []:
        plan = plan_by_id.get(disc.get("discussion_id"))
        if plan is None:
            continue
        disc["notes"] = scan_note(disc["discussion_id"], plan["scan_topic"])
        disc["prompt"] = plan["prompt"]
        disc["kind"] = plan.get("kind", "KNOWLEDGE_GAP")
        disc["status"] = "OPEN"
        disc["attaches_to"] = plan["attaches_to"]
        disc["rationale"] = plan["rationale"]
        disc["proposed_experiments"] = [plan["experiment"]]
        disc["posed_by"] = CURATOR
        disc["posed_date"] = POSED_DATE
        # The scan's PMIDs supported its sentence, not this question; they are
        # preserved in notes above rather than re-pointed at authored content.
        disc.pop("evidence", None)
        touched.append(disc["discussion_id"])
    if not touched:
        return []
    record_curation_event(
        doc,
        curator=CURATOR,
        action="CURATE_KNOWLEDGE_GAPS",
        changes=(
            "Replaced the scan's off-topic scraped sentence with a research "
            "question authored from this record's causal graph, anchored it via "
            "attaches_to, and sketched an experiment with a decision criterion. "
            "The scan's sentence and PMIDs are preserved in the discussion's "
            "notes."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    write_validated_trait(doc, path)
    return touched


def main() -> int:
    by_file: dict[str, dict[str, dict]] = {}
    for did, plan in PLAN.items():
        by_file.setdefault(plan["file"], {})[did] = plan
    total = 0
    for rel, plan_by_id in sorted(by_file.items()):
        touched = apply(TRAITS / rel, plan_by_id)
        missing = set(plan_by_id) - set(touched)
        if missing:
            print(f"NOT FOUND in {rel}: {', '.join(sorted(missing))}")
            return 1
        total += len(touched)
        print(f"{rel}: {', '.join(touched)}")
    print(f"\ncurated {total} discussions across {len(by_file)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
