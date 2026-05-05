---
标题: 级数的基本性质
标签: [数学, 第16讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 收敛级数满足线性运算、加括号不变和、改变有限项不影响敛散性等基本性质。
来源: 00_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 性质

### 性质1（线性性质）

若 $\sum u_n, \sum v_n$ 均收敛，则对任意常数 $a, b$：

$$\sum_{n=1}^{\infty} (a u_n \pm b v_n) = a \sum_{n=1}^{\infty} u_n \pm b \sum_{n=1}^{\infty} v_n$$

> 收敛 $\pm$ 发散 $=$ 发散；发散 $\pm$ 发散 $=$ 不一定。

### 性质2（有限项无关性）

改变级数的任意有限项，不会改变该级数的敛散性。

### 性质3（加括号）

收敛级数的项任意加括号后所得的新级数仍收敛，且和不变。

> 若加括号后发散，则原级数必发散；但加括号后收敛不能推出原级数收敛。

### 性质4（必要条件）

若 $\sum u_n$ 收敛，则 $\displaystyle\lim_{n \to \infty} u_n = 0$。

逆否命题：若 $\displaystyle\lim_{n \to \infty} u_n \neq 0$，则 $\sum u_n$ 必发散。
> 注意：$\displaystyle\lim_{n \to \infty} u_n = 0$ 是级数收敛的**必要不充分**条件。

## 相关页面

- [[NumericalSeries|常数项级数]]
- [[ConvergenceTestsForPositiveSeries|正项级数审敛法]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "级数")
SORT type ASC
```
