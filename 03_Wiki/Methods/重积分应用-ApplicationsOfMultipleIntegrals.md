---
标题: 重积分与曲线曲面积分的应用
标签: [数学, 第18讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 三重积分、曲线积分、曲面积分在求几何量（体积、面积、弧长）与物理量（质量、重心、转动惯量、引力）中的应用。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
---

## 三重积分的应用

### 体积
空间区域 $\Omega$ 的体积：$V = \iiint_{\Omega} \mathrm{d}v$.

### 重心（质心）
体密度 $\rho(x, y, z)$ 时，重心坐标：
$$
\overline{x} = \frac{\iiint_{\Omega} x\rho \, \mathrm{d}v}{\iiint_{\Omega} \rho \, \mathrm{d}v},\quad
\overline{y} = \frac{\iiint_{\Omega} y\rho \, \mathrm{d}v}{\iiint_{\Omega} \rho \, \mathrm{d}v},\quad
\overline{z} = \frac{\iiint_{\Omega} z\rho \, \mathrm{d}v}{\iiint_{\Omega} \rho \, \mathrm{d}v}.
$$

$\rho$ 为常数时重心即为形心。**形心公式逆用**：$\iiint_{\Omega} x \, \mathrm{d}v = \overline{x} \cdot V$.

### 转动惯量
$$
I_x = \iiint_{\Omega} (y^2 + z^2)\rho \, \mathrm{d}v,\quad
I_y = \iiint_{\Omega} (z^2 + x^2)\rho \, \mathrm{d}v,\quad
I_z = \iiint_{\Omega} (x^2 + y^2)\rho \, \mathrm{d}v.
$$

### 引力
物体对质点 $M_0(x_0, y_0, z_0)$ 的引力分量公式（略）。

## 第一型曲线积分的应用

- **弧长**：$l = \int_L 1 \, \mathrm{d}s$
- **重心/形心**：$\overline{x} = \dfrac{\int_L x\rho \, \mathrm{d}s}{\int_L \rho \, \mathrm{d}s}$ 等
- **转动惯量**：$I_z = \int_L (x^2 + y^2)\rho \, \mathrm{d}s$

## 第一型曲面积分的应用

- **曲面面积**：$A = \iint_{\Sigma} 1 \, \mathrm{d}S = \iint_{D_{xy}} \sqrt{1 + (z_x')^2 + (z_y')^2} \, \mathrm{d}x\mathrm{d}y$
- **重心/形心**：$\overline{z} = \dfrac{\iint_{\Sigma} z\rho \, \mathrm{d}S}{\iint_{\Sigma} \rho \, \mathrm{d}S}$ 等
- **转动惯量**：$I_z = \iint_{\Sigma} (x^2 + y^2)\rho \, \mathrm{d}S$

> [!TIP] 形心公式逆用技巧
> 若已知形心坐标和体积（面积、弧长），可直接计算 $\iiint x \, \mathrm{d}v = \overline{x} \cdot V$，避免直接积分。

## 相关页面

- [[三重积分-TripleIntegral]]
- [[第一型曲线积分-LineIntegralFirstKind]]
- [[第一型曲面积分-SurfaceIntegralFirstKind]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "应用")
SORT file.name
```
