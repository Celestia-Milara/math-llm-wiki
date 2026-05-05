---
标题: 极限四则运算法则
标签: [数学, 第1讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 当各极限都存在时，极限运算与四则运算可交换顺序。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 法则

设 $\lim f(x) = A$，$\lim g(x) = B$，则

1. **加减法**：$\lim [kf(x) \pm lg(x)] = kA \pm lB$（$k,l$ 为常数）
2. **乘法**：$\lim [f(x) \cdot g(x)] = A \cdot B$
3. **除法**：$\lim \frac{f(x)}{g(x)} = \frac{A}{B}$（$B \neq 0$）

> 口诀：加减乘除的极限等于极限的加减乘除（除法分母极限不为零）。

## 重要推论

- $\lim [f(x)]^n = [\lim f(x)]^n$
- 若 $\lim \frac{f(x)}{g(x)} = A$ 且 $\lim g(x) = 0$，则 $\lim f(x) = 0$
- 若 $\lim \frac{f(x)}{g(x)} = A \neq 0$ 且 $\lim f(x) = 0$，则 $\lim g(x) = 0$

## 慎用情况

当极限不存在时，不能直接套用四则运算法则。若恰有一个不存在，和差一定不存在；乘除可能存在也可能不存在。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
