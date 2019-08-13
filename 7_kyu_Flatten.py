def flatten(lst):   # 只展开一次
	res = []
	for x in lst:
		if type(x) == list: res += x
		else: res.append(x)
	return res

print(flatten([1 ,[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]))


def flatten1(lst):  # 全部展开，变成一维数组
	res = []
	while True:
		if lst == []:
			break
		for x in lst:
			if type(x) == list:
				lst = x + lst[1:]
				break
			else:
				res.append(x)
				lst.pop(0)
				break
	return res
print(flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]))

def flatten(lst):   # 全部展开，变成一维数组
	res = []
	for x in lst:
		if isinstance(x, list):
			res.extend(flatten(x))
		else:
			res.append(x)
	return res
print(flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]))