---
标题: 换元法
标签: [数学, 第9讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
问题类型: null
问题备注: ""
最后练习: null
摘要: 通过变量替换将复杂被积函数化简为可积形式，包括三角代换、根式代换、倒代换等。
来源: 00_Raw/09_第9讲_一元函数积分学的计算.md
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经人工核验。

## 基本思想

$$\int f(x)\,\mathrm{d}x \xlongequal{x=g(u)} \int f[g(u)]\,\mathrm{d}[g(u)] = \int f[g(u)]\,g'(u)\,\mathrm{d}u$$

要求 $x=g(u)$ 是单调可导函数，计算结束后用 $u=g^{-1}(x)$ 回代。

## 常用换元法

### 1. 三角代换

| 根式形式 | 代换 | 化简结果 |
|:--------|:----|:--------|
| $\sqrt{a^2-x^2}$ | $x=a\sin t$ | $a\cos t$ |
| $\sqrt{a^2+x^2}$ | $x=a\tan t$ | $a\sec t$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec t$ | $a\tan t$ |

### 2. 恒等变形后三角代换

对于 $\sqrt{ax^2+bx+c}$，先配方化为三种标准形式之一再作三角代换。

### 3. 根式代换

当被积函数含有 $\sqrt[n]{ax+b}$ 时，令 $\sqrt[n]{ax+b}=t$。

若同时含有 $\sqrt[n]{ax+b}$ 和 $\sqrt[m]{ax+b}$，取 $m,n$ 的最小公倍数 $l$，令 $\sqrt[l]{ax+b}=t$。

### 4. 倒代换

当分母幂次比分子高两次及以上时，令 $x=\frac{1}{t}$。

### 5. 复杂函数直接代换

当被积函数含有 $a^x,\mathrm{e}^x,\ln x,\arcsin x,\arctan x$ 等时，可令该复杂函数等于 $t$。

> [!TIP]
> 换元法的选择口诀：带根号看三角，根号直代取整幂，分母高次用倒换，复杂函数整体换。

---

## Dataview

```dataview
TABLE 
  status as "状态",
  summary as "摘要"
FROM "01_Wiki/Methods"
WHERE contains(tags, this.file.tags[1])
SORT file.name ASC
```
