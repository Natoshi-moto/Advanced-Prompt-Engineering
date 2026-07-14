#!/usr/bin/env python3
"""Verify the structural contracts of the Advanced Prompt Engineering repository."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_STATES = {
    "LATERAL",
    "CANDIDATE",
    "LOCKED",
    "IMPLEMENTED",
    "DEMONSTRATED",
    "FALSIFIED",
    "SUPERSEDED",
    "INFERRED",
    "UNVERIFIED",
}
REQUIRED_FILES = [
    "README.md",
    "README_START_HERE.md",
    "AGENTS.md",
    "CLAUDE.md",
    "STATUS.json",
    "STATUS.md",
    "NEXT_ACTION.md",
    "governance/CONSTITUTION.md",
    "docs/METHOD.md",
    "docs/EPISTEMIC_STATES.md",
]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_file(relative: str) -> Path:
    path = ROOT / relative
    if not path.is_file():
        fail(f"required file absent: {relative}")
    return path


def verify_status() -> None:
    status = load_json(require_file("STATUS.json"))
    if status.get("schema") != "ape.status/v1":
        fail("STATUS.json schema must be ape.status/v1")
    if status.get("promotion_authority") != "HUMAN_ONLY":
        fail("STATUS.json promotion_authority must be HUMAN_ONLY")

    declared_states = set(status.get("epistemic_states", []))
    if declared_states != ALLOWED_STATES:
        missing = sorted(ALLOWED_STATES - declared_states)
        extra = sorted(declared_states - ALLOWED_STATES)
        fail(f"epistemic state mismatch; missing={missing}, extra={extra}")

    route = status.get("active_route")
    if not isinstance(route, str) or not (ROOT / route).is_file():
        fail(f"active route does not exist: {route!r}")

    active_tasks = status.get("active_tasks")
    if not isinstance(active_tasks, list):
        fail("active_tasks must be a list")
    for task_id in active_tasks:
        task_path = ROOT / "operations" / "tasks" / f"{task_id}.json"
        task = load_json(task_path)
        if task.get("task_id") != task_id:
            fail(f"task identity mismatch in {task_path.relative_to(ROOT)}")
        if task.get("promotion_authority") != "HUMAN_ONLY":
            fail(f"task {task_id} must preserve HUMAN_ONLY promotion")


def verify_prompt_manifests() -> None:
    manifests = sorted((ROOT / "prompts").glob("*/*/MANIFEST.json"))
    if not manifests:
        fail("no versioned prompt manifests found")

    seen_ids: set[str] = set()
    for manifest_path in manifests:
        manifest = load_json(manifest_path)
        if manifest.get("schema") != "ape.prompt-manifest/v1":
            fail(f"bad manifest schema: {manifest_path.relative_to(ROOT)}")

        prompt_id = manifest.get("prompt_id")
        if not isinstance(prompt_id, str) or not prompt_id:
            fail(f"missing prompt_id: {manifest_path.relative_to(ROOT)}")
        if prompt_id in seen_ids:
            fail(f"duplicate prompt_id: {prompt_id}")
        seen_ids.add(prompt_id)

        state = manifest.get("state")
        if state not in ALLOWED_STATES:
            fail(f"invalid prompt state {state!r}: {manifest_path.relative_to(ROOT)}")
        if manifest.get("promotion_authority") != "HUMAN_ONLY":
            fail(f"prompt {prompt_id} must preserve HUMAN_ONLY promotion")

        prompt_name = manifest.get("prompt_file")
        if not isinstance(prompt_name, str) or Path(prompt_name).name != prompt_name:
            fail(f"prompt_file must be a local filename: {manifest_path.relative_to(ROOT)}")
        prompt_path = manifest_path.parent / prompt_name
        if not prompt_path.is_file():
            fail(f"prompt file absent: {prompt_path.relative_to(ROOT)}")

        expected = manifest.get("prompt_sha256")
        observed = sha256(prompt_path)
        if expected != observed:
            fail(
                f"prompt hash mismatch for {prompt_id}: "
                f"expected={expected}, observed={observed}"
            )
        print(f"PASS: {prompt_id} {manifest.get('version')} sha256={observed}")


def main() -> int:
    for relative in REQUIRED_FILES:
        require_file(relative)
        print(f"PASS: required file {relative}")
    verify_status()
    print("PASS: STATUS.json and active route/task contracts")
    verify_prompt_manifests()
    print("PASS: repository structural verification complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
