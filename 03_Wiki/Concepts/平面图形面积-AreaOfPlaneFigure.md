---
标题: 平面图形面积
标签: [数学, 第10讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 用定积分计算平面图形在直角坐标系、参数方程、极坐标系下的面积。
来源: 01_Raw/Archive/Lectures/10_第10讲_一元函数积分学的应用(一).md
---

## 定义

用定积分计算平面图形在直角坐标系、参数方程、极坐标系下的面积。

## 直角坐标系下的面积

曲线 $y = y_1(x)$ 与 $y = y_2(x)$ 及直线 $x = a$, $x = b$ 所围成的平面图形的面积：

$$
S = \int_a^b |y_1(x) - y_2(x)| \, \mathrm{d}x.
$$

**微元法思路**：
1. 取微元：$\Delta S = |y_1(x) - y_2(x)| \, \mathrm{d}x$
2. 积分：$S = \int_a^b |y_1(x) - y_2(x)| \, \mathrm{d}x$

## 参数方程下的面积

若曲线由参数方程 $\begin{cases} x = x(t), \\ y = y(t) \end{cases}$ 给出，则

$$
S = \int_\alpha^\beta y(t) x'(t) \, \mathrm{d}t.
$$

本质是直角坐标系下面积公式经换元法得到。

## 极坐标系下的面积

曲线 $r = r_1(\theta)$ 与 $r = r_2(\theta)$ 及射线 $\theta = \alpha$, $\theta = \beta$ 所围成的曲边扇形的面积：

$$
S = \frac{1}{2} \int_\alpha^\beta \left| r_1^2(\theta) - r_2^2(\theta) \right| \, \mathrm{d}\theta.
$$

**微元法推导**：当 $\mathrm{d}\theta \to 0$ 时，扇形区域近似为三角形，面积微元为 $\frac{1}{2} r^2(\theta) \, \mathrm{d}\theta$。

> [!TIP] 几何直觉
> 极坐标下的面积公式可理解为"大扇形面积减去小扇形面积"的积分形式。

## 注意事项

- 需确保被积函数在积分区间上保持非负（加绝对值）
- 可利用对称性简化计算
- 参数方程下的问题本质上是对定积分换元法的变相考查
- 面积公式可推广至收敛的广义积分情形

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/10_第10讲_一元函数积分学的应用(一).md`

```dataview
TABLE
  title as "名称",
  掌握状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND contains(标签, this.标签[2])
SORT file.name ASC
```
