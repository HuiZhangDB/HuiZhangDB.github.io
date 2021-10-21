---
title: 矩阵运算
tags:
  - python
categories:
  - Python基础
date: 2016-12-26 23:50:31
---

Python的`numpy`模块提供矩阵运算的功能，其中有两种不同的数据类型`matrix`和`array`都可以用于处理行列表示的数字元素。虽然它们看起来相似，但是在这两个数据类型上执行相同的数学运算可以得到不同的结果，其中`matrix`与MATLAB中的`matrices`等价。

具体来说，`matrix`是`array`的子类，要求维数必须为2。需要注意的是`array`的`*`表示元素分别相乘，`dot`才表示矩阵点乘。


