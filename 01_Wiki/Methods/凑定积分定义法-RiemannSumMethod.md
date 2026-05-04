---
title: 凑定积分定义法
tags: [数学, 第8讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 将 n 项和的极限转化为定积分计算，利用黎曼和的定义。
source: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验.

## 基本原理

$$\lim_{n\to\infty} \sum_{i=1}^n f\!\left(\frac{i}{n}\right)\cdot\frac{1}{n} = \int_0^1 f(x)\,\mathrm{d}x$$

更一般地：
$$\lim_{n\to\infty} \sum_{i=1}^n f\!\left(a+\frac{b-a}{n}i\right)\frac{b-a}{n} = \int_a^b f(x)\,\mathrm{d}x$$

## 操作步骤

1. **提出 $\frac{1}{n}$**：从通项中分解出因子 $\frac{1}{n}$
2. **凑出 $\frac{i}{n}$**：将剩余部分转化为关于 $\frac{i}{n}$ 的函数形式
3. **写定积分**：$\frac{i}{n} \to x$，$\frac{1}{n} \to \mathrm{d}x$，积分区间 $[0,1]$

## 典型示例

$$\begin{aligned}
\lim_{n\to\infty}\sum_{i=1}^n\frac{n+i}{n^2+i^2}
&= \lim_{n\to\infty}\sum_{i=1}^n\frac{1+\frac{i}{n}}{1+\left(\frac{i}{n}\right)^2}\cdot\frac{1}{n} \\[4pt]
&= \int_0^1 \frac{1+x}{1+x^2}\,\mathrm{d}x
\end{aligned}$$

## 适用条件

- 极限是 $n$ 项和的极限
- 通项能写成 $f\!\left(\frac{i}{n}\right)\cdot\frac{1}{n}$ 的形式
- 若不能凑成标准形式，考虑夹逼准则

> [!TIP]
> 若分母上出现 $n+i$，提出 $n$ 后化为 $1+\frac{i}{n}$；若分母上出现 $n^2+i^2$，提出 $n^2$ 后化为 $1+\left(\frac{i}{n}\right)^2$。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Concepts"
WHERE contains(tags, "定积分")
SORT file.name ASC
```
