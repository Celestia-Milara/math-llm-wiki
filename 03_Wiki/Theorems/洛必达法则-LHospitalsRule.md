---
标题: 洛必达法则
标签: [数学, 第1讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 在满足条件下，通过分子分母分别求导来计算 0/0 或 ∞/∞ 型未定式的极限。
来源: 01_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。
## 定理陈述


## 法则一（$\frac{0}{0}$ 型）

设：
1. $x \to a$（或 $x \to \infty$）时，$f(x)$ 及 $F(x)$ 都趋于零
2. $f'(x)$ 及 $F'(x)$ 在 $a$ 的某去心邻域内存在且 $F'(x) \neq 0$
3. $\lim \frac{f'(x)}{F'(x)}$ 存在或为无穷大

则：

$$\lim \frac{f(x)}{F(x)} = \lim \frac{f'(x)}{F'(x)}$$

## 法则二（$\frac{\infty}{\infty}$ 型）

将条件 1 中的"趋于零"改为"趋于无穷大"，结论相同。

## 注意事项

1. **仅适用于 $\frac{0}{0}$ 或 $\frac{\infty}{\infty}$ 型**，其他类型需先变形
2. **可多次使用**，只要仍满足条件
3. **右存在是左存在的充分条件，非必要条件**：若洛必达后极限不存在，原极限仍可能存在
   - 反例：$\lim_{x \to 0} \frac{x^2 \sin\frac{1}{x}}{x} = 0$，但洛必达后极限不存在

## 无穷大量比阶

当 $x \to +\infty$ 时：
$$\ln^\alpha x \ll x^\beta \ll a^x \quad (\alpha, \beta > 0, a > 1)$$

当 $n \to \infty$ 时：
$$\ln^\alpha n \ll n^\beta \ll a^n \ll n! \ll n^n \quad (\alpha, \beta > 0, a > 1)$$

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
