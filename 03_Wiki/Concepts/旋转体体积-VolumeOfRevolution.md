---
标题: 旋转体体积
标签: [数学, 第10讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 用定积分计算平面图形绕坐标轴或定直线旋转一周所成旋转体的体积。
来源: 01_Raw/Archive/Lectures/10_第10讲_一元函数积分学的应用(一).md
可信状态: S3 待核查
---

## 定义

用定积分计算平面图形绕坐标轴或定直线旋转一周所成旋转体的体积。

## 绕 $x$ 轴旋转（圆盘法）

曲线 $y = y(x)$ 与 $x = a$, $x = b$ 及 $x$ 轴围成的曲边梯形绕 $x$ 轴旋转一周：

$$
V_x = \pi \int_a^b y^2(x) \, \mathrm{d}x.
$$

**微元法**：取 $[x, x+\mathrm{d}x]$，体积微元 $\mathrm{d}V = \pi y^2(x) \, \mathrm{d}x$.

## 绕 $y$ 轴旋转（柱壳法）

曲线 $y = y(x)$ 与 $x = a$, $x = b$ 及 $x$ 轴围成的曲边梯形绕 $y$ 轴旋转一周：

$$
V_y = 2\pi \int_a^b x \, |y(x)| \, \mathrm{d}x.
$$

**柱壳法推导**：取小竖条绕 $y$ 轴旋转成"圆柱壳"，展开为长方体，其体积微元 $\mathrm{d}V_y = 2\pi x |y(x)| \, \mathrm{d}x$.

## 绕定直线旋转（一般公式）

平面曲线 $L: y = f(x), a \leqslant x \leqslant b$, 绕定直线 $L_0: Ax + By + C = 0$ 旋转一周：

$$
V = \frac{\pi}{(A^2 + B^2)^{3/2}} \int_a^b [Ax + Bf(x) + C]^2 \, |Af'(x) - B| \, \mathrm{d}x.
$$

> [!TIP] 几何直觉
> 圆盘法是将旋转体切成平行于 $x$ 轴的薄片，每片近似为圆柱体；柱壳法则将旋转体切成同心圆柱壳。

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/10_第10讲_一元函数积分学的应用(一).md`

```dataview
TABLE
  title as "名称",
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
