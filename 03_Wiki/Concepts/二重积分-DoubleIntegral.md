---
标题: 二重积分
标签: [数学, 第14讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 二元函数在有界闭区域上的积分，推广了定积分的概念，表示曲顶柱体的体积。
来源: 01_Raw/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

设 $f(x, y)$ 是有界闭区域 $D$ 上的有界函数。将 $D$ 任意分成 $n$ 个小闭区域 $\Delta\sigma_1, \Delta\sigma_2, \dots, \Delta\sigma_n$（$\Delta\sigma_i$ 也表示其面积）。在每个 $\Delta\sigma_i$ 上任取一点 $(\xi_i, \eta_i)$，作乘积 $f(\xi_i, \eta_i)\Delta\sigma_i$ 并求和。令 $\lambda = \max\{\Delta\sigma_i\}$，若极限

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i)\Delta\sigma_i
$$

总存在（与区域分割方式和点的取法无关），则称此极限为 $f(x, y)$ 在 $D$ 上的**二重积分**。

若 $f(x, y)$ 在有界闭区域 $D$ 上连续，则二重积分一定存在。

## 几何意义

- 当 $f(x, y) \geq 0$ 时，$\iint_D f(x, y)\,\mathrm{d}\sigma$ 表示以 $D$ 为底、$z = f(x, y)$ 为曲顶的曲顶柱体体积
- 当 $f(x, y) \leq 0$ 时，积分值为负，绝对值等于柱体体积
- 当 $f(x, y)$ 在 $D$ 上变号时，积分值等于 $xOy$ 面上方柱体体积减去下方柱体体积

## 基本性质

| 性质 | 公式 |
|------|------|
| 区域面积 | $\displaystyle \iint_D 1\cdot\mathrm{d}\sigma = \iint_D \mathrm{d}\sigma = A$ |
| 线性性质 | $\displaystyle \iint_D [k_1 f \pm k_2 g]\,\mathrm{d}\sigma = k_1\iint_D f\,\mathrm{d}\sigma \pm k_2\iint_D g\,\mathrm{d}\sigma$ |
| 可加性 | $\displaystyle \iint_D f\,\mathrm{d}\sigma = \iint_{D_1} f\,\mathrm{d}\sigma + \iint_{D_2} f\,\mathrm{d}\sigma\;(D = D_1 \cup D_2,\; D_1 \cap D_2 = \varnothing)$ |
| 保号性 | 若 $f(x, y) \leq g(x, y)$，则 $\displaystyle \iint_D f\,\mathrm{d}\sigma \leq \iint_D g\,\mathrm{d}\sigma$ |
| 估值定理 | $\displaystyle mA \leq \iint_D f(x, y)\,\mathrm{d}\sigma \leq MA$（$m, M$ 为 $f$ 在 $D$ 上的最小、最大值） |

## 二重积分中值定理

设 $f(x, y)$ 在有界闭区域 $D$ 上连续，$A$ 为 $D$ 的面积，则在 $D$ 上至少存在一点 $(\xi, \eta)$，使得

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = f(\xi, \eta) \cdot A.
$$

该定理常被用于处理抽象函数二重积分或难以直接计算的二重积分（如通过求导或极限问题）。

## 与定积分、三重积分的关系

| 积分类型 | 维数 | 几何/物理意义 |
|----------|------|--------------|
| $\displaystyle \int_a^b f(x)\,\mathrm{d}x$ | 一维 | 细长杆质量、曲线下面积 |
| $\displaystyle \iint_D f(x, y)\,\mathrm{d}\sigma$ | 二维 | 平面薄板质量、曲顶柱体体积 |
| $\displaystyle \iiint_\Omega f(x, y, z)\,\mathrm{d}V$ | 三维 | 空间物体质量 |

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
