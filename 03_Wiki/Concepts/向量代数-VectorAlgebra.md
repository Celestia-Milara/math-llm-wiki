---
标题: 向量代数
标签: [数学, 第17讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 研究向量的表达形式、数量积、向量积、混合积、方向余弦等基本运算与性质。
来源: 01_Raw/Archive/Lectures/17_第17讲_多元函数积分学的预备知识.md
可信状态: S3 待核查
---

## 定义

既有大小又有方向的量称为向量。研究向量的表达形式、数量积、向量积、混合积等基本运算与性质。

## 向量的表达形式

既有大小又有方向的量称为向量。两个向量大小相等、方向相同即相等，与位置无关（自由性）。

向量的坐标表示：
$$
\boxed{\boldsymbol{a}} = (a_x, a_y, a_z) = a_x \boldsymbol{i} + a_y \boldsymbol{j} + a_z \boldsymbol{k}.
$$

## 向量的运算

### 1. 数量积（内积、点积）

结果为标量。

$$
\boldsymbol{a} \cdot \boldsymbol{b} = (a_x, a_y, a_z) \cdot (b_x, b_y, b_z) = a_x b_x + a_y b_y + a_z b_z.
$$

$$
\boldsymbol{a} \cdot \boldsymbol{b} = |\boldsymbol{a}| |\boldsymbol{b}| \cos \theta, \quad 
\cos \theta = \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{|\boldsymbol{a}| |\boldsymbol{b}|}.
$$

**垂直条件**：$\boldsymbol{a} \perp \boldsymbol{b} \Leftrightarrow \boldsymbol{a} \cdot \boldsymbol{b} = 0 \Leftrightarrow a_x b_x + a_y b_y + a_z b_z = 0$.

**投影公式**：
$$
\operatorname{Prj}_{\boldsymbol{b}} \boldsymbol{a} = \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{|\boldsymbol{b}|} = \frac{a_x b_x + a_y b_y + a_z b_z}{\sqrt{b_x^2 + b_y^2 + b_z^2}}.
$$

### 2. 向量积（外积、叉积）

结果为向量。

$$
\boldsymbol{a} \times \boldsymbol{b} = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
a_x & a_y & a_z \\
b_x & b_y & b_z
\end{vmatrix},
\quad |\boldsymbol{a} \times \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}| \sin \theta.
$$

方向由右手规则确定（转向角不超过 $\pi$）。

**平行条件**：$\boldsymbol{a} /\!/ \boldsymbol{b} \Leftrightarrow \dfrac{a_x}{b_x} = \dfrac{a_y}{b_y} = \dfrac{a_z}{b_z}$.

### 3. 混合积

结果为标量。

$$
[\boldsymbol{a} \boldsymbol{b} \boldsymbol{c}] = (\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{c} = 
\begin{vmatrix}
a_x & a_y & a_z \\
b_x & b_y & b_z \\
c_x & c_y & c_z
\end{vmatrix}.
$$

**三向量共面条件**：$[\boldsymbol{a} \boldsymbol{b} \boldsymbol{c}] = 0$.

## 方向角与方向余弦

非零向量 $\boldsymbol{a}$ 与 $x, y, z$ 轴正向的夹角 $\alpha, \beta, \gamma$ 称为方向角。

方向余弦：
$$
\cos \alpha = \frac{a_x}{|\boldsymbol{a}|},\quad
\cos \beta = \frac{a_y}{|\boldsymbol{a}|},\quad
\cos \gamma = \frac{a_z}{|\boldsymbol{a}|},
\quad \cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1.
$$

单位向量：
$$
\boldsymbol{a}^\circ = \frac{\boldsymbol{a}}{|\boldsymbol{a}|} = (\cos \alpha, \cos \beta, \cos \gamma).
$$

> [!TIP] 几何直觉
> 向量的三种积对应三种几何意义：数量积衡量投影长度，向量积衡量平行四边形面积，混合积衡量平行六面体体积。

## 相关页面

- [[空间平面与直线-PlaneAndLine]]
- [[方向导数与梯度-DirectionalDerivativeAndGradient]]
- [[散度与旋度-DivergenceAndCurl]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, "向量代数") OR contains(标签, this.标签[1])
SORT file.name
```
