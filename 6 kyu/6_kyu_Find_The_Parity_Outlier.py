def find_outlier(integers):
	even = [ x for x in integers if x % 2 == 0 ]
	odd = [ x for x in integers if x % 2 == 1 ]
	return even[0] if len(even) == 1 else odd[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


# 大佬鼠
def find_outlier1(integers):
	parity = [n % 2 for n in integers]
	return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier2(integers):
	even = filter(lambda x: x % 2 == 0, integers)
	return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]