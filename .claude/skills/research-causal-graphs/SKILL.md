---
name: research-causal-graphs
description: Deep-research a trait's causal mechanism against the literature and compare it to the trait's existing causal_graphs. Defaults to the Edison Scientific platform (`edison`, a TraitMech alias for deep-research-client's `falcon`). Use when asked to research a trait mechanism, audit causal-graph completeness, find missing mechanism steps, or run/resume the batch trait-graph research sweep.
---

# Deep research for trait causal graphs

Runs literature deep research on TraitMech traits and uses the result to
assess whether each trait's `causal_graphs` capture the mechanism the
literature actually describes.

This is **paid, networked work**. Every real call costs money. Always dry-run
first, and never launch the full 343-trait sweep without the user explicitly
asking for it.

## Provider: "Edison" means `--provider falcon`

There is no `edison` provider. `deep-research-client` (0.2.4) offers
`perplexity, openai, falcon, asta, consensus, mock, cyberian, openscientist`,
and asking it for `edison` returns `ERROR - Unknown provider: edison`.

Falcon **is** the Edison research agent. The `edison_client` SDK talks to
`api.platform.edisonscientific.com`, and every job name it exposes is
`job-futurehouse-*` (`job-futurehouse-paperqa3`, `job-futurehouse-phoenix`, …)
— Edison Scientific and FutureHouse are the same platform, not two vendors.
Accordingly the client documents falcon's credential as:

```
Provider: falcon
Required: EDISON_API_KEY
```

TraitMech therefore accepts **`edison` as a provider alias**, resolved to
`falcon` by `research_trait.resolve_provider()`. It is the default everywhere:
`just research-trait <category> <slug>` and `run_trait_graph_audit.py` both use
it without being told. The alias resolves *before* output filenames are built,
so results stay in the existing `-deep-research-falcon.md` namespace and the ten
already-researched traits still count as done.

## Preflight

```bash
just research-provider falcon      # should print "Available", not "missing API key"
```

`EDISON_API_KEY` lives in `.env`. `just` injects it via `set dotenv-load := true`;
a bare `uv run` does **not**, so always drive this through `just` or export the
key first.

> **Preflight alone is not proof the run will work.**
> `just research-provider falcon` invokes `deep-research-client` directly and
> never calls `research_trait.research_env()`, so it can report **Available**
> while a real run — which does go through `research_env()` — fails to
> authenticate. Confirm the actual path before a paid batch:
>
> ```bash
> just research-trait <category> <slug> --dry-run
> ```
>
> A now-reverted change once made `research_env()` drop the Edison variable for
> falcon in favour of a FutureHouse-named one that is set nowhere, on the theory
> that it kept one vendor's secret away from another. The two are the same
> platform, so that removed the only working path while preflight still looked
> green. If research starts failing to authenticate, read `research_env()` first.

## Single trait

```bash
just research-trait <category> <slug> --dry-run     # provider defaults to edison
just research-trait <category> <slug>
just research-trait <category> <slug> --provider openai   # override
```

Writes `research/traits/<category>/<slug>-deep-research-falcon.md` plus a
`.citations.md` sidecar. `research/` is gitignored — these are inputs to
curation, not artifacts to commit.

## Batch sweep

`scripts/run_trait_graph_audit.py` enumerates every `REVIEWED` `term_kind: CLASS`
trait that already has a causal graph (353 traits; 10 already researched).

```bash
uv run python scripts/run_trait_graph_audit.py --dry-run
uv run python scripts/run_trait_graph_audit.py --limit 8          # pilot first
uv run python scripts/run_trait_graph_audit.py --category metabolism
uv run python scripts/run_trait_graph_audit.py --provider openai  # non-default
```

It is **resumable** (skips traits whose output file exists), **fail-soft** (one
failure doesn't stop the batch), and appends status rows to
`reports/trait_graph_audit_manifest.tsv`. Start with `--limit` and inspect the
output quality before committing to a long run. `--workers` >1 raises spend rate
and rate-limit risk; leave it at 1 unless asked.

## Turning research into graph changes

The research note is evidence, not a patch. For each trait:

1. Read the note against the trait's existing `causal_graphs`.
2. Identify mechanism steps the literature describes that the graph lacks, and
   graph claims the literature does not support.
3. Propose edges/nodes with citations. **Every `CausalEdge` requires edge-level
   `evidence`** — schema-enforced, since mechanism assertions carry no METPO
   provenance of their own.
4. Ground new nodes per `docs/GROUNDING_POLICY.md`. For `GENE_OR_PROTEIN`
   nodes, match the identifier type to the node's semantics — GO MF `…activity`
   for a function, GO CC `…complex` for a complex, InterPro for a family — and
   do **not** ground a taxon-agnostic node to one organism's UniProt accession.
   That mistake is what produced 162 dead groundings the repo just retracted.
5. Validate: `just validate-strict` and `just audit-graphs` must both stay at
   zero errors.

Never write a causal edge whose only support is the research note's prose
without a resolvable citation behind it — Falcon output includes a citations
sidecar; use it.

## Related

- `templates/trait_causal_graph_research.md` — the prompt template
- `docs/GROUNDING_POLICY.md` — node grounding rules
- `docs/CURATION_PLAYBOOK.md` — general curation workflow
