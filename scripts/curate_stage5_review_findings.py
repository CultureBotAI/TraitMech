#!/usr/bin/env python3
"""Curate Stage 5 grouped review remediation (Cycle 1 #1981, Cycle 2 #1995, Cycle 3 #2002).

Resolves the 4 actionable open findings from the Cycle 1 Stage 4 corpus-wide
record and cohort review (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1981), the 6 actionable open findings from the
Cycle 2 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1995), and the 17 actionable open findings from the
Cycle 3 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #2002):
- `F-DEF-SRC-CYANOPHYCIN-001`..`004` (Cycle 1 #1981, 4 records)
- `F-DEF-SRC-CARBON-FIXATION-010`..`015` (Cycle 2 #1995, 6 records)
- `F-C3S4-DEF-SRC-001`..`017` (Cycle 3 #2002, 17 records)

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
    """Process all 27 Stage 5 remediation targets. Returns (findings_resolved, files_updated)."""
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
