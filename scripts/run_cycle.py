#!/usr/bin/env python3
"""ABA cycle runner — one full research/strategize cycle with git push.

Replaces claude_code_sdk with direct Anthropic API calls routed through
OpenClaw's OAuth token.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

# ── API helpers ───────────────────────────────────────────────────────────────

def _detect_provider(prefer_claude: bool = False) -> tuple[str, str, str]:
    """Detect best available API provider.

    Returns (provider, api_key, base_url).
    Priority (default): OPENAI_API_KEY -> ANTHROPIC_API_KEY -> OpenClaw OAuth -> OPENROUTER_API_KEY
    Priority (prefer_claude): OpenClaw OAuth -> ANTHROPIC_API_KEY -> OPENAI_API_KEY -> OPENROUTER_API_KEY
    """
    import os

    def _openclaw_oauth() -> str:
        profiles_path = Path.home() / ".openclaw/agents/main/agent/auth-profiles.json"
        try:
            data = json.loads(profiles_path.read_text())
            token = data["profiles"]["anthropic:default"]["token"]
            if token.startswith("sk-ant-oat"):
                return token
        except Exception:
            pass
        return ""

    if prefer_claude:
        # Try Claude OAuth first
        token = _openclaw_oauth()
        if token:
            return "anthropic-oauth", token, "https://api.anthropic.com/v1"
        # Fall back to direct Anthropic API key
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if key:
            return "anthropic", key, "https://api.anthropic.com/v1"

    # OpenAI direct
    key = os.environ.get("OPENAI_API_KEY", "")
    if key:
        return "openai", key, "https://api.openai.com/v1"

    # Anthropic direct API key (not OAuth)
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key and not key.startswith("sk-ant-oat"):
        return "anthropic", key, "https://api.anthropic.com/v1"

    # OpenClaw OAuth token
    token = _openclaw_oauth()
    if token:
        return "anthropic-oauth", token, "https://api.anthropic.com/v1"

    # OpenRouter
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if key:
        return "openrouter", key, "https://openrouter.ai/api/v1"

    raise RuntimeError(
        "No usable API key found. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, or OPENROUTER_API_KEY."
    )


# Provider-specific model aliases
PROVIDER_MODELS = {
    "openai": {
        "agent": "gpt-4.1",
        "judge": "gpt-4.1-mini",
    },
    "anthropic": {
        "agent": "claude-sonnet-4-6",
        "judge": "claude-sonnet-4-6",
    },
    "anthropic-oauth": {
        "agent": "claude-sonnet-4-6",
        "judge": "claude-sonnet-4-6",
    },
    "openrouter": {
        "agent": "anthropic/claude-sonnet-4-6",
        "judge": "anthropic/claude-sonnet-4-6",
    },
}


def _call_api(
    api_key: str,
    prompt: str,
    model: str,
    provider: str = "openai",
    base_url: str = "https://api.openai.com/v1",
    max_tokens: int = 8192,
    system: str = "",
    json_mode: bool = False,
) -> tuple[str, int, int]:
    """Call LLM API. Returns (text, input_tokens, output_tokens).

    Supports OpenAI-compatible (openai, openrouter) and Anthropic APIs.
    json_mode=True forces structured JSON output at the API level.
    """
    import urllib.request

    headers = {"content-type": "application/json"}

    if provider in ("anthropic", "anthropic-oauth"):
        if provider == "anthropic-oauth":
            headers["Authorization"] = f"Bearer {api_key}"
            headers["anthropic-beta"] = "oauth-2025-04-20"
        else:
            headers["x-api-key"] = api_key
        headers["anthropic-version"] = "2023-06-01"
        url = f"{base_url}/messages"
        body: dict = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            body["system"] = system
        # JSON mode via tool use for Anthropic
        if json_mode:
            body["tools"] = [{
                "name": "score_business",
                "description": "Return a structured business assessment score",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "number", "description": "Score from 0.0 to 1.0"},
                        "reasoning": {"type": "string", "description": "One paragraph explaining the score"},
                        "suggestions": {"type": "string", "description": "One paragraph on how to improve"},
                    },
                    "required": ["score", "reasoning", "suggestions"],
                },
            }]
            body["tool_choice"] = {"type": "tool", "name": "score_business"}
        try:
            import httpx
            r = httpx.post(url, headers=headers, json=body, timeout=600)
            r.raise_for_status()
            data = r.json()
        except ImportError:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=600) as resp:
                data = json.loads(resp.read())
        # Extract text — handle tool_use response block
        if json_mode:
            for block in data.get("content", []):
                if block.get("type") == "tool_use":
                    return json.dumps(block["input"]), data.get("usage", {}).get("input_tokens", 0), data.get("usage", {}).get("output_tokens", 0)
        text = data["content"][0]["text"]
        usage = data.get("usage", {})
        return text, usage.get("input_tokens", 0), usage.get("output_tokens", 0)
    else:
        # OpenAI-compatible (openai, openrouter)
        headers["Authorization"] = f"Bearer {api_key}"
        if provider == "openrouter":
            headers["HTTP-Referer"] = "https://github.com/rookx88/worldcup"
        url = f"{base_url}/chat/completions"
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        body = {"model": model, "max_tokens": max_tokens, "messages": messages}
        if json_mode:
            body["response_format"] = {"type": "json_object"}
        try:
            import httpx
            r = httpx.post(url, headers=headers, json=body, timeout=600)
            r.raise_for_status()
            data = r.json()
        except ImportError:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=600) as resp:
                data = json.loads(resp.read())
        text = data["choices"][0]["message"]["content"] or ""
        usage = data.get("usage", {})
        return text, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)


# ── State helpers ─────────────────────────────────────────────────────────────

STATE_FILES = [
    "IDENTITY.md", "CONCEPT.md", "PLAYERS.md", "CHANNELS.md",
    "EXPERIMENTS.md", "MONETIZATION.md", "JOURNAL.md", "LEARNINGS.md",
    "METRICS.md", "ACTIONS.md", "PHASE.md", "PIPELINE.md",
    "OUTREACH.md", "CONVERSION.md",
]

APPEND_ONLY = {"JOURNAL.md", "LEARNINGS.md", "OUTREACH.md", "SIGNUPS.md"}

# Phase 2 transition thresholds
PHASE2_OVERALL_THRESHOLD = 0.95
PHASE2_DIM_THRESHOLD = 0.90

# Phase 1 rubrics only — Phase 2 adds execution rubrics
PHASE1_RUBRICS = {"concept-uniqueness", "market-positioning", "viral-mechanics", "marketing-reach", "product-readiness", "monetization-readiness"}
PHASE2_RUBRICS = {"user-acquisition", "engagement-quality"}


def _read(path: Path, default: str = "") -> str:
    return path.read_text() if path.exists() else default


def _snapshot(state_dir: Path) -> dict[str, str]:
    return {f: _read(state_dir / f) for f in STATE_FILES}


def _revert(state_dir: Path, snap: dict[str, str], preserve: set[str]) -> None:
    for name, content in snap.items():
        if name not in preserve:
            (state_dir / name).write_text(content)


def _load_state(state_dir: Path) -> dict[str, str]:
    return {f: _read(state_dir / f) for f in STATE_FILES}


def _content_is_empty(text: str) -> bool:
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("---") or line.startswith("_"):
            continue
        if line.startswith("(") and line.endswith(")"):
            continue
        return False
    return True


# ── Assessment ────────────────────────────────────────────────────────────────

# Assessor state files — exclude LEARNINGS.md (too large, not needed for scoring)
ASSESSOR_STATE_FILES = ["CONCEPT.md", "PLAYERS.md", "CHANNELS.md", "EXPERIMENTS.md", "MONETIZATION.md", "METRICS.md"]
ASSESSOR_PHASE2_FILES = ["PIPELINE.md", "OUTREACH.md", "CONVERSION.md"]
# Max drop in a single dimension before flagging as suspicious parse failure
SANITY_DROP_THRESHOLD = 0.5


def _parse_score(text: str) -> float:
    """Robustly extract score from assessor response."""
    clean = re.sub(r"```[a-z]*\n?", "", text).strip()
    start = clean.index("{")
    end = clean.rindex("}") + 1
    data = json.loads(clean[start:end])
    return max(0.0, min(1.0, float(data["score"])))


def _run_assessment(provider: str, api_key: str, base_url: str, root: Path, model: str, prior_scores: dict | None = None) -> dict:
    """Score all rubrics. Returns assessment dict.

    Mitigations:
    - JSON mode forced at API level (tool use / response_format)
    - LEARNINGS.md excluded from assessor prompt (too large, not needed)
    - Retry once on parse failure before falling back to prior score
    - Sanity check: drop > 0.5 on any dimension uses prior score instead
    """
    state_dir = root / "state"
    assessments_dir = root / "assessments"
    state = _load_state(state_dir)

    # Detect phase to include appropriate state files and rubrics
    current_phase = _get_phase(state)
    files_to_assess = ASSESSOR_STATE_FILES + (ASSESSOR_PHASE2_FILES if current_phase == 2 else [])

    state_text = "\n\n".join(
        f"### {name}\n{state[name]}"
        for name in files_to_assess
        if state.get(name, "").strip()
    )

    # Filter rubrics by phase
    all_rubric_dirs = sorted(d for d in assessments_dir.iterdir() if d.is_dir() and (d / "rubric.md").exists()) if assessments_dir.exists() else []
    if current_phase == 1:
        rubric_dirs = [d for d in all_rubric_dirs if d.name in PHASE1_RUBRICS]
    else:
        rubric_dirs = [d for d in all_rubric_dirs if d.name in PHASE1_RUBRICS | PHASE2_RUBRICS]
    if not rubric_dirs:
        return {"overall_score": 0.0, "dimension_scores": {}, "weakest_dimension": ""}

    judge_model = PROVIDER_MODELS.get(provider, {}).get("judge", model)
    dimension_scores = {}

    for rubric_dir in rubric_dirs:
        rubric_text = (rubric_dir / "rubric.md").read_text()
        prompt = f"""You are a business model assessor. Score the following business state against the rubric.

