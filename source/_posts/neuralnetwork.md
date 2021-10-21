---
title: 神经网络(Neural Networks)
date: 2017-06-15 16:54:11
tags:
  - ML
categories:
  - NG_ML
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## Why Neural Networks?
当遇到`特征数量很大(n is large)`的`复杂非线性问题`时，简单的逻辑回归（加入二次项或三次项）不再适用，因为会导致太多的特征量参与计算（不仅仅是\\(x_n, x_n^2,x_n^3\\)，还有\\(x_i{x_j},x_i^2{x_j}\\)等二次项和三次项）—— 带来巨大的计算代价和过拟合问题。

神经网络其实很早就出现了(A pretty old algorithm)，始于80年代，90年代有所衰减而现在又火了起来（计算机计算能力的提升）。神经网络模拟人脑神经的计算机制，在解决许多机器学习问题时有很好的效果。

人脑使用一种学习算法来处理无数不同的问题，这使得我们模拟它的计算机制成为可能。人脑甚至可以学习任何传感数据，这让神经网络成为最有可能实现人工智能的方法。

<!--More-->

## Representation
最简单的神经网络表达式：

$$\begin{bmatrix}x_0 \newline x_1 \newline x_2 \newline \end{bmatrix}\rightarrow\begin{bmatrix}\ \ \ \newline \end{bmatrix}\rightarrow h_\theta(x)$$

这是一个只有2层的神经网络，第1层`输入层`\\(\begin{bmatrix}x_0 \newline x_1 \newline x_2 \newline \end{bmatrix}\\)和第2层`输出层`\\(h_\theta(x)\\)。

输入层和输出层之间可以有中间层节点，称为`隐藏层(hidden layers)`。有一个隐藏层的神经网络可以表示为：

$$\begin{bmatrix}x_0 \newline x_1 \newline x_2 \newline x_3\end{bmatrix}\rightarrow\begin{bmatrix}a_1^{(2)} \newline a_2^{(2)} \newline a_3^{(2)} \newline \end{bmatrix}\rightarrow h_\theta(x)$$

$$\begin{align}& a_i^{(j)} = \text{"activation" of unit i in layer j} \newline& \Theta^{(j)} = \text{matrix of weights controlling function mapping from layer j to layer j+1}\end{align}$$

每个激活节点的计算方式：

$$\begin{align} a_1^{(2)} = g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3) \newline a_2^{(2)} = g(\Theta_{20}^{(1)}x_0 + \Theta_{21}^{(1)}x_1 + \Theta_{22}^{(1)}x_2 + \Theta_{23}^{(1)}x_3) \newline a_3^{(2)} = g(\Theta_{30}^{(1)}x_0 + \Theta_{31}^{(1)}x_1 + \Theta_{32}^{(1)}x_2 + \Theta_{33}^{(1)}x_3) \newline h_\Theta(x) = a_1^{(3)} = g(\Theta_{10}^{(2)}a_0^{(2)} + \Theta_{11}^{(2)}a_1^{(2)} + \Theta_{12}^{(2)}a_2^{(2)} + \Theta_{13}^{(2)}a_3^{(2)}) \newline \end{align}$$

值得注意的是，如果神经网络在第\\(j\\)层有\\(s_j\\)个节点，在第\\(j+1\\)层有\\(s_{j+1}\\)个节点，那么\\(\Theta^{(j)}\\)的维度会是\\(s_{j+1}\times(s_j +1)\\)。

增加隐藏层可以解决更多的复杂非线性问题。

## Application
### 二元逻辑运算
神经网络可以实现所有的逻辑门，例如：

$$\begin{align}AND:\newline\Theta^{(1)} &=\begin{bmatrix}-30 & 20 & 20\end{bmatrix} \newline NOR:\newline\Theta^{(1)} &= \begin{bmatrix}10 & -20 & -20\end{bmatrix} \newline OR:\newline\Theta^{(1)} &= \begin{bmatrix}-10 & 20 & 20\end{bmatrix} \newline\end{align}$$

### 多类分类
比如将数据分为4类，表达式可以是：

$$\begin{bmatrix}x_0 \newline x_1 \newline x_2 \newline ... \newline x_n\end{bmatrix}\rightarrow\begin{bmatrix}a_0^{(2)} \newline a_1^{(2)} \newline a_2^{(2)} \newline ... \newline \end{bmatrix}\rightarrow\begin{bmatrix}a_0^{(3)} \newline a_1^{(3)} \newline a_2^{(3)} \newline ...\newline \end{bmatrix}\rightarrow ... \rightarrow \begin{bmatrix}h_\Theta(x)_1 \newline h_\Theta(x)_2 \newline h_\Theta(x)_3 \newline h_\Theta(x)_4\end{bmatrix}$$

