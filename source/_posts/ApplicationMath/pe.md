---
title: Point Esimation 点估计
date: 2017-04-27 14:40:02
tags:
  - Math
categories:
  - 应用工程数学
---

## Hoeffding不等式
用于确认精确度，适用于所有有界的随机变量。假设有两两独立的变量X1...Xn，其中Xi都是`几乎`有界的变量，即满足  

```
P(ai<=Xi<=bi) = 1
```
则其期望满足：

```
P(|mean(X)-E(mean(X))|>=t) <= 2exp(-2(nt)^2/sum((bi - ai)^2))
```

## Regression回归分析
Bias-Variance Tradeoff

* 欠拟合 underfitting 高偏差 bias
* 过拟合 overfitting 高方差 variance

解决方法：1、减少选取的特征数量；2、正则化 regularization

## Polynomial Curve Fitting

```
Y = XA 
#使用法向量计算最小二乘法结果
A = (X.T * X) * X.T * Y
```