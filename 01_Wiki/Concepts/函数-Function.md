---
title: 函数
tags: [数学, 第1讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 描述变量之间的依赖关系，核心是定义域内每个 x 对应唯一确定的 y。
source: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设 $x$ 与 $y$ 是两个变量，$D$ 是一个给定的数集，若对于每一个 $x \in D$，按照一定的法则 $f$，有一个确定的 $y$ 值与之对应，则称 $y$ 为 $x$ 的函数，记作 $y = f(x)$。

- **自变量**：$x$
- **因变量**：$y$
- **定义域**：数集 $D$
- **值域**：$\{f(x) \mid x \in D\}$

## 单值函数与多值函数

- **单值函数**：一个 $x$ 对应唯一一个 $y$（可一对一或多对一）。
- **多值函数**：一个 $x$ 对应多个 $y$（一对多），不在传统函数定义范围内。

> 判断方法——铅直画线法：作铅直线，若任一条铅直线与曲线至多有一个交点，则为单值函数。

## 函数的表示法

1. 显函数：$y = f(x)$
2. 隐函数：$F(x, y) = 0$
3. 分段函数：不同区间用不同表达式
4. 参数方程：$\begin{cases} x = \varphi(t) \\ y = \psi(t) \end{cases}$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
