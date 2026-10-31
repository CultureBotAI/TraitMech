#!/usr/bin/env python3
"""Curate Stage 5 grouped review remediation (Cycle 1 #1981, Cycle 2 #1995, Cycle 3–8 #2002).

Resolves the 4 actionable open findings from the Cycle 1 Stage 4 corpus-wide
record and cohort review (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1981), the 6 actionable open findings from the
Cycle 2 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1995), the 17 actionable open findings from the
Cycle 3 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002), the 18 actionable open findings from the
Cycle 4 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002), the 7 actionable open findings from the
Cycle 5 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002), the 13 actionable open findings from the
Cycle 6 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002), the 15 actionable open findings from the
Cycle 7 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002), and the 12 actionable open findings from the
Cycle 8 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002):
- `F-DEF-SRC-CYANOPHYCIN-001`..`004` (Cycle 1 #1981, 4 records)
- `F-DEF-SRC-CARBON-FIXATION-010`..`015` (Cycle 2 #1995, 6 records)
- `F-C3S4-DEF-SRC-001`..`017` (Cycle 3 #2002, 17 records)
- `F-C4S4-DEF-SRC-001`..`018` (Cycle 4 #2002, 18 records)
- `F-C5S4-DEF-SRC-001`..`007` (Cycle 5 #2002, 7 records)
- `F-C6S4-DEF-SRC-001`..`013` (Cycle 6 #2002, 13 records)
- `F-C7S4-DEF-SRC-001`..`015` (Cycle 7 #2002, 15 records)
- `F-C8S4-DEF-SRC-001`..`012` (Cycle 8 #2002, 12 records)

Default is dry-run; pass `--apply` to write changes via `write_validated_trait`
and `record_curation_event`.

Usage:
    python scripts/curate_stage5_review_findings.py
    python scripts/curate_stage5_review_findings.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    validate_trait,
    write_validated_trait,
)

DO_NOT_WORK_PATH = REPO_ROOT / "DO_NOT_WORK.md"
CURATOR = "claude"
TIMESTAMP = "2026-10-22T05:20:00Z"
CYCLE2_TIMESTAMP = "2026-10-23T16:05:00Z"
CYCLE3_TIMESTAMP = "2026-10-24T02:45:00Z"
CYCLE4_TIMESTAMP = "2026-10-25T12:55:00Z"
CYCLE5_TIMESTAMP = "2026-10-25T21:40:00Z"
CYCLE6_TIMESTAMP = "2026-10-26T08:15:00Z"
CYCLE7_TIMESTAMP = "2026-10-30T22:10:00Z"
CYCLE8_TIMESTAMP = "2026-10-31T10:45:00Z"
ACTION = "ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE"

REMEDIATION_SPECS: dict[str, dict[str, Any]] = {
    "data/traits/morphology/cyanophycin_granule.yaml": {
        "identifier": "traitmech:000673",
        "finding_id": "F-DEF-SRC-CYANOPHYCIN-001",
        "timestamp": TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.01298-18",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.01298-18",
            "snippet": (
                "Cyanophycin accumulates in the form of opaque and light-scattering "
                "granules in the cell"
            ),
            "notes": (
                "Watzer and Forchhammer (2018), Introduction and Abstract, directly "
                "read in publisher HTML: cyanophycin accumulates as opaque, "
                "light-scattering intracellular storage granules serving as a "
                'temporary nitrogen reserve (abstract: "cyanophycin can be used as a '
                'temporary nitrogen storage"). Supports the record definition and '
                "definition_source."
            ),
        },
        "changes": (
            "Added DOI:10.1128/AEM.01298-18 with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-CYANOPHYCIN-001 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/cadmium_tolerant.yaml": {
        "identifier": "traitmech:000013",
        "finding_id": "F-DEF-SRC-CADMIUM-002",
        "timestamp": TIMESTAMP,
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA), P-type ATPases, and cation diffusion facilitators, "
                "supporting the record definition and definition_source for cadmium tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-CADMIUM-002 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/cobalt_tolerant.yaml": {
        "identifier": "traitmech:000015",
        "finding_id": "F-DEF-SRC-COBALT-003",
        "timestamp": TIMESTAMP,
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA and CnrCBA) and cation diffusion facilitators, "
                "supporting the record definition and definition_source for cobalt tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-COBALT-003 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/zinc_tolerant.yaml": {
        "identifier": "traitmech:000014",
        "finding_id": "F-DEF-SRC-ZINC-004",
        "timestamp": TIMESTAMP,
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA), P-type ATPases (including ZntA), and cation "
                "diffusion facilitators, supporting the record definition and "
                "definition_source for zinc tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-ZINC-004 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/metabolism/carbon_fixation.yaml": {
        "identifier": "traitmech:000019",
        "finding_id": "F-DEF-SRC-CARBON-FIXATION-010",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.02473-10",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.02473-10",
            "snippet": (
                "The reductive pentose phosphate cycle is the quantitatively most "
                "important mechanism of autotrophic CO2 fixation in nature."
            ),
            "notes": (
                'Berg (2011) "Ecological aspects of the distribution of different '
                'autotrophic CO2 fixation pathways" — authoritative review of the '
                "six known pathways."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/AEM.02473-10 (already "
            "present on causal_graphs[0].edges[11]) to record-level evidence[0] to "
            "match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CARBON-FIXATION-010 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/wood_ljungdahl_pathway.yaml": {
        "identifier": "traitmech:000022",
        "finding_id": "F-DEF-SRC-WOOD-LJUNGDAHL-011",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.bbapap.2008.08.012",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.bbapap.2008.08.012",
            "snippet": (
                "use the reductive acetyl-CoA or Wood-Ljungdahl pathway as their "
                "main mechanism for energy conservation and for synthesis of "
                "acetyl-CoA and cell carbon from CO2"
            ),
            "notes": (
                "Ragsdale & Pierce (2008) review the enzymology and bioenergetics "
                "of the Wood–Ljungdahl pathway."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.bbapap.2008.08.012 "
            "(already present on causal_graphs[0].edges[0]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-WOOD-LJUNGDAHL-011 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/propionic_acid_fermentation.yaml": {
        "identifier": "traitmech:000029",
        "finding_id": "F-DEF-SRC-PROPIONIC-FERM-012",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.3390/molecules31020333",
        "evidence_entry": {
            "reference": "DOI:10.3390/molecules31020333",
            "snippet": (
                "substrates such as glucose, glycerol or lactic acid are converted "
                "into propionic acid"
            ),
            "notes": (
                "Review of microbial propionic acid fermentation pathways "
                "(Wood-Werkman cycle and acrylate pathway), metabolic engineering, "
                "and bioprocess optimization."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3390/molecules31020333 "
            "(already present on causal_graphs[0].edges[1]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-PROPIONIC-FERM-012 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/manganese_oxidation.yaml": {
        "identifier": "traitmech:000032",
        "finding_id": "F-DEF-SRC-MANGANESE-OX-013",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.tim.2005.07.009",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.tim.2005.07.009",
            "snippet": (
                "the reaction might involve a unique multicopper oxidase system "
                "capable of a two-electron oxidation of the substrate"
            ),
            "notes": (
                'Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports '
                "bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase "
                "mechanism."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.tim.2005.07.009 "
            "(already present on causal_graphs[0].edges[3]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-MANGANESE-OX-013 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/cellulolysis.yaml": {
        "identifier": "traitmech:000111",
        "finding_id": "F-DEF-SRC-CELLULOLYSIS-014",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1128/MMBR.66.3.506-577.2002",
        "evidence_entry": {
            "reference": "DOI:10.1128/MMBR.66.3.506-577.2002",
            "snippet": "complexed cellulase systems",
            "notes": (
                "Lynd et al. review microbial cellulose utilization, its enzymology, "
                "and cellulosome systems."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/MMBR.66.3.506-577.2002 "
            "(already present on causal_graphs[0].edges[15]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CELLULOLYSIS-014 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/chitinolysis.yaml": {
        "identifier": "traitmech:000112",
        "finding_id": "F-DEF-SRC-CHITINOLYSIS-015",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2013.00149",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2013.00149",
            "snippet": (
                "initial hydrolysis of the (1→4)-β-glycoside bond, as seen for "
                "chitinase-catalyzed chitin degradation"
            ),
            "notes": (
                "Beier & Bertilsson review bacterial chitin degradation mechanisms "
                "and ecophysiological strategies."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2013.00149 "
            "(already present on causal_graphs[0].edges[6]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CHITINOLYSIS-015 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/physiology/photoorganoheterotrophic.yaml": {
        "identifier": "METPO:1000659",
        "finding_id": "F-C3S4-DEF-SRC-001",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1016/B978-012373944-5.00083-3",
        "evidence_entry": {
            "reference": "DOI:10.1016/B978-012373944-5.00083-3",
            "snippet": "use of light",
            "notes": (
                "Bryant & Frigaard (2006) overview chapter supports light as the "
                "energy source in photoheterotrophy categories."
            ),
        },
        "changes": (
            "Appended record-level evidence entry for definition_source "
            "DOI:10.1016/B978-012373944-5.00083-3 using the verified verbatim "
            "snippet already present on causal_graphs[0].edges[0].evidence[0] "
            "(Cycle 3 Stage 5 remediation of F-C3S4-DEF-SRC-001 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/physiology/oxidase_activity.yaml": {
        "identifier": "traitmech:000076",
        "finding_id": "F-C3S4-DEF-SRC-002",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.3390/microorganisms10050926",
        "evidence_entry": {
            "reference": "DOI:10.3390/microorganisms10050926",
            "snippet": (
                "Cytochrome c oxidases of the heme–copper oxygen reductase family A"
            ),
            "notes": (
                "Hederstedt reviews bacterial cytochrome c oxidase, the terminal "
                "respiratory oxidase detected by the oxidase test."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3390/microorganisms10050926 "
            "(already present on causal_graphs[0].edges[9].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-002 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/peritrichous.yaml": {
        "identifier": "traitmech:000060",
        "finding_id": "F-C3S4-DEF-SRC-003",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1093/femsre/fuv034",
        "evidence_entry": {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": "five to six flagellar filaments distributed over the cell body",
            "notes": (
                "Schuhmacher et al. describe peritrichous (surface-distributed) "
                "flagellation as one of the conserved flagellation patterns."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1093/femsre/fuv034 "
            "(already present on causal_graphs[0].edges[2].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-003 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/proteorhodopsin_phototrophy.yaml": {
        "identifier": "traitmech:000036",
        "finding_id": "F-C3S4-DEF-SRC-004",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.289.5486.1902",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.289.5486.1902",
            "snippet": "bound retinal to form an active, light-driven proton pump",
            "notes": (
                "Béjà et al. identified proteorhodopsin, a retinal-binding "
                "light-driven proton pump in an uncultivated marine bacterium, as "
                "evidence for a new type of phototrophy in the sea."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1126/science.289.5486.1902 "
            "(already present on causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-004 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/starch_degradation.yaml": {
        "identifier": "traitmech:000115",
        "finding_id": "F-C3S4-DEF-SRC-005",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1016/S0168-1656(01)00407-2",
        "evidence_entry": {
            "reference": "DOI:10.1016/S0168-1656(01)00407-2",
            "snippet": (
                "the use of starch-converting enzymes in the production of "
                "maltodextrin, modified starches, or glucose and fructose syrups"
            ),
            "notes": (
                "van der Maarel et al. review starch-converting enzymes of the "
                "alpha-amylase family that hydrolyze starch to oligosaccharides and "
                "glucose."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/S0168-1656(01)00407-2 "
            "(already present on causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-005 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/three_hydroxypropionate_bicycle.yaml": {
        "identifier": "traitmech:000023",
        "finding_id": "F-C3S4-DEF-SRC-006",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.02473-10",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.02473-10",
            "snippet": (
                "The 3-hydroxypropionate (Fuchs-Holo) bi-cycle. Enzymes: 1, "
                "acetyl-CoA carboxylase"
            ),
            "notes": (
                "Berg review describes the 3-hydroxypropionate bicycle and its "
                "association with Chloroflexus."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/AEM.02473-10 "
            "(already present on causal_graphs[0].edges[9].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-006 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/ethanol_fermentation.yaml": {
        "identifier": "traitmech:000028",
        "finding_id": "F-C3S4-DEF-SRC-007",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2021.703525",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2021.703525",
            "snippet": (
                "fermentation is defined as an anaerobic bacterial redox process of "
                "an organic substrate leading to different products"
            ),
            "notes": (
                "Review of fermentative energy conservation supports ethanol as an "
                "NADH-reoxidizing fermentation end product."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2021.703525 "
            "(already present on causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[1] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-007 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/lactic_acid_fermentation.yaml": {
        "identifier": "traitmech:000026",
        "finding_id": "F-C3S4-DEF-SRC-008",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2021.703525",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2021.703525",
            "snippet": (
                "fermentation is defined as an anaerobic bacterial redox process of "
                "an organic substrate leading to different products"
            ),
            "notes": (
                "Review of energy conservation in anaerobic fermentations supports "
                "lactate as a fermentation end product generated with "
                "substrate-level phosphorylation."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2021.703525 "
            "(already present on causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-008 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/mixed_acid_fermentation.yaml": {
        "identifier": "traitmech:000027",
        "finding_id": "F-C3S4-DEF-SRC-009",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2021.703525",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2021.703525",
            "snippet": (
                "fermentation is defined as an anaerobic bacterial redox process of "
                "an organic substrate leading to different products"
            ),
            "notes": (
                "Review of fermentative energy conservation lists acetate, ethanol, "
                "lactate, succinate and formate as products of mixed-acid "
                "fermentation."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2021.703525 "
            "(already present on sibling ethanol_fermentation.yaml and "
            "lactic_acid_fermentation.yaml causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-009 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/fermentative_hydrogen_production.yaml": {
        "identifier": "traitmech:000109",
        "finding_id": "F-C3S4-DEF-SRC-010",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2021.703525",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2021.703525",
            "snippet": (
                "fermentation is defined as an anaerobic bacterial redox process of "
                "an organic substrate leading to different products"
            ),
            "notes": (
                "Review of fermentative energy conservation supports H2 production "
                "as a redox-balancing fermentation output via hydrogenases."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2021.703525 "
            "(already present on sibling ethanol_fermentation.yaml and "
            "lactic_acid_fermentation.yaml causal_graphs[0].edges[0].evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-010 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/calvin_benson_bassham_cycle.yaml": {
        "identifier": "traitmech:000020",
        "finding_id": "F-C3S4-DEF-SRC-011",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.02473-10",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.02473-10",
            "snippet": (
                "The reductive pentose phosphate cycle is the quantitatively most "
                "important mechanism of autotrophic CO2 fixation in nature."
            ),
            "notes": (
                "Berg review identifies the Calvin-Benson-Bassham (reductive pentose "
                "phosphate) cycle as the reference autotrophic pathway against which "
                "the other five are distinguished."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/AEM.02473-10 "
            "(already present on parent record carbon_fixation.yaml evidence[0]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-011 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/dissimilatory_manganese_reduction.yaml": {
        "identifier": "traitmech:000108",
        "finding_id": "F-C3S4-DEF-SRC-012",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1128/mr.55.2.259-287.1991",
        "evidence_entry": {
            "reference": "DOI:10.1128/mr.55.2.259-287.1991",
            "snippet": (
                "The oxidation of organic matter coupled to the reduction of Fe(III) "
                "or Mn(IV) is one of the most important biogeochemical reactions in "
                "aquatic sediments, soils, and groundwater"
            ),
            "notes": (
                "Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as "
                "energy-conserving anaerobic respiration on metal-oxide acceptors."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/mr.55.2.259-287.1991 "
            "(already present on parent record dissimilatory_metal_reduction.yaml "
            "evidence[0]) to record-level evidence[0] to match definition_source "
            "(Cycle 3 Stage 5 remediation of F-C3S4-DEF-SRC-012 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml": {
        "identifier": "traitmech:000030",
        "finding_id": "F-C3S4-DEF-SRC-013",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.1254070",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.1254070",
            "snippet": (
                "Denitrification converts nitrate into nitrogenous gas and thus "
                "removes fixed nitrogen from the biosphere, whereas ammonification "
                "converts nitrate into ammonium"
            ),
            "notes": (
                "Kraft et al. show the donor-to-acceptor ratio governs whether "
                "nitrate respiration ends in ammonium (DNRA) or N2 (denitrification)."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1126/science.1254070 "
            "(already present on parent record nitrate_respiration.yaml "
            "evidence[0]) to record-level evidence[0] to match definition_source "
            "(Cycle 3 Stage 5 remediation of F-C3S4-DEF-SRC-013 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/free_living.yaml": {
        "identifier": "traitmech:000048",
        "finding_id": "F-C3S4-DEF-SRC-014",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro1341",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro1341",
            "snippet": "free-living microbial taxa",
            "notes": (
                "Martiny et al. support biogeographic patterning of free-living "
                "microbial taxa across environments."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro1341 "
            "(already present on sibling record soil_dwelling.yaml evidence[1]) to "
            "record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-014 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/amphitrichous.yaml": {
        "identifier": "traitmech:000059",
        "finding_id": "F-C3S4-DEF-SRC-015",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1093/femsre/fuv034",
        "evidence_entry": {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": (
                "Bacteria differ in number and location of their flagella that "
                "appear in regular patterns at the cell surface (flagellation "
                "pattern)."
            ),
            "notes": (
                "Schuhmacher et al. describe bipolar (amphitrichous) flagellation "
                "among the flagellation patterns governed by FlhF/FlhG."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1093/femsre/fuv034 "
            "(already present on sibling record polar_flagellation.yaml evidence[0]) "
            "to record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-015 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/lophotrichous.yaml": {
        "identifier": "traitmech:000058",
        "finding_id": "F-C3S4-DEF-SRC-016",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1093/femsre/fuv034",
        "evidence_entry": {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": (
                "Bacteria differ in number and location of their flagella that "
                "appear in regular patterns at the cell surface (flagellation "
                "pattern)."
            ),
            "notes": (
                "Schuhmacher et al. describe polar tufts of flagella (lophotrichous) "
                "among the regular flagellation patterns bacteria maintain."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1093/femsre/fuv034 "
            "(already present on sibling record polar_flagellation.yaml evidence[0]) "
            "to record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-016 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/monotrichous.yaml": {
        "identifier": "traitmech:000057",
        "finding_id": "F-C3S4-DEF-SRC-017",
        "timestamp": CYCLE3_TIMESTAMP,
        "definition_source": "DOI:10.1093/femsre/fuv034",
        "evidence_entry": {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": (
                "Bacteria differ in number and location of their flagella that "
                "appear in regular patterns at the cell surface (flagellation "
                "pattern)."
            ),
            "notes": (
                "Schuhmacher et al. describe single-flagellum (monotrichous, polar) "
                "flagellation as one regular flagellation pattern."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1093/femsre/fuv034 "
            "(already present on sibling record polar_flagellation.yaml evidence[0]) "
            "to record-level evidence[0] to match definition_source (Cycle 3 Stage 5 "
            "remediation of F-C3S4-DEF-SRC-017 in group "
            "G-C3S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/habitat_association.yaml": {
        "identifier": "traitmech:000047",
        "finding_id": "F-C4S4-DEF-SRC-001",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro1341",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro1341",
            "snippet": "free-living microbial taxa",
            "notes": (
                'Martiny et al., "Microbial biogeography", support habitat/niche as '
                "a structuring axis of microbial distribution; parent of the habitat "
                "sub-variants."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro1341 "
            "(already present on child records free_living.yaml evidence[0] and "
            "soil_dwelling.yaml evidence[1]) to record-level evidence[0] to match "
            "definition_source (Cycle 4 Stage 5 remediation of F-C4S4-DEF-SRC-001 "
            "in group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/environment/neutrophilic.yaml": {
        "identifier": "METPO:1003001",
        "finding_id": "F-C4S4-DEF-SRC-002",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro2549",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro2549",
            "snippet": "external pH values outside the cytoplasmic pH",
            "notes": (
                "Supports pH growth preference as tied to cytoplasmic pH requirements."
            ),
        },
        "changes": (
            "Replaced elliptical record-level evidence[0].snippet on "
            "DOI:10.1038/nrmicro2549 with contiguous verbatim snippet already "
            "present on causal_graphs[0].edges[0].evidence[0] (Cycle 4 Stage 5 "
            "remediation of F-C4S4-DEF-SRC-002 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/reductive_tca_cycle.yaml": {
        "identifier": "traitmech:000021",
        "finding_id": "F-C4S4-DEF-SRC-003",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.02473-10",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.02473-10",
            "snippet": (
                "the second autotrophic CO2 fixation cycle (the reductive citric "
                "acid cycle) had been discovered"
            ),
            "notes": (
                "Berg review describes the reductive citric acid cycle as functional "
                "in anaerobic/microaerophilic autotrophs."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/AEM.02473-10 "
            "(already present on parent record carbon_fixation.yaml "
            "causal_graphs[0].edges[12].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-003 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/cell_shape.yaml": {
        "identifier": "METPO:1000666",
        "finding_id": "F-C4S4-DEF-SRC-004",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro1205",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro1205",
            "snippet": "primary role in maintaining cell shape",
            "notes": (
                "Supports bacterial cell shape as determined by cell wall and "
                "cytoskeletal elements."
            ),
        },
        "changes": (
            "Replaced elliptical record-level evidence[0].snippet on "
            "DOI:10.1038/nrmicro1205 with contiguous verbatim snippet already "
            "present on causal_graphs[0].edges[0].evidence[0] (Cycle 4 Stage 5 "
            "remediation of F-C4S4-DEF-SRC-004 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/flagellar_arrangement.yaml": {
        "identifier": "traitmech:000056",
        "finding_id": "F-C4S4-DEF-SRC-005",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1093/femsre/fuv034",
        "evidence_entry": {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": (
                "Bacteria differ in number and location of their flagella that "
                "appear in regular patterns at the cell surface (flagellation "
                "pattern)."
            ),
            "notes": (
                "Schuhmacher, Thormann & Bange describe how bacteria maintain a "
                "regular number and cellular location of flagella (the flagellation "
                "pattern); parent of the specific arrangement sub-variants."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1093/femsre/fuv034 "
            "(already present on child records polar_flagellation.yaml, "
            "amphitrichous.yaml, lophotrichous.yaml, and monotrichous.yaml "
            "evidence[0]) to record-level evidence[0] to match definition_source "
            "(Cycle 4 Stage 5 remediation of F-C4S4-DEF-SRC-005 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/orange_pigmented.yaml": {
        "identifier": "METPO:1003026",
        "finding_id": "F-C4S4-DEF-SRC-006",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1080/1040841X.2025.2526423",
        "evidence_entry": {
            "reference": "DOI:10.1080/1040841X.2025.2526423",
            "snippet": "red, pink, orange, and yellow pigmentation in bacteria",
            "notes": (
                "Supports orange microbial pigmentation as a bacterial "
                "carotenoid-associated color phenotype."
            ),
        },
        "changes": (
            "Replaced elliptical record-level evidence[0].snippet on "
            "DOI:10.1080/1040841X.2025.2526423 with contiguous verbatim snippet "
            "already present on parent record carotenoid_pigmentation.yaml and "
            "sibling records pink_pigmented.yaml and yellow_pigmented.yaml "
            "evidence[0] (Cycle 4 Stage 5 remediation of F-C4S4-DEF-SRC-006 in "
            "group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/morphology/spirochete_shaped.yaml": {
        "identifier": "METPO:1000693",
        "finding_id": "F-C4S4-DEF-SRC-007",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1073/pnas.200221797",
        "evidence_entry": {
            "reference": "DOI:10.1073/pnas.200221797",
            "snippet": (
                "cell morphology is either a helix, a flat wave, or an irregularly "
                "shaped helix"
            ),
            "notes": (
                "Supports spirochete morphology as a cell-cylinder and "
                "periplasmic-flagella interaction."
            ),
        },
        "changes": (
            "Replaced elliptical record-level evidence[0].snippet on "
            "DOI:10.1073/pnas.200221797 with contiguous verbatim snippet already "
            "present on causal_graphs[0].edges[3].evidence[0] (Cycle 4 Stage 5 "
            "remediation of F-C4S4-DEF-SRC-007 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/physiology/chemolithoautotrophic.yaml": {
        "identifier": "METPO:1000637",
        "finding_id": "F-C4S4-DEF-SRC-008",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1146/annurev.micro.52.1.191",
        "evidence_entry": {
            "reference": "DOI:10.1146/annurev.micro.52.1.191",
            "snippet": "Carbon Dioxide Fixation in Chemoautotrophs",
            "notes": "Review supports chemoautotrophic bacterial CO2 fixation.",
        },
        "changes": (
            "Replaced elliptical record-level evidence[0].snippet on "
            "DOI:10.1146/annurev.micro.52.1.191 with contiguous verbatim snippet "
            "already present on causal_graphs[0].edges[5].evidence[0] and parent "
            "record chemoautotrophic.yaml evidence[0] (Cycle 4 Stage 5 remediation "
            "of F-C4S4-DEF-SRC-008 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_her_system.yaml": {
        "identifier": "traitmech:000409",
        "finding_id": "F-C4S4-DEF-SRC-009",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-009 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_hhe_system.yaml": {
        "identifier": "traitmech:000353",
        "finding_id": "F-C4S4-DEF-SRC-010",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-010 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_iet_system.yaml": {
        "identifier": "traitmech:000354",
        "finding_id": "F-C4S4-DEF-SRC-011",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-011 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_mza_system.yaml": {
        "identifier": "traitmech:000355",
        "finding_id": "F-C4S4-DEF-SRC-012",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-012 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_ppl_system.yaml": {
        "identifier": "traitmech:000356",
        "finding_id": "F-C4S4-DEF-SRC-013",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-013 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_qat_system.yaml": {
        "identifier": "traitmech:000359",
        "finding_id": "F-C4S4-DEF-SRC-014",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-014 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_rl_system.yaml": {
        "identifier": "traitmech:000352",
        "finding_id": "F-C4S4-DEF-SRC-015",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-015 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_tery_system.yaml": {
        "identifier": "traitmech:000360",
        "finding_id": "F-C4S4-DEF-SRC-016",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-016 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_tmn_system.yaml": {
        "identifier": "traitmech:000357",
        "finding_id": "F-C4S4-DEF-SRC-017",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-017 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_upx_system.yaml": {
        "identifier": "traitmech:000358",
        "finding_id": "F-C4S4-DEF-SRC-018",
        "timestamp": CYCLE4_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 4 Stage 5 remediation of "
            "F-C4S4-DEF-SRC-018 in group "
            "G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    # Cycle 5 Stage 5 remediation (#2002): 7 open findings from Cycle 5 Stage 4
    "data/traits/genomics/gao_her_duf_system.yaml": {
        "identifier": "traitmech:000361",
        "finding_id": "F-C5S4-DEF-SRC-001",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-001 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/gao_her_sir_system.yaml": {
        "identifier": "traitmech:000362",
        "finding_id": "F-C5S4-DEF-SRC-002",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.aba0372",
        "replace_reference": "PMID:32855333",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.aba0372",
            "snippet": (
                "By systematic defense gene prediction and heterologous "
                "reconstitution, here we discover 29 widespread antiviral gene "
                "cassettes, collectively present in 32% of all sequenced bacterial "
                "and archaeal genomes, that mediate protection against specific "
                "bacteriophages."
            ),
            "notes": (
                "Gao et al. support a systematic defense-gene prediction and "
                "heterologous reconstitution campaign that discovered widespread "
                "antiviral gene cassettes (PMID:32855333 / DOI:10.1126/science.aba0372)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32855333 to "
            "DOI:10.1126/science.aba0372 (same Gao et al. 2020 publication) to "
            "match definition_source while preserving the verified verbatim snippet "
            "and PMID cross-reference in notes (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-002 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/genome_streamlining.yaml": {
        "identifier": "traitmech:000099",
        "finding_id": "F-C5S4-DEF-SRC-003",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1038/ismej.2014.60",
        "evidence_entry": {
            "reference": "DOI:10.1038/ismej.2014.60",
            "snippet": "minimizes resources required for replication",
            "notes": (
                "Giovannoni et al. set out streamlining theory, explaining small "
                "streamlined genomes of abundant oligotrophic microbes."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/ismej.2014.60 "
            "(already present on oligotrophic.yaml "
            "causal_graphs[0].edges[2].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-003 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/biopolymer_degradation.yaml": {
        "identifier": "traitmech:000110",
        "finding_id": "F-C5S4-DEF-SRC-004",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cbpa.2015.10.018",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cbpa.2015.10.018",
            "snippet": (
                "The enzymatic degradation of cellulose and hemicellulose is "
                "accomplished in Nature via the collective action of multiple "
                "carbohydrate-active enzymes"
            ),
            "notes": (
                "Cragg et al. review lignocellulose degradation mechanisms across "
                "the tree of life, using complementary enzymes to deconstruct plant "
                "biopolymers; parent of the polymer-specific sub-variants."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.cbpa.2015.10.018 "
            "(already present on saprotrophy.yaml "
            "causal_graphs[0].edges[5].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-004 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/denitrification.yaml": {
        "identifier": "traitmech:000104",
        "finding_id": "F-C5S4-DEF-SRC-005",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1128/mmbr.61.4.533-616.1997",
        "evidence_entry": {
            "reference": "DOI:10.1128/mmbr.61.4.533-616.1997",
            "snippet": "N oxides as terminal electron acceptors",
            "notes": (
                "Zumft reviews the cell biology and molecular basis of "
                "denitrification, the stepwise respiratory reduction of nitrate to "
                "dinitrogen."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/mmbr.61.4.533-616.1997 "
            "(already present on ancestor records nitrogen_respiration.yaml and "
            "anaerobic_respiration.yaml evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-005 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/metabolism/sulfur_oxidation.yaml": {
        "identifier": "traitmech:000106",
        "finding_id": "F-C5S4-DEF-SRC-006",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1111/j.1574-6976.2009.00187.x",
        "evidence_entry": {
            "reference": "DOI:10.1111/j.1574-6976.2009.00187.x",
            "snippet": "lithotrophic sulfur oxidation",
            "notes": (
                "Ghosh & Dam review the biochemistry and molecular biology of "
                "lithotrophic sulfur oxidation across bacteria and archaea."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1111/j.1574-6976.2009.00187.x "
            "(already present on lithotrophic.yaml "
            "causal_graphs[0].edges[2].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 5 Stage 5 remediation of "
            "F-C5S4-DEF-SRC-006 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/physiology/catalase_activity.yaml": {
        "identifier": "traitmech:000075",
        "finding_id": "F-C5S4-DEF-SRC-007",
        "timestamp": CYCLE5_TIMESTAMP,
        "definition_source": "DOI:10.1007/s00018-003-3206-5",
        "evidence_entry": {
            "reference": "DOI:10.1007/s00018-003-3206-5",
            "snippet": (
                "hydrogen peroxide to water and molecular oxygen, serving to "
                "protect cells"
            ),
            "notes": (
                "Chelikani, Fita & Loewen review the diversity of catalases, "
                "enzymes that dismutate hydrogen peroxide to water and oxygen."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1007/s00018-003-3206-5 "
            "(already present on oxidative_stress_response.yaml evidence[1]) to "
            "record-level evidence[0] to match definition_source (Cycle 5 Stage 5 "
            "remediation of F-C5S4-DEF-SRC-007 in group "
            "G-C5S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_giy_yig_system.yaml": {
        "identifier": "traitmech:000346",
        "finding_id": "F-C6S4-DEF-SRC-001",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-001 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_hepn_tm_system.yaml": {
        "identifier": "traitmech:000347",
        "finding_id": "F-C6S4-DEF-SRC-002",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-002 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_hp_system.yaml": {
        "identifier": "traitmech:000348",
        "finding_id": "F-C6S4-DEF-SRC-003",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-003 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_hp_sdh_sah_system.yaml": {
        "identifier": "traitmech:000349",
        "finding_id": "F-C6S4-DEF-SRC-004",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-004 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_hsdr_like_system.yaml": {
        "identifier": "traitmech:000350",
        "finding_id": "F-C6S4-DEF-SRC-005",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-005 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/fs_sma_system.yaml": {
        "identifier": "traitmech:000351",
        "finding_id": "F-C6S4-DEF-SRC-006",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2022.07.014",
        "replace_reference": "PMID:35985290",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2022.07.014",
            "snippet": (
                "the phage-inducible chromosomal islands (PICIs), carry an "
                "impressive arsenal of defense mechanisms"
            ),
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal islands as "
                "carriers of mobile-element defense mechanisms "
                "(PMID:35985290 / DOI:10.1016/j.cell.2022.07.014)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:35985290 to "
            "DOI:10.1016/j.cell.2022.07.014 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-006 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/mazef_system.yaml": {
        "identifier": "traitmech:000345",
        "finding_id": "F-C6S4-DEF-SRC-007",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1098/rsbl.2025.0080",
        "replace_reference": "PMID:40494395",
        "evidence_entry": {
            "reference": "DOI:10.1098/rsbl.2025.0080",
            "snippet": (
                "we investigated the role of a model toxin-antitoxin system, "
                "MazEF, in protecting Escherichia coli against two RNA phage "
                "species"
            ),
            "notes": (
                "Nikolic et al. directly tested MazEF as an Escherichia coli "
                "toxin-antitoxin module protecting against RNA phages "
                "(PMID:40494395 / DOI:10.1098/rsbl.2025.0080)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:40494395 to "
            "DOI:10.1098/rsbl.2025.0080 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-007 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/mok_hok_sok_system.yaml": {
        "identifier": "traitmech:000372",
        "finding_id": "F-C6S4-DEF-SRC-008",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1128/jb.178.7.2044-2050.1996",
        "replace_reference": "PMID:8606182",
        "evidence_entry": {
            "reference": "DOI:10.1128/jb.178.7.2044-2050.1996",
            "snippet": (
                "To investigate whether the hok/sok locus evolved as a "
                "phage-exclusion mechanism, Escherichia coli cells that contain "
                "hok/sok on a pBR322-based plasmid were challenged with T1, T4, "
                "T5, T7, and lambda phage."
            ),
            "notes": (
                "Pecota and Wood tested whether a plasmid-carried hok/sok locus "
                "can act as a phage-exclusion mechanism "
                "(PMID:8606182 / DOI:10.1128/jb.178.7.2044-2050.1996)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:8606182 to "
            "DOI:10.1128/jb.178.7.2044-2050.1996 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 6 Stage 5 "
            "remediation of F-C6S4-DEF-SRC-008 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/pfiat_system.yaml": {
        "identifier": "traitmech:000365",
        "finding_id": "F-C6S4-DEF-SRC-009",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1111/1751-7915.13570",
        "replace_reference": "PMID:32246813",
        "evidence_entry": {
            "reference": "DOI:10.1111/1751-7915.13570",
            "snippet": (
                "we provided experimental evidence to demonstrate that PA0729 "
                "and the upstream ORF Rorf0727 near the right attachment site of "
                "Pf4 form a type II toxin/antitoxin (TA) pair."
            ),
            "notes": (
                "Li et al. experimentally identify PA0729 and Rorf0727 in the "
                "Pf4 prophage as a PfiT/PfiA type II toxin-antitoxin pair "
                "(PMID:32246813 / DOI:10.1111/1751-7915.13570)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:32246813 to "
            "DOI:10.1111/1751-7915.13570 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-009 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/prrc_system.yaml": {
        "identifier": "traitmech:000364",
        "finding_id": "F-C6S4-DEF-SRC-010",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1186/1743-422X-7-360",
        "replace_reference": "PMID:21129205",
        "evidence_entry": {
            "reference": "DOI:10.1186/1743-422X-7-360",
            "snippet": (
                "phage exclusion systems that involve T4-mediated activation of "
                "a latent endoribonuclease (PrrC) and cofactor-assisted "
                "activation of EF-Tu proteolysis (Gol-Lit)"
            ),
            "notes": (
                "Uzan et al. name PrrC as a T4-mediated phage-exclusion system "
                "that activates a latent endoribonuclease "
                "(PMID:21129205 / DOI:10.1186/1743-422X-7-360)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:21129205 to "
            "DOI:10.1186/1743-422X-7-360 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-010 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/rloc_system.yaml": {
        "identifier": "traitmech:000366",
        "finding_id": "F-C6S4-DEF-SRC-011",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1111/j.1365-2958.2008.06387.x",
        "replace_reference": "PMID:18681940",
        "evidence_entry": {
            "reference": "DOI:10.1111/j.1365-2958.2008.06387.x",
            "snippet": (
                "The conserved bacterial protein RloC, a distant homologue of "
                "the tRNA(Lys) anticodon nuclease (ACNase) PrrC, is shown here "
                "to act as a wobble nucleotide-excising and Zn(++)-responsive "
                "tRNase."
            ),
            "notes": (
                "Davidov and Kaufmann identify RloC as a conserved bacterial "
                "wobble nucleotide-excising, zinc-responsive tRNase related to "
                "PrrC (PMID:18681940 / DOI:10.1111/j.1365-2958.2008.06387.x)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:18681940 to "
            "DOI:10.1111/j.1365-2958.2008.06387.x so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 6 Stage 5 "
            "remediation of F-C6S4-DEF-SRC-011 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/rnlab_system.yaml": {
        "identifier": "traitmech:000367",
        "finding_id": "F-C6S4-DEF-SRC-012",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1534/genetics.110.121798",
        "replace_reference": "PMID:20980243",
        "evidence_entry": {
            "reference": "DOI:10.1534/genetics.110.121798",
            "snippet": (
                "RNase LS was originally identified as a potential antagonist "
                "of bacteriophage T4 infection. When T4 dmd is defective, RNase "
                "LS activity rapidly increases after T4 infection and cleaves "
                "T4 mRNAs to antagonize T4 reproduction."
            ),
            "notes": (
                "Koga et al. frame RnlA-dependent RNase LS activity as a "
                "potential antagonist of bacteriophage T4 dmd mutants "
                "(PMID:20980243 / DOI:10.1534/genetics.110.121798)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:20980243 to "
            "DOI:10.1534/genetics.110.121798 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while preserving "
            "the PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-012 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/tagi_system.yaml": {
        "identifier": "traitmech:000513",
        "finding_id": "F-C6S4-DEF-SRC-013",
        "timestamp": CYCLE6_TIMESTAMP,
        "definition_source": "DOI:10.1093/nar/gky781",
        "replace_reference": "PMID:30202937",
        "evidence_entry": {
            "reference": "DOI:10.1093/nar/gky781",
            "snippet": (
                "TagI belongs to the recently characterized SRA-HNH family of "
                "modification-dependent restriction endonucleases (REases) that "
                "also includes ScoA3IV (Sco5333) and TbiR51I (Tbis1)."
            ),
            "notes": (
                "Kisiala et al. support TagI as a member of an SRA-HNH "
                "modification-dependent restriction endonuclease family "
                "(PMID:30202937 / DOI:10.1093/nar/gky781)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:30202937 to "
            "DOI:10.1093/nar/gky781 so definition_source has an exact matching "
            "snippet-backed record-level evidence item while preserving the "
            "PubMed cross-reference in notes (Cycle 6 Stage 5 remediation of "
            "F-C6S4-DEF-SRC-013 in group "
            "G-C6S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abia_system.yaml": {
        "identifier": "traitmech:000344",
        "finding_id": "F-C7S4-DEF-SRC-001",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1128/aem.60.4.1129-1136.1994",
        "replace_reference": "PMID:16349225",
        "evidence_entry": {
            "reference": "DOI:10.1128/aem.60.4.1129-1136.1994",
            "snippet": (
                "The abiA gene (formerly hsp) encodes an abortive phage "
                "infection mechanism which inhibits phage DNA replication."
            ),
            "notes": (
                "Dinsmore and Klaenhammer describe abiA as the former hsp "
                "abortive-infection determinant and connect AbiA activity to "
                "inhibition of phage DNA replication "
                "(PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:16349225 to "
            "DOI:10.1128/aem.60.4.1129-1136.1994 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-001 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abib_system.yaml": {
        "identifier": "traitmech:000319",
        "finding_id": "F-C7S4-DEF-SRC-002",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1046/j.1365-2958.1996.371896.x",
        "replace_reference": "PMID:8825768",
        "evidence_entry": {
            "reference": "DOI:10.1046/j.1365-2958.1996.371896.x",
            "snippet": (
                "The abortive infection determinant AbiB prevents growth of "
                "the sensitive phage bIL170, but not of the resistant phage "
                "bIL41, on Lactococcus lactis strain IL1403"
            ),
            "notes": (
                "Parreira et al. place AbiB in the abortive-infection class "
                "and show that it blocks the sensitive lactococcal phage "
                "bIL170 on Lactococcus lactis IL1403 "
                "(PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:8825768 to "
            "DOI:10.1046/j.1365-2958.1996.371896.x so definition_source has "
            "an exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-002 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abic_system.yaml": {
        "identifier": "traitmech:000320",
        "finding_id": "F-C7S4-DEF-SRC-003",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1128/jb.174.22.7463-7469.1992",
        "replace_reference": "PMID:1429469",
        "evidence_entry": {
            "reference": "DOI:10.1128/jb.174.22.7463-7469.1992",
            "snippet": (
                "The genetic determinant for Prf (phage resistance five) was "
                "subcloned from the conjugative plasmid pTN20"
            ),
            "notes": (
                "Durmaz et al. subcloned the Prf determinant from the "
                "Lactococcus lactis ME2 conjugative plasmid pTN20 "
                "(PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:1429469 to "
            "DOI:10.1128/jb.174.22.7463-7469.1992 so definition_source has "
            "an exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-003 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abid_system.yaml": {
        "identifier": "traitmech:000318",
        "finding_id": "F-C7S4-DEF-SRC-004",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1128/aem.61.5.2023-2026.1995",
        "replace_reference": "PMID:7646042",
        "evidence_entry": {
            "reference": "DOI:10.1128/aem.61.5.2023-2026.1995",
            "snippet": (
                "A 6.3-kb fragment from pBF61 in Lactococcus lactis subsp. "
                "lactis KR5 was cloned and found to confer an abortive phage "
                "infection (Abi+) phenotype"
            ),
            "notes": (
                "McLandsborough et al. cloned the pBF61-derived fragment from "
                "Lactococcus lactis subsp. lactis KR5 and showed that it "
                "conferred an Abi phenotype "
                "(PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:7646042 to "
            "DOI:10.1128/aem.61.5.2023-2026.1995 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-004 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abii_system.yaml": {
        "identifier": "traitmech:000316",
        "finding_id": "F-C7S4-DEF-SRC-005",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1016/S0168-1656(97)01692-1",
        "replace_reference": "PMID:9195753",
        "evidence_entry": {
            "reference": "DOI:10.1016/S0168-1656(97)01692-1",
            "snippet": (
                "Plasmid pND852 (56 kb) encodes nisin resistance and was "
                "isolated from Lactococcus lactis ssp lactis (L. lactis) M138 "
                "by conjugation to L. lactis LM0230"
            ),
            "notes": (
                "Su et al. identified plasmid pND852 from Lactococcus lactis "
                "M138 as the source of the abiI-associated phage resistance "
                "locus (PMID:9195753 / DOI:10.1016/S0168-1656(97)01692-1)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:9195753 to "
            "DOI:10.1016/S0168-1656(97)01692-1 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-005 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abir_system.yaml": {
        "identifier": "traitmech:000317",
        "finding_id": "F-C7S4-DEF-SRC-006",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.66.6.2647-2651.2000",
        "replace_reference": "PMID:10831451",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.66.6.2647-2651.2000",
            "snippet": (
                "The native lactococcal plasmid pKR223 encodes two distinct "
                "phage resistance mechanisms, a restriction and modification "
                "(R/M) system designated LlaKR2I and an abortive infection "
                "mechanism (Abi) which affects prolate-headed-phage proliferation"
            ),
            "notes": (
                "Twomey et al. identify native Lactococcus lactis plasmid "
                "pKR223 as the source of a restriction-modification system "
                "and a separate abortive-infection determinant "
                "(PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:10831451 to "
            "DOI:10.1128/AEM.66.6.2647-2651.2000 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-006 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/abiu_system.yaml": {
        "identifier": "traitmech:000321",
        "finding_id": "F-C7S4-DEF-SRC-007",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.67.11.5225-5232.2001",
        "replace_reference": "PMID:11679349",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.67.11.5225-5232.2001",
            "snippet": (
                "This study reports on the identification and "
                "characterization of a novel abortive infection system, "
                "AbiU, from Lactococcus lactis."
            ),
            "notes": (
                "Dai et al. identify AbiU as a novel Lactococcus lactis "
                "abortive-infection system "
                "(PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:11679349 to "
            "DOI:10.1128/AEM.67.11.5225-5232.2001 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed cross-reference in notes (Cycle 7 Stage 5 "
            "remediation of F-C7S4-DEF-SRC-007 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/lit_system.yaml": {
        "identifier": "traitmech:000363",
        "finding_id": "F-C7S4-DEF-SRC-008",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1021/bi0495026",
        "replace_reference": "PMID:15196039",
        "evidence_entry": {
            "reference": "DOI:10.1021/bi0495026",
            "snippet": (
                "Bacteriophage exclusion is a suicide response to viral "
                "infection. In strains of Escherichia coli K-12 infected with "
                "T4 phage this process is mediated by the host-encoded Lit "
                "peptidase. Lit is activated by a unique sequence in the "
                "major head protein of the T4 phage (the Gol sequence) which "
                "then cleaves site-specifically the host translation factor "
                "EF-Tu, ultimately leading to cell death."
            ),
            "notes": (
                "Copeland et al. support host Lit as a T4-activated "
                "bacteriophage-exclusion peptidase that cleaves EF-Tu and "
                "leads to cell death "
                "(PMID:15196039 / DOI:10.1021/bi0495026)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from PMID:15196039 to "
            "DOI:10.1021/bi0495026 so definition_source has an exact matching "
            "snippet-backed record-level evidence item while preserving the "
            "PubMed cross-reference in notes (Cycle 7 Stage 5 remediation of "
            "F-C7S4-DEF-SRC-008 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/card_nlr_endonuclease_system.yaml": {
        "identifier": "traitmech:000550",
        "finding_id": "F-C7S4-DEF-SRC-009",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1101/2023.05.28.542683",
        "replace_reference": "https://europepmc.org/article/PPR/PPR668921",
        "evidence_entry": {
            "reference": "DOI:10.1101/2023.05.28.542683",
            "snippet": (
                "Here we show that CARD-like domains are present in defense "
                "systems that protect bacteria against phage."
            ),
            "notes": (
                "Wein et al. support bacterial CARD-like domains as parts of "
                "anti-phage defense systems "
                "(https://europepmc.org/article/PPR/PPR668921 / "
                "DOI:10.1101/2023.05.28.542683)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://europepmc.org/article/PPR/PPR668921 to "
            "DOI:10.1101/2023.05.28.542683 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while "
            "preserving the EuropePMC preprint cross-reference in notes "
            "(Cycle 7 Stage 5 remediation of F-C7S4-DEF-SRC-009 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/card_nlr_gasdermin_system.yaml": {
        "identifier": "traitmech:000555",
        "finding_id": "F-C7S4-DEF-SRC-010",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1101/2023.05.28.542683",
        "replace_reference": "https://europepmc.org/article/PPR/PPR668921",
        "evidence_entry": {
            "reference": "DOI:10.1101/2023.05.28.542683",
            "snippet": (
                "Here we show that CARD-like domains are present in defense "
                "systems that protect bacteria against phage."
            ),
            "notes": (
                "Wein et al. support bacterial CARD-like domains as parts of "
                "anti-phage defense systems "
                "(https://europepmc.org/article/PPR/PPR668921 / "
                "DOI:10.1101/2023.05.28.542683)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://europepmc.org/article/PPR/PPR668921 to "
            "DOI:10.1101/2023.05.28.542683 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while "
            "preserving the EuropePMC preprint cross-reference in notes "
            "(Cycle 7 Stage 5 remediation of F-C7S4-DEF-SRC-010 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/card_nlr_phospho_system.yaml": {
        "identifier": "traitmech:000551",
        "finding_id": "F-C7S4-DEF-SRC-011",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1101/2023.05.28.542683",
        "replace_reference": "https://europepmc.org/article/PPR/PPR668921",
        "evidence_entry": {
            "reference": "DOI:10.1101/2023.05.28.542683",
            "snippet": (
                "Here we show that CARD-like domains are present in defense "
                "systems that protect bacteria against phage."
            ),
            "notes": (
                "Wein et al. support bacterial CARD-like domains as parts of "
                "anti-phage defense systems "
                "(https://europepmc.org/article/PPR/PPR668921 / "
                "DOI:10.1101/2023.05.28.542683)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://europepmc.org/article/PPR/PPR668921 to "
            "DOI:10.1101/2023.05.28.542683 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while "
            "preserving the EuropePMC preprint cross-reference in notes "
            "(Cycle 7 Stage 5 remediation of F-C7S4-DEF-SRC-011 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/card_nlr_subtilase_system.yaml": {
        "identifier": "traitmech:000553",
        "finding_id": "F-C7S4-DEF-SRC-012",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1101/2023.05.28.542683",
        "replace_reference": "https://europepmc.org/article/PPR/PPR668921",
        "evidence_entry": {
            "reference": "DOI:10.1101/2023.05.28.542683",
            "snippet": (
                "Here we show that CARD-like domains are present in defense "
                "systems that protect bacteria against phage."
            ),
            "notes": (
                "Wein et al. support bacterial CARD-like domains as parts of "
                "anti-phage defense systems "
                "(https://europepmc.org/article/PPR/PPR668921 / "
                "DOI:10.1101/2023.05.28.542683)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://europepmc.org/article/PPR/PPR668921 to "
            "DOI:10.1101/2023.05.28.542683 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while "
            "preserving the EuropePMC preprint cross-reference in notes "
            "(Cycle 7 Stage 5 remediation of F-C7S4-DEF-SRC-012 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/card_nlr_system.yaml": {
        "identifier": "traitmech:000337",
        "finding_id": "F-C7S4-DEF-SRC-013",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1101/2023.05.28.542683",
        "replace_reference": "https://europepmc.org/article/PPR/PPR668921",
        "evidence_entry": {
            "reference": "DOI:10.1101/2023.05.28.542683",
            "snippet": (
                "Here we show that CARD-like domains are present in defense "
                "systems that protect bacteria against phage."
            ),
            "notes": (
                "The Wein et al. abstract supports CARD-like-domain systems "
                "as bacterial phage-defense systems "
                "(https://europepmc.org/article/PPR/PPR668921 / "
                "DOI:10.1101/2023.05.28.542683)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://europepmc.org/article/PPR/PPR668921 to "
            "DOI:10.1101/2023.05.28.542683 so definition_source has an exact "
            "matching snippet-backed record-level evidence item while "
            "preserving the EuropePMC preprint cross-reference in notes "
            "(Cycle 7 Stage 5 remediation of F-C7S4-DEF-SRC-013 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/nlr_like_bnacht_system.yaml": {
        "identifier": "traitmech:000408",
        "finding_id": "F-C7S4-DEF-SRC-014",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.cell.2023.04.015",
        "replace_reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.cell.2023.04.015",
            "snippet": (
                "Here we show that proteins containing a NACHT module, the "
                "central feature of the animal nucleotide-binding domain and "
                "leucine-rich repeat-containing gene family (NLRs), are found "
                "in bacteria and defend against phages."
            ),
            "notes": (
                "Kibby et al. support NACHT-module proteins as bacterial "
                "NLR-related proteins that defend against phages "
                "(https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ / "
                "DOI:10.1016/j.cell.2023.04.015)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ to "
            "DOI:10.1016/j.cell.2023.04.015 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed Central cross-reference in notes (Cycle 7 "
            "Stage 5 remediation of F-C7S4-DEF-SRC-014 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/genomics/pd_t2_1_system.yaml": {
        "identifier": "traitmech:000476",
        "finding_id": "F-C7S4-DEF-SRC-015",
        "timestamp": CYCLE7_TIMESTAMP,
        "definition_source": "DOI:10.1038/s41564-025-02239-6",
        "replace_reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/",
        "evidence_entry": {
            "reference": "DOI:10.1038/s41564-025-02239-6",
            "snippet": (
                "Two phage proteins were further investigated, revealing T7 "
                "gp17 and additional tail fiber proteins activated the "
                "undescribed antiphage system PD-T2\u20131 and identifying "
                "\u03bb gpE major capsid protein activated the antiphage "
                "system Avs8."
            ),
            "notes": (
                "Goedecke et al. report that T7 gp17 and additional tail "
                "fiber proteins activated the previously undescribed PD-T2-1 "
                "antiphage system "
                "(https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ / "
                "DOI:10.1038/s41564-025-02239-6)."
            ),
        },
        "changes": (
            "Aligned record-level evidence[0].reference from "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ to "
            "DOI:10.1038/s41564-025-02239-6 so definition_source has an "
            "exact matching snippet-backed record-level evidence item while "
            "preserving the PubMed Central cross-reference in notes (Cycle 7 "
            "Stage 5 remediation of F-C7S4-DEF-SRC-015 in group "
            "G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    # Cycle 8 Stage 5 remediation (#2002): 12 open findings from Cycle 8 Stage 4
    "data/traits/ecology/biofilm_formation.yaml": {
        "identifier": "traitmech:000053",
        "finding_id": "F-C8S4-DEF-SRC-001",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro.2016.94",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro.2016.94",
            "snippet": (
                "Bacterial biofilms are formed by communities that are embedded "
                "in a self-produced matrix of extracellular polymeric substances (EPS)."
            ),
            "notes": (
                "Flemming et al. describe matrix-enclosed, surface-associated "
                "communities (biofilms) as an emergent, distinct mode of bacterial life."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro.2016.94 "
            "(Flemming et al. 2016, already present on "
            "causal_graphs[0].edges[5].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-001 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/commensalism.yaml": {
        "identifier": "traitmech:000042",
        "finding_id": "F-C8S4-DEF-SRC-002",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/s41579-021-00550-7",
        "evidence_entry": {
            "reference": "DOI:10.1038/s41579-021-00550-7",
            "snippet": (
                "Symbiotic interactions can be neutral, harmful or have beneficial "
                "effects on the host organism. However, growing evidence suggests "
                "that microbial symbionts can evolve rapidly, resulting in drastic "
                "transitions along the parasite-mutualist continuum."
            ),
            "notes": (
                "Drew et al. place commensalism on the parasite-mutualist "
                "continuum as a near-neutral host interaction."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/s41579-021-00550-7 "
            "(Drew et al. 2021, already present on "
            "causal_graphs[0].edges[11].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-002 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/endosymbiosis.yaml": {
        "identifier": "traitmech:000045",
        "finding_id": "F-C8S4-DEF-SRC-003",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro2670",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro2670",
            "snippet": (
                "Since 2006, numerous cases of bacterial symbionts with "
                "extraordinarily small genomes have been reported. These "
                "organisms represent independent lineages from diverse bacterial "
                "groups. They have diminutive gene sets that rival some "
                "mitochondria and chloroplasts in terms of gene numbers and lack "
                "genes that are considered to be essential in other bacteria."
            ),
            "notes": (
                'McCutcheon & Moran, "Extreme genome reduction in symbiotic '
                'bacteria", characterize intracellular endosymbionts and their '
                "diminished genomes."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro2670 "
            "(McCutcheon & Moran 2011, already present on "
            "causal_graphs[0].edges[0].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-003 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/gut_associated.yaml": {
        "identifier": "traitmech:000052",
        "finding_id": "F-C8S4-DEF-SRC-004",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1126/science.1104816",
        "evidence_entry": {
            "reference": "DOI:10.1126/science.1104816",
            "snippet": (
                "The distal human intestine represents an anaerobic bioreactor "
                "programmed with an enormous population of bacteria, dominated by "
                "relatively few divisions that are highly diverse at the "
                "strain/subspecies level. This microbiota and its collective "
                "genomes (microbiome) provide us with genetic and metabolic "
                "attributes we have not been required to evolve on our own, "
                "including the ability to harvest otherwise inaccessible nutrients."
            ),
            "notes": (
                "B\u00e4ckhed et al. characterize the distal intestine as a dense "
                "microbial habitat whose residents provide metabolic capabilities "
                "to the host."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1126/science.1104816 "
            "(B\u00e4ckhed et al. 2005, already present on "
            "causal_graphs[0].edges[8].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-004 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/host_associated.yaml": {
        "identifier": "traitmech:000049",
        "finding_id": "F-C8S4-DEF-SRC-005",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1073/pnas.1218525110",
        "evidence_entry": {
            "reference": "DOI:10.1073/pnas.1218525110",
            "snippet": (
                "This review examines how a growing knowledge of the vast range "
                "of animal-bacterial interactions, whether in shared ecosystems "
                "or intimate symbioses, is fundamentally altering our "
                "understanding of animal biology."
            ),
            "notes": (
                "McFall-Ngai et al. document the ubiquity of host-associated "
                "microbial communities across the animal kingdom."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1073/pnas.1218525110 "
            "(McFall-Ngai et al. 2013, already present on "
            "causal_graphs[0].edges[0].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-005 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/mutualism.yaml": {
        "identifier": "traitmech:000041",
        "finding_id": "F-C8S4-DEF-SRC-006",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1073/pnas.1218525110",
        "evidence_entry": {
            "reference": "DOI:10.1073/pnas.1218525110",
            "snippet": (
                "This review examines how a growing knowledge of the vast range "
                "of animal-bacterial interactions, whether in shared ecosystems "
                "or intimate symbioses, is fundamentally altering our "
                "understanding of animal biology."
            ),
            "notes": (
                "McFall-Ngai et al. document widespread mutually beneficial "
                "host-microbe associations across animals."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1073/pnas.1218525110 "
            "(McFall-Ngai et al. 2013, already present on "
            "causal_graphs[0].edges[5].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-006 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/nitrogen_fixing_symbiosis.yaml": {
        "identifier": "traitmech:000044",
        "finding_id": "F-C8S4-DEF-SRC-007",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro.2017.171",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro.2017.171",
            "snippet": (
                "Rhizobia are some of the best-studied plant microbiota. These "
                "oligotrophic Alphaproteobacteria or Betaproteobacteria form "
                "symbioses with their legume hosts."
            ),
            "notes": (
                "Poole et al. describe the free-living-to-endosymbiont transition "
                "of rhizobia that forms N2-fixing legume root nodules."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro.2017.171 "
            "(Poole et al. 2018, already present on "
            "causal_graphs[0].edges[10].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-007 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/opportunistic_pathogen.yaml": {
        "identifier": "traitmech:000046",
        "finding_id": "F-C8S4-DEF-SRC-008",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.tim.2012.04.005",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.tim.2012.04.005",
            "snippet": (
                "An increasing number of studies now demonstrate that many "
                "opportunistic pathogens (OPs) do not conform to these "
                "assumptions, with virulence factors maintained instead because "
                "of advantages in non-parasitic contexts."
            ),
            "notes": (
                'Brown, Cornforth & Mideo, "Evolution of virulence in '
                'opportunistic pathogens", support context-dependent virulence '
                "maintained by advantages outside the host."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.tim.2012.04.005 "
            "(Brown, Cornforth & Mideo 2012, already present on "
            "causal_graphs[0].edges[6].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-008 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/parasitism.yaml": {
        "identifier": "traitmech:000043",
        "finding_id": "F-C8S4-DEF-SRC-009",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/s41579-021-00550-7",
        "evidence_entry": {
            "reference": "DOI:10.1038/s41579-021-00550-7",
            "snippet": (
                "Symbiotic interactions can be neutral, harmful or have beneficial "
                "effects on the host organism. However, growing evidence suggests "
                "that microbial symbionts can evolve rapidly, resulting in drastic "
                "transitions along the parasite-mutualist continuum."
            ),
            "notes": (
                "Drew et al. define parasitism as the harmful pole of the "
                "parasite-mutualist continuum and describe evolutionary "
                "transitions along it."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/s41579-021-00550-7 "
            "(Drew et al. 2021, already present on "
            "causal_graphs[0].edges[10].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-009 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/predatory_bacterium.yaml": {
        "identifier": "traitmech:000054",
        "finding_id": "F-C8S4-DEF-SRC-010",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1146/annurev.micro.091208.073346",
        "evidence_entry": {
            "reference": "DOI:10.1146/annurev.micro.091208.073346",
            "snippet": (
                "Bdellovibrio species are naturally predatory, small, motile, "
                "Deltaproteobacteria that invade the periplasm of other larger "
                "gram-negative bacteria, killing and digesting them."
            ),
            "notes": (
                'Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", '
                "describes invasion, killing, and digestion of prey bacteria as "
                "a predatory lifestyle."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from "
            "DOI:10.1146/annurev.micro.091208.073346 (Sockett 2009, already "
            "present on causal_graphs[0].edges[8].evidence[0]) to record-level "
            "evidence[0] to match definition_source (Cycle 8 Stage 5 remediation "
            "of F-C8S4-DEF-SRC-010 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/rhizosphere_association.yaml": {
        "identifier": "traitmech:000051",
        "finding_id": "F-C8S4-DEF-SRC-011",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1038/nrmicro3109",
        "evidence_entry": {
            "reference": "DOI:10.1038/nrmicro3109",
            "snippet": (
                "The rhizosphere is the interface between plant roots and soil "
                "where interactions among a myriad of microorganisms and "
                "invertebrates affect biogeochemical cycling, plant growth and "
                "tolerance to biotic and abiotic stress."
            ),
            "notes": (
                'Philippot et al., "Going back to the roots", define the '
                "rhizosphere as a distinct, root-influenced microbial habitat."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1038/nrmicro3109 "
            "(Philippot et al. 2013, already present on "
            "causal_graphs[0].edges[0].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-011 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
    "data/traits/ecology/symbiosis.yaml": {
        "identifier": "traitmech:000040",
        "finding_id": "F-C8S4-DEF-SRC-012",
        "timestamp": CYCLE8_TIMESTAMP,
        "definition_source": "DOI:10.1073/pnas.1218525110",
        "evidence_entry": {
            "reference": "DOI:10.1073/pnas.1218525110",
            "snippet": (
                "This review examines how a growing knowledge of the vast range "
                "of animal-bacterial interactions, whether in shared ecosystems "
                "or intimate symbioses, is fundamentally altering our "
                "understanding of animal biology."
            ),
            "notes": (
                'McFall-Ngai et al., "Animals in a bacterial world", supports '
                "persistent host-microbe association (symbiosis) as a pervasive "
                "microbial lifestyle; parent of the "
                "mutualism/commensalism/parasitism sub-variants."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1073/pnas.1218525110 "
            "(McFall-Ngai et al. 2013, already present on "
            "causal_graphs[0].edges[0].evidence[0]) to record-level evidence[0] "
            "to match definition_source (Cycle 8 Stage 5 remediation of "
            "F-C8S4-DEF-SRC-012 in group "
            "G-C8S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #2002)."
        ),
    },
}


def load_do_not_work(path: Path = DO_NOT_WORK_PATH) -> set[str]:
    """Return relative paths listed in DO_NOT_WORK.md."""
    excluded: set[str] = set()
    if not path.exists():
        return excluded
    for line in path.read_text(encoding="utf-8").splitlines():
        if "data/traits/" in line:
            for token in line.replace("`", " ").split():
                if token.startswith("data/traits/") and token.endswith(".yaml"):
                    excluded.add(token)
    return excluded


def apply_remediation_to_doc(doc: dict[str, Any], spec: dict[str, Any]) -> bool:
    """Ensure the specified definition_source evidence entry is present on doc."""
    if doc.get("identifier") != spec["identifier"]:
        raise ValueError(f"Identifier mismatch: {doc.get('identifier')} != {spec['identifier']}")
    if doc.get("definition_source") != spec["definition_source"]:
        raise ValueError(
            f"definition_source mismatch on {spec['identifier']}: "
            f"{doc.get('definition_source')} != {spec['definition_source']}"
        )

    evidence_list = list(doc.get("evidence") or [])
    target_ref = spec["evidence_entry"]["reference"]
    desired_entry = copy.deepcopy(spec["evidence_entry"])
    event_timestamp = str(spec.get("timestamp", TIMESTAMP))

    changed = False
    existing_idx = next(
        (i for i, item in enumerate(evidence_list) if item.get("reference") == target_ref),
        None,
    )
    if existing_idx is None and spec.get("replace_reference"):
        replace_ref = spec["replace_reference"]
        existing_idx = next(
            (i for i, item in enumerate(evidence_list) if item.get("reference") == replace_ref),
            None,
        )
    if existing_idx is None:
        evidence_list.append(desired_entry)
        doc["evidence"] = evidence_list
        changed = True
    elif evidence_list[existing_idx] != desired_entry:
        evidence_list[existing_idx] = desired_entry
        doc["evidence"] = evidence_list
        changed = True

    existing_events = [
        ev
        for ev in (doc.get("curation_history") or [])
        if ev.get("timestamp") == event_timestamp and ev.get("curator") == CURATOR
    ]
    if not existing_events or existing_events[-1].get("changes") != spec["changes"]:
        changed = True

    if changed:
        record_curation_event(
            doc,
            curator=CURATOR,
            action=ACTION,
            changes=spec["changes"],
            llm_assisted=True,
            timestamp=event_timestamp,
            upsert=True,
        )

    return changed


def process_all(
    repo_root: Path = REPO_ROOT,
    *,
    apply: bool = False,
) -> tuple[int, int]:
    """Process all 92 Stage 5 remediation targets. Returns (findings_resolved, files_updated)."""
    excluded = load_do_not_work(repo_root / "DO_NOT_WORK.md")
    findings_resolved = 0
    files_updated = 0

    for rel_path, spec in sorted(REMEDIATION_SPECS.items()):
        if rel_path in excluded:
            raise ValueError(f"Refusing to touch DO_NOT_WORK.md excluded file: {rel_path}")
        path = repo_root / rel_path
        if not path.is_file():
            raise FileNotFoundError(f"Missing target file: {path}")
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        changed = apply_remediation_to_doc(doc, spec)
        findings_resolved += 1
        if changed:
            errors = validate_trait(doc)
            if errors:
                raise ValidationFailedError(path, errors)
            if apply:
                write_validated_trait(doc, path)
            files_updated += 1

    return findings_resolved, files_updated


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to data/traits/ via write_validated_trait (default: dry-run).",
    )
    args = parser.parse_args(argv)
    resolved, updated = process_all(apply=args.apply)
    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"[{mode}] Stage 4 open findings resolved: {resolved}; files updated: {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
