---
标题: 微分的概念
标签: [数学, 第3讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 函数增量的线性主部，用"简单的线性量"近似"复杂的增量"。
来源: 01_Raw/03_第3讲_一元函数微分学的概念.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

设 $y = f(x)$ 在 $x_0$ 的某邻域内有定义，若存在与 $\Delta x$ 无关的常数 $A$，使得

$$\Delta y = A\Delta x + o(\Delta x)$$

则称 $f(x)$ 在 $x_0$ 处可微，$A\Delta x$ 称为**线性主部**，记作

$$\mathrm{d}y|_{x=x_0} = A\Delta x = f'(x_0)\,\mathrm{d}x$$

## 可微 $\iff$ 可导

一元函数中，可微与可导互为充要条件：

$$f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = A$$

## 几何意义

在点 $(x_0, y_0)$ 附近可以用切线段近似代替曲线段。

## 可微的判别步骤

1. 写增量 $\Delta y = f(x_0 + \Delta x) - f(x_0)$
2. 写线性增量 $A\Delta x = f'(x_0)\Delta x$
3. 作极限 $\lim_{\Delta x \to 0} \frac{\Delta y - A\Delta x}{\Delta x}$，若为 0 则可微

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
