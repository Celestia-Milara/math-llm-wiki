---
标题: 欧拉方程求解方法
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 通过变量代换 $x = \mathrm{e}^t$ 将欧拉方程化为常系数线性微分方程求解。
来源: 00_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 欧拉方程形式

$$x^2\frac{\mathrm{d}^2y}{\mathrm{d}x^2} + px\frac{\mathrm{d}y}{\mathrm{d}x} + qy = f(x)$$

## 解法步骤

### 当 $x > 0$ 时

令 $x = \mathrm{e}^t$，即 $t = \ln x$。

$$\begin{aligned}
\frac{\mathrm{d}y}{\mathrm{d}x} &= \frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t} \quad &\text{[一阶导数变换]} \\
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} &= \frac{1}{x^2}\left(\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t}\right) \quad &\text{[二阶导数变换]}
\end{aligned}$$

代入得：

$$\frac{\mathrm{d}^2y}{\mathrm{d}t^2} + (p-1)\frac{\mathrm{d}y}{\mathrm{d}t} + qy = f(\mathrm{e}^t)$$

求解后以 $t = \ln x$ 回代。

### 当 $x < 0$ 时

令 $x = -\mathrm{e}^t$，同理可得。

## 示例

欧拉方程 $x^2 y'' + 4xy' + 2y = 0\;(x > 0)$：

令 $x = \mathrm{e}^t$ 后化为 $\dfrac{\mathrm{d}^2y}{\mathrm{d}t^2} + 3\dfrac{\mathrm{d}y}{\mathrm{d}t} + 2y = 0$，通解为 $y = C_1\mathrm{e}^{-t} + C_2\mathrm{e}^{-2t} = \dfrac{C_1}{x} + \dfrac{C_2}{x^2}$。

## 相关页面

- [[EulerEquation|欧拉方程]]
- [[ConstantCoefficientODE|常系数线性微分方程求解]]

---

```dataview
TABLE title, type, summary
FROM "01_Wiki"
WHERE contains(tags, "欧拉方程") OR contains(tags, this.file.tags[1])
SORT type ASC
```
