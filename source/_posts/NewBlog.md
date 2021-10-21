---
title: Github Pages + Hexo
tags:
  - github
  - hexo
categories:
  - 博客
date: 2017-04-26 23:50:31
---

# 博客站点迁移

阿里云服务器快要到期不想再续，遂决定将博客迁移到免费的`GitHub Pages`上。

## 概述
`Github Pages`+`Hexo`(不使用`Jekyll`是因为没有找到好看的主题)  

1. 在GitHub上创建`GitHub Pages`
2. 配置本地`Hexo`环境，并与`GitHub Pages`绑定
3. 绑定域名

<!--More-->

## 创建Github Pages
直接在`GitHub`网站上创建一个仓库，仓库名必须为`myusername.github.io`。
{% asset_img 1493223050689.png %}

## 安装并配置Hexo
Step1. 根据[Hexo中文文档](https://hexo.io/zh-cn/docs/)中的提示进行安装：  

```
#先安装依赖库Node.js（假定已经安装好了Git）
$ brew install Node.js
#下载安装Hexo
$ npm install -g hexo-cli
```

Step2. 开始在本地建站

```
$ hexo init <Blogfolder>
$ cd <Blogfolder>
$ npm install
```

Step3. 在博客文件根目录下打开终端，启动本地服务器查看建站是否成功。成功后可以在`localhost:4000`浏览博客Hello World。

```
$ hexo s
```
{% asset_img 1493223087552.png %}

Step4. 根据[Hexo配置文档](https://hexo.io/docs/deployment.html)部署网站到`github pages`  
a. 修改站点配置文件`_config.yml`(Blogfolder/_config.yml)中的Deployment模块，把其中repo字段的值替换成自己github pages提交代码的git地址。(如果使用ssh，将`repo`改为相应ssh地址)

```
deploy:
  type: git
  repo: https://github.com/HuiZhangDB/HuiZhangDB.github.io.git
  branch: master
```

b.安装Hexo的Git部署插件[hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git)

```
$ npm install hexo-deployer-git --save
```

c. 现在可以把它发布到GitHub Pages上啦！

```
$ hexo clean  #清除缓存，在更改主题等后要使用
$ hexo g      #生成静态文件
$ hexo d      #部署网站
```

d. 在浏览器输入`http://myusername.github.io`可以看到自己的博客啦~

Step.5 自定义Hexo主题  
[Hexo模板](https://hexo.io/themes/)中有许多好看的模板可以选择，我选择了简洁好看的[even](https://github.com/ahonn/hexo-theme-even)主题。它的[主题文档](https://github.com/ahonn/hexo-theme-even/wiki)很详细地写了设置步骤，这里不再赘述。

> 如果以后要更新Hexo版本，只需要在博客根目录下运行 `npm update`

## 绑定域名

1. 购买域名
2. 选择一个DNS解析服务器
3. 域名解析到`myusrname.github.io`，以及Github Pages提供的IP:   
```
192.30.252.153
192.30.252.154
```
4. 在本地站点的`source`文件夹中创建`CNAME`文件，填写域名（不加http://）
5. 将本地站点部署更新到Github Pages
6. 等待DNS解析生效
7. 可以在浏览器输入自己的域名查看博客啦！

## 可以开始写文章啦！
为了方便管理文章中的图片等资源，可以开启[Hexo的资源文件管理功能](https://hexo.io/zh-cn/docs/asset-folders.html)

```
#将站点配置文件_config.yml中的post_asset_folder选项设为true来打开
post_asset_folder: true
```
接下来就可以开始自由写作啦~

```
$ hexo new (post) title
...writing
$ hexo clean
$ hexo d -g
```
为了方便文章管理，Hexo提供了可视化写作插件[hey](https://github.com/nihgwu/hexo-hey)，优点是可以拖拽图片，缺点是不方便随时写作。  

## 第三方服务设置
### 添加统计分析
主题[even](https://github.com/ahonn/hexo-theme-even)提供了对于百度统计和Google统计的支持，只需要修改主题配置文件中的`baidu_analytics`或`google_analytics`字段，填写`analytics id`就可以开启统计。

例如开启百度统计：  
step1. 在百度统计网站注册账号  
step2. 添加自有网站  
step3. 获取统计代码，得到其中的`baidu analytics id`

```javascript
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?this_code_is_the_baidu_analysis_id";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>

```
step4. 将`baidu analytics id`填入主题配置文件的`baidu_analytics`字段。
step5. 百度统计网站上检查代码成功，过一会就可以查看分析报告啦！

<!--### 添加评论服务
主题[even](https://github.com/ahonn/hexo-theme-even)提供了对于多说、Disqus和网易云跟帖的支持，由于多说即将关闭，本博客选择使用网易云跟帖。

1. 在[网易云跟帖](https://gentie.163.com/)注册账号，进入后台管理，设置站点信息，获取代码；
2. 修改主题配置文件中的`netease_key`字段，开启网易云跟帖；
3. 对于不开启评论的页面，文件头添加`comments`字段，设置为`false`。

网站部署更新后可以看到评论啦。-->

## 致谢
HuisBlog博客搭建过程主要参考[水瓶座iOSer的简书](http://www.jianshu.com/p/834d7cc0668d)，在此提出感谢。





