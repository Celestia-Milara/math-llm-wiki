---
title: 二重积分的对称性
tags: [数学, 第14讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 利用积分区域的对称性和被积函数的奇偶性简化二重积分计算，分为普通对称性和轮换对称性。
source: 00_Raw/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 普通对称性

### 关于 $y$ 轴对称

若 $D$ 关于 $y$ 轴对称，记 $D_1$ 为 $D$ 在 $y$ 轴右侧部分，则

$$
\iint_D f(x, y)\,\mathrm{d}\sigma =
\begin{cases}
2\displaystyle\iint_{D_1} f(x, y)\,\mathrm{d}\sigma, & f(x, y) = f(-x, y) \quad \text{（偶倍）},\\[10pt]
0, & f(x, y) = -f(-x, y) \quad \text{（奇零）}.
\end{cases}
$$

### 关于 $x$ 轴对称

若 $D$ 关于 $x$ 轴对称，记 $D_1$ 为 $D$ 在 $x$ 轴上侧部分，则

$$
\iint_D f(x, y)\,\mathrm{d}\sigma =
\begin{cases}
2\displaystyle\iint_{D_1} f(x, y)\,\mathrm{d}\sigma, & f(x, y) = f(x, -y),\\[10pt]
0, & f(x, y) = -f(x, -y).
\end{cases}
$$

### 关于 $x = a$ 对称

若 $D$ 关于 $x = a$ 对称，取对称点 $(x, y)$ 与 $(2a - x, y)$：

$$
\iint_D f(x, y)\,\mathrm{d}\sigma =
\begin{cases}
2\displaystyle\iint_{D_1} f(x, y)\,\mathrm{d}\sigma, & f(x, y) = f(2a - x, y),\\[10pt]
0, & f(x, y) = -f(2a - x, y).
\end{cases}
$$

### 关于 $y = a$ 对称

若 $D$ 关于 $y = a$ 对称，取对称点 $(x, y)$ 与 $(x, 2a - y)$。

### 关于原点对称

若 $D$ 关于原点对称，取对称点 $(x, y)$ 与 $(-x, -y)$：

$$
\iint_D f(x, y)\,\mathrm{d}\sigma =
\begin{cases}
2\displaystyle\iint_{D_1} f(x, y)\,\mathrm{d}\sigma, & f(x, y) = f(-x, -y),\\[10pt]
0, & f(x, y) = -f(-x, -y).
\end{cases}
$$

### 关于 $y = x$ 对称

若 $D$ 关于 $y = x$ 对称，取对称点 $(x, y)$ 与 $(y, x)$：

$$
\iint_D f(x, y)\,\mathrm{d}\sigma =
\begin{cases}
2\displaystyle\iint_{D_1} f(x, y)\,\mathrm{d}\sigma, & f(x, y) = f(y, x),\\[10pt]
0, & f(x, y) = -f(y, x).
\end{cases}
$$

> **口诀**：关键两点 — ① 看 $D$ 关于谁对称；② 将对称点代入 $f$，相等则 2 倍，相反则为 0。

## 轮换对称性

在直角坐标系下，若将 $x$ 与 $y$ 对调后，区域 $D$ 不变（即 $D$ 关于 $y = x$ 对称），则

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \iint_D f(y, x)\,\mathrm{d}\sigma.
$$

## 轮换对称性的应用技巧

当 $D$ 关于 $y = x$ 对称，但 $f(x, y)$ 与 $f(y, x)$ 既不相等也不相反时，考虑将二者相加：

$$
I = \iint_D f(x, y)\,\mathrm{d}\sigma = \iint_D f(y, x)\,\mathrm{d}\sigma = \frac12 \iint_D [f(x, y) + f(y, x)]\,\mathrm{d}\sigma.
$$

若 $f(x, y) + f(y, x) = a$（常数），则 $I = \frac{a}{2} S_D$，其中 $S_D$ 为 $D$ 的面积。

## 方法总结

遇到二重积分题目，**首先应考虑对称性**，看能否化简：

1. 检查 $D$ 的对称性（关于轴、原点、$y = x$ 等）
2. 检查 $f$ 在对称点处的取值关系
3. 满足普通对称性则使用偶倍奇零
4. 不满足普通对称性但 $D$ 关于 $y = x$ 对称，考虑轮换对称性

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
