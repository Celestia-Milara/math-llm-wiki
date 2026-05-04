---
title: 隐函数
tags: [数学, 第1讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 由方程 F(x, y) = 0 隐含确定的函数关系，不一定能显化。
source: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设方程 $F(x, y) = 0$，若当 $x$ 取某区间内的任一值时，总有满足该方程的唯一 $y$ 值存在，则称方程 $F(x, y) = 0$ 在该区间内确定了一个隐函数 $y = y(x)$。

## 说明

- 多值函数不能确定隐函数
- 有些隐函数可显化（如 $x + y^3 - 1 = 0 \Rightarrow y = \sqrt[3]{1 - x}$）
- 有些隐函数不易显化（如 $\sin(xy) = \ln\frac{x+e}{y} + 1$）

## 求值技巧

求 $y(x_0)$ 时：
- 若能直接代入 $x_0$ 求出 $y(x_0)$，则直接求
- 若不易求出，则用观察法（找特殊点或画图看交点）

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
