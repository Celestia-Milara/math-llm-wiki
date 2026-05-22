---
标题: 定积分性质
标签: [数学, 第8讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 定积分的线性性、可加性、保号性、估值定理和中值定理。
来源: 01_Raw/08_第8讲_一元函数积分学的概念与性质.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。
## 定理陈述


## 性质1：区间长度

若 $a<b$，则
$$\int_a^b \mathrm{d}x = b-a = L$$
其中 $L$ 为区间 $[a,b]$ 的长度。

## 性质2：线性性质

设 $k_1,k_2$ 为常数，则
$$\int_a^b [k_1 f(x) \pm k_2 g(x)]\,\mathrm{d}x = k_1\int_a^b f(x)\,\mathrm{d}x \pm k_2\int_a^b g(x)\,\mathrm{d}x$$

## 性质3：积分区间的可加性

无论 $a,b,c$ 的大小如何，总有
$$\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$$

## 性质4：保号性

若在 $[a,b]$ 上 $f(x) \le g(x)$，则
$$\int_a^b f(x)\,\mathrm{d}x \le \int_a^b g(x)\,\mathrm{d}x$$
特殊地，
$$\left|\int_a^b f(x)\,\mathrm{d}x\right| \le \int_a^b |f(x)|\,\mathrm{d}x$$

> 若 $f(x)$ 是 $[a,b]$ 上非负的连续函数且不恒等于零，则必有 $\int_a^b f(x)\,\mathrm{d}x > 0$。

## 性质5：估值定理

设 $M,m$ 分别是 $f(x)$ 在 $[a,b]$ 上的最大值和最小值，$L=b-a$，则
$$mL \le \int_a^b f(x)\,\mathrm{d}x \le ML$$

## 性质6：积分中值定理

设 $f(x)$ 在 $[a,b]$ 上连续，则在 $[a,b]$ 上至少存在一点 $\xi$，使得
$$\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$$

**证明**：由估值定理得 $m \le \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x \le M$，再由介值定理即得。

> [!TIP]
> 可证明 $\xi \in (a,b)$ 而非闭区间：令 $F(x)=\int_a^x f(t)\,\mathrm{d}t$ 并在 $[a,b]$ 上用拉格朗日中值定理即可。

---

## Dataview

```dataview
TABLE 
  掌握状态 as "状态"
FROM "03_Wiki/Methods"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
