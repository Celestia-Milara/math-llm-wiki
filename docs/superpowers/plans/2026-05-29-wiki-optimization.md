# 考研数学 LLM Wiki 优化计划

> **创建日期:** 2026-05-29
> **审查人:** Claude Code
> **状态:** 待执行

---

## 背景

2026-05-29 对项目进行了全面审查，发现以下关键问题：
- `章节映射.json` 路径全部指向旧目录（`00_Raw/`），导致 AI 导航功能失效
- `03_Wiki/ProblemTypes/` 目录完全空白，题型识别能力缺失
- `04_Records/KeyProblems/`、`04_Records/ConceptReviews/`、`04_Records/Reviews/` 均为空
- 部分模板的 Dataview 查询有误
- Wiki frontmatter 来源路径格式不统一
- 复习状态更新机制缺失

---

## 任务总览

| # | 任务 | 涉及文件 | 依赖 |
|---|------|---------|------|
| 1 | 修复章节映射.json 路径 | `01_Raw/章节映射.json` | 无 |
| 2 | 建立 ProblemTypes 页面 | `03_Wiki/ProblemTypes/` 下新建 5 个文件 | 无 |
| 3 | 修复模板 Dataview 查询 | `06_Templates/` 下 3 个文件 | 无 |
| 4 | 统一 Wiki frontmatter 来源路径 | `03_Wiki/` 下约 10 个文件 | 无 |
| 5 | 更新 CLAUDE.md 增加复习指令 | `CLAUDE.md` | 无 |
| 6 | 验证所有修改 | 全库 | 任务1-5完成后 |

---

## Task 1: 修复章节映射.json 路径

**文件:**
- 修改: `01_Raw/章节映射.json`

**说明:** 当前所有文件路径前缀为 `"00_Raw/`，应统一替换为 `"01_Raw/`。同时需要确认每个路径对应的文件是否真实存在于目标位置。

**步骤:**

- [ ] **Step 1: 备份原文件**

```powershell
Copy-Item "D:\tool\Obsidian\math\01_Raw\章节映射.json" "D:\tool\Obsidian\math\01_Raw\章节映射.json.bak"
```

- [ ] **Step 2: 读取文件内容，确认替换范围**

使用 Read 工具读取 `01_Raw/章节映射.json` 全文。

- [ ] **Step 3: 批量替换路径前缀**

将文件中所有 `"00_Raw/` 替换为 `"01_Raw/`：

```json
// 替换前：
"讲义": "00_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md"
"文件": "00_Raw/Archive/Problems\\01_第1讲_函数极限与连续_试题.md"

// 替换后：
"讲义": "01_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md"
"文件": "01_Raw/Archive/Problems/01_第1讲_函数极限与连续_试题.md"
```

同时将反斜杠 `\\` 统一为正斜杠 `/`。

- [ ] **Step 4: 验证关键路径是否存在**

从映射中取 3 个讲次的文件路径，用 Glob 工具验证文件是否存在。例如：

```
01_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md
01_Raw/Archive/Lectures/06_第6讲_一元函数微分学的应用(二).md
01_Raw/Archive/Problems/06_第6讲_一元函数微分学的应用（二）——中值定理、微分等式与微分不等式_试题.md
```

如果路径不存在，记录下来，后续任务中统一处理（可能文件实际在 `01_Raw/` 根目录而非 `Archive/` 子目录）。

---

## Task 2: 建立 ProblemTypes 页面

**文件:**
- 创建: `03_Wiki/ProblemTypes/渐近线综合判断题.md`
- 创建: `03_Wiki/ProblemTypes/中值定理极限题.md`
- 创建: `03_Wiki/ProblemTypes/辅助函数构造题.md`
- 创建: `03_Wiki/ProblemTypes/微分不等式证明题.md`
- 创建: `03_Wiki/ProblemTypes/定积分存在性与原函数存在性辨析题.md`

**说明:** 每个题型页必须包含：识别信号、步骤 SOP、避坑指南、关联错题链接。使用 `06_Templates/题型模板.md` 作为基础模板。

**步骤:**

- [ ] **Step 1: 创建 `03_Wiki/ProblemTypes/渐近线综合判断题.md`**

