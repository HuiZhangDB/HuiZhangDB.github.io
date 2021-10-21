---
title: Python GUI
date: 2017-09-27 14:39:06
tags:
  - PyGUI
categories:
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

最近的实验需要做一个桌面小程序来收集实验信息，决定选用跨平台的`Python`来写。  
在`Python图形界面编程`中常用的工具包有：

<!--More-->

* [PyQt](https://www.riverbankcomputing.com/software/pyqt) (Python和Qt库的成功融合)
* [wxPython](https://www.wxpython.org/) (wxWidgets的Python封装)
* [Tkinter](https://wiki.python.org/moin/TkInter/) (Python的标准GUI工具包)

这次使用的是`PyQt`（相关文档和资料比较多）。

## PyQt 
使用Qt开发程序可以从`Qt Widgets`或/和`Qt Quick`开始（[Qt Widgets、QML、Qt Quick的区别](http://blog.csdn.net/liang19890820/article/details/54141552)）。我们对实验工具的界面要求不高，可以直接使用`Qt Widgets`开发。它有几个重要的概念：

C1. UI 界面实现

> QApplication
>> QWidget

C2. 组件通信

> Signal & Slot （信号槽机制）

## 使用 PyInstaller 打包可执行程序
### 注意在打包后系统路径会发生变化
平时几种常用的获取当前运行脚本路径的方法：

```python
print(__file__)
print(os.path.realpath(__file__))
print('using sys.executable:', repr(os.path.dirname(os.path.realpath(sys.executable))))
print('using sys.argv[0]:', repr(os.path.dirname(os.path.realpath(sys.argv[0]))))
print(os.path.split(sys.argv[0]))
print(sys.path[0])
```
在工程中的运行结果：

```python
/Users/huizhang/Desktop/testpath/path.py
/Users/huizhang/Desktop/testpath/path.py
using sys.executable: '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/bin'
using sys.argv[0]: '/Users/huizhang/Desktop/testpath'
('/Users/huizhang/Desktop/testpath', 'path.py')
/Users/huizhang/Desktop/testpath
```

打包后的运行结果：

```sh
path.py
/Users/huizhang/path.py
using sys.executable: '/Users/huizhang/Desktop/testpath/dist/path.app/Contents/MacOS'
using sys.argv[0]: '/Users/huizhang/Desktop/testpath/dist/path.app/Contents/MacOS'
('/Users/huizhang/Desktop/testpath/dist/path.app/Contents/MacOS', 'path')
/Users/huizhang/Desktop/testpath/dist/path.app/Contents/MacOS/base_library.zip
```

### 打包数据文件
`pyinstaller`命令不能直接将工程中的数据文件一起打包，要实现这一步必须修改`.spec`文件。[legendtkl的博客](http://legendtkl.com/2015/11/06/pyinstaller/)中有`PyInstaller`的简介中文教程，也可以直接查看[官方文档](https://pythonhosted.org/PyInstaller/spec-files.html)。

添加数据文件只需要在`a.datas`里面添加二元组即可，二元组第一个参数`'/mygame/data'`是要添加的数据文件的本地索引，第二个参数`'data'`是在打包后的工程中的位置。

```
added_files = [
         ( '/mygame/data', 'data' ),
         ( '/mygame/sfx/*.mp3', 'sfx' ),
         ( 'src/README.txt', '.' )
         ]
         
    a = Analysis(...
         datas = added_files,
         ...
         )
```
`PyInstaller`会把打包的位置存在`sys._MEIPASS`，可以测试一下：

```python
img = os.path.join("res","img","test.jpg")

base_path0 = os.path.abspath(".")
base_path1 = os.path.dirname(os.path.realpath(sys.argv[0]))
try:
    base_path2 = sys._MEIPASS
except Exception:
    # PyInstaller打包前sys._MEIPASS不存在
    base_path2 = os.path.abspath(".")

print("img0: ",os.path.join(base_path0,img))
print("img1: ",os.path.join(base_path1,img))
print("img2: ",os.path.join(base_path2,img))
```
工程中的运行结果都一样：

```python
# 路径都正确
img0:  /Users/huizhang/Desktop/testinstaller/res/img/test.jpg 
img1:  /Users/huizhang/Desktop/testinstaller/res/img/test.jpg
img2:  /Users/huizhang/Desktop/testinstaller/res/img/test.jpg
```
打包后：

```python
# img0错误，img1和img2正确
img0:  /Users/huizhang/res/img/test.jpg 
img1:  /Users/huizhang/Desktop/testinstaller/dist/test.app/Contents/MacOS/res/img/test.jpg
img2:  /Users/huizhang/Desktop/testinstaller/dist/test.app/Contents/MacOS/res/img/test.jpg
```
### 开始打包

```sh
cd my_project_dir
# -w 参数指定打包为一个文件(.app)，-n 设置应用名，-i 设置应用图标。
pyi-makespec -w -n MyAppName -i appicon.icns MyMainScript.py
# 修改.spec文件中的 datas 以添加数据文件
pyinstaller MyAppName.spec
# 生成 built 文件夹和 dist 文件夹，打包好的文件在 dist 中。
```


## 附：使用PyQt过程中遇到的问题
### QSound不能播放音乐

```python
QSoundEffect(qaudio): Error decoding source  
```

QSound只能播放`.wav`

### QMediaPlayer没有声音

```python
no error but no sound
```
QUrl.fromLocalFile只能使用绝对路径

### QMediaPlayer.duration数据错误

```python
QMediaPlayer.duration() == 0
```
`QMediaPlayer.setMedia()`是异步执行的，如果在这个方法后马上调用`QMediaPlayer.duration()`得到的将是错误的值，因为`QMediaPlayer.setMedia()`还未设置好。应该在`durationchanged`信号发出后重新给其赋值。

### QMediaPlaylist循环播放
设置只播一首歌时`setPlaybackMode(CurrentItemOnce)`，每次本首歌曲播完index会被重置为`-1`。