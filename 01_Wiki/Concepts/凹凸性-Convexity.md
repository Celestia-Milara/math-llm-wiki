---
title: 凹凸性
tags: [数学, 第5讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 曲线弯曲方向的几何性质，由二阶导数的符号判定。
source: 00_Raw/05_第5讲_一元函数微分学的应用(一).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定义 1（弦中点法）

设 $f(x)$ 在区间 $I$ 上连续。若对 $I$ 上任意不同两点 $x_1, x_2$，恒有

$$
f\left(\frac{x_1 + x_2}{2}\right) < \frac{f(x_1) + f(x_2)}{2}
$$

则称 $y = f(x)$ 在 $I$ 上的图形是**凹的**（图形上任意弧段位于弦的下方）。

若恒有

$$
f\left(\frac{x_1 + x_2}{2}\right) > \frac{f(x_1) + f(x_2)}{2}
$$

则称 $y = f(x)$ 在 $I$ 上的图形是**凸的**（图形上任意弧段位于弦的上方）。

## 定义 2（切线法）

设 $f(x)$ 在 $[a,b]$ 上连续，在 $(a,b)$ 内可导。若曲线在任意点处的切线（除该点外）总在曲线的**下方**，则该曲线是**凹的**；若切线总在曲线的**上方**，则该曲线是**凸的**。

## 凹凸性的判别

设 $f(x)$ 在 $I$ 上二阶可导：

1. 若在 $I$ 上 $f''(x) > 0$，则 $f(x)$ 在 $I$ 上的图形是**凹**的。
2. 若在 $I$ 上 $f''(x) < 0$，则 $f(x)$ 在 $I$ 上的图形是**凸**的。

---

**来源**：`00_Raw/05_第5讲_一元函数微分学的应用(一).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