Frontmatter:
```yaml
---
标题: 渐近线综合判断题
标签: [数学, 第5讲, 题型]
创建日期: 2026-05-29
类型: 题型
问题类型:
摘要: 含铅直渐近线、水平渐近线、斜渐近线的综合判断，需分别讨论 x→a、x→±∞ 等方向
来源:
AI状态: 待核查
---
```

正文必须包含：
- 识别信号：函数含分式/对数/指数组合，定义域有间断点，$x\to\pm\infty$ 方向
- 步骤 SOP：① 找无定义点 → ② $x\to x_0$ 铅直渐近线 → ③ $x\to\pm\infty$ 水平/斜渐近线
- 避坑指南：$x\to+\infty$ 和 $x\to-\infty$ 必须分别计算；$y$ 轴铅直渐近线找 $x=0$；斜渐近线 $a=\lim y/x$，$b=\lim(y-ax)$
- 关联错题：`04_Records/Mistakes/05_题15_渐近线综合判断.md`、`04_Records/Mistakes/05_题20_渐近线条数.md`、`04_Records/Mistakes/05_题22_斜渐近线计算.md`、`04_Records/Mistakes/05_题23_多方向渐近线.md`

- [ ] **Step 2: 创建 `03_Wiki/ProblemTypes/中值定理极限题.md`**

Frontmatter:
```yaml
---
标题: 中值定理极限题
标签: [数学, 第6讲, 题型]
创建日期: 2026-05-29
类型: 题型
问题类型:
摘要: 通过拉格朗日/柯西中值定理将含中值的表达式转化为参数，再求极限
来源:
AI状态: 待核查
---
```

正文必须包含：
- 识别信号：题目中出现"存在 $\theta\in(0,1)$ 使得..." 或 "$\xi$"；最终要求某个含参数的极限
- 关键步骤：① 用中值定理建立等式 → ② 解出 $\theta$ 或 $\xi$ 的表达式 → ③ 求极限
- 避坑指南：不能直接对原式取极限，必须先解出 $\theta$ 表达式；$\theta$ 是 $x$ 的函数
- 关联错题：`04_Records/Mistakes/06_题5_拉格朗日中值定理极限.md`

- [ ] **Step 3: 创建 `03_Wiki/ProblemTypes/辅助函数构造题.md`**

Frontmatter:
```yaml
---
标题: 辅助函数构造题
标签: [数学, 第6讲, 题型]
创建日期: 2026-05-29
类型: 题型
问题类型:
摘要: 通过构造辅助函数将待证等式/不等式转化为罗尔定理的形式
来源:
AI状态: 待核查
---
```

正文必须包含：
- 识别信号：证明题中出现 $f'(\xi)g(\xi)+h(\xi)f(\xi)=0$ 或 $f'(\xi)=\lambda f(\xi)$ 等形式
- 常用构造模式表：
  - $f'(\xi)+\lambda f(\xi)=0$ → $F(x)=e^{\lambda x}f(x)$
  - $f'(\xi)-\lambda f(\xi)=0$ → $F(x)=e^{-\lambda x}f(x)$
  - $f'(\xi)g(\xi)-f(\xi)g'(\xi)=0$ → $F(x)=f(x)/g(x)$
- 避坑指南：先移项再反推；验证 $F(a)=F(b)$
- 关联错题：`04_Records/Mistakes/06_题20_辅助函数构造.md`

- [ ] **Step 4: 创建 `03_Wiki/ProblemTypes/微分不等式证明题.md`**

Frontmatter:
```yaml
---
标题: 微分不等式证明题
标签: [数学, 第6讲, 题型]
创建日期: 2026-05-29
类型: 题型
问题类型:
摘要: 利用单调性、中值定理或泰勒公式证明微分不等式
来源:
AI状态: 待核查
---
```

正文必须包含：
- 识别信号：待证不等式涉及函数值之间的大小关系，通常需要移项构造 $F(x)$
- 三种主要方法：① 单调性法（求导判断 $F'(x)$ 符号）② 中值定理法（拉格朗日转化后放缩）③ 泰勒公式法（展开后利用余项）
- 方法选择信号：
  - 不等式仅涉及一个函数 → 优先单调性
  - 不等式涉及两个函数值之差 → 优先拉格朗日
  - 高阶导数出现或区间较大 → 优先泰勒
