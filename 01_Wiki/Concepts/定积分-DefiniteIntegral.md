---
标题: 定积分
标签: [数学, 第8讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 定积分是黎曼和的极限，表示曲边梯形面积的代数和。
来源: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 定义

若函数 $f(x)$ 在区间 $[a,b]$ 上有界，在 $(a,b)$ 上任取 $n-1$ 个分点，记 $\Delta x_k = x_k - x_{k-1}$，$\lambda = \max\{\Delta x_k\}$，任取 $\xi_k \in [x_{k-1}, x_k]$，若极限
$$\lim_{\lambda \to 0} \sum_{k=1}^n f(\xi_k)\Delta x_k$$
存在且与分点及 $\xi_k$ 的取法无关，则称 $f(x)$ 在 $[a,b]$ 上**可积**，记作
$$\int_a^b f(x)\,\mathrm{d}x$$

## 几何意义

- 若 $f(x) \ge 0$：表示曲线 $y=f(x)$、$x=a$、$x=b$ 与 $x$ 轴所围曲边梯形的面积。
- 若 $f(x) \le 0$：表示曲边梯形面积的负值。
- 若 $f(x)$ 有正有负：表示 $x$ 轴上方面积减去下方面积（面积的代数和）。

![](d7ced49f1716c9856408e2e84e71b3e46d52ca8d36aa02d7f0e5cfc6ce66d41f.jpg)

## 精确定义（特殊取法）

将 $[a,b]$ 等分并取右端点：
$$\int_a^b f(x)\,\mathrm{d}x = \lim_{n\to\infty} \sum_{i=1}^n f\!\left(a + \frac{b-a}{n}i\right)\frac{b-a}{n}$$

## 两个规定

1. $\int_a^a f(x)\,\mathrm{d}x = 0$
2. $\int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$（当 $a>b$ 时）

## 定积分的值与被积函数及积分区间有关，与积分变量记法无关

$$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t = \int_a^b f(u)\,\mathrm{d}u$$

---

## Dataview

```dataview
TABLE 
  status as "状态",
  summary as "摘要"
FROM #数学 AND (#定理 OR #方法) 
WHERE contains(file.name, "定积分") OR contains(tags, "定积分")
SORT file.name ASC
```
