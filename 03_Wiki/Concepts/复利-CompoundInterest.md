---
标题: 复利与连续复利（Compound Interest）
标签: [数学, 第7讲, 概念]
创建日期: 2026-05-03
类型: 永久笔记
掌握状态: 待编译
摘要: 利息计入本金重复计息的金融数学概念，连续复利是支付次数趋于无穷时的极限情形。
来源: 01_Raw/Archive/Lectures/07_第7讲_一元函数微分学的应用(三).md
---

> [!WARNING] AI Generated
> 以下内容由 AI 从原始笔记编译，尚未经人工核验。

## 三种计息方式

### 1. 每年支付一次

年利率为 $r$，初始存款为 $A$ 元，$t$ 年后余额：

$$
A_t = A(1 + r)^t
$$

### 2. 每年支付 $n$ 次

年利率为 $r$，一年支付 $n$ 次，$t$ 年后余额：

$$
A_t = A\left(1 + \frac{r}{n}\right)^{nt}
$$

### 3. 连续复利（$n \to \infty$）

当支付次数趋于无穷时：

$$
\lim_{n \to \infty} A_t = \lim_{n \to \infty} A\left(1 + \frac{r}{n}\right)^{nt} = A\mathrm{e}^{rt}
$$

## 应用：现值计算

若 $t$ 年末总收入为 $R$，按连续复利折现，现值为：

$$
A(t) = R\mathrm{e}^{-rt}
$$

通过最大化现值函数可确定最佳投资期限。

---

**来源**：`01_Raw/07_第7讲_一元函数微分学的应用(三).md`

```dataview
TABLE 掌握状态, 类型 FROM "03_Wiki" WHERE contains(标签, this.标签[1]) SORT file.name ASC
```
