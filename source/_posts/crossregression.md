---
title: 交叉数据集和交叉文化下的音乐情感识别
date: 2017-05-31 20:52:38
tags:
  - MER
  - dataset
categories:
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

本文是作者在阅读*Cross-dataset and Cross-cultural Music Mood Prediction: A Case on Western and Chinese Pop Songs*这篇论文后的阅读笔记和总结感想。

<!--More-->

## 研究概述

很少有人研究情感回归模型在交叉数据集中的泛化能力（generalizability），或者说通用性，尤其是跨文化的音乐情感研究就更少了。*Hu X*和*Yang Y H*提取了3个不同文化背景流行音乐数据集的5种音乐情感特征集，评估了它们训练的情感回归模型的性能，特别是在交叉数据集上的适用性。

他们还设计进行了5个实验来探究`数据集大小`、`标记可靠性`、`音乐文化背景`和`注释者文化背景`对情感回归模型的`性能(performances)`以及`泛化能力(generalizability)`的影响。

整个研究回答了两个问题:

1. 哪种声学特征对音乐情感回归影响最大？在单一数据集内或者交叉数据集的情况下一样吗？
2. 使用一个数据集训练的情感回归模型适用于另一个数据集吗？数据集的大小、标记可靠程度和文化背景如何影响模型在交叉数据集下的泛化能力。

## 实验材料
### 3个不同文化背景下的流行音乐数据集

|||MER60|CH818|AMG1608|
|-----|----|----|----|----|
|Music|Format|Audio (mp3)|Audio (mp3)|Audio (mp3)|
||Size|60|818|1608|
||Culture|Western|Chinese|Western
||Length|30 seconds|30 seconds|30 seconds|
||Segment selection|`Chorus part`; `manual selected`|`Segment with the strongest emotion`|Audio previews from 7 digital|
|Annotators|Type|Volunteers|`Experts`|MTurk workers|
||Culture|Chinese|Chinese|Western|||Number|40 per clip|3 per clip|15–32 per clip|
||Scale|Continuous [-5, 5]|Continuous [-10, 10]|Continuous [-1, 1]|
|Annotations|Dimensions|V.A.|V.A.|V.A.|
||Interface|2-D interactive interface|two separate sliding bars|2-D interactive interface|
||Emotion|Intended|Intended|Intended|
||\\(\alpha\\)|V: 0.387; A: 0.704|V: 0.491; A: 0.617|V: 0.306; A: 0.458|

* 其中，\\(\alpha\\)是指`Krippendorff’s alpha`，用以量化标记可靠性；
* CH818使用回归模型自动识别提取了情感最为强烈\\((|valence|^2+|arousal|^2)\\)的30秒；
* CH818用`Pearson相关系数`表明了3个专家的打分是合理的（和均值非常接近）；
* AMG1608的每10个音乐片段中有1个复制，如果复制的音乐片段打分误差超过10%，该注释者的打分数据将会被删除。

### 5种声学特征（15个特征集合）

{% asset_img features.png %}

### 1个回归算法

* `Support Vector Regression(SVR)`模型 
* 使用`径向基函数(RBF)`作为核函数
* 通过`网格搜索`优化参数C和gamma

## 实验设计
首先，分别在2个维度下，评估15个单一数据集在9个数据集组合上（3个单一数据集，6个交叉数据集）的回归表现，用`step-wise forward feature selection algorithm`（一种贪婪算法，用局部最优近似全局最优）来选择特征集组合。

使用上述步骤中选择的特征进行5个实验：

{% asset_img experiments.png %}

* 实验1用以表明融合特征集比单一特征集效果有所提升；
* 实验2控制数据集大小，与实验1比较以验证数据集大小对预测能力的影响；
* 实验3控制训练集标记的可靠程度，与实验2比较以验证训练集标记可靠性对预测能力的影响；
* 实验4控制训练集和测试集的标记可靠性，与实验3比较以验证测试集标记可靠性对预测能力的影响；
* 实验5改变训练集和测试集的标记可靠性，得到一系列组合，以量化标记可靠程度对预测能力的影响。

## 实验结果
### [问题一] 情感回归的音频特征
1. 愉悦度维度的特征选择：loudness_ psysound、harmony_psysound、timbre_psysound；
2. 唤醒度维度的特征选择：timbre_psysound、rhythm_mirtb；
3. 单独的`Loudness`和`Timbre`特征在愉悦度和唤醒度上表现都非常好；
4. 单独的`Rhythm`特征对愉悦度预测有效；
5. 单独的`Chroma`特征有助于唤醒度预测，且对单一数据集内的愉悦度预测有用；
6. `Harmony`特征有利于单一数据集内的愉悦度预测，但与唤醒度预测无关；
7. 多种特征的联合可以提高模型的预测能力，尤其是在愉悦度维度。

### [问题二] 交叉数据集通用性
1. 训练集越大，愉悦度和唤醒度的预测越好；
2. 平衡训练集和测试集的标记可靠性对交叉数据集愉悦度预测有用，而可靠程度越高，唤醒度预测越准；
3. 在愉悦度维度，相同的文化背景对交叉数据集预测非常重要，如果歌曲本身和打标签的人都是不同文化背景下的，那么模型的泛化能力将无法保证，除非训练集和测试集都有相当高的标记可靠性；但文化背景对唤醒度预测影响不大，只要相关数据集的标记可靠性不是太低，情感回归模型在交叉数据集的表现和单一数据集内的表现相似。

## 启发和收获

1. 数据集标签的评估量化数值`Krippendorff’s alpha`
2. AMG1608注释者的标记质量控制策略
3. 多特征集的融合互补有助于提高预测能力
4. 该论文的实验设计逻辑非常严谨，变量控制严格，值得学习；
5. 实验的结果分析和结论不一样，结果分析应该就实验数据表现的方方面面都做以分析，甚至可以发掘到意料之外的有意思信息；而结论则是回答实验之初提出的问题。


## 参考文献
[1] *Hu X, Yang Y H. Cross-dataset and Cross-cultural Music Mood Prediction: A Case on Western and Chinese Pop Songs[J]. IEEE Transactions on Affective Computing, 2016.*