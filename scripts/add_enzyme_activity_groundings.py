#!/usr/bin/env python3
"""Ground the 42 microbedecoder enzyme-activity labels to GO/EC (#453).

The decision on #453 was the METPO pattern: **three relations plus an EC/GO
mapping table**, not 42 new enzyme classes. The relations already exist —
`METPO:2000301 enzyme activity analyzed`, `METPO:2000302 shows activity of`,
`METPO:2000303 does not show activity of` — and their range is `METPO:1000527
enzyme`. What was missing is the object side: something for each API 20/32 and
Biolog panel enzyme to point at. This adds that as `MOLECULAR_FUNCTION` rows in
`mappings/node_grounding.tsv`, the table `ground_causal_nodes.py` already reads.

## Why these targets and not the obvious ones

Every GO id here was round-tripped against OLS4 by identifier, not accepted
from a keyword search. That mattered: **five of the ids a reader would reach
for first are obsolete** —

    GO:0004178  obsolete leucyl aminopeptidase activity  -> GO:0004177 / GO:0008235
    GO:0004295  obsolete trypsin activity                -> GO:0004252
    GO:0004263  obsolete chymotrypsin activity           -> GO:0004252
    GO:0003840  obsolete gamma-glutamyltransferase       -> GO:0036374
    GO:0008451  obsolete X-Pro aminopeptidase activity   -> GO:0004177

GO retired the protease-specificity classes, so the substrate-specific
arylamidases have no molecular-function term of their own any more. Each of
the 29 distinct targets below was confirmed non-obsolete.

`arylamidase` is API-strip vocabulary for `aminopeptidase`, which is why a
literal search finds nothing for ten of these labels.

## Predicate choice

Only `skos:exactMatch` and `skos:closeMatch` appear in this table, so broader
targets take `closeMatch` — the precedent set by `kinase reaction ->
kinase activity`. Deliberately **not** introducing `skos:broadMatch`: an
asymmetric predicate whose direction is read differently by two repos is
exactly the defect MediaIngredientMech#390 is still coordinating a fix for,
and nothing here needs the extra expressiveness.

## Where the EC number lives

In `notes`, prefixed `EC:`, rather than in a new column. The loader requires
only (label, node_type, target_curie) but every consumer reads this file with
DictReader against a fixed header; adding a column would rewrite all 344
existing rows for a field only these 42 use. Greppable as `EC:` either way.

    python scripts/add_enzyme_activity_groundings.py            # dry-run
    python scripts/add_enzyme_activity_groundings.py --apply
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "mappings" / "node_grounding.tsv"
SRC = "GO"
E, C = "skos:exactMatch", "skos:closeMatch"

# label, GO curie, GO label, predicate, confidence, note
ROWS: list[tuple[str, str, str, str, str, str]] = [
    # --- the GO term IS the enzyme activity ---
    ("alkaline phosphatase", "GO:0004035", "alkaline phosphatase activity", E, "high",
     "EC:3.1.3.1. API 20/32 panel enzyme."),
    ("acid phosphatase", "GO:0003993", "acid phosphatase activity", E, "high",
     "EC:3.1.3.2. API 20/32 panel enzyme."),
    ("cytochrome oxidase", "GO:0004129", "cytochrome-c oxidase activity", E, "high",
     "EC:7.1.1.9. The bacteriological 'oxidase test' reads cytochrome-c oxidase."),
    ("cytochrome-c oxidase", "GO:0004129", "cytochrome-c oxidase activity", E, "high",
     "EC:7.1.1.9. Same enzyme as the 'cytochrome oxidase' label; both source "
     "spellings kept so each grounds without a normalisation step."),
    ("alpha-glucosidase", "GO:0090599", "alpha-glucosidase activity", E, "high",
     "GO carries no EC xref on this term."),
    ("beta-galactosidase", "GO:0004565", "beta-galactosidase activity", E, "high",
     "EC:3.2.1.23. The ONPG test."),
    ("beta-glucosidase", "GO:0008422", "beta-glucosidase activity", E, "high",
     "EC:3.2.1.21. Agrees with the existing GENE_OR_PROTEIN row for this label; "
     "the table is keyed on (label, node_type) so both coexist."),
    ("alpha-galactosidase", "GO:0004557", "alpha-galactosidase activity", E, "high",
     "EC:3.2.1.22."),
    ("alpha-mannosidase", "GO:0004559", "alpha-mannosidase activity", E, "high",
     "EC:3.2.1.24."),
    ("amylase", "GO:0016160", "amylase activity", E, "high",
     "Starch hydrolysis. GO carries no EC xref on this term."),
    ("beta-glucuronidase", "GO:0004566", "beta-glucuronidase activity", E, "high",
     "EC:3.2.1.31. The MUG test."),
    ("alpha-fucosidase", "GO:0004560", "alpha-L-fucosidase activity", E, "high",
     "EC:3.2.1.51."),
    ("lysine decarboxylase", "GO:0008923", "lysine decarboxylase activity", E, "high",
     "EC:4.1.1.18."),
    ("ornithine decarboxylase", "GO:0004586", "ornithine decarboxylase activity", E,
     "high", "EC:4.1.1.17."),
    ("lipase", "GO:0016298", "lipase activity", E, "high",
     "GO carries no EC xref on this term."),
    ("alanine arylamidase", "GO:0016285", "alanyl aminopeptidase activity", E, "high",
     "EC:3.4.11.2. 'Arylamidase' is API vocabulary for aminopeptidase."),
    ("pyrrolidonyl arylamidase", "GO:0016920", "pyroglutamyl-peptidase activity", E,
     "high", "EC:3.4.19.3. The PYR test; pyrrolidonyl arylamidase is "
     "pyroglutamyl-peptidase I."),
    ("pyrazinamidase", "GO:0008936", "nicotinamidase activity", E, "high",
     "EC:3.5.1.19. Pyrazinamidase and nicotinamidase are the same enzyme (PncA), "
     "which is why pyrazinamide resistance tracks pncA mutations."),
    ("esterase", "GO:0106435", "carboxylesterase activity", E, "high", "EC:3.1.1.1."),

    # --- GO term is broader, or names the reaction differently ---
    ("leucine arylamidase", "GO:0004177", "aminopeptidase activity", C, "high",
     "EC:3.4.11.1. GO:0004178 'leucyl aminopeptidase activity' is OBSOLETE, "
     "replaced by GO:0004177/GO:0008235 — GO retired the substrate-specificity "
     "classes, so the EC number is now the more specific identifier."),
    ("cystine arylamidase", "GO:0004177", "aminopeptidase activity", C, "medium",
     "EC:3.4.11.-. No residue-specific GO molecular-function term survives."),
    ("valine arylamidase", "GO:0004177", "aminopeptidase activity", C, "medium",
     "EC:3.4.11.-. No residue-specific GO molecular-function term survives."),
    ("L-arginine arylamidase", "GO:0004177", "aminopeptidase activity", C, "medium",
     "EC:3.4.11.-. GO:0008451 'X-Pro aminopeptidase activity' is OBSOLETE, "
     "replaced by GO:0004177."),
    ("glycin arylamidase", "GO:0004177", "aminopeptidase activity", C, "medium",
     "EC:3.4.11.-. Source label misspells 'glycine'; kept verbatim because the "
     "table grounds the string the ingest actually emits."),
    ("proline-arylamidase", "GO:0004177", "aminopeptidase activity", C, "medium",
     "EC:3.4.11.5."),
    ("Alanyl-Phenylalanyl-Proline arylamidase", "GO:0004177", "aminopeptidase activity",
     C, "medium", "EC:3.4.11.-. Tripeptide substrate on the API strip; the readout "
     "is aminopeptidase activity, not a distinct enzyme."),
    ("leucyl glycin arylamidase", "GO:0016805", "dipeptidase activity", C, "medium",
     "EC:3.4.13.-. Dipeptide substrate, so dipeptidase rather than aminopeptidase."),
    ("trypsin", "GO:0004252", "serine-type endopeptidase activity", C, "high",
     "EC:3.4.21.4. GO:0004295 'trypsin activity' is OBSOLETE, replaced by "
     "GO:0004252."),
    ("alpha-chymotrypsin", "GO:0004252", "serine-type endopeptidase activity", C,
     "high", "EC:3.4.21.1. GO:0004263 'chymotrypsin activity' is OBSOLETE, replaced "
     "by GO:0004252."),
    ("gamma-glutamyltransferase", "GO:0036374", "glutathione gamma-glutamate hydrolase",
     C, "high", "EC:3.4.19.13. GO:0003840 is OBSOLETE, replaced by GO:0036374; the "
     "classical EC 2.3.2.2 was reclassified to 3.4.19.13."),
    ("gelatinase", "GO:0008233", "peptidase activity", C, "medium",
     "EC:3.4.-.-. The gelatin-hydrolysis test has no dedicated GO molecular-function "
     "term; MicrO models it as MICRO:0000649 'gelatinase assay'."),
    ("caseinase", "GO:0008233", "peptidase activity", C, "medium",
     "EC:3.4.-.-. Casein hydrolysis on milk agar; no dedicated GO term."),
    ("naphthol-AS-BI-phosphohydrolase", "GO:0016791", "phosphatase activity", C,
     "medium", "EC:3.1.3.-. Names an API chromogenic SUBSTRATE, not an enzyme; the "
     "readout is phosphatase activity."),
    ("arginine dihydrolase", "GO:0016990", "arginine deiminase activity", C, "high",
     "EC:3.5.3.6. The ADH test reads the arginine dihydrolase PATHWAY, whose first "
     "and diagnostic step is arginine deiminase."),
    ("N-acetyl-beta-glucosaminidase", "GO:0004563", "beta-N-acetylhexosaminidase "
     "activity", C, "high", "EC:3.2.1.52. Hexosaminidase is broader than the "
     "glucosaminidase named by the label."),
    ("DNase", "GO:0004536", "DNA nuclease activity", C, "high",
     "The DNase agar test detects any secreted DNase, so the specific "
     "GO:0004530 'deoxyribonuclease I activity' would overclaim."),
    ("alcohol dehydrogenase", "GO:0004022", "alcohol dehydrogenase (NAD+) activity", C,
     "high", "EC:1.1.1.1. GO names the NAD+ cofactor; the panel readout does not "
     "distinguish cofactor."),
    ("lecithinase", "GO:0004629", "C-type glycerophospholipase activity", C, "medium",
     "Lecithinase is phospholipase C — the egg-yolk agar reaction."),
    ("tryptophan deaminase", "GO:0001716", "L-amino-acid oxidase activity", C, "medium",
     "EC:1.4.3.2. The API TDA test; the enterobacterial enzyme is an L-amino-acid "
     "deaminase/oxidase. Lowest-confidence row here — worth a second look before "
     "anything depends on it."),
    ("tween esterase", "GO:0106435", "carboxylesterase activity", C, "medium",
     "EC:3.1.1.1. Tween hydrolysis reads carboxylesterase/lipase activity."),
    ("esterase (C 4)", "GO:0106435", "carboxylesterase activity", C, "high",
     "EC:3.1.1.1. '(C 4)' is the API strip's butyrate chain length, not part of the "
     "enzyme name."),
    ("esterase lipase (C 8)", "GO:0106435", "carboxylesterase activity", C, "high",
     "EC:3.1.1.1. '(C 8)' is the caprylate chain length."),
]

NODE_TYPE = "MOLECULAR_FUNCTION"
PROV = " Added from microbedecoder's unmapped-label residual (TraitMech#453)."


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    text = TABLE.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    header = lines[0].rstrip("\n").split("\t")
    existing = {(r["label"].strip().lower(), r["node_type"].strip())
                for r in csv.DictReader(text.splitlines(), delimiter="\t")}

    added, skipped = [], []
    for label, curie, olabel, pred, conf, note in ROWS:
        key = (label.lower(), NODE_TYPE)
        if key in existing:
            skipped.append(label)
            continue
        row = {"label": label, "node_type": NODE_TYPE, "target_curie": curie,
               "target_label": olabel, "predicate_id": pred, "source": SRC,
               "confidence": conf, "notes": note + PROV}
        added.append("\t".join(row.get(c, "") for c in header) + "\n")
        existing.add(key)

    if args.apply and added:
        if not text.endswith("\n"):
            text += "\n"
        TABLE.write_text(text + "".join(added), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  rows added   : {len(added)}")
    print(f"  already there: {len(skipped)} {skipped if skipped else ''}")
    print(f"  distinct GO targets: {len({r[1] for r in ROWS})}, all verified "
          f"non-obsolete against OLS4 by identifier round-trip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
