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
- **推导链页**: `推导链名-Chain.md`，例如 `格林公式到路径无关-Chain.md`
- **题目记录页**: `来源-编号.md`，例如 `第8讲-例8.5.md`
- **输出页**: `[用途].md`，例如 `复习清单.md`、`弱点报告.md`

## 3. 链接规范
- **强制双向链接**: 遇到定理中引用的基础概念（如连续性、可导性），必须建立 `[[双向链接]]`。
- **MOC 嵌入**: 优先使用 `![[概念页#锚点]]` 嵌入已有定义，而非重新解释。
- **链接格式**: 使用 Wiki 链接 `[[文件名]]` 或 `[[文件名|显示文本]]`。
- **跨文件夹链接**: `[[Concepts/导数-Derivative|导数]]`

## 4. 标签规范
- 基础标签: `数学`
- 章节标签: `第3讲` `第9讲` `第18讲`（对应《30讲》讲次）
- 类型标签: `概念` `定理` `方法` `推导链` `题目记录` `索引`
- 状态标签: `待编译` `已建立心智模型` `已练习验证`（仅 Concepts/Theorems）

## 5. 文件组织
```
00_Raw/          - 原始素材
  Lectures/      - 教材 Markdown
  Problems/      - 习题题干及解析
  images/        - 原始图片素材
  Archive/       - 已编译归档
    Lectures/    - 已归档讲次
    Problems/    - 已归档题目
01_Wiki/
  Concepts/      - 核心定义与概念
  Theorems/      - 定理与证明
  Chains/        - 推导链（Why）
  Methods/       - 解题方法与技巧
  Records/       - 题目索引库（电子病历）
  MOC/           - 章节级索引页
02_Output/       - 弱点报告.md + 复习清单.md
03_Daily/        - 学习日志
04_Templates/    - 中文命名模板
```

## 6. Frontmatter 完整模板

### 概念 / 定理
```yaml
---
标题: [中文名称]
标签: [数学, 章节, 概念]
创建日期: YYYY-MM-DD
类型: 永久笔记
掌握状态: 待编译    # 待编译 | 已建立心智模型 | 已练习验证
摘要: 用一句话概括该定义或定理的核心思想。
来源: 00_Raw/原始文件路径
---
```

### 方法
```yaml
---
标题: [方法名称]
标签: [数学, 章节, 方法]
创建日期: YYYY-MM-DD
类型: 永久笔记
问题类型: null      # null | 用不来 | 易混淆
问题备注: ""
最后练习: null
摘要: 一句话概括该方法适用场景
来源: 00_Raw/原始文件路径
---
```

### 推导链
```yaml
---
标题: [推导链名称]
标签: [数学, 章节, 推导链]
创建日期: YYYY-MM-DD
类型: 永久笔记
掌握状态: 待编译
前置知识: []
摘要: 描述该推导的目标
来源: 00_Raw/原始文件路径
---
```

### 题目记录
```yaml
---
标题: [题目编号]
标签: [数学, 章节, 题目记录]
创建日期: YYYY-MM-DD
类型: 永久笔记
来源: "[[00_Raw/Problems/原始路径]]"
题目状态: 未做
错因类型: null
关联方法: []
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
```dataview
TABLE 掌握状态, 类型
FROM "01_Wiki"
WHERE contains(标签, this.标签[1])
SORT 创建日期 ASC
```
```

## 8. Dataview 查询模板
在 Wiki 页面底部放置以下 Dataview 查询（根据实际情况替换标签）：

````markdown
## 关联发现
```dataview
TABLE 掌握状态, 类型
FROM "01_Wiki"
WHERE contains(标签, this.标签[1])
SORT 创建日期 ASC
```
````

## 9. 归档记录
`00_Raw/Archive/Lectures/` 或 `00_Raw/Archive/Problems/` 中的文件需在 Frontmatter 追加：
```yaml
processed_at: YYYY-MM-DD
wiki_link: "[[01_Wiki/对应Wiki页面]]"
```
