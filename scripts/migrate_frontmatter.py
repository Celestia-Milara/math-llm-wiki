#!/usr/bin/env python3
"""迁移 v1 frontmatter (英文) → v2 frontmatter (中文)"""
import os
import re
from pathlib import Path

WIKI_DIR = Path("D:/tool/Obsidian/math/01_Wiki")
SCRIPTS_DIR = Path("D:/tool/Obsidian/math/scripts")


def tag_list_to_inline(tags_value):
    """Ensure tags are formatted as inline YAML list, not block format"""
    # Check if it's already inline [a, b, c]
    stripped = tags_value.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        # Already inline — normalize spacing
        inner = stripped[1:-1]
        items = [item.strip() for item in inner.split(",")]
        return f"[{', '.join(items)}]"

    # Handle block format: each line starts with "- "
    lines = stripped.split("\n")
    items = []
    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
        elif line and not line.startswith("#"):
            items.append(line)

    if items:
        return f"[{', '.join(items)}]"

    # Fallback: return as-is
    return tags_value


def process_wiki_file(filepath: Path, page_type: str):
    """Process a single Wiki file: read, transform frontmatter, write back"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        print(f"  SKIP: {filepath.name} (no frontmatter)")
        return

    yaml_text = match.group(1)
    body = match.group(2)

    # Parse frontmatter lines manually to preserve field order
    lines = yaml_text.split("\n")
    fm = {}
    current_key = None
    current_value_lines = []

    for line in lines:
        if ":" in line and not line.startswith(" "):
            # Save previous multi-line value
            if current_key is not None:
                fm[current_key] = "\n".join(current_value_lines)

            # Start new key
            colon_idx = line.index(":")
            key = line[:colon_idx].strip()
            value = line[colon_idx + 1:].strip()
            current_key = key
            current_value_lines = [value]
        elif current_key:
            current_value_lines.append(line)

    # Save last key
    if current_key is not None:
        fm[current_key] = "\n".join(current_value_lines)

    # Build new frontmatter in the desired field order
    output_order = ["标题", "标签", "创建日期", "类型",
                    "掌握状态",  # Concepts/Theorems only
                    "问题类型", "问题备注", "最后练习",  # Methods only
                    "摘要", "来源", "前置知识"]

    new_lines = []
    for field in output_order:
        if field == "掌握状态" and page_type in ("concepts", "theorems"):
            old_status = fm.get("status", "raw_compilation").strip()
            status_map = {
                "raw_compilation": "待编译",
                "mental_model_formed": "已建立心智模型",
                "practice_verified": "已练习验证",
            }
            val = status_map.get(old_status, old_status)
            new_lines.append(f"{field}: {val}")

        elif field == "问题类型" and page_type == "methods":
            new_lines.append(f"{field}: null")

        elif field == "问题备注" and page_type == "methods":
            new_lines.append(f'{field}: ""')

        elif field == "最后练习" and page_type == "methods":
            new_lines.append(f"{field}: null")

        elif field == "标题" and "title" in fm:
            new_lines.append(f"标题: {fm['title'].strip()}")

        elif field == "标签" and "tags" in fm:
            raw = fm["tags"].strip()
            new_lines.append(f"标签: {tag_list_to_inline(raw)}")

        elif field == "创建日期" and "created" in fm:
            new_lines.append(f"创建日期: {fm['created'].strip()}")

        elif field == "类型" and "type" in fm:
            old_type = fm["type"].strip()
            type_map = {"permanent": "永久笔记", "daily": "日记"}
            val = type_map.get(old_type, old_type)
            new_lines.append(f"类型: {val}")

        elif field == "摘要" and "summary" in fm:
            new_lines.append(f"摘要: {fm['summary'].strip()}")

        elif field == "来源" and "source" in fm:
            new_lines.append(f"来源: {fm['source'].strip()}")

        elif field == "前置知识" and "prerequisites" in fm:
            new_lines.append(f"前置知识: {fm['prerequisites'].strip()}")

    # Build new content
    new_frontmatter = "\n".join(new_lines)
    new_content = f"---\n{new_frontmatter}\n---\n{body}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  OK: {filepath.name}")


def main():
    # Ensure scripts dir exists
    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    errors = []
    for subdir, ptype in [("Concepts", "concepts"), ("Theorems", "theorems"), ("Methods", "methods")]:
        dir_path = WIKI_DIR / subdir
        if not dir_path.exists():
            print(f"  SKIP dir: {subdir} (not found)")
            continue
        print(f"\n=== {subdir} ===")
        for f in sorted(dir_path.glob("*.md")):
            try:
                process_wiki_file(f, ptype)
                count += 1
            except Exception as e:
                errors.append((f.name, str(e)))
                print(f"  ERR: {f.name} -> {e}")

    print(f"\nDone! {count} files processed.")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for name, msg in errors:
            print(f"  - {name}: {msg}")


if __name__ == "__main__":
    main()
