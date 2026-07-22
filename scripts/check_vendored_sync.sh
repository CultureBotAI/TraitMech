#!/usr/bin/env bash
# Drift check for the vendored byte-identical id↔label files.
#
# Canonical source: culturebotai-claw, shared/idlabel/. claw is private, so
# rather than a network fetch this diffs against a LOCAL sibling checkout of
# claw. A Mech that edits its vendored copy fails this check because the
# reference lives in another repo.
#
# Resolution order for the claw checkout:
#   1. $CLAW_ROOT (if set) — must contain shared/idlabel/
#   2. the usual sibling locations (../culturebotai-claw, ../../…) so this works
#      from a flat Mech (TraitMech/) and a nested one (CommunityMech/CommunityMech/)
#
# If no claw checkout is found (e.g. a CI runner without it), the check SKIPS
# and exits 0 — enforcement is LOCAL, for anyone doing cross-Mech work with the
# sibling checkout. It is NOT enforced in CI while claw is private. Making claw
# public again lets this revert to a pinned raw-fetch that CI can run.
#
# Dependency-free: bash + diff only.
set -euo pipefail

FILES=(
  scripts/validate_id_label_correspondence.py
  scripts/chem_formula.py
  tests/test_id_label_empty_adapter.py
  tests/test_id_label_unknown_prefix.py
  tests/test_id_label_plausibility.py
)

# Locate the canonical claw checkout.
canon_dir=""
if [ -n "${CLAW_ROOT:-}" ] && [ -d "${CLAW_ROOT}/shared/idlabel" ]; then
  canon_dir="${CLAW_ROOT}/shared/idlabel"
else
  for cand in ../culturebotai-claw ../../culturebotai-claw ../../../culturebotai-claw; do
    if [ -d "$cand/shared/idlabel" ]; then canon_dir="$cand/shared/idlabel"; break; fi
  done
fi

if [ -z "$canon_dir" ]; then
  echo "SKIP: culturebotai-claw checkout not found (set CLAW_ROOT to its path)."
  echo "  Cross-repo vendored-drift is NOT enforced here (claw is private)."
  echo "  Run locally alongside a claw checkout to enforce."
  exit 0
fi

# If the checkout is a git repo, report which claw commit we're comparing to,
# and warn (do not fail) when it differs from the recorded ref.
ref_note=""
if command -v git >/dev/null 2>&1 && git -C "$canon_dir" rev-parse HEAD >/dev/null 2>&1; then
  head="$(git -C "$canon_dir" rev-parse --short HEAD)"
  ref_note=" (claw@${head})"
  if [ -f scripts/.vendored_canon_ref ]; then
    want="$(tr -d '[:space:]' < scripts/.vendored_canon_ref)"
    have="$(git -C "$canon_dir" rev-parse HEAD)"
    if [ -n "$want" ] && [ "$want" != "$have" ]; then
      echo "NOTE: local claw is at ${have:0:8}, .vendored_canon_ref pins ${want:0:8}."
      echo "  Comparing against the local checkout; 'git -C <claw> checkout ${want:0:8}' to match the pin."
    fi
  fi
fi

fail=0
for f in "${FILES[@]}"; do
  [ -f "$f" ] || { echo "MISSING: $f not present locally"; fail=1; continue; }
  canon="$canon_dir/$f"
  [ -f "$canon" ] || { echo "ERROR: canonical $canon missing in claw checkout"; fail=1; continue; }
  if ! cmp -s "$canon" "$f"; then
    echo "DRIFT: $f differs from claw canonical$ref_note"; fail=1
  fi
done

if [ "$fail" -eq 0 ]; then
  echo "OK: all ${#FILES[@]} vendored files match claw canonical$ref_note"
else
  echo ""
  echo "To resolve: copy the canonical files from ${canon_dir}/, and if claw"
  echo "intentionally changed them, bump scripts/.vendored_canon_ref to the new claw commit."
  exit 1
fi
