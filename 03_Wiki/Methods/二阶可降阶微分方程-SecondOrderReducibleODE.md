---
标题: 二阶可降阶微分方程
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过换元将二阶方程化为一阶方程的三种基本类型：缺 $y$、缺 $x$、缺 $x$ 和 $y$。
来源: 01_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 类型一：$y'' = f(x, y')$（不显含 $y$）

令 $y' = p(x)$，则 $y'' = p'$，原方程化为：

$$\frac{\mathrm{d}p}{\mathrm{d}x} = f(x, p)$$

求解得 $p = \varphi(x, C_1)$，再积分得 $y = \int \varphi(x, C_1)\,\mathrm{d}x + C_2$。

## 类型二：$y'' = f(y, y')$（不显含 $x$）

令 $y' = p(y)$，则 $y'' = \dfrac{\mathrm{d}p}{\mathrm{d}x} = \dfrac{\mathrm{d}p}{\mathrm{d}y}\cdot\dfrac{\mathrm{d}y}{\mathrm{d}x} = p\dfrac{\mathrm{d}p}{\mathrm{d}y}$，原方程化为：

$$p\frac{\mathrm{d}p}{\mathrm{d}y} = f(y, p)$$

求解得 $p = \varphi(y, C_1)$，再由 $\dfrac{\mathrm{d}y}{\mathrm{d}x} = \varphi(y, C_1)$ 分离变量求解。

## 类型三：$y'' = f(y')$（既不显含 $y$ 也不显含 $x$）

按类型一（缺 $y$）处理，令 $y' = p$，$y'' = p'$。

## 相关页面

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[SeparableEquation|可分离变量型微分方程]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "微分方程")
SORT 类型 ASC
```
