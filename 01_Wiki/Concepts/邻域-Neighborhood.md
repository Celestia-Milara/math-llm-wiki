---
标题: 邻域
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 描述点 x₀"附近"的区间概念，是极限定义的几何基础。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

### $\delta$ 邻域

设 $x_0$ 是数轴上一个点，$\delta$ 是某一正数，则称 $(x_0 - \delta, x_0 + \delta)$ 为点 $x_0$ 的 $\delta$ 邻域，记作 $U(x_0, \delta)$：

$$U(x_0, \delta) = \{x \mid x_0 - \delta < x < x_0 + \delta\} = \{x \mid |x - x_0| < \delta\}$$

### 去心邻域

$$\bar{U}(x_0, \delta) = \{x \mid 0 < |x - x_0| < \delta\}$$

### 左、右邻域

- **右邻域** $U^+(x_0, \delta) = \{x \mid 0 < x - x_0 < \delta\}$
- **左邻域** $U^-(x_0, \delta) = \{x \mid 0 < x_0 - x < \delta\}$

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
