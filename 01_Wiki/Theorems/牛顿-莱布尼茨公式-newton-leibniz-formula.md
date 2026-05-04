---
title: 牛顿-莱布尼茨公式
tags: [数学, 第9讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 沟通定积分与不定积分的桥梁，将定积分计算转化为原函数在端点处的差值。
source: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 基本公式

设函数 $F(x)$ 是连续函数 $f(x)$ 在 $[a,b]$ 上的一个原函数，则
$$\int_a^b f(x)\,\mathrm{d}x = F(x)\Big|_a^b = F(b) - F(a)$$

## 推广形式

1. **有原函数但区间内有间断点**：若 $f(x)$ 在 $[a,b]$ 上有原函数 $F(x)$，公式仍成立。
2. **分段有原函数**：若 $[a,c)$ 上有原函数 $F_1(x)$，$(c,b]$ 上有原函数 $F_2(x)$，则
   $$\int_a^b f(x)\,\mathrm{d}x = [F_1(c-0)-F_1(a)] + [F_2(b)-F_2(c+0)]$$
   若 $F_1(c-0),F_2(c+0)$ 至少一个不存在，则积分发散。

## 注意事项

> [!WARNING]
> 牛顿-莱布尼茨公式要求 $F(x)$ 在 $[a,b]$ 上确实是 $f(x)$ 的原函数。当被积函数有间断点时，需小心处理——"分段有原函数"需分段使用公式，不能在整个区间上直接套用。

例如 $\int_0^{\frac{3}{4}\pi} \frac{1}{1+\cos^2 x}\,\mathrm{d}x$ 中，$\frac{1}{\sqrt{2}}\arctan\frac{\tan x}{\sqrt{2}}$ 在 $x=\frac{\pi}{2}$ 处无意义，需分段积分。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Methods" AND "01_Wiki/Concepts"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
