---
标题: 傅里叶级数
标签: [数学, 第16讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 将周期函数展开为三角函数（正弦、余弦）的无穷级数，适用于满足狄利克雷条件的函数。
来源: 01_Raw/Archive/Lectures/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 定义

设 $f(x)$ 是周期为 $2l$ 的周期函数，且在 $[-l, l]$ 上可积。傅里叶系数为：

$$a_n = \frac{1}{l} \int_{-l}^{l} f(x) \cos\frac{n\pi}{l}x \,\mathrm{d}x \quad (n = 0,1,2,\dots)$$
$$b_n = \frac{1}{l} \int_{-l}^{l} f(x) \sin\frac{n\pi}{l}x \,\mathrm{d}x \quad (n = 1,2,3,\dots)$$

傅里叶级数为：

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos\frac{n\pi}{l}x + b_n \sin\frac{n\pi}{l}x\right)$$

## 正弦级数与余弦级数

- **奇函数**：$a_n = 0$，展开为正弦级数 $\displaystyle \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{l}$
- **偶函数**：$b_n = 0$，展开为余弦级数 $\displaystyle \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\frac{n\pi x}{l}$

## 周期延拓

定义在 $[0, l]$ 上的函数可通过奇延拓（正弦级数）或偶延拓（余弦级数）展开。

---

```dataview
TABLE title, 掌握状态, 摘要
FROM "03_Wiki"
WHERE contains(标签, "傅里叶") OR contains(标签, "Fourier")
SORT 类型 ASC
```
