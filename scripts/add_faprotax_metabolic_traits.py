#!/usr/bin/env python3
"""Add FAPROTAX metabolic capability records from proposal cohort v11."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAIT_DIR = REPO_ROOT / "data" / "traits"
METABOLISM_DIR = TRAIT_DIR / "metabolism"

TIMESTAMP = "2026-09-08T00:00:00Z"
FAPROTAX = "DOI:10.1126/science.aaf4507"
CURATOR = "codex"

NEW_RECORDS: tuple[tuple[str, dict], ...] = (
    (
        "nitrogen_respiration",
        {
            "identifier": "traitmech:000121",
            "label": "nitrogen respiration",
            "definition": (
                "An anaerobic respiration in which an organism conserves energy by "
                "transferring electrons to an oxidized nitrogen compound as the "
                "terminal electron acceptor."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000802"],
            "synonyms": [
                {
                    "synonym_text": "nitrogen_respiration",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.61.4.533-616.1997",
                    "snippet": "N oxides as terminal electron acceptors",
                    "notes": (
                        "Zumft reviews denitrification as anaerobic respiration "
                        "with oxidized nitrogen compounds as electron acceptors."
                    ),
                },
            ],
        },
    ),
    (
        "nitrate_respiration",
        {
            "identifier": "traitmech:000122",
            "label": "nitrate respiration",
            "definition": (
                "A nitrogen respiration in which nitrate is the terminal electron "
                "acceptor, reduced to nitrite or further reduced products."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["traitmech:000121", "traitmech:000134"],
            "synonyms": [
                {
                    "synonym_text": "nitrate_respiration",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.1126/science.1254070",
                    "snippet": "bacterial nitrate respiration",
                    "notes": (
                        "Kraft et al. support nitrate respiration as a bacterial "
                        "nitrogen-oxide respiration branch with denitrification "
                        "or DNRA endpoints."
                    ),
                },
            ],
        },
    ),
    (
        "nitrite_respiration",
        {
            "identifier": "traitmech:000123",
            "label": "nitrite respiration",
            "definition": (
                "A nitrogen respiration in which nitrite is the terminal electron "
                "acceptor."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["traitmech:000121"],
            "synonyms": [
                {
                    "synonym_text": "nitrite_respiration",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.1128/aem.00292-25",
                    "snippet": "nitrite respiration continues unimpaired",
                    "notes": (
                        "Hird et al. review cytochrome c nitrite reductase as the "
                        "nitrite-to-ammonium step in respiratory DNRA."
                    ),
                },
            ],
        },
    ),
    (
        "respiration_of_sulfur_compounds",
        {
            "identifier": "traitmech:000124",
            "label": "respiration of sulfur compounds",
            "definition": (
                "An anaerobic respiration in which an organism conserves energy by "
                "transferring electrons to an inorganic sulfur compound as the "
                "terminal electron acceptor."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000802"],
            "synonyms": [
                {
                    "synonym_text": "respiration_of_sulfur_compounds",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1108245",
                    "snippet": "sulfate, sulfur, or thiosulfate respiration",
                    "notes": (
                        "Zavarzina et al. experimentally compare iron respiration "
                        "with sulfur/thiosulfate respiration in Dethiobacter "
                        "alkaliphilus."
                    ),
                },
            ],
        },
    ),
    (
        "sulfur_respiration",
        {
            "identifier": "traitmech:000125",
            "label": "sulfur respiration",
            "definition": (
                "A respiration of sulfur compounds in which elemental sulfur is "
                "the terminal electron acceptor and is reduced to sulfide."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["traitmech:000124"],
            "synonyms": [
                {
                    "synonym_text": "sulfur_respiration",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1108245",
                    "snippet": "Iron or sulfur respiration",
                    "notes": (
                        "Zavarzina et al. analyze a natronophilic bacterium capable "
                        "of reducing zero-valent sulfur during anaerobic respiration."
                    ),
                },
            ],
        },
    ),
    (
        "thiosulfate_respiration",
        {
            "identifier": "traitmech:000126",
            "label": "thiosulfate respiration",
            "definition": (
                "A respiration of sulfur compounds in which thiosulfate is the "
                "terminal electron acceptor."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["traitmech:000124"],
            "synonyms": [
                {
                    "synonym_text": "thiosulfate_respiration",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1108245",
                    "snippet": "sulfur- and thiosulfate reducing type strain",
                    "notes": (
                        "Zavarzina et al. analyze thiosulfate respiration in "
                        "Dethiobacter alkaliphilus as an anaerobic energy metabolism."
                    ),
                },
            ],
        },
    ),
    (
        "hydrogenotrophic_methanogenesis",
        {
            "identifier": "traitmech:000127",
            "label": "hydrogenotrophic methanogenesis",
            "definition": (
                "A methanogenesis in which carbon dioxide is reduced to methane "
                "using molecular hydrogen as the electron donor."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000844"],
            "synonyms": [
                {
                    "synonym_text": "hydrogenotrophic_methanogenesis",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
                {
                    "synonym_text": "methanogenesis_by_CO2_reduction_with_H2",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "xrefs": ["GO:0019386"],
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-011720-122807",
                    "snippet": "from CO2 and H2 to methane",
                    "notes": (
                        "The methanogenesis review supports the H2/CO2 branch of "
                        "archaeal methane production."
                    ),
                },
            ],
        },
    ),
    (
        "hydrocarbon_degradation",
        {
            "identifier": "traitmech:000128",
            "label": "hydrocarbon degradation",
            "definition": (
                "A metabolism in which an organism catabolizes a hydrocarbon, using "
                "it as a carbon and energy source."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "hydrocarbon_degradation",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "xrefs": ["GO:0120253"],
            "evidence": [
                {
                    "reference": "DOI:10.1128/MR.54.3.305-315.1990",
                    "snippet": "Microbial degradation of hydrocarbons in the environment",
                    "notes": (
                        "Leahy and Colwell review microbial hydrocarbon "
                        "degradation across environmental microorganisms."
                    ),
                },
            ],
        },
    ),
    (
        "aromatic_hydrocarbon_degradation",
        {
            "identifier": "traitmech:000129",
            "label": "aromatic hydrocarbon degradation",
            "definition": (
                "A hydrocarbon degradation in which the substrate carries at least "
                "one aromatic ring."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["traitmech:000128", "traitmech:000130"],
            "synonyms": [
                {
                    "synonym_text": "aromatic_hydrocarbon_degradation",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.1007/BF00058836",
                    "snippet": "The biodegradation of aromatic hydrocarbons by bacteria",
                    "notes": (
                        "Smith reviews bacterial biodegradation of aromatic "
                        "hydrocarbons as a distinct hydrocarbon-degradation branch."
                    ),
                },
            ],
        },
    ),
    (
        "aromatic_compound_degradation",
        {
            "identifier": "traitmech:000130",
            "label": "aromatic compound degradation",
            "definition": (
                "A metabolism in which an organism catabolizes an aromatic "
                "compound, whether or not that compound is a hydrocarbon."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "aromatic_compound_degradation",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.3390/ijerph6010278",
                    "snippet": "Bacterial Degradation of Aromatic Compounds",
                    "notes": (
                        "Seo et al. review bacterial pathways for degradation of "
                        "aromatic compounds."
                    ),
                },
            ],
        },
    ),
    (
        "dark_hydrogen_oxidation",
        {
            "identifier": "traitmech:000131",
            "label": "dark hydrogen oxidation",
            "definition": (
                "A metabolism in which an organism oxidizes molecular hydrogen as "
                "an electron donor for energy conservation independently of light."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "dark_hydrogen_oxidation",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.21775/cimb.006.159",
                    "snippet": "reversible oxidation of hydrogen gas",
                    "notes": (
                        "The hydrogenotrophy review supports hydrogenase-catalyzed "
                        "oxidation of molecular hydrogen for microbial energy "
                        "metabolism."
                    ),
                },
            ],
        },
    ),
    (
        "dark_oxidation_of_sulfur_compounds",
        {
            "identifier": "traitmech:000132",
            "label": "dark oxidation of sulfur compounds",
            "definition": (
                "A metabolism in which an organism oxidizes a reduced inorganic "
                "sulfur compound as an electron donor for energy conservation "
                "independently of light."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "dark_oxidation_of_sulfur_compounds",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "xrefs": ["GO:0019417"],
            "evidence": [
                {
                    "reference": "DOI:10.1111/j.1574-6976.2009.00187.x",
                    "snippet": (
                        "Lithotrophic sulfur oxidation is an ancient metabolic "
                        "process"
                    ),
                    "notes": (
                        "Ghosh and Dam review lithotrophic oxidation of reduced "
                        "inorganic sulfur compounds."
                    ),
                },
            ],
        },
    ),
    (
        "methanol_oxidation",
        {
            "identifier": "traitmech:000133",
            "label": "methanol oxidation",
            "definition": (
                "A metabolism in which an organism oxidizes methanol, typically to "
                "formaldehyde, as a carbon and energy source."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "methanol_oxidation",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "xrefs": ["GO:0015946"],
            "evidence": [
                {
                    "reference": "DOI:10.3389/fbioe.2021.787791",
                    "snippet": "methanol utilization in methylotrophy",
                    "notes": (
                        "Le et al. review methanol dehydrogenases as primary "
                        "enzymes that convert methanol to formaldehyde during "
                        "methylotrophy."
                    ),
                },
            ],
        },
    ),
    (
        "nitrate_reduction",
        {
            "identifier": "traitmech:000134",
            "label": "nitrate reduction",
            "definition": (
                "A metabolism in which an organism reduces nitrate, whether for "
                "energy conservation or for assimilation into biomass."
            ),
            "definition_source": FAPROTAX,
            "trait_category": "METABOLISM",
            "term_kind": "CLASS",
            "mapping_status": "PROPOSED",
            "parent_traits": ["METPO:1000060"],
            "synonyms": [
                {
                    "synonym_text": "nitrate_reduction",
                    "synonym_type": "EXACT_SYNONYM",
                    "source": FAPROTAX,
                },
            ],
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro.2018.9",
                    "snippet": "The microbial nitrogen-cycling network",
                    "notes": (
                        "Kuypers et al. review dissimilatory and assimilatory "
                        "nitrate-reducing steps in the microbial nitrogen cycle."
                    ),
                },
            ],
        },
    ),
)

REPARENTS: tuple[tuple[str, str, str, str], ...] = (
    (
        "denitrification",
        "METPO:1000802",
        "traitmech:000121",
        "Narrowed parent from anaerobic respiration to nitrogen respiration.",
    ),
    (
        "dissimilatory_nitrate_reduction_to_ammonium",
        "METPO:1000802",
        "traitmech:000121",
        "Narrowed parent from anaerobic respiration to nitrogen respiration.",
    ),
    (
        "dissimilatory_sulfate_reduction",
        "METPO:1000802",
        "traitmech:000124",
        "Narrowed parent from anaerobic respiration to respiration of sulfur compounds.",
    ),
)


def _load_trait(slug: str) -> tuple[Path, dict]:
    path = METABOLISM_DIR / f"{slug}.yaml"
    return path, yaml.safe_load(path.read_text(encoding="utf-8"))


def _replace_parent(doc: dict, old: str, new: str) -> bool:
    parents = list(doc.get("parent_traits") or [])
    updated = []
    for parent in parents:
        replacement = new if parent == old else parent
        if replacement not in updated:
            updated.append(replacement)
    if new not in updated:
        updated.append(new)
    if updated == parents:
        return False
    doc["parent_traits"] = updated
    return True


def _add_xylanolysis_synonym() -> tuple[Path, dict] | None:
    path, doc = _load_trait("xylan_degradation")
    synonyms = list(doc.get("synonyms") or [])
    if any(s.get("synonym_text") == "xylanolysis" for s in synonyms):
        return None
    synonyms.append(
        {
            "synonym_text": "xylanolysis",
            "synonym_type": "EXACT_SYNONYM",
            "source": FAPROTAX,
        }
    )
    doc["synonyms"] = synonyms
    record_curation_event(
        doc,
        curator=CURATOR,
        action="ADD_EXACT_SYNONYM",
        changes=(
            "Added xylanolysis as an exact FAPROTAX synonym rather than minting "
            "the duplicate v11 candidate because GO:0045493 already grounds "
            "xylan degradation."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return path, doc


def _new_records() -> list[tuple[Path, dict]]:
    existing_ids: dict[str, Path] = {}
    for path in TRAIT_DIR.rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        existing_ids[doc["identifier"]] = path

    records = []
    for slug, raw in NEW_RECORDS:
        path = METABOLISM_DIR / f"{slug}.yaml"
        record = copy.deepcopy(raw)
        identifier = record["identifier"]
        if path.exists():
            existing = yaml.safe_load(path.read_text(encoding="utf-8"))
            if existing["identifier"] != identifier:
                raise SystemExit(f"{path.relative_to(REPO_ROOT)} already exists")
            continue
        if identifier in existing_ids and existing_ids[identifier] != path:
            taken = existing_ids[identifier].relative_to(REPO_ROOT)
            raise SystemExit(f"{identifier} is already used by {taken}")
        record_curation_event(
            record,
            curator=CURATOR,
            action="PROPOSED_FROM_RESEARCH",
            changes=(
                "Proposed a DOI-backed FAPROTAX metabolic capability from "
                "proposals/metpo_traitmech_v11 after repository-wide duplicate "
                "review."
            ),
            llm_assisted=True,
            timestamp=TIMESTAMP,
        )
        records.append((path, record))
    return records


def _reparent_records() -> list[tuple[Path, dict]]:
    outputs = []
    for slug, old, new, changes in REPARENTS:
        path, doc = _load_trait(slug)
        if not _replace_parent(doc, old, new):
            continue
        record_curation_event(
            doc,
            curator=CURATOR,
            action="REFINE_PARENT_TRAIT",
            changes=changes,
            llm_assisted=True,
            timestamp=TIMESTAMP,
        )
        outputs.append((path, doc))
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    outputs = _new_records()
    outputs.extend(_reparent_records())
    xylan = _add_xylanolysis_synonym()
    if xylan:
        outputs.append(xylan)

    for path, doc in outputs:
        rel = path.relative_to(REPO_ROOT)
        if args.apply:
            write_validated_trait(doc, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
