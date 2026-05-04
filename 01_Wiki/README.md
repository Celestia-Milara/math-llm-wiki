# 01_Wiki - 结构化知识层

这是知识库的核心，由 AI 根据 `00_Raw` 编译而成。

## 子文件夹

### Concepts/ - 核心概念
存放数学定义、概念解释。

示例：
- [[导数-Derivative]]
- [[极限-Limit]]
- [[连续性-Continuity]]

### Theorems/ - 定理与证明
存放数学定理、引理、推论及其证明。

示例：
- [[中值定理-MeanValueTheorem]]
- [[泰勒公式-TaylorFormula]]
- [[格林公式-GreensTheorem]]

### Methods/ - 解题方法
存放解题套路、技巧、常见题型分析。

示例：
- [[换元积分法-SubstitutionMethod]]
- [[分部积分法-IntegrationByParts]]
- [[洛必达法则-LHopitalsRule]]

## 创建规范
每个 Wiki 页面必须包含 Frontmatter：
```yaml
---
title: [中文名称]
tags: [数学, 章节名, 类型]
created: YYYY-MM-DD
type: permanent
summary: 用一句话概括该定义或定理的核心思想。
---
```
