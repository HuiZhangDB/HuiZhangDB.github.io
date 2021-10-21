---
title: 逻辑回归(Logistic Regression)
date: 2017-06-03 15:11:54
tags:
  - ML
categories:
  - NG_ML
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## 分类表达式
### 分类和回归

* 分类问题和回归问题的形式是相似的，但它的预测值是一组有限的离散值。  
* 分类问题的求解可以看做是找边界线（面）的过程，即拟合边界曲线（面），特征空间内的点分布在该曲线（面）分割出来的不同子空间中；  
* 而回归问题的求解是拟合特征-预测值曲线（面），特征空间内的点分布在该曲线（面）上或者附近。

### 分类问题的假设表达式
#### 逻辑函数(Logistic Function or Sigmoid Function)
使用逻辑函数\\(g(z)\\)将预测值映射到[0, 1]区间中，使假设函数更适用于分类问题。

$$\begin{align}& 
h_\theta (x) = g ( \theta^T x ) 
\newline 
\newline& z = \theta^T x 
\newline& g(z) = \dfrac{1}{1 + e^{-z}}
\end{align}$$

<!--More-->

逻辑函数和输入值：

{% asset_img sigmoid.png %}

可以注意到：

$$\begin{align}z=0, e^{0}=1 \Rightarrow g(z)=1/2\newline z \to \infty, e^{-\infty} \to 0 \Rightarrow g(z)=1 \newline z \to -\infty, e^{\infty}\to \infty \Rightarrow g(z)=0 \end{align}$$

#### 假设函数的物理意义
\\(h_{\theta}(x)\\)表示预测值等于1的可能性：

$$\begin{align}& 
h_\theta(x) = P(y=1 | x ; \theta) = 1 - P(y=0 | x ; \theta) 
\newline& P(y = 0 | x;\theta) + P(y = 1 | x ; \theta) = 1
\end{align}$$

### 判定边界(Decision Boundary)
判定边界是指分隔开不同类特征点的曲线（面），它由\\(h_{\theta}(x)\\)假设函数决定。  
例如下面这个例子（二分类）中，判定边界是直线\\(x_1=5\\)

$$\begin{align}& \theta = \begin{bmatrix}5 \newline -1 \newline 0\end{bmatrix} \newline & y = 1 \; if \; 5 + (-1) x_1 + 0 x_2 \geq 0 \newline & 5 - x_1 \geq 0 \newline & - x_1 \geq -5 \newline& x_1 \leq 5 \newline \end{align}$$

注意逻辑函数(\\(e.g. \theta^Tx\\))的输入不一定是线性的，它可以是任何适合训练数据的形状，比如圆(\\(e.g. z =\theta_0+\theta_1x_1^2+\theta_2x_2^2\\))。

## 逻辑回归模型
### 损失函数和梯度下降
#### 损失函数
不能直接使用之前线性回归中使用的损失函数\\(J(\theta)=\frac{1}{2m}\sum_{i=0}^{i=m}(h_{\theta}(x_i)-y_i)^2\\)，使用逻辑函数会导致其发生扭曲，产生许多局部最优点（极小值），换句话说就不再是凸函数了。  
所以将损失函数修改为：

$$\begin{align}& J(\theta) = \dfrac{1}{m} \sum_{i=1}^m \mathrm{Cost}(h_\theta(x^{(i)}),y^{(i)}) \newline & \mathrm{Cost}(h_\theta(x),y) = -\log(h_\theta(x)) \; & \text{if y = 1} \newline & \mathrm{Cost}(h_\theta(x),y) = -\log(1-h_\theta(x)) \; & \text{if y = 0}\end{align}$$

即：

$$J(\theta) = - \frac{1}{m} \displaystyle \sum_{i=1}^m [y^{(i)}\log (h_\theta (x^{(i)})) + (1 - y^{(i)})\log (1 - h_\theta(x^{(i)}))]$$

向量形式为：

$$\begin{align} & h = g(X\theta)\newline & J(\theta) = \frac{1}{m} \cdot \left(-y^{T}\log(h)-(1-y)^{T}\log(1-h)\right) \end{align}$$

#### 梯度下降
梯度下降的标准形式：

$$\begin{align}& Repeat \; \lbrace \newline & \; \theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j}J(\theta) \newline & \rbrace\end{align}$$

代入以上\\(J(\theta)\\)得到：

$$\begin{align} & Repeat \; \lbrace \newline & \; \theta_j := \theta_j - \frac{\alpha}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} \newline & \rbrace \end{align}$$

向量形式为：

$$\theta := \theta - \frac{\alpha}{m} X^{T} (g(X \theta ) - \vec{y})$$

#### 优化算法
`Conjugate gradient`、 `BFGS`和`L-BFG`是梯度下降的优化算法，MATLAB有提供这几个库函数，使用这几个函数同样需要定义\\(J(\theta)\\)和\\(\dfrac{\partial}{\partial \theta_j}J(\theta)\\)。

