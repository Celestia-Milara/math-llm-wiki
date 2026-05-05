---
标题: 单调性
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 函数值随自变量增大而单调增加或减少的性质。
来源: 00_Raw/01_第1讲_函数极限与连续.md, 00_Raw/05_第5讲_一元函数微分学的应用(一).md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设 $f(x)$ 的定义域为 $D$，区间 $I \subset D$。对任意 $x_1, x_2 \in I$ 且 $x_1 < x_2$：

- **单调增加（严格）**：$f(x_1) < f(x_2)$
- **单调减少（严格）**：$f(x_1) > f(x_2)$

## 定义的等价形式

对任意 $x_1 \neq x_2$：

- 严格单增 $\Leftrightarrow (x_1 - x_2)[f(x_1) - f(x_2)] > 0$
- 严格单减 $\Leftrightarrow (x_1 - x_2)[f(x_1) - f(x_2)] < 0$
- 单调不减 $\Leftrightarrow (x_1 - x_2)[f(x_1) - f(x_2)] \geqslant 0$
- 单调不增 $\Leftrightarrow (x_1 - x_2)[f(x_1) - f(x_2)] \leqslant 0$

## 判别方法

1. **定义法**：充要条件
2. **导数法**：
   - 若 $f'(x) \geq 0$ 且等号仅在有限个点处成立，则 $f(x)$ 严格单调增加。
   - 若 $f'(x) \leq 0$ 且等号仅在有限个点处成立，则 $f(x)$ 严格单调减少。
   - 导数大于 0 是严格单调增加的**充分不必要**条件（如 $y = x^3$ 在 $x = 0$ 处导数为 0 但仍严格单调增加）。

## 相关条目

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
