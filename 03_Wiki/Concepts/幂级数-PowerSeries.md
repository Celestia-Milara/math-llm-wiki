---
标题: 幂级数
标签: [数学, 第16讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 通项为幂函数的函数项级数，是函数展开与求和的核心工具，具有收敛半径、收敛域等关键特征。
来源: 01_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

若 $\sum u_n(x)$ 的一般项 $u_n(x)$ 是 $x$ 的 $n$ 次幂函数，即 $u_n(x) = a_n x^n$ 或 $u_n(x) = a_n (x - x_0)^n$，则称为**幂级数**。标准形式为：

$$\sum_{n=0}^{\infty} a_n (x - x_0)^n = a_0 + a_1(x - x_0) + a_2(x - x_0)^2 + \cdots + a_n(x - x_0)^n + \cdots$$

## 收敛半径与收敛域

### 收敛半径

存在 $R \geqslant 0$ 使得：
- 当 $|x| < R$ 时，幂级数绝对收敛；
- 当 $|x| > R$ 时，幂级数发散。

$R$ 称为**收敛半径**。计算公式：

$$R = \begin{cases}
\displaystyle \frac{1}{\rho}, & \rho \neq 0, \rho \neq +\infty \\[10pt]
+\infty, & \rho = 0 \\[10pt]
0, & \rho = +\infty
\end{cases}$$

其中 $\rho = \displaystyle\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$ 或 $\rho = \displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|}$。

### 收敛域

收敛区间 $(-R, R)$ 加上端点处的敛散性确定收敛域。

## 泰勒级数与麦克劳林级数

若 $f(x)$ 在 $x_0$ 处任意阶可导，则其泰勒级数为：

$$f(x) \sim \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n$$

当 $x_0 = 0$ 时称为**麦克劳林级数**。

## 重要展开式

$$\begin{aligned}
\mathrm{e}^x &= \sum_{n=0}^{\infty} \frac{x^n}{n!}, \quad -\infty < x < +\infty \\
\frac{1}{1-x} &= \sum_{n=0}^{\infty} x^n, \quad -1 < x < 1 \\
\sin x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}, \quad -\infty < x < +\infty \\
\cos x &= \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}, \quad -\infty < x < +\infty \\
\ln(1+x) &= \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n}, \quad -1 < x \leqslant 1
\end{aligned}$$

## 相关页面

- [[NumericalSeries|常数项级数]]
- [[阿贝尔定理-AbelsTheorem|阿贝尔定理]]
- [[PowerSeriesConvergence|幂级数收敛域求法]]
- [[PowerSeriesSumFunction|幂级数求和函数]]
- [[FunctionExpansionIntoPowerSeries|函数展开成幂级数]]

---

```dataview
TABLE title, 掌握状态, 摘要
FROM "03_Wiki"
WHERE contains(标签, "幂级数") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
