---
title: 使用Magenta生成音乐
date: 2018-03-20 21:44:39
tags:
  - magenta
  - music
  - midi
categories:
  - Music Generation
---

最近开始入门计算机自动作曲领域（`算法作曲(algorithmic composition)`或称`自动作曲(automated composition)`）。计算机自动生成音乐的目标有节奏和旋律、和声/和弦、伴奏(acompaniment)、复调(counterpoint)、改编(arrangement)等。它的实现一般都是基于概率理论的（或者说其数学本质就是一个概率问题）：假设旋律（一段包含音高的时间序列）服从某种概率分布，求解这个分布的近似解（或者加上和声，求解它们的联合概率分布模型）。

[Magenta](https://github.com/tensorflow/magenta/blob/master/README.md#using-magenta) 是Google Brain团队使用深度学习研究自动作曲的开源项目，本文将简单描述使用Magenta生成MIDI音乐的过程。

<!--More-->

## 安装和配置支持Python3的Magenta环境
```sh
# 安装[Miniconda for python3](https://conda.io/miniconda.html)
$ sh Miniconda3-latest-MacOSX-x86_64.sh

# 创建Magenta的conda环境
$ conda create -n magenta python=3.6 jupyter

# 激活环境
$ source activate magenta

# 安装pip包
pip3 install magenta
```

## 使用Melody RNN模型生成旋律

```sh
# 如果没有设置永久环境变量(.bashrc/.bash_profile)，需要激活conda环境
# $ source $HOME/miniconda3/bin/activate

# 下载配置文件[basic_rnn/lookback_rnn/attention_rnn](https://github.com/tensorflow/magenta/tree/master/magenta/models/melody_rnn)

$ source activate magenta
$ BUNDLE_PATH=<absolute path of .mag file>
$ CONFIG=<one of 'basic_rnn', 'lookback_rnn', or 'attention_rnn', matching the bundle>

$ melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]"

# num_outputs表示生成旋律的数量
# num_steps表示以16分音符为单位的旋律长度
# primer_melody是输入的初始音高（如：小星星[60, -2, 60, -2, 67, -2, 67, -2]）
# primer_melody可以被primer_midi替换：--primer_midi=<absolute path to magenta/models/melody_rnn/primer.mid>
```

## 播放和评估MIDI效果
安装[FluidSynth](https://github.com/FluidSynth/fluidsynth)MIDI合成器:

```sh
$ brew install fluidsynth
```

并下载[SoundFont](https://musescore.org/zh-hans/node/36171#sf2-soundfonts)，为MIDI合成器提供乐器录音和音效。

```sh
$ fluidsynth /path/to/soundfont.sf2 /path/to/MIDI.mid
```
> 或者其实可以直接使用[musescore](https://musescore.org/zh-hans/download)来播放，好处是有GUI可以直接可视化乐谱！
