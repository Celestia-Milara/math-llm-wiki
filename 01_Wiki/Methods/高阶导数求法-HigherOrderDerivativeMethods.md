---
标题: 高阶导数求法
标签: [数学, 第4讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 归纳法、莱布尼茨公式、泰勒展开式——三种求高阶导数的方法。
来源: 00_Raw/04_第4讲_一元函数微分学的计算.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 status 改为 practice_verified。

## 常用高阶导数公式

$$(\mathrm{e}^{ax+b})^{(n)} = a^n \mathrm{e}^{ax+b}$$
$$[\sin(ax+b)]^{(n)} = a^n \sin\left(ax+b + \frac{n\pi}{2}\right)$$
$$[\cos(ax+b)]^{(n)} = a^n \cos\left(ax+b + \frac{n\pi}{2}\right)$$
$$[\ln(ax+b)]^{(n)} = (-1)^{n-1} a^n \frac{(n-1)!}{(ax+b)^n}$$
$$\left(\frac{1}{ax+b}\right)^{(n)} = (-1)^n a^n \frac{n!}{(ax+b)^{n+1}}$$

## 方法一：归纳法

逐次求导，探索规律，得出通式。适合无现成公式可套的函数。

如 $(\sin x)^{(n)} = \sin\left(x + n\cdot\frac{\pi}{2}\right)$。

## 方法二：莱布尼茨公式

用于求两个函数乘积的高阶导数：

$$(uv)^{(n)} = \sum_{k=0}^n C_n^k u^{(n-k)} v^{(k)}$$

当其中一个函数是低次幂函数（如 $x, x^2$）时，项数很少。

## 方法三：泰勒展开式

利用泰勒展开的唯一性，通过比较系数求 $f^{(n)}(x_0)$：

$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n$$

将函数展开为幂级数，对比 $x^n$ 的系数即得 $\frac{f^{(n)}(0)}{n!}$。

## 相关条目

```dataview
TABLE status, type
FROM #数学
WHERE contains(tags, this.file.tags[1]) AND type != "permanent"
SORT file.name ASC
```
