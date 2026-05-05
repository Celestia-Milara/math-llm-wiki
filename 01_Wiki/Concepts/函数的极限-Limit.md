---
标题: 函数的极限
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 当自变量无限接近某点时，函数值无限趋近于某一确定常数的过程。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## $\varepsilon$-$\delta$ 定义

设函数 $f(x)$ 在点 $x_0$ 的某一去心邻域内有定义。若存在常数 $A$，对任意 $\varepsilon > 0$，总存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，有 $|f(x) - A| < \varepsilon$，则称 $A$ 为 $f(x)$ 当 $x \to x_0$ 时的极限，记作

$$\lim_{x \to x_0} f(x) = A$$

## 极限的双向性

极限存在的充要条件是左、右极限存在且相等：

$$\lim_{x \to x_0} f(x) = A \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = A$$

## 常见不存在的极限例子

1. $\lim_{x \to \infty} \mathrm{e}^x$ 不存在（$x \to +\infty$ 为 $+\infty$，$x \to -\infty$ 为 $0$）
2. $\lim_{x \to 0} \frac{\sin x}{|x|}$ 不存在（左右极限分别为 $1$ 和 $-1$）
3. $\lim_{x \to \infty} \arctan x$ 不存在
4. $\lim_{x \to 0} [x]$ 不存在（$[x]$ 为取整函数）

## 24 种极限定义

自变量趋近方式有 6 种：$x \to x_0, x \to x_0^+, x \to x_0^-, x \to \infty, x \to +\infty, x \to -\infty$

函数趋近方式有 4 种：$f(x) \to A, f(x) \to \infty, f(x) \to +\infty, f(x) \to -\infty$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
