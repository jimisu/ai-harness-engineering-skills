#!/usr/bin/env python3
"""Validate the portable structure of every skill in this repository."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+\.md(?:#[^)]+)?)\)")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing YAML frontmatter delimiters")
    block = text.split("\n---\n", 1)[0].splitlines()[1:]
    values: dict[str, str] = {}
    for line in block:
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_skill(directory: Path) -> list[str]:
    errors: list[str] = []
    skill_file = directory / "SKILL.md"
    metadata_file = directory / "agents" / "openai.yaml"
    if not skill_file.is_file():
        return [f"{directory.name}: missing SKILL.md"]
    if not metadata_file.is_file():
        errors.append(f"{directory.name}: missing agents/openai.yaml")
    try:
        meta = frontmatter(skill_file)
        if set(meta) != {"name", "description"}:
            errors.append(f"{directory.name}: frontmatter must contain only name and description")
        if meta.get("name") != directory.name:
            errors.append(f"{directory.name}: frontmatter name does not match directory")
        if not NAME.fullmatch(meta.get("name", "")):
            errors.append(f"{directory.name}: invalid skill name")
        if not meta.get("description"):
            errors.append(f"{directory.name}: empty description")
    except ValueError as exc:
        errors.append(f"{directory.name}: {exc}")

    for markdown in directory.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            relative = target.split("#", 1)[0]
            if relative and not (markdown.parent / relative).resolve().is_file():
                errors.append(f"{markdown.relative_to(ROOT)}: unresolved link {target}")
    return errors


def validate_plugin_manifests() -> list[str]:
    errors: list[str] = []
    for relative in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing {relative}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{relative}: invalid JSON ({exc})")
            continue
        if not isinstance(data, dict) or not data.get("name"):
            errors.append(f"{relative}: missing name")
    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace.is_file():
        try:
            catalog = json.loads(marketplace.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            catalog = {}
        for plugin in catalog.get("plugins", []):
            for skill_path in plugin.get("skills", []):
                directory = (ROOT / skill_path).resolve()
                if not (directory / "SKILL.md").is_file():
                    errors.append(f"marketplace skill path missing SKILL.md: {skill_path}")
    return errors


def main() -> int:
    directories = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not directories:
        print("No skills found", file=sys.stderr)
        return 1
    errors = [error for directory in directories for error in validate_skill(directory)]
    errors.extend(validate_plugin_manifests())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(directories)} skills: " + ", ".join(d.name for d in directories))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
