---
标题: 线性微分方程
标签: [数学, 第15讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 未知函数及其各阶导数均以线性形式出现的微分方程，包括齐次与非齐次、常系数与变系数情形。
来源: 01_Raw/15_第15讲_微分方程.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

形如

$$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = f(x)$$

的微分方程称为 $n$ 阶**线性微分方程**，其中 $a_k(x)\;(k=0,1,\dots,n)$ 是自变量 $x$ 的函数，$a_n(x) \neq 0$。

## 分类

### 常系数 vs 变系数

当 $a_k(x)\;(k=0,1,\dots,n)$ 均为常数时，称为 $n$ 阶**常系数线性微分方程**。

### 齐次 vs 非齐次

- 若右端函数 $f(x) \equiv 0$，称为 $n$ 阶**齐次线性微分方程**。
- 若 $f(x) \not\equiv 0$，称为 $n$ 阶**非齐次线性微分方程**。

## 相关概念

- [[OrdinaryDifferentialEquation|常微分方程]]
- [[线性微分方程解的结构-StructureOfLinearODESolutions|线性微分方程解的结构]]
- [[ConstantCoefficientODE|常系数线性微分方程求解]]

---

```dataview
TABLE title, 掌握状态, 摘要
FROM "03_Wiki"
WHERE contains(标签, "线性微分方程") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
