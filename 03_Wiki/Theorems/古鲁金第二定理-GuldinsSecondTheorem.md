---
标题: 古鲁金第二定理（Pappus–Guldin 定理）
标签: [数学, 第14讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 平面区域绕不与之相交的轴旋转所得旋转体的体积等于区域面积乘以形心所经过的路程。
来源: 01_Raw/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定理陈述

将平面有界闭区域 $D$ 绕一条不穿过 $D$ 的直线 $L$ 旋转一周，所得旋转体的体积 $V$ 等于 $D$ 的面积 $S$ 乘以 $D$ 的形心 $(\overline{x}, \overline{y})$ 到 $L$ 的距离 $r$ 所经过的圆周路程：

$$
V = 2\pi \cdot S \cdot r(\overline{x}, \overline{y}),
$$

其中 $r(\overline{x}, \overline{y})$ 为形心到旋转轴的距离。

## 推导思想

将区域 $D$ 分成 $n$ 个小区域 $\Delta\sigma_i$，每个小区域绕轴旋转形成近似圆环体，其体积 $\Delta V_i \approx 2\pi r_i \Delta\sigma_i$，求和取极限即得。

## 应用场景

- 已知形心求旋转体体积
- 已知体积求形心坐标
- 复杂区域绕直线旋转的体积计算（避免直接积分）

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
