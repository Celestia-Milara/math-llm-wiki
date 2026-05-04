---
title: 第二型曲面积分
tags: [数学, 第18讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 第二型曲面积分（对坐标的曲面积分）是向量函数通过有向曲面的通量，物理背景为流量、电通量等。
source: 00_Raw/18_第18讲_多元函数积分学
---

## 物理背景

向量场 $\boldsymbol{F}$ 通过有向曲面 $\Sigma$ 的通量：
$$
\iint_{\Sigma} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{S} = \iint_{\Sigma} \boldsymbol{F} \cdot \boldsymbol{n}^\circ \, \mathrm{d}S,
$$
其中 $\boldsymbol{n}^\circ = (\cos\alpha, \cos\beta, \cos\gamma)$ 是 $\Sigma$ 在指定侧的单位法向量。

由于 $\mathrm{d}\boldsymbol{S} = (\mathrm{d}y\mathrm{d}z,\; \mathrm{d}z\mathrm{d}x,\; \mathrm{d}x\mathrm{d}y)$，得：
$$
\iint_{\Sigma} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{S} = \iint_{\Sigma} P \, \mathrm{d}y\mathrm{d}z + Q \, \mathrm{d}z\mathrm{d}x + R \, \mathrm{d}x\mathrm{d}y.
$$

## 定义

第二型曲面积分是向量函数 $\boldsymbol{F}(x, y, z) = P\boldsymbol{i} + Q\boldsymbol{j} + R\boldsymbol{k}$ 通过有向曲面 $\Sigma$ 的通量：
$$
\iint_{\Sigma} P(x, y, z) \, \mathrm{d}y\mathrm{d}z + Q(x, y, z) \, \mathrm{d}z\mathrm{d}x + R(x, y, z) \, \mathrm{d}x\mathrm{d}y.
$$

## 性质

1. **线性性质**：$\iint_{\Sigma} (k_1 \boldsymbol{F}_1 \pm k_2 \boldsymbol{F}_2) \cdot \mathrm{d}\boldsymbol{S} = k_1 \iint_{\Sigma} \boldsymbol{F}_1 \cdot \mathrm{d}\boldsymbol{S} \pm k_2 \iint_{\Sigma} \boldsymbol{F}_2 \cdot \mathrm{d}\boldsymbol{S}$.
2. **方向性**：$\iint_{\Sigma^-} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{S} = -\iint_{\Sigma^+} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{S}$.
3. **可加性**：曲面可分段积分。

> [!WARNING] AI Generated
> 与第二型曲线积分类似，第二型曲面积分也没有几何意义上的对称性，其"对称性"体现在数值计算中的抵消或叠加，需根据法向量方向具体判断。

## 相关页面

- [[第二型曲面积分计算方法-SurfaceIntegralSecondKindMethods]]
- [[第一型曲面积分-SurfaceIntegralFirstKind]]
- [[高斯公式-GaussTheorem]]
- [[斯托克斯公式-StokesTheorem]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "曲面积分")
SORT file.name
```
