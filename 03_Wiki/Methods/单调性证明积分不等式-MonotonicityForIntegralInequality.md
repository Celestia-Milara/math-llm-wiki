---
标题: 单调性证明积分不等式
标签: [数学, 第11讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过构造辅助函数并利用其单调性来证明积分不等式。
来源: 01_Raw/Archive/Lectures/11_第11讲_一元函数积分学的应用(二).md
可信状态: S3 待核查
---

## 方法概述

此方法多用于所给条件为"$f(x)$ 在 $[a, b]$ 上连续"的情形。

### 基本步骤

1. 将某一积分限（通常取上限）变量化
2. 移项构造辅助函数 $F(x)$
3. 求导分析 $F(x)$ 的单调性
4. 利用端点值确定符号

## 典型例题

**条件**：$f(x), g(x)$ 在 $[a, b]$ 上连续，$f(x)$ 单调增加，$0 \leqslant g(x) \leqslant 1$。

**结论**：

$$
\int_a^{a + \int_a^b g(t) \, \mathrm{d}t} f(x) \, \mathrm{d}x \leqslant \int_a^b f(x) g(x) \, \mathrm{d}x.
$$

**证明思路**：令 $F(x) = \int_a^{a + \int_a^x g(u) \, \mathrm{d}u} f(t) \, \mathrm{d}t - \int_a^x f(t) g(t) \, \mathrm{d}t$，求导得

$$
F'(x) = \left\{ f\left[a + \int_a^x g(u) \, \mathrm{d}u\right] - f(x) \right\} g(x) \leqslant 0,
$$

故 $F(x)$ 单调减少，由 $F(a) = 0$ 得 $F(b) \leqslant 0$。

## 常用技巧

- 辅助函数的构造通常源于"移项"
- 注意利用已知条件判断导数的符号
- 结合积分的保号性和比较定理

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
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
