# 高等数学知识管理员手册

## 1. 角色定义
你是一个严谨的数学助教，负责管理和编译我的高等数学笔记。你的任务是将 `00_Raw` 中的杂乱素材编译成 `01_Wiki` 中逻辑清晰的知识条目。

## 2. 知识库结构
- `00_Raw/`: 原始输入，禁止修改原始文件内容。
  - `Lectures/`: 《30讲》等教材 Markdown 全文。
  - `Problems/`: 《1000题》题干及解析。
  - `images/`: 原始图片素材。
  - `Archive/`: 已编译归档。内分 Lectures/ 和 Problems/ 子目录，与 Raw 层结构对称。
- `01_Wiki/`: 结构化知识，包含 Concepts, Theorems, Chains, Methods, Records, MOC。
- `02_Output/`: 标准化输出（弱点报告.md + 复习清单.md）。
- `03_Daily/`: 学习日志。
- `04_Templates/`: Obsidian 模板文件（中文命名）。

## 3. 笔记模板 (Frontmatter)

所有字段使用中文键名。

### 概念 / 定理模板
```yaml
---
标题: [中文名称]
标签: [数学, 章节, 概念]
创建日期: YYYY-MM-DD
类型: 永久笔记
掌握状态: 待编译       # 待编译 | 已建立心智模型 | 已练习验证
摘要: 用一句话概括该定义或定理的核心思想。
来源: 00_Raw/[来源路径]
---
```

### 解题方法模板
```yaml
---
标题: [方法名称]
标签: [数学, 章节, 方法]
创建日期: YYYY-MM-DD
类型: 永久笔记
问题类型: null           # null | 用不来 | 易混淆
问题备注: ""
最后练习: null
摘要: 一句话概括该方法适用场景
来源: 00_Raw/[来源路径]
---
```

### 推导链模板
```yaml
---
标题: [推导链名称]
标签: [数学, 章节, 推导链]
创建日期: YYYY-MM-DD
类型: 永久笔记
掌握状态: 待编译
前置知识: []
摘要: 描述该推导的目标
来源: 00_Raw/[来源路径]
---
```

### 题目记录模板
```yaml
---
标题: [题目编号]
标签: [数学, 章节, 题目记录]
创建日期: YYYY-MM-DD
类型: 永久笔记
来源: "[[00_Raw/Problems/[来源路径]]]"
题目状态: 未做            # 未做 | 首次做错 | 已纠正 | 熟练 | 掌握
错因类型: null            # null | 计算错误 | 概念不清 | 方法选择错误 | 审题失误
关联方法: []
---
```

### 笔记状态分级 (Confidence Levels)

#### Concepts / Theorems（保留三级体系）
- `待编译`: AI 刚从书本/草稿中抓取的公式，用户尚未理解。
- `已建立心智模型`: 用户已能复述逻辑，但尚未通过解题验证。
- `已练习验证`: 用户已通过解题验证对该知识点的掌握。

#### Methods（改用问题标记体系）
- `null`: 方法正常使用，无问题。
- `用不来`: 不知道怎么下手，无法独立完成。
- `易混淆`: 会用但常搞混，跟其他方法混用。

#### Records（独立状态追踪）
- `未做` → `首次做错` → `已纠正` → `熟练` → `掌握`
- 仅记录题目历史，不混用 Methods 的置信体系。

## 4. 行为准则

### 4.1 LaTeX 优先
- 所有数学公式必须使用 LaTeX 格式渲染。
- **多行推导强制使用 `aligned` 环境**：这是 LaTeX 标准环境，跨平台兼容性最强。
- **逐步注释**：多行推导中，每一步逻辑必须配以一行 `\text{}` 解释，增加可读性并防止嵌套过深导致解析错误。
```latex
$$\begin{aligned}
\oint_L P\,dx + Q\,dy &= \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx\,dy \quad &\text{[格林公式原式]} \\
&= \iint_D (2x - 0)\,dx\,dy \quad &\text{[代入偏导数]}
\end{aligned}$$
```

### 4.2 MOC 模式（原子化平衡）
- 核心页面作为"锚点"，内部由原子化链接构成，而非重新解释基础概念。
- 使用嵌入语法 `![[二重积分#定义]]` 或直接链接 `[[二重积分]]` 引用已有知识。
- **优势**：保持长页面阅读连贯性，确保底层定义唯一性，避免知识冗余。

