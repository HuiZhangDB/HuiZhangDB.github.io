---
title: 在博客中插入数学公式
date: 2017-05-02 15:09:59
tags:
  - tool
  - Math
categories:
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

Markdown本身并不支持数学公式的书写，使用[MathJax](https://www.mathjax.org/)来给我的博客插入公式只需要两步：  

1. 链接MathJax到要包含公式的网页中；  
2. 将公式放入网页让MathJax可以展示它。
  
[中文版入门指南](https://mathjax-chinese-doc.readthedocs.io/en/latest/start.html)
<!--More-->

## 到内容分发服务的安全链接

```javascript
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```
## 插入公式
行内公式使用`\\(...\\)`，两个`\`有一个是转义字符。

```
这是一个行内公式\\(c = a+b\\)
```
效果是：
这是一个行内公式\\(c = a+b\\)

行间公式使用`$$...$$`

```
这是一个行间公式
$$ E = mc^{2} $$
```

这是一个行间公式
$$ E = mc^{2} $$


## Hexo与Mathjax的转义冲突
按照以上两个步骤，按理来说应该就可以成功显示数学公式了。但是，有些时候会发现一些复杂的数学公式不能成功解析，原因是Hexo本身与Mathjax有一些特殊符号是互相冲突的：

* `_`的转义，在markdown中，`_`代表斜体，但在LaTeX中却是下标的意思；
* `\\`在markdown中会被定义为`\`，但在LaTeX中却代表换行；
* `*`在markdown中也是粗斜体的表示符号，在LaTeX中也被使用。

[Hexo下mathjax的转义问题](https://segmentfault.com/a/1190000007261752)提到了一些解决办法：

1. 手动转义：最直接，但通用型差，在其他markdown引擎中会解析失败；
2. 更换Hexo的markdown引擎：把Hexo默认的渲染markdown的引擎换掉，感觉有点过重了；
3. 修改Hexo渲染源码：修改Hexo的渲染源码，不改变文章内容，可迁移。

建议使用第3种办法，修改Hexo的渲染源码`nodes_modules/marked/lib/marked.js`:

S1. 去掉`\`的转义：
将文件中的

```js
escape: /^\\([\\`*{}\[\]()# +\-.!_>])/,
```
修改为

```js
escape: /^\\([`*{}\[\]()# +\-.!_>])/,
```
S2. 去掉特殊符号`_`：
找到斜体符号定义

```js
em: /^\b_((?:[^_]|__)+?)_\b|^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
```
去掉`_`的定义，修改为：

```js
em:/^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
```

修改完这两处后，LaTeX公式中的`_`和`\\`就不会解析错误啦。但值得注意的是`*`的问题没有被解决，不过`*`在LaTeX中使用并不多，markdown也同样需要一个表示粗斜体的符号，所以不在渲染文件中更改`*`的定义。这样就需要我们在写数学公式的时候注意`*`的使用了（例如，`\begin{align*}`应该改为`\begin{align}`）。

