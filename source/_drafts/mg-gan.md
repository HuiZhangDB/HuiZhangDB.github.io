---
title: 用 GAN 生成音乐片段
date: 2018-05-24 19:39:04
tags:
  - music
  - midi
  - DL
categories:
---

本文介绍了两种基于对抗生成网络的音乐生成模型。鉴于近年来 GAN 的大火，其在音乐上的应用也开始逐渐兴起。

<!--More-->

## C-RNN-GAN
`C-RNN-GAN`是论文 *Continuous recurrent neural networks with adversarial training* 中提出的模型。实验室师兄 @[Kue](http://fujiaqi.com/) 在知乎上有简要的介绍：

> GAN在音乐生成的首次应用，也是GAN处理连续序列数据的针对性研究。针对以往音乐计算研究中使用符号特征（Symbolic Representation）的不足（计算机更容易理解数字表达），以及GAN的优势，提出了一种LSTM/RNN的GAN网络。训练预测数据为作者下载的古典MIDI音乐，使用Tone length, Frequency, Intensity 和Timing作为特征。生成网络结构为2层单向LSTM，对抗网络为2层双向LSTM，每次生成指定长度×88音阶数据。生成音乐的评价使用韵律学的方式，根据Polyphony（两个音同时弹奏的频率）、Scale consistency（标准音程的比例）、Repetitions（音符组合重复的频率）、Tone span（整段音乐的最低最高音阶差）四个方面计算。

<div align=center>
{% asset_img c-rnn-gan.jpg %}
</div>

但这个模型存在一些缺点：

1. 单音轨的音乐生成效果比较稳定，多音轨的结果听起来很奇怪；
2. 只能生成钢琴曲。

* 模型训练 270 次后的生成效果：



## MuseGAN
个人觉得这是音乐生成的*state of art*。`musegan`是业界大牛 Yi Hsuan 的 MACLab 最新研究成果，发布在今年的人工智能顶会 AAAI 上：

Hao-Wen Dong\*, Wen-Yi Hsiao\*, Li-Chia Yang and Yi-Hsuan Yang,
"**MuseGAN: Multi-track Sequential Generative Adversarial Networks for
Symbolic Music Generation and Accompaniment**,"
in *AAAI Conference on Artificial Intelligence* (AAAI), 2018.

最大的优势是：**可以生成多乐器的复调音乐**。复杂的生成网络：

{% asset_img musegan.png %}

包含了音乐的全自动生成模块和伴奏生成模块。使用多个生成器解决互相依赖的多音轨旋律生成；使用 CNN 来理解音乐织体(Music Texture)。把音乐自动生成的模型简化抽象一下：

{% asset_img multitrack3.png %}

两组生成器，一组于协调音轨间的和弦关系；一组用于组织音轨内部的旋律生成。

模型训练50006次后的生成效果：



非常有启发的是，这个研究分析了音乐的时间结构 (temporal structure)：

{% asset_img temporal_structure.png %}

基于这个时间结构，我们可以把 MIDI 转为钢琴卷帘矩阵，然后看做一个大小固定的黑白图片：

<div align=center>
{% asset_img pianoroll.png %}
</div>

这样就可以使用图片的方式来设计和训练神经网络了（其生成器用 CNN 来实现）。

