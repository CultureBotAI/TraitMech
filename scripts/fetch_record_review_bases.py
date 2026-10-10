"""Recover exact review source commits without changing immutable review bundles."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import record_review as reviews

REF_PREFIX = "refs/record-review-bases/"
ZERO_SHA = "0" * 40


def git(root: Path, *args: str, missing_ok: bool = False) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, text=True,
            timeout=300, env={**os.environ, "GIT_NO_LAZY_FETCH": "1",
                             "GIT_TERMINAL_PROMPT": "0"},
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise reviews.ReviewError(f"Git operation failed: {args[0]}") from exc
    if result.returncode:
        if missing_ok and result.returncode == 1:
            return None
        raise reviews.ReviewError(f"Git operation failed: {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()


def recover(root: Path, *, apply: bool = False) -> dict:
    root = root.absolute()
    identity = reviews.repository_identity(root)
    documents = []
    # Validate every bundle before any network request or Git mutation.
    for relative in reviews.review_paths(root):
        document = reviews.parse_review_bundle(
            relative, reviews.read_bytes(root, relative),
            reviews.read_bytes(root, str(Path(relative).with_name("review.md"))),
        )
        if document["repository"].lower() != identity.lower():
            raise reviews.ReviewError(f"review repository disagrees with origin: {relative}")
        revision = document["source"]["git_revision"]
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise reviews.ReviewError("review source must be an exact lowercase 40-character commit SHA")
        documents.append((relative, document))

    plan = []
    for revision in sorted({doc["source"]["git_revision"] for _, doc in documents}):
        present = git(root, "rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}",
                      missing_ok=True)
        if present is not None and present != revision:
            raise reviews.ReviewError(f"source does not name a commit directly: {revision}")
        ref = REF_PREFIX + revision
        retained = git(root, "rev-parse", "--verify", "--quiet", ref, missing_ok=True)
        if retained is not None and retained != revision:
            raise reviews.ReviewError(f"refusing conflicting retained review base: {ref}")
        plan.append({"revision": revision, "missing": present is None,
                     "retained": retained is not None, "ref": ref})

    for _, document in documents:
        if not next(item["missing"] for item in plan
                    if item["revision"] == document["source"]["git_revision"]):
            provenance = reviews.source_provenance(root, document)
            if provenance["status"] in {"invalid", "unverified"}:
                raise reviews.ReviewError(f"source provenance {provenance['status']}: {provenance['reason']}")

    if apply:
        for item in plan:
            revision, ref = item["revision"], item["ref"]
            if item["missing"]:
                # Only the matching GitHub repository is contacted; no URL or ref
                # is accepted from the review. Fetched content is never executed.
                git(root, "fetch", "--no-tags", "--no-write-fetch-head",
                    "--no-recurse-submodules", f"https://github.com/{identity}.git", revision)
                if git(root, "rev-parse", "--verify", f"{revision}^{{commit}}") != revision:
                    raise reviews.ReviewError(f"fetched source is not the requested commit: {revision}")
            if not item["retained"]:
                git(root, "update-ref", ref, revision, ZERO_SHA)
        for relative, _ in documents:
            reviews.read_review(root, relative)

    return {"repository": identity, "apply": apply, "reviews": len(documents),
            "bases": plan, "status": "validated" if apply else "dry_run"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true",
                        help="fetch missing commits and retain local refs; default is read-only")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(recover(args.repo_root, apply=args.apply), indent=2))
    except (reviews.ReviewError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