## Business State
{state_text}

## Rubric: {rubric_dir.name}
{rubric_text}

Return a JSON object with keys: score (float 0.0-1.0), reasoning (string), suggestions (string)."""

        score = None
        last_err = None

        # Try up to 2 times (retry once on failure)
        for attempt in range(2):
            try:
                text, _, _ = _call_api(
                    api_key, prompt, model=judge_model,
                    provider=provider, base_url=base_url,
                    max_tokens=600, json_mode=True,
                )
                score = _parse_score(text)
                break
            except Exception as e:
                last_err = e
                if attempt == 0:
                    print(f"  Retrying {rubric_dir.name} assessment...", file=sys.stderr)

        if score is None:
            print(f"  Warning: assessment failed for {rubric_dir.name} after retry: {last_err}", file=sys.stderr)
            score = (prior_scores or {}).get(rubric_dir.name, 0.0)
            if score > 0:
                print(f"  Using prior score for {rubric_dir.name}: {score:.2f}", file=sys.stderr)

        # Sanity check: if drop > threshold vs prior, use prior
        prior = (prior_scores or {}).get(rubric_dir.name)
        if prior is not None and (prior - score) > SANITY_DROP_THRESHOLD:
            print(
                f"  Sanity check: {rubric_dir.name} dropped {prior:.2f}→{score:.2f} "
                f"(>{SANITY_DROP_THRESHOLD}). Using prior score.",
                file=sys.stderr,
            )
            score = prior

        dimension_scores[rubric_dir.name] = score

    overall = sum(dimension_scores.values()) / len(dimension_scores) if dimension_scores else 0.0
    weakest = min(dimension_scores, key=dimension_scores.get) if dimension_scores else ""

    return {
        "overall_score": overall,
        "dimension_scores": dimension_scores,
        "weakest_dimension": weakest,
    }


# ── Skill selection ───────────────────────────────────────────────────────────

def _get_phase(state: dict[str, str]) -> int:
    """Detect current phase from PHASE.md."""
    phase_text = state.get("PHASE.md", "")
    if "Phase 2" in phase_text and "Current Phase" in phase_text:
        # Check if Phase 2 is the current phase (not just mentioned in history)
        for line in phase_text.splitlines():
            if "**Phase 2" in line or "Phase 2 —" in line:
                if "Current Phase" in phase_text[max(0, phase_text.index(line)-200):phase_text.index(line)+50]:
                    return 2
    return 1


def _check_phase_transition(assessment: dict, state: dict[str, str]) -> bool:
    """Check if Phase 1 criteria are met for transitioning to Phase 2."""
    if _get_phase(state) == 2:
        return False  # Already in Phase 2
    overall = assessment.get("overall_score", 0)
    dims = assessment.get("dimension_scores", {})
    phase1_dims = {k: v for k, v in dims.items() if k in PHASE1_RUBRICS}
    all_above = all(v >= PHASE2_DIM_THRESHOLD for v in phase1_dims.values()) if phase1_dims else False
    return overall >= PHASE2_OVERALL_THRESHOLD and all_above


def _transition_to_phase2(root: Path, generation: int) -> None:
    """Write Phase 2 transition to PHASE.md and propose first action in ACTIONS.md."""
    state_dir = root / "state"

    # Update PHASE.md
    phase_path = state_dir / "PHASE.md"
    phase_content = _read(phase_path)
    phase_content = phase_content.replace(
        "**Phase 1 — Research & Strategy**",
        "**Phase 2 — Launch & Growth**"
    )
    phase_content += f"\n| Phase 2 | Generation {generation} | Transitioned from research to execution |\n"
    phase_path.write_text(phase_content)

    # Write first execution action to ACTIONS.md
    actions_path = state_dir / "ACTIONS.md"
    existing = _read(actions_path)
    first_action = f"""

