# Deep-research providers

This Mech supports three first-class deep-research lanes:

- `openscientist` through `deep-research-client`;
- `codex` through the native `codex exec` contract in
  `scripts/deep_research_contract.py`;
- `rosalind` (OpenAI GPT-Rosalind) through `deep-research-client`'s `openai`
  provider with an explicit model id.

The default sweep provider, `edison` (`falcon`), is documented in
`.claude/skills/research-causal-graphs/SKILL.md`.

Codex is intentionally not routed through the client's `cyberian` adapter.
The native command explicitly enables web search, runs ephemerally in a
read-only sandbox, requires a JSON-schema response, validates report length and
distinct HTTP(S) sources, and publishes atomically only after validation.

## Credentials

Codex uses the local Codex CLI login. Run `codex login status`; no API key is
stored in this repository.

OpenScientist requires:

```bash
export OPENSCIENTIST_API_KEY='name:secret'
# Optional; this is the default:
export OPENSCIENTIST_URL='https://www.openscientist.io'
```

The `name:secret` shape is required by the fleet contract. Never commit either
value or print it in logs.

GPT-Rosalind requires an OpenAI API key for an organisation admitted to
OpenAI's trusted-access program for the model:

```bash
export ROSALIND_API_KEY='...'   # preferred; overrides OPENAI_API_KEY for this lane
# or, if the general-purpose key IS the Rosalind key:
export OPENAI_API_KEY='...'
# Optional; defaults to the id in scripts/research_trait.py:
export ROSALIND_MODEL='gpt-rosalind'
```

`ROSALIND_API_KEY` deliberately overrides rather than fills in
`OPENAI_API_KEY`: a general-purpose OpenAI key in the shell must not silently
take a Rosalind call to an organisation that has no access to the model. The
key is read by `research_trait.research_env()` and never written by TraitMech
tooling.

## GPT-Rosalind lane

`rosalind` is a TraitMech provider name, not a `deep-research-client` provider.
`scripts/research_trait.py` resolves the aliases `gpt-rosalind` and
`gpt_rosalind` to it, writes the report to
`research/traits/<category>/<slug>-deep-research-rosalind.md`, and invokes the
client as `--provider openai --model <ROSALIND_MODEL>`. The report namespace is
kept separate from `-deep-research-openai.md` on purpose: an o3-deep-research
report and a GPT-Rosalind report are different evidence and must never satisfy
each other's resume check in `scripts/run_trait_graph_audit.py`.

What the lane exposes is what the client's `openai` provider exposes: one
Responses API call with web search enabled, the prompt template rendered from
the trait record, and a markdown answer. It carries no code-execution or
database tools, so treat its citations exactly like Falcon's: resolve every
DOI before curating from it.

Two reports in the `rosalind` namespace predate the lane. They were pasted in
by the maintainer from a GPT-Rosalind session and declare
`pipeline_run: false` in their front matter. That flag is what keeps them out
of the sweep's resume check and orphan gate; do not remove it, and do not
write it on a report the pipeline produced.

`scripts/deep_research_contract.py` is vendored and cannot carry a Rosalind
canary, so the lane has its own: `scripts/research_rosalind_canary.py`.

## Canary sequence

Run the non-billing checks first:

```bash
just deep-research-canary codex
just deep-research-canary openscientist
just rosalind-canary
```

The Codex canary verifies CLI authentication and support for native web search,
output schema, and last-message capture. The OpenScientist canary validates the
credential shape and confirms that `deep-research-client providers` discovers
the provider. It does not submit a hosted job.

The Rosalind canary makes one authenticated but unbilled call, listing the
models the credential may use, and fails unless the requested model id is among
them. That is the check that matters for this lane: the model is gated by
org-level trusted access, so a key can authenticate and still be refused the
model. It prints any Rosalind ids the credential does see, which is how a
renamed or snapshotted preview id is corrected (set `ROSALIND_MODEL`). It then
confirms `deep-research-client` discovers `openai` under the same environment
`research_env()` gives a real run. It cannot see quota or rate limits; only
the first real trait can.

Before any batch or paid run, execute one real target, inspect the report and
its cited sources, and only then authorize a bounded batch. Research artifacts
are curator inputs; they never update records automatically.

## Canonical pin

`scripts/deep_research_contract.py` is vendored byte-for-byte from the
canonical `CultureBotAI/culturebotai-claw` artifact. Fleet-governed Mechs pin
it through `scripts/.vendored_canon_ref`; repositories outside that manifest
use `scripts/.deep_research_contract_ref`. Do not let local copies evolve
independently.
