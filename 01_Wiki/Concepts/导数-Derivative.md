---
标题: 导数
标签: [数学, 第3讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 函数在某点处的瞬时变化率，描述函数值随自变量变化的快慢。
来源: 00_Raw/03_第3讲_一元函数微分学的概念.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

设 $y = f(x)$ 在 $x_0$ 的某邻域内有定义，给 $x_0$ 一个增量 $\Delta x$，若极限

$$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

存在，则称 $f(x)$ 在 $x_0$ 处可导。

### 等价形式

$$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

### 广义化

$$f'(x_0) = \lim_{\text{狗} \to 0} \frac{f(x_0 + \text{狗}) - f(x_0)}{\text{狗}}$$

## 单侧导数

- **左导数**：$f'_-(x_0) = \lim_{\Delta x \to 0^-} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$
- **右导数**：$f'_+(x_0) = \lim_{\Delta x \to 0^+} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$

> **可导充要条件**：$f'(x_0)$ 存在 $\iff$ $f'_-(x_0)$ 与 $f'_+(x_0)$ 均存在且相等

## 可导与连续的关系

**可导 $\Rightarrow$ 连续**，反之不真（如 $f(x) = |x|$ 在 $x=0$ 处连续但不可导）。

## 导数与函数特性

- 可导偶函数 $\Rightarrow$ $f'(x)$ 是奇函数
- 可导奇函数 $\Rightarrow$ $f'(x)$ 是偶函数
- 可导周期函数 $\Rightarrow$ $f'(x)$ 同周期
- 每求导一次，奇偶性互换一次

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
