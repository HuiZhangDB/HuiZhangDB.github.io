---
title: Python基础语法
tags:
  - python
categories:
  - Python基础
date: 2016-12-26 23:50:33
---

## 数据类型
* 整数
* 浮点数
* 布尔值
* 空值
* 字符串
* list和tuple
* dict和set

<!--More-->

## 函数参数
1. 必选参数
2. 默认参数	  
	默认参数必须指向不变参数
3. 可变参数  
	`*args`
4. 关键字参数  
	`**kw`

`参数组合的定义顺序必须是：必选参数、默认参数、可变参数、关键字参数。任意参数都可以通过类似这样的方式进项定义:func(*args,**kw)`

## 高级特性
* 切片(Slice)

```
L[start:end:every]
```
* 迭代

```python
>>> for x, y in [(1,2),(3,4),(5,6)]:
...     print x,y
... 
1 2
3 4
5 6
>>> for x in enumerate(['a','b','c']):
...     print x
... 
(0, 'a')
(1, 'b')
(2, 'c')

#可以这样判断是否为迭代对象
from collections import Iterable
print isinstance('abc',Iterable);#True
print isinstance(123,Iterable);#False
```
* 列表生成式

```python
>>> L = ['Hello','Word','I\'m',18,'years','old']
>>> [l.lower() for l in L if isinstance(l,str)]
['hello', 'word', "i'm", 'years', 'old']
```
* 生成器

```python
#一边循环一边计算后续元素以节省大量空间（不必创建完整的list）
>>> def odd():
...     print 'step1'
...     yield 1
...     print 'step2'
...     yield 2
...     print 'step3'
...     yield 3
... 
>>> o = odd()
>>> o.next()
step1
1
>>> o.next()
step2
2
>>> o.next()
step3
3
>>> o.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> o = odd()
>>> for n in o:
...     print n
... 
step1
1
step2
2
step3
3
```
**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000