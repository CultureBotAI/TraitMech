# METPO Proposal v445: Lamassu-HNH System

Reserve `METPO:1052200` for `traitmech:000568`, a GENOMICS class for
organism-level possession of a short-LmuB Lamassu locus with HNH-domain LmuA
and LmuC. The parent is `METPO:1018600`, reserved for Lamassu system
(`traitmech:000232`) in v109. This is one Scope A class; no properties,
schema vocabulary, or external equivalence mappings are proposed.

## Evidence and Scope

- [Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122), Results and
  Figure 1A, identify HNH as a short-Lamassu effector type. This supports a
  recognized biological architecture, not a new trait for an individual HMM.
- [Dataset S1](https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx)
  supplies 281 unique HNH-system calls, all with short LmuB. The canonical
  example links three mandatory hits in `S3_Lamassu_Detection` rows 121-123
  to assembly `GCF_009892245.1` in `S2_Genomes` row 1159.
- [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_009892245.1/dataset_report)
  resolves that assembly to Acinetobacter haemolyticus AN59, species taxon
  `NCBITaxon:29430`. This verifies identity; the published dataset supplies
  the computational genomic-possession evidence.
- The [executable DefenseFinder model](https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/Lamassu-Fam/Lamassu_HNH.xml)
  requires HNH-domain LmuA, LmuB and LmuC with exchangeable profiles.
  Unlike the study's observed architecture, it accepts either long or short
  LmuB. Its model key is therefore related, not exactly equivalent.

The same pinned repository's legacy summary rules and HMM inventory lack
HNH entries despite the executable model and HNH profile being present.
The executable XML was parsed directly rather than inferring model absence
from those summaries. Protein names, isolated HNH-profile hits, and HNH
molecular activity do not denote the organism-level trait. No exact xref or
protein accession is proposed. The AN59 example is explicitly computational,
not species-wide possession or experimentally measured antiviral activity.
HNH-specific functional validation and molecular mechanism remain open;
Cap4 and Lipase experiments are not transferred to this effector type.

## Identity and Round Trip

Pre-write searches included ignored and hidden files across the repository,
including METPO, records, proposals, research, generated pages and history.
No exact record or METPO term was found. The local ID, placeholder ID, slug
and v445 cohort were unused; the highest preceding cohort was v444
(`METPO:1052100`). The broader Lamassu record is retained as the parent.

Subset: `metpo_traitmech_2026_10`. The companion ROBOT template is generated
from the same definition and synonyms as the TraitRecord by
`scripts/add_lamassu_hnh_system_trait.py`. Only the related-synonym column
contains the software keys; no SSSOM equivalence is proposed.

Submit the template for upstream review via berkeleybop/metpo#535. After
acceptance, replace `traitmech:000568` with the assigned METPO ID and retain
the local identifier in migration provenance. Until human review, the local
record remains `PROPOSED`.
