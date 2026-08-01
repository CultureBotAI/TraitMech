# Agent identity: why agents cannot yet write

This is the gate on real autonomy in this fleet. Everything else in phase 0 is
done; this is not, and it **cannot be done by an agent** — GitHub has no API for
creating a GitHub App. There is no `POST /orgs/{org}/apps`, and the only
programmatic route, the app-manifest conversion flow, requires a browser
round-trip with a temporary code. Someone has to click.

Until then, `pr-shepherd` is comment-only. That is the correct scope, not a
stub.

## The two problems

### 1. `GITHUB_TOKEN` pushes do not trigger workflows

This is deliberate on GitHub's part — it prevents infinite CI loops. The
consequence for us is worse than the loop it prevents:

> An agent pushes a fix commit to a PR branch using the built-in token. No
> workflow runs. The PR shows **green because nothing evaluated it**, not
> because anything passed.

A human reviewer sees green checks and reasonably infers the change was
validated. This repo has been bitten repeatedly by checks that silently did not
run — `check_vendored_sync.sh` skipping when a checkout was absent (TraitMech
#182), a `paths:` filter narrower than the files it guarded
(MediaIngredientMech#160, CommunityMech#280, TraitMech#184), and a nightly
cross-repo job pointed at a directory that never existed, masked by a trailing
`|| true`. Adding an agent that produces green-because-unrun PRs would be the
same failure with a faster clock.

An App token is a different principal, so a push made with one **does** fire the
`pull_request: synchronize` event and the normal checks run.

### 2. One identity means the bot can approve itself

With a single agent identity, the actor that writes a change can approve it.
That is not review; it is a signature loop. Two Apps make self-approval
structurally impossible rather than merely discouraged.

## What to create

Two org-owned GitHub Apps. They must be **owned by CultureBotAI**, not by
Anthropic — minting a token with `actions/create-github-app-token` requires the
App's private key, and we do not have Anthropic's. The `claude` App already
installed on the org (app id `1236702`) is Anthropic's and cannot serve this
purpose; it backs `@claude` mentions, which is a different thing.

### `culturebot-agent` — the writer

Repository permissions:

| Permission | Level | Why |
|---|---|---|
| Contents | Read & write | push branches |
| Pull requests | Read & write | open PRs, comment |
| Issues | Read & write | file and update issues |
| Actions | Read | read check results |
| Metadata | Read | mandatory |

**Not** granted: Administration, Workflows, Secrets, Members. An agent that can
edit `.github/workflows/` can rewrite its own guardrails, which defeats the
point of having them.

### `culturebot-reviewer` — the reviewer

| Permission | Level | Why |
|---|---|---|
| Pull requests | Read & write | submit reviews, comment |
| Contents | Read | read the diff |
| Actions | Read | read check results |
| Metadata | Read | mandatory |

**Not** granted: Contents write. The reviewer must be unable to change what it
is reviewing.

## Setup

1. Create both Apps at `https://github.com/organizations/CultureBotAI/settings/apps/new`,
   with the permissions above. Uncheck "Active" under Webhook — neither App needs
   to receive events.
2. Install both on the org, scoped to the five Mech repos plus `culturebotai-claw`.
3. Generate a private key for each and download the `.pem`.
4. Add four **org secrets**, visibility "All repositories":
   - `AGENT_APP_ID`, `AGENT_APP_PRIVATE_KEY`
   - `REVIEWER_APP_ID`, `REVIEWER_APP_PRIVATE_KEY`
5. Delete the downloaded `.pem` files. The secret is the only copy that should
   persist.

## What changes in the workflows afterwards

Mint a short-lived token per run:

```yaml
- name: Generate writer token
  id: writer
  uses: actions/create-github-app-token@v1
  with:
    app-id: ${{ secrets.AGENT_APP_ID }}
    private-key: ${{ secrets.AGENT_APP_PRIVATE_KEY }}

- name: Checkout
  uses: actions/checkout@v4
  with:
    token: ${{ steps.writer.outputs.token }}
    persist-credentials: false   # serve the token via the gh credential helper
```

Then `pr-shepherd`'s prompt can lift its "do not push, do not merge" limits, and
gains one it does not have today: **after pushing a fix commit, do not manually
re-trigger review — the push itself fires `synchronize` and the checks start.**
Re-triggering by hand would double-run them.

Do not grant merge authority in the same change as push authority. Watch pushes
for a while first; merge is the one action with no undo that a human will not
see before it lands.

## Why the reviewer App is not optional

It is tempting to create only the writer and have a human review. That works
until the fleet is producing more PRs than a human reads, which is the point of
the exercise. Creating both now means the second one exists before it is needed,
rather than being added under pressure when the queue is already deep.

## Related

- `culturebotai-claw` `docs/AUTONOMOUS_LOOPS.md` — the design this implements
- `culturebotai-claw` `.github/agent-config.yaml` — model routing
- `culturebotai-claw` `.github/cron-profiles.yaml` — cadence and the kill switch,
  currently `active: "off"`
