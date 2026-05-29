---
标题: 弹性（Elasticity）
标签: [数学, 第7讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 因变量对自变量变化的反应灵敏度的度量，即相对变化率的比值。
来源: 01_Raw/Archive/Lectures/07_第7讲_一元函数微分学的应用(三).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定义

设函数 $y = f(x)$ 可导，称

$$
\eta = \lim_{\Delta x \to 0} \frac{\Delta y}{y} \Bigg/ \frac{\Delta x}{x} = \frac{x}{y} y' = \frac{x}{f(x)} f'(x)
$$

为函数 $y = f(x)$ 的**弹性函数**。

在 $x_0$ 处的（点）弹性：

$$
\eta|_{x=x_0} = \frac{x_0}{f(x_0)} f'(x_0)
$$

**经济意义**：在 $x_0$ 处，当自变量 $x$ 改变 $1\%$ 时，因变量 $y$ 将改变 $|\eta|_{x=x_0}|\%$。

## 常见弹性类型

### 需求的价格弹性

$$
\eta_d = \frac{EQ}{Ep} = \frac{p}{Q} \frac{\mathrm{d}Q}{\mathrm{d}p} = \frac{p}{Q(p)} Q'(p)
$$

需求函数单调减少，故 $Q'(p) < 0$，从而 $\eta_d < 0$。其经济意义：当价格为 $p$ 时，若提价 $1\%$，则需求量将减少 $|\eta_d|\%$。

> 若题设要求 $\eta_d > 0$，则取 $\eta_d = -\frac{p}{Q(p)} Q'(p)$。

### 供给的价格弹性

$$
\eta_s = \frac{Eq}{Ep} = \frac{p}{q} \frac{\mathrm{d}q}{\mathrm{d}p} = \frac{p}{q(p)} q'(p)
$$

供给函数单调增加，$q'(p) > 0$，故 $\eta_s > 0$。

### 收益的价格弹性

$$
\eta_r = \frac{ER}{Ep} = \frac{p}{R} \frac{\mathrm{d}R}{\mathrm{d}p}
$$

## 弹性与收益的关系

由 $R(p) = pQ(p)$ 可得：

$$
\frac{\mathrm{d}R}{\mathrm{d}p} = Q(1 - \eta)
$$

- 当 $\eta < 1$（缺乏弹性）时，$\frac{\mathrm{d}R}{\mathrm{d}p} > 0$，提价使收益增加。
- 当 $\eta > 1$（富有弹性）时，$\frac{\mathrm{d}R}{\mathrm{d}p} < 0$，提价使收益减少。
- 当 $\eta = 1$（单位弹性）时，收益达到最大。

---

**来源**：`01_Raw/07_第7讲_一元函数微分学的应用(三).md`

```dataview
TABLE 掌握状态, 类型 FROM "03_Wiki" WHERE contains(标签, this.标签[1]) SORT file.name ASC
```
