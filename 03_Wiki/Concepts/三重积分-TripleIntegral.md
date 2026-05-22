---
标题: 三重积分
标签: [数学, 第18讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 三重积分是定义在空间有界闭区域上、通过分割-近似-求和-取极限得到的积分，物理意义为空间物体的质量。
来源: 01_Raw/18_第18讲_多元函数积分学.md
---

## 定义

设 $f(x, y, z)$ 是空间有界闭区域 $\Omega$ 上的有界函数，将 $\Omega$ 任意分成 $n$ 个小闭区域 $\Delta v_1, \Delta v_2, \dots, \Delta v_n$，在每个 $\Delta v_i$ 上任取一点 $(\xi_i, \eta_i, \zeta_i)$，作和 $\sum_{i=1}^n f(\xi_i, \eta_i, \zeta_i) \Delta v_i$。当各小区域直径最大值 $\lambda \to 0$ 时，若极限存在且与分割取点无关，则称此极限为 $f(x, y, z)$ 在 $\Omega$ 上的三重积分：
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i, \zeta_i) \Delta v_i.
$$

若 $f$ 在 $\Omega$ 上连续，则三重积分一定存在。

**物理意义**：体密度为 $\rho(x, y, z)$ 的物体 $\Omega$ 的质量 $M = \iiint_{\Omega} \rho(x, y, z) \, \mathrm{d}v$.

## 性质

1. **求体积**：$\iiint_{\Omega} 1 \, \mathrm{d}v = V$.
2. **线性性质**：$\iiint_{\Omega} [k_1 f \pm k_2 g] \, \mathrm{d}v = k_1 \iiint_{\Omega} f \, \mathrm{d}v \pm k_2 \iiint_{\Omega} g \, \mathrm{d}v$.
3. **可加性**：$\Omega = \Omega_1 \cup \Omega_2$ 不交时，积分可拆分。
4. **保号性**：$f \leq g \;\Rightarrow\; \iiint_{\Omega} f \, \mathrm{d}v \leq \iiint_{\Omega} g \, \mathrm{d}v$.
5. **估值定理**：$m V \leq \iiint_{\Omega} f \, \mathrm{d}v \leq M V$.
6. **中值定理**：存在 $(\xi, \eta, \zeta) \in \Omega$ 使 $\iiint_{\Omega} f \, \mathrm{d}v = f(\xi, \eta, \zeta) V$.

## 对称性

### 普通对称性
若 $\Omega$ 关于 $xOz$ 面对称，则
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = 
\begin{cases}
2 \iiint_{\Omega_1} f(x, y, z) \, \mathrm{d}v, & f(x, y, z) = f(x, -y, z), \\
0, & f(x, y, z) = -f(x, -y, z).
\end{cases}
$$

### 轮换对称性
若将 $x$ 与 $y$ 对调后 $\Omega$ 不变，则 $\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = \iiint_{\Omega} f(y, x, z) \, \mathrm{d}v$。

例如球体 $\Omega: x^2 + y^2 + z^2 \leq R^2$ 有 $\iiint_{\Omega} f(x) \, \mathrm{d}v = \iiint_{\Omega} f(y) \, \mathrm{d}v = \iiint_{\Omega} f(z) \, \mathrm{d}v$。

## 相关页面

- [[三重积分计算方法-TripleIntegralMethods]]
- [[第一型曲线积分-LineIntegralFirstKind]]
- [[格林公式-GreensTheorem]]

```dataview
TABLE
  掌握状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "三重积分")
SORT file.name
```
