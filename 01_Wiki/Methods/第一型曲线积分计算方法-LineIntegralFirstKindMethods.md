---
标题: 第一型曲线积分计算方法
标签: [数学, 第18讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 第一型曲线积分（对弧长）的基本计算方法为"一投二代三计算"，将曲线积分化为定积分。
来源: 00_Raw/18_第18讲_多元函数积分学
---

## 基本思路

口诀：**一投二代三计算**——从定积分来，回到定积分去。

## 平面曲线情形

### ① 直角坐标系
$L: y = y(x),\; a \leq x \leq b$：
$$
\int_L f(x, y) \, \mathrm{d}s = \int_a^b f[x, y(x)] \sqrt{1 + [y'(x)]^2} \, \mathrm{d}x.
$$

### ② 参数式
$L: \begin{cases} x = x(t), \\ y = y(t) \end{cases},\; \alpha \leq t \leq \beta$：
$$
\int_L f(x, y) \, \mathrm{d}s = \int_\alpha^\beta f[x(t), y(t)] \sqrt{[x'(t)]^2 + [y'(t)]^2} \, \mathrm{d}t.
$$

### ③ 极坐标系
$L: r = r(\theta),\; \alpha \leq \theta \leq \beta$：
$$
\int_L f(x, y) \, \mathrm{d}s = \int_\alpha^\beta f[r(\theta)\cos\theta, r(\theta)\sin\theta] \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} \, \mathrm{d}\theta.
$$

## 空间曲线情形

$\Gamma: \begin{cases} x = x(t), \\ y = y(t), \\ z = z(t) \end{cases},\; \alpha \leq t \leq \beta$：
$$
\int_{\Gamma} f(x, y, z) \, \mathrm{d}s = \int_\alpha^\beta f[x(t), y(t), z(t)] \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2} \, \mathrm{d}t.
$$

## 应用

- 求曲线弧长：$l = \int_{\Gamma} 1 \, \mathrm{d}s$
- 求重心（形心）：$\overline{x} = \dfrac{\int_L x \, \mathrm{d}s}{\int_L 1 \, \mathrm{d}s}$，等等
- 求转动惯量：$I_z = \int_L (x^2 + y^2) \rho \, \mathrm{d}s$

> [!TIP] 易错提示
> 第一型曲线积分可将曲线方程代入被积函数，因为积分只发生在曲线上。利用此性质可大幅简化计算。

## 相关页面

- [[第一型曲线积分-LineIntegralFirstKind]]
- [[第一型曲面积分计算方法-SurfaceIntegralFirstKindMethods]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "曲线积分")
SORT file.name
```
