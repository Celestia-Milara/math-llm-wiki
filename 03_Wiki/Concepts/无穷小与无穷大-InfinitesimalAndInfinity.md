---
标题: 无穷小与无穷大
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 无穷小是以 0 为极限的变量，无穷大是其倒数；二者描述变化趋势而非具体数值。
来源: 01_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 可信状态 改为 S2 已核查。

## 定义

无穷小是以 0 为极限的变量，无穷大是其倒数，二者描述变化趋势而非具体数值。

## 无穷小

如果当 $x \to x_0$（或 $x \to \infty$）时，函数 $f(x)$ 的极限为零，则称 $f(x)$ 为该过程中的无穷小。

$$\lim_{x \to x_0} f(x) = 0$$

### 无穷小的性质

1. **有限个**无穷小的和是无穷小
2. 有界函数与无穷小的乘积是无穷小
3. **有限个**无穷小的乘积是无穷小

## 无穷大

如果当 $x \to x_0$（或 $x \to \infty$）时，$|f(x)|$ 无限增大，则称 $f(x)$ 为该过程中的无穷大。

$$\lim_{x \to x_0} f(x) = \infty$$

## 无穷小与无穷大的关系

在自变量的同一变化过程中：
- $f(x)$ 为无穷大 $\Rightarrow$ $\frac{1}{f(x)}$ 为无穷小
- $f(x)$ 为无穷小且 $f(x) \neq 0$ $\Rightarrow$ $\frac{1}{f(x)}$ 为无穷大

## 无穷小的比阶

设 $\lim \alpha(x) = 0$，$\lim \beta(x) = 0$，$\beta(x) \neq 0$：

- **高阶**：$\lim \frac{\alpha}{\beta} = 0$，记 $\alpha = o(\beta)$
- **低阶**：$\lim \frac{\alpha}{\beta} = \infty$
- **同阶**：$\lim \frac{\alpha}{\beta} = c \neq 0$
- **等价**：$\lim \frac{\alpha}{\beta} = 1$，记 $\alpha \sim \beta$
- **$k$ 阶**：$\lim \frac{\alpha}{[\beta]^k} = c \neq 0$

### 常用等价无穷小（$x \to 0$）

$$\sin x \sim x,\quad \tan x \sim x,\quad \arcsin x \sim x,\quad \arctan x \sim x,$$
$$\ln(1 + x) \sim x,\quad \mathrm{e}^x - 1 \sim x,\quad a^x - 1 \sim x\ln a,$$
$$1 - \cos x \sim \frac{1}{2}x^2,\quad (1 + x)^\alpha - 1 \sim \alpha x$$

## 相关条目

```dataview
TABLE 可信状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
