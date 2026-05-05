---
标题: 高阶导数
标签: [数学, 第3讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 对函数多次求导，描述变化率的变化率乃至更高阶信息。
来源: 00_Raw/03_第3讲_一元函数微分学的概念.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 定义

$$f''(x_0) = \lim_{\Delta x \to 0} \frac{f'(x_0 + \Delta x) - f'(x_0)}{\Delta x}$$

$$f^{(n)}(x_0) = \lim_{\Delta x \to 0} \frac{f^{(n-1)}(x_0 + \Delta x) - f^{(n-1)}(x_0)}{\Delta x}$$

## 记号

- $f'(x), f''(x), f'''(x)$
- $n \ge 4$ 时写为 $f^{(n)}(x)$

## 重要结论

- $f''(x_0)$ 存在 $\Rightarrow$ $f'(x)$ 在 $x_0$ 附近有定义且在 $x_0$ 处连续
- $f^{(n)}(x_0)$ 存在 $\Rightarrow$ $f^{(n-1)}(x)$ 在 $x_0$ 附近有定义且在 $x_0$ 处连续

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
