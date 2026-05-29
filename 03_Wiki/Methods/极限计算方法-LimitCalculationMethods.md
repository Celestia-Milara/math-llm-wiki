---
标题: 极限计算方法
标签: [数学, 第1讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 总结七种未定式的系统化解题流程：化简、判断、选择方法。
来源: 01_Raw/Archive/Lectures/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 解题三步法

### ① 化简先行

- 提出极限不为 0 的因式
- 等价无穷小代换
- 恒等变形：提公因式、拆项、合并、分子分母同除最高次幂、变量代换

### ② 判断类型

七种未定式：$\frac{0}{0}$、$\frac{\infty}{\infty}$、$0 \cdot \infty$、$\infty - \infty$、$1^\infty$、$\infty^0$、$0^0$

### ③ 选择方法

| 类型 | 推荐方法 |
|------|----------|
| $\frac{0}{0}$ | 洛必达、泰勒公式、等价无穷小 |
| $\frac{\infty}{\infty}$ | 洛必达、抓大头（同除最高次幂） |
| $0 \cdot \infty$ | 将简单因式放分母，化为 $\frac{0}{0}$ 或 $\frac{\infty}{\infty}$ |
| $\infty - \infty$ | 有分母则通分；无分母则倒代换或提公因式 |
| $1^\infty$ | 简化公式 $\lim u^v = \mathrm{e}^{\lim (u-1)v}$ |
| $\infty^0$ / $0^0$ | 恒等变形 $u^v = \mathrm{e}^{v\ln u}$，化为前三种 |

## 核心工具

1. **极限四则运算法则**
2. **洛必达法则**
3. **泰勒公式**（最强大，用于 $\frac{0}{0}$ 型）
4. **两个重要极限**
5. **夹逼准则**

## 常见技巧

### 幂指函数处理
$$u(x)^{v(x)} = \mathrm{e}^{v(x)\ln u(x)}$$

### 脱帽法
若 $\lim f(x) = A$，则 $f(x) = A + \alpha(x)$，其中 $\lim \alpha(x) = 0$

### $\mathrm{e}^\infty$ 需分左右
遇到 $\mathrm{e}^{\frac{1}{x-a}}$，必须讨论 $x \to a^+$ 和 $x \to a^-$

### 抓大头
$x \to \infty$ 时只看最高次项；$x \to 0$ 时只看最低次项

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
