#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
tcp编程测试
'''
import socket
import threading
import time

def server():
	#服务器
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('127.0.0.1',9999))
	s.listen(5)
	print 'Waiting for connection...'

	while True:
		sock, addr = s.accept()
		t = threading.Thread(target = tcplink, args = (sock,addr))
		t.start()

def tcplink(sock,addr):
	print 'Accepting new connnection from %s:%s...' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		# time.sleep(1)
		if data == 'exit' or not data:
			print 'exit or null'
			break
		else:
			print data
			sock.send('Hello, %s' %data)
	sock.close()
	print 'Connection from %s:%s closed' % addr

	


if __name__ == '__main__':
	server()

