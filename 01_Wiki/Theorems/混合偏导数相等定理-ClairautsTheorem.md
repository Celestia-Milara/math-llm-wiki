---
标题: 混合偏导数相等定理（Clairaut 定理）
标签: [数学, 第13讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 在连续性条件下，二阶混合偏导数与求导次序无关。
来源: 00_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定理内容

若函数 $z = f(x, y)$ 的两个二阶混合偏导数 $\frac{\partial^2 z}{\partial x \partial y}$ 及 $\frac{\partial^2 z}{\partial y \partial x}$ 都在区域 $D$ 内连续，则在 $D$ 内有

$$
\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial^2 z}{\partial y \partial x},
$$

即二阶混合偏导数在连续的条件下与求导的次序无关。

## 应用

该定理常用于以下场景：

1. **验证全微分存在性**：若 $\mathrm{d}u = P(x, y)\mathrm{d}x + Q(x, y)\mathrm{d}y$，且 $P_y' = Q_x'$（在偏导连续条件下），则可判定 $\mathrm{d}u$ 是某个函数的全微分
2. **简化计算**：在复合函数求导中，利用混合偏导相等可检验计算结果
3. **反问题**：已知混合偏导关系反求原函数

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
