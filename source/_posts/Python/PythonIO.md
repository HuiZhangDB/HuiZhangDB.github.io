---
title: PythonIO编程
tags:
  - python
categories:
  - Python基础
date: 2016-12-26 23:50:33
---

IO编程有两种模式，一种是`同步IO`，一种是`异步IO`。使用异步IO编写程序的性能会远远高于同步IO，但异步IO的缺点是编程模型复杂度远远高于同步IO。这里先讨论同步模式，异步IO复杂度太高，后续涉及到服务器端程序开发时再讨论。

<!--More-->

## 文件读写
操作文件的好习惯是使用`with`语句
### file-like Object
有`read()`方法的对象在Python中统称为file-like Object。除了文件外，还可以是内存的字节流、网络流、自定义流等。

### 字符编码
为了避免手动转码，可以使用`codecs`模块。

```python
>>> txt = u'测试'
>>> txt
u'\u6d4b\u8bd5'
>>> with codecs.open('testw.txt','w','utf-8') as f:
...     f.write(txt)
... 
>>> f
<closed file 'testw.txt', mode 'wb' at 0x10b35aae0>
>>> with codecs.open('testw.txt','r','utf-8') as f:
...     f.read()
... 
u'\u6d4b\u8bd5'
>>> u = u'\u6d4b\u8bd5'
>>> print u
测试
```
## 操作文件和目录
使用`os`,`os.path`以及`shutil`模块来操作文件和目录。  
示例代码{% asset_link search.py search.py %}

## 序列化
将变量从内存中变成可存储或传输的过程称之为序列化(picking)，序列化之后的内容就可以写入磁盘或者通过网络传输到其它机器上。反之将变量内容从序列化的对象重新读到内存里称之为反序列化(unpicking)。

### pickle和Cpickle
只能用于Python，且不同版本彼此不兼容，只能用于保存不重要的数据。

### Json
```python
dumps(obj,default)   #object->json
loads(json_str,object_hook)   #json->object
```

**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000