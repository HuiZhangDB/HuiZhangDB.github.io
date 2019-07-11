#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
tcp编程测试
'''
import socket

# def client():
# 	#客户端
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.connect(('www.sina.com.cn',80))
# 	s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 	buffer = []
# 	while True:
# 		d = s.recv(1024)
# 		if d:
# 			buffer.append(d)
# 		else:
# 			break
# 	data = ''.join(buffer)

# 	s.close()

# 	header, html = data.split('\r\n\r\n',1)
# 	print header
# 	with open('sina.html','wb') as f:
# 		f.write(html)

def client():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1',9999))
	print s.recv(1024)
	message = ['Hui','Meng','Hu','Xu','exit','test']
	for data in message:
		s.send(data)
		print s.recv(1024)
	s.send('exit')
	s.close()

if __name__ == '__main__':
	client()