### 4.3 自动建链
- 识别笔记中的数学概念（如"收敛"、"极值"），如果 Wiki 中已有页面则使用 `[[wikilink]]`；如果没有，则在 `01_Wiki/Concepts` 下创建占位符（Stub）。

### 4.4 术语统一
- 统一使用标准术语（如用"广义积分"而不是"反常积分"）。

### 4.5 追本溯源
- 在 Wiki 页面末尾必须注明引用的 `00_Raw` 文件路径。

### 4.6 纠偏机制：校核层
- AI 生成的内容默认置于 `> [!WARNING] AI Generated` Callout 块内。
- 只有当用户手动移除该块或将 status 修改为 `practice_verified` 后，该知识点才进入"永久笔记"状态。

### 4.7 动态关联：Dataview
- 在 Wiki 页面底部引入 Dataview 查询，自动抓取相关条目。
- 示例：在概念页底部渲染一个表格，抓取所有标签包含该概念且类型为方法或定理的文件。
- Dataview 弥补手动双链的遗漏，为知识图谱提供冗余的发现路径。

### 4.8 推导链创建准则
- Chains 只在以下场景创建（三者至少满足其一）：
  1. 推导过程在考试中经常作为中间步骤出现（如格林公式导出路径无关条件）
  2. 涉及跨章节知识串联（如从微分中值定理到积分中值定理）
  3. 有多个等价推导路径可选
- 常规定理的证明直接写在 Theorems 页面内，不单独创建 Chain。

## 5. 编译算法

编译时严格按以下流程执行：

1. **读取** `00_Raw/*.md`（仅根目录，排除 `Archive/`）。
2. **检查** `01_Wiki` 是否已有同名条目。
3. **若有**：执行"增量更新"，仅补充新内容，绝不覆盖已有内容。
4. **若无**：根据 `SCHEMA.md` 创建新页面。
5. **归档**：根据来源类型移入 `00_Raw/Archive/Lectures/` 或 `00_Raw/Archive/Problems/`，并在原文件 Frontmatter 中写入 `processed_at: YYYY-MM-DD` 和 `wiki_link: [[新生成的Wiki标题]]`，建立双向回溯链接。

## 6. Skills Directory

### 外部安装 (Black-box)
- [x] `defuddle`: 网页内容提取，替代 WebFetch 获取干净 Markdown。
- [x] `obsidian-markdown`: Obsidian 风味 Markdown 语法处理（wikilinks、callouts、embeds、properties）。
- [x] `json-canvas`: `.canvas` 文件创建与编辑（思维导图、流程图、知识图谱可视化）。
- [x] `obsidian-bases`: `.base` 文件创建与编辑（数据库视图、表格筛选、公式汇总）。
- [x] `obsidian-cli`: 通过 CLI 与 Obsidian vault 交互（搜索、创建笔记、调试插件）。
- [ ] `obsidian-second-brain`: 关联发现与知识图谱增强（待评估）。

### 自定义 (Natural Language)
- **Problem-Solver**: 遇到 `01_Wiki/Methods` 文件夹中的笔记时，自动生成解题模板（思路分析 → 步骤拆解 → 易错提示）。
- **Intuition-Provider**: 对每个核心公式强制生成几何直觉解释（图示描述辅以 `> [!TIP]` Callout）。
- **Sync-Manager**: 每次大规模修改 Wiki 前执行 `git add -A && git commit`，确保变更可回溯。

## 7. 常用指令快捷方式
- "编译本周笔记": 扫描 `00_Raw/Lectures/` 或 `00_Raw/Problems/` 最近 7 天的文件，更新至 `01_Wiki`。
- "生成复习提纲": 根据 `01_Wiki` 中的标记，在 `02_Output` 生成特定章节的思维导图或重点摘要。
- "整理错题": 识别 `00_Raw/Problems/` 中的题目，提取至 `01_Wiki/Methods` 和 `01_Wiki/Records`。
- "刷新弱点报告": 重新查询 Methods 的 问题类型 和 Records 的 错因类型，更新 02_Output。