分别训练4个假设函数，表示每个分类的可能性，取可能性最大的标签为分类结果。

## 损失函数
神经网络的损失函数标准形式：
$$\begin{gather} J(\Theta) = - \frac{1}{m} \sum_{i=1}^m \sum_{k=1}^K \left[y^{(i)}_k \log ((h_\Theta (x^{(i)}))_k) + (1 - y^{(i)}_k)\log (1 - (h_\Theta(x^{(i)}))_k)\right] + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2\end{gather}$$

$$\begin{align}& L = \text{ total number of layers in the network} \newline& s_l = \text{number of units (not counting bias unit) in layer \(l\)}\newline& K = \text{number of output units/classes}\end{align}$$

注意，第\\(l\\)层的\\(\Theta^{(l)}\\)矩阵大小为\\(s_{l+1}\times (s_l + 1)\\)，因此正则项\\(\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2\\)是除去截距项(\\(\Theta^{(l)}\\)第一列)的所有\\(\theta\\)的平方和。

这个损失函数\\(J(\Theta)\\)是非凸的，因此使用梯度下降可能只能得到局部最优值。

## 反向传播(Backprogation)
`反向传播算法`是用于计算损失函数偏导\\(\dfrac{\partial}{\partial \Theta_{i,j}^{(l)}}J(\Theta)\\)的算法：

```
Given training set {(x(1),y(1))⋯(x(m),y(m))}, set Δ(l)i,j := 0 for all (l,i,j), (hence you end up having a matrix full of zeros)

For training example t =1 to m:
1. Set a(1) := x(t)
2. Perform forward propagation to compute a(l) for l=2,3,…,L
3. Using y(t), compute delta(L) = a(L)−y(t)
4. Compute delta(L−1),delta(L−2),…,delta(2) using delta(l) = ((Θ(l))'delta(l+1)) .∗ a(l) .∗ (1−a(l))
5. Delta(l):= Delta(l)+ delta(l+1)(a(l))'
6. Regularization as the following equation.
```

$$\begin{align}& D_{i,j}^{(l)} = \frac{1}{m}(\Delta_{i,j}^{(l)} + \lambda \Theta_{i,j}^{(l)}) \quad \text{if \(j \neq 0\)}\newline&  D_{i,j}^{(l)} = \frac{1}{m}\Delta_{i,j}^{(l)} \quad \text{if \(j = 0\)}\end{align}$$

最后得到的\\(D_{i,j}^{(l)}\\)即要求的偏导\\(\dfrac{\partial}{\partial \Theta_{i,j}^{(l)}}J(\Theta)\\)。

可以使用`梯度检查(Gradient Checking)`来检查反向传播算法实现得是否正确。其依据：
$$\dfrac{\partial}{\partial\Theta}J(\Theta) \approx \dfrac{J(\Theta + \epsilon) - J(\Theta - \epsilon)}{2\epsilon}$$

对于每一个\\(\Theta^{(j)}\\)即：

$$\dfrac{\partial}{\partial\Theta_j}J(\Theta) \approx \dfrac{J(\Theta_1, \dots, \Theta_j + \epsilon, \dots, \Theta_n) - J(\Theta_1, \dots, \Theta_j - \epsilon, \dots, \Theta_n)}{2\epsilon}$$

当\\(\epsilon = 10^{-4} \\)时，可以保证其数学意义（足够小），再小的话计算机在计算的时候会出现数值错误，梯度检查的MATLAB实现：

```matlab
epsilon = 1e-4;
for i = 1:n,
  thetaPlus = theta;
  thetaPlus(i) += epsilon;
  thetaMinus = theta;
  thetaMinus(i) -= epsilon;
  gradApprox(i) = (J(thetaPlus) - J(thetaMinus))/(2*epsilon)
end;
```

## 神经网络的使用和训练
### 神经网络的结构
在准备使用神经网络来解决问题时，首先要设计神经网络的结构，包括有多少层隐藏层以及每层有多少节点：

1. 输入层节点数，即特征\\(x^{(i)}\\)的维度；
2. 输出层节点数，即分类的类数；
3. 隐藏层数目和每层的节点数，通常越多越好，但必须平衡随之增加的计算代价；
4. 默认原则：1个隐藏层，如果有1个以上的隐藏层，那么建议每层的节点数一样。

### 训练神经网络
1. 随机生成每层的\\(\Theta^{(l)}\\)；
2. 使用正向传播算出每个训练数据\\(x^{(i)}\\)的预测值\\(h_{\Theta}(x^{(i)})\\)；
3. 实现损失函数；
4. 使用反向传播算法实现损失函数偏导计算；
5. 使用梯度检查确保反向传播算法正确实现；
6. 使用梯度下降或其他优化算法来最小化损失函数，得到最终的\\(\Theta^{(l)}\\)值。

