---
标题: 渐近线
标签: [数学, 第5讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 当曲线上的点远离原点时，曲线与之无限接近的直线，分为铅直、水平、斜三种。
来源: 01_Raw/Archive/Lectures/05_第5讲_一元函数微分学的应用(一).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定义

当曲线上的点远离原点时，曲线与某直线充分靠近，则称该直线为曲线的**渐近线**。

## 三种渐近线

### 1. 铅直渐近线（Vertical Asymptote）

若 $\lim_{x \to x_0^+} f(x) = \infty$（或 $\lim_{x \to x_0^-} f(x) = \infty$），则 $x = x_0$ 为一条铅直渐近线。

$x_0$ 通常是：函数的无定义点、定义区间的端点、分段函数的分段点。

### 2. 水平渐近线（Horizontal Asymptote）

若 $\lim_{x \to +\infty} f(x) = y_1$，则 $y = y_1$ 为一条水平渐近线；
若 $\lim_{x \to -\infty} f(x) = y_2$，则 $y = y_2$ 为一条水平渐近线。

$x \to +\infty$ 与 $x \to -\infty$ 时的水平渐近线可能相同（如 $y = \mathrm{e}^{-|x|}$），也可能不同（如 $y = \arctan x$）。

### 3. 斜渐近线（Oblique Asymptote）

若 

$$
\lim_{x \to \infty} \frac{f(x)}{x} = a \quad (a \neq 0), \qquad 
\lim_{x \to \infty} [f(x) - ax] = b,
$$

则 $y = ax + b$ 是曲线 $y = f(x)$ 的一条斜渐近线。

## 寻找渐近线的顺序

1. 找**铅直渐近线**：找无定义点、区间端点、分段点，判断极限是否为无穷大。
2. 找**水平渐近线**：判断 $\lim_{x \to \infty} f(x)$ 是否为常数。
3. 找**斜渐近线**：若 $\lim_{x \to \infty} f(x) = \infty$，则判断 $\lim_{x \to \infty} \frac{f(x)}{x}$ 是否为非零常数 $a$，再求 $b$。

> [!NOTE] 注意
> - 求斜渐近线时，$a$ 与 $b$ 必须均存在才能确定有斜渐近线（如 $y = x + \sin x$ 满足 $a = 1$ 但 $b$ 不存在，故无斜渐近线）。
> - 曲线与渐近线可能有交点。

---

**来源**：`01_Raw/05_第5讲_一元函数微分学的应用(一).md`

```dataview
TABLE 掌握状态, 类型 FROM "03_Wiki" WHERE contains(标签, this.标签[1]) SORT file.name ASC
```
