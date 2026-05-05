---
标题: 变形技巧
标签: [数学, 附录, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 数学解题中的等式变形与不等式变形技巧，涵盖定义法、公式法、换元法、相消法、同除法、倒置法、平方开方法、共轭法等核心方法。
来源: 00_Raw/24_附录6_变形技巧.md
---

## 第一部分：等式变形与等价变形

### (1) 定义法

回归定义是最基本的变形方法。例如由极限定义处理极限问题，由导数定义处理可导性问题。

**例**：由 $\lim_{x\to x_0}\dfrac{f(x)}{x - x_0} = a$ 且 $f(x)$ 在 $x_0$ 处连续，可得 $f(x_0) = 0$，$f'(x_0) = a$。

### (2) 公式法

注意公式的**独特性**（指引解题方向）和**成立条件**（限定使用场景）。例如泰勒展开式：
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2}x^2 + \dots$$
其独特性在于用各阶导数值近似表示函数值。

### (3) 换元法

引入新元代换旧元，使问题简化。

- **复杂部分代换**：令 $t = \ln\left(1 + \sqrt{\frac{1+x}{x}}\right)$
- **平移换元**：$x \to 1$ 时令 $t = x - 1$，则 $t \to 0$
- **消元换元**：
  - $x_1 > x_2$ 时令 $x_1 = x_2 + t\;(t > 0)$
  - $x_1 > x_2 > 0$ 时令 $x_1 = tx_2\;(t > 1)$
  - **零和换元**：$x_1 + x_2 = a$ 时令 $x_1 = \dfrac{a}{2} + t,\; x_2 = \dfrac{a}{2} - t$
  - $x + y + z = 1$ 时令 $x = \frac{1}{3} + t_1,\; y = \frac{1}{3} + t_2,\; z = \frac{1}{3} - t_1 - t_2$
- **商抵换元**：$x_1x_2 = a^2$ 时令 $x_1 = ta,\; x_2 = \dfrac{a}{t}$

### (4) 相消法

**加减相消（裂项）**：
$$\frac{1}{n(n+k)} = \frac{1}{k}\left(\frac{1}{n} - \frac{1}{n+k}\right)$$
$$\frac{1}{(2n+1)(2n-1)} = \frac{1}{2}\left(\frac{1}{2n-1} - \frac{1}{2n+1}\right)$$
$$\frac{1}{\sqrt{n+1} + \sqrt{n}} = \sqrt{n+1} - \sqrt{n}$$

**乘除相消**：创造 $\dfrac{a_n}{a_{n-1}} = f(n)$，则 $a_n = \dfrac{a_n}{a_{n-1}} \cdot \dfrac{a_{n-1}}{a_{n-2}} \cdots \dfrac{a_2}{a_1} \cdot a_1$

**错位相消**（等比数列求和）：
$$S_n = a + aq + aq^2 + \dots + aq^{n-1}$$
$$qS_n = aq + aq^2 + \dots + aq^n$$
相减得 $(1 - q)S_n = a - aq^n$，故 $S_n = \dfrac{a(1 - q^n)}{1 - q}\;(q \neq 1)$

### (5) 同除法 / 解方程法

**型如 $a_{n+1} = ka_n + f(n)$**：
$$\frac{a_{n+1}}{k^{n+1}} = \frac{a_n}{k^n} + \frac{f(n)}{k^{n+1}}$$
化为 $\left\{\dfrac{a_n}{k^n}\right\}$ 的等差数列形式。

**型如 $a_{n+1} + Aa_n + Ba_{n-1} = 0$**：
特征方程 $\lambda^2 + A\lambda + B = 0$，若 $\Delta > 0$ 有 $a_n = C_1\lambda_1^n + C_2\lambda_2^n$；若 $\Delta = 0$ 有 $a_n = (C_1 + C_2n)\left(-\dfrac{A}{2}\right)^n$。

### (6) 倒置法

取倒数改变结构，适用于分母复杂、分子简单的情形：
$$a_{n+1} = \frac{a_n}{a_n + 2} \;\Longrightarrow\; \frac{1}{a_{n+1}} = 1 + \frac{2}{a_n}$$

### (7) 平方开方法

配成 $a^2$ 或 $a^2 + b^2$ 形式：
$$x^2 + \frac{1}{x^2} = \left(x + \frac{1}{x}\right)^2 - 2 = \left(x - \frac{1}{x}\right)^2 + 2$$
$$\mathrm{e}^{2x} + \mathrm{e}^{-2x} = (\mathrm{e}^x + \mathrm{e}^{-x})^2 - 2 = (\mathrm{e}^x - \mathrm{e}^{-x})^2 + 2$$

**平方和关系**：
$$a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ac)$$
$$a^2 + b^2 + c^2 + ab + bc + ac = \frac{1}{2}[(a+b)^2 + (b+c)^2 + (a+c)^2]$$

### (8) 特殊值法

