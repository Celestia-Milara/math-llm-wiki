---
标题: 极限的性质
标签: [数学, 第1讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 极限存在则必然满足唯一性、局部有界性、局部保号性。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 1. 唯一性

如果极限 $\lim_{x \to x_0} f(x)$ 存在，则极限唯一。

> 一个超实数有唯一的"核"（标准实数部分）。

## 2. 局部有界性

如果 $\lim_{x \to x_0} f(x) = A$，则存在常数 $M > 0$ 和 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，$|f(x)| \le M$。

## 3. 局部保号性

如果 $f(x) \to A > 0$（或 $A < 0$），则存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，$f(x) > 0$（或 $f(x) < 0$）。

**推论**：如果在 $x_0$ 的某去心邻域内 $f(x) \ge 0$ 且 $\lim_{x \to x_0} f(x) = A$，则 $A \ge 0$。

> 核心思想：只要核（极限值）大于零，其所有"光晕"（邻域内的函数值）都大于零。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
