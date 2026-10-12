# Memory of Acquired Stress Resistance

## Scope

Scope A: one physiological class, `traitmech:000712`, used by one new
TraitRecord. Scope B: zero predicates. Scope C: zero schema-enum lifts.
The record remains `PROPOSED`, not human-reviewed. This is an assayable
history-dependent phenotype, not a gene, reporter, individual experiment,
source-database field or precomposed organism-chemical assertion.

The proposed definition is a physiological phenotype in which a microbial
cell or lineage retains elevated resistance to a later stress challenge
after a previous inducing stress has been removed, through persistence of a
non-genetic state. The label and definition match the record verbatim.

## Evidence And Boundaries

[Guan et al. 2012](https://doi.org/10.1534/genetics.112.143016), PMID:22851651,
supports persistence of acquired peroxide resistance after salt removal.
The scientific abstract is distinct from the paper's transcriptional-memory
endpoint. Primary publisher HTML, relevant Methods and Results, actual
Figure 1 and S1/S2 were inspected. The record preserves assay, generation,
normalized-score and engineered daughter-marking qualifications rather than
silently combining those experiments.

[Govers et al. 2018](https://doi.org/10.1371/journal.pbio.2003853), PMID:30153247,
supports greater later heat-shock survival in aggregate-bearing descendants
than in their isogenic aggregate-free siblings. Primary XML, relevant Results
and Methods, actual Figure 4 and S6 were inspected. Figure 4C does not show
improved population-average survival after pretreatment. The native
heat-induced aggregate experiments are separate from synthetic induction
experiments; their time scales and conditions are not interchangeable.
Reporter validation was separately inspected in Figure 1 for the prior
aggregate-inheritance curation. A monomeric reporter label alone does not
establish freedom from artifacts.

Both evidence items carry short, directly matched, contiguous scientific-
abstract snippets. The source-verification sidecar retains primary-file
hashes, source-qualified MED identities, section locators, figure hashes,
notice-check limits and the actual native snippet-resolver disposition.
MED and publisher formula rendering differ for Guan; the selected quote
matches both without rewriting either source.

Persistent resistance is not merely faster transcriptional reactivation or
faster reacquisition after another induction. It need not occur in every
descendant or improve the population mean. Challenge conditions and genetic
background must be matched; persistent fluorescence, aggregate presence,
gene presence or ongoing stress exposure alone is insufficient. No universal
duration, number of generations, stressor identity or mechanism is specified.
Natural canonical taxa and protein-resolved graphs are deferred, not inferred
from laboratory reporters or a shared phenotype.

## Identity And Hierarchy

Use `METPO:1000059` phenotype, not a released stress-memory ID. Stress response
(`traitmech:000078`) concerns sensing and mounting protection. Its research
report includes cross-protection as an output but does not establish
persistence after stress removal. Carbon-source memory (`traitmech:000706`),
cue-triggered environmental anticipation (`traitmech:000707`), diversifying
bet hedging (`traitmech:000708`), persister formation and unequal aggregate
inheritance (`traitmech:000711`) have different defining criteria. Particular
observations can overlap without making these classes equivalent or disjoint.
Existing records are not reparented.

Pinned and current released METPO contain deprecated `METPO:1000293`
(obsolete stress response) and `METPO:1000222` (obsolete oxidative stress
response), below ObsoleteClass with an OMO:0001000 reason annotation and no
replacement or consider annotation in the inspected releases. These broader
lexical neighbors do not define the memory phenotype. Their historical
rationale remains unresolved; neither ID is reactivated or asserted as an
exact xref. No exact active or historical memory class was found in the
inspected ontology and proposal scope. The pinned ontology is unchanged.

Unqualified cellular memory, stress priming and cross-protection are not
exact synonyms. No external equivalence was established, so no xrefs,
SSSOM mappings, exact synonyms or property template are emitted.

## Novelty And Reservations

The pre-write audit used main `8de77540cae640dc1cf4740027187bfc050f07b1`.
Ignored and hidden files were included in all 22 registered TraitMech roots
and five known independent main copies; 18 retained historical tracked trees
were also searched with a positive-controlled PCRE pattern. Structured YAML
normalization covered 1,121 distinct trait versions. A fresh seed projection
had 399 terms, of which 344 were already among 1,106 live records; the 55
remaining exact-ID absences were not treated as accepted novel traits.
Frozen release-review inventories were reconciled rather than reused as a queue.

Fresh paginated PR/file inspections covered TraitMech #1782, #1476, #973 and
draft #924 (692 changed files); CommunityMech #1992 and draft #935; and METPO
#644, #643, #641, #640, #638 and #629. All 20 changed METPO files were read in
full at their immutable blob SHAs, including the range documents. Pending
heads and open sets were stable during each inspection. No competing local
ID, cohort or proposed block was found in the inspected scope.

Upstream heads were METPO `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`,
CommunityMech `80049bcc9195480a58633236169b62f86c23489a`, and KG-Microbe
`82c083a83afafb19b8b9ffd96066be840c18ed97`. KG-Microbe mapping/proposal
selection was checked against its fresh untruncated tree, not assumed
unchanged from an older main. METPO RDF and paginated issues/comments were
also inspected. The reservation audit covered 587 existing cohorts, 7,686
narrower interval occurrences and 128 registered CommunityMech roots.

The formal ADDITIONAL EDITOR namespace envelope in METPO #629 and its quoted
assessment in v587 were distinguished from actual term/cohort reservations.
Each exclusion was guarded by exact file hash and context; narrower current,
historical and retired reservations remained checked. Allocation receipts
retain those raw intervals and adjudications. Recheck immediately before
publication: these observations cannot eliminate concurrent allocation races.

Unavailable historical ignored/untracked bytes cannot be reconstructed.
Archives were not expanded and symlink directories were not traversed. This
is neither a global filesystem search nor a claim of discovery exhaustion.
Research-report mentions of preconditioning remain evidence leads, not
primary snippets or exact curated records.

## ID Space And Round Trip

- Local ID: `traitmech:000712`.
- Cohort: `metpo_traitmech_v588`.
- Full reserved class block: `METPO:1066500`-`METPO:1066599`.
- Only populated placeholder: `METPO:1066500`, not a released ID.
- Subset: `metpo_traitmech_2026_10`.

The append-only hundred block follows v587 without recycling its unused rows.
The class template uses the canonical 11-column, two-header format, with
required trailing empty ROBOT cells. Citations are definition provenance,
not ontology equivalences. METPO placeholders and parents expand to
`https://w3id.org/metpo/`, matching the pinned ontology.

After upstream review and official minting, use a separate reviewed migration
to replace the local ID, update references and mappings, and verify the
seeder round trip by exact ID. Do not emit this placeholder as an already
released METPO term or silently replace the pinned ontology.

## Verification

Run the guarded writer dry run, focused tests, LinkML/strict validation,
native snippet verification, proposal/coverage checks, ROBOT and ELK,
generated-product freshness, repository history validation, full QC and the
full test suite. Inspect actual proposal RDF expansion and rendered identity
provenance. Save immutable structured adversarial review before publication;
supported findings require issues and evidence-backed fixes, not a fabricated
issue count. PR checks and merge-queue checks are separate from local passes.
