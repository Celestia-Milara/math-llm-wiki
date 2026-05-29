---
标题: 质心与形心公式
标签: [数学, 第10讲, 第12讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 平面区域的形心（质心）坐标计算公式，及三心（重心、质心、形心）的关系。
来源: 01_Raw/Archive/Lectures/10_第10讲_一元函数积分学的应用(一).md
---
## 定理陈述


## 三心的概念

- **质心**：物体的质量分布中心，是物体的固有特性
- **重心**：物体所受地球引力的重力分布中心。在均匀重力场下，重心与质心重合
- **形心**：几何图形的分布中心，是固有几何量。当物体密度为常数时，质心与形心重合

在均匀重力场及均质条件下，三心重合。

## 离散系统的质心

设平面上有 $n$ 个质点 $(x_i, y_i)$，质量分别为 $m_i$，则质心坐标为

$$
\bar{x} = \frac{\sum_{i=1}^n x_i m_i}{\sum_{i=1}^n m_i}, \quad
\bar{y} = \frac{\sum_{i=1}^n y_i m_i}{\sum_{i=1}^n m_i}.
$$

其中 $M_y = \sum x_i m_i$ 称为系统绕 $y$ 轴的力矩。

## 平面区域的形心

设平面区域 $D = \{(x, y) \mid 0 \leqslant y \leqslant f(x), a \leqslant x \leqslant b\}$，$y = f(x)$ 在 $[a, b]$ 上连续，则形心坐标为

$$
\bar{x} = \frac{\int_a^b x f(x) \, \mathrm{d}x}{\int_a^b f(x) \, \mathrm{d}x}, \quad
\bar{y} = \frac{\frac{1}{2} \int_a^b f^2(x) \, \mathrm{d}x}{\int_a^b f(x) \, \mathrm{d}x}.
$$

## 连续曲线段的形心

对于质量系统为连续可求长曲线段 $L: y = f(x)$，当线密度 $\rho$ 为常数时，形心到直线 $L_0: ax + by + c = 0$ 的距离为

$$
r(\bar{x}, \bar{y}) = \frac{\int_a^b \frac{|ax + by + c|}{\sqrt{a^2 + b^2}} \sqrt{1 + [f'(x)]^2} \, \mathrm{d}x}{\int_a^b \sqrt{1 + [f'(x)]^2} \, \mathrm{d}x}.
$$

> [!TIP] 几何直觉
> 形心公式的分子是"力矩"的积分，分母是总面积（或总弧长），本质上是对坐标的加权平均。

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/10_第10讲_一元函数积分学的应用(一).md`, `01_Raw/12_第12讲_一元函数积分学的应用(三).md`

```dataview
TABLE
  title as "名称",
  掌握状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, "形心") OR contains(标签, "质心")
SORT file.name ASC
```
