---
title: 基本初等函数
tags: [数学, 第1讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 六类基本初等函数及其图像性质——常数、幂、指数、对数、三角、反三角。
source: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 分类

基本初等函数包括：常数函数、幂函数、指数函数、对数函数、三角函数、反三角函数。

由基本初等函数经过有限次四则运算和复合步骤构成的且可由一个式子表示的函数称为**初等函数**。

> 幂指函数 $u(x)^{v(x)} = \mathrm{e}^{v(x)\ln u(x)}$ 也是初等函数。

## 重要性质

### 幂函数求最值技巧

1. 见到 $\sqrt{u}$，可用 $u$ 来研究最值
2. 见到 $|u|$，由 $|u| = \sqrt{u^2}$，可用 $u^2$ 研究最值
3. 见到多项相乘，取对数再求导
4. 见到 $\frac{1}{u}$，可用 $u$ 研究最值（结论相反）

### 常用恒等变形

$$x = \mathrm{e}^{\ln x}\,(x > 0), \quad u^\nu = \mathrm{e}^{\ln u^\nu} = \mathrm{e}^{\nu \ln u}\,(u > 0)$$

### 三角恒等式

$$\sin^2\alpha + \cos^2\alpha = 1, \quad 1 + \tan^2\alpha = \sec^2\alpha, \quad 1 + \cot^2\alpha = \csc^2\alpha$$

## 重要函数图像

- $y = \ln(x + \sqrt{x^2 + 1})$（反双曲正弦，奇函数，等价无穷小 $\sim x$）
- $y = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2}$（双曲正弦）
- $y = \frac{\mathrm{e}^x + \mathrm{e}^{-x}}{2}$（双曲余弦，偶函数，悬链线）

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
