---
标题: 奇偶性
标签: [数学, 第1讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 函数在对称定义域上的对称性质，是四大特性中最常考的性质。
来源: 01_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 定义

设 $f(x)$ 的定义域 $D$ 关于原点对称：
- **偶函数**：$f(-x) = f(x)$，图形关于 $y$ 轴对称
- **奇函数**：$f(-x) = -f(x)$，图形关于原点对称

## 基本构造

- $f(x) + f(-x)$ 必是偶函数（如 $\frac{\mathrm{e}^x + \mathrm{e}^{-x}}{2}$）
- $f(x) - f(-x)$ 必是奇函数（如 $\frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2}$）

> 任一函数均可写成一个奇函数与一个偶函数之和：
> $$f(x) = \frac{1}{2}[f(x) + f(-x)] + \frac{1}{2}[f(x) - f(-x)]$$

## 复合函数奇偶性

**内偶则偶，内奇同外**：

| 内层 | 外层 | 复合结果 |
|------|------|----------|
| 偶   | 任意 | 偶       |
| 奇   | 奇   | 奇       |
| 奇   | 偶   | 偶       |
| 偶   | 偶   | 偶       |

## 导数与积分的奇偶性

- $f(x)$ 奇 $\Rightarrow f'(x)$ 偶 $\Rightarrow f''(x)$ 奇（求导一次奇偶性互换）
- $f(x)$ 奇 $\Rightarrow \int_0^x f(t)\,dt$ 偶

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
