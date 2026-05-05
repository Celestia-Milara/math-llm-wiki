---
标题: 复合函数
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 将一个函数的输出作为另一个函数的输入，构建多层函数关系。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设函数 $y = f(u)$ 的定义域为 $D_1$，函数 $u = g(x)$ 在 $D$ 上有定义，且 $g(D) \subset D_1$，则由

$$y = f[g(x)] \quad (x \in D)$$

确定的函数称为由 $u = g(x)$ 和 $y = f(u)$ 构成的复合函数，$u$ 称为中间变量。

## 复合方法

- 将内层函数整体代入外层函数
- 复合可以多层嵌套：$h[f[g(x)]]$

## 重要技巧

已知复合函数求原函数：将内层函数视为整体变量，找出对应法则。

如：$f\left(x + \frac{1}{x}\right) = \frac{x + x^3}{1 + x^4}$，通过变形将右侧也用 $x + \frac{1}{x}$ 表达。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