- 避坑指南：绝对值函数不可导，做题时需先处理
- 关联错题：`04_Records/Mistakes/06_题12_泰勒展开不等式.md`、`04_Records/Mistakes/06_题18_极值证明不等式.md`

- [ ] **Step 5: 创建 `03_Wiki/ProblemTypes/定积分存在性与原函数存在性辨析题.md`**

Frontmatter:
```yaml
---
标题: 定积分存在性与原函数存在性辨析题
标签: [数学, 第8讲, 题型]
创建日期: 2026-05-29
类型: 题型
问题类型:
摘要: 区分"定积分存在（可积）"与"原函数存在"的适用条件和关系
来源:
AI状态: 待核查
---
```

正文必须包含：
- 识别信号：题目问"是否存在原函数""是否可积"或两者都需要判定
- 核心辨析表（必须包含此表格）：
  - 连续函数 → 原函数存在 ✓，定积分存在 ✓
  - 有界 + 有限个第一类间断点 → 原函数不存在 ✗，定积分存在 ✓
  - 有界 + 振荡间断点 → 原函数可能存在 ?，定积分存在 ✓
- 避坑指南：定积分存在 ≠ 原函数存在；跳跃间断点处变限积分连续但不可导
- 关联错题：（目前第8讲暂无错题记录，可留空，待有错题后补充）

---

## Task 3: 修复模板 Dataview 查询

**文件:**
- 修改: `06_Templates/专题索引模板.md`
- 修改: `06_Templates/日记模板.md`

**说明:** `06_Templates/日记模板.md` 中的 Dataview 查询语句格式有误；`06_Templates/专题索引模板.md` 的查询逻辑无法正常工作。

**步骤:**

- [ ] **Step 1: 修复日记模板的 Dataview 查询**

读取 `06_Templates/日记模板.md`，将文件中的 Dataview 查询块替换为：

```dataview
TABLE WITHOUT ID
  file.link AS "文件名",
  记录原因 AS "类型",
  讲次 AS "讲次",
  题号 AS "题号"
FROM "04_Records"
WHERE file.mday >= this.file.mday - 7
SORT file.mday DESC
LIMIT 20
```

（当前日记模板无 Dataview 查询块，如果确认不需要则跳过此步。）

- [ ] **Step 2: 修复专题索引模板的 Dataview 查询**

读取 `06_Templates/专题索引模板.md`，将查询：

```dataview
TABLE 类型 AS 类型, 摘要 AS 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标题)
SORT 类型 ASC
```

替换为（专题索引模板的查询建议改为按讲次聚合的视图）：

```dataview
TABLE WITHOUT ID
  file.link AS "页面",
  类型 AS "类型",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, "第5讲") OR contains(标签, "第6讲")
SORT 类型 ASC
```

（注意：专题索引模板本身包含 `讲次` frontmatter 字段，理论上可以用 `WHERE 讲次 = this.讲次`，但 Obsidian Dataview 在模板文件中不支持 `this.讲次` 引用具体值，所以改为按标签匹配。）

---

## Task 4: 统一 Wiki frontmatter 来源路径格式

**文件:**
- 修改: `03_Wiki/` 下所有来源路径含 `01_Raw/Archive/` 和 `01_Raw/` 混用的页面

**说明:** 部分 Wiki 页面的 `来源` 字段指向 `01_Raw/03_第3讲...`（无 Archive），另一部分指向 `01_Raw/Archive/Lectures/06_第6讲...`，格式不统一。应统一为 `01_Raw/Archive/Lectures/` 格式（或根据实际文件位置决定）。

**步骤:**

- [ ] **Step 1: 扫描所有 Wiki 页面，找出来源路径格式**

```bash
grep "^来源:" 03_Wiki/Concepts/*.md 03_Wiki/Theorems/*.md 03_Wiki/Methods/*.md 03_Wiki/Hubs/*.md
```

- [ ] **Step 2: 确认实际讲义文件位置**

用 Glob 工具分别检查以下路径是否存在：

```
01_Raw/03_第3讲_一元函数微分学的概念.md        （Wiki 页面中引用的路径）
01_Raw/Archive/Lectures/03_第3讲_一元函数微分学的概念.md  （映射文件中的路径）
```

