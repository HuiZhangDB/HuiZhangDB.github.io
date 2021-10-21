---
title: 记录一些常用的Linux命令
date: 2018-04-12 19:42:17
tags:
  - linux
  - cmd
categories:
---
本文用于记录一些常用的Linux命令以备忘。

<!--More-->

## SSH服务相关
```sh
who # 查看当前登录的用户
who /var/log/wtmp # 查看自从wtmp文件创建以来的每一次登陆情况 
$HOME/.bash_history # 查看每个用户的历史命令
history #  当前用户的历史命令
top # 查看资源管理器
pkill -kill -t pts/1 # 强制断开某个连接(pts/1)

# 本地终端关闭后的程序运行
# 创建新的窗口
screen -S <sessionName>
# 分离当前会话
Ctrl-a d
# 查看会话
screen -ls
# 恢复会话
screen -r <sessionName>
```
### SSH SOCKS Proxy
```sh
# Firstly, run OpenSSH's SOCKS proxy
# If you can make an SSH connection from noinet to hasinet
noinet$ ssh -D 1080 hasinet
# If you can only make SSH connections to noinet from hasinet
hasinet$ ssh -D 1080 localhost -t ssh -R 1080:localhost:1080 noinet

# Then use the SOCKS proxy by proxychains
# download, upload and install proxychains to noinet
sudo dpkg -i ./libproxychains3_3.1-7_amd64.deb
sudo dpkg -i ./proxychains_3.1-7_all.deb

# Test connection
proxychains wget www.baidu.com

# apt through socks
sudo proxychains apt-get update
```

## 环境变量
```sh
# 系统环境变量文件
/etc/profile —— 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置；
/etc/environment —— 在登录时操作系统使用的第二个文件,系统在读取你自己的profile前,设置环境文件的环境变量；
/etc/bashrc —— 为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取；
# 用户环境变量文件
~/.profile —— 每个用户都可使用该文件输入专用于自己使用的shell信息，当用户登录时，该文件仅仅执行一次！默认情况下,它设置一些环境变量,执行用户的.bashrc文件；
~/.bashrc —— 该文件包含专用于你的bash shell的bash信息,当登录时以及每次打开新的shell时,该文件被读取；
```

## 防火墙
Linux高层使用`ufw`的防火墙为添加或删除简单规则提供了简易的方法，默认情况下，ufw处于禁用状态。几条`ufw`的常用命令：

```sh
# 查看防火墙状态
sudo ufw status
# 开启防火墙，并在系统启动时自动开启。
sudo ufw enable
# 关闭所有外部对本机的访问，但本机访问外部正常。
sudo ufw default deny
# 关闭防火墙
sudo ufw disable
# 开启/禁用
sudo ufw allow|deny [service]
```

低层用`iptables`实现访问控制：

```sh
# 查看iptables已有规则
sudo iptables -L -n -v
# 开放端口
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# 允许IP访问
sudo iptables -A INPUT -s 10.xx.xx.xx -dport 80 -j ACCEPT 
```

## 网络分析
`tcpdump`是基于Unix系统的命令行式的数据包嗅探工具，可以抓取流动在网卡上的数据包。

```sh
# 抓取主机10.37.63.255和主机10.37.63.61或10.37.63.95的通信
tcpdump host 10.37.63.255 and \(10.37.63.61 or 10.37.63.95 \)
```

`nethogs`是一款小巧的"net top"工具，可以显示每个进程所使用的带宽，并对列表排序，将耗用带宽最多的进程排在最上面。万一出现带宽使用突然激增的情况，用户迅速打开nethogs，就可以找到导致带宽使用激增的进程。nethogs可以报告程序的进程编号（PID）、用户和路径。

## 文件管理

```sh
# 查看当前文件夹下的文件数量
ls -l| grep "^-"| wc -l
# 查看当前路径下子文件夹中的问价数量
find . -maxdepth 1 -type d | while read dir; do count=$(find "$dir" -type f | wc -l); echo "$dir : $count"; done

```

## 文本编辑
### vim

```sh
# 跳转
0: 跳转到行首。
$: 跳转到行尾
```

## 包管理
### Anoconda