### ACTION-001
**Status:** PENDING
**Action:** Launch waitlist page — Copa is ready to find real players
**Hypothesis:** The business model is validated to 0.95+. Real customers exist in communities like r/entrepreneur and r/smallbusiness actively complaining about freelancer quality. Reaching out with a personalised message referencing their specific complaint will yield at least a 10% response rate.
**Method:** ABA will identify 10 prospects from Reddit/Indie Hackers, draft personalised outreach for each, and propose sending via this approval queue.
**Cost estimate:** $0 (organic outreach only in Phase 2)
**Risk:** Low — no spend, no public commitment, just conversations
**Requested by:** ABA Generation {generation} (Phase 2 transition)
"""
    actions_path.write_text(existing.rstrip() + first_action)
    print(f"  → Phase 2 transition written. ACTION-001 proposed in ACTIONS.md.", file=__import__("sys").stderr)


def _select_skill(root: Path, assessment: dict, state: dict[str, str]) -> tuple[str, str]:
    """Returns (skill_name, skill_text). Phase-aware."""
    phase = _get_phase(state)
    weakest = assessment.get("weakest_dimension", "")
    business = state.get("CONCEPT.md", "")
    audience = state.get("PLAYERS.md", "")

    if phase == 2:
        # Phase 2: rotate between execute and research based on weakest dimension
        if weakest in ("user-acquisition",):
            skill_name = "grow"
        elif weakest in ("engagement-quality",):
            skill_name = "convert"
        else:
            skill_name = "grow"  # Default to growth in Phase 2
    else:
        # Phase 1: research or strategize
        if _content_is_empty(business) or _content_is_empty(audience):
            skill_name = "research"
        elif weakest in ("concept-uniqueness", "market-positioning"):
            skill_name = "research"
        elif weakest in ("viral-mechanics", "product-readiness"):
            skill_name = "design"
        elif weakest in ("marketing-reach",):
            skill_name = "strategize"
        else:
            skill_name = "research"

    skill_path = root / "skills" / skill_name / "SKILL.md"
    skill_text = _read(skill_path, f"Make one meaningful change. Focus on: {skill_name}.")
    return skill_name, skill_text


# ── Agent turn ────────────────────────────────────────────────────────────────

WRITE_FILE_RE = re.compile(
    r"WRITE_FILE:\s*(\S+)\n```[^\n]*\n(.*?)```",
    re.DOTALL,
)


def _truncate_tail(text: str, max_lines: int) -> str:
    """Return only the last max_lines of text — keeps recent context, drops old bulk."""
    lines = text.splitlines()
    if len(lines) <= max_lines:
        return text
    dropped = len(lines) - max_lines
    return f"[... {dropped} earlier lines omitted ...]\n" + "\n".join(lines[-max_lines:])


# Files that grow unboundedly — truncate to last N lines in agent prompt
AGENT_PROMPT_TRUNCATION = {
    "JOURNAL.md": 40,
    "LEARNINGS.md": 60,
    "OUTREACH.md": 30,
    "CONVERSION.md": 30,
}

# Files not needed in agent prompt at all (too large, not actionable)
AGENT_PROMPT_SKIP = set()  # add filenames here if needed


CONVERSION_FOCUS_DIRECTIVE = """
## ⚠️ Cycle Focus: user-acquisition is critically low

