---
标题: 压缩映射原理
标签: [数学, 第2讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 当递推函数满足 Lipschitz 常数小于 1 时，数列收敛于不动点。
来源: 01_Raw/Archive/Lectures/02_第2讲_数列极限.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。
## 定理陈述


## 原理一

对数列 $\{x_n\}$，若存在常数 $k \in (0, 1)$，使得 $|x_{n+1} - a| \le k|x_n - a|$，则 $\{x_n\}$ 收敛于 $a$。

## 原理二

若 $x_{n+1} = f(x_n)$，$a$ 是 $f(x) = x$ 的唯一解，且对任意 $x \in \mathbb{R}$ 有 $|f'(x)| \le k < 1$，则 $\{x_n\}$ 收敛于 $a$。

证明：由拉格朗日中值定理，$|x_{n+1} - a| = |f(x_n) - f(a)| = |f'(\xi)| \cdot |x_n - a| \le k|x_n - a|$，再由原理一得证。

## 典型应用

当 $f$ 单调递减时，数列不单调，压缩映射是证明收敛的主要方法（如 $x_{n+1} = \cos x_n$）。

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
