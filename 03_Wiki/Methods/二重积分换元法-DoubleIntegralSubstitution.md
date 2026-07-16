---
标题: 二重积分换元法
标签: [数学, 第14讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 通过变量代换将复杂的积分区域或被积函数简化，需乘雅可比行列式的绝对值。
来源: 01_Raw/Archive/Lectures/14_第14讲_二重积分.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 可信状态 改为 S2 已核查。

## 换元公式

设变换 $\begin{cases} x = x(u, v), \\ y = y(u, v) \end{cases}$ 是 $(x, y)$ 平面到 $(u, v)$ 平面的一对一映射，且 $x(u, v), y(u, v)$ 存在一阶连续偏导数，$J \neq 0$，则

$$
\iint_{D_{xy}} f(x, y)\,\mathrm{d}x\,\mathrm{d}y
= \iint_{D_{uv}} f[x(u, v), y(u, v)]\,
\left|\frac{\partial(x, y)}{\partial(u, v)}\right|
\,\mathrm{d}u\,\mathrm{d}v,
$$

其中雅可比行列式

$$
\frac{\partial(x, y)}{\partial(u, v)} =
\begin{vmatrix}
\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[8pt]
\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}
\end{vmatrix}.
$$

## "三换"要点

与一元换元法类似，需完成三处替换：

| 一元换元 | 二重换元 |
|----------|----------|
| $f(x) \to f[\varphi(t)]$ | $f(x, y) \to f[x(u, v), y(u, v)]$ |
| $\int_a^b \to \int_\alpha^\beta$ | $\iint_{D_{xy}} \to \iint_{D_{uv}}$ |
| $\mathrm{d}x \to \varphi'(t)\,\mathrm{d}t$ | $\mathrm{d}x\,\mathrm{d}y \to |J|\,\mathrm{d}u\,\mathrm{d}v$ |

## 特例：极坐标换元

$$
\begin{cases}
x = r\cos\theta,\\
y = r\sin\theta,
\end{cases}
\qquad
|J| =
\begin{vmatrix}
\cos\theta & -r\sin\theta \\
\sin\theta & r\cos\theta
\end{vmatrix} = r,
$$

故 $\mathrm{d}x\,\mathrm{d}y = r\,\mathrm{d}r\,\mathrm{d}\theta$。

## 典型应用

### 例：线性换元

当被积函数含有 $\displaystyle\frac{y}{x+y}$ 等形式时，可令

$$
\begin{cases}
x + y = u,\\
y = v,
\end{cases}
\quad\text{则}\quad
\begin{cases}
x = u - v,\\
y = v,
\end{cases}
\quad J =
\begin{vmatrix}
1 & -1\\
0 & 1
\end{vmatrix} = 1.
$$

换元后积分区域和被积函数同时简化。

## 相关条目

```dataview
TABLE 可信状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
