---
标题: 微元法
标签: [数学, 第10讲, 第11讲, 第12讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 用定积分解决几何、物理等应用问题的核心方法——取微元再积分。
来源: 01_Raw/Archive/Lectures/10_第10讲_一元函数积分学的应用(一).md
---

## 方法概述

微元法是用定积分解决实际应用问题的核心思想。其基本步骤为：

1. **分割**：将整体量分割成无数个微小部分
2. **近似**：在每个微小部分上用线性近似代替精确值
3. **求和**：将所有微小部分累加
4. **取极限**：将求和转化为定积分

## 通用公式

$$
\text{总量} = \int_a^b (\text{微元表达式}) \, \mathrm{d}(\text{积分变量}).
$$

## 常见应用对照表

| 应用场景 | 微元形式 | 积分公式 |
|----------|----------|----------|
| 平面面积（直角坐标） | $\mathrm{d}S = |y_1 - y_2| \, \mathrm{d}x$ | $S = \int_a^b |y_1 - y_2| \, \mathrm{d}x$ |
| 平面面积（极坐标） | $\mathrm{d}S = \frac12 |r_1^2 - r_2^2| \, \mathrm{d}\theta$ | $S = \frac12 \int_\alpha^\beta |r_1^2 - r_2^2| \, \mathrm{d}\theta$ |
| 旋转体体积（$x$ 轴） | $\mathrm{d}V = \pi y^2 \, \mathrm{d}x$ | $V_x = \pi \int_a^b y^2 \, \mathrm{d}x$ |
| 旋转体体积（$y$ 轴） | $\mathrm{d}V_y = 2\pi x|y| \, \mathrm{d}x$ | $V_y = 2\pi \int_a^b x|y| \, \mathrm{d}x$ |
| 弧长 | $\mathrm{d}s = \sqrt{1 + (y')^2} \, \mathrm{d}x$ | $s = \int_a^b \sqrt{1 + (y')^2} \, \mathrm{d}x$ |
| 旋转侧面积 | $\mathrm{d}S = 2\pi |y| \, \mathrm{d}s$ | $S = 2\pi \int |y| \, \mathrm{d}s$ |
| 变力做功 | $\mathrm{d}W = F(x) \, \mathrm{d}x$ | $W = \int_a^b F(x) \, \mathrm{d}x$ |
| 抽水做功 | $\mathrm{d}W = \rho g x A(x) \, \mathrm{d}x$ | $W = \rho g \int_a^b x A(x) \, \mathrm{d}x$ |
| 静水压力 | $\mathrm{d}P = \rho g x [f(x) - h(x)] \, \mathrm{d}x$ | $P = \rho g \int_a^b x [f(x) - h(x)] \, \mathrm{d}x$ |

## 解题步骤

1. **建立坐标系**：选择合适的坐标系
2. **取微元**：在自变量 $x$ 处取增量 $\mathrm{d}x$，得到微小部分
3. **表达微元**：写出目标量的微元 $\mathrm{d}U = f(x) \, \mathrm{d}x$
4. **积分求和**：$U = \int_a^b f(x) \, \mathrm{d}x$

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
WHERE any(filter(this.标签, (t) => startswith(t, "第")), (chapter) => contains(标签, chapter))
SORT file.name ASC
```
