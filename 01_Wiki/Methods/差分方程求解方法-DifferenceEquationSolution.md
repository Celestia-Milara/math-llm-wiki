---
title: 差分方程求解方法
tags: [数学, 第15讲, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 一阶常系数线性差分方程 $y_{t+1} + ay_t = f(t)$ 的齐次解与非齐次特解的设定与求解。
source: 00_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 齐次差分方程

$$y_{t+1} + ay_t = 0$$

通解：$y_C(t) = C \cdot (-a)^t$，$C$ 为任意常数。

## 非齐次差分方程

$$y_{t+1} + ay_t = f(t)$$

通解 = 齐次通解 + 非齐次特解。

### 特解设定表

| $f(t)$ 形式 | 条件 | 特解形式 |
|---|---|---|
| $f(t) = d^t \cdot P_m(t)$ | $a + d \neq 0$ | $y_t^* = d^t \cdot Q_m(t)$ |
| | $a + d = 0$ | $y_t^* = t \cdot d^t \cdot Q_m(t)$ |
| $f(t) = b_1\cos\omega t + b_2\sin\omega t$ | $D \neq 0$ | $y_t^* = \alpha\cos\omega t + \beta\sin\omega t$ |
| | $D = 0$ | $y_t^* = t(\alpha\cos\omega t + \beta\sin\omega t)$ |

其中 $D = \begin{vmatrix} a+\cos\omega & \sin\omega \\ -\sin\omega & a+\cos\omega \end{vmatrix}$。

### 叠加原理

若 $\bar{y}_t$ 是 $y_{t+1}+ay_t = f_1(t)$ 的解，$\tilde{y}_t$ 是 $y_{t+1}+ay_t = f_2(t)$ 的解，则 $\bar{y}_t + \tilde{y}_t$ 是 $y_{t+1}+ay_t = f_1(t)+f_2(t)$ 的解。

> [!NOTE]
> 差分方程仅数学三要求，考频较低，考前记公式即可。

## 相关页面

- [[DifferenceEquation|差分与差分方程]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, "差分") OR contains(tags, this.file.tags[1])
SORT type ASC
```
