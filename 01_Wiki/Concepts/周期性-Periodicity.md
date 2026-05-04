---
title: 周期性
tags: [数学, 第1讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 函数值以固定周期重复出现的性质。
source: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设 $f(x)$ 的定义域为 $D$，如果存在正数 $T$，使得对任一 $x \in D$，有 $x \pm T \in D$，且 $f(x + T) = f(x)$，则称 $f(x)$ 为周期函数，$T$ 为周期（一般指最小正周期）。

## 重要结论

1. 若 $f(x)$ 以 $T$ 为周期，则 $f(ax + b)$ 以 $\frac{T}{|a|}$ 为周期
2. 若 $g(x)$ 是周期函数，则复合函数 $f[g(x)]$ 也是周期函数
3. 若 $f(x)$ 是以 $T$ 为周期的可导函数，则 $f'(x)$ 也以 $T$ 为周期
4. 若 $f(x)$ 是以 $T$ 为周期的连续函数，则 $\int_0^x f(t)dt$ 以 $T$ 为周期 $\iff \int_0^T f(x)dx = 0$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
