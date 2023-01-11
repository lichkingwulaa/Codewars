def sum_pairs(ints, s):
	while True:
		old_ints = ints[:]
		for x in sorted(list(set(ints)), key=ints.index):
			num = ints[:]
			index1 = num.index(x)
			num.remove(x)
			if s - x in num:
				index2 = num.index(s - x) + 1
				ints = ints[index1:index2 + 1]
				break
		if ints == old_ints:
			break
	if ints and ints[0] + ints[-1] == s:
		old_ints2 = ints[:]
		if ints[0] == ints[-1]:
			ints = sum_pairs(ints[1:-1], s)
		return [ints[0], ints[-1]] if ints else [old_ints2[0], old_ints2[-1]]
l1= [1, 4, 8, 7, 3, 15]
print(sum_pairs(l1, 8) )#== [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)

l2= [1, -2, 3, 0, -6, 1]
print(sum_pairs(l2, -6) )#== [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)

l3= [20, -13, 40]
print(sum_pairs(l3, -7) )#== None, "No Match: %s should return None for sum = -7" % l3)

l4= [1, 2, 3, 4, 1, 0]
print(sum_pairs(l4, 2) )#== [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)

l5= [10, 5, 2, 3, 7, 5]
print(sum_pairs(l5, 10) )#== [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)

l6= [4, -2, 3, 3, 4]
print(sum_pairs(l6, 8) )#== [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)

l7= [0, 2, 0]
print(sum_pairs(l7, 0) )#== [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)

l8= [5, 9, 13, -3]
print(sum_pairs(l8, 10) )#== [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)


# 大佬鼠
def sum_pairs(lst, s):
	cache = set()
	for i in lst:
		if s - i in cache:
			return [s - i, i]
		cache.add(i)