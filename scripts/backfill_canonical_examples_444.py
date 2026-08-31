#!/usr/bin/env python3
"""Resolve the 89-record canonical-example queue after the #591 policy decision.

The source ledger below is deliberately data, not an inference engine.  Each entry
is a natural organism phenotype reported by the cited primary paper (or, for the
BSL records, by the named public-health authority).  Quantitative notes retain the
reported strain, interval/value, units, and assay context available in the source.

Four records remain empty on purpose:

* ``biosafety_level_5`` is hypothetical and therefore has no real taxon instance;
* ``temperature_delta_very_low`` and ``temperature_delta_low`` have no retrieved
  natural-organism paper establishing both growth endpoints inside the exact bin;
* ``ph_range_high`` has no retrieved complete growth interval contained in its bin.

Their review is written into ``curation_history`` so the absence is an explicit
evidence disposition, not an overlooked queue item.  No paid-research provider is
used by this script or by the source review that produced the ledger.

Usage:
    python scripts/backfill_canonical_examples_444.py          # dry run
    python scripts/backfill_canonical_examples_444.py --apply  # write
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from trait_priority import build_queue  # noqa: E402
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-31T04:43:24Z"
CURATOR = "codex"
ADD_ACTION = "ADD_CANONICAL_EXAMPLES"
DEFER_ACTION = "REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP"


def source(taxon_id: str, taxon_label: str, reference: str) -> dict[str, str]:
    return {
        "taxon_id": taxon_id,
        "taxon_label": taxon_label,
        "reference": reference,
    }


SOURCES = {
    "aestuariibius": source(
        "NCBITaxon:3234132", "Aestuariibius violaceus", "DOI:10.1099/ijsem.0.006834"
    ),
    "amycolatopsis": source(
        "NCBITaxon:486505", "Amycolatopsis flava", "DOI:10.1007/s10482-015-0542-z"
    ),
    "aureivirga": source(
        "NCBITaxon:1182451", "Aureivirga marina", "DOI:10.1099/ijs.0.043257-0"
    ),
    "clostridium_psychrophilum": source(
        "NCBITaxon:132926",
        "Clostridium psychrophilum",
        "DOI:10.1016/j.bbalip.2013.02.004",
    ),
    "colwellia": source(
        "NCBITaxon:1513592",
        "Colwellia marinimaniae",
        "DOI:10.1099/ijsem.0.001671",
    ),
    "corynebacterium_diphtheriae": source(
        "NCBITaxon:1717",
        "Corynebacterium diphtheriae",
        "DOI:10.1111/j.1574-6976.2011.00298.x",
    ),
    "corynebacterium_glutamicum": source(
        "NCBITaxon:1718",
        "Corynebacterium glutamicum",
        "DOI:10.1111/j.1574-6976.2011.00298.x",
    ),
    "bacillus_nakamurai": source(
        "NCBITaxon:1793963", "Bacillus nakamurai", "DOI:10.1099/ijsem.0.001135"
    ),
    "ecoli": source("NCBITaxon:562", "Escherichia coli", "PMID:9278503"),
    "ecoli_adder": source(
        "NCBITaxon:562", "Escherichia coli", "DOI:10.1016/j.cell.2014.11.022"
    ),
    "ecoli_bsl": source(
        "NCBITaxon:562", "Escherichia coli", "PMID:21208457"
    ),
    "ecoli_halophily": source(
        "NCBITaxon:562", "Escherichia coli", "PMC8415458"
    ),
    "ecoli_oxygen": source(
        "NCBITaxon:562", "Escherichia coli", "DOI:10.1111/1751-7915.70051"
    ),
    "ecoli_ph": source(
        "NCBITaxon:83333", "Escherichia coli K-12", "DOI:10.1371/journal.pone.0018960"
    ),
    "ecoli_shape": source(
        "NCBITaxon:562", "Escherichia coli", "DOI:10.1038/nrmicro1205"
    ),
    "ecoli_thermal": source(
        "NCBITaxon:83333", "Escherichia coli K-12", "DOI:10.1128/AEM.05773-11"
    ),
    "ebola": source(
        "NCBITaxon:186538",
        "Zaire ebolavirus",
        "https://www.canada.ca/en/public-health/services/laboratory-biosafety-biosecurity/pathogen-safety-data-sheets-risk-assessment/ebolavirus.html",
    ),
    "evansella": source(
        "NCBITaxon:2069301", "Evansella tamaricis", "DOI:10.1099/ijsem.0.002543"
    ),
    "flavicella": source(
        "NCBITaxon:2585141", "Flavicella sediminum", "DOI:10.1099/ijsem.0.003839"
    ),
    "fundidesulfovibrio": source(
        "NCBITaxon:2922866",
        "Fundidesulfovibrio terrae",
        "DOI:10.1099/ijsem.0.005880",
    ),
    "gemmobacter": source(
        "NCBITaxon:2306023", "Gemmobacter lutimaris", "DOI:10.1099/ijsem.0.003375"
    ),
    "halomonas": source("NCBITaxon:2746", "Halomonas elongata", "PMID:20849449"),
    "kushneria": source(
        "NCBITaxon:504092", "Kushneria aurantia", "DOI:10.1099/ijs.0.001461-0"
    ),
    "lederbergia": source(
        "NCBITaxon:735518", "Lederbergia graminis", "DOI:10.1099/ijs.0.023820-0"
    ),
    "marinobacterium": source(
        "NCBITaxon:1232683",
        "Marinobacterium lacunae",
        "DOI:10.1007/s00203-023-03627-4",
    ),
    "microbaculum": source(
        "NCBITaxon:3447298", "Microbaculum mangrovi", "DOI:10.1099/ijsem.0.006972"
    ),
    "mucor": source(
        "NCBITaxon:36080", "Mucor circinelloides", "DOI:10.1016/j.heliyon.2024.e30812"
    ),
    "mycoplasmoides": source(
        "NCBITaxon:243273",
        "Mycoplasmoides genitalium G37",
        "DOI:10.1126/science.270.5235.397",
    ),
    "mycobacterium_h37rv": source(
        "NCBITaxon:83332",
        "Mycobacterium tuberculosis H37Rv",
        "DOI:10.1038/31159",
    ),
    "nakamurella": source(
        "NCBITaxon:1656892", "Nakamurella aerolata", "DOI:10.1007/s00284-020-02274-y"
    ),
    "natranaerobius": source(
        "NCBITaxon:375929",
        "Natranaerobius thermophilus",
        "DOI:10.1128/aem.00145-24",
    ),
    "oceanimonas": source(
        "NCBITaxon:3028314", "Oceanimonas pelagia", "DOI:10.1007/s10482-024-01948-y"
    ),
    "paludibaculum": source(
        "NCBITaxon:1473598",
        "Paludibaculum fermentans",
        "DOI:10.1099/ijs.0.066175-0",
    ),
    "paracoccus_mangrovi": source(
        "NCBITaxon:1715645", "Paracoccus mangrovi", "DOI:10.1099/ijsem.0.001993"
    ),
    "paraliobacillus": source(
        "NCBITaxon:200904", "Paraliobacillus ryukyuensis", "DOI:10.2323/jgam.48.269"
    ),
    "pelagibacter": source(
        "NCBITaxon:335992",
        "Candidatus Pelagibacter ubique HTCC1062",
        "PMID:16109880",
    ),
    "peribacillus": source(
        "NCBITaxon:718002", "Peribacillus endoradicis", "DOI:10.1099/ijs.0.028936-0"
    ),
    "picrophilus": source(
        "NCBITaxon:46632", "Picrophilus oshimae", "DOI:10.1007/s007920050044"
    ),
    "pontibacterium": source(
        "NCBITaxon:2781979", "Pontibacterium sinense", "DOI:10.1099/ijsem.0.006018"
    ),
    "pseudomonas_mangiferae": source(
        "NCBITaxon:2593654",
        "Pseudomonas mangiferae",
        "DOI:10.1099/ijsem.0.003657",
    ),
    "psychrobacter": source(
        "NCBITaxon:334543", "Psychrobacter arcticus", "DOI:10.1128/JB.01377-08"
    ),
    "psychromonas": source(
        "NCBITaxon:357794", "Psychromonas ingrahamii", "DOI:10.1099/ijs.0.64068-0"
    ),
    "rubellicoccus": source(
        "NCBITaxon:3080537",
        "Rubellicoccus peritrichatus",
        "DOI:10.1099/ijsem.0.006325",
    ),
    "ruixingdingia": source(
        "NCBITaxon:3073604", "Ruixingdingia sedimenti", "DOI:10.1099/ijsem.0.006350"
    ),
    "seongchinamella": source(
        "NCBITaxon:2547392",
        "Seongchinamella unica",
        "DOI:10.1099/ijsem.0.003914",
    ),
    "solimonas": source(
        "NCBITaxon:2086571", "Solimonas fluminis", "DOI:10.1099/ijsem.0.002865"
    ),
    "sphingomonas": source(
        "NCBITaxon:575322",
        "Sphingomonas oligoaromativorans",
        "DOI:10.1099/ijs.0.052894-0",
    ),
    "spirochaeta": source(
        "NCBITaxon:324679",
        "Spirochaeta dissipatitropha",
        "DOI:10.1099/ijs.0.65862-0",
    ),
    "spongorhabdus": source(
        "NCBITaxon:2995321",
        "Spongorhabdus nitratireducens",
        "DOI:10.1099/ijsem.0.007037",
    ),
    "streptomyces_coelicolor": source(
        "NCBITaxon:100226",
        "Streptomyces coelicolor A3(2)",
        "DOI:10.1038/417141a",
    ),
    "synechocystis": source(
        "NCBITaxon:1148", "Synechocystis sp. PCC 6803", "DOI:10.3390/md11082894"
    ),
    "thermoanaerobacter": source(
        "NCBITaxon:2325",
        "Thermoanaerobacter kivui",
        "DOI:10.3389/fmicb.2023.1265216",
    ),
}


# path without .yaml -> [(source key, exact source-scoped note), ...]
TRANCHE: dict[str, list[tuple[str, str]]] = {
    # Ecology: examples are scoped to a concrete branch of each broad class.
    "ecology/biosafety_level": [
        (
            "ecoli_bsl",
            "Escherichia coli K-12 laboratory lineages are handled at BSL-1; this is a concrete low-hazard branch of the biosafety-level classification, not a claim that all E. coli strains share one level.",
        )
    ],
    "ecology/biosafety_level_4": [
        (
            "ebola",
            "Zaire ebolavirus is assigned to the highest existing containment category by the cited national pathogen-safety authority and is a concrete BSL-4 agent.",
        )
    ],
    "ecology/habitat_association": [
        (
            "pelagibacter",
            "Strain HTCC1062 was isolated from the Oregon coastal ocean and the genome paper characterizes its streamlined marine-plankton habitat association; this exemplifies the marine branch of the broad habitat class.",
        )
    ],
    # Generic environmental measurement classes.  These examples demonstrate the
    # measurement kind; their notes do not promote one axis as the whole class.
    "environment/delta_phenotype_with_numerical_limits": [
        (
            "psychrobacter",
            "Psychrobacter arcticus 273-4 grew from -10 to 28 degrees C in the reported experiments (38 degrees C nominal breadth); the example demonstrates an endpoint-derived delta while retaining the source's endpoint caveat.",
        )
    ],
    "environment/growth_range_phenotype_with_numerical_limits": [
        (
            "natranaerobius",
            "Natranaerobius thermophilus was reported across 3.1-4.9 M total sodium at pH 9.5 and 53 degrees C; this is a bounded growth range on a salinity axis, not an NaCl conversion or an optimum claim.",
        )
    ],
    "environment/optimum_phenotype_with_numerical_limits": [
        (
            "oceanimonas",
            "The type-strain description separately reports optima of 30 degrees C and pH 7-8 while retaining the associated growth ranges, directly exemplifying a measured best-growth value rather than tolerance at one condition.",
        )
    ],
    "environment/ph_phenotype_with_numerical_limits": [
        (
            "ecoli_ph",
            "E. coli K-12 W3110 growth was measured across buffered external pH conditions; TolC affected maximal exponential growth at pH 4.5-6.0 but not 6.5-8.5, exemplifying a quantitative pH-growth phenotype.",
        )
    ],
    "environment/salinity_phenotype_with_numerical_limits": [
        (
            "natranaerobius",
            "The source measures long-term growth and cellular responses across 2.5-4.3 M total sodium and reports a 3.1-4.9 M growth range; units and total-sodium identity are retained rather than converted to NaCl.",
        )
    ],
    "environment/temperature_phenotype_with_numerical_limits": [
        (
            "thermoanaerobacter",
            "The study reports a 39 degrees C lower growth boundary, ancestral 66 degrees C optimum, and evolved 60 degrees C optimum for Thermoanaerobacter kivui, directly separating cardinal temperature values.",
        )
    ],
    # NaCl optimum/range/delta families.
    "environment/nacl_optimum": [
        (
            "paraliobacillus",
            "Strain O15-7T had a maximum-specific-growth-rate optimum spanning 0.75-3.0% (w/v) NaCl. Because that interval touches the low/mid1 boundary, #591 keeps the complete claim on the parent rather than duplicating it onto a bin.",
        )
    ],
    "environment/nacl_optimum_low": [
        (
            "sphingomonas",
            "Type strain SY-6T grew optimally at 0.01% (w/v) NaCl, wholly within the at-most-1% bin; its full reported growth range was 0-0.5%.",
        )
    ],
    "environment/nacl_optimum_mid1": [
        (
            "flavicella",
            "Type strain ALS 84T had a measured NaCl optimum of 2% (w/v), wholly inside the approximately 1-3% bin; growth occurred at 1-3%.",
        )
    ],
    "environment/nacl_optimum_mid2": [
        (
            "lederbergia",
            "The type strain, published as Bacillus graminis YC6957T and now NCBI-labelled Lederbergia graminis, grew optimally at 4-5% (w/v) NaCl, wholly inside the 3-8% bin.",
        )
    ],
    "environment/nacl_range": [
        (
            "kushneria",
            "Kushneria aurantia A10T grew from 5 to 17.5% (w/v) NaCl. The complete interval crosses the mid2/high boundary, so #591 places this distinct claim on the range parent only.",
        )
    ],
    "environment/nacl_range_low": [
        (
            "sphingomonas",
            "Type strain SY-6T grew from 0 to 0.5% (w/v) NaCl, with a 0.01% optimum; the complete reported range lies below the approximately 1% upper bound.",
        )
    ],
    "environment/nacl_range_mid1": [
        (
            "spongorhabdus",
            "Spongorhabdus nitratireducens strains XeTr1T and StTr2 grew across the complete reported 1-3% (w/v) NaCl interval, matching this bin without extrapolation.",
        )
    ],
    "environment/nacl_range_mid2": [
        (
            "aureivirga",
            "Aureivirga marina strain VI.14 grew at 3-5% (w/v) NaCl; the complete reported interval lies within the approximately 3-8% bin.",
        )
    ],
    "environment/nacl_range_high": [
        (
            "amycolatopsis",
            "Amycolatopsis flava AFM 10111T grew from 1 to 30% NaCl; its measured growth range extends well above the approximately 8% threshold, as this record defines.",
        )
    ],
    "environment/nacl_delta": [
        (
            "lederbergia",
            "The type strain, published as Bacillus graminis YC6957T, grew at 0-8% (w/v) NaCl. Its 8-point breadth meets a bin boundary, so #591 keeps this claim on the delta parent.",
        )
    ],
    "environment/nacl_delta_low": [
        (
            "sphingomonas",
            "Sphingomonas oligoaromativorans SY-6T grew from 0 to 0.5% (w/v) NaCl, a directly reported 0.5-point breadth wholly within the at-most-1% delta bin.",
        )
    ],
    "environment/nacl_delta_mid1": [
        (
            "aureivirga",
            "Aureivirga marina strain VI.14 grew from 3 to 5% (w/v) NaCl, a 2-point breadth wholly inside the approximately 1-3% delta bin.",
        )
    ],
    "environment/nacl_delta_mid2": [
        (
            "peribacillus",
            "The type strain, published as Bacillus endoradicis CCBAU 05776T and now NCBI-labelled Peribacillus endoradicis, grew from 0 to 7% NaCl, a 7-point breadth inside the 3-8% delta bin.",
        )
    ],
    "environment/halophily_preference": [
        (
            "halomonas",
            "Halomonas elongata DSM 2581T is a source-backed moderate-halophile model; this exemplifies the halophilic branch of the broad salt-preference class.",
        ),
        (
            "ecoli_halophily",
            "Escherichia coli is a non-halophilic comparator that grows without an elevated-salt requirement; it exemplifies a contrasting branch of this broad preference class.",
        ),
    ],
    "environment/slightly_halophilic": [
        (
            "paraliobacillus",
            "Paraliobacillus ryukyuensis O15-7T was explicitly described as slightly halophilic: maximum specific growth rate occurred at 0.75-3.0% NaCl although growth extended from 0 to 22%.",
        )
    ],
    # pH optimum/range/delta families.
    "environment/ph_optimum": [
        (
            "microbaculum",
            "Microbaculum mangrovi FT89T had a reported optimum interval of pH 6.0-7.0. Because the interval touches the low/mid1 boundary, #591 keeps this claim on the optimum parent.",
        )
    ],
    "environment/ph_optimum_low": [
        (
            "picrophilus",
            "Picrophilus oshimae has a directly measured growth optimum near pH 0.7, wholly below the approximately pH 6 upper bound for this bin.",
        )
    ],
    "environment/ph_optimum_mid1": [
        (
            "pseudomonas_mangiferae",
            "Pseudomonas mangiferae DMKU BBB3-04T grew optimally at pH 6.5, wholly within the approximately pH 6-7 bin; growth was reported at pH 6-8.",
        )
    ],
    "environment/ph_optimum_mid2": [
        (
            "rubellicoccus",
            "Rubellicoccus peritrichatus CR14T had an optimum of pH 7.6, a point value wholly within the approximately pH 7-8 bin; its measured range was pH 6-9.",
        )
    ],
    "environment/ph_range": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T grew at pH 7-10. The complete interval crosses the mid2/mid3 split, so #591 places this distinct claim on the pH-range parent.",
        )
    ],
    "environment/ph_range_very_low": [
        (
            "picrophilus",
            "Picrophilus oshimae is an extreme acidophile whose measured growth extends from approximately pH 0 to pH 4, with optimum near 0.7; the complete interval is confined to this very-low range bin.",
        )
    ],
    "environment/ph_range_mid1": [
        (
            "sphingomonas",
            "Sphingomonas oligoaromativorans SY-6T grew only at pH 6.0-7.0 in the type-strain study, with optimum pH 7.0; the complete interval matches this bin.",
        )
    ],
    "environment/ph_range_mid2": [
        (
            "solimonas",
            "Solimonas fluminis HR-BBT grew at pH 7-8 in the primary species description; the complete reported interval matches this bin.",
        )
    ],
    "environment/ph_range_mid3": [
        (
            "evansella",
            "The type strain, published as Bacillus tamaricis EGI 80668T and now NCBI-labelled Evansella tamaricis, grew at pH 8-10 with optimum pH 9; the complete interval matches this bin.",
        )
    ],
    "environment/ph_delta": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T grew at pH 7-10, a breadth of 3 pH units. Because 3 is a bin boundary, #591 keeps this distinct claim on the delta parent.",
        )
    ],
    "environment/ph_delta_very_low": [
        (
            "sphingomonas",
            "Sphingomonas oligoaromativorans SY-6T grew from pH 6.0 to 7.0, a directly reported breadth of one pH unit inside the at-most-1 bin.",
        )
    ],
    "environment/ph_delta_low": [
        (
            "paracoccus_mangrovi",
            "Paracoccus mangrovi gyp-1T grew from pH 5.5 to 7.0, a 1.5-unit breadth wholly inside the approximately 1-2 pH-unit bin.",
        )
    ],
    "environment/ph_delta_mid1": [
        (
            "lederbergia",
            "The type strain, published as Bacillus graminis YC6957T, grew from pH 6.0 to 8.5, a 2.5-unit breadth wholly inside the approximately 2-3 bin.",
        )
    ],
    "environment/ph_delta_mid2": [
        (
            "microbaculum",
            "Microbaculum mangrovi FT89T grew from pH 5.5 to 9.0, a 3.5-unit breadth wholly inside the approximately 3-4 bin.",
        )
    ],
    "environment/ph_delta_mid3": [
        (
            "gemmobacter",
            "Gemmobacter lutimaris YJ-T1-11T grew from pH 5.0 to 9.0; the directly reported four-unit breadth lies in the approximately 4-5 bin.",
        )
    ],
    "environment/ph_delta_high": [
        (
            "amycolatopsis",
            "Amycolatopsis flava AFM 10111T grew from pH 5 to 12, a seven-unit breadth wholly inside the approximately 5-9 pH-unit bin.",
        )
    ],
    "environment/ph_growth_preference": [
        (
            "picrophilus",
            "Picrophilus oshimae, with a growth optimum near pH 0.7, exemplifies the acidophilic branch of pH growth preference.",
        ),
        (
            "evansella",
            "Evansella tamaricis EGI 80668T, published as Bacillus tamaricis, grew at pH 8-10 with optimum pH 9 and exemplifies an alkaliphilic branch.",
        ),
    ],
    "environment/facultatively_acidophilic": [
        (
            "paludibaculum",
            "Paludibaculum fermentans P105T was described from acidic peat and grows from pH 4.0 to 7.2, directly establishing acidic growth together with near-neutral capacity.",
        )
    ],
    # Pressure measurements are distinct optimum, range, and derived-delta claims.
    "environment/pressure_optimum": [
        (
            "colwellia",
            "Colwellia marinimaniae MTCD1 had a measured optimum of 120 MPa at 6 degrees C in its primary species description.",
        )
    ],
    "environment/pressure_range": [
        (
            "colwellia",
            "Colwellia marinimaniae MTCD1 grew from 80 to 140 MPa at 6 degrees C; the note retains the strain, endpoints, units, and temperature.",
        )
    ],
    "environment/pressure_delta": [
        (
            "colwellia",
            "The measured 80-140 MPa growth interval of Colwellia marinimaniae MTCD1 at 6 degrees C gives a 60 MPa pressure breadth.",
        )
    ],
    # Temperature optimum/range/delta families.
    "environment/temperature_optimum": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T had an optimum at exactly 30 degrees C. Because that point is the mid2/mid3 boundary, #591 keeps it on the optimum parent.",
        )
    ],
    "environment/temperature_optimum_very_low": [
        (
            "clostridium_psychrophilum",
            "Clostridium psychrophilum was cultured near its reported optimal growth temperature of 5 degrees C and also at -5 degrees C for the cited membrane-lipid study; the optimum is wholly inside the at-most-10-degree bin.",
        )
    ],
    "environment/temperature_optimum_mid1": [
        (
            "rubellicoccus",
            "Rubellicoccus peritrichatus CR14T had a measured optimum of 25 degrees C, wholly within the approximately 22-27-degree bin; growth occurred at 20-30 degrees C.",
        )
    ],
    "environment/temperature_optimum_mid2": [
        (
            "pontibacterium",
            "Pontibacterium sinense N1Y112T had a measured optimum of 28 degrees C, wholly within the approximately 27-30-degree bin; growth occurred at 20-35 degrees C.",
        )
    ],
    "environment/temperature_optimum_mid3": [
        (
            "mucor",
            "Unperturbed Mucor circinelloides on cheese-based agar had fitted temperature optima of 32.1-32.5 degrees C without added salt, wholly inside the approximately 30-34-degree bin.",
        )
    ],
    "environment/temperature_optimum_mid4": [
        (
            "ecoli_thermal",
            "Wild-type E. coli K-12 in the thermal-evolution study had a 37 degrees C growth optimum before the glpF-associated shift, wholly inside the approximately 34-40-degree bin.",
        )
    ],
    "environment/temperature_range": [
        (
            "lederbergia",
            "The type strain, published as Bacillus graminis YC6957T, grew from 15 to 45 degrees C. Its 30-degree breadth meets a bin boundary, so #591 keeps this claim on the range parent.",
        )
    ],
    "environment/temperature_range_very_low": [
        (
            "psychromonas",
            "Psychromonas ingrahamii strain 37T grew from -12 to 10 degrees C in its primary species description, directly establishing growth at and below this bin's 10-degree threshold.",
        )
    ],
    "environment/temperature_range_low": [
        (
            "aestuariibius",
            "Aestuariibius violaceus 2305UL40-4T grew from 22 to 36 degrees C, a directly reported 14-degree breadth within the approximately 10-22-degree range-width bin.",
        )
    ],
    "environment/temperature_range_mid1": [
        (
            "nakamurella",
            "Nakamurella aerolata DB0629T grew from 10 to 35 degrees C, a directly reported 25-degree breadth within the approximately 22-27-degree bin.",
        )
    ],
    "environment/temperature_range_mid2": [
        (
            "pseudomonas_mangiferae",
            "Pseudomonas mangiferae DMKU BBB3-04T grew from 12 to 40 degrees C, a directly reported 28-degree breadth within the approximately 27-30-degree bin.",
        )
    ],
    "environment/temperature_range_mid3": [
        (
            "bacillus_nakamurai",
            "Bacillus nakamurai NRRL B-41091T grew from 17 to 50 degrees C in its primary species description, a directly reported 33-degree breadth within the approximately 30-34-degree range-width bin.",
        )
    ],
    "environment/temperature_range_mid4": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T grew from 10 to 45 degrees C, a directly reported 35-degree breadth within the approximately 34-40-degree bin.",
        )
    ],
    "environment/temperature_delta": [
        (
            "kushneria",
            "Kushneria aurantia A10T grew from 20 to 40 degrees C, a 20-degree breadth. Because 20 meets the mid1/mid2 boundary, #591 keeps the claim on the delta parent.",
        )
    ],
    "environment/temperature_delta_mid1": [
        (
            "pontibacterium",
            "Pontibacterium sinense N1Y112T grew from 20 to 35 degrees C, a 15-degree breadth wholly inside the approximately 10-20-degree delta bin.",
        )
    ],
    "environment/temperature_delta_mid2": [
        (
            "pseudomonas_mangiferae",
            "Pseudomonas mangiferae DMKU BBB3-04T grew from 12 to 40 degrees C, a 28-degree breadth wholly inside the approximately 20-30-degree delta bin.",
        )
    ],
    "environment/temperature_preference": [
        (
            "clostridium_psychrophilum",
            "Clostridium psychrophilum has an optimum near 5 degrees C and exemplifies the cold-adapted branch of the broad temperature-preference class.",
        ),
        (
            "thermoanaerobacter",
            "Thermoanaerobacter kivui had an ancestral 66 degrees C optimum and exemplifies a thermophilic branch of the broad temperature-preference class.",
        ),
    ],
    "environment/oxygen_preference": [
        (
            "ecoli_oxygen",
            "Escherichia coli grows by aerobic respiration when oxygen is present and switches to anaerobic respiration or fermentation without it, exemplifying a facultative branch of oxygen preference.",
        )
    ],
    # Genome composition and size.
    "genomics/gc_content": [
        (
            "ecoli",
            "The complete E. coli K-12 genome provides a source-backed whole-genome GC-composition measurement and is used here as a family-level exemplar, distinct from the bin-specific taxa below.",
        )
    ],
    "genomics/gc_low": [
        (
            "bacillus_nakamurai",
            "Bacillus nakamurai NRRL B-41091T has 43.8 mol% genomic GC in its primary species description, wholly inside this record's authoritative 42.65-57.0% interval.",
        )
    ],
    "genomics/gc_mid1": [
        (
            "streptomyces_coelicolor",
            "The complete Streptomyces coelicolor A3(2) genome is approximately 72.1% GC, wholly above this record's authoritative 66.3% threshold.",
        )
    ],
    "genomics/gc_high": [
        (
            "mycoplasmoides",
            "The complete Mycoplasmoides genitalium G37 genome is approximately 31.7% GC, wholly below this record's authoritative 42.65% threshold.",
        )
    ],
    "genomics/gc_mid2": [
        (
            "oceanimonas",
            "The Oceanimonas pelagia NTOU-MSR1T genome has 61.0 mol% GC, wholly inside this record's authoritative 57.0-66.3% interval.",
        )
    ],
    "genomics/gc_skew": [
        (
            "ecoli",
            "The complete circular E. coli K-12 chromosome is a source-backed model for leading/lagging-strand GC asymmetry and replication-origin inference.",
        )
    ],
    "genomics/genome_size": [
        (
            "mycoplasmoides",
            "The complete Mycoplasmoides genitalium G37 genome contains 580,070 base pairs, a directly sequenced compact-genome example.",
        )
    ],
    # Morphometry and broad morphology.
    "morphology/cell_length": [
        (
            "ecoli_adder",
            "Escherichia coli is the organism in the cited single-cell adder study, which directly measures and models inter-division cell-length control; this is a family-level, not bin-level, exemplar.",
        )
    ],
    "morphology/cell_length_very_small": [
        (
            "flavicella",
            "Flavicella sediminum ALS 84T cells measured 1.0-1.2 micrometres long in the primary species description, wholly inside the at-most-1.3-micrometre bin.",
        )
    ],
    "morphology/cell_length_small": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T cells measured approximately 1.8-2.0 micrometres long, within the approximately 1.3-2.0-micrometre bin.",
        )
    ],
    "morphology/cell_length_medium": [
        (
            "marinobacterium",
            "Marinobacterium lacunae AK27T cells measured 2.0-3.0 micrometres long in the primary species description, matching this bin.",
        )
    ],
    "morphology/cell_length_large": [
        (
            "spirochaeta",
            "Spirochaeta dissipatitropha ASpC2T cells measured 8-18 micrometres long, wholly above the approximately 3-micrometre threshold.",
        )
    ],
    "morphology/cell_width_very_small": [
        (
            "spirochaeta",
            "Spirochaeta dissipatitropha ASpC2T cells measured approximately 0.23 micrometres wide, wholly below the at-most-0.5-micrometre threshold.",
        )
    ],
    "morphology/cell_width_small": [
        (
            "oceanimonas",
            "Oceanimonas pelagia NTOU-MSR1T cells measured approximately 0.5-0.6 micrometres wide, within the approximately 0.5-0.65-micrometre bin.",
        )
    ],
    "morphology/cell_width_medium": [
        (
            "ruixingdingia",
            "Ruixingdingia sedimenti LG-4T cells measured 0.7-0.8 micrometres wide, wholly within the approximately 0.65-0.9-micrometre bin.",
        )
    ],
    "morphology/cell_width_large": [
        (
            "marinobacterium",
            "Marinobacterium lacunae AK27T cells measured 1.0-1.5 micrometres wide, wholly above the approximately 0.9-micrometre threshold.",
        )
    ],
    "morphology/gram_stain": [
        (
            "ecoli",
            "Escherichia coli exemplifies the Gram-negative outcome of the differential stain and its thin-peptidoglycan, outer-membrane envelope branch.",
        ),
        (
            "bsub",
            "Bacillus subtilis exemplifies the Gram-positive outcome and thick-peptidoglycan envelope branch of this broad stain class.",
        ),
    ],
    "morphology/cell_shape": [
        (
            "ecoli_shape",
            "Escherichia coli is a source-backed model in which cell-wall and cytoskeletal systems maintain a rod-shaped cellular form; this scopes the example to one branch of the broad shape class.",
        )
    ],
    "morphology/cream_pigmented": [
        (
            "seongchinamella",
            "Seongchinamella unica GH4-78T produced cream-coloured colonies in its primary species description, a direct unperturbed colony-pigmentation observation.",
        )
    ],
    "morphology/dumbbell_shaped": [
        (
            "corynebacterium_diphtheriae",
            "Corynebacterium diphtheriae undergoes snapping division that leaves daughter cells in V-shaped and transient dumbbell arrangements; the cited review synthesizes the primary corynebacterial division observations.",
        )
    ],
    "morphology/irregular_shaped": [
        (
            "corynebacterium_glutamicum",
            "Corynebacterium glutamicum exhibits coryneform, irregular cell arrangements produced by apical growth and snapping division; the note scopes the example to that natural morphology.",
        )
    ],
    # A broad trophic class needs examples from distinct branches.
    "physiology/trophic_type": [
        (
            "ecoli",
            "Escherichia coli exemplifies chemoorganoheterotrophy, one concrete combination of chemical energy, organic electron donors, and organic carbon within the broad trophic-type class.",
        ),
        (
            "synechocystis",
            "Synechocystis sp. PCC 6803 exemplifies oxygenic photoautotrophy, a contrasting light-energy and inorganic-carbon branch of the broad trophic-type class.",
        ),
    ],
}

# Bacillus subtilis is kept separate because its existing corpus citation is a
# species/genome reference rather than one of the new literature-led sources.
SOURCES["bsub"] = source("NCBITaxon:1423", "Bacillus subtilis", "PMID:9384377")


DEFERRED = {
    "ecology/biosafety_level_5": (
        "The class is explicitly hypothetical and above every implemented containment "
        "level; assigning a real organism would falsely assert an authority-backed BSL-5 "
        "classification that does not exist."
    ),
    "environment/temperature_delta_very_low": (
        "The tracked artifact explicitly found no natural organism with both sustained-"
        "growth endpoints establishing a 1-5 degree C breadth. Cold growth, an optimum, "
        "or an assay window is not a measured delta under #591."
    ),
    "environment/temperature_delta_low": (
        "The tracked artifact explicitly found no natural organism with both sustained-"
        "growth endpoints establishing a non-boundary 5-10 degree C breadth. Stress "
        "survival and one-endpoint studies do not qualify under #591."
    ),
    "environment/ph_range_high": (
        "No retrieved primary source established a natural organism whose complete "
        "growth interval is contained in pH 10-14. Sources that merely grow above pH 10 "
        "also extend below the bin and therefore remain parent-level evidence under #591."
    ),
}


def validate_ledger() -> None:
    """Fail closed when the hand-reviewed ledger drifts or contradicts itself."""
    if len(TRANCHE) != 85 or len(DEFERRED) != 4:
        raise RuntimeError(
            f"expected 85 populated and 4 deferred records, found "
            f"{len(TRANCHE)} and {len(DEFERRED)}"
        )
    overlap = set(TRANCHE) & set(DEFERRED)
    if overlap:
        raise RuntimeError(f"records cannot be both populated and deferred: {overlap}")
    for slug, rows in TRANCHE.items():
        if not rows:
            raise RuntimeError(f"{slug}: populated tranche has no examples")
        for source_key, note in rows:
            if source_key not in SOURCES:
                raise RuntimeError(f"{slug}: unknown source key {source_key!r}")
            if not note.strip():
                raise RuntimeError(f"{slug}: empty source-scoped note")
            if "not used" in note.lower() or "outside this record" in note.lower():
                raise RuntimeError(f"{slug}: note describes a rejected exemplar")


def expected_queue() -> set[str]:
    rows, _meta = build_queue()
    return {
        f"{row['category']}/{row['slug']}"
        for row in rows
        if row["action"] == ADD_ACTION
    }


def _insert_examples(doc: dict[str, Any], examples: list[dict[str, str]]) -> None:
    if "canonical_examples" in doc:
        doc["canonical_examples"] = examples
        return
    rebuilt: dict[str, Any] = {}
    for key, value in doc.items():
        rebuilt[key] = value
        if key == "evidence":
            rebuilt["canonical_examples"] = examples
    if "canonical_examples" not in rebuilt:
        rebuilt["canonical_examples"] = examples
    doc.clear()
    doc.update(rebuilt)


def _write(doc: dict[str, Any], path: Path, write: bool) -> None:
    if write:
        write_validated_trait(doc, path)
        return
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(doc, Path(tmp) / path.name)


def apply(write: bool = False) -> int:
    validate_ledger()
    planned = set(TRANCHE) | set(DEFERRED)
    queue = expected_queue()
    post_apply_queue = set(DEFERRED)
    if queue not in (planned, post_apply_queue):
        missing = sorted(queue - planned)
        stale = sorted(planned - queue)
        raise RuntimeError(
            f"#444 plan no longer matches live queue; missing={missing}, stale={stale}"
        )
    if queue == planned and len(queue) != 89:
        raise RuntimeError(f"expected the post-#591 queue of 89 records, found {len(queue)}")

    added = reviewed_empty = unchanged = 0
    for slug in sorted(planned):
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        existing = doc.get("canonical_examples") or []
        if slug in TRANCHE:
            examples = [
                {**SOURCES[source_key], "note": note}
                for source_key, note in TRANCHE[slug]
            ]
            if existing == examples:
                unchanged += 1
                continue
            if existing:
                raise ValueError(f"{slug}: gained examples since the 89-record baseline")
            _insert_examples(doc, examples)
            record_curation_event(
                doc,
                curator=CURATOR,
                action=ADD_ACTION,
                changes=(
                    f"Resolved issue #444 after the #591 source/bin policy with "
                    f"{len(examples)} direct source-backed canonical example(s): "
                    + ", ".join(
                        f"{example['taxon_label']} ({example['taxon_id']}; "
                        f"{example['reference']})"
                        for example in examples
                    )
                    + ". The note retains the measured value or scopes broad-class "
                    "examples to the cited branch; no paid research was used."
                ),
                llm_assisted=True,
                timestamp=TIMESTAMP,
                upsert=True,
            )
            added += 1
        else:
            if existing:
                raise ValueError(f"{slug}: deferred record unexpectedly has examples")
            record_curation_event(
                doc,
                curator=CURATOR,
                action=DEFER_ACTION,
                changes=(
                    f"Reviewed issue #444 after #591 and left canonical_examples empty: "
                    f"{DEFERRED[slug]} No paid research was used."
                ),
                llm_assisted=True,
                timestamp=TIMESTAMP,
                upsert=True,
            )
            reviewed_empty += 1
        _write(doc, path, write)

    mode = "applied" if write else "dry run"
    print(
        f"{mode}: {added} record(s) gained examples; {reviewed_empty} explicit "
        f"evidence deferral(s); {unchanged} already applied"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write; default is dry run")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