This cycle has ONE job: move the pipeline one step closer to a real conversation with a real prospect.

**Do exactly ONE of these — pick the highest-leverage option given current state:**
1. If PIPELINE.md has identified prospects with no outreach drafted → draft ONE outreach message and write it to ACTIONS.md as PENDING
2. If ACTIONS.md has APPROVED outreach → mark it COMPLETED, update PIPELINE.md status to "Contacted"
3. If all prospects have been contacted with no response → identify ONE new prospect from Reddit/IH/Twitter and add to PIPELINE.md
4. If a response has been logged → propose the follow-up action in ACTIONS.md

Do NOT rewrite strategy, refine messaging templates, or improve frameworks this cycle.
Do NOT produce a long plan. Output the one concrete file change + JOURNAL entry only.
"""


def _build_prompt(generation: int, state: dict[str, str], assessment: dict, skill_text: str) -> str:
    sections = []
    for name, text in state.items():
        if name in AGENT_PROMPT_SKIP:
            continue
        if name in AGENT_PROMPT_TRUNCATION:
            text = _truncate_tail(text or "", AGENT_PROMPT_TRUNCATION[name])
        sections.append(f"### {name}\n{text or '(empty)'}")
    state_sections = "\n\n".join(sections)

    # When conversion-progress is the weakest dimension, inject a focused directive
    # that prevents the model from generating an exhaustive plan (which causes timeouts)
    weakest = assessment.get("weakest_dimension", "")
    focus_block = CONVERSION_FOCUS_DIRECTIVE if weakest in ("user-acquisition", "engagement-quality") else ""

    return f"""You are Copa, an autonomized business agent running generation {generation}.

