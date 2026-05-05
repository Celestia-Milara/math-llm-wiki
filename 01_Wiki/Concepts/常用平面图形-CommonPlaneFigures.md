---
标题: 常用平面图形
标签: [数学, 附录, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 高等数学中常见的平面曲线，包括心形线、双纽线、螺线、玫瑰线、摆线、星形线、笛卡儿叶形线等。
来源: 00_Raw/20_附录2_常用平面图形.md
---

## 心形线 (Cardioid)

极坐标方程：
$$r = a(1 + \cos\theta) \quad (a > 0)$$

心形线是外摆线的一种，具有一个尖点。

## 伯努利双纽线 (Bernoulli Lemniscate)

极坐标方程：
$$r^2 = a^2 \cos 2\theta \quad (a > 0)$$
$$r^2 = a^2 \sin 2\theta \quad (a > 0)$$

形状如"无穷"符号 $\infty$。

## 阿基米德螺线 (Archimedean Spiral)

极坐标方程：
$$r = a\theta \quad (a > 0,\; \theta \geqslant 0)$$

动点沿射线匀速运动的同时射线匀速转动。

## 对数螺线 (Logarithmic Spiral)

极坐标方程：
$$r = \mathrm{e}^{\alpha\theta} \quad (\alpha > 0)$$

亦称等角螺线，曲率半径与弧长成正比。

## 双曲螺线 (Hyperbolic Spiral)

极坐标方程：
$$r\theta = a \quad (a > 0)$$

当 $\theta \to \infty$ 时 $r \to 0$。

## 三叶玫瑰线 (Three-leaf Rose)

极坐标方程：
$$r = a\sin 3\theta \quad (a > 0)$$
$$r = a\cos 3\theta \quad (a > 0)$$

具有三片花瓣形状。

## 四叶玫瑰线 (Four-leaf Rose)

极坐标方程：
$$r = a\sin 2\theta \quad (a > 0)$$
$$r = a\cos 2\theta \quad (a > 0)$$

具有四片花瓣形状。

## 摆线 (Cycloid)

参数方程：
$$\begin{cases}
x = a(t - \sin t), \\
y = a(1 - \cos t)
\end{cases} \quad a > 0$$

亦称平摆线，是圆沿直线滚动时圆周上一点形成的轨迹。

## 星形线 (Astroid)

参数方程与直角坐标方程：
$$\begin{cases}
x = a\cos^3 t, \\
y = a\sin^3 t
\end{cases} \quad \text{或} \quad x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}} \quad (a > 0)$$

内摆线的一种，形状如四角星。

## 笛卡儿叶形线 (Folium of Descartes)

直角坐标方程与参数方程：
$$x^3 + y^3 - 3axy = 0 \quad \text{或} \quad \begin{cases}
x = \dfrac{3at}{1 + t^3},\\[6pt]
y = \dfrac{3at^2}{1 + t^3}
\end{cases} \quad (a > 0)$$

具有一个结点和一条渐近线。

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `00_Raw/20_附录2_常用平面图形.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE tags AS 标签, status AS 状态
FROM "01_Wiki"
WHERE contains(tags, "平面图形") OR contains(tags, "曲线")
SORT file.name ASC
```
