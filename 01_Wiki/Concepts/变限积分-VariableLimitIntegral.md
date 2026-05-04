---
title: 变限积分
tags: [数学, 第8讲, 第9讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 由定积分定义的函数，积分上限或下限为变量。
source: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 定义

当 $x$ 在 $[a,b]$ 上变动时，积分 $\int_a^x f(t)\,\mathrm{d}t$ 是一个关于 $x$ 的函数，记作
$$F(x) = \int_a^x f(t)\,\mathrm{d}t \quad (a \le x \le b)$$
称为**变上限积分**。类似可定义变下限积分和上、下限都变化的积分，统称**变限积分**。

## 基本性质

1. **连续性**：若 $f(x)$ 在 $I$ 上可积，则 $F(x) = \int_a^x f(t)\,\mathrm{d}t$ 在 $I$ 上**连续**。
2. **可导性**：若 $f(x)$ 在 $I$ 上连续，则 $F(x)$ 在 $I$ 上可导且
   $$F'(x) = f(x)$$
3. **间断点处的情况**：
   - 若 $x_0$ 是 $f(x)$ 的**跳跃间断点**，则 $F(x)$ 在 $x_0$ 处连续但**不可导**，且
     $$F'_-(x_0) = \lim_{x\to x_0^-} f(x),\quad F'_+(x_0) = \lim_{x\to x_0^+} f(x)$$
   - 若 $x_0$ 是 $f(x)$ 的**可去间断点**，则 $F(x)$ 在 $x_0$ 处可导，且 $F'(x_0) = \lim_{x\to x_0} f(x)$

## 本质

变限积分是定积分的推广，本质是一个由定积分定义的**函数**，而非一个数值。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM #数学 AND (#定理 OR #方法) 
WHERE contains(tags, "变限积分")
SORT file.ctime ASC
```
