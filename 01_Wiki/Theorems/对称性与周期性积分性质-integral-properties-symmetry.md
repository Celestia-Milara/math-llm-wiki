---
title: 对称性与周期性积分性质
tags: [数学, 第9讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 偶函数、奇函数、周期函数的定积分简化公式，以及华里士公式和区间再现公式。
source: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 奇偶函数定积分

设 $f(x)$ 为连续函数：

- **偶函数**：$\displaystyle\int_{-a}^a f(x)\,\mathrm{d}x = 2\int_0^a f(x)\,\mathrm{d}x$
- **奇函数**：$\displaystyle\int_{-a}^a f(x)\,\mathrm{d}x = 0$

## 周期函数定积分

设 $f(x)$ 是以 $T$ 为周期的连续函数，则对任意实数 $a$：
$$\int_a^{a+T} f(x)\,\mathrm{d}x = \int_0^T f(x)\,\mathrm{d}x$$
即在长度为一个周期的区间上的定积分，与区间的起点位置无关。

## 区间再现公式

$$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(a+b-x)\,\mathrm{d}x$$

**推广**：若 $f(x)+f(a+b-x)$ 简单，则
$$\int_a^b f(x)\,\mathrm{d}x = \int_a^b \frac{f(x)+f(a+b-x)}{2}\,\mathrm{d}x$$

## 华里士公式 (Wallis)

$$\int_0^{\frac{\pi}{2}} \sin^n x\,\mathrm{d}x = \int_0^{\frac{\pi}{2}} \cos^n x\,\mathrm{d}x =
\begin{cases}
\displaystyle\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdots\frac{2}{3}\cdot 1, & n\text{为大于1的奇数},\\[8pt]
\displaystyle\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdots\frac{1}{2}\cdot\frac{\pi}{2}, & n\text{为正偶数}.
\end{cases}$$

### 变体形式

$$\int_0^\pi \sin^n x\,\mathrm{d}x = 
\begin{cases}
2\cdot\frac{n-1}{n}\cdots\frac{2}{3}\cdot 1, & n\text{为奇数},\\
2\cdot\frac{n-1}{n}\cdots\frac{1}{2}\cdot\frac{\pi}{2}, & n\text{为偶数}.
\end{cases}$$

$$\int_0^\pi \cos^n x\,\mathrm{d}x = 
\begin{cases}
0, & n\text{为奇数},\\
2\cdot\frac{n-1}{n}\cdots\frac{1}{2}\cdot\frac{\pi}{2}, & n\text{为偶数}.
\end{cases}$$

---

## Dataview

```dataview
TABLE 
  status as "状态",
  summary as "摘要"
FROM "01_Wiki/Methods"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
