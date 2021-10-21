---
title: 聚类
date: 2017-04-27 14:40:01
tags:
  - Math
categories:
  - 应用工程数学
---

## 相似性衡量 

* 距离
* 相似性
* 核函数
* DTW（dynamic time warping 一种特殊的距离算法）

## 聚类算法

* 划分聚类(Partition-based methods)  
确认聚类数量，挑选初始点 -> 类内的点足够近，类间的点足够远。

* 密度聚类(Density-based methods)  
指定圈的最大半径，包含的最少点数量 -> 画圈。

* 模型聚类(Model-based methods)  
基于概率模型和神经网络模型 -> 同一类属于同一概率分布

* 层次聚类(Hierarchical methods)  
自下而上法 (bottom-up) 和自上而下法 (top-down)，根据linkage迭代联合或者排异。

* 网格聚类(Grid-based methods)
将数据空间划分为网格单元，将数据对象集映射到网格单元中。计算每个单元的密度，根据阈值确定高密度单元 -> 相近的高密度单元组成类

<!--More-->
### 常用聚类算法
[Overview of clustering methods](http://scikit-learn.org/stable/modules/clustering.html#clustering)  

* k-means
{% asset_img kmeans01.png %}
{% asset_img kmeans02.png %}

* GMM
{% asset_img gmm01.png %}
{% asset_img gmm02.png %}

## 数据简化
* 变化
* 降维
* 抽样