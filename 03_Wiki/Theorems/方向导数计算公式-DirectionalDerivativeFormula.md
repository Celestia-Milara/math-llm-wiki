---
标题: 方向导数计算公式
标签: [数学, 第17讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 可微函数沿任一方向的方向导数等于梯度与该方向单位向量的点积。
来源: 01_Raw/Archive/Lectures/17_第17讲_多元函数积分学的预备知识.md
可信状态: S3 待核查
---

## 定理陈述

设三元函数 $u = u(x, y, z)$ 在点 $P_0(x_0, y_0, z_0)$ 处可微分，则 $u$ 在 $P_0$ 处沿任一方向 $\boldsymbol{l}$ 的方向导数都存在，且
$$
\left.\frac{\partial u}{\partial l}\right|_{P_0} = u_x'(P_0) \cos\alpha + u_y'(P_0) \cos\beta + u_z'(P_0) \cos\gamma,
$$
其中 $(\cos\alpha, \cos\beta, \cos\gamma)$ 为方向 $\boldsymbol{l}$ 的方向余弦。

## 推导

$$
\begin{aligned}
\left.\frac{\partial u}{\partial l}\right|_{P_0}
&= \lim_{t \to 0^+} \frac{u(x_0 + \Delta x, y_0 + \Delta y, z_0 + \Delta z) - u(x_0, y_0, z_0)}{t} \quad &\text{[方向导数定义]} \\
&= \lim_{t \to 0^+} \frac{u_x'(P_0) \Delta x + u_y'(P_0) \Delta y + u_z'(P_0) \Delta z + o(t)}{t} \quad &\text{[可微定义]} \\
&= u_x'(P_0) \cos\alpha + u_y'(P_0) \cos\beta + u_z'(P_0) \cos\gamma \quad &\text{[}\frac{\Delta x}{t} = \cos\alpha\text{, 等]}
\end{aligned}
$$

其中 $\begin{cases} \Delta x = t \cos\alpha, \\ \Delta y = t \cos\beta, \\ \Delta z = t \cos\gamma, \end{cases}$ $t = \sqrt{(\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2}$.

## 与梯度的关系

$$
\left.\frac{\partial u}{\partial l}\right|_{P_0} = \mathbf{grad}\, u\big|_{P_0} \cdot \boldsymbol{l}^\circ = \bigl|\mathbf{grad}\, u\big|_{P_0}\bigr| \cos\theta.
$$

- $\theta = 0$：方向导数取最大值 $|\mathbf{grad}\, u|$
- $\theta = \dfrac{\pi}{2}$：方向导数为 $0$

## 相关页面

- [[方向导数与梯度-DirectionalDerivativeAndGradient]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "方向导数")
SORT file.name
```
