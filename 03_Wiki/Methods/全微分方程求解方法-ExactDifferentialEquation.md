---
标题: 全微分方程求解方法
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 若 $P\mathrm{d}x + Q\mathrm{d}y = 0$ 的左端是某二元函数的全微分，则直接积分求出原函数即得通解。
来源: 01_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 全微分条件

若函数 $P(x,y), Q(x,y)$ 在单连通区域 $D$ 上具有一阶连续偏导数，且满足：

$$\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$$

则 $P\mathrm{d}x + Q\mathrm{d}y$ 是某二元函数 $u(x,y)$ 的全微分。

## 全微分方程

形如 $P(x,y)\,\mathrm{d}x + Q(x,y)\,\mathrm{d}y = 0$ 的方程，若左端是 $u(x,y)$ 的全微分，则称其为全微分方程，通解为 $u(x,y) = C$。

## 求解方法

通过曲线积分或凑微分法求出原函数 $u(x,y)$：

$$u(x,y) = \int_{x_0}^x P(x,y)\,\mathrm{d}x + \int_{y_0}^y Q(x_0,y)\,\mathrm{d}y$$

> [!NOTE]
> 全微分方程仅数学一要求。

## 相关页面

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[一阶线性微分方程-FirstOrderLinearODE|一阶线性微分方程]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "微分方程")
SORT 类型 ASC
```
