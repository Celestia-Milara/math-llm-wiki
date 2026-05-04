---
title: 图像变换
tags: [数学, 附录, 方法]
created: 2026-05-03
type: permanent
status: raw_compilation
summary: 函数图像的平移、伸缩、对称与翻折变换规则，以及基于隐式方程 F(x,y)=0 的对称性判别方法。
source: 00_Raw/19_附录1_图像变换.md
---

## 平移变换 (Translation)

- 沿 $x$ 轴向左平移 $x_0 > 0$ 个单位：$y = f(x) \;\rightarrow\; y = f(x + x_0)$
- 沿 $x$ 轴向右平移 $x_0 > 0$ 个单位：$y = f(x) \;\rightarrow\; y = f(x - x_0)$
- 沿 $y$ 轴向上平移 $y_0 > 0$ 个单位：$y = f(x) \;\rightarrow\; y = f(x) + y_0$
- 沿 $y$ 轴向下平移 $y_0 > 0$ 个单位：$y = f(x) \;\rightarrow\; y = f(x) - y_0$

## 对称变换 (Symmetry)

- 关于 $x$ 轴对称：$y = f(x) \;\rightarrow\; y = -f(x)$
- 关于 $y$ 轴对称：$y = f(x) \;\rightarrow\; y = f(-x)$
- 关于原点对称：$y = f(x) \;\rightarrow\; y = -f(-x)$
- 关于直线 $y = x$ 对称：$y = f(x) \;\rightarrow\; y = f^{-1}(x)$
- $y = |f(x)|$：保留 $x$ 轴及上方部分，将下方部分关于 $x$ 轴对称翻折到上方
- $y = f(|x|)$：保留 $y$ 轴及右侧部分，去掉左侧部分，再将右侧关于 $y$ 轴对称到左侧

## 伸缩变换 (Stretching/Compression)

- 水平伸缩：$y = f(kx)$
  - $k > 1$：横坐标缩短到原来的 $\dfrac{1}{k}$，纵坐标不变
  - $0 < k < 1$：横坐标伸长到原来的 $\dfrac{1}{k}$，纵坐标不变
- 垂直伸缩：$y = k f(x)$
  - $k > 1$：纵坐标伸长到原来的 $k$ 倍，横坐标不变
  - $0 < k < 1$：纵坐标缩短到原来的 $k$ 倍，横坐标不变

## 隐式方程的对称性判别

对于 $F(x, y) = f(x) - y = 0$，有以下对称性判据：

| 条件 | 对称性 |
|------|--------|
| $F(x, y) = F(-x, y)$ | 关于 $y$ 轴 ($x=0$) 对称 |
| $F(x, y) = F(2T - x, y)$ 或 $F(T+x, y) = F(T-x, y)$ | 关于 $x = T$ 对称 |
| $F(x, y) = F(x, -y)$ | 关于 $x$ 轴 ($y=0$) 对称 |
| $F(x, y) = F(x, 2T - y)$ 或 $F(x, T+y) = F(x, T-y)$ | 关于 $y = T$ 对称 |
| $F(x, y) = F(-x, -y)$ | 关于原点 $(0,0)$ 对称 |
| $F(a+x, y) = F(a-x, -y)$ | 关于点 $(a, 0)$ 对称 |
| $F(x, y) = F(y, x)$ | 关于直线 $y = x$ 对称 |

## 示例

**例 1** $y^2 = x^3 - x^4$：令 $F(x, y) = x^3 - x^4 - y^2$，则 $F(x, y) = F(x, -y)$，关于 $x$ 轴对称。

**例 2** $y^2 = (1 - x^2)^3$：令 $F(x, y) = (1 - x^2)^3 - y^2$，则
$$\begin{aligned}
F(x, y) &= F(-x, y) \quad &\text{[关于 } y \text{ 轴对称]} \\
F(x, y) &= F(x, -y) \quad &\text{[关于 } x \text{ 轴对称]} \\
F(x, y) &= F(-x, -y) \quad &\text{[关于原点对称]}
\end{aligned}$$

**例 3** $x^3 + y^3 - 3xy = 0$：令 $F(x, y) = x^3 + y^3 - 3xy$，则 $F(x, y) = F(y, x)$，关于 $y = x$ 对称。

---

> [!WARNING] AI Generated
> 本页内容由 AI 从 `00_Raw/19_附录1_图像变换.md` 编译而成，尚未经人工审核。

## Dataview 查询

```dataview
TABLE tags AS 标签, status AS 状态
FROM "01_Wiki"
WHERE contains(tags, "图像变换") OR contains(file.name, "Graph")
SORT file.name ASC
```
