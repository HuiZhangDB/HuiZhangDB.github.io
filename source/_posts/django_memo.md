---
title: Django 网站开发初始化与自动部署流程备忘
date: 2018-03-24 12:15:09
tags:
  - python
  - web
categories:
---

本文用以记录基于 Python + Django 开发网站时，初始化项目流程以及自动部署流程。
> Python + Django + Nginx + Gunicorn

<!--More-->

## 网站初始化创建
### 创建 Virtualenv

```sh
# 创建网站使用的Python环境
cd path/to/directory/<../web_root>
python -m venv virtualenv
# 激活虚拟环境
source virtualenv/bin/activate
```

在 Virtualenv 下安装Django, Gunicorn：

```sh
pip install django, gunicorn
```
### 新建 Django Project 并上传到 Git 库

```sh
django-admin.py startproject NewProjectName

# 上传到Git
cd  NewProjectName
git init
touch README.md
git remote add [shortname(origin)] [url]
git add .
git commit -m 'comments' 
git push -u origin master
```
> 新建应用命令：python manage.py startapp appName

## 服务器初始化环境和自动部署
### 服务器 Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

```sh
server$ sudo add-apt-repository ppa:deadsnakes/ppa
server$ sudo apt update
server$ sudo apt install nginx git python36 python3.6-venv

server$ sudo systemctl start nginx
```

### 初始化部署（利用 fabric 实现自动化）
S1. 本地编写自动部署脚本并执行：

```sh
cd NewProjectName
pip install fabric3

mkdir deploy_tools
cd deploy_tools

touch fabfile.py
# 编写fabfile.py文件里的自动部署函数deploy()

touch nginx.template.conf
# Nginx config for virtual host

touch gunicorn-systemd.template.service
# Systemd job for Gunicorn

# 执行自动部署脚本
fab <function_name(deploy)>:host=SERVER_ADDRESS
```
> 自动部署脚本一般要实现：  
> 1. 从 Git 库 pull 最新的源代码  
> 2. 创建或更新虚拟环境  
> 3. 创建或更新环境变量  
> 4. 更新静态文件  
> 5. 更新数据库

S2. 在服务器上修改 Nginx 和 Gunicorn 的配置文件：

```sh
# 修改nginx配置文件
server$ cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/<hostname>/g" \
    | sudo tee /etc/nginx/sites-available/<hostname>

# 激活nginx配置    
server$ sudo ln -s /etc/nginx/sites-available/<hostname> \
    /etc/nginx/sites-enabled/<hostname>

# 修改gunicorn配置文件
server$ cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/<hostname>/g" \
    | sudo tee /etc/systemd/system/gunicorn-<hostname>.service
```
> 备忘一下 Nginx 和 Gunicorn 的常用配置文件：

```
# nginx.template.conf
server {
    listen 80;
    server_name DOMAIN/IP;

    location /static {
        alias /path/to/project/root/static;
    }

    location / {
        proxy_pass http://unix:/tmp/DOMAIN/IP.socket;
        proxy_set_header Host $host;
    }
}

# gunicorn-systemd.template.service
[Unit]
Description=Gunicorn server for DOMAIN/IP

[Service]
Restart=on-failure
User=yourusername
WorkingDirectory=/path/to/project/root/
EnvironmentFile=/path/to/project/root/.env

ExecStart=/path/to/gunicorn/bin/gunicorn \
    --bind unix:/tmp/DOMAIN/IP.socket \
    PROJECT_NAME.wsgi:application

[Install]
WantedBy=multi-user.target
```

S3. 重新加载 nginx 配置并开启 gunicorn 服务：

```sh
# 让 Systemd 重新加载 gunicorn 配置文件
server$ sudo systemctl daemon-reload

# 重启 nginx 服务
server$ sudo systemctl reload nginx

# 开启当前网站的 gunicorn 服务
server$ sudo systemctl enable gunicorn-<hostname>
server$ sudo systemctl start gunicorn-<hostname>
```


### 自动更新部署
在本地开发源代码更新，push到Git后：

S1. 本地执行自动部署脚本：

```sh
cd deploy_tools
fab <function_name(deploy)>:host=SERVER_ADDRESS
```
S2. 服务器端重启gunicorn：

```sh
server$ sudo systemctl daemon-reload
server$ sudo systemctl restart gunicorn-<hostname>
```

> 备忘 nginx 和 gunicorn 的日志信息：  
> nginx（网站访问日志）: /var/log/nginx/access.log error.log  
> gunicorn 状态：sudo systemctl status gunicorn\-\<hostname\>  
> gunicorn（网站运行日志）: sudo journalctl -u gunicorn\-\<hostname\>


### 遇到的坑们
#### 重装 Nginx
有些时候服务器上已有的 Nginx 有问题但不清楚之前的配置啊啥的，可以考虑重装 Nginx：
> 这时候一定要彻底删除所有配置文件！有一次没删干净，重装的 Niginx 还保留着之前的配置就很凉，不管怎么改 sites-enabled 下的配置文件都始终显示欢迎界面，后来发现是 /etc/nginx 下的 nginx.conf 直接被人改了。。

```sh
# 首先删除nginx，–purge包括配置文件
$ sudo apt-get --purge remove nginx
# 自动移除全部不使用的软件包
$ sudo apt-get autoremove
# 罗列出与nginx相关的软件
$ dpkg --get-selections|grep nginx
nginx                       install
nginx-common                    install
nginx-core                  install
# 删除以上查询出与nginx有关的软件，一定要删哦，有次没删去nginx-common，配置就保留了。。
$ sudo apt-get --purge remove nginx
$ sudo apt-get --purge remove nginx-common
$ sudo apt-get --purge remove nginx-core

# 查看nginx正在运行的进程，如果有就kill掉
$ ps -ef |grep nginx
root      7875  2317  0 15:02 ?        00:00:00 nginx: master process /usr/sbin/nginx
www-data  7876  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7877  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7878  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7879  7875  0 15:02 ?        00:00:00 nginx: worker process
stephen   8321  3510  0 15:20 pts/0    00:00:00 grep --color=auto nginx
$ sudo kill  -9  7875 7876 7877 7879

# 全局查找与nginx相关的文件并删除
$ sudo  find  /  -name  nginx*
$ sudo rm -rf file

# 可以重装了
$ sudo apt-get update
$ sudo apt-get install nginx
```

#### /etc/nginx/sites-enabled 下的软链接
有时候部署完了之后却被拒绝连接，可以尝试删除 /etc/nginx/sites-enabled 下使用的软链接，直接使用配置文件：

```sh
$ sudo cp /your/path/djangopro_nginx.conf   /etc/nginx/sites-enabled/
```



