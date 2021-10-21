---
title: Python小贴士
tags:
  - python
categories:
  - Python基础
date: 2016-12-26 23:50:33
---

## `with`...`as`
有一些任务，可能事先需要设置（setup），事后做清理工作（teardown）。对于这种场景，Python的with语句提供了一种非常方便的处理方式。一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。

**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000