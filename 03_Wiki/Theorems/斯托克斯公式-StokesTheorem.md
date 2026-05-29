---
标题: 斯托克斯公式
标签: [数学, 第18讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 斯托克斯公式建立了空间曲面积分与其边界曲线上的曲线积分之间的联系，是格林公式在三维空间曲面的推广。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
---

## 定理陈述

设 $\Sigma$ 为分片光滑有向曲面片，$\Gamma$ 为逐段光滑的 $\Sigma$ 的边界，方向与 $\Sigma$ 的法向量成右手系，$P, Q, R$ 具有连续一阶偏导数，则

**第二型曲面积分形式**：
$$
\oint_{\Gamma} P \, \mathrm{d}x + Q \, \mathrm{d}y + R \, \mathrm{d}z = \iint_{\Sigma}
\begin{vmatrix}
\mathrm{d}y\mathrm{d}z & \mathrm{d}z\mathrm{d}x & \mathrm{d}x\mathrm{d}y \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix}.
$$

**第一型曲面积分形式**（用单位法向量 $(\cos\alpha, \cos\beta, \cos\gamma)$ 表示）：
$$
\oint_{\Gamma} P \, \mathrm{d}x + Q \, \mathrm{d}y + R \, \mathrm{d}z = \iint_{\Sigma}
\begin{vmatrix}
\cos\alpha & \cos\beta & \cos\gamma \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix} \mathrm{d}S.
$$

## 使用要点

- 公式与绷在 $\Gamma$ 上的曲面大小、形状无关——选最简单的曲面（如平面）进行计算
- 右手系：拇指指向法向量，四指弯曲方向为曲线正向

> [!TIP] 记忆技巧
> 将 $\Gamma$ 想象成肥皂泡的塑料圈，$\Sigma$ 是上面绷的肥皂膜。无论膜的形状如何，公式都成立，因此选最简单的平面膜即可。

## 相关页面

- [[第二型曲线积分计算方法-LineIntegralSecondKindMethods]]
- [[格林公式-GreensTheorem]]
- [[高斯公式-GaussTheorem]]
- [[散度与旋度-DivergenceAndCurl]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "斯托克斯公式")
SORT file.name
```
