---
标题: 空间平面与直线
标签: [数学, 第17讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 空间平面和直线的各种方程形式、以及点线面之间的位置关系与距离公式。
来源: 01_Raw/Archive/Lectures/17_第17讲_多元函数积分学的预备知识.md
可信状态: S3 待核查
---

## 定义

空间平面和直线的各种方程形式、以及点线面之间的位置关系与距离公式。

## 平面方程

平面的法向量 $\boldsymbol{n} = (A, B, C)$：

1. **一般式**：$Ax + By + Cz + D = 0$.
2. **点法式**：$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$.
3. **三点式**：$\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ x - x_2 & y - y_2 & z - z_2 \\ x - x_3 & y - y_3 & z - z_3 \end{vmatrix} = 0$.
4. **截距式**：$\dfrac{x}{a} + \dfrac{y}{b} + \dfrac{z}{c} = 1$.
5. **平面束方程**：过直线 $L$ 的平面束为
   $$
   A_1 x + B_1 y + C_1 z + D_1 + \lambda (A_2 x + B_2 y + C_2 z + D_2) = 0.
   $$

## 直线方程

直线的方向向量 $\boldsymbol{\tau} = (l, m, n)$：

1. **一般式（交面式）**：$\begin{cases} A_1 x + B_1 y + C_1 z + D_1 = 0, \\ A_2 x + B_2 y + C_2 z + D_2 = 0, \end{cases}$ 方向向量 $\boldsymbol{\tau} = \boldsymbol{n}_1 \times \boldsymbol{n}_2$.

2. **点向式**：$\dfrac{x - x_0}{l} = \dfrac{y - y_0}{m} = \dfrac{z - z_0}{n}$.

3. **参数式**：$\begin{cases} x = x_0 + lt, \\ y = y_0 + mt, \\ z = z_0 + nt. \end{cases}$

4. **两点式**：$\dfrac{x - x_1}{x_2 - x_1} = \dfrac{y - y_1}{y_2 - y_1} = \dfrac{z - z_1}{z_2 - z_1}$.

## 位置关系

### 直线与直线
设 $\boldsymbol{\tau}_1 = (l_1, m_1, n_1), \boldsymbol{\tau}_2 = (l_2, m_2, n_2)$：
- **垂直**：$\boldsymbol{\tau}_1 \perp \boldsymbol{\tau}_2 \Leftrightarrow l_1 l_2 + m_1 m_2 + n_1 n_2 = 0$.
- **平行**：$\boldsymbol{\tau}_1 /\!/ \boldsymbol{\tau}_2 \Leftrightarrow \dfrac{l_1}{l_2} = \dfrac{m_1}{m_2} = \dfrac{n_1}{n_2}$.
- **夹角**：$\theta = \arccos \dfrac{|\boldsymbol{\tau}_1 \cdot \boldsymbol{\tau}_2|}{|\boldsymbol{\tau}_1| |\boldsymbol{\tau}_2|}$.

### 平面与平面
设 $\boldsymbol{n}_1 = (A_1, B_1, C_1), \boldsymbol{n}_2 = (A_2, B_2, C_2)$：
- **垂直**：$\boldsymbol{n}_1 \perp \boldsymbol{n}_2 \Leftrightarrow A_1 A_2 + B_1 B_2 + C_1 C_2 = 0$.
- **平行**：$\boldsymbol{n}_1 /\!/ \boldsymbol{n}_2 \Leftrightarrow \dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2}$.
- **夹角**：$\theta = \arccos \dfrac{|\boldsymbol{n}_1 \cdot \boldsymbol{n}_2|}{|\boldsymbol{n}_1| |\boldsymbol{n}_2|}$.

### 直线与平面
设 $\boldsymbol{\tau} = (l, m, n), \boldsymbol{n} = (A, B, C)$：
- **垂直**：$\boldsymbol{\tau} /\!/ \boldsymbol{n} \Leftrightarrow \dfrac{l}{A} = \dfrac{m}{B} = \dfrac{n}{C}$.
- **平行**：$\boldsymbol{\tau} \perp \boldsymbol{n} \Leftrightarrow Al + Bm + Cn = 0$.
- **夹角**：$\theta = \arcsin \dfrac{|\boldsymbol{\tau} \cdot \boldsymbol{n}|}{|\boldsymbol{\tau}| |\boldsymbol{n}|}$.

## 距离公式

### 点到直线的距离
点 $M_1(x_1, y_1, z_1)$ 到直线 $\dfrac{x - x_0}{l} = \dfrac{y - y_0}{m} = \dfrac{z - z_0}{n}$ 的距离：
$$
d = \frac{|\boldsymbol{\tau} \times \overrightarrow{M_1 M_0}|}{|\boldsymbol{\tau}|}.
$$

### 点到平面的距离
点 $P_0(x_0, y_0, z_0)$ 到平面 $Ax + By + Cz + D = 0$ 的距离：
$$
d = \frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}}.
$$

## 相关页面

- [[向量代数-VectorAlgebra]]
- [[空间曲线与曲面-SpaceCurveAndSurface]]
- [[距离与位置关系-DistanceAndPosition]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name
```
