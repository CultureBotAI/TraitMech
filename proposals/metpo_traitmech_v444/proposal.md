# METPO Proposal v444: Lamassu Hydrolase-Protease System

Reserve `METPO:1052100` for `traitmech:000567`, a GENOMICS class for
possession of a paired hydrolase/protease Lamassu defense locus with LmuB and
LmuC. The parent is `METPO:1018600`, reserved for Lamassu system
(`traitmech:000232`) in v109. This is one Scope A class; no properties,
schema vocabulary, or external equivalence mappings are proposed.

## Evidence and Scope

- [Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122) describe the
  paired architecture and identify the validated B. cereus B4077 system.
- [Millman et al.](https://doi.org/10.1016/j.chom.2022.09.017), Figure 2,
  provide the experimental context for the paired system. Exact substrates
  and activation order remain unresolved.
- The [executable DefenseFinder model](https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/Lamassu-Fam/Lamassu_Hydrolase-Protease.xml)
  requires protease, hydrolase, LmuB and LmuC components with listed
  exchangeable profiles. Its companion summary TSV instead describes three
  mandatory matches with accessory LmuC and older profile names. The trait
  follows the biological architecture, not those stale summary thresholds.

The existing Lamassu-Hydrolase and Lamassu-Protease records follow separate
legacy table rules that each forbid the other's effector profile. They do not
represent the paired locus and are not asserted as equivalent or parent terms.
Their reconciliation with executable models remains a parent-record TODO.
Source model keys are related synonyms, not exact synonyms. Protein names,
hydrolase activity, protease activity, and profile hits alone do not denote
this organism-level trait. No protein accession or exact external xref is
proposed. The example is restricted to strain B4077 using `NCBITaxon:1396`;
it does not assert species-wide possession or native-host assay results.

## Identity and Round Trip

Pre-write searches included ignored and hidden files across the repository,
including METPO, records, proposals, research, generated pages and history.
The paired label appeared only in pending parent discussions and their
provenance; the candidate local ID, placeholder ID, slug and v444 cohort were
unused. The highest preceding cohort was v443 (`METPO:1052000`).

Subset: `metpo_traitmech_2026_10`. The companion ROBOT template is generated
from the same definition and synonyms as the TraitRecord by
`scripts/add_lamassu_hydrolase_protease_system_trait.py`.

Submit the template for upstream review via berkeleybop/metpo#535. After
upstream acceptance, replace `traitmech:000567` with the assigned METPO ID
and retain the local identifier in migration provenance. Until human review,
the local record remains `PROPOSED`.
