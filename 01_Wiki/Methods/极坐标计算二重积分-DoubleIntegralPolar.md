---
title: 极坐标计算二重积分
tags: [数学, 第14讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 在极坐标系下计算二重积分，适用于被积函数含平方和或积分区域为圆（部分）的情形。
source: 00_Raw/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 坐标转换

直角坐标与极坐标的关系：

$$
\begin{cases}
x = r\cos\theta,\\
y = r\sin\theta,
\end{cases}
\qquad
\mathrm{d}\sigma = r\,\mathrm{d}r\,\mathrm{d}\theta.
$$

## 三种基本情形

### 情形 1：极点在区域外部

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \int_\alpha^\beta \mathrm{d}\theta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\, r\,\mathrm{d}r.
$$

### 情形 2：极点在区域边界上

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \int_\alpha^\beta \mathrm{d}\theta \int_0^{r(\theta)} f(r\cos\theta, r\sin\theta)\, r\,\mathrm{d}r.
$$

### 情形 3：极点在区域内部

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \int_0^{2\pi} \mathrm{d}\theta \int_0^{r(\theta)} f(r\cos\theta, r\sin\theta)\, r\,\mathrm{d}r.
$$

## 定限方法

1. 从 $Ox$ 轴逆时针出发，先碰到积分区域时 $\theta = \alpha$，后离开时 $\theta = \beta$
2. 在 $\theta$ 范围内画射线，先交的内曲线为 $r = r_1(\theta)$，后交的外曲线为 $r = r_2(\theta)$

> **一般先积 $r$，后积 $\theta$**（因为区域通常是关于中心对称的）。

## 选择极坐标的原则

**优先选用极坐标系**，如果满足以下至少一条：

1. **被积函数**为 $f(x^2 + y^2)$、$f(y/x)$、$f(x/y)$ 等形式
2. **积分区域**为圆或圆的一部分（圆环、扇形、半圆等）

否则优先考虑直角坐标系。

## 常见积分

高斯积分（需记忆）：

$$
\int_{-\infty}^{+\infty} \mathrm{e}^{-x^2}\,\mathrm{d}x = \sqrt{\pi},\qquad
\int_0^{+\infty} \mathrm{e}^{-x^2}\,\mathrm{d}x = \frac{\sqrt{\pi}}{2}.
$$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
