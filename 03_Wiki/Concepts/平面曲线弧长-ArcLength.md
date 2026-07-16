---
标题: 平面曲线弧长
标签: [数学, 第10讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 用定积分计算光滑曲线在直角坐标、参数方程、极坐标三种表示下的弧长。
来源: 01_Raw/Archive/Lectures/10_第10讲_一元函数积分学的应用(一).md
可信状态: S3 待核查
---

## 定义

用定积分计算光滑曲线在直角坐标、参数方程、极坐标三种表示下的弧长。

## 直角坐标方程

若光滑曲线由 $y = y(x) \, (a \leqslant x \leqslant b)$ 给出，则弧长为

$$
s = \int_a^b \sqrt{1 + [y'(x)]^2} \, \mathrm{d}x.
$$

## 参数方程

若光滑曲线由 $\begin{cases} x = x(t), \\ y = y(t) \end{cases} \, (\alpha \leqslant t \leqslant \beta)$ 给出，则弧长为

$$
s = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2} \, \mathrm{d}t.
$$

## 极坐标方程

若光滑曲线由 $r = r(\theta) \, (\alpha \leqslant \theta \leqslant \beta)$ 给出，则弧长为

$$
s = \int_\alpha^\beta \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} \, \mathrm{d}\theta.
$$

## 弧长微元

三种形式下的弧长微元 $\mathrm{d}s$：

| 坐标系 | 弧长微元 |
|--------|----------|
| 直角坐标 | $\mathrm{d}s = \sqrt{1 + (y')^2} \, \mathrm{d}x$ |
| 参数方程 | $\mathrm{d}s = \sqrt{(x')^2 + (y')^2} \, \mathrm{d}t$ |
| 极坐标 | $\mathrm{d}s = \sqrt{r^2 + (r')^2} \, \mathrm{d}\theta$ |

> [!TIP] 几何直觉
> 弧长计算公式的实质是将曲线切分成无数小直线段，用勾股定理求每段长度再求和。

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
