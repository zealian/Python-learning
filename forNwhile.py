# -*- coding: utf-8 -*-
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L=['Bart','Lisa','Adam']
print('Use \'for\'')
for x in L:
	print('Hello, %s' % x)
print('Use \'while\'')
x=0
while x<len(L):
	print('Hello, %s' % L[x]) 
	x=x+1
