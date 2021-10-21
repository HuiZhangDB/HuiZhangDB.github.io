---
title: 多变量线性回归
date: 2017-06-03 15:06:05
tags:
  - ML
categories:
  - NG_ML
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>


## 多变量线性回归假设函数
多变量假设函数的标准形式(multivariable hypothesis function)  

$$
\begin{align}h_\theta(x) =\begin{bmatrix}\theta_0 \hspace{2em} \theta_1 \hspace{2em} ... \hspace{2em} \theta_n\end{bmatrix}\begin{bmatrix}x_0 \newline x_1 \newline \vdots \newline x_n\end{bmatrix}= \theta^T x\end{align}
$$

<!--More-->

## 多变量的梯度下降

$$
\begin{align}& \text{Repeat until convergence:} \; \lbrace \newline \; & \theta_j := \theta_j - \alpha \frac{1}{m} \sum\limits_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x_j^{(i)} \; & \text{for j := 0...n}\newline \rbrace\end{align}
$$

* `特征缩放(Feature Scaling)`和`均值正规化(mean normalization)`可以加快梯度下降的速度（缩小范围，减少迭代次数）。

$$
x_i := \dfrac{x_i - \mu_i}{s_i}
$$

* `学习速率(Learning Rate)`：现已证明，如果学习速率\\(\alpha\\)充分小，则损失函数\\(J(\theta)\\)会（单调递减）随着迭代次数的增加而减小。总之`阈值(threshold)`很难确定。
若\\(\alpha\\)太小，则收敛速度慢；
若\\(\alpha\\)太大，则损失函数可能不单调递减而不收敛。

### 多项式回归
多元函数和多项式函数的转换：

$$
h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_1^2 + \theta_3 x_1^3
$$

可转换为

$$
h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3
$$

即\\(x_2 = x_1^2, x_3 = x_1^3\\)，此时需要特别注意的是`featrue scaling`：如果\\(x_1\\)取值[1,1000]，那么\\(x_2\\)的取值范围将是[1,1000000]，\\(x_3\\)则是[1,1000000000]。

## 使用法方程(Normal Equation)进行参数计算 
线性回归的法方程：

$$
\theta = (X^T X)^{-1}X^T y
$$

注意，法方程中的\\(X\\)维数是\\(m\times (n+1)\\)，因为加了一列全是1的列向量以保存\\(\theta_0\\)，即`截距项(intercept term)`。

|梯度下降|法方程|
|----|----|
|需要选择\\(\alpha\\)|无需选择\\(\alpha\\)|
|需要迭代|无需迭代|
|\\(O(kn^2)\\)（\\(k\\)是迭代次数）| \\(O(n^3)\\)（矩阵求逆具有三次方的复杂度）|
|特征数量\\(n\\)很大的时候效果很好|\\(n\\)很大的时候非常慢(<10000)|

### 法方程不可逆
法方程有解的充分条件是\\(X^TX\\)可逆，而一些常见的因素可能会导致其不可逆：

1. 冗余特征(Redundant features)，即可能有多个特征强相关（线性相关）--> 删除相关特征
2. 过多特征 (e.g. m ≤ n)，即特征数量超过样本数量 --> 减少特征




