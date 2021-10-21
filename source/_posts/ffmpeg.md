---
title: FFmpeg实用操作
date: 2017-10-24 11:53:55
tags:
  - ffmpeg
categories:
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

最近的实验中有许多音频处理的工作，使用`FFmpeg`较为频繁，本文用于记录实验中使用过的操作（[官方文档](https://ffmpeg.org/ffmpeg-utils.html#time-duration-syntax)）以及其中遇到的一些问题（感谢[DavidAQ](http://davidaq.com/tutorial/2014/11/20/ffmpeg-commands.html)的答疑解惑）。
<!--More-->

### 转格式
```shell
$ ffmpeg -i Input.mp3 Output.wav
```

### 截取
官网提供的命令:

```shell
$ ffmpeg -i Input.mp3 -ss Starttime -t Duration Output.mp3
```

但是经过FFmpeg处理的音频文件，在苹果系统(OSX, IOS)以及苹果的播放器(ITunes, QuickTime)上往往会显示错误的长度时间。这是`FFmpeg`的Bug，需要添加参数`-write_xing`规避：

```shell
$ ffmpeg -i Input.mp3 -write_xing 0 -ss Starttime -t Duration Output.mp3
```

或者指定音频编码器直接复制原来的编码：

```shell
$ ffmpeg -ss Starttime -i Input.mp3 -t Duration -acodec copy Output.mp3
```
把`-ss`提到`-i`前面作为输入文件的处理参数，这样会先跳转到`Starttime`再开始解码，而原来的会从开始解码然后丢弃掉`Starttime`之前的结果，同时`-acodec copy`表示音频的编码不会发生改变，这样会大大提高速度。

> 注意处理文件如果不是图片，不要让输入文件与输出文件相同，覆盖后会出现神奇的Bug。

### 淡入（淡出）
`FFmpeg`的音频过滤器可以实现这一效果：

```shell
$ ffmpeg -i Input.mp3 -write_xing 0 -af afade=t=in:ss=0:d=15 Output.mp3
```