---
title: 单调有界准则
tags: [数学, 第2讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 单调有界数列必有极限，是证明数列收敛最重要的准则之一。
source: 00_Raw/02_第2讲_数列极限.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 准则

单调有界数列必有极限：

- **单调增加 + 有上界** $\Rightarrow$ 极限存在
- **单调减少 + 有下界** $\Rightarrow$ 极限存在

## 证明数列单调性的常用方法

### a. 作差法 / 作商法

- $x_{n+1} - x_n > 0$ 或 $\frac{x_{n+1}}{x_n} > 1$（同号时）$\Rightarrow$ 单调增加

### b. 数学归纳法

1. 验证 $n = 1$ 成立
2. 设 $n = k$ 成立
3. 证 $n = k+1$ 成立

### c. 利用重要不等式

如 $\mathrm{e}^x \ge x + 1$，$x - 1 \ge \ln x$，$\sin x \le x$ 等

### d. 递推函数单调性

若 $x_{n+1} = f(x_n)$：
- $f'(x) > 0$ $\Rightarrow$ $\{x_n\}$ 单调（$x_2 > x_1$ 时单调增，$x_2 < x_1$ 时单调减）
- $f'(x) < 0$ $\Rightarrow$ $\{x_n\}$ 不单调（可考虑压缩映射）

## 求极限

先证明收敛，再对递推式两边取极限，解方程得极限值。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
