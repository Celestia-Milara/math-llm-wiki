---
title: 拉格朗日中值定理证明积分不等式
tags: [数学, 第11讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 利用拉格朗日中值定理将函数值与导数值关联，证明积分不等式。
source: 00_Raw/11_第11讲_一元函数积分学的应用(二).md
---

## 方法概述

此方法多用于所给条件为"$f(x)$ 一阶可导"且某一端点值较简单（甚至为 0）的题目。

### 基本思路

1. 将积分区间分成两个子区间 $[0, x]$ 和 $[x, 1]$
2. 在每个子区间上使用拉格朗日中值定理
3. 利用导数最大值 $M$ 对 $|f(x)|$ 进行放缩

## 典型例题

**条件**：$f(x)$ 在 $[0, 1]$ 上具有一阶连续导数，$f(0) = f(1) = 0$，$M = \max_{x \in [0,1]} |f'(x)|$。

**结论**：

$$
\left| \int_0^1 f(x) \, \mathrm{d}x \right| \leqslant \frac{1}{4} M.
$$

**证明要点**：

在 $[0, x]$ 上：$f(x) = f'(\xi_1)x \Rightarrow |f(x)| \leqslant Mx$。

在 $[x, 1]$ 上：$f(x) = -f'(\xi_2)(1 - x) \Rightarrow |f(x)| \leqslant M(1 - x)$。

于是

$$
\begin{aligned}
\left| \int_0^1 f(x) \, \mathrm{d}x \right|
&\leqslant \int_0^x |f(t)| \, \mathrm{d}t + \int_x^1 |f(t)| \, \mathrm{d}t \\
&\leqslant M \int_0^x t \, \mathrm{d}t + M \int_x^1 (1 - t) \, \mathrm{d}t \\
&= M\left[ \frac{x^2}{2} + \frac{(1 - x)^2}{2} \right] = M\left[ \left(x - \frac12\right)^2 + \frac14 \right] \geqslant \frac{M}{4}.
\end{aligned}
$$

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`00_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  status as "状态",
  summary as "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
