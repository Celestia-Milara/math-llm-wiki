---
标题: 介值定理与零点定理
标签: [数学, 第6讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 闭区间上连续函数的四个基本定理，包括有界与最值定理、介值定理、平均值定理、零点定理。
来源: 00_Raw/06_第6讲_一元函数微分学的应用(二).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 涉及函数的中值定理（连续函数性质）

设 $f(x)$ 在 $[a,b]$ 上连续，则有以下定理：

### 定理 1：有界与最值定理

$$
m \leq f(x) \leq M
$$

其中 $m, M$ 分别为 $f(x)$ 在 $[a,b]$ 上的最小值与最大值。

### 定理 2：介值定理

当 $m \leq \mu \leq M$ 时，存在 $\xi \in [a,b]$，使得 $f(\xi) = \mu$。

### 定理 3：平均值定理

当 $a < x_1 < x_2 < \cdots < x_n < b$ 时，在 $[x_1, x_n]$ 内至少存在一点 $\xi$，使得

$$
f(\xi) = \frac{f(x_1) + f(x_2) + \cdots + f(x_n)}{n}
$$

### 定理 4：零点定理

当 $f(a) \cdot f(b) < 0$ 时，存在 $\xi \in (a, b)$，使得 $f(\xi) = 0$。

**推广的零点定理**：若 $f(x)$ 在 $(a,b)$ 内连续，$\lim_{x \to a^+} f(x) = \alpha$，$\lim_{x \to b^-} f(x) = \beta$，且 $\alpha \cdot \beta < 0$，则 $f(x) = 0$ 在 $(a,b)$ 内至少有一个根。其中 $a, b, \alpha, \beta$ 可以是有限数或无穷大。

---

**来源**：`00_Raw/06_第6讲_一元函数微分学的应用(二).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
