---
title: 支持向量机(SVM)
date: 2017-06-26 21:10:58
tags:
  - ML
categories:
  - NG_ML
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## 支持向量机的假设函数和损失函数
回忆一下逻辑回归的损失函数：

$$min_\theta\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}(-logh_\theta(x^{(i)})+(1-y^{(i)})(-log(1-h_\theta(x^{(i)}))]+\frac{\lambda}{2m}\sum_{j=1}^n\theta_j^2$$

支持向量机的损失函数与之类似：

$$min_\theta C\sum_{i=1}^{m}[y^{(i)}cost_1(\theta^Tx^{(i)})+(1-y^{(i)})cost_0(\theta^Tx^{(i)})]+\frac{1}{2}\sum_{j=1}^n\theta_j^2$$

<!--More-->

\\(cost_{1}(z) \quad (y=1)\\)：

{% asset_img cost1.png %}

\\(cost_{0}(z) \quad (y=0)\\)：

{% asset_img cost0.png %}

注意到除了从\\(-log((1-)\frac{1}{1+e^z})\\)到\\(cost_{0/1}(z)\\)的变化外，用于`trade-off`的\\(\lambda\\)也在支持向量机中通常以参数\\(C\\)的形式出现，\\(C\\)可以理解为\\(\frac{1}{\lambda}\\)。

支持向量机的假设函数：

$$\begin{equation}
h_\theta(x)=\begin{cases}
1 & \text{if}\quad \theta^Tx\ge 0 \\
0 & \text{otherwise}
\end{cases}
\end{equation}$$


## Large Margin Classification
SVM常常被称作为`Large Margin Classification`，为什么呢？因为它对于决策边界要求更加严格：

* 如果\\(y=1\\)，我们想要\\(\theta^Tx \ge 1\\)（而不是\\(\ge 0\\)）；
* 如果\\(y=0\\)，我们想要\\(\theta^Tx \le -1\\)（而不是\\(< 0\\)）；

当满足以上条件时，\\(cost_{0/1}(z)=0\\)，从而将\\(minJ(\theta)\\)转化为以下的凸优化问题：

$$\begin{align}& min_\theta\frac{1}{2}\sum_{j=1}^{n}\theta_j^2 \\ 
& s.t. \begin{cases}
\theta^Tx^{(i)}\ge 1 & \text{if} \quad y^{(i)}=1 \\
\theta^Tx^{(i)}\le -1 & \text{if} \quad y^{(i)}=0
\end{cases}
\end{align}$$

将\\(x^{(i)}\\)在向量\\(\theta\\)上的投影写作\\(p^{(i)}\\)，可以变化形式为：

$$\begin{align}& min_\theta\frac{1}{2}\sum_{j=1}^{n}\theta_j^2 \\ 
& s.t. \begin{cases}
p^{(i)}||\theta||\ge 1 & \text{if} \quad y^{(i)}=1 \\
p^{(i)}||\theta||\le -1 & \text{if} \quad y^{(i)}=0
\end{cases}
\end{align}$$

\\(\theta\\)向量是决策边界\\(\theta^Tx=0\\)的法向量，为了使\\(||\theta||\\)（即目标函数）尽量小，在条件限制下，\\(p\\)就要尽可能大，即\\(x\\)在\\(\theta\\)方向的投影尽可能大，这就使得决策边界离两边数据尽可能远。

SVM是凸函数优化，最后的结果是全局最优点，不需要担心局部最优问题。

## 核函数(Kernels)
核函数将一系列特征\\(x_1,...x_n\\)映射到另一组特征\\(f_1,...\\)上，可以给SVM加上非线性性质。它有两个重要概念：

1. `地标点(landmarks)`：\\(l^{(1)},...,l^{(n)}\\)；
2. `近似度(Similarity)`: 
$$similarity(x,l)=1\quad \text{if}\quad x\approx l\\ \\similarity(x,l)=0\quad \text{if \(x\) is far away form }l$$

地标点一般直接使用训练集中的点\\(l^{(1)} = x^{(1)},...,l^{(m)} = x^{(m)}\\)；  
常用的近似度函数有:

* `线性核函数(linear kernel)`：线性核函数其实就是不用核函数，\\(f_n = x_n\\)；
* `高斯核函数(Gaussian kernel)`：\\(f_m = similarity(x,l)=exp(-\frac{||x-l^{(m)}||}{2\sigma^2})\\)

在高斯核函数中，\\(\sigma\\)也可以起到`trade-off`的作用：

* \\(\sigma\\)过小：高方差、低偏差；
* \\(\sigma\\)过大：高偏差、低方差。

## 使用SVM

```
1. First choose parameter C and kernel;
2. Given training data: (x1,y1),(x2,y2)...(xm,ym), choose l1=x1,..., lm=xm;
3. mapping features using similarity:
	f1 = similarity(x,l1)
	.
	.
	.
	fm = similarity(x,lm)

4. Feature scaling
5. traing svm with f, C, sigma(hypotyhesis: predict y=1 if theta*f >= 0)
```

## 逻辑回归和SVM
1. \\(n\\)很大（和\\(m\\)相近）：使用逻辑回归或者不带核函数的（或者线性核函数）的SVM，这两者效果类似，不用复杂的非线性特征以防止过拟合；
2. \\(n\\)很小，\\(m\\)不大不小 (intermediate) ：使用带高斯核的SVM；
3. \\(n\\)很小，\\(m\\)很大：增加特征，然后使用逻辑回归或者不带核函数的SVM。

神经网络在以上三种情况下都表现很好，但是训练速度很慢。



