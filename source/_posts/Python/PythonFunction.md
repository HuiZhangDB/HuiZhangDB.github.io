---
title: Python函数式编程
tags:
  - python
categories:
  - Python基础
---

函数式编程是高度抽象的编程范式,纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的函数语言，由于函数内部的变量状态不确定，同样的输入可能得到不同的输出，这种函数是有副作用的。函数式编程允许将函数本身作为参数传入另一个函数，还允许返回一个函数。

Python对函数式编程提供部分支持。由于Python允许使用变量，因此Python不是纯函数式编程语言。

<!--More-->

## 高阶函数 
接受其它函数作为参数的函数称为高阶函数

```python
#一个最简单的高阶函数
>>> def add(x,y,f):
...     print f(x)+f(y)
... 
>>> add(-5,6,abs)
11
```
### map和reduce
`map()`接受两个参数，一个函数和一个序列，将传入的函数依次作用到序列的每一个元素，并把结果作为新的list返回。

```python
#使用map规范用户输入的英文名字
>>> def adapt(s):
...     return s.capitalize()
... 
>>> L1 = ['adam', 'LISA', 'barT']
>>> L2= map(adapt,L1)
>>> print L2
['Adam', 'Lisa', 'Bart']
```
`reduce()`把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce()把结果继续和序列的下一个元素做累积计算。

```python
>>> def mul(x,y):
...     return x*y
... 
>>> def prod(L):
...     return reduce(mul,L)
... 
>>> prod([1,2,3,4,5,6])
720
```
### filter
`filter()`过滤器根据返回值是`True`还是`False`来决定是否保留该元素

```python
#删除1~100中的所有素数
>>> def notprime(n):
...     if n==1 or n==2:
...             return False
...     elif 0 in [n%i for i in range(2,n)]:
...             return True
...     else:
...             return False
... 
>>> filter(notprime,range(1,101))
[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]
```
### sorted
`sorted()`可以接收一个比较函数来实现自定义的排序

```python
#倒序排序
>>> def reversed_cmp(x,y):
...     if x<y:
...             return 1
...     elif x>y:
...             return -1
...     else:
...             return 0
... 
>>> sorted([1,2,32,44,5],reversed_cmp)
[44, 32, 5, 2, 1]
```
## 返回函数和闭包
高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。
这样把相关参数和变量都保存在返回的函数称为`闭包(Closure)`，这样的程序结构具有极大的威力。  
返回闭包的时候需要牢记的一点就是,返回函数不要使用任何循环变量，或者后续会发生变化的变量：

```python
#在闭包中使用循环变量会发生的情况
>>> def count():
...     fs = []
...     for i in range(1,4):
...             def f():
...                     return i*i
...             fs.append(f)
...     return fs
...             
>>> f1,f2,f3 = count()
>>> f1()
9
>>> f2()
9
>>> f3()
9
```
```python
#如果一定要引用循环变量，可以再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变。
#这样的缺点是代码较长，可以使用lambda函数缩短代码。
>>> def count():
...     fs = []
...     for i in range(1,4):
...             def f(j):
...                     def g():
...                             return j*j
...                     return g
...             fs.append(f(i))
...     return fs
... 
>>> f1,f2,f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```
## 匿名函数
`lambda`表示匿名函数，匿名函数的使用限制是只能有一个表达式，不用写`return`，返回值就是该表达式的结果。因为匿名函数没有名字，所以不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以被赋给一个变量，再利用该变量来调用该函数：

```python
#一个简单的匿名函数
>>> f = lambda x: x*x
>>> f(2)
4
>>> f
<function <lambda> at 0x10d2600c8>
```
```python
#可以把匿名函数作为返回值
>>> def count():
...     fs = []
...     for i in range(1,4):
...             def f(j):
...                     return lambda : j*j
...             fs.append(f(i))
...     return fs
... 
>>> f1,f2,f3 = count()
>>> f1
<function <lambda> at 0x10d260de8>
>>> f1()
1
>>> f2()
4
>>> f3()
9
```
## 装饰器
在代码运行期间动态增加功能的方式称为装饰器，可以用来在不修改函数定义的前提下增强函数功能。装饰器本质上就是一个返回函数的高阶函数。

```python
#一个简单的装饰器，给函数调用添加日志。
>>> def log(func):
...     @functools.wraps(func) #保证包装后的函数签名不变
...     def wrapper(*args,**kw):
...             print 'begin call %s()' %func.__name__
...             f = func(*args,**kw) #func在这里已经执行
...             print 'end call %s()' %func.__name__
...             return f #注意这里返回的f并不是一个函数，而是func(*args,**kw)的执行结果
...     return wrapper
... 
>>> @log
... def now():
...     print 'This is now'
... 
>>> now()
begin call now()
This is now
end call now()
```
## 偏函数
`functools`模块提供的一个有意思的功能是偏函数，它和数学上偏函数的定义不一样。`functools.partial`的作用是设置某个函数的默认值，返回一个新的函数，使其调用更加简单。

```python
>>> int2 = functools.partial(int,base = 2)
>>> int2('10')
2
>>> int2('100')
4
```
实际上，创建偏函数时接收的是`函数对象`、`*args`、`**kw`这三个参数。上面在传入

```python
int2 = functools.partial(int,base = 2)
```
的时候：

```python
int2('10')
#相当于
kw = {'base': 2}
int('10',**kw)
```
再看下一个例子：

```python
>>> max2 = functools.partial(max,10)
>>> max2(1,2,3,4)
10
```
在这个例子中，

```python
max2 = functools.partial(max,10)
```
实际上把`10`作为了`*args`的一部分自动添加到了左边，也就是说：

```python
max2(1,2,3,4)
#相当于
args = (10,1,2,3,4)
max(*args)
```
**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000