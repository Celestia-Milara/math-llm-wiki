---
标题: 积分中值定理（推广形式）
标签: [数学, 第11讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 推广的积分中值定理：带权函数的积分中值定理及其特殊形式。
来源: 01_Raw/Archive/Lectures/11_第11讲_一元函数积分学的应用(二).md
---
## 定理陈述


## 积分中值定理（基本形式）

设 $f(x)$ 在 $[a, b]$ 上连续，则至少存在一点 $\xi \in [a, b]$，使得

$$
\int_a^b f(x) \, \mathrm{d}x = f(\xi)(b - a).
$$

## 推广的积分中值定理

设 $f(x), g(x)$ 在 $[a, b]$ 上连续，且 $g(x)$ 在 $[a, b]$ 上不变号，则至少存在一点 $\xi \in [a, b]$，使得

$$
\int_a^b f(x) g(x) \, \mathrm{d}x = f(\xi) \int_a^b g(x) \, \mathrm{d}x.
$$

## 证明思路

当 $g(x) \neq 0$ 且不变号时（不妨设 $g(x) > 0$），令

$$
F(x) = \int_a^x f(t) g(t) \, \mathrm{d}t, \quad G(x) = \int_a^x g(t) \, \mathrm{d}t,
$$

在 $[a, b]$ 上应用柯西中值定理：

$$
\frac{F(b) - F(a)}{G(b) - G(a)} = \frac{F'(\xi)}{G'(\xi)} = \frac{f(\xi) g(\xi)}{g(\xi)} = f(\xi).
$$

## 注意事项

- 当 $g(x) = 1$ 时，推广形式退化为基本形式
- 当被积函数依赖于参数 $n$ 时，中值 $\xi$ 也与 $n$ 有关，记为 $\xi_n$
- 使用中值定理时需注意中值点的变化性

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/11_第11讲_一元函数积分学的应用(二).md`

```dataview
TABLE
  title as "名称",
  掌握状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
