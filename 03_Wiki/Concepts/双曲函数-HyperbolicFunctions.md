---
标题: 双曲函数
标签: [数学, 附录, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 双曲函数（双曲正弦、双曲余弦、双曲正切）的定义、基本恒等式、倍角公式、反双曲函数及其与对数函数的联系。
来源: 01_Raw/Archive/Lectures/23_附录5_从指数函数到双曲函数.md
可信状态: S3 待核查
---

## 从指数函数出发

指数函数 $y = \mathrm{e}^x$ 满足 $\dfrac{\mathrm{d}y}{\mathrm{d}t} = ky$，是描述自然增长与衰减的基本函数。

自然对数 $\ln x = \log_{\mathrm{e}} x$，与常用对数的换算：
$$\ln x = \ln 10 \cdot \lg x \quad (\ln 10 \approx 2.302585)$$
$$\lg x = \lg \mathrm{e} \cdot \ln x \quad (\lg \mathrm{e} \approx 0.434294)$$

## 双曲函数的定义

双曲函数是由指数函数 $\mathrm{e}^x$ 与 $\mathrm{e}^{-x}$ 构成的初等函数：

| 名称 | 表达式 |
|------|--------|
| 双曲正弦 | $\displaystyle \operatorname{sh} x = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2}$ |
| 双曲余弦 | $\displaystyle \operatorname{ch} x = \frac{\mathrm{e}^x + \mathrm{e}^{-x}}{2}$ |
| 双曲正切 | $\displaystyle \operatorname{th} x = \frac{\operatorname{sh} x}{\operatorname{ch} x} = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{\mathrm{e}^x + \mathrm{e}^{-x}}$ |

### 奇偶性

$$\begin{aligned}
\operatorname{sh}(-x) &= -\operatorname{sh} x \quad &\text{[奇函数]} \\
\operatorname{ch}(-x) &= \operatorname{ch} x \quad &\text{[偶函数]} \\
\operatorname{th}(-x) &= -\operatorname{th} x \quad &\text{[奇函数]}
\end{aligned}$$

## 基本恒等式

由定义直接可得：
$$\mathrm{e}^x = \operatorname{ch} x + \operatorname{sh} x, \qquad \mathrm{e}^{-x} = \operatorname{ch} x - \operatorname{sh} x$$

### 和差公式

$$\begin{aligned}
\operatorname{sh}(u \pm v) &= \operatorname{sh} u \operatorname{ch} v \pm \operatorname{ch} u \operatorname{sh} v, \tag{5-1}\\[4pt]
\operatorname{ch}(u \pm v) &= \operatorname{ch} u \operatorname{ch} v \pm \operatorname{sh} u \operatorname{sh} v. \tag{5-2}
\end{aligned}$$

### 基本恒等式

$$\operatorname{ch}^2 u - \operatorname{sh}^2 u = 1. \tag{5-3}$$

由 (5-3) 式可得：
$$1 - \operatorname{th}^2 u = \frac{1}{\operatorname{ch}^2 u}. \tag{5-4}$$

### 倍角公式

$$\begin{aligned}
\operatorname{sh} 2u &= 2\operatorname{sh} u \operatorname{ch} u, \tag{5-5}\\[4pt]
\operatorname{ch} 2u &= \operatorname{ch}^2 u + \operatorname{sh}^2 u = 2\operatorname{ch}^2 u - 1. \tag{5-6}
\end{aligned}$$

## 反双曲函数

反双曲函数是双曲函数的反函数，与对数函数有密切联系：

| 反函数 | 对数表达式 | 定义域 |
|--------|-----------|--------|
| $\operatorname{arsh} x$ | $\ln(x + \sqrt{x^2 + 1})$ | $(-\infty, +\infty)$ |
| $\operatorname{arch} x$ | $\ln(x + \sqrt{x^2 - 1})$ | $[1, +\infty)$ |
| $\operatorname{arth} x$ | $\dfrac{1}{2}\ln\dfrac{1 + x}{1 - x}$ | $(-1, 1)$ |

### 推导要点（以 $\operatorname{arsh} x$ 为例）

由 $x = \operatorname{sh} y = \dfrac{\mathrm{e}^y - \mathrm{e}^{-y}}{2}$，两边乘以 $2\mathrm{e}^y$ 得：
$$(\mathrm{e}^y)^2 - 2x\mathrm{e}^y - 1 = 0$$
解关于 $\mathrm{e}^y$ 的二次方程并取正根：
$$\mathrm{e}^y = x + \sqrt{x^2 + 1} \;\Longrightarrow\; y = \ln(x + \sqrt{x^2 + 1})$$

注意 $\operatorname{arch} x$ 是双值函数，通常取主值 $\operatorname{arch} x = \ln(x + \sqrt{x^2 - 1})$.

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `01_Raw/23_附录5_从指数函数到双曲函数.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE 标签 AS 标签, 可信状态 AS 状态
FROM "03_Wiki"
WHERE contains(标签, "双曲函数") OR contains(标签, "指数函数")
SORT file.name ASC
```
