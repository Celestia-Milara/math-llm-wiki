---
标题: 正项级数审敛法
标签: [数学, 第16讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 正项级数敛散性判别的六种方法：收敛原则、比较判别法、比值/根值判别法、积分判别法。
来源: 00_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 收敛原则

正项级数 $\sum u_n$ 收敛 $\iff$ 部分和数列 $\{S_n\}$ **有界**。

> 正项级数部分和数列单调不减，故有界则收敛，无界则发散至 $+\infty$。

## 比较判别法

若 $0 \leqslant u_n \leqslant v_n$，则：
- $\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛
- $\sum u_n$ 发散 $\Rightarrow$ $\sum v_n$ 发散

**常用比较对象**：几何级数 $\sum aq^{n}$ 和 $p$ 级数 $\sum \dfrac{1}{n^p}$。

## 比较判别法的极限形式

若 $\displaystyle\lim_{n \to \infty} \frac{u_n}{v_n} = A$，则：

- $A = 0$：$\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛
- $A = +\infty$：$\sum v_n$ 发散 $\Rightarrow$ $\sum u_n$ 发散
- $0 < A < +\infty$：$\sum u_n$ 与 $\sum v_n$ 同敛散

## 比值判别法（达朗贝尔判别法）

若 $\displaystyle\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = \rho$，则：
- $\rho < 1$：收敛
- $\rho > 1$：发散
- $\rho = 1$：失效

## 根值判别法（柯西判别法）

若 $\displaystyle\lim_{n \to \infty} \sqrt[n]{u_n} = \rho$，则：
- $\rho < 1$：收敛
- $\rho > 1$：发散
- $\rho = 1$：失效

## 积分判别法

若存在 $[1, +\infty)$ 上单调减少的非负连续函数 $f(x)$ 使 $u_n = f(n)$，则 $\sum u_n$ 与 $\int_1^{+\infty} f(x)\,\mathrm{d}x$ 同敛散。

## 相关页面

- [[NumericalSeries|常数项级数]]
- [[莱布尼茨判别法-LeibnizTest|莱布尼茨判别法]]
- [[AbsoluteAndConditionalConvergence|绝对收敛与条件收敛]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "级数")
SORT type ASC
```
