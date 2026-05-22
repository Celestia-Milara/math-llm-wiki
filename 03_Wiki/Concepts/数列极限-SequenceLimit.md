---
标题: 数列极限
标签: [数学, 第2讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 描述正整数下标 n → ∞ 时数列通项 xₙ 的趋近行为，是函数极限的离散版本。
来源: 01_Raw/02_第2讲_数列极限.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

数列 $\{x_n\}$ 是按照下标 $n$ 从小到大排列的一列数，可视为整标函数 $x_n = f(n), n \in \mathbf{N}_+$。

### 子列

从原数列选取无穷多项并按原顺序组成的新数列，记作 $\{a_{n_k}\}$。

### 常见数列

- **等差数列**：$a_n = a_1 + (n-1)d$, $S_n = \frac{n}{2}(a_1 + a_n)$
- **等比数列**：$a_n = a_1 r^{n-1}$, $S_n = \frac{a_1(1-r^n)}{1-r} (r \neq 1)$

### 求和公式

$$\sum_{k=1}^n k = \frac{n(n+1)}{2}, \quad \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{k=1}^n \frac{1}{k(k+1)} = \frac{n}{n+1}$$

## ε-N 定义

设 $\{x_n\}$ 为一数列，若存在常数 $a$，对任意 $\varepsilon > 0$，总存在正整数 $N$，使得当 $n > N$ 时，$|x_n - a| < \varepsilon$ 恒成立，则称 $a$ 是数列 $\{x_n\}$ 的极限，记作 $\lim_{n \to \infty} x_n = a$。

## 收敛数列的性质

1. **唯一性**：极限若存在，则唯一
2. **有界性**：收敛数列必有界
3. **保号性**：若 $\lim_{n \to \infty} x_n = a > b$，则存在 $N > 0$，当 $n > N$ 时 $x_n > b$；反之，若 $x_n \geq b$ 且极限存在，则 $\lim x_n \geq b$

## 收敛与子列的关系

若数列 $\{a_n\}$ 收敛，则其任何子列收敛到同一极限。

> 推论：$\lim_{n \to \infty} a_n = a \iff \lim_{k \to \infty} a_{2k} = a \land \lim_{k \to \infty} a_{2k-1} = a$

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
