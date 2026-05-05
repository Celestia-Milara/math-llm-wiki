---
标题: 重要公式汇总
标签: [数学, 附录, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 三角函数公式（诱导、倍角、半角、和差、积化和差、万能）、一元二次方程、因式分解、二项式定理、阶乘与双阶乘公式汇总。
来源: 00_Raw/22_附录4_重要公式.md
---

## 1 三角函数公式

### 1.1 诱导公式

口诀：**奇变偶不变，符号看象限**。

$$\begin{cases}
\sin\left(\dfrac{\pi}{2} \pm \alpha\right) = \cos\alpha, \\[6pt]
\sin(\pi \pm \alpha) = \mp \sin\alpha, \\[6pt]
\cos\left(\dfrac{\pi}{2} \pm \alpha\right) = \mp \sin\alpha, \\[6pt]
\cos(\pi \pm \alpha) = -\cos\alpha
\end{cases}$$

### 1.2 倍角公式

$$\begin{aligned}
\sin 2\alpha &= 2\sin\alpha\cos\alpha, \\[4pt]
\cos 2\alpha &= \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1, \\[4pt]
\sin 3\alpha &= -4\sin^3\alpha + 3\sin\alpha, \\[4pt]
\cos 3\alpha &= 4\cos^3\alpha - 3\cos\alpha, \\[4pt]
\tan 2\alpha &= \frac{2\tan\alpha}{1 - \tan^2\alpha}, \\[4pt]
\cot 2\alpha &= \frac{\cot^2\alpha - 1}{2\cot\alpha}
\end{aligned}$$

### 1.3 半角公式（降幂公式）

$$\begin{aligned}
\sin^2\frac{\alpha}{2} &= \frac{1}{2}(1 - \cos\alpha), \\[4pt]
\cos^2\frac{\alpha}{2} &= \frac{1}{2}(1 + \cos\alpha), \\[4pt]
\sin\frac{\alpha}{2} &= \pm\sqrt{\frac{1 - \cos\alpha}{2}}, \\[4pt]
\cos\frac{\alpha}{2} &= \pm\sqrt{\frac{1 + \cos\alpha}{2}}, \\[4pt]
\tan\frac{\alpha}{2} &= \frac{1 - \cos\alpha}{\sin\alpha} = \frac{\sin\alpha}{1 + \cos\alpha} = \pm\sqrt{\frac{1 - \cos\alpha}{1 + \cos\alpha}}, \\[4pt]
\cot\frac{\alpha}{2} &= \frac{\sin\alpha}{1 - \cos\alpha} = \frac{1 + \cos\alpha}{\sin\alpha} = \pm\sqrt{\frac{1 + \cos\alpha}{1 - \cos\alpha}}
\end{aligned}$$

### 1.4 和差公式

$$\begin{aligned}
\sin(\alpha \pm \beta) &= \sin\alpha\cos\beta \pm \cos\alpha\sin\beta, \\[4pt]
\cos(\alpha \pm \beta) &= \cos\alpha\cos\beta \mp \sin\alpha\sin\beta, \\[4pt]
\tan(\alpha \pm \beta) &= \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}, \\[4pt]
\cot(\alpha \pm \beta) &= \frac{\cot\alpha\cot\beta \mp 1}{\cot\beta \pm \cot\alpha}
\end{aligned}$$

### 1.5 积化和差与和差化积

**积化和差**：
$$\begin{aligned}
\sin\alpha\cos\beta &= \frac{1}{2}[\sin(\alpha+\beta) + \sin(\alpha-\beta)], \\[4pt]
\cos\alpha\sin\beta &= \frac{1}{2}[\sin(\alpha+\beta) - \sin(\alpha-\beta)], \\[4pt]
\cos\alpha\cos\beta &= \frac{1}{2}[\cos(\alpha+\beta) + \cos(\alpha-\beta)], \\[4pt]
\sin\alpha\sin\beta &= \frac{1}{2}[\cos(\alpha-\beta) - \cos(\alpha+\beta)]
\end{aligned}$$

**和差化积**：
$$\begin{aligned}
\sin\alpha + \sin\beta &= 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}, \\[4pt]
\sin\alpha - \sin\beta &= 2\sin\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}, \\[4pt]
\cos\alpha + \cos\beta &= 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}, \\[4pt]
\cos\alpha - \cos\beta &= -2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}
\end{aligned}$$

### 1.6 万能公式

设 $u = \tan\dfrac{x}{2}\;(-\pi < x < \pi)$，则
$$\sin x = \frac{2u}{1 + u^2},\qquad \cos x = \frac{1 - u^2}{1 + u^2}$$

### 1.7 常用变形

$$\tan\left(\frac{\pi}{4} - \alpha\right) = \frac{1 - \tan\alpha}{1 + \tan\alpha}$$

## 2 一元二次方程

标准形式 $ax^2 + bx + c = 0\;(a \neq 0)$：

- **判别式**：$\Delta = b^2 - 4ac$
- $\Delta \geqslant 0$：实根 $x_{1,2} = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- $\Delta < 0$：共轭复根 $x_{1,2} = \dfrac{-b \pm \sqrt{4ac - b^2}\,i}{2a}$
- **韦达定理**：$x_1 + x_2 = -\dfrac{b}{a},\quad x_1x_2 = \dfrac{c}{a}$

## 3 因式分解公式

$$\begin{aligned}
(a + b)^2 &= a^2 + 2ab + b^2 \\[4pt]
(a - b)^2 &= a^2 - 2ab + b^2 \\[4pt]
(a + b)^3 &= a^3 + 3a^2b + 3ab^2 + b^3 \\[4pt]
(a - b)^3 &= a^3 - 3a^2b + 3ab^2 - b^3 \\[4pt]
a^2 - b^2 &= (a + b)(a - b) \\[4pt]
a^3 - b^3 &= (a - b)(a^2 + ab + b^2) \\[4pt]
a^3 + b^3 &= (a + b)(a^2 - ab + b^2) \\[4pt]
a^n - b^n &= (a - b)(a^{n-1} + a^{n-2}b + \dots + ab^{n-2} + b^{n-1}) \quad (n \in \mathbb{N}^+) \\[4pt]
a^n + b^n &= (a + b)(a^{n-1} - a^{n-2}b + \dots - ab^{n-2} + b^{n-1}) \quad (n \text{为正奇数})
\end{aligned}$$

## 4 二项式定理

$$(a + b)^n = \sum_{k=0}^{n} C_n^k a^{n-k} b^k = a^n + n a^{n-1}b + \frac{n(n-1)}{2!}a^{n-2}b^2 + \dots + n a b^{n-1} + b^n$$

## 5 阶乘与双阶乘

- $n! = 1 \cdot 2 \cdot 3 \cdots n$，规定 $0! = 1$
- $(2n)!! = 2 \cdot 4 \cdot 6 \cdots (2n) = 2^n \cdot n!$
- $(2n - 1)!! = 1 \cdot 3 \cdot 5 \cdots (2n - 1)$

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `00_Raw/22_附录4_重要公式.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE tags AS 标签, status AS 状态
FROM "01_Wiki"
WHERE contains(tags, "公式") OR contains(tags, "三角函数")
SORT file.name ASC
```
