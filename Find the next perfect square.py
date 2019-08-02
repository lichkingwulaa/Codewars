# 确定平方数
from time import process_time

def is_square(n):
	"""牛顿迭代法确定平方数"""
	x = n*0.01
	while abs(x**2-n)>1:
		x = (x + n/x)/2
	if int(x)**2 == n or (int(x)+1)**2 == n:
		return True
	else:
		return False
process_time()
num = input('number:')
print(is_square(int(num)))
print("程序运行时间是:%-5.5ss" % process_time())


# 大佬鼠的迷惑方法
def is_square1(n):
	if n >= 0:
		if int(n ** .5) ** 2 == n:
			return True
	return False


# 大大佬鼠的迷惑方法
def is_square2(n):
	return n>=0 and int(n ** .5) ** 2 == n