# def two_sum(numbers, target):
# 	for i, x in enumerate(numbers):
# 		if target - x in numbers.pop(i):
# 			return [numbers.index(x), numbers.index(target - x)]
#
# print(sorted(two_sum([1,2,3], 4)), [0,2])
# print(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# print(sorted(two_sum([2,2,3], 4)), [0,1])
d = {}
for x in range(1,27):
	d[str(chr(x + 64  + 32))] = x

print(d)