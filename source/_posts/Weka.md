---
title: Weka Simple Introduction
date: 2017-12-23 13:42:49
tags:
  - ML
categories:
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

[Weka](https://www.cs.waikato.ac.nz/~ml/weka/)是一个轻量级的开源数据挖掘工具（used in GUI or called from code），在简单使用一些机器学习算法或者进行一些实验性的探索时很好用。
<!--More-->

## Weka GUI操作简介
打开`Weka`图形界面后会看到5个应用：

* Explorer
* Experiment
* KnowledgeFlow
* Workbench
* Simple CLI

### Explorer
在`Explorer`中即可完成整套机器学习任务：

1. `Preprocess`：选择和调整数据
2. `Classify `：训练和测试学习模型
3. `Cluster `：学习数据聚类
4. `Associate`：学习联合数据
5. `Select attributes`：选择最相关的数据属性
6. `Visualize`：可视化2维数据图像

### Experiment
方便用户创建、执行、修改和分析实验：可以在多个数据集上执行多个算法并分析效果。

1. `Setup`:设置实验环境
2. `Run`: 执行实验
3. `Analysis`：分析实验评估结果

### KnowledgeFlow
`KnowledgeFlow`是`Explorer`的替代方案，为`Weka`中的核心算法提供了图形化前端。

### Simple CLI
`Simple CLI`是一个简单的*weka shell*，可以在其最后的文本框中输入执行*weka command*。