```sh
# 当前版本
conda -V
# 已安装的包
conda list
# 当前有的虚拟环境
conda env list or conda info -e 
# 检查更新当前conda
conda update conda 
# 创建python虚拟环境
conda create -n your_env_name python=X.X(2.7/3.6)
# 激活/关闭虚拟环境
conda activate your_env_name
conda deactivate
```

## 磁盘管理
Linux磁盘管理常用三个命令为`df`、`du`和`fdisk`：

* df：列出文件系统的整体磁盘使用量
* du：检查磁盘空间使用量
* fdisk：用于磁盘分区

例如查看指定文件夹内的文件占有空间：

```sh
du -h --max-depth=1 your_dir
```

> [Linux 磁盘操作的基本概念和命令](http://ohmystack.com/articles/LVM-basic)  
> [linux下挂载硬盘并合并到系统盘](https://www.jianshu.com/p/e6a53b53d585)  
> [linux 安装新硬盘](http://wiki.ubuntu.org.cn/%E5%AE%89%E8%A3%85%E6%96%B0%E7%A1%AC%E7%9B%98)


由于实验室工作站系统磁盘容量满了，因此要将空闲磁盘挂载上来：

```sh
# 查看磁盘及分区状况，选定空闲磁盘
fdisk -l
# 首先给空闲磁盘分区：
fdisk /dev/sdc
# 接下来格式化分区，sdc1 是我们刚刚新建的分区
mkfs.ext4 /dev/sdc1
```
使用交互命令进行操作（如有旧分区想删除可以键入命令 'd'）：  
{% asset_img new_partition.png %}

本来想使用LVM直接给系统盘扩容，但好像不行。。

```sh
# 安装LVM工具
sudo apt-get install lvm2
# 但是 vgdisplay 无显示，说明不可用LVM扩容... 
```
那直接挂载到文件夹用算了：

```sh
# 设定挂载点
sudo mkdir ~/disk1
# 挂载上来
sudo mount /dev/sdc1 ~/disk1
# 设置开机自动挂载
# 查看sdc1的UUID
sudo blkid
# 将信息添加到启动文件中
echo "UUID=xxx /home/data ext4 defaults,errors=remount-ro 0 1" >> /etc/fstab
# 此时挂载了新磁盘的文件夹权限属于root，把其访问权限改为777，便于文件的读写和执行
sudo chmod -R 777 /home/data
# 重启
```

### /boot 空间不足
由于linux内核一直在更新，更新后，旧的内核就不在使用，但旧的内核文件还在boot里面，占据着空间，更新几次过后boot分区就会被占满，显示boot磁盘空间不足。可以将不用的内核文件删除，释放空间。

```sh
# 首先查看已安装的内核
dpkg --get-selections |grep linux-image
# 查看自己当前启动的是哪个内核
uname -a
# 对于显示 install 的旧内核，删除多余的内核版本
sudo apt purge linux-image-xxx-generic
# 显示 deinstall 说明：系统没有安装此内核，但是在配置文件中还残留它的信息（有可能是以前卸载的时候不彻底）
sudo dpkg -P linux-image-xxx-generic
```
有可能在执行卸载命令（sudo apt purge linux-image-xxx-generic）时报错:
> ...You might want to run 'apt-get -f install' to correct these.

这是说有的软件包缺少依赖关系，建议我们修复执行。那么执行`sudo apt -f install`来修复，但又有问题：
> gzip: stdout: No space left on device
 
原因是这样：在修复的时候需要下载依赖包，然而在/boot下本来就没有多余的空间了，所以无法修复依赖的问题。解决办法就是先把boot空间下几个比较大的文件暂存到别的文件夹，腾出来足够的空间来修复依赖，等依赖修复好了并且删除了旧的内核后再迁移回来（如果文件没什么用处就不用迁移回来了）。我删除了几个不用的内核文件`initrd.img-4.4.0-128-generic`以腾出空间。

然后使用`sudo apt -f install`修复成功。

再接着`sudo apt purge linux-image-xxx`删除没用的旧内核即可。

## 参考材料
[1] [Ubuntu 16.04 防火墙](https://help.ubuntu.com/lts/serverguide/firewall.html)   
[2] [使用 nethogs 查看每个进程流量 ](http://einverne.github.io/post/2017/07/use-nethogs-to-check-network-traffic-per-process.html)  
[3] [/boot空间不足的解决办法](https://blog.csdn.net/qq_27818541/article/details/72675954)