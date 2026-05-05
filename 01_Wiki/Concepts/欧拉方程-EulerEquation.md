---
标题: 欧拉方程
标签: [数学, 第15讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 具有 $x^2y''+pxy'+qy=f(x)$ 形式的变系数线性微分方程，可通过变量代换化为常系数线性微分方程求解。
来源: 00_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

形如

$$x^2\frac{\mathrm{d}^2y}{\mathrm{d}x^2} + px\frac{\mathrm{d}y}{\mathrm{d}x} + qy = f(x)$$

的方程称为**欧拉方程**，其中 $p, q$ 为常数，$f(x)$ 为已知连续函数。

## 解法思路

通过变量代换化为常系数线性微分方程：

当 $x > 0$ 时，令 $x = \mathrm{e}^t$，则 $t = \ln x$。

$$\begin{aligned}
\frac{\mathrm{d}y}{\mathrm{d}x} &= \frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t} \quad &\text{[链式法则]} \\
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} &= \frac{1}{x^2}\left(\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t}\right) \quad &\text{[二阶导数变换]}
\end{aligned}$$

代入原方程化为：

$$\frac{\mathrm{d}^2y}{\mathrm{d}t^2} + (p-1)\frac{\mathrm{d}y}{\mathrm{d}t} + qy = f(\mathrm{e}^t)$$

求解后以 $t = \ln x$ 回代。

> [!NOTE]
> 仅数学一要求掌握欧拉方程，但变换思想值得所有考生学习。

## 相关页面

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[ConstantCoefficientODE|常系数线性微分方程求解]]
- [[EulerEquationSolution|欧拉方程求解方法]]

---

```dataview
TABLE title, status, summary
FROM "01_Wiki"
WHERE contains(tags, "欧拉方程") OR contains(tags, "Euler")
SORT type ASC
```
