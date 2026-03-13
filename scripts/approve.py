#!/usr/bin/env python3
"""Approve or deny a pending ABA action in ACTIONS.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def update_action(root: Path, action_id: str, decision: str) -> tuple[bool, str]:
    """Update the status of an action in ACTIONS.md.

    Returns (success, message).
    """
    actions_path = root / "state" / "ACTIONS.md"
    if not actions_path.exists():
        return False, "ACTIONS.md not found"

    content = actions_path.read_text()
    decision_upper = decision.upper()

    # Find the action section and update its status
    # Pattern: within the ### ACTION-ID section, find Status: PENDING and replace
    pattern = rf"(### {re.escape(action_id)}.*?(?=### |\Z))"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return False, f"Action {action_id} not found in ACTIONS.md"

    section = match.group(1)
    if "PENDING" not in section:
        current = "APPROVED" if "APPROVED" in section else "DENIED" if "DENIED" in section else "unknown"
        return False, f"Action {action_id} is not PENDING (current: {current})"

    updated_section = re.sub(
        r"\*\*Status:\*\* PENDING",
        f"**Status:** {decision_upper}",
        section,
    )
    # Also handle plain "Status: PENDING" format
    updated_section = re.sub(
        r"Status: PENDING",
        f"Status: {decision_upper}",
        updated_section,
    )

    new_content = content[: match.start()] + updated_section + content[match.end() :]
    actions_path.write_text(new_content)
    return True, f"Action {action_id} marked as {decision_upper}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Approve or deny an ABA action")
    parser.add_argument("--root", required=True, help="ABA repo root")
    parser.add_argument("--action", required=True, help="Action ID (e.g. ACTION-001)")
    parser.add_argument(
        "--decision",
        required=True,
        choices=["approved", "denied"],
        help="Decision",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    success, msg = update_action(root, args.action, args.decision)
    print(msg)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
