"""
https://www.codewars.com/kata/find-the-next-perfect-square/train/python
"""
def find_next_square(sq):
	return (int(sq ** 0.5) + 1)** 2 if int(sq ** 0.5) ** 2 == sq else -1


# 确定是否是平方数
def is_square(n):
	"""牛顿迭代法确定平方数"""
	x = n*0.01
	while abs(x**2-n)>1:
		x = (x + n/x)/2
	if int(x)**2 == n or (int(x)+1)**2 == n:
		return True
	else:
		return False


# 大佬鼠的迷惑方法
def is_square1(n):
	if n >= 0:
		if int(n ** .5) ** 2 == n:
			return True
	return False


# 大大佬鼠的迷惑方法
def is_square2(n):
	return n>=0 and int(n ** .5) ** 2 == n