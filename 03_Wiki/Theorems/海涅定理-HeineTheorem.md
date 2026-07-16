---
标题: 海涅定理（归结原则）
标签: [数学, 第2讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 联系数列极限与函数极限的桥梁，将数列极限转化为函数极限以使用洛必达等工具。
来源: 01_Raw/Archive/Lectures/02_第2讲_数列极限.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 可信状态 改为 S2 已核查。

## 定理陈述

设 $f(x)$ 在 $\overset{\circ}{U}(x_0, \delta)$ 内有定义，则

$$\lim_{x \to x_0} f(x) = A \iff \text{对任何以 } x_0 \text{ 为极限的数列 } \{x_n\} (x_n \neq x_0), \lim_{n \to \infty} f(x_n) = A$$

## 核心用途

数列极限不能直接用洛必达法则，通过海涅定理转化为函数极限后，便可使用洛必达、泰勒等强大工具。

### 常见转化

- $x \to 0$ 时，取 $x_n = \frac{1}{n}$，则 $\lim_{n \to \infty} f(\frac{1}{n}) = \lim_{x \to 0} f(x)$
- $x \to +\infty$ 时，取 $x_n = n$，则 $\lim_{n \to \infty} f(n) = \lim_{x \to +\infty} f(x)$

## 证明函数不连续

取有理数列和无理数列分别得到不同极限值，从而证明函数在该点不连续。

## 相关条目

```dataview
TABLE 可信状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
