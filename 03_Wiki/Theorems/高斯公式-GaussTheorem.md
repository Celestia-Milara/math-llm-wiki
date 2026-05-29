---
标题: 高斯公式
标签: [数学, 第18讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 高斯公式建立了空间闭区域上的三重积分与其边界曲面上的第二型曲面积分之间的联系，是格林公式在三维的推广。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
---

## 定理陈述

设空间有界闭区域 $\Omega$ 由分片光滑封闭曲面 $\Sigma$ 围成，$P, Q, R$ 在 $\Omega$ 上具有一阶连续偏导数，$\Sigma$ 取外侧，则
$$
\oiint_{\Sigma} P \, \mathrm{d}y\mathrm{d}z + Q \, \mathrm{d}z\mathrm{d}x + R \, \mathrm{d}x\mathrm{d}y = \iiint_{\Omega} \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) \mathrm{d}v.
$$

右侧的被积函数即为散度 $\operatorname{div} \boldsymbol{F}$。

## 三大应用情形

### ① 封闭曲面且内部无奇点
直接用高斯公式将曲面积分化为三重积分。

### ② 非封闭曲面——补面法
补一块简单曲面（如平面）使封闭，用高斯公式后再减去补面上的积分。

### ③ 封闭曲面有奇点——换面法
若内部有奇点但除奇点外 $\operatorname{div} \boldsymbol{F} = 0$，则换一个包围奇点的简单曲面（如球面）：
$$
\oiint_{\Sigma} = \oiint_{\Sigma_1} \quad (\text{同方向}).
$$

## 与格林公式的类比

| 格林公式（二维） | 高斯公式（三维） |
|----------------|----------------|
| 边界：闭曲线 $L$ | 边界：闭曲面 $\Sigma$ |
| 内部：平面区域 $D$ | 内部：空间区域 $\Omega$ |
| $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}$ | $\dfrac{\partial P}{\partial x} + \dfrac{\partial Q}{\partial y} + \dfrac{\partial R}{\partial z}$ |

## 相关页面

- [[第二型曲面积分计算方法-SurfaceIntegralSecondKindMethods]]
- [[散度与旋度-DivergenceAndCurl]]
- [[格林公式-GreensTheorem]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "高斯公式")
SORT file.name
```
