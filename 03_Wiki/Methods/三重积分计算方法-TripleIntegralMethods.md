---
标题: 三重积分计算方法
标签: [数学, 第18讲, 方法]
创建日期: 2026-05-03
类型: 永久笔记
摘要: 三重积分的四种计算方法：直角坐标（先一后二/先二后一）、柱面坐标、球面坐标、一般换元法。
来源: 01_Raw/Archive/Lectures/18_第18讲_多元函数积分学.md
可信状态: S3 待核查
---

## 1. 直角坐标系

### 先一后二法（投影穿线法）
适用于 $\Omega$ 有下曲面 $z = z_1(x,y)$、上曲面 $z = z_2(x,y)$，无侧面或侧面为柱面：
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = \iint_{D_{xy}} \mathrm{d}\sigma \int_{z_1(x,y)}^{z_2(x,y)} f(x, y, z) \, \mathrm{d}z.
$$

口诀：**后积先定限，限内画条线，先交写下限，后交写上限**。

### 先二后一法（定限截面法）
适用于 $\Omega$ 是旋转体的情形：
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = \int_a^b \mathrm{d}z \iint_{D_z} f(x, y, z) \, \mathrm{d}\sigma.
$$

## 2. 柱面坐标系

令 $\begin{cases} x = r\cos\theta, \\ y = r\sin\theta, \\ z = z, \end{cases}$ 则
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}x\mathrm{d}y\mathrm{d}z = \iiint_{\Omega} f(r\cos\theta, r\sin\theta, z) \, r \, \mathrm{d}r\mathrm{d}\theta\mathrm{d}z.
$$

适用于被积函数含 $x^2 + y^2$ 或积分区域为柱体、锥体等。

## 3. 球面坐标系

令 $\begin{cases} x = r\sin\varphi\cos\theta, \\ y = r\sin\varphi\sin\theta, \\ z = r\cos\varphi, \end{cases}$ 则
$$
\iiint_{\Omega} f(x, y, z) \, \mathrm{d}v = \iiint_{\Omega} f(r\sin\varphi\cos\theta, r\sin\varphi\sin\theta, r\cos\varphi) \, r^2\sin\varphi \, \mathrm{d}r\mathrm{d}\varphi\mathrm{d}\theta.
$$

适用于被积函数含 $x^2 + y^2 + z^2$，积分区域为球或锥的部分。

**球面坐标三步法**：
1. **转**：从 $xOz$ 面出发，绕 $z$ 轴逆时针旋转（$\theta$ 从 $\theta_1$ 到 $\theta_2$）
2. **开**：从 $z$ 轴出发，圆锥面半顶角 $\varphi$（$\varphi$ 从 $\varphi_1(\theta)$ 到 $\varphi_2(\theta)$）
3. **穿**：从原点引射线，$r$ 从 $r_1(\varphi,\theta)$ 到 $r_2(\varphi,\theta)$

## 4. 一般换元法

$$
\iiint_{\Omega_{xyz}} f(x, y, z) \, \mathrm{d}x\mathrm{d}y\mathrm{d}z = \iiint_{\Omega_{uvw}} f[x(u,v,w), y(u,v,w), z(u,v,w)] \left| \frac{\partial(x,y,z)}{\partial(u,v,w)} \right| \mathrm{d}u\mathrm{d}v\mathrm{d}w.
$$

雅可比行列式 $\dfrac{\partial(x,y,z)}{\partial(u,v,w)} = \begin{vmatrix} x_u & x_v & x_w \\ y_u & y_v & y_w \\ z_u & z_v & z_w \end{vmatrix}$.

## 相关页面

- [[三重积分-TripleIntegral]]
- [[重积分应用-ApplicationsOfMultipleIntegrals]]

```dataview
TABLE
  可信状态 AS "状态",
  摘要 AS "摘要"
FROM "03_Wiki"
WHERE contains(标签, this.标签[1]) OR contains(标签, "三重积分")
SORT file.name
```
