---
标题: 泰勒公式
标签: [数学, 第1讲, 第6讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 用多项式逼近可导函数的方法，是极限计算最强大的工具。
来源: 01_Raw/01_第1讲_函数极限与连续.md, 01_Raw/06_第6讲_一元函数微分学的应用(二).md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。
## 定理陈述


## 公式（两种余项形式）

### 带佩亚诺余项的 $n$ 阶泰勒公式（局部）

适用于求极限、判定无穷小的阶数、判定极值等。

设 $f(x)$ 在点 $x_0$ 处 $n$ 阶可导，则存在 $x_0$ 的一个邻域，有

$$f(x) = f(x_0) + f'(x_0)(x - x_0) + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + o((x - x_0)^n)$$

### 带拉格朗日余项的 $n$ 阶泰勒公式（整体）

适用于区间上的证明题，如证不等式、中值等式等。

设 $f(x)$ 在点 $x_0$ 的某个邻域内 $n+1$ 阶导数存在，则

$$f(x) = f(x_0) + f'(x_0)(x - x_0) + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$$

其中 $\xi$ 介于 $x$ 与 $x_0$ 之间。

### 麦克劳林公式（$x_0 = 0$）

**拉格朗日余项**：
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + \frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1}$$

**佩亚诺余项**：
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + o(x^n)$$

## 常用泰勒展开（$x \to 0$）

**完整麦克劳林展开式**（带佩亚诺余项）：

$$\begin{aligned}
\mathrm{e}^x &= 1 + x + \frac{1}{2!}x^2 + \cdots + \frac{1}{n!}x^n + o(x^n) \\
\sin x &= x - \frac{x^3}{3!} + \cdots + (-1)^n\frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1}) \\
\cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots + (-1)^n\frac{x^{2n}}{(2n)!} + o(x^{2n}) \\
\frac{1}{1-x} &= 1 + x + x^2 + \cdots + x^n + o(x^n) \\
\frac{1}{1+x} &= 1 - x + x^2 - \cdots + (-1)^nx^n + o(x^n) \\
\ln(1+x) &= x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + (-1)^{n-1}\frac{x^n}{n} + o(x^n) \\
(1+x)^\alpha &= 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \cdots + \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n + o(x^n)
\end{aligned}$$

### 常用前几项（$x \to 0$）

$$\begin{aligned}
\sin x &= x - \frac{x^3}{3!} + o(x^3) \\
\cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^4) \\
\arcsin x &= x + \frac{x^3}{3!} + o(x^3) \\
\tan x &= x + \frac{x^3}{3} + o(x^3) \\
\arctan x &= x - \frac{x^3}{3} + o(x^3) \\
\ln(1 + x) &= x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3) \\
\mathrm{e}^x &= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + o(x^3) \\
(1 + x)^\alpha &= 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + o(x^2)
\end{aligned}$$

## 展开原则

### ① $\frac{A}{B}$ 型——上下同阶
分母（或分子）是 $x$ 的 $k$ 次幂，则把分子（或分母）展开到 $x$ 的 $k$ 次幂。

### ② $A - B$ 型——幂次最低
将 $A, B$ 分别展开到系数不相等的 $x$ 的最低次幂。

## 差函数的等价无穷小

$$\begin{aligned}
x - \sin x &\sim \frac{1}{6}x^3 \\
\arcsin x - x &\sim \frac{1}{6}x^3 \\
\tan x - x &\sim \frac{1}{3}x^3 \\
x - \arctan x &\sim \frac{1}{3}x^3 \\
x - \ln(1 + x) &\sim \frac{1}{2}x^2
\end{aligned}$$

## 相关条目

## 应用场景

1. **求极限**：使用佩亚诺余项展开。
2. **证明不等式**：使用拉格朗日余项展开。
3. **判定极值/拐点**：展开到合适的阶数，利用展开式判定。
4. **中值等式证明**：选择适当的展开点和被展开点构造等式。

## 使用技巧

- **展开点 $x_0$ 的选择**：取已知导数值的点或待证导数值的点。
- **被展开点 $x$ 的选择**：取已知函数值的点或特殊点（端点、中间点等）。
- **消去未知项**：通过代入特殊点相加减，消去未知的函数值或导数值。

```dataview
TABLE 掌握状态, 类型 FROM "03_Wiki" WHERE any(filter(this.标签, (t) => startswith(t, "第")), (chapter) => contains(标签, chapter)) SORT file.name ASC
```
