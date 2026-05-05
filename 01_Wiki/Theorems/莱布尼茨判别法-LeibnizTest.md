---
标题: 莱布尼茨判别法
标签: [数学, 第16讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 交错级数的审敛定理：若通项绝对值单调递减且趋于零，则级数收敛。
来源: 00_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 莱布尼茨判别法

设交错级数 $\displaystyle \sum_{n=1}^{\infty} (-1)^{n-1} u_n$，其中 $u_n > 0\;(n=1,2,\dots)$。若同时满足：

1. $\{u_n\}$ **单调不增**（即 $u_{n+1} \leqslant u_n$）；
2. $\displaystyle\lim_{n \to \infty} u_n = 0$。

则该交错级数**收敛**。

> [!WARNING]
> 莱布尼茨判别法只是**充分条件**，不是必要条件。不满足单调性时级数仍可能收敛。

## 单调性判别方法

- 比较 $u_{n+1} - u_n$ 与 0 的大小，或 $\dfrac{u_{n+1}}{u_n}$ 与 1 的大小。
- 若 $u_n = f(n)$ 且 $f$ 可导，通过 $f'(x)$ 的正负判断单调性。

## 相关页面

- [[NumericalSeries|常数项级数]]
- [[AbsoluteAndConditionalConvergence|绝对收敛与条件收敛]]
- [[级数的基本性质-BasicPropertiesOfSeries|级数的基本性质]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "级数")
SORT type ASC
```
