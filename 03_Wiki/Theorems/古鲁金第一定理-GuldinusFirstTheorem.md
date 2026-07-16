---
标题: 古鲁金第一定理
标签: [数学, 第12讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 平面曲线绕不与之相交的轴旋转所得侧面积等于曲线弧长乘以形心所经路程。
来源: 01_Raw/Archive/Lectures/12_第12讲_一元函数积分学的应用(三).md
可信状态: S3 待核查
---

## 定理陈述

将曲线段 $L$ 绕直线 $L_0$ 旋转一周所得的旋转侧面积 $A$ 为

$$
A = 2\pi \cdot r(\bar{x}, \bar{y}) \cdot l,
$$

其中 $l$ 为曲线段 $L$ 的弧长，$r(\bar{x}, \bar{y})$ 为曲线形心到旋转轴 $L_0$ 的距离。

## 数学推导

曲线段 $L$ 绕直线 $L_0: ax + by + c = 0$ 旋转一周的侧面积：

$$
A = \int_a^b 2\pi \cdot \frac{|ax + by + c|}{\sqrt{a^2 + b^2}} \sqrt{1 + [f'(x)]^2} \, \mathrm{d}x.
$$

与形心到直线的距离公式比较：

$$
r(\bar{x}, \bar{y}) = \frac{\int_a^b \frac{|ax + by + c|}{\sqrt{a^2 + b^2}} \sqrt{1 + [f'(x)]^2} \, \mathrm{d}x}{\int_a^b \sqrt{1 + [f'(x)]^2} \, \mathrm{d}x},
$$

即得 $A = 2\pi \cdot r(\bar{x}, \bar{y}) \cdot l$.

## 应用示例

圆 $x^2 + y^2 = 1$ 绕直线 $x = 2$ 旋转一周所成旋转体的表面积：

由古鲁金第一定理，圆的周长为 $2\pi$，圆心 $(0,0)$ 到直线 $x = 2$ 的距离为 $2$，故表面积 $= 2\pi \cdot 2 \cdot 2\pi = 8\pi^2$.

> [!TIP] 几何直觉
> 古鲁金第一定理将旋转侧面积的计算转化为形心位置和弧长的乘积，避免了直接复杂的积分运算。

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/12_第12讲_一元函数积分学的应用(三).md`

```dataview
TABLE
  title as "名称",
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "旋转")
SORT file.name ASC
```
