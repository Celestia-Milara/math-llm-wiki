---
标题: 第二型曲面积分计算方法
标签: [数学, 第18讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 第二型曲面积分（对坐标）的三种计算方法：投影法、转换投影法、高斯公式法（补面/挖洞）。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
---

## 1. 基本方法——投影法（化为二重积分）

将积分拆成三项，分别投影到相应坐标面：

对于 $\iint_{\Sigma} R(x, y, z) \, \mathrm{d}x\mathrm{d}y$（投影到 $xOy$ 面）：
- 一投：确定 $\Sigma$ 在 $xOy$ 面上的投影域 $D_{xy}$
- 二代：代入 $z = z(x, y)$
- 三计算：$\mathrm{d}x\mathrm{d}y$ 前符号由法向量方向决定（上正下负）

$$
\iint_{\Sigma} R(x, y, z) \, \mathrm{d}x\mathrm{d}y = \pm \iint_{D_{xy}} R[x, y, z(x, y)] \, \mathrm{d}x\mathrm{d}y.
$$

符号选取：
- **上侧**（$\cos\gamma > 0$）取 $+$
- **下侧**（$\cos\gamma < 0$）取 $-$

类似处理 $\iint_{\Sigma} P \, \mathrm{d}y\mathrm{d}z$ 和 $\iint_{\Sigma} Q \, \mathrm{d}z\mathrm{d}x$.

## 2. 转换投影法

若曲面 $\Sigma: z = z(x, y)$，则
$$
\iint_{\Sigma} P \, \mathrm{d}y\mathrm{d}z + Q \, \mathrm{d}z\mathrm{d}x + R \, \mathrm{d}x\mathrm{d}y = \pm \iint_D \left( -P \frac{\partial z}{\partial x} - Q \frac{\partial z}{\partial y} + R \right) \mathrm{d}x\mathrm{d}y.
$$

符号选取：**上正下负**。

## 3. 高斯公式法

### 情形一：封闭曲面且内部无奇点
$$
\oiint_{\Sigma} P \, \mathrm{d}y\mathrm{d}z + Q \, \mathrm{d}z\mathrm{d}x + R \, \mathrm{d}x\mathrm{d}y = \iiint_{\Omega} \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) \mathrm{d}v.
$$

### 情形二：非封闭曲面——补面法
补一块简单平面使封闭，然后用高斯公式减去补面的积分。

### 情形三：有奇点——换面法
若内部有奇点但除奇点外 $\operatorname{div} \boldsymbol{F} = 0$，可换一个包围奇点的简单曲面：
$$
\oiint_{\Sigma} = \oiint_{\Sigma_1} \quad (\text{同方向}).
$$

## 相关页面

- [[第二型曲面积分-SurfaceIntegralSecondKind]]
- [[高斯公式-GaussTheorem]]
- [[第一型曲面积分计算方法-SurfaceIntegralFirstKindMethods]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "曲面积分")
SORT file.name
```
