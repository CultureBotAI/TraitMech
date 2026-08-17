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
                "whether either single mutant is attenuated to the same degree "
                "as the double mutant"
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
            "Nitric oxide triggers biofilm dispersal in this record by way of "
            "falling c-di-GMP. Is lowered c-di-GMP the only route from NO to "
            "dispersal, or can NO disperse a biofilm whose c-di-GMP pool is "
            "held high?"
        ),
        "attaches_to": [
            "causal_graphs#biofilm_dispersal",
            "causal_graphs#c_di_gmp",
        ],
        "rationale": (
            "The record encodes NO -> c-di-GMP -> dispersal as a single chain, "
            "which makes c-di-GMP the necessary intermediate. NO-releasing "
            "dispersal agents are being developed as antibiofilm adjuncts; if "
            "the chain is the whole story, strains with constitutively high "
            "c-di-GMP are intrinsically refractory to them, and that is a "
            "resistance mechanism the graph currently cannot express."
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
                "whether NO still releases cells when measured c-di-GMP does "
                "not fall"
            ),
            "would_support": (
                "the clamped biofilm does not disperse -- c-di-GMP is the "
                "necessary intermediate and the single chain is correct"
            ),
            "would_refute": (
                "the clamped biofilm disperses anyway -- a c-di-GMP-independent "
                "route exists and the graph needs a second edge"
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
            "decision_criterion": (
                "whether any binding framework assigns agents to a fifth level"
            ),
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
            "The graph treats the decay test as evidence of containment, but the "
            "test is performed on a sealed, static room, and the room only "
            "matters when it is occupied and in use. If the two diverge, "
            "facilities are certified against a condition they never operate in, "
            "and the edge from pressure_decay_testing to containment is weaker "
            "than the record implies."
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
            "Every BSL-4 engineering control in this record assumes terrestrial "
            "gravity and an atmosphere that can be exhausted -- suit "
            "overpressure, directional airflow, airlocks, chemical showers. "
            "Which of them still contain an agent in a closed-loop habitat with "
            "no outside air to exhaust to?"
        ),
        "attaches_to": [
            "causal_graphs#positive_pressure_suit",
            "causal_graphs#airlock",
            "causal_graphs#decontamination_shower",
        ],
        "rationale": (
            "Sample-return and crewed-habitat missions need containment for "
            "agents with no countermeasure, which is exactly what BSL-4 is for, "
            "but the controls are specified as equipment rather than as the "
            "physics they rely on. Sedimentation-dependent controls behave "
            "differently in microgravity and a closed atmosphere has nowhere to "
            "exhaust; the record cannot currently distinguish a control that "
            "transfers from one that does not."
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
            "This record routes genome reduction through both drift-like causes "
            "(transmission bottlenecks, limited recombination) and "
            "selection-like ones (metabolic gene loss compensated by the host). "
            "Which dominates, and does the balance shift as an association ages?"
        ),
        "attaches_to": [
            "causal_graphs#reductive_genome_evolution",
            "causal_graphs#transmission_bottleneck",
            "causal_graphs#metabolic_gene_loss",
        ],
        "rationale": (
            "The two mechanisms predict opposite things about which genes go "
            "first: drift under a bottleneck removes genes roughly regardless of "
            "function, while host compensation removes exactly the genes whose "
            "products the host supplies. Because the record encodes both without "
            "weighting them, it cannot be used to predict what a newly sequenced "
            "symbiont will have lost -- which is most of what a reduction model "
            "is for."
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
                "whether host-complemented functions are lost preferentially "
                "once effective population size is controlled for"
            ),
            "would_support": (
                "loss is enriched for host-complemented functions beyond the "
                "drift expectation -- compensation drives the loss spectrum"
            ),
            "would_refute": (
                "loss tracks effective population size with no functional "
                "enrichment -- drift dominates and compensation is a consequence"
            ),
        },
        "scan_topic": "growth anomalies in corals",
    },
    "kgscan-d5aefedf82bb": {
        "file": "ecology/free_living.yaml",
        "prompt": (
            "Three compatible-solute systems -- ectoine, glycine betaine, and "
            "trehalose -- all feed osmotic stress tolerance in this record. Are "
            "they redundant backups, or does each cover a distinct range of "
            "osmolarity, temperature, and carbon availability?"
        ),
        "attaches_to": [
            "causal_graphs#osmotic_stress_tolerance",
            "causal_graphs#ectoine_biosynthesis",
            "causal_graphs#glycine_betaine_system",
            "causal_graphs#trehalose_biosynthesis",
        ],
        "rationale": (
            "Three parallel edges into one node is the graph's way of saying "
            "the routes are interchangeable, which is a strong claim given their "
            "costs differ -- de novo ectoine synthesis is carbon-expensive where "
            "betaine uptake is cheap when a precursor is available. If they are "
            "actually condition-partitioned, a genome carrying only one is "
            "osmotolerant over a narrower envelope than the record predicts, and "
            "that matters for anything inferring habitat range from gene content."
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
                "whether any single knockout loses growth in a region of the "
                "matrix where the others are sufficient"
            ),
            "would_support": (
                "single knockouts match wild type wherever another system is "
                "usable -- the routes are redundant as drawn"
            ),
            "would_refute": (
                "each single knockout fails in its own region -- the routes are "
                "partitioned and the parallel edges need conditions"
            ),
        },
        "scan_topic": "protozoan infection and gut microbial diversity",
    },
    "kgscan-4fc1a06fa1e3": {
        "file": "ecology/gut_associated.yaml",
        "prompt": (
            "Luminal oxygen limitation and the primary fermenter community "
            "appear here as separate features of the gut habitat. Which "
            "establishes which -- does the anoxic lumen permit the fermenters, "
            "or do the fermenters and the host epithelium create the anoxia?"
        ),
        "attaches_to": [
            "causal_graphs#luminal_oxygen_limitation",
            "causal_graphs#primary_fermenter_community",
        ],
        "rationale": (
            "The record presents both as given properties of the habitat, which "
            "leaves the causal direction unstated and therefore unusable. It is "
            "the direction that matters clinically: if the community maintains "
            "the anoxia, then losing the fermenters raises luminal oxygen and "
            "opens the door to facultative pathogens -- a self-reinforcing loop "
            "the current graph cannot represent, because a loop needs the arrow "
            "to point somewhere."
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
                "whether luminal oxygen falls before or only after the "
                "fermenters establish"
            ),
            "would_support": (
                "oxygen falls only after fermenter establishment and rises on "
                "their depletion -- the community creates the anoxia"
            ),
            "would_refute": (
                "the lumen is already anoxic before fermenters arrive -- the "
                "habitat permits them and the arrow points the other way"
            ),
        },
        "scan_topic": "plant-derived xenomiRs crossing kingdom barriers",
    },
}


