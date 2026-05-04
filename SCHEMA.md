# 高等数学 Vault 格式规范

## 1. 公式规范
- **行内公式**: 使用 `$...$`，例如 `$x^2 + y^2 = z^2$`
- **独立公式**: 使用 `$$...$$`，例如：
  ```markdown
  $$\int_a^b f(x) \, dx = F(b) - F(a)$$
  ```
- **多行对齐**: 强制使用 `aligned` 环境，每步配 `\text{}` 注释：
  ```markdown
  $$\begin{aligned}
  f(x) &= x^2 + 1 \quad &\text{[原函数]} \\
  f'(x) &= 2x \quad &\text{[求导]}
  \end{aligned}$$
  ```

## 2. 命名规范
- **概念页**: `中文-英文.md`，例如 `导数-Derivative.md`、`极限-Limit.md`
- **定理页**: `定理中文名-Theorem.md`，例如 `中值定理-MeanValueTheorem.md`
- **方法页**: `方法名-Method.md`，例如 `换元积分法-SubstitutionMethod.md`
- **输出页**: `[日期]-[用途].md`，例如 `2026-04-27-复习提纲.md`

## 3. 链接规范
- **强制双向链接**: 遇到定理中引用的基础概念（如连续性、可导性），必须建立 `[[双向链接]]`。
- **MOC 嵌入**: 优先使用 `![[概念页#锚点]]` 嵌入已有定义，而非重新解释。
- **链接格式**: 使用 Wiki 链接 `[[文件名]]` 或 `[[文件名|显示文本]]`。
- **跨文件夹链接**: `[[Concepts/导数-Derivative|导数]]`

## 4. 标签规范
- 基础标签: `#数学`
- 章节标签: `#微积分` `#线性代数` `#概率论`
- 类型标签: `#概念` `#定理` `#方法` `#例题`
- 状态标签: `#raw_compilation` `#mental_model_formed` `#practice_verified` `#重点`

## 5. 文件组织
```
00_Raw/          - 原始素材（手写笔记扫描件、教材摘录、网课截图）
  Archive/       - 已编译归档（AI 编译后自动移入）
01_Wiki/
  Concepts/      - 核心定义与概念
  Theorems/      - 定理与证明
  Methods/       - 解题方法与技巧
02_Output/       - 生成的复习提纲、错题分析、知识对比
03_Daily/        - 学习日志与进度追踪
```

## 6. Frontmatter 完整模板
```yaml
---
title: [中文名称]
tags: [数学, 章节名, 类型]
created: YYYY-MM-DD
type: permanent
status: raw_compilation    # raw_compilation | mental_model_formed | practice_verified
summary: 用一句话概括该定义或定理的核心思想。
source: 00_Raw/YYYY-MM-DD-原始文件名   # 追本溯源
---
```

## 7. Wiki 页面正文结构
每个 Wiki 页面应按以下结构组织：

```markdown
> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义 / 定理陈述
（核心内容，使用 MOC 嵌入引用基础概念）

## 推导 / 证明
（逐步 aligned 推导，每步配 \text{} 注释）

## 实践与纠偏
- **经典例题**: [[02_Output/Problems/相关例题]]
- **易错点**: > [!CAUTION] 符号问题等关键注意事项
- **关联回溯**: 原始素材自 [[00_Raw/YYYY-MM-DD-原始文件]]

## 相关条目
（Dataview 自动渲染区域，勿手动编辑）
```

## 8. Dataview 查询模板
在 Wiki 页面底部放置以下 Dataview 查询（根据实际情况替换标签）：

````markdown
## 关联发现
```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
````

## 9. 归档记录
`00_Raw/Archive/` 中的文件需在 Frontmatter 追加：
```yaml
processed_at: YYYY-MM-DD
wiki_link: "[[01_Wiki/对应Wiki页面]]"
```
