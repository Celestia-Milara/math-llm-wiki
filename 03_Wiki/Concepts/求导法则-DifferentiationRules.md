---
标题: 求导法则
标签: [数学, 第4讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 四则运算、复合函数、反函数、隐函数、参数方程、对数求导法等求导方法汇总。
来源: 01_Raw/Archive/Lectures/04_第4讲_一元函数微分学的计算.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 可信状态 改为 S2 已核查。

## 基本求导公式

$(x^\alpha)' = \alpha x^{\alpha-1}$，$(a^x)' = a^x \ln a$，$(\mathrm{e}^x)' = \mathrm{e}^x$

$(\log_a x)' = \frac{1}{x\ln a}$，$(\ln |x|)' = \frac{1}{x}$

$(\sin x)' = \cos x$，$(\cos x)' = -\sin x$，$(\tan x)' = \sec^2 x$，$(\cot x)' = -\csc^2 x$

$(\sec x)' = \sec x \tan x$，$(\csc x)' = -\csc x \cot x$

$(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$，$(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$

$(\arctan x)' = \frac{1}{1+x^2}$，$(\operatorname{arccot} x)' = -\frac{1}{1+x^2}$

$[\ln(x+\sqrt{x^2+1})]' = \frac{1}{\sqrt{x^2+1}}$

## 四则运算法则

- $(u \pm v)' = u' \pm v'$
- $(uv)' = u'v + uv'$
- $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

## 复合函数求导（链式法则）

$$\{f[g(x)]\}' = f'[g(x)] \cdot g'(x)$$

## 一阶微分形式不变性

无论 $u$ 是中间变量还是自变量，$\mathrm{d}[f(u)] = f'(u)\,\mathrm{d}u$ 都成立。

## 分段函数求导

- 分段点处用导数定义（左/右导数）
- 非分段点处用导数公式

## 反函数求导

设 $y = f(x)$ 可导且 $f'(x) \neq 0$，反函数 $x = \varphi(y)$，则

$$\varphi'(y) = \frac{1}{f'(x)},\quad \varphi''(y) = -\frac{f''(x)}{[f'(x)]^3}$$

## 隐函数求导

方程 $F(x, y) = 0$ 两边对 $x$ 求导，将 $y$ 视为中间变量，解出 $y'$。

## 参数方程求导

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\psi'(t)}{\varphi'(t)},\quad \frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\psi''(t)\varphi'(t) - \psi'(t)\varphi''(t)}{[\varphi'(t)]^3}$$

## 对数求导法

用于多项相乘、相除、开方、乘方的式子：取对数 $\ln y = \ln f(x)$，再对 $x$ 求导。

## 幂指函数求导

$$u(x)^{v(x)} = \mathrm{e}^{v(x)\ln u(x)}$$ 再按复合函数求导。

## 相关条目

```dataview
TABLE 可信状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
