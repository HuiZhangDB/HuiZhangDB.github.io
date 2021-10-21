---
title: Python面向对象编程
tags:
  - python
categories:
  - Python基础
date: 2016-12-26 23:50:33
---

`数据封装`、`继承`和`多态`是面向对象的三大特点，`类`和`实例`是面向对象最重要的概念。在类中定义的函数与普通函数相比只有一点不同，就是第一个参数永远是是咧变量`self`，并且在调用时不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以仍然可以使用默认参数、可变参数和关键字参数。

<!--More-->

## 数据封装
通过在实例上调用方法可以直接操作对象内部的数据，但无需知道方法内部的实现细节。即，可以用类的方法来`封装`其数据和逻辑。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```python
>>> class Student(object):
...     def __init__(self,name,score):
...             self.name = name
...             self.score = score
...     def print_score(self):
...             print '%s: %s' %(self.name, self.score)
... 
>>> bart = Student('Bart',98)
>>> lisa = Student('Lisa',80)
>>> bart.age = 8
>>> bart.age 
8
>>> lisa.age 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```
## 访问限制
想要类的内部属性不被外部访问，可以加上前缀`__`将其定义为私有变量。

```python
>>> class Student(object):
...     def __init__(self,name,score):
...             self.__name = name
...             self.__score = score
...     def print_score(self):
...             print '%s: %s' %(self.name, self.score)
... 
>>> bart = Student('Bart',98)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
```
这样使得外部代码不能随意修改对象内部的状态。但也可以使用`get_name`或者`set_score`这样的方法获取或者修改（可以检查参数避免传入无效参数）类属性。

```python
def get_name(self):
	return self.__name

def set_score(self,score):
	if 0 <= score <= 100:
			self.__score = score
	else:
		raise ValueError('bad score')	
```
但值得注意的是，还有一种以一个下划线`_`开头的实例变量名，比如`_name`，这样的实例变量名外部是可以访问的，但按照约定俗成的规定，看到这样变量的意思是：“虽然我可以访问，但请把我视为一个私有变量，不要随意访问。”
## 继承和多态
在定义一个class的时候可以从现有的class继承，新的class就是`子类(Subclass)`，被继承的class称为`基类、父类或超类(Superclass)`。继承可以把父类的所有功能都直接拿过来，子类只需要新增自己特有的方法，也可以把父类不合适的方法覆盖重写。

有了继承，才能有多态。多态使得调用父类型的方法时不需要考虑其切确的子类型，在运行时解释器会根据该对象的确切类型决定具体方法。在调用类实例的方法时，尽量把变量当做父类类型，这样所有的子类类型都可以被正常接收。著名的“开闭”原则：

* 对拓展开放：允许新增子类
* 对修改封闭：不需要修改依赖父类的函数

任何时候，如果没有合适的类可以继承，就继承自object类。
## 获取对象信息
在不知道对象信息的时候可以使用内置函数剖析对象获得内部数据。

```python
type(123)              #返回一个type类型，指明对象类型
isinstance('a',str)    #返回布尔值，判断对象是否是某种类型
dir('ABC')             #返回一个list，包含对象的所有属性和方法
```
**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000