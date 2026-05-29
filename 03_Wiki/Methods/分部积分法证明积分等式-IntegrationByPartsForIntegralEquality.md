---
标题: 分部积分法证明积分等式
标签: [数学, 第11讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过分部积分法将复杂积分等式转化为已知形式，常用于证明含函数及其导数的积分等式。
来源: 01_Raw/Archive/Lectures/11_第11讲_一元函数积分学的应用(二).md
---

## 方法概述

当被积函数中出现函数与导数、或两项相乘的形式时，通常考虑分部积分法。

### 基本步骤

1. 识别被积函数中的 $u$（易求导部分）和 $\mathrm{d}v$（易积分部分）
2. 套用公式 $\int u \, \mathrm{d}v = uv - \int v \, \mathrm{d}u$
3. 利用边界条件简化

## 典型例题

**条件**：$f(x)$ 的二阶导数 $f''(x)$ 在 $[0, 1]$ 上连续，$f(0) = f(1) = 0$。

**结论**：

$$
\int_0^1 f(x) \, \mathrm{d}x = \frac12 \int_0^1 x(x - 1) f''(x) \, \mathrm{d}x.
$$

**证明要点**：

$$
\begin{aligned}
\frac12 \int_0^1 x(x-1) f''(x) \, \mathrm{d}x
&= \frac12 \int_0^1 x(x-1) \, \mathrm{d}[f'(x)] \\
&= \frac12 x(x-1) f'(x) \Big|_0^1 - \frac12 \int_0^1 f'(x)(2x - 1) \, \mathrm{d}x \\
&= -\frac12 \int_0^1 (2x - 1) \, \mathrm{d}[f(x)] \\
&= -\frac12 (2x - 1) f(x) \Big|_0^1 + \int_0^1 f(x) \, \mathrm{d}x = \int_0^1 f(x) \, \mathrm{d}x.
\end{aligned}
$$

## 适用场景

- 被积函数出现函数与 $x$ 的多项式乘积
- 被积函数含导数形式
- 需要利用边界条件消去边界项

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  掌握状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
