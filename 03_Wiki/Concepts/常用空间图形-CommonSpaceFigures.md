---
标题: 常用空间图形
标签: [数学, 附录, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 高等数学中常见的空间曲面与曲线，包括球面、平面、锥面、旋转抛物面、圆柱面、双曲面、马鞍面及其交线。
来源: 01_Raw/Archive/Lectures/21_附录3_常用空间图形.md
可信状态: S3 待核查
---

## (1) 上半球面 (Upper Hemisphere)

$$z = \sqrt{a^2 - x^2 - y^2}, \quad a > 0$$

## (2) 平面截距式 (Plane in Intercept Form)

$$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1, \quad a,b,c > 0, \quad x,y,z \geqslant 0$$

## (3) 圆锥面（上半）(Upper Cone)

$$z = \sqrt{x^2 + y^2}$$

## (4) 圆锥面 (Cone)

$$x^2 + y^2 = z^2$$

## (5) 旋转抛物面 (Paraboloid of Revolution)

$$z = x^2 + y^2$$

## (6) 圆柱面 (Cylinder)

$$x^2 + y^2 = a^2, \quad z \geqslant 0, \; a > 0$$

## (7) 单叶双曲面 (Hyperboloid of One Sheet)

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$$

## (8) 双叶双曲面 (Hyperboloid of Two Sheets)

$$\frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$$

## (9) 曲面 (Parabolic-类型 Surface)

$$\sqrt{x} + \sqrt{y} + \sqrt{z} = \sqrt{a}, \quad a > 0$$

## (10) 双曲抛物面 / 马鞍面 (Hyperbolic Paraboloid)

$$z = xy$$

## (11) 马鞍面与平面交线

$$\begin{cases}
z = xy, \\
y = x, \\
x = 1, \\
z = 0
\end{cases}$$

## (12) 马鞍面与平面交线

$$\begin{cases}
z = xy, \\
x + y = 1, \\
z = 0
\end{cases}$$

## (13) 马鞍面与圆柱面交线

$$\begin{cases}
z = xy, \\
x^2 + y^2 = a^2 \quad (a > 0)
\end{cases}$$

## (14) 旋转抛物面与柱面交线

$$\begin{cases}
z = x^2 + y^2, \\
z = 1 - x^2
\end{cases}$$

## (15) 圆柱面与柱面交线

$$\begin{cases}
x^2 + y^2 = 1, \\
z = 1 - x^2
\end{cases}$$

## (16) 旋转曲面 (Surface of Revolution)

$$x^2 + (y - z)^2 = (1 - z)^2, \quad 0 \leqslant z \leqslant 1$$

## (17) 旋转抛物面与圆柱面交线

$$\begin{cases}
z = x^2 + y^2, \\
x^2 + (y - 1)^2 = 1
\end{cases}$$

## (18) 多曲面围成区域

$$\begin{cases}
z = 2(x^2 + y^2), \\
x^2 + y^2 = x, \\
x^2 + y^2 = 2x, \\
z = 0
\end{cases}$$

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `01_Raw/21_附录3_常用空间图形.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE 标签 AS 标签, 可信状态 AS 状态
FROM "03_Wiki"
WHERE contains(标签, "空间图形") OR contains(标签, "曲面")
SORT file.name ASC
```
