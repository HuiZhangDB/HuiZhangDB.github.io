---
title: Deep Learning 简介
date: 2017-04-18 21:18:07
tags:
  - DL
categories:
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

深度学习是机器学习的一种类型，机器学习的核心任务是寻找合适的模型，深度学习的核心任务是寻找合适的参数（权重和偏移）。 

<!--More-->
 
## 深度学习的关键步骤
简单来说，深度学习包含三个关键步骤：  
1. 定义一组函数 -> 确定神经网络结构（层数、神经元数量）    
2. 判断函数优度 -> 定义损失函数  
3. 选择最优函数 -> 寻找最优参数（反向传播和梯度下降）

{% asset_img basic_steps.png %}

### 深度学习的理论基础
只要给出足够数量的隐藏神经元，带一个隐藏层的神经网络可以实现任何连续函数 \\(f\\)

$$ f: R^{N} \rightarrow R^{M} $$

> The Universality Theorem for Neural Networks: A hidden layer network can represent any continuous function.

<!--Modularization-->

## 优化学习效果的秘诀

* 选择合适的损失函数可以提高整体效果，比如改用 Square Error 为 Cross Entropy；
* 使用 `Mini-batch`加速优化；
* 使用新的激活函数，比如改用 Sigmoid 为 ReLU, Maxout 等；
* 自适应的学习速率
* 使用参数优化算法（但不保证达到全局最优），如 Adam。

> Mini-batch does not really minimize total loss, but faster!   
> Shuffle the training examples for each epoch.

### 防止过拟合

* Early Stopping：画出学习曲线(Learning Curves)  
{% asset_img stopearly.png %}

* Weight Decay (One kind of regularization)  
{% asset_img WeightDecay.png %}

* Dropout (A kind of ensemble)

> Each neuron has p% to dropout;
> For each mini-batch, we resample the dropout neurons and use the new network for training.

* 优化神经网络结构 (CNN is a very good example)

## 神经网络变体

### Convolutional Neural Network (CNN)

CNN的三条性质：

* Some patterns are much smaller than the whole image
* The same patterns appear in different regions.
* Subsampling the pixels will not change the object

### Recurrent Neural Network (RNN)