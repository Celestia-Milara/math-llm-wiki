# Vault v1 → v2 迁移实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有高数 vault 从 v1 结构迁移到 v2 优化结构，更新 frontmatter 为中文字段，新增 Chains/Records/MOC 目录和模板

**Architecture:** 迁移分三阶段：①目录结构调整 → ②全量 frontmatter 批处理 → ③文档与模板更新。核心是 Python 批处理脚本处理 100+ 个 Wiki 页面的 frontmatter 中文化转换

**Tech Stack:** Python 3（批处理脚本）、sed/bash（目录操作）、Obsidian（手动验证）

---

### Task 1: 创建 v2 新增目录结构

**Files:**
- Create directories under `D:/tool/Obsidian/math/`

- [ ] **Step 1: 创建新目录**

```bash
# 00_Raw 新增子目录
mkdir -p "00_Raw/Lectures"
mkdir -p "00_Raw/Problems"
mkdir -p "00_Raw/Archive/Lectures"
mkdir -p "00_Raw/Archive/Problems"

# 01_Wiki 新增子目录
mkdir -p "01_Wiki/Chains"
mkdir -p "01_Wiki/Records"
mkdir -p "01_Wiki/MOC"

# 02_Output 目录已存在，无需创建
```

- [ ] **Step 2: 迁移现有归档文件到 Lectures 子目录**

当前 `00_Raw/Archive/` 下所有讲次（01_到 24_）应归入 `00_Raw/Archive/Lectures/`。题目文件（如有）归入 `00_Raw/Archive/Problems/`。

```bash
cd "D:/tool/Obsidian/math"
mv 00_Raw/Archive/*.md 00_Raw/Archive/Lectures/ 2>/dev/null
# 如果 Archive 下有 Problems 已存在则不用动
```

注意：此命令要求 Archive 目录下当前无子目录。如果 Archive 下已有 Lectures/ 或 Problems/ 目录则跳过。

- [ ] **Step 3: 验证迁移结果**

```bash
echo "=== 00_Raw/Archive ===" && ls -la "00_Raw/Archive/" && echo "=== 00_Raw/Archive/Lectures ===" && ls "00_Raw/Archive/Lectures/" | head -5 && echo "..." && ls "00_Raw/Archive/Lectures/" | wc -l
```

预期：Archive 目录下 Lectures/ 包含 24 个 .md 文件

- [ ] **Step 4: 提交**

```bash
git add .
git commit -m "chore: 创建 v2 目录结构，将归档文件移入 Lectures 子目录"
```

---

### Task 2: 创建 v2 模板文件

**Files:**
- Create: `04_Templates/概念模板.md`
- Create: `04_Templates/定理模板.md`
- Create: `04_Templates/方法模板.md`
- Create: `04_Templates/推导链模板.md`
- Create: `04_Templates/题目记录模板.md`
- Modify: `04_Templates/Daily Note Template.md` → 更新 frontmatter

- [ ] **Step 1: 创建 概念模板.md**

```markdown
---
标题: 
标签: [数学, 章节, 概念]
创建日期: {{date:YYYY-MM-DD}}
类型: 永久笔记
掌握状态: 待编译
摘要: 
来源: 
---

> [!WARNING] AI 生成
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除本块。

## 定义

## 相关条目
```dataview
TABLE 类型 AS 笔记类型, 掌握状态 AS 掌握情况
FROM "01_Wiki"
WHERE contains(标签, this.标签[1])
SORT 创建日期 ASC
```
```

- [ ] **Step 2: 创建 定理模板.md**

```markdown
---
标题: 
标签: [数学, 章节, 定理]
创建日期: {{date:YYYY-MM-DD}}
类型: 永久笔记
掌握状态: 待编译
摘要: 
来源: 
---

> [!WARNING] AI 生成
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除本块。

## 陈述

## 证明

## 相关条目
```dataview
TABLE 类型 AS 笔记类型, 掌握状态 AS 掌握情况
FROM "01_Wiki"
WHERE contains(标签, this.标签[1])
SORT 创建日期 ASC
```
```

- [ ] **Step 3: 创建 方法模板.md**

```markdown
---
标题: 
标签: [数学, 章节, 方法]
创建日期: {{date:YYYY-MM-DD}}
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 
来源: 
---

> [!WARNING] AI 生成
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除本块。

## 适用条件

## 步骤 (SOP)

## 避坑指南

## 相关题目
```dataview
TABLE 题目状态 AS 状态, 错因类型 AS 错因, 来源 AS 来源
FROM "01_Wiki/Records"
WHERE contains(关联方法, [[当前方法标题]])
SORT 创建日期 DESC
```
```

