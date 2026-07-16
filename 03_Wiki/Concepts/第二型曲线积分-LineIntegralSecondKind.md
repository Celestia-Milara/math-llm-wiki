---
标题: 第二型曲线积分
标签: [数学, 第18讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 第二型曲线积分（对坐标的曲线积分）是向量函数沿有向曲线的积分，物理背景为变力沿曲线做功。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
可信状态: S3 待核查
---

## 物理背景

在变力 $\boldsymbol{F}(x, y) = P(x, y)\boldsymbol{i} + Q(x, y)\boldsymbol{j}$ 作用下，质点沿有向曲线 $L$ 从 $A$ 到 $B$ 所做的功为
$$
W = \int_L \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{s} = \int_L P(x, y) \, \mathrm{d}x + Q(x, y) \, \mathrm{d}y.
$$

## 定义

第二型曲线积分的被积函数 $\boldsymbol{F}(x, y) = P(x, y)\boldsymbol{i} + Q(x, y)\boldsymbol{j}$ 定义在平面有向曲线 $L$ 上：
$$
\int_L P(x, y) \, \mathrm{d}x + Q(x, y) \, \mathrm{d}y.
$$

与第一型曲线积分的本质区别：第二型曲线积分是向量函数沿有向曲线的积分，具有方向性，无几何量可言。

## 性质

1. **线性性质**：$\int_{\Gamma} (k_1 \boldsymbol{F}_1 \pm k_2 \boldsymbol{F}_2) \cdot \mathrm{d}\boldsymbol{s} = k_1 \int_{\Gamma} \boldsymbol{F}_1 \cdot \mathrm{d}\boldsymbol{s} \pm k_2 \int_{\Gamma} \boldsymbol{F}_2 \cdot \mathrm{d}\boldsymbol{s}$.
2. **有向性**：$\int_{\widehat{AB}} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{s} = -\int_{\widehat{BA}} \boldsymbol{F} \cdot \mathrm{d}\boldsymbol{s}$.
3. **可加性**：路径可分段积分。

> [!WARNING] AI Generated
> 第二型曲线积分没有几何意义上的对称性。由于方向的存在，不能直接套用第一型曲线积分的对称性结论，需要根据方向的具体分量判断数值上的抵消或叠加。

## 相关页面

- [[第二型曲线积分计算方法-LineIntegralSecondKindMethods]]
- [[第一型曲线积分-LineIntegralFirstKind]]
- [[格林公式-GreensTheorem]]
- [[曲线积分与路径无关-PathIndependence]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "曲线积分")
SORT file.name
```
