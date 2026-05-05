---
标题: 夹逼准则
标签: [数学, 第1讲, 定理]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 若 f(x) 被 h(x) 和 g(x) 夹在中间且两端极限相等，则 f(x) 极限存在且等于该值。
来源: 00_Raw/01_第1讲_函数极限与连续.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定理

如果函数 $f(x)$、$g(x)$ 及 $h(x)$ 满足：

1. $h(x) \leqslant f(x) \leqslant g(x)$
2. $\lim g(x) = \lim h(x) = A$

则 $\lim f(x)$ 存在，且 $\lim f(x) = A$。

## 注意事项

$\lim [g(x) - h(x)] = 0$ **不能**推出 $\lim f(x)$ 一定存在，因为 $\lim g(x)$ 和 $\lim h(x)$ 可能都不存在。

## 典型应用

当常规方法（等价无穷小、泰勒公式、洛必达法则）无法使用时，夹逼准则是重要突破口。常用于含 `[x]` 取整函数或振荡函数的极限。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
