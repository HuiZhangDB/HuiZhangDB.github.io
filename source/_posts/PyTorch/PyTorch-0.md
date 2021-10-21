---
title: 安装PyTorch
date: 2018-04-12 19:37:00
tags:
  - DL
categories:
  - PyTorch
---

本文记录一下给服务器安装PyTorch的过程。

<!--More-->

## 准备工作
### 安装包管理器Anaconda

1. 下载[Anaconda for python3.6](https://docs.anaconda.com/anaconda/install/linux)
2. 上传到服务器`scp Anaconda3-5.1.0-Linux-x86_64.sh user@server:~/share`
3. 安装`bash ~/share/Anaconda3-5.1.0-Linux-x86_64.sh`
4. 激活`source ~/.bashrc`
5. 更新到最新版`conda update -n base conda`

> Anaconda 会自动修改环境变量，用户下的python(及pip)将会被切换为python3.6，但不会影响系统使用的python版本：  
> 可以使用 sudo su 切换到root再使用 python(python3) --version 查看
 
### 更新pip和numpy到最新版本
```sh
# 更新pip3和numpy
conda update pip
conda update numpy
```

### 安装GPU加速工具包
选择正确版本的[CUDA TOOLKIT](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)和[目标主机设置](https://developer.nvidia.com/cuda-downloads)，下载cuda-repo-xx.deb

```sh
# 安装前设置主机环境
sudo apt-get install linux-headers-$(uname -r)

# 安装合适版本
sudo dpkg -i cuda-repo-ubuntu1604_9.1.85-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub`
sudo apt-get update
sudo apt-get install cuda

# 安装后设置
# 1. 添加环境变量（写入~/.bashrc）
export PATH=/usr/local/cuda-9.1/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
# 此时可以查看安装的cuda版本了
nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2017 NVIDIA Corporation
Built on Fri_Nov__3_21:07:56_CDT_2017
Cuda compilation tools, release 9.1, V9.1.85

# 2.* 如果是POWER9系统，需要设置以支持cuda9的新特性
# 创建 /usr/lib/systemd/system/nvidia-persistenced.service 并使生效
sudo systemctl enable nvidia-persistenced
# 删除一条LINUX的默认udev rule
注释掉/lib/udev/rules.d/40-vm-hotadd.rules的其中一行：
# SUBSYSTEM=="memory", ACTION=="add", DEVPATH=="/devices/system/memory/memory[0-9]*", TEST=="state", ATTR{state}="online"

# 重启主机以生效
```

> nvidia-persistenced.service 文件内容：

```
[Unit]
Description=NVIDIA Persistence Daemon
Wants=syslog.target

[Service]
Type=forking
PIDFile=/var/run/nvidia-persistenced/nvidia-persistenced.pid
Restart=always
ExecStart=/usr/bin/nvidia-persistenced --verbose
ExecStopPost=/bin/rm -rf /var/run/nvidia-persistenced

[Install]
WantedBy=multi-user.target
```

## 开始安装PyTorch
本来想使用Anaconda安装的，但它的镜像连接不上，改用PIP安装。

```sh
pip install http://download.pytorch.org/whl/cu91/torch-0.3.1-cp36-cp36m-linux_x86_64.whl 
pip install torchvision
```
> 如果由于网络原因安装失败可以先下载下来再 pip install ~/TorchFileLocalPath

安装成功：

```sh
>>> python
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import torchvision
>>> 

```

### 使用Pycharm进行远程开发与调试
强大的`Pycharm Pro`IDE可以直接在服务器上开发、调试，就不用再给本地搭建和服务器上一样的环境了。在Tools->Deployment里面可以设置自动部署（或者在创建项目时选用远程服务器和解释器）。

需要设置的有`SFTP`和`Remote Interpreter`。SFTP用于代码同步，类似git上传，同步后可以在服务器上直接运行上传的代码。

1. 在Tools->Deployment中添加SFTP服务：`Connect`页填写服务器连接选项，`Mapping`页设置本地路径和远程路径（注意这个路径是相对于前面的Root Path的）的映射；
2. 选择自动上传(Automatic Uploaded)；
3. Preference->Project Interpreter中添加远程解释器，可以使用已添加的SFTP中的服务器设置（使用Deployment Configure选项）

> 遇到了问题，Python Console不可用，远程连接控制台不成功：  
> ssh://usr@10.xx.xx.xx:22/home/usr/anaconda3/bin/python -u /home/usr/.pycharm_helpers/pydev/pydevconsole.py 0 0  
> Couldn't connect to console process.   
> Process finished with exit code -1    
> 这是[Pycharm的一个未解决BUG](https://youtrack.jetbrains.com/issue/PY-18029#tab=Comments)，但评论中提到的解决方法[allowing the server public IP for all traffic](https://stackoverflow.com/questions/31323363/pycharm-4-5-3-remote-console-cannot-connect-to-remote-process/31323892)对我的情况没用。无法解决，暂搁置。

Python Console 问题后续:

* 查看pycharm的log无有用提示（`~/Library/Logs/PyCharm2018.1/idea.log`）；
* 使用`nettop`监控pycharm进程通信发现有一个通信一直被关闭，以为是进程通信的问题：{% asset_img pycharm_tcp_closed.jpeg %}  
* 给macos开发端口：修改`\etc\pf.conf`配置文件，但还是没有解决问题。

```sh
sudo vim /etc/pf.conf

# 添加规则允许本机IP访问任何端口
pass in proto tcp from 127.0.0.1
pass in proto tcp from localhost

# 使配置生效
sudo pfctl -evf /etc/pf.conf
```

### 使用Jupyter Notebook
`Jupyter`是一个基于 websocket 的 Python 交互式编程环境。由于之前在 Pycharm 配置的远程解释器无法运行Python Console，所以使用 Jupyter Notebook 以方便进行实验。（Jupyter虽然不适合作为生产环境，但作为实验环境来说非常好用。）

在服务器上安装Jupyter Notebook：

```sh
server$ pip install jupyter
```

开启服务：

```sh
server$ jupyter notebook --no-browser --port=8080  
#no-browser since that is not available through an SSH session
```
> 可以保存配置以简化启动命令：jupyter notebook --generate-config；  
> 然后在~/.jupyter/jupyter_notebook_config.py中添加：  
> c.NotebookApp.password = 'sha1:a86...使用notebook.auth.passwd()生成的密文'  
c.NotebookApp.open_browser = False  
c.NotebookApp.port =8080  

通过 SSH 进行远程访问：

```sh
ssh -N -L 8080:localhost:8080 <remote_user>@<remote_host>
# Add the option -N to tell SSH that I'm not going to execute any remote commands. This ensures that the connection cannot be used in that way, see this as an added security measure.
# Add the -L option that tells SSH to open up a tunnel from port 8080 on the remote machine to port 8080 in my local machine.
```

现在本地可以通过`http://localhost:8080/`使用 Jupyter Notebook 啦~

## 参考资料
[1] [pycharm 远程服务器开发调试](https://www.jianshu.com/p/988cd2137139)  
[2] [Pycharm远程调试使用服务器资源](http://paranoth.me/2018/03/19/Pycharm%E8%BF%9C%E7%A8%8B%E8%B0%83%E8%AF%95%E4%BD%BF%E7%94%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%B5%84%E6%BA%90/)  
[3] [OSX上pf的简单配置笔记](https://blog.chionlab.moe/2016/02/01/use-pf-on-osx/)