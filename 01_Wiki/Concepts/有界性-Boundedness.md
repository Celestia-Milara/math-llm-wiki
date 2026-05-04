---
title: 有界性
tags: [数学, 第1讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 在指定区间内，函数值能被某正数 M "完全包起来"。
source: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设 $f(x)$ 的定义域为 $D$，数集 $I \subset D$。如果存在某个正数 $M$，使对任一 $x \in I$，有 $|f(x)| \leqslant M$，则称 $f(x)$ 在 $I$ 上有界；否则称无界。

## 几何理解

从几何上看，若函数 $y = f(x)$ 的图形能够被直线 $y = -M$ 和 $y = M$ "完全包起来"，则为有界。

## 重要注意

1. 讨论有界性**必须指明区间** $I$，不同区间结论不同。
   - 如 $y = \frac{1}{x}$ 在 $(2, +\infty)$ 内有界，但在 $(0, 2)$ 内无界。
2. 若在区间 $I$ 上存在点 $x_0$ 使得 $\lim_{x \to x_0} f(x) = \infty$，则 $f(x)$ 在 $I$ 上无界。

## 常用不等式证明有界

- $\frac{a+b}{2} \geqslant \sqrt{ab} \quad (a, b > 0)$
- $\frac{2}{\frac{1}{a} + \frac{1}{b}} \leqslant \sqrt{ab} \leqslant \frac{a+b}{2} \leqslant \sqrt{\frac{a^2+b^2}{2}} \quad (a, b > 0)$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
