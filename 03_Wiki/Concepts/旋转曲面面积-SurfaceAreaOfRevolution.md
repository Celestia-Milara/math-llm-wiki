---
标题: 旋转曲面面积（侧面积）
标签: [数学, 第10讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 用定积分计算平面曲线绕坐标轴旋转一周所得旋转曲面的侧面积。
来源: 01_Raw/10_第10讲_一元函数积分学的应用(一).md
---

## 定义

用定积分计算平面曲线绕坐标轴旋转一周所得旋转曲面的侧面积。

## 直角坐标方程

曲线 $L: y = f(x) \, (a \leqslant x \leqslant b)$ 绕 $x$ 轴旋转一周：

$$
S = 2\pi \int_a^b |y| \sqrt{1 + (y')^2} \, \mathrm{d}x.
$$

## 参数方程

曲线 $L: \begin{cases} x = x(t), \\ y = y(t) \end{cases} \, (\alpha \leqslant t \leqslant \beta)$ 绕 $x$ 轴旋转一周：

$$
S = 2\pi \int_\alpha^\beta |y(t)| \sqrt{(x'(t))^2 + (y'(t))^2} \, \mathrm{d}t.
$$

## 极坐标方程

曲线 $L: r = r(\theta) \, (\alpha \leqslant \theta \leqslant \beta)$ 绕 $x$ 轴旋转一周：

$$
S = 2\pi \int_\alpha^\beta |r(\theta)\sin\theta| \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} \, \mathrm{d}\theta.
$$

## 与弧长的关系

旋转侧面积公式是在弧长公式基础上乘以 $2\pi |y|$（旋转半径对应的周长）：

$$
S = 2\pi \int |y| \, \mathrm{d}s,
$$

其中 $\mathrm{d}s$ 为弧长微元。

> [!TIP] 几何直觉
> 将曲线切分成小段，每段绕 $x$ 轴旋转形成"圆台侧面"，其面积近似为 $2\pi |y| \, \mathrm{d}s$。

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
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
