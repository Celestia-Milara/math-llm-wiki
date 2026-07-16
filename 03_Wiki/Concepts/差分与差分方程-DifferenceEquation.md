---
标题: 差分与差分方程
标签: [数学, 第15讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 离散变量函数的差分运算及以一阶常系数线性差分方程为代表的求解理论。
来源: 01_Raw/Archive/Lectures/15_第15讲_微分方程.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

设函数 $y_t = f(t),\; t = 0, \pm 1, \pm 2, \dots$。

**一阶差分**定义为：

$$\Delta y_t = y_{t+1} - y_t = f(t+1) - f(t)$$

**二阶差分**定义为：

$$\Delta^2 y_t = \Delta(\Delta y_t) = \Delta y_{t+1} - \Delta y_t = y_{t+2} - 2y_{t+1} + y_t$$

## 一阶常系数线性差分方程

一般形式为：

$$y_{t+1} + ay_t = f(t)$$

其中 $f(t)$ 为已知函数，$a$ 为非零常数。

### 齐次差分方程

$$y_{t+1} + ay_t = 0$$

通解为 $y_C(t) = C \cdot (-a)^t$，$C$ 为任意常数。

### 非齐次差分方程

若 $y_t^*$ 是一个特解，$y_C(t)$ 是齐次通解，则非齐次通解为：

$$y_t = y_C(t) + y_t^*$$

## 相关页面

- [[03_Wiki/Concepts/常微分方程-OrdinaryDifferentialEquation|常微分方程]]
- [[03_Wiki/Methods/差分方程求解方法-DifferenceEquationSolution|差分方程求解方法]]

---

```dataview
TABLE title, 可信状态, 摘要
FROM "03_Wiki"
WHERE contains(标签, "差分") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
