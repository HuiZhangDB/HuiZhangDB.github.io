---
title: 音乐摘要（Music Summarization）文献调研
date: 2018-10-29 20:36:15
tags:
  - MIR
categories:
---

最近的研究要提取音乐中的亮点部分（副歌部分）作为“摘要”展示，这篇博文用于简要调研与这个主题相关的一些研究。

主题检索关键词：`Music Thumbnailing`, `Highlight Extraction`, `Chorus Detection`。

<!--More-->

维基百科对于副歌的定义：

>副歌（英文为Refrain或惯称Chorus）是歌曲中一句或一段重复的歌词及音乐段落。通常出现在几段正歌（又称作主歌，英文为Verse）之间，即由第一节正歌唱到副歌后，连接第二节正歌再返回副歌，如此类推。有些副歌在重复时，每段的歌词完全相同，但是也有一些歌曲在副歌的重复部分中，会对歌词做出一定的改动。副歌与正歌一起组成正副歌形式，作为流行音乐中最重要最常用的音乐形式之一，通常体现为二部曲式，某些歌曲更会加入音乐过门或是桥段来作衔接。一般作曲者也会先写出副歌部分，后再进行正歌的创作。为了让整体的关系变得更紧密，许多流行曲也会编写导歌（英文为Pre-Chorus，也称为Post-Chorus）作为两者之间的连系，即由正歌至导歌后才到副歌，为副歌预先作好铺排，从而丰富副歌歌词所表达的内在含意。

之所以要强调音乐的副歌部分是因为：

> 副歌采用重复的形式，在歌曲中通常位于情感上的高潮部分，以其概括性令听者易于记忆。事实上，大部分人初次听到一首歌曲后，最先记住的就是它的副歌部分，一般人哼唱一首歌的时候也大都哼唱其副歌部分。

## 早期方法

以往的研究一般假设：反复出现次数最多的旋律模式即为副歌。这些研究往往会首先使用`self- similarity matrix (SSM)`或者`hidden Markov model (HMM)`等方法将歌曲分成多个片段，然后提取出最频繁出现的作为结果：

[1] Bartsch M A, Wakefield G H. Audio thumbnailing of popular music using chroma-based representations[J]. IEEE Transactions on multimedia, 2005, 7(1): 96-104.  
[2] Cooper M, Foote J. Summarizing popular music via structural similarity analysis[C]//Applications of Signal Processing to Audio and Acoustics, 2003 IEEE Workshop on. IEEE, 2003: 127-130.  
[3] Logan B, Chu S. Music summarization using key phrases[C]//icassp. IEEE, 2000: II749-II752.  
[4] Peeters G, La Burthe A, Rodet X. Toward automatic music audio summary generation from signal analysis[C]//ISMIR. 2002: 1-1.


但这些研究具有一些缺陷。首先，这里对于副歌的假设就可能出现错误（有些歌曲的副歌部分并不是出现次数最多的片段）；其次，对于重复出现的副歌片段无法进行区分，也就是说不能挑选出最具有代表性的一个音乐片段（随机选择其中一个可能不是很好的策略）。

## 使用用户数据

在一些在线音乐网站中，有的会使用用户的行为日志来检测音乐的亮点部分。比如[5]中用到的来自`SoundCloud`的音乐，让用户给其打了带时间戳的标签。[6]中认为用户常常会把进度条拉到一首歌最好的部分，这样就只需要在用户切到的位置附近做峰值检测了。但这些日志数据一般都不会公开。

[5] Yadati K, Larson M, Liem C C S, et al. Detecting Drops in Electronic Dance Music: Content based approaches to a socially significant music event[C]//ISMIR. 2014: 143-148.  
[6] Bittner R M, Gu M, Hernandez G, et al. Automatic playlist sequencing and transitions[C]//Proc. Int. Society of Music Information Retrieval Conf. 2017.  


## 注意力机制

[7] Ha J W, Kim A, Kim C, et al. Automatic Music Highlight Extraction using Convolutional Recurrent Attention Networks[J]. arXiv preprint arXiv:1712.05901, 2017.  
[8] Huang Y S, Chou S Y, Yang Y H. Pop Music Highlighter: Marking the Emotion Keypoints[J]. arXiv preprint arXiv:1802.10495, 2018.

[7]和[8]都提出了基于注意力机制的神经网络模型来检测音乐副歌。不同之处在于[7]使用的是音乐风格（Genre）标签来训练模型，而[8]使用的是音乐情感（Emotion）标签来进行训练（具体的网络结构也有不同）。最后[8]得到的结果要好一点（THE-STATE-OF-ART）。
