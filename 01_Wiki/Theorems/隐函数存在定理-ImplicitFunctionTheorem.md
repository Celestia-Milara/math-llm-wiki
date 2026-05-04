---
title: 隐函数存在定理
tags: [数学, 第13讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 给出由方程确定隐函数的充分条件，并提供隐函数求导公式。
source: 00_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定理 1（二元方程情形）

对于由方程 $F(x, y) = 0$ 确定的隐函数 $y = f(x)$，若 $F_y'(x, y) \neq 0$，则有

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{F_x'(x, y)}{F_y'(x, y)}.
$$

**证明思路**：将 $y = f(x)$ 代入 $F(x, y) = 0$ 得 $F[x, f(x)] = 0$，两边对 $x$ 求导：

$$
F_x'(x, y) + F_y'(x, y) \cdot \frac{\mathrm{d}y}{\mathrm{d}x} = 0,
$$

因 $F_y' \neq 0$，故 $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{F_x'}{F_y'}$。

## 定理 2（三元方程情形）

对于由方程 $F(x, y, z) = 0$ 确定的隐函数 $z = f(x, y)$，若 $F_z'(x, y, z) \neq 0$，则有

$$
\frac{\partial z}{\partial x} = -\frac{F_x'(x, y, z)}{F_z'(x, y, z)},\qquad
\frac{\partial z}{\partial y} = -\frac{F_y'(x, y, z)}{F_z'(x, y, z)}.
$$

## 使用要点

- 使用公式法时，$x, y, z$ 被视为**独立变量**（对 $x$ 求偏导时 $y, z$ 当常数）
- 定理的条件是**充分但非必要条件**——反例：$F(x, y) = (y - x)^2$，在 $(0,0)$ 处 $F_y' = 0$，但仍有隐函数 $y = x$
- 判断多变量的隐函数存在时，需检查所有可能的偏导数组合

## 三种方法对比

对于隐函数求偏导，有三种等价方法：

1. **公式法**（隐函数存在定理）：$\displaystyle \frac{\partial z}{\partial x} = -\frac{F_x'}{F_z'}$
2. **复合函数求导法**：方程两边直接对自变量求偏导
3. **全微分形式不变性**：方程两边求全微分，整理出 $\mathrm{d}z$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
