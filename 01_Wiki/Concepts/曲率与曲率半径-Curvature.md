---
title: 曲率与曲率半径（Curvature and Curvature Radius）
tags: [数学, 第5讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 描述曲线弯曲程度的度量，曲率越大弯曲程度越大，曲率半径为曲率的倒数。
source: 00_Raw/05_第5讲_一元函数微分学的应用(一).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 曲率公式

设 $y(x)$ 二阶可导，则曲线 $y = y(x)$ 在点 $(x, y(x))$ 处的曲率为：

$$
k = \frac{|y''|}{\left[1 + (y')^2\right]^{3/2}}
$$

## 曲率半径

曲率半径 $R$ 是曲率的倒数：

$$
R = \frac{1}{k} = \frac{\left[1 + (y')^2\right]^{3/2}}{|y''|} \quad (y'' \neq 0)
$$

> 曲线弯曲程度越大，曲率越大，曲率半径越小。

## 参数方程形式的曲率

若曲线由参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$ 给出，则：

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{y'_t}{x'_t}, \qquad
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{y'_t}{x'_t}\right) \cdot \frac{1}{x'_t}
$$

代入曲率公式计算。

---

**来源**：`00_Raw/05_第5讲_一元函数微分学的应用(一).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
