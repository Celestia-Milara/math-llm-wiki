---
title: 有理函数积分
tags: [数学, 第9讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 将有理真分式分解为最简有理分式之和再逐项积分。
source: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 基本思想

形如 $\displaystyle\int\frac{P_n(x)}{Q_m(x)}\,\mathrm{d}x\;(n<m)$ 的积分，将分母因式分解后，把被积函数拆成若干项**最简有理分式**之和。

若 $n \ge m$，先用多项式除法化为多项式 + 真分式。

## 因式分解与拆分规则

| 分母因式类型 | 拆分项 |
|:-----------|:------|
| 一次单因式 $ax+b$ | $\displaystyle\frac{A}{ax+b}$ |
| $k$ 重一次因式 $(ax+b)^k$ | $\displaystyle\frac{A_1}{ax+b}+\frac{A_2}{(ax+b)^2}+\cdots+\frac{A_k}{(ax+b)^k}$ |
| 二次单因式 $px^2+qx+r$ | $\displaystyle\frac{Ax+B}{px^2+qx+r}$ |
| $k$ 重二次因式 $(px^2+qx+r)^k$ | $\displaystyle\frac{A_1x+B_1}{px^2+qx+r}+\frac{A_2x+B_2}{(px^2+qx+r)^2}+\cdots+\frac{A_kx+B_k}{(px^2+qx+r)^k}$ |

## 待定系数法

两种方法求拆分后的系数：
1. **展开比较同次幂系数**（系统但较烦琐）
2. **赋特殊值法**（代入 $x$ 的适当值得到简单条件）

## 三角函数有理式

$R(\sin x,\cos x)$ 型，可用**万能公式**令 $t=\tan\frac{x}{2}$：

$$\sin x = \frac{2t}{1+t^2},\quad \cos x = \frac{1-t^2}{1+t^2},\quad \mathrm{d}x = \frac{2}{1+t^2}\,\mathrm{d}t$$

### 特殊情形简化

- $R(-\sin x,\cos x) = -R(\sin x,\cos x)$：令 $\cos x = t$
- $R(\sin x,-\cos x) = -R(\sin x,\cos x)$：令 $\sin x = t$
- $R(-\sin x,-\cos x) = R(\sin x,\cos x)$：令 $\tan x = t$

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Methods"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
