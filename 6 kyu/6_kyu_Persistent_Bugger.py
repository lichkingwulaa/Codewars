def persistence(n):
	i = 0
	while True:
		if 0 <= n <= 9:
			break
		res = 1
		for x in str(n):
			res *= int(x)
		n = res
		i += 1
	return i

print(persistence(999))