#!/usr/bin/env python3
"""#356 tranche 3: decide PATHWAY vs BIOLOGICAL_PROCESS, and write the rule down.

The first two tranches needed no new judgement -- tranche 1 because
``CausalNodeTypeEnum`` named the nodes as its own examples, tranche 2 because
#352 had already settled "a protein is not its activity". This one has neither,
and the schema does not help: PATHWAY is "a pathway or pathway-like mechanism"
and BIOLOGICAL_PROCESS is "a biological process". Neither decides
`ectoine_biosynthesis`.

THE DESCRIPTIONS DO NOT DECIDE IT EITHER, which is what makes this tranche
different from tranche 2. There, the two typings described visibly different
things (the enzyme vs its activity). Here they describe the same thing in the
same words -- `carotenoid_biosynthesis` is "Enzymatic PATHWAY producing
carotenoid pigments" under BIOLOGICAL_PROCESS and "Biosynthetic PATHWAY
producing carotenoid pigments" under PATHWAY. The split is arbitrary.

AND THE GROUNDING CANNOT DECIDE IT, which is the finding worth keeping. This
repo's standing doctrine is that the grounding settles a typing argument (#352,
#360, #382). It cannot here, because GO HAS NO PATHWAY BRANCH: every one of
these grounds to a GO biological_process -- GO:0019491, GO:0022900, GO:0009767,
GO:0016117, GO:0006113, GO:0006119, GO:0006636, GO:0002047 -- and five families
carry the IDENTICAL CURIE under both typings. Even the METPO groundings resolve
to METPO:1000060 "metabolism", itself defined as "A biological process that
maintain life in an organism". Read literally, the grounding says every one of
these is a biological process and PATHWAY should not exist.

PATHWAY IS NOT VESTIGIAL, though, and that is the same shape as the CAPACITY
finding in #352. Twelve CURIEs corpus-wide are typed PATHWAY and never
BIOLOGICAL_PROCESS, and they are the canonical named routes: GO:0006099
(tricarboxylic acid cycle), GO:0006097 (glyoxylate cycle), GO:0019253
(reductive pentose-phosphate cycle). There is a real sense here; it is just not
one GO draws.

So the rule has to be a stated curation convention rather than an inference, and
it must be written down or the split simply recurs:

    PATHWAY             a NAMED, conventionally enumerable multi-step route --
                        one whose steps a curator could list, and which has a
                        proper name in the literature. TCA cycle, Calvin cycle,
                        ectoine biosynthesis, the respiratory chain.

    BIOLOGICAL_PROCESS  everything else -- strategies, reaction classes, and
                        processes with no canonical step list.

The rule earns its keep by disagreeing with the majority twice: `ectoine_biosynthesis`
is 4 BIOLOGICAL_PROCESS to 2 PATHWAY and `carotenoid_biosynthesis` 5 to 1, and
both become PATHWAY because both are named biosynthetic routes -- five-step, with
the enzymes named (lysC/asd/ectB/ectA/ectC) in the corpus's own description. A
rule that only ever ratified the majority would not be a rule.

Usage:
    python scripts/migrate_pathway_vs_process.py [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import emit_trait_yaml  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"
TIMESTAMP = "2026-08-16T02:00:00Z"
ACTION = "NORMALISE_NODE_TYPE"

TARGET: dict[str, tuple[str, str]] = {
    "ectoine_biosynthesis": (
        "PATHWAY",
        "A named route, enumerated two ways and both of them enumerations. "
        "environment/euryhaline.yaml counts five steps from L-aspartate "
        "(lysC/asd/ectB/ectA/ectC); environment/nacl_delta_mid1.yaml counts the three "
        "ectABC enzymes proper. Naming the file matters because the two differ and a "
        "bare quote would put euryhaline's wording into nacl_delta_mid1's record (#400 "
        "review). Either way the steps can be listed, which is the test. Applied "
        "AGAINST the majority, which was 4 BIOLOGICAL_PROCESS to 2 before this tranche.",
    ),
    "carotenoid_biosynthesis": (
        "PATHWAY",
        "A named biosynthetic route. Most descriptions call it one outright, including "
        "BIOLOGICAL_PROCESS-typed ones ('Enzymatic pathway producing carotenoid "
        "pigments'); red_pigmented.yaml instead ENUMERATES the steps -- 'Phytoene "
        "synthase condenses two GGPP to phytoene, then desaturation/isomerization yields "
        "lycopene' -- which is the rule's own test for PATHWAY met explicitly rather than "
        "by naming. "
        "Applied AGAINST the majority, which was 5 BIOLOGICAL_PROCESS to 1 before this tranche.",
    ),
    "pufa_biosynthesis": (
        "PATHWAY",
        "A named biosynthetic route to polyunsaturated fatty acids. The two typings "
        "describe it in near-identical words, so the split was arbitrary and the rule "
        "breaks the 1-1 tie.",
    ),
    "phenazine_biosynthesis": (
        "PATHWAY",
        "A named biosynthetic route; both typings say 'Biosynthetic pathway producing "
        "phenazine pigments'. The rule breaks the 1-1 tie.",
    ),
    "electron_transport_chain": (
        "PATHWAY",
        "A named route through enumerable complexes. Was 4 PATHWAY to 2 before "
        "this tranche.",
    ),
    "photosynthetic_electron_transport": (
        "PATHWAY",
        "A named route in every record that carries it, though NOT THE SAME ROUTE, "
        "which is why no single step list belongs in this rationale. "
        "metabolism/phototrophy.yaml enumerates the oxygenic form ('Electron flow from "
        "water through PSII, cytochrome b6f and PSI'); photoheterotrophic.yaml and "
        "photoorganoheterotrophic.yaml cover ANOXYGENIC phototrophy -- one reaction "
        "centre, cyclic flow, no water oxidation -- and say the neutral thing on "
        "purpose. Quoting the oxygenic steps at them would assert biology they "
        "specifically do not claim (#400 review). Both forms are named routes whose "
        "steps a curator could list, which is the test. Was 5 PATHWAY to 1 before this "
        "tranche.",
    ),
    "oxidative_phosphorylation": (
        "PATHWAY",
        "A named route through enumerable complexes -- environment/ph_delta_mid1.yaml "
        "lists them (nuo, cyo, ndh, sdh). The rule breaks what was a 2-2 tie before "
        "this tranche.",
    ),
    "salt_in_strategy": (
        "BIOLOGICAL_PROCESS",
        "A STRATEGY, not a route. The family is described as osmoadaptation by "
        "accumulating intracellular inorganic ions -- haloalkaliphilic.yaml puts it as "
        "'Osmoadaptation by intracellular accumulation of inorganic ions (e.g. K+)', and "
        "the wording varies by record. There is no step list to enumerate, which is exactly the "
        "distinction this rule draws. Was 7 BIOLOGICAL_PROCESS to 1 before this "
        "tranche.",
    ),
    "aa_decarboxylation": (
        "BIOLOGICAL_PROCESS",
        "The same concept as amino_acid_decarboxylation under a shorter id, with a "
        "BYTE-IDENTICAL label ('amino-acid decarboxylation pathways') and a "
        "reaction-class description ('Decarboxylation pathways that consume protons "
        "and store energy as PMF'). Caught in review (#394): both this table and "
        "INCONSISTENT_NODE_TYPE key on node_id, so retyping the long-named one would "
        "have created a fresh split between two ids nothing compares. Included here "
        "rather than left, because this tranche is what would have caused it.",
    ),
    "amino_acid_decarboxylation": (
        "BIOLOGICAL_PROCESS",
        "A REACTION CLASS, not a route. The corpus describes it that way in "
        "neutrophilic.yaml -- 'Enzyme-catalyzed decarboxylation reaction that "
        "consumes cytoplasmic protons' -- and the wording varies by record, so read that "
        "as the family's sense rather than as this record's own text. Named systems "
        "that implement it (Gad) would be "
        "pathways; the reaction class is not. Was 4 BIOLOGICAL_PROCESS to 2 before this tranche.",
    ),
    "fermentation": (
        "BIOLOGICAL_PROCESS",
        "A CLASS of routes rather than one route -- fermentation names a mode of energy "
        "conservation with many distinct implementations, so its steps cannot be "
        "enumerated without picking one. Was 3 BIOLOGICAL_PROCESS to 2 before this tranche. NOTE its "
        "groundings disagree with each other (GO:0006113 x3, METPO:1002005, and "
        "METPO:1000845 which is ACETOGENESIS, a different concept) -- filed as #391 and "
        "deliberately NOT touched here, because retyping a node while carrying a wrong "
        "CURIE along unchanged would make it look reviewed.",
    ),
}


def apply(dry_run: bool = False) -> int:
    changed = 0
    for path in sorted(TRAITS.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        rel = str(path.relative_to(TRAITS))
        notes: list[str] = []
        # IN SCOPE means the file contains a targeted node, whether or not its
        # type still needs changing. The event is recorded for all of them, and
        # upserted, so editing a rationale and re-running refreshes what shipped.
        # Recording only on CHANGE is what let the script and the corpus diverge
        # in #392: the fix landed in the table and never reached the data, and
        # recovering meant restoring 22 files and re-running (#395).
        in_scope: list[str] = []
        for graph in (doc.get("causal_graphs") or []):
            for node in (graph.get("nodes") or []):
                nid = node.get("node_id")
                if nid not in TARGET:
                    continue
                in_scope.append(nid)
                target, _why = TARGET[nid]
                if node.get("node_type") != target:
                    was = node.get("node_type")
                    node["node_type"] = target
                    notes.append(f"{nid}: {was} -> {target}")
                    print(f"  {rel:56s} {nid} {was} -> {target}")
        if in_scope:
            touched = list(dict.fromkeys(in_scope))
            rationale = " ".join(TARGET[n][1] for n in touched if n in TARGET)
            # STATE THE DECISION, NOT THE DELTA. An upserted event is rewritten
            # on every re-run, so anything transient in it gets overwritten with
            # whatever this run happened to do -- the first version of this said
            # "no change needed here" on a re-run and erased the record of the
            # change it had made. What is permanently true is the decision: this
            # node is typed T in this record, under this rule, for this reason.
            # The before-and-after belongs in the commit diff, which is where
            # git already keeps it accurately.
            settled = ", ".join(f"{nid} is typed {TARGET[nid][0]}" for nid in touched)
            record_curation_event(
                doc, curator="claude", action=ACTION, llm_assisted=True,
                timestamp=TIMESTAMP, upsert=True,
                changes=("Under the PATHWAY-vs-BIOLOGICAL_PROCESS rule, one node_id means "
                         f"one thing corpus-wide (issue 356): {settled}. PATHWAY is a "
                         "named, conventionally enumerable multi-step route; "
                         f"BIOLOGICAL_PROCESS is everything else. {rationale}"),
            )
            changed += len(notes)
            if not dry_run:
                path.write_text(emit_trait_yaml(doc))
    print(f"\n{changed} node(s) retyped{' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
