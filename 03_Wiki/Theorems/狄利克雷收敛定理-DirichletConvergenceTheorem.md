---
标题: 狄利克雷收敛定理
标签: [数学, 第16讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 给出傅里叶级数收敛的充分条件，并确定和函数在连续点与间断点的取值。
来源: 01_Raw/Archive/Lectures/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。
## 定理陈述


## 狄利克雷收敛定理

设 $f(x)$ 是以 $2l$ 为周期的可积函数，如果在 $[-l, l]$ 上 $f(x)$ 满足：
1. 连续或只有有限个第一类间断点；
2. 至多只有有限个极值点。

则 $f(x)$ 的傅里叶级数在 $[-l, l]$ 上处处收敛。和函数 $S(x)$ 为：

$$S(x) = \begin{cases}
f(x), & x \text{为连续点} \\[6pt]
\displaystyle \frac{f(x-0) + f(x+0)}{2}, & x \text{为间断点} \\[10pt]
\displaystyle \frac{f(-l+0) + f(l-0)}{2}, & x = \pm l
\end{cases}$$

## 要点

- 傅里叶级数用 $\sim$ 连接而非等号，因为 $S(x)$ 与 $f(x)$ 不一定相等。
- 在连续点处 $S(x) = f(x)$。
- 在第一类间断点处，$S(x)$ 收敛于左右极限的平均值。

## 相关页面

- [[FourierSeries|傅里叶级数]]
- [[FourierSeriesExpansion|傅里叶级数展开方法]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, "傅里叶") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
