---
title: Python模块
tags:
  - python
categories:
  - Python基础
---

## 包
可以使用包`package`来组织模块，每一个包目录下都有一个`__init__.py`的文件，这个文件是必须存在的，否则Python会将其视为普通目录而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为`__init__.py`本身就是一个模块，而它的模块名就是`package`。

<!--More-->

```python
__author__ = 'huizhang
#!/usr/bin/env python
# coding = utf-8

'This is the comment of the document. The first string of any python file is its comment.'

import sys

def BasicEx():
    args = sys.argv   #sys模块的agrv变量将命令行的所有参数储存在了一个list中，argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print 'Hello, word!'
    elif len(args) == 2:
        print 'Hello, %s!' %args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__': 
    BasicEx()
    #在使用命令行运行.py文件时，Python解释器将一个特殊变量__name__置为'__main___'，而如果在其他地方导入该模块，if判断将失效。因此这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
```
在上述代码中，第2、3行是标准注释，第2行使得`BasicEx.py`可以直接在Unix/Linux/Mac上运行，第3行注释表示文件本身使用的是标准UTF-8编码。在命令行运行该文件的效果：

```python
$ python BasicEx.py 
Hello, word!
$ python BasicEx.py Hui
Hello, Hui!
$ python BasicEx.py Hui haha
Too many arguments!
```
而在启动Python交互环境之后：

```python
>>> import BasicEx
>>> BasicEx.BasicEx()
Hello, word!
#在导入时没有打印而是在调用函数之后才能打印出'Hello, word!'
```
## 别名
导入模块时可以使用别名，这样可以在运行时根据当前环境选择最合适的模块。比如，Python标准库一般会提供`StringIO`和`cStringIO`两个库，这两个库的接口和功能是一样的，但是`cStringIO`是用C写的，速度更快，所以可以经常看到这样的写法：

```python
try:
	import cStringIO as StringIO
except ImportError: #导入失败会捕获到ImportError
	import StringIO
```
这样就可以优先导入`cStringIO`。如果有些平台不提供`cStringIO`，还可以降级使用`StringIO`。在导入`cStringIO`的时候，用`import...as...`指定了别名`StringIO`。因此后续代码引用`StringIO`即可正常工作。

Python是动态语言，函数签名一致就接口一样，因此无论导入哪个模块后续代码都能正常工作。

## 作用域
Python通过前缀`_`来区别变量类别

* 正常的函数和变量名是公开的，可以被直接引用。
* 类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上述`__name__`等，模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不使用这种变量名。
* 类似`_xxx`和`__xxx`这样的函数或者变量就是非公开的，仅仅在模块内部使用，而不应该被直接引用。

我们所说的private函数和变量“不应该”被直接引用，不是说“不能”，因为Python没有一种方法可以完全限制访问private的函数或变量，但是从编程习惯上来说不应该引用private函数或变量。

```python
def _private_1(name):
	return 'Hello, %s' %name
def _private_2(name):
	return 'Hi, %s' %name
	
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
```
我们在模块里公开`greeting()`函数，而把内部逻辑用private函数隐藏起来了，这样调用`greeting()`函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法。

即，外部不需要引用的函数全部定义为private，只有外部需要引用的函数才定义为public。
## HomeBrew
为了不影响系统自带的Python（怕啥时候给搞崩了），使用`Homebrew`安装新的Python以供学习和练习。

[Homebrew][Homebrew]是Mac下的一个包管理工具，它下载源码解压然后`./configure && make install`,同时包含相关依存库。它会`自动配置好各种环境变量`，并`易于卸载和更新`。

```python
$ brew install python
.
.
.
successfully installed
.
$ python
Python 2.7.12 (default, Dec  6 2016, 12:19:10) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
`Homebrew`安装的python路径是：

```
/usr/local/Frameworks/Python.framework/Versions/
```
备注一下`Homebrew`的常用命令：

```
brew list            # 列出本机通过brew安装的所有软件
brew search xxx      # 模糊搜索brew 支持的软件。如果不加软件名，就会列出所有它支持的软件。
brew install xxx     # 安装源码
brew info xxx        # 显示软件的各种信息，包括版本啊源码地址啊
brew uninstall xxx   # 卸载软件，很爽，一键静默卸载
brew update          # 更新 Homebrew 本身
brew outdated        # 看一下哪些软件可以升级
brew upgrade xxx     # 如果不是所有的都要升级，那就这样升级指定的软件
brew upgrade         # 如果都要升级，直接升级完所有可以更新的软件
brew cleanup         # 然后清理干净各种下载的缓存
```
## 安装使用第三方模块
Python安装第三方模块是通过setuptools这个工具完成的。Python有两个封装了setuptools的包管理工具：`easy_install`和`pip`。目前官方推荐使用`pip`。  

举例安装一个常用的用于图片处理的第三方库`PIL`(Python Imaging Library, 现改名为Pillow)

```python
$ pip install Pillow 
.
.
.
>>> from PIL import Image
>>> im = Image.open('./Desktop/test.jpg')
>>> print im.format, im.size, im.mode
JPEG (274, 274) RGB
```
### 模块搜索路径
当我们试图加载一个模块的时候，Python会在指定路径下搜索对应的.py文件。默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在`sys`模块的`path`变量中。可以查看当前的搜索路径：

```python
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/site-packages', '/Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg', '/Library/Python/2.7/site-packages']
```
如果我们要添加自己的搜索目录，有两种方法：

1. 直接修改`sys.path.append('/my_py_scripts')`
2. 设置环境变量`PYTHONPATH`,该环境变量的值会被自动添加到模块搜索路径中。

**感谢网上恩师[廖雪峰老师的Python教程][廖雪峰老师的教程]，本文大部分内容都摘自于此。**

[廖雪峰老师的教程]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
[Homebrew]: http://brew.sh/index_zh-cn.html