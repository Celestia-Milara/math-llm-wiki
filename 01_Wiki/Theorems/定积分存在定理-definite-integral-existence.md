---
title: 定积分存在定理
tags: [数学, 第8讲, 定理]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 定积分存在的充分条件和必要条件，包括连续、单调、有界等情形。
source: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 充分条件

若 $f(x)$ 满足以下条件之一，则 $\int_a^b f(x)\,\mathrm{d}x$ 存在：

1. **$f(x)$ 在 $[a,b]$ 上连续**
2. **$f(x)$ 在 $[a,b]$ 上单调**
3. **$f(x)$ 在 $[a,b]$ 上有界，且只有有限个间断点**（不包含无穷间断点）
4. **$f(x)$ 在 $[a,b]$ 上有有限个第一类间断点**

## 必要条件

若定积分 $\int_a^b f(x)\,\mathrm{d}x$ 存在，则 $f(x)$ 在 $[a,b]$ 上**必有界**。

## 不定积分与定积分存在性对比

| 函数类型 | 不定积分（原函数） | 定积分（黎曼可积） |
|:--------|:-----------------|:-----------------|
| 连续函数 | 存在 | 存在 |
| 有界、有限个第一类间断点 | **不存在** | **存在** |
| 有界、振荡间断点 | 可能存在 | **存在** |
| 无界函数 | 不存在 | 不存在 |
| 单调函数 | 不一定 | 存在 |

---

## Dataview

```dataview
TABLE 
  status as "状态",
  summary as "摘要"
FROM "01_Wiki/Theorems"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