- [ ] **Step 4: 创建 推导链模板.md**

```markdown
---
标题: 
标签: [数学, 章节, 推导链]
创建日期: {{date:YYYY-MM-DD}}
类型: 永久笔记
掌握状态: 待编译
前置知识: []
摘要: 
来源: 
---

> [!WARNING] AI 生成
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除本块。

## 推导路径

## 关键节点

## 相关条目
```dataview
TABLE 类型 AS 类型, 掌握状态 AS 掌握情况
FROM "01_Wiki"
WHERE contains(标签, this.标签[1])
SORT 创建日期 ASC
```
```

- [ ] **Step 5: 创建 题目记录模板.md**

```markdown
---
标题: 
标签: [数学, 章节, 题目记录]
创建日期: {{date:YYYY-MM-DD}}
类型: 永久笔记
来源: 
题目状态: 未做
错因类型: null
关联方法: []
---

> [!WARNING] AI 生成
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除本块。

## 错因分析

## 关联方法
```

- [ ] **Step 6: 更新日记模板**

```markdown
---
标题: {{date:YYYY-MM-DD}}
标签: [日记, 学习日志]
创建日期: {{date:YYYY-MM-DD}}
类型: 日记
---

# {{date:YYYY年MM月DD日}}

## 学习内容

## 错题

## 思考
```

- [ ] **Step 7: 删除旧模板文件（英文命名的概念/定理/方法模板如果有）**

检查 `04_Templates/` 下是否存在旧的英文模板文件。如果有：

```bash
ls -la "04_Templates/"
# 如存在 Concept_Template.md、Theorem_Template.md 等旧文件：
rm 04_Templates/Concept_Template.md 2>/dev/null
rm 04_Templates/Theorem_Template.md 2>/dev/null
rm 04_Templates/Method_Template.md 2>/dev/null
rm 04_Templates/Problem_Template.md 2>/dev/null
```

注意：保留 `Daily Note Template.md`（已被更新，不是删除再创建）。

- [ ] **Step 8: 提交**

```bash
git add 04_Templates/
git commit -m "feat: 创建 v2 中文模板，更新日记模板 frontmatter"
```

---

### Task 3: 编写并执行 frontmatter 迁移脚本

**Files:**
- Create: `scripts/migrate_frontmatter.py`
- Modify: 所有 `01_Wiki/Concepts/*.md`（约 56 个文件）
- Modify: 所有 `01_Wiki/Theorems/*.md`（约 38 个文件）
- Modify: 所有 `01_Wiki/Methods/*.md`（约 54 个文件）

- [ ] **Step 1: 创建迁移脚本**

