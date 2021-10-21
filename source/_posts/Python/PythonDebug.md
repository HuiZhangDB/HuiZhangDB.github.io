---
title: Python错误、调试和测试
tags:
  - python
categories:
  - Python基础
---

## 错误处理
`try`...`except`...`finnaly`...

<!--More-->
## 调试
### print
简单粗暴不加以赘述
### assert
凡是用`print`来辅助查看的地方，都可以用断言`assert`来代替。如果断言失败，`assert`语句本身就会抛出`AssertionError`。

在启动Python解释器时，可以使用`-O`参数来关闭`assert`,此时所有的`assert`语句可以被看做`pass`。
### logging
`logging`不会抛出错误，而且会=可以输出到文件。
### pdb和IDE
虽然IDE用起来比较方便，但是最后你会发现logging才是终极武器。

## 单元测试
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作，是未来重构代码的信心保证。


单元测试的测试用例要覆盖常用的输入组合、边界条件和各种异常。单元测试代码要非常简单，如果测试代码太复杂，那么它可能本身就有bug。

## 文档测试
`doctest`可以直接提取注释中的代码并执行测试。`doctest`严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候可以用`...`表示中间一大段烦人的输出。测试文档{%asset_link mydict.py mydict.py%}

```python
#!/usr/bin/env python
#coding = utf-8

class Dict(dict):
	'''
	a simple dict

	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1,b=2,c='3')
	>>> d2.c
	'3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Dict' object has no attribute '%s'" %key)

	def __setattr__(self,key,value):
		self[key] = value


if __name__ == '__main__':
	import doctest
	doctest.testmod()
```

```python
$ python mydict.py
$
#什么输出也没有说明doctest的运行都是正确的.
#如果程序有问题比如注释掉'__getattr__()'，再运行就会出错：
$ python mydict.py
**********************************************************************
File "mydict.py", line 10, in __main__.Dict
Failed example:
    d1.x
Exception raised:
    Traceback (most recent call last):
      ...
    AttributeError: 'Dict' object has no attribute 'x'
**********************************************************************
File "mydict.py", line 16, in __main__.Dict
Failed example:
    d2.c
Exception raised:
    Traceback (most recent call last):
      ...
    AttributeError: 'Dict' object has no attribute 'c'
**********************************************************************
1 items had failures:
   2 of   9 in __main__.Dict
***Test Failed*** 2 failures.
```
**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000