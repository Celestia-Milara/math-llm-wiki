---
标题: 绝对收敛与条件收敛
标签: [数学, 第16讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 任意项级数的两种收敛类型——绝对值级数收敛者为绝对收敛，自身收敛但绝对值级数发散者为条件收敛。
来源: 01_Raw/Archive/Lectures/16_第16讲_无穷级数.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

设 $\sum u_n$ 为任意项级数。

- **绝对收敛**：$\sum |u_n|$ 收敛，则 $\sum u_n$ 必收敛。
- **条件收敛**：$\sum u_n$ 收敛，但 $\sum |u_n|$ 发散。

## 性质

1. 若 $\sum u_n$ 绝对收敛，$\sum v_n$ 条件收敛，则 $\sum (u_n \pm v_n)$ 条件收敛。
2. 若 $\sum u_n, \sum v_n$ 均绝对收敛，则 $\sum (u_n \pm v_n)$ 绝对收敛。
3. 若 $\sum u_n$ 条件收敛，则其正项部分和负项部分构成的级数均发散。

## 交错 $p$ 级数的敛散性

$$\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n^p} \begin{cases}
\text{绝对收敛}, & p > 1 \\
\text{条件收敛}, & 0 < p \leqslant 1
\end{cases}$$

## 相关页面

- [[03_Wiki/Concepts/常数项级数-NumericalSeries|常数项级数]]
- [[03_Wiki/Methods/正项级数审敛法-ConvergenceTestsForPositiveSeries|正项级数审敛法]]
- [[03_Wiki/Theorems/莱布尼茨判别法-LeibnizTest|交错级数审敛法]]

---

```dataview
TABLE title, 可信状态, 摘要
FROM "03_Wiki"
WHERE contains(标签, "收敛") AND 类型 != "概念"
SORT 类型 ASC
```
