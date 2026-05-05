---
标题: 变限积分求导公式
标签: [数学, 第9讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 对积分上限和下限都是函数的变限积分求导的方法。
来源: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 求导公式

设 $F(x) = \int_{\varphi_1(x)}^{\varphi_2(x)} f(t)\,\mathrm{d}t$，其中 $f$ 连续，$\varphi_1,\varphi_2$ 可导，则

$$F'(x) = \frac{\mathrm{d}}{\mathrm{d}x}\left[\int_{\varphi_1(x)}^{\varphi_2(x)} f(t)\,\mathrm{d}t\right] = f[\varphi_2(x)]\,\varphi_2'(x) - f[\varphi_1(x)]\,\varphi_1'(x)$$

## 注意事项

> [!WARNING]
> 当被积函数中含有"求导变量 $x$"时，不能直接套用公式。必须通过恒等变形（如变量代换）将 $x$ 移出被积函数后才能求导。

例如：$\frac{\mathrm{d}}{\mathrm{d}x}\int_x^{x^2} f(xt)\,\mathrm{d}t$ 需先令 $u=xt$ 换元再求导。

## 重要结论（关于奇偶性与周期性）

1. 若 $f$ 为可积的奇函数，则 $\int_0^x f(t)\,\mathrm{d}t$ 为偶函数；$\int_a^x f(t)\,\mathrm{d}t$ 也为偶函数。
2. 若 $f$ 为可积的偶函数，则 $\int_0^x f(t)\,\mathrm{d}t$ 为奇函数。
3. 若 $f$ 为可积且以 $T$ 为周期的函数，则 $\int_0^x f(t)\,\mathrm{d}t$ 以 $T$ 为周期 $\iff \int_0^T f(x)\,\mathrm{d}x = 0$。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Concepts"
WHERE contains(tags, "变限积分")
SORT file.name ASC
```
