---
标题: 空间曲线的切线与法平面
标签: [数学, 第17讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 通过参数方程或方程组求空间曲线在某点的切向量，进而得到切线方程和法平面方程。
来源: 00_Raw/17_第17讲_多元函数积分学的预备知识
---

## 参数方程情形

曲线 $\Gamma: \begin{cases} x = x(t), \\ y = y(t), \\ z = z(t) \end{cases}$，$t \in I$，$x(t), y(t), z(t)$ 可导且不同时为 0。

在 $P_0(x_0, y_0, z_0)$ 处（对应 $t = t_0$）：
- **切向量**：$\boldsymbol{\tau} = (x'(t_0), y'(t_0), z'(t_0))$
- **切线方程**：$\dfrac{x - x_0}{x'(t_0)} = \dfrac{y - y_0}{y'(t_0)} = \dfrac{z - z_0}{z'(t_0)}$
- **法平面方程**：$x'(t_0)(x - x_0) + y'(t_0)(y - y_0) + z'(t_0)(z - z_0) = 0$

## 一般式（方程组）情形

曲线 $\Gamma: \begin{cases} F(x, y, z) = 0, \\ G(x, y, z) = 0. \end{cases}$

在 $P_0$ 处的切向量为两个梯度向量的叉乘：
$$
\boldsymbol{\tau} = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
F_x' & F_y' & F_z' \\
G_x' & G_y' & G_z'
\end{vmatrix}_{P_0} = (A, B, C).
$$

- **切线方程**：$\dfrac{x - x_0}{A} = \dfrac{y - y_0}{B} = \dfrac{z - z_0}{C}$
- **法平面方程**：$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$

## 解题步骤

1. 确定曲线类型（参数式 / 一般式）
2. 求出切向量 $\boldsymbol{\tau}$
3. 代入切线方程和法平面方程的标准形式

> [!WARNING] AI Generated
> 对于一般式曲线，当 $\dfrac{\partial(F,G)}{\partial(y,z)} \neq 0$ 时可确定隐函数 $y = y(x), z = z(x)$，此时切向量也可通过隐函数求导得到。

## 相关页面

- [[空间平面与直线-PlaneAndLine]]
- [[空间曲面切平面与法线-TangentPlaneAndNormalLine]]
- [[向量代数-VectorAlgebra]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1])
SORT file.name
```
