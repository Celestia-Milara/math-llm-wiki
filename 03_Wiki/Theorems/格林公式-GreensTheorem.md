---
标题: 格林公式
标签: [数学, 第18讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 格林公式建立了平面闭区域上的二重积分与其边界曲线上的第二型曲线积分之间的联系。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
可信状态: S3 待核查
---

## 定理陈述

设平面有界闭区域 $D$ 由分段光滑曲线 $L$ 围成，$P(x, y), Q(x, y)$ 在 $D$ 上具有一阶连续偏导数，$L$ 取正向，则
$$
\oint_L P \, \mathrm{d}x + Q \, \mathrm{d}y = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \mathrm{d}\sigma.
$$

> **正向**：沿 $L$ 前进时，左手始终在 $D$ 内部（逆时针方向）。

## 三大应用情形

### ① 曲线封闭且无奇点
直接用格林公式将环路积分化为二重积分。

### ② 非封闭曲线——补线法
补一条有向线段使曲线封闭，然后用格林公式，最后减去补线上的积分：
$$
\int_{L_{AB}} = \oint_{L_{AB} + C_{BA}} - \int_{C_{BA}}.
$$

### ③ 封闭曲线但有奇点——换路径法
若除奇点外 $\dfrac{\partial Q}{\partial x} = \dfrac{\partial P}{\partial y}$，则换一条包围奇点的简单曲线：
$$
\oint_L = \oint_{L_1}.
$$

## 理论意义

格林公式类似于定积分中的牛顿-莱布尼茨公式——把区域内部的整体性计算转换到边界上（或逆用），简化计算。

## 相关页面

- [[第二型曲线积分计算方法-LineIntegralSecondKindMethods]]
- [[曲线积分与路径无关-PathIndependence]]
- [[高斯公式-GaussTheorem]]
- [[斯托克斯公式-StokesTheorem]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "格林公式")
SORT file.name
```
