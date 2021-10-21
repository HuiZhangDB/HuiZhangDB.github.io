---
title: 给实验室配置共有资源
date: 2018-04-10 20:31:21
tags:
  - server
categories:
---

最近导师新购置了一台工作站，为了让大家可以共享一些文件和计算资源，我在这台工作站上配置了SSH和FTP服务。本文用以记录我的配置过程。

<!--More--> 

## 设置SSH服务器远程登录管理
```sh
# 1. 开启服务器上的SSH服务
# 1-1. 更新软件列表
sudo apt-get update
# 1-2. 更新本地软件
sudo apt-get upgrade
# 1-3. 安装ssh服务
sudo apt-get install openssh-server
# 1-4. 开启ssh服务
sudo /etc/init.d/ssh start

# 2. 添加公钥认证
# 在本地机器上生成公私钥对
ssh-keygen
# 复制公钥到远程服务器上
ssh-copy-id [-i your_id_rsa.pub] <username>@<server IP>
# 之后可以直接使用ssh [-i your_id_rsa] <username>@<server IP>登录
```

## 配置FTP文件共享服务
使用`vsftpd`来开启FTP服务器：

```sh
# 1. 下载并安装`vsftpd`
sudo apt-get install vsftpd

# 2. 创建可登陆用户账户及文件目录和权限
# 2-1. 在ubuntu中创建新用户happiftp和密码******
# 2-2. 将新用户的登录目录/home/happiftp作为FTP文件根目录
# 2-3. 在/home/happiftp下创建public文件夹给匿名用户使用
# 2-4. 设置登录根目录及实际可操作目录的权限[1]
sudo chmod 500 /home/happiftp
sudo chmod 500 /home/happiftp/public
sudo chmod 777 /home/happiftp/HappiLabFiles
sudo chmod 777 /home/happiftp/public/upload

# 3. 修改vsftpd配置文件
[...]
utf8_filesystem=YES

# 使用本地账户登录的设置
local_root=/home/happiftp/
local_enable=YES
write_enable=YES
local_umask=077
# 限制登录用户不能进入到上级目录
chroot_local_user=YES
#chroot_list_enable=YES
#chroot_list_file=/etc/vsftpd.chroot_list

# 匿名用户设置
anon_root=/home/happiftp/public/
anonymous_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_umask=022

# 重启vsftpd服务
sudo service vsftpd restart
```
> [1] 出于安全考虑，vsftpd不支持将具有完全权限的文件夹作为FTP登录的根目录。如果出现这种情况，FTP客户端将无法登录：  
> 500 OOPS: vsftpd: refusing to run with writable root inside chroot()  

<!--## 配置多个虚拟机账户-->

## 配置学校网络链接
这样设置完成后还只能从实验室内网登录这些服务，但我希望大家能连接校网就能使用，这样就需要设置一下实验室路由器了。

1. 给工作站主机保留ip地址，使其在实验室内网中的ip不会变化：局域网IP设置->地址保留->添加地址保留；
2. 需要开放端口映射或者设置DMZ主机，让校网用户可以访问实验室工作站。由于DMZ主机会开放主机的所有端口，现使用端口映射：端口映射/端口触发->添加FTP端口映射（内外部端口都设置为20-21）和SSH端口映射（内外部端口都设置为22）；
3. 这时校网用户可以通过路由器的222.xx.xx.xx（zjuvpn提供的ip）访问主机服务，但这个ip是学校动态分配的，一直会变。。同时，无法通过10.xx.xx.xx静态IP访问主机，推测是因为使用这个IP时候路由器的信号传入和传出走的是不同的路线使得不通，所以要设置静态路由来指定信号传输地址：静态路由->添加3条地址分别为10.0.0.0，210.xx.xx.0，222.xx.0.0（网关10.xx.xx.1）的静态路由表。

> 大概是计网知识已经还给老师了，自己各种搞不定路由设置，这里超感谢我的朋友@[Richard](https://blog.hlyue.com/)帮忙。

## 参考资料
[1] [端口映射和DMZ主机](http://blog.sina.com.cn/s/blog_816caa410101kvpx.html)