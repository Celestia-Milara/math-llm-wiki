---
标题: 夹逼准则求积分极限
标签: [数学, 第11讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 利用夹逼准则（迫敛性）求与参数 $n$ 有关的定积分的极限。
来源: 01_Raw/Archive/Lectures/11_第11讲_一元函数积分学的应用(二).md
可信状态: S3 待核查
---

## 方法概述

对于被积函数中含有参数 $n$ 的定积分，当 $n \to \infty$ 时求极限，常用夹逼准则。

### 基本思路

1. 对被积函数进行放缩，找到上界和下界
2. 利用积分的保号性得到积分的不等式关系
3. 证明上界和下界的极限相等

## 基本结论

设 $f(x)$ 在 $[0, 1]$ 上连续，则

$$
\lim_{n \to \infty} \int_0^1 x^n f(x) \, \mathrm{d}x = 0.
$$

**证明**：由 $m \leqslant f(x) \leqslant M$，得 $m \int_0^1 x^n \, \mathrm{d}x \leqslant \int_0^1 x^n f(x) \, \mathrm{d}x \leqslant M \int_0^1 x^n \, \mathrm{d}x$，即

$$
\frac{m}{n+1} \leqslant \int_0^1 x^n f(x) \, \mathrm{d}x \leqslant \frac{M}{n+1},
$$

由夹逼准则得极限为 0。

## 常用放缩技巧

- $0 \leqslant \frac{x^{n+1}}{1+x} \leqslant x^{n+1}$（$0 \leqslant x \leqslant 1$）
- $0 \leqslant \ln(1+t) \leqslant t$（$0 \leqslant t \leqslant 1$）
- $\mathrm{e}^{-x^n} \leqslant \frac{1}{x^n+1} \leqslant \frac{1}{x^n}$

## 典型例题

**例**：$\lim_{n \to \infty} \int_0^1 (n+1) x^n \ln(1+x) \, \mathrm{d}x = \ln 2$。

**思路**：凑微分得 $\int_0^1 \ln(1+x) \, \mathrm{d}(x^{n+1})$，分部积分后利用放缩法处理剩余项。

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "夹逼准则")
SORT file.name ASC
```
