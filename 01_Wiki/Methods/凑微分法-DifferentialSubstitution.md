---
标题: 凑微分法
标签: [数学, 第9讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 将一部分被积函数放入微分号d后面，形成复合函数结构以简化积分。
来源: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 基本原理

$$\int f[g(x)]\,g'(x)\,\mathrm{d}x = \int f[g(x)]\,\mathrm{d}[g(x)] = \int f(u)\,\mathrm{d}u$$

若能代入基本积分公式，则凑微分成功。

## 常用凑微分公式

$$\begin{aligned}
&x\,\mathrm{d}x = \frac12\mathrm{d}(x^2), \quad
\sqrt{x}\,\mathrm{d}x = \frac23\mathrm{d}\!\left(x^{\frac32}\right), \quad
\frac{\mathrm{d}x}{\sqrt{x}} = 2\mathrm{d}(\sqrt{x}), \\[4pt]
&\frac{\mathrm{d}x}{x^2} = \mathrm{d}\!\left(-\frac1x\right), \quad
\frac{\mathrm{d}x}{x} = \mathrm{d}(\ln x)\;(x>0), \quad
\mathrm{e}^x\mathrm{d}x = \mathrm{d}(\mathrm{e}^x), \\[4pt]
&\sin x\,\mathrm{d}x = \mathrm{d}(-\cos x), \quad
\cos x\,\mathrm{d}x = \mathrm{d}(\sin x), \\[4pt]
&\sec^2 x\,\mathrm{d}x = \mathrm{d}(\tan x), \quad
\csc^2 x\,\mathrm{d}x = \mathrm{d}(-\cot x), \\[4pt]
&\frac{\mathrm{d}x}{1+x^2} = \mathrm{d}(\arctan x), \quad
\frac{\mathrm{d}x}{\sqrt{1-x^2}} = \mathrm{d}(\arcsin x).
\end{aligned}$$

## 技巧

当不是标准凑微分公式时，对被积函数的复杂部分 $g(x)$ 求导，看是否满足 $\mathrm{d}[g(x)] = g'(x)\,\mathrm{d}x$ 等于被积函数中的某部分。

> [!TIP]
> 凑微分的核心思路是"选择复杂部分放入 $\mathrm{d}$ 后面"。判断标准：放入后能否代换成基本积分公式中的形式。

---

## Dataview

```dataview
TABLE 
  status as "状态"
FROM "01_Wiki/Concepts"
WHERE contains(tags, this.file.tags[1]) AND contains(tags, "概念")
SORT file.name ASC
```
