---
标题: 微分算子法
标签: [数学, 第15讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 将微分方程化为算子多项式的代数形式，通过逆算子求解非齐次方程的特解，计算量小但需记忆规则。
来源: 01_Raw/Archive/Lectures/15_第15讲_微分方程.md
可信状态: S3 待核查
---

> [!WARNING] AI Generated
> 以下内容为 AI 从原始笔记编译，尚未经用户验证。

## 基本约定

令 $\mathrm{D} = \dfrac{\mathrm{d}}{\mathrm{d}x}$，则 $y'' + py' + qy = f(x)$ 可写为：

$$(\mathrm{D}^2 + p\mathrm{D} + q)y = f(x), \quad \text{记 } F(\mathrm{D}) = \mathrm{D}^2 + p\mathrm{D} + q$$

特解为：$y^* = \dfrac{1}{F(\mathrm{D})} f(x)$。

## 常见类型

### 1. $\dfrac{1}{F(\mathrm{D})}\mathrm{e}^{\alpha x}$ 型

- 若 $F(\alpha) \neq 0$：$y^* = \dfrac{1}{F(\alpha)}\mathrm{e}^{\alpha x}$
- 若 $F(\alpha) = 0,\; F'(\alpha) \neq 0$：$y^* = x \cdot \dfrac{1}{F'(\alpha)}\mathrm{e}^{\alpha x}$
- 若 $F(\alpha) = F'(\alpha) = 0,\; F''(\alpha) \neq 0$：$y^* = x^2 \cdot \dfrac{1}{F''(\alpha)}\mathrm{e}^{\alpha x}$

### 2. $\dfrac{1}{F(\mathrm{D})}\cos\beta x$ 或 $\dfrac{1}{F(\mathrm{D})}\sin\beta x$ 型

代入 $\mathrm{D}^2 = -\beta^2$，化算子为代数式求解。

### 3. $\dfrac{1}{F(\mathrm{D})}$ 作用于多项式型

将 $\dfrac{1}{F(\mathrm{D})}$ 展开为泰勒多项式 $Q_k(\mathrm{D})$，再作用于多项式。

### 4. $\dfrac{1}{F(\mathrm{D})}\mathrm{e}^{\alpha x}v(x)$ 型（移位性质）

$$\frac{1}{F(\mathrm{D})}\mathrm{e}^{\alpha x}v(x) = \mathrm{e}^{\alpha x} \cdot \frac{1}{F(\mathrm{D}+\alpha)} v(x)$$

> [!TIP]
> 待定系数法易设出形式但计算量大；微分算子法计算量小但需记忆规则。建议两种方法都掌握。

## 相关页面

- [[03_Wiki/Methods/常系数线性微分方程求解-ConstantCoefficientODE|常系数线性微分方程求解]]
- [[线性微分方程解的结构-StructureOfLinearODESolutions|线性微分方程解的结构]]

---

```dataview
TABLE title, 类型, 摘要
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "微分方程")
SORT 类型 ASC
```