令 $x = x_0$ 使表达式与条件建立联系。例如对三次多项式 $f(x) = ax^3 + bx^2 + cx + d$：
$$a + b + c + d = f(1),\; a - b + c - d = -f(-1)$$
$$a + c = \frac{1}{2}[f(1) - f(-1)],\; b + d = \frac{1}{2}[f(1) + f(-1)]$$

### (9) 因式分解法

$$a^2 + ab + b^2 = \frac{a^3 - b^3}{a - b},\qquad a^2 - ab + b^2 = \frac{a^3 + b^3}{a + b}$$

### (10) 整数幂和法

$$1^k + 2^k + \dots + n^k = \frac{1}{k+1}n^{k+1} + R_k$$
例如 $1^2 + 2^2 + \dots + n^2 = \frac{1}{3}n^3 + R_2$，常用于放缩法中。

### (11) 三角公式法

**辅助角公式**：
$$a\sin x + b\cos x = \sqrt{a^2 + b^2}\sin(x + \varphi)$$
其中 $\varphi$ 为向量 $(a,b)$ 的方向角。

### (12) 共轭法

利用共轭式的运算简化问题：

- **根式共轭**：$\sqrt{a} - \sqrt{b}$ 与 $\sqrt{a} + \sqrt{b}$，乘积为 $a - b$
- **三角共轭**：$\sin x$ 与 $\cos x$（平方和为 $1$）
- **线性组合共轭**：$a\sin x + b\cos x$ 与 $b\sin x - a\cos x$（平方和为 $a^2 + b^2$）
- **余弦乘积共轭**：$\cos ax\cos bx$ 与 $\sin ax\sin bx$（和差化积的出发点）

### 其他常用变形

- $a = a + b - b$（加项减项）
- $a = \dfrac{a}{b} \cdot b$（除项乘项）
- $1 = a \cdot \dfrac{1}{a} = \sin^2 x + \cos^2 x = a^0$（1 的转化）
- $a^b = c^d \Rightarrow b\ln a = d\ln c$（取对数法）
- $\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$

## 第二部分：不等式变形

### (1) 抽象型基本不等关系

$$\begin{aligned}
\frac{2}{\frac{1}{a} + \frac{1}{b}} &\leq \sqrt{ab} \leq \frac{a + b}{2} \leq \sqrt{\frac{a^2 + b^2}{2}} \quad (a,b > 0) \\[6pt]
|ab| &\leq \frac{a^2 + b^2}{2} \\[6pt]
a^2 + b^2 &\geq 2ab \\[6pt]
4ab &\leq (a + b)^2 \leq 2(a^2 + b^2) \\[6pt]
\frac{1}{a} + \frac{1}{b} &\geq \frac{4}{a + b}\quad (a,b > 0) \\[6pt]
\frac{a + b + c}{3} &\geq \sqrt[3]{abc}\quad (a,b,c > 0) \\[6pt]
a + \frac{1}{a} &\geq 2 \quad (a > 0)
\end{aligned}$$

**柯西不等式**：
$$(a_1b_1 + a_2b_2)^2 \leqslant (a_1^2 + a_2^2)(b_1^2 + b_2^2)$$
积分形式：
$$\left[\int_a^b f(x)g(x)\,\mathrm{d}x\right]^2 \leqslant \int_a^b f^2(x)\,\mathrm{d}x \cdot \int_a^b g^2(x)\,\mathrm{d}x$$

### (2) 初等函数不等关系

$$\begin{aligned}
\mathrm{e}^x &\geqslant x + 1 \\[4pt]
1 - \frac{1}{x} &\leqslant \ln x \leqslant x - 1 \\[4pt]
\sin x &< x < \tan x \quad \left(0 < x < \frac{\pi}{2}\right) \\[4pt]
\left(1 + \frac{1}{x}\right)^x &< \mathrm{e} \quad (x > 0) \\[4pt]
x\ln x &\geqslant -\frac{1}{\mathrm{e}} \quad (x > 0)
\end{aligned}$$

### (3) 函数性态中的不等关系

- **极限保号性**：若 $\lim x_n = a \neq 0$，则当 $n$ 足够大时 $|x_n| > \dfrac{|a|}{2}$
- **单调性**：$f$ 单调递增 $\Rightarrow (x - x_0)[f(x) - f(x_0)] \geqslant 0$
- **凹凸性**：$f''(x) > 0 \Rightarrow f(x) \leqslant f(a) + \dfrac{f(b) - f(a)}{b - a}(x - a)$
- **积分不等式**：$\displaystyle\left|\int_a^b f(x)\,\mathrm{d}x\right| \leqslant \int_a^b |f(x)|\,\mathrm{d}x$

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `00_Raw/24_附录6_变形技巧.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE tags AS 标签, status AS 状态
FROM "01_Wiki"
WHERE contains(tags, "变形") OR contains(tags, "方法")
SORT file.name ASC
```
