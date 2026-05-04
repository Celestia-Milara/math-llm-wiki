---
title: 原函数存在定理
tags: [数学, 第8讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 连续函数必有原函数；含第一类间断点和无穷间断点的函数必无原函数。
source: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 定理一（充分条件）

**连续函数 $f(x)$ 必有原函数 $F(x)$。**

证明思路：若 $f(x)$ 在 $[a,b]$ 上连续，则
$$F(x) = \int_a^x f(t)\,\mathrm{d}t$$
在 $[a,b]$ 上可导，且 $F'(x) = f(x)$。

由积分中值定理：
$$\frac{F(x+\Delta x)-F(x)}{\Delta x} = \frac{1}{\Delta x}\int_x^{x+\Delta x} f(t)\,\mathrm{d}t = f(\xi) \to f(x) \quad (\Delta x\to 0)$$

## 定理二（必要条件）

**含有第一类间断点或无穷间断点的函数 $f(x)$，在包含该间断点的区间内必没有原函数。**

证明思路：可导函数 $F(x)$ 的导函数 $F'(x)$ 具有**介值性**（达布定理），且 $F'(x)$ 不存在第一类间断点和无穷间断点。

## 重要推论

$$\text{函数 } f(x) \text{ 连续} \;\Rightarrow\;
\left\{
\begin{aligned}
&\int f(x)\,\mathrm{d}x = \int_a^x f(t)\,\mathrm{d}t + C,\\
&\left[\int_a^x f(t)\,\mathrm{d}t\right]' = f(x).
\end{aligned}
\right.$$

## 间断点类型与原函数关系

| 间断点类型 | 是否存在原函数 |
|:----------|:--------------|
| 连续 | 一定存在 |
| 可去间断点 | 不存在 |
| 跳跃间断点 | 不存在 |
| 无穷间断点 | 不存在 |
| 振荡间断点 | **不确定**（取决于函数具体形式） |

> [!TIP]
> 振荡间断点的情况需要具体分析。如 $f(x)=\begin{cases}2x\sin\frac1x-\cos\frac1x,&x\neq0\\0,&x=0\end{cases}$ 存在原函数 $F(x)=x^2\sin\frac1x$；而 $f(x)=\begin{cases}\frac1x\sin\frac1x,&x\neq0\\0,&x=0\end{cases}$ 不存在原函数。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.ctime ASC
```
