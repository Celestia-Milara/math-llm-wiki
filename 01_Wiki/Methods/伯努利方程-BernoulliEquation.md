---
title: 伯努利方程
tags: [数学, 第15讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 形如 $y' + p(x)y = q(x)y^n$ 的非线性一阶微分方程，通过代换化为一阶线性方程求解。
source: 00_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 标准形式

$$\frac{\mathrm{d}y}{\mathrm{d}x} + p(x)y = q(x)y^n \quad (n \neq 0, 1)$$

## 解法步骤

1. 变形为 $y^{-n} \cdot \dfrac{\mathrm{d}y}{\mathrm{d}x} + p(x)y^{1-n} = q(x)$。

2. 令 $z = y^{1-n}$，则 $\dfrac{\mathrm{d}z}{\mathrm{d}x} = (1-n)y^{-n}\dfrac{\mathrm{d}y}{\mathrm{d}x}$。

3. 化为 $\dfrac{1}{1-n}\dfrac{\mathrm{d}z}{\mathrm{d}x} + p(x)z = q(x)$，即一阶线性微分方程。

> [!NOTE]
> 伯努利方程仅数学一考试明确要求，但换元思想值得所有考生掌握。

## 相关页面

- [[FirstOrderLinearODE|一阶线性微分方程]]
- [[SeparableEquation|可分离变量型微分方程]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "微分方程")
SORT type ASC
```
