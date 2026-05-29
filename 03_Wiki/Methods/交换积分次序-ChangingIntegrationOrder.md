---
标题: 交换积分次序
标签: [数学, 第14讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 当一种积分次序无法直接计算时，通过重画积分区域来交换积分次序。
来源: 01_Raw/Archive/Lectures/14_第14讲_二重积分.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 何时需要交换积分次序

当累次积分无法直接计算时，考虑交换积分次序：

1. **被积函数没有初等函数形式的原函数**，例如：
   $$
   \frac{\sin x}{x},\; \frac{\cos x}{x},\; \frac{\ln(1+x)}{x},\; \frac{1}{\ln x},\;
   \sin x^2,\; \cos x^2,\; \sin\frac{1}{x},\; \cos\frac{1}{x},\;
   \frac{\mathrm{e}^x}{x},\; \mathrm{e}^{ax^2+bx+c}\;(a \neq 0)
   $$

2. **被积函数仅含 $x$（或仅含 $y$）**，换序后可先积另一变量将其作为常数提取

## 交换步骤

1. **确定积分区域** $D$：从原累次积分的上下限还原 $D$ 的边界
2. **画区域图**：准确画出 $D$ 的图形
3. **按新次序定限**：用另一类型的区域表达式写出新的累次积分

## 典型模式

### 模式一：从 X 型换为 Y 型

$$
\int_a^b \mathrm{d}x \int_{\varphi_1(x)}^{\varphi_2(x)} f(x, y)\,\mathrm{d}y
\;\Longrightarrow\;
\int_c^d \mathrm{d}y \int_{\psi_1(y)}^{\psi_2(y)} f(x, y)\,\mathrm{d}x.
$$

### 模式二：被积函数仅含 $x$

$$
\int_c^d \mathrm{d}y \int_{x_1(y)}^{x_2(y)} f(x)\,\mathrm{d}x
\;\Longrightarrow\;
\int_a^b f(x)\,\mathrm{d}x \int_{y_1(x)}^{y_2(x)} \mathrm{d}y
= \int_a^b f(x)\,[y_2(x) - y_1(x)]\,\mathrm{d}x.
$$

## 注意事项

- 交换上下限时添加负号以保证上限 $\geq$ 下限
- 注意分段区域的处理
- 先画出积分区域图是关键

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
