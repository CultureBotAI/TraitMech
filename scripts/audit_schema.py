#!/usr/bin/env python3
"""Schema audit probes for the TraitMech LinkML schema.

Programmatic detection of common schema-quality issues:
  - classes lacking an `identifier:` slot
  - slots/attributes with `range: string` whose name suggests a typed term/enum
  - divergent term-field naming across descriptors
  - inconsistent `required:` use across parallel structures
  - enums declared but never referenced as a `range:`
  - `range:` references to undefined classes/types/enums

Output: stdout text. Pipe to / capture in `reports/schema_gap_audit.md` (the
human report is composed by hand using these probe results).
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import yaml

SCHEMA_PATH = Path("src/traitmech/schema/traitmech.yaml")

# Slot-name fragments that strongly suggest an enum / typed term is appropriate.
SUSPECT_FRAGMENTS = [
    "phase", "mode", "type", "status", "kind", "unit", "units",
    "atmosphere", "salinity", "temperature_range", "ph_range", "light_cycle",
    "category", "relationship", "modifier", "format", "version",
]

# Slot-name fragments that explicitly indicate ontology references.
TERM_NAME_FRAGMENTS = ["term", "ontology", "curie", "_id"]

BUILTIN_RANGES = {
    "string", "integer", "boolean", "float", "double", "date", "datetime",
    "uri", "uriorcurie", "ncname", "objectidentifier", "nodeidentifier",
    "decimal", "time",
}


def class_line_index(text_lines: list[str]) -> dict[str, int]:
    """Map class name -> 1-indexed line of its declaration."""
    out: dict[str, int] = {}
    in_classes = False
    for i, line in enumerate(text_lines):
        if line.startswith("classes:"):
            in_classes = True
            continue
        if in_classes:
            if re.match(r"^[a-zA-Z]\w*:", line):  # next top-level key
                if not line.startswith(" "):
                    in_classes = False
                    continue
            m = re.match(r"^  (\w+):\s*$", line)
            if m:
                out[m.group(1)] = i + 1
    return out


def iter_attributes(schema: dict) -> Iterable[tuple[str, str, dict]]:
    """Yield (class_name, attr_name, attr_def) for every attribute on every class."""
    for cname, cdef in (schema.get("classes") or {}).items():
        for aname, adef in (cdef.get("attributes") or {}).items():
            yield cname, aname, (adef or {})


def local_imported_type_names(
    schema_path: Path, schema: dict, seen: set[Path] | None = None
) -> set[str]:
    """Collect classes, enums, and types from recursively imported local YAML.

    Prefix imports such as ``linkml:types`` are supplied by LinkML itself and
    are covered by ``BUILTIN_RANGES``. Bare imports resolve beside the importing
    schema, matching LinkML's local import convention.
    """
    seen = {schema_path.resolve()} if seen is None else seen
    names: set[str] = set()
    for imported in schema.get("imports") or []:
        imported = str(imported)
        if ":" in imported:
            continue
        candidate = schema_path.parent / imported
        if candidate.suffix not in {".yaml", ".yml"}:
            candidate = candidate.with_suffix(".yaml")
        candidate = candidate.resolve()
        if candidate in seen or not candidate.is_file():
            continue
        seen.add(candidate)
        imported_schema = yaml.safe_load(candidate.read_text()) or {}
        for section in ("classes", "enums", "types"):
            names.update((imported_schema.get(section) or {}).keys())
        names.update(local_imported_type_names(candidate, imported_schema, seen))
    return names


def undefined_range_hits(schema: dict, imported_names: set[str]) -> list[tuple[str, str, str]]:
    """Return attributes whose ranges resolve nowhere in the schema closure."""
    known = (
        set(schema.get("classes") or {})
        | set(schema.get("enums") or {})
        | set(schema.get("types") or {})
        | BUILTIN_RANGES
        | imported_names
    )
    hits = []
    for cname, aname, adef in iter_attributes(schema):
        value_range = adef.get("range")
        if isinstance(value_range, str) and value_range not in known:
            hits.append((cname, aname, value_range))
    return hits


def report_section(title: str) -> None:
    print()
    print(f"## {title}")
    print()


def main() -> int:
    text = SCHEMA_PATH.read_text()
    text_lines = text.splitlines()
    schema = yaml.safe_load(text)
    classes = schema.get("classes") or {}
    enums = schema.get("enums") or {}
    cls_lines = class_line_index(text_lines)

    print(f"# Schema audit probes — {SCHEMA_PATH}")
    print()
    print(f"- classes: {len(classes)}")
    print(f"- enums:   {len(enums)}")
    print(f"- raw lines: {len(text_lines)}")

    # 1. Classes lacking an identifier slot (and not abstract / mixin).
    report_section("Classes lacking an `identifier: true` slot")
    print("Classes intended as referenceable entities should expose an identifier.")
    print()
    for cname, cdef in classes.items():
        if cdef.get("abstract") or cdef.get("mixin"):
            continue
        attrs = cdef.get("attributes") or {}
        has_id = any((a or {}).get("identifier") for a in attrs.values())
        if not has_id and attrs:
            line = cls_lines.get(cname, "?")
            print(f"- `{cname}` (line {line}) — {len(attrs)} attrs, no identifier slot")

    # 2. Suspect `range: string` slots (likely should be enum or typed term).
    report_section("Slots with `range: string` that look like they should be enums or typed terms")
    suspects = []
    for cname, aname, adef in iter_attributes(schema):
        if adef.get("range") != "string":
            continue
        lname = aname.lower()
        if any(frag in lname for frag in SUSPECT_FRAGMENTS):
            suspects.append((cname, aname, adef.get("description", "")[:80]))
    print(f"({len(suspects)} hits)")
    print()
    for cname, aname, desc in suspects[:60]:
        print(f"- `{cname}.{aname}` — {desc}")
    if len(suspects) > 60:
        print(f"- ... {len(suspects) - 60} more")

    # 3. Term-field naming divergence across descriptors.
    report_section("Term/ontology slot naming divergence")
    term_names: dict[str, list[str]] = defaultdict(list)
    for cname, aname, _adef in iter_attributes(schema):
        lname = aname.lower()
        if any(frag in lname for frag in TERM_NAME_FRAGMENTS):
            term_names[aname].append(cname)
    for name in sorted(term_names):
        owners = term_names[name]
        print(f"- `{name}` used on: {', '.join(sorted(owners))}")

    # 4. Inconsistent `required: true` for analogous slot names.
    report_section("Inconsistent `required:` for analogously-named attributes across classes")
    by_attr: dict[str, list[tuple[str, bool]]] = defaultdict(list)
    for cname, aname, adef in iter_attributes(schema):
        by_attr[aname].append((cname, bool(adef.get("required"))))
    for aname, owners in sorted(by_attr.items()):
        if len({req for _, req in owners}) > 1 and len(owners) >= 2:
            req_owners = [c for c, r in owners if r]
            opt_owners = [c for c, r in owners if not r]
            print(f"- `{aname}` — required in: {sorted(req_owners)} | optional in: {sorted(opt_owners)}")

    # 5. Enums declared but never used as a range anywhere.
    report_section("Enums declared but never referenced as a `range:`")
    used_ranges: set[str] = set()
    for _cname, _aname, adef in iter_attributes(schema):
        r = adef.get("range")
        if isinstance(r, str):
            used_ranges.add(r)
    orphan = sorted(set(enums) - used_ranges)
    if orphan:
        for e in orphan:
            print(f"- `{e}`")
    else:
        print("(none)")

    # 6. range: refers to a name that isn't a class/enum/built-in type.
    report_section("Attributes whose `range:` is undefined in this schema")
    imported_names = local_imported_type_names(SCHEMA_PATH, schema)
    unknown_hits = undefined_range_hits(schema, imported_names)
    print(f"({len(unknown_hits)} hits)")
    for cname, aname, rng in unknown_hits[:40]:
        print(f"- `{cname}.{aname}` -> range: `{rng}`")
    if len(unknown_hits) > 40:
        print(f"- ... {len(unknown_hits) - 40} more")

    # 7. Enum value casing audit — are any enums lowercase while others are UPPER?
    report_section("Enum value casing audit")
    for ename, edef in enums.items():
        pv = (edef or {}).get("permissible_values") or {}
        vals = list(pv)
        if not vals:
            continue
        upper = [v for v in vals if v == v.upper() and any(c.isalpha() for c in v)]
        lower = [v for v in vals if v == v.lower() and any(c.isalpha() for c in v)]
        mixed = [v for v in vals if v not in upper and v not in lower]
        if (1 if upper else 0) + (1 if lower else 0) + (1 if mixed else 0) >= 2:
            sample = ", ".join(vals[:6])
            print(f"- `{ename}` mixes casing — sample: {sample}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
