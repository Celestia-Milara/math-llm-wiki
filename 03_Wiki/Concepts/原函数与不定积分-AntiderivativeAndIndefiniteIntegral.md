---
标题: 原函数与不定积分
标签: [数学, 第8讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 原函数是导数的逆运算概念，不定积分表示全体原函数。
来源: 01_Raw/Archive/Lectures/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 定义

设函数 $f(x)$ 定义在某区间 $I$ 上，若存在可导函数 $F(x)$，对于该区间上任意一点都有 $F'(x)=f(x)$ 成立，则称 $F(x)$ 是 $f(x)$ 在区间 $I$ 上的**一个原函数**。

称
$$\int f(x)\,\mathrm{d}x = F(x) + C$$
为 $f(x)$ 在区间 $I$ 上的**不定积分**，表示 $f(x)$ 的全体原函数。

## 基本性质

1. **线性性**：$\int [k_1 f(x) \pm k_2 g(x)]\,\mathrm{d}x = k_1\int f(x)\,\mathrm{d}x \pm k_2\int g(x)\,\mathrm{d}x$
2. **与微分互为逆运算**：
   - $\frac{\mathrm{d}}{\mathrm{d}x}\left[\int f(x)\,\mathrm{d}x\right] = f(x)$
   - $\int F'(x)\,\mathrm{d}x = F(x) + C$

## 重要说明

- 谈到原函数与不定积分，必须指明 $f(x)$ 所定义的区间。
- 若 $f(x)$ 有原函数，则原函数一定有无穷多个，彼此相差一个常数。
- 不定积分仅是对全体原函数的记号，**不是**一个函数值。

---

## Dataview

```dataview
TABLE 
  file.ctime as "创建时间",
  掌握状态 as "状态"
FROM "03_Wiki"
WHERE contains(file.name, "原函数") OR contains(file.name, "不定积分")
SORT file.ctime DESC
```
