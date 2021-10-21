---
title: 多组SSH-Key公钥/私钥的配置
date: 2017-04-29 10:47:56
tags:
  - ssh
  - github
categories:
---

由于在同时使用`Github`和`Git@OSchina`（Github私有库需要收费且Git@OSchina在国内的访问速度较快），所以需要设置两组SSH-Key。

<!--More-->

## 本地生成公私钥
Step1. 本地生成ssh keys命令：`ssh-keygen -t rsa -C "注册邮箱"`，生成的公私秘钥会提示是否需要重命名，键入自定义名称（防止再次生成的秘钥覆盖之前的），可跳过密码设置。

```bash
# 生成github ssh keys
$ ssh-keygen -t rsa -C "githubEmail"
Generating public/private rsa key in pair...
Enter file in which to save the key ("默认位置"): ~/.ssh/github_rsa 
Enter passphrase ...
...

# 生成git@oschina ssh keys
$ ssh-keygen -t rsa -C "git@oschinaEmail"
Generating public/private rsa key in pair...
Enter file in which to save the key ("默认位置"): ~/.ssh/oschina_rsa 
Enter passphrase ...
...

```
Step2. 配置`config`将两组秘钥对应到相应的远程仓库。在.ssh/目录下新建`config`文件，其中`Host`是一个别名，命名可以随意，用来进行远程连接，当然使用真实的主机名称也是可以的。`HostName`和`IdentityFile`是各自主机名称以及对应的秘钥文件。

```bash
#github configuration
Host github.com
	HostName github.com
	IdentityFile ~/.ssh/github_rsa
	User githubEmail

#gitoschina configuration
Host git.oschina.net
	HostName git.oschina.net
	IdentityFile ~/.ssh/oschina_rsa
	User git@oschinaEmail
```

## 将公钥添加到账户
分别将生成的公钥添加到相应的Git账户

## 测试
测试Git连接，提示是否建立连接：yes。成功后会提示`Welcome...`

```bash
$ ssh -T git@github.com
$ ssh -T git@git.oschina.net
```
