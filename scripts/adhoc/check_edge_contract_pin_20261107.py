"""Check the optional CLAW runtime origin and pin for #767, 2026-11-07.

Inputs: an explicit CLAW checkout and the imported native contract module.
Output: verified shared commit and package origin; no repository mutation.
"""

import argparse
import inspect
import subprocess
from pathlib import Path

from kg_microbe_curation import native
from kg_microbe_reviews import load_document

from traitmech.edge_curation import CLAW_COMMIT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claw-root", type=Path, required=True)
    args = parser.parse_args()
    checkout = args.claw_root.resolve()
    if Path(native.__file__).resolve().parent != checkout / "src/kg_microbe_curation":
        raise ValueError("Native contract was imported from an unexpected checkout")
    loader = Path(inspect.getsourcefile(load_document)).resolve()
    if loader != checkout / "src/kg_microbe_governance/artifacts/scripts/record_review.py":
        raise ValueError("Native YAML loader was imported from an unexpected checkout")
    head = subprocess.check_output(["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True).strip()
    if head != CLAW_COMMIT or native.NATIVE_CONTRACT != "kg-microbe-native-assertion/v1":
        raise ValueError("Shared contract differs from the immutable adapter pin")
    origin = subprocess.check_output(["git", "-C", str(checkout), "remote", "get-url", "origin"], text=True).strip()
    if origin not in {"https://github.com/CultureBotAI/culturebotai-claw.git",
                      "https://github.com/CultureBotAI/culturebotai-claw",
                      "git@github.com:CultureBotAI/culturebotai-claw.git"}:
        raise ValueError("Unexpected shared contract repository")
    changed = subprocess.check_output([
        "git", "-C", str(checkout), "status", "--porcelain", "--",
        "src/kg_microbe_curation", "src/kg_microbe_reviews",
        "src/kg_microbe_governance",
    ], text=True)
    if changed:
        raise ValueError("Shared contract source has uncommitted changes")
    print(f"Verified CLAW {head}; {native.NATIVE_CONTRACT}")


if __name__ == "__main__":
    main()