## Current Business State
{state_sections}

## Pre-Cycle Assessment
Overall score: {assessment['overall_score']:.2f}
Weakest dimension: {weakest or 'none'}
Scores: {json.dumps(assessment.get('dimension_scores', {}), indent=2)}
{focus_block}
## Your Task
{skill_text}

## File Writing Protocol
When you want to update a state file, use this EXACT format:

WRITE_FILE: state/FILENAME.md
```
[full file content here]
```

Rules:
- Only output WRITE_FILE blocks for files you actually changed
- For JOURNAL.md: output ONLY the new entry to append (not the full file)
- For LEARNINGS.md: output ONLY the new notes to append (not the full file)
- For all other files: output the complete file content
- Always end with a WRITE_FILE: state/JOURNAL.md block documenting what you did and why
- One meaningful change per cycle — do not rewrite everything
"""


def _apply_writes(state_dir: Path, response_text: str) -> list[str]:
    """Parse WRITE_FILE blocks and apply them. Returns list of changed files."""
    changed = []
    for match in WRITE_FILE_RE.finditer(response_text):
        filepath = match.group(1).strip()
        content = match.group(2)
        filename = Path(filepath).name

        # Security: only write to state/ files
        if not filepath.startswith("state/"):
            print(f"  Skipping write to non-state path: {filepath}", file=sys.stderr)
            continue

        target = state_dir / filename
        if filename in APPEND_ONLY:
            # Append with separator
            existing = _read(target)
            separator = "\n\n---\n\n" if existing.strip() else ""
            target.write_text(existing + separator + content.strip() + "\n")
        else:
            target.write_text(content)
        changed.append(filename)

    return changed


# ── Git push ──────────────────────────────────────────────────────────────────

def _git_push(root: Path, message: str) -> dict:
    import subprocess

    def run(cmd):
        r = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
        return r.returncode, r.stdout.strip(), r.stderr.strip()

    rc, out, _ = run(["git", "status", "--porcelain"])
    if not out:
        return {"success": True, "output": "nothing to commit", "error": ""}

    run(["git", "add", "-A"])
    rc, out, err = run(["git", "commit", "-m", message])
    if rc != 0:
        return {"success": False, "output": out, "error": err}

    rc, out, err = run(["git", "push", "origin", "HEAD"])
    if rc != 0:
        return {"success": False, "output": out, "error": f"push failed: {err}"}

    return {"success": True, "output": out, "error": ""}


# ── Pending actions check ─────────────────────────────────────────────────────

def _pending_actions(actions_text: str) -> list[str]:
    sections = re.split(r"(?=^### )", actions_text, flags=re.MULTILINE)
    pending = []
    for section in sections:
        if "PENDING" in section:
            header = re.match(r"### (ACTION-\w+)", section)
            if header:
                pending.append(header.group(1))
    return pending


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Run one ABA business cycle")
    parser.add_argument("--root", required=True, help="ABA repo root")
    parser.add_argument("--push", action="store_true", help="Git commit and push after success")
    parser.add_argument("--dry-run", action="store_true", help="No file writes or push")
    parser.add_argument("--model", default="claude-sonnet-4-6", help="Model for agent turn")
    parser.add_argument("--use-claude", action="store_true", help="Prefer Claude OAuth over OpenAI")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    state_dir = root / "state"
    gen_file = state_dir / "GENERATION_COUNT"
    generation = int(_read(gen_file, "0").strip() or "0")
    next_gen = generation + 1

    print(f"\n{'='*48}")
    print(f"  ABA — business cycle generation {next_gen}")
    print(f"{'='*48}\n")

    provider, api_key, base_url = _detect_provider(prefer_claude=True)
    agent_model = PROVIDER_MODELS.get(provider, {}).get("agent", args.model)
    print(f"  Provider: {provider} | Agent model: {agent_model}")
    total_in = total_out = 0

    # 1. Snapshot
    snapshot = _snapshot(state_dir)

    # 2. Pre-assessment
    print("→ Pre-cycle assessment...")
    pre = _run_assessment(provider, api_key, base_url, root, args.model)
    print(f"  Overall: {pre['overall_score']:.2f}")
    for dim, score in sorted(pre["dimension_scores"].items()):
        print(f"    {dim}: {score:.2f}")
    print(f"  Weakest: {pre.get('weakest_dimension', 'none')}")

    # 3. Check for phase transition
    state = _load_state(state_dir)
    if _check_phase_transition(pre, state) and not args.dry_run:
        print("\n🎯 Phase 1 complete! Transitioning to Phase 2 — Execution mode.")
        _transition_to_phase2(root, next_gen)
        state = _load_state(state_dir)  # Reload after transition writes

    # 4. Select skill
    current_phase = _get_phase(state)
    print(f"  Phase: {current_phase}")
    skill_name, skill_text = _select_skill(root, pre, state)

    # Inject pending action context
    actions_text = state.get("ACTIONS.md", "")
    pending = _pending_actions(actions_text)
    if pending:
        skill_text += f"\n\n## Pending Actions\nThe following actions need processing: {', '.join(pending)}. Check ACTIONS.md for their current status and handle accordingly."

    print(f"\n→ Running {skill_name} cycle...")

    # 5. Agent turn
    prompt = _build_prompt(next_gen, state, pre, skill_text)

    if not args.dry_run:
        response, in_tok, out_tok = _call_api(api_key, prompt, model=agent_model, provider=provider, base_url=base_url, max_tokens=32768)
        total_in += in_tok
        total_out += out_tok
        print(f"  Agent responded ({in_tok}in / {out_tok}out tokens)")

        # 5. Apply writes
        changed = _apply_writes(state_dir, response)
        print(f"  Files changed: {', '.join(changed) or 'none'}")
    else:
        print("  [DRY RUN] Skipping agent call and file writes")
        response = ""
        changed = []

    # 6. Post-assessment
    print("\n→ Post-cycle assessment...")
    post = _run_assessment(provider, api_key, base_url, root, args.model, prior_scores=pre["dimension_scores"])
    print(f"  Overall: {post['overall_score']:.2f}")
    for dim, score in sorted(post["dimension_scores"].items()):
        delta = score - pre["dimension_scores"].get(dim, score)
        arrow = "↑" if delta > 0.01 else "↓" if delta < -0.01 else "="
        print(f"    {dim}: {score:.2f} {arrow}")

    # 7. Regression check
    regressed = post["overall_score"] < pre["overall_score"] - 0.05

    if regressed:
        print(f"\n✗ Regression detected ({pre['overall_score']:.2f} → {post['overall_score']:.2f}). Reverting.")
        if not args.dry_run:
            _revert(state_dir, snapshot, preserve={"JOURNAL.md"})
            # Append failure note to journal
            journal_path = state_dir / "JOURNAL.md"
            existing = _read(journal_path)
            sep = "\n\n---\n\n" if existing.strip() else ""
            journal_path.write_text(
                existing + sep +
                f"## Generation {next_gen} — REVERTED\n\n"
                f"Cycle reverted: score fell from {pre['overall_score']:.2f} to {post['overall_score']:.2f}.\n"
            )
        sys.exit(1)

    # 8. Commit generation
    if not args.dry_run:
        gen_file.write_text(str(next_gen))

    cost = (total_in * 3.0 + total_out * 15.0) / 1_000_000
    print(f"\n✓ Generation {next_gen} complete")
    print(f"  Score: {pre['overall_score']:.2f} → {post['overall_score']:.2f}")
    print(f"  Tokens: {total_in}in / {total_out}out")
    print(f"  Estimated cost: ${cost:.4f}")

    # 9. Git push
    if args.push and not args.dry_run:
        commit_msg = f"Copa: generation {next_gen} — {skill_name} cycle (score {post['overall_score']:.2f})"
        print(f"\n→ Pushing to git...")
        git_result = _git_push(root, commit_msg)
        if git_result["success"]:
            print(f"  ✓ {git_result['output'] or 'pushed'}")
        else:
            print(f"  ✗ Push failed: {git_result['error']}", file=sys.stderr)

    # 10. Report pending actions
    new_actions = _read(state_dir / "ACTIONS.md")
    still_pending = _pending_actions(new_actions)
    if still_pending:
        print(f"\n⚠ Pending actions requiring approval: {', '.join(still_pending)}")
        print("  Use: /aba approve ACTION-ID  or  /aba deny ACTION-ID")

    print()


if __name__ == "__main__":
    main()
