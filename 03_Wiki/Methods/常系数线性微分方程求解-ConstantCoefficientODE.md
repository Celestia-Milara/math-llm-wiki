---
标题: 常系数线性微分方程求解
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过特征方程求解常系数齐次线性微分方程，再用待定系数法或微分算子法求解非齐次方程。
来源: 01_Raw/Archive/Lectures/15_第15讲_微分方程.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 二阶常系数齐次线性微分方程

方程 $y'' + py' + qy = 0$，对应的特征方程为 $r^2 + pr + q = 0$。

$$\begin{aligned}
\Delta > 0 &: \quad y = C_1\mathrm{e}^{r_1 x} + C_2\mathrm{e}^{r_2 x} \quad &\text{[两个不等实根]} \\
\Delta = 0 &: \quad y = (C_1 + C_2 x)\mathrm{e}^{r x} \quad &\text{[二重实根]} \\
\Delta < 0 &: \quad y = \mathrm{e}^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x) \quad &\text{[共轭复根 } \alpha \pm \beta\mathrm{i}]
\end{aligned}$$

## 二阶常系数非齐次线性微分方程

方程 $y'' + py' + qy = f(x)$，通解 = 齐次通解 + 非齐次特解。

### 情形一：$f(x) = P_n(x)\mathrm{e}^{\alpha x}$

设特解 $y^* = \mathrm{e}^{\alpha x} Q_n(x) \cdot x^k$，其中

$$k = \begin{cases}
0, & \alpha \text{ 不是特征根} \\
1, & \alpha \text{ 是单特征根} \\
2, & \alpha \text{ 是二重特征根}
\end{cases}$$

### 情形二：$f(x) = \mathrm{e}^{\alpha x}[P_m(x)\cos\beta x + P_n(x)\sin\beta x]$

设特解 $y^* = \mathrm{e}^{\alpha x}[Q_l^{(1)}(x)\cos\beta x + Q_l^{(2)}(x)\sin\beta x] \cdot x^k$，其中

$$l = \max\{m, n\}, \quad k = \begin{cases}
0, & \alpha \pm \beta\mathrm{i} \text{ 不是特征根} \\
1, & \alpha \pm \beta\mathrm{i} \text{ 是特征根}
\end{cases}$$

### 总结：一看（自由项形式），二算（特征根），三比较（$\alpha$ 与特征根的关系）

## 高阶常系数齐次线性微分方程

- 单实根 $r$：对应 $C\mathrm{e}^{rx}$
- $k$ 重复根 $r$：对应 $(C_1 + C_2 x + \cdots + C_k x^{k-1})\mathrm{e}^{rx}$
- 单复根 $\alpha \pm \beta\mathrm{i}$：对应 $\mathrm{e}^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$
- 二重复根 $\alpha \pm \beta\mathrm{i}$：对应 $\mathrm{e}^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x + C_3 x\cos\beta x + C_4 x\sin\beta x)$

## 相关页面

- [[03_Wiki/Concepts/线性微分方程-LinearDifferentialEquation|线性微分方程]]
- [[线性微分方程解的结构-StructureOfLinearODESolutions|线性微分方程解的结构]]
- [[03_Wiki/Methods/微分算子法-DifferentialOperatorMethod|微分算子法]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "常系数")
SORT 类型 ASC
```
