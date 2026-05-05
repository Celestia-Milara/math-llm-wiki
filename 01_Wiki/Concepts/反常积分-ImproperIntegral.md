---
标题: 反常积分
标签: [数学, 第8讲, 第9讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 破坏定积分两个必要条件（区间有限、函数有界）的积分，分为无穷区间和无界函数两类。
来源: 00_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 分类

定积分存在有两个必要条件：① 积分区间有限；② 被积函数有界。破坏其中任意一条即引出反常积分。

$$
\left\{
\begin{array}{l}
\text{定积分（常义积分）}
\begin{cases}
\text{区间有限} \\
\text{被积函数有界}
\end{cases} \\[6pt]
\text{反常积分（广义积分）}
\begin{cases}
\text{无穷区间上的反常积分} \\
\text{无界函数的反常积分（瑕积分）}
\end{cases}
\end{array}
\right.
$$

## 无穷区间上的反常积分

设 $F(x)$ 是 $f(x)$ 的一个原函数。

1. $\int_a^{+\infty} f(x)\,\mathrm{d}x = \lim_{x\to +\infty} F(x) - F(a)$
2. $\int_{-\infty}^b f(x)\,\mathrm{d}x = F(b) - \lim_{x\to -\infty} F(x)$
3. $\int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = \int_{-\infty}^{x_0} f(x)\,\mathrm{d}x + \int_{x_0}^{+\infty} f(x)\,\mathrm{d}x$（右端两个积分均收敛才收敛）

## 无界函数的反常积分（瑕积分）

设 $x_0$ 为瑕点（$f(x)$ 在该点邻域内无界）。

1. $x=a$ 为唯一瑕点：$\int_a^b f(x)\,\mathrm{d}x = F(b) - \lim_{x\to a^+} F(x)$
2. $x=b$ 为唯一瑕点：$\int_a^b f(x)\,\mathrm{d}x = \lim_{x\to b^-} F(x) - F(a)$
3. $x=c\in(a,b)$ 为唯一瑕点：拆分后分别处理

**不存在**"发散 $+$ 发散 $=$ 收敛"的情形。

## 奇点

"$\infty$" 和瑕点统称为**奇点**。在判别敛散性时，一个积分中只能有一个奇点，出现两个及以上奇点需拆分。

---

## Dataview

```dataview
TABLE 
  status as "状态",
  summary as "摘要"
FROM #数学 AND (#定理 OR #方法) 
WHERE contains(file.name, "反常积分") OR contains(tags, "反常积分")
SORT file.ctime ASC
```
