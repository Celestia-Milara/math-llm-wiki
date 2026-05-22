---
标题: 广义积分比较判别法
标签: [数学, 第8讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 通过比较函数的大小或极限来判别广义积分的敛散性。
来源: 01_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。
## 定理陈述


## 无穷区间的比较判别法

设 $f(x),g(x)$ 在 $[a,+\infty)$ 上连续，且 $0 \le f(x) \le g(x)$，则：

1. 若 $\int_a^{+\infty} g(x)\,\mathrm{d}x$ 收敛，则 $\int_a^{+\infty} f(x)\,\mathrm{d}x$ 收敛
2. 若 $\int_a^{+\infty} f(x)\,\mathrm{d}x$ 发散，则 $\int_a^{+\infty} g(x)\,\mathrm{d}x$ 发散

### 极限形式

设 $\displaystyle\lim_{x\to +\infty} \frac{f(x)}{g(x)} = \lambda$（有限或 $\infty$），则：

- $\lambda \neq 0,\infty$：两者同敛散
- $\lambda = 0$：$\int g$ 收敛 $\Rightarrow$ $\int f$ 收敛
- $\lambda = \infty$：$\int g$ 发散 $\Rightarrow$ $\int f$ 发散

## 无界函数的比较判别法

设 $f(x),g(x)$ 在 $(a,b]$ 上连续，瑕点同为 $x=a$，且 $0 \le f(x) \le g(x)$，则：

1. 若 $\int_a^b g(x)\,\mathrm{d}x$ 收敛，则 $\int_a^b f(x)\,\mathrm{d}x$ 收敛
2. 若 $\int_a^b f(x)\,\mathrm{d}x$ 发散，则 $\int_a^b g(x)\,\mathrm{d}x$ 发散

### 极限形式（瑕点 $x=a$）

设 $\displaystyle\lim_{x\to a^+} \frac{f(x)}{g(x)} = \lambda$，结论同无穷区间情形。

## 两个重要参考对象

### 瑕积分（$x=0$ 为瑕点）
$$\int_0^1 \frac{1}{x^p}\,\mathrm{d}x
\begin{cases}
\text{收敛}, & 0 < p < 1, \\
\text{发散}, & p \ge 1.
\end{cases}$$

### 无穷区间
$$\int_1^{+\infty} \frac{1}{x^p}\,\mathrm{d}x
\begin{cases}
\text{收敛}, & p > 1, \\
\text{发散}, & p \le 1.
\end{cases}$$

### 含对数因子
$$\int_1^{+\infty} \frac{\ln x}{x^p}\,\mathrm{d}x
\begin{cases}
\text{收敛}, & p > 1, \\
\text{发散}, & p \le 1.
\end{cases}
\qquad
\int_0^1 \frac{\ln x}{x^p}\,\mathrm{d}x
\begin{cases}
\text{收敛}, & 0 \le p < 1, \\
\text{发散}, & p \ge 1.
\end{cases}$$

---

## Dataview

```dataview
TABLE 
  掌握状态 as "状态",
  source as "来源"
FROM "03_Wiki/Concepts"
WHERE contains(标签, "广义积分")
SORT file.name ASC
```
