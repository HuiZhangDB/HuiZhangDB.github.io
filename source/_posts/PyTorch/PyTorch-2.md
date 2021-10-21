---
title: PyTorch 导入数据集
date: 2018-04-19 17:43:40
tags:
  - DL
categories:
  - PyTorch
---

对于任何机器学习模型的训练过程，导入数据都是最基础的一步。在 PyTorch 中，可以使用一些 Python 的标准库将数据导入为 numpy array，然后再转换为 `torch.*Tensor`。

> * For images, packages such as Pillow, OpenCV are useful
> * For audio, packages such as scipy and librosa
> * For text, either raw Python or Cython based loading, or NLTK and SpaCy are useful

<!--More-->

PyTorch 还专门为视觉定制了一个包`torchvision`：

* `torchvision.datasets`可以直接导入一些常用的图形数据库，如 Imagenet, CIFAR10, MNIST 等。
* `torchvision.transforms`还包含了很多图形数据转换器（data transformers for images）。

另外，[torchaudio](http://pytorch.org/audio/index.html?highlight=torchaudio#module-torchaudio) 提供了一个简单的音频数据的 I/O。但它只提供了专用于两个数据集 VCTK, YesNo 的数据导入操作。如果想使用其他数据集，还是要定制自己的`torch.utils.data.Dataset`，然后结合`torch.utils.data.DataLoader`来使用。举例：

```python
#! usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'huizhang'

import torch.utils.data as data
import torch
import torchaudio
import os
import csv
import numpy as np

class MyAudioDataset(data.Dataset):

    categories = ('Passionate', 'Bittersweet', 'Sweet', 'Witty', 'Campy',
               'Fiery', 'Volatile', 'Wry', 'Intense', 'Boisterous', 'Fun', 'Rollicking',
               'Rousing', 'Amiable-good natured', 'Literate', 'Brooding', 'Visceral', 'Tense - Anxious',
               'whimsical', 'Autumnal', 'Wistful', 'Silly', 'Cheerful', 'Poignant', 'Rowdy', 'Agressive',
               'Confident', 'Humorous')

    def __init__(self, ptfile, audiodir=None, labelfile=None):

        self.ptfile = ptfile
        self.audiodir = audiodir
        self.labelfile = labelfile

        if not os.path.exists(ptfile):
            if audiodir==None or labelfile==None:
                raise ValueError('No ptfile. Lack path for audiodir and labelfile')
            self._process_audio_and_labels_into_tensorsfile()

        self.data, self.label = torch.load(self.ptfile)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        audio, target = self.data[item], self.label[item]

        return audio, target

    def _process_audio_and_labels_into_tensorsfile(self):
        mp3s = [f for f in os.listdir(self.audiodir) if f[-4:]=='.mp3' ]
        signals = []
        labels = []

        for f in mp3s:
            print(f)
            full_path = os.path.join(self.audiodir, f)
            sig, sr = torchaudio.load(full_path)
            sig = torch.transpose(sig, 0, 1) # transpose dim0 and dim1 to put channel in different columns
            sig_norm = sig[:, -25*44100:] # convert signals with equal length (25s * 44.1khz)
            signals.append(sig_norm)

        with open(self.labelfile) as f:
            reader = csv.reader(f)
            for r in reader:
                # for  multi-target
                labels_in_num = []
                for label_str in r:
                    label_num = MyAudioDataset.categories.index(label_str) # convert label string into index of categories tuple
                    labels_in_num.append(label_num)
                labels.append(torch.from_numpy(np.array(labels_in_num))) # saved as torch

        torch.save((signals, labels), self.ptfile)  # each one is saved as a list of tensors with the same size

if __name__ == '__main__':
    audiodir = '../datasets/MIREX-like_mood/Audio'
    labelfile = '../datasets/MIREX-like_mood/categories.txt'
    ptfile = 'MIREX-like_mood.pt'

    mydataset = MyAudioDataset(ptfile, audiodir, labelfile)
    print(mydataset.__getitem__(i))
```

Tips：

* PyTorch 所有的数据集对象都是`torch.utils.data.Dataset`的子类。在继承它的时候必须要重写其`__len__`和`__getitem__`方法；
* 为了方便数据的存储和读入，可以将数据存为`.pt`文件（PyTorch 的标准数据文件）；
* 对于多通道输入对象（如，3通道的RGB图片、2通道的MP3音乐），应该存储为 nAttributes * nChannels，即`torchaudio.load`导入的信号需要转置再存储；
* 标签要转换为标签组的下标后再写入文件，以方便训练和计算损失。

> torchaudio 报错：in audio_open(): NoBackendError。--> 缺少解码器：apt install libav-tools

## 参考资料
[1] [这里](https://www.kaggle.com/solomonk/pytorch-speech-recognition-challenge-wip)把音频转换为了频谱图片然后再导入计算，有点意思。
