---
标题: 常数项级数
标签: [数学, 第16讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 无穷多个常数项相加的形式化表达式，通过部分和数列的极限定义其收敛与发散。
来源: 00_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

给定无穷数列 $u_1, u_2, \dots, u_n, \dots$，将其各项用加号连起来得到：

$$\sum_{n=1}^{\infty} u_n = u_1 + u_2 + \cdots + u_n + \cdots$$

称为**无穷级数**，简称**级数**。$u_n$ 称为通项。若 $u_n$ 是常数，则称为**常数项级数**。

## 收敛与发散

令部分和 $S_n = u_1 + u_2 + \cdots + u_n$。

- 若 $\displaystyle\lim_{n \to \infty} S_n = S$（存在有限），则称级数 **收敛**，$S$ 称为级数的和。
- 若 $\displaystyle\lim_{n \to \infty} S_n$ 不存在，则称级数 **发散**。

## 几何级数（等比级数）

$$\sum_{n=1}^{\infty} a q^{n-1} \begin{cases}
\text{收敛}, & |q| < 1, \text{和为 } \dfrac{a}{1-q} \\[6pt]
\text{发散}, & |q| \geqslant 1
\end{cases}$$

## $p$ 级数

$$\sum_{n=1}^{\infty} \frac{1}{n^p} \begin{cases}
\text{收敛}, & p > 1 \\
\text{发散}, & p \leqslant 1
\end{cases}$$

## 相关概念

- [[AbsoluteAndConditionalConvergence|绝对收敛与条件收敛]]
- [[PowerSeries|幂级数]]
- [[级数的基本性质-BasicPropertiesOfSeries|级数的基本性质]]

---

```dataview
TABLE title, status, summary
FROM "01_Wiki"
WHERE contains(tags, "级数") OR contains(tags, this.file.tags[1])
SORT type ASC
```