```matlab
function [jVal, gradient] = costFunction(theta)
  jVal = [...code to compute J(theta)...];
  gradient = [...code to compute derivative of J(theta)...];
end
```
MATLAB提供了`fminunc()`函数来实现优化：

```matlab
options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2,1);
   [optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options);
```

## 过拟合(Overfitting)和正则化(Regularization)
`欠拟合(underfitting)`或`高偏差(high bias)`，是指假设函数不足以描述数据趋势，通常由假设函数过于简单或者特征维数太少导致；  
`过拟合(overfitting)`或`高方差(high variance)`，是指假设函数对训练集拟合良好但对测试集的通用性差，通常由于假设函数过于复杂或特征维数太高。

解决过拟合问题的常用方法：

1. 减少特征维数：手动选择特征、使用模型选择算法；
2. `正则化(Regularization)`：保留所有特征，但减小参数\\(\theta_j\\)的量级；正则化在有许多弱相关特征(slightly useful features)的时候很有用。

### 线性回归的正则化
#### 损失函数正则化
正则化其实就是通过增加参数在损失函数中的影响来减弱其最后在假设函数中的权重：  
例如，对于假设函数\\(\theta_0 + \theta_1x + \theta_2x^2 + \theta_3x^3 + \theta_4x^4\\)，如果想让它变得更加“二次方”，即排除\\(\theta_3x^3 \\)和\\(\theta_4x^4\\)的影响，可以通过修改损失函数来实现：

$$min_\theta\ \dfrac{1}{2m}\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2 + 1000\cdot\theta_3^2 + 1000\cdot\theta_4^2$$

正则化所有参数（除了\\(\theta_0\\)）：

$$min_\theta\ \dfrac{1}{2m}\  \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda\ \sum_{j=1}^n \theta_j^2$$

其中\\(\lambda\\)是`正则化系数(regularization parameter)`，\\(\lambda\\)越大，拟合曲线越平滑，但要注意的是\\(\lambda\\)过大可能导致欠拟合。

#### 梯度下降正则化
对于线性回归而言，正则化后的梯度下降：

$$\begin{align} & \text{Repeat}\ \lbrace \newline & \ \ \ \ \theta_0 := \theta_0 - \alpha\ \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)} \newline & \ \ \ \ \theta_j := \theta_j - \alpha\ \left[ \left( \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} \right) + \frac{\lambda}{m}\theta_j \right] &\ \ \ \ \ \ \ \ \ \ j \in \lbrace 1,2...n\rbrace\newline & \rbrace \end{align}$$ 

#### 法方程正则化
正则化后的法方程可以写为：

$$\begin{align}& \theta = \left( X^TX + \lambda \cdot L \right)^{-1} X^Ty \newline& \text{where}\ \ L = \begin{bmatrix} 0 & & & & \newline & 1 & & & \newline & & 1 & & \newline & & & \ddots & \newline & & & & 1 \newline\end{bmatrix}\end{align}$$

要注意梯度下降中的下标\\(j\\)是从1开始的，同样，法方程中\\(\lambda(1,1)=0\\)，这是因为截取项\\(\theta_0\\)是不需要正则化的。

### 逻辑回归的正则化
#### 正则化后的损失函数
逻辑回归的损失函数加上正则化项：

$$J(\theta) = - \frac{1}{m} \sum_{i=1}^m [ y^{(i)}\ \log (h_\theta (x^{(i)})) + (1 - y^{(i)})\ \log (1 - h_\theta(x^{(i)}))] + \frac{\lambda}{2m}\sum_{j=1}^n \theta_j^2$$

注意\\(\sum_{j=1}^n \theta_j^2\\)下标从1开始，在梯度下降中也要特别注意\\(\theta_0\\)的更新。

#### 正则化后的梯度下降

$$\begin{align} & \text{Repeat}\ \lbrace \newline & \ \ \ \ \theta_0 := \theta_0 - \alpha\ \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)} \newline & \ \ \ \ \theta_j := \theta_j - \alpha\ \left[ \left( \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} \right) + \frac{\lambda}{m}\theta_j \right] &\ \ \ \ \ \ \ \ \ \ j \in \lbrace 1,2...n\rbrace\newline & \rbrace \end{align}$$ 

## 多值分类
当预测分类值有多个，如\\(y={0,1,2,...,n}\\)时，可以将其看做\\(n+1\\)个二值分类问题：对于每一类，将其看做一类而其他所有的看做一类。

$$\begin{align}& y \in \lbrace0, 1 ... n\rbrace \newline& h_\theta^{(0)}(x) = P(y = 0 | x ; \theta) \newline& h_\theta^{(1)}(x) = P(y = 1 | x ; \theta) \newline& \cdots \newline& h_\theta^{(n)}(x) = P(y = n | x ; \theta) \newline& \mathrm{prediction} = \max_i( h_\theta ^{(i)}(x) )\newline\end{align}$$

1. 训练时，对每一类做二值逻辑回归分类器训练；
2. 预测时，计算每类的预测值，最大的为结果。

举个例子（3值分类）：

{% asset_img 3classes.png %}



