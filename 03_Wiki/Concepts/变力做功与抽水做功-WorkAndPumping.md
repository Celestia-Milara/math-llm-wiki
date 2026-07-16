---
标题: 变力做功与抽水做功
标签: [数学, 第12讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 用定积分计算变力沿直线做功和抽水（提升液体）所做的功。
来源: 01_Raw/Archive/Lectures/12_第12讲_一元函数积分学的应用(三).md
可信状态: S3 待核查
---

## 变力沿直线做功

设方向沿 $x$ 轴正向的力函数为 $y = F(x) \, (a \leqslant x \leqslant b)$，则物体沿 $x$ 轴从点 $a$ 移动到点 $b$ 时，变力 $F(x)$ 所做的功为

$$
W = \int_a^b F(x) \, \mathrm{d}x.
$$

**功的微元**：$\mathrm{d}W = F(x) \, \mathrm{d}x$，表示小位移上的功。

## 抽水做功

将容器中的水全部抽出所做的功为

$$
W = \rho g \int_a^b x A(x) \, \mathrm{d}x,
$$

其中 $\rho$ 为水的密度，$g$ 为重力加速度，$A(x)$ 为 $x$ 处的水平截面面积。

**功的微元**：$\mathrm{d}W = \rho g x A(x) \, \mathrm{d}x$，表示位于 $x$ 处厚度为 $\mathrm{d}x$ 的一层水被抽出（路程为 $x$）所做的功。

### 解题步骤

1. 建立坐标系（对称、高为正方向）
2. 确定 $x$ 处的水平截面面积 $A(x)$
3. 取微元 $\mathrm{d}W = \rho g x A(x) \, \mathrm{d}x$
4. 积分 $W = \rho g \int_a^b x A(x) \, \mathrm{d}x$

> [!TIP] 几何直觉
> 抽水做功的本质是将每一薄层水"提升"到容器顶部，提升高度 $x$ 不同，做功也不同。

> [!WARNING] AI Generated
> 本页面由 AI 根据原始笔记自动编译，未经人工校核。

---

**来源**：`01_Raw/12_第12讲_一元函数积分学的应用(三).md`

```dataview
TABLE
  title as "名称",
  可信状态 as "状态",
  摘要 as "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1])
SORT file.name ASC
```
