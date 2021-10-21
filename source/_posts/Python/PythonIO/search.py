#!usr/bin/env python
#coding = utf-8

import os
import sys
'''
查找当前目录及子目录下文件名含有指定字符串的文件
'''

def search(str):
	match = []		
	pwd = os.path.abspath('.')
	filename = os.listdir('.')
	for name in filename:
		if os.path.isdir(name):
			subname = []
			for x in os.listdir(name):
				subname.append(os.path.join(name,x))
			filename += subname

		elif os.path.isfile(name) and str in os.path.split(name)[1]:
			match.append(name)

	print match




if __name__ == '__main__':
	arg = sys.argv
	if len(arg) != 2:
		raise ValueError('Wrong argument!')
	else:
		search(arg[1])