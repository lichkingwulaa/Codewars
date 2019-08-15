def top(a1):
	return a1.pop(0) if a1 else []

def right(a2):
	return [x.pop(-1) for x in a2] if a2 else []

def bottom(a3):
	return a3.pop(-1)[::-1] if a3 else []

def left(a4):
	return [x.pop(0) for x in a4][::-1] if a4 else []


def snail(array):
	res = []
	while array:
		res += top(array)
		res += right(array)
		res += bottom(array)
		res += left(array)
	return res


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)


# 大佬鼠
def snail0(array):
	return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

def snail(array):
	a = []
	while array:
		a.extend(list(array.pop(0)))
		array = zip(*array)
		array.reverse()
	return a