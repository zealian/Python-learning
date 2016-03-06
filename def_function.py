#练习

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解。
#提示：计算平方根可以调用math.sqrt()函数：

# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	delta=b**2 - 4 * a * c
	if a != 0:
		if delta < 0:
			return 'error'
		elif delta == 0:
			x1 = -b / (2 * a)  
			x2 = x1
		else:
			x1 = (-b + math.sqrt(delta)) / (2 * a)
			x2 = (-b - math.sqrt(delta)) / (2 * a)
		return x1, x2
	else:
		return (-c / b)