---
title: MER 声学特征提取
date: 2017-04-29 16:02:17
tags:
  - MER
  - tool
  - feature
categories:
---

## 特征集和提取工具
最近的任务目标是：确定`音乐情感特征集（声学特征）`和`提取方法`  

<!--More-->
 
为了确定要提取的音乐情感声学特征集`Acoustics Features Set for Music Emotion`，最近看了很多相关文章（{% post_link MERFeature %}）。发现对于以前的音乐情感研究工作，研究人员多数使用[Marsyas](http://marsyas.info/)（最新版本为2015年发布）和[MIRtoolbox](https://cn.mathworks.com/matlabcentral/fileexchange/24583-mirtoolbox)（MATLAB工具包）。
  
然而近年来有一个专用于`情感计算`和`音乐信息检索`的特征提取工具`openSMILE`异军突起，这是由TUM（德国慕尼黑工业大学）开发的开源工具，近年来多个Challenge（ISComparE, MediaEval, Emobase等）频繁使用其作为`Baseline feature dataset`的提取工具，`openSMILE`针对这几个挑战也在其发布的版本中包含了相应的`config`文件。（{%  post_link openSMILE openSMILE安装指南 %}）

最终，我决定使用`the 2013 Computational Paralinguistics Evaluation (ComParE)`[1] 提出的基线数据集{% post_link IS13feature %}（它同样在`MediaEval 2014`中被作为基线数据集[2]）。它在[3] 中表现出了评估speech, music, 以及 acoustic events的多维度情感鲁棒性。

同时，我决定使用`openSMILE`作为特征提取工具。

## 提取流程
拟下载的音乐文件为`MP3`格式，而`openSMILE`只支持`WAV`，所以首先需要用`ffmpeg`转换格式：

```
$ sh transformat.sh
```
```sh
#!/bin/sh
#transformat.sh
#transform MP3 to WAV

echo "Please Enter the MusicPath -> "
read mpath
cd ${mpath}
mkdir 'wav'

for m in *.mp3
do
ffmpeg -i "${m}" "wav/${m%.mp3}.wav"
done

```

然后使用`openSMILE`批量提取音乐特征：

```
$ sh smileEX.sh
```

```sh
#!/bin/sh
#smileEX.sh
#Extract features in batch by using openSMILE

echo "Please Enter the openSMILE Path -> "
read opensmile
echo "Please Enter the Music Path -> "
read mpath
cd ${mpath}

for m in *.wav
do
${opensmile}/SMILExtract -C "${opensmile}/config/IS13_ComParE.conf"  -I "${m}"  -O  IS13features.arff  -instname "${m%.wav}"
done
```
从QQ音乐和网易云音乐下载的测试音乐特征提取成功。

## Reference
[1] Schuller B, Steidl S, Batliner A, et al. The INTERSPEECH 2013 computational paralinguistics challenge: social signals, conflict, emotion, autism[J]. 2013.  
[2] Aljanaki A, Yang Y H, Soleymani M. Developing a benchmark for emotional analysis of music[J]. PloS one, 2017, 12(3): e0173392.  
[3] Weninger F, Eyben F, Schuller B W, et al. On the acoustics of emotion in audio: what speech, music, and sound have in common[J]. 2013.


