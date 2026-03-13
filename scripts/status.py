#!/usr/bin/env python3
"""ABA status report — human-readable, WhatsApp-friendly."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def _read(path: Path, default: str = "") -> str:
    return path.read_text() if path.exists() else default


def _last_n_lines(text: str, n: int) -> str:
    lines = [l for l in text.splitlines() if l.strip()]
    return "\n".join(lines[-n:])


def _pending_actions(actions_text: str) -> list[str]:
    sections = re.split(r"(?=^### )", actions_text, flags=re.MULTILINE)
    pending = []
    for section in sections:
        if "PENDING" in section:
            header = re.match(r"### (ACTION-\w+)", section)
            action_id = header.group(1) if header else "unknown"
            # Extract one-line description
            desc_match = re.search(r"\*\*Action:\*\*\s*(.+)", section)
            desc = desc_match.group(1).strip()[:80] if desc_match else "No description"
            pending.append(f"{action_id}: {desc}")
    return pending


def _latest_scores(results_dir: Path) -> dict | None:
    if not results_dir.exists():
        return None
    reports = sorted(results_dir.glob("assessment_*.json"))
    if not reports:
        return None
    try:
        return json.loads(reports[-1].read_text())
    except Exception:
        return None


def _last_commit(root: Path) -> str:
    try:
        r = subprocess.run(
            ["git", "log", "-1", "--pretty=%h %s (%cr)"],
            cwd=root, capture_output=True, text=True
        )
        return r.stdout.strip() or "no commits"
    except Exception:
        return "git not available"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    state_dir = root / "state"

    generation = _read(state_dir / "GENERATION_COUNT", "0").strip()
    actions_text = _read(state_dir / "ACTIONS.md")
    journal_text = _read(state_dir / "JOURNAL.md")
    pending = _pending_actions(actions_text)
    scores = _latest_scores(root / "results")
    last_commit = _last_commit(root)

    lines = []
    lines.append(f"ABA Status — Generation {generation}")
    lines.append("")

    if scores:
        lines.append(f"Latest scores (overall: {scores.get('overall_score', 0):.2f})")
        for dim, score in sorted(scores.get("dimension_scores", {}).items()):
            bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
            lines.append(f"  {dim}: {bar} {score:.2f}")
        weakest = scores.get("weakest_dimension", "")
        if weakest:
            lines.append(f"  Weakest: {weakest}")
    else:
        lines.append("No assessment scores yet")

    lines.append("")
    lines.append(f"Last commit: {last_commit}")

    if pending:
        lines.append("")
        lines.append(f"PENDING ACTIONS ({len(pending)}):")
        for p in pending:
            lines.append(f"  • {p}")
        lines.append("Reply '/aba approve ACTION-ID' or '/aba deny ACTION-ID'")
    else:
        lines.append("No pending actions")

    if journal_text:
        lines.append("")
        lines.append("Recent journal:")
        recent = _last_n_lines(journal_text, 8)
        for line in recent.splitlines():
            lines.append(f"  {line}")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
