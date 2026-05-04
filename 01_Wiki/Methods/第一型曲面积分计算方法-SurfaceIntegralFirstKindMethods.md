---
title: 第一型曲面积分计算方法
tags: [数学, 第18讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 第一型曲面积分（对面积）的基本计算方法为"一投二代三计算"，将曲面积分化为二重积分。
source: 00_Raw/18_第18讲_多元函数积分学
---

## 基本思路

口诀：**一投二代三计算**——"从二重积分来，回到二重积分去"。

## 计算步骤

将曲面 $\Sigma$ 投影到 $xOy$ 面（也可选 $yOz$ 或 $zOx$ 面）：

1. **一投**：确定 $\Sigma$ 在 $xOy$ 面上的投影区域 $D_{xy}$
2. **二代**：将曲面方程 $z = z(x, y)$ 代入 $f(x, y, z)$
3. **三计算**：计算 $\mathrm{d}S = \sqrt{1 + (z_x')^2 + (z_y')^2} \, \mathrm{d}x\mathrm{d}y$

$$
\iint_{\Sigma} f(x, y, z) \, \mathrm{d}S = \iint_{D_{xy}} f[x, y, z(x, y)] \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2} \, \mathrm{d}x\mathrm{d}y.
$$

## 常用曲面的 $\mathrm{d}S$ 公式

- **柱面** $x^2 + y^2 = a^2$：$\mathrm{d}S = \dfrac{a}{\sqrt{a^2 - x^2}} \mathrm{d}x\mathrm{d}z$
- **球面** $x^2 + y^2 + z^2 = a^2$：$\mathrm{d}S = \dfrac{a}{\sqrt{a^2 - x^2 - y^2}} \mathrm{d}x\mathrm{d}y$
- **锥面** $z = \sqrt{x^2 + y^2}$：$\mathrm{d}S = \sqrt{2} \, \mathrm{d}x\mathrm{d}y$

## 投影注意事项

- 曲面投影后若有重合点，且对称性不可用，则需换投影面或拆分曲面
- 投影到 $xOy$ 面要求 $z = z(x, y)$ 是单值函数

## 应用

- 求曲面面积：$A = \iint_{\Sigma} 1 \, \mathrm{d}S = \iint_{D_{xy}} \sqrt{1 + (z_x')^2 + (z_y')^2} \, \mathrm{d}x\mathrm{d}y$
- 求重心（形心）
- 求转动惯量

## 相关页面

- [[第一型曲面积分-SurfaceIntegralFirstKind]]
- [[第二型曲面积分计算方法-SurfaceIntegralSecondKindMethods]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "曲面积分")
SORT file.name
```
