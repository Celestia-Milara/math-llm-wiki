---
title: 分部积分法
tags: [数学, 第9讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 将难以直接计算的积分转化为另一个更容易计算的积分，核心是u和v的选取。
source: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 基本公式

$$\int u\,\mathrm{d}v = uv - \int v\,\mathrm{d}u$$

## u,v 选取原则

"反对幂（三）指"——**相对位置在左边的宜选作 $u$（求导），右边的宜选作 $v$（积分）**：

| 类型 | $u$ 选 | $v$ 选 |
|:----|:------|:------|
| $P_n(x)\mathrm{e}^{kx},\;P_n(x)\sin ax,\;P_n(x)\cos ax$ | $P_n(x)$ | $\mathrm{e}^{kx},\sin ax,\cos ax$ |
| $\mathrm{e}^{ax}\sin bx,\;\mathrm{e}^{ax}\cos bx$ | 任一因子 | 另一因子 |
| $P_n(x)\ln x,\;P_n(x)\arcsin x,\;P_n(x)\arctan x$ | $\ln x,\arcsin x,\arctan x$ | $P_n(x)$ |

## 分部积分法的推广公式（表格法）

$$\int u v^{(n+1)}\,\mathrm{d}x = u v^{(n)} - u' v^{(n-1)} + u'' v^{(n-2)} - \cdots + (-1)^n u^{(n)} v + (-1)^{n+1}\! \int u^{(n+1)} v\,\mathrm{d}x$$

**表格法计算**：以 $u$ 为起点错位相乘，符号 "+" "-" 相间。

例如 $\int (x^3+2x+6)\mathrm{e}^{2x}\,\mathrm{d}x$：

| $u$ 的各阶导数 | $x^3+2x+6$ | $3x^2+2$ | $6x$ | $6$ | $0$ |
|:-------------|:----------:|:--------:|:---:|:--:|:-:|
| $v^{(4)}$ 的各阶原函数 | $\mathrm{e}^{2x}$ | $\frac12\mathrm{e}^{2x}$ | $\frac14\mathrm{e}^{2x}$ | $\frac18\mathrm{e}^{2x}$ | $\frac1{16}\mathrm{e}^{2x}$ |

## 循环积分

当被积函数为 $\mathrm{e}^{ax}\sin bx$ 或 $\mathrm{e}^{ax}\cos bx$ 时，分部积分可能建立方程，解出积分值。

$$\int \mathrm{e}^{ax}\sin bx\,\mathrm{d}x = \frac{a\mathrm{e}^{ax}\sin bx - b\mathrm{e}^{ax}\cos bx}{a^2+b^2}+C $$

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Methods"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