```python
#!/usr/bin/env python3
"""
迁移 v1 frontmatter (英文) → v2 frontmatter (中文)
处理对象: 01_Wiki/Concepts/, 01_Wiki/Theorems/, 01_Wiki/Methods/
"""

import os
import re
import yaml
from pathlib import Path

WIKI_DIR = Path("D:/tool/Obsidian/math/01_Wiki")

# 字段名映射 (所有页面类型通用)
FIELD_MAP = {
    "title": "标题",
    "tags": "标签",
    "created": "创建日期",
    "type": "类型",
    "summary": "摘要",
    "source": "来源",
    "status": None,  # 按页面类型特殊处理
    "prerequisites": "前置知识",
}

# 类型值映射
TYPE_MAP = {
    "permanent": "永久笔记",
    "daily": "日记",
}

# 状态值映射（Concepts / Theorems）
STATUS_MAP = {
    "raw_compilation": "待编译",
    "mental_model_formed": "已建立心智模型",
    "practice_verified": "已练习验证",
}


def rename_fields(frontmatter: dict) -> dict:
    """重命名 frontmatter 字段名为中文"""
    result = {}
    for k, v in frontmatter.items():
        new_key = FIELD_MAP.get(k, k)  # 不在映射表中的保留原字段名
        if new_key is None:
            continue  # status 会在页面类型处理逻辑中添加
        # 转换 type 的值
        if k == "type" and v in TYPE_MAP:
            v = TYPE_MAP[v]
        result[new_key] = v
    return result


def process_wiki_file(filepath: Path, page_type: str):
    """处理单个 Wiki 页面"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 解析 frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        print(f"  SKIP (no frontmatter): {filepath.name}")
        return

    yaml_text = match.group(1)
    body = match.group(2)

    try:
        fm = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        print(f"  ERROR parsing YAML: {filepath.name} - {e}")
        return

    if not isinstance(fm, dict):
        print(f"  SKIP (not a dict): {filepath.name}")
        return

    # 重命名字段
    new_fm = rename_fields(fm)

    # 按页面类型处理特有字段
    if page_type in ("concepts", "theorems"):
        old_status = fm.get("status", "raw_compilation")
        new_fm["掌握状态"] = STATUS_MAP.get(old_status, old_status)

    elif page_type == "methods":
        # Methods 改用 问题类型 体系
        new_fm["问题类型"] = None
        new_fm["问题备注"] = ""
        new_fm["最后练习"] = None

    # 写入新 frontmatter
    new_yaml = yaml.dump(
        new_fm, allow_unicode=True, default_flow_style=False, sort_keys=False
    )
    # 处理多行值（如 tags 的 inline list）
    # yaml.dump 默认使用 block 格式，手动调整 tags 为 inline
    new_content = f"---\n{new_yaml.rstrip()}\n---\n{body}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  OK: {filepath.name}")


def main():
    # Concepts
    print("=== Concepts ===")
    for f in sorted((WIKI_DIR / "Concepts").glob("*.md")):
        process_wiki_file(f, "concepts")

    # Theorems
    print("\n=== Theorems ===")
    for f in sorted((WIKI_DIR / "Theorems").glob("*.md")):
        process_wiki_file(f, "theorems")

    # Methods
    print("\n=== Methods ===")
    for f in sorted((WIKI_DIR / "Methods").glob("*.md")):
        process_wiki_file(f, "methods")

    print("\nDone!")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 创建脚本目录并运行迁移**

```bash
mkdir -p "D:/tool/Obsidian/math/scripts"
# 将上面的 Python 脚本写入 scripts/migrate_frontmatter.py

# 检查 Python 可用性
python3 --version 2>/dev/null || python --version 2>/dev/null

# 安装 PyYAML（如缺失）
pip install pyyaml 2>/dev/null || pip3 install pyyaml 2>/dev/null

# 运行迁移
cd "D:/tool/Obsidian/math"
python scripts/migrate_frontmatter.py
```

预期输出：显示每个文件 OK，最终 DONE。

- [ ] **Step 3: 抽样验证迁移结果**

```bash
echo "=== Concepts ==="
head -10 "01_Wiki/Concepts/导数-Derivative.md"
echo "=== Methods ==="
head -10 "01_Wiki/Methods/分部积分法-IntegrationByParts.md"
echo "=== Theorems ==="
head -10 "01_Wiki/Theorems/格林公式-GreensTheorem.md"
```

检查要点：
- 字段名是否为中文（`标题`, `标签`, `创建日期`, `掌握状态` 等）
- `类型` 是否已改为 `永久笔记`
- Methods 的 `问题类型: null` 和 `问题备注: ""` 是否存在
- Concepts/Theorems 的 `掌握状态: 待编译` 是否正确
- `来源` 字段值是否保留

- [ ] **Step 4: 检查是否存在 tags 格式问题**

由于 `yaml.dump` 默认将列表写为 block 格式，会导致 `标签` 从 `[数学, 第3讲, 概念]` 变为：
```yaml
标签:
- 数学
- 第3讲
- 概念
```
Dataview 支持两种格式，但 inline 格式更紧凑。如果 step 3 验证发现 tags 变成 block 格式，执行以下修复脚本：

```python
#!/usr/bin/env python3
"""将 block 格式的 tags 转为 inline 格式（如果需要）"""
from pathlib import Path
import re

wiki_dir = Path("D:/tool/Obsidian/math/01_Wiki")
for subdir in ["Concepts", "Theorems", "Methods"]:
    for f in sorted((wiki_dir / subdir).glob("*.md")):
        content = f.read_text(encoding="utf-8")
        # 检查是否 block 格式的标签
        if "标签:\n" in content:
            # 提取标签值并转为 inline
            lines = content.split("\n")
            new_lines = []
            i = 0
            while i < len(lines):
                if lines[i].startswith("标签:") and i + 1 < len(lines) and lines[i + 1].strip().startswith("- "):
                    tags = []
                    i += 1
                    while i < len(lines) and lines[i].strip().startswith("- "):
                        tags.append(lines[i].strip()[2:])
                        i += 1
                    new_lines.append(f"标签: [{', '.join(tags)}]")
                    continue
                new_lines.append(lines[i])
                i += 1
            f.write_text("\n".join(new_lines), encoding="utf-8")
            print(f"  FIXED: {f.name}")
