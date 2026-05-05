---
标题: 相关变化率（Related Rates）
标签: [数学, 第7讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 通过已知变化率求解未知变化率的链式法则应用，涉及参变量之间通过导数相互关联。
来源: 00_Raw/07_第7讲_一元函数微分学的应用(三).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 定义

若函数 $y = f(x)$ 由参数方程 $\begin{cases} x = x(t), \\ y = y(t) \end{cases}$ 确定且可导，则

$$
\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{\mathrm{d}y}{\mathrm{d}x} \cdot \frac{\mathrm{d}x}{\mathrm{d}t} = f'(x) \frac{\mathrm{d}x}{\mathrm{d}t}
$$

$\frac{\mathrm{d}y}{\mathrm{d}t}$ 与 $\frac{\mathrm{d}x}{\mathrm{d}t}$ 由 $f'(x)$ 联系在一起，这种相互关联的变化率称为**相关变化率**。

## 通用方法

$$
\frac{\mathrm{d}A}{\mathrm{d}C} = \frac{\frac{\mathrm{d}A}{\mathrm{d}B}}{\frac{\mathrm{d}C}{\mathrm{d}B}}
$$

通过已知变化率求未知变化率。

## 解题步骤

1. **建立相关变量方程**：写出问题中各变量之间的函数关系。
2. **求导找出相关变化率**：对时间 $t$ 求导，用链式法则建立变化率之间的关系。
3. **代入已知量求解**：将已知点处的数值代入，求出未知变化率。

---

**来源**：`00_Raw/07_第7讲_一元函数微分学的应用(三).md`

```dataview
TABLE status, type FROM #数学 WHERE contains(tags, this.file.tags[1]) SORT file.name ASC
```
