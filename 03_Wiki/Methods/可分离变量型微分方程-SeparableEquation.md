---
标题: 可分离变量型微分方程
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 形如 $y' = f(x)g(y)$ 的方程，通过分离变量后两边积分求解。
来源: 01_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 直接可分离型

形如 $y' = f(x)g(y)$ 的方程，解法为：

$$\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)g(y) \quad\Rightarrow\quad \int \frac{\mathrm{d}y}{g(y)} = \int f(x)\,\mathrm{d}x$$

## 换元后可分离型

形如 $\dfrac{\mathrm{d}y}{\mathrm{d}x} = f(ax + by + c)$ 的方程（$a, b$ 全不为零）。

解法：令 $u = ax + by + c$，则 $\dfrac{\mathrm{d}u}{\mathrm{d}x} = a + bf(u)$，化为可分离变量型。

## 注意事项

- 不定积分后常加 $\ln C$ 而非 $C$，便于合并。
- 分离变量时可能丢失使分母为零的解（奇解）。
- 通解中的常数往往是在一定范围内取值的常数，未必是全体实数。

## 相关页面

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[一阶线性微分方程-FirstOrderLinearODE|一阶线性微分方程]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, "微分方程") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
