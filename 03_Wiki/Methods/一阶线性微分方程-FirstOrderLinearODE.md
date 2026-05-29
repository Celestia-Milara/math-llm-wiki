---
标题: 一阶线性微分方程
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 形如 $y' + p(x)y = q(x)$ 的方程，可通过积分因子法化为全微分形式求解。
来源: 01_Raw/Archive/Lectures/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 标准形式

$$y' + p(x)y = q(x)$$

其中 $p(x), q(x)$ 为已知连续函数。

## 通解公式

$$y = \mathrm{e}^{-\int p(x)\,\mathrm{d}x} \left[ \int \mathrm{e}^{\int p(x)\,\mathrm{d}x} \cdot q(x)\,\mathrm{d}x + C \right]$$

## 推导（积分因子法）

方程两边乘以 $\mathrm{e}^{\int p(x)\,\mathrm{d}x}$：

$$\begin{aligned}
\mathrm{e}^{\int p\,\mathrm{d}x} \cdot y' + \mathrm{e}^{\int p\,\mathrm{d}x} p \cdot y &= \mathrm{e}^{\int p\,\mathrm{d}x} \cdot q(x) \quad &\text{[乘以积分因子]} \\
\left[ \mathrm{e}^{\int p\,\mathrm{d}x} \cdot y \right]' &= \mathrm{e}^{\int p\,\mathrm{d}x} \cdot q(x) \quad &\text{[左边为乘积的导数]} \\
\mathrm{e}^{\int p\,\mathrm{d}x} \cdot y &= \int \mathrm{e}^{\int p\,\mathrm{d}x} \cdot q(x)\,\mathrm{d}x + C \quad &\text{[两边积分]}
\end{aligned}$$

## 定积分形式

研究解的性质（周期性、有界性、极限）时，常用定积分表达式：

$$y = \mathrm{e}^{-\int_{x_0}^x p(t)\,\mathrm{d}t} \left[ \int_{x_0}^x q(t)\,\mathrm{e}^{\int_{x_0}^t p(s)\,\mathrm{d}s}\,\mathrm{d}t + C \right]$$

## 变量互换

当 $\dfrac{\mathrm{d}y}{\mathrm{d}x}$ 形式复杂时，可交换 $x$ 与 $y$ 的角色，将方程化为 $\dfrac{\mathrm{d}x}{\mathrm{d}y} + p(y)x = q(y)$ 的形式求解。

## 相关页面

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[SeparableEquation|可分离变量型微分方程]]
- [[BernoulliEquation|伯努利方程]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "线性微分方程")
SORT 类型 ASC
```
