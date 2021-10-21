---
title: Python面向对象高级编程
tags:
  - python
categories:
  - Python基础
---

## 实例动态绑定
通常情况下，我们可以给实例绑定任何属性和方法，这就是动态语言的灵活性。但是给一个实例绑定的方法对另一个实例是不起作用的。为了给所有实例都绑定方法，可以给class绑定方法。

```python
def addmethod(self):
	pass
	
Student.addmethod = MethodType(addmethod,None,Student)
```

<!--More-->
如果想要限制class的属性，可以使用特殊变量`__slots__`来限制该class能添加的属性：

```python
>>> class Student(object):
...     __slots__ = ('name','age')#用tuple定义允许绑定的属性名称
... 
>>> s = Student()
>>> s.name = 'Micheal'
>>> s.age = 8
>>> s.score = 90
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```
需要注意的是，`__score__`中定义的属性仅对当前类起作用，对继承的子类是不起作用的。

```python
>>> class GraduateStudent(Student):
...     pass
... 
>>> g = GraduateStudent()
>>> g.score = 99
>>> g.score
99
```
## 使用@property
`@property`是Python内置的一个装饰器，可以把一个getter方法变成属性，同时还会创建另一个装饰器`@xxx.setter`，负责把一个setter方法变成属性赋值，这样我们就拥有了一个可控的属性操作。如果只定义getter方法而不定义setter方法就会得到一个只读属性。

```python
>>> class Student(object):
...     @property
...     def score(self):
...             return self._score
...     @score.setter
...     def score(self,value):
...             if not isinstance(value,int):
...                     raise ValueError('score must be an integer')
...             if value<0 or value>100:
...                     raise ValueError('score must between 0~100')
...             self._score = value
... 
>>> s = Student()
>>> s.score = 99
>>> s.score
99
>>> s.score = 101
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 10, in score
ValueError: score must between 0~100
>>> s.score = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in score
ValueError: score must be an integer
```
注意这里的`score`是一个property对象，getter方法和setter方法重用了这个名字，而`_score`是私有属性。实际属性值储存在`_score`中，`score`则为这个私有变量提供接口。如果混淆了两者就会出现可怕的bug：

```python
>>> class Student(object):
...     @property
...     def score(self):
...             return self.score
...     @score.setter
...     def score(self,value):
...             if not isinstance(value,int):
...                     raise ValueError('score must be an integer')
...             if value<0 or value>100:
...                     raise ValueError('score must between 0~100')
...             self.score = value#这里会无法停止循环调用score的setter方法
... 
>>> s = Student()
>>> s.score = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
  File "<stdin>", line 11, in score
RuntimeError: maximum recursion depth exceeded
```
## 多重继承
一个子类可以通过多重继承同时获得多个父类的所有功能。
### Mixin
在设计类的继承关系时，通常主线都是单一继承下来的，例如，`Dog`继承自`Animal`。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让`Dog`除了继承自`Animal`之外再同时继承`Runnable`。这种设计通常称之为`Mixin`。

```python
class Dog(Animal,Runnable):
	pass
```

为了更好地看出继承关系，我们把`Runnable`和`Flyable`改为`RunnableMixin`和`FlyableMixin`。类似的，还可以定义出肉食动物`CarnivorousMixin`和植食动物`HerbivoresMixin`，让某个动物同时拥有好几个Mixin：

```python
class Dog(Animal,RunnableMixin,CarnivorousMixin):
	pass
```
Mixin的目的就是给一个类增加多个功能，这样在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。

Python允许使用多重继承，因此Mixin是一种常见设计。而只允许单一继承的语言（如Java）不能使用Mixin的设计。
## 定制类
Python中有许多特殊用途的函数可以帮助我们定制类

```python
__slots__
__len__
__str__
__repr__
__iter__
__getitem__
__getattr__
__call__  #可使用callable()来判断对象是否是“可调用”对象
```
## 使用元类
`type()`既可以返回一个对象的类型，还可以创建出新的类型。  
`metaclass`允许创建类或者修改类，可以把类看成是metaclass创建出的来的“实例”。

*正常情况下不会碰到需要使用`metaclass`的情况，所以现在先略过。*


**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000