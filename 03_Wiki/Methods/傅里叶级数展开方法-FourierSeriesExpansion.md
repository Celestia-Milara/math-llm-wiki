---
标题: 傅里叶级数展开方法
标签: [数学, 第16讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 周期函数的傅里叶级数展开、正弦级数与余弦级数展开、奇延拓与偶延拓的计算方法。
来源: 01_Raw/Archive/Lectures/16_第16讲_无穷级数.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 傅里叶系数计算

周期为 $2l$ 的函数 $f(x)$ 的傅里叶系数：

$$\begin{aligned}
a_n &= \frac{1}{l} \int_{-l}^{l} f(x) \cos\frac{n\pi}{l}x \,\mathrm{d}x \quad (n = 0,1,2,\dots) \\
b_n &= \frac{1}{l} \int_{-l}^{l} f(x) \sin\frac{n\pi}{l}x \,\mathrm{d}x \quad (n = 1,2,3,\dots)
\end{aligned}$$

傅里叶级数：$\displaystyle f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos\frac{n\pi}{l}x + b_n \sin\frac{n\pi}{l}x\right)$

## 正弦级数与余弦级数

### 奇函数（正弦级数）

$$f(x) \sim \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{l}, \quad b_n = \frac{2}{l} \int_0^l f(x) \sin\frac{n\pi x}{l}\,\mathrm{d}x$$

### 偶函数（余弦级数）

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\frac{n\pi x}{l}, \quad a_n = \frac{2}{l} \int_0^l f(x) \cos\frac{n\pi x}{l}\,\mathrm{d}x$$

## 周期延拓

定义在 $[0, l]$ 上的函数：
- **奇延拓**获得正弦级数展开
- **偶延拓**获得余弦级数展开

## 狄利克雷定理的应用

和函数 $S(x)$ 在连续点等于 $f(x)$，在第一类间断点等于左右极限平均值，在端点 $\pm l$ 等于 $\dfrac{f(-l+0) + f(l-0)}{2}$。

## 常见应用

利用傅里叶展开求数项级数的和，如 $\displaystyle \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$。

## 相关页面

- [[FourierSeries|傅里叶级数]]
- [[狄利克雷收敛定理-DirichletConvergenceTheorem|狄利克雷收敛定理]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, "傅里叶") OR contains(标签, this.标签[1])
SORT 类型 ASC
```
