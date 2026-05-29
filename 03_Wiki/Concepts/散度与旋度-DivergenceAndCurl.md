---
标题: 散度与旋度
标签: [数学, 第17讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 散度描述向量场的发散强度（源），旋度描述向量场的旋转强度（涡），是向量场论的核心概念。
来源: 01_Raw/Archive/Lectures/17_第17讲_多元函数积分学的预备知识.md
---

## 定义

散度描述向量场的发散强度（源），旋度描述向量场的旋转强度（涡），是向量场论的核心概念。

## 散度

设向量场 $\boldsymbol{A}(x, y, z) = P(x, y, z)\boldsymbol{i} + Q(x, y, z)\boldsymbol{j} + R(x, y, z)\boldsymbol{k}$，则散度为
$$
\operatorname{div} \boldsymbol{A} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}.
$$

散度是标量，表示向量场中某点处向外（内）发散的程度——"源"的强度。

> [!TIP] 几何直觉
> $ \operatorname{div} \boldsymbol{A} > 0 $ 表示该点有向外发散的"源"；$ \operatorname{div} \boldsymbol{A} < 0 $ 表示该点有向内汇聚的"汇"；$ \operatorname{div} \boldsymbol{A} = 0 $ 表示该点处无源，称为无源场。

## 旋度

设向量场 $\boldsymbol{A}(x, y, z) = P\boldsymbol{i} + Q\boldsymbol{j} + R\boldsymbol{k}$，则旋度为
$$
\operatorname{rot} \boldsymbol{A} = 
\begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix}.
$$

旋度是向量，描述向量场中某点处向量旋转的强度。

> [!TIP] 几何直觉
> 旋度的方向是旋转的轴向（右手规则），模长表示旋转强度。$ \operatorname{rot} \boldsymbol{A} = \boldsymbol{0} $ 称为无旋场。

## 与梯度对比

| 概念 | 作用对象 | 结果类型 | 物理意义 |
|------|---------|---------|---------|
| 梯度 $\nabla u$ | 数量场 $u$ | 向量 | 最大方向导数 |
| 散度 $\nabla \cdot \boldsymbol{A}$ | 向量场 $\boldsymbol{A}$ | 标量 | 源强度 |
| 旋度 $\nabla \times \boldsymbol{A}$ | 向量场 $\boldsymbol{A}$ | 向量 | 旋转强度 |

## 相关页面

- [[方向导数与梯度-DirectionalDerivativeAndGradient]]
- [[向量代数-VectorAlgebra]]
- [[数量场-ScalarField]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "场论")
SORT file.name
```
