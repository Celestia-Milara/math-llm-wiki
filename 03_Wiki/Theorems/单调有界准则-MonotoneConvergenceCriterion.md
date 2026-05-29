---
标题: 单调有界准则
标签: [数学, 第2讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 单调有界数列必有极限，是证明数列收敛最重要的准则之一。
来源: 01_Raw/Archive/Lectures/02_第2讲_数列极限.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定理陈述

单调有界数列必有极限：

- **单调增加 + 有上界** $\Rightarrow$ 极限存在
- **单调减少 + 有下界** $\Rightarrow$ 极限存在

## 证明数列单调性的常用方法

### a. 作差法 / 作商法

- $x_{n+1} - x_n > 0$ 或 $\frac{x_{n+1}}{x_n} > 1$（同号时）$\Rightarrow$ 单调增加

### b. 数学归纳法

1. 验证 $n = 1$ 成立
2. 设 $n = k$ 成立
3. 证 $n = k+1$ 成立

### c. 利用重要不等式

如 $\mathrm{e}^x \ge x + 1$，$x - 1 \ge \ln x$，$\sin x \le x$ 等

### d. 递推函数单调性

若 $x_{n+1} = f(x_n)$：
- $f'(x) > 0$ $\Rightarrow$ $\{x_n\}$ 单调（$x_2 > x_1$ 时单调增，$x_2 < x_1$ 时单调减）
- $f'(x) < 0$ $\Rightarrow$ $\{x_n\}$ 不单调（可考虑压缩映射）

## 求极限

先证明收敛，再对递推式两边取极限，解方程得极限值。

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
