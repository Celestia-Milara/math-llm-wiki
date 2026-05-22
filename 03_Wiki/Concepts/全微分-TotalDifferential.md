---
标题: 全微分
标签: [数学, 第13讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 多元函数全增量的线性主部，反映函数在各个方向上的变化率综合效果。
来源: 01_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

设函数 $z = f(x, y)$ 在点 $(x, y)$ 的某邻域内有定义，若全增量

$$
\Delta z = f(x + \Delta x, y + \Delta y) - f(x, y)
$$

可表示为

$$
\Delta z = A \Delta x + B \Delta y + o(\rho), \quad \rho = \sqrt{(\Delta x)^2 + (\Delta y)^2},
$$

其中 $A, B$ 仅与点 $(x, y)$ 有关，而与 $\Delta x, \Delta y$ 无关，则称 $z = f(x, y)$ 在点 $(x, y)$ 处**可微**，并称 $A\Delta x + B\Delta y$ 为**全微分**，记作

$$
\mathrm{d}z = A\Delta x + B\Delta y = A\,\mathrm{d}x + B\,\mathrm{d}y.
$$

## 可微的必要条件

若 $z = f(x, y)$ 在点 $(x, y)$ 处可微，则偏导数存在且

$$
A = \frac{\partial z}{\partial x},\quad B = \frac{\partial z}{\partial y},
$$

即

$$
\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y.
$$

## 可微的充分条件

若 $z = f(x, y)$ 在点 $(x, y)$ 处的偏导数存在且连续，则该函数在该点处可微。

## 一元函数 vs 二元函数对比

| 性质 | 一元函数 $y = f(x)$ | 二元函数 $z = f(x, y)$ |
|------|---------------------|----------------------|
| 可微与可导 | 可微 $\Leftrightarrow$ 可导 | 可微 $\Rightarrow$ 偏导存在（逆不真） |
| 增量表达式 | $\Delta y = A\Delta x + o(\Delta x)$ | $\Delta z = A\Delta x + B\Delta y + o(\rho)$ |
| 微分 | $\mathrm{d}y = f'(x)\mathrm{d}x$ | $\mathrm{d}z = f_x'\mathrm{d}x + f_y'\mathrm{d}y$ |

## 可微的判别步骤

判别 $z = f(x, y)$ 在 $(x_0, y_0)$ 处是否可微：

1. 写出全增量 $\Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$
2. 写出线性增量 $A\Delta x + B\Delta y$，其中 $A = f_x'(x_0, y_0),\; B = f_y'(x_0, y_0)$
3. 作极限

$$
\lim_{\substack{\Delta x \to 0 \\ \Delta y \to 0}} \frac{\Delta z - (A\Delta x + B\Delta y)}{\sqrt{(\Delta x)^2 + (\Delta y)^2}}.
$$

若该极限等于 $0$，则可微；否则不可微。

## 全微分形式不变性

设 $z = f(u, v)$，其中 $u = u(x, y),\; v = v(x, y)$，若 $f, u, v$ 分别有连续偏导数，则无论 $u, v$ 是自变量还是中间变量，总有

$$
\mathrm{d}z = \frac{\partial z}{\partial u}\mathrm{d}u + \frac{\partial z}{\partial v}\mathrm{d}v.
$$

这一性质称为**全微分形式不变性**，常用于隐函数求导。

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
