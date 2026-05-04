---
title: 积分等式与不等式
tags: [数学, 第11讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 涉及积分形式的中值定理、夹逼准则求积分极限及积分不等式的证明方法。
source: 00_Raw/11_第11讲_一元函数积分学的应用(二).md
---

## 积分等式

积分等式问题主要涉及：
- 积分形式的中值定理（推广的积分中值定理）
- 用夹逼准则求一类积分的极限
- 用分部积分法证明特殊的积分等式

## 积分不等式

积分不等式问题的证明方法包括：

| 方法 | 适用条件 |
|------|----------|
| 函数的单调性 | $f(x)$ 在 $[a,b]$ 上连续 |
| 拉格朗日中值定理 | $f(x)$ 一阶可导，端点值简单（常为0） |
| 泰勒公式 | $f(x)$ 二阶可导，有简单函数值 |
| 分部积分法 | 被积函数为两项相乘 |
| 牛顿-莱布尼茨公式 | 需建立 $f(x)$ 与导数积分的关系 |

## 重要结论

设 $f(x)$ 在 $[0,1]$ 上连续，则

$$
\lim_{n \to \infty} \int_0^1 x^n f(x) \, \mathrm{d}x = 0.
$$

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`00_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  status as "状态",
  summary as "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