```

- [ ] **Step 5: 提交**

```bash
git add scripts/ 01_Wiki/
git commit -m "feat: 全量 frontmatter 中文化迁移 (Concepts/Theorems/Methods)"
```

---

### Task 4: 更新现有日记 frontmatter

**Files:**
- Modify: `03_Daily/2026-05-04.md`

- [ ] **Step 1: 更新日记 frontmatter**

```yaml
---
标题: 2026-05-04
标签: [日记, 学习日志]
创建日期: 2026-05-04
类型: 日记
---
```

使用 Edit 工具将原有 frontmatter 替换。

- [ ] **Step 2: 提交**

```bash
git add 03_Daily/
git commit -m "chore: 更新日记 frontmatter 为中文字段"
```

---

### Task 5: 创建初始 MOC 索引页

**Files:**
- Create: `01_Wiki/MOC/README.md`（MOC 目录说明）
- Create: `01_Wiki/MOC/一元函数微分学-MOC.md`（示例 MOC）

- [ ] **Step 1: 创建 MOC 目录说明**

```markdown
---
标题: MOC 索引
标签: [数学, 目录, 索引]
创建日期: 2026-05-05
类型: 永久笔记
摘要: 章节级 Map of Content 入口，统领各章知识点
---

# MOC 索引

各章节知识地图：

- [[01_Wiki/MOC/一元函数微分学-MOC|一元函数微分学]]
```

- [ ] **Step 2: 创建示例 MOC（一元函数微分学）**

基于现有 Concepts/Theorems/Methods 中 `第3讲` 到 `第7讲` 标签的页面：

```markdown
---
标题: 一元函数微分学
标签: [数学, 微积分, 索引]
创建日期: 2026-05-05
类型: 永久笔记
摘要: 一元函数微分学知识图谱（第3-7讲）
---

# 一元函数微分学

