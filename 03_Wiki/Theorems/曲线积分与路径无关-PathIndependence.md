---
标题: 曲线积分与路径无关的条件
标签: [数学, 第18讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 在单连通区域中，曲线积分与路径无关等价于旋度为零，也等价于存在势函数（全微分）。
来源: 01_Raw/18_第18讲_多元函数积分学.md
---

## 定理陈述

设 $P(x, y), Q(x, y)$ 在单连通区域 $G$ 内具有一阶连续偏导数，则曲线积分 $\int_L P \, \mathrm{d}x + Q \, \mathrm{d}y$ 在 $G$ 内**与路径无关**的充分必要条件是：
$$
\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} \quad \text{在 } G \text{ 内处处成立}.
$$

## 六个等价命题

在单连通区域 $D$ 内，$P, Q$ 一阶偏导连续，以下命题等价：

1. $\displaystyle \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$ 在 $D$ 内处处成立
2. 沿 $D$ 内任意闭曲线 $L$ 有 $\displaystyle \oint_L P \, \mathrm{d}x + Q \, \mathrm{d}y = 0$
3. $\displaystyle \int_{L_1} P \, \mathrm{d}x + Q \, \mathrm{d}y = \int_{L_2} P \, \mathrm{d}x + Q \, \mathrm{d}y$（与路径无关）
4. $\mathrm{d}u = P \, \mathrm{d}x + Q \, \mathrm{d}y$（$P \, \mathrm{d}x + Q \, \mathrm{d}y$ 是某二元函数 $u(x, y)$ 的全微分）
5. $P \, \mathrm{d}x + Q \, \mathrm{d}y = 0$ 是全微分方程
6. $(P, Q)$ 是某二元函数 $u$ 的梯度

## 原函数的求法（折线法）

若 $\dfrac{\partial Q}{\partial x} = \dfrac{\partial P}{\partial y}$，则
$$
u(x, y) = \int_{x_0}^x P(x, y_0) \, \mathrm{d}x + \int_{y_0}^y Q(x, y) \, \mathrm{d}y,
$$
或
$$
u(x, y) = \int_{x_0}^x P(x, y) \, \mathrm{d}x + \int_{y_0}^y Q(x_0, y) \, \mathrm{d}y.
$$

进而 $\displaystyle \int_{(x_0, y_0)}^{(x, y)} P \, \mathrm{d}x + Q \, \mathrm{d}y = u(x, y) - u(x_0, y_0)$.

> **单连通区域**：不含"洞"的区域。含洞的区域称为复连通区域。

## 相关页面

- [[第二型曲线积分计算方法-LineIntegralSecondKindMethods]]
- [[格林公式-GreensTheorem]]
- [[方向导数与梯度-DirectionalDerivativeAndGradient]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "曲线积分")
SORT file.name
```
