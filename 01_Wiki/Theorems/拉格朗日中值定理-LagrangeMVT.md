---
title: 拉格朗日中值定理（Lagrange's Mean Value Theorem）
tags: [数学, 第6讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 可导函数在区间上某点的切线斜率等于区间两端点连线的斜率。
source: 00_Raw/06_第6讲_一元函数微分学的应用(二).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定理内容

设 $f(x)$ 满足：

1. 在 $[a,b]$ 上**连续**
2. 在 $(a,b)$ 内**可导**

则存在 $\xi \in (a,b)$，使得

$$
f'(\xi) = \frac{f(b) - f(a)}{b - a}
$$

即

$$
f(b) - f(a) = f'(\xi)(b - a)
$$

## 推论

若在区间 $(a,b)$ 上 $f'(x) \equiv 0$，则 $f(x)$ 在该区间上为常数。

## 应用

1. **用导函数的值控制函数值的增减**：见到 $f(a) - f(b)$ 或 $f$ 与 $f'$ 的关系，考虑拉格朗日中值定理。
2. **证明函数有界**：若 $f'(x)$ 在 $(a,b)$ 内有界，则 $f(x)$ 在 $(a,b)$ 内有界。
3. **证明不等式**：将函数差转化为导数值与区间长度的乘积进行放缩。
4. **与其它定理结合**：常与柯西中值定理结合使用。

---

**来源**：`00_Raw/06_第6讲_一元函数微分学的应用(二).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
