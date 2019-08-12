def two_oldest_ages(ages):
	a = max(ages)
	ages.remove(a)
	b = max(ages)
	return [b, a]


two_oldest_ages([1, 5, 87, 45, 8, 8])


# 大佬鼠
def two_oldest_ages1(ages):
	return sorted(ages)[-2:]