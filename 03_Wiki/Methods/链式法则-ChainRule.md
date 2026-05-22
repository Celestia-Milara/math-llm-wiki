---
标题: 链式法则（多元复合函数求导）
标签: [数学, 第13讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 多元复合函数对自变量求偏导的规则，通过复合结构图逐层求导。
来源: 01_Raw/13_第13讲_多元函数微分学.md
---

> [!WARNING] AI Generated
> 此内容由 AI 初次编译，尚未经人工核对。核对后请移除此块或将 掌握状态 改为 practice_verified。

## 基本法则

### 情形一：两个中间变量、两个自变量

设 $z = f(u, v)$，其中 $u = u(x, y),\; v = v(x, y)$，则

$$
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x},
\qquad
\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y}.
$$

### 情形二：两个中间变量、一个自变量（全导数）

设 $z = f(u, v)$，其中 $u = u(t),\; v = v(t)$，则

$$
\frac{\mathrm{d}z}{\mathrm{d}t} = \frac{\partial z}{\partial u}\frac{\mathrm{d}u}{\mathrm{d}t} + \frac{\partial z}{\partial v}\frac{\mathrm{d}v}{\mathrm{d}t},
$$

称为 $z$ 对 $t$ 的**全导数**。

## 复合结构图

绘制复合结构图可帮助确定求导路径：

```
      z
     / \
    u   v
   / \ / \
  x   y   t (视具体情形)
```

**口诀**："祖孙三代，爷爷对每个孩子都爱是不变的"——无论 $z$ 对哪个变量求导，也不论已经求了几阶导，求导后的新函数仍然保持与原函数完全相同的复合结构。

## 关键技巧

1. **记号区分**：$f_1'$ 表示对第 1 个位置求导，$f_2'$ 表示对第 2 个位置求导
   - 如 $f_1'(x^2, \mathrm{e}^x)$ 表示 $f$ 对第一个中间变量 $u = x^2$ 的偏导
2. **高阶偏导**：复合函数求高阶偏导时，一阶偏导函数保持与原函数相同的复合结构
3. **嵌套层次**：画复合结构图可避免遗漏分支

## 典型例题思路

**例**：设 $z = f(\mathrm{e}^x\sin y, x^2 + y^2)$，$f$ 有二阶连续偏导，求 $\frac{\partial^2 z}{\partial x \partial y}$。

步骤：
1. 画复合结构图，确定每个位置对应的表达式
2. 先用链式法则求一阶偏导
3. 再对一阶偏导结果使用链式法则和乘积法则求二阶偏导
4. 混合偏导相等条件可用于简化

## 相关条目

```dataview
TABLE 掌握状态, 类型
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) AND 类型 != "permanent"
SORT file.name ASC
```
