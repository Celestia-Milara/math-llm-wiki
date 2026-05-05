---
标题: 函数平均值
标签: [数学, 第10讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 函数在闭区间上的平均值定义为函数在该区间的定积分除以区间长度。
来源: 00_Raw/10_第10讲_一元函数积分学的应用(一).md
---

## 定义

设 $y(x)$ 在 $[a, b]$ 上连续，则 $y(x)$ 在 $[a, b]$ 上的平均值为

$$
\bar{y} = \frac{1}{b - a} \int_a^b y(x) \, \mathrm{d}x.
$$

## 与积分中值定理的联系

由积分中值定理，存在 $\xi \in [a, b]$，使得

$$
\bar{y} = \frac{1}{b - a} \int_a^b y(x) \, \mathrm{d}x = y(\xi).
$$

即连续函数在区间上的平均值等于该区间上某点的函数值。

## 注意事项

- 平均值公式常用于求函数在一段区间上的平均变化率
- 在物理和经济应用中经常出现（如平均成本、平均速度等）

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`00_Raw/10_第10讲_一元函数积分学的应用(一).md`

```dataview
TABLE
  title as "名称",
  status as "状态",
  summary as "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
