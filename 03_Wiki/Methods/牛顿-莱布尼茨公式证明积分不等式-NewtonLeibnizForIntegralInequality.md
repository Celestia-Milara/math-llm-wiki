---
标题: 牛顿-莱布尼茨公式证明积分不等式
标签: [数学, 第11讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 利用牛顿-莱布尼茨公式联系函数值与导数的积分，证明积分不等式。
来源: 01_Raw/Archive/Lectures/11_第11讲_一元函数积分学的应用(二).md
可信状态: S3 待核查
---

## 方法概述

当需要建立 $f(x)$ 与 $\int_a^b f'(x) \, \mathrm{d}x$ 之间的关系时，牛顿-莱布尼茨公式是桥梁。

### 基本思路

1. 利用 $f(x) = f(x) - f(a) = \int_a^x f'(t) \, \mathrm{d}t$
2. 利用 $f(x) = f(x) - f(b) = \int_b^x f'(t) \, \mathrm{d}t = -\int_x^b f'(t) \, \mathrm{d}t$
3. 将两个表达式相加，消去方向性

## 典型例题

**条件**：$f'(x)$ 在 $[a, b]$ 上连续，$f(a) = f(b) = 0$.

**结论**：

$$
|f(x)| \leqslant \frac12 \int_a^b |f'(x)| \, \mathrm{d}x.
$$

**证明要点**：

$$
|f(x)| = \left| \int_a^x f'(t) \, \mathrm{d}t \right| \leqslant \int_a^x |f'(t)| \, \mathrm{d}t,
$$

$$
|f(x)| = \left| \int_b^x f'(t) \, \mathrm{d}t \right| = \left| \int_x^b f'(t) \, \mathrm{d}t \right| \leqslant \int_x^b |f'(t)| \, \mathrm{d}t.
$$

两式相加：

$$
2|f(x)| \leqslant \int_a^x |f'(t)| \, \mathrm{d}t + \int_x^b |f'(t)| \, \mathrm{d}t = \int_a^b |f'(t)| \, \mathrm{d}t.
$$

## 适用场景

- 函数端点值为 0
- 需将函数值与导数积分关联
- 被积函数含导数形式

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
