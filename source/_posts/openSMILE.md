---
title: openSMILE
date: 2017-04-27 14:28:08
tags:
  - MER
  - feature
  - tool
categories:
---

S1. 下载最新的稳定版本[openSMILE](http://audeering.com/technology/opensmile/#download)

S2. 下载依赖工具库  

* autotools(automake, autoconf, libtool, and m4)  
* make
* GNU C and C++ compiler gcc and g++

```
$ brew install automake
$ brew install autoconf
$ brew install libtool
$ brew install m4
$ brew install gcc
```

S3. 解压并安装

```
$ tar-zxvf opensmile-X.X.X.tar.gz
$ cd opensmile-X.X.X
$ sh buildStandalone.sh
```

S4. 测试安装是否成功  

```
$ SMILExtract -h
```
