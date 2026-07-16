---
标题: 方向导数与梯度
标签: [数学, 第17讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 方向导数描述函数沿某方向的变化率，梯度是函数变化率最大的方向向量，二者通过投影关联。
来源: 01_Raw/Archive/Lectures/17_第17讲_多元函数积分学的预备知识.md
可信状态: S3 待核查
---

## 定义

方向导数描述函数沿某方向的变化率，梯度是函数变化率最大的方向向量，二者通过投影关联。

## 方向导数

### 定义
设 $u = u(x, y, z)$ 在点 $P_0(x_0, y_0, z_0)$ 的邻域内有定义，$l$ 为从 $P_0$ 出发的射线，$t$ 为 $P$ 与 $P_0$ 的距离，则方向导数为
$$
\left.\frac{\partial u}{\partial l}\right|_{P_0} = \lim_{t \to 0^+} \frac{u(P) - u(P_0)}{t}.
$$

### 计算公式
若 $u$ 在 $P_0$ 处可微，则沿方向 $\boldsymbol{l}$（方向余弦 $(\cos\alpha, \cos\beta, \cos\gamma)$）的方向导数为
$$
\left.\frac{\partial u}{\partial l}\right|_{P_0} = u_x'(P_0) \cos\alpha + u_y'(P_0) \cos\beta + u_z'(P_0) \cos\gamma.
$$

## 梯度

### 定义
设 $u = u(x, y, z)$ 在 $P_0$ 处具有一阶连续偏导数，则
$$
\left.\mathbf{grad}\, u\right|_{P_0} = \bigl(u_x'(P_0),\; u_y'(P_0),\; u_z'(P_0)\bigr).
$$

### 运算性质
- $\mathbf{grad}(u \pm v) = \mathbf{grad}\, u \pm \mathbf{grad}\, v$
- $\mathbf{grad}(uv) = v\,\mathbf{grad}\, u + u\,\mathbf{grad}\, v$
- $\mathbf{grad}\!\left(\dfrac{u}{v}\right) = \dfrac{v\,\mathbf{grad}\, u - u\,\mathbf{grad}\, v}{v^2}\;(v \neq 0)$

## 方向导数与梯度的关系

$$
\left.\frac{\partial u}{\partial l}\right|_{P_0} = \mathbf{grad}\, u\big|_{P_0} \cdot \boldsymbol{l}^\circ
= \bigl|\mathbf{grad}\, u\big|_{P_0}\bigr| \cos\theta,
$$
其中 $\theta$ 为梯度与 $\boldsymbol{l}^\circ$ 的夹角。

**重要结论**：
- 当 $\cos\theta = 1$（即 $\boldsymbol{l}$ 与梯度同向）时，方向导数取最大值 $|\mathbf{grad}\, u|$.
- 当 $\cos\theta = 0$（即 $\boldsymbol{l}$ 与梯度垂直）时，方向导数为 $0$.

$$
\bigl|\mathbf{grad}\, u\bigr| = \sqrt{(u_x')^2 + (u_y')^2 + (u_z')^2}.
$$

> [!TIP] 几何直觉
> 梯度指向函数增长最快的方向，其模等于最大增长速率。在等高线（等值面）上，梯度处处与等高线（等值面）垂直。

## 相关页面

- [[向量代数-VectorAlgebra]]
- [[散度与旋度-DivergenceAndCurl]]
- [[方向导数计算公式-DirectionalDerivativeFormula]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "方向导数") OR contains(标签, "梯度")
SORT file.name
```
