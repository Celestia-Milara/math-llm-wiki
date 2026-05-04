---
title: 基本积分公式
tags: [数学, 第9讲, 概念]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 不定积分计算的基础，所有积分方法最终都化为基本积分公式。
source: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

基本积分公式的由来：$[F(x)]' = f(x) \;\Rightarrow\; \int f(x)\,\mathrm{d}x = F(x) + C$。所有积分计算通过各种方法最后都化为基本积分公式。

## 10组基本公式

1. $\displaystyle\int x^k\,\mathrm{d}x = \frac{1}{k+1}x^{k+1}+C \;(k\neq -1)$

2. $\displaystyle\int \frac{1}{x}\,\mathrm{d}x = \ln|x|+C$

3. $\displaystyle\int \mathrm{e}^x\,\mathrm{d}x = \mathrm{e}^x+C$；$\displaystyle\int a^x\,\mathrm{d}x = \frac{a^x}{\ln a}+C \;(a>0,a\neq 1)$

4. **三角函数**
   $$\begin{aligned}
   &\int \sin x\,\mathrm{d}x = -\cos x+C,\quad \int \cos x\,\mathrm{d}x = \sin x+C, \\
   &\int \tan x\,\mathrm{d}x = -\ln|\cos x|+C,\quad \int \cot x\,\mathrm{d}x = \ln|\sin x|+C, \\
   &\int \sec x\,\mathrm{d}x = \ln|\sec x+\tan x|+C,\quad \int \csc x\,\mathrm{d}x = \ln|\csc x-\cot x|+C, \\
   &\int \sec^2 x\,\mathrm{d}x = \tan x+C,\quad \int \csc^2 x\,\mathrm{d}x = -\cot x+C, \\
   &\int \sec x\tan x\,\mathrm{d}x = \sec x+C,\quad \int \csc x\cot x\,\mathrm{d}x = -\csc x+C.
   \end{aligned}$$

5. $\displaystyle\int \frac{1}{1+x^2}\,\mathrm{d}x = \arctan x+C$；$\displaystyle\int \frac{1}{a^2+x^2}\,\mathrm{d}x = \frac{1}{a}\arctan\frac{x}{a}+C$

6. $\displaystyle\int \frac{1}{\sqrt{1-x^2}}\,\mathrm{d}x = \arcsin x+C$；$\displaystyle\int \frac{1}{\sqrt{a^2-x^2}}\,\mathrm{d}x = \arcsin\frac{x}{a}+C$

7. $\displaystyle\int \frac{1}{\sqrt{x^2+a^2}}\,\mathrm{d}x = \ln\!\left(x+\sqrt{x^2+a^2}\right)+C$；$\displaystyle\int \frac{1}{\sqrt{x^2-a^2}}\,\mathrm{d}x = \ln\!\left|x+\sqrt{x^2-a^2}\right|+C$

8. $\displaystyle\int \frac{1}{x^2-a^2}\,\mathrm{d}x = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C$

9. $\displaystyle\int \sqrt{a^2-x^2}\,\mathrm{d}x = \frac{a^2}{2}\arcsin\frac{x}{a}+\frac{x}{2}\sqrt{a^2-x^2}+C$

10. **平方化简**
    $$\begin{aligned}
    &\int \sin^2 x\,\mathrm{d}x = \frac{x}{2}-\frac{\sin 2x}{4}+C,\quad
    \int \cos^2 x\,\mathrm{d}x = \frac{x}{2}+\frac{\sin 2x}{4}+C, \\
    &\int \tan^2 x\,\mathrm{d}x = \tan x - x + C,\quad
    \int \cot^2 x\,\mathrm{d}x = -\cot x - x + C.
    \end{aligned}$$

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM #数学 AND (#方法) 
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
