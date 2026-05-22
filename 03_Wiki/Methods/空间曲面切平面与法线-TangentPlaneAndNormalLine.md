---
标题: 空间曲面的切平面与法线
标签: [数学, 第17讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过隐式方程或显式方程求曲面的法向量，进而得到切平面方程和法线方程。
来源: 01_Raw/17_第17讲_多元函数积分学的预备知识.md
---

## 隐式方程情形

曲面 $\Sigma: F(x, y, z) = 0$，$F$ 一阶偏导连续。

在 $P_0(x_0, y_0, z_0)$ 处：
- **法向量**：$\boldsymbol{n} = \bigl(F_x'|_{P_0},\; F_y'|_{P_0},\; F_z'|_{P_0}\bigr)$
- **切平面方程**：$F_x'|_{P_0}(x - x_0) + F_y'|_{P_0}(y - y_0) + F_z'|_{P_0}(z - z_0) = 0$
- **法线方程**：$\dfrac{x - x_0}{F_x'|_{P_0}} = \dfrac{y - y_0}{F_y'|_{P_0}} = \dfrac{z - z_0}{F_z'|_{P_0}}$

## 显式函数情形

曲面 $z = f(x, y) \;\Rightarrow\; f(x, y) - z = 0$。

在 $P_0(x_0, y_0, z_0)$ 处：
- **法向量**：$\boldsymbol{n} = \bigl(f_x'(x_0, y_0),\; f_y'(x_0, y_0),\; -1\bigr)$（方向向下）
- **切平面方程**：$f_x'(x_0, y_0)(x - x_0) + f_y'(x_0, y_0)(y - y_0) - (z - z_0) = 0$
- **法线方程**：$\dfrac{x - x_0}{f_x'(x_0, y_0)} = \dfrac{y - y_0}{f_y'(x_0, y_0)} = \dfrac{z - z_0}{-1}$

> [!TIP] 几何直觉
> 曲面的梯度向量 $\nabla F$ 就是法向量。对于显式 $z = f(x, y)$，将其改写为 $f(x, y) - z = 0$ 后用梯度法即可得到法向量。

## 相关页面

- [[空间曲线切线与法平面-TangentAndNormalPlane]]
- [[空间平面与直线-PlaneAndLine]]
- [[方向导数与梯度-DirectionalDerivativeAndGradient]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name
```
