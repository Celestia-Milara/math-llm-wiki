---
标题: 第一型曲线积分
标签: [数学, 第18讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 第一型曲线积分（对弧长的曲线积分）是定义在曲线弧上的数量函数积分，物理背景为曲线质量。
来源: 01_Raw/18_第18讲_多元函数积分学.md
---

## 定义

设 $L$ 为 $xOy$ 面内光滑曲线弧，$f(x, y)$ 在 $L$ 上有界，将 $L$ 分成 $n$ 个小弧段，$\Delta s_i$ 为第 $i$ 段弧长，$(\xi_i, \eta_i)$ 为上任一点，作和 $\sum f(\xi_i, \eta_i) \Delta s_i$. 当各小弧段长度最大值 $\lambda \to 0$ 时极限存在，则称为 $f(x, y)$ 在 $L$ 上的第一型曲线积分：
$$
\int_L f(x, y) \, \mathrm{d}s = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i) \Delta s_i.
$$

可推广至空间曲线 $\Gamma$：$\int_{\Gamma} f(x, y, z) \, \mathrm{d}s$.

> 第一型曲线积分的弧微分 $\mathrm{d}s = \sqrt{(\mathrm{d}x)^2 + (\mathrm{d}y)^2 + (\mathrm{d}z)^2}$.

## 性质

1. **求弧长**：$\int_{\Gamma} 1 \, \mathrm{d}s = l_{\Gamma}$.
2. **线性性质**：$\int_{\Gamma} (k_1 f \pm k_2 g) \, \mathrm{d}s = k_1 \int_{\Gamma} f \, \mathrm{d}s \pm k_2 \int_{\Gamma} g \, \mathrm{d}s$.
3. **可加性**：$\Gamma = \Gamma_1 \cup \Gamma_2$ 可分段积分.
4. **保号性**、**估值定理**、**中值定理**与二重/三重积分类似.

## 对称性

### 普通对称性
若 $\Gamma$ 关于 $xOz$ 面对称，则
$$
\int_{\Gamma} f(x, y, z) \, \mathrm{d}s = 
\begin{cases}
2 \int_{\Gamma_1} f(x, y, z) \, \mathrm{d}s, & f\text{关于}y\text{为偶函数}, \\
0, & f\text{关于}y\text{为奇函数}.
\end{cases}
$$

### 轮换对称性
对调 $x, y$ 后 $\Gamma$ 不变，则 $\int_{\Gamma} f(x, y, z) \, \mathrm{d}s = \int_{\Gamma} f(y, x, z) \, \mathrm{d}s$.

## 与定积分的对比

| 定积分 | 第一型曲线积分 |
|-------|--------------|
| 定义在直线段 $[a, b]$ 上 | 定义在曲线弧 $L$ 上 |
| $\mathrm{d}x > 0$（$a < b$ 时） | $\mathrm{d}s > 0$（恒正） |
| 可代入直线方程 | 可代入曲线方程 |

## 相关页面

- [[第一型曲线积分计算方法-LineIntegralFirstKindMethods]]
- [[第一型曲面积分-SurfaceIntegralFirstKind]]
- [[第二型曲线积分-LineIntegralSecondKind]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "曲线积分")
SORT file.name
```
