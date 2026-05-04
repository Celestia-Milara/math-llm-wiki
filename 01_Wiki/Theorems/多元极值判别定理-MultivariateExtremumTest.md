---
title: 极值判别定理
tags: [数学, 第13讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 多元函数取极值的必要条件和充分条件（判别式法），以及拉格朗日乘数法。
source: 00_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 无条件极值的必要条件

设 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处一阶偏导数存在且取极值，则

$$
f_x'(x_0, y_0) = 0,\quad f_y'(x_0, y_0) = 0.
$$

称满足上式的点为**驻点**（或**可疑点**）。

> **注意**：
> - 偏导数不存在的点也可能是极值点（如 $z = \sqrt{x^2 + y^2}$ 在 $(0,0)$ 处取极小值但偏导不存在）
> - 必要条件也适用于三元及以上函数

## 无条件极值的充分条件（判别式法）

设 $f(x, y)$ 在 $(x_0, y_0)$ 的某邻域内连续且有一阶及二阶连续偏导数，又 $f_x'(x_0, y_0) = 0,\; f_y'(x_0, y_0) = 0$。记

$$
A = f_{xx}''(x_0, y_0),\quad B = f_{xy}''(x_0, y_0),\quad C = f_{yy}''(x_0, y_0),
$$

则判别式 $\Delta = AC - B^2$ 决定极值情况：

| 条件 | 结论 |
|------|------|
| $\Delta > 0$ 且 $A > 0$ | 极小值 |
| $\Delta > 0$ 且 $A < 0$ | 极大值 |
| $\Delta < 0$ | 非极值（鞍点） |
| $\Delta = 0$ | 方法失效，需另谋他法 |

## 条件极值与拉格朗日乘数法

求目标函数 $u = f(x, y, z)$ 在约束条件 $\varphi(x, y, z) = 0,\; \psi(x, y, z) = 0$ 下的最值：

1. **构造辅助函数**：
   $$F(x, y, z, \lambda, \mu) = f(x, y, z) + \lambda\varphi(x, y, z) + \mu\psi(x, y, z).$$

2. **令所有偏导数为零**：
   $$
   \begin{cases}
   F_x' = f_x' + \lambda\varphi_x' + \mu\psi_x' = 0, &\quad\text{（自变量个数 = 目标函数自变量数 + 约束个数）}\\
   F_y' = f_y' + \lambda\varphi_y' + \mu\psi_y' = 0,\\
   F_z' = f_z' + \lambda\varphi_z' + \mu\psi_z' = 0,\\
   F_\lambda' = \varphi(x, y, z) = 0,\\
   F_\mu' = \psi(x, y, z) = 0.
   \end{cases}
   $$

3. **解方程组**得备选点 $P_i$，比较 $f(P_i)$ 得最值。

## 有界闭区域上连续函数的最值问题

**理论依据**：有界闭区域 $D$ 上的多元连续函数一定存在最大值和最小值。

**求解步骤**：
1. 根据 $f_x' = 0,\; f_y' = 0$ 或偏导不存在，求出区域 $D$ **内部**的所有可疑点
2. 用拉格朗日乘数法或代入法求出区域 $D$ **边界**上的所有可疑点
3. 比较以上所有可疑点的函数值，最小值为最小值，最大值为最大值

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
