---
title: 边际函数（Marginal Function）
tags: [数学, 第7讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 经济学中导数的应用，表示当自变量改变一个单位时因变量的近似改变量。
source: 00_Raw/07_第7讲_一元函数微分学的应用(三).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定义

若函数 $f(x)$ 可导，则称 $f'(x)$ 为 $f(x)$ 的**边际函数**。$f'(x_0)$ 称为 $f(x)$ 在 $x_0$ 点的边际值。

由微分近似 $\Delta y \approx \mathrm{d}y$，取 $\Delta x = 1$，得：

$$
f(x_0 + 1) - f(x_0) \approx f'(x_0)
$$

**解释**：在 $x_0$ 点，当 $x$ 改变一个单位时，函数 $f(x)$ 近似改变 $|f'(x_0)|$ 个单位。

## 常见边际函数

### 边际成本（MC）

设总成本函数 $C = C(Q)$（$Q$ 为产量），则

$$
MC = C'(Q)
$$

### 边际收益（MR）

设总收益函数 $R = R(Q)$（$Q$ 为销售量），则

$$
MR = R'(Q)
$$

### 边际利润（ML）

设利润函数 $L = L(Q)$（$Q$ 为销售量），则

$$
ML = L'(Q)
$$

## 利润最大化条件

令边际利润为零：$ML = L'(Q) = 0$，即 $MC = MR$（边际成本 = 边际收益）。

---

**来源**：`00_Raw/07_第7讲_一元函数微分学的应用(三).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
