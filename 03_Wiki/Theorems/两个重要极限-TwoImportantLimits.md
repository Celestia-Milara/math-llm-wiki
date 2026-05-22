---
标题: 两个重要极限
标签: [数学, 第1讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: sinx/x 和 (1+1/x)^x 是两个基础极限，广泛用于各类极限计算。
来源: 01_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。
## 定理陈述


## 第一个重要极限

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

广义化：$\displaystyle\lim_{\text{狗} \to 0} \frac{\sin \text{狗}}{\text{狗}} = 1$

## 第二个重要极限

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = \mathrm{e}, \quad \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = \mathrm{e}$$

广义化：$\displaystyle\lim_{\text{狗} \to \infty} \left(1 + \frac{1}{\text{狗}}\right)^{\text{狗}} = \mathrm{e}$

## $1^\infty$ 型简化公式

对于幂指函数 $u(x)^{v(x)}$ 的 $1^\infty$ 型极限：

$$\lim u^v = \mathrm{e}^{\lim (u-1)v}$$

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
