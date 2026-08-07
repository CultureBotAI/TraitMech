# Verification Suite & Common Pitfalls

*Reference for the **metpo-proposal** skill — see [`../SKILL.md`](../SKILL.md) for the overview, scopes, ID-space conventions, and workflow.*

---

### 5. Verify

```bash
# Convenience wrapper (recommended)
just verify-proposal <cohort>

# Manual equivalents:

# Column-count sanity (must print nothing)
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_properties_robot.tsv

# Enum coverage (Scope C only) — every CausalNodeTypeEnum value should appear
# as a leaf row whose definition_source matches the enum value.
uv run python -c "
import re, yaml
schema = yaml.safe_load(open('src/traitmech/schema/traitmech.yaml'))
values = list(schema['enums']['CausalNodeTypeEnum']['permissible_values'])
tsv = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').read()
missing = [v for v in values if f'CausalNodeTypeEnum.{v}' not in tsv]
print('Missing leaves:', missing or 'none')
"

# Scope-A citations — every traitmech:NNNNNN a cohort CITES resolves to a real
# record. Whole-corpus coverage is NOT a per-cohort property: v5 lifts the
# synthetic traits, v1/v3/v7 lift other things, and demanding it of every cohort
# failed three of them permanently over work they never took on (#319).
just verify-proposal <cohort>          # per-cohort: citations resolve

# The cross-cohort property, asserted once over the union of all cohorts and
# part of `just qc`:
just audit-proposal-coverage           # every corpus id is lifted by SOME cohort

# definition_source hygiene (issue #83) — column 4 must be a citation, never
# a cross-ontology equivalence IRI. This must print nothing.
uv run python -c "
import csv, glob, re
EQUIV = re.compile(r'^(OMP|MICRO|PATO|GO|CHEBI|ENVO|EFO|SO|PR|UBERON|CL|RO|OBI):', re.I)
bad = []
for f in glob.glob('proposals/<cohort>/metpo_proposal_*_robot.tsv'):
    rows = list(csv.reader(open(f), delimiter='\t'))
    for r in rows[2:]:
        if len(r) > 3 and r[3]:
            for tok in r[3].split('|'):
                if EQUIV.match(tok.strip()):
                    bad.append((f, r[0], tok.strip()))
print('definition_source equivalence leaks:', bad or 'none')
"

# Parent integrity — every SC % parent resolves in-file or to a known METPO IRI
uv run python -c "
import re
tsv = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').read().splitlines()[2:]
ids_in_file = {r.split('\t')[0] for r in tsv}
parents = {r.split('\t')[4] for r in tsv if r.strip()}
external_ok = re.compile(r'^METPO:\d+$')
missing = [p for p in parents if p not in ids_in_file and not external_ok.match(p)]
print('Parents missing locally:', missing or 'none')
"
```

For full ROBOT + ELK validation use the wrapper, which mirrors the
canonical kg-microbe `validate_with_robot()` invocation
(`kg-microbe/scripts/extract_metpo_proposals.py:1643`):

```bash
just robot-validate-proposal <cohort>
```

The wrapper auto-discovers the `robot` binary in this order:
`$ROBOT` → `$ROBOT_BIN` → `which robot` → `../kg-microbe/data/raw/robot`.
It compiles the classes TSV (and the properties TSV if present), merges
with `data/raw/metpo.owl`, and runs ELK with axiom-generators `SubClass
EquivalentClass`. OWL artifacts land in `reports/robot/<cohort>/`.

Pass criteria: all `robot` commands exit zero with no `UNSAT` warnings.
A reasoned output line count much larger than the merged input signals
unintended inferred equivalences (the wrapper prints a WARN at +200
lines) — investigate before submitting.

If you need to run the raw commands yourself (e.g. for prefix tweaks
not yet in the wrapper):

```bash
robot template --template proposals/<cohort>/metpo_proposal_classes_robot.tsv \
    --prefix "METPO: http://purl.obolibrary.org/obo/METPO_" \
    --prefix "biolink: https://w3id.org/biolink/vocab/" \
    --prefix "RO: http://purl.obolibrary.org/obo/RO_" \
    --output /tmp/classes.owl
robot template --template proposals/<cohort>/metpo_proposal_properties_robot.tsv \
    --prefix "METPO: http://purl.obolibrary.org/obo/METPO_" \
    --prefix "biolink: https://w3id.org/biolink/vocab/" \
    --output /tmp/properties.owl
robot merge --input data/raw/metpo.owl --input /tmp/classes.owl --input /tmp/properties.owl \
    --output /tmp/merged.owl
robot reason --reasoner ELK --input /tmp/merged.owl \
    --axiom-generators "SubClass EquivalentClass" --output /tmp/reasoned.owl
```


---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| `awk` reports row 2 has 8/9 columns | Trailing tabs missing on ROBOT header | Append `\t\t\t` to row 2 (see step 4) |
| ROBOT error "subject of axiom is not a class" | Property row referencing a class IRI in the `RANGE` column when ROBOT expects a class declaration | Declare the range class as its own row in the classes TSV first |
| ELK reports unsatisfiable class | Intermediate parent created with conflicting `SC %` axioms | Inspect the parent chain — usually a copy-paste error in the `parent` column |
| Copilot flags "schema lifted incorrectly" | The leaf's definition doesn't match the schema enum's description verbatim | Copy the schema description into the `definition` column, *then* edit only for Aristotelian form. Reword more freely in the proposal narrative. |
| Reviewer asks for an existing METPO ID | The lifted concept already exists in METPO under a different label | Use the existing IRI; remove the row from the proposal; record the alias in the next seeder run so the `traitmech:` ID gets retired. |
| `traitmech:` ID in `data/traits/` is in NO cohort's TSV | Coverage gap — the id has no METPO home, so it cannot be cross-referenced from kg-microbe | `just audit-proposal-coverage` names it; add a row to a Scope-A cohort (v5 is the existing one). Not a per-cohort failure (#319). |
| A cohort cites a `traitmech:` ID that no record has | Typo, or a citation left behind after a record was renamed or removed | `just verify-proposal <cohort>` names it; fix the citation. |
| An ontology IRI (`OMP:`, `PATO:`, `GO:`, …) sits in `definition_source` (col 4) | Cross-ontology equivalence mistaken for definition provenance (issue #83) | Move it: lightweight hint → `xrefs` (`hasDbXref`); semantic alignment → `metpo_proposal_mappings.sssom.tsv` with a `skos:*Match`. Keep col 4 for citations only. Catch with the `definition_source` hygiene check in step 5. |
| `CausalNodeTypeEnum` value renamed but proposal still cites old name | Schema drift after proposal was drafted | Use Path C (new cohort version) if v1 is merged; Path A otherwise. |

