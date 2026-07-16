---
标题: Gamma函数
标签: [数学, 第9讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 一种重要的特殊函数，用于快速计算含指数幂的反常积分，具有递推性质。
来源: 01_Raw/Archive/Lectures/09_第9讲_一元函数积分学的计算.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 定义

$$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1} \mathrm{e}^{-x}\,\mathrm{d}x \quad (\alpha > 0)$$

等价形式（令 $x=t^2$）：
$$\Gamma(\alpha) = 2\int_0^{+\infty} t^{2\alpha-1} \mathrm{e}^{-t^2}\,\mathrm{d}t$$

## 核心性质

1. **递推式**：$\Gamma(\alpha+1) = \alpha\,\Gamma(\alpha)$
2. **特殊值**：
   - $\Gamma(1) = 1$
   - $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
3. **整数阶**：$\Gamma(n+1) = n!$（$n$ 为非负整数）
4. **半整数阶示例**：$\Gamma\left(\frac{5}{2}\right) = \frac{3}{2}\cdot\frac{1}{2}\cdot\Gamma\left(\frac{1}{2}\right) = \frac{3}{4}\sqrt{\pi}$

## 应用

Gamma 函数在计算形如 $\int_0^{+\infty} x^n \mathrm{e}^{-x}\,\mathrm{d}x$ 的反常积分时极为高效：
$$\int_0^{+\infty} x^n \mathrm{e}^{-x}\,\mathrm{d}x = \Gamma(n+1) = n!$$

> [!TIP]
> Gamma 函数的递推性使其成为处理含 $\mathrm{e}^{-x}$ 和幂函数乘积极限的利器，尤其是与 $\sqrt{\pi}$ 相关的半整数阶结果值得牢记。

---

## Dataview

```dataview
TABLE 
  可信状态 as "状态"
FROM "03_Wiki"
WHERE contains(file.name, "广义积分") OR contains(标签, "广义积分")
SORT file.ctime ASC
```
