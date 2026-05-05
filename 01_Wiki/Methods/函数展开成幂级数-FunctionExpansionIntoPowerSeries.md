---
标题: 函数展开成幂级数
标签: [数学, 第16讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 利用已知展开式通过代换、四则运算、逐项求导/积分将函数间接展开为幂级数。
来源: 00_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 直接法（一般不使用）

计算 $a_n = \dfrac{f^{(n)}(x_0)}{n!}$ 并代入泰勒级数公式，计算量大。

## 间接法（常用）

利用已知展开式，通过以下手段得到展开式：

1. **变量代换**：如 $\ln(1-x+x^2) = \ln(1+x^3) - \ln(1+x)$
2. **四则运算**
3. **逐项求导**：如 $\arctan x = \int_0^x \dfrac{1}{1+t^2}\,\mathrm{d}t$ 先导后积
4. **逐项积分**
5. **待定系数法**

## 必须熟记的展开式

| 函数 | 展开式 | 收敛域 |
|---|---|---|
| $\mathrm{e}^x$ | $\sum \dfrac{x^n}{n!}$ | $(-\infty, +\infty)$ |
| $\dfrac{1}{1-x}$ | $\sum x^n$ | $(-1, 1)$ |
| $\dfrac{1}{1+x}$ | $\sum (-1)^n x^n$ | $(-1, 1)$ |
| $\ln(1+x)$ | $\sum (-1)^{n-1} \dfrac{x^n}{n}$ | $(-1, 1]$ |
| $\sin x$ | $\sum (-1)^n \dfrac{x^{2n+1}}{(2n+1)!}$ | $(-\infty, +\infty)$ |
| $\cos x$ | $\sum (-1)^n \dfrac{x^{2n}}{(2n)!}$ | $(-\infty, +\infty)$ |
| $\arctan x$ | $\sum (-1)^n \dfrac{x^{2n+1}}{2n+1}$ | $[-1, 1]$ |

## 相关页面

- [[PowerSeries|幂级数]]
- [[PowerSeriesSumFunction|幂级数求和函数]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "展开")
SORT type ASC
```
