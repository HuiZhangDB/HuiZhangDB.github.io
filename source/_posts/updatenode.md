---
title: Node更新到8.0+导致的一些问题
date: 2017-10-31 13:19:00
tags:
categories:
  - 博客
---

最近更新了`Node.js`，结果在使用`hexo new post`的时候开始报错：
<!--More-->

### 报错一 dyld
```
dyld: Library not loaded: /usr/local/opt/icu4c/lib/libicui18n.58.dylib
  Referenced from: /usr/local/bin/node
  Reason: image not found
Abort trap: 6
```
重新安装`node`：

```
brew reinstall node --without-icu4c
```
成功解决！

### 报错二 DTraceProviderBindings.node
```
Error: The module '/usr/local/lib/node_modules/hexo-cli/node_modules/dtrace-provider/build/Release/DTraceProviderBindings.node'
was compiled against a different Node.js version using
NODE_MODULE_VERSION 51. This version of Node.js requires
NODE_MODULE_VERSION 57. Please try re-compiling or re-installing
the module (for instance, using `npm rebuild` or `npm install`).
    at Object.Module._extensions..node (module.js:641:18)
    at Module.load (module.js:531:32)
    at tryModuleLoad (module.js:494:12)
    at Function.Module._load (module.js:486:3)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/dtrace-provider/dtrace-provider.js:17:23)
    at Module._compile (module.js:612:30)
    at Object.Module._extensions..js (module.js:623:10)
    at Module.load (module.js:531:32)
    at tryModuleLoad (module.js:494:12)
    at Function.Module._load (module.js:486:3)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/bunyan/lib/bunyan.js:79:18)
    at Module._compile (module.js:612:30)
{ Error: Cannot find module './build/default/DTraceProviderBindings'
    at Function.Module._resolveFilename (module.js:513:15)
    at Function.Module._load (module.js:463:25)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/dtrace-provider/dtrace-provider.js:17:23)
    at Module._compile (module.js:612:30)
    at Object.Module._extensions..js (module.js:623:10)
    at Module.load (module.js:531:32)
    at tryModuleLoad (module.js:494:12)
    at Function.Module._load (module.js:486:3)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/bunyan/lib/bunyan.js:79:18)
    at Module._compile (module.js:612:30)
    at Object.Module._extensions..js (module.js:623:10)
    at Module.load (module.js:531:32) code: 'MODULE_NOT_FOUND' }
{ Error: Cannot find module './build/Debug/DTraceProviderBindings'
    at Function.Module._resolveFilename (module.js:513:15)
    at Function.Module._load (module.js:463:25)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/dtrace-provider/dtrace-provider.js:17:23)
    at Module._compile (module.js:612:30)
    at Object.Module._extensions..js (module.js:623:10)
    at Module.load (module.js:531:32)
    at tryModuleLoad (module.js:494:12)
    at Function.Module._load (module.js:486:3)
    at Module.require (module.js:556:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/usr/local/lib/node_modules/hexo-cli/node_modules/bunyan/lib/bunyan.js:79:18)
    at Module._compile (module.js:612:30)
    at Object.Module._extensions..js (module.js:623:10)
    at Module.load (module.js:531:32) code: 'MODULE_NOT_FOUND' }
```
`DTraceProviderBindings`针对的`node`版本错误，刚开始以为是`node_module`没有更新，因此重新安装：

```
$ rm -rf node_modules
$ npm install
$ hexo clean
```
没有解决，继续报错。。尝试重新安装`hexo命令行工具`：

```
npm install -g hexo-cli
```
成功解决！

### 报错三 DeprecationWarning
```
(node:14238) [DEP0061] DeprecationWarning: fs.SyncWriteStream is deprecated.
```

`DeprecationWarning`函数已经弃用，使用`--debug`参数调试：

```
$ hexo version --debug  
DEBUG Plugin loaded: hexo-deployer-git                                     
[DEP0061] DeprecationWarning: fs.SyncWriteStream is deprecated.
```

发现是`hexo-deployer-git`的问题，更新这个模块：

```
$ npm update hexo-deployer-git
```

没有成功，删除包再重新安装：

```
$ npm uninstall hexo-deployer-git
$ npm install hexo-deployer-git --save
```

成功解决！