## 核心概念
![[Concepts/导数-Derivative#定义]]
![[Concepts/微分-Differential#定义]]

## 关键定理
![[Theorems/费马定理-FermatTheorem#陈述]]
![[Theorems/罗尔定理-RolleTheorem#陈述]]
![[Theorems/拉格朗日中值定理-LagrangeMVT#陈述]]

## 解题方法
![[Methods/极限计算方法-LimitCalculationMethods#适用条件]]
```

注意：此 MOC 仅为示例框架，具体嵌入内容需在后续手动补充章节锚点。

- [ ] **Step 3: 提交**

```bash
git add 01_Wiki/MOC/
git commit -m "feat: 创建 MOC 索引目录及一元函数微分学示例页面"
```

---

### Task 6: 创建标准化 02_Output 文件

**Files:**
- Create: `02_Output/弱点报告.md`
- Create: `02_Output/复习清单.md`

- [ ] **Step 1: 创建 复习清单.md**

```markdown
---
标题: 复习清单
标签: [数学, 输出, 复习]
创建日期: 2026-05-05
类型: 永久笔记
摘要: 当前存在问题的解题方法清单，按最后练习时间排序
---

# 复习清单

```dataview
TABLE 问题类型 AS 问题, 问题备注 AS 备注, 最后练习 AS 最后练习日期, 摘要 AS 方法概述
FROM "01_Wiki/Methods"
WHERE 问题类型 != null
SORT 最后练习 ASC
```
```

- [ ] **Step 2: 创建 弱点报告.md**

```markdown
---
标题: 弱点报告
标签: [数学, 输出, 分析]
创建日期: 2026-05-05
类型: 永久笔记
摘要: 基于题目记录的错因分布分析
---

# 弱点报告

## 错因分布

```dataview
TABLE rows.错因类型 AS 错因, length(rows) AS 题数
FROM "01_Wiki/Records"
WHERE 错因类型 != null
GROUP BY 错因类型
SORT length(rows) DESC
```

## 近期错题

```dataview
TABLE 来源 AS 题目, 错因类型 AS 错因, 关联方法 AS 关联方法
FROM "01_Wiki/Records"
WHERE 题目状态 = "首次做错"
SORT 创建日期 DESC
```
```

- [ ] **Step 3: 删除旧的 README.md（可选）**

```bash
# 02_Output 下的 README.md 已被 v2 标准文件替代
rm 02_Output/README.md
```

- [ ] **Step 4: 提交**

```bash
git add 02_Output/
git commit -m "feat: 创建标准化输出文件（弱点报告 + 复习清单）"
```

---

### Task 7: 更新 CLAUDE.md 和 SCHEMA.md

**Files:**
- Modify: `CLAUDE.md`
- Modify: `SCHEMA.md`

- [ ] **Step 1: 更新 CLAUDE.md**

将 `CLAUDE.md` 整体替换为 v2 规范。关键改动点：
- 角色定义：不变
- 知识库结构：更新目录树为 v2 结构
- 行为准则：Methods 的置信体系改为 `问题类型` 标记，新增 Chains 相关准则
- 编译算法：归档路径改为 `00_Raw/Archive/Lectures/` 和 `00_Raw/Archive/Problems/`
- 模板引用：指向中文命名的模板文件

- [ ] **Step 2: 更新 SCHEMA.md**

关键改动：
- 命名规范：新增 `推导链页`、`题目记录页` 命名规则
- 标签规范：状态标签改为中文（`#待编译`、`#已建立心智模型`、`#已练习验证`）
- 文件组织：更新为 v2 目录树
- Frontmatter 模板：替换为 v2 中文字段
- 归档记录：不变

- [ ] **Step 3: 提交**

```bash
git add CLAUDE.md SCHEMA.md
git commit -m "docs: 更新 CLAUDE.md 和 SCHEMA.md 为 v2 规范"
```

---

### Task 8: 全量检查与验证

**Files:**
- 所有迁移后的文件

- [ ] **Step 1: 统计文件数量**

```bash
echo "=== 文件统计 ==="
echo -n "Concepts:  " && ls 01_Wiki/Concepts/*.md | wc -l
echo -n "Theorems:  " && ls 01_Wiki/Theorems/*.md | wc -l
echo -n "Methods:   " && ls 01_Wiki/Methods/*.md | wc -l
echo -n "Chains:    " && ls 01_Wiki/Chains/*.md | wc -l
echo -n "Records:   " && ls 01_Wiki/Records/*.md | wc -l
echo -n "MOC:       " && ls 01_Wiki/MOC/*.md | wc -l
echo -n "Templates: " && ls 04_Templates/*.md | wc -l
echo -n "Archive:   " && ls 00_Raw/Archive/Lectures/*.md | wc -l
echo -n "Daily:     " && ls 03_Daily/*.md | wc -l
```

- [ ] **Step 2: 检查是否有遗漏英文 frontmatter 的 Wiki 文件**

```bash
# 查找任何文件中仍含有英文 frontmatter 字段名
grep -l "^title:" 01_Wiki/Concepts/*.md 01_Wiki/Theorems/*.md 01_Wiki/Methods/*.md
# 预期输出为空（表示所有都迁移完成）
```

- [ ] **Step 3: 验证 frontmatter 完整性**

```bash
# 检查必填字段是否存在
for dir in Concepts Theorems Methods; do
    for f in 01_Wiki/$dir/*.md; do
        missing=""
        head -20 "$f" | grep -q "标题:"    || missing="$missing 标题"
        head -20 "$f" | grep -q "标签:"     || missing="$missing 标签"
        head -20 "$f" | grep -q "创建日期:" || missing="$missing 创建日期"
        head -20 "$f" | grep -q "类型:"     || missing="$missing 类型"
        head -20 "$f" | grep -q "摘要:"     || missing="$missing 摘要"
        head -20 "$f" | grep -q "来源:"     || missing="$missing 来源"
        if [ -n "$missing" ]; then
            echo "MISSING:$f ->$missing"
        fi
    done
done
```

预期输出为空（无缺失字段）。

- [ ] **Step 4: 最终提交**

```bash
git add -A
git status
git commit -m "chore: v1→v2 迁移全量验证通过"
```

---

### 执行顺序总结

| 序号 | Task | 操作类型 | 影响文件数 |
|---|---|---|---|
| 1 | 目录结构调整 | mkdir + mv | 24 个文件搬迁 |
| 2 | 创建模板 | 创建 5 个新文件 + 更新 1 个 | 6 个文件 |
| 3 | Frontmatter 迁移 | Python 批处理 | ~148 个文件 |
| 4 | 日记更新 | 手动编辑 | 1 个文件 |
| 5 | MOC 创建 | 创建新文件 | 2 个文件 |
| 6 | 02_Output | 创建新文件 | 2 个文件 |
| 7 | 文档更新 | 大幅修改 | 2 个文件 |
| 8 | 全量验证 | grep 检查 | — |
