---
标题: 幂级数收敛域求法
标签: [数学, 第16讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过比值/根值判别法求收敛半径，再单独讨论端点处的敛散性确定收敛域。
来源: 01_Raw/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 不缺项幂级数 $\sum a_n x^n$

### 收敛半径

$$R = \begin{cases}
\displaystyle \frac{1}{\rho}, & \rho \neq 0, \rho \neq +\infty \\[10pt]
+\infty, & \rho = 0 \\[10pt]
0, & \rho = +\infty
\end{cases}$$

其中 $\rho = \displaystyle\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$ 或 $\rho = \displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|}$。

### 收敛域

收敛区间 $(-R, R)$，再单独判断 $x = \pm R$ 处的敛散性。

## 缺项幂级数或一般函数项级数

对 $\sum |u_n(x)|$ 用比值或根值判别法：

$$\lim_{n \to \infty} \frac{|u_{n+1}(x)|}{|u_n(x)|} < 1 \quad \Rightarrow \quad \text{收敛区间}$$

再单独讨论端点处的敛散性。

## 抽象型幂级数

已知 $\sum a_n(x-x_1)^n$ 的敛散性，讨论 $\sum b_n(x-x_2)^m$ 的敛散性：
- 平移收敛区间
- 提出/乘以因式 $(x-x_0)^k$，收敛半径不变
- 逐项求导/积分，收敛半径不变，但收敛域可能缩小/扩大

## 重要考点

若 $\sum a_n(x-x_0)^n$ 在 $x_1$ 处**条件收敛** $\Rightarrow$ 收敛半径 $R = |x_1 - x_0|$。

## 相关页面

- [[PowerSeries|幂级数]]
- [[阿贝尔定理-AbelsTheorem|阿贝尔定理]]
- [[PowerSeriesSumFunction|幂级数求和函数]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "幂级数")
SORT 类型 ASC
```