def scan_note(disc: dict, topic: str) -> str:
    """Preserve the scan's output verbatim, and say why it is not the prompt.

    The sentence and the PMIDs move here together. Splitting them would leave
    the PMIDs looking like support for the authored question, which is exactly
    the false provenance this migration exists to avoid.
    """
    refs = ", ".join(e["reference"] for e in (disc.get("evidence") or []))
    return (
        f"Scan provenance (#409). The kg-microbe-kgscan pass raised this "
        f"discussion with the prompt {disc['prompt']!r}, retrieved from "
        f"{refs}. That sentence is about {topic}, not about this trait: the scan "
        f"matched the hedging vocabulary of a gap statement without checking "
        f"that the gap was about the trait it was filed under. The prompt above "
        f"was authored instead from this record's own causal graph, and those "
        f"PMIDs are not carried as its evidence because they support the "
        f"scraped sentence rather than the question. Both are kept here so "
        f"nothing the scan produced is lost."
    )


def apply(path: Path, plan_by_id: dict[str, dict]) -> list[str]:
    doc = yaml.safe_load(path.read_text())
    touched = []
    for disc in doc.get("discussions") or []:
        plan = plan_by_id.get(disc.get("discussion_id"))
        if plan is None:
            continue
        disc["notes"] = scan_note(disc, plan["scan_topic"])
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
