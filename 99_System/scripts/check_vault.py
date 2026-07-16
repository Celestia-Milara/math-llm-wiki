#!/usr/bin/env python3
"""Read-only health checks for the math reference vault."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.S)


def relative_without_suffix(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def note_index() -> tuple[dict[str, Path], dict[str, list[Path]]]:
    paths: dict[str, Path] = {}
    stems: dict[str, list[Path]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(ROOT).parts
        if parts[:2] in {("99_System", "Archive"), ("06_Templates", "Archive")} or ".claude" in parts:
            continue
        paths[path.relative_to(ROOT).as_posix()] = path
        paths[relative_without_suffix(path)] = path
        stems.setdefault(path.stem, []).append(path)
    return paths, stems


def resolve(target: str, paths: dict[str, Path], stems: dict[str, list[Path]]) -> bool:
    normalized = target.strip().replace("\\", "/")
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    if normalized in paths:
        return True
    candidates = stems.get(Path(normalized).name, [])
    return len(candidates) == 1


def frontmatter(text: str) -> str | None:
    match = FRONTMATTER.match(text)
    return match.group(1) if match else None


def key_values(front: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in front.splitlines():
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def check_links(errors: list[str]) -> None:
    paths, stems = note_index()
    active = [ROOT / "README.md", ROOT / "CLAUDE.md", ROOT / "01_Raw" / "资料主索引.md"]
    active.extend((ROOT / "03_Wiki").rglob("*.md"))
    for path in active:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for match in WIKILINK.finditer(text):
            target = match.group(1)
            if not resolve(target, paths, stems):
                errors.append(f"broken active wikilink: {path.relative_to(ROOT)} -> {target}")


def check_wiki_schema(errors: list[str]) -> None:
    forbidden = {"掌握状态", "问题类型", "问题备注", "最后练习"}
    allowed_status = {"S1 定位数据", "S2 已核查", "S3 待核查", "S3 需修正"}
    for path in (ROOT / "03_Wiki").rglob("*.md"):
        front = frontmatter(path.read_text(encoding="utf-8-sig", errors="replace"))
        if front is None:
            errors.append(f"missing frontmatter: {path.relative_to(ROOT)}")
            continue
        values = key_values(front)
        if not values.get("标题") or not values.get("类型") or not values.get("来源"):
            errors.append(f"missing Wiki core fields: {path.relative_to(ROOT)}")
        if values.get("可信状态") not in allowed_status:
            errors.append(f"missing or invalid trust status: {path.relative_to(ROOT)}")
        for field in forbidden | {"AI状态"}:
            if field in values:
                errors.append(f"legacy Wiki field {field}: {path.relative_to(ROOT)}")


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8-sig", errors="replace").splitlines())


def valid_range(node: object, label: str, errors: list[str]) -> None:
    if not isinstance(node, dict):
        errors.append(f"invalid mapping node: {label}")
        return
    rel, start, end = node.get("文件"), node.get("起始行"), node.get("结束行")
    if not isinstance(rel, str) or not isinstance(start, int) or not isinstance(end, int):
        errors.append(f"missing mapping fields: {label}")
        return
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"mapped file missing: {label} -> {rel}")
        return
    if start < 1 or end < start or end > line_count(path):
        errors.append(f"mapping line range out of bounds: {label} -> {start}-{end}/{line_count(path)}")


def check_mapping(errors: list[str]) -> None:
    path = ROOT / "01_Raw" / "章节映射.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"mapping JSON invalid: {exc}")
        return
    if data.get("schema_version") != "2.0":
        errors.append("mapping schema_version must be 2.0")
    for entry in data.get("mappings", []):
        label = f"高等数学第{entry.get('讲次', '?')}讲"
        lecture = entry.get("讲义")
        if not isinstance(lecture, str) or not (ROOT / lecture).is_file():
            errors.append(f"mapped lecture missing: {label} -> {lecture}")
        for book in ("试题册", "解析册"):
            for level, node in entry.get(book, {}).items():
                valid_range(node, f"{label} {book}/{level}", errors)
    for entry in data.get("catalog", []):
        label = f"{entry.get('科目', '?')} {entry.get('课程单元', '?')}"
        if not all(entry.get(field) for field in ("科目", "模块", "课程单元")):
            errors.append(f"catalog hierarchy incomplete: {label}")
        material = entry.get("资料")
        if not isinstance(material, dict) or not material:
            errors.append(f"catalog material missing: {label}")
            continue
        for kind, node in material.items():
            valid_range(node, f"{label} {kind}", errors)


def check_record_relations(errors: list[str]) -> None:
    paths, stems = note_index()
    for path in (ROOT / "04_Records").rglob("*.md"):
        front = frontmatter(path.read_text(encoding="utf-8-sig", errors="replace"))
        if front is None:
            continue
        for field in ("关联概念", "关联方法", "关联题型"):
            field_match = re.search(rf"^{field}:.*?(?=^[^ \t].*?:|\Z)", front, re.M | re.S)
            if not field_match:
                continue
            value = field_match.group(0)
            for link in WIKILINK.findall(value):
                if not resolve(link, paths, stems):
                    errors.append(f"broken historical relation: {path.relative_to(ROOT)} {field} -> {link}")


def main() -> int:
    errors: list[str] = []
    check_links(errors)
    check_wiki_schema(errors)
    check_mapping(errors)
    check_record_relations(errors)
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for item in errors:
            print(f"- {item}")
        return 1
    print("PASS: active links, Wiki schema, mapping ranges, and historical relations are valid.")
    print("Read-only mode: no files were modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
