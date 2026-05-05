---
标题: 第二型曲线积分计算方法
标签: [数学, 第18讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 第二型曲线积分的三种主要计算方法：化为定积分（参数法）、格林公式法（补线/挖洞）、与路径无关法。
来源: 00_Raw/18_第18讲_多元函数积分学
---

## 1. 基本方法——化为定积分

设 $L: \begin{cases} x = x(t), \\ y = y(t) \end{cases}$，$t: \alpha \to \beta$（$\alpha$ 对应起点，$\beta$ 对应终点）：
$$
\int_L P(x, y) \, \mathrm{d}x + Q(x, y) \, \mathrm{d}y = \int_\alpha^\beta \bigl[ P(x(t), y(t)) x'(t) + Q(x(t), y(t)) y'(t) \bigr] \, \mathrm{d}t.
$$

> $\alpha, \beta$ 的大小关系无关紧要，关键是分别对应起点和终点（与第一型不同）。

## 2. 格林公式法

### 情形一：曲线封闭且无奇点
直接使用格林公式：
$$
\oint_L P \, \mathrm{d}x + Q \, \mathrm{d}y = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \mathrm{d}\sigma.
$$

### 情形二：非封闭曲线——补线法
补一条有向线段 $C_{BA}$ 构成封闭曲线，则
$$
\int_{L_{AB}} = \oint_{L_{AB} + C_{BA}} - \int_{C_{BA}}.
$$

### 情形三：封闭曲线但有奇点——换路径法
若除奇点外处处 $\dfrac{\partial Q}{\partial x} = \dfrac{\partial P}{\partial y}$，则换一条包围奇点的简单曲线 $L_1$：
$$
\oint_L P \, \mathrm{d}x + Q \, \mathrm{d}y = \oint_{L_1} P \, \mathrm{d}x + Q \, \mathrm{d}y.
$$

## 3. 与路径无关时——折线法

若 $\dfrac{\partial Q}{\partial x} = \dfrac{\partial P}{\partial y}$，则积分与路径无关，可取平行于坐标轴的折线计算：
$$
\int_{(x_0, y_0)}^{(x, y)} P \, \mathrm{d}x + Q \, \mathrm{d}y = \int_{x_0}^x P(x, y_0) \, \mathrm{d}x + \int_{y_0}^y Q(x, y) \, \mathrm{d}y.
$$

## 空间第二型曲线积分

$$
\int_{\Gamma} P \, \mathrm{d}x + Q \, \mathrm{d}y + R \, \mathrm{d}z = \int_\alpha^\beta \bigl[ P x'(t) + Q y'(t) + R z'(t) \bigr] \, \mathrm{d}t.
$$

或用 [[斯托克斯公式-StokesTheorem]] 转化为曲面积分。

## 相关页面

- [[第二型曲线积分-LineIntegralSecondKind]]
- [[格林公式-GreensTheorem]]
- [[曲线积分与路径无关-PathIndependence]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "曲线积分")
SORT file.name
```
