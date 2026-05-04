---
title: 齐次型微分方程
tags: [数学, 第15讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 形如 $\dfrac{\mathrm{d}y}{\mathrm{d}x} = \varphi\left(\dfrac{y}{x}\right)$ 的方程，通过代换 $u = y/x$ 化为可分离变量型。
source: 00_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 标准形式

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \varphi\left(\frac{y}{x}\right)$$

## 解法

令 $u = \dfrac{y}{x}$，则 $y = ux$，于是：

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u + x\frac{\mathrm{d}u}{\mathrm{d}x}$$

代入原方程得：

$$x\frac{\mathrm{d}u}{\mathrm{d}x} + u = \varphi(u) \quad\Rightarrow\quad \frac{\mathrm{d}u}{\varphi(u)-u} = \frac{\mathrm{d}x}{x}$$

化为可分离变量型求解，最后以 $u = \dfrac{y}{x}$ 回代。

> 注意与常系数齐次线性微分方程区分：齐次型方程是关于 $\dfrac{y}{x}$ 的函数，而非关于 $y$ 的线性齐次。

## 相关页面

- [[SeparableEquation|可分离变量型微分方程]]
- [[OrdinaryDifferentialEquation|常微分方程]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "微分方程")
SORT type ASC
```
