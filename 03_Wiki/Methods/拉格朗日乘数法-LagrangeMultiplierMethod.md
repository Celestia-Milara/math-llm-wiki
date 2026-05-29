---
标题: 拉格朗日乘数法
标签: [数学, 第13讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 求解多元函数在约束条件下的极值问题，通过构造辅助函数转化为无条件极值。
来源: 01_Raw/Archive/Lectures/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 方法概述

求目标函数 $u = f(x, y, z)$ 在约束条件 $\varphi(x, y, z) = 0$（或多个约束）下的条件极值。

## 基本步骤（单约束）

1. **构造拉格朗日函数**：
   $$F(x, y, z, \lambda) = f(x, y, z) + \lambda\varphi(x, y, z).$$

2. **令所有一阶偏导为零**：
   $$
   \begin{cases}
   F_x' = f_x' + \lambda\varphi_x' = 0,\\
   F_y' = f_y' + \lambda\varphi_y' = 0,\\
   F_z' = f_z' + \lambda\varphi_z' = 0,\\
   F_\lambda' = \varphi(x, y, z) = 0.
   \end{cases}
   $$

3. **解方程组**得备选点 $P_i$。

4. **比较函数值**得最值。根据实际问题背景判断（唯一可能极值点即为所求）。

## 基本步骤（多约束）

对约束条件 $\varphi(x, y, z) = 0,\; \psi(x, y, z) = 0$：

1. **构造辅助函数**：
   $$F(x, y, z, \lambda, \mu) = f + \lambda\varphi + \mu\psi.$$

2. 自变量个数 $=$ 目标函数自变量个数 $+$ 约束个数。

3. 令所有偏导为零并解方程组。

## 注意事项

- 若约束条件可解出 $z = z(x, y)$，则直接代入目标函数转化为无条件极值（**代入法**）
- 对于不封闭的约束曲线（如圆弧），需注意比较端点值
- 拉格朗日乘数法是求解条件极值的通用方法，适用于线性或非线性约束

## 最远（近）点垂线原理

若 $\Gamma$ 是光滑闭曲线，$Q$ 是 $\Gamma$ 外一点，$P_1, P_2$ 分别为 $\Gamma$ 上与 $Q$ 的最远、最近点，则直线 $P_1Q, P_2Q$ 分别在 $P_1, P_2$ 处与 $\Gamma$ 垂直。该原理可直接使用，可节约计算时间。

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
