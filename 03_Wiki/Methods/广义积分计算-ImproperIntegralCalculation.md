---
标题: 广义积分计算
标签: [数学, 第9讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 识别奇点、拆分区间，在收敛条件下利用定积分方法计算广义积分。
来源: 01_Raw/Archive/Lectures/09_第9讲_一元函数积分学的计算.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验.

## 计算步骤

1. **识别奇点**：找出所有 $\infty$ 和瑕点（使函数无界的点）
2. **拆分区间**：每个区间内只有一个奇点
3. **分段处理**：在每个区间上计算或判别敛散性
4. **取极限**：利用极限计算得到最终值

## 关键技巧

### 1. 收敛条件下的换元

在收敛的条件下，通过换元可以实现广义积分与定积分的相互转化。

### 2. Gamma 函数

对于形如 $\int_0^{+\infty} x^n \mathrm{e}^{-x}\,\mathrm{d}x$ 的积分：
$$\int_0^{+\infty} x^n \mathrm{e}^{-x}\,\mathrm{d}x = \Gamma(n+1) = n!$$

更一般地：
$$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1}\mathrm{e}^{-x}\,\mathrm{d}x$$

### 3. 递推式

分部积分法可能建立递推式 $I_n = f(I_{n-1})$，适用于含参数 $n$ 的广义积分。

## 对称区间上的广义积分

- 偶函数：$\int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = 2\int_0^{+\infty} f(x)\,\mathrm{d}x$（右端收敛时）
- 奇函数：$\int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = 0$（右端收敛时）

> [!WARNING]
> 只有在广义积分收敛时，才有 $\int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = \lim_{R\to +\infty}\int_{-R}^R f(x)\,\mathrm{d}x$。例如 $\int_{-\infty}^{+\infty} x^3\,\mathrm{d}x$ 发散而不是 $0$。

---

## Dataview

```dataview
TABLE 
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki/Concepts" AND "03_Wiki/Theorems"
WHERE contains(标签, "广义积分")
SORT file.name ASC
```
