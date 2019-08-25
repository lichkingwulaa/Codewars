"""
https://www.codewars.com/kata/are-they-the-same/python
"""
def comp(array1, array2):
	if array1 is None or array2 is None:
		return False
	i = 0
	while True:
		if not array1:
			if not array2:
				return True
			else:
				return False
		elif array1[i]**2 in array2:
			array2.remove(array1[i] ** 2)
			array1.remove(array1[i])
			i = 0
		else:
			return False

a1 = [121, 144, 19, 161,  19, 144, 19, 11 ]
a2 = [11*11, 121*121, 144*144,19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1,a2))


# 大佬鼠的迷惑方法
def comp1(array1, array2):
	try:
		return sorted([i ** 2 for i in array1]) == sorted(array2)
	except:
		return False


# 汪小佬 2019.08.25
def comp(array1, array2):
	return False if None in [array1, array2] else [x ** 2 for x in sorted(array1)] == sorted(array2)


