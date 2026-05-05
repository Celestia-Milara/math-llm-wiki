---
标题: 第一型曲面积分
标签: [数学, 第18讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 第一型曲面积分（对面积的曲面积分）是定义在曲面上的数量函数积分，物理背景为曲面薄片的质量。
来源: 00_Raw/18_第18讲_多元函数积分学
---

## 定义

设曲面 $\Sigma$ 光滑，$f(x, y, z)$ 在 $\Sigma$ 上有界，将 $\Sigma$ 分成 $n$ 个小块 $\Delta S_i$，$(\xi_i, \eta_i, \zeta_i)$ 为上任一点，作和 $\sum f(\xi_i, \eta_i, \zeta_i) \Delta S_i$. 当各小块直径最大值 $\lambda \to 0$ 时极限存在，则称为 $f(x, y, z)$ 在 $\Sigma$ 上的第一型曲面积分：
$$
\iint_{\Sigma} f(x, y, z) \, \mathrm{d}S = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i, \zeta_i) \Delta S_i.
$$

**物理意义**：面密度为 $\mu(x, y, z)$ 的曲面薄片的质量 $M = \iint_{\Sigma} \mu(x, y, z) \, \mathrm{d}S$.

## 性质

1. **求曲面面积**：$\iint_{\Sigma} 1 \, \mathrm{d}S = A$.
2. **线性性质**、**可加性**、**保号性**、**估值定理**、**中值定理**与二重积分类似.

## 对称性

### 普通对称性
若 $\Sigma$ 关于 $xOz$ 面对称，则
$$
\iint_{\Sigma} f(x, y, z) \, \mathrm{d}S = 
\begin{cases}
2 \iint_{\Sigma_1} f(x, y, z) \, \mathrm{d}S, & f\text{关于}y\text{为偶函数}, \\
0, & f\text{关于}y\text{为奇函数}.
\end{cases}
$$

### 轮换对称性
当 $\Sigma: z = z(x, y)$ 为单值函数时，对调 $x, y$ 后 $\Sigma$ 不变，则积分值不变。

## 与二重积分的对比

| 二重积分 | 第一型曲面积分 |
|---------|--------------|
| 定义在平面区域 $D$ 上 | 定义在空间曲面 $\Sigma$ 上 |
| $\mathrm{d}\sigma = \mathrm{d}x\mathrm{d}y$ | $\mathrm{d}S = \sqrt{1 + (z_x')^2 + (z_y')^2}\,\mathrm{d}x\mathrm{d}y$ |

## 相关页面

- [[第一型曲面积分计算方法-SurfaceIntegralFirstKindMethods]]
- [[第一型曲线积分-LineIntegralFirstKind]]
- [[第二型曲面积分-SurfaceIntegralSecondKind]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1]) OR contains(tags, "曲面积分")
SORT file.name
```
