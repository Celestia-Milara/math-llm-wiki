---
标题: 直角坐标计算二重积分
标签: [数学, 第14讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 在直角坐标系下将二重积分化为累次积分，分为 X 型区域和 Y 型区域两种情形。
来源: 01_Raw/Archive/Lectures/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 基本思想

在直角坐标系下，$\mathrm{d}\sigma = \mathrm{d}x\,\mathrm{d}y$，将二重积分化为先对 $x$ 或先对 $y$ 的累次积分。

## X 型区域

区域 $D$ 表示为：$\varphi_1(x) \leq y \leq \varphi_2(x),\; a \leq x \leq b$。

特征：穿过 $D$ 内部且平行于 $y$ 轴的直线与 $D$ 的边界相交不多于两点。

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \int_a^b \mathrm{d}x \int_{\varphi_1(x)}^{\varphi_2(x)} f(x, y)\,\mathrm{d}y.
$$

> **后积 $x$** —— 先确定 $x$ 的范围，再对 $y$ 积分。

## Y 型区域

区域 $D$ 表示为：$\psi_1(y) \leq x \leq \psi_2(y),\; c \leq y \leq d$。

特征：穿过 $D$ 内部且平行于 $x$ 轴的直线与 $D$ 的边界相交不多于两点。

$$
\iint_D f(x, y)\,\mathrm{d}\sigma = \int_c^d \mathrm{d}y \int_{\psi_1(y)}^{\psi_2(y)} f(x, y)\,\mathrm{d}x.
$$

> **后积 $y$** —— 先确定 $y$ 的范围，再对 $x$ 积分。

## 积分次序选择原则

| 考虑因素 | 优先选择的次序 |
|----------|---------------|
| 被积函数易对 $y$ 积分 | 先 $y$ 后 $x$（X 型） |
| 被积函数易对 $x$ 积分 | 先 $x$ 后 $y$（Y 型） |
| 区域是 X 型但非 Y 型 | 先 $y$ 后 $x$ |
| 区域是 Y 型但非 X 型 | 先 $x$ 后 $y$ |

## 关键点

- **画区域图**：确定积分限的关键是准确画出 $D$ 的边界图形
- **下限 $\leq$ 上限**：$\mathrm{d}x > 0,\; \mathrm{d}y > 0,\; \mathrm{d}\sigma > 0$
- **分段处理**：若区域形状复杂，可分成多个子区域分别积分后相加

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
