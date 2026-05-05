---
标题: 数量场与向量场
标签: [数学, 第17讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 场是空间区域上的对应法则，数量场对应标量函数，向量场对应向量函数。
来源: 00_Raw/17_第17讲_多元函数积分学的预备知识
---

## 数量场

如果空间区域 $\Omega$ 上的每一点 $M(x, y, z)$ 都对应着一个数量 $u$，则确定了一个数量函数 $u = u(x, y, z)$，表示一个**数量场**。

> 数量场只讲大小，不讲方向。例如温度场。

## 向量场

如果空间区域 $\Omega$ 上的每一点 $M(x, y, z)$ 都对应着一个向量 $\boldsymbol{F}$，则确定了一个向量函数
$$
\boldsymbol{F}(x, y, z) = P(x, y, z)\boldsymbol{i} + Q(x, y, z)\boldsymbol{j} + R(x, y, z)\boldsymbol{k},
$$
表示一个**向量场**。

> 向量场既讲大小，也讲方向。例如引力场、电场、磁场、流速场。

## 相关概念
- 数量场的梯度 $\rightarrow$ [[方向导数与梯度-DirectionalDerivativeAndGradient]]
- 向量场的散度、旋度 $\rightarrow$ [[散度与旋度-DivergenceAndCurl]]

```dataview
TABLE
  status AS "状态",
  summary AS "摘要"
FROM "01_Wiki"
WHERE contains(tags, this.file.tags[1])
SORT file.name
```