- [ ] **Step 3: 根据实际位置统一来源路径**

如果讲义在 `01_Raw/Archive/Lectures/` 下，则将所有 `01_Raw/数字_` 格式的来源改为 `01_Raw/Archive/Lectures/` 格式。

需要修改的典型页面（根据已有样本）：
- `03_Wiki/Concepts/导数-Derivative.md`：`来源: 01_Raw/03_第3讲_一元函数微分学的概念.md`
- `03_Wiki/Theorems/泰勒公式-TaylorFormula.md`：`来源: 01_Raw/01_第1讲_函数极限与连续.md, 01_Raw/06_第6讲...`

---

## Task 5: 更新 CLAUDE.md 增加复习指令

**文件:**
- 修改: `CLAUDE.md`

**说明:** 当前 CLAUDE.md 缺少"复习更新"工作流，导致错题记录的 `复习状态` 和 `下次复习日期` 从创建后就无人更新。需要在第4节"三个高频工作流"中增加第4个工作流。

**步骤:**

- [ ] **Step 1: 在 CLAUDE.md 第4节末尾增加工作流**

读取 `CLAUDE.md`，找到第4节末尾（`### 4.3 审查概念理解` 之后），追加以下内容：

````markdown
### 4.4 更新复习记录

触发：用户完成错题重做、或者需要更新复习状态。

流程：
1. 找到对应的 `04_Records/Mistakes/` 或 `04_Records/KeyProblems/` 文件。
2. 更新 `复习状态`：
   - 重做正确 → `已纠正`
   - 重做仍错 → `已重做仍错`，下次复习日期 +3天
   - 已完全掌握 → `已掌握`
3. 在复习记录表格中追加一行（日期、动作、结果）。
4. 如果该题已连续正确两次以上，可以将其标记为 `已掌握` 并更新下次复习日期为空。

**间隔重复原则：**
- 首次错 → 1天后复习
- 重做仍错 → 3天后复习
- 重做正确 → 7天后复习
- 连续两次正确 → `已掌握`，不再提醒

### 4.5 生成薄弱环节诊断

触发：用户学完一讲、做完练习后，或主动说"薄弱环节诊断"。

流程：
1. 读取 `04_Records/Mistakes/` 中该讲的错题记录。
2. 按 `错因类型` 聚合统计，识别高频错因。
3. 按 `关联方法` 聚合，识别薄弱方法。
4. 生成诊断报告，写入 `05_Outputs/StageSummaries/YYYY-MM-DD_第N讲薄弱环节.md`。
5. 如果发现某方法/题型反复出错，提示是否需要建立 `03_Wiki/ProblemTypes/` 页面。
````

---

## Task 6: 验证所有修改

**文件:** 无需创建新文件，但需逐一确认前面任务的质量。

**步骤:**

- [ ] **Step 1: 验证章节映射.json**

读取修复后的 `01_Raw/章节映射.json`，确认：
- 不再有 `"00_Raw/` 路径
- JSON 格式可被正常解析
- 取 3 个讲次的文件路径用 Glob 验证存在

- [ ] **Step 2: 验证 ProblemTypes 页面**

检查 5 个新建的 ProblemTypes 页面：
- 每个页面 frontmatter 包含 `标题`、`标签`、`类型`、`AI状态`
- 每个页面正文包含"识别信号""避坑指南"等章节
- 每个页面底部的 Dataview 关联错题查询中的文件路径与实际存在相符

- [ ] **Step 3: 验证模板 Dataview 查询**

读取修复后的 `06_Templates/专题索引模板.md`，确认 Dataview 查询语法正确。

- [ ] **Step 4: 验证 CLAUDE.md**

读取修复后的 `CLAUDE.md`，确认第4.4节和第4.5节内容已正确追加，格式与现有内容一致。

---

## 执行方式选择

计划完成并保存后，有两种执行方式：

**1. 子 Agent 驱动（推荐）** — 每个任务由独立子 Agent 执行，期间有检查点回顾，迭代快

**2. 内联执行** — 在当前会话中顺序执行所有任务，每个检查点后暂停等待确认

**选择哪种方式？**
