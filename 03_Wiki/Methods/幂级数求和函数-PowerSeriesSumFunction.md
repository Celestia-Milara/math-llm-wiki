---
标题: 幂级数求和函数
标签: [数学, 第16讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 利用逐项求导、逐项积分及重要展开式将幂级数化为封闭形式，包括代数法、微分方程法。
来源: 01_Raw/Archive/Lectures/16_第16讲_无穷级数.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 基本原理

在收敛域上，记 $S(x) = \sum u_n(x)$ 为和函数。

## 常用公式

$$\begin{aligned}
\sum_{n=0}^{\infty} x^n &= \frac{1}{1-x}, \quad |x| < 1 \\
\sum_{n=1}^{\infty} n x^{n-1} &= \frac{1}{(1-x)^2}, \quad |x| < 1 \\
\sum_{n=1}^{\infty} \frac{x^n}{n} &= -\ln(1-x), \quad -1 \leqslant x < 1
\end{aligned}$$

## 核心策略

### 先导后积

当 $(an+b)^c$ 在**分母**上时，先求导消去分母，再积分还原：

$$S(x) = S(x_0) + \int_{x_0}^x S'(t)\,\mathrm{d}t$$

### 先积后导

当 $(an+b)^c$ 在**分子**上时，先积分消去分子，再求导还原：

$$\left[ \int S(x)\,\mathrm{d}x \right]' = S(x)$$

### 微分方程法

对于抽象系数的幂级数，利用递推关系建立 $S(x)$ 的微分方程求解。

## 重要展开式（反向使用可求和函数）

$$\begin{aligned}
\mathrm{e}^x &= \sum_{n=0}^{\infty} \frac{x^n}{n!} \\
\frac{1}{1-x} &= \sum_{n=0}^{\infty} x^n \\
\sin x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} \\
\ln(1+x) &= \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n}
\end{aligned}$$

> [!TIP]
> 求和函数两步走：① 求收敛域；② 根据系数特征选择先导后积或先积后导。

## 相关页面

- [[03_Wiki/Concepts/幂级数-PowerSeries|幂级数]]
- [[03_Wiki/Methods/幂级数收敛域求法-PowerSeriesConvergence|幂级数收敛域求法]]
- [[03_Wiki/Methods/函数展开成幂级数-FunctionExpansionIntoPowerSeries|函数展开成幂级数]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "幂级数")
SORT 类型 ASC
```
