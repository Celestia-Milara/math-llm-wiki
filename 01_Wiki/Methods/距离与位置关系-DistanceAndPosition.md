---
title: 距离与位置关系
tags: [数学, 第17讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 空间解析几何中点到直线、点到平面的距离公式以及线线、线面、面面位置关系的判定方法。
source: 00_Raw/17_第17讲_多元函数积分学的预备知识
---

## 点到直线的距离

点 $M_1(x_1, y_1, z_1)$ 到直线 $L: \dfrac{x - x_0}{l} = \dfrac{y - y_0}{m} = \dfrac{z - z_0}{n}$ 的距离：
$$
d = \frac{|\boldsymbol{\tau} \times \overrightarrow{M_1 M_0}|}{|\boldsymbol{\tau}|}
= \frac{\left\| \begin{array}{ccc}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
l & m & n \\
x_0 - x_1 & y_0 - y_1 & z_0 - z_1
\end{array} \right\|}{\sqrt{l^2 + m^2 + n^2}}.
$$

**思路**：平行四边形面积 = 底 $\times$ 高 $\Rightarrow |\boldsymbol{\tau}| \cdot d = |\boldsymbol{\tau} \times \overrightarrow{M_1M_0}|$.

## 点到平面的距离

点 $P_0(x_0, y_0, z_0)$ 到平面 $Ax + By + Cz + D = 0$ 的距离：
$$
d = \frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}}.
$$

## 位置关系判定

### 直线与直线
设 $\boldsymbol{\tau}_1 = (l_1, m_1, n_1)$, $\boldsymbol{\tau}_2 = (l_2, m_2, n_2)$：
- 垂直 $\Leftrightarrow$ $\boldsymbol{\tau}_1 \perp \boldsymbol{\tau}_2$ $\Leftrightarrow$ $l_1 l_2 + m_1 m_2 + n_1 n_2 = 0$
- 平行 $\Leftrightarrow$ $\boldsymbol{\tau}_1 /\!/ \boldsymbol{\tau}_2$ $\Leftrightarrow$ $\dfrac{l_1}{l_2} = \dfrac{m_1}{m_2} = \dfrac{n_1}{n_2}$
- 夹角：$\theta = \arccos \dfrac{|\boldsymbol{\tau}_1 \cdot \boldsymbol{\tau}_2|}{|\boldsymbol{\tau}_1| |\boldsymbol{\tau}_2|}$

### 平面与平面
设 $\boldsymbol{n}_1 = (A_1, B_1, C_1)$, $\boldsymbol{n}_2 = (A_2, B_2, C_2)$：
- 垂直 $\Leftrightarrow$ $\boldsymbol{n}_1 \perp \boldsymbol{n}_2$ $\Leftrightarrow$ $A_1 A_2 + B_1 B_2 + C_1 C_2 = 0$
- 平行 $\Leftrightarrow$ $\boldsymbol{n}_1 /\!/ \boldsymbol{n}_2$ $\Leftrightarrow$ $\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2}$
- 夹角：$\theta = \arccos \dfrac{|\boldsymbol{n}_1 \cdot \boldsymbol{n}_2|}{|\boldsymbol{n}_1| |\boldsymbol{n}_2|}$

### 直线与平面
设 $\boldsymbol{\tau} = (l, m, n)$, $\boldsymbol{n} = (A, B, C)$：
- 垂直 $\Leftrightarrow$ $\boldsymbol{\tau} /\!/ \boldsymbol{n}$ $\Leftrightarrow$ $\dfrac{l}{A} = \dfrac{m}{B} = \dfrac{n}{C}$
- 平行 $\Leftrightarrow$ $\boldsymbol{\tau} \perp \boldsymbol{n}$ $\Leftrightarrow$ $Al + Bm + Cn = 0$
- 夹角：$\theta = \arcsin \dfrac{|\boldsymbol{\tau} \cdot \boldsymbol{n}|}{|\boldsymbol{\tau}| |\boldsymbol{n}|}$

## 相关页面

- [[空间平面与直线-PlaneAndLine]]
- [[向量代数-VectorAlgebra]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "解析几何")
SORT file.name
```
