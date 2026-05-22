---
标题: 偏导数
标签: [数学, 第13讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 多元函数对单个变量的导数，将其他变量视为常数后按一元函数求导。
来源: 01_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某邻域内有定义，若极限

$$
\lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}
$$

存在，则称此极限为 $f$ 在 $(x_0, y_0)$ 处对 $x$ 的偏导数，记作

$$
\left.\frac{\partial z}{\partial x}\right|_{(x_0, y_0)},\quad \left.\frac{\partial f}{\partial x}\right|_{(x_0, y_0)},\quad z_x'(x_0, y_0),\quad f_x'(x_0, y_0).
$$

即

$$
f_x'(x_0, y_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}.
$$

类似地，对 $y$ 的偏导数

$$
f_y'(x_0, y_0) = \lim_{\Delta y \to 0} \frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y}.
$$

## 几何意义

- $f_x'(x_0, y_0)$ 表示曲线 $\begin{cases} z = f(x, y), \\ y = y_0 \end{cases}$ 在点 $(x_0, y_0, z_0)$ 处的切线对 $x$ 轴的斜率。
- $f_y'(x_0, y_0)$ 表示曲线 $\begin{cases} z = f(x, y), \\ x = x_0 \end{cases}$ 在点 $(x_0, y_0, z_0)$ 处的切线对 $y$ 轴的斜率。

## 高阶偏导数

若偏导数 $f_x'(x, y)$ 和 $f_y'(x, y)$ 仍然具有偏导数，则称其偏导数为二阶偏导数：

$$
\begin{aligned}
\frac{\partial^2 z}{\partial x^2} &= \frac{\partial}{\partial x}\left(\frac{\partial z}{\partial x}\right) = f_{xx}''(x, y), \\[4pt]
\frac{\partial^2 z}{\partial x \partial y} &= \frac{\partial}{\partial y}\left(\frac{\partial z}{\partial x}\right) = f_{xy}''(x, y), \\[4pt]
\frac{\partial^2 z}{\partial y^2} &= \frac{\partial}{\partial y}\left(\frac{\partial z}{\partial y}\right) = f_{yy}''(x, y), \\[4pt]
\frac{\partial^2 z}{\partial y \partial x} &= \frac{\partial}{\partial x}\left(\frac{\partial z}{\partial y}\right) = f_{yx}''(x, y).
\end{aligned}
$$

其中 $\frac{\partial^2 z}{\partial x \partial y}$ 与 $\frac{\partial^2 z}{\partial y \partial x}$ 称为**二阶混合偏导数**。

## 混合偏导数相等条件（Clairaut 定理）

若 $f_{xy}''(x, y)$ 和 $f_{yx}''(x, y)$ 都在区域 $D$ 内连续，则在 $D$ 内有

$$
\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial^2 z}{\partial y \partial x},
$$

即二阶混合偏导数在连续的条件下与求导次序无关。

## 计算方法

求 $f_x'(x_0, y_0)$ 有两种方式：

1. **先代值再求导**：$f_x'(x_0, y_0) = \left.\frac{\mathrm{d}}{\mathrm{d}x} f(x, y_0)\right|_{x = x_0}$
2. **先求导再代值**：$f_x'(x_0, y_0) = f_x'(x, y)\big|_{y = y_0}^{x = x_0}$

## 注意事项

- 偏导数存在 **不能推出** 函数在该点可微（见 [[全微分-TotalDifferential]]）
- 偏导数 $\frac{\partial f}{\partial x} \equiv 0$ **不能直接推出** $f(x, y)$ 仅与 $y$ 有关（需要区域连通性条件）

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
