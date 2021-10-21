---
title: K-means和PCA
date: 2017-07-04 16:45:02
tags:
  - ML
categories:
  - NG_ML
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## K-means
`K-means`是一个常用且有效的聚类算法。它的算法可以描述为：

```matlab
Firstly randomly initiallize the K centroids mu1,mu2,...,muk;
Repeat{
	% Cluster assignment step
	for i = 1 to m
		ci = index of cluster centroid cloest to xi;
	% Move centroid
	for k = 1 to k
		muk = mean of points xs assigned to cluster k;
}

```

<!--More-->

### 优化目标
像逻辑回归等监督学习算法一样，`K-means`等无监督学习算法同样有损失函数来作为优化目标：

$$min_{c,\mu}J(c^{(1)},...,c^{(m)},\mu_1,...,.\mu_K) = \frac{1}{m}||x^{(i)}-\mu_{c^{(i)}}||^2$$

\\(minJ\\)表示我们的优化目标是最小化同类点到聚类中心的距离。

### 随机初始化
当\\(K\\)值较小的时候，初始中心点的位置对最后的聚类结果有非常大的影响。只随机生成一组初始点可能会导致最后的结果是局部最优解`local optima`。因此，当\\(K\\)值较小的时候，我们可以使用多组初始中心点以避免这个问题：

```matlab
for i = 1 to 100 {
	Randomly initialize K-means;
	Run K-means, get c1,...,cm, mu1,...,muk;
	Compute cost function/distortion; 
}

Choose the cluster that gave the lowest cost J.
```

### 选择聚类数目
怎样选择聚类数目\\(K\\)是一个很难说的问题，有时就算是人类专家在看到一组可视化数据后都很难给出精准的答案。现有的选择\\(K\\)的算法有`ELbow Method`，但它对很多情况都并不适用。通常来说，决定\\(K\\)的大小需要我们根据具体问题和之后的目标来具体分析。

### 应用
1. 市场分割
2. 社交网络分析
3. 计算集群组织
4. 天文数据分析

## PCA
`PCA`也是最常用的无监督算法之一，它的算法可以描述为：

```matlab
1. Feature Preprocessing: feature scaling and mean normaliza1on;
2. Compute covariance matrix:
	Sigma = 1/m * X' * X;
3. Compute eigenvectors of matrix Sigma:
	[U,S,V] = svd(Sigma);
4. Ureduce = U(:,1:k);
5. Xreduce = X * Ureduce;
6. Xrecover = Xreduce * Ureduce';
```
### 优化目标
PCA的目标可以描述为：要找到最合适的一组向量\\(\mu^{(1)},...,\mu^{(k)}\\)，将原始数据映射到这组向量围成的新的特征空间中，使其`投影距离最小(minimize the projec1on error)`。

### 选择主成分数量
通常，我们可以用到达一定`保留方差(retained variance)`的最小\\(k\\)值来作为主成分数量。可以看一个保留了99%方差的例子：

$$\frac{\frac{1}{m}\sum_{i=1}^m||x^{(i)}-x^{(1)}_{approx}||^2}{\frac{1}{m}\sum_{i=1}^m||x^{(i)}||^2} \le 0.01 $$

上述值可以通过协方差矩阵奇异值分解后得到的\\(S\\)来计算，\\(S\\)是一个对角矩阵，上述不等式等同于：

$$\frac{\sum_{i=1}^kS_{ii}}{\sum_{i=1}^mS_{ii}}\ge 0.99$$

### 应用
应该用于：

1. 数据压缩：减小数据储存代价、加快运算速度（\\(k<n\\)，由保留方差计算）；
2. 数据可视化（\\(k=2 \quad or\quad k=3\\)）

错误的应用：

1. 减小特征集以防止过拟合：PCA只分析了特征之间\\(x_1,...x_n\\)的关系，并没有考虑特征的变化对\\(y\\)的影响，使用PCA可能会丢失和\\(y\\)相关的重要信息。因此防止过拟合不应该用PCA，而应该使用正则化。
2. 在机器学习系统的开始设计阶段使用：应该先使用原始数据，只有在原始数据效果不好（太慢之类的）时候再考虑用PCA。